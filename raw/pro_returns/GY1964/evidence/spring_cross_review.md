# Independent consistency review: spring records 36–50

Reviewer: autumn-records research agent. Review date: **12 November 2026**.

## Scope and independence

I read all **73 items** in work/parts/spring/items.json and all **eight provisional problems** in work/parts/spring/problems.json. For each item I examined the notes, modern statement, reconstruction, fate, present status and assessment fields. The review focused on precise hypotheses and conclusions, particularly enveloping/Weyl algebras, circular-ensemble gaps, convex geometry, trace commutators, subnormal operators, Volterra operators and weighted shifts.

The final updated **1964-50.13** was included: trace-class imaginary part, canonical self-adjoint reducing component, the original Livšic theorem, and separation from the broader Hilbert–Schmidt survey claim. I did not edit the spring data.

This is a mathematical consistency review, not a repeated literature audit. I did not undertake new web searches or independently authenticate every bibliography entry. For the Bishop passage I consulted the English and Russian P000089 source files, and for the weighted-shift scope I checked the existing spring research log. I did not reread every manuscript scan.

The original extraction for records 36–43 had SHA-256:

    235dfe15e2a7fa2a3efa1b3e0533556ef341ff6fd16dad099d489b9fc51550ca

The final snapshot used for records 44–50, including updated 50.13, had SHA-256:

    02ba6638b29f8c23d73cadc2cce2c571e08aae8b387ecd13dcdacff89f873c7a

Spring's author confirmed that the late change concerned 50.13 and that the remaining data were final. Read-only extraction code and captured outputs are retained as spring_review_extract.py, spring_review_36_43.txt, spring_review_44_49.txt and spring_review_50.txt in work/evidence/.

## Concrete corrections

### 1. Item 1964-44.2: state the dimension restriction

The modern statement says the brightness function determines an origin-symmetric convex body in R^n but does not explicitly impose **n≥2**.

The omitted restriction matters. In R¹, both K=[−1,1] and L=[−2,2] are origin-symmetric convex bodies. For either unit direction, projection onto its orthogonal complement is the singleton {0}, with zero-dimensional volume one. The brightness functions therefore agree while K and L differ.

**Minimal correction:** change the opening to:

> For n≥2, the brightness function determines an origin-symmetric convex body K⊂R^n uniquely among such bodies.

The source's three-dimensional context and the preceding item's n≥2 hypothesis support this intended scope. This is a missing-hypothesis repair; no fate or class change is needed.

### 2. Item 1964-50.7: receipt does not establish public circulation

The fate gives receipt/revision dates for Bernstein–Robinson and Halmos, then concludes:

> Thus both arguments circulated before this May 1965 lecture although publication followed it.

The dates establish that the manuscripts had been submitted before the lecture. They do not by themselves establish an earlier date of **public circulation**. This is the same distinction already maintained elsewhere in the chapter for Dobrushin's announcement.

**Minimal correction:** replace that sentence by:

> Both manuscripts had been submitted before this May 1965 lecture; publication followed in 1966. The notebook itself records the oral report, while no separate earlier public-distribution date is established here.

If independent evidence of pre-lecture public distribution exists, it can instead be cited explicitly. The published theorem, attribution to Allen R. Bernstein, and class-A match do not require alteration.

## Findings in the requested high-risk areas

No further concrete mathematical error requiring correction was found in the reviewed statements.

- **Enveloping and Weyl algebras:** the finite-dimensional complex restriction makes the zero-ideal Dixmier–Moeglin criterion appropriate. The explicit translation/multiplication module for the two-dimensional nonabelian Lie algebra is simple and faithful. Growth dimension separates different Weyl ranks and is correctly distinguished from the fixed-rank endomorphism conjecture.
- **Circular ensembles and gaps:** the COE/CUE Vandermonde powers, logarithmic-energy sign, normalized gap integral and N=1 disproof of an exact cosine-power CUE formula are consistent. The even sine-kernel asymptotic is not silently identified with the notebook's uncertain scaling. The nearest-neighbor formula uses the Palm law and the intensity factor.
- **Convex geometry:** the even spherical-Radon inversion, central-symmetry qualification for brightness, and suitable Euclidean structure in Dvoretzky's theorem are properly separated. Only the n≥2 edge case above needs repair.
- **Trace identities:** the finite-interval logarithmic-derivative sign, relative-resolvent trace and whole-line free Wronskian normalization are consistent. The Neumann comparison formula vanishes for a constant potential as it should. The commutator entry correctly distinguishes trace class of both products from trace class of their difference; [S*,S] has rank-one trace one.
- **Subnormal operators:** the normal extension requires invariance, not merely compression. Finite-dimensional subnormality implies normality. The weights 1,1,2,2,… give a valid hyponormal/non-subnormal counterexample: the first three moment values force concentration at one, contradicting the next moment. Brown's solved special-class problem remains distinct from the unrestricted Hilbert-space problem.
- **Polynomial compactness:** the Hessenberg product, escaping-corner hypothesis, asymptotic projection membership and finite-spectrum zero factorization are consistent. The zero entire function is correctly excluded.
- **Lattices and shifts:** forward/backward orientation and endpoint spaces are handled correctly. The displayed bilateral shift weights agree algebraically with the ratio of Domar's weight sequence. The Volterra lattice has the correct reverse inclusion. The two-sided measure-Volterra counterexample yields incomparable invariant summands, so it defeats the literal linear-order conjecture.
- **Bishop operators:** the universal invariant-subspace question and existence of one cyclic vector are separated. No universal cyclicity theorem or new resolution is inferred from the partial results.
- **Final 50.13:** its restricted trace-class theorem is consistent with the stated canonical decomposition. The broader survey scope is explicitly qualified rather than attributed to the unread stronger original theorem.

## Problem-index consistency

The eight supplied problem statements agree with the scoped mathematical questions in their linked items. In particular, the weighted-shift classification entry explicitly describes a verification gap rather than declaring an unverified general problem open; the bilateral integer-chain example is labelled solved; and the Bishop invariant-subspace and cyclic-vector questions are distinct.

Root's separate problem-index review has already identified the Brown subnormal problem as an additional entry to create. I did not duplicate that action or modify the provisional problem IDs.

The two concrete corrections above were sent to root and the spring author. No source files were edited.
