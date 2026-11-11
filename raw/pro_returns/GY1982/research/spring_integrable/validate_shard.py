"""Validate the research shard without modifying shared chapter outputs."""
import collections,csv,json,pathlib,re
D=pathlib.Path(__file__).parent
T=json.loads((D/'talks.json').read_text())
I=json.loads((D/'items.json').read_text())
P=json.loads((D/'problems.json').read_text())
C=list(csv.DictReader((D/'corrections.csv').open()))
A=json.loads((D/'source_audit.json').read_text())
B=(D/'references.bib').read_text()
keys=set(re.findall(r'@\w+\{([^,\s]+)',B))
errors=[]
def check(value,message):
 if not value:errors.append(message)
check([t['record'] for t in T]==[586,587,588,589,590,591,592,594,593,596,595,598],'Talk source order')
required=set('id record pages kind title notes statement reconstruction class fate present_status literal_correctness publication_match verification development problem worth refs confidence'.split())
enum={
 'kind':set('definition construction theorem claim conjecture question problem method remark'.split()),
 'class':set('ABCDEF'),
 'literal_correctness':{'correct','correct with missing hypotheses','false as written','not determinable'},
 'publication_match':{'exact','partial','thematic only','none found'},
 'verification':{'read the result','publisher metadata checked','indirect','unresolved lead'},
 'development':{'none','annotated','developed in this chapter'},
 'confidence':{'high','medium','low'}
}
for record in [t['record'] for t in T]:
 rows=[x for x in I if x['record']==record]
 check([x['id'] for x in rows]==[f'1982-{record}.{n}' for n in range(1,len(rows)+1)],f'Consecutive IDs for {record}')
for x in I:
 check(required<=x.keys(),x['id']+' missing fields')
 for k,values in enum.items():check(x[k] in values,x['id']+' invalid '+k)
 check(set(x['refs'])<=keys,x['id']+' unknown bibliography key')
 if x['class'] in 'CD':check(bool(x['worth']),x['id']+' missing worth')
 if x['problem']:check(x['problem'] in {p['id'] for p in P},x['id']+' unknown problem')
 for value in x.values():
  if isinstance(value,str):
   used={k.strip() for m in re.finditer(r'\\cite\w*(?:\[[^\]]*\])?\{([^}]+)\}',value) for k in m.group(1).split(',')}
   check(used<=set(x['refs']),x['id']+' citation not listed in refs '+str(used-set(x['refs'])))
for p in P:
 check(p['status_date']=='2026-11',p['id']+' date')
 check(set(p['refs'])<=keys,p['id']+' unknown reference')
 check(bool(re.search(r'\\cite',p['status'])),p['id']+' standalone status lacks citation')
 for occurrence in p['occurrences']:
  if occurrence.startswith('1982-'):check(occurrence in {x['id'] for x in I},p['id']+' missing occurrence')
check(keys==set(A),'Every bibliography key has current opened-source audit')
for key in keys:
 check(A[key]['opened_url'].startswith('https://'),key+' missing opened URL')
 check(bool(A[key]['locator_and_scope']),key+' missing locator/scope')
check(len(re.findall(r'note\s*=\s*\{verified\}',B))==len(keys),'Bibliography verification notes')
# A precise shared ledger row may cover several related formulas on one item.
false_ledger={
 '1982-586.1':[('P001087','equation (3), variational annotation')],
 '1982-586.4':[('P001088','equation (10)')],
 '1982-586.6':[('P001089','equation (12)'),('P001089','equation (13)')],
 '1982-587.2':[('P001089','binomial expansion')],
 '1982-587.5':[('P001091','free spectral zeta normalization')],
 '1982-587.8':[('P001092','Euler and formal sums')],
 '1982-587.10':[('P001092','Clausen value')],
 '1982-588.3':[('P001094','local action covering')],
 '1982-589.2':[('P001094','factorization exponential')],
 '1982-590.3':[('P001096','Fedosov block projector'),('P001097','auxiliary symbol a and cutoff')],
 '1982-592.8':[('P001105',r'\(n=2\) tau reconstruction')],
 '1982-593.1':[('P001109','stationary-phase formula for fixed submanifolds')],
 '1982-593.2':[('P001109','pushforward and variation of symplectic form')],
 '1982-593.5':[('P001111','square of the Cartan differential')],
 '1982-595.2':[('P001113','good integral equations at every prime'),('P001114','local zeta definition (2)')],
 '1982-595.3':[('P001114','finite-field zero location')],
 '1982-595.7':[('P001114','completed elliptic functional equation')]
}
ledger={(c['page'],c['place']) for c in C}
for x in I:
 if x['literal_correctness']=='false as written':
  check(x['id'] in false_ledger,x['id']+' has no mapped correction')
  for pair in false_ledger.get(x['id'],[]):check(pair in ledger,x['id']+' missing correction '+str(pair))
# Check raw LaTeX fields, including the builder's raw correction cells.
latex_fields={'summary','notes','statement','reconstruction','fate','present_status','worth','status'}
for x in T+I+P+C:
 for field,value in x.items():
  if not isinstance(value,str):continue
  label=str(x.get('id',x.get('record',x.get('page'))))+' '+field
  check(not any(ord(c)<32 and c not in '\n\r' for c in value),label+' control character')
  if field not in latex_fields and not (x in C and field in {'transcription_reads','should_read','evidence'}):continue
  clean=re.sub(r'\\nolinkurl\{[^}]*\}','',value)
  clean=re.sub(r'\\cite\w*(?:\[[^\]]*\])?\{[^}]*\}','',clean)
  check(len(re.findall(r'\\\(',clean))==len(re.findall(r'\\\)',clean)),label+' inline math delimiters')
  check(len(re.findall(r'\\\[',clean))==len(re.findall(r'\\\]',clean)),label+' display math delimiters')
  check(not re.search(r'(?<!\\)[#%]',clean),label+' unescaped hash/percent')
  clean=re.sub(r'\\\(.*?\\\)|\\\[.*?\\\]','',clean,flags=re.S)
  check(not re.search(r'(?<!\\)[_^&]',clean),label+' bare math token outside math')
report={
 'result':'PASS' if not errors else 'FAIL',
 'talks':len(T),'items':len(I),'problems':len(P),'correction_rows':len(C),
 'bibliography_keys':len(keys),'classes':dict(collections.Counter(x['class'] for x in I)),
 'items_by_record':dict(collections.Counter(str(x['record']) for x in I)),
 'false_as_written_to_corrections':{x['id']:false_ledger.get(x['id'],[]) for x in I if x['literal_correctness']=='false as written'},
 'errors':errors
}
(D/'validation_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
