#!/usr/bin/env python3
"""Merge the independently researched source-order batches without changing IDs.

Run after the three batches are complete. Inputs are ../parts/{early,middle,late}
in the working workspace, or code/authoring/{early,middle,late} in the ZIP.
Editorial adjustments after merging are recorded in code/editorial_changes.json.
"""
from pathlib import Path
import csv
import json
import shutil
from audit_chapter import bib_entries

D=Path(__file__).resolve().parent.parent
PARTS=D.parent/'parts'
if not PARTS.exists():
    PARTS=D/'code/authoring'
names=['early','middle','late']
talks=[]
items=[]
problems={}
corrections=[]
references={}
conflicts=[]

for name in names:
    folder=PARTS/name
    talks.extend(json.loads((folder/'talks.json').read_text()))
    items.extend(json.loads((folder/'items.json').read_text()))
    for p in json.loads((folder/'problems.json').read_text()):
        key=p['id']
        if key in problems:
            old=problems[key]
            old['occurrences']=list(dict.fromkeys(old['occurrences']+p['occurrences']))
            old['refs']=list(dict.fromkeys(old['refs']+p['refs']))
            if old['statement']!=p['statement']:
                old['statement']+='\n\n'+p['statement']
            if old['status']!=p['status']:
                old['status']+='\n\n'+p['status']
        else:
            problems[key]=p
    corrections.extend(csv.DictReader((folder/'corrections.csv').open()))
    for key,entry in bib_entries((folder/'references.bib').read_text()):
        if key in references and references[key]!=entry:
            conflicts.append({'key':key,'later_batch':name,
                              'kept':references[key],'alternative':entry})
        else:
            references[key]=entry

for key,entry in bib_entries((D/'root_references.bib').read_text()):
    if key in references and references[key]!=entry:
        conflicts.append({'key':key,'later_batch':'root','kept':entry,
                          'alternative':references[key]})
    references[key]=entry

order=list(range(462,476))+[477,476]+list(range(478,489))
rank={rec:i for i,rec in enumerate(order)}
talks.sort(key=lambda t:rank[t['record']])
items.sort(key=lambda x:(rank[x['record']],int(x['id'].split('.')[-1])))
for p in problems.values():
    p['occurrences']=sorted(set(p['occurrences']),key=lambda x:tuple(map(int,x.replace('.','-').split('-'))))
corrections.sort(key=lambda c:(c['page'],c['place']))

for suffix,data in [('talks',talks),('items',items),('problems',list(problems.values()))]:
    (D/f'GY1979_{suffix}.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
with (D/'GY1979_corrections.csv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=['page','place','transcription_reads','should_read',
                                      'evidence','applies_to','type'])
    writer.writeheader();writer.writerows(corrections)
(D/'GY1979_references.bib').write_text('\n\n'.join(references[k] for k in sorted(references))+'\n')
(D/'code/bibliography_merge_conflicts.json').write_text(json.dumps(conflicts,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'records':len(talks),'items':len(items),'problems':len(problems),
                  'references':len(references),'corrections':len(corrections),
                  'bibliography_conflicts_to_review':len(conflicts)},indent=2))
