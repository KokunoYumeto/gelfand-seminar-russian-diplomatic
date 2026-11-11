# Final visual and structural PDF review

Date: 11 November 2026. Final PDF: `GY1980_test.pdf` (139 pages).
SHA-256: `3fe94e1406d04bbb170473637fb05e65b051ab015fed04759a4344bc557d67ee`.

## Inspection scope

The autumn reviewer inspected all contact sheets for pages 1–64, full pages 2, 8, 12, 31 and 61, and enlarged Cyrillic passages on pages 3, 46–49 and 53. The spring reviewer inspected the contact sheets for pages 65–107 and 117–139, plus full pages 75, 81, 96, 98, 117, 128, 131, 138 and 139. Their detailed reports and the checksums of that inspection version are included alongside this report.

The root reviewer inspected full development pages 108–113 and problem-index page 116, as well as the overview. The final pass corrected spacing after result markers, shortened an overlong proof heading, typeset the recursion bounds in item 1980-526.2, and replaced compressed author/year references in the correction apparatus with normal citations. It also replaced an inaccurate verbal phrase in Corollary 1.7 with the exact condition `4 does not divide 10`; the lemma and its underlying order argument were already correct. These edits do not change the mathematical results, item identities or classifications.

After that final rebuild, the root reviewer inspected all three contact sheets covering pages 97–139 and full pages 98, 112, 116, 128 and 131. The final page count remains 139. The revised mathematical inequality and citations render correctly. No clipping, overlapping text, missing glyph boxes, illegible formulas or heading collisions were observed. All pages are covered by the combined inspection, with the final changes rechecked in their affected range.

## Recorded machine checks

The final XeLaTeX and BibTeX logs contain zero LaTeX errors, unresolved citations/references, unstable labels, duplicate labels, missing glyphs, overfull boxes or BibTeX warnings. Every one of the 39 record labels and 246 occurrence identifiers is present in the PDF. There are no empty pages or text spans outside the physical page. The overview occupies parts of pages 1–2. All listed PDF fonts are embedded. Eleven underfull-line diagnostics remain; inspected line spacing is readable and these are not overflow or content-loss errors.

The contact sheets were generated from every page with PyMuPDF. The enlarged representative pages were rendered with Poppler; the rendering commands are reproducible through `code/audit_pdf.py`, with an additional `pdftoppm -f 98 -singlefile -scale-to 1500 -png GY1980_test.pdf qa/representative_098` for the final recursion-bound check. Rendered images are reproducible QA intermediates and are omitted from the archive.

**Acceptance: PASS.** This is a layout and completeness review. The independent mathematical proof review and exact computation outputs are separate evidence and are not replaced by this visual inspection.
