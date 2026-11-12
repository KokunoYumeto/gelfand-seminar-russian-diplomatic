#!/usr/bin/env python3
"""Validate the winter data without compiling or changing shared output."""
from pathlib import Path
import collections, csv, json, re

HERE=Path(__file__).resolve().parent
WORK=HERE.parents[1]
talks=json.loads((HERE/'talks.json').read_text())
items=json.loads((HERE/'items.json').read_text())
problems=json.loads((HERE/'problems.json').read_text())
bib=(HERE/'references.bib').read_text()
keys=set(re.findall(r'@\w+\{([^,]+),',bib))
errors=[]
required=set('id record pages kind title notes statement reconstruction class fate present_status literal_correctness publication_match verification development problem worth refs confidence'.split())
enums={
 'kind':set('definition construction theorem claim conjecture question problem method remark'.split()),
 'class':set('ABCDEF'),
 'literal_correctness':{'correct','correct with missing hypotheses','false as written','not determinable'},
 'publication_match':{'exact','partial','thematic only','none found'},
 'verification':{'read the result','publisher metadata checked','indirect','unresolved lead'},
 'development':{'none','annotated','developed in this chapter'},
 'confidence':{'high','medium','low'}
}
expected=set()
for ident in re.findall(r'1964-(\d+\.\d+)',(WORK/'previous_index.md').read_text()):
 if 15<=int(ident.split('.')[0])<=35:expected.add('1964-'+ident)
actual={i['id'] for i in items}
if expected!=actual:errors.append(('occurrence difference',sorted(expected-actual),sorted(actual-expected)))
if len(actual)!=len(items):errors.append('duplicate item IDs')
if [t['record'] for t in talks]!=list(range(15,36)):errors.append('talk record order')
if next(t for t in talks if t['record']==23)['kind']!='plan':errors.append('record23 not plan')
for it in items:
 if required-set(it):errors.append((it['id'],'missing fields',sorted(required-set(it))))
 for field,allowed in enums.items():
  if it[field] not in allowed:errors.append((it['id'],'enum',field,it[field]))
 if it['class'] in 'CD' and not it['worth']:errors.append((it['id'],'missing worth'))
 if not it['present_status'].startswith('As of '):errors.append((it['id'],'undated status'))
 cited=set()
 for field,value in it.items():
  if not isinstance(value,str):continue
  if re.search(r'[\x00-\x08\x0b\x0c\x0e-\x1f]',value):errors.append((it['id'],field,'control character'))
  if value.count(r'\(')!=value.count(r'\)'):errors.append((it['id'],field,'math delimiter'))
  for raw in re.findall(r'\\cite[tp]\*?(?:\[[^\]]*\]){0,2}\{([^}]+)\}',value):
   cited.update(raw.split(','))
 if cited-set(it['refs']):errors.append((it['id'],'citations missing from refs',sorted(cited-set(it['refs']))))
 if set(it['refs'])-keys:errors.append((it['id'],'unknown refs',sorted(set(it['refs'])-keys)))
for record in range(15,36):
 seq=[int(i['id'].split('.')[1]) for i in items if i['record']==record]
 if seq!=list(range(1,len(seq)+1)):errors.append((record,'nonconsecutive item IDs',seq))
pids={p['id'] for p in problems}
for it in items:
 if it['problem'] and it['problem'] not in pids:errors.append((it['id'],'missing problem'))
for p in problems:
 if set(p['occurrences'])-actual:errors.append((p['id'],'unknown occurrence'))
 if set(p['refs'])-keys:errors.append((p['id'],'unknown refs'))
 if p['status_date']!='2026-11':errors.append((p['id'],'wrong status date'))
with (HERE/'corrections.csv').open() as stream:
 rows=list(csv.DictReader(stream))
for row in rows:
 if row['applies_to'] not in {'ru','en','both'}:errors.append(('bad correction language',row))
 if row['type'] not in {'transcription','translation','ambiguity','faithful_error','provenance',''}:errors.append(('bad correction type',row))
print('Records:',len(talks),'(15–35, including plan23)')
print('Occurrence IDs:',len(actual),'exactly match all supplied same-year first-run IDs in scope')
print('Classes:',dict(sorted(collections.Counter(i['class'] for i in items).items())))
print('Bibliography:',len(keys),'entries; all referenced keys present')
print('Problems:',len(problems),'(four provisional W identifiers for root merge; shared GP-1964-02)')
print('Corrections:',len(rows))
print('Errors:',len(errors))
for error in errors:print(error)
raise SystemExit(bool(errors))
