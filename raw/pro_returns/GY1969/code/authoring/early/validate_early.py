"""Data integrity checks for the assigned segment; no chapter build."""
from pathlib import Path
from collections import Counter
import csv,json,re
D=Path(__file__).resolve().parent
root=D.parents[1]
talks=json.loads((D/'talks.json').read_text())
items=json.loads((D/'items.json').read_text())
problems=json.loads((D/'problems.json').read_text())
sources=json.loads((D/'sources.json').read_text())
corrections=list(csv.DictReader((D/'corrections.csv').open()))
errors=[]
def check(ok,message):
 if not ok: errors.append(message)
check(sorted(t['record'] for t in talks)==list(range(174,191)),'Record coverage or duplicates')
check(len(set(i['id'] for i in items))==len(items),'Duplicate occurrence ID')
check(len(set(p['id'] for p in problems))==len(problems),'Duplicate problem ID')
for record in range(174,191):
 seq=[i['id'] for i in items if i['record']==record]
 year=1969 if record<=183 else 1970
 check(seq==[f'{year}-{record}.{n}' for n in range(1,len(seq)+1)],f'Occurrence numbering {record}')
problem_ids={p['id'] for p in problems}
item_ids={i['id'] for i in items}
previous=(root/'previous_index.md').read_text()
bibfiles=[D/'references.bib',root/'references_cumulative.bib',root/'parts/root/references.bib']
bib='\n'.join(p.read_text() for p in bibfiles)
bibkeys=set(re.findall(r'@\w+\s*\{\s*([^,\s]+)',bib))
latex_fields=['notes','statement','reconstruction','fate','present_status','worth','summary','status']
for obj in talks+items+problems:
 label=obj.get('id',str(obj.get('record')))
 for field,value in obj.items():
  if isinstance(value,str):
   check(not any(ord(c)<32 and c not in '\n\r' for c in value),f'Control character {label}.{field}')
   check('``' not in value,f'Legacy opening quote {label}.{field}')
  if field in latex_fields and isinstance(value,str):
   check(value.count(r'\(')==value.count(r'\)'),f'Inline math delimiters {label}.{field}')
   check(value.count(r'\[')==value.count(r'\]'),f'Display math delimiters {label}.{field}')
   depth=0
   for token in re.findall(r'\\[{}]|[{}]',value):
    if token=='{':depth+=1
    if token=='}':depth-=1
    if depth<0:break
   check(depth==0,f'Brace balance {label}.{field}')
   outside=re.sub(r'\\\(.*?\\\)|\\\[.*?\\\]', '',value,flags=re.S)
   outside=re.sub(r'\\(?:nolinkurl|url)\{[^}]*\}','',outside)
   check(not re.search(r'(?<!\\)[_^]',outside),f'Bare math character {label}.{field}')
   cites=re.findall(r'\\cite[tp](?:\[[^]]*\])?\{([^}]+)\}',value)
   for group in cites:
    for key in group.split(','):
     check(key in bibkeys,f'Missing bibliography key {key}')
     if 'refs' in obj:check(key in obj['refs'],f'Cited key absent from refs {label}: {key}')
 if 'refs' in obj:
  for key in obj['refs']:check(key in bibkeys,f'Missing ref {label}: {key}')
 if obj.get('problem'):check(obj['problem'] in problem_ids,f'Missing problem object {label}')
 if obj.get('class') in ['C','D']:check(bool(obj['worth']),f'Empty worth {label}')
for p in problems:
 for occurrence in p['occurrences']:
  check(occurrence in item_ids or occurrence in previous,f'Missing problem occurrence {occurrence}')
for row in corrections:
 for field in ['transcription_reads','should_read','evidence']:
  value=row[field]
  outside=re.sub(r'\\\(.*?\\\)|\\\[.*?\\\]', '',value,flags=re.S)
  outside=re.sub(r'\\(?:nolinkurl|url)\{[^}]*\}','',outside)
  check(not re.search(r'(?<!\\)[_^]',outside),f'Bare math character in correction {row["page"]}.{field}')
report=dict(records=len(talks),items=len(items),problems=len(problems),corrections=len(corrections),references=len(re.findall(r'@\w+\s*\{',(D/'references.bib').read_text())),source_entries=len(sources),classes=dict(Counter(i['class'] for i in items)),verification=dict(Counter(i['verification'] for i in items)),by_record=dict(Counter(i['record'] for i in items)),errors=errors)
(D/'validation.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
raise SystemExit(bool(errors))
