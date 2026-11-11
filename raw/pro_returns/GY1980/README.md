# GY1980 — critical companion to the Gelfand seminar, 1980–81

Start with `GY1980_test.pdf` for the complete typeset chapter or `GY1980_report.md` for the research findings, counts, evidence limitations and methodological decisions.

## Main files

The seven schema files are:

- `GY1980_talks.json`: records, speakers, dates and source-page footprints.
- `GY1980_items.json`: mathematical occurrences and their assessments.
- `GY1980_problems.json`: problem identities, occurrences and present status.
- `GY1980_overview.tex`: the chapter overview.
- `GY1980_development.tex`: proofs, computations and their limitations.
- `GY1980_corrections.csv`: the correction apparatus.
- `GY1980_references.bib`: the chapter bibliography.

`GY1980_chapter.tex` and `GY1980_test.tex` are generated files. The supplied format specification is also included.

## Build the chapter

From this directory, using Python 3 and an installation of XeLaTeX and BibTeX:

```sh
python code/finalize_typesetting.py
python code/format_corrections.py
python code/validate.py
python build_chapter.py GY1980
python code/build_pdf.py
```

The two formatting scripts are idempotent. The build script runs XeLaTeX, BibTeX and two further XeLaTeX passes, with additional passes if needed for stable cross-references, preserving a log for each pass. It uses a normal TeX installation when available and can generate missing formats in a local runtime directory from installed TeX sources.

The supplied style requires the standard AMS, natbib and hyperref packages and a font supporting Cyrillic, such as CMU Serif or DejaVu Serif. The `checks` directory holds the build logs and records completed validation and PDF audits. The supplied cumulative bibliography and earlier index are preserved as read-only inputs to the integration and audit scripts. The chapter has its own bibliography and problem index among the seven schema files listed above.

To refresh the report and README after compilation while preserving the overview and area-classification CSV:

```sh
python code/write_synthesis.py --report-only
```

The report reads the audited counts and detects the current PDF page count automatically. PyMuPDF is required for page counting when the PDF is present. `requirements.txt` records the Python package versions used. To repeat the PDF structure checks and generate contact sheets and enlarged page images, run `python code/audit_pdf.py`; this also requires Pillow and the Poppler commands `pdftoppm` and `pdffonts`.

## Reproduce the mathematical checks

The computations use Python 3 and SymPy 1.14.0, with exact coefficients:

```sh
python code/check_weyl.py > checks/weyl_output.txt
python code/check_formal.py > checks/formal_output.txt
python code/check_curve_models.py > checks/curve_models_output.txt
```

The first script checks the notebook counterexample, the corrected Dixmier pair, the centered genus-two pair, its spectral polynomial and discriminant; it also runs the independent checks of operator action. The second checks the formal pseudodifferential expression. The third checks the affine coordinate identity, squarefreeness and absence of affine singularities. Mathematical proofs and limitations appear in `GY1980_development.tex` and the PDF.

## Research and authoring audit

The `parts` directory contains batch data for the records, bibliography and search ledgers, scan-coverage notes and authoring scripts, making the research process inspectable. The seven top-level schema files are the authoritative chapter inputs. The integration and synthesis scripts combine and summarize the audited batches; rebuilding the chapter from those seven files does not require rerunning them.

The `inputs` directory preserves the original English and Russian source files, the manifest and prompt, and the original `GY1980_scans.zip` archive. The supplied earlier index and cumulative bibliography are also included. Extracted scan images and individual source-page files are omitted to avoid duplicating the source archive and transcriptions. To reproduce those working files from the preserved inputs:

```sh
python code/extract_sources.py
```

This script reconstructs the 65 page blocks in each language and the 65 notebook scans, checks their expected range, and records source-file checksums. A separate page-coverage ledger records the source regions used in the chapter.

All 39 records, numbered 490–528, are included. This restores records 510–512, which were wrongly dated 1991 in the source catalog. Status judgments are dated November 2026. The general curve-field embedding conjecture remains the subject of a qualified class-C assessment; the development establishes the bounded results described in the report.

`checks/manifest_sha256.txt` records the payload checksums. `code/package.py` rebuilds the ZIP after successful schema, mathematical, PDF and visual checks; it verifies every archived payload against that manifest and checks the archive CRCs. The manifest excludes itself and the packaging log to avoid circular hashes.
