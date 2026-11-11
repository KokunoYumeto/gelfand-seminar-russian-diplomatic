import json,re,csv,collections
from pathlib import Path
p=Path(__file__).resolve().parent
items=json.loads((p/'autumn_items.json').read_text());talks=json.loads((p/'autumn_talks.json').read_text());probs=json.loads((p/'autumn_problems.json').read_text());s=(p/'autumn_references.bib').read_text();keys=re.findall(r'(?m)^@\w+\{([^,]+),',s)
assert len(keys)==len(set(keys))
required=['id','record','pages','kind','title','notes','statement','reconstruction','class','fate','present_status','literal_correctness','publication_match','verification','development','problem','worth','refs','confidence']
for x in items:
 assert all(k in x for k in required), x['id']
 assert x['kind'] in 'definition construction theorem claim conjecture question problem method remark'.split(),x['id']
 for k,v in x.items():
  if isinstance(v,str):assert not re.search(r'[\x00-\x08\x0b\x0c\x0e-\x1f]',v),(x['id'],k,repr(v))
 citations=[]
 for k in ['notes','statement','fate','present_status','reconstruction','worth']:
  for m in re.finditer(r'\\cite[tp](?:\[[^\]]*\])?\{([^}]+)\}',x[k]):citations += m[1].split(',')
 assert set(citations)<=set(x['refs']),(x['id'],set(citations)-set(x['refs']))
 assert set(x['refs'])<=set(keys),(x['id'],set(x['refs'])-set(keys))
for r in range(490,500):
 a=[x for x in items if x['record']==r]
 assert [x['id'] for x in a]==[f'1980-{r}.{j+1}' for j in range(len(a))]
for x in probs:
 assert set(x['refs'])<=set(keys),x['id']
 assert all(a=='1967-144.7' or a in {i['id'] for i in items} for a in x['occurrences']),x['id']
print('Records',len(talks),'items',len(items),'problems',len(probs),'refs',len(keys),'corrections',len(list(csv.DictReader((p/'autumn_corrections.csv').open()))))
print('Classes',dict(collections.Counter(x['class'] for x in items)))
print('Source order',[t['record'] for t in talks])
print('F items',[x['id'] for x in items if x['class']=='F'])
print('All schema, citation and control-character checks passed.')
