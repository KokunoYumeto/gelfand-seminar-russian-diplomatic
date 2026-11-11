# GY1981 — the Gelfand seminar, 1981–82

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
