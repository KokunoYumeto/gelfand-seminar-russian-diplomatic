"""Read-only schema, reference and editorial validation of this record batch."""
from pathlib import Path
import json,csv,re,collections,unicodedata
p=Path(__file__).resolve().parent
talks=json.loads((p/'talks.json').read_text())
items=json.loads((p/'items.json').read_text())
problems=json.loads((p/'problems.json').read_text())
corrections=list(csv.DictReader((p/'corrections.csv').open()))
bib=(p/'references.bib').read_text()
keys=re.findall(r'@\w+\s*\{\s*([^,\s]+)',bib)
assert len(keys)==len(set(keys))
assert set(x['record'] for x in talks)=={277,278,283,284,294,295,297}
assert len(talks)==7 and len(items)==79 and len(problems)==4
fields={'id','record','pages','kind','title','notes','statement','reconstruction','class','fate','present_status','literal_correctness','publication_match','verification','development','problem','worth','refs','confidence'}
enum={
 'kind':{'definition','construction','theorem','claim','conjecture','question','problem','method','remark'},
 'class':set('ABCDEF'),
 'literal_correctness':{'correct','correct with missing hypotheses','false as written','not determinable'},
 'publication_match':{'exact','partial','thematic only','none found'},
 'verification':{'read the result','publisher metadata checked','indirect','unresolved lead'},
 'development':{'none','annotated','developed in this chapter'},
 'confidence':{'high','medium','low'}
}
ids={x['id'] for x in items};assert len(ids)==len(items)
problemids={x['id'] for x in problems}
for x in items:
 assert fields<=x.keys(),x['id']
 for k,allowed in enum.items():assert x[k] in allowed,(x['id'],k)
 assert x['present_status'].startswith('As of 9 November 2026:'),x['id']
 assert set(x['refs'])<=set(keys),(x['id'],x['refs'])
 assert not x['problem'] or x['problem'] in problemids
 if x['class'] in 'CD':assert x['worth']
for t in talks:
 group=[x for x in items if x['record']==t['record']]
 assert [x['id'] for x in group]==[f"1972-{t['record']}.{i}" for i in range(1,len(group)+1)]
for q in problems:
 assert {'id','title','statement','occurrences','status','status_date','refs'}<=q.keys()
 assert q['status_date']=='2026-11' and set(q['refs'])<=set(keys)
 assert set(q['occurrences'])<=ids
 for iid in q['occurrences']:assert next(x for x in items if x['id']==iid)['problem']==q['id'],iid
for obj in talks+items+problems+corrections:
 for k,v in obj.items():
  if isinstance(v,str):
   assert not any(ord(c)<32 for c in v),(obj.get('id'),k,'control character')
   assert r'\textquotesingle' not in v
   for cite in re.findall(r'\\cite[pt]?\*?(?:\[[^]]*\])*\{([^}]+)\}',v):
    assert set(cite.split(','))<=set(keys),(obj.get('id'),cite)
   assert v.count(r'\(')==v.count(r'\)'),(obj.get('id'),k,'math delimiters')
   assert v.count(r'\[')==v.count(r'\]'),(obj.get('id'),k,'display delimiters')
   # Braces escaped as literal delimiters are excluded.
   b=re.sub(r'\\[{}]','',v)
   assert b.count('{')==b.count('}'),(obj.get('id'),k,'braces')
   if k in {'summary','notes','statement','reconstruction','fate','present_status','status','worth','place','transcription_reads','should_read','evidence'}:
    outside=re.sub(r'\\\(.*?\\\)|\\\[.*?\\\]','',v,flags=re.S)
    assert not re.search(r'(?<!\\)[_^]',outside),(obj.get('id'),k,'bare subscript/superscript')
    bad=[c for c in v if ord(c)>127 and (unicodedata.category(c) in {'Sm','No'} or '\u0370'<=c<='\u03ff')]
    assert not bad,(obj.get('id'),k,'Unicode math',bad)
for c in corrections:
 assert c['applies_to'] in {'en','ru','both'}
 assert c['type'] in {'transcription','translation','ambiguity','faithful_error','provenance',''}
for key in keys:
 start=re.search(r'@\w+\s*\{\s*'+re.escape(key)+',',bib).start()
 end=bib.find('\n}',start)
 entry=bib[start:end]
 assert re.search(r'\b(url|doi)\s*=',entry),key
 assert re.search(r'note\s*=\s*\{verified\}',entry),key
for iid in ['1972-283.1','1972-283.9']:
 assert r'\ours' in next(x for x in items if x['id']==iid)['reconstruction']
print('PASS: complete schema, enums, IDs, reciprocal problem links, dated statuses, citation keys, LaTeX delimiter and prose-control checks.')
print('Talk page spans:',[(t['record'],t['pages']) for t in talks])
print('Items by record:',dict(collections.Counter(x['record'] for x in items)))
print('Items by class:',dict(sorted(collections.Counter(x['class'] for x in items).items())))
print('Problems:',len(problems),'Corrections:',len(corrections),'References:',len(keys))
print('PASS: raw-LaTeX prose contains no bare _/^ outside math or Unicode mathematical glyphs.')
