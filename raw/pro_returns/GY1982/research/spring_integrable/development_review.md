# Independent review of the four-unitary development

Reviewed 11 November 2026 by the spring/integrable-systems agent, independently of the root author. The reviewed proof and checker hashes are recorded in development_review_checks.json.

**Verdict: the proof, stated finite-rank formulas, and application of the local large-matrix theorem are correct. No mathematical change is required.**

## Independent derivation of the moments

This review used a character argument, distinct from both the conditional two-trace computation in the text and the matrix-index contractions in the code.

For an irreducible unitary representation \(\rho\) of dimension \(r\), averaging the first conjugation gives
\[
\int \rho(U)\rho(V)\rho(U)^*\,dU=\frac{\chi_\rho(V)}r I.
\]
Multiplying by \(\rho(V)^*\), taking the trace and integrating over \(V\), Schur orthogonality gives
\[
\mathbb E\chi_\rho(UVU^{-1}V^{-1})=\frac1r.
\]
For the fundamental \(U(N)\) representation, \(C=\operatorname{Tr}[U,V]\), this gives \(\mathbb EC=1/N\). The identities
\[
(\operatorname{Tr}g)^2=\chi_{\operatorname{Sym}^2}(g)+\chi_{\Lambda^2}(g),
\qquad
|\operatorname{Tr}g|^2=1+\chi_{\operatorname{Ad}}(g)
\]
therefore give, for every \(N\ge2\),
\[
\mathbb EC^2=\frac{2}{N(N+1)}+\frac{2}{N(N-1)}
=\frac4{N^2-1},\qquad
\mathbb E|C|^2=1+\frac1{N^2-1}=\frac{N^2}{N^2-1}.
\]
All dimensions used here are positive at \(N=2\), and \(\Lambda^2\) remains a nontrivial one-dimensional determinant representation. At \(N=1\) it disappears; the scalar case must indeed be calculated separately.

The conditional mean for a real plaquette \(X=C+\overline C\), with the shared matrix \(U\) fixed, is \(2|\operatorname{Tr}U|^2/N\). Since \(\mathbb E|\operatorname{Tr}U|^4=2\), distinct plaquettes sharing exactly one matrix have covariance \(4/N^2\). Disjoint pairs are independent. There are \(\binom d2\) plaquettes and \(d\binom{d-1}2\) unordered adjacent pairs. Including the factor two in the variance sum reproduces
\[
F'_{d,N}(0)=-d-\frac{d(d-1)}{N^2},\qquad
F''_{d,N}(0)=d(d-1)\left(\frac{N^2+4}{N^2-1}+\frac{4d-10}{N^2}\right).
\]
For \(d=4\), this is exactly the root formula, including the \(72/N^2\) term.

The checker independently verifies this character derivation symbolically for \(d=2,3,4,5,6,9\). The additional values are checks of the counting implementation; the displayed count proves the formula for every fixed \(d\).

## Local theorem: exact scope

I opened and read Collins, Guionnet and Maurel-Segala, arXiv:math/0608193v3, Introduction and Theorem 0.1 on PDF pages 1–3, and Corollary 7.1 on PDF page 35:

https://arxiv.org/pdf/math/0608193

The theorem gives the limit at sufficiently small **real** coupling, analyticity of the resulting function near zero, and identification of its derivatives with limits of the formal finite-\(N\) derivatives. Corollary 7.1 states the last equality explicitly. The polynomial
\[
V=-\sum_{\mu,\nu}U_\mu U_\nu U_\mu^*U_\nu^*
\]
is self-adjoint because taking adjoints swaps the two indices. Its degree and number of variables are fixed as \(N\) grows. Any unused external Hermitian variables can be set to zero, so the boundedness and limiting-moment hypotheses are satisfied. The paper uses probability Haar measure and the ordinary, unnormalized matrix trace.

The root text correctly limits the conclusion to real small-coupling convergence with an analytic extension of the limiting function. The paper itself warns on PDF page 3 that convergence of the complex-coupling integrals was not established there. The root neither asserts such convergence nor infers a global branch from the two coefficients.

The arXiv abstract page was opened for chronology: first submission 8 August 2006; the full version inspected here is the 25 June 2008 revision; journal reference Advances in Mathematics 222(1), 172–215 (2009), DOI 10.1016/j.aim.2009.03.019:

https://arxiv.org/abs/math/0608193

The journal landing-page fetch returned 403 in this review; the full theorem was read in the primary author preprint, not on that blocked page.

## Other proof and code checks

The global bounds follow from the real paired off-diagonal action; the diagonal term is exactly \(dN\). The signs after removing that term are correct. Differentiation under the compact integral gives \(F'=-\mathbb E_\beta S/N\) and \(F''=\operatorname{Var}_\beta S\). Entirety of the partition function and positivity on the real axis imply local analyticity of its logarithm around each real point, without an entire logarithm. The equi-Lipschitz/Arzelà–Ascoli argument gives compact subsequential convergence and does not claim uniqueness.

The entrywise formula implemented in the checker agrees with Collins and Śniady, Corollary 2.4, which I opened and read on PDF page 5:

https://arxiv.org/pdf/math-ph/0402073

The adjoint-token row/column reversal is correct; free index classes contribute one \(N\) each; the degree-two weights are \(1/(N^2-1)\) and \(-1/[N(N^2-1)]\); the diagonal plaquettes are legitimately omitted from the variance. The ordered-pair total \(4+36+144+400=584\) is correct.

The original checker was executed from an isolated namespace with its output destination redirected to this shard. All symbolic assertions and rational evaluations passed. No shared parent output was edited.

## Review artifacts

- review_haar_development.py: independent character computation and isolated rerun.
- development_review_checks.json: result, exact formulas and hashes.
- root_haar_rerun.txt: complete checker output.
- haar_check_results.json: isolated rerun's machine-readable results.

These are verification of a bounded standard calculation, not a novelty claim or an all-coupling solution.
