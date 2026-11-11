from pathlib import Path
from collections import Counter,defaultdict
import json,re,csv
p=Path(__file__).resolve().parents[1]
talks=json.loads((p/'late_talks.json').read_text())
items=json.loads((p/'late_items.json').read_text())
problems=json.loads((p/'late_problems.json').read_text())
bib=(p/'late_references.bib').read_text()
corrections=list(csv.DictReader((p/'late_corrections.csv').open()))
keys=set(re.findall(r'@\w+\{([^,]+),',bib))
errors=[]
required={'id','record','pages','kind','title','notes','statement','reconstruction','class','fate','present_status','literal_correctness','publication_match','verification','development','problem','worth','refs','confidence'}
kinds={'definition','construction','theorem','claim','conjecture','question','problem','method','remark'}
ids={a['id'] for a in items}
assert set(t['record'] for t in talks)==set(range(352,362))
assert len(talks)==10 and len(ids)==len(items)
per=defaultdict(list)
def citations(text):
 return {k.strip() for m in re.finditer(r'\\cite[tp](?:\[[^\]]*\])?\{([^}]+)\}',text) for k in m.group(1).split(',')}
for a in items:
 missing=required-set(a)
 if missing: errors.append(f"{a['id']}: missing {missing}")
 if a['kind'] not in kinds:errors.append(f"{a['id']}: kind")
 per[a['record']].append(a['id'])
 used=set()
 for field in ('notes','statement','reconstruction','fate','present_status','worth'):
  s=a[field]
  used|=citations(s)
  for left,right in ((r'\(',r'\)'),(r'\[',r'\]')):
   if s.count(left)!=s.count(right):errors.append(f"{a['id']}/{field}: math delimiters")
  cleaned=s.replace(r'\{','').replace(r'\}','')
  balance=0
  for c in cleaned:
   if c=='{':balance+=1
   elif c=='}':balance-=1
   if balance<0:errors.append(f"{a['id']}/{field}: negative brace balance");break
  if balance:errors.append(f"{a['id']}/{field}: brace balance {balance}")
 if used-set(a['refs']):errors.append(f"{a['id']}: unlisted citations {used-set(a['refs'])}")
 if set(a['refs'])-keys:errors.append(f"{a['id']}: missing bib entries")
 if 'November 2026' not in a['present_status']:errors.append(f"{a['id']}: status date")
 if a['class'] in 'CD' and not a['worth']:errors.append(f"{a['id']}: worth")
for rec,occ in per.items():
 if occ!=[f'1974-{rec}.{n}' for n in range(1,len(occ)+1)]:errors.append(f"{rec}: IDs not consecutive")
problemids={a['id'] for a in problems}
for q in problems:
 if set(q['occurrences'])-ids:errors.append(f"{q['id']}: missing occurrence")
 if set(q['refs'])-keys:errors.append(f"{q['id']}: missing reference")
 for i in q['occurrences']:
  a=next(a for a in items if a['id']==i)
  if a['problem']!=q['id']:errors.append(f"{q['id']}: absent item backref {i}")
for a in items:
 if a['problem'] and a['problem'] not in problemids:errors.append(f"{a['id']}: missing problem")
for t in talks:
 if citations(t['summary'])-keys:errors.append(f"talk {t['record']}: missing ref")
for c in corrections:
 for value in c.values():
  if citations(value)-keys:errors.append(f"correction {c['page']}: missing ref")
audit=(p/'late_audit.tex').read_text()
if citations(audit)-keys:errors.append("audit: missing bib")
# Every bibliography entry is opened; exact reading scope is carried in annote.
entries=re.split(r'(?m)(?=^@)',bib)
for e in entries:
 if not e.strip():continue
 if not re.search(r'(?:url|doi)\s*=',e):errors.append("bib: no locator")
 if not re.search(r'note\s*=\s*\{verified\}',e):errors.append("bib: verification missing")
def area(a):
 r=a['record']; n=int(a['id'].split('.')[1])
 if r in (354,355):return 'Statistical mechanics and Gibbs fields'
 if r==358:return 'Probability foundations'
 if r==359:return 'Quantum field theory'
 if r in (360,361):return 'Complex analysis and geometry'
 if r==356 and 11<=n<=13:return 'Symplectic geometry'
 if r==357 and n>=7:return 'Algebraic differential operators'
 return 'Microlocal analysis and integral geometry'
area_map={a['id']:area(a) for a in items}
speaker_by_rec={t['record']:t['speaker'] for t in talks}
speaker_counts=Counter(a.get('speaker',speaker_by_rec[a['record']]) for a in items)
result={
 'records':len(talks),'items':len(items),'problems':len(problems),'corrections':len(corrections),'references':len(keys),
 'classes':dict(Counter(a['class'] for a in items)),
 'record_counts':dict(Counter(a['record'] for a in items)),
 'verification':dict(Counter(a['verification'] for a in items)),
 'publication_match':dict(Counter(a['publication_match'] for a in items)),
 'literal_correctness':dict(Counter(a['literal_correctness'] for a in items)),
 'speaker_counts':dict(speaker_counts),
 'area_counts':dict(Counter(area_map.values())),
 'errors':errors
}
(p/'late_area_map.json').write_text(json.dumps(area_map,ensure_ascii=False,indent=2)+'\n')
(p/'late_code'/'validation_output.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
if errors:raise SystemExit(1)
