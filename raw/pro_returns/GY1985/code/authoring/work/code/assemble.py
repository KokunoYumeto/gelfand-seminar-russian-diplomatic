"""Merge reviewed research fragments into the seven-file chapter format.

Run from the task workspace: python work/code/assemble.py
The published data can be rebuilt directly with build_chapter.py; this script
also preserves the authoring-stage merge and bibliography-key audit.
"""
import collections,csv,hashlib,json,re,shutil,unicodedata
from pathlib import Path
from format_corrections import format_rows
from format_layout import format_layout

W=Path(__file__).resolve().parent.parent
D=W/'deliverable';D.mkdir(exist_ok=True)
PARTS=['early','strings','virasoro','late']
ORDER=[641,642,643,644,646,645,647,648,649,650,651,653,652,654,655,656,657,658,659,660,661,662,663,664,665,666]

def field(entry,name):
    m=re.search(r'\b'+re.escape(name)+r'\s*=\s*([{"])',entry,re.I)
    if not m:return ''
    start=m.end();delim=m.group(1)
    if delim=='"':return entry[start:entry.find('"',start)]
    depth=1;i=start
    while i<len(entry):
        if entry[i]=='{':depth+=1
        elif entry[i]=='}':
            depth-=1
            if depth==0:return entry[start:i]
        i+=1
    raise ValueError('Unbalanced field '+name)

def parse_bib(text):
    starts=list(re.finditer(r'(?m)^@\w+\s*\{\s*([^,\s]+)\s*,',text))
    return [(m.group(1),text[m.start():starts[i+1].start() if i+1<len(starts) else len(text)].strip()) for i,m in enumerate(starts)]

def norm(t):
    return re.sub(r'[^a-z0-9]','',unicodedata.normalize('NFKD',t).encode('ascii','ignore').decode().lower())

def identity(e):
    doi=field(e,'doi').lower().strip().removeprefix('https://doi.org/')
    return ('doi',doi) if doi else ('title-year',norm(field(e,'title')),field(e,'year'))

cum=json.loads((W/'code/cumulative_keys.json').read_text())
cum_id={};cum_title={}
for key,e in cum.items():
    cum_id.setdefault(identity(e),key)
    cum_title.setdefault((norm(field(e,'title')),field(e,'year')),key)

talks=[];items=[];problems=[];rows=[];bibs=[]
for part in PARTS:
    p=W/part
    talks+=json.loads((p/'talks.json').read_text())
    items+=json.loads((p/'items.json').read_text())
    problems+=json.loads((p/'problems.json').read_text())
    rows+=list(csv.DictReader((p/'corrections.csv').open()))
    bibs += [(key,entry,part) for key,entry in parse_bib((p/'references.bib').read_text())]

# The two date rows repeat the more detailed provenance rows already supplied
# by the integrating review. Keep one account of each date in the main ledger.
adj_corrections=W/'strings/adjacent_corrections.csv'
if adj_corrections.exists():
    for row in csv.DictReader(adj_corrections.open()):
        if row['place'] not in {'ADJ-667 date','ADJ-668 date'}:rows.append(row)
rows=format_rows(rows)
talks,items=format_layout(talks,items)
assert set(t['record'] for t in talks)==set(ORDER) and len(talks)==len(ORDER)
talks.sort(key=lambda t:ORDER.index(t['record']))
items.sort(key=lambda i:(ORDER.index(i['record']),int(i['id'].split('.')[1])))

aliases={};unique={};duplicates=[]
for key,entry,part in bibs:
    canonical=key if key in cum else cum_id.get(identity(entry)) or cum_title.get((norm(field(entry,'title')),field(entry,'year'))) or key
    if canonical!=key:aliases[key]=canonical
    entry=re.sub(r'^(@\w+\s*\{\s*)[^,\s]+',lambda m:m.group(1)+canonical,entry,count=1)
    if canonical in unique:
        # Reuse one entry with the richest current verification annotation.
        old=unique[canonical]
        old_ann=field(old['entry'],'annote')+field(old['entry'],'audit')
        new_ann=field(entry,'annote')+field(entry,'audit')
        duplicates.append({'key':canonical,'parts':[old['part'],part],'same_doi':field(old['entry'],'doi')==field(entry,'doi')})
        if len(new_ann)>len(old_ann):unique[canonical]={'entry':entry,'part':part}
    else:unique[canonical]={'entry':entry,'part':part}

def remap(obj):
    if isinstance(obj,str):
        for old,new in aliases.items():obj=re.sub(r'(?<![A-Za-z0-9_])'+re.escape(old)+r'(?![A-Za-z0-9_])',new,obj)
        return obj
    if isinstance(obj,list):return [remap(x) for x in obj]
    if isinstance(obj,dict):return {k:remap(v) for k,v in obj.items()}
    return obj

talks,items,problems,rows=map(remap,(talks,items,problems,rows))
for name,obj in [('talks',talks),('items',items),('problems',problems)]:
    (D/f'GY1985_{name}.json').write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')

with (D/'GY1985_corrections.csv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=['page','place','transcription_reads','should_read','evidence','applies_to','type'])
    writer.writeheader();writer.writerows(rows)
(D/'GY1985_references.bib').write_text('\n\n'.join(remap(unique[k]['entry']) for k in sorted(unique))+'\n')

development=(W/'virasoro/stacking_development.tex').read_text()+'\n'+(W/'late/checks.tex').read_text()
adj=W/'strings/adjacent.tex'
if adj.exists():development+='\n'+adj.read_text()
(D/'GY1985_development.tex').write_text(remap(development))
(D/'GY1985_overview.tex').write_text(remap((W/'late/overview.tex').read_text()))
if (W/'strings/adjacent_items.json').exists():
    adjacent=remap(json.loads((W/'strings/adjacent_items.json').read_text()))
    (D/'GY1985_adjacent_items.json').write_text(json.dumps(adjacent,ensure_ascii=False,indent=2)+'\n')

for f in ('build_chapter.py','gelfand_companion.sty','CHAPTER_FORMAT.md'):
    shutil.copy2(W/'kit'/f,D/f)

audit=D/'audit';audit.mkdir(exist_ok=True)
(audit/'bibliography_merge.json').write_text(json.dumps({'aliases_to_cumulative':aliases,'duplicate_current_entries':duplicates,'selected_count':len(unique)},ensure_ascii=False,indent=2)+'\n')

primary={641:'M. M. Kapranov',642:'V. I. Arnold',643:'A. V. Zelevinsky',644:'A. V. Zelevinsky',645:'B. L. Feigin',646:'M.-F. Vigneras',647:'I. M. Gelfand',648:'A. A. Beilinson',649:'B. L. Feigin',650:'B. L. Feigin',651:'D. B. Fuchs',652:'D. B. Fuchs',653:'Yu. S. Ryzhikova',654:'Werner Müller',655:'B. L. Feigin',656:'Yu. S. Ryzhikova',657:'B. L. Feigin',658:'A. M. Vershik',659:'B. L. Feigin',660:'B. L. Feigin',661:'A. V. Zelevinsky',662:'B. L. Feigin',663:'S. P. Novikov',664:'V. G. Knizhnik',665:'Catalogue heading',666:'A. A. Beilinson'}
area_groups={
 'Algebraic geometry, twistor constructions, integrable operators':[641,663],
 'Abelian integrals and singularities':[642],
 'Combinatorics and Schubert calculus':[643,661],
 'Representations of local reductive groups':[644,646],
 'Automorphic representations and arithmetic':[648],
 'Spectral geometry and singular elliptic operators':[654],
 'Convex geometry and realization spaces':[647,658],
 'Subspace lattices and representations':[653,656],
 'String geometry, determinant lines, and moduli':[645,649,650,664,666],
 'Virasoro, affine algebras, and boson--fermion constructions':[651,652,655,657,659,660,662]}
area_of={r:name for name,rs in area_groups.items() for r in rs}
assert set(area_of)==set(ORDER)-{665}
statistics={
 'records':len(talks),'items':len(items),'problems':len(problems),'references':len(unique),'corrections':len(rows),
 'by_class':{c:sum(x['class']==c for x in items) for c in 'ABCDEF'},
 'by_record':{str(t['record']):sum(x['record']==t['record'] for x in items) for t in talks},
 'by_primary_speaker':dict(sorted(collections.Counter(primary[x['record']] for x in items).items())),
 'by_area':{a:sum(x['record'] in rs for x in items) for a,rs in area_groups.items()},
 'area_records':area_groups,
 'literal_correctness':dict(collections.Counter(x['literal_correctness'] for x in items)),
 'verification':dict(collections.Counter(x['verification'] for x in items)),
 'correction_type':dict(collections.Counter(r['type'] for r in rows)),
 'talk_kind':dict(collections.Counter(t['kind'] for t in talks)),
 'developed_items':[x['id'] for x in items if x['development']=='developed in this chapter'],
 'adjacent_items':len(json.loads((D/'GY1985_adjacent_items.json').read_text())) if (D/'GY1985_adjacent_items.json').exists() else 0}
(audit/'statistics.json').write_text(json.dumps(statistics,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(statistics,ensure_ascii=False,indent=2))
