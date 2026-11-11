from pathlib import Path
import re,json,unicodedata,difflib,collections
W=Path(__file__).resolve().parents[2]

def parse(path):
    s=path.read_text(); entries=[]
    for m in re.finditer(r'@(\w+)\s*\{\s*([^,\s]+)\s*,',s):
        i=m.end(); fields={}; end=i
        while i<len(s):
            while i<len(s) and s[i] in ' \t\n\r,':i+=1
            if i==len(s) or s[i]=='}':end=i+1;break
            f=re.match(r'([A-Za-z]\w*)\s*=\s*',s[i:])
            if not f:raise ValueError((path,m.group(2),s[i:i+50]))
            key=f.group(1).lower();i+=f.end();start=i
            if s[i]=='{':
                depth=1;i+=1;start=i
                while depth and i<len(s):
                    if s[i]=='{' and s[i-1]!='\\':depth+=1
                    elif s[i]=='}' and s[i-1]!='\\':depth-=1
                    i+=1
                val=s[start:i-1]
            elif s[i]=='"':
                i+=1;start=i
                while i<len(s) and not(s[i]=='"' and s[i-1]!='\\'):i+=1
                val=s[start:i];i+=1
            else:
                while i<len(s) and s[i] not in ',\n}':i+=1
                val=s[start:i].strip()
            fields[key]=val
        entries.append(dict(key=m.group(2),type=m.group(1).lower(),source=str(path),fields=fields,raw=s[m.start():end]))
    return entries

def norm(v):
    v=unicodedata.normalize('NFKD',v).encode('ascii','ignore').decode().lower()
    v=re.sub(r'\\[a-zA-Z]+',' ',v)
    return ''.join(c for c in v if c.isalnum())
def doi(e):return e['fields'].get('doi','').lower().replace('https://doi.org/','').strip()
def simpleurl(e):
    u=e['fields'].get('url','')
    x=re.search(r'(?:mathnet\.ru/(?:eng/)?|paperid=)([a-z]+\d+)',u)
    if x:return x.group(1)
    if 'paperid=' in u:
        j=re.search(r'jrnid=([^&]+)',u);p=re.search(r'paperid=(\d+)',u)
        if j and p:return j.group(1)+p.group(1)
    return u.rstrip('/').lower()

cum=parse(W/'references_cumulative.bib')
current=[]
for part in ['early','middle','late','root']:
    z=parse(W/'parts'/part/'references.bib')
    for e in z:e['part']=part
    current+=z
print('COUNTS',collections.Counter(e['part'] for e in current),'cumulative',len(cum))
allmatches=[]
for a in current:
    matches=[]
    for b in cum:
        samekey=a['key']==b['key']; samedoi=bool(doi(a) and doi(a)==doi(b));sameurl=bool(simpleurl(a) and simpleurl(a)==simpleurl(b))
        na=norm(a['fields'].get('title',''));nb=norm(b['fields'].get('title',''))
        score=difflib.SequenceMatcher(None,na,nb).ratio()
        sameyear=a['fields'].get('year')==b['fields'].get('year')
        if samekey or samedoi or sameurl or (score>.87 and sameyear) or score>.96:
            matches.append(dict(key=b['key'],samekey=samekey,samedoi=samedoi,sameurl=sameurl,score=round(score,3),title=b['fields'].get('title'),doi=doi(b),year=b['fields'].get('year')))
    allmatches.append(dict(key=a['key'],part=a['part'],title=a['fields'].get('title'),doi=doi(a),matches=matches))
    if matches:
        print('MATCH',a['part'],a['key'],json.dumps(matches,ensure_ascii=False))

groups=collections.defaultdict(list)
for e in current:groups[e['key']].append(e)
for k,g in groups.items():
    if len(g)>1:
        print('DUPKEY',k,'parts',[x['part'] for x in g])
        for f in ['title','year','journal','volume','number','pages','doi','url','note']:
            vals={x['part']:x['fields'].get(f,'') for x in g}
            if len(set(vals.values()))>1:print(' DIFF',f,vals)
for i,a in enumerate(current):
    for b in current[i+1:]:
        if a['key']==b['key']:continue
        na=norm(a['fields'].get('title',''));nb=norm(b['fields'].get('title',''))
        score=difflib.SequenceMatcher(None,na,nb).ratio()
        if (doi(a) and doi(a)==doi(b)) or score>.93:
            print('CURRENTALIASES',a['part'],a['key'],b['part'],b['key'],'similarity',score,'same DOI',doi(a)==doi(b))

(W/'parts/middle/bibliography_identity_matches.json').write_text(json.dumps({'current':current,'matches':allmatches},ensure_ascii=False,indent=2))
