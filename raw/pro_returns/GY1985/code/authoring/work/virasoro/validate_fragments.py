from pathlib import Path
import json,re,csv,collections
out=Path('work/virasoro'); items=json.loads((out/'items.json').read_text()); talks=json.loads((out/'talks.json').read_text()); probs=json.loads((out/'problems.json').read_text())
required={'id','record','pages','kind','title','notes','statement','reconstruction','class','fate','present_status','literal_correctness','publication_match','verification','development','problem','worth','refs','confidence'}
allowed={
'kind':set('definition construction theorem claim conjecture question problem method remark'.split()),
'class':set('ABCDEF'),
'literal_correctness':{'correct','correct with missing hypotheses','false as written','not determinable'},
'publication_match':{'exact','partial','thematic only','none found'},
'verification':{'read the result','publisher metadata checked','indirect','unresolved lead'},
'development':{'none','annotated','developed in this chapter'},
'confidence':{'high','medium','low'}}
bib=(out/'references.bib').read_text(); keys=re.findall(r'@\w+\{([^,]+),',bib); assert len(keys)==len(set(keys))
keyset=set(keys); ids={i['id'] for i in items}; assert len(ids)==len(items)
assert [t['record'] for t in talks]==[658,659,660,661,662]
bounds={658:(1229,1231),659:(1231,1235),660:(1236,1238),661:(1238,1240),662:(1241,1244)}
for i in items:
 assert required<=set(i), i['id']
 for field,vals in allowed.items(): assert i[field] in vals,(i['id'],field,i[field])
 assert set(i['refs'])<=keyset,(i['id'],set(i['refs'])-keyset)
 assert i['class'] not in 'CD' or i['worth'],i['id']
 for n in re.findall(r'P(\d+)',i['pages']): assert bounds[i['record']][0]<=int(n)<=bounds[i['record']][1],i['id']
 for field in ('notes','statement','reconstruction','fate','present_status','worth'):
  txt=i[field]
  assert txt.count(r'\(')==txt.count(r'\)'),(i['id'],field,'inline math')
  assert txt.count(r'\[')==txt.count(r'\]'),(i['id'],field,'display math')
  plain=re.sub(r'\\[{}]','',txt)
  assert plain.count('{')==plain.count('}'),(i['id'],field,'braces')
  cites=set()
  for match in re.finditer(r'\\cite[pt](?:\[[^]]*\])?\{([^}]+)\}',txt): cites.update(match[1].split(','))
  assert cites<=set(i['refs']),(i['id'],field,cites-set(i['refs']))
for rec in bounds:
 group=[i for i in items if i['record']==rec]
 assert [i['id'] for i in group]==[f'1985-{rec}.{j}' for j in range(1,len(group)+1)]
pmap={p['id']:p for p in probs}
for p in probs:
 assert p['status_date']=='2026-11'
 assert set(p['occurrences'])<=ids
 assert set(p['refs'])<=keyset
for i in items:
 if i['problem']:
  assert i['problem'] in pmap
  assert i['id'] in pmap[i['problem']]['occurrences'],i['id']
for p in probs:
 for ident in p['occurrences']:
  assert next(i for i in items if i['id']==ident)['problem']==p['id'],ident
rows=list(csv.DictReader((out/'corrections.csv').open()))
assert all(r['type'] in {'transcription','translation','ambiguity','faithful_error','provenance',''} for r in rows)
assert all(r['applies_to'] in {'ru','en','both'} for r in rows)
sources=json.loads((out/'sources.json').read_text())
assert len({s['url'] for s in sources})==len(sources)
report=[f'Validated {len(talks)} talks, {len(items)} items, {len(probs)} problems',f'Per record: {dict(collections.Counter(i["record"] for i in items))}',f'Classes: {dict(collections.Counter(i["class"] for i in items))}',f'{len(keys)} bibliography keys; all item citations resolve and are declared',f'{len(rows)} correction rows; {len(sources)} unique source endpoints', 'All required fields, enums, consecutive IDs, source page bounds, math delimiters, brace counts, and bidirectional problem links passed.', 'Full XeLaTeX/BibTeX compilation is assigned to root integration.']
(out/'validation_output.txt').write_text('\n'.join(report)+'\n');print('\n'.join(report))
