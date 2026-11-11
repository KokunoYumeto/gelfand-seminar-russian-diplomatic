import json,re,csv,collections
from pathlib import Path
root=Path(__file__).resolve().parents[1];out=root/'shards'
talks=json.loads((out/'early_talks.json').read_text());items=json.loads((out/'early_items.json').read_text());problems=json.loads((out/'early_problems.json').read_text());areas=json.loads((out/'early_areas.json').read_text())
bib=(out/'early_references.bib').read_text()
def field(entry,name):
 m=re.search(r'\b'+name+r'\s*=\s*\{',entry)
 if not m:return ''
 i=m.end();j=i;depth=1
 while depth:
  if entry[j]=='{' and entry[j-1]!='\\':depth+=1
  if entry[j]=='}' and entry[j-1]!='\\':depth-=1
  j+=1
 return entry[i:j-1]
parts=re.split(r'(?=@\w+\s*\{)',bib);entries={re.match(r'@\w+\s*\{([^,]+),',e).group(1):e for e in parts if e.startswith('@')}
ids={
'anosov1967geodesic':'turn80view2',
'bernsteingelfandgelfand1973schubert':'turn8view4; turn18view6 (initial PDF response); turn129view0; turn131view0 (later redirection)',
'brownspencer1976double':'turn57view2 (full PDF); turn135view2',
'dipperjames1986representations':'turn62view1; turn109view1',
'gelfandserganova1987combinatorial':'turn21view4; turn59view1; turn62view3; turn63view2 (negative bimatroid search)',
'good1970short':'turn57view0; turn135view1',
'grothendieck1957homological':'turn18view1',
'halversonram1999bitraces':'turn83view0; turn95view0; turn96view0',
'hartshorne1966residues':'turn18view2',
'hutchinson1981fractals':'turn80view3',
'kerov1987realizations':'turn18view5; turn59view0; turn63view3; turn111view0',
'knorrer1982geodesics':'original retrieval failed; exact failed-call ID not retained; indirect theorem turn62view0/turn63view0',
'kraskiewiczpragacz2004schubert':'turn8view0; turn21view3; turn72view1; turn113view2',
'kung1978bimatroids':'original retrieval failed403; exact failed-call ID not retained; modern primary attribution turn62view2/turn100view2',
'lascouxschutzenberger1982schubert':'turn128view0 (author bibliography); turn129view1; turn133view0 (full result)',
'macdonald1995symmetric':'turn18view0; turn72view3 (Jacobi-Trudi); turn72view4 (Frobenius)',
'nist2026dlmf':'turn113view0; turn113view1',
'oxleybriefly':'turn14view4; turn95view1',
'ram1991frobenius':'turn80view0 (scanned PDF, no main-result OCR)',
'rohrleulirsch2026bimatroids':'turn62view2; turn63view1; turn100view2',
'smale1967dynamical':'turn80view4',
'speyersturmfels2003tropical':'turn99view1; turn135view0',
'stacks2026foundations':'turn14view0; turn14view1; turn67view1; turn67view2; turn99view2',
'sullivan1985quasiconformal':'turn55view0; turn59view2',
'tarski1951decision':'turn80view1; turn96view1',
'veselovwu2020geodesic':'turn62view0; turn63view0',
'weyman2003syzygies':'turn82view2; turn83view4',
'yoccoz1984conjugaison':'turn82view0'}
assert set(entries)==set(ids)
log=(out/'early_research.md').read_text().split('<!-- GENERATED LEDGER -->')[0]
log+='\n<!-- GENERATED LEDGER -->\n'
for key in sorted(entries):
 e=entries[key];url=field(e,'url') or 'https://doi.org/'+field(e,'doi')
 scope=field(e,'annote').replace('Accessed11November2026','Accessed 11 November 2026').replace('Accessed11November2026.','Accessed 11 November 2026.')
 log+='\n### '+key+'\n\n'+field(e,'title')+'\n\nURL: '+url+'\n\nVerification: **'+field(e,'note')+'**. '+scope+'\n\nObserved retrieval IDs: '+ids[key]+'.\n'
(out/'early_research.md').write_text(log)
required={'id','record','pages','kind','title','notes','statement','reconstruction','class','fate','present_status','literal_correctness','publication_match','verification','development','problem','worth','refs','confidence'}
for item in items:
 assert required<=item.keys() and set(item)-required<={'speaker'},item['id']
 assert item['id'].startswith('1987-'+str(item['record'])+'.')
 for key,value in item.items():
  if isinstance(value,str):
   assert not any(ord(c)<32 for c in value),(item['id'],key,'control')
   if key=='title':assert '\\' not in value,(item['id'],'LaTeX title')
   for cited in re.findall(r'\\cite[pt]?(?:\[[^]]*\])?\{([^}]+)\}',value):
    assert set(cited.split(','))<=set(item['refs']),(item['id'],cited,item['refs'])
 assert set(item['refs'])<=entries.keys()
 assert item['class'] in 'ABCDEF'
 if item['class'] in 'CD':assert item['worth']
for talk in talks:
 for key,value in talk.items():
  if isinstance(value,str):assert not any(ord(c)<32 for c in value),(talk['record'],key)
 assert '\\' not in talk['title']
for record in range(714,727):
 its=[x for x in items if x['record']==record]
 assert [x['id'] for x in its]==[f'1987-{record}.{i}' for i in range(1,len(its)+1)]
assert [x['record'] for x in talks]==[714,715,716,717,719,718,720,721,722,723,724,725,726]
for p in problems:
 assert p['status_date']=='2026-11'
 assert set(p['refs'])<=entries.keys()
 for occ in p['occurrences']:
  if occ.startswith('1987-'):assert any(x['id']==occ and x['problem']==p['id'] for x in items)
record_areas={str(t['record']):sorted({areas[x['id']] for x in items if x['record']==t['record']}) for t in talks}
(out/'early_record_areas.json').write_text(json.dumps(record_areas,ensure_ascii=False,indent=2)+'\n')

# Correction-table body cells are rendered as LaTeX verbatim by the builder.
correction_rows=list(csv.DictReader((out/'early_corrections.csv').open()))
for row in correction_rows:
 for key,value in row.items():
  if key=='type':continue
  assert not any(ord(c)<32 for c in value),(row['page'],key,'control')
  assert value.count(r'\(')==value.count(r'\)'),(row['page'],key,'math delimiters')
  assert value.count(r'\[')==value.count(r'\]'),(row['page'],key,'display delimiters')
  plain=re.sub(r'\\\(.*?\\\)|\\\[.*?\\\]','',value)
  assert not re.search(r'(?<!\\)[_^$&#%]',plain),(row['page'],key,'unescaped LaTeX special',plain)

result={'talks':len(talks),'items':len(items),'problems':len(problems),'references':len(entries),'corrections':len(list(csv.DictReader((out/'early_corrections.csv').open()))),'classes':dict(collections.Counter(x['class'] for x in items)),'records':dict(collections.Counter(x['record'] for x in items)),'control_characters':'none','titles':'plain text','citation_ref_consistency':'pass','correction_latex':'pass'}
(root/'logs/early_schema_audit.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
