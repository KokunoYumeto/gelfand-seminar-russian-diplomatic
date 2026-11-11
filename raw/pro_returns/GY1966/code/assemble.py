"""Assemble the reviewed allocations; preserve catalogue order and audit links.

Run from the archive root: python code/assemble.py
The reviewed JSON/BibTeX/CSV inputs are in code/authoring/. The authoring scripts
are also preserved there. This assembler uses only the Python standard library.
"""
from pathlib import Path
import argparse, collections, csv, hashlib, json, re

HERE=Path(__file__).resolve().parent
OUT=HERE.parent
ap=argparse.ArgumentParser();ap.add_argument('--source',type=Path,default=HERE/'authoring')
args=ap.parse_args();source=args.source.resolve()
allocations=['root','pde','arnold','algebra']
talks=[];items=[];problems=[];corrections=[];bib={};duplicates=[]
for allocation in allocations:
    p=source/allocation
    talks+=json.loads((p/'talks.json').read_text())
    items+=json.loads((p/'items.json').read_text())
    problems+=json.loads((p/'problems.json').read_text())
    corrections+=list(csv.DictReader((p/'corrections.csv').open()))
    text=(p/'references.bib').read_text()
    starts=list(re.finditer(r'(?m)^@\w+\s*\{\s*([^,\s]+)\s*,',text))
    for j,m in enumerate(starts):
        key=m.group(1);entry=text[m.start():starts[j+1].start() if j+1<len(starts) else len(text)].strip()
        if key in bib:
            def doi(s):
                d=re.search(r'\bdoi\s*=\s*\{([^}]+)\}',s,re.I)
                return d.group(1).lower() if d else None
            if doi(entry) and doi(bib[key]) and doi(entry)!=doi(bib[key]):
                raise ValueError('Conflicting DOI for '+key)
            duplicates.append({'key':key,'later_allocation':allocation,'policy':'first verified entry retained'})
        else:bib[key]=entry

talks.sort(key=lambda x:x['record'])
items.sort(key=lambda x:(x['record'],int(x['id'].split('.')[1])))
assert [x['record'] for x in talks]==list(range(92,130))
assert len({x['id'] for x in items})==len(items)

# New problem IDs are consecutive in first-occurrence order. Prior-year IDs persist.
def order(p):
    current=[x for x in p['occurrences'] if x.startswith('1966-')]
    return min((int(x.split('-')[1].split('.')[0]),int(x.split('.')[1])) for x in current)
new=sorted((p for p in problems if p['id'].startswith('GP-1966-')),key=order)
mapping={p['id']:f'GP-1966-{n:02d}' for n,p in enumerate(new,1)}
def replace_ids(v):
    if isinstance(v,str):return re.sub(r'GP-1966-\d+',lambda m:mapping.get(m.group(),m.group()),v)
    if isinstance(v,list):return [replace_ids(x) for x in v]
    if isinstance(v,dict):return {k:replace_ids(x) for k,x in v.items()}
    return v
talks,items,problems,corrections=replace_ids([talks,items,problems,corrections])
# Display long formulae and remove two unbreakable prose constructions.
for x in items:
    if x['id']=='1966-99.8':
        s=x['statement']
        start=s.index(r'\(\mathbb E\sum')
        end=s.index(r'\)',start)
        tail=s[end+2:]
        if tail.startswith(','):
            x['statement']=s[:start]+r'\['+s[start+2:end]+r',\]'+tail[1:]
        else:
            x['statement']=s[:start]+r'\['+s[start+2:end]+r'\]'+tail
    x['reconstruction']=x.get('reconstruction','').replace('density/conjugation factors','density and conjugation factors')
    x['statement']=x['statement'].replace('Under the phase-amplitude hypotheses in item 1966-102.2,','Under the hypotheses of item 1966-102.2,')
    x['statement']=x['statement'].replace('Properly supported classical operators form a filtered algebra:','The properly supported classical operators satisfy')
    x['fate']=x['fate'].replace(r'\S2, especially (2.17)--(2.18)',r'\S2, (2.17)--(2.18)')
    if x['record']==126 and 'Noether--Muskhelishvili formula' in x['notes']:
        x['notes']=x['notes'].replace(r'is \(\operatorname{ind}',r'is \[\operatorname{ind}').replace(r'\arg\det\sigma\).',r'\arg\det\sigma.\]')
for p in problems:
    if p['title']=='Invariant distributions for the three-dimensional Lorentz form':
        p['title']='Invariant distributions for the Lorentz form'
problems.sort(key=lambda p:(0 if not p['id'].startswith('GP-1966-') else 1,order(p)))
for p in problems:
    if p['refs'] and not re.search(r'\\cite[pt]?\{',p['status']):
        p['status']+=' See \\citep{'+','.join(p['refs'])+'}.'

byid={x['id']:x for x in items};byrec={x['record']:x for x in talks}
for x in items:
    assert set(x['refs'])<=set(bib),(x['id'],set(x['refs'])-set(bib))
    if x['class'] in 'CD':assert x.get('worth'),x['id']
for p in problems:
    assert set(p['refs'])<=set(bib),p['id']
    for i in p['occurrences']:
        if i.startswith('1966-'):assert i in byid,(p['id'],i)
for x in items:
    if x.get('problem'):
        p=next(p for p in problems if p['id']==x['problem'])
        assert x['id'] in p['occurrences'],x['id']

for name,data in [('talks',talks),('items',items),('problems',problems)]:
    (OUT/f'GY1966_{name}.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
with (OUT/'GY1966_corrections.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['page','place','transcription_reads','should_read','evidence','applies_to','type']);w.writeheader();w.writerows(corrections)
(OUT/'GY1966_references.bib').write_text('\n\n'.join(bib.values())+'\n')

def area(x):
    r=x['record'];n=int(x['id'].split('.')[1])
    if r in [93,101,109,119,121,122,123,125]:return 'Lie groups, representations and algebraic quotients'
    if r in [92,115,116] or r==124 and n<=5:return 'Topology and singularity theory'
    if r==94:return 'Dynamical systems'
    if r==95:return 'Functional analysis and infinite-dimensional equations'
    if r in [97,98,103,104,105,111,112,120,126,127] or r==114 and n==1:return 'K-theory, index theory and elliptic/PDO analysis'
    if r in [96,110,113,129]:return 'Hyperbolic, fluid and heat equations'
    if r in [99,100,106,107]:return 'Statistical mechanics and probability'
    if r==108 or r==124 and n>=6:return 'Symplectic, Maslov and semiclassical analysis'
    if r==102:return 'Sturm-Liouville theory and special functions'
    if r==114:return 'Differential geometry'
    raise ValueError(x['id'])

classes=collections.Counter(x['class'] for x in items)
areas=collections.Counter(area(x) for x in items)
speakers=collections.Counter(byrec[x['record']]['speaker'] for x in items)
verification=collections.Counter(x['verification'] for x in items)
literal=collections.Counter(x['literal_correctness'] for x in items)
matches=collections.Counter(x['publication_match'] for x in items)
correction_types=collections.Counter(x['type'] for x in corrections)
record_rows=[]
for t in talks:
    a=[x for x in items if x['record']==t['record']];c=collections.Counter(x['class'] for x in a)
    record_rows.append({'record':t['record'],'speaker':t['speaker'],'kind':t.get('kind','talk'),'items':len(a),**{k:c[k] for k in 'ABCDEF'}})

def page_numbers(s):
    result=set()
    ranges=list(re.finditer(r'P(\d{6})\s*[-–]+\s*P?(\d{6})',s))
    for m in ranges:result.update(range(int(m.group(1)),int(m.group(2))+1))
    result.update(int(n) for n in re.findall(r'P(\d{6})',s))
    return result
coverage=[]
for page in range(140,208):
    a=[x for x in items if page in page_numbers(x['pages'])]
    coverage.append({'page':f'P{page:06d}','items':'; '.join(x['id'] for x in a),
                     'records':'; '.join(str(r) for r in sorted({x['record'] for x in a})),
                     'scan_review':'visually inspected; allocation findings record decisive readings'})
with (HERE/'source_page_coverage.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['page','items','records','scan_review']);w.writeheader();w.writerows(coverage)
stats={'status_date':'2026-11-09','records':len(talks),'items':len(items),'problems':len(problems),
       'new_problems':len(new),'references':len(bib),'corrections':len(corrections),
       'classes':{k:classes[k] for k in 'ABCDEF'},'speakers':dict(speakers),'areas':dict(areas),
       'verification':dict(verification),'literal_correctness':dict(literal),'publication_match':dict(matches),
       'correction_types':dict(correction_types),'records_detail':record_rows,
       'problem_id_map':mapping,'duplicate_references':duplicates,
       'pages_without_item_occurrence':[x['page'] for x in coverage if not x['items']],
       'C_items':[x['id'] for x in items if x['class']=='C']}
(HERE/'audit_counts.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2)+'\n')
(HERE/'item_areas.json').write_text(json.dumps({x['id']:area(x) for x in items},indent=2)+'\n')

def table(counter,label):
    return '\n'.join([f'| {label} | Items |','|---|---:|']+[f'| {k} | {v} |' for k,v in counter.items()]+[f'| **Total** | **{sum(counter.values())}** |'])
tokens={'@@ITEMS@@':str(len(items)),'@@RECORDS@@':str(len(talks)),'@@PROBLEMS@@':str(len(problems)),
        '@@NEWPROBLEMS@@':str(len(new)),'@@REFERENCES@@':str(len(bib)),'@@CORRECTIONS@@':str(len(corrections)),
        '@@CLASS_TEX@@':' & '.join(str(classes[k]) for k in 'ABCDEF'),
        '@@CLASS_TABLE@@':table({k:classes[k] for k in 'ABCDEF'},'Class'),
        '@@SPEAKER_TABLE@@':table(speakers,'Catalogue speaker'),
        '@@AREA_TABLE@@':table(areas,'Primary area'),
        '@@VERIFICATION_TABLE@@':table(verification,'Verification'),
        '@@LITERAL_TABLE@@':table(literal,'Literal correctness'),
        '@@MATCH_TABLE@@':table(matches,'Publication match'),
        '@@CORRECTION_TABLE@@':table(correction_types,'Correction type'),
        '@@RECORD_TABLE@@':'\n'.join(['| Record | Catalogue speaker | Kind | Items | A | B | C | D | E | F |','|---:|---|---|---:|---:|---:|---:|---:|---:|---:|']+[f"| {r['record']} | {r['speaker'] or '—'} | {r['kind']} | {r['items']} | "+' | '.join(str(r[k]) for k in 'ABCDEF')+' |' for r in record_rows])}
for template,dest in [('overview.template.tex','GY1966_overview.tex'),('report.template.md','GY1966_report.md')]:
    if (HERE/template).exists():
        t=(HERE/template).read_text()
        for k,v in tokens.items():t=t.replace(k,v)
        assert '@@' not in t,template
        (OUT/dest).write_text(t)
print(json.dumps({k:stats[k] for k in ['records','items','problems','references','corrections','classes','C_items','pages_without_item_occurrence']},indent=2))
