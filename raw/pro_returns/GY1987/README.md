# GY1987 — critical companion, 1987–88

Start with **GY1987_test.pdf** for the complete typeset chapter or
**GY1987_report.md** for the editorial findings and quantitative audit.
The seven files specified by CHAPTER_FORMAT.md are at the archive root.
They cover all 38 records in source order, 287 mathematical occurrences,
27 indexed problems, 99 references and 85 corrections/critical annotations.
The status date is 11 November 2026.

## Rebuild

Use Python 3 and a normal TeX Live installation with XeLaTeX, BibTeX,
fontspec, the standard AMS/natbib/hyperref packages and DejaVu Serif:

```sh
python build_chapter.py GY1987
xelatex -interaction=nonstopmode -halt-on-error GY1987_test.tex
bibtex GY1987_test
xelatex -interaction=nonstopmode -halt-on-error GY1987_test.tex
xelatex -interaction=nonstopmode -halt-on-error GY1987_test.tex
```

`python code/build_document.py .` runs that sequence, resolves any remaining
cross-reference rerun request, and logs every command. It also contains the
documented private-format workaround used on the research host; it changes
no system installation. The supplied builder and style are unchanged.

## Recheck data and calculations

```sh
python code/integrate_and_audit.py --directory .
python code/verify_development.py > logs/development_checks.json
python code/early_checks.py > logs/early_checks_stdout.txt
python code/inspect_pdf.py . --render
```

The mathematical checks require NumPy and SymPy. The PDF audit requires
PyMuPDF and Pillow. Exact versions are recorded with the outputs.
Finite numerical diagnostics support, and do not replace, the full proofs.
The early checks intentionally retain counterexamples to false printed
formulas; a diagnostic counterexample is not a failed corrected theorem.

## Evidence and production history

- `research/` contains source maps, opened-source/locator ledgers,
  bounded-search qualifications and the independent mathematical review.
- `logs/` contains the final schema, bibliography-identity, computation,
  build and page-layout results, plus the extracted text of this edition.
- `research/authoring/` preserves authoring scripts and their frozen shard
  outputs. Some historical scripts use the original workspace layout or
  original attachments. These scripts are provenance, not a substitute
  for the authoritative root files; final integration overrides are retained.
- The cumulative-key comparison requires the separately supplied
  references_cumulative.bib and previous_index.md. Its completed result is
  included in logs/reference_identity_audit.json and the integration audit.
- Original scan archives, source transcriptions, downloaded research papers,
  full-paper OCR, model/runtime caches and private TeX formats are omitted.
  Download/OCR scripts remain available; their factual findings and checked
  locators are preserved in the research ledgers. External sources retain
  their own rights and availability conditions.
- `research/source_manifest.json` identifies the supplied inputs by hashes.
  `checksums.sha256` verifies every payload file except itself.

The bibliography marks 97 entries verified and two unverified. Here
“verified” means that a link or DOI was opened; the per-entry annotations
and per-item assessment state whether the actual result, only metadata,
or an indirect attribution was read. No new-priority claim is made for the
four worked developments/annotations.
