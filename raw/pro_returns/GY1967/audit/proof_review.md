# Independent algebraic review of the Weyl-coordinate development

Reviewer: `/root/records_155_166`. Date: 9 November 2026.

Reviewed file: `output/GY1967/GY1967_development.tex`, as read after the parent’s request to check the complete proof. This review did not edit that file. Literature novelty and historical status are outside this proof audit; the development already explicitly identifies the result as a known bounded case.

## Verdict

**No mathematical defect found.** The formal-series construction supports the centralizer lemma. The normalizer formula, both inverse compositions, the shear conjugation action, and the polynomial boundary are correct with the stated characteristic-zero base field, left coefficient convention, and composition of algebra automorphisms.

The proof’s scope is correctly bounded by equality of the rational coordinate fields, not containment. It does not infer generation of the division ring merely from a Weyl commutator relation.

## 1. Formal pseudodifferential division ring

Let K=C(q), with its usual derivation, and let S consist of sums bounded above in powers of p. The coefficient-finiteness argument is sufficient. For a coefficient of exponent ℓ in a product of orders at most m,n, contributing indices satisfy i≤m,j≤n and i+j≥ℓ. Therefore i≥ℓ−n and j≥ℓ−m, leaving finitely many pairs; the derivative index is fixed by k=i+j−ℓ. No analytic convergence is being assumed.

The associativity identity in the text has the correct indices. For fixed nonnegative derivative orders u,v, the coefficient of a·b^(u)·c^(v) in the left-associated triple product is

\[
\binom{i}{u}\binom{i+j-u}{v}.
\]

In the right-associated product it is

\[
\sum_{t=0}^{v}\binom jt
 \binom i{u+v-t}\binom{u+v-t}u.
\]

Factoring the last two binomial factors as binom(i,u)binom(i−u,v−t) gives Vandermonde with j and i−u. The identity remains valid for negative i,j because these generalized binomial coefficients satisfy the same polynomial identity in characteristic zero. Each total coefficient remains a finite sum, so passing from monomials to the formal series is justified.

For a nonzero series with top term a_m p^m, the order of a product is the sum of orders and its leading coefficient is the product of leading coefficients. Thus multiplying by the monomial inverse p^(−m)a_m^(−1) on the left gives 1+R with order(R)≤−1. Powers R^k have order≤−k, so the geometric inverse is coefficientwise well defined and works on both sides. The stated monomial inverse has the correct order. Consequently S is a division ring, not merely a ring of formal expressions.

The injection of K[p;∂q] follows from uniqueness of its polynomial expansion. Its Ore fraction embedding into S uses the standard universal property of localization into a division ring. The identification of that fraction ring with Frac(A1) is consistent with the initial definition: localizing the coefficient polynomial ring to C(q) does not change the generated division ring.

## 2. Centralizer and rational shears

The negative-power commutator is valid. Since q has first derivative1 and all higher derivatives zero, only derivative indices0 and1 occur, giving [p^j,q]=j p^(j−1) for every integer j. Therefore [T,q] has distinct powers with coefficient j a_j. Characteristic zero forces all a_j with j≠0 to vanish. The proof does not require a convergence argument or an unsupported centralizer theorem.

The reverse inclusion C(q)⊂Cent(q) is immediate. An automorphism fixing q fixes every rational function of q because it fixes C pointwise and preserves inverses. Hence the kernel is exactly p↦p+r(q); the inverse shear is r↦−r. Their additive composition law is correct.

## 3. Automorphisms of C(q)

The degree argument is valid over C. A rational self-map of P1 is represented by a coprime homogeneous pair of the same degree. Composing two such pairs introduces no common projective zero: any such zero would map to a common zero of the outer pair. Degrees therefore multiply, and a rational inverse forces degree1. This yields precisely the Möbius functions with nonzero determinant.

No assumption that every automorphism of the full division ring preserves C(q) is inserted at this step.

## 4. Normalizer and surjectivity

Write θ for the Möbius image of q. Then [θ′(q)^(−1)p,θ(q)]=1, with the coefficient on the left as stated. The difference between φ(p) and this expression commutes with θ. Since C(θ)=C(q), commuting with θ implies commuting with q by rational substitution, so the centralizer lemma applies.

Conversely, p↦θ′^(−1)p+r and f(q)↦f(θ(q)) respect the Ore relation by the chain rule. A nonzero order-m polynomial has nonzero leading coefficient f_m(θ)θ′^(−m), establishing injectivity. The proof of surjectivity is complete: q is a rational function of φ(q), and then p=θ′(q)(φ(p)−r(q)) belongs to the image division ring.

## 5. Inverse and composition order

Let ψ=θ^(−1). The proposed inverse has

\[
q\longmapsto\psi(q),\qquad
p\longmapsto\frac1{\psi'(q)}p-
                \frac{r(\psi(q))}{\psi'(q)}.
\]

This is correct, including the position of p. The identities ψ′(θ(q))θ′(q)=1 and θ′(ψ(q))ψ′(q)=1 cancel the leading coefficient in either composition. The remaining rational term cancels exactly. No derivative correction arises because the coefficient remains left of p throughout; moving it to the right would change the expression and require a commutator correction.

As an additional check, the complete pair-composition formula, under the convention (φ∘χ)(x)=φ(χ(x)), is

\[
\phi_{\theta,r}\circ\phi_{\eta,s}
=\phi_{\eta\circ\theta,\;
 r/(\eta'\circ\theta)+s\circ\theta}.
\]

Indeed q maps to η(θ(q)), while the p coefficient is
1/[η′(θ(q))θ′(q)]. This confirms the text’s warning that the order of displayed rational functions is reversed relative to the order of the corresponding substitution automorphisms. Setting r=s=0 proves that the lifts form a section of restriction as a group homomorphism. It would be incorrect to claim the usual functional-composition law θ∘η for those same ordered automorphisms, but the text does not do so.

For conjugation, apply σθ^(−1), then u_r, then σθ. The rational coefficient in σθ^(−1)(p) becomes θ′ after the final substitution. The result is

\[
\sigma_\theta u_r\sigma_\theta^{-1}(p)
=p+\theta'(q)r(\theta(q)),
\]

and q is fixed. Thus the displayed action is correct. It is the θ′ multiplier, not its reciprocal, for this ordering of conjugation.

## 6. Polynomial boundary

PBW uniqueness together with the formal expansion gives A1∩C(q)=C[q]. If an automorphism and its inverse preserve A1, then θ(q) and ψ(q) are polynomials. Their composition is the identity, so their degrees are1. The coefficient θ′ is therefore a nonzero constant a. Subtracting a^(−1)p from φ(p) places r in A1∩C(q), hence r is polynomial.

Conversely, affine θ and polynomial r have affine inverse ψ and polynomial inverse remainder −r(ψ)/ψ′. Both directions preserve A1. This proves equality of the intersection with Aut(A1), not just necessary conditions.

The examples are consistent: p↦p+1/q is a division-ring shear but is excluded by the intersection calculation; θ(q)=−1/q has derivative1/q² and therefore lift p↦q²p, exactly as displayed.

## 7. Remaining scope and editorial observations

The final obstruction is mathematically accurate. Any full automorphism transports the self-centralizing field C(q) to C(φ(q)), but those fields need not coincide. The normalizer computation controls one stabilizer and does not classify its entire orbit. The additional generation condition on a candidate Weyl pair is correctly kept separate from its commutator relation.

No proof correction is required. One optional readability improvement would be to include the pair-composition formula from this review, but the current chain-rule argument and explicit convention already suffice. The integrated occurrence cross-reference and audit-file path should be checked by the parent’s build process; this review has not independently compiled the chapter.

This proof review is independent of the parent’s symbolic tests. Finite tests may detect arithmetic mistakes but do not replace the coefficient-finiteness, associativity, localization, or degree arguments checked here.
