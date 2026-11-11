# Independent review of the mathematical development

**Reviewer:** late-record subagent. **Date:** 10 November 2026. **Text reviewed:** GY1979/GY1979_development.tex, as read during the final integration. This review rederives the assertions from their definitions and checks the hypotheses. It does not infer correctness from the accompanying 36 numerical examples or from agreement between the two programs.

**Verdict.** The regular-representation reduction, the dual-number and matrix-pair examples, the complete \(n=2,N=4\) even-commutant description, and the compactly supported \(SU(2)\) diagnostic are correct under the stated hypotheses. No mathematical correction is required. The finite-algebra reduction uses \(\mathbb C\); the commutant calculation works over both \(\mathbb R\) and \(\mathbb C\). The distinction between these fields, ordinary commutation and supercommutation, and proof failure versus reducibility is already preserved in the development.

## 1. Internal conjugacy and the regular representation

Let \(\mathcal A\) be a finite-dimensional unital complex algebra, with its basis fixed once. Associativity gives

\[
L_aL_b=L_{ab},\qquad L_1=I,\qquad L_a(1)=a.
\]

Thus \(L\) is a faithful algebra representation. If \(L_a\) is invertible, let \(b=L_a^{-1}(1)\), so \(ab=1\). The equality \(a(ba-1)=0\) and injectivity of \(L_a\) imply \(ba=1\). This proves the required equality of groups

\[
L(\mathcal A^\times)=L(\mathcal A)^\times,
\]

where the right side means the nonsingular matrices lying in the image algebra. No enlargement to the entire ambient general linear group is allowed. For \(b\in\mathcal A^\times\), multiplication gives

\[
L_bL_aL_b^{-1}=L_{bab^{-1}}.
\]

Conversely, every permitted similarity has this form, and faithfulness recovers the original equality in \(\mathcal A\). Hence the reduction preserves the exact equivalence relation.

For the even supermatrix algebra, its parity conditions are stable under ordinary matrix multiplication with exterior coefficients, and the identity belongs to the even part. A matrix inverse of an even element, when it exists, is even: writing the inverse as its even plus odd part and comparing parities gives zero odd part. Therefore the units used by the algebraic reduction agree with the intended invertible even changes of basis.

### Check against the cited canonical-form theorem

I independently opened Sergeichuk's full primary author copy, https://arxiv.org/pdf/0709.2485 . Section 1.1, Theorem 1.1 on PDF p. 5, the concluding observation on p. 6, and Theorem 1.3 on p. 13 were read. The first theorem puts any unital complex matrix algebra into reduced form; the second gives a unique canonical matrix for its similarity action. The source uses an algebraically closed field, so the development's use of \(\mathbb C\) fits.

For clarity, the pullback of the canonical representative can be written explicitly. Fix \(P\), depending only on \(\Gamma=L(\mathcal A)\), with \(\Gamma'=P^{-1}\Gamma P\) reduced. If \(C_{\Gamma'}\) denotes the theorem's canonical-map operation, then

\[
a_{\rm can}
=L^{-1}\!\left(P\,C_{\Gamma'}(P^{-1}L_aP)\,P^{-1}\right).
\]

The argument of \(L^{-1}\) really lies in \(\Gamma\), because the algorithm produces a matrix in the same \(\Gamma'\)-similarity orbit, and internal conjugation preserves \(\Gamma'\). Fixing \(P\) uniformly is essential; choosing it afresh depending on \(a\) without a convention would obscure canonicity. The chapter already refers to a fixed algebra and fixed basis, so this is an explicit unpacking, not a repair.

The word algorithm has its ordinary exact algebraic meaning here, allowing exact field operations and eigenvalue/order decisions in the chosen coefficient model. This reduction does not assert an implementable Turing procedure on arbitrary black-box complex numbers, nor a short finite list of Jordan-shaped blocks. Those stronger readings are unnecessary.

### The two explanatory subcases

For \(D=\bigoplus_i\lambda_iI\), exact multiplication modulo \(\varepsilon^2=0\) gives

\[
(I+\varepsilon S)(D+\varepsilon A_1)(I-\varepsilon S)
=D+\varepsilon(A_1+[S,D]).
\]

The off-diagonal block equation is \([S,D]_{ij}=(\lambda_j-\lambda_i)S_{ij}\), so distinct eigenvalues eliminate precisely those blocks. In a subsequent equivalence between normal forms with the same ordered \(D\), the constant part of the conjugating matrix commutes with \(D\) and is block diagonal. A nilpotent correction cannot alter the diagonal blocks through \([S,D]\). Consequently the ordinary similarity classes of the surviving restrictions are necessary and sufficient invariants. This proves completeness, not just existence.

For the three-generator example, the positive-degree ideal of \((\Lambda_3)_{\bar0}\) has square zero. Writing an invertible \(P\) as \(P_0+R\), every product involving \(R\) and a positive-degree term of \(A-\lambda I\) vanishes. Therefore conjugation acts separately on the coefficients of \(\xi_1\xi_2\) and \(\xi_1\xi_3\) by the same \(P_0\). Their linear independence proves both directions of the simultaneous-similarity reduction. The unused \(\xi_2\xi_3\) coefficient in \(P\) cannot introduce a hidden equivalence.

## 2. The finite even commutant: deriving all equations

The calculation uses the ordinary matrix commutator, not a graded commutator. An even exterior monomial commutes with every exterior monomial. Thus for disjoint odd \(I\) and even \(J\),

\[
(\xi_IA_I)(\xi_JB_J)-(\xi_JB_J)(\xi_IA_I)
=\epsilon(I,J)\xi_{I\cup J}[A_I,B_J].
\]

If the sets intersect, the product is zero. Equating the independent exterior monomial coefficients therefore gives exactly the displayed finite system, with no omitted equations or genericity assumption. For \(N\ge1\), the numbers of even and odd monomials are both \(2^{N-1}\). This verifies the stated matrix size of the linear system before dependencies.

The kernel is an algebra: if \(B\) and \(C\) commute with \(A\), then \(ABC=BAC=BCA\), so \(BC\) commutes with \(A\). The identity lies in it. The coefficient description therefore determines the actual embedded commutant algebra, rather than just its dimension.

For \(N=4\), odd coefficients have degrees one or three and even coefficients degrees zero, two or four. The only possible nonzero commutator degrees are one and three. Writing the coefficients as in the chapter, direct sorting gives

\[
[X_i,B_0]=0,
\qquad
[X_i,B_{jk}]-[X_j,B_{ik}]+[X_k,B_{ij}]
 +[Z_{ijk},B_0]=0.
\]

The minus sign in the middle term comes from moving \(\xi_j\) past \(\xi_i\). There can be no equation involving the top-degree coefficient \(D\), since every product with \(A\) then has degree at least five. This is the main structural simplification.

Subtracting an odd scalar matrix from \(A\) changes none of these equations because every entry of \(B\) is even. Traceless reduction is consequently legitimate, not a conjugacy assumption. The factor \(1/2\) requires characteristic different from two, which holds over the two stated fields.

### Elementary centralizers

A nonzero traceless \(2\times2\) matrix \(X\) is nonscalar. If every vector spanned an invariant line, linearity applied to two independent vectors and their sum would make \(X\) scalar. Hence a cyclic vector \(v\) exists. A commuting map is determined by its value at \(v\), because it must take \(Xv\) to \(X\) times that value. This proves

\[
Z(X)=\mathbb K I+\mathbb K X.
\]

If \(X,Y\) are independent traceless matrices, an element of both centralizers must be scalar, because
\(aI+bX=cI+dY\) has traceless part \(bX=dY\). Thus \(Z(X,Y)=\mathbb K I\). This argument includes nilpotent matrices and real matrices with nonreal eigenvalues; diagonalization is not used.

The trace pairing on \(M_2(\mathbb K)\) is nondegenerate, and

\[
\operatorname{tr}(T[X,U])=\operatorname{tr}([T,X]U).
\]

The annihilator of \([X,M_2]+[Y,M_2]\) is therefore \(Z(X,Y)\). For an independent traceless pair, the sum has dimension three and lies in \(\mathfrak{sl}_2\), hence equals \(\mathfrak{sl}_2\). This proves the surjectivity used in the rank-two case without assuming a particular real or complex orbit type of the pair.

### Rank three

A linear change of exterior generators may send the full-rank linear coefficient tensor to \(H,E,F,0\). This does not require a simultaneous matrix conjugation sending an arbitrary triple to that triple: it is a change in the generator factor of the tensor. All cubic coefficients must undergo the same exterior-algebra automorphism, as the chapter specifies.

The degree-one equations make \(B_0\) scalar, so all cubic corrections drop out. Put \(U=B_{14},V=B_{24},W=B_{34}\), with scalar parts removed. The three equations are

\[
[H,V]=[E,U],\quad [H,W]=[F,U],\quad [E,W]=[F,V].
\]

Write \(U=aH+bE+cF\). In the first equation the \(H\)-coefficient forces \(c=0\), and \(V=dH-aE\). In the second, the \(H\)-coefficient forces \(b=0\), and \(W=gH-aF\). The final equation becomes

\[
-2gE-aH=2dF+aH,
\]

so \(a=d=g=0\). Thus \(U,V,W\) have only the three scalar freedoms stated. The remaining triple of two-form coefficients gives a map \(M_2^3\to\mathfrak{sl}_2\) whose image contains \(E,F\) from commutators with \(H\) and \(H\) from a commutator with \(E\). Its rank is three, giving a nine-dimensional kernel. The total dimension is \(1+3+9+4=17\).

### Rank two

Choose coefficients \(X,Y,0,0\) with \(X,Y\) independent. Again \(B_0\) is scalar and the cubic part disappears. The equations for triples 134 and 234 force \(B_{34}\) into the joint centralizer, so it is scalar. The equations for triples 123 and 124 are independent copies of a map \(M_2^2\to\mathfrak{sl}_2\) with rank three by the trace-pairing argument. Each has five-dimensional kernel. \(B_{12}\) is free. The total is \(1+1+5+5+4+4=20\).

### Rank one

With linear part \(\xi_1X\), the constant coefficient is \(B_0=cI+dX\). For \(1<j<k\), the degree-three equation is

\[
[X,B_{jk}]+d[Z_{1jk},X]
=[X,B_{jk}-dZ_{1jk}]=0.
\]

Hence \(B_{jk}=dZ_{1jk}+u_{jk}I+v_{jk}X\), with the positive sign of \(dZ_{1jk}\) exactly as printed. The triple 234 contains no linear term and gives \(d[Z_{234},X]=0\). This removes precisely the one parameter \(d\) when the indicated commutator is nonzero; it imposes no extra condition on the three pairs involving index 1. The independent counts are 12 for those free pairs, six for the other pairs, four for \(D\), and either two or one for the constant term. The dimensions are 24 or 23. Nilpotent \(X\) causes no exception.

### Rank zero

Only the four equations \([Z_{ijk},B_0]=0\) survive. All six two-form coefficients and the top coefficient are free, giving 28 dimensions before the constant term. Zero cubic span allows all four constant dimensions. A one-dimensional nonzero traceless span allows two. Two or more independent traceless coefficients allow one. The resulting dimensions \(32,30,29\) are exhaustive.

### Scope of the theorem

The theorem describes every solution coefficient in adapted exterior coordinates, and thus the embedded algebra. It does not claim that equal dimensions imply isomorphic commutant algebras, or that the listed integer strata classify all inputs \(A\) up to conjugacy. The text does not make either stronger claim. The general \(n=3\) suggestion is correctly left as a future determinantal-rank problem; the independent-pair centralizer shortcut used here genuinely fails in higher matrix size.

## 3. The \(SU(2)\) derivative counterexample

The proposed matrices satisfy

\[
X^\dagger=-X,\quad Y^\dagger=-Y,\quad
\operatorname{tr}X=\operatorname{tr}Y=0,\quad
X^2=Y^2=-I,\quad XY=-YX.
\]

In particular \((xX+yY)^2=-(x^2+y^2)I\), so separating even and odd powers of the exponential proves the displayed sine/cosine formula directly. At \(y=0,x>0\), the first \(y\)-derivative of \(r=(x^2+y^2)^{1/2}\) is zero, hence

\[
\partial_y e^{xX+yY}\big|_{y=0}=\frac{\sin x}{x}Y.
\]

Right multiplication by \(e^{-xX}\), followed by \(YX=-XY\), yields

\[
\beta_y=\frac{\sin x\cos x}{x}Y+\frac{\sin^2x}{x}XY.
\]

At \(x=\pi/2\) the result is \(2XY/\pi\), while the original tangent is \(Y\). A nonzero diagonal matrix cannot equal a nonzero off-diagonal one. The right-versus-left logarithmic-derivative convention is consistent throughout; a change of convention would change the cross-term sign but still give a counterexample.

For an independent derivation, differentiating the absolutely convergent matrix power series gives

\[
D\exp_\Phi(H)
=\int_0^1e^{(1-t)\Phi}He^{t\Phi}\,dt.
\]

Right multiplication and a change of variable give the adjoint integral in the chapter. Since \([X,Y]=2XY\) and \([X,XY]=-2Y\), the adjoint evolution of \(Y\) solves a two-dimensional rotation system and equals
\(\cos(2tx)Y+\sin(2tx)XY\). Integrating gives exactly the two coefficients above. Its expansion is \(Y+xXY+O(x^2)\), independently verifying the first nonabelian correction.

A smooth bump identically one on an open neighborhood of the chosen point preserves both the value and first derivatives there. Multiplication by that bump keeps \(\Phi\) in the real vector space \(\mathfrak{su}(2)\), and the exponential is in \(SU(2)\) and equals the identity outside a compact set. On an arbitrary surface chart centered at \(q\), one may explicitly use

\[
\Phi(u,v)=\chi(u,v)\bigl((\pi/2+u)X+vY\bigr),
\]

with support compactly inside the chart. Extension by zero is smooth. This supplies the required local counterexample on every surface, irrespective of the available coordinate range. No orientability or global trivialization issue arises for a Lie-algebra-valued function in a chart.

### Check against the documented flaw and limits of the conclusion

I independently opened Hasebe's primary v3 PDF, https://arxiv.org/pdf/0805.1329 , dated 15 January 2011, and Shimada's v2, https://arxiv.org/pdf/math-ph/0404042 , dated 1 February 2005. Hasebe p. 1 identifies the use of \(d\Phi_{s,t}=\beta(\exp\Phi_{s,t})\) in Shimada's Lemma 4.6, equation (4.28), as invalid in the nonabelian setting. Hasebe's §2.3, Eq. (2.1), uses exactly the right logarithmic derivative used here. His abstract retains the earlier all-dimensional claim, so the corrected introduction, rather than the abstract alone, controls interpretation.

The chapter's example disproves the differential identity used in that argument. It does not prove that the representation is reducible, does not show that no repaired proof exists, and does not establish a final present-day status by itself. Those logical limits are stated correctly in the development. I have checked the diagnostic's mathematics and the cited correction; I have not repeated the parent's independent literature search for every later energy-representation result.

## 4. Review disposition

All three requested mathematical checks pass from their definitions. The explicit canonical-representative pullback and the chart-centered bump formula above are optional clarifications. They expose no missing hypothesis in the current text. No changes to the parent's development file were made by this reviewer.
