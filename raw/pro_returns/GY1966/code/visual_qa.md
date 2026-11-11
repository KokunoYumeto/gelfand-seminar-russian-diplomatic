# Final PDF visual verification

**Result: PASS.** The final `GY1966_test.pdf` has 146 pages. Every page was
rendered with Poppler at 85 dpi, decoded fully to RGB, and inspected in numbered
contact sheets. Selected pages were also inspected individually. The final
render followed the last XeLaTeX pass with resolved cross-references.

| Final pages | Inspection | Outcome |
|---|---|---|
| 1–48 | Four contact sheets; individual pages 24, 29, 36, with earlier detailed checks of the corresponding formula pages | No clipping, overlap, bad glyphs, or stranded item starts observed; the factorial-density display punctuation is corrected. |
| 49–96 | Four contact sheets; individual final pages 61, 78, 83, 84, with the continuation check extending to 97–98 | Both stranded item starts, the empty-field heading punctuation, and the two short continuation widows are corrected. |
| 97–146 | Five contact sheets; individual final pages 111, 114, 116–119, 146 | Equations, class badges, headings, and bibliography are within the margins; item 129.7 displays `construction`; the final reference is complete. |
| 115–120 | Independent individual-page inspection of all six development pages | All eight proof-marker spaces are corrected; displayed bounds, integrals, equation numbers, citations, proof endings, and transitions are legible. |

The first inspection used a 144-page draft. It found two item headings separated
from their body text, two short continuation widows, unnecessary punctuation in
heading-only records, missing spaces after eight `\ours` markers, and punctuation
placed on a new line after one display. These were corrected, the document was
compiled twice to settle references, and the complete 146-page final version was
inspected again. The earlier observations and the explicit final confirmations
are retained in `code/reviews/`.

The final log has no TeX errors, undefined references or citations, missing
characters, font substitution warnings, or overfull boxes. Modest underfull-line
diagnostics remain; the rendered pages have acceptable spacing. Font embedding
is recorded in `code/build/pdffonts.txt`. The overview occupies the first page
and part of the second, meeting the requested one-to-two-page length.

The local Poppler multi-page export occasionally produced a truncated PNG while
returning success. The QA script detects decode failures and rerenders the
affected pages separately. Only fully decoded images were admitted to the final
inspection. The delivered PDF itself had no corresponding defect. Raster
intermediates are reproducible with `code/render_pdf_qa.py` and are not included
in the archive.

This is a visual and production check. The schema audit and independent
mathematical reviews are separate records; visual inspection is not evidence
for a mathematical claim.

A final automated extraction check detected one additional inline proof-marker space
in item 1966-109.2. It was corrected and page 49 was rerendered and inspected.
All other pages retained identical extracted text and word geometry; the document
remains 146 pages. This final local check supplements the complete inspection above.
