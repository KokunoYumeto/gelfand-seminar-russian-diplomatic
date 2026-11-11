# Independent checks of local editorial arguments

Assessment date: 9 November 2026. These checks re-derive the displayed deductions;
they do not turn a metadata-only bibliographic match into a read theorem. The
separate research ledgers identify the sources actually obtained. The three
extended checks are also described in `GY1971_development.tex` and the root
research log.

| Occurrence | Independent check | Outcome |
| --- | --- | --- |
| 1971-241.1 | For a monomial differential operator of order m, each commutator with multiplication by f removes one derivative and introduces one derivative of f. After m commutators, the m! permutations give the symmetric principal symbol. The positive sign requires δ_f A = [A,m_f]; that convention was added explicitly after review. | Correct with the now explicit commutator convention. |
| 1971-241.5 | The derivation identity at 1 gives D(1)=0 even in characteristic two. Additivity annihilates the prime field. The recursively defined higher alternating-derivation functors therefore vanish as well. | No error found. |
| 1971-241.6 | For A=F₂[y]/(y²), Ω¹=A dy and the exterior powers above degree one vanish. The image of d is F₂ dy, its kernel is F₂, and Ω¹/dA has basis y dy. | H⁰=F₂, H¹=F₂ and higher groups zero, as stated. This does not compute the unidentified alternative complex. |
| 1971-243.2 | The flow x↦x+t on (0,1) is only locally defined. The complete R-action on R/Z has stabilizer Z despite evaluation being an isomorphism. | Both counterexamples satisfy their claimed hypotheses. |
| 1971-243.9 | Direct differentiation yields [∂x,x^(k+1)∂x]=(k+1)x^k∂x over characteristic zero. This leaves the proposed vanishing-order subspace. | It is not an ideal of all formal vector fields. |
| 1971-243.11 | The abelian one-dimensional Lie algebra has zero cochain differential, hence H¹=R. The invariant form dx on the contractible manifold R is the differential of x. | The comparison cannot be an isomorphism in this example. |
| 1971-243.17 | A homotopy of subbundles gives a quotient bundle on M×[0,1]. Its endpoint pullbacks are isomorphic, so their Pontryagin classes agree; Bott's necessary vanishing at the integrable endpoint transfers to the original one. | The deduction is necessary only; no sufficiency claim is made. |
| 1971-259.4 | Apply the long exact sequence of the homotopy fibre to S¹. The map on π₂(BU)=Z is multiplication by k−1, while reduced K⁰(S¹)=0. | [S¹,F_k]=Z/(k−1); it is nonzero for k>2. |
| 1971-261.3 | An inverse modulo trace class is an inverse modulo compact operators. For a Fredholm operator, split off its finite-dimensional kernel and cokernel and invert on the complementary closed subspaces. The two remainders are finite rank. | The algebraic quotient spectrum is exactly the Fredholm essential spectrum. No Banach-algebra quotient assertion is used. |
| 1971-265.3 | On an infinite discrete space, the constant function one restricts to a nonzero value at every point. Its family of restrictions belongs to a product but not a direct sum. | The direct-sum sheaf formula fails for infinite covers. |
| 1971-266.4 | Use the length-one projective resolution Z→Z→Z/p. Applying Hom(−,Z/p) gives Ext¹(Z/p,Z/p)=Z/p. Source and shifted target have cohomology in different degrees, so every induced degreewise cohomology map is zero. | The cohomology functor on the derived category is not faithful. |
| 1971-268.2 | MU₀=Z records the oriented count. Every compact complex zero-manifold is a finite set with positive complex orientations, so its class is nonnegative. The negative generator is a valid stable complex bordism class. | The claimed universal complex-manifold realization needs qualification. |
| 1971-268.6 | At a geometric point of Spec(MU_*), tensoring the coefficient module produces the residue field, whereas integral K⁰ of a point is Z. Inverting one generator does not impose all relations of the multiplicative formal group law. | The notebook's bare fibre cannot be identified with integral K-theory. The Conner–Floyd theorem itself is cited to literature. |
| 1971-270.7 | Differentiate F(F(x,y),z)=F(x,F(y,z)) with respect to z at zero. This gives f(F(x,y))=∂₂F(x,y)f(y). Since f(0)=1, its formal inverse exists. Over a Q-algebra, coefficientwise integration gives ℓ; differentiation in y and evaluation at zero prove ℓ(F)=ℓ(x)+ℓ(y). | The argument establishes commutativity without assuming it. Division by positive integers is essential. |

The additional independent reviews of the finite Radon arguments (235.1–2),
the compactness argument (233.8), and the cusp-ring counterexample (256.8) are
preserved with the reviewers' source fragments. The graded spectral-flow proof,
Dyson computation and mass computation have separate independent reviews in
the root research log and their full finite outputs in `audit/`.
