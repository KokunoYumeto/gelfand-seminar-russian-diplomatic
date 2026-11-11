# Final report and overview consistency review

**Date:** 2026-11-10. **Reviewed:** `deliverable/GY1976/GY1976_report.md`, `GY1976_overview.tex`, the final JSON/CSV/BibTeX data, source-scope sidecars, development text, and relevant saved checks. The temporary build/visual-QA placeholder was deliberately excluded from the review. No final deliverable files were edited and no new broad literature search was undertaken.

## Verdict

**No substantive inconsistency in the mathematical summary, counts or source scope was found.** The account of historical fate, uncertainty and absence of research novelty is appropriately limited. Two small wording changes would make the proof-audit claims exactly match the saved work.

## Concrete wording issues

### 1. Narrow the Berezinian audit-table description

In report §4, the row “Berezinian and super-coordinate shift” currently describes its first derivation as:

> Derive the correct determinant and boundary-coordinate formulas

The saved material gives a diagonal `1|1` Berezinian test, cites the general block formula, and directly expands the nilpotent circle/half-line changes. It does **not** supply a derivation of the general Berezinian determinant formula or its multiplicativity. The present wording could be read as claiming that broader proof.

**Suggested replacement:**

> Check the diagonal Berezinian and expand the nilpotent circle and half-line coordinate changes

The existing third-column wording about exposing the reciprocal and missing divisor remains accurate. Evidence: development subsection “Critical checks on the Berezinian and flatness signs”; `code/middle_checks.py` and its output; occurrences 1976-406.8, .13, .14 and .15.

### 2. Limit the universal authorship-macro claim to the development section

Report §4 says:

> Every result proved or computed for this task is marked with the supplied `\\ours` or `\\oursComputed` convention.

The central development results are marked, but some elementary computations in item reconstruction fields, such as the circle expansion in 1976-406.14 and half-line coefficient in .15, are identified as editorial reconstructions without those macros. Their provenance is clear; the report's universal wording is broader than the literal tagging.

**Suggested replacement:**

> In the development section, the results proved or computed for this task carry the supplied `\ours` or `\oursComputed` markers; the item reconstruction fields separately identify editorial additions.

The report is Markdown, so a single literal backslash inside each inline-code span is sufficient. The source currently displays two.

## Confirmed against the final data

- **250 occurrences**, comprising **227 core** plus **23 corrected-1978 appendix occurrences**.
- Entire-package classes **A 55, B 2, E 176, F 17**; core classes **A 45, B 2, E 163, F 17**; appendix **A 10, E 13**.
- **23 records, 15 problem entries, 65 bibliography entries, 108 correction rows**.
- Every record-level count, attributed-speaker count, primary-area count, literal-correctness count, publication-match count, verification-depth count and editorial-development count agrees with the JSON or source-scope sidecar.
- The page ledger has **55 pages**, partitioned into **46 core, 4 record-437, 5 adjacent-context pages**, as reported. Corrected `1977-437.n` and `GP-1977` identifiers agree with the actual academic-year rule.
- The source order around P000699 is consistently **414, 416, 415, 417**. Headings/plans remain included without invented item counts.
- The supplied Russian and English transcriptions in `sources/` are byte-for-byte identical to their attached originals.
- The record-437 summary explicitly distinguishes its January 1978 receipt date from public circulation and says that A denotes subsequent publication, without claiming discovery after the February lecture.

## Assessment of evidential and novelty claims

The report correctly distinguishes opening a bibliographic URL from reading a particular theorem, explicitly limits “read the result,” and does not turn failed searches into proofs of nonexistence. The negative-search examples remain F, not fabricated open questions. The source-matching table supplies concrete formulas or result locators and separates original publication, translation, receipt and preprint dates.

The overview and report correctly restrict the critical audits: the trace identity does not purport to construct a projector without analytic boundary prescriptions; vanishing along one ODE solution does not establish point flatness; finite matrix checks do not establish the all-dimensional contraction theorem; the packet counterexample explicitly needs compactness and unitarity; the raw BGG kernel example exposes an omitted grading convention without contradicting BGG. The final inverse-indexing remark expressly relies on reciprocity and does not claim a new proof of it.

The absence of C/D work is presented as a conclusion about the identifiable questions and evidence in this package, without asserting that every surrounding field is closed. The critical-verification text makes no claim of a newly solved open problem. No change to counts, classifications, problem identity, source scope or proof conclusions is recommended by this review.
