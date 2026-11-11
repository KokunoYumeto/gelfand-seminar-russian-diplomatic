# Development-section visual QA

Reviewed on 9 November 2026. This was a read-only inspection; the deliverable was not edited.

## Scope and version

- PDF: `deliverable/GY1966_test.pdf`, 144 pages.
- SHA-256 of the inspected PDF: `775758437f2aecc0093c90cf8f61af01a614b1775bf136f92420f007f3945b6b`.
- PyMuPDF locates section **1.39 Developments** on physical PDF page **113**. The development ends with two lines at the top of page **118**, before section 1.40 Problem index. Printed page numbers agree with physical PDF page numbers.
- Full-page images actually viewed: `research/pdfqa/page-113.png`, `page-114.png`, `page-115.png`, `page-116.png`, `page-117.png`, and `page-118.png`. Every development page was inspected individually at full-page resolution, rather than only in a contact sheet.
- Supplementary PyMuPDF checks found no text spans outside the physical page rectangle and no Unicode replacement glyph in the extracted text of pages 113–118. These checks supplemented, rather than replaced, the visual inspection.

## Finding requiring a small correction

**Repeated missing space after the editorial marker.** On pages 114–117 the marker `[proved here]` touches the next word. The eight affected result headings are Lemma 1.1, Theorem 1.2, Corollary 1.3, Proposition 1.4, Example 1.5, Remark 1.6, Proposition 1.7, and Remark 1.8. Visible examples include `[proved here]For`, `[proved here]Assume`, `[proved here]Under`, `[proved here]Let`, `[proved here]Take`, and `[proved here]If`.

The source `deliverable/GY1966_development.tex` has a bare `\ours` at the end of each corresponding heading line. An explicit control-space after each, `\ours\ `, will separate the marker from the following text. The `[computed here]` marker on page 117 already has an explicit following space and renders correctly. This is a spacing defect only; no mathematical content is missing or obscured. Reported to the coordinating agent during inspection. No fix was applied by this reviewer.

## Page-by-page observations

| PDF page | Development content inspected | Rendering observations |
|---|---|---|
| **113** | Section and subsection headings; historical scope; Minlos citation; subsequent literature scope; ordered-pair observable; factorial-density definition. | Heading hierarchy and margins are consistent. Both displayed formulas are complete and readable, including summation conditions, integral domain, and differential factors. Minlos (1968), Pulvirenti–Tsagkarogiannis (2015), and Kuna–Tsagkarogiannis (2018) citations resolve to normal author–date text, with no question marks or raw citation keys. Ordinary line-end hyphenation is legible. The factorial-density definition continues with “for nonnegative measurable h” on page 114; the display itself is not split or clipped. |
| **114** | Covariance density; assumptions (1.1)–(1.2); Lemma 1.1 and proof; variance identity (1.3); Theorem 1.2; bounds (1.4)–(1.5); Chebyshev display; start of theorem proof. | All equation numbers align at the right margin without colliding with formulas. Double sums, subscripts, integrals, norms, fractions, absolute-value bars, and indicator conditions are intact. The lemma proof ends with a visible QED square. The theorem proof continues normally to page 115; no display is cut by the page boundary. The missing marker spaces affect Lemma 1.1 and Theorem 1.2. |
| **115** | Cross-edge integral bound; finite-size correction display; end of Theorem 1.2 proof; Corollary 1.3; concentration display (1.6); truncation proof and L1 bound; Proposition 1.4 and its mean formula. | Every proof display stays inside the text area. In (1.6), the probability delimiters, normalization, two right-hand terms, and equation number are distinct and readable. The theorem and corollary QED squares are visible. Proposition 1.4 has several full lines and both formulas before its proof continues on page 116, so its heading is not orphaned. The long corollary heading wraps but remains legible. Missing marker spaces affect Corollary 1.3 and Proposition 1.4. |
| **116** | Proof of Proposition 1.4 and overlap formula; Example 1.5 and its proof; Remark 1.6 with shell-singular kernel; Proposition 1.7 with canonical densities and variance bound. | The overlap-volume quotient, singular exponents, indicator subscripts, falling-factorial notation, and the hard-core kernel's nested absolute-value/norm bars render clearly. The two completed proofs have visible QED squares. All displayed bounds and inline formulas fit the text area; there is no overlap with the footer or header. Proposition 1.7's proof starts on page 117 after its complete statement and displays. Missing marker spaces affect Example 1.5, Remark 1.6, and Proposition 1.7. |
| **117** | Canonical-identity proof; Remark 1.8 and effective-volume display; independent-checks account; remaining-obstruction discussion. | The falling-factorial expressions and reciprocal effective-volume display are intact. The canonical proof's QED square is visible. The monospaced code filename renders with its underscores and no clipping. The `[computed here]` marker is correctly spaced. The final prose paragraph continues by two lines on page 118, with no cut or overlap. Remark 1.8 has the repeated missing marker space. |
| **118** | Final two lines of the development; transition to the problem index. | Both closing lines are fully visible. The next section starts with clear vertical separation and a normal heading. No stray equation number, unresolved citation, orphaned proof marker, or residual fragment appears at the transition. The remaining page belongs to the problem index and was not treated as development content. |

## Outcome

No clipped equations, missing mathematical glyphs, overlapping text, misplaced equation numbers, unresolved citations, or broken proof displays were found in the development section. The only concrete visual defect found is the missing interword space after eight `[proved here]` markers. After that spacing edit, the affected pages should be regenerated and checked for any changed line breaks.

## Final review after the spacing correction — 146-page version

This final review supersedes the outstanding spacing finding above. All six full-page final images were opened and visually inspected: `research/pdfqa_final/page-115.png` through `page-120.png`. In this version, section 1.39 begins on **page 115** and its closing two lines appear on **page 120**, immediately before the problem index.

| Final PDF page | Final visual check |
|---|---|
| **115** | Development title and historical discussion are intact. Both displays, the factorial-density definition, and the author–date citations remain legible. No clipping or changed-margin problem is visible. |
| **116** | The markers for **Lemma 1.1** and **Theorem 1.2** are now separated from “For” and “Assume.” All displayed collision terms, bounds (1.1)–(1.5), integral limits, norms, probability delimiters, and right-aligned equation numbers remain clear and unobstructed. |
| **117** | The markers for **Corollary 1.3** and **Proposition 1.4** are correctly separated from their statements. The corollary's statement now starts cleanly on the following line. The truncation estimate (1.6), expectation bounds, L1 bound, and mean-identification displays remain fully legible; no display is clipped at the page boundary. |
| **118** | **Example 1.5**, **Remark 1.6**, and **Proposition 1.7** all have correctly spaced markers. Where the following sentence moves to the next line, it remains a complete, normally set paragraph. The singular-kernel exponents, nested norm/absolute-value bars, factorial densities, canonical bounds, and variance display remain readable and within the text area. |
| **119** | **Remark 1.8** now has a visible space before “For.” Its effective-volume display and the preceding canonical proof remain intact. The computed-here paragraph, code filename, and concluding discussion have no clipping, overlap, or unusual line-break defect. |
| **120** | The final two development lines are complete and legible. The transition to section 1.40 is clean, with normal vertical separation and no orphaned formula or proof marker. |

**Final outcome:** the missing space is corrected at all eight result markers. Equation legibility, proof-display layout, citations, and page transitions remain satisfactory throughout pages 115–120. No remaining visual defect was found in this assigned section. No mathematical re-review, optional retesting, or deliverable edit was performed.
