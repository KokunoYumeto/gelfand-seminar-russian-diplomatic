#!/usr/bin/env python3
"""Package the finished chapter, reproducible calculations and audit records.

No source scans or downloaded reference PDFs are redistributed. The seven
required data files and the compiled PDF are at the archive root.
"""
from pathlib import Path
import argparse
import hashlib
import json
import shutil
import zipfile


REQUIRED = [
    'GY1975_talks.json', 'GY1975_items.json', 'GY1975_problems.json',
    'GY1975_overview.tex', 'GY1975_development.tex', 'GY1975_corrections.csv',
    'GY1975_references.bib', 'GY1975_report.md', 'GY1975_chapter.tex',
    'GY1975_test.tex', 'GY1975_test.pdf',
]

parser = argparse.ArgumentParser()
parser.add_argument('--workspace', type=Path,
                    default=Path(__file__).resolve().parent.parent)
parser.add_argument('--chapter', type=Path)
parser.add_argument('--destination', type=Path, required=True)
parser.add_argument('--archive', type=Path, required=True)
parser.add_argument('--attachments', type=Path)
args = parser.parse_args()
base = args.workspace.resolve()
chapter = (args.chapter or base / 'chapter').resolve()
dest = args.destination.resolve()
archive = args.archive.resolve()
if dest == base or dest == chapter:
    raise SystemExit('Destination must be a distinct staging directory.')
if dest.exists() and any(dest.iterdir()):
    raise SystemExit('Staging directory must be empty; select a fresh destination.')
dest.mkdir(parents=True, exist_ok=True)


def copy(source, target):
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)


for name in REQUIRED + ['build_chapter.py', 'gelfand_companion.sty', 'CHAPTER_FORMAT.md']:
    copy(chapter / name, dest / name)
for name in ['GY1975_test.bbl']:
    if (chapter / name).exists():
        copy(chapter / name, dest / name)
for folder in ['computations', 'kit']:
    shutil.copytree(base / folder, dest / folder)
shutil.copytree(chapter / 'build_logs', dest / 'build_logs')
shutil.copytree(chapter / 'audit', dest / 'audit')
for path in (base / 'code').glob('*.py'):
    copy(path, dest / 'code' / path.name)
for path in (base / 'fragments').iterdir():
    if path.suffix not in {'.py', '.json', '.csv', '.bib', '.tex', '.md'}:
        continue
    if path.name.endswith(('_en.tex', '_ru.tex')) or path.name == 'b_checks_output.json':
        continue
    copy(path, dest / 'fragments' / path.name)
for name in ['previous_index.md', 'references_cumulative.bib']:
    copy(base / name, dest / name)

# Preserve the author's original code placement while replacing execution-
# workspace paths by paths relative to each script. These are path edits only.
path_edits = {
    'code/a_author.py': [
        ("ROOT=Path('/workspace/scratch/86f2b069d3ff')", 'ROOT=Path(__file__).resolve().parent.parent'),
        ("OUT=ROOT/'work/fragments'", "OUT=ROOT/'fragments'"),
    ],
    'fragments/b_author.py': [
        ("P=Path('work/fragments')", 'P=Path(__file__).resolve().parent'),
    ],
    'fragments/c_build.py': [
        ("OUT=Path('/workspace/scratch/86f2b069d3ff/work/fragments')", 'OUT=Path(__file__).resolve().parent'),
    ],
    'fragments/c_bibliography.py': [
        ("P=Path('/workspace/scratch/86f2b069d3ff/work/fragments')", 'P=Path(__file__).resolve().parent'),
    ],
    'fragments/c_source_ledger.py': [
        ("P=Path('/workspace/scratch/86f2b069d3ff/work/fragments')", 'P=Path(__file__).resolve().parent'),
    ],
}
applied = []
for name, edits in path_edits.items():
    path = dest / name
    text = path.read_text()
    for old, new in edits:
        if old not in text:
            raise ValueError(f'Expected path edit absent in {name}: {old}')
        text = text.replace(old, new)
        applied.append({'file': name, 'old': old, 'new': new})
    path.write_text(text)
(dest / 'audit/packaging_path_edits.json').write_text(json.dumps(applied, indent=2) + '\n')

attachments = (args.attachments or base.parent / 'upload').resolve()
if attachments.is_dir():
    input_manifest = []
    for path in sorted(attachments.iterdir()):
        if path.is_file():
            input_manifest.append({'name': path.name, 'bytes': path.stat().st_size,
                'sha256': hashlib.sha256(path.read_bytes()).hexdigest()})
    (dest / 'audit/input_manifest.json').write_text(json.dumps(input_manifest, indent=2) + '\n')
    if (attachments / 'GY1975_talks.md').exists():
        copy(attachments / 'GY1975_talks.md', dest / 'inputs/GY1975_talks.md')

readme = '''# GY1975: critical companion to the 1975–76 Gelfand seminar

Start with **GY1975_test.pdf** for the complete chapter and
**GY1975_report.md** for the research method, counts, limitations, and website
recommendations. The status date is **10 November 2026**.

The archive contains all 34 catalogue records, 256 mathematical occurrences,
20 problem entries, 90 references, and 91 corrections or qualifications.
The overview occupies the first two pages; the two bounded developments,
problem index, correction apparatus, and bibliography follow the occurrences.

## Files and provenance

The seven required data files are at the archive root. The generated chapter,
test driver, PDF and BibTeX output are supplied alongside them. The original
builder, style and format specification are unchanged, with matching copies
under `kit/`. The supplied earlier-year index and cumulative bibliography are
included as assembly inputs. The source catalogue is under `inputs/`.

`code/` contains build, assembly, audit, and mathematical programs.
`computations/` contains their mathematical outputs. `fragments/` preserves
the authored blocks, development text, templates, and source-ledger programs.
`audit/` contains count tables, exact source-page coverage, bibliography/source
ledgers, research logs, PDF checks, and hashes. `build_logs/` contains the actual
XeLaTeX, BibTeX and builder output.

The original notebook scans and full Russian/English transcriptions remain
the supplied source inputs; they are not duplicated here. Downloaded external
reference PDFs and failed web responses are not included. Source URLs and
verification limits remain in the bibliography and ledgers. Search reference
IDs in research logs are historical retrieval identifiers, not portable URLs;
use the recorded URLs for access.

## Rebuild the chapter

From this directory, with Python and a complete XeLaTeX/BibTeX installation:

```sh
python build_chapter.py GY1975
xelatex GY1975_test
bibtex GY1975_test
xelatex GY1975_test
xelatex GY1975_test
```

Alternatively, `python code/build_pdf.py --directory .` runs the sequence,
records logs, and repeats LaTeX if cross-references require another pass.
Its process-local fallback addresses this execution image's missing TeX
filename database and format; it does not change system files or the style.
A font with Cyrillic coverage is required by the supplied style.

The independent structural audit is:

```sh
python code/audit_chapter.py . --catalog inputs/GY1975_talks.md --previous-index previous_index.md
```

Two intentional source-range notices concern 383.11–12: the manuscript
continues onto P000641 while the catalogue envelope ends at P000640. The
record retains the catalogue envelope and the items retain their actual pages.

To reassemble the authored fragments before building:

```sh
python code/integrate_chapter.py --source fragments --output . --cumulative references_cumulative.bib
python code/create_report.py --chapter . --fragments fragments
```

Do not edit the generated chapter directly. Normal scholarly revisions belong
in the data or authored fragments. Assembly reapplies the recorded correction
formatting and rebuilds counts.

## Reproduce the mathematics

The integer Euler-product computation uses the Python standard library:

```sh
python code/perchik_series.py --max-m 40 --output computations/m40
python code/perchik_series.py --max-m 90 --output computations/m90
python code/perchik_series.py --max-m 150 --output computations/m150
python code/verify_perchik.py
python code/a_tau_check.py
python code/spectral_phase_check.py
python code/b_checks.py
```

Each Euler run compares every retained Laurent coefficient from two different
algorithms. The m=150 run takes longer than the smaller runs. The independent
audit compares the saved prefixes and numerical claims. The tau checks are
finite, through n=50. The final program requires SymPy and mpmath; its symbolic
operator identities are exact, while its Abel quadrature is numerical. The
spectral-phase floating-point checks supplement the written proofs and are
not interval-arithmetic certificates. No finite calculation proves the
unbounded nonvanishing or general spectral-convergence questions.

The programs were run with Python 3.12.14, SymPy 1.14.0 and mpmath 1.3.0.
`code/requirements-math.txt` records the two nonstandard mathematical packages.
For optional PDF QA, `python code/pdf_audit.py .` requires Poppler's pdftoppm,
PyMuPDF and Pillow; exact tested versions are in `audit/pdf_audit.json`.

## Integrity and interpretation

`audit/manifest.sha256` records SHA-256 hashes for every other packaged file.
The archive's ZIP CRC was checked after creation. The assessment fields separate
literal correctness, publication match, verification, development and confidence.
Class F records an identification limit. Class C specifies a residual question;
it is not inferred merely from a failed search. Chronology qualifications,
including the provisional Perchik dissertation classification, are explicit.
'''
(dest / 'README.md').write_text(readme)
(dest / 'code/requirements-math.txt').write_text('sympy==1.14.0\nmpmath==1.3.0\n')

assert all((dest / name).is_file() for name in REQUIRED)
assert json.loads((dest / 'audit/data_audit.json').read_text())['passed']
assert json.loads((dest / 'audit/pdf_audit.json').read_text())['automated_pass']
assert json.loads((dest / 'audit/final_build_audit.json').read_text())['visual_review_passed']
assert 'pending in this authoring snapshot' not in (dest / 'GY1975_report.md').read_text()
assert '@@' not in (dest / 'GY1975_report.md').read_text()
for p in dest.rglob('*.py'):
    compile(p.read_text(), str(p), 'exec')
package_audit = {'required_files': REQUIRED, 'required_files_present': True,
    'python_sources_compile': True, 'source_scans_redistributed': False,
    'downloaded_reference_pdfs_redistributed': False,
    'path_edits_are_only_packaging_changes': True}
(dest / 'audit/package_audit.json').write_text(json.dumps(package_audit, indent=2) + '\n')
files = sorted(p for p in dest.rglob('*') if p.is_file())
manifest = '\n'.join(hashlib.sha256(p.read_bytes()).hexdigest() + '  ' + p.relative_to(dest).as_posix()
                     for p in files) + '\n'
(dest / 'audit/manifest.sha256').write_text(manifest)
archive.parent.mkdir(parents=True, exist_ok=True)
with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
    for p in sorted(dest.rglob('*')):
        if p.is_file():
            z.write(p, p.relative_to(dest).as_posix())
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    names = z.namelist()
    assert set(REQUIRED) <= set(names)
print(json.dumps({'archive': str(archive), 'bytes': archive.stat().st_size,
    'sha256': hashlib.sha256(archive.read_bytes()).hexdigest(),
    'files': len(names), 'zip_crc_check': 'passed'}, indent=2))
