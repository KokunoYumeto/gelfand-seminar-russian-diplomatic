"""Check cumulative-key reuse by DOI and normalized title; report only."""
from pathlib import Path
import re
import unicodedata
ROOT=Path(__file__).resolve().parent

def entries(path):
    s=path.read_text()
    starts=list(re.finditer(r"(?m)^@\w+\s*\{\s*([^,\s]+)\s*,",s))
    result={}
    for j,m in enumerate(starts):
        body=s[m.end():starts[j+1].start() if j+1<len(starts) else len(s)]
        fields={}
        p=0
        while p<len(body):
            z=re.search(r"(\w+)\s*=\s*",body[p:])
            if not z:break
            name=z.group(1).lower();a=p+z.end()
            if a>=len(body):break
            if body[a]=="{":
                d=1;b=a+1
                while b<len(body) and d:
                    if body[b]=="{":d+=1
                    elif body[b]=="}":d-=1
                    b+=1
                fields[name]=body[a+1:b-1];p=b
            elif body[a]=='"':
                b=a+1
                while b<len(body) and (body[b]!='"' or body[b-1]=="\\"):b+=1
                fields[name]=body[a+1:b];p=b+1
            else:
                b=body.find(",",a)
                if b<0:b=len(body)
                fields[name]=body[a:b].strip();p=b+1
        result[m.group(1)]=fields
    return result

def norm(s):
    s=unicodedata.normalize("NFKD",s).lower()
    return re.sub(r"[^a-z0-9]","",s)

def doi(s):return s.lower().strip().removeprefix("https://doi.org/").removeprefix("http://dx.doi.org/")

old=entries(ROOT/"references_cumulative.bib")
bydoi={doi(v["doi"]):k for k,v in old.items() if v.get("doi")}
bytitle={norm(v["title"]):k for k,v in old.items() if v.get("title")}
found=0
for p in sorted((ROOT/"parts").glob("*references.bib")):
    for k,v in entries(p).items():
        match=bydoi.get(doi(v.get("doi",""))) or bytitle.get(norm(v.get("title","")))
        if match and k!=match:
            found+=1;print(f"{p.name}: {k} -> {match} [{v.get('title')}]")
print(f"Potential cumulative-key mismatches: {found}")
