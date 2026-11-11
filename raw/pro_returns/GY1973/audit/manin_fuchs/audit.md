# Research audit: Manin, operator/K-theory and Rudakov fragment

**Scope:** MCCME records 303–311, excluding the agenda in302 and every page from the new22 October heading onP525. **Status date:**9 November 2026.

## Coverage and provenance

The fragment has112 items in9 talk entries. Counts are A4, C2, E95, F11; B0, D0. Records303, 304, 305, 307, 306, 308, 309, 310, 311 contain respectively17, 12, 16, 3, 10, 13, 20, 9, 12 items. The ordering307before306 follows the scan; catalogue identifiers are unchanged. Record 309 includes8explicitly attributed Mishchenko interventions. Record 310 includes Kirillov's distinctP522intervention. No records are discarded because the inclusive catalogue range overlaps a neighboring talk.

Every item has the exact required schema, literal-correctness assessment, publication-match strength, verification level, dated status, references and confidence. The item index distinguishes a construction from its later theorem, avoids turning unformulated analogies into research problems, and preserves repeated exposition as separate historical occurrences. Broad areas are in area_map.json.

## Problems and Stage 2 decision

GP-1972-403 is reused only for ordinary p-adic interpolation of modular L-values, with the four exact prior occurrences and the current period/distribution/interpolation occurrences. The new identifiers GP-1973-10 and11 denote the ζ(3) and Euler-constant transcendence questions. The latter is an elliptical occurrence and therefore has medium historical-identification confidence. The dated search and the precise weaker arithmetic results are documented in search_log.md. Neither famous transcendence question admits a responsible bounded development from these notes; neither is claimed solved.

No class D is assigned. Eleven F entries are under-specified records or unresolved identifications, not evidence that a precise research question remains open. Particularly: the BDF pair nonclosure assertion has no checked exact ambient hypotheses or counterexample; the affine-group question has no identified operator; cross-prime integration and bounded representation remarks lack quantifiers; the regulator e5 lacks normalization; Kirillov's Diff classification lacks a representation category. The index does not manufacture missing problems.

## Mathematical-critical decisions

- Manin's sign measure is bounded for oddp. P503andP505 have opposite signs. The P505moment formula is independently reconstructed, including its total mass and Euler factor. It is not a transcription fix silently passed off as original text.
- The raw invariant-distribution integral depends on tags. This is compatible with separately defined fixed-tag integrals.
- Compact analytic manifold is the correct Russian reading of the P501abbreviation. Serre's theorem requires pure positive dimension; its invariant is a class moduloq−1.
- The finite-period module, two periods, Hecke recurrence and ordinary interpolation are identified in Manin1973. The source's ellipses are not used to claim an exact interpolation normalization match.
- Helton–Howe traces require bounded self-adjoint operators and a trace-class commutator. Their measure is purely imaginary in the unscaled trace convention; ordering independence concerns the trace.
- BDF means C*-extensions with the stated equivalence, not arbitrary Banach extensions. The even/odd degree and unreduced basepoint summand are separated. One-operator norm closure is verified; the pair claim remainsF.
- The source's false statement about faces of nondegenerate simplices is refuted by the nerve ofC2. Simplicial-space realization still has a topology, and products use compactly generated spaces.
- Mishchenko's exact Fredholm construction was publicly announced before this session. The general-ring exposition and the full symbol/K-homology correspondence are marked with their correct scope and verification limits. The tensor shorthand is replaced by compression, and the integer Fredholm component is restored.
- Rudakov's discrete topology, countable dimension, finite jet quotients and height hypotheses are explicit. A finite-dimensional quotient algebra does not imply a finite-dimensional module. The later Hamiltonian height-one theorem is separately dated1975.
- The Q-construction uses π(i+1), while the positive plus-construction groups use π(i). The exact comparison is to ΩBQ with the discreteK0 factor. Finite-rank automorphism maps to unloopedBQ are nullhomotopic, and addition of a free summand is naturally homotopic to the identity.

## Independent checks and code

critical_verifications.tex contains complete elementary proofs marked [proved here]: sign-measure compatibility and all polynomial moments, tag dependence, theC2 counterexample, and both Q natural-transformation checks. These are critical verification of source formulas, not Stage 2 solutions toC/D problems. The root agent independently rederived these arguments and confirmed their validity; its suggested wording refinement distinguishes absolute value1 on residue balls from at most1 on arbitrary clopens. The root also independently computed exact finite sums and p-adic valuation growth for p=3, 5, 7 in its independent_checks.py/output; these computations support checks but are not substituted for the proof.

The data builders, bibliography writer, validation script, acquisition scripts and this audit generator are preserved. validation_output.json records 112 items, 9 talks, 3 problems, 24 references, 32 corrections and zero errors. The supplied chapter builder ran successfully; its output is in build_output.txt. A plain local XeLaTeX call failed because the default environment lacked xelatex.fmt, before reading the TeX. The root has a tested workspace format/font configuration and explicitly assumed the integrated compile, so no local PDF success is claimed.

Full external copyrighted source volumes are temporary research inputs rather than deliverable content; the downloaded Douglas volume is not needed in the final package. Its public URL and reproduction script remain. No source-reading failure is called a theorem failure.

## Per-item evidence ledger

This ledger repeats the exact item-level authority/locator and qualification from the data, so every occurrence can be audited without guessing which generic reference supports it. “Read the result” means the theorem or construction was read, not that every cited long proof was independently rechecked. Bibliography annote fields distinguish full primary reading from metadata-only records and author retrospectives.

### Record 303: Yu. I. Manin — 1973-09-03

**1973-303.1 — Finding an integration theory for compact p-adic spaces** (P000501; class E; exact; read the result).

\citet[\S8.1 and Theorem~8.6]{manin1973periods}; the concrete answers, rather than an unspecified universal class, are the subject of this exposition.

Literal assessment: correct with missing hypotheses. Compactness, completeness and boundedness are explicit sufficient hypotheses supplied here; the notebook asks a programme-level question, not uniqueness of an optimal measure class.

**1973-303.2 — Adelic Mellin motivation with an unspecified quotient** (P000502; classF; thematic only; indirect).

\citet[Introduction and \S1]{manin1976nonarchimedean} supplies a developed adelic framework, but does not identify every missing symbol in this line.

Literal assessment: not determinable. 

**1973-303.3 — Bernoulli values of the classical zeta function** (P000502; class E; exact; read the result).

Classical formulas, restated in \citet[\S1 and \S5]{nica2024irrationality}.

Literal assessment: correct with missing hypotheses. The Bernoulli convention and omitted constants are supplied; divergent power sums are not ordinary convergent sums.

**1973-303.4 — Gelfand on divergent sums and spectral parity** (P000502; classF; thematic only; indirect).

The Bernoulli identity is classical; \citet[\S1 and \S5]{nica2024irrationality} does not settle the unformulated spectral comparison.

Literal assessment: not determinable. 

**1973-303.5 — Removing the Euler factor and interpolating zeta values** (P000502; class E; exact; read the result).

\citet[\S0.1--0.3]{manin1976nonarchimedean} restates the Kubota--Leopoldt construction (1964).

Literal assessment: correct with missing hypotheses. The sign, branch restriction and pole are indispensable editorial qualifications.

**1973-303.6 — The proposed cross-prime analytic analogy** (P000502; classF; none found; unresolved lead).

No exact problem was identified after reading the corresponding integration sections of \citet[\S8]{manin1973periods} and \citet[Introduction]{manin1976nonarchimedean}.

Literal assessment: not determinable. 

**1973-303.7 — Serre classification of compact non-Archimedean manifolds** (P000502; class E; exact; read the result).

\citet[Theorem~1 and corollary, p.~409]{serre1965 classification}; received March 1964, published 1965.

Literal assessment: correct with missing hypotheses. The English translation says analytic set, but the Russian abbreviation and scan say analytic manifold. Pure positive dimension and nonemptiness are stated explicitly here.

**1973-303.8 — Computing the Serre invariant by reduction** (P000503; class E; exact; read the result).

\citet[example (i), p.~410]{serre1965 classification}.

Literal assessment: correct with missing hypotheses. The integer number of residue discs is one representative of the invariant, not a canonical integer-valued invariant of the analytic manifold.

**1973-303.9 — The projective line as two analytic balls** (P000503; class E; exact; read the result).

An explicit instance of \citet[Theorem~1]{serre1965 classification}.

Literal assessment: false as written. Replace Qp by K and pA by the maximal ideal for ramified extensions; the omitted point at infinity is included in the inverse-coordinate chart.

**1973-303.10 — Compact Lie groups and supernatural order** (P000503; class E; exact; read the result).

\citet[example (ii), p.~410]{serre1965 classification} gives the compact-group application.

Literal assessment: false as written. The invariant is a residue class. The notebook\textquoteright s displayed modulus p in the SL2 example is incompatible with the preceding theorem.

**1973-303.11 — Distributions on clopen subsets** (P000503; class E; exact; read the result).

\citet[\S8.1]{manin1973periods}.

**1973-303.12 — The residue-class tree and compatibility equation** (P000503; class E; exact; read the result).

\citet[\S8.1, equation~(24)]{manin1973periods}.

**1973-303.13 — Invariant p-adic distribution is unbounded** (P000503; class E; exact; read the result).

\citet[\S8.4]{manin1973periods}; already occurrence 1972-298.2.

**1973-303.14 — The bounded two-valued distribution** (P000503-P000504; class E; exact; read the result).

\citet[\S8.4, regularized distributions]{manin1973periods}; this is a signed normalization of the c=2 construction.

Literal assessment: correct with missing hypotheses. Odd p excludes an unassigned midpoint and makes 2 a unit. P000505 uses the opposite overall sign.

**1973-303.15 — Integration by arbitrary tagged clopen partitions** (P000504; class E; exact; read the result).

\citet[\S8.5--8.6]{manin1973periods}.

Literal assessment: correct with missing hypotheses. Disjointness, shrinking mesh and tag independence make the limiting convention explicit.

**1973-303.16 — The linear function fails to integrate against the invariant distribution** (P000504; class E; exact; read the result).

This is the elementary obstruction discussed before \citet[Theorem~8.6]{manin1973periods}.

**1973-303.17 — Moderate growth suffices for Lipschitz integration** (P000504; class E; exact; read the result).

\citet[Theorem~8.6]{manin1973periods}.

Literal assessment: correct with missing hypotheses. The convergence is uniform over all residue balls; pointwise shrinking alone is not the stated sufficient uniform estimate.

### Record 304: Yu. I. Manin — 1973-09-10

**1973-304.1 — Repeated Lipschitz integration criterion** (P000505; class E; exact; read the result).

\citet[Theorem~8.6]{manin1973periods}.

Literal assessment: correct with missing hypotheses. Uniformity and the finite-chart interpretation are supplied as in item 1973-303.17.

**1973-304.2 — Moments of the sign distribution** (P000505; class E; partial; read the result).

The underlying regularized distribution is in \citet[\S8.4]{manin1973periods}; the exact normalization displayed here is independently reconstructed from the notebook definition.

Literal assessment: false as written. The Bernoulli convention is not defined on this page. The formula here follows from finite power sums, not by silently correcting B indices in the source; see the included exact-arithmetic check.

**1973-304.3 — Restriction to units produces the Euler factor** (P000505; class E; exact; read the result).

\citet[\S8.4--8.7]{manin1973periods}; notebook-specific exponents are checked directly.

Literal assessment: false as written. The level variable m is replaced by the moment exponent r only in the modern statement.

**1973-304.4 — Continuous character space and its disc coordinates** (P000506; class E; exact; read the result).

\citet[\S8.3]{manin1973periods}; occurrence 1972-299.4 already records the p=2 qualification.

Literal assessment: correct with missing hypotheses. Continuity, the Teichmuller lift, and the separate p=2 case are made explicit.

**1973-304.5 — Analyticity of the p-adic Mellin transform** (P000506; class E; exact; read the result).

\citet[Theorem~8.7]{manin1973periods}.

Literal assessment: correct with missing hypotheses. 

**1973-304.6 — Holomorphic cusp forms for the full modular group** (P000506; class E; exact; read the result).

\citet[\S1.1--1.2]{manin1973periods}.

**1973-304.7 — The discriminant form and low-weight dimensions** (P000506; class E; exact; read the result).

\citet[\S1.2 and the weight tables in \S7]{manin1973periods}.

Literal assessment: correct with missing hypotheses. The notebook shorthand must not be read as dimension one at every weight from 12 through26; weight24 is the first two-dimensional example.

**1973-304.8 — Hecke eigenbasis and algebraic Fourier coefficients** (P000506-P000507; class E; exact; read the result).

\citet[\S1.2 and \S3]{manin1973periods}.

Literal assessment: correct with missing hypotheses. Normalized eigenforms, not every arbitrary algebraic basis, give the Euler product. The obscured exponent is resolved by the next clear display on P000507.

**1973-304.9 — The prime Hecke operator and its coefficient recurrence** (P000507; class E; exact; read the result).

\citet[\S3, formula~(11)]{manin1973periods}.

**1973-304.10 — Rational-cusp period integrals** (P000507; class E; exact; read the result).

\citet[\S3.2 and Proposition~9.2]{manin1973periods}.

Literal assessment: correct with missing hypotheses. The unqualified phrase about irrational points is retained as a heuristic, not a theorem with universal quantifier.

**1973-304.11 — The period distribution relation** (P000507; class E; exact; read the result).

\citet[Proposition~9.2(d)]{manin1973periods}.

**1973-304.12 — The tentative correction of the period half-measure** (P000508; class E; partial; read the result).

\citet[Lemma~9.4 and formula~(39)]{manin1973periods}.

Literal assessment: false as written. Both the second exponent and the direction of the denominator shift are repaired, using the explicit corrected repetition on P000509, not merely the printed formula.

### Record 305: Yu. I. Manin — 1973-09-17

**1973-305.1 — The corrected quadratic-root distribution** (P000509; class E; exact; read the result).

\citet[Lemma~9.4 and formula~(39)]{manin1973periods}, up to the stated overall factor \(\rho\).

**1973-305.2 — Periods and critical L-values** (P000509; class E; exact; read the result).

\citet[\S1.1--1.2]{manin1973periods}.

**1973-305.3 — Continued fractions and integral modular-symbol reduction** (P000509; class E; exact; read the result).

\citet[Proposition~3.2 and Proposition~9.2(c)]{manin1973periods}.

Literal assessment: correct with missing hypotheses. The initial edge and its orientation repair the first sum\textquoteright s lower index 0, which otherwise invokes an undefined convergent -1.

**1973-305.4 — Parity and reality of periods** (P000509; class E; exact; read the result).

\citet[Proposition~9.2, proof]{manin1973periods}.

Literal assessment: correct with missing hypotheses. The real-coefficient hypothesis is necessary and appears on the following page.

**1973-305.5 — Algebraicity after two period normalizations** (P000510; class E; exact; read the result).

\citet[Theorem~1.2]{manin1973periods}; submitted in 1973 after the earlier-year seminar exposition.

Literal assessment: correct with missing hypotheses. Normalization, eigenform and nonzero-period hypotheses are explicit. The theorem does not prove that the common factors themselves are transcendental.

**1973-305.6 — Eichler-Shimura period relations** (P000510; class E; exact; read the result).

\citet[\S2, equations~(4)--(5)]{manin1973periods}.

**1973-305.7 — Odd period coordinates and the one-dimensional even excess** (P000510; class E; exact; read the result).

\citet[\S2, Proposition~2.3]{manin1973periods}.

Literal assessment: correct with missing hypotheses. The standard period-polynomial conventions and weight range are supplied; this assertion is not about arbitrary cohomology of all modular forms.

**1973-305.8 — Hecke operators on period coordinates** (P000510; class E; exact; read the result).

\citet[Proposition~3.2]{manin1973periods}.

Literal assessment: false as written. The minus sign in the analytic formula is a notebook error, contradicted by its own P000507 formula and Fourier recurrence.

**1973-305.9 — Ramanujan congruence modulo 691** (P000510; class E; exact; read the result).

\citet[\S1.3 and \S7]{manin1973periods} supplies a period-based proof of the older congruence.

**1973-305.10 — Algebraic normalized period measures** (P000511; class E; exact; read the result).

\citet[Proposition~9.2(c), \S9.3--9.5]{manin1973periods}.

Literal assessment: correct with missing hypotheses. The choice of complex parity convention, number-field embedding and completion is indispensable.

**1973-305.11 — The ordinary root gives a bounded measure** (P000511; class E; exact; read the result).

\citet[\S9.5]{manin1973periods}.

Literal assessment: correct with missing hypotheses. The root valuations and positive conclusion are exact. The assertion that every nonunit-root distribution must grow needs a noncancellation hypothesis.

**1973-305.12 — The unresolved relation between a_p and p** (P000511; classF; thematic only; indirect).

\citet[\S9.5]{manin1973periods} discusses growth, but does not supply missing quantifiers for this remark.

Literal assessment: not determinable. 

**1973-305.13 — Primitive-character interpolation of the critical value at one** (P000511; class E; partial; read the result).

\citet[Theorem~10.2, formula~(40)]{manin1973periods} supplies the complete normalization. The notes alone do not determine their dots.

Literal assessment: correct with missing hypotheses. No numerical prefactor is attributed to the notebook: its ellipses prevent a literal normalization match. Locally constant character sums exist even without a bounded measure.

**1973-305.14 — The Lichtenbaum regulator interpretation of zeta(3)** (P000511; classF; partial; read the result).

\citet[\S4]{lichtenbaum1972values} is the historical conjectural setting; \citet[\S6.4]{borel1977zeta} establishes the regulator comparison up to rational factors, with its normalization explicitly defined.

Literal assessment: not determinable. The weaker Borel comparison is identified separately. It is not claimed to verify the exact notebook coefficient 2, nor to solve all modern special-value conjectures.

**1973-305.15 — Transcendence of zeta(3)** (P000511; class C; exact; read the result).

Ap\'ery proved irrationality in 1978; \citet[\S1, p.~2; manuscript dated 26 October 2024]{nica2024irrationality} explicitly separates that theorem from the still-unknown transcendence question. A recent preprint, \citet[Theorem~1.6; v2 dated 15 October 2026]{lai2026linear}, reports linear independence of \(1,\zeta(3),\zeta(4)\). This is a strictly weaker arithmetic assertion and is not a proof of transcendence; its theorem statement and introduction, rather than the complete proof, were checked.

**1973-305.16 — The arithmetic nature of Euler's constant** (P000511; class C; partial; read the result).

\citet[Conjectures~1.0.1--1.0.2 and \S3]{lagarias2013euler} surveys the arithmetic problem; even irrationality remains unproved in the accepted results checked.

Literal assessment: correct with missing hypotheses. The antecedent of “also” is identified, but the weak notebook wording is preserved; no claim of a newly posed precise irrationality conjecture is made.

### Record 307: I. M. Gelfand — 1973-09-24

**1973-307.1 — Wallach factorization through the Poisson bracket** (P000512; class E; exact; read the result).

The algebraic form of Wallach\textquoteright s lemma is proved in \citet[\S4, algebraic preliminaries and Proposition~4.2]{heltonhowe1975traces}, extending the 1973 work. This is an exposition of the Helton--Howe programme, not a new theorem by the seminar speaker.

Literal assessment: correct with missing hypotheses. The polynomial ring and characteristic zero are fixed explicitly. The two-variable conclusion cannot be read as a theorem with an unspecified Poisson structure in an arbitrary number of variables.

**1973-307.2 — The Helton--Howe trace measure** (P000512; class E; exact; read the result).

\citet[main theorem, formula~\((1^{\prime})\)]{heltonhowe1973integral}, presented at Halifax in April 1973 and printed in October. The ordering assertion is checked in \citet[Theorem~I and preceding paragraph]{heltonhowe1975traces}. The exact measure normalization is restated in \citet[Theorem~3.3]{sugahara2026heltonhowe}; its newer Toeplitz applications are not needed for the 1973 assertion.

Literal assessment: correct with missing hypotheses. Bounded operators and a complex measure remove domain and missing-factor ambiguities. Nuclear here means trace class.

**1973-307.3 — Normed rings in a proposed p-adic operator theory** (P000512; classF; thematic only; unresolved lead).

The operator-algebra context is documented by \citet[Introduction]{heltonhowe1975traces}; comparison with \citet[Introduction]{manin1976nonarchimedean} does not identify a precise common construction.

Literal assessment: not determinable. 

### Record 306: A. A. Kirillov — 1973-09-24

**1973-306.1 — C*-extensions by the compact operators** (P000512; class E; exact; read the result).

\citet{browndouglasfillmore1973unitary}; the definitions and chronology are checked in the authors\textquoteright s retrospective \citet[pp.~699--701]{douglas1980extensions}.

Literal assessment: correct with missing hypotheses. C*-structure, metrizability, essentiality and stable equivalence replace the misleading unrestricted Banach-algebra wording.

**1973-306.2 — Busby maps, splitting and addition** (P000512; class E; exact; read the result).

\citet[p.~700]{douglas1980extensions} gives precisely these equivalent constructions and attributes the commutative case to the 1973 work.

Literal assessment: correct with missing hypotheses. 

**1973-306.3 — Suspensions and the homological interpretation** (P000512; class E; exact; read the result).

\citet[p.~702]{douglas1980extensions} distinguishes the two degrees and the solution of Atiyah\textquoteright s problem; the full treatment is \citet{browndouglasfillmore1977extensions}.

Literal assessment: correct with missing hypotheses. Reduced suspensions, the even/odd degree distinction, and the cycle quotient are supplied. The result was announced in the BDF programme before this exposition; the 1977 proof date is not its first circulation.

**1973-306.4 — Exact sequence for a closed subcomplex** (P000513; class E; exact; read the result).

The generalized homology theorem in \citet[p.~702]{douglas1980extensions} supplies the exactness framework; \citet{browndouglasfillmore1977extensions} is the full original treatment.

Literal assessment: correct with missing hypotheses. The finite CW-pair scope avoids treating an arbitrary inclusion as a cofiber sequence without qualifications.

**1973-306.5 — The family index pairing** (P000513; class E; partial; indirect).

The scalar pairing and the K-homology identification are checked in \citet[pp.~702--703]{douglas1980extensions}; the family refinement is a reconstruction of the explicit notebook formula, not a separately located theorem in the accessible 1973 text.

Literal assessment: correct with missing hypotheses. Finite complexes, stabilized representatives and norm-continuous local lifts are needed for the family index; the compressed first line in the notebook does not fix degrees.

**1973-306.6 — The garbled relation between Ext and degree-zero K-homology** (P000513; class E; partial; read the result).

\citet[p.~702]{douglas1980extensions} explicitly identifies \(E_0(X)\) with \(K_0(X)\).

Literal assessment: false as written. This is a degree correction, not a proposed decipherment of the overwritten operation. The added summand is the unreduced basepoint summand.

**1973-306.7 — The affine-group extension and two indices** (P000513; classF; thematic only; unresolved lead).

The planar index classification in \citet[pp.~701--702]{douglas1980extensions} explains the graph interpretation. It does not identify this particular affine-group extension. The scan confirms an infinity-shaped symbol, not a written definition of the space.

Literal assessment: not determinable. The figure-eight interpretation is conditional. It is not substituted for the source symbol as an established transcription correction.

**1973-306.8 — Extensions of the circle are classified by the index** (P000513; class E; exact; read the result).

\citet[pp.~701--702]{douglas1980extensions}; compare the equivalent normal-operator classification in \citet[Theorem~1.1 and following paragraph]{friisrordam2001approximation}.

Literal assessment: correct with missing hypotheses. The missing second unitary relation follows from the *-homomorphism. The single displayed relation alone would allow a coisometry with infinite-dimensional kernel, which is not Fredholm.

**1973-306.9 — Normal operators plus compact operators form a closed set** (P000513; class E; exact; read the result).

The 1973 BDF result is reproved in \citet[Theorem~1.1 and \S2, proof of Theorem~1.1]{friisrordam2001approximation}; the primary article identifies BDF Corollary~11.2 as the original source.

**1973-306.10 — The asserted failure of closure for pairs** (P000513; classF; none found; unresolved lead).

Exact-phrase and BDF-title searches, the available 1973 metadata, \citet[pp.~699--704]{douglas1980extensions}, and \citet[\S2]{friisrordam2001approximation} did not locate the asserted pair counterexample. Neither the one-variable theorem nor general Ext theory alone verifies it.

Literal assessment: not determinable. 

### Record 308: D. B. Fuchs — 1973-09-24

**1973-308.1 — Simplicial objects and the simplex category** (P000513-P000514; class E; exact; read the result).

\citet[\S1, p.~105]{segal1968classifying}; \citet[\S1]{quillen1973higher}.

**1973-308.2 — The face and degeneracy presentation** (P000514; class E; exact; read the result).

This expands the functorial definition in \citet[\S1]{segal1968classifying}; no additional result is attributed to the speaker.

**1973-308.3 — The singular simplicial set** (P000514; class E; exact; read the result).

The construction is an instance of \citet[\S1]{segal1968classifying}; the distinction between sets and spaces is explicit there.

**1973-308.4 — Geometric realization and its CW cells** (P000515; class E; exact; read the result).

\citet[\S1, p.~105]{segal1968classifying}; \citet[\S1, realization preliminaries]{quillen1973higher}.

Literal assessment: correct with missing hypotheses. The all-simplices quotient avoids the notebook\textquoteright s incorrect assumption that every face of a nondegenerate simplex stays nondegenerate.

**1973-308.5 — Faces of nondegenerate simplices can be degenerate** (P000515; class E; partial; read the result).

The nerve and its degeneracies are defined in \citet[\S2--3]{segal1968classifying}. \ours\ The counterexample uses these definitions directly and was independently checked against the face and degeneracy formulas.

Literal assessment: false as written. The counterexample is editorial; the erroneous sentence is visibly in the scan and is not blamed on the transcription.

**1973-308.6 — Realizing a simplicial space retains a topology** (P000515; class E; exact; read the result).

\citet[\S1, p.~106]{segal1968classifying} explicitly defines realization of simplicial spaces.

Literal assessment: false as written. Replacing ``topological structure by ``the preceding cell structure is a mathematical emendation, not a reading supplied by the manuscript.

**1973-308.7 — The singular realization comparison** (P000515; class E; exact; indirect).

This is the standard realization--singular comparison underlying the classifying-space constructions in \citet[Chapter~IV, \S3]{weibel2013kbook}.

Literal assessment: correct with missing hypotheses. ``Good is replaced by the explicit CW-type condition. No homotopy-equivalence assertion is made for arbitrary spaces.

**1973-308.8 — An ordered simplicial model of a polyhedron** (P000515; class E; exact; read the result).

\citet[\S4, p.~108]{segal1968classifying} stresses the need to order vertices and the natural ordering of barycentric subdivision.

Literal assessment: correct with missing hypotheses. The vertex-preserving and order-preserving restrictions are supplied.

**1973-308.9 — Realization of products and the topology convention** (P000515; class E; exact; read the result).

\citet[\S1, p.~106]{segal1968classifying} and \citet[\S1, realization preliminaries]{quillen1973higher} state the k-space qualification.

Literal assessment: correct with missing hypotheses. The notebook does not specify the category of spaces.

**1973-308.10 — The simplicial interval** (P000515; class E; exact; read the result).

The interval-category construction in \citet[Proposition~2.1]{segal1968classifying} is exactly this model.

**1973-308.11 — The nerve and classifying space of a small category** (P000516; class E; exact; read the result).

\citet[\S2]{segal1968classifying}; \citet[\S1]{quillen1973higher}.

**1973-308.12 — Groups as one-object categories and the C2 example** (P000516; class E; exact; read the result).

\citet[\S3]{segal1968classifying}.

**1973-308.13 — The first definition of the Q-construction and higher K-groups** (P000513; P000516; class E; exact; read the result).

\citet[\S2, pp.~99--103]{quillen1973higher}. The manuscript was prepared in early 1973; this is an exposition of it.

Literal assessment: correct with missing hypotheses. Admissibility, middle-object isomorphism and the basepoint are made explicit; record 311 gives the detailed occurrence.

### Record 309: D. B. Fuchs — 1973-10-08

**1973-309.1 — The product of two simplicial intervals** (P000517; class E; exact; read the result).

This directly instantiates the product-realization construction of \citet[\S1]{segal1968classifying}.

**1973-309.2 — The nerve revisited** (P000517; class E; exact; read the result).

\citet[\S2]{segal1968classifying}; compare the correction in item 1973-308.5.

**1973-309.3 — Barycentric subdivision as a nerve** (P000517; class E; exact; read the result).

\citet[\S4, p.~108]{segal1968classifying}.

**1973-309.4 — Natural transformations induce homotopies** (P000517-P000518; class E; exact; read the result).

\citet[Proposition~2.1 and following remark]{segal1968classifying}; \citet[\S1, Proposition~2]{quillen1973higher}.

Literal assessment: correct with missing hypotheses. The category \(\{0\to1\}\) is distinguished from its realized interval.

**1973-309.5 — Initial and terminal objects give contractions** (P000518; class E; exact; read the result).

\citet[\S1, Corollary~2 to Proposition~2]{quillen1973higher}.

**1973-309.6 — Adjoints give homotopy equivalences** (P000518; class E; exact; read the result).

\citet[\S1, Corollary~1 to Proposition~2]{quillen1973higher}.

**1973-309.7 — Opposite categories have the same classifying space** (P000518; class E; exact; read the result).

\citet[\S1, opposite-category construction]{quillen1973higher}.

**1973-309.8 — The homotopy sequence of a fibration** (P000518; class E; exact; read the result).

This is the standard homotopy-fiber convention used by \citet[\S1, Theorem~B]{quillen1973higher}.

Literal assessment: correct with missing hypotheses. Basepoints and the low-degree qualification are supplied.

**1973-309.9 — Mapping paths replace an arbitrary map by a fibration** (P000518; class E; exact; read the result).

The construction fixes the homotopy-fiber meaning in \citet[\S1, Theorem~B]{quillen1973higher}.

Literal assessment: correct with missing hypotheses. The path-space topology is stated explicitly.

**1973-309.10 — The comma-category map to the homotopy fiber** (P000518-P000519; class E; exact; read the result).

\citet[\S1, pp.~93--97]{quillen1973higher}.

**1973-309.11 — Quillen Theorem B** (P000518-P000519; class E; exact; read the result).

\citet[Theorem~B, p.~97]{quillen1973higher}.

**1973-309.12 — A proposed limit over comma categories** (P000519; classF; thematic only; unresolved lead).

Comparison with \citet[\S1, Theorem~B and its proof]{quillen1973higher} does not identify an additional theorem with these quantifiers.

Literal assessment: not determinable. 

**1973-309.13 — Fredholm representations of a ring with involution** (P000519; class E; exact; read the result).

\citet[Definition~1.1]{mishchenko1974infinite}; the paper was submitted December 1972 and its central construction was announced in 1973. The notebook generalizes the definition from group rings to *-rings. The public pre-talk announcement is \citet[\S\S1--3, p.~239]{mishchenko1973infinite}, published in the March--April 1973 issue and received 10 October 1972.

Literal assessment: correct with missing hypotheses. Boundedness, complex Hilbert spaces and preservation of involution are explicit.

**1973-309.14 — Twisting a Fredholm cycle by a vector bundle** (P000519-P000520; class E; exact; read the result).

The Fredholm-cycle pairing is recalled in \citet[p.~702]{douglas1980extensions}; the family-index formalism is in \citet[\S2]{atiyahsinger1971families}.

Literal assessment: correct with missing hypotheses. Projection compression makes the shorthand tensor construction precise and avoids treating a compactly intertwining operator as an exact module homomorphism.

**1973-309.15 — Integer-valued pairings lose torsion information** (P000520; class E; exact; read the result).

The distinction between Fredholm cycles and their integer pairing is explicit in \citet[p.~702]{douglas1980extensions}.

Literal assessment: correct with missing hypotheses. The initial identification is not retained as a definition of K-homology; it is qualified by the notebook itself.

**1973-309.16 — Families refine the numerical index** (P000520; class E; exact; read the result).

\citet[\S2, family-index construction]{atiyahsinger1971families}; \citet[p.~702]{douglas1980extensions} gives the cycle interpretation.

Literal assessment: correct with missing hypotheses. Compact parameter spaces and the index-bundle construction are supplied. A full characterization of all natural transformations is not asserted.

**1973-309.17 — Elliptic symbols and analytic K-homology** (P000520; class E; partial; indirect).

The symbol and family-index conventions are checked in \citet[Introduction and \S2]{atiyahsinger1971families}; the Fredholm-cycle framework is in \citet[p.~702]{douglas1980extensions}. The full duality identification is used here as the modern formulation of the notebook\textquoteright s Poincare-duality shorthand.

Literal assessment: correct with missing hypotheses. Compact supports, a closed manifold and bounded normalization are essential; the statement is not ordinary untwisted K-cohomological Poincare duality on an arbitrary manifold.

**1973-309.18 — The K-class of a Fredholm representation of a discrete group** (P000519-P000520; class E; exact; read the result).

\citet[\S2, Lemma~2.1 and pp.~86--87]{mishchenko1974infinite}. The construction itself works beyond the finitely presented groups emphasized in that paper; the 1973 announcement predates this intervention. The public pre-talk announcement is \citet[\S\S1--3, p.~239]{mishchenko1973infinite}, published in the March--April 1973 issue and received 10 October 1972.

Literal assessment: correct with missing hypotheses. For an infinite CW complex the K-group is representable K-theory. The stability of the Fredholm set under compact perturbations justifies each interpolation.

**1973-309.19 — The Fredholm space has one component for each index** (P000520; class E; exact; read the result).

The family-index description in \citet[Introduction and \S2]{atiyahsinger1971families} and the Fredholm-family use in \citet[\S2]{mishchenko1974infinite} require the index components.

Literal assessment: false as written. The missing integer component is an emendation. A general F in the notebook is not assumed to have index zero.

**1973-309.20 — Generalized signatures of Hermitian forms** (P000519; class E; exact; read the result).

\citet[\S3, Definition~3.4 and Theorem~3.5]{mishchenko1974infinite} supplies the construction and its group-ring invariance. The public pre-talk announcement is \citet[\S\S1--3, p.~239]{mishchenko1973infinite}, published in the March--April 1973 issue and received 10 October 1972.

Literal assessment: correct with missing hypotheses. The notebook gives no formula; the positive/negative spectral-compression formula is supplied from the paper. No analogous Wall-group descent for every unspecified *-ring is inferred.

### Record 310: A. N. Rudakov — 1973-10-15

**1973-310.1 — The formal vector-field algebra and its filtration** (P000521; class E; exact; read the result).

\citet[\S1, pp.~836--838]{rudakov1974irreducible}.

Literal assessment: correct with missing hypotheses. Characteristic zero and the meaning of degree for formal power series are supplied.

**1973-310.2 — Continuity into a discrete countable-dimensional module** (P000521; class E; exact; read the result).

\citet[Lemma~2.1, p.~839]{rudakov1974irreducible}.

Literal assessment: false as written. Automorphisms is the wrong target for a Lie-algebra action: even the zero Lie element acts by the zero endomorphism, not an invertible map. The neighborhood quantifier means every v in V.

**1973-310.3 — Inflation from a finite jet quotient followed by induction** (P000521; class E; exact; read the result).

\citet[Definitions~2.2--2.3 and following observation, pp.~839--840]{rudakov1974irreducible}.

Literal assessment: correct with missing hypotheses. The abstract M in the opening programme is specialized to the open filtered subalgebra used in the theorem. No finite-dimensional-module hypothesis is added.

**1973-310.4 — Minimal height and the kernel submodule** (P000521; class A; exact; read the result).

\citet[Definition~3.1, Proposition~3.2 and Corollary~3.3, p.~840]{rudakov1974irreducible}.

Literal assessment: false as written. The printed paper explicitly adjoins zero; the notebook set omits it. The short argument here is a critical verification of the definition, not a new classification result.

**1973-310.5 — Irreducibility and reconstruction above height one** (P000521; class A; exact; read the result).

\citet[Theorem~6.1 and Corollaries~6.2--6.3, pp.~843--844]{rudakov1974irreducible}; the manuscript was received six days before this talk and appeared in 1974.

Literal assessment: correct with missing hypotheses. The primary paper resolves the provisional bound as 1. Continuity, irreducibility, topology and filtration are inherited from the preceding definitions; the assertion is not about all abstract Wn-modules.

**1973-310.6 — The differential-form exceptions for W_n** (P000521; class A; exact; read the result).

\citet[Definition~13.6, Theorem~13.7 and Corollaries~13.8--13.9, pp.~865--866]{rudakov1974irreducible}.

Literal assessment: correct with missing hypotheses. The exact height-one statement is given instead of extending the shorthand to all unrestricted module categories. The dual is the continuous dual of the linearly compact formal-form space, hence discrete; the trivial representation is separately understood. Closed positive-degree formal forms are exact in characteristic zero.

**1973-310.7 — The corresponding Hamiltonian result** (P000521; class A; partial; read the result).

\citet[\S1 and Theorem~6.1, Corollaries~6.2--6.3]{rudakov1974irreducible} explicitly includes H alongside W, S and K. The subsequent height-one classification for Hamiltonian algebras is \citet[Definition~5.5, Corollary~5.9 and Theorem~5.10, pp.~477--480]{rudakov1975types}, over an algebraically closed field of characteristic zero; received 7 October 1974 and published in 1975. This supplies later fate, without attributing that complete exceptional list to the one-line 1973 remark.

Literal assessment: correct with missing hypotheses. Only the precise high-height assertion supported by the paper is identified. The Wn exceptional list is not transferred to the Hamiltonian algebra.

**1973-310.8 — The parenthetical bounded-representation question** (P000521; classF; thematic only; unresolved lead).

\citet[\S\S2--3]{rudakov1974irreducible} defines continuity and height but does not determine the missing predicate of this parenthetical question.

Literal assessment: not determinable. 

**1973-310.9 — Kirillov on finite-functional-dimension diffeomorphism representations** (P000522; classF; thematic only; read the result).

\citet[\S1.1, pp.~5--7]{vershikgelfandgraev1975diffeomorphisms} gives relevant examples of finite functional dimension and cites Kirillov\textquoteright s 1974 preprint. This is a thematic match, not a proof of the unqualified classification sentence.

Literal assessment: not determinable. 

### Record 311: D. B. Fuchs — 1973-10-15

**1973-311.1 — The dual comma category and homotopy fibres** (P000522; class E; exact; read the result).

\citet[Theorem~B and its dual, p.~97]{quillen1973higher}.

Literal assessment: correct with missing hypotheses. Theorem B\textquoteright s arrow-invariance hypothesis remains necessary; a comma category is not automatically a homotopy fibre for every functor.

**1973-311.2 — Quillen Theorem A** (P000522; class E; exact; read the result).

\citet[Theorem~A, p.~93]{quillen1973higher}.

**1973-311.3 — An exact category inside an abelian category** (P000522; class E; exact; read the result).

\citet[\S2, pp.~99--100]{quillen1973higher}.

Literal assessment: correct with missing hypotheses. Additivity and the requirement that every term belong to M are stated explicitly. Not every ambient monomorphism between objects of M is admissible.

**1973-311.4 — Admissible epimorphisms survive pullback** (P000522; class E; exact; read the result).

\citet[\S2, exact-category axiom (b), pp.~99--100]{quillen1973higher}.

**1973-311.5 — Morphisms in Q are admissible subquotient spans** (P000523; class E; exact; read the result).

\citet[\S2, definition of Q, p.~101]{quillen1973higher}.

**1973-311.6 — Composition of Q spans by fibre product** (P000523; class E; exact; read the result).

\citet[\S2, definition of composition in Q, p.~101]{quillen1973higher}.

**1973-311.7 — Higher K groups as shifted homotopy groups of BQ** (P000523; class E; exact; read the result).

\citet[\S2, definition and Theorem~1, pp.~101--103]{quillen1973higher}.

Literal assessment: correct with missing hypotheses. Essential smallness justifies the classifying-space construction; zero objects give equivalent choices of basepoint.

**1973-311.8 — The exact category of finitely generated projective modules** (P000523; class E; exact; read the result).

\citet[Introduction and \S2]{quillen1973higher}.

Literal assessment: correct with missing hypotheses. The identity convention on rings and modules is explicit. All these short exact sequences split, but their span category and K groups are still nontrivial.

**1973-311.9 — The plus construction and its corrected degree** (P000523; class E; exact; read the result).

\citet[Introduction, pp.~85--86]{quillen1973higher}; precise conventions in \citet[Definition~IV.1.1 and IV.1.1.1]{weibel2013kbook}.

Literal assessment: false as written. The source transcription intentionally preserves i+1. That index is correct for BQ and incorrect for BGL-plus. The map and H-space requirements alone do not specify the plus construction without its perfect subgroup.

**1973-311.10 — The plus/Q comparison needs a loop space** (P000523; class E; exact; read the result).

Announced in \citet[Introduction, p.~86]{quillen1973higher}; a full proof and exact statement are in \citet[Theorem~IV.7.1 and Corollary~IV.7.2]{weibel2013kbook}.

Literal assessment: false as written. The notebook itself retracts the unlooped equality. Both the loop and the discrete K0 factor matter; a mere map to BQ is insufficient to establish the comparison.

**1973-311.11 — Finite-rank automorphisms give nullhomotopic maps to BQ** (P000523-P000524; class E; exact; read the result).

Functoriality of nerves and the natural-transformation homotopy are \citet[\S1, Proposition~2]{quillen1973higher}. The specific nullhomotopy is our direct check of the notebook construction, not a quoted plus/Q comparison theorem.

**1973-311.12 — Adding a free summand is homotopic to the identity on BQ** (P000524; class E; exact; read the result).

\citet[\S1, Proposition~2]{quillen1973higher} supplies the homotopy mechanism. The direct check below establishes the exact stabilization sentence; the separate comparison theorem remains \citet[Corollary~IV.7.2]{weibel2013kbook}.

