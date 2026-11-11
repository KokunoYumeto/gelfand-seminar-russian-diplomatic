# Independent review of the bounded Weyl-field development

**Reviewer:** early-records agent, independently of the author of the development.  
**Review date:** 9 November 2026.  
**Outcome:** The stated restricted results and their proofs are mathematically sound under the displayed hypotheses. No mathematical correction was required by this review.

The review covered the entire development text and the entire symbolic-check script, with particular attention to the formal-series centralizer, noncommutative signs, inverse and composition formulas, innerness, finite-group averaging, and the limits of the conclusions. The two existing execution logs were also read. I did not perform a redundant third parameter run; the independent contribution here is the written derivation and the code audit.

## Version reviewed

| File | SHA-256 at the time of review |
|---|---|
| GY1965_development.tex | 3473c4523d11b03685ce9f123c6bbd3c7ec76f7c6d9a5b823f1d9a9f443a270e |
| code/check_weyl.py | 89b18ed9491d40df44e59a7bae4598654c7ca389fff775029638c3749f5da8de |

These identify the reviewed mathematical text and code. Later purely editorial changes may change the hashes.

## 1. Formal pseudodifferential series and the centralizer

Let \(K=\mathbb C(x)\), \(\delta=d/dx\), and \([p,x]=1\). For series bounded above in the exponent of \(p\), the coefficient of \(p^\ell\) in a product is well defined. Indeed, if the two upper bounds are \(m,n\), a contribution from \(a_i p^i b_j p^j\) has \(i+j-r=\ell\), \(r\ge0\). Consequently \(i\ge\ell-n\) and \(j\ge\ell-m\), leaving finitely many pairs.

I independently expanded the two bracketings of three monomials. The coefficient of
\[
a\,b^{(r)}c^{(s)}p^{i+j+k-r-s}
\]
in the left bracketing is
\[
\binom{i}{r}\binom{i+j-r}{s}.
\]
In the right bracketing it is
\[
\sum_{t=0}^s\binom{j}{t}
\binom{i}{r+s-t}\binom{r+s-t}{r}.
\]
The identity
\[
\binom{i}{r+s-t}\binom{r+s-t}{r}
=\binom{i}{r}\binom{i-r}{s-t}
\]
followed by generalized Vandermonde proves equality, including negative integer \(i,j\). This uses an identity of generalized binomial coefficients, not division by a binomial coefficient that might vanish. Coefficientwise finiteness extends associativity to the stated series.

A nonzero series has an invertible leading monomial \(a_m p^m\). After factoring it on the left, the remaining factor is \(1+Q\) with order at most \(-1\) for \(Q\). The geometric series is a two-sided formal inverse: the order decreases with each power and every coefficient is therefore a finite sum. This justifies the division-ring construction and the embedding of the Ore quotient. No analytic convergence is being used.

Finally,
\[
[p^j,x]=j p^{j-1}
\]
holds for every integer \(j\), since all derivatives of \(x\) above the first vanish. Thus
\[
\left[\sum_j a_jp^j,x\right]=\sum_j j a_jp^{j-1}.
\]
Uniqueness of the formal expansion and characteristic zero force \(a_j=0\) for every \(j\ne0\). The centralizer is exactly \(K\). There is no unproved assertion here that a rational differential operator has finite order in both directions: the proof deliberately allows its infinite negative-order expansion.

## 2. Stabilizer, chain rule, and inverse

If an automorphism fixing \(\mathbb C\) preserves \(K\), its image \(f=\phi(x)\) is a rational function with a rational compositional inverse. Multiplicativity of degree under composition gives degree one, hence the Möbius form.

The commutator check has the correct order:
\[
\left[\frac1{f'}p,f\right]
=\frac1{f'}[p,f]=1.
\]
The difference \(\phi(p)-f'^{-1}p\) commutes with \(f\), hence with \(\mathbb C(f)=K\), and in particular with \(x\). The centralizer calculation therefore puts the difference in \(K\). This step uses equality \(\mathbb C(f)=K\), not just an inclusion.

For the converse, if \(P=f'^{-1}p+h\), then
\[
[P,a(f)]=f'^{-1}(a(f))'=a'(f),
\]
which is precisely the transformed Ore relation. For \(u=f^{-1}\), the proposed inverse
\[
x\longmapsto u,\qquad
p\longmapsto f'(u)p-f'(u)h(u)
\]
was checked in both orders. For example, applying the forward map to the latter expression gives
\[
f'(x)\bigl(f'(x)^{-1}p+h(x)\bigr)-f'(x)h(x)=p.
\]
All coefficient factors remain on the left, so no hidden differentiation of a moved coefficient is omitted.

The inversion example \(x\mapsto x^{-1}\), \(p\mapsto-x^2p\) is indeed an involution. The Fourier example has the correct sign: \([-x,p]=1\).

## 3. Inner translations and the condition at infinity

If \(T_h=\operatorname{Ad}_u\) fixes \(x\), then \(u\) commutes with \(x\); hence \(u\in K^\times\). From \(pu=up+u'\),
\[
upu^{-1}=p-u'/u.
\]
The negative sign in the criterion is therefore correct.

A nonzero rational function factors as \(C\prod_a(x-a)^{m_a}\), \(m_a\in\mathbb Z\), so its negative logarithmic derivative has only simple finite poles, integral residues, and no polynomial part. Conversely, those three conditions give the finite product with exponent \(-r_a\). The zero function is included and is implemented by \(u=1\).

There is no additional missing global residue restriction. Once the finite residues are integers and the polynomial part vanishes, the residue of \(h(x)\,dx\) at infinity is automatically the negative sum of those residues and hence also integral.

The quotient describing the image of translations in the outer automorphism group is correct as an **abelian-group** quotient. Partial fractions split \(K\) additively into polynomial terms, higher principal parts, and simple-pole coefficients; the logarithmic derivatives form exactly the integral lattice in the last summands. The text correctly warns that \(\mathbb C/\mathbb Z\) is not a complex vector space.

The outer-torsion example is also correct. The class of \(T_{1/(mx)}\) has exact order \(m\), whereas the actual automorphism has infinite order because its positive powers are the distinct nonzero translations \(T_{r/(mx)}\).

## 4. Semidirect action and the finite-group cocycle

There are two translation parameters in the text and code, and they are consistent:
\[
\phi(p)=f'^{-1}p+h,\qquad
T_bL_\sigma(p)=\frac{p+b}{f'},\qquad b=f'h.
\]
Confusing \(b\) with \(h\) would change the composition formula, but neither the proof nor the script makes that error.

Direct conjugation, before invoking group notation, gives
\[
L_\sigma T_bL_\sigma^{-1}(p)=p+f'(x)b(f(x)).
\]
Thus \(R_\sigma b=f'b(f)\). Because automorphisms act by substitution, the coordinate image for \(\sigma\tau\) is \(f_\tau\circ f_\sigma\). The chain rule gives
\[
R_\sigma R_\tau b
=f_\sigma' f_\tau'(f_\sigma)b(f_\tau(f_\sigma))
=R_{\sigma\tau}b.
\]
The multiplication law in the manuscript follows.

For finite \(H\), the kernel of restriction is contained in the torsion-free additive translation group, so restriction is injective. The cocycle equation
\[
b_{\sigma\tau}=b_\sigma+R_\sigma b_\tau
\]
then has the averaging solution \(b_\sigma=a-R_\sigma a\), where \(a=|Q|^{-1}\sum_\tau b_\tau\). Summing over \(\tau\) is legitimate because left multiplication permutes the finite group. Substitution into the conjugation formula gives
\[
T_{-a}(T_{b_\sigma}L_\sigma)T_a=L_\sigma.
\]
Both the sign and the side of the conjugation are correct.

The result concerns finite groups **inside the selected rational-subfield stabilizer**. It does not prove that every finite subgroup of the full Weyl-field automorphism group stabilizes a conjugate rational subfield. The text explicitly preserves this limitation. It also correctly keeps separate the further issue of whether the conjugating translation is inner.

## 5. Symbolic-code audit and existing executions

The multiplication routine implements the finite differential-operator identity
\[
(a_i p^i)(b_jp^j)=
\sum_{r=0}^{i}\binom{i}{r}a_i b_j^{(r)}p^{i-r+j}
\]
for nonnegative integer powers. All test inputs satisfy that restriction. It does not purport to implement the full formal Laurent-series division ring used in the centralizer proof.

The transformation routine substitutes coefficients and then raises the transformed \(p\) using this multiplication. The inverse-pair formula in the code is the \(b\)-parameter version of the inverse above:
\[
c(x)=-\,\frac{b(u(x))}{f'(u(x))}.
\]
The independent action on ordinary monomials does not call the multiplication routine and checks the commutator directly by differentiation. The wrong-sign and missing-chain-rule negative controls detect the intended errors.

The finite \(C_2\) example uses \(f=-x\), \(a=(x^2-1)^{-1}\), \(b=2a\). Since \(R_\sigma a=-a\), its square is the identity and the stated average removes the translation. This was checked algebraically in addition to inspecting the code.

The PBW recurrence counts exponent tuples by exact degree after adjoining each variable, then sums through the cutoff. It includes zero variables and degree cutoff zero. Comparison with \(\binom{N+2n+k}{2n+k}\) is correct as a counting check; it assumes, rather than proves by computation, the relevant PBW basis.

The two retained execution logs, with seeds **1965** and **20261109**, each report:

| Check | Passing instances per run |
|---|---:|
| Commutators | 60 |
| Inverses | 60 |
| Composition | 40 |
| Independent monomial action | 300 |
| Finite-group identities | 2 |
| PBW counts | 175 |
| Logarithmic-derivative implementers | 3 |

Both negative controls passed by rejecting the deliberately wrong identities. These are finite algebraic checks and do not replace the written universal proofs.

One harmless comment in the script calls the explicit \(C_2\) example “from the text,” although the main prose only presents the general cocycle result. It may be changed to “an explicit \(C_2\) cocycle” for editorial precision; no code or mathematical behavior depends on it.

## Scope and attribution

The development expressly credits the known rational-subfield stabilizer and uses “proved here” to mark the supplied proof, not mathematical priority. This review independently checks the proofs and their bounded scope; it is not a new exhaustive literature search for the full automorphism group. The text's dated “no later classification found in the search” language is appropriately weaker than a proof of nonexistence of such literature.
