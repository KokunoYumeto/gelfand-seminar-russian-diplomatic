# GY1964 — critical companion to the 1964–65 Gelfand seminar

Status checked through **12 November 2026**. This archive contains the complete
chapter and the reproducible research record requested in GY1964_prompt.md.

## Reading the result

Start with `GY1964_test.pdf` (**144 pages**) for the typeset chapter, or
`GY1964_report.md` for the editorial findings, counts, search decisions,
limitations, and website recommendations. The chapter covers **49
records, 248 mathematical occurrences, 17 indexed
problems, 129 references, and 119 corrections**.
All 247 supplied occurrence IDs are retained. The added support assertion is
1964-6.9. P000090 belongs to the next academic year and is retained only in
the source extracts and provenance discussion.

The seven authoritative sources are `GY1964_talks.json`, `GY1964_items.json`,
`GY1964_problems.json`, `GY1964_overview.tex`, `GY1964_development.tex`,
`GY1964_corrections.csv`, and `GY1964_references.bib`. The supplied format is
reproduced in `CHAPTER_FORMAT.md`. `GY1964_chapter.tex` and `GY1964_test.tex`
are generated from these sources.

The bibliography has 123 entries marked
`verified` and 6 marked `unverified`.
These markers record whether the link or DOI opened. The occurrence fields
and bibliography annotations separately state whether the theorem, abstract,
metadata, or only an indirect source was inspected.

## Build the chapter

Requirements: Python 3, XeLaTeX, BibTeX, and the packages used by the supplied
style (fontspec, babel, AMS packages, mathtools, natbib, xurl, hyperref,
booktabs, longtable, enumitem, needspace, and etoolbox). The PDF was built
with TeX Live 2025/dev and embedded DejaVu Serif, Latin Modern, and Computer
Modern mathematical fonts. The style also supports CMU Serif if installed.

From the extracted archive directory:

```sh
python build_chapter.py GY1964
xelatex -interaction=nonstopmode -halt-on-error GY1964_test.tex
bibtex GY1964_test
xelatex -interaction=nonstopmode -halt-on-error GY1964_test.tex
xelatex -interaction=nonstopmode -halt-on-error GY1964_test.tex
```

Or run the wrapper, which preserves command output and checks the final log:

```sh
python code/build_and_check.py .
```

The execution environment contained TeX packages but dangling filename and
format databases. `code/tex_environment.py` handles that specific condition
by using the installed trees and creating a local XeLaTeX format in
`.tex-cache`. It does not alter the system installation or the supplied
builder/style. A normally configured TeX installation needs no fallback.

## Reproduce the exact mathematics

Python 3.12.14 and SymPy 1.14.0 were used. The independent checker uses only
the Python standard library. Run in this order:

```sh
python code/bishop_certificates.py evidence/bishop_certificates.json > evidence/bishop_certificates_output.txt
python code/independent_bishop_check.py > evidence/independent_bishop_check_output.txt
python code/finite_action_check.py evidence/finite_action_check.json > evidence/finite_action_check_output.txt
```

The two Bishop implementations use different elimination and integration
routes. They agree on the endpoint signs, all 31 small coprime pairs, and
all five exact approximation certificates. The all-denominator statements
are proved in the development, rather than inferred from these checks.
`evidence/development_proof_review.md` records the independent proof review.
The finite group script checks the 168-element counterexample in 1964-34.13.

## Reconstruct the data from reviewed blocks

The frozen research blocks are in `parts/autumn`, `parts/winter`, and
`parts/spring`, with `parts/root_references.bib` supplying shared primary
references. Their own generation scripts and outputs are retained. The
following sequence reconstructs the delivered root files from the reviewed
block data, applies the logged editorial changes, and regenerates the report:

```sh
python code/normalize_corrections.py --check-only
python code/assemble_data.py .
python code/finalize_data.py .
python code/audit_data.py .
python code/make_report.py .
python code/build_and_check.py .
```

Run finalization only after fresh assembly: it assigns canonical problem
IDs and intentionally rejects an already-finalized input. The problem map,
before/after decisions, bibliography merge review, and correction formatting
ledger are in `evidence/`. Thirteen question-kind occurrences intentionally
lack a separate problem entry; `evidence/problem_index_review.md` gives the
reason for each exclusion and records the added Brown subnormal problem.

## Source and visual audits

`source_pages/` contains all 90 Russian and English page extracts from the
supplied transcriptions. The reduced reading extracts in `parts/` are
convenience outputs; the diplomatic Russian and scans govern doubtful
readings. To repeat extraction and input hashing, supply the directory
containing the original six attachments:

```sh
python code/audit_inputs.py /path/to/original-attachments
python code/extract_sources.py /path/to/original-attachments
```

The source hashes are in `evidence/input_audit.json`. Use the originally
supplied scan archive for scan review. Research logs retain source URLs,
locators, access limits, and chronology decisions. The three block reviews,
proof review, final build logs, and visual review are separate records of
different kinds of verification.

For page rendering, install PyMuPDF, Pillow, and Poppler's `pdftoppm`, then run:

```sh
python code/render_review.py GY1964_test.pdf evidence/visual
```

Every page was rendered at 90 dpi; labelled contact sheets and a page
inventory are included. The visual review also examined selected full pages,
including the overview, mathematical development, problem index,
corrections, and bibliography. The final build has no errors, overflowing
boxes, missing glyphs, undefined references, font warnings, or bibliography
warnings. Earlier build-attempt logs are retained as superseded diagnostics.

`MANIFEST.sha256` records every delivered file except itself. No network
access is required to rebuild the chapter or rerun the exact computations.
