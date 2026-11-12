"""Assemble the GY1986 chapter from the three independently researched slices.

Run from any working directory after all slices have completed.
Input attachments remain unchanged. This script checks bibliography-key reuse,
record coverage, field vocabularies, source pages, citations and problem links.
"""
from pathlib import Path
from collections import Counter
import csv, json, re, shutil, hashlib

OUT=Path(__file__).resolve().parents[2]
ROOT=OUT.parent
PART_ROOT=ROOT/'parts' if (ROOT/'parts').exists() else OUT/'code'/'parts'
PARTS=[PART_ROOT/x for x in ['A','B','C']]
META=ROOT/'work' if (ROOT/'work'/'previous_index.md').exists() else OUT/'code'/'source_metadata'
PREVIOUS=META/'previous_index.md'
CUMULATIVE=META/'references_cumulative.bib'
SOURCE_RECORD_ORDER=list(range(667,713))
for earlier,later in [(683,682),(704,703),(708,707)]:
    a,b=SOURCE_RECORD_ORDER.index(earlier),SOURCE_RECORD_ORDER.index(later)
    SOURCE_RECORD_ORDER[a],SOURCE_RECORD_ORDER[b]=SOURCE_RECORD_ORDER[b],SOURCE_RECORD_ORDER[a]

def bib_entries(text):
    result={}
    for match in re.finditer(r'@([A-Za-z]+)\s*\{\s*([^,\s]+)\s*,',text):
        if match.group(1).lower() in {'comment','preamble','string'}:
            continue
        start=match.start(); brace=text.index('{',start); depth=1; i=brace+1
        while i < len(text) and depth:
            if text[i]=='\\':
                i+=2; continue
            if text[i]=='{': depth+=1
            elif text[i]=='}': depth-=1
            i+=1
        if depth: raise ValueError('unbalanced BibTeX entry '+match.group(2))
        entry=text[start:i]
        key=match.group(2)
        if key in result and result[key] != entry:
            # Older cumulative chapters can repeat a key with annotations.
            # Preserve the first bibliographic identity for key reuse.
            continue
        result[key]=entry
    return result

def field(entry,name):
    m=re.search(r'\b'+re.escape(name)+r'\s*=\s*\{([^{}]*)\}',entry,re.I)
    return m.group(1).strip() if m else ''

def doi(entry):
    value=field(entry,'doi').lower()
    return re.sub(r'^https?://(?:dx\.)?doi\.org/','',value).rstrip('.')

def citekeys(text):
    result=set()
    for match in re.finditer(r'\\cite[pt]?\*?(?:\[[^\]]*\])*\{([^}]*)\}',text):
        result.update(x.strip() for x in match[1].split(',') if x.strip())
    return result

def rewrite_citations(value,aliases):
    if isinstance(value,list):
        return [rewrite_citations(x,aliases) for x in value]
    if isinstance(value,dict):
        new={k:rewrite_citations(v,aliases) for k,v in value.items()}
        if 'refs' in new:
            new['refs']=list(dict.fromkeys(aliases.get(x,x) for x in new['refs']))
        return new
    if isinstance(value,str):
        def rep(m):
            return m[1]+','.join(aliases.get(x.strip(),x.strip()) for x in m[2].split(','))+'}'
        return re.sub(r'(\\cite[pt]?\*?(?:\[[^\]]*\])*\{)([^}]+)\}',rep,value)
    return value

def layout_adjustments(items,corrections):
    """Typeset long formulas and preserve plain correction text as literals."""
    byid={x['id']:x for x in items}
    for id_ in ['1986-685.5','1986-695.8','1986-695.10','1986-700.12','1986-700.14']:
        x=byid[id_]
        spans=list(re.finditer(r'\\\((.*?)\\\)',x['statement'],re.S))
        longest=max(spans,key=lambda m:len(m[1]))
        x['statement']=x['statement'][:longest.start()]+r'\['+longest[1]+r'\]'+x['statement'][longest.end():]
    x=byid['1986-712.8']
    x['statement']=(
        r'For compact K\"ahler \(X\) and \(p\ge1\), put '
        r'\[J^p(X)=\frac{H^{2p-1}(X,\mathbb C)}{F^pH^{2p-1}(X,\mathbb C)+\operatorname{im}H^{2p-1}(X,\mathbb Z(p))}.\] '
        r'There is an exact sequence '
        r'\[0\to J^p(X)\to H^{2p}_{\mathcal D}(X,\mathbb Z(p))'
        r'\to\{c\in H^{2p}(X,\mathbb Z(p)):c_{\mathbb C}\in F^p\}\to0.\] '
        r'The left group is the intermediate Jacobian. The right description retains torsion; '
        r'a literal intersection inside complex cohomology would lose it.'
    )
    # The CSV permits both plain text and LaTeX. The supplied builder inserts
    # cells literally, so protect text-mode metacharacters while retaining
    # existing explicit mathematics and escaped LaTeX commands.
    replacements={'_':r'\_','^':r'\textasciicircum{}','%':r'\%','&':r'\&','#':r'\#'}
    for row in corrections:
        if row['page']=='P001366' and row['place']=='resolvent square root':
            row['should_read']=(
                r"With \(R=f^2-(V'/\lambda)f\), the radicand is "
                r"\[\left(V'/(2\lambda)\right)^2+R.\]"
            )
        for fieldname in ['place','transcription_reads','should_read','evidence']:
            pieces=re.split(r'(\\\(.*?\\\)|\\\[.*?\\\])',row[fieldname],flags=re.S)
            for i in range(0,len(pieces),2):
                pieces[i]=re.sub(r'(?<!\\)[_^%&#]',lambda m:replacements[m[0]],pieces[i])
            row[fieldname]=''.join(pieces)
    return items,corrections

def load_parts():
    talks=[];items=[];problems=[];corrections=[];bibs={}
    for part in PARTS:
        talks.extend(json.loads((part/'talks.json').read_text()))
        items.extend(json.loads((part/'items.json').read_text()))
        problems.extend(json.loads((part/'problems.json').read_text()))
        with (part/'corrections.csv').open(newline='') as f:
            corrections.extend(csv.DictReader(f))
        for key,entry in bib_entries((part/'references.bib').read_text()).items():
            if key in bibs:
                old=bibs[key]
                if doi(old) and doi(entry) and doi(old)!=doi(entry):
                    raise ValueError('conflicting DOI for '+key)
                # Prefer fuller checked annotations, but never replace a verified
                # entry with an unverified one.
                if field(entry,'note')=='verified' and (field(old,'note')!='verified' or len(entry)>len(old)):
                    bibs[key]=entry
            else: bibs[key]=entry
    source_position={record:i for i,record in enumerate(SOURCE_RECORD_ORDER)}
    talks.sort(key=lambda x:source_position[x['record']])
    items.sort(key=lambda x:(source_position[x['record']],int(x['id'].split('.')[-1])))
    assert sorted(t['record'] for t in talks) == list(range(667,713)), 'All 46 catalogue records must be present exactly once'
    merged={}
    for p in problems:
        if p['id'] not in merged: merged[p['id']]=p
        else:
            dest=merged[p['id']]
            dest['occurrences']=list(dict.fromkeys(dest['occurrences']+p['occurrences']))
            dest['refs']=list(dict.fromkeys(dest['refs']+p['refs']))
            if dest['statement']!=p['statement']:
                dest['statement']+=' '+p['statement']
            if dest['status']!=p['status']:
                dest['status']+=' '+p['status']
    unique=[]
    seen=set()
    for row in corrections:
        sig=tuple(row.get(k,'') for k in ['page','place','transcription_reads','should_read','evidence','applies_to','type'])
        if sig not in seen:
            seen.add(sig);unique.append(row)
    return talks,items,list(merged.values()),unique,bibs

def validate(talks,items,problems,corrections,bibs):
    errors=[];ids={x['id'] for x in items};pids={p['id'] for p in problems}
    if len(ids)!=len(items):errors.append('duplicate item IDs')
    oldids=set(re.findall(r'\b\d{4}-\d+\.\d+\b',PREVIOUS.read_text()))
    enum={
        'kind':{'definition','construction','theorem','claim','conjecture','question','problem','method','remark'},
        'class':set('ABCDEF'),
        'literal_correctness':{'correct','correct with missing hypotheses','false as written','not determinable'},
        'publication_match':{'exact','partial','thematic only','none found'},
        'verification':{'read the result','publisher metadata checked','indirect','unresolved lead'},
        'development':{'none','annotated','developed in this chapter'},
        'confidence':{'high','medium','low'}}
    required={'id','record','pages','kind','title','notes','statement','reconstruction','class','fate','present_status','literal_correctness','publication_match','verification','development','problem','worth','refs','confidence'}
    recs={t['record']:t for t in talks}
    for t in talks:
        if t.get('kind') not in {'talk','plan','heading','other'}:errors.append('bad talk kind '+str(t['record']))
    for record in range(667,713):
        xs=[x for x in items if x['record']==record]
        if [x['id'] for x in xs]!=[f'1986-{record}.{i}' for i in range(1,len(xs)+1)]:
            errors.append('nonsequential item IDs '+str(record))
    for x in items:
        label=x['id']
        for k in required-set(x):errors.append(label+': missing '+k)
        for k,allowed in enum.items():
            if x.get(k) not in allowed:errors.append(label+': bad '+k+' '+str(x.get(k)))
        if x.get('class') in 'CD' and not x.get('worth'):errors.append(label+': missing development assessment')
        if x.get('problem') and x['problem'] not in pids:errors.append(label+': missing problem')
        if not re.search(r'2026|November',x.get('present_status','')):errors.append(label+': undated status')
        for page in re.findall(r'P(\d{6})',x['pages']):
            if not 1257<=int(page)<=1384:errors.append(label+': source page outside packet')
        cited=citekeys(' '.join(v for v in x.values() if isinstance(v,str)))
        missing=cited-set(x['refs'])
        if missing:errors.append(label+': cited key missing from refs '+str(missing))
        for key in x['refs']:
            if key not in bibs:errors.append(label+': missing bibliography '+key)
    for p in problems:
        if p['status_date']!='2026-11':errors.append(p['id']+': bad status month')
        for occurrence in p['occurrences']:
            if occurrence not in ids and occurrence not in oldids:errors.append(p['id']+': unknown occurrence '+occurrence)
        for key in p['refs']:
            if key not in bibs:errors.append(p['id']+': missing bibliography '+key)
    for key,entry in bibs.items():
        if not field(entry,'url') and not field(entry,'doi'):errors.append(key+': no URL or DOI')
        if field(entry,'note') not in {'verified','unverified'}:errors.append(key+': invalid verification note')
    if errors:
        raise ValueError('\n'.join(errors))

def main():
    talks,items,problems,corrections,bibs=load_parts()
    items,corrections=layout_adjustments(items,corrections)
    # Every current occurrence carrying a problem ID must be reachable from
    # that problem's index entry, including cross-slice recurrences.
    pmap={p['id']:p for p in problems}
    for x in items:
        pid=x.get('problem')
        if pid and pid in pmap:
            pmap[pid]['occurrences']=list(dict.fromkeys(pmap[pid]['occurrences']+[x['id']]))
    for p in problems:
        p['occurrences'].sort(key=lambda s:tuple(int(n) for n in re.findall(r'\d+',s)))
    problems.sort(key=lambda p:tuple(int(n) for n in re.findall(r'\d+',p['id'])))
    cumulative=bib_entries(CUMULATIVE.read_text())
    existing_doi={}
    for key,entry in cumulative.items():
        if doi(entry):existing_doi.setdefault(doi(entry),key)
    aliases={}
    for key,entry in list(bibs.items()):
        if key not in cumulative and doi(entry) in existing_doi:
            aliases[key]=existing_doi[doi(entry)]
    # Exact same-paper aliases across the three new slices.
    bydoi={}
    for key,entry in bibs.items():
        canonical=aliases.get(key,key)
        identity=doi(entry)
        if identity and identity in bydoi and canonical!=bydoi[identity]:
            aliases[key]=bydoi[identity]
        elif identity:bydoi[identity]=canonical
    # Flatten any two-step alias.
    for key in list(aliases):
        while aliases.get(aliases[key]) and aliases[aliases[key]]!=aliases[key]:
            aliases[key]=aliases[aliases[key]]
    rewritten={}
    for key,entry in bibs.items():
        new=aliases.get(key,key)
        entry=re.sub(r'(@\w+\s*\{\s*)'+re.escape(key)+r'(?=\s*,)',lambda m:m[1]+new,entry,count=1)
        if new not in rewritten:
            rewritten[new]=entry
        elif (field(entry,'note')=='verified',len(entry)) > (field(rewritten[new],'note')=='verified',len(rewritten[new])):
            rewritten[new]=entry
    bibs=rewritten
    # Plainnat cannot print both volume and number for a book/incollection.
    # Preserve both identifiers by putting the non-series number in its
    # appropriate descriptive field; bibliographic identity is unchanged.
    if 'soule1986regulateurs' in bibs:
        entry=bibs['soule1986regulateurs']
        entry=entry.replace(r'booktitle={S{\'e}minaire Bourbaki, 1984/85}',
                            r'booktitle={S{\'e}minaire Bourbaki, 1984/85, expos{\'e} 644}')
        entry=re.sub(r'\s*number\s*=\s*\{644\},?','',entry)
        bibs['soule1986regulateurs']=entry
    if 'zaslavsky1975facing' in bibs:
        entry=bibs['zaslavsky1975facing']
        entry=entry.replace('series = {Memoirs of the American Mathematical Society}',
                            'series = {Memoirs of the American Mathematical Society, vol. 1}')
        entry=re.sub(r'\s*volume\s*=\s*\{1\},?','',entry)
        bibs['zaslavsky1975facing']=entry
    talks=rewrite_citations(talks,aliases);items=rewrite_citations(items,aliases)
    problems=rewrite_citations(problems,aliases);corrections=rewrite_citations(corrections,aliases)
    for filename in ['GY1986_development.tex','GY1986_overview.tex']:
        path=OUT/filename
        if path.exists():path.write_text(rewrite_citations(path.read_text(),aliases))
    # Additional root citations are reused from the cumulative bibliography.
    needed=set()
    for x in items+problems:needed.update(x['refs'])
    for obj in talks+items+problems+corrections:
        needed.update(citekeys(' '.join(v for v in obj.values() if isinstance(v,str))))
    for filename in ['GY1986_development.tex','GY1986_overview.tex']:
        path=OUT/filename
        if path.exists():needed.update(citekeys(path.read_text()))
    for key in needed:
        if key not in bibs and key in cumulative:bibs[key]=cumulative[key]
    bibs['mccme2026gelfandcatalogue']="""@misc{mccme2026gelfandcatalogue,
  author = {{Moscow Center for Continuous Mathematical Education}},
  title = {Notes of the {I. M. Gelfand} seminar: chronological catalogue},
  year = {2026},
  url = {https://old.mccme.ru/gelfand/notes/all-links.html},
  annote = {Catalogue opened on 12 November 2026. The attached index supplies record-level metadata; manuscript conflicts are retained separately.},
  note = {verified}
}"""
    validate(talks,items,problems,corrections,bibs)
    for name,data in [('talks',talks),('items',items),('problems',problems)]:
        (OUT/f'GY1986_{name}.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    columns=['page','place','transcription_reads','should_read','evidence','applies_to','type']
    with (OUT/'GY1986_corrections.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=columns);writer.writeheader()
        writer.writerows({k:row.get(k,'') for k in columns} for row in corrections)
    (OUT/'GY1986_references.bib').write_text(
        '% Verified sources for GY1986; status cutoff 12 November 2026.\n'
        '% The note field records URL/DOI inspection, not proof certification.\n\n'+
        '\n\n'.join(bibs[k] for k in sorted(bibs))+'\n')
    kit=ROOT/'work'/'kit' if (ROOT/'work'/'kit').exists() else OUT/'code'/'kit_original'
    (OUT/'code'/'kit_original').mkdir(parents=True,exist_ok=True)
    for filename in ['build_chapter.py','gelfand_companion.sty','CHAPTER_FORMAT.md']:
        shutil.copy2(kit/filename,OUT/filename)
        original=OUT/'code'/'kit_original'/filename
        if (kit/filename).resolve()!=original.resolve():shutil.copy2(kit/filename,original)
    builder=OUT/'build_chapter.py'
    builder.write_text(builder.read_text().replace(
        r'\\setlength{\\emergencystretch}{2em}',
        r'\\setlength{\\emergencystretch}{4em}'))
    manifest=ROOT/'root_notes'/'input_manifest.json'
    if manifest.exists():shutil.copy2(manifest,OUT/'code'/'root'/'input_manifest.json')
    counts={'records':len(talks),'items':len(items),'problems':len(problems),'references':len(bibs),'corrections':len(corrections),
            'classes':dict(Counter(x['class'] for x in items)),
            'literal_correctness':dict(Counter(x['literal_correctness'] for x in items)),
            'verification':dict(Counter(x['verification'] for x in items)),
            'publication_match':dict(Counter(x['publication_match'] for x in items)),
            'development':dict(Counter(x['development'] for x in items)),
            'confidence':dict(Counter(x['confidence'] for x in items)),
            'bibliography_aliases':aliases,
            'unverified_references':[key for key,entry in bibs.items() if field(entry,'note')=='unverified']}
    (OUT/'code'/'root'/'assembly_counts.json').write_text(json.dumps(counts,indent=2))
    print(json.dumps(counts,indent=2))
    print('Strict assembly checks passed; all 46 catalogue records are present.')

if __name__=='__main__':
    main()

