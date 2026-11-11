#!/usr/bin/env python3
"""Compare final citation identities with the supplied cumulative bibliography."""
import json,re,sys,unicodedata
from collections import defaultdict
from pathlib import Path
from integrate_and_audit import bib_entries,bib_field

base=Path(sys.argv[1] if len(sys.argv)>1 else '.').resolve()
out=base/'output'
old=bib_entries((base/'references_cumulative.bib').read_text())
new=bib_entries((out/'GY1987_references.bib').read_text())
bydoi=defaultdict(set);bytitle=defaultdict(set)
def norm(s):
    s=unicodedata.normalize('NFKD',s).casefold()
    return re.sub('[^a-z0-9]','',s)
def doi(raw):return re.sub(r'https?://(?:dx\.)?doi\.org/','',bib_field(raw,'doi').lower()).strip()
for key,raw in old:
    if doi(raw):bydoi[doi(raw)].add(key)
    bytitle[(norm(bib_field(raw,'title')),bib_field(raw,'year'))].add(key)
issues=[];matches=[]
for key,raw in new:
    candidates=bydoi.get(doi(raw),set())|bytitle.get((norm(bib_field(raw,'title')),bib_field(raw,'year')),set())
    if candidates and key not in candidates:
        issues.append({'new_key':key,'existing_keys':sorted(candidates),'title':bib_field(raw,'title'),
                       'doi':doi(raw)})
    elif candidates:matches.append({'key':key,'existing_keys':sorted(candidates)})
result={'status':'PASS' if not issues else 'REVIEW','same_work_different_key_candidates':issues,
        'reused_key_matches':matches,'new_entries':len(new),'cumulative_entries_including_duplicates':len(old)}
(out/'logs'/'reference_identity_audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
