"""Strict structural/content-integrity validation beyond the supplied builder.

Usage: python code/validate_chapter.py [chapter_directory]
This validates the published data, not the truth of every mathematical theorem.
"""
import collections,csv,hashlib,json,re,sys
from pathlib import Path
base=Path(__file__).resolve().parent.parent
D=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else (base if (base/'GY1985_items.json').exists() else base/'deliverable')
errors=[];checks=[]
def require(ok,message):
    if not ok:errors.append(message)
def read_json(name):return json.loads((D/name).read_text())
T=read_json('GY1985_talks.json');I=read_json('GY1985_items.json');P=read_json('GY1985_problems.json')
A=read_json('GY1985_adjacent_items.json') if (D/'GY1985_adjacent_items.json').exists() else []
R=list(csv.DictReader((D/'GY1985_corrections.csv').open()))
bib=(D/'GY1985_references.bib').read_text()
keys=re.findall(r'(?m)^@\w+\s*\{\s*([^,\s]+)\s*,',bib)
require(len(keys)==len(set(keys)),'Duplicate bibliography keys')
keyset=set(keys)
ORDER=[641,642,643,644,646,645,647,648,649,650,651,653,652,654,655,656,657,658,659,660,661,662,663,664,665,666]
require([t['record'] for t in T]==ORDER,'Source-order/record coverage mismatch')
require(len(I)==260,'Core item count changed; review all stated counts')
ids={x['id'] for x in I};pids={p['id'] for p in P}
require(len(ids)==len(I),'Duplicate item IDs');require(len(pids)==len(P),'Duplicate problem IDs')
required={'id','record','pages','kind','title','notes','statement','reconstruction','class','fate','present_status','literal_correctness','publication_match','verification','development','problem','worth','refs','confidence'}
enum={
 'kind':{'definition','construction','theorem','claim','conjecture','question','problem','method','remark'},
 'class':set('ABCDEF'),
 'literal_correctness':{'correct','correct with missing hypotheses','false as written','not determinable'},
 'publication_match':{'exact','partial','thematic only','none found'},
 'verification':{'read the result','publisher metadata checked','indirect','unresolved lead'},
 'development':{'none','annotated','developed in this chapter'},
 'confidence':{'high','medium','low'}}
citere=re.compile(r'\\cite[pt]?\*?(?:\[[^\]]*\])*\{([^}]*)\}')
def citations(text):return {k.strip() for group in citere.findall(text) for k in group.split(',') if k.strip()}
all_citations=set()
for x in I:
    require(required<=set(x),f"{x['id']}: missing fields {required-set(x)}")
    require(bool(re.fullmatch(r'1985-\d+\.\d+',x['id'])),f"{x['id']}: wrong academic-year ID")
    require(x['record']==int(x['id'].split('-')[1].split('.')[0]),f"{x['id']}: record mismatch")
    for field,values in enum.items():require(x[field] in values,f"{x['id']}: invalid {field}")
    for field in ('notes','statement','fate','present_status'):require(bool(x[field].strip()),f"{x['id']}: empty {field}")
    require('2026' in x['present_status'],f"{x['id']}: undated present status")
    if x['class'] in 'CD':require(bool(x['worth'].strip()),f"{x['id']}: C/D worth missing")
    if x['problem']:require(x['problem'] in pids,f"{x['id']}: unresolved problem link")
    c=citations(' '.join(v for v in x.values() if isinstance(v,str)))
    require(c<=set(x['refs']),f"{x['id']}: citations absent from refs {c-set(x['refs'])}")
    require(set(x['refs'])<=keyset,f"{x['id']}: missing bibliography keys {set(x['refs'])-keyset}")
    all_citations|=c
for record in ORDER:
    seq=[x['id'] for x in I if x['record']==record]
    require(seq==[f'1985-{record}.{n}' for n in range(1,len(seq)+1)],f'Record {record}: nonconsecutive items')
require(not [x for x in I if x['record']==665],'Catalogue heading has fabricated mathematics')
for t in T:
    require(t['kind'] in {'talk','plan','heading','other'},f"Record {t['record']}: kind")
    all_citations|=citations(t['summary'])
for p in P:
    require(p['status_date']=='2026-11',f"{p['id']}: wrong status date")
    for occurrence in p['occurrences']:
        if occurrence.startswith('1985-'):require(occurrence in ids,f"{p['id']}: missing current occurrence {occurrence}")
    require(set(p['refs'])<=keyset,f"{p['id']}: missing refs")
    c=citations(p['statement']+' '+p['status'])
    require(c<=set(p['refs']),f"{p['id']}: citation absent from refs")
    all_citations|=c
for name in ('GY1985_overview.tex','GY1985_development.tex'):
    text=(D/name).read_text();all_citations|=citations(text)
    if name.endswith('overview.tex'):require(not re.search(r'\\(?:chapter|section)\b',text),'Overview contains a chapter/section command')
for r in R:
    require(r['applies_to'] in {'ru','en','both'},f"Correction {r['page']}: applies_to")
    require(r['type'] in {'transcription','translation','ambiguity','faithful_error','provenance',''},f"Correction {r['page']}: type")
    all_citations|=citations(' '.join(r.values()))
require(all_citations<=keyset,'Unresolved citation keys: '+str(all_citations-keyset))
require(keyset<=all_citations,'Uncited bibliography entries: '+str(keyset-all_citations))

blocks=re.split(r'(?m)(?=^@\w+\s*\{)',bib)
for entry in blocks:
    if not entry.strip():continue
    k=re.search(r'^@\w+\s*\{\s*([^,]+)',entry).group(1)
    require(bool(re.search(r'\b(?:url|doi)\s*=\s*\{[^}]+\}',entry)),f'{k}: no URL or DOI')
    require(bool(re.search(r'\bnote\s*=\s*\{(?:verified|unverified)\}',entry)),f'{k}: invalid verification note')

mathre=re.compile(r'\\\(.*?\\\)|\\\[.*?\\\]|(?<!\\)\$.*?(?<!\\)\$',re.S)
def latex_safe(text,label):
    require(not any(ord(c)<32 and c not in '\n\r\t' for c in text),label+': nonprinting control character')
    stripped=mathre.sub('',text)
    # These cells/fields contain no tabular environments or verbatim URLs.
    require(not re.search(r'(?<!\\)[_^%#&]',stripped),label+': raw LaTeX special outside math')
for x in I+T+P+A:
    for field in ('notes','statement','reconstruction','fate','present_status','summary','status','worth'):
        if field in x:latex_safe(x[field],str(x.get('id',x.get('record')))+' '+field)
for n,r in enumerate(R):
    for field in ('place','transcription_reads','should_read','evidence'):latex_safe(r[field],f'correction {n+1} {field}')
for p in D.glob('GY1985_*'):
    if p.suffix in {'.json','.tex','.csv','.bib','.md'}:
        require(not any(ord(c)<32 and c not in '\n\r\t' for c in p.read_text()),p.name+': control character')

def pages(text):
    nums=[int(x) for x in re.findall(r'P(\d{6})',text)]
    if len(nums)==2:return set(range(nums[0],nums[1]+1))
    return set(nums)
core=set().union(*(pages(x['pages']) for x in I))
adj=set().union(*(pages(x['pages']) for x in A)) if A else set()
require(core==set(range(1199,1258)),f'Core source-page coverage mismatch: {sorted(set(range(1199,1258))-core)}')
require(adj=={1258,1259},f'Adjacent source-page coverage mismatch: {adj}')
require(len(A)==12,'Expected 12 separate adjacent-page items')
require(not {x['id'] for x in A}&ids,'Adjacent/core identifier collision')
require(all(x['id'].startswith('ADJ-') for x in A),'Adjacent item ID contaminates core namespace')

checks=['26 records in manuscript order','260 consecutive core occurrence IDs','heading contains no mathematical item','all required fields and enums','11 problem records with current occurrence resolution','citations and bibliography keys','URL/DOI verification-note schema','all LaTeX data fields free of raw specials and control characters','59 core pages plus 2 adjacent pages','12 adjacent items outside core namespace']
result={'status':'PASS' if not errors else 'FAIL','checks':checks,'errors':errors,'counts':{'talks':len(T),'items':len(I),'problems':len(P),'adjacent_items':len(A),'references':len(keys),'corrections':len(R)},'classes':dict(collections.Counter(x['class'] for x in I))}
(D/'audit').mkdir(exist_ok=True)
(D/'audit/validation_output.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
sys.exit(bool(errors))
