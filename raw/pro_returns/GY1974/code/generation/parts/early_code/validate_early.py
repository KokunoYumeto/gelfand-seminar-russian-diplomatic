from pathlib import Path
import json,re,csv,collections
root=Path(__file__).resolve().parents[2];p=root/'parts'
items=json.loads((p/'early_items.json').read_text());talks=json.loads((p/'early_talks.json').read_text());probs=json.loads((p/'early_problems.json').read_text());boundary=json.loads((p/'early_boundary.json').read_text());bib=(p/'early_references.bib').read_text();keys=set(re.findall(r'@\w+\s*\{\s*([^,\s]+)',bib))
assert {t['record'] for t in talks}=={331,332,334,335,336,337,338,339,340,341}
required={'id','record','pages','kind','title','notes','statement','reconstruction','class','fate','present_status','literal_correctness','publication_match','verification','development','problem','worth','refs','confidence'}
for record in {t['record'] for t in talks}:
 a=[v for v in items if v['record']==record]
 assert [v['id'] for v in a]==[f'1974-{record}.{j+1}' for j in range(len(a))]
for v in items:
 assert required<=set(v),v['id']
 assert v['class'] in 'ABCDEF'
 assert v['literal_correctness'] in {'correct','correct with missing hypotheses','false as written','not determinable'}
 assert v['publication_match'] in {'exact','partial','thematic only','none found'}
 assert v['verification'] in {'read the result','publisher metadata checked','indirect','unresolved lead'}
 assert v['development'] in {'none','annotated','developed in this chapter'}
 assert set(v['refs'])<=keys,(v['id'],set(v['refs'])-keys)
 for field,value in v.items():
  if isinstance(value,str):
   assert not any(ord(c)<32 and c not in '\n\r' for c in value),(v['id'],field)
   refs=set()
   for m in re.finditer(r'\\cite[tp](?:\[[^]]*\])?\{([^}]+)\}',value):refs.update(m.group(1).split(','))
   assert refs<=set(v['refs']),(v['id'],refs-set(v['refs']))
 assert not v['worth'] or v['class'] in 'CD'
byid={v['id']:v for v in items}
for pr in probs:
 assert set(pr['refs'])<=keys
 for oid in pr['occurrences']:
  if oid in byid:assert byid[oid]['problem']==pr['id'],(pr['id'],oid)
for v in items:
 if v['problem'] and v['problem']!='GP-1974-10':
  assert any(pr['id']==v['problem'] and v['id'] in pr['occurrences'] for pr in probs),v['id']
assert len(boundary)==26
for v in boundary:assert set(v['refs'])<=keys
# Braces in authored TeX must balance. Escaped braces are ignored.
for f in ['early_audit.tex','early_boundary.tex']:
 s=(p/f).read_text();d=0
 for m in re.finditer(r'(?<!\\)[{}]',s):
  d+=1 if m.group()=='{' else -1
  assert d>=0,(f,m.start())
 assert d==0,f
report={'talks':len(talks),'items_raw':len(items),'items_excluding_five_source_aliases':len(items)-5,'class_counts':dict(collections.Counter(v['class'] for v in items)),'problems_owned':len(probs),'boundary_prior_rows':len(boundary),'bibliography_keys':len(keys),'correction_rows':len(list(csv.DictReader((p/'early_corrections.csv').open()))),'checks':'All structural, enum, citation, reciprocal-link, control-character and TeX-brace checks passed. Shared-kit build and compilation are performed by root after merge.'}
(p/'early_code/validation.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
