"""Read-only aggregate schema, citation and occurrence audit of parts a--d."""
from pathlib import Path
from collections import Counter,defaultdict
import re,json,datetime
ROOT=Path(__file__).resolve().parents[2]
PARTS=ROOT/'parts'
OUT=PARTS/'b'
rx_cite=re.compile(r'\\cite(?:p|t)?\*?(?:\[[^\]]*\])*\{([^}]*)\}')
def cites(obj):
    text=' '.join(str(v) for v in obj.values() if isinstance(v,str)) if isinstance(obj,dict) else str(obj)
    return {k.strip() for grp in rx_cite.findall(text) for k in grp.split(',') if k.strip()}
required_item=['id','record','pages','kind','title','notes','statement','reconstruction','class','fate','present_status','literal_correctness','publication_match','verification','development','problem','worth','refs','confidence']
required_talk=['record','date','speaker','pages','title','kind','summary']
required_problem=['id','title','statement','occurrences','status','status_date','refs']
enums={
 'kind':{'definition','construction','theorem','claim','conjecture','question','problem','method','remark'},
 'class':set('ABCDEF'),
 'literal_correctness':{'correct','correct with missing hypotheses','false as written','not determinable'},
 'publication_match':{'exact','partial','thematic only','none found'},
 'verification':{'read the result','publisher metadata checked','indirect','unresolved lead'},
 'development':{'none','annotated','developed in this chapter'},
 'confidence':{'high','medium','low'}}
issues=[];extras=[];stats={};data={};allitems={};alltalks={};allproblems=defaultdict(list);allbib=defaultdict(list)
def issue(severity,location,message):issues.append({'severity':severity,'location':location,'message':message})
for name in 'abcd':
    p=PARTS/name
    obj={k:json.loads((p/(k+'.json')).read_text()) for k in ['talks','items','problems']}
    bib=(p/'references.bib').read_text();keys=re.findall(r'@\w+\s*\{\s*([^,\s]+)\s*,',bib);keyset=set(keys)
    for k,n in Counter(keys).items():
        if n>1:issue('warning',name+'/references.bib',f'bibliography key {k} occurs {n} times')
    for k in keyset:allbib[k].append(name)
    for t in obj['talks']:
        loc=f'{name}:record {t.get("record")}'
        for key in required_talk:
            if key not in t:issue('error',loc,'missing talk field '+key)
        if t.get('kind') not in {'talk','plan','heading','other'}:issue('error',loc,'invalid talk kind')
        if t['record'] in alltalks:issue('error',loc,'duplicate record across parts')
        alltalks[t['record']]=t
        for key in cites(t)-keyset:issue('error',loc,'talk citation has no local bibliography entry: '+key)
    for x in obj['items']:
        loc=f'{name}:{x.get("id")}'
        for key in required_item:
            if key not in x:issue('error',loc,'missing item field '+key)
        for field,allowed in enums.items():
            if x.get(field) not in allowed:issue('error',loc,'invalid '+field+': '+repr(x.get(field)))
        if not re.fullmatch(r'1981-\d+\.\d+',x.get('id','')):issue('error',loc,'wrong academic-year item identifier')
        elif int(x['id'].split('-')[1].split('.')[0])!=x['record']:issue('error',loc,'record disagrees with identifier')
        if x['id'] in allitems:issue('error',loc,'duplicate item identifier')
        allitems[x['id']]=x
        if x.get('record') not in {t['record'] for t in obj['talks']}:issue('error',loc,'no local talk entry')
        if x.get('class') in 'CD' and not x.get('worth'):issue('error',loc,'C/D has no worth statement')
        if not isinstance(x.get('refs'),list) or not all(isinstance(k,str) for k in x.get('refs',[])):issue('error',loc,'refs is not a string list')
        declared=set(x.get('refs',[]));inline=cites(x)
        for key in declared-keyset:issue('error',loc,'declared reference has no local bibliography entry: '+key)
        for key in inline-declared:issue('error',loc,'inline citation is absent from item refs: '+key)
        for key in inline-keyset:issue('error',loc,'inline citation has no local bibliography entry: '+key)
        if declared-inline:extras.append({'location':loc,'extra_refs':sorted(declared-inline),'kind':'item'})
        if not x.get('area'):issue('warning',loc,'area field absent or empty')
    byrec=defaultdict(list)
    for x in obj['items']:byrec[x['record']].append(x['id'])
    for rec,ids in byrec.items():
        expected=[f'1981-{rec}.{j}' for j in range(1,len(ids)+1)]
        if ids!=expected:issue('error',f'{name}:record {rec}','item numbering/order is not consecutive')
    for pr in obj['problems']:
        loc=f'{name}:{pr.get("id")}'
        for key in required_problem:
            if key not in pr:issue('error',loc,'missing problem field '+key)
        allproblems[pr['id']].append((name,pr))
        declared=set(pr.get('refs',[]));inline=cites(pr)
        for key in inline-declared:issue('error',loc,'inline citation is absent from problem refs: '+key)
        for key in (declared|inline)-keyset:issue('error',loc,'problem reference has no local bibliography entry: '+key)
        if declared-inline:extras.append({'location':loc,'extra_refs':sorted(declared-inline),'kind':'problem'})
        if len(pr.get('occurrences',[]))!=len(set(pr.get('occurrences',[]))):issue('warning',loc,'duplicate occurrence identifiers')
    for fn in ['development.tex','overview.tex']:
        fp=p/fn
        if fp.exists():
            for key in cites(fp.read_text())-keyset:issue('error',name+'/'+fn,'citation has no local bibliography entry: '+key)
    stats[name]={'talks':len(obj['talks']),'items':len(obj['items']),'problems':len(obj['problems']),'bibliography_keys':len(keyset),'classes':dict(Counter(x['class'] for x in obj['items']))}
    data[name]=obj
previous=(ROOT/'previous_index.md').read_text()
previous_ids=set(re.findall(r'\b\d{4}-\d+\.\d+\b',previous))
previous_gp=set(re.findall(r'\bGP-\d{4}-\d+\b',previous))
for pid,entries in allproblems.items():
    if len(entries)>1:issue('merge note',pid,'problem appears in multiple parts: '+', '.join(n for n,p in entries)+'; union occurrences and references during merge')
    for name,pr in entries:
        for occurrence in pr['occurrences']:
            if occurrence.startswith('1981-'):
                if occurrence not in allitems:issue('error',f'{name}:{pid}','current-year occurrence does not exist: '+occurrence)
                elif allitems[occurrence].get('problem') not in {'',pid}:issue('warning',f'{name}:{pid}',f'occurrence {occurrence} points to a different problem '+allitems[occurrence]['problem'])
            elif occurrence not in previous_ids:issue('warning',f'{name}:{pid}','earlier occurrence not located in supplied previous index: '+occurrence)
for iid,x in allitems.items():
    pid=x.get('problem')
    if pid:
        if pid not in allproblems:issue('error',iid,'item points to absent problem '+pid)
        elif not any(iid in p['occurrences'] for name,p in allproblems[pid]):issue('error',iid,'item is absent from occurrence list of its problem '+pid)
if set(alltalks)!=set(range(530,560)):
    issue('error','aggregate talks','record set differs from 530--559: missing='+str(sorted(set(range(530,560))-set(alltalks)))+' extra='+str(sorted(set(alltalks)-set(range(530,560)))))
report={'timestamp_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'parts':stats,'counts':{'talks':len(alltalks),'items':len(allitems),'problem_ids':len(allproblems),'unique_bibliography_keys':len(allbib),'errors':sum(x['severity']=='error' for x in issues),'warnings':sum(x['severity']=='warning' for x in issues)},'issues':issues,'declared_refs_without_inline_citation':extras,'shared_bibliography_keys':{k:v for k,v in allbib.items() if len(v)>1}}
(OUT/'aggregate_data_audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
lines=['# Aggregate data audit: parts a–d','',f"Snapshot: {report['timestamp_utc']}. Read-only audit; no other part was edited.",'','## Scope and result','',f"Checked {len(alltalks)} talks, {len(allitems)} mathematical items, {len(allproblems)} distinct problem IDs and {len(allbib)} distinct bibliography keys. Found **{report['counts']['errors']} errors** and **{report['counts']['warnings']} warnings** under the checks below.",'','| Part | Talks | Items | Problem entries | Bibliography keys | Classes |','|---|---:|---:|---:|---:|---|']
for n,v in stats.items():lines.append(f"| {n} | {v['talks']} | {v['items']} | {v['problems']} | {v['bibliography_keys']} | "+', '.join(f'{k}={q}' for k,q in sorted(v['classes'].items()))+' |')
lines+=['','The script checks required fields and enums; academic-year IDs and per-record consecutive numbering; complete record coverage 530–559; inline citations against each item/problem reference list and local bibliography; citations in talk summaries and development/overview TeX; item-to-problem links; current-year occurrence targets; earlier occurrences against the supplied previous index; C/D worth statements; and area coverage. Bibliographic identities, proofs and source sufficiency remain substantive checks rather than schema properties.','','## Errors, warnings and merge notes','']
if not issues:lines.append('None.')
for x in issues:lines.append(f"- **{x['severity']} — {x['location']}**: {x['message']}")
lines+=['','## Declared references without an inline citation command','','These are review notes, not automatic errors. A reference list can supply structured evidence while the prose names a work without using `\\citet`/`\\citep`. If strict command/list equality is desired, the parent can add appropriate inline citations or remove unused declarations.']
for x in extras:lines.append(f"- {x['location']} ({x['kind']}): "+', '.join(x['extra_refs']))
lines+=['','## Shared bibliography keys','','The following keys occur in multiple part bibliographies. The parent is handling identity-preserving deduplication; this audit does not merge or rewrite them.','']
for k,v in sorted(report['shared_bibliography_keys'].items()):lines.append('- '+k+': '+', '.join(v))
lines+=['','## Substantive spectral-cut check','','Pending a short comparison with the already cited primary sources; no broad new search was performed.','']
(OUT/'aggregate_data_audit.md').write_text('\n'.join(lines))
print(json.dumps(report['counts']))
for x in issues:print(json.dumps(x,ensure_ascii=False))
