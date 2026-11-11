# Independent checks supplied to the coordinating agent

Date: 2026-11-09. These checks do not alter the files owned by other agents.

## Conditional pair-sum variance bound

Let Ω be a measurable finite-volume subset of R^d, |Ω|=V>0. Let a simple point process have symmetric factorial moment densities r_2,r_3,r_4 relative to Lebesgue measure. Let f be a real even function in L1∩L2 and write the ordered pair sum F=Σ_{i≠j} f(x_i−x_j), with both points restricted to Ω. Suppose, almost everywhere,

- r_2≤C_2 and r_3≤C_3;
- |r_4(x_1,x_2,x_3,x_4)−r_2(x_1,x_2)r_2(x_3,x_4)| ≤ C_4 Σ_{a∈{1,2}, b∈{3,4}} g(x_a−x_b)+C_0/V;
- g≥0 belongs to L1.

For a volume-indexed family, all constants and the L1 norm of g must be uniform in V. No translation invariance of the densities is used by the estimate.

### Independent derivation of the combinatorial coefficients

Expand F² using ordered pairs (i,j) and (k,l). If exactly two indices occur, the second pair equals the first or its reversal. Evenness of f gives two copies of f_12². If exactly three indices occur, the coincident-index choices are i=k, i=l, j=k, and j=l. Symmetry of the factorial density, evenness of f, and relabeling give four copies of f_12 f_23. The remaining terms use four distinct indices. Consequently

E F² = 2∫_{Ω²} f_12² r_2 + 4∫_{Ω³} f_12 f_23 r_3 + ∫_{Ω⁴} f_12 f_34 r_4.

Subtracting (E F)² replaces r_4 in the last integral by r_4−r_2 r_2. Coordinate diagonals have Lebesgue measure zero, so they do not add extra terms to that product integral. Absolute integrability follows from the stated bounds; alternatively establish the formula first for bounded truncations and then use the bounds for absolute convergence.

### Independent derivation of the analytic constants

The pair term is at most 2 C_2 V ||f||_2². Integrating the leaves of the path 1–2–3 gives a bound V||f||_1² for the absolute triple integral before its density constant and coefficient 4.

For each of the four cross terms g(x_a−x_b), the two f-edges (1,2) and (3,4), together with the g-edge, form a tree on four vertices. Fix one vertex and successively integrate the leaves, enlarging each leaf domain from Ω to R^d. This gives V||f||_1²||g||_1 for each term. The constant remainder contributes (C_0/V)(V||f||_1)². Thus

Var F ≤ V [2 C_2 ||f||_2² + 4 C_3 ||f||_1² + (4 C_4 ||g||_1+C_0)||f||_1²].

The proposed coefficients are correct. For signed f the proof must explicitly bound the triple and disjoint integrands in absolute value, rather than assert they are nonnegative.

### Canonical example and the necessity of the 1/V allowance

For N independent uniform points in Ω, r_k=(N)_k/V^k. For N≥2,

|r_4−r_2²| = N(N−1)(4N−6)/V⁴ ≤ 4ρ³/V, where ρ=N/V.

Therefore a density-uniform bound permits C_0=4 sup ρ³. A purely integrable cross-decay estimate without a finite-volume remainder would miss this spatially constant canonical correction.

### L1 does not imply a finite variance

Take Ω to be a ball, N≥2 independent uniform points, and f(x)=|x|^(−α) 1_{0<|x|<1}, where d/2≤α<d. Define f(0) arbitrarily, since collisions have probability zero. Then f is even, nonnegative, L1, and not L2. Its pair expectation is finite. The overlap measure |Ω∩(Ω−h)| is bounded below by a positive constant for all sufficiently small h, so ∫_{Ω²} f(x−y)² dx dy diverges. Since F≥0, the two-index contribution gives E F²=∞. Thus this is a genuine finite-expectation, infinite-variance counterexample, rather than an undefined random variable.

## Truncation and concentration for L1 kernels

For a fixed real even f∈L1, let f_M=f 1_{|f|≤M}. Then ||f_M||_2²≤M||f||_1 and f_M∈L1∩L2. The r_2 bound alone gives E|F(f−f_M)|≤C_2 V||f−f_M||_1, hence

E|[F(f−f_M)−E F(f−f_M)]/V|≤2 C_2 ||f−f_M||_1.

Split the centered error into its truncated part and its centered tail. Chebyshev at threshold ε/2 for the first and Markov at ε/2 for the second give

P(|F(f)/V−E F(f)/V|>ε) ≤ 4 K(f_M)/(ε² V) + 4 C_2 ||f−f_M||_1/ε,

where K is exactly the bracket in the variance bound. First V→∞ with M fixed and then M→∞ proves concentration about the V-dependent expectation. The proposed constants are correct. This conclusion is a weak law centered at the actual mean; convergence to a fixed thermodynamic number additionally requires convergence of E F/V. The L1 counterexample to finite variance does not obstruct this concentration argument.

## Record 94 checks

The following issues were reported directly to the coordinator:

1. **Heisenberg coordinate mismatch in 94.3.** The proposed group law `(a+a2,b+b2+ac2,c+c2)` would make b central and fit weights a,c↦u(a,c), b↦u²b. The draft instead displayed `(a+a2,b+b2,c+c2+ab2)`, which makes c central, but retained those former weights and the former proof. The consistent repair is either to change the law or to scale a,b by u and c by u². The current mixed conventions do not define a group homomorphism. This was caught by checking the cross term independently.
2. **Source pages and stated status of the four assertions.** Items 94.8–94.11 are on P000143. Only assertion 1 has a question mark; assertions 2–4 are explicitly grouped under “Опровергнуты Смейлом.” Notes fields should preserve that contemporary refutation rather than describe all four as unresolved questions.
3. **Generic periodic density.** The residual Diff^1(M) statement is mathematically correct. The opened Pugh translation at https://www.mathnet.ru/php/getFT.phtml?jrnid=mat&option_lang=eng&paperid=491&what=fullt gives the flow statement in Theorem 6.5, pp.144–145. Its “second category” is defined as complement-meagre, hence residual. The analogous diffeomorphism result follows by the usual countable-basis argument from the C1 closing lemma and persistence after making a periodic orbit hyperbolic. The literal source statement and modern counterpart should be distinguished if citing only that translation.
4. **Anosov classification.** The strong topological-conjugacy conjecture is distinct from the weaker manifold-homeomorphism conjecture. The opened Spatzier paper, *On the work of Rodriguez Hertz on rigidity in dynamics*, J. Modern Dynamics 10 (2016), 191–207, Conjecture 2.3, p.192, explicitly states the former: https://sites.lsa.umich.edu/spatzier/wp-content/uploads/sites/1081/2023/03/brinprize.pdf . Deré–Mainkar's opened arXiv:2008.09717, abstract and pp.1–2, states the weaker manifold question. Its preprint date is 21 August 2020, publisher first-online date 10 November 2022, journal-volume date 2023.
5. **Precision.** Use closed orientable surfaces in 94.6 unless boundary conditions are specified. In 94.7 say “finite union of hyperbolic equilibria and periodic orbits,” rather than “finite nonwandering set,” since a periodic flow orbit has infinitely many points.
6. **Problem identities.** GP-1966-01 through 07 have distinct statements and consistently refer to 94.4, .8, .9, .10, .11, .16, .17. No earlier matching GP identity was found in the supplied previous index. The spectral-decomposition item correctly retains both Axiom A clauses despite the notebook's claim that the first clause alone suffices.


## Independent review of items 1966-102.1, 1966-102.5, and 1966-104.4

### Sturm converse counterexample (102.1)

The proposed y=x^(-1/2) exp(epsilon cos(2x²)) sin(x²), epsilon=1/100, and the displayed f are correct. Put A=x^(-1/2) exp(epsilon cos(2x²)) and a=A′/A=−1/(2x)−4 epsilon x sin(2x²). Then

 y″/A=(a′+a²−4x²)sin(x²)+(4xa+2)cos(x²).

Using sin(2t)cot(t)=1+cos(2t), followed by continuity at the zeros, gives

 f=x²[4+16 epsilon+32 epsilon cos(2x²)−16 epsilon²sin²(2x²)]−3/(4x²).

For x>1, the bracket is at least 4−16/100−16/10000, so f>7721/2500>0. At 2x²=pi/2+2k pi,

 f′=2x(4+16 epsilon−16 epsilon²)−128 epsilon x³+3/(2x³),

which is negative for all sufficiently large k. The zeros sqrt(k pi) have strictly decreasing consecutive gaps. Thus the positive-coefficient converse is disproved by the example as stated.

`check_sturm_endpoint.py` computes the residual exactly in a Laurent polynomial algebra with u=sin(x²), v=cos(x²), reduced modulo u²+v²−1. The exact residual vanishes. An independent second-order Taylor-jet calculation gives maximum relative residual 4.116185065749563e−16 over 24 samples. This independent calculation does not reuse the hand-derived f′ or the polynomial derivative code.

### Reciprocal endpoint limit (102.5)

The two-sided endpoint proof is correct for a C1 function with simple consecutive zeros a,b and no interior zero. Choose 0<eta<|y′(a)| before bounding |y(x)| between (|y′(a)|−eta)(x−a) and (|y′(a)|+eta)(x−a). Raising to lambda in (−1,0) reverses the inequalities. After integration and multiplication by lambda+1, the endpoint contribution tends to 1/|y′(a)|; the compact middle portion contributes zero. Repeat at b. The original wording “for each delta>0” should be restricted below the nonzero endpoint slope before fractional powers are taken.

The same code compares the exact beta formula for sin(x) on [0,pi] against independently regularized numerical quadrature. At delta=lambda+1=1e−8 the two values are 2.000000013862945 and 2.0000000138629437, respectively, tending to 2. A second beta example y=x(1−x²) on [0,1] tends to 3/2, matching endpoint slopes 1 and −2; at delta=1e−8 the beta value is 1.5000000000000044. These examples test the formula and do not replace the general endpoint proof.

### Stabilization of a Fredholm family (104.4)

The reconstruction is correct. For a norm-continuous family of bounded Fredholm operators between complex Hilbert spaces, a finite-dimensional complement at one point makes the augmentation surjective nearby because surjectivity is open for operators with a bounded right inverse. Compactness supplies a finite sum V of such complements. For B_x surjective and a right inverse R_0 of B_x0, a local right inverse is R_x=R_0(B_x R_0)^(-1). The norm-continuous projection P_x=I−R_xB_x has image ker B_x. Its finite rank is locally constant, and nearby projections yield a local bundle trivialization.

For V contained in W, the exact sequence is obtained from (u,w) in ker B_W by the map (u,w)↦w mod V. It is onto because B_V is onto; its kernel is ker B_V. This is an exact sequence of finite-rank complex bundles and splits over compact Hausdorff X, so the virtual difference is unchanged. A sum compares arbitrary choices. Applying this construction over X×[0,1] proves homotopy invariance, using homotopy invariance of bundle K-theory. Explicitly specify “complex Hilbert spaces” for the complex K^0 statement. The ambiguous projected notebook homotopy is not needed by this proof.
