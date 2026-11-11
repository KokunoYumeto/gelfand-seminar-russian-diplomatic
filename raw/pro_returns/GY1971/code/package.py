#!/usr/bin/env python3
"""Create the single delivery archive and verify every archived file hash."""
import hashlib
import json
import pathlib
import zipfile


def main():
    root=pathlib.Path(__file__).resolve().parents[1]
    target=root.parent/'GY1971.zip'
    required=['talks.json','items.json','problems.json','overview.tex',
              'development.tex','corrections.csv','references.bib','report.md',
              'chapter.tex','test.pdf','test.tex']
    for suffix in required:
        if not (root/('GY1971_'+suffix)).is_file():
            raise RuntimeError('Missing required deliverable: '+suffix)
    skip_files={'audit/package_validation.json','audit/deliverable_manifest.json'}
    files=[p for p in sorted(root.rglob('*')) if p.is_file()
           and '.build-cache' not in p.parts and '__pycache__' not in p.parts
           and p.suffix!='.pyc' and 'preliminary' not in p.name
           and str(p.relative_to(root)) not in skip_files]
    manifest=[{'path':str(p.relative_to(root)), 'bytes':p.stat().st_size,
               'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in files]
    mpath=root/'audit'/'deliverable_manifest.json'
    mpath.write_text(json.dumps(manifest,indent=2)+'\n')
    files.append(mpath)
    with zipfile.ZipFile(target,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for p in files:
            z.write(p,arcname=str(p.relative_to(root)))
    with zipfile.ZipFile(target) as z:
        bad=z.testzip()
        if bad:raise RuntimeError('ZIP integrity failure: '+bad)
        for row in manifest:
            digest=hashlib.sha256(z.read(row['path'])).hexdigest()
            if digest!=row['sha256']:
                raise RuntimeError('Hash mismatch: '+row['path'])
        count=len(z.namelist())
    validation={'files_after_adding_this_report':count+1,
                'zip_integrity':'passed','all_manifest_hashes':'passed',
                'required_deliverables':'present'}
    validation_path=root/'audit'/'package_validation.json'
    validation_path.write_text(json.dumps(validation,indent=2)+'\n')
    with zipfile.ZipFile(target,'a',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        z.write(validation_path,arcname='audit/package_validation.json')
    with zipfile.ZipFile(target) as z:
        if z.testzip():raise RuntimeError('Final ZIP integrity failure')
    result={'archive':target.name,'bytes':target.stat().st_size,
            'sha256':hashlib.sha256(target.read_bytes()).hexdigest(),
            'files':count+1,'zip_integrity':'passed','all_manifest_hashes':'passed',
            'required_deliverables':'present'}
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
