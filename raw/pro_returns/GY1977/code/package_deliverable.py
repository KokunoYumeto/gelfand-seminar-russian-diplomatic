"""Package the single final download, including inputs, code and evidence.

Usage: python work/code/package_deliverable.py delivery/GY1977
Run only after final compilation, PDF review and report regeneration.
"""
from pathlib import Path
import hashlib,json,shutil,sys,zipfile

ROOT=Path(__file__).resolve().parents[2]
D=Path(sys.argv[1]).resolve()
CODE=D/'code';CODE.mkdir(exist_ok=True)
OUT=CODE/'output';OUT.mkdir(exist_ok=True)
for p in (ROOT/'work/code').glob('*.py'):shutil.copy2(p,CODE/p.name)
for p in (ROOT/'work/code/output').glob('*'):
    if p.is_file():shutil.copy2(p,OUT/p.name)

for part in ['early','middle','late','root']:
    src=ROOT/'work/parts'/part
    inputs=CODE/'editorial_inputs'/part;inputs.mkdir(parents=True,exist_ok=True)
    for name in ['talks.json','items.json','problems.json','areas.json','references.bib','references.json','corrections.csv','development.tex','overview.tex','coin_annotation.tex']:
        p=src/name
        if p.exists():shutil.copy2(p,inputs/name)
    for p in src.glob('*.json'):shutil.copy2(p,inputs/p.name)
    gens=CODE/'editorial_generators'/part;gens.mkdir(parents=True,exist_ok=True)
    for p in src.glob('*.py'):shutil.copy2(p,gens/p.name)
    logs=CODE/'research_logs';logs.mkdir(exist_ok=True)
    for name in ['research_log.md','review.md','report_review.md','laplacian_review.md','kp_review.md','bibliography_review.md','visual_review.md']:
        p=src/name
        if p.exists():shutil.copy2(p,logs/f'{part}_{name}')
    for p in src.glob('*check*.py'):shutil.copy2(p,CODE/p.name)
    for p in src.glob('*check*.json'):shutil.copy2(p,OUT/p.name)
    for p in src.glob('*verification*.py'):shutil.copy2(p,CODE/p.name)
    for p in src.glob('*verification*.json'):shutil.copy2(p,OUT/p.name)
    for p in src.glob('verify_*.py'):shutil.copy2(p,CODE/p.name)

supplied=CODE/'source_inputs';supplied.mkdir(exist_ok=True)
for name in ['GY1977_en.tex','GY1977_ru.tex','GY1977_talks.md','GY1977_prompt.md']:
    shutil.copy2(ROOT/'upload'/name,supplied/name)
for name in ['previous_index.md','references_cumulative.bib']:
    shutil.copy2(ROOT/'work'/name,supplied/name)
kit=supplied/'kit';kit.mkdir(exist_ok=True)
for name in ['build_chapter.py','gelfand_companion.sty','CHAPTER_FORMAT.md']:
    shutil.copy2(ROOT/'work/kit'/name,kit/name)
shutil.copy2(ROOT/'work/recovered_scans/GELFAND-P000722.png',OUT/'recovered_GELFAND-P000722.png')
runtime=CODE/'tex_runtime';runtime.mkdir(exist_ok=True)
for name in ['run_tex.py','README.md','runtime_manifest.json','bootstrap.log']:
    shutil.copy2(ROOT/'work/tex_runtime'/name,runtime/name)
smoke=runtime/'smoke';smoke.mkdir(exist_ok=True)
for name in ['smoke.tex','smoke.bib','smoke.pdf','smoke.log','smoke_checks.json']:
    p=ROOT/'work/tex_runtime/smoke'/name
    if p.exists():shutil.copy2(p,smoke/name)

readme=r'''# GY1977 — critical companion chapter

Read `GY1977_test.pdf` for the complete chapter. `GY1977_report.md` explains
scope, counts, provenance, methods, limitations and website presentation.
The packet includes 28 requested catalogue envelopes and adjacent material
from 1978–79; read each affected talk's provenance notice before using dates.

## Rebuild the chapter

From this directory, with Python 3, XeLaTeX and BibTeX installed:

```sh
python build_chapter.py GY1977
xelatex -interaction=nonstopmode -halt-on-error GY1977_test.tex
bibtex GY1977_test
xelatex -interaction=nonstopmode -halt-on-error GY1977_test.tex
xelatex -interaction=nonstopmode -halt-on-error GY1977_test.tex
python code/validate_chapter.py .
```

The style uses CMU Serif when available, otherwise DejaVu Serif. The original
supplied kit is preserved under `code/source_inputs/kit/`. Any local
typography amendments are documented in `code/output/build_validation.json`.
The canonical data are the top-level JSON/CSV/BibTeX and overview/development
files; do not edit the generated chapter by hand.

The working environment's installed TeX packages had missing lookup databases
and no format file. `code/tex_runtime/run_tex.py` repairs that situation using
workspace-local files only. If needed on a comparable Linux installation,
run `python code/tex_runtime/run_tex.py xelatex ...` and similarly for BibTeX.
No package download or system modification was needed for this chapter.

## Rerun the mathematical checks

Python dependencies: SymPy; Pillow for scan integrity and contact sheets;
pypdf for PDF inspection. The symbolic checks do not require internet access.

```sh
python code/check_jets.py
python code/check_kp.py
python code/check_laplacian.py
python code/coin_check.py
python code/verify_emendations.py
```

Additional Calogero verification scripts are included in `code/` and in the
late-range editorial generators. Their docstrings identify their outputs.
Existing outputs are under `code/output/`; the coin script writes its JSON
beside the script, as in the original working run. Exact arithmetic is used
where claimed. Finite checks are not substitutes for the general proofs.

## Editorial evidence and reassembly

- `code/editorial_inputs/` contains the completed per-range research fragments.
- `code/editorial_generators/` contains the record-writing scripts actually
  used in the working session. They preserve original workspace paths and
  are archival evidence, not the preferred public rebuild interface.
- `code/research_logs/` contains access/search decisions and the independent
  proof review. URLs and theorem locators are in the reference audit.
- `code/source_inputs/` contains the supplied text transcriptions, catalogue,
  task specification, previous index and cumulative bibliography.
- `code/output/` contains scientific results, counts, validation/build logs,
  the scan-recovery audit and the recovered P000722 image.

To reproduce the fragment assembly in a fresh output directory:

```sh
python code/assemble_fragments.py code/editorial_inputs reassembled code/source_inputs
python code/make_report.py reassembled
python code/repair_typesetting.py reassembled
```

Then rebuild from the generated canonical files as above. Final typography
repairs, if any, are also recorded as a deterministic code script.

The original 94-image scan ZIP is not duplicated here. `audit_scans.py` and
`recover_scan_722.py` retain their original workspace-layout assumptions:
place the original images in `scans/` and the scripts in `work/code/` beneath
one workspace root. Recovery additionally needs network access to MCCME.
The recovery script verifies the complete neighboring scans and that the
damaged attachment is a prefix of the recovered page; it does not overwrite
the original upload.

Downloaded research papers are cited, not redistributed. All source and
status assertions distinguish a full-result read from a metadata check.
The final status date is 10 November 2026. The explicit integral cohomology
development makes no claim of research priority.
'''
(D/'README.md').write_text(readme)
required=['GY1977_'+suffix for suffix in ['talks.json','items.json','problems.json','overview.tex','development.tex','corrections.csv','references.bib','report.md','chapter.tex','test.pdf']]
top=required+['GY1977_test.tex','build_chapter.py','gelfand_companion.sty','CHAPTER_FORMAT.md','README.md']
assert all((D/x).is_file() for x in top),'A required deliverable is missing'
validation=json.loads((OUT/'data_validation.json').read_text())
build=json.loads((OUT/'build_validation.json').read_text())
assert validation['result']=='PASS' and build['result']=='PASS'
assert 'to be recorded' not in (D/'GY1977_report.md').read_text()

def included():
    return sorted([D/x for x in top]+[p for p in CODE.rglob('*') if p.is_file() and '__pycache__' not in p.parts])

package_summary={'result':'PASS','required_files':required,'archive_crc_test':'passed',
                 'scope':'Single archive; canonical data, compiled PDF, reproducibility code and outputs.'}
(OUT/'package_validation.json').write_text(json.dumps(package_summary,indent=2)+'\n')
files=included()
manifest=''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.relative_to(D).as_posix()+'\n' for p in files)
(D/'MANIFEST.sha256').write_text(manifest)
files.append(D/'MANIFEST.sha256')
dest=D.parent/'GY1977.zip'
with zipfile.ZipFile(dest,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for p in files:z.write(p,p.relative_to(D).as_posix())
with zipfile.ZipFile(dest) as z:
    assert z.testzip() is None
    assert set(required)<=set(z.namelist())
print(json.dumps({'zip':str(dest),'files':len(files),'bytes':dest.stat().st_size,
                  'sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),'crc':'PASS'},indent=2))
