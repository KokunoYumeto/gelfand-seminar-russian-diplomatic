"""Additional semantic consistency checks beyond the supplied chapter builder."""
from pathlib import Path
from collections import Counter,defaultdict
import csv,json,re
from bib_tools import entries

ROOT=Path(__file__).resolve().parents[1]
D=ROOT
talks=json.loads((D/'GY1978_talks.json').read_text())
items=json.loads((D/'GY1978_items.json').read_text())
problems=json.loads((D/'GY1978_problems.json').read_text())
bib=entries((D/'GY1978_references.bib').read_text())
keys={e['key'] for e in bib}
assert len(keys)==len(bib),'Duplicate bibliography keys'
for e in bib:
    assert e['fields'].get('url') or e['fields'].get('doi'),e['key']
    assert e['fields'].get('note') in ['verified','unverified'],e['key']
enum={
'kind':set('definition construction theorem claim conjecture question problem method remark'.split()),
'class':set('ABCDEF'),
'literal_correctness':{'correct','correct with missing hypotheses','false as written','not determinable'},
'publication_match':{'exact','partial','thematic only','none found'},
'verification':{'read the result','publisher metadata checked','indirect','unresolved lead'},
'development':{'none','annotated','developed in this chapter'},
'confidence':{'high','medium','low'}}
required={'id','record','pages','kind','title','notes','statement','reconstruction','class','fate','present_status','literal_correctness','publication_match','verification','development','problem','worth','refs','confidence'}
seen=set(); by_rec=defaultdict(list)
citations=re.compile(r'\\cite[pt]?\*?(?:\[[^\]]*\])*\{([^}]*)\}')
for x in items:
    assert required<=set(x),(x.get('id'),'missing fields',required-set(x))
    assert x['id'] not in seen
    seen.add(x['id']);by_rec[x['record']].append(x)
    for key,values in enum.items():assert x[key] in values,(x['id'],key,x[key])
    assert set(x['refs'])<=keys,(x['id'],'unknown reference')
    if x['class'] in 'CD':assert x['worth']
    assert '2026' in x['present_status'],x['id']
    for value in [v for v in x.values() if isinstance(v,str)]:
        assert not any(ord(c)<32 and c not in '\n\t' for c in value),(x['id'],'control character')
        for group in citations.findall(value):
            assert set(k.strip() for k in group.split(','))<=set(x['refs']),(x['id'],'citation absent from refs',group)
for t in talks:
    assert t['kind'] in {'talk','plan','heading','other'}
    a=by_rec[t['record']]
    if t['kind']=='talk':assert a,(t['record'],'missing mathematical items')
    assert [x['id'] for x in a]==[f"1978-{t['record']}.{i}" for i in range(1,len(a)+1)]
pids={p['id'] for p in problems}
assert len(pids)==len(problems)
for x in items:
    if x['problem']:
        assert x['problem'] in pids
        assert x['id'] in next(p['occurrences'] for p in problems if p['id']==x['problem'])
for p in problems:
    assert p['status_date']=='2026-11'
    assert set(p['refs'])<=keys
    for i in p['occurrences']:
        if i.startswith('1978-'):
            assert i in seen,(p['id'],'unknown occurrence',i)
            assert next(x['problem'] for x in items if x['id']==i)==p['id'],(p['id'],'asymmetric problem link',i)
with (D/'GY1978_corrections.csv').open(newline='',encoding='utf-8') as f:
    corrections=list(csv.DictReader(f))
for c in corrections:
    assert c['applies_to'] in {'ru','en','both'}
    assert c['type'] in {'transcription','translation','ambiguity','faithful_error','provenance',''}
    assert all(c[k] for k in ['page','place','transcription_reads','should_read','evidence'])
print('Records:',len(talks),'Items:',len(items),'Problems:',len(problems),'References:',len(bib),'Corrections:',len(corrections))
print('Classes:',dict(sorted(Counter(x['class'] for x in items).items())))
for field in ['literal_correctness','publication_match','verification','development']:
    print(field+':',dict(sorted(Counter(x[field] for x in items).items())))
print('All schema, chronology-date, ID, bibliography and bidirectional problem-link checks passed.')
