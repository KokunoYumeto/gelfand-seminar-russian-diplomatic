# Independent review of the early explanatory arguments

**Reviewer:** late-record agent. **Date:** 9 November 2026.

**Scope.** I read `work/parts/early_report.md`, all **21** reconstructions marked `\ours` or `\oursComputed` in `early_items.json`, and the surrounding statements needed for their hypotheses. I independently checked **19** of those marked arguments. The noncoherent-ring example (1965-64.2) and dual-numbers comparison (1965-66.3) were already checked by root and were excluded from duplicate review as requested. I also checked Bernstein's complete source proof, 1965-62.1, because the report specifically relies on it. The separate Weyl development and publication-identification claims were outside this review.

**Outcome.** The principal proofs and counterexamples are sound. There is one small false necessity claim in the wording of 1965-63.8, leaving its Jacobian formula intact, and one field hypothesis that should be repeated in the standalone statement of 1965-58.2. Root has independently confirmed the first correction and is applying it centrally in assembly; the frozen early data were not altered.

All mathematical verifications below are supplied for this audit (`\ours` / `\oursComputed`), without a novelty claim.

## 1. Correction to 1965-63.8: unit weights are sufficient, not necessary

The formula
\[
 \int\delta(x-f(x))\,dx
 =\sum_{p=f(p)}\frac{1}{|\det(I-df_p)|}
\]
is correct with the stated nondegeneracy and consistent density conventions. The sentence saying that this equals the unweighted count **only** under unit-weight conditions is too strong: unequal positive weights can add to the number of points.

**Independent computation (`\oursComputed`).** On the closed one-dimensional manifold \(\mathbb{RP}^1\), let
\[
 f(x)=3x.
\]
Its two fixed points are \(0\) and \(\infty\). In the coordinate \(x\) at zero, the derivative is \(3\); in the coordinate \(y=1/x\) at infinity, the map is \(y\mapsto y/3\), with derivative \(1/3\). Both fixed points are nondegenerate, and their weights are
\[
 \frac1{|1-3|}=\frac12,\qquad
 \frac1{|1-1/3|}=\frac32.
\]
Their sum is \(2\), exactly the number of fixed points, although neither weight is \(1\). As a further consistency check, the de Rham local indices are \(-1\) and \(+1\), whose sum \(0\) agrees with the Lefschetz number of this orientation-preserving degree-one circle map.

**Recommended wording:** “The expression is generally a weighted fixed-point sum rather than an unweighted count. Unit weights suffice for equality with the count, but equality can also occur accidentally.”

**Disposition.** Root independently recomputed the example and accepted the correction for central assembly, including the example as a marked verification. No frozen tranche file was changed by this reviewer.

## 2. Hypothesis clarification in 1965-58.2

The marked example \(x^2=0\) versus \(x=0\) is correct. The formula
\[
 k[V(I)] = k[x_1,\ldots,x_n]/\sqrt I
\]
for functions on the **classical point set** requires the algebraically closed field hypothesis already present in the occurrence's notes. The standalone statement should repeat it explicitly.

**Independent check (`\ours`).** For \(k=\mathbb R\) and \(I=(x^2+1)\), the real zero set is empty, while \(\sqrt I=I\) and \(\mathbb R[x]/I\cong\mathbb C\ne0\). Thus the same point-set formula is not valid over an arbitrary field. This does not affect the scheme distinction or the argument in the intended algebraically closed context.

## 3. Checks of the other supplied arguments

| Occurrence | Independent mathematical check | Verdict |
|---|---|---|
| **1965-53.7** | In degree \(q=0\), the nonzero constant function on a bounded domain satisfies \(\bar\partial 1=0\); the degree-lowering adjoint is zero, so \(Q(1,1)=0\), while the boundary norm is positive. The example correctly excludes a degree-zero boundary estimate of the stated form. | Pass. |
| **1965-54.1** | For \(z=r^2\), \(K\,dA=4r(1+4r^2)^{-3/2}\,dr\,d\theta\), and \(\int_0^\infty4r(1+4r^2)^{-3/2}dr=1\). Thus total curvature is \(2\pi\). Independently, its injective Gauss map covers the open upper hemisphere, again giving \(2\pi\). The graph metric dominates the Euclidean base metric and gives a complete graph; it is homeomorphic to the plane. The Euclidean plane has total curvature \(0<2\pi\chi\). | Pass. |
| **1965-55.10** | The graded contraction rule gives \(\iota_v(\xi\wedge\omega)=\xi(v)\omega-\xi\wedge\iota_v\omega\). Choosing \(\xi(v)=1\) supplies a contracting homotopy in every degree. The sign \(df\wedge s=(-1)^q s\wedge df\) is correct. | Pass. |
| **1965-56.2** | Instantiate the example on \(S^1\): \(Su=\int_{S^1}u\) has smooth constant kernel, so \(I+S\) has principal symbol \(1\) and is elliptic of order zero. Choose \(u\) supported away from a point with nonzero integral; then \((I+S)u\) is nonzero there. It is therefore nonlocal and cannot be a differential operator. Ellipticity does not require invertibility of \(I+S\). | Pass. |
| **1965-56.4** | The Dolbeault complex on \(\mathbb C\) is elliptic, but its degree-zero cohomology contains the linearly independent functions \(1,z,z^2,\ldots\). This is a valid counterexample to omitting compactness. | Pass. |
| **1965-58.7** | A section on \(D(x)\cup D(y)\) lies in \(k[x,y]_x\cap k[x,y]_y\). If \(a/x^m=b/y^n\), then \(y^na=x^mb\); coprimality of \(x\) and \(y\) forces \(x^m\mid a\), so the intersection is \(k[x,y]\). The canonical map to its spectrum is the original open inclusion, since it induces the usual coordinate restrictions. An affine \(U\) would make that map an isomorphism, contradicting the missing origin. | Pass for schemes over any field. |
| **1965-58.10** | Every nonempty basic open \(U\times V\) of the product of two cofinite topologies meets the diagonal because \(U\cap V\ne\varnothing\). The diagonal is proper and dense there but Zariski closed in the affine plane. Product basic opens are also Zariski open, so the claimed strict refinement follows. | Pass. |
| **1965-58.12** | In the mixed chart of the doubled-origin line, the diagonal image is the punctured diagonal. Its scheme-theoretic closure is the full diagonal, including the pair of distinct origins. Over an algebraically closed field this also proves the classical point-set version. | Pass. Interpret arbitrary-field notation as schemes, not only rational-point topology. |
| **1965-60.1; 1965-62.1** | On a positive eigenspace, \(dd^*/\lambda+d^*d/\lambda=1\). A closed \(s\) therefore equals \(d(d^*s/\lambda)\), and commutation with \(\Box\) keeps the primitive in that eigenspace. For a concrete check, a nonzero Fourier mode of the circle de Rham complex has nonzero Laplacian eigenspaces but an isomorphism between its degree-zero and degree-one spaces; its cohomology is zero. | Dynin's displayed identification is false; Bernstein's contraction proof is complete under the stated spectral setup. |
| **1965-61.4** | Compression gives \(\lvert\operatorname{tr}T_\lambda\rvert\le\lVert T\rVert\dim\Gamma_\lambda\), without requiring eigenspace preservation. The bound \(N(\Lambda)=O(\Lambda^{n/2})\) makes the weighted sum converge for \(\Re z>n/2\). On compact subsets of that half-plane the same argument absorbs powers of \(\log(1+\lambda)\), giving normal convergence of all complex derivatives and hence holomorphy. A smooth weighted diffeomorphism pullback is bounded by change of variables. | Pass. The warning about arbitrary smooth maps is appropriate. |
| **1965-61.7** | Periodic integration by parts gives \((\partial_t)^*=-\partial_t\). Hence both circle Laplacians are \(-\partial_t^2\), with eigenvalues \(m^2\). | Pass. |
| **1965-63.4** | A chain map preserves \(B^i\subset Z^i\subset C^i\), so its trace splits over the filtration's diagonal blocks. The chain-map identity conjugates the \(L^i\) block to the \(B^{i+1}\) block via \(d:L^i\to B^{i+1}\). Their alternating traces cancel; invariant complements are unnecessary. | Pass for the finite bounded complex in the surrounding setup. |
| **1965-64.5** | The finite-type cokernel has finitely many local generators. Each has zero germ at \(x\), so each vanishes on a neighbourhood; their finite intersection is a neighbourhood on which the entire cokernel vanishes. No Noetherian or coherence hypothesis is needed for this step. | Pass. |
| **1965-66.1** | The countable direct sum \(Q=\bigoplus_{n\ge0}P\) is projective and isomorphic to \(P\oplus Q\). A Grothendieck relation allowing these objects gives \([Q]=[P]+[Q]\), hence \([P]=0\). | Pass; finite generation prevents this swindle in ordinary \(K_0\). |
| **1965-66.2** | Projectivity of \(P_2\) lifts its identity through \(P\to P_2\), giving a section and the isomorphism \(P\cong P_1\oplus P_2\). No canonical section is claimed. | Pass. |
| **1965-67.2** | For nonzero positive-definite \(\varphi\), the cone contains distinct \(0\) and \(2\varphi\), and \(\varphi=(0+2\varphi)/2\). It is therefore not an extreme point of that unnormalized convex set. | Pass. |
| **1965-65.4** | After triangularization over an algebraic closure, the trace of \(\Lambda^q A\) is the \(q\)-th elementary symmetric polynomial in the diagonal entries. Summing with alternating signs gives \(\prod_j(1-\lambda_j)=\det(I-A)\). Descent follows because both sides are polynomials in the entries. | Pass; diagonalizability is not required. |

## 4. Review limits and final disposition

The two root-reviewed algebra examples, 1965-64.2 and 1965-66.3, were read for context but not treated as new independent verification in this report. I did not re-review the original literature's analytic theorems, the historical class assignments, or scan/transcription judgments. In particular, the transverse entire-continuation theorem is a cited result rather than a new proof supplied by the early agent.

Apart from the already accepted central wording repair in 1965-63.8 and the explicit field-hypothesis repetition in 1965-58.2, **no substantive correction is needed to the reviewed explanatory arguments**.

