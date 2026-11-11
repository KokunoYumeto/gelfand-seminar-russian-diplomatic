# Independent visual review of the assembled GY1977 chapter

Review date: 10 November 2026. Reviewer: middle-records agent.

## Material actually inspected

The following three contact sheets were opened as images and every thumbnail was examined, covering 75 consecutive pages, 76–150 inclusive:

- `delivery/GY1977/code/output/qa/contact_076_100.png`: pages 76–100.
- `delivery/GY1977/code/output/qa/contact_101_125.png`: pages 101–125.
- `delivery/GY1977/code/output/qa/contact_126_150.png`: pages 126–150.

The following five full-page PNGs were then opened individually and examined at their supplied resolution:

- `delivery/pdf_review_pages/page-129.png`: KP development, Laurent coefficients, Hamiltonians, Poisson-bracket proof, and zero-curvature normalization remark.
- `delivery/pdf_review_pages/page-133.png`: Hermite interaction-matrix development and algebraic verification remark.
- `delivery/pdf_review_pages/page-134.png`: opening of the problem index and its first four entries.
- `delivery/pdf_review_pages/page-141.png`: corrections concerning source boundaries, the recovered P722 scan, and local algebra formulas.
- `delivery/pdf_review_pages/page-145.png`: corrections containing the KP Hamiltonian, Lax-operator formulas, instanton notation, and the record 435 date.

An earlier attempt to display six full-page images together produced a truncated tool response; those images were not counted as inspected on that basis. The five pages listed above were subsequently displayed and read individually.

## Layout observations

Across the 75 thumbnails, no clipping, overlapping text or equations, intrusion into page margins, collisions with running heads or page numbers, unexpected blank pages, or obviously defective page breaks were visible. Dense item text and classification boxes remain aligned. Section headings retain following content. The development section, problem index, and corrections retain consistent spacing and indentation.

The five full-page checks confirmed that displayed formulas, matrices, summation signs, equation labels, correction headings, and body text remain inside the text area. On page 141, the long recovered-scan URL and code path wrap within the available width. On page 145, the compact Hamiltonian and zero-curvature corrections remain legible and separate from their surrounding prose. Some paragraphs and correction entries continue across page boundaries, but the inspected breaks were ordinary continuations, without isolated headings or visible collisions.

This was a visual layout review of the specified rendered pages, not an additional mathematical or bibliographic review. The parent reported successful compilation with zero errors, warnings, and overfull boxes; that log result was not independently rerun here.

## Concrete typography observations reported to the assembler

1. The parent had already identified proof-status markers consuming trailing whitespace, such as `[proved here]With` and `[computed here]Let`. The same defect was visible on full pages 129 and 133. The parent reported adding explicit spacing after all 16 marker occurrences and a successful rebuild. This was not raised as a separate new defect.
2. Page 133, Remark 1.16: the rendered phrases `For occurrence1977-457.18` and `For occurrence1977-457.25` omit a space between the noun and the identifier. These were reported, and the parent confirmed adding both spaces to the deterministic typography repair script.
3. Page 141, first correction: `End of record426` in the heading and `in record426` in the critical reading omit the ordinary word–number space. Page 141, second correction evidence: `Gelfand–Dikii1977` omits the name–year space. All three were reported together to the parent for the final typography pass.

No other concrete visual defect was found in the inspected material. The images inspected here precede the final marker/spacing rerender; verification of those final repaired renderings remains with the assembler unless a subsequent review note is appended below.

## Edit scope

This review created only this report. No canonical data, fragment research files, generated chapter files, or build files were edited.

## Final development-page review

The rerendered full-page images `page-127.png`, `page-128.png`, `page-129.png`, and `page-130.png` in `delivery/pdf_review_pages/` were opened individually and visually inspected. These four page images correspond, as confirmed by the assembler and its render manifest, to the PDF SHA-256:

`67d8e58fbe8164c92410168257ddcc72d6db57583c7a153b6ddc986d426dcef8`

The inspected pages cover the integral finite-jet cohomology development, the Laplace-spectrum verification, the KP normalization verification, and the opening of the coin-weighing verification. Wrapping is clean: section and proposition titles, body paragraphs, displayed identities, long formulas, equation labels, and the proof endings remain within the text area without collisions or clipped characters. Continuation of the final remark from page 130 is an ordinary paragraph continuation.

The proof-status markers are separated from the following prose. The narrow visual gap before italic `Suppose` on page 130 was additionally checked against the current source (`\ours{}` followed by a newline) and PDF text extraction, which explicitly reads `[proved here] Suppose exactly`; the other page-130 marker reads `[proved here] When`. The text extraction was from the subsequent correction-only rebuild, SHA-256 `5175541e8358a5c5fbc77e4ece6b24e6ae50fce6e79ea80b3c0d0156ad72833f`. The assembler confirmed that the development content was unchanged between these two PDFs; the intervening edits concerned author–year spacing in the corrections only.

No remaining concrete defect was found in these four development pages. The assembler is responsible for comparing these stable page images with the last correction-only build and checking any changed correction-page images. This addendum certifies the explicitly identified render, not an uninspected later file.
