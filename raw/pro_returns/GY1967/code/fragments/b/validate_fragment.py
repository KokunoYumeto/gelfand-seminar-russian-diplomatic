"""Structural validation of the six integration files; no theorem proof claimed."""
from pathlib import Path
import json,csv,re,collections

root=Path(__file__).parent
talks=json.loads((root/'talks.json').read_text())
items=json.loads((root/'items.json').read_text())
problems=json.loads((root/'problems.json').read_text())
rows=list(csv.DictReader((root/'corrections.csv').open()))
bib=(root/'references.bib').read_text()
keys=re.findall(r'@\w+\{([^,]+),',bib)
errors=[]
assert len(keys)==len(set(keys))
assert [x['record'] for x in talks]==list(range(141,155))
assert len(items)==len({x['id'] for x in items})
assert all(not any(i['record']==r for i in items) for r in [141,148])
enums={
 'kind':{'definition','construction','theorem','claim','conjecture','question','problem','method','remark'},
 'class':set('ABCDEF'),
 'literal_correctness':{'correct','correct with missing hypotheses','false as written','not determinable'},
 'publication_match':{'exact','partial','thematic only','none found'},
 'verification':{'read the result','publisher metadata checked','indirect','unresolved lead'},
 'development':{'none','annotated','developed in this chapter'},
 'confidence':{'high','medium','low'}}
required={'id','record','pages','kind','title','notes','statement','reconstruction','class','fate','present_status','literal_correctness','publication_match','verification','development','problem','worth','refs','confidence'}
for rec in range(142,155):
 group=[x for x in items if x['record']==rec]
 year=1967 if rec<=147 else 1968
 if [x['id'] for x in group]!=[f'{year}-{rec}.{j+1}' for j in range(len(group))]:errors.append(f'IDs for record{rec}')
for obj in items:
 ident=obj['id']
 if required-set(obj):errors.append((ident,'missing fields'))
 for k,vals in enums.items():
  if obj[k] not in vals:errors.append((ident,k,obj[k]))
 if obj['class'] in 'CD' and not obj['worth']:errors.append((ident,'empty worth'))
 if 'November 2026' not in obj['present_status']:errors.append((ident,'undated status'))
 if not re.fullmatch(r'P\d{6}(?:-P\d{6})?',obj['pages']):errors.append((ident,'pages'))
 for key in obj['refs']:
  if key not in keys:errors.append((ident,'missing bib',key))
 text=' '.join(v for v in obj.values() if isinstance(v,str))
 for keygroup in re.findall(r'\\cite[tp](?:\[[^\]]*\])?\{([^}]+)\}',text):
  for key in keygroup.split(','):
   if key not in obj['refs']:errors.append((ident,'citation not in refs',key))
 if obj['problem']:
  matches=[p for p in problems if p['id']==obj['problem']]
  if len(matches)!=1 or ident not in matches[0]['occurrences']:errors.append((ident,'problem link'))
for group in [talks,items,problems,rows]:
 for obj in group:
  ident=obj.get('id',obj.get('record',obj.get('page')))
  for k,v in obj.items():
   if not isinstance(v,str):continue
   if any(ord(c)<32 and c not in '\n\t' for c in v):errors.append((ident,k,'control character'))
   for a,b in [(r'\(',r'\)'),(r'\[',r'\]')]:
    if v.count(a)!=v.count(b):errors.append((ident,k,'math delimiters'))
   if v.count('{')!=v.count('}'):errors.append((ident,k,'braces'))
for row in rows:
 for k in ['place','transcription_reads','should_read','evidence']:
  text=re.sub(r'\\\(.*?\\\)|\\\[.*?\\\]','',row[k],flags=re.S)
  if re.search(r'(?<!\\)[_^$&%#]',text):errors.append((row['page'],k,'raw LaTeX special outside math'))
report={'talks':len(talks),'items':len(items),'problems':len(problems),'corrections':len(rows),'references':len(keys),'classes':dict(collections.Counter(x['class'] for x in items)),'errors':errors}
(root/'validation.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
raise SystemExit(bool(errors))
