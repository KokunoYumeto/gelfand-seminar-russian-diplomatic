Independent editorial proof review, 12 November 2026.
1. Reviewer records_b verified covariance theorem D1 with A>0, 0<eta<d, bounded Jordan sets. Near-diagonal bound O(L^{-(d-eta)}+delta^{d-eta}); off-diagonal Riemann sums have null discontinuity sets. Positive-volume variance implies unique exponent d-eta/2. Unit-square target independently reduced to D4, including checks J_0=1 and J_1=4 asinh(1)-(4/3)(sqrt(2)-1). No weak convergence follows from covariance convergence alone.
2. Reviewer records_c independently derived the Radon raw energy 8 pi^2 ||f||_2^2 and normalized average 2 pi |E|. Also derived ||Rf||_2^2=(1/pi)int |fhat(xi)|^2/|xi|^2 dxi <=4||f||_1^2+8pi^2||f||_2^2. L1/L2 Schwartz approximation identifies actual sections and their weak derivatives; almost every direction, no boundary regularity needed.
3. Reviewer records_c checked H=pq^2, q=-1/tau,p=h tau^2. Jacobian of (q,p) with respect to (t0,h) is -1, so the nonstationary family has two independent constants. Q=q+p,P=q+2p is canonical. Generic fibre is C*, function field C(q), projective genus zero. q^2 d/dq is not translation invariant on the multiplicative group, so no generalized-group linearization is claimed.
4. Reviewer records_b checked G=(R3,+), pi=z dx-wedge-dy is multiplicative and Poisson; dual [dx,dy]=dz. H=z-axis has annihilator span(dx,dy) not closed, but every invariant algebra of a trivial action is Poisson closed. This disproves the single-action necessity, not the sufficient coisotropic condition.
5. Root JavaScript program independently checked covariance pair counts against direct four-index sums, two quadrature resolutions, three ball radii, six 4x4 differential symbols and twelve Hamiltonian solution values. All checks are finite audits; analytic proofs establish the stated universal claims.

# Independent mathematical checks supplied to the parent

These checks concern the parent's separate bounded-development work and are not additional items assigned to records 611–619.

## Covariance scaling

Let $(\sigma_x)_{x\in\mathbb Z^d}$ be a real stationary field with finite second moments, covariance $\rho(h)$, and constants $0<\eta<d$, $C<\infty$ such that $|\rho(h)|\leq C(1+|h|)^{-\eta}$ and $|h|^\eta\rho(h)\to A$ uniformly over lattice directions as $|h|\to\infty$. For bounded Jordan-measurable sets B,C, write $S_L(B)=\sum_{x\in LB\cap\mathbb Z^d}\sigma_x$. Then
$L^{-2d+\eta}\operatorname{Cov}(S_L(B),S_L(C))\to A\int_B\int_C|u-v|^{-\eta}\,du\,dv$.

For $|x-y|<\delta L$, the number of possible x is $O(L^d)$ and the lattice sum of $(1+|h|)^{-\eta}$ over $|h|<\delta L$ is $O(1+(\delta L)^{d-\eta})$. After normalization the absolute contribution is $O(L^{-d+\eta}+\delta^{d-\eta})$. On the complementary region, uniform covariance asymptotics and the bounded, Riemann-integrable truncated kernel give the ordinary lattice Riemann-sum limit. Jordan boundaries and the hypersurface $|u-v|=\delta$ have measure zero. The limiting integral over the excluded diagonal neighborhood is $O(\delta^{d-\eta})$. Let L tend to infinity and then delta to zero.

If $A>0$ and B has positive volume, the limiting variance coefficient is finite and strictly positive, so the unique power normalization yielding a finite nonzero variance is $\alpha=d-\eta/2$. If A is only assumed nonzero, positivity of variance forces A>0. If A=0, the stated asymptotic does not determine a unique exponent. These covariance conclusions do not establish weak convergence of the field or identify a limiting distribution; tightness, uniform integrability where needed, and higher-order information are separate issues.

For d=2 and the unit square, convolution reduces the integral to
$4\int_0^1\int_0^1(1-x)(1-y)(x^2+y^2)^{-\eta/2}\,dx\,dy$.
Split across x=y and substitute y=xt in the lower triangle. The result is
$8\int_0^1(1+t^2)^{-\eta/2}[1/(2-\eta)-(1+t)/(3-\eta)+t/(4-\eta)]\,dt$.
Equivalently it equals
$\frac{8}{(2-\eta)(3-\eta)(4-\eta)}\int_0^1[(4-\eta)-(2-\eta)t](1+t^2)^{-\eta/2}\,dt$.
The eta=0 continuation gives 1; eta=1 gives $4\operatorname{arsinh}(1)-\frac43(\sqrt2-1)$.

## Single-action counterexample to a coisotropy equivalence

Let $G=(\mathbb R^3,+)$ and $\pi_G=z\,\partial_x\wedge\partial_y$. Its linear coefficients make the bivector multiplicative, and its Schouten bracket vanishes because its coefficient is independent of x and y. The Lie bialgebra cobracket satisfies $\delta(e_z)=e_x\wedge e_y$ and $\delta(e_x)=\delta(e_y)=0$, so the dual Lie algebra has $[dx,dy]=dz$. For the z-axis subgroup H, $\mathfrak h^\perp=\operatorname{span}(dx,dy)$ is not a Lie subalgebra; H is not coisotropic. Equivalently, at a point of H with z nonzero, the image of its conormal under $\pi_G^\sharp$ is the xy-plane rather than a subspace of the z-axis tangent.

Let G act trivially on any symplectic manifold M. The action map is the projection $G\times M\to M$ and is Poisson for the product Poisson structure. All smooth functions on M are H-invariant, and they form a Poisson subalgebra. Thus Poisson closure of invariants for one arbitrary Poisson action does not imply coisotropy of H. A universal-action version requires its own quantifiers and hypotheses.

Both checks were done directly. They are reviews of the parent's proposed bounded statements, not external-literature claims or new notebook occurrences.

# Independent review: Laurent poles and compact algebraic complete integrability

Reviewed 2026-11-12. The proposed example is correct for the narrowly stated implication: existence of an (n−1)-parameter Laurent family, even with every chosen coordinate having a pole, does not by itself force generic invariant fibres to admit a compact abelian-variety completion. Here n=2 means the complex dimension of phase space; it must not be confused with the number of degrees of freedom, which is one.

Take the symplectic affine plane with form dq∧dp and Hamiltonian H=pq². Hamilton's equations are q'=∂H/∂p=q² and p'=−∂H/∂q=−2pq. For τ=t−t₀, every nonconstant solution is q=−τ⁻¹, p=hτ², and H=h. The branch q=0, p=constant is a separate family of equilibria on the zero fibre. At fixed t₀, the nonconstant Laurent family has the one free parameter h=n−1. The parameter map (t₀,h)↦(q(t),p(t)) has Jacobian determinant −1 wherever τ≠0, so the family genuinely supplies two local integration constants and is not a lower-dimensional special solution family.

The linear change Q=q+p, P=q+2p is symplectic: its matrix has determinant one and dQ∧dP=dq∧dp. Its inverse is p=P−Q, q=2Q−P. Therefore H=(P−Q)(2Q−P)² and the same solutions become Q=−τ⁻¹+hτ² and P=−τ⁻¹+2hτ². Both coordinates have simple poles with nonzero leading coefficient, for every h, including generic h≠0.

For a fixed h≠0 the invariant affine curve pq²=h is smooth: its gradient (2pq,q²) never vanishes on it. The map q↦(q,h/q²) identifies that curve algebraically with C*. Its function field is C(q), so its unique smooth projective completion is P¹, of genus zero. Any smooth compact algebraic completion of the same curve has the same function field and hence the same genus. A positive-dimensional complex abelian variety of dimension one has genus one. Thus this generic invariant curve cannot be an open algebraic subset of an elliptic curve, nor have a smooth projective abelian completion.

The zero fibre is singular/reducible as a scheme, but the argument uses h≠0 and does not depend on it. The affine cubic closure can be singular at infinity; its normalization is P¹, which is the relevant smooth completion.

Scope: the example is a one-degree-of-freedom Liouville-integrable system. It does not contradict statements allowing generalized Jacobians, rational degenerations, generalized algebraic groups, or additional hypotheses beyond the bare Laurent-family condition. Moreover, on C* the vector field q²∂q is not translation invariant for the multiplicative group law: invariant vector fields there are constant multiples of q∂q. On P¹ it extends holomorphically and becomes −∂u in the chart u=1/q, with its unique double zero at q=0. Therefore the example should not be described as linear flow on the algebraic group C* merely because its generic affine fibre is C*.

Suggested precise proposition: 'There exists a polynomial Hamiltonian on the symplectic affine plane whose general nonstationary solution admits a one-parameter Laurent expansion at a movable pole, in linear symplectic coordinates in which both coordinate functions have simple poles, while every nonzero invariant fibre has rational, rather than abelian, smooth projective completion.' The displayed example proves this proposition directly.

No external factual premise is needed beyond the standard birational invariance of genus for smooth projective curves and the fact that one-dimensional abelian varieties are elliptic curves. This is an independent elementary check; it makes no claim about an exact theorem in the historical source until that theorem's complete hypotheses and its definition of algebraic complete integrability have been matched.

# Independent review: three-dimensional Radon section energy

Reviewed 2026-11-12. The claim and constants are correct, with the derivative interpreted as the weak derivative and the section function defined for almost every plane. Surface measure dΩ on S² must have total mass 4π.

More generally let f∈L¹(R³)∩L²(R³) and define Rf(θ,t)=∫_{x·θ=t}f(x)dH²(x). With Fourier convention f̂(ξ)=∫e^(−ix·ξ)f(x)dx and one-dimensional Plancherel factor (2π)⁻¹, the Fourier-slice formula is (Rf(θ,·))̂(σ)=f̂(σθ). For Schwartz f,
∫_{S²}∫_R |∂tRf|²dt dΩ
=(2π)⁻¹∫_{S²}∫_R σ²|f̂(σθ)|²dσ dΩ
=π⁻¹∫_{R³}|f̂(ξ)|²dξ
=8π²||f||²₂.
The middle equality counts each nonzero ξ twice because σ ranges over both signs.

The unweighted L² norm also has an exact expression:
||Rf||²_{L²(S²×R)}=π⁻¹∫_{R³}|f̂(ξ)|²|ξ|⁻²dξ.
It is finite for f∈L¹∩L². On |ξ|≤1, |f̂(ξ)|≤||f||₁ and ∫_{|ξ|≤1}|ξ|⁻²dξ=4π. On |ξ|>1, the integral is bounded by ∫|f̂|²=(2π)³||f||²₂. Consequently
||Rf||²₂≤4||f||²₁+8π²||f||²₂.
The particular cutoff 1 merely fixes a convenient nonhomogeneous estimate.

Choose Schwartz f_j→f in both L¹ and L². The displayed estimate makes Rf_j Cauchy in L²(S²×R), and the energy identity makes ∂tRf_j Cauchy in that same space. Closedness of the weak derivative gives a limit U with ∂tU∈L² and preserves the equality by strong convergence. On the other hand,
||R(f_j−f)||_{L¹(S²×R)}≤4π||f_j−f||₁,
by the plane-coordinate Fubini formula. Hence the L² limit equals the physical plane integral Rf almost everywhere; for example use local convergence in measure, or an almost-everywhere subsequence from both limits. Fubini then implies Rf(θ,·)∈H¹(R) for almost every θ, with the above integrated derivative norm.

For f=1_E with E Lebesgue-measurable and |E|<∞, f∈L¹∩L² and ||f||²₂=|E|. Thus
(4π)⁻¹∫_{S²}∫_R|S′_θ(t)|²dt dΩ=2π|E|,
and S_θ∈H¹(R) for almost every θ. No boundedness, convexity, boundary regularity, or finite perimeter assumption is required. Empty/null E is included.

Necessary precision: the theorem asserts almost-everywhere directional regularity, not H¹ for every direction. Plane sections can depend on the chosen representative of E on an exceptional set of planes, but the jointly almost-everywhere Radon function, its weak derivative, and the integrated identity are unaffected. Do not identify S′ with a pointwise boundary integral without extra regularity. The argument supplies the exact theorem for measurable finite-volume sets without such a boundary formula.

Sanity check: for the ball of radius R, S_θ(t)=π(R²−t²) for |t|≤R and zero otherwise. Its derivative energy is 8π²R³/3, equal to 2π·(4πR³/3), confirming the normalization.
