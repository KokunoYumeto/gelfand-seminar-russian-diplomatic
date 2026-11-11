"""Stricter schema, cross-reference, bibliography and coverage audit."""
import csv,json,re,collections
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
TAG='GY1980'
def read(s):return json.loads((ROOT/f'{TAG}_{s}.json').read_text())
talks,items,problems=read('talks'),read('items'),read('problems')
errors=[]
def check(ok,msg):
    if not ok:errors.append(msg)
def cites(s):
    return {key.strip() for group in re.findall(r'\\cite[a-z]*\*?(?:\[[^\]]*\])*\{([^}]+)\}',s)
            for key in group.split(',')}
def strings(o):
    if isinstance(o,str):return [o]
    if isinstance(o,list):return sum((strings(x) for x in o),[])
    if isinstance(o,dict):return sum((strings(x) for x in o.values()),[])
    return []
check(len(talks)==39,'Expected all36 suppliedrecords plus recovered510,511,512')
check({t['record'] for t in talks}==set(range(490,529)),'Record set mismatch')
check(len({t['record'] for t in talks})==len(talks),'Duplicate records')
ids={x['id'] for x in items};pids={p['id'] for p in problems}
check(len(ids)==len(items),'Duplicate item identifiers')
check(len(pids)==len(problems),'Duplicate problem identifiers')
enums={
 'kind':{'definition','construction','theorem','claim','conjecture','question','problem','method','remark'},
 'class':set('ABCDEF'),
 'literal_correctness':{'correct','correct with missing hypotheses','false as written','not determinable'},
 'publication_match':{'exact','partial','thematic only','none found'},
 'verification':{'read the result','publisher metadata checked','indirect','unresolved lead'},
 'development':{'none','annotated','developed in this chapter'},
 'confidence':{'high','medium','low'}}
required={'id','record','pages','kind','title','notes','statement','reconstruction','class','fate','present_status',
          'literal_correctness','publication_match','verification','development','problem','worth','refs','confidence'}
bib=(ROOT/f'{TAG}_references.bib').read_text()
keys=re.findall(r'(?m)^\s*@\w+\s*\{\s*([^,\s]+)\s*,',bib)
check(len(keys)==len(set(keys)),'Duplicate bibliography keys')
keys=set(keys)
previous=(ROOT/'previous_index.md').read_text()
for t in talks:
    check({'record','date','speaker','pages','title','kind','summary'}<=set(t),'Talk fields missing '+str(t.get('record')))
    check(t['kind'] in {'talk','plan','heading','other'},'Bad talk kind '+str(t['record']))
for x in items:
    i=x['id'];check(required<=set(x),'Missing item fields '+i)
    for f,vals in enums.items():check(x.get(f) in vals,'Bad '+f+' '+i)
    check(re.fullmatch(r'1980-'+str(x['record'])+r'\.\d+',i) is not None,'Bad item ID '+i)
    check('2026' in x['present_status'],'Undated status '+i)
    check(set(x['refs'])<=keys,'Unknown ref in '+i)
    check(cites(' '.join(strings(x)))<=set(x['refs']),'Cited work absent from refs '+i+': '+str(cites(' '.join(strings(x)))-set(x['refs'])))
    if x['class'] in 'CD':check(bool(x['worth']),'C/D item without worth '+i)
    if x['problem']:check(x['problem'] in pids,'Unknown problem in '+i)
for t in talks:
    group=[x for x in items if x['record']==t['record']]
    check([x['id'] for x in group]==[f"1980-{t['record']}.{n}" for n in range(1,len(group)+1)],'Nonconsecutive items '+str(t['record']))
for p in problems:
    check(p['status_date']=='2026-11','Bad problem date '+p['id'])
    check(set(p['refs'])<=keys,'Unknown problem ref '+p['id'])
    check(cites(' '.join(strings(p)))<=set(p['refs']),'Cited work absent from problem refs '+p['id'])
    for o in p['occurrences']:
        if o.startswith('1980-'):
            check(o in ids,'Unknown current occurrence '+o)
            if o in ids:check(next(x for x in items if x['id']==o)['problem']==p['id'],'Nonreciprocal problem link '+o)
        else:check(o in previous,'Earlier occurrence absent from supplied index '+o)
for x in items:
    if x['problem'] in pids:
        p=next(p for p in problems if p['id']==x['problem'])
        check(x['id'] in p['occurrences'],'Problem missing occurrence '+x['id'])
with (ROOT/f'{TAG}_corrections.csv').open() as f:rows=list(csv.DictReader(f))
for r in rows:
    check(r['applies_to'] in {'ru','en','both'},'Bad correction language '+r['page'])
    check(r['type'] in {'transcription','translation','ambiguity','faithful_error','provenance'},'Bad correction type '+r['page'])
alltext=' '.join(strings([talks,items,problems,rows]))+(ROOT/f'{TAG}_development.tex').read_text()+(ROOT/f'{TAG}_overview.tex').read_text()
check(cites(alltext)<=keys,'Unknown global citation '+str(cites(alltext)-keys))
for entry in re.split(r'(?m)(?=^\s*@\w+\s*\{)',bib):
    if not entry.strip():continue
    key=re.search(r'@\w+\s*\{\s*([^,]+)',entry).group(1)
    check(bool(re.search(r'\b(?:doi|url)\s*=',entry)),'No URL/DOI '+key)
    check(bool(re.search(r'\bnote\s*=\s*\{(?:verified|unverified)\}',entry)),'No verification tag '+key)
check(not re.search(r'\\(?:chapter|section)\b',(ROOT/f'{TAG}_overview.tex').read_text()),'Forbidden overview heading')

# Page footprint: record boundary P000916 belongs to the earlier year.
coverage=collections.defaultdict(set)
for x in items:
    nums=[int(n) for n in re.findall(r'P0*(\d+)',x['pages'])]
    if len(nums)==2 and re.search(r'[-–]',x['pages']):nums=list(range(min(nums),max(nums)+1))
    for n in nums:coverage[n].add(x['record'])
with (ROOT/'checks/source_page_coverage.csv').open('w',newline='') as f:
    w=csv.writer(f);w.writerow(['page','record_footprints','disposition'])
    for n in range(916,981):
        disposition='Prior-year continuation; see1979-488.1--.7' if n==916 else 'Current-year mathematical material'
        page_records=coverage[n]
        if n==954:
            disposition='Khovanskii heading and bibliography only; mathematical content starts P000955'
            page_records={509}
        w.writerow([f'P{n:06d}',';'.join(map(str,sorted(page_records))),disposition])
        if n not in {916,954}:check(bool(coverage[n]),'Unaccounted current page '+str(n))
print('VALIDATION RECORDS',len(talks),'ITEMS',len(items),'PROBLEMS',len(problems),'REFERENCES',len(keys))
print('CURRENT MATHEMATICAL PAGE COVERAGE',len([p for p in coverage if 917<=p<=980 and coverage[p]]),'/63')
print('ADDITIONAL PAGES ACCOUNTED FOR: P000916 prior-year continuation; P000954 heading/bibliography')
for e in errors:print('ERROR:',e)
print('STRICT VALIDATION', 'PASS' if not errors else 'FAIL')
raise SystemExit(bool(errors))
