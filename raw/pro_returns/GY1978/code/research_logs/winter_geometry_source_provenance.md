# Winter source boundaries and the source-established Fuchs addition

Audit date: 10 November 2026. Both supplied English and Russian text have been read for P812–P825 and P829, with the mathematical formulas and all talk transitions checked against the supplied scans. The fourteen-entry catalogue in `GY1978_talks.md` is not an exhaustive inventory of the dated talks present in those files. Record 457 below is a transparent source-established addition; it is not silently inserted as if the supplied list contained it.

## Assigned records and actual boundaries

| Record | Source-supported extent | Boundary evidence | Coverage |
|---|---|---|---|
| 452 | Upper P812, before the underlined Belavin heading | “Что нужно знать? (по А. А. Белавину)”; reading programme, catalogue attribution to I. M. Gelfand | Plan; zero mathematical items. Reading titles do not create invented problems. |
| 453 | Lower P812 through P815 | Separate Belavin heading; next dated Belavin talk starts P816 | 20 items: ADHM, gauge averaging, chain and continuum fermions, bosonization, exchange algebra, Baxter weights, transfer matrices. |
| 454 | P816 through P820 | “19/II-79г.” and Belavin at P816; new dated speaker at P821 | 26 items, including the literal eight-vertex equation error and the exact spin-one obstruction. P820's last commutation condition is unfinished. |
| 455 | P821–P822 | “26.2.79г.”, S. Gelfand, “from a lecture by Manin”; Beilinson heading starts P823 | 14 items: conformal/Grassmannian geometry, holomorphic connections, variational equation, incidence and third-neighbourhood criterion. |
| 456 | P823 only | Separate A. Beilinson heading; new date and Fuchs at P824 | 4 items. Date 26 February comes from the catalogue and preceding dated session; P823 carries no independent date. |
| 457, added | P824–P825 and P829 only | P824 visibly reads “5/III-79” and “Д. Б. Фукс”; P829 resumes a Lie-algebra construction; Ogievetsky begins P830 | 12 items for every supplied segment. P826–P828 are absent, so neither a complete lecture nor their detailed contents are claimed. |

The first evidence wrapper on P829 is itself incorrectly labeled `GELFAND-P000826`, although its `SourcePage` command and the actual scan are P829. This is a wrapper-provenance error, not evidence that P826 was supplied.

## Why the earlier occurrence IDs are aliases

The previous index contains precisely the same mathematics under incompatible academic-year and talk boundaries. The original IDs are retained in notes and mappings for traceability. They must not be presented as evidence that the same question was discussed in 1977 and then again in 1979. The attached previous index gives titles and classifications; it does not supply the missing earlier chapter's complete statements.

| Prior-index ID | Available source segment | Current occurrence(s) | Exact relationship |
|---|---|---|---|
| 1977-451.11 | P812, quaternionic instanton matrices and parameter count | 1978-453.1–2 | Same paragraph; split into construction and dimension in this chapter. |
| 1977-451.12 | P812, “beautiful” parametrization question | 1978-453.3 | Same aesthetic request; no fixed rational/global criterion. |
| 1977-451.13 | P812, gauge averaging and confinement inference | 1978-453.4–5 | Same source argument; valid vanishing and invalid confinement inference separated. |
| 1977-457.1 | P823, flag projections | 1978-456.1 | Beilinson, not Fuchs. |
| 1977-457.2 | P823, horizontal sections and descent | 1978-456.2–3 | Same null-curve argument, split for its local hypotheses. |
| 1977-457.3 | P823, reverse transform and quadric triviality | 1978-456.4 | Same final line. Full Yang–Mills additionally needs the preceding third-formal-neighbourhood condition. |
| 1977-457.4 | P824, grading and adjoint transitivity | 1978-457.1 | Same definition, corrected classification scope. |
| 1977-457.5 | P824, four vector-field families and classification claim | 1978-457.2–6 | Same source list, separated into four definitions and the hypothesis-sensitive classification assertion. |
| 1977-457.6 | P824 lower part and P825 equations (7)–(13) | 1978-457.7 | Same maximal-prolongation construction. “Everything recovered” requires maximality and a specified faithful action. |
| 1977-457.7 | P825, recursive bracket via Jacobi | 1978-457.8 | Same bracket construction. The polynomial realization used to justify existence is explicitly an editorial explanation, not a claim to the missing next page. |
| 1977-457.8–16 | Not present as developed statements in supplied P824–P825/P829 | No new occurrences assigned | Titles suggest a polynomial realization, rank-one criterion, an infinite-dimensional/Poisson suggestion, generalized Cartan matrices, Serre relations, root and height gradings, growth, centre and untwisted loops. Those missing segments are not reconstructed from titles. P825's last sentence only starts another construction. |
| 1977-457.17 | Upper P829, involution and alternating loop coefficients, negative transpose on sl(3) | 1978-457.9–10 | Same construction and example. It is centreless; central extension and degree derivation are not on the page. |
| 1977-457.18 | Middle/lower P829, coefficients congruent to j−i modulo 3 | 1978-457.11 | Same bracket, identified explicitly with Laurent loops of sl(2). Graded simplicity and ordinary simplicity differ. |
| 1977-457.19 | P829, “three simple ones” and final exhaustion sentence | 1978-457.12 | Same incomplete assertion. Only one example is supplied, and its unconventional grading fails local generation by degrees −1,0,1. |
| 1977-457.20–25 | P830–P831, Ogievetsky's dated 19 March 1979 talk | Root/spring agent's record 458 | Displaced into the prior Fuchs entry. These are not Fuchs content or evidence of a 1977 recurrence. |

## Mathematical content of the added Fuchs record

The added record does not depend on inventing material from missing pages:

1. The adjoint maps to `Hom(g_-1,g_(i-1))` and `Hom(g_1,g_(i+1))` define the displayed transitivity conditions. Finite-dimensional pieces, local generation, irreducibility and simplicity are additional classification hypotheses.
2. Polynomial vector fields have degree-zero algebra `gl_n`; divergence-free fields preserve volume; Hamiltonian fields preserve a fixed symplectic form; contact fields preserve a distribution and require a weighted depth-two grading. These are all already classical.
3. For a finite-dimensional faithful pair `h ⊂ gl(V)`, the symmetric-tensor intersection defines the **maximal** depth-one Cartan prolongation. Arbitrary transitive extensions embed in it and need not equal it. Jacobi determines the bracket recursively, and polynomial vector fields establish existence.
4. An involutive Lie automorphism gives the alternating twisted loop subalgebra. Negative transpose on `sl_3` has `so_3` fixed part and five-dimensional symmetric traceless negative part.
5. The period-three basis rule identifies a centreless `sl_2` Laurent loop algebra. An explicit basis map is in item 1978-457.11. Evaluation at the loop parameter 1 gives a proper nonzero ungraded ideal. The degrees −1,0,1 span a constant `sl_2`, so this particular grading does not meet Kac's local-generation convention.
6. The “three” and “exhaust everything” claims cannot be matched to a theorem with definite quantifiers. The finite-growth theorem does not license omission of its hypotheses, and missing pages cannot be treated as evidence that those hypotheses were said.

Primary checks: Kac (1968), introduction and Chapters I–IV as specified in `research_log.md`; Guillemin–Quillen–Sternberg (1967), publisher metadata; Fu–Hwang (2010), Definition 2.1. Their verified URLs and bibliographic records are in `refs.bib`. The pre-existing classification results make this exposition class E where identifiable; the incomplete final universal assertion remains F. No new open Fuchs problem is created.

## Problem-ID discipline

GP-1977-05, fixed-charge instanton classification and connectedness, is not reused for the word “beautiful”: the latter supplies no rationality, connectedness, global-coordinate or algorithmic criterion. GP-1977-10 and occurrence 1977-436.16 provide a thematic quantum inverse-scattering link, but do not have the same quantifiers as either the finite periodic XYZ diagonalization problem or the specific spin-one deformation question. Record 1977-431 concerns commuting ordinary differential operators and is not the relevant quantum inverse-scattering occurrence.

## Limits of the source-established addition

The catalogue's record-457 URL was attempted but inaccessible through the browsing tool. The number is the missing integer between the supplied records 456 and 458 and is also present in the previous index; the dated speaker identification is independently visible on the scan. The report must explicitly say **fourteen commissioned records plus one source-established partial addition**, not claim that the supplied catalogue itself contained fifteen entries. The surviving pages establish the lecture's date and speaker but not its full missing middle.
