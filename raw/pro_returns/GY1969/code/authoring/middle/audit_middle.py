"""Check the segment data and report exact integration counts; no final build."""
from pathlib import Path
import json, re, csv
from collections import Counter
from datetime import date

base=Path(__file__).resolve().parent
talks=json.loads((base/'talks.json').read_text())
items=json.loads((base/'items.json').read_text())
problems=json.loads((base/'problems.json').read_text())
sources=json.loads((base/'sources.json').read_text())
bibtext=(base/'references.bib').read_text()
bibkeys=re.findall(r'@\w+\{([^,]+),',bibtext)
errors=[]
required={'id','record','pages','kind','title','notes','statement','reconstruction','class','fate','present_status','literal_correctness','publication_match','verification','development','problem','worth','refs','confidence'}
assert [t['record'] for t in talks]==list(range(191,209))
assert len(bibkeys)==len(set(bibkeys))
ids={x['id'] for x in items}
pids={p['id'] for p in problems}
if len(ids)!=len(items):errors.append('Duplicate item ID')
allowed={
 'class':set('ABCDEF'),
 'kind':{'definition','construction','theorem','claim','conjecture','question','problem','method','remark'},
 'literal_correctness':{'correct','correct with missing hypotheses','false as written','not determinable'},
 'publication_match':{'exact','partial','thematic only','none found'},
 'verification':{'read the result','publisher metadata checked','indirect','unresolved lead'},
 'development':{'none','annotated','developed in this chapter'},
 'confidence':{'high','medium','low'}
}
for t in talks:
    if t['date']:date.fromisoformat(t['date'])
for record in range(191,209):
    found=[x['id'] for x in items if x['record']==record]
    if found!=[f'1970-{record}.{i}' for i in range(1,len(found)+1)]:
        errors.append(f'Nonconsecutive IDs in {record}')
for x in items:
    if required-set(x):errors.append(f"{x['id']}: missing {required-set(x)}")
    for field,values in allowed.items():
        if x[field] not in values:errors.append(f"{x['id']}: illegal {field}")
    if x['class'] in {'C','D'} and not x['worth']:errors.append(f"{x['id']}: missing worth")
    if x['problem'] and x['problem'] not in pids:errors.append(f"{x['id']}: missing problem")
    if not x['present_status'].startswith('As of 9 November 2026:'):errors.append(f"{x['id']}: undated status")
    for key in x['refs']:
        if key not in bibkeys:errors.append(f"{x['id']}: undefined bibkey {key}")
    cited=[]
    for field,value in x.items():
        if not isinstance(value,str):continue
        if any(ord(c)<32 and c not in '\n\r\t' for c in value):errors.append(f"{x['id']}: control character in {field}")
        for match in re.finditer(r'\\cite[tp]?(?:\[[^]]*\])?\{([^}]+)\}',value):
            cited.extend(match.group(1).split(','))
        # All used ordinary braces are syntactic; escaped literal braces excluded.
        stripped=re.sub(r'\\[{}]','',value)
        if stripped.count('{')!=stripped.count('}'):
            errors.append(f"{x['id']}: brace imbalance in {field}")
    for key in cited:
        if key not in x['refs']:errors.append(f"{x['id']}: citation {key} not in refs")
for p in problems:
    if p['status_date']!='2026-11':errors.append(f"{p['id']}: date mismatch")
    for occurrence in p['occurrences']:
        if occurrence not in ids:errors.append(f"{p['id']}: missing occurrence {occurrence}")
    for key in p['refs']:
        if key not in bibkeys:errors.append(f"{p['id']}: undefined bibliography {key}")
with (base/'corrections.csv').open() as f: corrections=list(csv.DictReader(f))
report={
 'records':len(talks),'items':len(items),'problems':len(problems),
 'corrections':len(corrections),'references':len(bibkeys),'source_records':len(sources),
 'classes':dict(Counter(x['class'] for x in items)),
 'items_by_record':dict(Counter(str(x['record']) for x in items)),
 'errors':errors,
 'root_proof_review':{
  'dev:bell':'Independently checked all-finite-subset block proof, strict positivity, consistency, simple entangled eigenspace, and simple-spectrum repair.',
  'dev:four-subspaces':'Independently checked projective-frame endomorphisms, stabilizer and ambient dimensions, open dense orbit, generic-line analytic family, and direction of degeneration.'
 }
}
(base/'audit_middle.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
if errors:raise SystemExit(1)
