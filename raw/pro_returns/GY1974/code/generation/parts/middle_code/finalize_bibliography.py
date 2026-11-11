"""Fill reused bibliography keys and check the middle-record deliverables."""
import csv,json,re
from pathlib import Path
OUT=Path(__file__).resolve().parents[1]
WORK=OUT.parent
def entries(path):
 if not path.exists(): return {}
 text=path.read_text()
 out={}
 for m in re.finditer(r'(?m)^@\w+\{([^,]+),.*?(?=^@|\Z)',text,re.S|re.M):
  out.setdefault(m.group(1),m.group(0).strip())
 return out
items=json.loads((OUT/'middle_items.json').read_text())
problems=json.loads((OUT/'middle_problems.json').read_text())
needed={key for d in items+problems for key in d['refs']}
sources={}
for path in [OUT/'middle_references.bib',OUT/'early_references.bib',OUT/'root_references.bib',WORK/'references_cumulative.bib']:
 for key,value in entries(path).items(): sources.setdefault(key,value)
assert needed<=sources.keys(),sorted(needed-sources.keys())
(OUT/'middle_references.bib').write_text('\n\n'.join(sources[k] for k in sorted(needed))+'\n')
assert len({d['id'] for d in items})==len(items)
assert sorted({d['record'] for d in items})==[342,343,344,345,346,347,349,350,351]
for record in sorted({d['record'] for d in items}):
 rows=[d for d in items if d['record']==record]
 assert [d['id'] for d in rows]==[f'1974-{record}.{i}' for i in range(1,len(rows)+1)]
for d in items:
 cited=set()
 for value in d.values():
  if isinstance(value,str):
   assert not re.search('[\x00-\x08\x0b-\x1f\t]',value),(d['id'],repr(value))
   for match in re.finditer(r'\\cite[tp](?:\[[^]]*\])?\{([^}]+)\}',value):cited.update(match.group(1).split(','))
 assert cited<=set(d['refs']),(d['id'],cited-set(d['refs']))
 assert d['literal_correctness'] in ['correct','correct with missing hypotheses','false as written','not determinable']
 assert d['verification'] in ['read the result','publisher metadata checked','indirect','unresolved lead']
 assert d['publication_match'] in ['exact','partial','thematic only','none found']
 if d['class'] in 'CD':assert d['worth']
def check_raw_math(value,location):
 if not isinstance(value,str):return
 assert not re.search(r'(?<!\\)\\S[IVXLCDM]+\b',value),(location,'section command joined to Roman numeral')
 stripped=re.sub(r'\\\(.*?\\\)|\\\[.*?\\\]','',value,flags=re.S)
 assert not re.search(r'(?<!\\)[_%^]',stripped),(location,stripped)
for filename in ['middle_items.json','middle_talks.json','middle_problems.json']:
 for d in json.loads((OUT/filename).read_text()):
  for key,value in d.items():check_raw_math(value,(filename,d.get('id',d.get('record')),key))
for d in csv.DictReader((OUT/'middle_corrections.csv').open()):
 for key in ['transcription_reads','should_read','evidence']:check_raw_math(d[key],('corrections',d['page'],key))
assert not re.search(r'(?<!\\)\\S[IVXLCDM]+\b',(OUT/'middle_audit.tex').read_text()),'joined Roman section command in audit'
print('Verified',len(items),'items,',len(problems),'problem entries,',len(needed),'bibliography keys; no control characters or missing cited keys.')
print('No unescaped underscores, percent signs or carets outside math in the LaTeX fields.')
