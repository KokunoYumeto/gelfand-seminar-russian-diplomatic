# Independent review of problem-index omissions

Reviewed 12 November 2026: the 248 occurrences and 16 problem entries in work/output/GY1964_items.json and GY1964_problems.json, against the 14 question-without-problem flags in work/evidence/data_audit_output.txt. The requested filename audit_data_output.txt is not present; data_audit_output.txt contains the relevant flags.

**Conclusion: add one solved problem entry for 1964-50.5, the invariant-subspace problem for subnormal operators. The other 13 omissions are defensible.** No final data files were edited.

## Decision rule and scope

CHAPTER_FORMAT.md requires a definite question or conjecture that recurs, was taken up by later literature, or remains open; it expressly discourages creating a problem for every occurrence. A question mark or the item kind “problem” therefore does not by itself require an index entry. Conversely, a definite historically open problem with an exact later solution belongs in the index even though it is solved today.

This was an editorial consistency review of the supplied statements, reconstructions, fates, and nearby occurrences, not a fresh literature search or an independent verification of every cited theorem. All existing item-to-problem and problem-to-item links were checked in both directions; there were no link errors.

## All 14 flags

| Occurrence | Decision | Reason |
|---|---|---|
| 1964-13.10 | Exclude | The proposed field-uniform character functor lacks a category, topology, transition maps, and a transfer assertion. Turning it into a specific modern conjecture would supply the essential question editorially. |
| 1964-19.3 | Exclude | The Behrens–Fisher model is definite, but the notes use it as a nuisance-parameter example. No level, sidedness, admissible test class, or optimality criterion identifies one research question whose resolution is being sought. |
| 1964-19.6 | Exclude | “Primary ideals on a ball” does not determine the function algebra, support, ideal, or requested property. The separately indexed maximal-ideal problem in 20.1 supplies the definite question; it should not be projected back onto this fragment. |
| 1964-25.3 | Exclude | Combining internal and spacetime symmetries is a broad programme. The analytic scattering, finite-particle, ordinary-Lie and regularity hypotheses belong to the later Coleman–Mandula formulation. Its partial match documents a development without recovering one exact notebook conjecture. |
| 1964-29.2 | Exclude | The identity-plus-compact sheaf analogy leaves section topologies, compactness, cohomology topology, and the index unspecified. Several inequivalent precise problems could be constructed from it. |
| 1964-29.3 | Exclude | Infinite-order ellipticity lacks a symbol class, growth conditions, function space, and definition of ellipticity. No single definite research question is recovered. |
| 1964-29.4 | Exclude | Continuous coefficients plus “hypoellipticity” does not determine the operator, solution class, or target regularity. A modern low-regularity conjecture would be an added question. |
| 1964-34.11 | Exclude | The cohomology reconstruction question leaves degree, coefficients, retained operations, and equivalence of systems unstated. It must remain distinct from the precise spectral-reconstruction question in 34.13. |
| 1964-41.2 | Exclude | Extending Dyson calculations to symmetric spaces is a developed direction, not one complete calculation or classification problem. The space, invariant measure, normalization, and observable remain to be chosen. Class B need not imply a separate definite problem entry. |
| 1964-44.2 | Exclude | With the inherited central-symmetry convention, this is exposition of an earlier projection-uniqueness theorem. Without that convention, elementary nonuniqueness already defeats the broad wording. No distinct later problem or residual question is identified. The adjacent central-section theorem is a different assertion, not recurrence of this exact question. |
| 1964-46.2 | Exclude | Asking what “angle” means for two subspaces leads to the established principal-angle invariants. It is an expository definition/classification request, with no new research assertion or residual problem. |
| 1964-50.5 | **Add** | The notebook explicitly says the invariant-subspace question for subnormal operators is unsolved. The modern statement is definite, and Brown's 1978 result is identified as an exact later affirmative solution. This meets the schema directly. |
| 1964-50.19 | Exclude | The literal two-sided measure-Volterra conjecture is refuted by the displayed atomless probability-measure example. The regular one-sided repair is prior Volterra theory. No later treatment of this exact two-sided conjecture, recurrence of it, or definite remaining classification problem has been established. Keep the counterexample in the occurrence rather than inventing a repaired open problem. |
| 1964-50.23 | Exclude | “Why invariant subspaces, and what could replace them?” is methodological. It does not specify a quantified assertion or one structural invariant that a later theorem could settle. |

## Recommended addition

Use the next available ID, provisionally GP-1964-17, without implying an already approved renumbering:

- **Title:** Invariant subspaces for subnormal operators.
- **Statement:** Does every bounded subnormal operator on a complex Hilbert space of dimension greater than one possess a nonzero proper closed invariant subspace?
- **Occurrences:** 1964-50.5.
- **Status:** As of November 2026: solved affirmatively by Brown in 1978. The publisher abstract explicitly confirms the theorem; the full subscription article was not read in this run.
- **Status date:** 2026-11.
- **Reference:** brown1978subnormal, with a citation to the abstract and pp. 310–333.

The occurrence should receive the same problem ID. A separate entry is preferable to folding it into GP-1964-07: the unrestricted Hilbert-space invariant-subspace question and its solved subnormal restriction have different hypotheses and present statuses. No additional research or mathematical reconstruction is required to make this addition from the evidence already recorded.

## Reviewed snapshots

- GY1964_items.json SHA-256: 73115ab4af4e772f1fe13a1693e23d0d44fa657717a30453dc7ef500a6dc6b0d.
- GY1964_problems.json SHA-256: f6f0fc4000dd121f3270ed0194e1bec00d8839a64c5b2f434b8615938bbcfbd8.
