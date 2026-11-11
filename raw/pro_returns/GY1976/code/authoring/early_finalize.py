#!/usr/bin/env python3
"""Finalize legible bibliography prose without altering keys, DOI or URLs."""
from pathlib import Path
import runpy,re
root=Path(__file__).resolve().parent
ns=runpy.run_path(str(root/'early_author.py'))
clean=ns['clean_prose']
p=root/'early_references.bib';text=p.read_text();changes=[]
for m in re.finditer(r'\b(title|booktitle|annote)\s*=\s*\{',text):
    start=m.end();level=1;j=start
    while level:
        if text[j]=='{':level+=1
        elif text[j]=='}':level-=1
        j+=1
    value=clean(text[start:j-1])
    value=value.replace('FIANpreprint','FIAN preprint').replace('JETPLetters','JETP Letters').replace('PDGreview','PDG review').replace('Phys.Rev.','Phys. Rev.').replace('Phys.Usp','Phys. Usp').replace('S.Navas','S. Navas')
    for old,new in {'entryR 18':'entry R18','ArXivv 1':'ArXiv v1','sectionsVII':'sections VII','SectionsI--IIIand sectionIVarea-law':'Sections I--III and section IV area-law','issueDecember':'issue December','revisedAugust':'revised August','ReviewD':'Review D','SU(3)application':'SU(3) application','Yu.A.Gol':'Yu. A. Gol','}19':'} 19','}20':'} 20',')read':') read',')equations':') equations'}.items():value=value.replace(old,new)
    if m.group(1)=='annote':
        # The URLs here contain no commas; retain every URL/DOI character exactly.
        value=re.sub(r'(?<=[,;])(?=\S)', ' ',value)
        value=re.sub(r'(?<=\d)(?=\([A-Za-z])', ' ',value)
    changes.append((start,j-1,value))
for a,b,v in reversed(changes):text=text[:a]+v+text[b:]
p.write_text(text.replace('% Records397--405. All links below opened2026-11-10;', '% Records 397--405. All links below opened 2026-11-10;'))
print('Finalized author data and bibliography prose; keys, identifiers, DOI and URLs unchanged.')
