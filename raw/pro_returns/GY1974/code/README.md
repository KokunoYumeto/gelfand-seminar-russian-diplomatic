# Reproducing the GY1974 companion

This directory preserves the edited research inputs, the scripts that assemble
them, and the mathematical checks used in the chapter. The default regeneration
route starts from the **edited snapshots in `generation/parts/`**. It does not
repeat historical research or reconstruct the notes automatically.

All commands below are run from the directory containing this README unless a
different directory is shown. Use `python3` in place of `python` if needed. None
of the default steps requires a network connection.

## 1. What is authoritative

| Location | Role |
|---|---|
| `generation/parts/*_talks.json`, `*_items.json`, `*_problems.json` | Edited record, occurrence and problem snapshots for the four record groups. |
| `generation/parts/*_references.bib`, `root_source_catalogue.bib` | Bibliographic inputs, including their verification annotations. |
| `generation/parts/*_corrections.csv` | Edited correction and provenance rows. |
| `generation/parts/*_audit.tex`, `early_boundary.tex` | Authored proof audits and the adjacent-page audit. |
| `generation/parts/*_research.md`, `early_boundary.json`, `early_boundary.md`, `late_area_map.json` | Research trails, source reading scopes, coverage and classification notes. |
| `generation/layout_edits.json` | Explicit final presentation repairs applied by the assembler. These are part of the reproducible inputs. |
| `generation/overview_template.tex`, `report_template.md` | Editorial templates populated with the assembled counts. |
| `generation/report_references.md`, `validation_report.md` | Final reference and validation inserts, when available at snapshot time. |
| `generation/previous_index.md`, `references_cumulative.bib` | Supplied prior-year index and cumulative key reference. |
| `generation/kit/` | Unchanged supplied renderer, style and schema used for this delivery. |
| `kit_original/` | Untouched small files extracted from the supplied chapter kit. |
| `environment/` | Small optional helpers documenting the editorial machine's TeX runtime repair; no caches, generated formats or smoke PDFs. |
| `generation/inputs/` | Supplied task brief and catalogue list, preserved as contextual text inputs. |
| `generation/parts/*_code/` | Optional drafting and local validation scripts, with their recorded check results. |
| The three mathematical scripts and result files beside this README | Flat copies of the computations cited in the development appendix. |

The snapshot manifest records the UTC copy time, source and packaged SHA-256
hashes, and every path substitution made in copied scripts. The source work
directory was not modified by packaging. The manifest's `pending_final_inserts`
list must be empty for the final refreshed package. A nonempty list identifies
an interim snapshot; the report renderer then uses its explicit placeholder.

The assembled current-year occurrence index has five compatibility aliases for
source occurrences already indexed in the preceding year. The 26 adjacent-page
audit rows remain a separate prior-index audit. Regeneration preserves these
editorial distinctions; it does not create new current-year records for them.

## 2. Regenerate from the edited snapshots

Install Python 3.10 or later. The default assembly, schema checks and the three
mathematical scripts use only the Python standard library; no `pip` installation
is needed for them.

```bash
python generation/regenerate.py
```

The wrapper checks the snapshot hashes and performs these steps in order:

1. `assemble_chapter.py` merges the four record groups, reconciles the explicit
   cross-group problem links, applies the recorded presentation repairs, merges
   and audits bibliography entries, and writes the counts and schema report.
2. `render_development.py` assembles the five authored audit components in the
   chapter's recorded order and applies its explicit path and spacing repairs.
3. `render_frontmatter.py` fills the overview and report templates, including
   the prior-index boundary table and the available report inserts.
4. The wrapper copies the unchanged supplied style, renderer and available
   packaged fonts, runs `check_bib_keys.py`, and calls the supplied chapter
   renderer. Editorial layout repairs are explicit data in `layout_edits.json`;
   they do not alter the kit code.

The output is **`generation/GY1974/`**. This is a new output directory inside the
reproduction workspace; the delivered chapter files two levels above it are
not overwritten. The renderer writes `GY1974_chapter.tex` and its standalone
`GY1974_test.tex` driver. The assembler also preserves all annotation scopes
from duplicated bibliography entries in `bibliography_verification.json`, even
when the final `.bib` uses only one entry per key.

The independent commands, useful when inspecting a stage, are:

```bash
python generation/assemble_chapter.py
python generation/render_development.py
python generation/render_frontmatter.py
python generation/check_bib_keys.py
python generation/kit/build_chapter.py GY1974 generation/GY1974
```

Use the wrapper for a fresh output directory because it also copies the style
and fonts needed by the PDF step. The bibliography-key checker is a reporting
aid based on normalized DOI/title matches; it is not a semantic proof that two
references are the same work.

If intentionally editing a preserved snapshot, retain a separate copy first
and invoke:

```bash
python generation/regenerate.py --allow-edited-inputs
```

That option bypasses only the frozen-file hash comparison. The assembler and
renderer still run their ordinary data and reference checks. A successful
schema check establishes structural consistency, not the historical truth of
the prose or the completeness of the literature search.

## 3. Compile the regenerated chapter

Install a TeX distribution with **XeLaTeX and BibTeX**, the `book` class,
`plainnat.bst`, and these packages (including their normal dependencies):

`geometry`, `iftex`, `fontspec`, `babel` with English and Russian support,
`amsmath`, `amssymb`, `amsthm`, `mathtools`, `xcolor`, `longtable`, `booktabs`,
`array`, `enumitem`, `needspace`, `etoolbox`, `natbib`, `xurl`, and `hyperref`.

A current complete TeX Live or MiKTeX installation is sufficient. On systems
that split TeX Live into distribution packages, the XeTeX, recommended/extra
LaTeX, recommended fonts and Cyrillic-language collections cover the required
components. Package-manager commands are platform dependent.

The complete chapter package includes four DejaVu Serif font files and their
license in its top-level `fonts/` directory. The regeneration wrapper copies
them to the new chapter directory. If only this code directory was copied, keep
the chapter's `fonts/` alongside it, or install CMU Serif or DejaVu Serif as a
system font. The style contains those fallback choices. Font or TeX-version
changes may alter page breaks and PDF bytes without changing the source text.

```bash
cd generation/GY1974
xelatex -interaction=nonstopmode -halt-on-error GY1974_test.tex
bibtex GY1974_test
xelatex -interaction=nonstopmode -halt-on-error GY1974_test.tex
xelatex -interaction=nonstopmode -halt-on-error GY1974_test.tex
```

Inspect `GY1974_test.log` and the BibTeX log for errors, undefined citations or
references, missing glyphs and layout warnings. The expected PDF is
`GY1974_test.pdf`. The preserved `validation_report.md` is a record of the
editorial build, not certification of a later local build. A byte-for-byte PDF
match is not asserted, since engine versions, fonts and PDF metadata can vary.

### Optional repair for the original restricted TeX environment

A normally configured TeX installation **does not need** `environment/env.sh`
or `environment/build_format.sh`. They preserve the workaround used on the
editorial machine, where Debian TeX package trees were installed but filename
databases and the prebuilt XeLaTeX format were missing. They still assume the
Debian-style `/usr/share/texlive` and `/etc/fonts` locations documented in the
environment README; they are not an installer for an arbitrary platform.

For that specific situation, use Bash and run the following from the top-level
chapter directory (the directory that contains `code/`):

```bash
bash code/environment/build_format.sh
source code/environment/env.sh
```

The copied helper derives the archive location from its own script path and
places generated format/cache files under the chapter's `.texruntime/`
directory. No cache or prebuilt `.fmt` file is distributed. Continue with the
ordinary XeLaTeX/BibTeX commands in the same sourced shell. The environment
README's smoke-test discussion records the earlier local diagnostic; the smoke
document and its output are intentionally absent. The full chapter validation
belongs to the separate final validation report.

## 4. Rerun the mathematical checks

Run these from the directory containing this README:

```bash
python exact_checks.py
python check_dilogarithm.py
python check_spectral_compatibility.py
```

| Script | Recorded result | Scope |
|---|---|---|
| `exact_checks.py` | `exact_checks.json` | Exact polynomial identities for the genus-two Hamiltonian and conditional spectral normalization; rational first-order jet checks of the singular-system tensor in dimensions 3–6. |
| `check_dilogarithm.py` | `check_dilogarithm.out` | High-precision evaluations associated with the two logarithmic integrals, together with the stated positive-series tail controls. |
| `check_spectral_compatibility.py` | `check_spectral_compatibility.txt` | Algebraic compatibility identities and explicit examples used in the entire-function reconstruction audit. |

`exact_checks.py` rewrites its adjacent JSON result. The other two scripts print
their results. To compare without overwriting the recorded text:

```bash
python check_dilogarithm.py > check_dilogarithm.rerun.txt
python check_spectral_compatibility.py > check_spectral_compatibility.rerun.txt
```

These computations support the proofs and diagnostics stated in the appendix.
Finite sample checks of a tensor do not replace the dimension-independent
proof, and decimal arithmetic is not silently treated as a complete interval
arithmetic certificate. The explicit mathematical scope and rounding/tail
qualifications remain in the authored audit text. None of these scripts claims
mathematical novelty.

## 5. Optional original drafting generators

The per-group generators contain editorially written prose and bibliographic
choices. They are preserved to show how the initial structured inputs were
produced, **not as the default way to reproduce the final edited snapshots**.
Manual corrections made after drafting may be present only in those snapshots
or in `layout_edits.json`. Running a generator can overwrite its group's JSON,
CSV, bibliography or research log. Work on a disposable copy when investigating
these scripts.

Their intended local order is:

| Group | Drafting sequence |
|---|---|
| Early | `build_early.py`, `build_bib.py`, `build_boundary.py`, `build_research.py`; then `validate_early.py`. |
| Middle | `build_middle.py`, then `finalize_bibliography.py`; `compile_middle.py` is an optional isolated TeX build. |
| Extra record | `root_code/build_extra.py`. |
| Late | `make_late.py`, then `make_late_bib.py`; then `validate_late.py`. |

Each script resides in its corresponding `generation/parts/*_code/` directory
and can be invoked with Python by its relative path. Some bibliography drafts
reuse the cumulative file or another group's already-present bibliography, so
retain the complete snapshot tree. The middle isolated build strips only its
private copy of cross-group occurrences before checking that excerpt; it is
not a substitute for checking the full chapter.

Only filesystem locations were changed in the copied scripts: early generators
now locate the packaged `parts/` and cumulative bibliography relative to
`generation/`, as does the optional middle CSV repair/audit helper; the optional
late font-copy utility reads the fonts supplied
with the chapter instead of an editor-machine runtime directory. Every such
replacement is listed in the manifest. Other generator logic was preserved.

The optional `late_code/copy_fonts.py` utility requires `fontTools` for its
font-character coverage inspection (`python -m pip install fonttools`). It is
unnecessary for ordinary regeneration, which uses standard-library file copies.
It expects the supplied top-level font files. No Matplotlib installation or
machine-specific runtime is required by the packaged version.

## 6. Refresh after final editorial changes

This subsection is for the maintainer with the original editorial workspace.
The package can be refreshed after the last data, bibliography, layout or TeX
repair without editing the authoritative inputs. From the original workspace:

```bash
python work/GY1974/code/generation/refresh_snapshots.py --source-work work --require-final-inserts
```

The command refreshes all selected part snapshots and their text code/log
files; the root assembly, development and frontmatter renderers; the explicit
layout edits; overview/report templates; reference and validation inserts;
the current kit; prior index/cumulative bibliography; and the flat mathematical
scripts and recorded outputs. It also refreshes the small environment helper,
original-kit and
task/catalogue copies when the original uploaded kit and text inputs are
available. It writes a new manifest and reports pending inserts.

Refresh after the final source edits, not merely after a PDF compilation. In
particular, final math-mode fixes to correction cells, the middle-record
343.2 repair, and later additions to `report_references.md` or
`validation_report.md` must be captured. The `--require-final-inserts` option
prevents a final refresh while either report insert is still absent. It does
not independently determine whether the source author has finished editing.

After refreshing, rerun `generation/regenerate.py` in a disposable copy and
compare the resulting chapter inputs with the delivered inputs. The wrapper
does not change the top-level delivered chapter, so the final editorial PDF
build remains a separate responsibility.

The packaged automated check performs that isolated regeneration and reruns the
three mathematical checks, without compiling a PDF:

```bash
python generation/check_reproduction.py
python generation/check_reproduction.py --compare-delivered
```

The second command additionally requires exact agreement of the regenerated
text/data outputs with the delivered chapter inputs and generated TeX. It is
intended for the final refreshed package, after the top-level outputs have also
been rebuilt. Successful checks write `reproduction_check.json` beside this
README, identifying the tested snapshot-manifest hash and the checks performed.
Temporary check directories are removed on exit. This recorded result must be
rerun after a later snapshot refresh; its recorded hash distinguishes it from a
check of an earlier snapshot.

## 7. Input and reproducibility boundaries

The source scans, full Russian/English transcriptions, downloaded reference
PDFs, web-response caches, page-preview images, TeX runtimes and failed build
logs are not bundled here. They are unnecessary for deterministic assembly
from the edited snapshots, and the original scans/transcriptions were supplied
separately with the task. The research logs retain the source-page identifiers,
verified URLs, reading scopes and retrieval reference identifiers. Retrieval
identifiers are historical trace information and are not a portable web API.

Rebuilding the files reproduces the recorded editorial decisions; it cannot
recreate the act of reading a scan, prove an exact publication match, update a
November 2026 status, or establish that a literature search was exhaustive.
Those limits are represented explicitly in the occurrence fields and research
logs. Reassessing them requires the original source material and fresh source
inspection. The code makes no unrecorded claim that an unidentified item is an
open problem, or that an editorial verification is a new theorem.
