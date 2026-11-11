"""Validate the owned data fragment against CHAPTER_FORMAT.md.

Run after make_fragment.py. This checks integration contracts, not mathematical
truth; the latter is documented by source verification and independent checks.
"""
from pathlib import Path
import csv
import json
import re
from collections import Counter

p = Path(__file__).resolve().parent
items = json.loads((p/'items.json').read_text())
talks = json.loads((p/'talks.json').read_text())
problems = json.loads((p/'problems.json').read_text())
areas = json.loads((p/'area_map.json').read_text())
corrections = list(csv.DictReader((p/'corrections.csv').open()))
bib = (p/'references.bib').read_text()
keys = re.findall(r'@\w+\s*\{\s*([^,\s]+)\s*,', bib)
errors = []

def check(condition, message):
    if not condition:
        errors.append(message)

item_fields = {'id','record','pages','kind','title','notes','statement','reconstruction',
               'class','fate','present_status','literal_correctness','publication_match',
               'verification','development','problem','worth','refs','confidence'}
order = [313,312,314,315,316,317,318,319,321,320,322,323]
check([t['record'] for t in talks] == order, 'Wrong source order or missing record')
check(len(keys) == len(set(keys)), 'Duplicate bibliography keys')
ids = {x['id'] for x in items}
check(len(ids) == len(items), 'Duplicate item IDs')
check(set(areas) == ids, 'Area-map coverage differs from item coverage')
check(all(areas.values()), 'Empty area')
problem_ids = {x['id'] for x in problems}
check(len(problem_ids) == len(problems), 'Duplicate problem IDs')
check(all('GP-1973-' in x and 30 <= int(x.rsplit('-',1)[1]) <=49 for x in problem_ids), 'Problem ID outside reserved block')

for record in order:
    seq = [x['id'] for x in items if x['record']==record]
    check(seq == [f'1973-{record}.{i}' for i in range(1,len(seq)+1)],f'{record}: nonconsecutive IDs')
for x in items:
    ident = x['id']
    check(item_fields <= set(x), f'{ident}: missing fields')
    check(set(x) <= item_fields|{'speaker'},f'{ident}: unexpected fields')
    check(x['kind'] in {'definition','construction','theorem','claim','conjecture','question','problem','method','remark'},f'{ident}: kind')
    check(x['class'] in set('ABCDEF'),f'{ident}: class')
    check(x['literal_correctness'] in {'correct','correct with missing hypotheses','false as written','not determinable'},f'{ident}: literal status')
    check(x['publication_match'] in {'exact','partial','thematic only','none found'},f'{ident}: publication match')
    check(x['verification'] in {'read the result','publisher metadata checked','indirect','unresolved lead'},f'{ident}: verification')
    check(x['development'] in {'none','annotated','developed in this chapter'},f'{ident}: development')
    check(x['confidence'] in {'high','medium','low'},f'{ident}: confidence')
    check(x['present_status'].startswith('As of 9 November 2026:'),f'{ident}: undated status')
    check(not x['problem'] or x['problem'] in problem_ids,f'{ident}: missing linked problem')
    check(x['class'] not in {'C','D'} or bool(x['worth']),f'{ident}: no worth assessment')
    check(set(x['refs']) <= set(keys),f'{ident}: missing bibliography entry')
    cited = set()
    for value in x.values():
        if isinstance(value,str):
            for group in re.findall(r'\\cite[pt]?\*?(?:\[[^\]]*\])*\{([^}]*)\}',value):
                cited.update(k.strip() for k in group.split(','))
    check(cited <= set(x['refs']),f'{ident}: cited key missing from refs')
for x in problems:
    check(x['status_date']=='2026-11',f'{x["id"]}: date')
    check(set(x['refs']) <= set(keys),f'{x["id"]}: missing bibliography')
    check(all(not y.startswith('1973-') or y in ids for y in x['occurrences']),f'{x["id"]}: missing current occurrence')
for x in corrections:
    check(x['applies_to'] in {'ru','en','both'},'Invalid correction scope')
    check(x['type'] in {'transcription','translation','ambiguity','faithful_error','provenance',''},'Invalid correction type')
for entry in re.split(r'(?=@\w+\s*\{)',bib)[1:]:
    key = re.search(r'@\w+\s*\{\s*([^,\s]+)',entry).group(1)
    check(bool(re.search(r'\b(?:url|doi)\s*=\s*\{',entry)),f'{key}: no URL/DOI')
    check(bool(re.search(r'\bnote\s*=\s*\{(?:verified|unverified)\}',entry)),f'{key}: no verification note')
    check('annote' in entry,f'{key}: no verification-scope annotation')

report = {
    'status_date':'2026-11-09',
    'talks':len(talks),'items':len(items),'problems':len(problems),
    'references':len(keys),'corrections':len(corrections),
    'classes':dict(Counter(x['class'] for x in items)),
    'items_by_record':dict(Counter(x['record'] for x in items)),
    'areas':dict(Counter(areas.values())),
    'errors':errors,
}
(p/'validation_output.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
raise SystemExit(bool(errors))
