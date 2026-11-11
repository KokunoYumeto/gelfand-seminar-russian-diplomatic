from pathlib import Path
import re

def stripcmd(t,name,n):
 p=0
 while True:
  p=t.find('\\'+name+'{',p)
  if p<0:return t
  q=p+len(name)+1
  for k in range(n):
   if t[q]!='{':break
   d=1;q+=1
   while d and q<len(t):
    if t[q]=='{' and t[q-1]!='\\':d+=1
    if t[q]=='}' and t[q-1]!='\\':d-=1
    q+=1
  t=t[:p]+t[q:]
for lang in ('en','ru'):
 chunks=[]
 for i in range(125,140):
  t=Path(f'work/pages/P{i:06d}_{lang}.txt').read_text()
  t=stripcmd(t,'SourceFigure',3)
  t=re.sub(r'\\(?:begin|end)\{GelfandAdjacentEvidence\}(?:\{[^}]*\}){0,2}','',t)
  t=re.sub(r'\n{3,}','\n\n',t)
  chunks.append(t)
 Path(f'work/parts/late_reading_{lang}.txt').write_text('\n'.join(chunks))
