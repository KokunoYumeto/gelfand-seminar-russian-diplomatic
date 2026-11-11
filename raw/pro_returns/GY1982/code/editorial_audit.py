#!/usr/bin/env python3
"""Join per-researcher source audits and correction links after final assembly.

The JSON/CSV are authoritative. This auxiliary audit verifies that every
bibliography entry has an opened-source record and every false-as-written
assessment has an explicit correction-ledger cross-reference.
"""
from pathlib import Path
import argparse
import csv
import json
import re
from chapter_checks import bib_entries,bib_field

GROUPS=['autumn_physics','winter_geometry','spring_integrable']


def norm(value):
    return re.sub(r'\s+',' ',value.replace('\textquotesingle',r'\textquotesingle')).strip()


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--directory',type=Path,required=True)
    parser.add_argument('--shards',type=Path,required=True)
    parser.add_argument('--root-audit',type=Path,required=True)
    args=parser.parse_args()
    root=args.directory
    assembly=json.loads((root/'code/assembly_audit.json').read_text())
    aliases={m['draft_key']:m['final_key'] for m in assembly['bibliography_mappings']}
    bib=bib_entries((root/'GY1982_references.bib').read_text())
    items=json.loads((root/'GY1982_items.json').read_text())
    corrections=list(csv.DictReader((root/'GY1982_corrections.csv').open()))
    sources={}
    crosswalk={}
    errors=[]
    for group in GROUPS+['root']:
        folder=args.root_audit if group=='root' else args.shards/group
        source_file=folder/'source_audit.json'
        if not source_file.exists():
            errors.append('Missing per-key source audit: '+group)
            continue
        audit=json.loads(source_file.read_text())
        if isinstance(audit,dict) and 'references' in audit:
            audit=audit['references']
        if isinstance(audit,list):
            audit={x.get('key',x.get('bibkey')):x for x in audit}
        for key,data in audit.items():
            canonical=aliases.get(key,key)
            if canonical not in bib:
                continue
            entry={'research_group':group,'draft_key':key,**data}
            sources.setdefault(canonical,[]).append(entry)
        for name in ['validation_report.json','correction_map.json']:
            path=folder/name
            if not path.exists():continue
            data=json.loads(path.read_text())
            mapping=data.get('false_as_written_to_corrections',data)
            for item_id,pairs in mapping.items():
                if not re.fullmatch(r'1982-\d+\.\d+',item_id):continue
                if isinstance(pairs,dict):pairs=pairs.get('corrections',[])
                crosswalk.setdefault(item_id,[])
                for pair in pairs:
                    if isinstance(pair,dict):pair=[pair['page'],pair['place']]
                    if pair not in crosswalk[item_id]:crosswalk[item_id].append(pair)
    for key in bib:
        if key not in sources:
            errors.append('No opened-source audit for '+key)
        elif not any(s.get('opened_url') or s.get('opened_urls') for s in sources[key]):
            errors.append('No opened URL recorded for '+key)
    linked={}
    for item in items:
        if item['literal_correctness']!='false as written':continue
        item_id=item['id']
        pairs=crosswalk.get(item_id,[])
        if not pairs:
            errors.append('No correction crosswalk for '+item_id)
        matches=[]
        for page,place in pairs:
            rows=[{'data_row':n,'page':r['page'],'place':r['place'],'type':r['type']}
                  for n,r in enumerate(corrections,1)
                  if norm(r['page'])==norm(page) and norm(r['place'])==norm(place)]
            if not rows:
                errors.append('Correction target missing for '+item_id+': '+page+' / '+place)
            for row in rows:
                if row not in matches:matches.append(row)
        linked[item_id]=matches
    result={
        'result':'PASS' if not errors else 'FAIL',
        'status_date':'2026-11',
        'bibliography_entries':len(bib),
        'entries_with_source_audit':len(sources),
        'bibliography_verification_notes':{label:sum(bib_field(e,'note').strip()==label for e in bib.values()) for label in ['verified','unverified']},
        'false_as_written_items':len(linked),
        'false_as_written_to_corrections':linked,
        'reference_sources':sources,
        'errors':errors,
    }
    (root/'code/editorial_audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['reference_sources','false_as_written_to_corrections']},ensure_ascii=False,indent=2))
    raise SystemExit(bool(errors))


if __name__=='__main__':main()
