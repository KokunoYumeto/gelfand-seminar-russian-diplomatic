# Final integration consistency review

**Date:** 2026-11-10. **Scope:** read-only comparison of `GY1979_report.md`, `GY1979_overview.tex`, merged talk/item/problem JSON, the final early batch, and existing verification outputs. No further literature research was performed. No merged or final file was edited.

## Confirmed

- All numerical totals match the merged files: **27 records, 252 items, 10 problem threads, 104 bibliography entries, 106 correction rows**.
- Class counts agree: **A12, B7, C3, D0, E203, F27**. Verification counts agree: **197 read the result, 23 publisher metadata checked, 27 indirect, 5 unresolved lead**.
- The final change of **463.3 / GP-1979-05 from provisional C to B** is present. Its infinitely-many-invariants quantifier and the single-extra-invariant distinction are retained. Neither report nor overview calls this an open problem.
- **468.12 is E**, and the report correctly explains why a finite coefficient kernel is already an effective answer. Its bounded structural development does not imply historical novelty or global openness.
- The report's commutant dimensions **17, 20, 23, 24, 29, 30, 32**, **36 exact examples**, and **1,706 basis-product checks** agree with the development and saved output. The energy diagnostic correctly disclaims a reducibility counterexample.
- P000840 is consistently prior carry-in **1978-460.12–20**; P000917–918 are consistently excluded from current-year occurrences. The updated BGG prior occurrences are retained.
- Sergeichuk chronology is correct in the item/development: **1999 preprint, 2000 journal, 2007 repository deposit**. The report's 2000 author–year citation does not contradict that chronology.

## Material consistency fixes

1. **Record 465 source span.** Merged `talks.pages` is `P000849-P000853`, but its own summary correctly says Kallosh's programme begins at the foot of P000848. For an actual-talk-span interpretation, use **P000848-P000853**. If `pages` intentionally means only pages containing indexed mathematical items, make that narrower convention explicit. All other early source spans agree with the critical boundaries.

2. **Normal-form development flag.** The report and `dev:berezin-normal` explicitly supply three proved propositions and an example for **468.11**, but its `development` field remains `annotated`; only 468.12 has `developed in this chapter`. Consider marking **468.11 developed in this chapter**. This describes work performed here, not a novelty claim, and is consistent with its B classification. Otherwise explain why the substantial normal-form subsection is excluded from this metadata category.

3. **Energy-proof attribution.** Report §2 says a “later author correction” identifies the defect. That can wrongly suggest a correction by Shimada himself. The checked diagnoses are by **Hasebe and Ando**. Prefer **“later primary papers identify a specific noncommutative differential identity used incorrectly.”** Overview's **“uncorrected proof claim”** also exceeds the deliberately bounded current-status search; prefer **“a published proof claim with a documented gap.”**

## Smaller wording and chronology qualifications

4. **Correction taxonomy.** Overview says the 106 corrections distinguish mistranslations or mistranscriptions. The CSV contains **75 faithful_error, 17 ambiguity, 14 provenance**, with no rows tagged translation or transcription. Safer wording: **“The 106 annotations distinguish faithfully transcribed mathematical errors, unresolved readings, and provenance discrepancies.”**

5. **Conference fragments and counting rule.** Report §1 says nonmathematical conference-name lists remain in summaries rather than separate items. Items **462.2–4** deliberately preserve underdetermined mathematical conference reports as F occurrences. Clarify the rule, for example: **“Bare reading lists remain contextual; mathematically intended but underdetermined conference reports are retained as F occurrences.”** The current count does not require changing.

6. **463.2 and the A chronology label.** This item is A, but its exact formula locator is the **1988** paper. The **1980** article was verified at metadata level, not read for that exact formula. The surrounding text should preserve **“early programme identified in 1980; exact formula read in the 1988 expansion”**, rather than imply an independently verified exact soon-after theorem match. This is an evidence qualification, not a newly established reason to change the class or counts.

## No stale classification narrative found

The overview/report correctly separate A/B publication chronology, E exposition, C residual scope, F identification limits, and proof work performed in this chapter. In particular, the new B classification of the resonance question does not leave a stale open-problem assertion in the reviewed prose. The normal-form/wildness discussion does not claim that canonical algorithms are impossible, and the commutant discussion does not manufacture an open problem to justify a bounded development.
