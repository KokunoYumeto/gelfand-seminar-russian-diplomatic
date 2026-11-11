import json, csv, re
from pathlib import Path
D=Path(__file__).parent
def read(n):return json.loads((D/n).read_text())
def write(n,x):(D/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
items=read('items.json')
by={x['id']:x for x in items}
replacements={
 '``locally.':r'\emph{locally}.',
 '``exponential numbers':r'\emph{exponential numbers}',
 '``plane.':r'\emph{plane}.',
 '``Plane means':r'\emph{Plane} means',
 '``normal here':r'\emph{normal} here',
 '``always about':r'\emph{always} about',
 '``describe does':r'\emph{describe} does',
 r'``\(k\)-forms with values in \(M\).':r'\emph{\(k\)-forms with values in \(M\)}.',
 r'``\(D_2\ne0\),':r'\(D_2\ne0\),',
 '``this is a complex.':r'\emph{this is a complex}.',
 '``resolution must':r'\emph{resolution} must',
 '``complex is':r'\emph{complex} is',
 '``the index over any ring.':r'\emph{the index over any ring}.',
 '``for every ring.':r'\emph{for every ring}.'
}
for x in items:
 for k,v in x.items():
  if isinstance(v,str):
   for a,b in replacements.items():v=v.replace(a,b)
   x[k]=v
for id in ['1971-235.1','1971-235.2','1971-233.8']:
 x=by[id]
 if not x['reconstruction'].startswith(r'\ours'):x['reconstruction']=r'\ours\ '+x['reconstruction']
by['1971-235.1']['statement']=by['1971-235.1']['statement'].replace('The count uses',r'\ours\ The count uses')
by['1971-235.2']['statement']=by['1971-235.2']['statement'].replace('Necessity follows',r'\ours\ Necessity follows')
by['1971-233.8']['statement']=by['1971-233.8']['statement'] if by['1971-233.8']['statement'].startswith(r'\ours') else r'\ours\ '+by['1971-233.8']['statement']
by['1971-232.3']['fate']=r'The precise graded identity belongs to the Frölicher--Nijenhuis calculus reviewed in \citet[\S\S1--2]{michor1989derivations}; \citet{michor1987remarks} gives a broader account. The relation of this identity to the unidentified Rego announcement is only a reconstruction, not an exact publication match.'
by['1971-232.3']['refs']=['michor1989derivations','michor1987remarks']
by['1971-237.8']['reconstruction']=r'\ours\ The parity-symmetry deduction is supplied here and proved in the chapter’s verification subsection. It diagnoses the literal recorded example; it does not reconstruct an unrecorded operator restriction.'
by['1971-243.3']['statement']=by['1971-243.3']['statement'].replace(r'\operatorname{Der}_{\mathbb R}',r'\operatorname{Der}^{\mathrm{cont}}_{\mathbb R}')
write('items.json',items)
ps=read('problems.json')
for p in ps:
 if p['id']=='GP-1970-26':p['title']='Homotoping a distribution to a foliation'
write('problems.json',ps)
areas={
 229:'Symplectic geometry and geometric quantization',
 231:'Algebraic groups and representation theory',
 232:'Differential geometry',
 233:'Operator theory and Banach spaces',
 234:'Microlocal analysis',
 235:'Finite geometry and integral geometry',
 236:'Foliations and characteristic classes',
 237:'Index theory and spectral flow',
 238:'Algebraic geometry and motives',
 239:'Schubert calculus and characteristic classes',
 240:'Algebraic differential calculus',
 241:'Algebraic differential calculus',
 242:'Algebraic differential calculus',
 243:'Formal geometry and foliation cohomology'
}
mapping={x['id']:areas[x['record']] for x in items}
mapping['1971-239.7']='Algebraic groups and representation theory'
write('areas.json',mapping)
# Preserve mathematical LaTeX; escape literal special characters in older prose cells.
path=D/'corrections.csv'
with path.open(newline='') as f:
 reader=csv.DictReader(f);header=reader.fieldnames;rows=list(reader)
def safe(s):
 s=s.replace(r'B\G',r'\(B\backslash G\)')
 parts=re.split(r'(\\\(.*?\\\)|\\\[.*?\\\])',s,flags=re.S)
 for j in range(0,len(parts),2):
  parts[j]=re.sub(r'(?<!\\)([_&#%])',r'\\\1',parts[j])
  parts[j]=re.sub(r'(?<!\\)\^',r'\\textasciicircum{}',parts[j])
 return ''.join(parts)
for row in rows:
 for k in ['place','transcription_reads','should_read','evidence']:row[k]=safe(row[k])
with path.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=header);w.writeheader();w.writerows(rows)
print(f'Finalized {len(items)} items, {len(ps)} problems, {len(rows)} correction rows and {len(mapping)} area assignments.')
