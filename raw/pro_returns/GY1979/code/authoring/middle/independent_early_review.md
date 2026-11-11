# Independent review of the early batch's annotated calculations

**Reviewer:** middle-records agent, independent of the early author. **Date:** 10 November 2026.

**Conclusion:** the Gaussian and quartic integral values, DS resonant counterexample, and unit-sphere heat/zeta values are correct. The symplectic normal-form statement matches the cited theorem. No numerical or algebraic correction is required. Two small additions make the individual statements self-contained: state the closed-manifold/nonnegative-operator and positive-spectrum-zeta assumptions in 465.21; state finite dimensionality explicitly in 466.4. The numerical quadrature is evidence, not a certified interval enclosure; the existing early qualification is appropriate.

## Material independently checked

Read `parts/early/verify_annotations.py`, `parts/early/annotation_checks.json`, and items 1979-463.10, 1979-465.21, and 1979-466.1–.4. Read the relevant Russian and English source passages, and inspected the original PNGs P000845, P000846, P000852, P000853, and P000854. In particular, the second DS denominator really has sums, the four integrals really have the specified exponents/frequencies, and the notebook distinguishes a rejected multiplicity interpretation from its later integrality assertion.

No early/final file was edited or regenerated. Independent executable calculations are in `parts/middle/independent_early_checks.py`; their output is `parts/middle/independent_early_checks.json`.

## 1. Gaussian and narrow-quartic exercises: correct

For $a>0$, differentiating $I(a,b)=\int_{\mathbb R}e^{-ax^2}\cos(bx)\,dx$ under the integral and integrating by parts gives $\partial_b I=-bI/(2a)$. Together with $I(a,0)=\sqrt{\pi/a}$, this proves the two values in 466.1. No contour assumption is needed for that proof.

For the quartic integral, integration of each even Taylor term gives

\[
\int_{\mathbb R}e^{-ax^4}\cos(bx)\,dx
=\frac1{2a^{1/4}}\sum_{k\geq0}\frac{(-1)^k\Gamma((2k+1)/4)}{(2k)!}
(ba^{-1/4})^{2k}.
\]

The domination $e^{-ax^4+|b||x|}$ is integrable, so the derivation and convergence claim are sound. An independent finite sum through $k=12$, rather than the early script's infinite summation routine, gives $0.3206479707071545821145415122771041299523032533\ldots$. The integrated global Taylor remainder is bounded analytically by

\[
\frac{\Gamma((2N+3)/4)|b|^{2N+2}}{2(2N+2)!a^{(2N+3)/4}},
\]

which is $3.159\times10^{-45}$ or less for $a=1000,b=1,N=12$. This independently supports all digits displayed in item 466.2. Floating-point evaluation of the finite sum itself was performed at 85 decimal digits; it was not converted into interval arithmetic.

## 2. Highly oscillatory quartic: contour, scale, saddles, and value correct

Write $b=4r^3>0$, $\Phi(z)=-z^4+ibz$, and shift the real line to $z=t+ir/2$. On the vertical closing edges, with imaginary part bounded between $0$ and $r/2$, $\Re\Phi(\pm R+iv)=-R^4+O(R^2)$; therefore the closing-edge integrals tend to zero. The integrand is entire. The contour shift is legitimate for every fixed $b$.

On the shifted line the two peaks are at $t=\pm\sqrt3r/2$, the real part at either peak is $-3r^4/2$, and the negative-half integrand is the complex conjugate of the positive-half integrand. These facts justify both the early script's exponential rescaling and its $2\Re$ symmetry reduction.

For an independent implementation, use $t=\sqrt3r/2+y/r$ on the positive half. Its exact local exponent after removing the real scale and saddle phase is

\[
-3(1+i\sqrt3)y^2-\frac{2(\sqrt3+i)y^3}{r^2}-\frac{y^4}{r^4}.
\]

The integral was evaluated on the fixed finite interval $[-14,14]$, subdivided around zero, at 85 decimal digits. This removes the early implementation's large original-coordinate peaks and semi-infinite quadrature. On the actual positive half-contour, $t\geq0$,

\[
|e^{\Phi(t+ir/2)+3r^4/2}|=e^{-(t^2-3r^2/4)^2}\leq e^{-3y^2/4}.
\]

Consequently the absolute discarded-tail bound for the rescaled full integral is at most

\[
\frac4r\int_{14}^{\infty}e^{-3y^2/4}\,dy <4.343\times10^{-66}.
\]

The independently obtained values are

\[
 e^{3r^4/2}I(1,1000)=0.153952449291199637845089961312218831377125582139230483641920022598\ldots,
\]
\[
 I(1,1000)=1.7020109383843244214221414386507305361516165751535870749439810759\ldots\times10^{-1027}.
\]

The numerical difference from the early script's 105-digit rescaled value is about $1.01\times10^{-83}$. This unusually stronger agreement than the conservative analytic tail bound is only a numerical observation; the quadrature itself is not interval certified.

The upper-half-plane saddles $r e^{i\pi/6}$ and $r e^{5i\pi/6}$, together with their Gaussian factors, give precisely

\[
 I(1,b)=\sqrt{\frac{2\pi}{3}}r^{-1}e^{-3r^4/2}
 \left[\cos\left(\frac{3\sqrt3r^4}{2}-\frac\pi6\right)+O(r^{-4})\right].
\]

The potentially $r^{-2}$ term is odd in the local Gaussian variable and integrates to zero. The next cosine correction has coefficient $7/(144r^4)$ and phase shifted by $-2\pi/3$; it improves the value as expected. The leading expression's actual relative error at $b=1000$ is approximately $1.4168\times10^{-5}$. The early text correctly states an absolute remainder inside the braces, avoiding a false uniform relative-error assertion near cosine zeros.

## 3. Printed DS coefficient: exact counterexample correct

The source coefficient is

\[
 w=\frac{(p_1-p_3)^2-(q_1-q_3)^2}{(p_1-p_3)^2+(q_1-q_3)^2}
 +\frac{(p_2-p_4)^2-(q_2-q_4)^2}{(p_2+p_4)^2+(q_2+q_4)^2}.
\]

With $\omega(p,q)=-p^2+q^2$, the quartet

\[
 k_1=(1,0),\quad k_2=(0,1),\quad k_3=(0,0),\quad k_4=(1,1)
\]

satisfies both printed conservation equations. Its denominators are $1$ and $5$, and $w=1+1/5=6/5$. Changing only the denominator's internal plus signs gives $2$, as stated. Thus the numerical counterexample does not depend on an illicit singular denominator or on rounding.

No source hypothesis excludes a zero momentum. If a reader nevertheless worries about that feature, the translated quartet $(2,2),(1,3),(1,2),(2,3)$ has all vectors nonzero, preserves both conservation laws, and gives $w=1+1/45=46/45\ne0$. This is optional corroboration; the existing counterexample needs no replacement. The early text appropriately declines to reconstruct a different symmetrized kernel without source evidence.

## 4. Scalar Laplacian on the unit round four-sphere: correct, also verified spectrally

The substitution in the local heat coefficient is arithmetically correct:

\[
\frac{8\pi^2/3}{360(4\pi)^2}\{5\cdot12^2-2\cdot36+2\cdot24\}=\frac{29}{90}.
\]

I independently opened Gilkey's author-hosted first edition and checked Theorem 4.8.16(c), printed p.327, and Lemma 1.10.1 with the positive-semidefinite extension on pp.79–80: https://darkwing.uoregon.edu/~gilkey/dirPDF/InvarianceTheory1Ed.pdf. Its opposite curvature sign convention does not affect these squared curvature contractions; the integrated derivative term vanishes on the closed sphere.

An independent spectral calculation avoids reusing the heat-coefficient substitution. The eigenvalues and multiplicities are $\lambda_l=l(l+3)$ and $d_l=(l+1)(l+2)(2l+3)/6$, with $l\geq1$ for the positive spectrum. Put $q=5/2$. A binomial expansion in $9/(4(l+3/2)^2)$ expresses the spectral zeta function through Hurwitz zeta functions. At $s=0$, the $k=0$ term and the poles in the $k=1,2$ terms give

\[
\zeta_\Delta(0)=\frac13\left[\zeta_H(-3,5/2)-\frac14\zeta_H(-1,5/2)+\frac{81}{64}-\frac9{32}\right].
\]

Here $\zeta_H(-1,5/2)=-47/24$ and $\zeta_H(-3,5/2)=-3367/960$, so exact rational arithmetic yields $-61/90$. The one-dimensional constant kernel then gives $B_4=\zeta_\Delta(0)+1=29/90$. Both results agree with the early output.

**Suggested precision edit:** begin the general assertion in 465.21 with “For a nonnegative self-adjoint Laplace-type operator $P$ on a closed smooth four-dimensional Riemannian manifold, with zeta formed from its positive eigenvalues, …”. This makes explicit the hypotheses already needed by the heat discussion. A manifold with boundary requires boundary conditions and boundary heat contributions; the sphere example has neither issue.

## 5. Symplectic self-adjoint normal form: correct

Opened https://arxiv.org/pdf/1710.00697 and checked Theorems 1/10 and Corollary 11, with the displayed finite-dimensional, characteristic-not-two, perfect-field/splitting hypotheses. The definition $\omega(Au,v)=\omega(u,Av)$ gives $A^T\Omega=\Omega A$, which is satisfied by 
$A=\operatorname{diag}(J,J^T)$ for the standard symplectic matrix. There is no missing minus sign; a minus sign would pertain to the different Hamiltonian/skew-adjoint condition. Over $\mathbb C$, the stated paired Jordan form follows. The reconstruction correctly separates the perfect-field polarization assertion from a Jordan form over a field in which the characteristic polynomial need not split.

**Suggested precision edit:** insert “finite-dimensional” before “symplectic space” in the precise statement of 466.4. The later 2017 exposition is correctly described as a proof of an older classification and not a claim of first discovery in 2017. Its cited predecessors are 1987/1988 and 2005; those particular references by themselves do not establish a publication before 1979, so a more specific pre-1979 publication date should not be added without another source.
