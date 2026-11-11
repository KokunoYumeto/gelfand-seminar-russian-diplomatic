# GY1967 — Gelfand seminar critical companion

**Academic years:** 1967–68 and 1968–69. **Research status date:** 9 November 2026.

Open **GY1967_test.pdf** for the compiled chapter and **GY1967_report.md** for the research methods, counts, source-boundary decisions, limitations, and build report. The chapter covers all 43 supplied catalogue records (131–173), with 320 mathematical occurrences, 11 indexed problems, 101 correction rows, and 95 bibliography entries.

## Main files

| File | Purpose |
| --- | --- |
| `GY1967_talks.json` | All catalogue records, in source order, including plans and empty headings. |
| `GY1967_items.json` | The complete occurrence index, precise formulations, reconstructions, fates, dated statuses, and assessment fields. |
| `GY1967_problems.json` | Definite historical questions, exact recurrences, and their subsequent status. |
| `GY1967_overview.tex` | Chapter overview. |
| `GY1967_development.tex` | A complete, explicitly nonnovel rederivation of the coordinate-field stabilizer in the first Weyl division ring. |
| `GY1967_corrections.csv` | Translation, ambiguity, provenance, and faithful mathematical errors, distinguished explicitly. |
| `GY1967_references.bib` | Checked bibliography with retained cumulative keys and verification annotations. |
| `GY1967_report.md` | Counts by class, speaker and area; research findings and methodological qualifications. |
| `GY1967_chapter.tex` | Generated chapter for inclusion in the companion reader. |
| `GY1967_test.tex`, `GY1967_test.pdf` | Standalone driver and compiled chapter with bibliography. |

The final class counts are **A 42, B 8, C 3, D 0, E 239, F 28**. The three C occurrences concern the general Anosov classification, Weyl division-ring automorphisms, and the pointwise hyperbolic circle remainder. The development proves a known bounded special case of the second question; it does not claim to solve the full problem.

## Build the chapter

Use Python 3, XeLaTeX, and BibTeX from a TeX Live installation. The four bundled DejaVu Serif faces supply Cyrillic and italic text; their license is in `fonts/`. Run from this directory:

```bash
bash code/build.sh
```

The script executes the amended supplied builder, XeLaTeX, BibTeX, and XeLaTeX twice, with error stopping. It uses a local format-cache fallback only when the installed XeLaTeX format cannot be found. On a nonstandard TeX installation, configure TeX normally or set `GY1967_TEXMF` to the installed search trees. The direct equivalent on an ordinarily configured system is:

```bash
python3 build_chapter.py GY1967
xelatex -interaction=nonstopmode -halt-on-error GY1967_test.tex
bibtex GY1967_test
xelatex -interaction=nonstopmode -halt-on-error GY1967_test.tex
xelatex -interaction=nonstopmode -halt-on-error GY1967_test.tex
```

The original supplied builder, style, and format specification are preserved unchanged in `code/kit_original/`; `code/kit_changes.patch` shows the amendments. These support both academic years, render the problem index and readable correction entries, validate citations, and improve typography. Final build logs and machine checks are in `audit/`.

## Reproduce integration and computations

The packaged fragments are sufficient to regenerate the structured data without network access:

```bash
python3 code/integrate.py
python3 code/validate_dataset.py
python3 code/make_report.py
```

`audit/regeneration.json` records that this packaged-input route reproduced the final JSON, CSV and bibliography byte-for-byte. `code/editorial_overrides.json` makes the last independent-review decisions explicit. In particular, occurrence `1967-142.3` is F and the provisional problem `GP-1967-20` is removed; frozen fragment counts predating that decision are not the final counts.

For the exact symbolic checks, install the versions in `code/requirements.txt` into an environment of your choice, then run:

```bash
python3 code/verify_weyl.py
python3 code/verify_editorial_calculations.py
python3 code/fragments/a/checks.py
```

Their saved outputs record 522 exact Weyl assertions, 105 editorial arithmetic checks, and six additional elementary verification families. The computations supplement the complete proofs; finite tests are not used as proofs of universal statements. Independent proof reviews are included in `audit/`.

For optional page rendering, install Pillow and Poppler, then run `python3 code/render_review.py`. It writes review images to `.build-cache/review/`; these intermediates are intentionally omitted from this archive. `audit/visual_review.md` records the actual inspection scope.

## Provenance and archive conventions

`code/inputs/` contains the user-supplied text inputs, previous index, and cumulative bibliography. Original scan images remain the supplied external input. `audit/source_audit_*.md` records the literature and scan checks; a `verified` bibliography note means that its URL or DOI was opened, not that every proof in the work was independently checked.

`code/fragments/` preserves the final intermediate data, authoring scripts, early validation outputs, and research notes from the four record groups. Those authoring scripts are historical construction records, not the recommended rebuild entry point: some retain workspace paths, earlier provisional classifications, or references to the original workspace layout. The final integration and chapter-build commands above are portable and authoritative. A fragment's earlier failed build or incomplete research checkpoint does not supersede the final audit. The source-fetch scripts document attempted routes, including failed or non-PDF responses; final source audits identify the successful readings.

Pages P283–P284 begin explicitly dated September 1969 material outside the 43-record catalogue. The report inventories that material, and the correction table explains the boundary. No additional occurrence IDs are silently assigned to it.

No third-party journal PDFs, downloaded literature images, dependency trees, or browser session data are redistributed. `MANIFEST.sha256` records every included file except the manifest itself; it can be checked with `sha256sum -c MANIFEST.sha256` from this directory.
