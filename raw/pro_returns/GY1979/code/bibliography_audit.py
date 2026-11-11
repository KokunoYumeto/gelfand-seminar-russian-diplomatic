#!/usr/bin/env python3
"""Find probable duplicates and cumulative-key violations for editorial review.

This is a diagnostic, not an automatic rewrite: different editions and versions
can share much of a title. Run with the supplied cumulative bibliography path.
"""
from pathlib import Path
from difflib import SequenceMatcher
import collections
import json
import re
import sys
import unicodedata
from audit_chapter import bib_entries

D=Path(__file__).resolve().parent.parent

def field(entry,name):
    m=re.search(r'\b'+name+r'\s*=\s*([{"])',entry,re.I)
    if not m:return ''
    if m.group(1)=='"':
        return entry[m.end():entry.find('"',m.end())]
    i=m.end();depth=1;j=i
    while j<len(entry) and depth:
        if entry[j]=='{' and entry[j-1]!='\\':depth+=1
        if entry[j]=='}' and entry[j-1]!='\\':depth-=1
        j+=1
    return entry[i:j-1]

def normalize(s):
    s=unicodedata.normalize('NFKD',s).lower()
    s=re.sub(r'\\[a-zA-Z]+','',s)
    return re.sub(r'[^a-z0-9]','',s)

def doi(entry):
    return field(entry,'doi').lower().strip().removeprefix('https://doi.org/')

current=dict(bib_entries((D/'GY1979_references.bib').read_text()))
old_path=Path(sys.argv[1]) if len(sys.argv)>1 else D.parent/'references_cumulative.bib'
old=dict(bib_entries(old_path.read_text())) if old_path.exists() else {}
same_doi=collections.defaultdict(list)
for key,entry in current.items():
    if doi(entry):same_doi[doi(entry)].append(key)
duplicate_doi={d:ks for d,ks in same_doi.items() if len(ks)>1}
matches=[]
for key,entry in current.items():
    if key in old:continue
    title=normalize(field(entry,'title'));dy=field(entry,'year')
    for ok,oe in old.items():
        if doi(entry) and doi(entry)==doi(oe):
            matches.append({'chapter_key':key,'cumulative_key':ok,'match':'identical DOI'});continue
        ot=normalize(field(oe,'title'))
        similarity=SequenceMatcher(None,title,ot).ratio()
        if title and ot and (title==ot or (similarity>=.88 and dy==field(oe,'year'))):
            matches.append({'chapter_key':key,'cumulative_key':ok,'match':'title/year',
                            'similarity':round(similarity,3),
                            'chapter_title':field(entry,'title'),'cumulative_title':field(oe,'title')})
result={'chapter_references':len(current),'cumulative_references':len(old),
        'duplicate_DOIs':duplicate_doi,'possible_cumulative_key_reuse':matches,
        'scope':'Candidates require editorial review; this script does not infer identity from a topic match.'}
(D/'code/bibliography_audit_output.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
