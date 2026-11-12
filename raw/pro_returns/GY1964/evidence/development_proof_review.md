# Independent logical review of the Bishop development

Reviewer: winter-source subagent. Date: 12 November 2026.

Reviewed /workspace/scratch/f63c951485b7/work/output/GY1964_development.tex as supplied by the root agent. This review checks the mathematical arguments independently. It does not claim to verify the inaccessible August 2026 preprint, establish novelty, or repeat the two existing independent exact-arithmetic computations.

## Conclusions

No logical proof gap was found in the bounded development.

1. **Endpoint determinant.** Iteration of the weighted cyclic matrix gives the stated product entries. At the endpoint the first row is (1,0,...,0). Reversing the remaining rows gives the triangular matrix with diagonal products from a_i through a_(q-1). The reversal sign is (-1)^((q-1)(q-2)/2), and each a_j occurs exactly j times. Coprimality supplies every nonzero factor. For denominator16 the determinant scaling exponent is 0+...+15=120.
2. **Rational cyclicity.** The qth power is scalar multiplication by the strictly increasing polynomial m_q. Polynomial approximation on its image permits arbitrary continuous scalar coefficients of each cyclic-matrix column. Density of continuous functions in the associated finite weighted L2 measure extends this to bounded measurable coefficients. Truncating both the inverse matrix norm and the target gives bounded coefficients and converges to every L2 target. Finitely many singular fibres have measure zero. Uniform invertibility is neither needed nor asserted.
3. **Finite-orbit continuity.** The exact squared L2 difference of a sawtooth and its translate is d(1-d). Telescoping the product and bounding all remaining factors by one gives the sum of square roots, then the stated weaker polynomial coefficient bound. The cases k=0 and k=1 are explicitly covered.
4. **Finite certificate.** The stated transfer radius has square root 1/1300; the bound R(Q)<13 contributes strictly less than 1/100, and the rational error contributes strictly less than 1/100. The resulting 1/50 bound follows. Numerical fractions were already checked by two distinct root-owned implementations and were not recomputed here.
5. **Computable gap rule.** Strict rational error inequalities are decidable by piecewise polynomial integration. Rational-coefficient approximants exist because the target and orbit vectors are real. For each denominator only finitely many searches occur and each terminates by rational cyclicity. The chosen Psi(q) and the convergent inequality imply transfer error below 1/(2q) and total error below 1/q. On the infinite stipulated subsequence denominators tend to infinity; every fixed monomial therefore lies in the closed cyclic space. Polynomial density gives the conclusion.
6. **Generic conclusion.** The finite-orbit estimate makes each approximation set open. Each union contains all rational parameters by rational cyclicity and is therefore dense. The intersection over target and accuracy is a dense G-delta; intersection with the irrational parameters remains a dense G-delta. This is a fixed-vector conclusion, and the text correctly distinguishes it from cyclicity of every nonzero vector and from absence of invariant subspaces.

## Minor clarity suggestion sent to root

In the continuity proof, explicitly choose d as the fractional part of j(alpha-beta), or state that when |j(alpha-beta)|<=1 the identity also holds with this absolute value because d(1-d) is unchanged by replacing d with 1-d. This makes the treatment of negative shifts transparent. The inequality in the reviewed text is already correct.

## Scope limits

The theorem supplies a total computable sufficient gap function, without a manageable growth bound. Its construction is nonvacuous because later continued-fraction denominators can be made arbitrarily large by choosing partial quotients. It does not prove cyclicity at every irrational parameter. The source comparison and novelty restraint concerning the inaccessible 2026 lead are appropriate.
