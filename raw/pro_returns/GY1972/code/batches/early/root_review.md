# Independent cross-batch review

Reviewed 9 November 2026. This is a read-only review of the root and other item batches; only files in `batches/early/` were written by this reviewer. The root has accepted and applied the substantive Berezin and Henkin corrections below. No chapter assembly or compilation was performed.

## Root mathematical review

### Berezin: 1972-291.19 is F

The marginal question on P486 does not specify the nonhomogeneous domain class, the analytic symbol algebra, admissible parameters, convergence conditions, or allowable changes of the integral kernel. The associated formal unital deformation theorem is a precise contextual comparison, but it is not a partial solution to a uniquely recoverable analytic problem. Accordingly, the item should be F, with literal correctness not determinable, partial publication match, no GP-1972-401, and no C-worth sentence. The root accepted this recommendation.

The later discussion was independently read in Berezin (1974), *Quantization*, §2.8, printed p.1133: https://www.math.stonybrook.edu/~leontak/Berezin-Quantization.pdf. It explicitly distinguishes the nonhomogeneous construction from the hypotheses under which a nonzero algebra has been established. The source provides historical context without fixing the notebook's omitted analytic category.

### Berezin: signs and hypotheses

P484, P486 and P487 were independently inspected as images. The root's corrected formulas are consistent:

- The Fock product differentiates the first symbol in the antiholomorphic variable and the second in the holomorphic variable.
- In the stated Gaussian normalization, annihilation is h times holomorphic differentiation and creation is multiplication by z.
- The Berezin transform is exp(h Delta/4); the Weyl midpoint is exp(h Delta/8) in the chosen real coordinates.
- The bounded-domain overlap has cross terms in the numerator and diagonal terms in the denominator; the Hilbert weight has exponent -1/h.
- On the disk, beta=2/h>1, the norm density is proportional to (1-|z|^2)^(beta-2), and the kernel is (1-z bar(v))^(-beta).
- Scalar convexity gives the stated trace inequality when the trace domains and normalized frame measure are specified. It does not imply an unrestricted operator inequality.

The operator-symbol identities were independently read in Berezin (1972), *Covariant and contravariant symbols of operators*, §§1–2: https://www.mathnet.ru/php/getFT.phtml?jrnid=im&paperid=2347&what=fullteng. The root also corrected the homogeneous-domain locator to §5 and restricted the compact published match to the classical symmetric cases.

### Henkin: 1972-292.3

Replace “F(U) is closed in Omega” with “F(D)=F(U) intersect Omega is a closed complex submanifold of Omega.” The neighbourhood U extends across the boundary, so its entire image is not a subset of Omega. Choosing U so that closure D is O(U)-convex makes the precise application transparent. The root accepted this correction.

Forstneric (2026), Theorem 1, independently opened at https://users.fmf.uni-lj.si/forstneric/papers/2026FH.pdf, states the Stein, holomorphic-convexity, proper embedding, convex-target and transversality hypotheses. The other Henkin statements were checked for regularity, boundary values, norm estimates and transverse submanifold hypotheses.

### Lomonosov: record 290

The corrected scaling separates the compact image from zero. The finite covering gives a positive partition denominator, the fixed point is nonzero, and commutativity makes the temporary compact eigenspace invariant. The finite-dimensional eigenspace belongs to the contradiction argument; it is not the theorem's promised conclusion. The locally convex reconstruction explicitly uses completeness, Hausdorffness and relative compactness of the image of a zero-neighbourhood. No further mathematical correction was identified.

## Independent arithmetic and endpoint checks

`independent_audit_checks.py` imports no root code. It independently implements exact Bernoulli recurrence, rational matrix coefficients, polynomial differentiation and direct sums. Results are in `independent_audit_checks.json`.

### 1972-298.8

For p=5 and k_i=1+2*5^i, put n_i=2k_i. Then n_i is congruent to2 modulo4 and tends p-adically to2. Continuity of the appropriate nonpolar tame-character branch gives

    (1-5^(n_i-1))*zeta(1-n_i) -> (1-5)*zeta(-1) = 1/3.

Since 5^(n_i-1) tends to zero, the raw values tend to1/3. The constant sequence k=1 instead gives -1/12. Their difference is5/12, so the notebook's sequence-independent raw continuity claim fails. Exact checks for i=0,1,2,3 yield valuations of raw-minus-1/3 equal to1,2,3,4, and valuations of raw-plus-1/12 equal to1 throughout. These computations supplement the branch-continuity proof.

### 1972-300.1–300.4

All65 power-sum cases and65 mixed-polynomial triangular systems passed, for degrees0–12 and endpoints0,1,2,5,11. The power-sum endpoint B_(k+1)(1) is correct. At k=0 it gives n, including n=0; B_1(0) would instead give n+1. The finite Taylor system has an upper triangular coefficient matrix with unit diagonal. Its inverse first row is B_r/r!, beginning1,-1/2,1/12,0,-1/720. The determinant and endpoint-derivative conventions are consistent. DLMF24.2 and24.4.1 were independently checked at https://dlmf.nist.gov/24.2 and https://dlmf.nist.gov/24.4.

## Buchstaber's reconstructed C programme

The relevant item is1972-287.11. Retaining C with medium confidence is justified by the explicit antecedent on P479: homotopy groups of the representing space. The later chosen trivialization data identify the smooth refinement with G/O. The residual numerical programme is the all-degree determination of pi_q(G/O), via coker J_q, ker J_(q-1) and the extension between them. The existence of the exact sequence is already established; no particular uncomputed finite-degree group should be invented. Lack of a bounded target prevents choosing this programme for new development, rather than making it unidentifiable.

Ranicki (2002), §9.2, Proposition9.21 and table9.22, was independently read at https://webhomes.maths.ed.ac.uk/~v1ranick/books/surgery.pdf. The cited finite progress was independently checked in Burklund, Isaksen, and Xu (2026), introduction and Theorem1.1, https://link.springer.com/article/10.1007/s42543-025-00098-y. Neither source is described as an all-degree numerical solution.

## Final schema and reference audit

`audit_final_batches.py` and `final_batch_audit.json` record the latest machine-readable snapshot, including SHA256 hashes of the input JSON files. The audit is read-only outside this batch. It checks required fields and types; every allowed assessment value; nonempty notes, statements, fates and statuses; November2026 dating; consecutive and globally unique occurrence IDs; talk linkage; reciprocal problem linkage; C/D worth statements; citation/ref-list/local-bibliography coverage; bibliography URL/DOI and verification notes; conflicting shared keys; control characters; and math-delimiter balance. A separate exact DOI/URL comparison found no replacement of an existing cumulative key by a newly named key.

The snapshot comprises28 talks and272 items: A25, B14, C1, D0, E219, F13. After the topology agent's repairs, it has **zero schema/link errors and zero bibliography warnings**.

The audit found and the topology agent corrected GP-1972-302's missing reciprocal link at1972-277.9. The agent also added ours markers to the supplied pencil substitution in1972-283.1 and zero-extension argument in1972-283.9. One further marker was recommended to the Buchstaber agent and parent: the supplied two-term-resolution calculation of Ext^2=0 in1972-279.4 should carry ours. This is a provenance-label repair, not a mathematical objection.

Three remaining automated marker candidates are false positives:1972-276.2 refers to a counterexample already in the notebook;1972-273.7 discusses independent bibliographic identification;1972-274.2 uses independently only to distinguish valuation normalization. None asserts a newly supplied proof in the flagged text.

Optional consistency suggestion sent to the parent: topology items277.7,283.1,283.8,283.9,283.11,294.9 and295.6 have ours markers but development=none. If annotated denotes the presence of short editorial checks, changing that field to annotated would make the assessment convention uniform. All existing values remain syntactically valid.
