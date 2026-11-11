"""Assemble audited research fragments; retain canonical source data as output.

Usage in the working workspace:
  python work/code/assemble_fragments.py work/parts delivery/GY1977 work
The last argument contains the supplied cumulative bibliography and kit.
This script performs no network requests and never modifies input fragments.
"""
from pathlib import Path
from collections import Counter
import csv,json,re,shutil,sys

PARTS=Path(sys.argv[1]);OUT=Path(sys.argv[2]);SUPPLIED=Path(sys.argv[3])
OUT.mkdir(parents=True,exist_ok=True)
ORDER=list(range(419,437))+list(range(438,446))+[451,457]
FIELDS=['page','place','transcription_reads','should_read','evidence','applies_to','type']

def bib_entries(text):
    result=[]
    for m in re.finditer(r'(?m)^\s*@([A-Za-z]+)\s*\{\s*([^,\s]+)\s*,',text):
        i=m.end();depth=1
        while depth and i<len(text):
            if text[i]=='{':depth+=1
            elif text[i]=='}':depth-=1
            i+=1
        if depth:raise ValueError('Unbalanced BibTeX entry '+m.group(2))
        result.append((m.group(2),text[m.start():i].strip()))
    return result

def field(entry,name):
    m=re.search(r'\b'+name+r'\s*=\s*\{',entry,re.I)
    if not m:return ''
    i=m.end();start=i;depth=1
    while depth and i<len(entry):
        if entry[i]=='{':depth+=1
        elif entry[i]=='}':depth-=1
        i+=1
    return entry[start:i-1].strip()

def normdoi(entry):
    return re.sub(r'^https?://(?:dx\.)?doi.org/','',field(entry,'doi').lower()).rstrip('.')

old={};old_doi={}
for k,e in bib_entries((SUPPLIED/'references_cumulative.bib').read_text()):
    old.setdefault(k,e)
    if normdoi(e):old_doi.setdefault(normdoi(e),k)

talks=[];items=[];problems=[];corrections=[];areas={};entries=[];audit=[]
for name in ['early','middle','late','root']:
    p=PARTS/name
    for filename,target in [('talks.json',talks),('items.json',items),('problems.json',problems),('references.json',audit)]:
        if (p/filename).exists():
            data=json.loads((p/filename).read_text())
            if isinstance(data,list):target.extend(data)
            elif filename=='references.json':target.extend([dict(key=k,**v) if isinstance(v,dict) else {'key':k,'evidence':v} for k,v in data.items()])
            else:raise TypeError(str(p/filename))
    if (p/'areas.json').exists():areas.update(json.loads((p/'areas.json').read_text()))
    if (p/'references.bib').exists():entries.extend(bib_entries((p/'references.bib').read_text()))
    if (p/'corrections.csv').exists():
        with (p/'corrections.csv').open(newline='') as f:corrections.extend(csv.DictReader(f))

assert sorted(t['record'] for t in talks)==sorted(ORDER),'Expected exactly the 28 requested catalogue records.'
talks.sort(key=lambda x:ORDER.index(x['record']))
items.sort(key=lambda x:(ORDER.index(x['record']),int(x['id'].split('.')[-1])))
# Dates identify the supplied catalogue envelopes; observed dates are retained
# and explained in summaries and provenance corrections. This is essential
# for the explicitly adjacent 1978–79 material in the requested page packet.
catalogue_dates={419:'1977-09-05',420:'1977-09-05',421:'1977-09-12',422:'1977-09-19',
423:'1977-09-19',424:'1977-09-19',425:'1977-09-19',426:'1977-10-03',427:'1977-09-19',
428:'1977-10-03',429:'1977-10-10',430:'1977-10-24',431:'1977-10-24',432:'1977-10-31',
433:'1977-11-15',434:'1977-11-15',435:'1977-09-21',436:'1977-11-28',438:'1978-02-27',
439:'1978-03-06',440:'1978-03-13',441:'1978-03-20',442:'1978-03-20',443:'1978-03-27',
444:'1978-04-04',445:'',451:'',457:'1978-03-05'}
for t in talks:t['date']=catalogue_dates[t['record']]

keymap={};bib={};bib_rendering_changes=[]
for k,e in entries:
    canonical=k if k in old else old_doi.get(normdoi(e),k)
    keymap[k]=canonical
    e=re.sub(r'(@\w+\s*\{\s*)'+re.escape(k)+r'(?=\s*,)',lambda m:m.group(1)+canonical,e,count=1)
    if field(e,'eid') and not field(e,'pages'):
        article=field(e,'eid')
        prefix=e[:e.rfind('}')].rstrip().rstrip(',')
        e=prefix+',\n pages = {Article~'+article+'}\n}'
        bib_rendering_changes.append({'key':canonical,'change':'Retained eid and added pages={Article~'+article+'} for plainnat article-number rendering.'})
    if canonical in bib:
        a,b=normdoi(bib[canonical]),normdoi(e)
        if a and b and a!=b:raise ValueError('Conflicting bibliography DOI for '+canonical)
    else:bib[canonical]=e

newprobs=sorted([p for p in problems if p['id'].startswith('GP-1977-')],
    key=lambda p:min((ORDER.index(int(o.split('-')[1].split('.')[0])),int(o.split('.')[-1])) for o in p['occurrences'] if o.startswith('1977-')))
pidmap={p['id']:f'GP-1977-{i:02d}' for i,p in enumerate(newprobs,1)}

def replace_cites(text):
    def change(m):
        return m.group(1)+','.join(keymap.get(k.strip(),k.strip()) for k in m.group(2).split(','))+'}'
    text=re.sub(r'(\\cite[pt]?\*?(?:\[[^\]]*\])*\{)([^}]+)\}',change,text)
    if pidmap:
        pattern=r'(?<![A-Za-z0-9-])(?:'+'|'.join(re.escape(k) for k in pidmap)+r')(?![0-9])'
        text=re.sub(pattern,lambda m:pidmap[m.group()],text)
    return text

def transform(obj):
    if isinstance(obj,list):return [transform(x) for x in obj]
    if isinstance(obj,dict):
        return {k:(list(dict.fromkeys(keymap.get(x,x) for x in v)) if k=='refs' else transform(v)) for k,v in obj.items()}
    if isinstance(obj,str):
        if obj in pidmap:return pidmap[obj]
        return replace_cites(obj)
    return obj

talks,items,problems,corrections=map(transform,[talks,items,problems,corrections])
for a in audit:
    if a.get('key') in keymap:
        original=a['key'];a['key']=keymap[original]
        if a['key']!=original:a['original_key']=original
problems.sort(key=lambda p:min((int(o.split('-')[0]),int(o.split('-')[1].split('.')[0]),int(o.split('.')[-1])) for o in p['occurrences']))
for name,data in [('talks',talks),('items',items),('problems',problems)]:
    (OUT/f'GY1977_{name}.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')

seen=set();unique=[]
for c in corrections:
    c={k:str(c.get(k,'') or '') for k in FIELDS}
    key=tuple(c[k] for k in FIELDS)
    if key not in seen:unique.append(c);seen.add(key)
unique.sort(key=lambda x:(x['page'],x['place']))
with (OUT/'GY1977_corrections.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=FIELDS);w.writeheader();w.writerows(unique)

dev='\n\n'.join((PARTS/n/'development.tex').read_text() for n in ['root','early','middle','late'] if (PARTS/n/'development.tex').exists())
(OUT/'GY1977_development.tex').write_text(replace_cites(dev))
overview=PARTS/'root/overview.tex'
if overview.exists():(OUT/'GY1977_overview.tex').write_text(replace_cites(overview.read_text()))

alltext='\n'.join([json.dumps(talks),json.dumps(items),json.dumps(problems),dev]).replace('\\\\','\\')
refkeys=set(k for i in items+problems for k in i.get('refs',[]))
for cited in re.findall(r'\\cite[pt]?\*?(?:\[[^\]]*\])*\{([^}]+)\}',replace_cites(alltext)):
    refkeys.update(k.strip() for k in cited.split(','))
if overview.exists():
    for cited in re.findall(r'\\cite[pt]?\*?(?:\[[^\]]*\])*\{([^}]+)\}',replace_cites(overview.read_text())):refkeys.update(k.strip() for k in cited.split(','))
missing=refkeys-bib.keys()
if missing:raise ValueError('Cited bibliography entries missing: '+','.join(sorted(missing)))
(OUT/'GY1977_references.bib').write_text('\n\n'.join(bib[k] for k in sorted(bib))+'\n')

record_speaker={t['record']:t['speaker'] or '(catalogue heading / adjacent material)' for t in talks}
def primary_area(i):
    r=i['record'];n=int(i['id'].split('.')[-1]);title=i['title'].lower()
    if r in [419,423,432,435]:return 'Gauge theory and twistor geometry'
    if r in [420,426,431,434,436,443]:return 'Integrable systems and spectral theory'
    if r==421:return 'Arithmetic groups and rigidity'
    if r in [424,445]:return 'Combinatorics, information, and foundations'
    if r==425:return 'Statistical physics, gravitation, and cosmology'
    if r==427:return 'Seminar method and unidentified remarks'
    if r in [428,429,430]:return 'Representation theory'
    if r==433:return 'Complex and operator analysis'
    if r in [438,440]:return 'Algebraic geometry, arrangements, and homological algebra'
    if r==439:
        return 'Algebraic geometry, arrangements, and homological algebra' if n==1 else 'Integrable systems and spectral theory'
    if r in [441,444]:return 'Topology and Lie algebra cohomology'
    if r==442:return 'Microlocal analysis and differential geometry' if n>=8 else 'Integrable systems and spectral theory'
    if r==451:
        return 'Gauge theory and twistor geometry' if any(w in title for w in ['instanton','adhm','belavin','self-dual','gauge']) else 'Representation theory'
    if r==457:
        who=(i.get('speaker','')+' '+title).lower()
        if 'ogievetsky' in who or 'super' in title:return 'Supersymmetry and quantum field theory'
        if 'beilinson' in who or 'incidence' in title:return 'Microlocal analysis and differential geometry'
        return 'Topology and Lie algebra cohomology'
    return areas.get(i['id'],'UNASSIGNED')
def speaker_label(i):
    if not i.get('speaker') and i['record']==457:return 'D. B. Fuchs'
    if not i.get('speaker') and i['record']==451:return 'Unidentified preceding lecturer'
    who=i.get('speaker') or record_speaker[i['record']]
    aliases={'F. Calogero and A. Degasperis':'F. Calogero / A. Degasperis',
             'F. Calogero, jointly with A. Degasperis':'F. Calogero / A. Degasperis',
             'V. M. Buchstaber, with A. V. Shokurov':'V. M. Buchstaber / A. V. Shokurov',
             'D. B. Fuchs, with I. M. Gelfand':'D. B. Fuchs / I. M. Gelfand',
             'M. D. Kruskal (adjacent lecture)':'M. D. Kruskal',
             'V. P. Palamodov (Mathematical Society, 21 March 1978)':'V. P. Palamodov'}
    return aliases.get(who,who)
raw_areas=areas.copy()
areas={i['id']:primary_area(i) for i in items}
stats={'records':len(talks),'items':len(items),'problems':len(problems),'references':len(bib),'corrections':len(unique),
       'by_class':{k:sum(i['class']==k for i in items) for k in 'ABCDEF'},
       'by_speaker':dict(sorted(Counter(speaker_label(i) for i in items).items())),
       'by_area':dict(sorted(Counter(areas.get(i['id'],'UNASSIGNED') for i in items).items())),
       'by_record':{str(t['record']):sum(i['record']==t['record'] for i in items) for t in talks},
       'by_verification':dict(sorted(Counter(i['verification'] for i in items).items())),
       'by_literal_correctness':dict(sorted(Counter(i['literal_correctness'] for i in items).items())),
       'by_publication_match':dict(sorted(Counter(i['publication_match'] for i in items).items())),
       'by_correction_type':dict(sorted(Counter(c['type'] for c in unique).items())),
       'adjacent_1978_79_items':sum(i['record'] in [445,451,457] for i in items),
       'substantive_requested_year_items':sum(i['record'] not in [445,451,457] for i in items),
       'new_problem_id_map':pidmap,'bibliography_key_map':{k:v for k,v in keymap.items() if k!=v},
       'bibliography_rendering_changes':bib_rendering_changes}
codeout=OUT/'code/output';codeout.mkdir(parents=True,exist_ok=True)
(codeout/'chapter_counts.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2)+'\n')
(codeout/'reference_audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
(codeout/'areas.json').write_text(json.dumps(areas,ensure_ascii=False,indent=2)+'\n')
(codeout/'areas_original_labels.json').write_text(json.dumps(raw_areas,ensure_ascii=False,indent=2)+'\n')
for name in ['build_chapter.py','gelfand_companion.sty','CHAPTER_FORMAT.md']:
    shutil.copy2(SUPPLIED/'kit'/name,OUT/name)
print(json.dumps(stats,ensure_ascii=False,indent=2))
