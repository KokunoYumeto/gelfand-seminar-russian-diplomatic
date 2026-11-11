"""Independent structural and cross-reference audit, additional to supplied builder."""
from pathlib import Path
import collections, csv, json, re, sys

ROOT=Path(__file__).resolve().parents[1]
T=json.loads((ROOT/'GY1967_talks.json').read_text())
I=json.loads((ROOT/'GY1967_items.json').read_text())
P=json.loads((ROOT/'GY1967_problems.json').read_text())
with (ROOT/'GY1967_corrections.csv').open(newline='') as f: C=list(csv.DictReader(f))
B=(ROOT/'GY1967_references.bib').read_text()
BK=set(re.findall(r'@\w+\s*\{\s*([^,\s]+)',B))
errors=[]
def require(ok,message):
    if not ok: errors.append(message)
def cites(text):
    return {k.strip() for g in re.findall(r'\\cite[pt]?\*?(?:\[[^\]]*\])*\{([^}]*)\}',text) for k in g.split(',')}
def allstrings(x):
    if isinstance(x,str): yield x
    elif isinstance(x,dict):
        for v in x.values(): yield from allstrings(v)
    elif isinstance(x,list):
        for v in x: yield from allstrings(v)

require(len(T)==43,'Expected exactly 43 catalogue records')
require({x['record'] for x in T}==set(range(131,174)),'Records 131–173 are not covered exactly')
require(len({x['record'] for x in T})==len(T),'Duplicate records')
ids={x['id'] for x in I}; recs={x['record']:x for x in T}; probs={p['id']:p for p in P}
require(len(ids)==len(I),'Duplicate item IDs')
require(len(probs)==len(P),'Duplicate problem IDs')
required={'id','record','pages','kind','title','notes','statement','reconstruction','class','fate','present_status',
          'literal_correctness','publication_match','verification','development','problem','worth','refs','confidence'}
enums={'kind':{'definition','construction','theorem','claim','conjecture','question','problem','method','remark'},
       'class':set('ABCDEF'),
       'literal_correctness':{'correct','correct with missing hypotheses','false as written','not determinable'},
       'publication_match':{'exact','partial','thematic only','none found'},
       'verification':{'read the result','publisher metadata checked','indirect','unresolved lead'},
       'development':{'none','annotated','developed in this chapter'},
       'confidence':{'high','medium','low'}}
for t in T:
    require(t.get('kind') in {'talk','plan','heading','other'},f"record {t['record']}: bad kind")
    group=[x for x in I if x['record']==t['record']]
    year=1967 if t['record']<=147 else 1968
    require([x['id'] for x in group]==[f"{year}-{t['record']}.{n}" for n in range(1,len(group)+1)],f"record {t['record']}: nonsequential/wrong-year IDs")
for x in I:
    k=x['id']
    require(required<=set(x),f'{k}: missing fields {required-set(x)}')
    require(x['record'] in recs,f'{k}: no record')
    for field,allowed in enums.items(): require(x.get(field) in allowed,f'{k}: invalid {field}={x.get(field)}')
    require('November 2026' in x['present_status'] or '2026-11' in x['present_status'],f'{k}: undated status')
    require(x['class'] not in 'CD' or bool(x['worth']),f'{k}: C/D without worth statement')
    require(set(x['refs'])<=BK,f"{k}: absent bibliography keys {set(x['refs'])-BK}")
    cc=cites('\n'.join(allstrings({a:v for a,v in x.items() if a!='refs'})))
    require(cc<=set(x['refs']),f"{k}: cited keys omitted from refs {cc-set(x['refs'])}")
    pages=[int(n) for n in re.findall(r'P(\d+)',x['pages'])]
    require(pages and all(208<=n<=282 for n in pages),f'{k}: out-of-scope item source page')
    if x['problem']:
        require(x['problem'] in probs,f'{k}: absent problem')
        if x['problem'] in probs: require(k in probs[x['problem']]['occurrences'],f'{k}: nonreciprocal problem link')
for p in P:
    require(p['status_date']=='2026-11',f"{p['id']}: wrong status date")
    require(set(p['refs'])<=BK,f"{p['id']}: missing bibliography keys")
    require(cites(p['statement']+p['status'])<=set(p['refs']),f"{p['id']}: cite missing from refs")
    for occurrence in p['occurrences']:
        if occurrence.startswith(('1967-','1968-')):
            require(occurrence in ids,f"{p['id']}: absent current occurrence {occurrence}")
            if occurrence in ids:
                x=next(x for x in I if x['id']==occurrence)
                require(x['problem']==p['id'],f"{p['id']}: occurrence {occurrence} has nonreciprocal link")
for value in allstrings([T,I,P,C]):
    bad=[ord(ch) for ch in value if ord(ch)<32 and ch not in '\n\r']
    require(not bad,f'Control characters in data {bad}: {value[:100]!r}')
for group in [T,I,P,C]:
    for row in group:
        require(cites('\n'.join(allstrings(row)))<=BK,f"missing citation key: {row.get('id',row.get('record',row.get('page')))}")
for m in re.finditer(r'(?ms)^@\w+\s*\{\s*([^,\s]+)\s*,.*?(?=^@|\Z)',B):
    entry=m[0];key=m[1]
    require(bool(re.search(r'\b(?:doi|url)\s*=',entry,re.I)),f'{key}: no DOI/URL')
    require(bool(re.search(r'\bnote\s*=\s*\{(?:verified|unverified)\}',entry,re.I)),f'{key}: no explicit verification note')

result={'status':'PASS' if not errors else 'FAIL','records':len(T),'items':len(I),'problems':len(P),
        'references':len(BK),'corrections':len(C),
        'classes':dict(sorted(collections.Counter(x['class'] for x in I).items())),
        'literal_correctness':dict(collections.Counter(x['literal_correctness'] for x in I)),
        'verification_levels':dict(collections.Counter(x['verification'] for x in I)),
        'talk_kinds':dict(collections.Counter(t['kind'] for t in T)),
        'empty_records':[t['record'] for t in T if not any(i['record']==t['record'] for i in I)],
        'errors':errors}
(ROOT/'audit/dataset_validation.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
sys.exit(bool(errors))
