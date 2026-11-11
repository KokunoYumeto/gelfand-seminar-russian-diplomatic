# GY1979 — Gelfand seminar, academic year 1979–80

**Assessment and release documentation:** 2026-11-10.

This package contains the critical companion chapter for all **27 catalogue records, 462–488**, with **252 mathematical occurrences, 10 problem threads, 104 bibliography entries, and 106 correction/provenance annotations**. The historical-fate counts are **A 12, B 7, C 3, D 0, E 203, F 27**. Record 481 is retained as a heading. Records follow manuscript source order, including 477 before 476.

Start with **`GY1979_test.pdf`** for the complete rendered chapter and **`GY1979_report.md`** for the coverage decisions, principal findings, research limitations, and proposed website presentation. The filename `GY1979_test.pdf` follows the supplied chapter-builder convention; it is the delivered standalone reading copy.

## Contents

### The seven chapter inputs

| File | Contents |
|---|---|
| `GY1979_talks.json` | Critical talk identification, dates, source spans, summaries and record kinds. |
| `GY1979_items.json` | Notebook statements, rigorous reconstructions, historical fates, dated status, verification levels and citations for every occurrence. |
| `GY1979_problems.json` | Problem identities, precise scope, earlier/current occurrences and dated status. |
| `GY1979_overview.tex` | Overview of the year and class counts. |
| `GY1979_development.tex` | Proved normal-form reductions, the complete bounded Grassmann commutant calculation, and the energy-representation proof diagnostic. |
| `GY1979_corrections.csv` | Faithfully transcribed mathematical errors, unresolved readings and provenance discrepancies. |
| `GY1979_references.bib` | The complete bibliography, with verification annotations and source locators. |

`GY1979_chapter.tex` and `GY1979_test.tex` are generated from these inputs. `build_chapter.py`, `gelfand_companion.sty`, and `CHAPTER_FORMAT.md` supply the builder, formatting macros, and schema. The untouched supplied kit is retained under `code/kit_original/` for comparison with the final formatting support.

### Evidence, authoring and review

- `code/root_research_log.md` and `code/authoring/{early,middle,late}/research_log.md` preserve source access, queries, locators, chronology, and inference limits.
- `code/catalog_original.json`, `code/catalog_crosswalk.csv`, `code/source_coverage.csv`, and `code/boundary_inventory.md` preserve the original catalogue and critical boundary decisions.
- `code/editorial_config.json` is the saved set of final integration decisions. `code/editorial_changes.json` and `code/corrections_typesetting_output.json` record their application.
- `code/integration_review.md`, `code/independent_early_review.md`, and `code/proof_review.md` preserve the independent reviews. **`code/review_disposition.md` records which review comments were resolved and supersedes their outstanding-action wording.**
- `code/bibliography_merge_conflicts.json` retains three historical same-key alternatives. They are resolved in `code/review_disposition.md`; they are not three unresolved bibliographic identities.
- `code/bibliography_metadata_output.json` preserves the supplemental DOI-registration responses. A metadata check does not imply that a mathematical theorem was read.
- `code/verify_berezin.py`, `code/verify_energy_identity.py`, and the authoring subdirectories contain executable checks and their saved outputs. `code/runtime_versions.json` records the Python-library versions used.
- `code/build_output.txt`, `code/build_status.json`, and `code/audit_output.json` preserve the integrated build and audit results.

`code/pdf_qa_output.json`, `code/visual_qa.md`, and `code/qa_contact_sheets/` document the final visual inspection. `code/package_manifest.json` hashes the ordinary archive members, and `code/archive_validation.json` records the final ZIP integrity checks. `python code/package_delivery.py` recreates and checks the archive in the parent directory.

The original working paths in the logs map to packaged paths as follows:

| Original workspace path | Packaged path relative to this README |
|---|---|
| `parts/early/` | `code/authoring/early/` |
| `parts/middle/` | `code/authoring/middle/` |
| `parts/late/` | `code/authoring/late/` |
| `kit/` | `code/kit_original/` |

Source scans, full source transcriptions, earlier-year attachments, and downloaded public papers are intentionally **not redistributed**. Their identifiers, citations, access records and the input manifest preserve provenance. They are unnecessary for rebuilding the finished chapter, but are needed to repeat the source audit itself.

## Rebuild the finished chapter

From the directory containing this README, run:

```bash
python code/build_all.py
```

The `python` executable must invoke Python 3. The script resolves the package directory from its own location, runs the supplied builder and independent audit, then performs the required XeLaTeX/BibTeX sequence. It writes the regenerated `GY1979_test.pdf`, auxiliary TeX files, `code/build_output.txt`, and `code/build_status.json`. It uses the delivered seven chapter inputs; it does not rerun literature searches, reassemble the authoring batches, or rerun the independent mathematical computations.

The corresponding individual commands, from the same directory, are:

```bash
python build_chapter.py GY1979
python code/audit_chapter.py
xelatex -interaction=nonstopmode -halt-on-error GY1979_test.tex
bibtex GY1979_test
xelatex -interaction=nonstopmode -halt-on-error GY1979_test.tex
xelatex -interaction=nonstopmode -halt-on-error GY1979_test.tex
```

Use `build_all.py` when the installed TeX tree lacks a prebuilt XeLaTeX format. Its helper creates a local format from installed sources without changing system configuration. This fallback expects the Linux TeX trees used in the original environment; on another platform, an ordinary correctly configured TeX installation is preferable.

The delivered build completed all six stages with exit code zero. The final log has **no LaTeX errors, undefined references/citations, missing-character warnings, or overfull boxes**. Some underfull-box messages remain recorded in `code/build_status.json`. The final PDF page count, byte size and SHA-256 are recorded in `code/pdf_qa_output.json`. All 144 pages were rendered and inspected in contact sheets, with full-page checks of the developments and representative text, corrections and references; see `code/visual_qa.md`. A different TeX/font version can change line breaks, PDF metadata and byte size without changing the mathematical content.

## Optional reassembly from the packaged batch outputs

The final seven inputs already include all editorial decisions. To reproduce their integration from the saved batch JSON/CSV/BibTeX in a clean extracted package, use this order:

```bash
python code/assemble_chapter.py
python code/apply_editorial_changes.py
python code/typeset_corrections.py
python code/source_coverage.py
python code/write_report.py
python code/build_all.py
```

This sequence overwrites the merged data, report and generated chapter using the saved authoring outputs, `root_references.bib`, `code/editorial_config.json`, and saved DOI-metadata results. It retains `GY1979_development.tex` as an authored input. `assemble_chapter.py` uses `code/authoring/` in the extracted package; if a sibling `../parts/` directory exists, the script deliberately prefers that original workspace source. Use a clean extraction when reproducing the packaged snapshot.

`code/prepare_editorial_config.py` records how the final configuration was prepared; it is not needed when using the delivered configuration. `code/stage_support.py` records workspace-to-package staging and likewise is not part of the ordinary rebuild. Individual authoring scripts are preserved as research provenance, but some expect the original cumulative bibliography or other workspace inputs. The portable reassembly path begins with their **saved outputs**, not by blindly rerunning every script in `code/authoring/`.

## Optional mathematical checks

Install the computation dependencies if they are not already available:

```bash
python -m pip install sympy==1.14.0 mpmath==1.3.0
```

Then run, from the package directory:

```bash
python code/verify_berezin.py > code/verify_berezin_output.json
python code/verify_energy_identity.py > code/verify_energy_identity_output.json
python code/authoring/early/verify_annotations.py
python code/authoring/middle/independent_early_checks.py
```

The last two scripts write their JSON outputs beside themselves; the middle check reads the early output through the preserved sibling-directory layout. The checks cover exact Grassmann coefficients, the noncommutative differential identity, Fourier integrals, the printed resonance-coefficient counterexample, and the scalar four-sphere heat/zeta values. The quartic quadrature is not interval certified. The independent review supplies analytical tail/remainder estimates where stated; numerical agreement is not a substitute for a complete numerical error enclosure. The general algebraic results are proved in the chapter rather than inferred from the finite test set.

## Dependencies

- **Python 3**, tested with **3.12.14**. The chapter builder, merger and data audit use the standard library.
- **XeLaTeX, BibTeX, `kpsewhich`**, and a working TeX distribution. The local-format fallback additionally uses `xetex` and the installed XeLaTeX source tree.
- TeX packages used by the wrapper/style: `geometry`, `iftex`, `fontspec`, `babel` with Russian support, `amsmath`, `amssymb`, `amsthm`, `mathtools`, `xcolor`, `longtable`, `booktabs`, `array`, `enumitem`, `needspace`, `etoolbox`, `natbib`, `xurl`, and `hyperref`, together with the `plainnat` bibliography style.
- A Cyrillic-capable serif font, preferably **CMU Serif** or **DejaVu Serif**. If a `fonts/DejaVuSerif.ttf` family is present, the style uses that local family first; otherwise it checks installed fonts.
- **SymPy 1.14.0** and **mpmath 1.3.0** for the optional mathematical checks. They are not needed for the ordinary PDF rebuild.
- **PyMuPDF** and **Pillow** for the optional `python code/pdf_qa.py` rendering pass; PyMuPDF is also used by `python code/package_delivery.py` to record the PDF page count.

No network access is required for the ordinary build, portable reassembly, or saved mathematical checks once these dependencies are installed. Source retrieval and fresh DOI verification are separate research operations.

## Interpretation and limits

Assessments are dated **2026-11**. Class letters, literal correctness, publication-match strength, verification level, and work proved here are independent fields. In particular, an opened bibliographic record verifies identity, not the full proof; a failed search does not establish openness; and a retrospective application does not establish historical influence.

The final editorial record supersedes earlier provisional research conclusions. This includes the exact Zakharov–Schulman 1980 source identification and Manakov attribution, the distinction between its kinetic criterion and the later general Hamiltonian theorem, the B classification of the infinite-invariant resonance question, and the E classification of the literal finite commutant task. The two-dimensional energy-representation status remains explicitly bounded by the checked literature. Neither that diagnostic nor the bounded matrix developments carries an unsupported priority claim.
