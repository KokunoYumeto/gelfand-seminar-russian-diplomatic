# Root research and verification log

Status date: 12 November 2026. Primary and independently repeated checks are distinguished from indexed leads.

## Scope and provenance

- Read all six attached-file names and the entire task prompt and supplied chapter format.
- `audit_inputs.py` hashes the supplied inputs and confirms that `previous_index.md` contains 247 items from this same academic year, no earlier-year occurrence identifiers, and no problem identifiers. `references_cumulative.bib` has no entries.
- Opened the original MCCME catalogue, <https://old.mccme.ru/gelfand/notes/all-links.html>. Its first 49 substantive records agree with the supplied list; record 23 is a plan. The source order used in the chapter is the supplied catalogue sequence, without sorting by date. Source-page citation inside each item identifies actual notebook placement, including interleaving.
- The supplied upper page envelope includes the next academic year: P000090 begins Kohn's 20 September material, rather than continuing Halmos. This is excluded from the 1964–65 item count and retained as a provenance correction.
- Root independently viewed full scans P000011, P000088 and P000089, and read their Russian and English text. The Bishop weight, irrational rotation, separate cyclicity sentence, and lower integration endpoint zero in the Volterra suggestion are visible. The strict/non-strict contraction sign on P88 remains ambiguous; no invisible stroke is supplied.

## Bishop operators

Queries included: `Bishop operators invariant subspaces cyclic vectors irrational alpha Chamizo Gallardo Monsalve 2024 2025 2026`, `Bishop operators cyclicity all irrational Chalendar Partington 2025`, `Bishop operators cyclic 2024 2025 2026`, and the exact Ma title. Current-status searches used the stronger search engine and recent-year filters.

- Béhani, *A study of Bishop operators from the point of view of linear dynamics*: <https://arxiv.org/pdf/2207.11419> opened as a 26-page primary manuscript. Read rational determinant Theorems 4.4 and 4.5, generic theorem 4.9, gap theorem 4.16, and final open questions. First arXiv posting 23 July 2022; journal metadata found at the publisher: JMAA 526(1), 127204 (1 October 2023), DOI 10.1016/j.jmaa.2023.127204. Direct publisher open returned 403; the manuscript was read successfully.
- Chamizo, Gallardo-Gutiérrez, Monsalve-López, and Ubis: <https://arxiv.org/abs/1812.08059> and <https://arxiv.org/pdf/1812.08059> opened. Read Theorem 3.7 (a sufficient denominator-growth condition) and Theorem 4.1 (a limit of the method). First posted 19 December 2018, journal publication Advances in Mathematics 375 (2020), 107365, DOI 10.1016/j.aim.2020.107365. Locators in the chapter refer to the opened 2018 version.
- Ma, *Rational Bishop determinants and explicit cyclicity criteria*, arXiv:2608.27946 (28 August 2026): repeatedly retrieved indexed primary abstract metadata. Direct arXiv abstract, HTML and PDF opens returned DisabledError. It is therefore an **unverified lead**, not an assumed theorem. The advertised (9,16) example was independently established by the chapter's own exact arithmetic; no novelty is claimed.
- Abadias and Monsalve-López, *Regular fractional weighted Wiener algebras and invariant subspaces*, JMAA 553(2) (2026), 129875, DOI 10.1016/j.jmaa.2025.129875: publisher-indexed abstract found, but publisher and institutional PDF opens failed (403/timeout). This supplementary lead is not used for a technical claim or included in the chapter bibliography.

## Random-walk audit

- Pönitz and Tittmann (2000), <https://www.combinatorics.org/ojs/index.php/eljc/article/view/v7i1r21>, DOI 10.37236/1499: primary abstract and metadata opened. The square-lattice upper bound 2.679192495 already suffices to disprove the exponential-rate conjecture mu=e under the uniform square-lattice SAW interpretation.
- Duminil-Copin and Hammond, <https://arxiv.org/pdf/1205.0401>: primary 27-page manuscript opened; Theorem 1.1 and Corollary 1.2 read. The sampling law is uniform among length-n nearest-neighbour self-avoiding walks on Z^d, d>=2. The theorem proves exponential suppression of ballistic displacement, not the planar three-quarter exponent. Posted 2 May 2012; journal metadata identifies Communications in Mathematical Physics 324(2) (2013), 401–423, DOI 10.1007/s00220-013-1811-1.
- Couronné, <https://link.springer.com/article/10.1007/s10955-025-03542-6>: primary publisher abstract opened (published 31 October 2025, JSP 192, article 153). Bound 2.662343. <https://arxiv.org/abs/2211.16146> also opened: first posting 29 November 2022, revision 6 December 2022. Thus first circulation and journal publication differ substantially.
- Tomar, <https://www.mefyi.com/papers/connective-constant-bound/>: primary author page opened, including abstract and explicit preprint status. First posted 21 October 2026, DOI 10.5281/zenodo.23540764; claims an exact certificate giving 2.6586513. The certificate was not downloaded or independently rerun; reported only as a recent preprint claim, unnecessary for the refutation of mu=e.
- September 2026 OpenAI honeycomb-walk papers appeared in current searches. The primary GitHub page for *Mass and covering exponents for fixed-length honeycomb walks* opened as repository metadata; the main TeX endpoint did not open. No theorem from this lead is used. Its lattice and diameter observable also do not directly match the source's expected endpoint displacement on the square-lattice interpretation.

## Donoghue and Volterra audit

- Yakubovich, <https://www.mathnet.ru/eng/znsl4181>, primary abstract and bibliographic metadata opened. Russian publication 1985, Zap. Nauchn. Sem. LOMI 141, 100–143; English translation 1987, J. Soviet Math. 37(5), 1323–1346, DOI 10.1007/BF01327041. Monotone moduli decreasing to zero are a sufficient condition for unicellularity; that does not constitute a necessary-and-sufficient classification for arbitrary weights.
- The whole-line Volterra conjecture admits a source-relevant atomless counterexample: probability density 1/2 on [-1,1] with integration from 0 splits the two half-interval L2 spaces into nonzero incomparable invariant subspaces. This reasoning was communicated to the source reviewer for the item's annotation. It does not depend on conventions at atoms.

## Independent mathematics and computation

- `bishop_certificates.py` constructs rational fibres, compares direct cyclic matrix powers with product formulas for all 31 coprime pairs with 2<=q<=10, and computes five rational least-squares certificates with direct residual verification.
- `independent_bishop_check.py` uses no symbolic-algebra library or import from the first script. Integer Bareiss elimination verifies the determinant signs; Fraction polynomial arithmetic separately verifies every reported error integral and coefficient bound. All checks agree.
- The all-q endpoint formula is proved by triangularization, not inferred from those finite checks. The orbit-continuity estimate is proved using the exact sawtooth L2 identity d(1-d). The continued-fraction criterion was rechecked with the fixed-target/subsequence quantifiers in that order. All supplied results are explicitly marked as proofs or computations supplied in this chapter, without a novelty assertion.
# Contraction-theory historical audit (12 November 2026)

The Szeged author catalogue led to the individual original papers, avoiding an
oversized issue PDF. Sz.-Nagy and Foias, VIII (1964), 38–71,
<https://acta.bibl.u-szeged.hu/14015/1/math_025_fasc_001_002_038-071.pdf>,
Theorem 1 (p. 50) gives the completely nonunitary contraction model, and
Theorem 3 (p. 58) states the characteristic-function equivalence criterion.
The receipt/revision dates printed on p. 71 are 23 April / 27 December 1963.
Theorem statements and model formulas were read, not merely metadata.

IX (1964), 283–316,
<https://acta.bibl.u-szeged.hu/14044/1/math_025_fasc_003_004_283-316.pdf>,
Theorem 3 and Remark (ii), p. 314, explicitly give the invariant-subspace
conclusion when neither sequence of powers tends strongly to zero; dimension
greater than one is specified. The receipt date is 1 May 1964. The general
model also appears as (3.16)–(3.17), p. 295.

The linked erratum was checked rather than ignored: *Corrections et compléments
aux Contractions IX* (1965), 193–196,
<https://acta.bibl.u-szeged.hu/14072/1/math_026_fasc_001_002_193-196.pdf>.
Its first page retracts Proposition 5.4 and explains that Theorem 3 and its
proof are unaffected. Thus the invariant-subspace result used here survives
the erratum. No reliance is placed on the retracted proposition or on the
unrestricted versions of the dependent spectral assertions.

## Integer-chain problem: a successful backward-reference search

Queries combined unicellularity, bilateral shifts, invariant-subspace lattices,
and integer order type. Shkarin's primary manuscript
<https://arxiv.org/pdf/1209.1458>, p. 3 and reference [7], led to Domar (1981),
*Translation invariant subspaces of weighted l^p and L^p spaces*, Math. Scand.
49, 133–144, DOI 10.7146/math.scand.a-11926. The publisher page and PDF opened;
the PDF had no extractable text, so it was downloaded and pages 133–135 were
rendered and visually read. Primary URL:
<https://journals.msp.org/mscand/article/download/1747/1746/1778>.

Theorem 2 gives an exact integer-tail lattice under specified logarithmic
convexity/concavity, summability, and quadratic growth conditions. Choosing
w_n = exp(-2 n |n|) satisfies all of them: on the negative half-line log w is
2n^2 and on the positive half-line it is -2n^2; the summability series is
2 sum_{n>=1} exp(-2n); the quadratic limits are 2 and -2, exceeding the
required log 3 thresholds in the appropriate directions. Conjugation from
weighted l^2(w) by c -> (w_n c_n) yields the ordinary Hilbert-space forward
shift S e_j = exp(-2|2j+1|) e_{j+1}. Its invariant subspaces are precisely the
coordinate tails plus zero and the whole space. Reindexing the tails by -n
gives the increasing integer chain in the source question.

This resolves the precise completed-order interpretation of 1964-50.17; it
is a B/exact identification, not an F lead or a manufactured open problem.
The paper was received 9 June 1980 and published in 1981. Its submission date
is not asserted to be the first public circulation. The chosen weight and
unitary-conjugation formula received a second independent check by the
spring-source reviewer. The reviewer read the original scanned hypotheses
and confirmed the decreasing weight, both curvature signs, summability,
quadratic limits, bounded shift, and exact tail-lattice correspondence.

## Independent finite-action check

For 1964-34.13, `finite_action_check.py` independently enumerates all 168
invertible three-by-three binary matrices. Both actions on seven nonzero
vectors/covectors are transitive. Their fixed-point characters agree for
every element (histogram: 48 zeros, 98 ones, 21 threes, one seven). The
24-element stabilizer of a vector fixes no nonzero covector. This confirms
equivalent complex permutation representations but inequivalent actions.
The independent conceptual check is equality of the ranks of g-I and its
transpose, together with the explicit upper-block form of a vector stabilizer.

## Final editorial and index checks

Root independently read the Russian of P000015 and viewed the scan. Its
closing support-of-measure assertion is distinct from the preceding
Radon-measure discussion and was omitted from the supplied baseline.
It is retained as the added occurrence 1964-6.9, under the explicitly stated
finite positive Hausdorff Radon convention. The compact-cover and inner
regularity argument was checked independently and uses regularity on all
Borel sets, not local compactness.

An independent reader reviewed all 83 original autumn occurrences; the
separately checked support assertion makes 84. The review found three
needed hypotheses: the proper orthochronous Lorentz component, invariance
of the punctured distribution under an origin-fixing action, and positivity
and finiteness of the canonical partition function. These were returned to
the source owner for correction. The overview/report also distinguish
expository class E from a fully audited theorem-level priority claim.

The independent problem-index review checked all 14 question-kind entries
without a problem link. It recommended adding the solved subnormal
invariant-subspace question in 1964-50.5, and documented why the other
13 entries do not specify distinct qualifying research questions. The
added entry is assigned its canonical number in first-occurrence order;
the reviewer’s provisional number is not a historical identifier.

The VIII/IX bibliography ownership mismatch was corrected by adding the
reopened primary IX record. Three duplicate bibliography records differ
only in formatting and access annotations; their author, year, title,
pages and result status agree. The shared invariant-subspace problem
received one merged statement and status through finalize_data.py.


The independent spring-item review covered all 73 occurrences. Its two
corrections, n>=2 in projection-brightness uniqueness and submission rather
than inferred public circulation for the polynomially-compact papers, are
applied in finalize_data.py. The independent winter-item review covered all
91 occurrences and supplied the positive-phase-volume hypothesis in 22.1
and valid projective/Stiefel index range in 30.7. These exact field changes
are preserved in editorial_changes.json. The saved review notes state the
scope of the checks and do not claim a fresh proof of every cited theorem.
