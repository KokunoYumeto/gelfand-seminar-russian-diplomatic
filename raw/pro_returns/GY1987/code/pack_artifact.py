#!/usr/bin/env python3
"""Stage the completed edition and its reproducibility records, then zip it.

Run in the research workspace: python code/pack_artifact.py
The package's seven data files are authoritative; historical authoring
scripts are retained separately from the portable rebuild/check scripts.
"""
import hashlib
import json
from pathlib import Path
import shutil
import sys
import zipfile

WORK=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path(__file__).resolve().parents[1]
OUT=WORK/'output'
STAGE=WORK.parent/'GY1987_package'
ARCHIVE=WORK.parent/'GY1987.zip'

def digest(path):
    h=hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda:stream.read(1048576),b''):h.update(block)
    return h.hexdigest()

def copy(src,rel):
    dest=STAGE/rel
    dest.parent.mkdir(parents=True,exist_ok=True)
    shutil.copy2(src,dest)

required=['GY1987_talks.json','GY1987_items.json','GY1987_problems.json',
 'GY1987_overview.tex','GY1987_development.tex','GY1987_corrections.csv',
 'GY1987_references.bib','GY1987_report.md','GY1987_chapter.tex',
 'GY1987_test.pdf','GY1987_test.tex','build_chapter.py',
 'gelfand_companion.sty','CHAPTER_FORMAT.md','GY1987_test.bbl']
for name in required:
    if not (OUT/name).is_file():raise FileNotFoundError(name)
for name in ['data_audit.json','reference_identity_audit.json','build_commands.json','pdf_audit.json']:
    data=json.loads((OUT/'logs'/name).read_text())
    if data['status']!='PASS':raise RuntimeError(f'Failed final audit: {name}')
if not (OUT/'logs'/'visual_review.json').is_file():
    raise RuntimeError('The final visual review must be recorded before packaging')

STAGE.mkdir(exist_ok=True)
for name in required:copy(OUT/name,name)
for p in (OUT/'logs').iterdir():
    if p.is_file() and 'checkpoint' not in p.name:copy(p,Path('logs')/p.name)
for name in ['GY1987_test.log','GY1987_test.blg']:
    copy(OUT/name,Path('logs')/name)
for name in ['development_checks.json','early_checks.json','early_checks_stdout.txt',
 'early_checks_root_rerun.txt','early_schema_audit.json','integration_final.json',
 'reference_identity_final.json','report_final.json']:
    copy(WORK/'logs'/name,Path('logs')/name)

portable=['integrate_and_audit.py','audit_reference_identity.py','build_document.py',
 'inspect_pdf.py','verify_development.py','early_checks.py','write_overview_report.py',
 'pack_artifact.py']
for name in portable:copy(WORK/'code'/name,Path('code')/name)
for p in (WORK/'code').glob('*.py'):
    if p.name not in portable:copy(p,Path('research/authoring/code')/p.name)
for p in (WORK/'shards').glob('*.py'):
    copy(p,Path('research/authoring/shards')/p.name)

for prefix in ['early','middle','late']:
    for suffix in ['talks.json','items.json','problems.json','corrections.csv','references.bib']:
        name=f'{prefix}_{suffix}'
        copy(WORK/'shards'/name,Path('research/authoring/shards')/name)
    copy(WORK/'shards'/f'{prefix}_research.md',Path('research')/f'{prefix}_research.md')
for name in ['early_areas.json','early_record_areas.json','early_existing_bib.json',
 'late_areas.json','late_crossref.json','root_overrides.json','root_layout_patches.json',
 'root_correction_formats.json','root_references.bib']:
    copy(WORK/'shards'/name,Path('research/authoring/shards')/name)
for name in ['root_research.md','late_peer_review.md']:
    copy(WORK/'shards'/name,Path('research')/name)
for name in ['late_validation.json','middle_validation.txt']:
    copy(WORK/'shards'/name,Path('logs')/name)
copy(WORK/'shards/primary/download_log.txt','logs/primary_download_log.txt')
copy(WORK/'qa/GY1987_extracted.txt','logs/GY1987_pdf_text.txt')

inputs=[]
for p in sorted((WORK.parent/'upload').iterdir()):
    if p.is_file():inputs.append({'filename':p.name,'bytes':p.stat().st_size,'sha256':digest(p)})
(STAGE/'research/source_manifest.json').write_text(json.dumps({
 'scope':'Only the attachments supplied for this conversation; hashes identify inputs, not claims of authorship.',
 'files':inputs},indent=2)+'\n')

readme='''# GY1987 — critical companion, 1987–88

Start with **GY1987_test.pdf** for the complete typeset chapter or
**GY1987_report.md** for the editorial findings and quantitative audit.
The seven files specified by CHAPTER_FORMAT.md are at the archive root.
They cover all 38 records in source order, 287 mathematical occurrences,
27 indexed problems, 99 references and 85 corrections/critical annotations.
The status date is 11 November 2026.

## Rebuild

Use Python 3 and a normal TeX Live installation with XeLaTeX, BibTeX,
fontspec, the standard AMS/natbib/hyperref packages and DejaVu Serif:

```sh
python build_chapter.py GY1987
xelatex -interaction=nonstopmode -halt-on-error GY1987_test.tex
bibtex GY1987_test
xelatex -interaction=nonstopmode -halt-on-error GY1987_test.tex
xelatex -interaction=nonstopmode -halt-on-error GY1987_test.tex
```

`python code/build_document.py .` runs that sequence, resolves any remaining
cross-reference rerun request, and logs every command. It also contains the
documented private-format workaround used on the research host; it changes
no system installation. The supplied builder and style are unchanged.

## Recheck data and calculations

```sh
python code/integrate_and_audit.py --directory .
python code/verify_development.py > logs/development_checks.json
python code/early_checks.py > logs/early_checks_stdout.txt
python code/inspect_pdf.py . --render
```

The mathematical checks require NumPy and SymPy. The PDF audit requires
PyMuPDF and Pillow. Exact versions are recorded with the outputs.
Finite numerical diagnostics support, and do not replace, the full proofs.
The early checks intentionally retain counterexamples to false printed
formulas; a diagnostic counterexample is not a failed corrected theorem.

## Evidence and production history

- `research/` contains source maps, opened-source/locator ledgers,
  bounded-search qualifications and the independent mathematical review.
- `logs/` contains the final schema, bibliography-identity, computation,
  build and page-layout results, plus the extracted text of this edition.
- `research/authoring/` preserves authoring scripts and their frozen shard
  outputs. Some historical scripts use the original workspace layout or
  original attachments. These scripts are provenance, not a substitute
  for the authoritative root files; final integration overrides are retained.
- The cumulative-key comparison requires the separately supplied
  references_cumulative.bib and previous_index.md. Its completed result is
  included in logs/reference_identity_audit.json and the integration audit.
- Original scan archives, source transcriptions, downloaded research papers,
  full-paper OCR, model/runtime caches and private TeX formats are omitted.
  Download/OCR scripts remain available; their factual findings and checked
  locators are preserved in the research ledgers. External sources retain
  their own rights and availability conditions.
- `research/source_manifest.json` identifies the supplied inputs by hashes.
  `checksums.sha256` verifies every payload file except itself.

The bibliography marks 97 entries verified and two unverified. Here
“verified” means that a link or DOI was opened; the per-entry annotations
and per-item assessment state whether the actual result, only metadata,
or an indirect attribution was read. No new-priority claim is made for the
four worked developments/annotations.
'''
(STAGE/'README.md').write_text(readme)

payload=sorted(p for p in STAGE.rglob('*') if p.is_file() and p.name not in ['checksums.sha256','package_manifest.json'])
manifest={'status':'PASS','archive_name':ARCHIVE.name,'files_before_manifest_and_checksums':len(payload),
 'files':[{'path':str(p.relative_to(STAGE)),'bytes':p.stat().st_size,'sha256':digest(p)} for p in payload]}
(STAGE/'logs/package_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
payload=sorted(p for p in STAGE.rglob('*') if p.is_file() and p.name!='checksums.sha256')
(STAGE/'checksums.sha256').write_text(''.join(digest(p)+'  '+str(p.relative_to(STAGE))+'\n' for p in payload))
with zipfile.ZipFile(ARCHIVE,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for p in sorted(STAGE.rglob('*')):
        if p.is_file():z.write(p,str(p.relative_to(STAGE)))
with zipfile.ZipFile(ARCHIVE) as z:
    bad=z.testzip()
    if bad:raise RuntimeError('ZIP CRC failure: '+bad)
    names=z.namelist()
    if any(name.startswith('/') or '..' in Path(name).parts for name in names):
        raise RuntimeError('Unsafe archive member')
summary={'status':'PASS','archive':str(ARCHIVE),'files':len(names),'bytes':ARCHIVE.stat().st_size,
 'sha256':digest(ARCHIVE),'required_files_present':all(x in names for x in required)}
print(json.dumps(summary,indent=2))
