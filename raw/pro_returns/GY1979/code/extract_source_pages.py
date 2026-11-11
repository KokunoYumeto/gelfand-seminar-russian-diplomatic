#!/usr/bin/env python3
"""Reproduce the page split used to audit the user-supplied source files.

Usage: python code/extract_source_pages.py PATH_TO_ATTACHMENTS OUTPUT_DIR
The attached source and scan archives are inputs, not required for rebuilding
the finished chapter from the seven chapter data files.
"""
from pathlib import Path
import hashlib
import json
import re
import sys
import zipfile

src=Path(sys.argv[1]).resolve()
out=Path(sys.argv[2]).resolve()
out.mkdir(parents=True,exist_ok=True)
manifest=[]
for language in ('ru','en'):
    path=src/f'GY1979_{language}.tex'
    text=path.read_text()
    matches=list(re.finditer(r'\\SourcePage\{GELFAND-P(\d{6})\}',text))
    for i,match in enumerate(matches):
        page=int(match.group(1))
        if not 840<=page<=918:
            continue
        end=matches[i+1].start() if i+1<len(matches) else len(text)
        chunk=text[match.start():end]
        target=out/f'P{page:06d}_{language}.tex'
        target.write_text(chunk)
        manifest.append({'page':f'P{page:06d}','language':language,
                         'file':target.name,'sha256':hashlib.sha256(chunk.encode()).hexdigest()})
for archive in ('GY1979_kit.zip','GY1979_scans.zip'):
    path=src/archive
    with zipfile.ZipFile(path) as z:
        for info in z.infolist():
            destination=(out/info.filename).resolve()
            if not destination.is_relative_to(out):
                raise ValueError('Unsafe archive entry '+info.filename)
        z.extractall(out)
(out/'extraction_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({'page_fragments':len(manifest),'first_page':'P000840','last_page':'P000918',
                  'note':'Extraction preserves page envelopes, not talk attribution.'},indent=2))
