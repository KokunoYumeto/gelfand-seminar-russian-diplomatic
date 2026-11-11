from pathlib import Path
import json,re,csv
from collections import Counter
w=Path('work')
items=json.loads((w/'late_items.json').read_text())
talks=json.loads((w/'late_talks.json').read_text())
problems=json.loads((w/'late_problems.json').read_text())
bib=(w/'late_references.bib').read_text()
keys=re.findall(r'(?m)^@\w+\{([^,]+),',bib)
required=set('id record pages kind title notes statement reconstruction class fate present_status literal_correctness publication_match verification development problem worth refs confidence'.split())
errors=[];ids=set()
for it in items:
    if required-set(it):errors.append([it['id'],'missingfields',sorted(required-set(it))])
    if it['id'] in ids:errors.append([it['id'],'duplicateID'])
    ids.add(it['id'])
    if it['class'] in 'CD' and not it['worth']:errors.append([it['id'],'missingworth'])
    if not it['present_status'].startswith('As of November 2026:'):errors.append([it['id'],'statusdate'])
    for ref in it['refs']:
        if ref not in keys:errors.append([it['id'],'missingbib',ref])
    for f in ['notes','statement','reconstruction','fate','present_status']:
        value=it[f]
        if re.search(r'\\(?:SourcePage|SourceFigure|Unclear|Incomplete|Needspace)\b',value):errors.append([it['id'],'transcriptionmacro',f])
        clean=re.sub(r'\\[{}]','',value)
        if clean.count('{')!=clean.count('}'):errors.append([it['id'],'braces',f])
        if value.count(r'\(')!=value.count(r'\)') or value.count(r'\[')!=value.count(r'\]'):errors.append([it['id'],'mathdelimiters',f])
for t in talks:
    nums=[int(i['id'].split('.')[-1]) for i in items if i['record']==t['record']]
    if nums!=list(range(1,len(nums)+1)):errors.append([t['record'],'numbering'])
for pr in problems:
    for ref in pr['refs']:
        if ref not in keys:errors.append([pr['id'],'missingbib',ref])
    for occ in pr['occurrences']:
        if occ.startswith('1976-4') and occ not in ids and not occ.startswith('1976-410.'):
            errors.append([pr['id'],'missinglocaloccurrence',occ])
for it in items:
    if it['problem'] and it['problem'] not in {p['id'] for p in problems}:errors.append([it['id'],'missingproblem'])
meta=json.loads((w/'late_meta.json').read_text())
if set(meta['areas'])!=ids:errors.append(['area_map_mismatch'])
if len(keys)!=len(set(keys)):errors.append(['duplicatebibkeys'])
corr=list(csv.DictReader((w/'late_corrections.csv').open()))
result={'errors':errors,'talks':len(talks),'items':len(items),'by_class':dict(Counter(i['class'] for i in items)),'problems':len(problems),'references':len(keys),'corrections':len(corr),'source_order':[t['record'] for t in talks]}
print(json.dumps(result,indent=2))
raise SystemExit(bool(errors))
