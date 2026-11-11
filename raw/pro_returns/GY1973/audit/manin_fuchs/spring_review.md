# Independent mathematical review of the spring fragment

Reviewer: `/root/manin_fuchs`. Review date: 9 November 2026.

Scope: the 100 items in `work/fragments/spring_integrable/items.json`, records 325–333. The review is read-only with respect to that fragment. It checks mathematical normalization, missing hypotheses, and the distinction between an exact result and thematic context. It does not represent a second full bibliographical audit of every reference. The parent agent received the two concrete qualifications below. No further material mathematical issue was identified in the expressions and hypotheses checked here.

## Two qualifications for integration

### 1973-327.12: the two real forms of KP

The corrected compatibility calculation in 327.11 is consistent. With

\[
P=D^2+u,\qquad
Q=D^3+\tfrac34(uD+Du)+\lambda D+w,
\]

one obtains

\[
[P,Q]=2w_xD+w_{xx}-\tfrac14u_{xxx}-\tfrac32uu_x-\lambda u_x.
\]

For the assignment \(\beta\partial_z+P\), \(\alpha\partial_t+Q\), the compatibility conditions are

\[
w_x=-\tfrac34\beta u_z,\qquad
\beta w_z=\alpha u_t+\tfrac14u_{xxx}+\tfrac32uu_x+\lambda u_x.
\]

Their elimination gives exactly the equation recorded in the fragment:

\[
(4\alpha u_t+u_{xxx}+6uu_x+4\lambda u_x)_x
+3\beta^2u_{zz}=0.
\]

The sentence “Nonzero rescalings yield the usual two signs of KP” needs a qualification about the field and the real form. For real nonzero \(\beta\), real changes of scale cannot change the relative sign between \(u_{xxxx}\) and \(u_{zz}\): their scaling factors contain fourth and second powers, respectively. Thus real rescaling alone produces the positive transverse sign in this convention. A purely imaginary \(\beta\), together with a compatible reality condition on the auxiliary coefficient \(w\), gives the other real KP equation. Equivalently, one can explicitly allow complex continuation of the transverse variable. This is a qualification to the rescaling sentence, not a correction to the displayed elimination.

Suggested wording: “For real nonzero \(\beta\), real rescalings give the positive transverse sign of KP. The opposite real form results from a purely imaginary \(\beta\) and the corresponding reality reduction. Independence of the transverse variable gives KdV after the stated integration condition.”

### 1973-333.19: orientation of the half-wave flow

Item 333.18 fixes \(U(t)=\exp(+it\sqrt L)\). With the output-first primed relation used in 329.7, its canonical relation is the graph of geodesic flow at **negative time**. This follows directly in Euclidean coordinates from the phase

\[
\Phi(t,x,y,\xi)=(x-y)\cdot\xi+t|\xi|.
\]

Stationarity in \(\xi\) gives \(x=y-t\xi/|\xi|\), and the primed relation preserves the input covector \(\xi\). Thus \(U(t)\) transports \((y,\xi)\) by \(\exp(-tH_{|\xi|})\). The opposite exponential \(\exp(-it\sqrt L)\) has positive flow time. Item 333.19 currently says “by the Hamilton flow” without fixing this orientation. That is harmless for its unparameterized geodesics and the distance relation involving \(|t|\), but an explicit time sign would make it consistent with the adopted conventions.

Suggested insertion: “With the convention \(U(t)=e^{it\sqrt L}\), the primed canonical relation is the graph of geodesic flow at time \(-t\).” The statements about nonminimizing geodesic connections, caustics, and closed-geodesic length loci remain unchanged.

## Independently checked calculations and hypotheses

### Periodic Schrödinger and finite-gap material, record 326

The Lax normalization \(A_1=4D^3-3(uD+Du)\) gives \([A_1,-D^2+u]=u'''-6uu'\), as stated. The self-adjointness claim has a real periodic bounded potential and the appropriate \(H^2\) domain. The Floquet transform's sign, quasiperiodic boundary condition, inverse factor \(1/(2\pi)\), and Plancherel factor are mutually consistent. Gauging to periodic functions gives \(-(D+i\theta/T)^2+u\), with derivative \(-2i(D+i\theta/T)/T\).

The half-trace discriminant convention gives multipliers satisfying \(\rho^2-2d\rho+1=0\). The discussion correctly distinguishes bounded Bloch solutions inside a band from the existence of at least one bounded solution at a band edge. The constant-potential spectrum \([c,\infty)\) and discriminant \(\cos(T\sqrt{\lambda-c})\) are consistent. A closed gap has monodromy \(\pm I\); an open-gap endpoint permits a nontrivial Jordan block. The finite-gap inverse problem includes divisor data and does not claim that a finite-gap theorem solves the unrestricted inverse problem. The nontrivial odd-order commuting-operator condition avoids the vacuous polynomial-in-\(L\) case. The Riccati equation \(\chi_x+2ik\chi+\chi^2=u\) and the distinction between periodic and decaying integrals are consistent.

### Dressing and compatibility, record 327

The derivation rule for \(D=\partial_x+\partial_y\) on the truncated convolution has the necessary diagonal boundary term. For constant-coefficient differential operators, the full-kernel commutator uses \(\partial_x^n-(-1)^n\partial_y^n\). The two-operator zero-curvature sign is correct. The scalar second/third-order computation is recorded above. In the matrix first-order example, the first-order coefficient cancels by the Jacobi identity when the constant matrices commute, and the remaining commutator term has the stated order. The nilpotent linearization is valid under its explicit square-zero condition.

### Whitham averaging, record 328

For \(X=\varepsilon x\), \(S=\varepsilon t\), the slow-variable equation contains the factor \(\varepsilon^2\) in front of its second derivatives. Substituting a rapidly varying phase \(\Theta(X,S)/\varepsilon\) gives the leading oscillator equation \((\omega^2-k^2)f_{\theta\theta}+V'(f)=0\). Its period quadrature includes both legs of the oscillation. The averaged Euler–Lagrange equation and phase compatibility have consistent signs. The incompletely recorded action claim remains F rather than becoming a manufactured research problem.

### Wavefront and kernels, record 329

The definition of wavefront set fixes a cutoff and conic neighborhood before requiring decay of every order. The characteristic function of a smooth domain has the conormal wavefront set when its jump is nonzero. For extension of an operator to arbitrary compactly supported distributions, excluding wavefront points with zero output covector is the relevant condition; excluding points with zero input covector removes the independent output singularity term. The fragment assigns these roles correctly. The primed relation reverses the input covector and handles input-first versus output-first order explicitly. Kernel composition has the necessary support condition and wavefront transversality. The product criterion excludes opposing covectors. The discussion distinguishes the appropriate topology from an unrestricted continuity claim.

### Solitons and Miura transform, record 330

The profile \(q=2\kappa^2\operatorname{sech}^2(\kappa(x-\kappa^2t-h))\) solves \(4q_t+q_{xxx}+6qq_x=0\). The two-soliton displacement contains the correct factor \(\kappa_j^{-1}\log((\kappa_1+\kappa_2)/(\kappa_1-\kappa_2))\). The Wronskian-like polynomial \(P'Q-PQ'-2i\zeta PQ\) agrees with the exponential matching relation. The imaginary spectral node and its cubic time factor give the stated speed. The Miura identity

\[
u_t-6uu_x+u_{xxx}
=(D+2v)(v_t-6v^2v_x+v_{xxx}),\qquad u=v_x+v^2,
\]

is correct. Missing time-operator data and an unspecified amplitude claim are retained as limitations.

### Gauge groups and Fock normalization, record 331

The image of bundle automorphisms in the diffeomorphism group consists of diffeomorphisms preserving the bundle's isomorphism class. The gauge group is the section group of the adjoint bundle, with the ordinary current group only in a trivialization. The normalized exponential vector has components \(\xi^{\otimes n}/\sqrt{n!}\) and squared norm \(e^{\|\xi\|^2}\); the alternative weighted convention is distinguished.

### Heat and spectral trace material, record 333

The nonnegative operator \(L=-\Delta_g\), conjugated eigenfunction in the heat-kernel expansion, and closed-manifold hypothesis are explicit. The integrated coefficients \(a_1=\int R/6\) and

\[
a_2=\frac1{360}\int(2|\mathrm{Riem}|^2-2|\mathrm{Ric}|^2+5R^2)
\]

have the standard scalar-Laplacian normalization. The local Gaussian factor is restored. The higher coefficient's attribution remains bounded by the evidence.

The Cauchy smoothing correction is substantive and correct: Laplacian eigenvalue growth produces a tail comparable to \(\sum j^{-4/n}\), while square-root frequencies produce \(\sum j^{-2/n}\). The respective convergence conditions are \(n<4\) and \(n<2\). The heat-trace right half-plane and positive half-wave upper half-plane are distinct and correctly specified. Exact circle doublets are asserted only for the metric scalar Laplacian; arbitrary potential perturbations are excluded. The wave-trace length statement uses singular-support inclusion and separately qualifies clean fixed-point hypotheses and possible cancellations.

## Additional independent primary-source check: 1973-333.16

Shnirel'man, A. I. (1975). The asymptotic multiplicity of the spectrum of the Laplace operator. *Uspekhi Matematicheskikh Nauk, 30*(4[184]), 265–266. [Primary metadata](https://www.mathnet.ru/eng/rm4279); [full Russian text](https://www.mathnet.ru/php/getFT.phtml?jrnid=rm&option_lang=eng&paperid=4279&what=fullt).

I independently opened the metadata page and both pages of the Russian paper, including rendered page images. The paper explicitly defines \(\Lambda=\sqrt{-\Delta}\), states its result for every \(k>1\) and every \(N\), and assumes a smooth metric on the two-torus sufficiently close to the Euclidean metric. The displayed theorem is precisely a bound on the minimum of the preceding and following adjacent gaps by \(C_Nk^{-N}\). The following paragraph explicitly distinguishes Lazutkin's positive-density subsequence result. The proof invokes four distinct invariant KAM tori paired by the involution \((x,\omega)\mapsto(x,-\omega)\); the Diophantine restriction appears in the text. The receipt date on the second page is 7 May 1974. Thus the seemingly strong all-index quantifier, square-root spectral parameter, KAM qualification, and publication chronology in item 333.16 are supported by the actual paper.

Access trail: authoritative search1 query for Shnirelman/multiplicity/1975; metadata opened; its full-text link clicked; both PDF pages rendered. Tool references: `turn175search0`, `turn176view0`, `turn177view0`, `turn178view0`, `turn178view1`. A previous attempt using the Russian-interface URL failed; the English-interface full-text link succeeded. This review does not treat the failed access as evidence against the publication or the theorem.

## Exact versus thematic matching

The Green-polynomial heading in 325 and the Whitham–KdV heading in 332 remain insufficient to recover a theorem. The latter does not conflate B. M. Gurevich with A. V. Gurevich. The circle-lattice/zeta-zero analogy, ambiguous generic-gap question, and tentative three-torus remark remain F with their missing mathematical data stated. The billiard periodic-orbit claim distinguishes a boundary problem from a related closed-manifold trace theorem. None of these cases was promoted to an open problem by analogy.

## Disposition

The parent agent was informed of both convention qualifications and of the independently verified Shnirelman theorem. The review made no edits to the spring fragment and generated no new problem identifiers or status changes.
