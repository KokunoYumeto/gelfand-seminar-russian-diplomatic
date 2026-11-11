#!/usr/bin/env python3
"""Package the completed chapter and verify the resulting ZIP's integrity."""
from pathlib import Path
import argparse
import hashlib
import json
import re
import zipfile

REQUIRED=[
    'GY1982_talks.json','GY1982_items.json','GY1982_problems.json',
    'GY1982_overview.tex','GY1982_development.tex','GY1982_corrections.csv',
    'GY1982_references.bib','GY1982_report.md','GY1982_chapter.tex',
    'GY1982_test.tex','GY1982_test.pdf','build_chapter.py','gelfand_companion.sty',
    'README.md','code/validation_statistics.json','code/editorial_audit.json',
    'code/source_coverage.json','code/pdf_geometry.json','code/visual_review.json',
    'code/build_logs/build_manifest.json','code/haar_check_results.json',
]


def include(path):
    if any(p in {'__pycache__','tex_cache','render','rendered_pages'} for p in path.parts):return False
    if path.suffix in {'.pyc','.fmt','.aux','.out','.toc','.synctex','.fls','.fdb_latexmk'}:return False
    if path.name in {'MANIFEST.json'}:return False
    # The final compilation log is available in the recorded build output.
    if path.suffix in {'.log','.blg'} and len(path.parts)==1:return False
    return True


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--directory',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    root=args.directory.resolve()
    missing=[name for name in REQUIRED if not (root/name).is_file() or (root/name).stat().st_size==0]
    if missing:raise SystemExit('Missing required completed files: '+', '.join(missing))
    stats=json.loads((root/'code/validation_statistics.json').read_text())
    audit=json.loads((root/'code/editorial_audit.json').read_text())
    build=json.loads((root/'code/build_logs/build_manifest.json').read_text())
    coverage=json.loads((root/'code/source_coverage.json').read_text())
    geometry=json.loads((root/'code/pdf_geometry.json').read_text())
    visual=json.loads((root/'code/visual_review.json').read_text())
    if stats['errors'] or audit['errors'] or build['unresolved_diagnostics'] or build['overfull_boxes']:
        raise SystemExit('Unresolved validation or layout diagnostics.')
    if coverage['uncovered_pages'] or coverage['out_of_year_item_pages']:
        raise SystemExit('Unresolved source-page coverage issue.')
    if not geometry['automated_pass'] or visual['result']!='PASS':
        raise SystemExit('PDF verification is incomplete.')
    if visual['pdf_sha256']!=hashlib.sha256((root/'GY1982_test.pdf').read_bytes()).hexdigest():
        raise SystemExit('Visual review does not identify the final PDF.')
    for name in ['GY1982_overview.tex','GY1982_development.tex','GY1982_report.md','GY1982_chapter.tex']:
        if re.search(r'@@[A-Z_]+@@',(root/name).read_text()):
            raise SystemExit('Template placeholder remains in '+name)
    files=sorted(p for p in root.rglob('*') if p.is_file() and include(p.relative_to(root)))
    manifest={
        'task':'GY1982','status_date':'2026-11',
        'records':stats['records'],'items':stats['items'],'problems':stats['problems'],
        'pdf_pages':geometry['pages'],
        'note':'Hashes cover every packaged file except MANIFEST.json itself.',
        'files':[{'path':p.relative_to(root).as_posix(),'bytes':p.stat().st_size,
                  'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in files],
    }
    manifest_path=root/'MANIFEST.json'
    manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    files.append(manifest_path)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(args.output,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as archive:
        for path in files:archive.write(path,path.relative_to(root).as_posix())
    with zipfile.ZipFile(args.output) as archive:
        bad=archive.testzip()
        if bad:raise SystemExit('Corrupt ZIP member: '+bad)
        for entry in manifest['files']:
            data=archive.read(entry['path'])
            if len(data)!=entry['bytes'] or hashlib.sha256(data).hexdigest()!=entry['sha256']:
                raise SystemExit('ZIP content mismatch: '+entry['path'])
    result={'result':'PASS','archive':args.output.name,'members':len(files),
            'bytes':args.output.stat().st_size,
            'sha256':hashlib.sha256(args.output.read_bytes()).hexdigest(),
            'records':stats['records'],'items':stats['items'],'pdf_pages':geometry['pages']}
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
