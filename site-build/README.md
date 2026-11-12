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
- **Permalinks**: `/r/?398` (record), `/r/?1976-398.5` (item), `/r/?GP-1976-01` (problem), `/r/?P000659` (notebook
  page), `/r/?1976-77` (academic year), `/r/?1976-09-06` (date).
- **Data**: `/data/` holds items, talks, problems, references, pages, records and corrections as CSV and JSON, with the
  works registry, the academic years and the pages revised since each chapter was written.

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
| G8 render | `g8_render.py` | the pages and `/data/` | — |
| G10 checks | `g10_check.py` | `reports/g10_*.tsv` | counts equal the data; no LaTeX outside math; no broken inside link; every record, year and problem in both languages; notices; no local paths or e-mail addresses |

Requirements: Python 3.11 or later with lxml; pandoc 3; poppler (`pdftotext`, `pdfinfo`); the GitHub CLI; MathJax
3.2.2 (the es5 folder of the npm package, named by `GELFAND_MATHJAX`; versions and hashes in
`data/vendor.lock.json`).

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
