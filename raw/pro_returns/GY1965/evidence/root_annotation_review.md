# Parent review of the remaining critical annotations

**Date:** 9 November 2026. **Outcome:** The two early algebra examples and the late geometric and mechanical calculations pass independent derivation. All arguments below are checks supplied here, without a novelty claim. This review complements `early_proof_review.md`, `middle_proof_review.md`, and `development_review.md`.

## 1965-64.2: finite presentation does not imply coherence over an arbitrary ring

Let

\[
A=k[x_1,x_2,\ldots]/(x_1x_j:j\ge2),\qquad J=(x_2,x_3,\ldots).
\]

Every element has a unique expression \(f(x_1)+g\), with \(f\in k[x_1]\) and \(g\in J\). Multiplication by \(x_1\) kills \(g\) and gives \(x_1f(x_1)\), which vanishes only when \(f=0\). Thus \(\operatorname{ann}(x_1)=J\). The classes of \(x_j\), \(j\ge2\), are linearly independent in \(J/J^2\). The action of \(x_1\) is zero there, so a finite set of generators of \(J\) as an \(A\)-module would force this quotient to be finite-dimensional over \(k\), a contradiction. Hence the kernel of \(A\xrightarrow{x_1}A\) is not finitely generated. The module \(A\) has its one-generator free presentation but is not coherent. This independently verifies the actual example; non-Noetherianness by itself would not suffice.

## 1965-66.3: the natural map for the dual numbers

For \(A=k[\varepsilon]/(\varepsilon^2)\), every finitely generated projective module is free. One direct argument lifts a basis of \(P/(\varepsilon)P\) to a surjection \(A^r\to P\). Projectivity splits it; the complementary finite module has zero reduction modulo the maximal ideal and therefore vanishes by Nakayama's lemma. Rank consequently identifies \(K_0(A)\) with \(\mathbb Z\).

Every finitely generated \(A\)-module has finite length, with the unique simple module \(k\). Composition length identifies \(G_0(A)\) with \(\mathbb Z[k]\). The exact sequence

\[
0\longrightarrow (\varepsilon)\cong k\longrightarrow A\longrightarrow k\longrightarrow0
\]

gives \([A]=2[k]\). The natural comparison map is multiplication by two and is not an isomorphism, although its source and target are abstractly infinite cyclic. This checks the precise comparison made in the occurrence, without identifying the notebook's unspecified \(E(X)\).

## 1965-83.3–5: the recorded top

I independently eliminated the cyclic velocities from the recorded normalized Lagrangian. The momenta are \(n=\dot\varphi+u\dot\psi\) and \(e=\dot\psi+u\dot\varphi\); inversion of the coefficient matrix gives the denominator \(1-u^2\). Its quadratic energy numerator is \(n^2+e^2-2neu\). Multiplying the energy equation by \(2(1-u^2)\) gives

\[
\dot u^2=2(h-pu)(1-u^2)-n^2-e^2+2neu.
\]

Expansion agrees with every coefficient in the delivered cubic. The elimination is valid on \(|u|<1\); the endpoint and physical-branch qualifications are retained. `code/check_annotations.py` repeats this calculation symbolically through a separate implementation from `code/late_checks.py`.

## 1965-86.1: boundary-cosine normalization

I checked both proofs in `late_math_checks.tex`. In chord coordinates, \(n\cdot dM=dp+a\,d\theta\) and \(n\cdot dN=dp+b\,d\theta\); their exterior product contributes the chord length \(b-a\), rather than its reciprocal. The map from ordered boundary pairs to an unoriented line has multiplicity two. Fubini's chord-length integral is the area, giving \(2\pi|K|\).

The separate flux proof has the same sign. Its field \(F_M(x)=(m_M\cdot r)r/|r|^2\) is bounded, with divergence \((m_M\cdot r)/|r|^2\) in dimension two away from \(M\). The excised small-circle flux tends to zero. The absolute singularity is bounded by \(|x-M|^{-1}\), integrable uniformly on a bounded planar set and then over the finite boundary length. Reversing the order of integration is therefore justified. The final interior logarithmic flux is \(2\pi\), agreeing with the chord proof. The circle computation and independent numerical parameters check the same constant. No distance denominator should be inserted into the recorded formula.

## 1965-86.2: the slice counterexample and the averaged identity

For the ellipsoid, differentiating \(S(t)=\pi ab(1-t^2/c^2)\) gives \(S'(t)=-2\pi abt/c^2\). Integration gives \(8\pi^2a^2b^2/(3c)\), whose ratio to volume is \(2\pi ab/c^2\). The shape dependence defeats a universal fixed-direction constant; it is not a mere normalization discrepancy.

For the separately labelled angular average, the Fourier convention in the proof gives a one-dimensional Plancherel factor \((2\pi)^{-1}\), the signed-radius polar parametrization counts every nonzero vector twice, and three-dimensional Plancherel contributes \((2\pi)^3\). Their product is \(8\pi^2\). The proof and its density formulation are consistent. Neither the angular averaging nor that coefficient is retrospectively attributed to the source.

## Final disposition

These checks required no further correction to the delivered formulas. The separate reviews' field, weighted-count, frame, germ, and existence-interval improvements were applied centrally and are explained in the main report. Finite computations supplement these derivations; they are not used to claim an infinite theorem by sampling.
