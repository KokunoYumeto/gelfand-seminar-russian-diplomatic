#!/usr/bin/env python3
"""Merge research checkpoints and audit the GY1987 chapter's data.

Run from the research workspace with --assemble to merge the retained
shards. In the delivered package, run without --assemble to audit its
seven authoritative files. The assembler makes explicitly logged
typographic normalizations and applies the separately authored root
editorial overrides; it never infers mathematical or historical edits.
"""
import argparse
from collections import Counter, defaultdict
import csv
import json
from pathlib import Path
import re
import shutil
import sys

TAG = "GY1987"
SOURCE_ORDER = [714,715,716,717,719,718]+list(range(720,732))+[733,732]+list(range(734,752))
CITE = re.compile(r"\\cite(?:p|t|alp|alt|author|year|yearpar)?\*?(?:\[[^\]]*\])*\{([^}]*)\}")
ITEM_KEYS = set("id record pages kind title notes statement reconstruction class fate present_status literal_correctness publication_match verification development problem worth refs confidence".split())
TALK_KEYS = set("record date speaker pages title kind summary".split())
PROBLEM_KEYS = set("id title statement occurrences status status_date refs".split())
ENUMS = {
    "kind": set("definition construction theorem claim conjecture question problem method remark".split()),
    "class": set("ABCDEF"),
    "literal_correctness": {"correct","correct with missing hypotheses","false as written","not determinable"},
    "publication_match": {"exact","partial","thematic only","none found"},
    "verification": {"read the result","publisher metadata checked","indirect","unresolved lead"},
    "development": {"none","annotated","developed in this chapter"},
    "confidence": {"high","medium","low"},
}


def bib_entries(text):
    """Return raw balanced-brace BibTeX entries, without rewriting TeX."""
    result = []
    pos = 0
    start_re = re.compile(r"@([A-Za-z]+)\s*\{\s*([^,\s]+)\s*,")
    while match := start_re.search(text,pos):
        start, depth, i = match.start(), 1, match.end()
        while i < len(text) and depth:
            if text[i] == "\\":
                i += 2
                continue
            if text[i] == "{": depth += 1
            if text[i] == "}": depth -= 1
            i += 1
        if depth:
            raise ValueError(f"Unclosed bibliography entry {match.group(2)}")
        result.append((match.group(2),text[start:i].strip()))
        pos = i
    return result


def bib_field(raw,name):
    match = re.search(r"(?:^|[,\n])\s*"+re.escape(name)+r"\s*=\s*",raw,re.I)
    if not match: return ""
    p = match.end()
    if raw[p] == "{":
        depth, i = 1,p+1
        while i < len(raw) and depth:
            if raw[i] == "\\": i += 2; continue
            if raw[i] == "{": depth += 1
            if raw[i] == "}": depth -= 1
            i += 1
        return raw[p+1:i-1].strip()
    if raw[p] == '"':
        i = p+1
        while i < len(raw):
            if raw[i] == "\\": i += 2; continue
            if raw[i] == '"': break
            i += 1
        return raw[p+1:i].strip()
    return re.split(r"[,\n]",raw[p:],1)[0].strip()


def replace_bib_field(raw,name,value):
    match=re.search(r"(?:^|[,\n])\s*"+re.escape(name)+r"\s*=\s*",raw,re.I)
    if not match:
        return raw.rstrip()[:-1].rstrip().rstrip(',')+',\n '+name+'={'+value+'}\n}'
    p=match.end()
    if raw[p]!='{':raise ValueError('Expected a braced bibliography field '+name)
    depth,i=1,p+1
    while i<len(raw) and depth:
        if raw[i]=='\\':i+=2;continue
        if raw[i]=='{':depth+=1
        if raw[i]=='}':depth-=1
        i+=1
    return raw[:p]+'{'+value+'}'+raw[i:]


def citations(value):
    if isinstance(value,str):
        return {k.strip() for group in CITE.findall(value) for k in group.split(',') if k.strip()}
    if isinstance(value,dict): return set().union(*(citations(v) for v in value.values()))
    if isinstance(value,list): return set().union(*(citations(v) for v in value)) if value else set()
    return set()


def normalize(value,where,changes):
    if isinstance(value,str):
        old = value
        value = value.replace('\textquotesingle ',"'").replace(r'\textquotesingle ',"'")
        value = value.replace("notes'exponent","notes' exponent")
        if not where.endswith(('.id','.refs','.problem')):
            value=re.sub(r'\b(published|December|November|Section|Sections|Theorem|Theorems|Lemma|Proposition|Equation|equation|equations|DLMF|Kerov|Lukyanov|Khovanova)(?=\d)',r'\1 ',value)
        if where.endswith('.title') or where.endswith('.speaker'):
            value = value.replace(r'Kn\"orrer','Knörrer').replace('Kn"orrer','Knörrer')
        if value != old:
            changes.append({"field":where,"before":old,"after":value,
                            "reason":"Typographic normalization of apostrophes, plain-text diacritics, or prose spacing"})
        return value
    if isinstance(value,dict):
        return {k:normalize(v,where+'.'+k,changes) for k,v in value.items()}
    if isinstance(value,list):
        return [normalize(v,where+f'[{i}]',changes) for i,v in enumerate(value)]
    return value


def write_json(path,value):
    path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')


def assemble(base,out):
    out.mkdir(exist_ok=True)
    changes=[]
    talks=[]; items=[]; problems=[]; corrections=[]; areas={}
    for prefix in ['early','middle','late']:
        for kind,target in [('talks',talks),('items',items),('problems',problems)]:
            p=base/'shards'/f'{prefix}_{kind}.json'
            target.extend(normalize(json.loads(p.read_text()),p.name,changes))
        p=base/'shards'/f'{prefix}_corrections.csv'
        with p.open(newline='',encoding='utf-8') as stream:
            corrections.extend(normalize(list(csv.DictReader(stream)),p.name,changes))
        p=base/'shards'/f'{prefix}_areas.json'
        if p.exists(): areas.update(json.loads(p.read_text()))
    order={r:i for i,r in enumerate(SOURCE_ORDER)}
    talks.sort(key=lambda x:order.get(x['record'],1000))
    items.sort(key=lambda x:(order.get(x['record'],1000),int(x['id'].split('.')[-1])))
    # Each shard may refer to a recurring earlier problem. Merge only identical
    # IDs, retaining the union of occurrences and references for manual review.
    merged={}
    for p in problems:
        if p['id'] in merged:
            q=merged[p['id']]
            q['occurrences']=list(dict.fromkeys(q['occurrences']+p['occurrences']))
            q['refs']=list(dict.fromkeys(q['refs']+p['refs']))
            if q['statement'] != p['statement']:
                changes.append({'field':p['id'],'reason':'Duplicate problem ID; retained first statement for manual review',
                                'alternative_statement':p['statement']})
        else: merged[p['id']]=p
    problems=list(merged.values())
    override_path=base/'shards'/'root_overrides.json'
    if override_path.exists():
        overrides=json.loads(override_path.read_text())
        for kind,values in [('items',items),('problems',problems)]:
            for x in values:
                if x['id'] in overrides.get(kind,{}):
                    patch=overrides[kind][x['id']]
                    x.update(patch)
                    changes.append({'field':x['id'],'reason':'Explicit root literature/development integration',
                                    'updated_fields':sorted(patch)})
    layout_path=base/'shards'/'root_layout_patches.json'
    if layout_path.exists():
        layouts=json.loads(layout_path.read_text())
        for x in items:
            if x['id'] in layouts:
                x.update(layouts[x['id']])
                changes.append({'field':x['id'],'reason':'Display long formulas or add discretionary line breaks',
                                'updated_fields':sorted(layouts[x['id']])})
    for kind,data in [('talks',talks),('items',items),('problems',problems)]:
        write_json(out/f'{TAG}_{kind}.json',data)
    correction_format_path=base/'shards'/'root_correction_formats.json'
    if correction_format_path.exists():
        formats=json.loads(correction_format_path.read_text())
        for row in corrections:
            key=row['page']+'|'+row['place']
            if key in formats:
                row.update(formats[key])
                changes.append({'field':key,'reason':'Explicit mathematical typesetting of CSV prose/formula fragments'})
    corrections.sort(key=lambda x:x['page'])
    with (out/f'{TAG}_corrections.csv').open('w',newline='',encoding='utf-8') as stream:
        writer=csv.DictWriter(stream,fieldnames='page place transcription_reads should_read evidence applies_to type'.split())
        writer.writeheader();writer.writerows(corrections)
    # The agents supply complete reused entries or explicitly opened new ones.
    # The cumulative file is a fallback, never silently upgraded to "read".
    ref_sources=[]
    for prefix in ['early','middle','late']:
        exact=base/'shards'/f'{prefix}_references.bib'
        alternatives=sorted((base/'shards').glob(f'{prefix}_*references.bib'))
        ref_sources.extend([exact] if exact.exists() else alternatives)
    ref_sources.append(base/'shards'/'root_references.bib')
    entries={}; duplicate_entries=[]
    for path in ref_sources:
        for key,raw in bib_entries(path.read_text()):
            if key in entries and entries[key] != raw:
                duplicate_entries.append({'key':key,'preferred_source':str(path),
                                          'reason':'Last metadata entry retained; verification annotations merged',
                                          'previous_year':bib_field(entries[key],'year'),
                                          'preferred_year':bib_field(raw,'year')})
                previous_annote=bib_field(entries[key],'annote')
                latest_annote=bib_field(raw,'annote')
                if previous_annote and previous_annote!=latest_annote:
                    raw=replace_bib_field(raw,'annote',latest_annote+' Additional independently recorded verification: '+previous_annote)
            entries[key]=raw
    needed=citations(talks)|citations(items)|citations(problems)|citations(corrections)
    for name in ['overview','development']:
        path=out/f'{TAG}_{name}.tex'
        if path.exists():needed|=citations(path.read_text())
    needed|={k for x in items+problems for k in x.get('refs',[])}
    fallback=[]
    for key,raw in bib_entries((base/'references_cumulative.bib').read_text()):
        if key in needed and key not in entries:
            entries[key]=raw;fallback.append(key)
    retained={k:v for k,v in entries.items() if k in needed}
    proper_names = sorted(['Cartan','Riemannian','Coxeter','Gabriel','Perron',
        'Riemann--Hilbert','Fourier','Weil',"Gel'fand--Dikii",'Ruelle',
        'Yang--Baxter','Markov','Tamagawa','Grassmannian','Jones','Fermat',
        'Morse','Div','Stacks Project'],key=len,reverse=True)
    proper_pattern=re.compile(r'(?<!\{)\b('+ '|'.join(re.escape(x) for x in proper_names)+r')\b')
    for key,raw in list(retained.items()):
        old_title=bib_field(raw,'title')
        if key in {'riemann1851grundlagen','lindemann1882pi'}:
            new_title='{'+old_title+'}'
        else:
            new_title=proper_pattern.sub(lambda m:'{'+m.group(1)+'}',old_title)
        if new_title!=old_title:
            retained[key]=replace_bib_field(raw,'title',new_title)
            changes.append({'field':key+'.title','reason':'Protect proper-name capitalization in the supplied BibTeX style'})
    (out/f'{TAG}_references.bib').write_text('\n\n'.join(retained[k] for k in sorted(retained))+'\n')
    write_json(out/'logs'/'assembly_log.json',{'typographic_normalizations':changes,
               'reference_duplicates':duplicate_entries,'cumulative_fallback_keys':fallback,
               'missing_reference_keys':sorted(needed-set(entries)),
               'references_supplied_but_unused':sorted(set(entries)-needed)})
    write_json(out/'logs'/'item_areas.json',areas)
    for name in ['build_chapter.py','gelfand_companion.sty','CHAPTER_FORMAT.md']:
        shutil.copy2(base/'kit'/name,out/name)


def audit(out,previous=None):
    errors=[];warnings=[]
    data={k:json.loads((out/f'{TAG}_{k}.json').read_text()) for k in ['talks','items','problems']}
    talks,items,problems=(data[k] for k in ['talks','items','problems'])
    refs_list=bib_entries((out/f'{TAG}_references.bib').read_text())
    refs=dict(refs_list)
    if len(refs_list)!=len(refs):errors.append('Duplicate bibliography keys')
    recs={x['record']:x for x in talks}; ids={x['id']:x for x in items}; pids={x['id']:x for x in problems}
    if [x['record'] for x in talks]!=SOURCE_ORDER:errors.append('Record list differs from verified 38-record source order')
    if len(ids)!=len(items):errors.append('Duplicate item identifiers')
    if len(pids)!=len(problems):errors.append('Duplicate problem identifiers')
    for kind,values,keys in [('talks',talks,TALK_KEYS),('items',items,ITEM_KEYS),('problems',problems,PROBLEM_KEYS)]:
        for x in values:
            label=str(x.get('id',x.get('record')))
            missing=keys-set(x)
            if missing:errors.append(f'{label}: missing {sorted(missing)}')
            for k,v in x.items():
                if isinstance(v,str):
                    if any(ord(c)<32 and c!='\n' for c in v):errors.append(f'{label}.{k}: control character')
                    if k in ['title','speaker','date','pages'] and '\\' in v:errors.append(f'{label}.{k}: LaTeX in plain-text field')
            missing_cites=citations(x)-set(refs)
            if missing_cites:errors.append(f'{label}: missing cited references {sorted(missing_cites)}')
            if kind!='talks':
                if citations(x)-set(x['refs']):errors.append(f'{label}: cited keys absent from refs: {sorted(citations(x)-set(x["refs"]))}')
                if set(x['refs'])-set(refs):errors.append(f'{label}: refs absent from bibliography: {sorted(set(x["refs"])-set(refs))}')
    byrec=defaultdict(list)
    for x in items:
        label=x['id'];byrec[x['record']].append(label)
        for k,allowed in ENUMS.items():
            if x[k] not in allowed:errors.append(f'{label}: invalid {k} {x[k]}')
        if x['record'] not in recs:errors.append(f'{label}: no parent record')
        if x['class'] in 'CD' and not x['worth']:errors.append(f'{label}: C/D without worth sentence')
        if '2026' not in x['present_status']:errors.append(f'{label}: status lacks explicit year')
        if x['problem'] and x['problem'] not in pids:errors.append(f'{label}: missing problem')
        if x['problem'] in pids and label not in pids[x['problem']]['occurrences']:errors.append(f'{label}: problem backlink absent')
        if any(int(p)>1477 for p in re.findall(r'P0*(\d+)',x['pages'])):errors.append(f'{label}: outside academic-year source boundary')
    for record,found in byrec.items():
        expected=[f'1987-{record}.{i}' for i in range(1,len(found)+1)]
        if found!=expected:errors.append(f'{record}: items not consecutively numbered')
    for record,t in recs.items():
        if t.get('kind')=='talk' and not byrec[record]:warnings.append(f'Record {record} is a talk with no mathematical items; verify source coverage')
    for p in problems:
        if p['status_date']!='2026-11':errors.append(f'{p["id"]}: wrong status date')
        for occurrence in p['occurrences']:
            if occurrence.startswith('1987-') and occurrence not in ids:errors.append(f'{p["id"]}: nonexistent current occurrence {occurrence}')
            elif previous and not occurrence.startswith('1987-') and occurrence not in previous:errors.append(f'{p["id"]}: prior occurrence absent from supplied index: {occurrence}')
    for key,raw in refs.items():
        if not bib_field(raw,'url') and not bib_field(raw,'doi'):errors.append(f'{key}: no DOI or URL')
        if bib_field(raw,'note') not in ['verified','unverified']:errors.append(f'{key}: invalid verification note {bib_field(raw,"note")}')
    for name in ['overview','development']:
        path=out/f'{TAG}_{name}.tex'
        if not path.exists():errors.append(f'Missing {path.name}');continue
        for key in citations(path.read_text())-set(refs):errors.append(f'{path.name}: absent citation {key}')
    with (out/f'{TAG}_corrections.csv').open(newline='',encoding='utf-8') as stream:
        corrections=list(csv.DictReader(stream))
    for row in corrections:
        if row['type'] not in ['transcription','translation','ambiguity','faithful_error','provenance','']:errors.append('Invalid correction type '+row['type'])
        if row['applies_to'] not in ['ru','en','both']:errors.append('Invalid applies_to '+row['applies_to'])
    coverage=defaultdict(list)
    for t in talks:
        nums=[int(p) for p in re.findall(r'P0*(\d+)',t['pages'])]
        if nums:
            for page in range(min(nums),max(nums)+1):coverage[page].append(t['record'])
    context_pages={1460:'Bourbaki reading list; explicitly described in record 747 summary'} if 'P001460' in recs.get(747,{}).get('summary','') else {}
    not_covered=[p for p in range(1385,1478) if p not in coverage and p not in context_pages]
    if not_covered:warnings.append('Pages outside talk page ranges; account as source context: '+str(not_covered))
    result={'status':'PASS' if not errors else 'FAIL','counts':{
        'records':len(talks),'items':len(items),'problems':len(problems),'references':len(refs),'corrections':len(corrections),
        'classes':dict(sorted(Counter(x['class'] for x in items).items())),
        'by_record':{str(r):len(byrec[r]) for r in SOURCE_ORDER},
        'by_speaker':dict(Counter(x.get('speaker') or recs[x['record']]['speaker'] or 'Unattributed' for x in items)),
        'literal_correctness':dict(Counter(x['literal_correctness'] for x in items)),
        'publication_match':dict(Counter(x['publication_match'] for x in items)),
        'verification':dict(Counter(x['verification'] for x in items)),
        'correction_types':dict(Counter(x['type'] for x in corrections))},
        'page_coverage':{f'P{p:06}':r for p,r in sorted(coverage.items())},
        'context_pages':{f'P{p:06}':reason for p,reason in context_pages.items()},
        'uncovered_context_pages':not_covered,'excluded_next_year_pages':['P001478','P001479'],
        'errors':errors,'warnings':warnings}
    write_json(out/'logs'/'data_audit.json',result)
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return not errors


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--assemble',action='store_true')
    parser.add_argument('--directory',type=Path,default=Path('.'))
    args=parser.parse_args()
    base=args.directory.resolve()
    out=base/'output' if args.assemble else base
    (out/'logs').mkdir(parents=True,exist_ok=True)
    if args.assemble:assemble(base,out)
    previous=(base/'previous_index.md').read_text() if (base/'previous_index.md').exists() else None
    sys.exit(0 if audit(out,previous) else 1)
