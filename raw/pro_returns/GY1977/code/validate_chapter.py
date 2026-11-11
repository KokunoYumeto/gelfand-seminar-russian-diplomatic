"""Strict companion-data checks in addition to the supplied chapter builder."""
from pathlib import Path
from collections import Counter
import csv,json,re,sys

D=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parent.parent
tag='GY1977'
talks=json.loads((D/f'{tag}_talks.json').read_text())
items=json.loads((D/f'{tag}_items.json').read_text())
problems=json.loads((D/f'{tag}_problems.json').read_text())
bib=(D/f'{tag}_references.bib').read_text()
keys=re.findall(r'(?m)^\s*@\w+\s*\{\s*([^,\s]+)\s*,',bib)
errors=[];warnings=[]
def require(test,message):
    if not test:errors.append(message)
expected=list(range(419,437))+list(range(438,446))+[451,457]
require([t['record'] for t in talks]==expected,'Catalogue coverage or source order differs from requested 28 records')
require(len(keys)==len(set(keys)),'Duplicate bibliography keys')
talk_keys={'record','date','speaker','pages','title','kind','summary'}
item_keys={'id','record','pages','kind','title','notes','statement','reconstruction','class','fate','present_status','literal_correctness','publication_match','verification','development','problem','worth','refs','confidence'}
values={'kind':{'definition','construction','theorem','claim','conjecture','question','problem','method','remark'},
        'class':set('ABCDEF'),'literal_correctness':{'correct','correct with missing hypotheses','false as written','not determinable'},
        'publication_match':{'exact','partial','thematic only','none found'},
        'verification':{'read the result','publisher metadata checked','indirect','unresolved lead'},
        'development':{'none','annotated','developed in this chapter'},'confidence':{'high','medium','low'}}
ids={i['id'] for i in items};pids={p['id'] for p in problems}
require(len(ids)==len(items),'Duplicate item IDs')
require(len(pids)==len(problems),'Duplicate problem IDs')
cite_pattern=r'\\cite[pt]?\*?(?:\[[^\]]*\])*\{([^}]+)\}'
for t in talks:
    require(talk_keys<=t.keys(),f'Talk {t["record"]}: missing fields {talk_keys-t.keys()}')
    require(t.get('kind') in {'talk','plan','heading','other'},f'Talk {t["record"]}: invalid kind')
for i in items:
    ident=i['id']
    require(item_keys<=i.keys(),f'{ident}: missing fields {item_keys-i.keys()}')
    require(re.fullmatch(r'1977-'+str(i['record'])+r'\.[1-9][0-9]*',ident),f'{ident}: identifier/cohort mismatch')
    for k,allowed in values.items():require(i.get(k) in allowed,f'{ident}: invalid {k}={i.get(k)}')
    require(i['record'] in expected,f'{ident}: missing record')
    require(not i.get('problem') or i['problem'] in pids,f'{ident}: missing problem target')
    if i['class'] in 'CD':require(bool(i.get('worth')),f'{ident}: class C/D lacks worth assessment')
    require(bool(re.search(r'2026|November',i.get('present_status',''))),f'{ident}: status lacks date')
    local=set()
    for v in i.values():
        if isinstance(v,str):
            require(not any(ord(c)<32 and c!='\n' for c in v),f'{ident}: unexpected control character in text')
            for group in re.findall(cite_pattern,v):local.update(k.strip() for k in group.split(','))
    require(local<=set(i['refs']),f'{ident}: citations missing from refs: {local-set(i["refs"])}')
    require(set(i['refs'])<=set(keys),f'{ident}: absent bibliography references')
    for k in ['notes','statement','fate','present_status']:
        require(bool(i[k].strip()),f'{ident}: empty {k}')
for record in expected:
    group=[i['id'] for i in items if i['record']==record]
    require(group==[f'1977-{record}.{n}' for n in range(1,len(group)+1)],f'{record}: nonconsecutive items')
for p in problems:
    require(p.get('status_date')=='2026-11',f'{p["id"]}: wrong status date')
    for ident in p['occurrences']:
        if ident.startswith('1977-'):
            require(ident in ids,f'{p["id"]}: missing current occurrence {ident}')
            if ident in ids:
                item=next(i for i in items if i['id']==ident)
                require(item.get('problem')==p['id'],f'{p["id"]}: occurrence {ident} does not link back to problem')
    require(set(p['refs'])<=set(keys),f'{p["id"]}: missing references')
    local=set()
    for v in p.values():
        if isinstance(v,str):
            for group in re.findall(cite_pattern,v):local.update(k.strip() for k in group.split(','))
    require(local<=set(p['refs']),f'{p["id"]}: citations missing from refs: {local-set(p["refs"])}')

starts=list(re.finditer(r'(?m)^\s*@\w+\s*\{\s*([^,\s]+)\s*,',bib))
for j,m in enumerate(starts):
    entry=bib[m.start():starts[j+1].start() if j+1<len(starts) else len(bib)]
    key=m.group(1)
    require(bool(re.search(r'\b(?:url|doi)\s*=',entry,re.I)),f'{key}: no URL or DOI')
    require(bool(re.search(r'\bnote\s*=\s*\{(?:verified|unverified)\}',entry,re.I)),f'{key}: no verification note')

with (D/f'{tag}_corrections.csv').open(newline='') as f:corrections=list(csv.DictReader(f))
for c in corrections:
    require(c.get('applies_to') in {'en','ru','both'},f'Correction {c.get("page")}: applies_to invalid')
    require(c.get('type') in {'transcription','translation','ambiguity','faithful_error','provenance',''},f'Correction {c.get("page")}: type invalid')
    require(bool(c.get('evidence')),f'Correction {c.get("page")}: no evidence')

def pages(text):
    out=set()
    for m in re.finditer(r'P(\d{6})(?:\s*[-–]\s*P?(\d{6}))?',text):
        start=int(m.group(1));end=int(m.group(2) or start)
        out.update(range(start,end+1))
    return out
packet=set(range(705,755))|set(range(756,788))|set(range(810,813))|set(range(823,832))
item_pages=set().union(*(pages(i['pages']) for i in items))
talk_pages=set().union(*(pages(t['pages']) for t in talks))
require(item_pages<=packet,f'Items cite pages outside supplied packet: {sorted(item_pages-packet)}')
uncovered=sorted(packet-item_pages)
if uncovered:warnings.append('Source pages without an individual item locator (may be headings/continuations): '+str(uncovered))
fulltext='\n'.join(p.read_text() for p in D.glob('GY1977_*.tex'))+'\n'+json.dumps(items)
require('TODO' not in fulltext and 'PLACEHOLDER' not in fulltext,'Unfinished placeholder text')
result={'result':'PASS' if not errors else 'FAIL','records':len(talks),'items':len(items),'problems':len(problems),
        'references':len(keys),'corrections':len(corrections),'packet_pages':len(packet),
        'pages_with_item_locators':len(item_pages),'uncovered_page_ids':uncovered,'errors':errors,'warnings':warnings}
out=D/'code/output';out.mkdir(parents=True,exist_ok=True)
(out/'data_validation.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
sys.exit(bool(errors))
