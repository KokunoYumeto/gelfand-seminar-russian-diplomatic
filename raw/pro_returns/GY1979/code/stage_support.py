#!/usr/bin/env python3
"""Preserve authoring inputs, outputs and independent reviews for the final ZIP."""
from pathlib import Path
import hashlib,json,shutil,sys
import sympy,mpmath
D=Path(__file__).resolve().parent.parent
source=D.parent/'parts'
copied=[]
if source.exists():
    for batch in ('early','middle','late'):
        target=D/'code/authoring'/batch;target.mkdir(parents=True,exist_ok=True)
        for path in (source/batch).iterdir():
            if path.is_file() and path.suffix in {'.py','.json','.csv','.bib','.md'}:
                shutil.copy2(path,target/path.name);copied.append(str((target/path.name).relative_to(D)))
    for batch,name in [('late','proof_review.md'),('middle','independent_early_review.md'),
                       ('early','integration_review.md')]:
        p=source/batch/name
        if p.exists():shutil.copy2(p,D/'code'/name)
    # Executable independent checks remain with their sibling early input JSON.
    for name in ('independent_early_checks.py','independent_early_checks.json'):
        (D/'code'/name).unlink(missing_ok=True)
    later=source/'late/boundary_inventory.md'
    if later.exists():
        intro=(D/'code/carry_in_inventory.md').read_text()
        (D/'code/boundary_inventory.md').write_text(intro+'\n\n---\n\n'+later.read_text())
kit=D.parent/'kit'
if kit.exists():
    target=D/'code/kit_original';target.mkdir(exist_ok=True)
    for name in ('build_chapter.py','gelfand_companion.sty','CHAPTER_FORMAT.md'):
        shutil.copy2(kit/name,target/name)
uploads=D.parent/'upload'
manifest=[]
if uploads.exists():
    for path in sorted(uploads.iterdir()):
        if path.is_file():
            manifest.append({'name':path.name,'bytes':path.stat().st_size,
                             'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
    (D/'code/input_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
runtime={'python':sys.version,'sympy':sympy.__version__,'mpmath':mpmath.__version__}
(D/'code/runtime_versions.json').write_text(json.dumps(runtime,indent=2)+'\n')
print(json.dumps({'authoring_files_copied':len(copied),'input_files_hashed':len(manifest),
                  'runtime':runtime},indent=2))
