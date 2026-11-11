from pathlib import Path
import json,re,csv,collections
p=Path(__file__).resolve().parent
talks=json.loads((p/'talks.json').read_text()); items=json.loads((p/'items.json').read_text()); probs=json.loads((p/'problems.json').read_text())
assert [t['record'] for t in talks]==list(range(530,538))
assert not [x for x in items if x['record']==530]
required='id record pages kind title notes statement reconstruction class fate present_status literal_correctness publication_match verification development problem worth refs confidence area'.split()
enums={'class':list('ABCDEF'),'kind':['definition','construction','theorem','claim','conjecture','question','problem','method','remark'],'literal_correctness':['correct','correct with missing hypotheses','false as written','not determinable'],'publication_match':['exact','partial','thematic only','none found'],'verification':['read the result','publisher metadata checked','indirect','unresolved lead'],'development':['none','annotated','developed in this chapter'],'confidence':['high','medium','low']}
for rec in range(531,538):
 part=[x for x in items if x['record']==rec]
 assert [x['id'] for x in part]==[f'1981-{rec}.{n}' for n in range(1,len(part)+1)]
for x in items:
 assert all(k in x for k in required),(x['id'],set(required)-x.keys())
 for k,vs in enums.items():assert x[k] in vs,(x['id'],k,x[k])
 assert x['class'] not in 'CD' or x['worth']
keys=re.findall(r'(?m)^@\w+\{([^,]+)',(p/'references.bib').read_text())
assert len(keys)==len(set(keys))
used=set()
for x in items+probs:used.update(x['refs'])
for name in ['talks.json','items.json','problems.json','development.tex']:
 txt=(p/name).read_text()
 if name.endswith('.json'):
  txt='\n'.join(str(v) for x in json.loads(txt) for v in x.values() if isinstance(v,str))
 used.update(k.strip() for a in re.findall(r'\\cite[tp]?(?:\[[^]]*\])*\{([^}]+)\}',txt) for k in a.split(','))
assert not used-set(keys),used-set(keys)
assert all(x['problem']=='' or x['problem'] in {q['id'] for q in probs} for x in items)
assert all(o in {x['id'] for x in items} for q in probs for o in q['occurrences'])
rows=list(csv.DictReader((p/'corrections.csv').open()))
assert all(x['type'] in ['transcription','translation','ambiguity','faithful_error','provenance',''] for x in rows)
assert all(x['applies_to'] in ['ru','en','both'] for x in rows)
for name,fields in [('items.json',['notes','statement','reconstruction','fate','present_status','worth']),('talks.json',['summary']),('problems.json',['statement','status'])]:
 for x in json.loads((p/name).read_text()):
  for f in fields:
   s=re.sub(r'\\\(.*?\\\)|\\\[.*?\\\]','',x.get(f,''),flags=re.S)
   assert not re.search(r'(?<!\\)[_^]',s),(x.get('id',x.get('record')),f,s)
   assert not re.search(r'[\x00-\x08\x0b\x0c\x0e-\x1f]',x.get(f,'')),(x.get('id'),f)
for row in rows:
 for field in ('place','transcription_reads','should_read','evidence'):
  outside=re.sub(r'\\\(.*?\\\)|\\\[.*?\\\]', '',row[field],flags=re.S)
  assert not re.search(r'(?<!\\)[_^]',outside),(row['page'],field,outside)
result=['SCHEMA/CITATION AUDIT PASS',f'Talks={len(talks)} items={len(items)} problems={len(probs)} corrections={len(rows)} references={len(keys)}','Class counts '+str(dict(collections.Counter(x['class'] for x in items))),'Verification counts '+str(dict(collections.Counter(x['verification'] for x in items))),'Record counts '+str(dict(collections.Counter(x['record'] for x in items))),'Unused bibliography entries '+str(set(keys)-used),'No raw underscores/carets outside mathematical delimiters in LaTeX data fields; no control characters.']
print('\n'.join(result))
(p/'validation_output.txt').write_text('\n'.join(result)+'\n')
