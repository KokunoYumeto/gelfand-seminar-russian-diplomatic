# GY1971 — critical companion chapter

Start with **GY1971_test.pdf** for the typeset chapter and **GY1971_report.md**
for the research findings, counts, verification limits and proposed website
presentation. The assessment date is 9 November 2026.

The requested scope is all 45 MCCME records 229–271, 286 and 288. Record 288 is
retained as requested but dated 19 February 1973 from the scan; its item prefix
is therefore 1972-288. The generated mixed-year title reflects this one
exception and does not indicate a complete chapter for 1972–73.

## Main files

The seven schema files are `GY1971_talks.json`, `GY1971_items.json`,
`GY1971_problems.json`, `GY1971_overview.tex`, `GY1971_development.tex`,
`GY1971_corrections.csv`, and `GY1971_references.bib`. Edit these and rebuild
to change the chapter. The generated files are `GY1971_chapter.tex`,
`GY1971_test.tex`, and `GY1971_test.pdf`.

`CHAPTER_FORMAT.md`, `build_chapter.py`, and `gelfand_companion.sty` are the
supplied format and build tools, unchanged. The supplied style supports the
bundled DejaVu Serif fonts; their license is in `fonts/`.

## Rebuilding

With Python 3, XeLaTeX and BibTeX installed, run from this directory:

```sh
python code/audit_data.py
python code/build.py
```

The wrapper runs the supplied builder, then XeLaTeX, BibTeX, XeLaTeX and
XeLaTeX. On a container missing its generated TeX format, it creates a private
format under `.build-cache/`. It does not alter the system installation.

To regenerate the delivered source data from the frozen research fragments
before building:

```sh
python code/merge_fragments.py
python code/make_report.py
python code/audit_data.py
python code/build.py
```

That first command overwrites the seven-file JSON/CSV/bibliography outputs
with the frozen editorial snapshot. It is unnecessary if you are editing the
delivered data files directly. The original authoring scripts are preserved
beside their fragments as provenance; the frozen JSON/CSV/BibTeX snapshot is
the integration input. The original transcriptions and task specification are
in `source_inputs/`; scan hashes and the supplied input hashes are recorded in
`audit/input_manifest.json`.

## Exact computations and audit material

`code/check_dyson.py` and `code/check_mass.py` use Python's standard library
and exact integer or rational arithmetic. Their complete outputs, independent
checks, reference/search ledgers, source coverage, record boundaries,
classification counts and build logs are retained under `audit/` and
`code/source_fragments/`. Run `python code/check_dyson.py --limit 100` or
`python code/check_mass.py`; each writes its complete result to standard output.
Finite Dyson agreement is explicitly not an all-degree proof. The
lattice calculation evaluates a historical mass formula and a lower bound;
it does not enumerate all classes.

`code/inspect_pdf.py` records page geometry and renders layout contact sheets
when PyMuPDF and Pillow are installed. The final visual inspection record is
`audit/pdf_layout_review.md`. The machine checks establish file and reference
consistency; they do not replace the mathematical and historical reviews.
