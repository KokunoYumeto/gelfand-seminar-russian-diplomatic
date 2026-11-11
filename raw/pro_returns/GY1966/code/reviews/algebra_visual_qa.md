# GY1966 visual QA: PDF pages 97–144

## Scope and method

Read-only visual review performed on 9 November 2026. I inspected all four supplied contact sheets (`contact-097-108.jpg`, `contact-109-120.jpg`, `contact-121-132.jpg`, and `contact-133-144.jpg`) using the image viewer. I additionally inspected the individual rendered pages **104, 106, 109, 112, 114, 115, 116, 117, 121, 123, 127, 133, 138, 139, 142, and 144** at their supplied full resolution.

The inspected renders predate the final change of item 129.7's kind from `example` to `construction`; that known label update is correctly present in the structured data and is not treated as a current data defect. No deliverable files were edited during this review.

## Concrete finding

**Minor typography defect requiring correction:** the `\ours` marker runs into the following statement text at the starts of several development results. Examples actually visible in the renders:

- Page 114: `[proved here]For an even kernel` in Lemma 1.1 and `[proved here]Assume` in Theorem 1.2.
- Page 115: `[proved here]Under` in Corollary 1.3 and `[proved here]Let` in Proposition 1.4.
- Page 116: `[proved here]Take` in Example 1.5, `[proved here]If` in Remark 1.6, and `[proved here]For` in Proposition 1.7.
- Page 117: `[proved here]For` in Remark 1.8.

An explicit space after the marker at these result starts resolves the defect. The integrating editor was notified. A fresh render of the affected development pages is needed to confirm the correction; this review does not claim that a not-yet-inspected render is fixed.

## Other observations

**Pages 97–112, occurrence entries:** headings, class badges, field labels, and continuation pages are aligned consistently. No class badge collides with its title. The auxiliary-potential block matrix on page 104 and family-index criterion on page 106 fit comfortably within the text block. The hyperplane-section formula on page 109 and residue integral on page 112 render their subscripts, superscripts, Greek letters, and integral bounds legibly. The explicit restriction `x_0 > 0` is visible in the statement on page 112. The transition from record 127 to the record 128 heading is intact and does not create an empty page.

**Pages 113–117, development:** the numbered hypotheses and variance bounds have distinct equation numbers, adequate vertical spacing, and no collision with body text. The collision-expansion formula, truncation bound, L1 estimate, singular-kernel examples, and canonical correction all fit the page width. Proof-end squares are visible and not superimposed on formulas. The only defect found here is the missing word space after the proof marker described above.

**Pages 118–121, problem index:** long problem headings wrap within the margins. Problem identifiers, occurrences, statuses, and citations remain legible. Continued entries at the tops of pages have clear context. Page 121's final problem continues naturally to page 122 without an orphaned heading.

**Pages 122–138, corrections:** entries use consistent heading and field-label formatting. Full-resolution inspection confirmed Cyrillic glyphs on pages 123 and 133 and mathematical notation on page 123. The plain-text formula transcriptions and escaped underscores/carets on pages 127 and 138 remain readable; no literal LaTeX command residue, missing-glyph square, or clipped line was observed. The last correction ends with substantial but normal whitespace before the bibliography's chapter-opening page.

**Pages 139–144, bibliography:** the chapter-opening title, subsequent running headers, author names, accents, journal titles, DOIs, and URLs render correctly. Long URLs wrap within the text block, including those on pages 139 and 142. Entries remain distinct; normal entry continuations across pages do not collide with headers or page numbers. The final page ends cleanly within its bottom margin.

## Disposition

**Pass for clipping, overlap, page boundaries, mathematical glyph rendering, and section transitions in the inspected pages. One minor marker-spacing correction remains pending fresh visual confirmation.** This is a visual-layout review, not a claim to have independently rechecked every mathematical statement or every bibliography entry in the 48-page range.

The separate structured-data audit was rerun after the two earlier data/report corrections and now passes **15 of 15** audit groups, with no remaining issues in its stated scope.

## Final rerender confirmation — 146-page PDF

**Final result: PASS for the reviewed range, pages 97–146.** This final confirmation supersedes the earlier pending typography finding and the provisional page numbers above.

On 9 November 2026 I inspected all five final contact sheets in `research/pdfqa_final/`: `contact-097-108.jpg`, `contact-109-120.jpg`, `contact-121-132.jpg`, `contact-133-144.jpg`, and `contact-145-146.jpg`. These show all **50 final pages** assigned for this review. I additionally inspected final individual pages **111, 114, 116, 117, 118, 119, and 146** at full resolution.

- **The corrected item label is present:** final page 111 displays `1966-129.7` with `Kind; source. construction; P000205`. Its wrapped title, class badge, formulas, and assessment remain inside the text block.
- **The earlier marker-spacing defect is resolved:** the result starts on final pages 116–119 now separate `[proved here]` from the following text, either by a visible word space or a normal line break. The variance, truncation, canonical-gas, and effective-volume displays remain aligned and legible after reflow.
- **The final residue formula is intact:** page 114 retains the explicit `x_0 > 0` restriction and the properly positioned integral, exponent, and residue-form symbols. There is no collision with the adjacent body text or class badge.
- **No new layout defect was observed across pages 97–146:** no clipping, overlap, missing-glyph blocks, broken equation numbering, or collision with headers or page numbers. The problem-index, corrections, and bibliography transitions remain clear after pagination changed.
- **The bibliography ends cleanly on page 146:** the final Yau entry, DOI, URL, and verification label are visible within the bottom margin. Long bibliography URLs wrap within the text block; no final entry is cut off and there is no unintended trailing content.

No further correction is requested from this final visual pass. The original provisional observations above are retained as an audit trail of the defect that was found and then corrected.
