# Independent mathematical checks

**Reviewer:** child agent `/root/records_259_288`.  
**Date:** 9 November 2026.  
**Inputs read:** the final statements and reconstructions of items 1971-233.1, 1971-233.8, 1971-235.1–2 in `work/a/items.json`; item 1971-261.3 in `work/c/items.json`; the root’s exact-integer Dyson implementation and its reported outputs. This review checks the editorial mathematics independently. It does not upgrade publication matches or verification levels for historical references.

## 1. Critical-exponent compactness: item 1971-233.8

### Hypotheses and definition

Let (E) be a finite-dimensional real or complex normed space. Let (r\geq1) be an integer and (0\leq\rho<1). Write (r_{\mathrm{sp}}(T)) for the spectral radius, to distinguish it from the integer exponent. The preceding occurrence defines (q(E)) as the least positive integer (q) for which every contraction (T) with (\|T^q\|=1) has (r_{\mathrm{sp}}(T)=1), or (q(E)=\infty) if no such integer exists.

Define

\[
\mathcal A_\rho=\{T\in\operatorname{End}(E):\|T\|\leq1,\quad r_{\mathrm{sp}}(T)\leq\rho\},
\qquad
C(E,r,\rho)=\max_{T\in\mathcal A_\rho}\|T^r\|.
\]

### Independent derivation

The space (\operatorname{End}(E)) is finite dimensional. Its closed operator-norm unit ball is compact. The spectral radius is continuous in finite dimension: the coefficients of the characteristic polynomial depend continuously on the matrix entries, and the finite multiset of roots varies continuously, with multiplicity, as a multiset. For real matrices this statement is applied to the complexified characteristic polynomial. Therefore (\mathcal A_\rho) is a closed subset of a compact set. It is nonempty because it contains the zero operator. The map (T\mapsto\|T^r\|) is continuous, so its maximum is attained.

Suppose (q=q(E)<\infty) and (r\geq q). Every contraction satisfies

\[
\|T^r\|\leq\|T^q\|\,\|T^{r-q}\|\leq\|T^q\|\leq1.
\]

If the attained maximum were 1, a maximizing (T\in\mathcal A_\rho) would satisfy (\|T^q\|=1). By the defining property of (q(E)), its spectral radius would be 1, contradicting (r_{\mathrm{sp}}(T)\leq\rho<1). Hence (C(E,r,\rho)<1).

Conversely, let (r<q(E)), including the case (q(E)=\infty). The defining property fails at exponent (r). Thus there is a contraction (T) with (\|T^r\|=1) and spectral radius different from 1. Since (r_{\mathrm{sp}}(T)\leq\|T\|\leq1), this means (r_{\mathrm{sp}}(T)<1). Choose any (\rho\in[r_{\mathrm{sp}}(T),1)). Then (T\in\mathcal A_\rho), so (C(E,r,\rho)\geq1); contractivity gives the reverse inequality. Therefore the maximum is exactly 1.

### Boundary cases

- In dimension one, every operator is multiplication by a scalar. Consequently (q(E)=1) and (C(E,r,\rho)=\rho^r) for every (r\geq1), including (\rho=0). There is no predecessor case (r<q(E)) within the stated positive-exponent domain.
- Allowing (\rho=0) is harmless: the admissible set consists of nilpotent contractions in finite dimension and still contains zero. The proof requires no division by (\rho).
- The equality case in the converse permits a nilpotent witness. If the original notebook requires (0<\rho<1), replace a zero spectral-radius bound by any positive number less than 1.
- For (q(E)=\infty), the converse works separately for every positive (r). It does not assert that a single operator works for all (r).
- The zero-dimensional space, if admitted, is vacuous: (q(E)=1), all power norms are zero, and the strict inequality still holds under the usual zero-operator convention.

**Finding:** the statement and proof are correct. Finite dimension, a fixed (\rho<1), and attainment are essential to the uniform strict inequality. This check supplies no exact value of (C) for arbitrary norms and does not establish a general classification of maximizers.

## 2. Affine finite-field Radon inversion: item 1971-235.1

Let (q) be a prime power, (n\geq1), (V=\mathbb F_q^n), and let (\mathcal H) be the set of affine hyperplanes. Functions take values in (\mathbb C). The transform is

\[
Rf(H)=\sum_{x\in H}f(x).
\]

There are

\[
a=\frac{q^n-1}{q-1}
\]

linear hyperplane directions: each is the kernel of a nonzero linear functional, and exactly (q-1) scalar multiples have the same kernel. Every direction contributes exactly one affine hyperplane through a prescribed point (x). Therefore exactly (a) hyperplanes contain (x).

For distinct (x,y), an affine hyperplane of direction (\ker\ell) contains both precisely when (\ell(x-y)=0). Such nonzero functionals form the punctured ((n-1))-dimensional annihilator of (x-y). Thus the number through both points is

\[
b=\frac{q^{n-1}-1}{q-1}.
\]

Writing (C=\sum_{y\in V}f(y)) and interchanging two finite sums gives

\[
\begin{aligned}
\sum_{H\ni x}Rf(H)
&=a f(x)+b\sum_{y\ne x}f(y)\\
&=(a-b)f(x)+bC\\
&=q^{n-1}f(x)+bC.
\end{aligned}
\]

Since the values lie in characteristic zero, division by (q^{n-1}) is valid. This is exactly the stated inversion formula. Its apparently external constant (C) is recoverable from the data: the hyperplanes in any one parallel class partition (V), so their transformed values sum to (C).

For (n=1), hyperplanes are single points, (a=1), (b=0), and (R) is the identity. The formula remains valid. The hypothesis (n\geq1) avoids an empty, ill-defined hyperplane setting in dimension zero. No claim is made for function-value fields of characteristic dividing (q).

**Finding:** all incidence coefficients and the inversion formula are correct, including the smallest dimension and (q=2).

## 3. Affine Radon range: item 1971-235.2

### Check of the submitted dimension argument

The (a) parallel classes are disjoint blocks of (q) hyperplanes each, so the space of all hyperplane data has dimension (aq). Fix one reference class. Equality of every other class sum with the reference sum gives (a-1) independent linear equations: in a linear relation among these equations, looking at a coordinate in any nonreference block forces its corresponding coefficient to vanish. Their common solution space therefore has dimension

\[
aq-(a-1)=a(q-1)+1=q^n.
\]

The image of (R) satisfies these equations because a parallel class partitions (V). The inversion above makes (R) injective, so its image has dimension (q^n), equal to the entire constraint space. Necessity and sufficiency both follow.

When (n=1), (a=1); there are zero constraints and all data are in the range, exactly as required by (R=I).

### Second derivation, independent of dimension counting

Suppose (n\geq2) and data (\varphi:\mathcal H\to\mathbb C) have the same class sum (C) in every parallel direction. Define

\[
f(x)=q^{1-n}\left(\sum_{K\ni x}\varphi(K)-bC\right).
\]

Fix an affine hyperplane (H). It contains (q^{n-1}) points. Its intersection with a different parallel hyperplane is empty, while its intersection with a hyperplane of a different direction contains (q^{n-2}) points. Hence

\[
\sum_{x\in H}\sum_{K\ni x}\varphi(K)
=q^{n-1}\varphi(H)+q^{n-2}(a-1)C.
\]

The identity (a-1=qb) now yields

\[
\begin{aligned}
Rf(H)
&=q^{1-n}\bigl(q^{n-1}\varphi(H)+q^{n-2}(a-1)C-q^{n-1}bC\bigr)\\
&=\varphi(H).
\end{aligned}
\]

Dimension one was handled separately; the intersection count (q^{n-2}) is not applied there. This direct reconstruction independently confirms the range assertion.

**Finding:** the submitted proof passes, and the second proof reaches the same conclusion without using rank or dimension equality.

## 4. Algebraic quotient spectrum: item 1971-261.3

Let (A=T-\lambda I\) be bounded on an infinite-dimensional Hilbert space (\mathcal H). Its coset in (\mathcal B(\mathcal H)/\mathcal S_1\) is invertible exactly when a bounded (S) satisfies

\[
I-SA\in\mathcal S_1,\qquad I-AS\in\mathcal S_1.
\]

### A Fredholm operator gives an inverse modulo trace class

If (A) is Fredholm, its kernel (N) and cokernel (M=(\operatorname{ran}A)^\perp) are finite dimensional and its range is closed. The restriction

\[
A:N^\perp\longrightarrow\operatorname{ran}A
\]

is a bounded bijection with bounded inverse. Let (S) be that inverse on the range and zero on (M). Then

\[
SA=I-P_N,\qquad AS=I-P_M.
\]

Both errors are finite rank and therefore trace class. Thus the coset of (A) is invertible.

### An inverse modulo trace class gives Fredholmness

Conversely, put (K=I-SA) and (L=I-AS), which are compact because they are trace class. On \(\ker A\), the compact operator (K) is the identity; therefore \(\ker A\) is finite dimensional.

To check closed range without simply citing the Fredholm criterion, suppose (A) were not bounded below on ((\ker A)^\perp). There would be unit vectors (x_j\) in that subspace with (Ax_j\to0). Passing to a subsequence, compactness makes (Kx_j) converge. But (x_j=SAx_j+Kx_j), so (x_j) also converges to a unit vector (x\in(\ker A)^\perp) satisfying (Ax=0), a contradiction. Thus the range is closed. Applying the same kernel argument to (A^*), using (S^*A^*=I-L^*), proves that the cokernel is finite dimensional. Hence (A) is Fredholm.

The two arguments establish that the algebraic coset spectrum is exactly the Fredholm essential spectrum. The trace-class ideal need not be closed in the operator norm; no Banach-algebra quotient is used.

**Small-space convention:** on a finite-dimensional Hilbert space the trace-class ideal is the whole operator algebra. Every operator is Fredholm, so the essential spectrum is empty. The quotient is the zero algebra, whose spectrum is likewise empty if it is treated as a unital algebra with (0=1). To avoid that convention in the chapter’s wording, it is cleaner to state the quotient claim for an infinite-dimensional Hilbert space. The chapter’s statement and authoring source now explicitly impose infinite dimension, as requested by the root; the mathematical assertion is otherwise unchanged.

## 5. Previously completed independent Dyson review

The root’s `GY1971/code/check_dyson.py` was inspected independently. The residue order ((1,2,3,4,0)), deduction (e=-(a+b+c+d)), bound (\lfloor\sqrt{10N}\rfloor), denominator (1!2!3!4!=288), and labelled-coordinate convention agree with the notebook formula. No additional (5!) divisor is permitted. The ten-factor Vandermonde has even total sign under reversal of all difference orientations. The leading (q) in the Euler product is essential.

The Euler-product expansion, divisor-sum recurrence and complete residue-lattice enumeration agree for (1\leq n\leq100). This is finite computational verification; the all-(n) identity remains a cited literature result. The first twelve coefficients and the missing-constant-term diagnosis are recorded in `research_log.md`. No additional computation was needed to resolve an outstanding risk.

## Review conclusion

The requested compactness and finite-Radon editorial results pass independent proof checks, including their boundary cases. The Radon range result also passes a distinct direct-reconstruction proof. The quotient-spectrum argument passes in both directions, with only the harmless finite-dimensional zero-algebra convention noted above. No change to a mathematical conclusion, no new open problem, and no additional classification claim follows from this audit.
