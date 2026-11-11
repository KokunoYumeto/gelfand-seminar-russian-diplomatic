# Reproducing GY1966

The reading copy is `GY1966_test.pdf`. The seven chapter-format files, the report,
and the generated chapter are at the archive root. The status audit is dated
9 November 2026. The PDF has 146 pages, including the bibliography.

## Build the reader

Run these commands from the extracted archive root with Python 3.10 or later and a configured
TeX Live installation providing XeLaTeX and BibTeX:

```bash
python code/assemble.py
python build_chapter.py GY1966
xelatex -interaction=nonstopmode -halt-on-error GY1966_test.tex
bibtex GY1966_test
xelatex -interaction=nonstopmode -halt-on-error GY1966_test.tex
xelatex -interaction=nonstopmode -halt-on-error GY1966_test.tex
```

The supplied `build_chapter.py` is unchanged. Its original copy and the supplied
format specification are in `code/kit_supplied/`. The assembler uses only the
Python standard library. It merges the four reviewed allocations, assigns the
twenty new GP identifiers in first-occurrence order, preserves `GP-1965-03`,
checks links and references, and generates the report tables and overview counts.

The assembler reads the reviewed JSON, CSV, and BibTeX files under
`code/authoring/`. Those files are the authoritative assembly inputs. The draft
authoring scripts are also retained as research provenance; manual review and
source corrections followed their initial execution. Rebuilding the chapter
does not require rerunning those draft scripts, which could replace reviewed
wording with an earlier draft. The input transcriptions, catalogue, earlier
index, and cumulative bibliography are in `code/source_inputs/`. Source scans
are identified by their original page IDs and are not duplicated in this bundle.

The development is maintained directly in `GY1966_development.tex`. The overview
and report templates are `code/overview.template.tex` and
`code/report.template.md`; change the templates before regenerating those files.

## TeX environment and typography

The included DejaVu Serif font files cover the English and Russian prose; their
license is included in `fonts/`. Mathematical fonts come from TeX Live. The style
loads the usual AMS packages, fontspec, babel, natbib, hyperref, xurl, enumitem,
needspace, etoolbox, and table packages. Author–year citations and the supplied
reader's `plainnat` bibliography convention are preserved.

`code/style_adaptations.diff` records the changes from the supplied style:
portable font loading and a Russian-language fallback; six lines of reserved
space at item starts; suppression of one-line paragraph widows; and omission
of punctuation for empty speaker/date fields in catalogue headings. The chapter
macro interface is unchanged. Explicit spaces after proof markers and display
punctuation were corrected in the chapter inputs.

The execution environment had installed TeX packages but incomplete generated
format and font-map state. The optional script below reconstructs that state
locally on the Debian-style TeX paths used for this run, without installing
packages or changing system files:

```bash
python code/setup_local_tex.py
source code/texenv.sh
```

After sourcing the environment, use the same build commands above. A normally
configured TeX installation does not need this repair. Generated format/cache
files are excluded from the archive; the script and its execution log are kept.

## Independent mathematical computations

All four programs below use only the Python standard library and write their
JSON output beside the script. Their outputs and the execution stdout are
included. They are finite computational checks and are not substituted for the
proofs or generalized beyond their stated scope.

```bash
python code/check_pair_partitions.py
python code/check_singularities.py
python code/check_sturm_endpoint.py
python code/check_editorial_algebra.py
```

The first program checks the 2/4/1 collision coefficients on nine configurations,
all 128 configurations of a nonuniform seven-site process, and 205 rational
canonical-ensemble parameter pairs. The second compares two Boardman-symbol
counting algorithms 246 times and independently checks six local-algebra lengths,
the transversality determinants, and the complex-square Jacobian. The third
checks the Sturm equation and endpoint normalizations. The fourth verifies the
cyclic-group augmentation calculation and the quadratic-unit Heisenberg example.
Their exact conclusions and limitations are recorded in their JSON outputs.

The independent written reviews of the variance proof and other reconstructions
are retained under `code/authoring/`. These reviews re-derived the bounds and
checked the counterexamples; they did not treat successful numerical tests as
proofs of an unrestricted theorem.

## Structural audit and visual verification

```bash
python code/audit_final.py
python code/verify_delivery.py
```

The portable audit writes `code/final_audit.json` and `code/final_audit.md`. It
checks the schema, enumeration, counts, catalogue agreement, source-page
coverage, reciprocal problem links, earlier-year links, citation/reference
consistency, reference-key reuse, class A authorship, and the explicit gaps in
class C. Its final result is 15 checks passed, with no issues. It does not itself
prove the mathematics or certify the rendered pages.

`code/visual_qa.md` records the actual page inspections. Final XeLaTeX, BibTeX,
PDF metadata, and embedded-font logs are in `code/build/`. Earlier build-pass
logs are retained as execution provenance; the file named
`code/build/xelatex_final.log` is the final diagnostic record. It has no errors,
undefined references/citations, missing characters, or overfull boxes. Modest
underfull-line diagnostics remain; their rendered lines were checked visually.

For an optional new visual review, install Pillow and PyMuPDF and provide
Poppler's `pdftoppm`, then run:

```bash
python code/render_pdf_qa.py /path/to/qa-output
```

This decodes every page PNG and makes numbered twelve-page contact sheets.
The raster files are reproducible QA intermediates and are excluded from the
archive. The rendering log is included.

`MANIFEST.sha256` at the archive root records all delivered files other than the
manifest itself. It can be checked on extraction with `sha256sum -c
MANIFEST.sha256`. Rebuilding changes generated files and therefore requires a
fresh manifest if the rebuilt version is to be archived.
