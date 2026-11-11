"""Read-only bibliography comparison; writes its own report in fragment c."""
import difflib,json,re,unicodedata
from pathlib import Path
D=Path(__file__).parent
root=D.parents[1]
def braced(s,pos):
 depth=1;j=pos+1
 while j<len(s) and depth:
  if s[j]=='{':depth+=1
  elif s[j]=='}':depth-=1
  j+=1
 return s[pos+1:j-1],j
def entries(path):
 s=path.read_text();out=[];p=0
 while m:=re.search(r'@(\w+)\s*\{\s*([^,]+),',s[p:]):
  start=p+m.start();bodypos=p+m.end()-1
  body,end=braced(s,s.index('{',start));p=end
  key,rest=body.split(',',1);fields={};fp=0
  while f:=re.search(r'(\w+)\s*=\s*',rest[fp:]):
   name=f[1].lower();vpos=fp+f.end()
   if rest[vpos]=='{':val,fp=braced(rest,vpos)
   elif rest[vpos]=='"':
    fp=rest.index('"',vpos+1)+1;val=rest[vpos+1:fp-1]
   else:
    stop=rest.find(',',vpos);fp=len(rest) if stop<0 else stop;val=rest[vpos:fp]
   fields[name]=val.strip()
  out.append(dict(key=key.strip(),type=m[1],fields=fields))
 return out
def norm(s):
 s=unicodedata.normalize('NFKD',s).lower()
 s=re.sub(r'\\[\'"`^~=.uvHcbdkr]\s*\{?([a-z])\}?',r'\1',s)
 s=re.sub(r'\\[a-z]+','',s)
 return re.sub(r'[^a-z0-9]+','',s)
paths={'cumulative':root/'source_kit/references_cumulative.bib','a':root/'fragments/a/references.bib','b':root/'fragments/b/references.bib'}
data={k:entries(v) for k,v in paths.items()}
lines=[]
for name,es in data.items():
 lines.append(f'{name}: {len(es)} entries')
 if name!='cumulative':
  for e in es:lines.append(f"  {e['key']} | {e['fields'].get('year','')} | {e['fields'].get('title','')}")
for name in ['a','b']:
 lines.append('\n'+name.upper()+' V CUMULATIVE')
 for e in data[name]:
  f=e['fields']
  for ce in data['cumulative']:
   cf=ce['fields'];causes=[]
   if e['key']==ce['key']:causes.append('same key')
   for field in ['doi','url']:
    if f.get(field) and norm(f[field])==norm(cf.get(field,'')):causes.append('same '+field)
   ratio=difflib.SequenceMatcher(None,norm(f.get('title','')),norm(cf.get('title',''))).ratio()
   if ratio>.77:causes.append(f'title similarity {ratio:.3f}')
   if causes:
    lines.append(f"{e['key']} => {ce['key']} [{', '.join(causes)}]")
    for field in sorted(set(f)|set(cf)):
     if field in ['annote','note']:continue
     if f.get(field)!=cf.get(field):lines.append(f'  {field}: NEW={f.get(field)!r}; OLD={cf.get(field)!r}')
lines.append('\nA V B')
for ae in data['a']:
 for be in data['b']:
  af=ae['fields'];bf=be['fields']
  if ae['key']==be['key'] or (af.get('doi') and af.get('doi')==bf.get('doi')) or norm(af.get('title',''))==norm(bf.get('title','')):
   lines.append(f"{ae['key']} = {be['key']}")
out='\n'.join(lines)+'\n'
(D/'bibliography_comparison.txt').write_text(out)
(D/'bibliography_parsed.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
print(out)
