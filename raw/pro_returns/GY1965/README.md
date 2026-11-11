# GY1965 — critical companion, 1965–66

Open **GY1965_test.pdf** for the complete English chapter. **GY1965_report.md** explains the inventory, literature searches, decisions, verification limits, and reproducibility. Present-status assessments are dated **9 November 2026**.

The chapter covers all **37 records (53–89)** and **298 mathematical occurrences**, with **9 indexed questions**, **63 bibliography entries**, and **26 correction/apparatus entries**. The classification counts are A: 22; B: 7; C: 1; D: 0; E: 246; F: 22. These count occurrences, including repeated exposition, rather than distinct theorems.

## Contents

| File or directory | Purpose |
|---|---|
| `GY1965_test.pdf` | Complete compiled chapter, including overview, record and occurrence catalogue, bounded development, problem index, corrections, and references |
| `GY1965_talks.json`, `GY1965_items.json`, `GY1965_problems.json` | Structured record, occurrence, and question data |
| `GY1965_overview.tex`, `GY1965_development.tex` | The two narrative components of the seven-file chapter format |
| `GY1965_corrections.csv`, `GY1965_references.bib` | Critical apparatus and checked bibliography |
| `GY1965_report.md` | Counts, research methods, conclusions, caveats, and proposed format improvements |
| `GY1965_chapter.tex`, `GY1965_test.tex`, `GY1965_test.bbl` | Generated chapter, standalone driver, and generated bibliography |
| `build_chapter.py`, `gelfand_companion.sty`, `fonts/` | Compatible build tools and licensed fonts |
| `code/` | Assembly, validation, exact computations, retained computation outputs, and authoring scripts |
| `code/parts/` | Frozen research tranches used to reproduce the merged data |
| `code/kit_original/` | Untouched supplied format, builder, and style |
| `evidence/` | Source-access ledgers, research reports, independent proof reviews, and build/PDF audits |

The sole class-C question asks for the automorphisms of a Weyl division ring. The development gives a complete bounded treatment of the subgroup preserving a chosen rational function field, its inner rational translations, the resulting outer translation subgroup, and finite-group cocycle removal. It makes no claim to classify the unrestricted group or to establish priority for these results. The chapter explains precisely what remains unresolved in the verified literature.

## Build and reproduce

With Python 3, XeLaTeX and BibTeX installed, run from this directory:

```bash
bash code/build.sh
```

The script runs the supplied-compatible builder, the additional data audit, XeLaTeX, BibTeX, and two final XeLaTeX passes. It can initialize a local XeLaTeX format if necessary on a minimal TeX installation. Logs are written to `evidence/build/`. The bundled fonts permit reproducible Cyrillic and full bold/italic faces; the style also retains system-font fallbacks.

To reconstruct the merged data and count-dependent summaries first:

```bash
python code/assemble.py --parts code/parts --output .
python code/write_summary.py .
bash code/build.sh
```

The exact symbolic checks use SymPy 1.14.0. Their two Weyl-field parameter runs and the annotation checks are retained beside the scripts. Each script's argument/help text describes its invocation. `code/audit_pdf.py` additionally uses PyMuPDF and Pillow; its checks complement the recorded visual review.

The original Russian and English transcriptions, scans, record list, and previous-year index were supplied by the task and are not duplicated here. Historical authoring and extraction scripts under `code/research/` and `code/prepare_sources.py` refer to those original inputs; reproduction of the final merged chapter uses the self-contained frozen tranches instead. Original provisional problem IDs in those tranches are deliberately preserved; `evidence/assembly.json` records their final renumbering and bibliography aliases.

`MANIFEST.sha256` records the SHA-256 of every other file in this archive. Independent proof checks, accepted corrections from those checks, and the final PDF inspection are documented in `evidence/`.
