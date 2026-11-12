# Independent mathematical consistency review: winter records 15–35

Reviewer: spring researcher. Audit date: 12 November 2026.

## Scope and outcome

I read the notes, modern statement, reconstruction, fate, classification, literal-correctness, publication-match and verification fields of **all 91 entries** in `work/parts/winter/items.json`. This was a bounded mathematical consistency check of the supplied formulations, with emphasis on Fredholm theory, statistics, differential jets, K-theory and group actions. It was not a new literature search, a verification of every bibliography entry, or an independent proof audit of every cited theorem. No winter data or corrections were edited.

**No material theorem-level contradiction was found in the principal reconstructed results.** Two small explicit-hypothesis corrections are recommended below. Neither changes an item's class, source identification or substantive fate.

| Records | Entries read | Principal checks |
|---|---:|---|
| 15–21 | 24 | Fredholm perturbations and family index; retracted invariant-subspace announcement; immanant positivity; WKB transport and Maslov conventions; sufficiency versus similarity versus invariance; Bayes weighting; holomorphic division |
| 22–28 | 25 | Semiclassical counting; Sturm zero counts and determinant argument; congruence and triangle groups; spin-flavour tensor embedding and Poincaré block law; conormal jets and square-zero lifting; Peetre and elliptic-resolution hypotheses |
| 29–33 | 23 | Compact perturbations; sphere fields and block extension; KO degrees and projective-space torsion; Noetherian operators; essential self-adjointness versus strong commutation; pure-point and Lebesgue multiplicities; tensor spectral convolution |
| 34–35 | 19 | Type-I decomposition; compact homogeneous actions; Prüfer duality; affine-group representations; compact hyperbolic quotients; cocycle conventions; transitive cocycle classification; finite-action counterexample; multiplicative reconstruction; deliberately unidentified programme fragments |
| **Total** | **91** | |

Record 23 has no occurrence items in the supplied winter file; this is not an omitted item in the review.

## Recommended corrections

### 1964-22.1: require positive phase volume when using asymptotic equivalence

The modern statement uses

\[
N_h(E)\sim (2\pi h)^{-d}\operatorname{vol}\{(x,p):|p|^2/2+V(x)<E\}
\]

under a “compact regular sublevel” assumption. That assumption permits the empty sublevel: for example, take the smooth confining potential \(V(x)=|x|^2\) and \(E=-1\). The level is regular vacuously, its sublevel is empty and compact, and both counting function and displayed volume are zero. The conventional ratio definition of \(\sim\) is then undefined.

**Minimal repair:** add that the phase sublevel has positive volume, equivalently in this confining real-potential setting require \(E>\min V\), retaining the regular-value hypothesis. Alternatively write the Weyl law in the additive form

\[
N_h(E)=(2\pi h)^{-d}\operatorname{vol}\{H<E\}+o(h^{-d}),
\]

which does not require a nonzero leading coefficient. This is a boundary-case precision correction, not a defect in the intended positive-energy Weyl theorem. The supplied P000045 transcription was reread; its energy/index confusion is already separately represented by the item's literal-correctness field.

### 1964-30.7: state the parameter range for the projective/Stiefel quotient

The formula

\[
\mathbb{RP}^{n-1}/\mathbb{RP}^{n-k-2}
\longrightarrow O(n)/O(n-k-1)
\]

has no explicit range for \(n,k\). Its ordinary nonnegative-dimensional interpretation requires integers \(n\ge2\) and \(0\le k\le n-2\). The endpoint \(k=n-1\) can also be included if the text explicitly declares the empty-projective-space and zero-dimensional-orthogonal-group conventions. Larger \(k\) is not meaningful in the written notation.

**Minimal repair:** begin the modern statement with “For integers \(n\ge2\) and \(0\le k\le n-2\)”. The reflection map and its collapsed subspace are otherwise correct: the last \(k+1\) columns of \(I-2vv^t\) equal the standard frame precisely when the corresponding coordinates of \(v\) vanish. P000059 was reread to check the source quotient.

## Checks that did not produce corrections

- **Fredholm statements 15.1–15.4:** compact perturbation invariance, local constancy, the derivative index of a connected Fredholm map, and the stabilized family bundle are consistent in the stated Banach/Hilbert and norm-continuity settings. The family statement correctly retains information beyond the integer index.
- **Statistics 19.1–19.5:** the source's similar-test definition is correctly distinguished from group invariance; no universal Behrens–Fisher optimum is asserted. P000039–P000040 were reread. Their Bayesian “a priori distribution” language supplies the probability-measure interpretation of the alternative weighting.
- **Jets 26.1–26.4 and 31.1:** primary contraction from generic localization justifies the first-order conormal criterion when \(P^2\subset Q\). Characteristic zero supplies the required separability for extension of the conormal functionals. The square-zero correction has the necessary invertibility assumption. The formal exponential is not mistaken for an analytically convergent flow. The modern Noetherian-operator statement uses polynomial coefficients rather than an unrestricted constant-coefficient claim.
- **K-theory 30.4–30.6:** the KO degree shift, eight-periodic coefficient table, reduced/unreduced distinction and order \(2^{\phi(k)}\) are consistent. P000058 explicitly stabilizes by possibly different trivial ranks \(N_1,N_2\); thus the rank-forgetting sentence in 30.4 is correct in the source's convention. Equal-rank stabilization would be a different convention, not evidence of an error here.
- **Group examples 25.1–25.2:** the tensor product is injective on \(SU(2)\times SU(3)\), since the possible central kernel is the intersection of second and third roots of unity. The corrected Poincaré block matrix multiplies according to the displayed semidirect-product law.
- **Unbounded operators 32.1–32.5:** the pair of nonreal range tests, precise derivative domains, distinction between infinitesimal and strong commutation, and stronger Nelson-Laplacian criterion are maintained. There is no invalid inference from essential self-adjointness of all linear combinations to group integration.
- **Dynamics and cocycles 33.1–34.15:** constants are removed where required; absolute continuity is separated from equivalence of maximal spectral type; the full affine group is distinguished from its positive-dilation subgroup. The right-action cocycle identity agrees with the order of operator multiplication. The finite \(GL(3,\mathbb F_2)\) example has equal permutation characters and nonconjugate stabilizers. Multiplicative \(L^\infty\) structure, probability state and normality are retained in the reconstruction assertion.
- **Unidentified items:** their statements refrain from converting missing hypotheses or undefined objects into definite open problems. The September 2026 simple-Lebesgue-spectrum claim is explicitly separated from independently verified established results.

## Handoff

The two recommended hypothesis edits were sent to root. No live changes were made to `work/parts/winter/`. The review supports proceeding with assembly after those bounded corrections; it does not certify the complete proofs of external publications or establish the acceptance of recent claimed solutions.
