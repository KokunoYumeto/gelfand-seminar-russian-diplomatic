"""Validate the owned block and refresh the source inventory, without modifying other parts."""
from pathlib import Path
from collections import Counter
import csv
import json
import re

P = Path(__file__).resolve().parent
items = json.loads((P/'items.json').read_text())
talks = json.loads((P/'talks.json').read_text())
problems = json.loads((P/'problems.json').read_text())
corrections = list(csv.DictReader((P/'corrections.csv').open()))
required = {'id','record','pages','kind','title','notes','statement','reconstruction',
            'class','fate','present_status','literal_correctness','publication_match',
            'verification','development','problem','worth','refs','confidence'}
assert len(items) == 73 and len(talks) == 15
assert len(problems) == 8 and len(corrections) == 33
assert {t['record'] for t in talks} == set(range(36,51))
assert len({i['id'] for i in items}) == len(items)
assert len({p['id'] for p in problems}) == len(problems)
problem_ids = {p['id'] for p in problems}
all_bib = '\n'.join(q.read_text() for q in P.parent.rglob('*references.bib'))
all_keys = set(re.findall(r'@\w+\{([^,]+),', all_bib))
for record in range(36,51):
    group = [i for i in items if i['record'] == record]
    assert [i['id'] for i in group] == [f'1964-{record}.{n}' for n in range(1,len(group)+1)]
for item in items:
    assert required <= set(item), (item['id'], required-set(item))
    assert item['class'] in 'ABCDEF'
    assert item['confidence'] in {'high','medium','low'}
    assert item['literal_correctness'] in {'correct','correct with missing hypotheses','false as written','not determinable'}
    assert item['publication_match'] in {'exact','partial','thematic only','none found'}
    assert item['verification'] in {'read the result','publisher metadata checked','indirect','unresolved lead'}
    assert item['development'] in {'none','annotated','developed in this chapter'}
    if item['class'] in 'CD':
        assert item['worth'], item['id']
    if item['problem']:
        assert item['problem'] in problem_ids, (item['id'],item['problem'])
        prob = next(p for p in problems if p['id'] == item['problem'])
        assert item['id'] in prob['occurrences'], item['id']
    cited = set()
    for field in ('notes','statement','reconstruction','fate','present_status','worth'):
        for citation in re.findall(r'\\cite\w*(?:\[[^\]]*\])?\{([^}]+)\}', item[field]):
            cited.update(k.strip() for k in citation.split(','))
    assert cited <= set(item['refs']), (item['id'],cited-set(item['refs']))
    assert set(item['refs']) <= all_keys, (item['id'],set(item['refs'])-all_keys)
    assert '2026' in item['present_status'], item['id']
for prob in problems:
    assert prob['status_date'] == '2026-11'
    assert set(prob['refs']) <= all_keys, (prob['id'],set(prob['refs'])-all_keys)
    for occurrence in prob['occurrences']:
        if occurrence in {i['id'] for i in items}:
            assert next(i for i in items if i['id']==occurrence)['problem'] == prob['id']

bibtext = (P/'references.bib').read_text()
entries = []
for chunk in re.split(r'(?=@\w+\{)', bibtext)[1:]:
    key = re.match(r'@\w+\{([^,]+),', chunk).group(1)
    fields = dict(re.findall(r'^  (\w+) = \{(.*)\},?$', chunk, re.M))
    assert 'url' in fields or 'doi' in fields, key
    assert fields.get('note') in {'verified','unverified'}, key
    assert fields.get('annote'), key
    entries.append((key,fields))
assert len(entries) == 50
heading = '## Primary-source URL and locator inventory'
log = (P/'research_log.md').read_text().split(heading)[0]
log += heading + '\n\nThe following inventory is generated from the checked bibliography. Each entry records the verification depth. Root-owned Domar, Sz.-Nagy–Foiaş and Ma entries are described above and resolved during the global bibliography merge.\n\n'
for key,fields in sorted(entries):
    log += f"### {key}\n\n{fields.get('title','')} ({fields.get('year','')}). **{fields['note']}**.\n\n"
    if 'url' in fields:
        log += fields['url'] + '\n\n'
    if 'doi' in fields:
        log += 'DOI: ' + fields['doi'] + '\n\n'
    log += fields['annote'] + '\n\n'
(P/'research_log.md').write_text(log)
counts = Counter(i['class'] for i in items)
print(f'PASS: {len(talks)} talks, {len(items)} items, {len(problems)} problems, {len(corrections)} corrections, {len(entries)} bibliography entries.')
print('Classes: '+', '.join(f'{k}={counts[k]}' for k in 'ABCDEF'))
print('Citation keys, mandatory assessment fields, consecutive IDs, and problem backlinks: PASS.')
print('Root-owned bibliography keys used: '+', '.join(sorted({k for i in items for k in i['refs']}- {k for k,f in entries})))
print('Refreshed complete primary-source URL and locator inventory in research_log.md.')
