"""Read BibTeX entries without changing their TeX; report key reuse and collisions."""
from pathlib import Path
import re
import unicodedata

def entries(text):
    positions=list(re.finditer(r"(?m)^@\w+\s*\{\s*([^,\s]+)\s*,",text))
    return [(m.group(1),text[m.start():positions[i+1].start() if i+1<len(positions) else len(text)].strip()+"\n")
            for i,m in enumerate(positions)]

def field(entry,name):
    m=re.search(r"\b"+re.escape(name)+r"\s*=\s*([{\"])",entry,re.I)
    if not m:return ""
    start=m.end();depth=1;quote=m.group(1)=='"'
    if quote:
        for i in range(start,len(entry)):
            if entry[i]=='"' and entry[i-1]!="\\":return entry[start:i]
    else:
        for i in range(start,len(entry)):
            if entry[i]=="{" and entry[i-1]!="\\":depth+=1
            elif entry[i]=="}" and entry[i-1]!="\\":
                depth-=1
                if depth==0:return entry[start:i]
    return ""

def norm(text):
    text=unicodedata.normalize("NFKD",text).lower()
    return "".join(c for c in text if c.isalnum())

def main():
    root=Path(__file__).resolve().parent
    cumulative=entries((root/"references_cumulative.bib").read_text())
    oldkeys={k for k,_ in cumulative}
    refs=[]
    for folder in sorted((root/"fragments").iterdir()):
        p=folder/"references.bib"
        if p.exists():refs.extend((folder.name,k,e) for k,e in entries(p.read_text()))
    print("Checked current fragments:",len(refs),"entries")
    for owner,key,entry in refs:
        if key in oldkeys:continue
        doi=field(entry,"doi").lower()
        title=norm(field(entry,"title"))
        url=field(entry,"url")
        candidates={k for k,e in cumulative if
                    (doi and doi==field(e,"doi").lower())
                    or (title and title==norm(field(e,"title")))
                    or (url and url==field(e,"url"))}
        if candidates:print("REUSE CANDIDATE",owner,key,sorted(candidates))
    bykey={}
    for owner,key,e in refs:bykey.setdefault(key,[]).append((owner,e))
    for key,values in bykey.items():
        if len(values)>1:
            print("DUPLICATE",key,[o for o,_ in values])
            for name in ["title","year","pages","doi","url"]:
                vals={field(e,name) for _,e in values}
                if len(vals)>1:print(" ",name,vals)
    bywork={}
    for owner,key,e in refs:
        identity=field(e,"doi").lower() or norm(field(e,"title"))
        bywork.setdefault(identity,[]).append((owner,key))
    for identity,values in bywork.items():
        if len({k for _,k in values})>1:
            print("SAME WORK DIFFERENT KEYS",identity,values)

if __name__=="__main__":main()
