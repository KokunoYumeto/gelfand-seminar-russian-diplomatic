# Independent review of the KP normalization development

Date: **10 November 2026**. Reviewed the newly appended KP subsection in `work/parts/root/development.tex`, together with `work/code/check_kp.py` and `work/code/output/kp_checks.json`. No root file was edited. This review checks the written local proof and its computational support; it does not independently re-audit the complete classification theorem in Krichever's paper.

## Verdict

**The local distinct-pole equivalence, the general-N Poisson-commutation proof and the commutator/time convention are correct.** The rational-function converse does not lose an additional condition at infinity. The proof is appropriately limited to the displayed finite pole ansatz and to local evolution away from collisions.

Two minor editorial changes were reported to the parent:

- In the displayed fourth-order Laurent coefficient, replace `q_{i,y}^{,2}` by `q_{i,y}^{\,2}`.
- Say that the scalar coefficient in M cannot **in general** be the same u as in L. Particular solutions, such as constant u, can satisfy that identification; the failure concerns a general Lax formula.

Neither point changes the propositions or their proof.

## 1. Complete principal-part calculation

Fix a parameter point and a pole i, and write s=x−q_i. Pairwise distinctness makes the contribution from all other poles analytic in s:

\[
u=-2s^{-2}+R(s),\qquad R=R_0+R_1s+R_2s^2+R_3s^3+\cdots.
\]

The singular parameter derivatives are

\[
u_t=-4q_{i,t}s^{-3}+\text{analytic},\qquad
u_{yy}=-4q_{i,yy}s^{-3}-12q_{i,y}^{2}s^{-4}+\text{analytic}.
\]

The analytic remainder stays analytic under the parameter derivatives: locally the other pole locations remain separated from q_i. Rewriting that remainder in the moving coordinate does not create a negative power.

Directly in the x-coordinate,

\[
6(uu_x)_x+u_{xxxx}
=-72R,s^{-4}+48R'\,s^{-3}-12R''\,s^{-2}
  +\text{analytic}.
\]

Here the two sixth-order contributions cancel. For R_m s^m, the indicated coefficient of s^(m−4) is

\[
-72+48m-12m(m-1)=-12(m-2)(m-3).
\]

Therefore m=2 and m=3 give zero. This explicitly verifies the absence of second- and first-order principal parts; it is not assumed merely because the fourth- and third-order terms were computed. There is also no fifth-order term.

Consequently the complete remaining principal part of the PDE is

\[
\bigl(48q_{i,t}-72R_0-36q_{i,y}^{2}\bigr)s^{-4}
+\bigl(-24R_1-12q_{i,yy}\bigr)s^{-3}.
\]

For the other poles,

\[
R_0=-2\sum_{j\ne i}(q_i-q_j)^{-2},\qquad
R_1=4\sum_{j\ne i}(q_i-q_j)^{-3}.
\]

Their substitution gives precisely the two equations (K1), with coefficients −8, 3/4 and −3 as printed. Thus both necessity and the claimed list of possible finite principal parts are verified.

## 2. Why the converse at infinity is sufficient

At a fixed parameter point the PDE residual is a rational function of x. Its only possible finite poles are the finitely many q_i. Under (K1), the complete calculation above removes every principal part at every such point. The residual is therefore a polynomial.

There is no unaccounted polynomial contribution at infinity. For the stated finite pole ansatz,

\[
u=O(x^{-2}),\quad u_t=O(x^{-3}),\quad
u_{yy}=O(x^{-3}),\quad u_{xxxx}=O(x^{-6}),\quad
(uu_x)_x=O(x^{-6}).
\]

Hence the PDE residual is O(x^−3) and tends to zero as x tends to infinity. A polynomial with that behavior is identically zero. Uniformity over the whole parameter domain is unnecessary: the argument is pointwise in parameters, and the hypothesis gives the required derivatives there.

This proof would need adjustment if one allowed a polynomial background, infinitely many poles, a varying number of poles or collisions. None of those is included in the proposition. There is no integration in x in this argument, so no arbitrary x-independent forcing term has been silently dropped. The separate Lax-operator integration issue is handled below.

## 3. General-N canonical Poisson bracket

On the distinct-position locus, put d_ij=q_i−q_j. The four required gradients are

\[
H_{p_i}=p_i,\qquad
H_{q_i}=8\sum_{j\ne i}d_{ij}^{-3},
\]

\[
K_{p_i}=\frac34p_i^2-3\sum_{k\ne i}d_{ik}^{-2},\qquad
K_{q_i}=6\sum_{j\ne i}(p_i+p_j)d_{ij}^{-3}.
\]

These formulas follow directly from the unordered-pair sums in (K2). In particular, the signs from differentiating with respect to the second index of a pair are already incorporated by d_ji=−d_ij.

Using the stated canonical convention,

\[
\{H,K\}=\sum_i(H_{q_i}K_{p_i}-H_{p_i}K_{q_i}),
\]

the p_i² terms cancel exactly. The remaining momentum-dependent contribution is

\[
-6\sum_{i\ne j}p_i p_j d_{ij}^{-3}=0,
\]

because the summands for (i,j) and (j,i) have opposite signs. The sole residual expression is the triple sum printed in the proof:

\[
-24\sum_i\sum_{j\ne i}\sum_{k\ne i}
d_{ij}^{-3}d_{ik}^{-2}.
\]

When j=k, each summand is d_ij^−5; exchanging i and j cancels those terms. For three distinct indices, each unordered triple occurs in exactly six ordered summands. No factor is lost by grouping this way.

For one unordered triple, set

\[
a=q_i-q_j,\quad b=q_j-q_k,\quad c=q_k-q_i,
\qquad a+b+c=0.
\]

The complete six-term contribution, before multiplication by −24, is

\[
T=\frac{c-a}{a^3c^3}
 +\frac{a-b}{a^3b^3}
 +\frac{b-c}{b^3c^3}.
\]

Multiplication by the nonzero denominator a³b³c³ gives

\[
a^3(b-c)+b^3(c-a)+c^3(a-b).
\]

This is the exact numerator in the development. It factors as

\[
(a+b+c)(a-b)(a-c)(b-c),
\]

and therefore vanishes. This establishes the Poisson identity for arbitrary finite N; it is not inferred from the numerical checks at small N. The distinct-position hypothesis is exactly what permits the denominator manipulations.

## 4. Flow compatibility and what is actually constructed

Hamilton's equations for H give q_(i,y)=p_i and p_(i,y)=−8Σ_(j≠i)d_ij^−3. Hamilton's equations for K give q_(i,t)=3p_i²/4−3Σ_(j≠i)d_ij^−2. These are the two required equations (K1) after eliminating p.

The vanishing Poisson bracket implies that the two Hamiltonian vector fields commute. On the open locus of distinct positions they are smooth, so their local flows exist and commute. Starting from any phase point in that locus gives a sufficiently small two-parameter family on which the poles remain distinct. Substitution into the first proposition yields a meromorphic-in-x KP solution on that local parameter domain.

The argument does not assert global completeness of either flow, continuation through collisions, regularity on the entire real x-axis when real poles are present, or classification of all rational KP solutions. The written scope statement properly excludes those stronger conclusions.

## 5. Differential-operator commutator and time convention

For D=∂_x, L=D²+u and M=D³+(3/2)uD+w, direct use of the Leibniz rule gives

\[
[L,M]=\left(2w_x-\frac32u_{xx}\right)D
+w_{xx}-u_{xxx}-\frac32uu_x.
\]

For the development's operator pair,

\[
[\partial_y-L,\partial_t+M]=M_y+L_t-[L,M].
\]

Its D coefficient is (3/2)(u_y+u_xx)−2w_x, so the stated equation w_x=3(u_xx+u_y)/4 is correct. The scalar coefficient is

\[
F=u_t+w_y-w_{xx}+u_{xxx}+\frac32uu_x.
\]

Using the D-coefficient equation,

\[
4F_x=4u_{tx}+3u_{yy}+u_{xxxx}+6(uu_x)_x,
\]

which is exactly the notebook PDE. Conversely, if that PDE holds and w_0 is any local primitive of the specified w_x, then F_x=0, so F=C(y,t). Replacing w_0 by w_0+h(y,t) changes F to F+h_y. Choosing h_y=−C locally makes the full scalar coefficient vanish. This justifies the integration-function sentence in the development. Global boundary or periodicity requirements may obstruct a globally preferred choice and are correctly left separate.

For the alternative pair with ∂_t−M, the scalar equation becomes

\[
u_t-w_y+w_{xx}-u_{xxx}-\frac32uu_x=0.
\]

After differentiation and elimination, it gives

\[
3u_{yy}+(-4u_t+6uu_x+u_{xxx})_x=0.
\]

Thus t↦−t converts this convention to the development's displayed PDE. The sign explanation is correct.

## 6. Computational support and its limits

The inspected script computes the two leading Laurent coefficients symbolically, forms operator products by the Leibniz rule, and checks the minus/minus commutator convention and its time reversal. Its recorded signs agree with the independent calculations above.

For the Poisson identity, it separately checks the three-difference polynomial symbolically and differentiates the complete Hamiltonians directly. It simplifies the full bracket identically for N=2,3 and evaluates it at20 exact distinct-position samples for each of N=2,3,4, with a declared deterministic seed. These are useful verification checks, but the general-N conclusion rests on the written six-term triple cancellation, which has been independently verified here.

The script explicitly asserts the fourth- and third-order Laurent coefficients; it does not separately assert all the absent negative powers. The complete principal-part calculation in §1 of this review supplies that independent check. The development's proof already states the cancellation correctly, so this is an explanation of evidence strength rather than a flaw in its argument.

**Recommendation:** retain the propositions and proof, making only the two minor editorial fixes listed at the start.
