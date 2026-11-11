# GY1975: critical companion to the 1975–76 Gelfand seminar

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
