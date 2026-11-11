"""Integrate audited record batches, reuse existing bibliography keys, validate.

Run from the chapter directory: python code/integrate.py
The supplied cumulative bibliography and earlier index are read-only inputs.
The seven chapter files are authoritative after integration and final review.
"""
import collections,csv,json,re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PARTS=ROOT/'parts'
TAG='GY1980'
BATCHES=('autumn','winter','root','spring')

def readjson(p): return json.loads(p.read_text(encoding='utf-8'))
def writejson(p,obj): p.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def bib_entries(text):
    out=[]
    for m in re.finditer(r'(?m)^\s*@([A-Za-z]+)\s*\{\s*([^,\s]+)\s*,',text):
        start=text.index('{',m.start());depth=0
        for end in range(start,len(text)):
            c=text[end]
            if c=='{': depth+=1
            elif c=='}': depth-=1
            if depth==0: break
        else: raise ValueError('Unbalanced bibliography entry '+m.group(2))
        out.append((m.group(2),text[m.start():end+1].strip()))
    return out

def field(entry,name):
    m=re.search(r'(?i)\b'+re.escape(name)+r'\s*=\s*([{"])',entry)
    if not m:return ''
    start=m.end();end=start;depth=1
    if m.group(1)=='"':
        while end<len(entry) and entry[end]!='"':end+=1
    else:
        while end<len(entry) and depth:
            if entry[end]=='{':depth+=1
            if entry[end]=='}':depth-=1
            end+=1
        end-=1
    return entry[start:end]

def norm(s):return re.sub('[^a-z0-9]','',s.lower())
def doi(entry):return field(entry,'doi').lower().strip().removeprefix('https://doi.org/')
def citekeys(text):
    keys=[]
    for m in re.finditer(r'\\(?:cite[a-z]*|nocite)\*?(?:\[[^\]]*\])*\{([^}]+)\}',text):
        keys.extend(k.strip() for k in m.group(1).split(',') if k.strip()!='*')
    return set(keys)

talks=[];items=[];problems=[];corrections=[];areas={}
for batch in BATCHES:
    for suffix,target in [('talks',talks),('items',items),('problems',problems)]:
        target.extend(readjson(PARTS/f'{batch}_{suffix}.json'))
    with (PARTS/f'{batch}_corrections.csv').open(encoding='utf-8') as f:
        corrections.extend(csv.DictReader(f))
    areas.update(readjson(PARTS/f'{batch}_areas.json'))

cumulative={};duplicate_keys=collections.Counter()
for key,entry in bib_entries((ROOT/'references_cumulative.bib').read_text()):
    if key in cumulative:duplicate_keys[key]+=1
    else:cumulative[key]=entry
current={}
for batch in BATCHES:
    path=PARTS/f'{batch}_references.bib'
    if not path.exists():raise FileNotFoundError(path)
    for key,entry in bib_entries(path.read_text()):
        if key in current and current[key]!=entry:
            print('BIBLIOGRAPHY REPEATED CURRENT KEY (first retained):',key)
        else:current[key]=entry

bydoi={};bytitle={}
for key,entry in cumulative.items():
    if doi(entry):bydoi.setdefault(doi(entry),key)
    title=norm(field(entry,'title'))
    if len(title)>25:bytitle.setdefault((title,field(entry,'year')),key)
aliases={}
for key,entry in current.items():
    if key in cumulative:continue
    same=bydoi.get(doi(entry)) if doi(entry) else None
    same=same or bytitle.get((norm(field(entry,'title')),field(entry,'year')))
    if same and same!=key:aliases[key]=same

def replacekeys(obj):
    if isinstance(obj,str):
        for old,new in aliases.items():
            obj=re.sub(r'(?<![A-Za-z0-9_])'+re.escape(old)+r'(?![A-Za-z0-9_])',new,obj)
        return obj
    if isinstance(obj,list):return [replacekeys(v) for v in obj]
    if isinstance(obj,dict):return {k:replacekeys(v) for k,v in obj.items()}
    return obj
talks,items,problems,corrections=[replacekeys(v) for v in [talks,items,problems,corrections]]
for filename in [f'{TAG}_development.tex',f'{TAG}_overview.tex']:
    p=ROOT/filename
    if p.exists():p.write_text(replacekeys(p.read_text()),encoding='utf-8')

# First appearance in the manuscript, including Gelfand's introductions.
order=[490,491,492,493,494,495,497,496,499,498,500,501,502,503,504,505,
       506,507,508,509,511,510,512,513,514,515,516,517,518,519,520,521,
       522,523,524,525,526,527,528]
order_path=PARTS/'source_record_order.json'
if order_path.exists():order=readjson(order_path)
rank={r:i for i,r in enumerate(order)}
talks.sort(key=lambda t:rank[t['record']])
items.sort(key=lambda x:(rank[x['record']],int(x['id'].rsplit('.',1)[1])))

# A recurring problem may be reported by two batches; merge occurrences and refs.
merged={}
for p in problems:
    if p['id'] not in merged:merged[p['id']]=p
    else:
        old=merged[p['id']]
        old['occurrences']=list(dict.fromkeys(old['occurrences']+p['occurrences']))
        old['refs']=list(dict.fromkeys(old['refs']+p['refs']))
        if old['statement']!=p['statement'] or old['status']!=p['status']:
            raise ValueError('Manual problem reconciliation required for '+p['id'])
problems=list(merged.values())
problems.sort(key=lambda p:p['id'])

corrections.sort(key=lambda r:(int(re.search(r'P0*(\d+)',r['page']).group(1))
                              if re.search(r'P0*(\d+)',r['page']) else 0,r['place']))
for suffix,obj in [('talks',talks),('items',items),('problems',problems)]:
    writejson(ROOT/f'{TAG}_{suffix}.json',obj)
with (ROOT/f'{TAG}_corrections.csv').open('w',newline='',encoding='utf-8') as f:
    writer=csv.DictWriter(f,fieldnames=['page','place','transcription_reads','should_read','evidence','applies_to','type'])
    writer.writeheader();writer.writerows(corrections)

needed={'mccme2026gelfand'}
for x in items+problems:needed.update(x['refs'])
text=json.dumps([talks,items,problems,corrections],ensure_ascii=False).replace('\\\\','\\')
for filename in [f'{TAG}_development.tex',f'{TAG}_overview.tex']:
    p=ROOT/filename
    if p.exists():text+='\n'+p.read_text()
needed.update(citekeys(text))
pool=dict(cumulative)
for key,entry in current.items():
    canonical=aliases.get(key,key)
    if key==canonical:pool[key]=entry
refs={key:pool[key] for key in sorted(needed)}
(ROOT/f'{TAG}_references.bib').write_text('\n\n'.join(refs.values())+'\n',encoding='utf-8')
writejson(ROOT/'checks/bibliography_key_reuse.json',aliases)
writejson(ROOT/'checks/item_areas.json',areas)

counts={
 'records':len(talks),'items':len(items),'problems':len(problems),'references':len(refs),'corrections':len(corrections),
 'classes':dict(sorted(collections.Counter(x['class'] for x in items).items())),
 'verification':dict(sorted(collections.Counter(x['verification'] for x in items).items())),
 'literal_correctness':dict(sorted(collections.Counter(x['literal_correctness'] for x in items).items())),
 'publication_match':dict(sorted(collections.Counter(x['publication_match'] for x in items).items())),
 'confidence':dict(sorted(collections.Counter(x['confidence'] for x in items).items())),
 'correction_types':dict(sorted(collections.Counter(x['type'] for x in corrections).items()))}
talkmap={t['record']:t for t in talks}
counts['speakers']=dict(sorted(collections.Counter((x.get('speaker') or talkmap[x['record']]['speaker']).split(' (')[0] for x in items).items()))
counts['areas']=dict(sorted(collections.Counter(areas[x['id']] for x in items).items()))
writejson(ROOT/'checks/counts.json',counts)
print('CUMULATIVE DUPLICATE-KEY OCCURRENCES:',sum(duplicate_keys.values()))
print('REUSED KEYS:',json.dumps(aliases,sort_keys=True))
print(json.dumps(counts,ensure_ascii=False,indent=2))
