"""Export reproducibility materials without redistributing retrieved papers.

Full retrieval bodies remain working evidence; this deliverable includes
the queries, opened references, URLs, locators in the authored records, and
all original mathematical programs and their full computation outputs.
"""
from pathlib import Path
import json,re,shutil

OUT=Path(__file__).resolve().parents[2]
ROOT=OUT.parent

def extract_call(obj):
    if not isinstance(obj,dict):return None
    for a,b in [('q','r'),('args','result'),('query','result')]:
        if a in obj and b in obj:return obj[a],obj[b]
    return None

def summaries(result):
    texts=[]
    if isinstance(result,dict):
        for block in result.get('content',[]):
            if isinstance(block,dict) and block.get('type')=='text':texts.append(block.get('text',''))
    elif isinstance(result,str):texts=[result]
    body='\n'.join(texts)
    rows=[]
    for m in re.finditer(r'(?m)^([^\n]{0,450}) \((https?://[^\s]+)\)\n【([^】]+)】',body):
        title,url,ref=m.groups()
        rows.append({'source_ref':ref,'title':title,'url':url})
    urls=sorted(set(re.findall(r'https?://[^\s<>{}\"\\]+',body)))
    # Returned webpage text is intentionally not exported.
    failures=bool(re.search(r'Failed to fetch|not accessible via this tool|Internal Error|403 Forbidden',body))
    return rows,urls,failures

def sanitize(calls):
    parsed=[];refmap={}
    for name,obj in calls:
        call=extract_call(obj)
        if call is None:continue
        request,result=call
        sources,urls,failures=summaries(result)
        refmap.update({x['source_ref']:x['url'] for x in sources})
        parsed.append({'working_log':name,'request':request,'returned_source_metadata':sources,
                       'returned_urls':urls,'contains_fetch_failure':failures})
    for entry in parsed:
        request=entry['request']
        if isinstance(request,dict):
            opened=[]
            for spec in request.get('open') or []:
                ref=spec.get('ref_id','')
                opened.append({'requested_ref':ref,'resolved_url':ref if ref.startswith('http') else refmap.get(ref,'')})
            entry['open_requests']=opened
    return {'purpose':'Queries and source metadata; full third-party retrieval bodies are not redistributed.',
            'verification_caution':'An open request can fail. Bibliography notes and item verification levels distinguish successful metadata/result reading from unresolved leads.',
            'calls':parsed}

def main():
    target=OUT/'code'/'parts';target.mkdir(parents=True,exist_ok=True)
    all_calls=[]
    for label in ['A','B','C']:
        src=ROOT/'parts'/label;dst=target/label
        dst.mkdir(exist_ok=True)
        for name in ['talks.json','items.json','problems.json','corrections.csv','references.bib','research_notes.md']:
            if (src/name).exists():shutil.copy2(src/name,dst/name)
        for p in src.rglob('*'):
            if not p.is_file():continue
            relative=p.relative_to(src)
            if p.suffix=='.json':
                try:obj=json.loads(p.read_text())
                except (ValueError,UnicodeDecodeError):continue
                if extract_call(obj):
                    all_calls.append((str(Path(label)/relative),obj));continue
                if any(word in p.name for word in ['validation','inventory','witness','certificate','editorial_checks']):
                    dest=dst/relative;dest.parent.mkdir(parents=True,exist_ok=True)
                    shutil.copy2(p,dest)
            # Save original authored programs, their complete textual outputs,
            # and user-provided source excerpts. Exclude downloaded papers and
            # large scan copies, which remain with the original input packet.
            if p.suffix in {'.py','.out','.log'}:
                dest=dst/relative;dest.parent.mkdir(parents=True,exist_ok=True)
                if p.name=='read_suslin.out':
                    dest.write_text(
                        'Opened https://www.maths.dur.ac.uk/users/herbert.gangl/Suslin_K3_Bloch_group.pdf; 994999 bytes.\n'
                        'The original introduction and Theorem 5.2 were inspected.\n'
                        'Chronology excerpt (11 words): "Most of the results in this paper were obtained in 1982."\n'
                        'Full OCR text is omitted from distribution. Mathematical scope and bibliographic metadata are recorded in item 1986-712.15.\n'
                    )
                else:shutil.copy2(p,dest)
            if p.suffix=='.md':
                dest=dst/relative;dest.parent.mkdir(parents=True,exist_ok=True)
                shutil.copy2(p,dest)
            if p.name=='research_queries.jsonl':
                dest=dst/relative;dest.parent.mkdir(parents=True,exist_ok=True)
                shutil.copy2(p,dest)
            if p.name=='verification_ledger.csv':
                dest=dst/relative;dest.parent.mkdir(parents=True,exist_ok=True)
                shutil.copy2(p,dest)
            if relative.parts[0] in {'evidence','source'} and p.suffix in {'.tex','.txt'}:
                text=p.read_text()
                if '\\SourcePage{' in text:
                    dest=dst/relative;dest.parent.mkdir(parents=True,exist_ok=True)
                    shutil.copy2(p,dest)
        print('Exported',label,'authored data, programs, computation outputs, and source excerpts.')
    seen_root_calls=set()
    for raw in sorted((ROOT/'root_notes').glob('root_research_*.json')):
        for i,obj in enumerate(json.loads(raw.read_text()),1):
            call=extract_call(obj)
            signature=json.dumps(call[0],sort_keys=True) if call else ''
            if call and signature not in seen_root_calls:
                seen_root_calls.add(signature)
                all_calls.append((f'root/{raw.stem}/call_{i:03d}',obj))
    ledger=sanitize(all_calls)
    (OUT/'code'/'root'/'research_log.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n')
    metadata=OUT/'code'/'source_metadata';metadata.mkdir(exist_ok=True)
    for name in ['previous_index.md','references_cumulative.bib']:
        shutil.copy2(ROOT/'work'/name,metadata/name)
    for source,targetname in [('GY1986_prompt(2).md','task_prompt.md'),('GY1986_talks(2).md','catalogue_records.md')]:
        shutil.copy2(ROOT/'upload'/source,metadata/targetname)
    print('Sanitized retrieval calls:',len(ledger['calls']))
    print('Full retrieved third-party paper texts are excluded; computation outputs are complete.')

if __name__=='__main__':
    main()

