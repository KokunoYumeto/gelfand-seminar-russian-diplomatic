# The Gelfand seminar website: build

This folder builds the static website <https://kokunoyumeto.github.io/gelfand-seminar-russian-diplomatic/>: the
notes of the I. M. Gelfand seminar (the Russian diplomatic transcription and its English translation, as published in
the readers releases of this repository) together with the critical companion in `../companion/` (one chapter per
academic year, AI-written by GPT-6 Astra (ChatGPT Pro mode)). Every page exists in Russian (`/ru/`) and English
(`/en/`).

## What the site has

- **Years**: one page per academic year (August starts the year), with the year's chapter overview, the count of
  items by class, all talks of the year and the problems of the chapter.
- **Talks**: one page per record of the MCCME catalogue (774 records), with the companion's summary and items. Each
  item has four views: what the notebook says, the precise statement (and reconstruction), its fate in the
  literature, and its present status with the companion's assessment. Beside them, the notebook pages of the record
  with the scan at MCCME and the page in each reader PDF.
- **Problems**: the problem index across the years, one page per problem with every chapter's entry.
- **References**, **speakers** and the **developed questions** of each chapter.
- **Notebook text**: one page per archive chapter (34), with every notebook page in order: its number, the number
  written on it, the scan, the pages of the two reader PDFs, the catalogue records on it and the companion items that
  cite it, then the text passage by passage, with the transcriber's marked readings and their scan crops. The figures
  (TikZ pictures and diagrams) are typeset from the transcription's LaTeX as SVG. A switch shows the Russian, the
  English or both side by side, aligned passage by passage. Talk pages load the text of their notebook pages on demand.
- **Search**: Pagefind, one index per language (`/ru/search/`, `/en/search/`); the reference box in the header goes
  to a record, item, problem, page or year, and searches when the text is not a reference.
- **Permalinks**: `/r/?398` (record), `/r/?1976-398.5` (item), `/r/?GP-1976-01` (problem), `/r/?P000659` (notebook
  page), `/r/?P000659.2` (passage), `/r/?1976-77` (academic year), `/r/?1976-09-06` (date).
- **Data**: `/data/` holds items, talks, problems, references, pages, records and corrections as CSV and JSON, with the
  works registry, the academic years and the pages revised since each chapter was written; `/data/pages/{ru,en}/`
  holds the text of each notebook page as JSON.

Notices on the pages: a status line naming how each text was made and when; the rights statement in the page's
language; where the transcription of a page changed after a chapter was written, a notice on the talk and a mark on
each item citing that page (step G7); on Russian pages, a note that the commentary is in English; for years without a
companion chapter, a stub notice.

## Steps

Run `python -I build/run_all.py` (options in its header). Each step writes its output under the build folder
`GELFAND_WORK` (default `site-build/_work/`, not committed) and stops the build when its check fails.

| Step | Script | Output | Check |
|---|---|---|---|
| sync | `sync_companion.py --returns DIR` | `../companion/years/`, new chapters in `data/works.json` | seven data files per chapter; no local paths, e-mail addresses or listed terms |
| G1 lock | `g1_lock.py` | `gelfand.lock.json`, the release assets | SHA-256 of each asset equals GitHub's digest |
| G2 registry | `g2_registry.py` | records, pages, academic years | every record and page placed; PDF page map complete |
| G7 revised pages | `g7_stale.py` | pages revised since each chapter was written | the text each chapter was written against matches its recorded hash |
| G5 companion | `g5_companion.py` | companion fields as HTML (pandoc, Chicago author-date) | no unconverted field, no undefined citation key |
| G6 links | `g6_links.py` | items, problems, pages, references linked | every record, problem id, occurrence and reference resolves |
| G3 notebook | `g3_notebook.py` | the 1,527 pages of each language as HTML (pandoc, formulas for MathJax), passages, marked readings, figures and scan crops | parity: the same pages, passage numbers and marked-reading labels in Russian and English; nothing unconverted; no LaTeX outside math; balanced blocks and unique ids per page |
| G4 figures | `g4_figures.py` | one SVG per figure (LuaLaTeX with the edition's preamble, `preview`, `pdftocairo` or `mutool`) | at most 2 % of the figures without SVG (listed in `reports/g4_failed.tsv`; the page then points to the scan and the PDF) |
| G8 render | `g8_render.py` | the pages, `/data/` and the page shards | — |
| G9 search | `g9_search.py` | `/pagefind/` (Pagefind 1.3.0) | both languages indexed; each index holds every indexed page of its language |
| G10 checks | `g10_check.py` | `reports/g10_*.tsv` | counts equal the data; no LaTeX outside math; no broken inside link; every record, year and problem in both languages; notices; the notebook pages, passages and marked readings equal G3's; a sample of 50 outside links answers; size under 1 GB; no local paths or e-mail addresses |

Requirements: Python 3.11 or later with lxml; pandoc 3; poppler (`pdftotext`, `pdfinfo`, `pdftocairo`); LuaLaTeX with
TikZ, tikz-cd and preview, and the Noto Serif fonts the edition's preamble loads (G4; `GELFAND_LATEX_JOBS` documents
at a time, default 4; `mutool` as a second converter if found, or `GELFAND_MUTOOL`); the GitHub CLI; MathJax 3.2.2
(the es5 folder of the npm package, named by `GELFAND_MATHJAX`) and Pagefind 1.3.0 (`GELFAND_PAGEFIND`, the
executable of the npm package `@pagefind/windows-x64` or the binary for another system); versions and hashes in
`data/vendor.lock.json`. Formulas that use macros MathJax lacks are typeset by LuaLaTeX as figures (G3 reads the list
of MathJax's macros from `GELFAND_MATHJAX`).

## Works registry and removal

`data/works.json` lists every work the site shows: the two notebook texts and one entry per companion chapter, each
with an `include` flag; `exclude_records` lists catalogue records left out. A work switched off (or named in
`GELFAND_EXCLUDE` for one build) disappears from every page, index and data file at the next build, and links into it
become plain text. Removing a work is a rebuild and a new deploy; no history is rewritten.

## Deploy

`deploy/make_site_tarball.py` packs the checked site and prints two commands: create a pre-release `site-YYYY-MM-DD`
holding the tarball, then run `.github/workflows/pages.yml` on main with that tag. The workflow deploys the tarball to
GitHub Pages and deletes the site release, so no built site is kept in the repository.

## Corrections to the catalogue

`data/catalogue_fixes.json`: records 510–512 are dated 23 Feb 1981 (the catalogue prints "23-Feb-91"; the reason is
given there), and records 603 and 694 are talks without notes.
