"""Collect the chapter's executable provenance without downloaded source PDFs."""
from pathlib import Path
import shutil
import json
import re

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'final'/'GY1981'
CODE=OUT/'code';CODE.mkdir(exist_ok=True)
RESEARCH=OUT/'research';RESEARCH.mkdir(exist_ok=True)

for name in ['bibtools.py','assemble_chapter.py','validate_chapter.py','make_report.py',
             'pdf_quality.py','final_quality.py','prepare_package.py','make_zip.py']:
    shutil.copy2(ROOT/name,CODE/name)
for name in ['references_cumulative.bib','previous_index.md','assembly_counts.json',
             'assembly_output.txt','assembly_console.txt','schema_validation.json',
             'report_generation.txt','pdf_quality_output.json']:
    if (ROOT/name).exists():shutil.copy2(ROOT/name,CODE/name)

for part in 'abcd':
    source=ROOT/'parts'/part
    target=CODE/'parts'/part
    for f in source.rglob('*'):
        if not f.is_file():continue
        rel=f.relative_to(source)
        if any(x in {'source_cache','scan_review','qa','__pycache__'} for x in rel.parts):continue
        allowed=(f.suffix in {'.py','.json','.csv','.bib','.tex','.md','.log'} or
                 f.suffix=='.txt' and any(t in f.name for t in ['output','console','validation']))
        if not allowed:continue
        dest=target/rel;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(f,dest)
    shutil.copy2(source/'research_log.md',RESEARCH/f'records_{part}_research_log.md')
for name in ['goldsheid_audit.md','aggregate_data_audit.md']:
    shutil.copy2(ROOT/'parts/b'/name,RESEARCH/name)

# Path-only portability repairs in the saved authoring scripts. The mathematics
# and exact arithmetic are unchanged; the original run used the workspace path.
for name in ['make_items.py','make_support.py']:
    f=CODE/'parts/b'/name;s=f.read_text()
    s=s.replace("p=Path('work/parts/b')","p=Path(__file__).resolve().parent")
    s=s.replace("Path('work/references_cumulative.bib')","(p.parents[1]/'references_cumulative.bib')")
    f.write_text(s)
f=CODE/'parts/b/audit_aggregate.py'
if f.exists():
    s=f.read_text().replace("ROOT=Path(__file__).resolve().parents[3]","ROOT=Path(__file__).resolve().parents[2]")
    s=s.replace("PARTS=ROOT/'work/parts'","PARTS=ROOT/'parts'")
    s=s.replace("ROOT/'work/previous_index.md'","ROOT/'previous_index.md'")
    f.write_text(s)

for sub in ['kit','kit_original']:
    target=CODE/sub;target.mkdir(exist_ok=True)
    for name in ['build_chapter.py','gelfand_companion.sty','CHAPTER_FORMAT.md']:
        shutil.copy2(ROOT/'kit'/name,target/name)

tex=CODE/'texenv';tex.mkdir(exist_ok=True)
for f in (ROOT/'texenv').iterdir():
    if f.is_file() and f.suffix in {'.sh','.md','.log','.json','.txt'}:
        shutil.copy2(f,tex/f.name)
smoke=tex/'smoke';smoke.mkdir(exist_ok=True)
for name in ['smoke.tex','smoke.bib','smoke.pdf']:
    shutil.copy2(ROOT/'texenv/smoke'/name,smoke/name)

verify=CODE/'verification';verify.mkdir(exist_ok=True)
for name in ['build_validation.log','latex_first.log','latex_second.log','latex_third.log',
             'latex_final.log','bibtex_output.log','GY1981_test.log','GY1981_test.blg']:
    shutil.copy2(OUT/name,verify/name)
shutil.copy2(ROOT/'final_fonts.txt',verify/'embedded_fonts.txt')
qa=verify/'pdf_qa';qa.mkdir(exist_ok=True)
for name in ['structure.json']:
    shutil.copy2(ROOT/'pdf_qa'/name,qa/name)
for f in (ROOT/'pdf_qa').glob('contact_*.png'):shutil.copy2(f,qa/f.name)
for f in (ROOT/'pdf_qa').glob('visual_review_*.md'):shutil.copy2(f,qa/f.name)
if (ROOT/'final_quality.json').exists():shutil.copy2(ROOT/'final_quality.json',verify/'final_quality.json')

readme=r'''# GY1981 — the Gelfand seminar, 1981–82

Start with **GY1981_test.pdf**, the complete 150-page critical companion, and
**GY1981_report.md**, the methods, counts and verification report. The two-page
overview is at the beginning of the PDF. Assessment date: 11 November 2026.

## Main files

| File | Purpose |
|---|---|
| GY1981_talks.json | All 30 records, in manuscript order |
| GY1981_items.json | 210 distinct mathematical occurrences |
| GY1981_problems.json | 17 linked problem entries |
| GY1981_overview.tex | Two-page year overview |
| GY1981_development.tex | Complete bounded developments and verification annotations |
| GY1981_corrections.csv | 134 corrections, ambiguities and provenance entries |
| GY1981_references.bib | 93 real references, with verification scope annotations |
| GY1981_report.md | Counts, findings, limits, method and website recommendations |
| GY1981_chapter.tex | Generated chapter for the common reader |
| GY1981_test.tex / GY1981_test.pdf | Stand-alone driver and compiled chapter |
| build_chapter.py / gelfand_companion.sty | Compatible builder and style |

`research/` contains the four source/literature logs and independent audits.
`code/parts/` contains the authoring snapshots, mathematical verification scripts
and their outputs. `code/verification/` records the final build and PDF checks.
Downloaded research PDFs and manuscript scan caches are deliberately absent.
The supplied cumulative bibliography and earlier index are retained under `code/`
to make key reuse and occurrence matching reproducible.

## Rebuild the delivered chapter

From this directory, with Python 3 and a complete TeX Live installation:

```bash
python3 build_chapter.py GY1981
xelatex -interaction=nonstopmode -halt-on-error GY1981_test.tex
bibtex GY1981_test
xelatex -interaction=nonstopmode -halt-on-error GY1981_test.tex
xelatex -interaction=nonstopmode -halt-on-error GY1981_test.tex
```

Repeat the last command if TeX requests another label pass. The bundled DejaVu
Serif files and license preserve the text font used for this PDF. The builder
prints all bibliography entries in the data through `\nocite{*}`. The style's
only change is explicit spacing after the proved/computed markers. The received
kit is preserved under `code/kit_original/`.

For the restricted TeX installation used in the research run, the executable and
packages existed but the default format databases did not. A reproducible local
repair, with no download or system modification, is supplied:

```bash
bash code/texenv/setup_tex.sh
source code/texenv/env.sh
```

Then use the standard build commands above. See `code/texenv/README.md` for the
diagnosis and smoke-test evidence. The generated binary format and caches are
not portable across TeX versions and are therefore regenerated, not archived.

## Validate and reproduce the mathematical checks

```bash
python3 code/validate_chapter.py .
python3 code/parts/a/editorial_checks.py
python3 code/parts/b/verify_annotations.py
python3 code/parts/b/verify_negative_cut.py
python3 code/parts/c/code/check_partition_and_metric.py
python3 code/parts/d/code/verify_root.py
```

The mathematical scripts use Python 3, SymPy, NumPy and SciPy where indicated.
The root run used NumPy 2.3.5, SciPy 1.17.0 and SymPy 1.14.0. Exact calculations
are separated from exploratory optimization. A numerical feasible gap is an
upper bound from one admissible phase choice, not a certified global minimum.
The saved outputs specify all tested ranges and seeds.

To regenerate the merged data from the saved record snapshots, use
`python3 code/assemble_chapter.py .`; then rebuild the chapter. To regenerate the
count tables use `python3 code/make_report.py .`. These are authoring operations
that replace the corresponding files. The normal PDF rebuild uses the delivered
final JSON, CSV and TeX directly and does not require rerunning research.

The PDF QA script additionally uses PyMuPDF and Pillow plus Poppler's `pdftoppm`.
It renders every page, records internal links and page bounds, and generates the
included contact sheets. All 210 item identifiers are present in the PDF. The
final quality record gives the clean citation, glyph and layout diagnostics.

The new proofs have no historical-priority claim. Their exact limits are stated
beside them: Goldsheid's 1/sqrt(2) bound fails, but existence of a larger universal
constant below one is not settled; Haefliger's equation is solved here in C0,
while the original C∞ assertions remain separate. The explicit negative-cut
Dirac example is an editorial verification of a false blanket notebook claim.
'''
(OUT/'README.md').write_text(readme)

# Intermediate TeX files are archived in the verification directory where useful;
# the root contains the clean inputs, the final BibTeX output and the final PDF.
for name in ['GY1981_test.aux','GY1981_test.out','GY1981_test.log','GY1981_test.blg',
             'build_validation.log','latex_first.log','latex_second.log','latex_third.log',
             'latex_final.log','bibtex_output.log']:
    p=OUT/name
    if p.exists():p.unlink()
print(json.dumps({'prepared_directory':str(OUT),'files_before_manifest':sum(p.is_file() for p in OUT.rglob('*')),
                  'downloaded_primary_pdfs_included':False,'fonts_and_license_included':True},indent=2))
