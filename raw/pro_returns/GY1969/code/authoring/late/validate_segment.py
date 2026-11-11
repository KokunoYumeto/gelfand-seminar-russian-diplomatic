#!/usr/bin/env python3
"""Check the segment schema and cross-references without compiling the chapter."""
from pathlib import Path
import json,re,csv,collections
P=Path(__file__).resolve().parent
talks=json.loads((P/'talks.json').read_text())
items=json.loads((P/'items.json').read_text())
problems=json.loads((P/'problems.json').read_text())
sources=json.loads((P/'sources.json').read_text())
assert [t['record'] for t in talks]==list(range(209,229))
fields={'id','record','pages','kind','title','notes','statement','reconstruction','class','fate','present_status','literal_correctness','publication_match','verification','development','problem','worth','refs','confidence'}
ids={i['id'] for i in items}
assert len(ids)==len(items)
for r in range(209,229):
    group=[i for i in items if i['record']==r]
    assert [i['id'] for i in group]==[f'1970-{r}.{n+1}' for n in range(len(group))]
bib=(P/'references.bib').read_text()
keys=set(re.findall(r'(?m)^@\w+\{([^,\s]+),',bib))
assert len(keys)==len(re.findall(r'(?m)^@',bib))
pids={p['id'] for p in problems}
for i in items:
    assert fields<=set(i),i['id']
    assert set(i['refs'])<=keys,(i['id'],set(i['refs'])-keys)
    assert i['class'] in 'ABCDEF'
    assert i['verification'] in {'read the result','publisher metadata checked','indirect','unresolved lead'}
    assert i['literal_correctness'] in {'correct','correct with missing hypotheses','false as written','not determinable'}
    assert i['publication_match'] in {'exact','partial','thematic only','none found'}
    assert i['development'] in {'none','annotated','developed in this chapter'}
    if i['class'] in 'CD': assert i['worth']
    if i['problem']: assert i['problem'] in pids
    assert '2026' in i['present_status']
    for f in ('notes','statement','reconstruction','fate','present_status','worth'):
        s=i[f]
        assert not any(ord(c)<32 and c not in '\n\r\t' for c in s),(i['id'],f,'control character')
        assert s.count(r'\(')==s.count(r'\)'),(i['id'],f,'inline math')
        assert s.count(r'\[')==s.count(r'\]'),(i['id'],f,'display math')
        depth=0
        for n,c in enumerate(s):
            if c in '{}':
                count=0; j=n-1
                while j>=0 and s[j]=='\\': count+=1; j-=1
                if count%2: continue
                depth += 1 if c=='{' else -1
                assert depth>=0,(i['id'],f,'brace underflow')
        assert depth==0,(i['id'],f,'unclosed brace')
        for match in re.findall(r'\\cite[pt](?:\[[^\]]*\])?\{([^}]*)\}',s):
            assert set(match.split(','))<=set(i['refs']),(i['id'],f,match)
for p in problems:
    assert set(p['occurrences'])<=ids,(p['id'],set(p['occurrences'])-ids)
    assert set(p['refs'])<=keys
    for occurrence in p['occurrences']:
        assert next(i for i in items if i['id']==occurrence)['problem']==p['id'],(p['id'],occurrence)
assert next(i for i in items if i['id']=='1970-228.8')['problem']=='GP-1970-59'
assert all('P000360' not in i['pages'] for i in items)
assert {s['key'] for s in sources}>=keys
assert [s['key'] for s in sources if not s['opened']]==['houma2026zeros']
with (P/'corrections.csv').open(newline='') as f:
    corrections=list(csv.DictReader(f))
assert all(c['type'] in {'transcription','translation','ambiguity','faithful_error','provenance',''} for c in corrections)
print('PASS: schema, consecutive IDs, all citation keys, problem links, source coverage, TeX delimiters, and excluded P360.')
print('Talks:',len(talks),'Items:',len(items),'Problems:',len(problems),'Corrections:',len(corrections),'Bibliography entries:',len(keys))
print('Classes:',dict(sorted(collections.Counter(i['class'] for i in items).items())))
print('Sources:',sum(s['opened'] for s in sources),'opened;',sum(not s['opened'] for s in sources),'unopened lead')
print('Mathematical verification is described in research_notes.md; this script checks structure, not theorems.')
