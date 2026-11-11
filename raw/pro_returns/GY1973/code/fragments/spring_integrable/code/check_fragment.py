from pathlib import Path
import json, re, csv, collections
P=Path(__file__).resolve().parents[1]
a=json.loads((P/'items.json').read_text())
t=json.loads((P/'talks.json').read_text())
p=json.loads((P/'problems.json').read_text())
area=json.loads((P/'area_map.json').read_text())
bib=(P/'references.bib').read_text()
keys=re.findall(r'(?m)^@\w+\{([^,]+),',bib)
errors=[]
if len(keys)!=len(set(keys)):errors.append('duplicate bibliography keys')
for rec in range(324,334):
 if sum(x['record']==rec for x in t)!=1:errors.append(f'record{rec} missing or duplicated')
 seq=[x for x in a if x['record']==rec]
 if [x['id'] for x in seq]!=[f'1973-{rec}.{i}' for i in range(1,len(seq)+1)]:errors.append(f'record{rec} nonsequential IDs')
for x in a:
 if x['id'] not in area:errors.append(x['id']+' no area')
 if x['class'] in 'CD' and not x.get('worth'):errors.append(x['id']+' no worth')
 for k in x['refs']:
  if k not in keys:errors.append(x['id']+' missing ref '+k)
 for field,value in x.items():
  if isinstance(value,str):
   if any(ord(c)<32 and c not in '\n\t' for c in value):errors.append(x['id']+' control byte in '+field)
   if value.count(r'\(')!=value.count(r'\)'):errors.append(x['id']+' math delimiter mismatch in '+field)
   for cite in re.findall(r'\\cite[tp]?(?:\[[^\]]*\])?\{([^}]+)\}',value):
    for k in cite.split(','):
     if k not in x['refs']:errors.append(x['id']+' undeclared citation '+k)
ids={x['id'] for x in a}
for q in p:
 for k in q['refs']:
  if k not in keys:errors.append(q['id']+' missing ref '+k)
 for id in q['occurrences']:
  if id not in ids and id.startswith('1973-'):errors.append(q['id']+' missing occurrence '+id)
c=list(csv.DictReader((P/'corrections.csv').open()))
report={'date':'2026-11-09','records':[x['record'] for x in t],'items':len(a),'classes':dict(collections.Counter(x['class'] for x in a)),'items_by_record':dict(collections.Counter(str(x['record']) for x in a)),'problems':[x['id'] for x in p],'references':len(keys),'corrections':len(c),'errors':errors}
(P/'output'/'data_check.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
if errors:raise SystemExit(1)
