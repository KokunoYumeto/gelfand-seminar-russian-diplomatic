"""Validate the records 698--712 handoff without editing the shared kit.

Run from any directory. The complete chapter is separately compiled by root.
This audit checks schema enums, chronology fields, occurrence numbering,
problem links, citation declarations, bibliography coverage and brace balance.
"""
from pathlib import Path
import collections
import csv
import json
import re

root = Path(__file__).resolve().parents[1]
talks = json.loads((root / 'talks.json').read_text())
items = json.loads((root / 'items.json').read_text())
problems = json.loads((root / 'problems.json').read_text())
bib = (root / 'references.bib').read_text()
keys = re.findall(r'@\w+\s*\{\s*([^,\s]+)', bib)
assert len(keys) == len(set(keys)), 'Duplicate bibliography keys'
keys = set(keys)
assert [x['record'] for x in talks] == list(range(698, 713))
assert len({x['id'] for x in items}) == len(items)
assert len({p['id'] for p in problems}) == len(problems)
enums = {
    'kind': {'definition', 'construction', 'theorem', 'claim', 'conjecture',
             'question', 'problem', 'method', 'remark'},
    'class': set('ABCDEF'),
    'literal_correctness': {'correct', 'correct with missing hypotheses',
                            'false as written', 'not determinable'},
    'publication_match': {'exact', 'partial', 'thematic only', 'none found'},
    'verification': {'read the result', 'publisher metadata checked',
                     'indirect', 'unresolved lead'},
    'development': {'none', 'annotated', 'developed in this chapter'},
    'confidence': {'high', 'medium', 'low'},
}
required = {'id','record','pages','kind','title','notes','statement',
            'reconstruction','class','fate','present_status','literal_correctness',
            'publication_match','verification','development','problem','worth',
            'refs','confidence'}
pid = {p['id']:p for p in problems}
item_by_id = {x['id']:x for x in items}
citations = re.compile(r'\\cite[tp](?:\[[^\]]*\])?\{([^}]+)\}')
def tex_audit(label, value):
    level = 0
    for m in re.finditer(r'(?<!\\)[{}]', value):
        level += 1 if m.group() == '{' else -1
        assert level >= 0, (label, 'unbalanced closing brace')
    assert level == 0, (label, 'unbalanced braces')
    assert value.count(r'\(') == value.count(r'\)'), (label, 'inline math')
    assert value.count(r'\[') == value.count(r'\]'), (label, 'display math')
    cited = {k.strip() for group in citations.findall(value)
             for k in group.split(',')}
    assert cited <= keys, (label, 'missing citation', cited - keys)
    return cited

for t in talks:
    assert t['kind'] in {'talk','plan','heading','other'}
    tex_audit(str(t['record']),t['summary'])
for record in range(698,713):
    group = [x for x in items if x['record']==record]
    assert [x['id'] for x in group] == [f'1986-{record}.{n}' for n in range(1,len(group)+1)]
for x in items:
    assert required <= x.keys(), (x['id'], required-x.keys())
    for name, allowed in enums.items():
        assert x[name] in allowed, (x['id'],name,x[name])
    assert set(x['refs']) <= keys, (x['id'], 'missing refs')
    cited = set()
    for field in ('notes','statement','reconstruction','fate','present_status','worth'):
        cited |= tex_audit(x['id'] + ':' + field, x[field])
    assert cited <= set(x['refs']), (x['id'], 'undeclared refs', cited-set(x['refs']))
    if x['class'] in {'C','D'}:
        assert x['worth'].strip(), x['id']
    if x['problem']:
        assert x['problem'] in pid, (x['id'], 'missing problem')
        assert x['id'] in pid[x['problem']]['occurrences'], x['id']
for p in problems:
    assert p['status_date']=='2026-11'
    assert set(p['refs']) <= keys
    cited = tex_audit(p['id'],p['statement']) | tex_audit(p['id'],p['status'])
    assert cited <= set(p['refs']), (p['id'], 'undeclared refs')
    for occ in p['occurrences']:
        assert occ in item_by_id or occ in {'1986-688.5','1986-695.11'}, (p['id'],occ)
        if occ in item_by_id:
            assert item_by_id[occ]['problem']==p['id']
with (root/'corrections.csv').open(newline='') as f:
    reader=csv.DictReader(f)
    assert reader.fieldnames==['page','place','transcription_reads','should_read','evidence','applies_to','type']
    corrections=list(reader)
for x in corrections:
    assert x['applies_to'] in {'ru','en','both'}
    assert x['type'] in {'transcription','translation','ambiguity','faithful_error','provenance',''}
print('PASS: required fields, schema enums, IDs, references, problem links and TeX delimiters')
print('Records:',len(talks),'Items:',len(items),'Problems:',len(problems))
print('Classes:',dict(sorted(collections.Counter(x['class'] for x in items).items())))
print('Items by record:',dict(sorted(collections.Counter(x['record'] for x in items).items())))
print('Bibliography:',len(keys),'Corrections:',len(corrections))
print('Verification:',dict(sorted(collections.Counter(x['verification'] for x in items).items())))
print('Source-order swaps for integrated assembly: 704 before 703; 708 before 707.')
print('No other source-order adjustment identified in this slice.')
