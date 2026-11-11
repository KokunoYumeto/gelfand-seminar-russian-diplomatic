# Independent review of GP-1966-09

Reviewer: the PDE/statistical-physics slice agent, independently of the author of the development. Date: 9 November 2026.

Scope: the version of GY1966_development.tex inspected during this review; root items 1966-100.2–1966-100.12; the source transcription at P000151 and P000154–P000157; direct inspection of the P000151 scan; and the opened English primary text of Minlos (1968), printed pp. 139–142 and 158–164.

## Verdict

The conditional variance theorem is correct with exactly the stated coefficients. The ordered-pair convention, evenness of the real kernel, uniformity of constants in volume, absolute integrability, and separate requirement for convergence of the mean are all necessary qualifications and are present in the inspected development. The ideal-gas and hard-core counterexamples are valid. The canonical finite-volume correction and the order-dependent effective-volume calculation are also correct.

One definite historical wording correction is required: printed p. 164 **Problem 3** asks for precise inequalities in the proofs of (3.27) and (3.28). The exponential estimate (3.29) belongs to the **separate following Remark 1**, not to that problem's wording. Both places in the inspected development attributing an exponential-estimate request to Problem 3 should be changed accordingly.

The truncation proof can be strengthened to centered convergence in \(L^1\), with one short additional estimate given below. This strengthening does not require any additional correlation hypotheses.

The Class C designation needs a qualification: the historical correlation programme is partly developed, but its undeclared exceptional parameter set does not specify one precise presently open theorem. The completed conditional estimate must not itself be presented as an open problem.

## 1. Conventions and exact collision expansion

For a simple point process in a bounded measurable vessel \(\Omega\), let \(V=|\Omega|\in(0,\infty)\), and use ordered factorial moment densities:
\[
\mathbb E\sum_{i_1,\ldots,i_k\ \mathrm{distinct}}
h(X_{i_1},\ldots,X_{i_k})
=\int_{\Omega^k}h\,r_k.
\]
Assume a finite number of points almost surely. Let \(f\) be real and even and put
\[
F=\sum_{i\ne j} f(X_i-X_j),\qquad f_{ij}=f(x_i-x_j).
\]

Re-expanding the two ordered sums independently gives three disjoint types of terms.

1. Two labels: for each first ordered pair, the second pair is either that pair or its reversal. Evenness gives \(2\sum_{i\ne j}f_{ij}^2\).
2. Three labels: the shared label can occupy either coordinate of each pair, giving four terms. Relabelling and evenness identify their sums with \(4\sum_{i,j,k\ {\rm distinct}}f_{ij}f_{jk}\).
3. Four labels: each pair of ordered pairs already corresponds to one ordered quadruple, giving coefficient one.

After integration and subtraction of the square of the expectation,
\[
\operatorname{Var}F
=2\int_{\Omega^2}f_{12}^{\,2}r_2
+4\int_{\Omega^3}f_{12}f_{23}r_3
+\int_{\Omega^4}f_{12}f_{34}B_{12;34},
\]
where
\[
B_{12;34}=r_4(x_1,x_2,x_3,x_4)
-r_2(x_1,x_2)r_2(x_3,x_4).
\]
These coefficients are correct also for configurations with fewer than four points: the corresponding distinct-tuple sums are empty. The object \(B_{12;34}\) is the disjoint-pair covariance density, not the fourth factorial cumulant.

## 2. Independent derivation of the constants

Assume almost everywhere
\[
0\le r_2\le C_2,\qquad 0\le r_3\le C_3,
\]
\[
|B_{12;34}|
\le C_4\{g(x_1-x_3)+g(x_1-x_4)+g(x_2-x_3)+g(x_2-x_4)\}
+\frac{C_0}{V},
\]
where \(g\ge0\), \(g\in L^1(\mathbb R^d)\), and the constants are nonnegative. For a sequence of vessels, the same \(g\) and constants must work uniformly.

For \(f\in L^1\cap L^2\), the two-label integral is at most
\[
2C_2\int_\Omega dx_1\int_{\mathbb R^d}|f(z)|^2\,dz
=2C_2V\|f\|_2^2.
\]
Integrating \(x_1\) and \(x_3\) first with \(x_2\) fixed bounds the absolute three-label integral by
\[
4C_3V\|f\|_1^2.
\]

For example, the cross term \(g(x_1-x_3)\) obeys
\[
\begin{split}
&\int_{\Omega^4}|f(x_1-x_2)||f(x_3-x_4)|g(x_1-x_3)\,dx_1\cdots dx_4\\
&\quad\le \|f\|_1^2\int_{\Omega^2}g(x_1-x_3)\,dx_1dx_3
\le V\|f\|_1^2\|g\|_1.
\end{split}
\]
The other three cross terms have the same bound by relabelling. Finally,
\[
\frac{C_0}{V}\int_{\Omega^4}|f_{12}f_{34}|
\le\frac{C_0}{V}(V\|f\|_1)^2
=C_0V\|f\|_1^2.
\]
Thus
\[
\boxed{\operatorname{Var}F\le
V\left[2C_2\|f\|_2^2+
(4C_3+4C_4\|g\|_1+C_0)\|f\|_1^2\right].}
\]
No sign of \(f\) was used. No translation invariance, vessel boundary estimate, or Gibbs property is required for this implication.

The proof's integrability justification is sound: the unsubtracted fourth-order term has, besides the controlled \(B_{12;34}\) contribution, a term bounded by \(C_2^2V^2\|f\|_1^2\). Hence the exact variance identity can be applied without a hidden exchange of divergent signed integrals.

The conclusion is \(O(V)\). Neither a limiting coefficient nor its positivity follows from these assumptions. With deterministic \(N/V\to\rho\in(0,\infty)\), it is also \(O(N)\).

## 3. Truncation and the stronger centered \(L^1\) conclusion

Set \(f_M=f\,\mathbf1_{\{|f|\le M\}}\). Then \(\|f_M\|_2^2\le M\|f\|_1\), and \(\|f-f_M\|_1\to0\). The factorial two-point formula gives
\[
\mathbb E|F(f)-F(f_M)|\le C_2V\|f-f_M\|_1.
\]
Centering the remainder costs at most a factor two. By Cauchy–Schwarz on the centered truncated statistic,
\[
\boxed{
\frac{\mathbb E|F(f)-\mathbb EF(f)|}{V}
\le\sqrt{\frac{K(f_M)}{V}}+2C_2\|f-f_M\|_1,
}
\]
where \(K\) is the bracketed constant in the variance theorem. First let \(V\to\infty\) with \(M\) fixed, and then let \(M\to\infty\). This proves centered convergence in \(L^1\), and therefore in probability.

The development's more explicit probability inequality is also correct:
\[
\mathbb P\{|F-\mathbb EF|>\epsilon V\}
\le \frac{4K(f_M)}{\epsilon^2V}
+\frac{4C_2}{\epsilon}\|f-f_M\|_1.
\]
The second coefficient is four because centering costs two and the union-bound threshold is \(\epsilon/2\).

Neither assertion proves convergence of \(\mathbb EF/V\). The separate sufficient condition involving averaged two-point densities \(A_n(z)\) is correct: \(0\le A_n\le C_2\), almost-everywhere convergence, and \(f\in L^1\) give the mean limit by dominated convergence. Combined with the displayed stronger estimate, the resulting convergence to the limiting constant is also in \(L^1\).

## 4. Counterexamples and historical admissibility

### Ideal gas

For \(N\ge2\) independent uniform points in \([0,L]^d\), \(L>2\), the canonical factorial density is \(r_2=(N)_2/V^2>0\). The function
\[
f(z)=|z|^{-\alpha}\mathbf1_{\{0<|z|<1\}},
\qquad d/2\le\alpha<d,
\]
is nonnegative, even, in \(L^1\), and outside \(L^2\). Restricting the first point to \([1,L-1]^d\) leaves a full unit ball of admissible differences. Thus the integral of \(r_2f^2\) is infinite, while the first moment is finite. Since every summand is nonnegative, the second moment of \(F\), and hence its variance, is infinite.

This example remains available along a fixed-density thermodynamic sequence; the later canonical calculation verifies uniform correlation bounds of the proposed form. It disproves the claimed finite variance under \(L^1\) alone, not the repaired centered law of large numbers.

The P000151 scan explicitly describes hard spheres as a case considered sometimes and allows a potential defined either for \(r>0\) or for \(r>\delta\). The published account also distinguishes these two settings (Minlos, 1968, pp. 139–140). Thus a hard core is not universally imposed by the source setup.

### Positive hard core

Let \(a>0\) denote the **excluded pair distance**, with potential \(+\infty\) for \(r<a\) and zero for \(r>a\). In a cube of side \(L>6a\), the two-particle canonical partition function is finite and positive. Its two-point factorial density is a positive constant on allowed pairs.

Use
\[
f(z)=\bigl||z|-2a\bigr|^{-3/4}
\mathbf1_{\{0<||z|-2a|<a/4\}}.
\]
The shell is strictly outside the core: its radii range from \(7a/4\) to \(9a/4\). The radial Jacobian is bounded above and below by positive constants there, so \(f\in L^1\) follows from exponent \(-3/4\), while \(f\notin L^2\) follows from exponent \(-3/2\). An interior cube of positive measure accommodates every difference on that shell. Consequently the weighted \(f^2\) integral diverges and the ordered-pair variance is infinite.

This checks the hard-core example in every dimension \(d\ge1\), with the usual two directions in dimension one. Values on the singular sphere can be assigned arbitrarily. If \(a\) instead denotes a particle's physical radius, the forbidden pair distance is \(2a\), so the shell must be moved or the notation changed; the inspected development defines the forbidden pair distance directly and is mathematically consistent.

## 5. Canonical finite-volume correction

Direct polynomial expansion gives
\[
(N)_4-(N)_2^2
=N(N-1)\{(N-2)(N-3)-N(N-1)\}
=-N(N-1)(4N-6).
\]
For \(N\ge2\),
\[
|r_4-r_2^2|
=\frac{N(N-1)(4N-6)}{V^4}
\le\frac{4(N/V)^3}{V}.
\]
Thus \(C_0=4\bar\rho^3\), \(C_4=0\), \(C_2=\bar\rho^2\), and \(C_3=\bar\rho^3\) work uniformly when \(N/V\le\bar\rho\). With the current density used for one fixed vessel, the stated bound
\[
\operatorname{Var}F\le
2\rho_N^2V\|f\|_2^2+8\rho_N^3V\|f\|_1^2
\]
follows. The small cases \(N=2,3\), where \((N)_4=0\), do not create an exception.

The source's \(k\)-dependent effective density is also respected. For fixed \(k\le N\),
\[
\rho_{N,k}=(N)_k^{1/k}/V,\qquad
v_{N,k}=V/(N)_k^{1/k}
\]
matches \(r_k\) exactly and satisfies \(v_{N,k}\to v\) if \(V/N\to v\). Failure of a single common density to match orders one and two does not refute the actual order-dependent claim.

## 6. Historical statement and classification limits

The primary source was reopened at:

https://www.mathnet.ru/php/getFT.phtml?jrnid=rm&option_lang=eng&paperid=5594&what=fullteng

Bibliographic entry: Minlos, R. A. (1968). Lectures on statistical physics. *Russian Mathematical Surveys, 23*(1), 137–196. https://doi.org/10.1070/RM1968v023n01ABEH001235

Printed p. 162 gives the \(L^1\) assumption (3.24); p. 163 displays the \(f^2\) contribution. The p. 164 remark supplies integrable spatial decay and a boundary-strip condition. Problem 3 requests explicit inequalities for the mean and concentration arguments. Remark 1 separately discusses exponential concentration. These locators were read in the opened primary text; no claim is made to have reconstructed every proof in that paper.

The historical source's undefined exceptional parameter set prevents extraction of a precise unrestricted all-density theorem. The modern dilute-regime references cited by the root should be matched only within their verified hypotheses. Their existence does not establish a general unresolved theorem outside those regimes; absence of such a theorem in the inspected sources is not proof that no criterion exists.

Recommended classification language:

> The historical programme is only partly realized at the level of its broad formulation. The explicit conditional inequalities considered here are proved below. The notes do not identify a single precise all-density residual conjecture, because the exceptional parameters and admissible limiting states are not specified.

If Class C is interpreted strictly as requiring a definite currently open statement, the unformulated remainder belongs under F, while the concentration calculation can remain an A/E item with a checked modern annotation. A C label must not be retained merely to produce a Stage 2 development. The user's instructions expressly permit no qualifying C/D development.

An adjacent caution concerns item 1966-100.4: P000156 expressly allows exceptional parameters and failure of the indicated rate for some \(v\). A range-only universal implication is false, but that quantifier should not silently be attributed to the qualified notebook discussion. The ideal canonical finite-size correction is a distinct exact obstruction and should remain separate.

## 7. Correction-table repair

Only the correction-table emission in parts/pde/build_part.py was changed: raw prose underscores and carets are escaped while explicit \( \ldots \) and \[ \ldots \] math segments are preserved. Regeneration produced the same 27 correction rows. An independent scan of all displayed text fields found no remaining unescaped prose underscore or caret.

SHA-256 comparisons confirmed that talks.json, items.json, problems.json and references.bib remained byte-identical. Slice counts remain 10 records, 69 items, 8 problems and 23 bibliography entries. This correction did not alter mathematical items, statuses or classifications.

This review consists of independent analytic derivations and source checks. It does not claim a separate rerun of the root's combinatorial test program.
