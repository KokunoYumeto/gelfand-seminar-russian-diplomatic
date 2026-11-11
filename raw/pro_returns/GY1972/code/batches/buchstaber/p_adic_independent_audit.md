# Independent review of parent record 299

Reviewer: Buchstaber-series agent. Date: 2026-11-09. Parent items 1972-299.11–.14 were read after they were saved. This file records an independent mathematical check, not an additional occurrence or a literature-source claim.

## Coset definition and finite additivity

Assume P is periodic with period one and satisfies

\[
\sum_{j=0}^{p-1}P((x+j)/p)=a_pP(x)-cP(px),\qquad c=p^{w-2},
\]

and alpha is a nonzero root of alpha²−a_p alpha+p^{w−1}=0. Put

\[
\mu_m(a)=\alpha^{-m}P(a/p^m)-c\alpha^{-m-1}P(a/p^{m-1}),\qquad m\ge1.
\]

Replacing a by a+kp^m changes the two P arguments by the integers k and kp, so the value depends only on the coset. Write P_m=P(a/p^m). Directly summing children gives

\[
\begin{aligned}
\sum_{j=0}^{p-1}\mu_{m+1}(a+jp^m)
 &=\alpha^{-m-1}(a_pP_m-cP_{m-1})
   -pc\alpha^{-m-2}P_m\\
 &=\alpha^{-m-2}(a_p\alpha-p^{w-1})P_m
   -c\alpha^{-m-1}P_{m-1}\\
 &=\alpha^{-m}P_m-c\alpha^{-m-1}P_{m-1}=mu_m(a).
\end{aligned}
\]

The second sum uses periodicity P(a/p^m+j)=P_m. The root identity is exactly the one required; no additional p factor is missing. When w≥2, alpha is a p-adic unit, and P takes values in a fixed valuation ring, the formula is uniformly bounded. Defining the level-zero mass by the sum of level-one masses is consistent.

## Primitive-character cancellation

Let chi have exact conductor q=p^r and be nontrivial. For r≥2, group residues a modulo p^r by a modulo p^{r−1}. The value P(a/p^{r−1}) is constant on each fibre, while the sum of chi or chi^{-1} over each fibre is zero: primitivity means the character is nontrivial on the last principal-unit kernel. For r=1, P(a)=P(0) and the sum of a nontrivial conductor-p character over the units is zero. Thus

\[
\int_{\mathbb Z_p^\times}\chi^{-1}\,d\mu
=\alpha^{-r}\sum_{a\bmod q}\chi^{-1}(a)P(a/q).
\]

Character values at nonunits are zero. This check covers the r=1 endpoint rather than assuming every fibre is a nontrivial principal-unit coset.

## Parity and interpolation constant

For real Fourier coefficients, f(−conjugate(z))=conjugate(f(z)). Reflecting the cusp-to-cusp path in J(x)=integral from 0 to x gives

\[
J(-x)=-\overline{J(x)}.
\]

Consequently Re J is odd and Im J is even. Pairing a and −a shows the notebook's real component has zero pairing with every even character. This confirms parent 299.11.

For the corrected convention

\[
I(x)=\int_x^{i\infty} f(z)\,dz,
\qquad P(x)=\frac{I(x)+I(-x)}{2\Omega_+},
\]

parametrize z=a/q+it. Then I(a/q)=i integral from 0 to infinity of f(a/q+it)dt. The finite Gauss identity gives, for every t>0,

\[
\sum_a\chi^{-1}(a)f(a/q+it)
=\tau(\chi^{-1})\sum_{n\ge1}a_n\chi(n)e^{-2\pi nt}.
\]

The cusp integrals converge at both ends; the Mellin integral identifies their value with L(f,chi,1)/(2 pi). Therefore

\[
\sum_a\chi^{-1}(a)I(a/q)
=\frac{i\tau(\chi^{-1})}{2\pi}L(f,\chi,1).
\]

For even chi, substitution a to −a shows that the I(−a/q) sum equals the I(a/q) sum. The factor two cancels the denominator two in P. Hence the exact prefactor in parent 299.14 is correct:

\[
\int\chi^{-1}\,d\mu
=\alpha^{-r}\frac{i\tau(\chi^{-1})}{2\pi\Omega_+}L(f,\chi,1).
\]

The complex expression is interpreted through the stated algebraic period normalization before a p-adic embedding is applied. It is essential to use the Mellin-integral justification rather than claim unregularized convergence of the Dirichlet series at s=1 in arbitrary higher weight. Parent 299.14 already uses the correct Mellin wording.

## Review conclusion

Finite additivity, well-defined coset values, primitive-character cancellation, real/imaginary parity, and the i/(2 pi Omega_+) prefactor all agree with the saved parent items under their stated hypotheses. These checks were communicated to the parent. The historical Hecke-period identity and algebraicity hypotheses are supplied by the parent's verified Manin source; this independent audit does not assert a separate reading of that paper.
