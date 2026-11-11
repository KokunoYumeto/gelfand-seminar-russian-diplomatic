"""Structural QA for fragment c; mathematical arguments are checked separately."""
import collections,csv,json,re
from pathlib import Path
D=Path(__file__).parent
T=json.loads((D/'talks.json').read_text())
I=json.loads((D/'items.json').read_text())
P=json.loads((D/'problems.json').read_text())
C=list(csv.DictReader((D/'corrections.csv').open()))
B=(D/'references.bib').read_text()
keys=re.findall(r'@\w+\s*\{\s*([^,\s]+)',B)
errors=[]
def ck(test,msg):
 if not test:errors.append(msg)
def raw_math_specials(value):
 """Find unescaped _ or ^ outside explicit TeX math delimiters."""
 mode=None;found=[];i=0
 while i<len(value):
  pair=value[i:i+2]
  if pair in (r'\(',r'\['):mode=pair;i+=2;continue
  if pair in (r'\)',r'\]'):mode=None;i+=2;continue
  if value[i]=='\\':i+=2;continue
  if value[i]=='$':
   token='$$' if pair=='$$' else '$'
   mode=None if mode==token else token;i+=len(token);continue
  if value[i] in '_^' and mode is None:found.append((i,value[max(0,i-20):i+25]))
  i+=1
 return found
def check_text(value,label):
 ck(not any(ord(c)<32 and c not in '\n\r' for c in value),f'{label}: control character')
 # Ignore escaped literal braces; other braces must balance.
 bare=re.sub(r'\\[{}]','',value)
 level=0
 for char in bare:
  if char=='{':level+=1
  if char=='}':level-=1
  if level<0:break
 ck(level==0,f'{label}: brace imbalance')
 ck(value.count(r'\(')==value.count(r'\)'),f'{label}: inline math imbalance')
 ck(value.count(r'\[')==value.count(r'\]'),f'{label}: display math imbalance')
 for match in re.finditer(r'\\cite[tp](?:\[[^]]*\]){0,2}\{([^}]+)\}',value):
  for key in match[1].split(','):ck(key in keys,f'{label}: missing bib key {key}')
def citations(obj):
 result=set()
 for value in obj.values():
  if isinstance(value,str):
   for m in re.finditer(r'\\cite[tp](?:\[[^]]*\]){0,2}\{([^}]+)\}',value):result.update(m[1].split(','))
 return result
itemfields=set('id record pages kind title notes statement reconstruction class fate present_status literal_correctness publication_match verification development problem worth refs confidence'.split())
talkfields=set('record date speaker pages title kind summary'.split())
problemfields=set('id title statement occurrences status status_date refs'.split())
allowed={
 'class':set('ABCDEF'),
 'kind':set('definition construction theorem claim conjecture question problem method remark'.split()),
 'literal_correctness':{'correct','correct with missing hypotheses','false as written','not determinable'},
 'publication_match':{'exact','partial','thematic only','none found'},
 'verification':{'read the result','publisher metadata checked','indirect','unresolved lead'},
 'development':{'none','annotated','developed in this chapter'},
 'confidence':{'high','medium','low'}}
ck(len(keys)==len(set(keys)),'duplicate bibliography keys')
ck([t['record'] for t in T]==[155,156,157,158,159,160,161,162,164,163,165,166],'wrong source record order')
seq=collections.Counter()
for x in I:
 label=x.get('id','missing id');ck(itemfields<=set(x),f'{label}: missing fields {itemfields-set(x)}')
 seq[x['record']]+=1
 ck(label==f"1968-{x['record']}.{seq[x['record']]}",f'{label}: sequence')
 for field,values in allowed.items():ck(x[field] in values,f'{label}: invalid {field}')
 ck('November 2026' in x['present_status'],f'{label}: status date missing')
 ck(set(x['refs'])<=set(keys),f'{label}: unresolved refs')
 ck(citations(x)<=set(x['refs']),f'{label}: cited works omitted from refs {citations(x)-set(x["refs"])}')
 if x['class'] in {'C','D'}:ck(bool(x['worth']),f'{label}: worth absent')
 if x['problem']:ck(x['problem'] in {p['id'] for p in P},f'{label}: absent problem')
 for k,v in x.items():
  if isinstance(v,str):check_text(v,label+'.'+k)
for t in T:
 ck(talkfields<=set(t),f'talk{t["record"]}: missing field')
 ck(t['kind'] in {'talk','plan','heading','other'},f'talk{t["record"]}: invalid kind')
 check_text(t['summary'],f'talk{t["record"]}')
for p in P:
 ck(problemfields<=set(p),f'{p["id"]}: missing field')
 ck(p['status_date']=='2026-11',f'{p["id"]}: date')
 ck(citations(p)<=set(p['refs']),f'{p["id"]}: refs')
 for oid in p['occurrences']:ck(oid in {x['id'] for x in I},f'{p["id"]}: absent occurrence {oid}')
 for k,v in p.items():
  if isinstance(v,str):check_text(v,p['id']+'.'+k)
for n,c in enumerate(C):
 ck(c['applies_to'] in {'ru','en','both'},f'correction{n}: applies_to')
 ck(c['type'] in {'','transcription','translation','ambiguity','faithful_error','provenance'},f'correction{n}: type')
 for k,v in c.items():check_text(v,f'correction{n}.{k}')
 for k in ['page','place','transcription_reads','should_read','evidence']:
  ck(not raw_math_specials(c[k]),f'correction{n}.{k}: raw math special outside delimiters {raw_math_specials(c[k])}')
ck(seq[158]==seq[165]==0,'invented items in contentless records')
ck(len(T)==12 and len(I)==76 and len(C)==19 and len(P)==1 and len(keys)==22,'unexpected counts')
report=[f'Records: {len(T)}',f'Items: {len(I)}',f'Classes: {dict(sorted(collections.Counter(x["class"] for x in I).items()))}',f'Corrections: {len(C)}',f'Problems: {len(P)}',f'References: {len(keys)}']
report+=['ERROR: '+e for e in errors] or ['PASS: required structure, IDs, citations, control characters, delimiter checks, and CSV math-special protection.']
text='\n'.join(report)+'\n'
(D/'validation.txt').write_text(text)
print(text,end='')
raise SystemExit(bool(errors))
