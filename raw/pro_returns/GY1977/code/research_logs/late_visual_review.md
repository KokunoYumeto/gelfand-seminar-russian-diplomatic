# Independent visual review: correction ending and bibliography

Review date: **10 November 2026**.

## Render identity

Before inspection, the SHA-256 of `delivery/GY1977/GY1977_test.pdf` matched `delivery/GY1977/code/output/qa/render_manifest.json`:

`63b3b43e07127617866b0eac3845f7b32be097a1cb7a14d97bfa22a42c25b8cc`

The manifest recorded **161 pages**. Its timestamp and the contact-sheet timestamp followed the PDF timestamp. The PDF and manifest hashes were checked again after the final page view and still matched this value. This review applies to that exact rendered version.

## Images actually inspected

- Contact sheet: `delivery/GY1977/code/output/qa/contact_151_161.png`, showing all eleven pages 151–161.
- Full-page images: `delivery/pdf_review_pages/page-151.png`, `page-154.png`, `page-155.png`, `page-158.png`, `page-159.png`, `page-160.png`, and `page-161.png`.
- Pages 151 and 154 were checked for the final correction entries, inline formulas, subscripts, superscripts, long headings, text wrapping, and the end of the correction section.
- Pages 155, 158–161 were checked for bibliography layout and long DOI/URL wrapping. Page 159 includes the final added MCCME catalogue reference. These bibliography pages use transliterated author/title forms; the requested long-DOI/URL case was therefore inspected rather than an absent Cyrillic entry.

## Findings

**No concrete visual defects identified in the inspected images.**

The correction mathematics renders without raw underscore/caret notation, missing glyph boxes, overlapping text, or clipping. The correction section ends cleanly on page 154, and the bibliography begins on page 155. Long DOI and URL strings wrap within the text area on the inspected bibliography pages, including the MathNet query strings, the Pavez-Cornejo DOI, and the MCCME catalogue URL. Page 161 retains its final entries within the page boundary. Headers and page numbers are visible and unobstructed.

No mathematical data, bibliography records, source statements, or build files were edited during this review. The later developmental-marker whitespace repair announced by the parent is outside this reviewed PDF hash; comparison with any subsequent renders remains part of the parent's final assembly check.

## Additional proof-page review after the marker-spacing repair

The next inspected PDF and render manifest matched SHA-256

`67d8e58fbe8164c92410168257ddcc72d6db57583c7a153b6ddc986d426dcef8`

before the image inspection. The parent confirmed that pages 151–161 in this version are pixel-identical to the correction and bibliography pages reviewed above.

Actually inspected at full-page size: `delivery/pdf_review_pages/page-131.png`, `page-132.png`, and `page-133.png`. Enlarged details from the page-132 and page-133 images were also inspected to distinguish the narrow space after an upright proof marker from the following italic capital.

**No concrete visual defects identified on these three pages.** The `[computed here]` markers are separated from the following words, including the same-line starts of Propositions 1.14 and 1.15. Occurrence references have the intended separation from their introductory prose. The transmission, scaling, Bianchi and Hermite displays, the interaction matrix, the loop-basis equations and the supersymmetry paragraph remain inside the text area, with no overlap or missing glyph boxes. The proof-ending squares are visible and unobstructed.

During this review, the parent began a subsequent build changing correction citation-label spacing. The findings in this subsection therefore attest specifically to the rendered hash above. The parent is checking pixel identity of the unchanged proof pages against that subsequent build. No research, mathematical-data edits or build-file edits were performed for this additional visual check.
