"""Structural and textual QA for the autumn contribution; no theorem is proved by this script."""
import csv,json,re
from collections import Counter
from pathlib import Path
P=Path(__file__).resolve().parent
items=json.loads((P/'items.json').read_text())
talks=json.loads((P/'talks.json').read_text())
problems=json.loads((P/'problems.json').read_text())
bib=(P/'references.bib').read_text()
corrections=list(csv.DictReader((P/'corrections.csv').open()))
errors=[]
required={'id','record','pages','kind','title','notes','statement','reconstruction','class','fate','present_status','literal_correctness','publication_match','verification','development','problem','worth','refs','confidence'}
enums={
 'kind':{'definition','construction','theorem','claim','conjecture','question','problem','method','remark'},
 'class':set('ABCDEF'),
 'literal_correctness':{'correct','correct with missing hypotheses','false as written','not determinable'},
 'publication_match':{'exact','partial','thematic only','none found'},
 'verification':{'read the result','publisher metadata checked','indirect','unresolved lead'},
 'development':{'none','annotated','developed in this chapter'},
 'confidence':{'high','medium','low'},
}
ids={x['id'] for x in items}
if len(ids)!=len(items): errors.append('Duplicate item IDs')
bibkeys=re.findall(r'@\w+\{([^,]+),',bib)
if len(bibkeys)!=len(set(bibkeys)): errors.append('Duplicate bibliography keys')
allrefs=set()
for x in items:
    missing=required-set(x)
    if missing: errors.append(f"{x['id']}: missing {sorted(missing)}")
    for k,options in enums.items():
        if x[k] not in options: errors.append(f"{x['id']}: invalid {k}={x[k]}")
    if x['class'] in {'C','D'} and not x['worth']: errors.append(f"{x['id']}: missing worth")
    if not x['present_status'].startswith('As of November 2026:'): errors.append(f"{x['id']}: undated status")
    allrefs.update(x['refs'])
    cited=set()
    for k,v in x.items():
        if not isinstance(v,str): continue
        if re.search(r'[\x00-\x08\x0b\x0c\x0e-\x1f]',v): errors.append(f"{x['id']} {k}: control character")
        if v.count(r'\(')!=v.count(r'\)') or v.count(r'\[')!=v.count(r'\]'): errors.append(f"{x['id']} {k}: math delimiters")
        for c in re.findall(r'\\cite\w*(?:\[[^\]]*\])?\{([^}]+)\}',v): cited.update(c.split(','))
    if cited-set(x['refs']): errors.append(f"{x['id']}: cited keys absent from refs {cited-set(x['refs'])}")
    for k in ['id','pages','title','kind']:
        if '\\' in x[k]: errors.append(f"{x['id']} {k}: LaTeX in plain field")
for r in range(2,15):
    ns=[int(x['id'].split('.')[1]) for x in items if x['record']==r]
    if ns!=list(range(1,len(ns)+1)): errors.append(f'Record {r}: nonconsecutive IDs {ns}')
for x in problems:
    allrefs.update(x['refs'])
    if x['status_date']!='2026-11': errors.append(f"{x['id']}: wrong status date")
    if set(x['occurrences'])-ids: errors.append(f"{x['id']}: missing occurrences")
if allrefs-set(bibkeys): errors.append(f'Missing bibliography keys: {sorted(allrefs-set(bibkeys))}')
for key,body in re.findall(r'@\w+\{([^,]+),(.*?)(?=\n@\w+\{|\Z)',bib,re.S):
    if not re.search(r'\b(?:url|doi)\s*=',body): errors.append(f'{key}: missing URL/DOI')
    if 'note = {verified}' not in body: errors.append(f'{key}: missing verification note')
    if 'annote =' not in body: errors.append(f'{key}: missing access scope')
for x in corrections:
    if x['applies_to'] not in {'ru','en','both'}: errors.append('Invalid correction language')
    if x['type'] not in {'transcription','translation','ambiguity','faithful_error','provenance',''}: errors.append('Invalid correction type')
print(f'Talks: {len(talks)}; records: {[x["record"] for x in talks]}')
print(f'Items: {len(items)}')
print('Items by record:',dict(sorted(Counter(x['record'] for x in items).items())))
print('Class counts:',dict(sorted(Counter(x['class'] for x in items).items())))
print('Literal-correctness counts:',dict(sorted(Counter(x['literal_correctness'] for x in items).items())))
print('Verification counts:',dict(sorted(Counter(x['verification'] for x in items).items())))
print(f'Problems: {len(problems)}; IDs: {[x["id"] for x in problems]}')
print(f'References used: {len(allrefs)}; bibliography entries: {len(bibkeys)}')
print('Unused bibliography entries:',sorted(set(bibkeys)-allrefs))
print(f'Corrections: {len(corrections)}; types:',dict(sorted(Counter(x['type'] for x in corrections).items())))
print('C/D items:',[(x['id'],x['worth']) for x in items if x['class'] in {'C','D'}])
print('F identifications:',[(x['id'],x['title']) for x in items if x['class']=='F'])
print('Bibliography keys:',', '.join(sorted(bibkeys)))
print('Errors:',len(errors))
for e in errors: print('ERROR:',e)
if errors: raise SystemExit(1)
