# Independent conceptual review of the bounded development

Date: 10 November 2026. Reviewer: winter-records agent. Scope: a second-pass mathematical review of the root draft `GY1980_development.tex`, read after the winter data were saved. This is a conceptual audit of the stated arguments and their hypotheses, not a claim to a new theorem, a new historical attribution, or an independent rerun of all symbolic computations.

## Conclusion

The unit obstruction, the prescribed affine genus-two counterexample, the order test for injectivity, and the passage from an embedded commutative coordinate ring to its function field are correct under the explicit hypotheses now present in the draft. I found no remaining flaw in those arguments. The draft correctly separates the all-genus-two existence theorem, the choice of affine model, and the universal function-field question.

## Exact scope of the unit obstruction

The source is the coordinate ring of a smooth irreducible affine curve over **C**, its smooth projective model has genus at least one, and the map is an **injective unital C-algebra homomorphism** into the ring of finite-order ordinary differential operators **C(x)[D]**, with **Df = fD + f′**. The source must contain a unit that is not in **C**. These hypotheses are all explicit in the current proposition.

For nonzero operators, the highest derivative coefficient of a product is the product of the highest coefficients. The order is additive and nonnegative in this ring. Hence its units are exactly the nonzero rational multiplication operators. Injectivity and C-linearity force the image of the chosen nonconstant unit to be a nonconstant rational function f. In characteristic zero, f′ is nonzero. The coefficient of D^(m−1) in [A,f], for a positive-order A with leading term a_m D^m, is m a_m f′; lower-order summands cannot cancel it. Thus the centralizer of f in the ordinary differential-operator ring is exactly C(x).

The commutativity of the whole source consequently gives an embedding of its fraction field into C(x). This is an inclusion of one-variable function fields over C and induces a nonconstant rational map from P1 to the smooth projective model of the source curve. Properness of the target and smoothness of P1 extend the map across the finitely many initially undefined points; a nonconstant morphism of projective curves is finite. Characteristic zero ensures separability. Riemann–Hurwitz then contradicts positive genus. The current draft has these qualifications. An alternative proof could use Lüroth's theorem, but no replacement is needed.

## The concrete affine example

For F(z,w)=z w²−z⁴−1, the identity z(w²−z³)=1 proves that z is a unit. It is nonconstant, as is also clear from the birational hyperelliptic model. Setting Y=zw gives an isomorphism of this affine curve with the open set z≠0 of Y²=z⁵+z. The polynomial z⁵+z has five simple roots: its derivative is 1 at zero and −4 at the nonzero roots. Its odd degree contributes one branch point at infinity, giving six simple branch points and genus two.

Irreducibility follows because z⁵+z has an odd valuation at each simple zero and is therefore not a square in C(z). Smoothness of the prescribed affine model follows directly from z≠0 and F_w=2zw: at a possible common zero of the partial derivatives, w would vanish, but F_z=−4z³ would be nonzero. Thus every hypothesis of the unit obstruction is met.

This proves failure for the prescribed affine coordinate ring. It does **not** obstruct the abstract function field in the Weyl division ring. The draft's final corollary explains this correctly: using the previously checked genus-two existence theorem, w is represented by M_0 P_0^(-1). If that quotient were an ordinary differential operator, P_0((M_0 P_0^(-1))²−P_0³)=1 would make the positive-order P_0 a unit in C(x)[D], a contradiction. The quotient can have positive total differential order and nevertheless fail to be an ordinary differential operator; the argument does not require its total order to be negative.

## The order test and field extension

The unique representative f(z)+g(z)w follows from division by the monic quadratic relation in w. A positive-order P is transcendental over C by the order of its successive powers. Nonzero f(P) and g(P)M have respective orders r deg(f) and r deg(g)+s. When r does not divide s, these orders are incongruent modulo r and cannot cancel. The one-summand cases are also nonzero. This proves injectivity. The nonsquare assumption on F guarantees an integral curve ring; it is sufficient for the field interpretation and is not an extra unsupported consequence of the order argument.

The same proof works in C(x)[D], as stated later in the draft. For the certificate, r=4 and s=10 satisfy the condition. Extension to the ordinary commutative fraction field inside Q(A1) is valid because the embedded source is commutative, and its inverses commute with every element of that source. No assertion about the rank of the full centralizer follows merely from the greatest common divisor of the two exhibited orders, and the draft correctly avoids that inference.

## Normalizations and computational scope

I checked the algebraic conventions and the smoothness calculation conceptually, using the recorded exact outputs rather than rerunning the expensive full operator multiplication.

- With [D,x]=1, Lx=xL+2D, so (3/2)(xL+Lx)=3xL+3D. The corrected elliptic expression in the draft is consistent.
- The distinction between the displayed Mironov expression and the centered operator M is a scalar shift. If the displayed operator is M+9, its correct relation is (M_displayed−9)²=F(P). Such a scalar does not change commutation but does change the uncentered polynomial equation. The draft states this precisely and limits the source claim to the checked preprint.
- For F_a(z)=z⁵+27az²+81, a common root of F_a and its derivative must be nonzero and satisfies z³=−54a/5 and az²=−5. Hence z=54a²/25 and 2916a⁵+3125=0. Conversely those relations produce a common root. This independently confirms the stated exceptional parameter locus.
- The finite multiplication formula uses left normal form and ordinary x-derivatives, consistently with Df=fD+f′. The separate test on monomials 1,x,…,x^r does detect every coefficient of an operator of order at most r, by induction. Checks at finitely many parameters alone would not prove the symbolic parameter identity; the draft explicitly relies on its all-parameter polynomial computation for that claim.
- The formal square-root correction has the right leading mechanism: (L+xL^(-1))² introduces 2D L^(-1), and the added −D L^(-2) cancels that defect to the relevant order. I did not independently reproduce every truncated coefficient, and the audit does not claim otherwise.

No patch is required for these proofs. The status of Oganesyan's theorem and the literature search for the universal conjecture remains the responsibility of the root's source audit; this review does not independently recertify papers outside the winter assignment.
