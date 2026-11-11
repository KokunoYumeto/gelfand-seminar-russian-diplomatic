#!/usr/bin/env python3
"""Create and verify the deliverable archive from this chapter directory.

Usage: python code/package_chapter.py . /path/to/GY1965.zip
The archive stores files directly at its root and excludes build temporaries.
"""
from pathlib import Path
import hashlib
import json
import sys
import zipfile

root = Path(sys.argv[1]).resolve()
destination = Path(sys.argv[2]).resolve()
required = [f'GY1965_{suffix}' for suffix in (
    'talks.json','items.json','problems.json','overview.tex','development.tex',
    'corrections.csv','references.bib','report.md','chapter.tex','test.pdf')]
for name in required:
    if not (root/name).is_file():
        raise SystemExit(f'Missing required deliverable: {name}')
excluded_suffixes = {'.aux','.out','.pyc'}
def include(path):
    relative = path.relative_to(root)
    if any(p in {'__pycache__','build-work'} for p in relative.parts):
        return False
    if relative.name == 'MANIFEST.sha256' or path.suffix in excluded_suffixes:
        return False
    if len(relative.parts)==1 and path.suffix in {'.log','.blg'}:
        return False
    return path.is_file() and path != destination

files = sorted((p for p in root.rglob('*') if include(p)),key=lambda p:p.relative_to(root).as_posix())
manifest = root/'MANIFEST.sha256'
manifest.write_text(''.join(f'{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.relative_to(root).as_posix()}\n' for p in files))
files.append(manifest)
destination.parent.mkdir(parents=True,exist_ok=True)
with zipfile.ZipFile(destination,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as archive:
    for path in files:
        archive.write(path,path.relative_to(root).as_posix())
with zipfile.ZipFile(destination) as archive:
    bad=archive.testzip()
    assert bad is None, bad
    entries=archive.namelist()
    assert len(entries)==len(set(entries))
    assert all(name in entries for name in required)
    assert all(not name.startswith('/') and '..' not in Path(name).parts for name in entries)
    for line in archive.read('MANIFEST.sha256').decode().splitlines():
        expected,name=line.split('  ',1)
        assert hashlib.sha256(archive.read(name)).hexdigest()==expected,name
print(json.dumps({'archive':destination.name,'files':len(files),'bytes':destination.stat().st_size,
                  'sha256':hashlib.sha256(destination.read_bytes()).hexdigest(),
                  'required_deliverables':len(required),'crc':'PASS','manifest':'PASS'},indent=2))
