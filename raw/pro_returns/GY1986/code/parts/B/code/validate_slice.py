"""Validate the local data schema and source-key/link invariants before merging."""
from pathlib import Path
import collections
import csv
import json
import re

B = Path(__file__).resolve().parents[1]
talks = json.loads((B/'talks.json').read_text())
items = json.loads((B/'items.json').read_text())
problems = json.loads((B/'problems.json').read_text())
bib = (B/'references.bib').read_text()
keys = re.findall(r'@\w+\s*\{\s*([^,\s]+)\s*,', bib)
errors = []
def require(ok, message):
    if not ok:
        errors.append(message)
require([x['record'] for x in talks] == list(range(682,698)), 'Talk order/coverage')
require(len(keys) == len(set(keys)), 'Duplicate bibliography keys')
require(len({x['id'] for x in items}) == len(items), 'Duplicate occurrence IDs')
itemids = {x['id'] for x in items}
problemids = {x['id'] for x in problems}
required = {'id','record','pages','kind','title','notes','statement',
            'reconstruction','class','fate','present_status','literal_correctness',
            'publication_match','verification','development','problem','worth',
            'refs','confidence'}
allowed = {
    'class': set('ABCDEF'),
    'kind': {'definition','construction','theorem','claim','conjecture','question','problem','method','remark'},
    'literal_correctness': {'correct','correct with missing hypotheses','false as written','not determinable'},
    'publication_match': {'exact','partial','thematic only','none found'},
    'verification': {'read the result','publisher metadata checked','indirect','unresolved lead'},
    'development': {'none','annotated','developed in this chapter'},
    'confidence': {'high','medium','low'},
}
for record in range(682,698):
    selected = [x for x in items if x['record']==record]
    require([x['id'] for x in selected] == [
        f'1986-{record}.{n}' for n in range(1,len(selected)+1)],
        f'Nonconsecutive occurrences: {record}')
for item in items:
    label=item['id']
    require(required <= item.keys(), f'Missing fields: {label}')
    for field, options in allowed.items():
        require(item[field] in options, f'Invalid {field}: {label}')
    if item['class'] in 'CD':
        require(bool(item['worth']), f'Missing worth: {label}')
    require(item['problem'] in problemids|{'','GP-1986-60'}, f'Unknown problem: {label}')
    require(set(item['refs']) <= set(keys), f'Missing reference: {label}')
    for field in ('notes','statement','reconstruction','fate','present_status','worth'):
        value=item[field]
        require(value.count(r'\(')==value.count(r'\)'), f'Math delimiter mismatch: {label}/{field}')
        require(value.count(r'\[')==value.count(r'\]'), f'Display delimiter mismatch: {label}/{field}')
        require(value.count('{')==value.count('}'), f'Brace mismatch: {label}/{field}')
        for match in re.finditer(r'\\cite[tp](?:\[[^\]]*\])?\{([^}]+)\}',value):
            require(set(match.group(1).split(',')) <= set(item['refs']),
                    f'Cite absent from refs: {label}/{field}/{match.group(1)}')
for problem in problems:
    require(set(problem['occurrences']) <= itemids, 'Problem occurrence outside slice: '+problem['id'])
    require(set(problem['refs']) <= set(keys), 'Problem reference absent: '+problem['id'])
    require(problem['status_date']=='2026-11', 'Incorrect status cutoff: '+problem['id'])
for item in items:
    if item['problem'] and item['problem'] != 'GP-1986-60':
        p=next(p for p in problems if p['id']==item['problem'])
        require(item['id'] in p['occurrences'], 'Unlisted problem occurrence: '+item['id'])
print('Talks:',len(talks))
print('Items:',len(items))
print('Classes:',dict(sorted(collections.Counter(x['class'] for x in items).items())))
print('Problems:',len(problems),'; external consolidated GP-1986-60 occurrences:',
      ', '.join(x['id'] for x in items if x['problem']=='GP-1986-60'))
print('References:',len(keys))
print('Corrections:',len(list(csv.DictReader((B/'corrections.csv').open()))))
if errors:
    for error in errors:
        print('ERROR:',error)
    raise SystemExit(1)
print('PASS: local schema, occurrence numbering, problem links, references, and LaTeX delimiter checks')
