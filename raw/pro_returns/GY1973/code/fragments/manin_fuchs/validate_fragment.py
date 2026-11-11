from pathlib import Path
import json,re,csv,collections,subprocess,shutil
P=Path(__file__).resolve().parent
items=json.loads((P/'items.json').read_text()); talks=json.loads((P/'talks.json').read_text()); problems=json.loads((P/'problems.json').read_text())
bib=(P/'references.bib').read_text();bk=re.findall(r'(?m)^@\w+\{([^,]+),',bib); errors=[]
if len(bk)!=len(set(bk)):errors.append('duplicate bibliography keys')
required={'id','record','pages','kind','title','notes','statement','reconstruction','class','fate','present_status','literal_correctness','publication_match','verification','development','problem','worth','refs','confidence'}
for i in items:
 if not required<=i.keys():errors.append((i['id'],'missing fields',required-i.keys()))
 for k,v in i.items():
  if isinstance(v,str) and any(ord(c)<32 for c in v):errors.append((i['id'],k,'control character',repr(v)))
 for r in i['refs']:
  if r not in bk:errors.append((i['id'],'missing ref',r))
 cited=set()
 for v in i.values():
  if isinstance(v,str):
   for m in re.findall(r'\\cite[pt]?\*?(?:\[[^\]]*\])*\{([^}]*)\}',v):cited.update(x.strip() for x in m.split(','))
 if not cited<=set(i['refs']):errors.append((i['id'],'unlisted cited refs',cited-set(i['refs'])))
 if i['class'] in 'CD' and not i['worth']:errors.append((i['id'],'missing C/D rationale'))
 if not i['present_status'].startswith('As of 9 November 2026: '):errors.append((i['id'],'status date'))
for t in talks:
 seq=[i['id'] for i in items if i['record']==t['record']]
 if seq!=[f"1973-{t['record']}.{n}" for n in range(1,len(seq)+1)]:errors.append(('nonconsecutive',t['record']))
for p in problems:
 for i in items:
  if i['problem']==p['id'] and i['id'] not in p['occurrences']:errors.append(('missing reciprocal occurrence',i['id']))
counts=collections.Counter(i['class'] for i in items)
report={'items':len(items),'talks':len(talks),'problems':len(problems),'bibliography_entries':len(bk),'classes':dict(counts),'by_record':dict(collections.Counter(i['record'] for i in items)),'corrections':len(list(csv.DictReader((P/'corrections.csv').open()))),'errors':errors}
(P/'validation_output.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(json.dumps(report,ensure_ascii=False,indent=2))
if errors:raise SystemExit(1)
C=P/'compile_check';C.mkdir(exist_ok=True)
for n in ['talks.json','items.json','problems.json','references.bib','corrections.csv']:shutil.copyfile(P/n,C/f'GY1973_{n}')
(C/'GY1973_overview.tex').write_text('Fragment validation: records 303--311.\n')
shutil.copyfile(P/'critical_verifications.tex',C/'GY1973_development.tex')
shutil.copyfile(P.parents[1]/'kit'/'gelfand_companion.sty',C/'gelfand_companion.sty')
r=subprocess.run(['python',str(P.parents[1]/'kit'/'build_chapter.py'),'GY1973',str(C)],text=True,capture_output=True)
(P/'build_output.txt').write_text(r.stdout+r.stderr);print(r.stdout+r.stderr)
raise SystemExit(r.returncode)
