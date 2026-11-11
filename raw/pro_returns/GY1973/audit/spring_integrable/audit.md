# Spring fragment audit

**Final research/data handoff: 9 November 2026.** Owner: /root/spring_integrable. All writes are confined to work/fragments/spring_integrable/.

## Scope and inventory

The fragment contains ten separate archive entries, records 324–333, in physical source order. Record 324 is a calendar divider with no mathematical occurrences. Records 331 and 332 are source-recovered supplementary entries: the official archive assigns these identities but dates them 25 March 1975, while P000551 clearly says 25/III-74 between the 18 March and 1 April 1974 sessions. The corrected date is 1974-03-25. Every occurrence ID uses the academic-year prefix 1973.

| Record | Items | Principal coverage |
|---|---:|---|
|324|0|Calendar divider; overlapping folio range is not a second lecture|
|325|2|Finite/algebraic GL; the English Green-polynomial heading, with no recoverable theorem|
|326|22|Lax operators; Floquet bands and monodromy; inverse data; stationary finite-gap systems; density; Riccati integrals|
|327|21|Volterra dressing; compatible operators; KP/KdV and matrix reductions; nonlinear-wave examples; incomplete general assertions|
|328|6|Slow variables; oscillator and turning-point quadrature; averaged variation; unexplained constant action|
|329|13|Wavefront sets; conormals; kernel action/composition; multiplication; phase/symbol hypotheses; cutoff oscillatory integrals|
|330|11|Solitons; damaged collision bound; shifts; Bargmann/interpolation construction; Wronskian; cubic time; Miura map|
|331|4|Current/diffeomorphism representation program; bundle automorphisms; Fock space and normalization|
|332|1|Whitham–KdV title only|
|333|20|Heat invariants; curvature; attribution gaps; traces; spectral gaps; circle/two-torus multiplicity; propagation|

Totals: **100 items: A14, B3, C0, D0, E67, F16; five problems; 29 references; 32 corrections.** The area map covers every item.

## Decisive matches and chronology

Novikov 1974, received 18 February 1974, matches the stationary finite-gap and matrix-evolution material. Receipt precedes the 25 February session, while publication follows it. Zakharov–Shabat 1974, received 14 March, matches the 4 March dressing presentation. The latter source heading faithfully reads 1973; the official chronology establishes 1974.

Finite-gap density, GP-1973-52, is solved. Grébert–Kappeler–Pöschel 2004 Theorem 1.2 and its §5 proof were read in the author-hosted PDF. Their first-proof credit is Marchenko–Ostrovskii 1975, distinguished from the later proof actually inspected. Dubrovin–Matveev–Novikov 1976 Chapter 2 §3, Russian pp.84–87, was also read: the sheet-labelled gap divisor, trace formula, divisor evolution and stationary converse justify the finite-gap statements. The inverse problem item remains only a partial match to the source's unrestricted periodic wording.

Shabat 2014 explicitly cites the 1974 Gelfand seminar on Russian p.305. Theorem 1 is a precise nondegenerate interpolation theorem. Its forty-year lag does not fit class A. The stronger unrestricted scalar assertion in the notebook remains F because the ordinary Schrödinger reduction and regularity assumptions are missing; the later verified construction is stated separately.

**Shnirelman 1975, received 7 May 1974, exactly matches item 1973-333.16.** Both Russian pages, the all-indices theorem and Lemmas 1–3, were read. The spectral parameter belongs to the positive square root of the Laplacian. The author explicitly distinguishes his all-indices theorem from Lazutkin's positive-density subsequence result. This supersedes the provisional F assessment in early progress notes. Final classification is B: a parenthetical attribution to others does not itself establish a separate speaker intervention.

## Source and reconstruction controls

English and Russian source were read over P000537–P000553, and these scans were inspected at formulas/ambiguities. Critical corrections distinguish faithful notebook errors from paleographic uncertainty and archive provenance.

Substantive emendations include the Floquet normalization/conjugation, constant-potential threshold, free spectral parameter, traceless-matrix determinant sign, kernel commutator signs, KP coefficients, fast-phase cancellation of epsilon squared, Whitham's publication year, input-covector sign in kernel relations, and soliton coefficient 6. Composition order itself is not an error: the source defines an input-first convention.

The final Hörmander distributional kernel-map locator is Theorem 2.5.14, pp.130–131; the extension discussion precedes it. Multiplication is sequentially continuous in the original pseudotopology. It is not presented as unqualified joint continuity for every locally convex topology.

P550's interpolation node-count sign and empty auxiliary operator remain unfilled. The Wronskian identity requires a compatible exponential assignment and leading coefficient. A modern theorem does not decide obscured handwriting.

General bundle automorphisms have gauge group Γ(AdE) and base subgroup preserving the bundle isomorphism class. The ordinary current group and whole diffeomorphism group require the trivial-bundle setting. Fock factorial conventions are stated explicitly.

Heat and wave parameters are separated. The off-diagonal heat expansion needs its Gaussian. Cauchy smoothing has dimension-dependent convergence; switching from eigenvalues to frequencies materially changes the threshold. Global propagation is described in cotangent phase space. A returning geodesic must also return its covector to contribute to the stationary trace relation, and cancellation can prevent equality of all closed lengths with the singular support.

Independent sibling review identified two additional qualifications, now incorporated: real rescalings with real beta yield only one KP relative sign; the other real form needs imaginary beta with a compatible reality reduction. For U(t)=exp(+it sqrt(L)), the output-first primed relation follows negative-time geodesic flow G^(−t), as the Euclidean phase (x−y)·xi+t|xi| confirms.

Added hypotheses and normalized formulas are marked as reconstructions. Verification labels distinguish full-result reading, metadata checking, and indirect or unresolved leads.

## Problems and non-problems

IDs used: GP-1973-50 (Hill-band monotonicity), 51 (supplementary inverse data), 52 (finite-gap density), 53 (hierarchy/dressing construction), 54 (collision shifts). Reserved IDs 55–69 are unused. Earlier index entries are conceptual continuations where appropriate, without reusing a problem ID for mere thematic overlap.

No defensible C/D item remains in this fragment. The universal Hamiltonian slogan lacks a functional setting. The collision inequality has damaged indexing. Koblenz's independent fourth-coefficient attribution is unverified. The circle/zeta-zero analogy, generic-versus-universal gap phrase, and tentative three-torus comparison lack a definite recovered statement. Their F status denotes identification/scope gaps, not mathematical openness. The universal adjacent-gap reading is already false on a circle.

Record 332's archive speaker is B. M. Gurevich; the A. V. Gurevich–Pitaevskii paper is thematic only. Record 325 has no recorded Green-polynomial identity. Famous results are not substituted for missing lecture content.

## Reproducibility and checks

The generator make_fragment.py saves record-by-record data and final evidence refinements. make_references.py reuses cumulative keys and records current-run access in annotations. requirements.txt pins SymPy 1.14.0.

Seven symbolic/elementary checks passed in verify_emendations.py:

1. Lax commutator by formal composition and direct action on a generic function.
2. KP commutator, compatibility equations, and elimination.
3. Soliton residual: coefficient 6 is zero; coefficient 1 is nonzero, including a rational parameter sample.
4. Traceless 2×2 characteristic polynomial.
5. Miura residual factorization.
6. Circle doublets.
7. Fast-phase chain-rule scaling.

These are critical-emendation checks, not new research or Stage 2 C/D contributions. Outputs: output/emendation_checks.json and .txt.

check_fragment.py verifies roster, sequential IDs, references, declared citations, problem links, control characters, math delimiters, and area coverage. It passes with no errors; output/data_check.json records counts. The supplied build_chapter.py also passes. A local XeLaTeX invocation encountered the default format-file environment, not a document error; root requested compilation in its configured integrated run. No independent complete fragment-PDF compilation is claimed.

Private scan previews, downloaded primary-source audit copies, dependency installations, and build_check are working material. No root/other-agent file was modified and no Library action was performed.
