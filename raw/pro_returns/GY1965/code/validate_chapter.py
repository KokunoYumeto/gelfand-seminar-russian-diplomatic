#!/usr/bin/env python3
"""Additional semantic and provenance checks beyond the supplied builder.

Usage: python code/validate_chapter.py [chapter-directory]
No claim of automated mathematical verification is made by these checks.
"""
import collections
import csv
import json
from pathlib import Path
import re
import sys

base = Path(sys.argv[1]) if len(sys.argv)>1 else Path('.')
tag = 'GY1965'
talks,items,problems = [json.loads((base/f'{tag}_{k}.json').read_text())
                        for k in ['talks','items','problems']]
bib = (base/f'{tag}_references.bib').read_text()
errors,warnings=[],[]

def require(condition, message):
    if not condition: errors.append(message)

def citations(text):
    groups=re.findall(r'\\cite[pt]?\*?(?:\[[^\]]*\])*\{([^}]*)\}',text)
    return {k.strip() for group in groups for k in group.split(',')}

bib_matches=list(re.finditer(r'(?m)^@\w+\s*\{\s*([^,\s]+)\s*,',bib))
bibkeys=[m.group(1) for m in bib_matches]
require(len(bibkeys)==len(set(bibkeys)),'Duplicate bibliography keys')
for i,m in enumerate(bib_matches):
    entry=bib[m.start():bib_matches[i+1].start() if i+1<len(bib_matches) else len(bib)]
    require(bool(re.search(r'(?i)\b(?:doi|url)\s*=',entry)),f'{m.group(1)} lacks DOI/URL')
    require(bool(re.search(r'(?i)\bnote\s*=\s*\{(?:un)?verified\}',entry)),
            f'{m.group(1)} lacks required verification note')
ids={x['id'] for x in items}
problem_by_id={p['id']:p for p in problems}
record_by_id={t['record']:t for t in talks}
require(len(talks)==37 and set(record_by_id)==set(range(53,90)), 'Incomplete record coverage')
require(len(ids)==len(items),'Duplicate occurrence IDs')
require(len(problem_by_id)==len(problems),'Duplicate problem IDs')
require([p['id'] for p in problems]==[f'GP-1965-{i:02}' for i in range(1,len(problems)+1)],
        'Problem IDs not consecutive in source order')
enums = {
 'kind':{'definition','construction','theorem','claim','conjecture','question','problem','method','remark'},
 'class':set('ABCDEF'),
 'literal_correctness':{'correct','correct with missing hypotheses','false as written','not determinable'},
 'publication_match':{'exact','partial','thematic only','none found'},
 'verification':{'read the result','publisher metadata checked','indirect','unresolved lead'},
 'development':{'none','annotated','developed in this chapter'},
 'confidence':{'high','medium','low'}}
per_record=collections.defaultdict(list)
for x in items:
    per_record[x['record']].append(x)
    for k,values in enums.items():
        require(x.get(k) in values,f"{x['id']}: invalid {k} {x.get(k)!r}")
    for k in ['pages','title','notes','statement','fate','present_status']:
        require(bool(x.get(k)),f"{x['id']}: empty {k}")
    require('reconstruction' in x,f"{x['id']}: reconstruction field absent")
    for field,value in x.items():
        if isinstance(value,str):
            require(not any(ord(c)<32 and c not in '\n\r' for c in value),
                    f"{x['id']}: decoded control character in {field}")
    require('2026' in x['present_status'],f"{x['id']}: undated status")
    require(x['record'] in record_by_id,f"{x['id']}: absent record")
    require(re.fullmatch(rf"1965-{x['record']}\.\d+",x['id']) is not None,
            f"{x['id']}: malformed ID or wrong academic year")
    require(set(x['refs'])<=set(bibkeys),f"{x['id']}: unknown reference key")
    cited=citations(' '.join(v for v in x.values() if isinstance(v,str)))
    require(cited<=set(x['refs']),f"{x['id']}: cited keys absent from refs: {cited-set(x['refs'])}")
    if x['class'] in ['C','D']:
        require(bool(x.get('worth')),f"{x['id']}: missing C/D assessment")
    if x.get('problem'):
        require(x['problem'] in problem_by_id,f"{x['id']}: absent problem")
        if x['problem'] in problem_by_id:
            require(x['id'] in problem_by_id[x['problem']]['occurrences'],
                    f"{x['id']}: problem does not link back")
    if x['kind'] in ['question','problem','conjecture'] and x['class']!='F' and not x.get('problem'):
        warnings.append(f"{x['id']}: definite question without problem link; review manually")
for record,group in per_record.items():
    require([x['id'] for x in group]==[f'1965-{record}.{i}' for i in range(1,len(group)+1)],
            f'Record {record}: nonconsecutive items')
for p in problems:
    require(p['status_date']=='2026-11',f"{p['id']}: wrong status date")
    require(set(p['refs'])<=set(bibkeys),f"{p['id']}: unknown reference")
    require(citations(p['statement']+' '+p['status'])<=set(p['refs']),
            f"{p['id']}: cited keys absent from refs")
    for o in p['occurrences']:
        if o.startswith('1965-'):
            require(o in ids,f"{p['id']}: unknown current occurrence {o}")
            if o in ids:
                x=next(x for x in items if x['id']==o)
                require(x.get('problem')==p['id'],f"{p['id']}: {o} does not link back")
        else:
            require(o.startswith('1964-'),f"{p['id']}: unexpected earlier-year reference {o}")
for name in ['overview.tex','development.tex']:
    text=(base/f'{tag}_{name}').read_text()
    require(citations(text)<=set(bibkeys),f'{name}: unknown citation')
all_text_files = [base/f'{tag}_{x}' for x in ['talks.json','items.json','problems.json',
                  'overview.tex','development.tex','corrections.csv','references.bib']]
for path in all_text_files:
    text=path.read_text()
    require(not any(ord(c)<32 and c not in '\n\r\t' for c in text),
            f'{path.name}: nonprinting control character')
    require(not re.search(r'\bTODO\b|\bTBD\b|PLACEHOLDER',text),f'{path.name}: unresolved placeholder')
with (base/f'{tag}_corrections.csv').open(newline='') as stream:
    for i,row in enumerate(csv.DictReader(stream),1):
        require(row['applies_to'] in ['ru','en','both'],f'Correction {i}: invalid language')
        require(all(row.values()),f'Correction {i}: blank required cell')
        require(citations(' '.join(row.values()))<=set(bibkeys),f'Correction {i}: unknown citation')
print('Record, item, problem, bibliography, citation, enum and control-character audit')
print(f'{len(talks)} records; {len(items)} occurrences; {len(problems)} problems; {len(bibkeys)} references')
for w in warnings: print('REVIEW:',w)
for e in errors: print('ERROR:',e)
print(f'Errors: {len(errors)}; review notices: {len(warnings)}')
sys.exit(bool(errors))
