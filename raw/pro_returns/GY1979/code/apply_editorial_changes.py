#!/usr/bin/env python3
"""Apply explicit, logged integration decisions after merging the three batches.

The original catalog ranges remain in catalog_original.json and the generated
crosswalk. Final talks.pages consistently denotes the actual source span.
Optional citation aliases and problem overrides are human-reviewed decisions
stored in editorial_config.json, not inferred automatically.
"""
from pathlib import Path
import csv
import json
import re
from audit_chapter import bib_entries,page_numbers

D=Path(__file__).resolve().parent.parent
config_path=D/'code/editorial_config.json'
cfg=json.loads(config_path.read_text()) if config_path.exists() else {}
data={suffix:json.loads((D/f'GY1979_{suffix}.json').read_text())
      for suffix in ('talks','items','problems')}
catalog={t['record']:t for t in json.loads((D/'code/catalog_original.json').read_text())}
edits=[]
crosswalk=[]
for t in data['talks']:
    rec=t['record']
    pages=set().union(*(page_numbers(x['pages']) for x in data['items'] if x['record']==rec))
    if pages:
        actual=f'P{min(pages):06d}'
        if len(pages)>1:actual+=f'-P{max(pages):06d}'
        actual=cfg.get('source_span_overrides',{}).get(str(rec),actual)
        if t['pages']!=actual:
            edits.append({'target':f'talk:{rec}.pages','before':t['pages'],'after':actual,
                          'reason':'Normalize source-page field to the critical actual span; preserve catalog envelope in crosswalk.'})
            t['pages']=actual
    if rec==462:
        old='The catalogue page interval is retained verbatim.'
        new='The overlapping catalogue page interval is retained in the provenance crosswalk; the source-page field gives the actual talk span.'
        t['summary']=t['summary'].replace(old,new)
    crosswalk.append({**catalog[rec],'critical_date':t['date'],
                      'critical_pages':t['pages'],'record_kind':t['kind'],
                      'note':'Catalog heading; no separate mathematical occurrence.' if t['kind']=='heading' else
                      ('Manuscript date 29/X-79 overrides the catalog month.' if rec==473 else
                       'Source boundaries established from dated/speaker headings and item locations.')})

for id,patch in cfg.get('item_overrides',{}).items():
    x=next(x for x in data['items'] if x['id']==id)
    for field,value in patch.items():
        if x.get(field)!=value:
            edits.append({'target':id+'.'+field,'before':x.get(field),'after':value,
                          'reason':'Explicit review decision in editorial_config.json.'})
            x[field]=value
for id,patch in cfg.get('problem_overrides',{}).items():
    p=next(p for p in data['problems'] if p['id']==id)
    for field,value in patch.items():
        if p.get(field)!=value:
            edits.append({'target':id+'.'+field,'before':p.get(field),'after':value,
                          'reason':'Reconcile overlapping problem descriptions without changing quantifiers.'})
            p[field]=value

aliases=cfg.get('citation_key_aliases',{})
def replace_aliases(x):
    if isinstance(x,str):
        x=re.sub(r'\\S([IVX]+)\b',r'\\S~\1',x)
        x=x.replace('boundary_inventory.md',r'\texttt{code/boundary\_inventory.md}')
        for old,new in aliases.items():
            x=re.sub(r'(?<![A-Za-z0-9_])'+re.escape(old)+r'(?![A-Za-z0-9_])',new,x)
        return x
    if isinstance(x,list):return [replace_aliases(y) for y in x]
    if isinstance(x,dict):return {k:replace_aliases(v) for k,v in x.items()}
    return x
data=replace_aliases(data)
for suffix,obj in data.items():
    (D/f'GY1979_{suffix}.json').write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
if aliases:
    for suffix in ('development.tex','corrections.csv'):
        p=D/f'GY1979_{suffix}';p.write_text(replace_aliases(p.read_text()))
    entries={}
    for k,entry in bib_entries((D/'GY1979_references.bib').read_text()):
        key=aliases.get(k,k)
        revised=re.sub(r'(@\w+\s*\{\s*)'+re.escape(k)+r'\s*,',r'\g<1>'+key+',',entry,count=1)
        if key not in entries:entries[key]=revised
    (D/'GY1979_references.bib').write_text('\n\n'.join(entries[k] for k in sorted(entries))+'\n')
    edits.append({'citation_key_aliases':aliases,'reason':'Reuse keys for identical works already in the cumulative bibliography.'})

def bib_field(entry,name):
    match=re.search(r'\b'+name+r'\s*=\s*\{',entry,re.I)
    if not match:return None,None,None
    start=match.end();j=start;depth=1
    while j<len(entry) and depth:
        if entry[j]=='{' and entry[j-1]!='\\':depth+=1
        if entry[j]=='}' and entry[j-1]!='\\':depth-=1
        j+=1
    return start,j-1,entry[start:j-1]

def set_bib_field(entry,name,value):
    start,end,old=bib_field(entry,name)
    if start is not None:return entry[:start]+value+entry[end:]
    return entry.rstrip()[:-1].rstrip().rstrip(',')+',\n  '+name+' = {'+value+'},\n}'

def remove_bib_field(entry,name):
    start,end,_=bib_field(entry,name)
    if start is None:return entry
    match=re.search(r'\b'+name+r'\s*=\s*\{',entry,re.I)
    finish=end+1
    while finish<len(entry) and entry[finish].isspace():finish+=1
    if finish<len(entry) and entry[finish]==',':finish+=1
    return entry[:match.start()]+entry[finish:]

entries=dict(bib_entries((D/'GY1979_references.bib').read_text()))
metadata_path=D/'code/bibliography_metadata_output.json'
if metadata_path.exists():
    for row in json.loads(metadata_path.read_text()):
        key=row['key']
        if row['result']!='PASS' or key not in entries:continue
        e=entries[key]
        e=set_bib_field(e,'note','verified')
        e=set_bib_field(e,'url',row['opened_url'])
        _,_,annote=bib_field(e,'annote')
        supplement='Root supplemental check: DOI registration metadata opened through Crossref on 10 November 2026; title, authors, journal and pagination compared. This verifies bibliographic identity only; per-item result-verification limits remain unchanged. Exact response fields are saved in code/bibliography_metadata_output.json.'
        if supplement not in (annote or ''):e=set_bib_field(e,'annote',(annote or '')+' '+supplement)
        entries[key]=e
    edits.append({'target':'bibliography DOI metadata verification',
                  'verified_keys':[r['key'] for r in json.loads(metadata_path.read_text()) if r['result']=='PASS'],
                  'reason':'Supplemental public DOI-registration metadata actually opened; no theorem verification upgraded.'})
for key,patch in cfg.get('bibliography_fields',{}).items():
    for field,value in patch.items():
        _,_,old=bib_field(entries[key],field)
        if old!=value:
            edits.append({'target':key+'.'+field,'before':old,'after':value,
                          'reason':'Correct bibliographic metadata or LaTeX spelling after source comparison.'})
            entries[key]=remove_bib_field(entries[key],field) if value is None else set_bib_field(entries[key],field,value)
(D/'GY1979_references.bib').write_text('\n\n'.join(entries[k] for k in sorted(entries))+'\n')
with (D/'code/catalog_crosswalk.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(crosswalk[0]));w.writeheader();w.writerows(crosswalk)
(D/'code/editorial_changes.json').write_text(json.dumps(edits,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'critical_source_spans':len(crosswalk),'logged_changes':len(edits)},indent=2))
