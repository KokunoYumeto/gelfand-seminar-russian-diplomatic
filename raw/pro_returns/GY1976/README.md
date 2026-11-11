# GY1976 — critical companion

Start with **GY1976_test.pdf** for the complete typeset chapter and
**GY1976_report.md** for the findings, counts, scope decisions and audit.

The seven prescribed source files are at the archive root, together with
the generated chapter, its test driver and the supplied builder/style.
The original 23 catalogue records are all represented. Record 437 is an
explicit chronological appendix: its scan dates it to 13 February 1978,
so its corrected occurrence identifiers begin `1977-437`.

## Contents

- `GY1976_talks.json`, `GY1976_items.json`, `GY1976_problems.json`: the
  record, occurrence and problem indices, using the prescribed field sets.
- `GY1976_overview.tex`, `GY1976_development.tex`: the short overview and
  fully stated critical mathematical checks. No C/D research development
  qualified; the latter file makes no claim of newly solved open problems.
- `GY1976_corrections.csv`, `GY1976_references.bib`: typed emendations,
  provenance and verified bibliography.
- `GY1976_chapter.tex`, `GY1976_test.tex`, `GY1976_test.pdf`: generated
  chapter, driver and delivered PDF; `.bbl`, `.blg` and `.log` preserve the
  final bibliography/build record.
- `sources/`: unaltered attached instructions, catalogue and bilingual
  transcriptions; `sources/scans/` contains all 55 attached scan PNGs.
- `code/research/`: source-search logs, exact locators, critical proofs
  and independent review notes.
- `code/segments/`: the independently authored segment data, including
  provenance/area metadata that is deliberately outside the core schema.
- `code/output/`: counts, validation, exact mathematical computations,
  TeX logs, PDF text extraction and compact visual-review sheets.
- `code/inputs/`: the supplied earlier-year index and cumulative bibliography.
- `code/kit_original/`: unchanged supplied format, builder and style.
- `code/authoring/`: the historical authoring/extraction scripts. These
  retain their original workspace assumptions; their completed outputs
  are in `code/segments`. The portable rebuild starts from the core files.
- `fonts/`: the DejaVu Serif files used for reproducible Cyrillic and Latin
  text, with their distribution licence.
- `MANIFEST.sha256`: hashes for every delivered file other than the
  manifest itself.

## Rebuild

Use Python 3, a TeX installation with XeLaTeX/BibTeX and the packages
required by `gelfand_companion.sty`. From this directory:

```bash
python code/validate_chapter.py .
python code/compile_chapter.py .
```

The second command runs the supplied builder, then XeLaTeX, BibTeX and
two further XeLaTeX passes. Its local-format fallback is documented in
the script and is only used when the installed TeX format is absent.

The main mathematical checks need SymPy:

```bash
python code/critical_checks.py --output code/output/critical_checks.json
python code/early_checks.py
python code/middle_checks.py
```

The exact outputs from the delivered run are retained in `code/output`.
The computational checks audit the implementation and specified examples;
the general mathematical assertions are supported by complete proofs or
the precisely cited literature, not extrapolated from finite tests.

For regeneration from the archived editorial segments:

```bash
python code/merge_chapter.py --segments code/segments --output .
python code/write_frontmatter.py .
python code/validate_chapter.py .
python code/compile_chapter.py .
```

Visual rerendering uses Poppler's `pdftoppm`, PyMuPDF and Pillow:

```bash
python code/render_and_audit.py .
```

The PDF audit deliberately returns visual-review status to pending after
a new render; its page images still need editorial inspection.

The runtime versions used were Python 3, SymPy 1.14.0, PyMuPDF 1.26.6
and Pillow 13.0.0. Source publication PDFs downloaded for research are
not redistributed. Their opened URLs and reading locators are recorded
in the bibliography and logs.
