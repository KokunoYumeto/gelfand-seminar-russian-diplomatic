#!/usr/bin/env python3
"""Assemble independently researched record groups and reconcile bibliography keys.

This records the original assembly step. The final JSON/TeX/CSV files include
subsequent editorial corrections and are authoritative for rebuilding the PDF.
Do not rerun assembly over an edited chapter without reviewing its differences.
The standalone rebuild.py reads the final data directly and does not run this.
"""
from pathlib import Path
import argparse
import csv
import json
import re
import unicodedata
from chapter_checks import bib_field

ORDER = list(range(561,593)) + [594,593,596,595,598]
GROUPS = ['autumn_physics','winter_geometry','spring_integrable']


def split_bib(text):
    """Retain duplicated legacy keys for comparison, without silently losing entries."""
    result = []
    for match in re.finditer(r'@([a-zA-Z]+)\s*\{\s*([^,\s]+)\s*,',text):
        start = match.start()
        index = text.index('{',start)
        depth = 0
        while index < len(text):
            char = text[index]
            escaped = index > 0 and text[index-1]=='\\'
            if char=='{' and not escaped:
                depth += 1
            elif char=='}' and not escaped:
                depth -= 1
                if depth==0:
                    break
            index += 1
        if index==len(text):
            raise ValueError('Unbalanced bibliography entry: '+match[2])
        result.append((match[2],text[start:index+1]))
    return result


def norm_doi(entry):
    value = bib_field(entry,'doi').strip().lower()
    return re.sub(r'^https?://(?:dx\.)?doi\.org/','',value).replace('\\_','_')


def norm_title(entry):
    value = unicodedata.normalize('NFKD',bib_field(entry,'title')).lower()
    return re.sub(r'[^a-z0-9]','',value)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--shards',type=Path,required=True)
    parser.add_argument('--root-references',type=Path,required=True)
    parser.add_argument('--cumulative',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    output = args.output
    output.mkdir(parents=True,exist_ok=True)
    (output/'code').mkdir(exist_ok=True)
    talks,items,problems,corrections,drafts = [],[],[],[],[]
    audit = {'record_order':ORDER,'legacy_duplicate_keys':[],
             'bibliography_mappings':[],'duplicate_draft_entries':[],
             'escape_repairs':[],'editorial_adjustments':[]}
    for group in GROUPS:
        folder = args.shards/group
        for name,container in [('talks',talks),('items',items),('problems',problems)]:
            container.extend(json.loads((folder/f'{name}.json').read_text()))
        corrections.extend(csv.DictReader((folder/'corrections.csv').open()))
        drafts.extend((key,entry,group) for key,entry in split_bib((folder/'references.bib').read_text()))
    drafts.extend((key,entry,'root') for key,entry in split_bib(args.root_references.read_text()))
    records = [t['record'] for t in talks]
    if set(records)!=set(ORDER) or len(records)!=len(ORDER):
        raise SystemExit('Assembly requires all 37 records exactly once; found '+str(sorted(records)))
    talks.sort(key=lambda t:ORDER.index(t['record']))
    items.sort(key=lambda x:(ORDER.index(x['record']),int(x['id'].split('.')[1])))
    seen_problems = set()
    for p in problems:
        if p['id'] in seen_problems:
            raise ValueError('Duplicate problem object requires an editorial merge: '+p['id'])
        seen_problems.add(p['id'])
    problems.sort(key=lambda p:min((ORDER.index(int(i.split('-')[1].split('.')[0])),int(i.split('.')[1]))
                                  for i in p['occurrences'] if i.startswith('1982-')))

    legacy_keys,legacy_doi,legacy_title = {},{},{}
    for key,entry in split_bib(args.cumulative.read_text()):
        if key in legacy_keys:
            audit['legacy_duplicate_keys'].append(key)
        legacy_keys.setdefault(key,entry)
        doi = norm_doi(entry)
        if doi:
            legacy_doi.setdefault(doi,key)
        title_year = (norm_title(entry),bib_field(entry,'year').strip())
        if title_year[0]:
            legacy_title.setdefault(title_year,key)
    aliases = {}
    consolidated = {}
    current_doi,current_title = {},{}
    for key,entry,group in drafts:
        doi = norm_doi(entry)
        title_year = (norm_title(entry),bib_field(entry,'year').strip())
        if doi and doi in legacy_doi:
            canonical,reason = legacy_doi[doi],'same DOI in cumulative bibliography'
        elif key in legacy_keys:
            canonical,reason = key,'key already in cumulative bibliography'
        elif title_year in legacy_title:
            canonical,reason = legacy_title[title_year],'same normalized title and year in cumulative bibliography'
        elif doi and doi in current_doi:
            canonical,reason = current_doi[doi],'same DOI within this chapter'
        elif title_year in current_title:
            canonical,reason = current_title[title_year],'same normalized title and year within this chapter'
        else:
            canonical,reason = key,'new reference'
        if key in aliases and aliases[key]!=canonical:
            raise ValueError('Inconsistent alias: '+key)
        aliases[key] = canonical
        if doi:
            current_doi.setdefault(doi,canonical)
        current_title.setdefault(title_year,canonical)
        audit['bibliography_mappings'].append({'source_group':group,'draft_key':key,
                                               'final_key':canonical,'reason':reason})
        renamed = re.sub(r'(@[A-Za-z]+\s*\{\s*)[^,\s]+',lambda m:m[1]+canonical,entry,count=1)
        if canonical in consolidated:
            old = consolidated[canonical]
            old_doi = norm_doi(old)
            if old_doi and doi and doi!=old_doi:
                raise ValueError('Conflicting DOI for '+canonical+': '+old_doi+' / '+doi)
            audit['duplicate_draft_entries'].append({'key':canonical,'source_group':group})
            # Prefer the fuller fresh record, retaining an opened-source URL.
            if len(renamed)>len(old):
                consolidated[canonical]=renamed
        else:
            consolidated[canonical]=renamed

    cite_pattern = re.compile(r'(\\cite[pt]?\*?(?:\[[^\]]*\])*\{)([^}]+)(\})')
    def transform(value,location):
        if isinstance(value,str):
            if '\textquotesingle' in value:  # Python tab followed by extquotesingle
                audit['escape_repairs'].append(location)
                value=value.replace('\textquotesingle',r'\textquotesingle')
            value=cite_pattern.sub(lambda m:m[1]+','.join(aliases.get(k.strip(),k.strip())
                                                           for k in m[2].split(','))+m[3],value)
            return value
        if isinstance(value,list):
            return [transform(x,location+f'[{i}]') for i,x in enumerate(value)]
        if isinstance(value,dict):
            result={k:transform(v,location+'.'+k) for k,v in value.items()}
            if 'refs' in result:
                result['refs']=list(dict.fromkeys(aliases.get(k,k) for k in result['refs']))
            return result
        return value
    talks=transform(talks,'talks')
    items=transform(items,'items')
    problems=transform(problems,'problems')
    corrections=transform(corrections,'corrections')
    for talk in talks:
        if talk['kind']=='heading':
            if talk['speaker']=='-':
                talk['speaker']=''
            talk['title']=talk['title'].replace('Year1983','Year 1983')
    for item in items:
        if item['id']=='1982-565.6':
            item['development']='developed in this chapter'
            if '\\hyperref[dev:1982-migdal]' not in item['fate']:
                item['fate']+=r' The bounded calculation in \hyperref[dev:1982-migdal]{the development section} proves the first two local coefficients in the exact notebook convention.'
            audit['editorial_adjustments'].append('Linked 1982-565.6 to the completed local free-energy development.')
    for suffix in ('overview.tex','development.tex'):
        path=output/f'GY1982_{suffix}'
        if path.exists():
            path.write_text(transform(path.read_text(),suffix))
    for name,data in [('talks',talks),('items',items),('problems',problems)]:
        (output/f'GY1982_{name}.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    fields=['page','place','transcription_reads','should_read','evidence','applies_to','type']
    corrections.sort(key=lambda x:x['page'])
    with (output/'GY1982_corrections.csv').open('w',newline='') as stream:
        writer=csv.DictWriter(stream,fieldnames=fields)
        writer.writeheader()
        writer.writerows(corrections)
    (output/'GY1982_references.bib').write_text('\n\n'.join(consolidated[k] for k in sorted(consolidated))+'\n')
    audit['summary']={'records':len(talks),'items':len(items),'problems':len(problems),
                      'corrections':len(corrections),'references':len(consolidated)}
    (output/'code'/'assembly_audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(audit['summary'],indent=2))
    print('Assembly complete; review bibliography mappings and then validate the chapter.')


if __name__=='__main__':
    main()
