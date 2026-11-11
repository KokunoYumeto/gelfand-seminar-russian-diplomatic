# Final visual review: requested pages 36, 102, 121, and 156

## Reviewed version and method

- Source: `work/deliverable/GY1985_test.pdf`, 164 PDF pages.
- Build gate: `work/deliverable/audit/build_output.json` reported **PASS**, with no remaining layout/reference messages, before rendering.
- PDF modification time: **2026-11-11 09:43:10.045418 UTC**.
- Audit modification time: **2026-11-11 09:43:10.059856 UTC**.
- SHA-256: `37c570e640c61dcfa77d3a187ee215c54f70fd7a460236bba4e77b71119b7274`.
- PyMuPDF rendered each requested physical PDF page at scale 2, approximately 144 dpi, producing 1191 × 1684 pixel PNGs. Each full-page render was independently inspected with `view_image`.
- Rendered evidence: `work/strings/final_review/page_036.png`, `page_102.png`, `page_121.png`, and `page_156.png`. `render_manifest.json` records the page identification and source version.
- This was read-only QA. No source, PDF, or chapter content was edited.

## Verdict

**Layout passes on all four sampled pages:** no clipped text or formulas, overlapping blocks, margin collisions, broken glyphs, black replacement squares, or unresolved citation placeholders were observed. Running headers, page numbers, class boxes, and paragraph boundaries are readable and consistently aligned.

**Two residual typography issues remain in this reviewed version:** missing separation after some proof markers on page 121, and several joined prose/date tokens and raw mathematical shorthand on page 156. These do not obscure the mathematics but should be corrected for final editorial polish. The exact instances are recorded below.

## Page-by-page observations

### Page 36 — Liouville and determinant material

The page contains items 1985-650.8, 1985-650.9, and the beginning of 1985-650.10. Item titles and right-aligned class boxes remain clear, including the two-line title of 650.9. The curvature formula, exponential conformal factors, integrals, Seiberg-bound inequalities, and determinant powers are legible at the inspected scale. Author–year citations and theorem/equation locators render normally. Field labels are distinguishable from the body paragraphs. The final item continues at the page break after several substantive lines; its heading is not stranded. No corrective layout action is indicated.

### Page 102 — Jacobian recognition and moduli

The page begins with a legitimate continuation, then contains the Beltrami-coordinate and elliptic-moduli items. Inline theta/KP expressions, cohomology groups, dual pairings, the Beltrami smallness condition, group symbols, and inequalities stay within the margins. The multiline item title and class box do not collide. Citations to Shiota, Krichever, and Belavin–Knizhnik are readable and contain no placeholders. Paragraph spacing and line breaking are acceptable. No corrective layout action is indicated.

### Page 121 — supplied proofs

The Baker–Akhiezer expansions, hyperelliptic differential basis, and torus Beltrami formula are fully visible. Displayed formulas have adequate vertical separation; proof-ending squares sit clear of text. The bottom display is inside the page, with a visible lower margin. The continuation into the next page is not a clipping defect.

Residual spacing issue: the proof marker is immediately followed by the next italic word in two headings/intros:

- Lemma 1.8: `[proved here]Use the notebook's ...`
- Lemma 1.10: `[proved here]Write ...`

Insert explicit separation after the marker invocation in those places (for example `\ours\ ` or a suitable empty-group/space construction). Proposition 1.9 begins its statement on the next line, so the same adjacency is not visually problematic there.

### Page 156 — late corrections and provenance

The correction entries have clear headings and sufficiently separated reading/evidence paragraphs. The quotient formulas and Fourier derivative formula are legible. The Russian phrase **«всю C!!»** renders correctly; its Cyrillic letters are distinct, without missing-glyph boxes. Nothing overlaps or crosses a margin.

Residual joined-token and raw-shorthand instances visible on this page include:

- `dated24Feb86`, `check:24Feb85`, `Sunday,24Feb86`, `Monday,24Feb87`;
- `Catalogue24February1987`, `Manuscript24February1986`;
- `writes24.2.86`, `Beilinson's17Feb86`;
- `Triple(C,p,x)`, `Kontsevich1987section1`;
- `atp`, `throughp`, and `genus>=2`.

These should be normal prose spacing and, where appropriate, mathematical notation: for example “dated 24 February 1986,” “Kontsevich (1987), §1,” “at \(p\),” “through \(p\),” and “genus \(g\ge2\).” The date conflict itself is clearly communicated and is not an issue for this visual review. The word “Teichmueller” is readable; its romanized spelling is a stylistic choice rather than a font defect.

## Scope

This review covers only the four requested pages of the identified PDF version. It does not replace root's separate review of the overview, stacked diagrams, other proofs, or bibliography. No further mathematical research or substantive factual reassessment was undertaken.
