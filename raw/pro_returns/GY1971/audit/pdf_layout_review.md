# Final PDF build and visual review

**Verdict: passed. Assessment date: 9 November 2026.**

The final `GY1971_test.pdf` has **158 A4 pages**. Its overview occupies pages
1–2; the occurrence sequence begins on page 3. The extended editorial
verifications occupy pages 127–129, the problem index begins on page 130,
corrections begin on page 132, and the bibliography begins on page 152.

## Build and machine checks

- The supplied Python builder completed successfully: 45 records, 262 items,
  9 problem entries, 84 references and 127 corrections.
- The required XeLaTeX → BibTeX → XeLaTeX → XeLaTeX sequence completed.
- The final log has **zero LaTeX/package warnings, zero overfull boxes, zero
  undefined citations or references, and zero missing-character messages**.
- Twelve underfull-box notices remain. They concern loose justification in
  scholarly prose and do not indicate missing text or clipping. The rendered
  pages were reviewed and no blocking spacing defect was found.
- The geometry audit found **zero text spans outside a physical page and zero
  potential body-margin overhangs**. Extracted text contains no replacement
  characters. The PDF contains 1,043 link annotations.
- The supplied builder, style and format specification are byte-for-byte
  unchanged. The environment repair used a private XeLaTeX format and bundled
  existing font faces; no system TeX installation was modified.

The complete machine output is `pdf_layout.json`; build logs and consistency
output are adjacent in this directory. These checks concern document integrity
and do not substitute for the source and mathematical audits.

## Visual coverage

All pages were rendered into ten contact sheets and reviewed in three disjoint
groups. The detailed reviewer ledgers are:

| PDF pages | Full-page detail checks | Ledger |
| --- | --- | --- |
| 1–64 | 3, 11, 14, 17, 18, 41, 48, 59 | `pdf_review_pages_001_064.md` |
| 65–128 | 76, 85, 87, 96, 107, 118, 126 | `pdf_review_pages_065_128.md` |
| 129–158 | 132, 140, 147, 150, 151, 152, 158 | `pdf_review_pages_129_158.md` |

The coordinating review additionally inspected the overview, complete extended
verifications and problem-index pages at full-page resolution, including
pages 1–2 and 127–131. Long formulas, theorem labels, occurrence labels,
Russian text, paragraph boundaries, margins and bibliography wrapping were
checked. No clipping, overlap, missing blocks, unexpected blank pages or
visibly absent glyphs were found.

## Final spacing repair and recheck

The visual pass found that an unbraced editorial marker could consume the
space before the following word. Explicit empty braces now terminate those
markers. The final rebuild changed only whitespace on pages **29–31 and
127–129**; every page retained exactly the same non-whitespace extracted text
and the page count remained 158. This comparison is recorded in
`spacing_rebuild_comparison.json`.

All six affected pages were rendered again and visually rechecked after the
repair. The markers now separate correctly from the following prose. The
final machine geometry and log checks were rerun on this rebuilt PDF and
remain clean. The earlier reviewers' notes about a pending marker repair are
therefore closed by this final recheck.

## Scope of the visual verdict

Contact sheets provide complete layout coverage; enlarged pages provide
targeted mathematical and typographical inspection. The verdict does not claim
that every formula was re-proved from the rendered PDF. Proof checks, finite
computation checks, bibliographic access levels and unresolved identifications
are documented separately and retain their stated limitations.
