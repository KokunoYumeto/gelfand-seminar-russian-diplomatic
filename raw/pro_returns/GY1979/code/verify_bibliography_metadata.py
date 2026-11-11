#!/usr/bin/env python3
"""Check DOI registration metadata for otherwise inaccessible publisher records.

This verifies bibliographic identity, never an unread theorem or its proof.
No API key or private source is used. Full abstracts are deliberately not stored.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime,timezone
import json
import re
import urllib.request
from audit_chapter import bib_entries

D=Path(__file__).resolve().parent.parent
output_path=D/'code/bibliography_metadata_output.json'
existing={r['key']:r for r in json.loads(output_path.read_text())} if output_path.exists() else {}
targets=[]
for key,entry in bib_entries((D/'GY1979_references.bib').read_text()):
    if re.search(r'note\s*=\s*\{unverified\}',entry):
        doi=re.search(r'\bdoi\s*=\s*\{([^}]+)\}',entry).group(1)
        if existing.get(key,{}).get('result')!='PASS':targets.append((key,doi))

def fetch(target):
    key,doi=target
    url='https://api.crossref.org/works/'+doi
    result={'key':key,'queried_doi':doi,'opened_url':url,
            'accessed_at':datetime.now(timezone.utc).isoformat(),
            'verified_scope':'DOI registration metadata only; no original full proof read.'}
    try:
        request=urllib.request.Request(url,headers={'User-Agent':'GY1979-critical-companion/1.0'})
        with urllib.request.urlopen(request,timeout=25) as response:
            message=json.load(response)['message']
        result['http_status']=200
        result['metadata']={f:message.get(f) for f in
            ['DOI','title','author','container-title','volume','issue','page',
             'published','published-print','published-online','URL','publisher','type']}
        result['doi_matches']=message['DOI'].lower()==doi.lower()
        result['result']='PASS' if result['doi_matches'] else 'MISMATCH'
    except Exception as exc:
        result['result']='INACCESSIBLE'
        result['error']=type(exc).__name__+': '+str(exc)
    return result

with ThreadPoolExecutor(max_workers=4) as pool:
    results=list(pool.map(fetch,targets))
for row in results:
    previous=existing.get(row['key'])
    if previous:
        row['previous_attempts']=previous.get('previous_attempts',[])+[
            {k:previous.get(k) for k in ('accessed_at','result','error')}]
    existing[row['key']]=row
results=[existing[k] for k in sorted(existing)]
output_path.write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
print(json.dumps([{'key':r['key'],'result':r['result'],
                   'title':r.get('metadata',{}).get('title')} for r in results],ensure_ascii=False,indent=2))
