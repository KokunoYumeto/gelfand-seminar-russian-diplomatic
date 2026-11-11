# Independent final peer review: records 735–738

Reviewer: late-record agent. Date: 11 November 2026. Scope: all 54 current mathematical statements (735: 3; 736: 16; 737: 15; 738: 20). The middle-record files were not edited by the reviewer.

## Outcome

No mathematical error was found in the final statements as reviewed. One small definition-completeness request was sent to the middle agent: repeat the explicit definition of tau and the exchange operator in 738.18.statement. The middle agent accepted that addition. This review checks statement correctness and critical hypotheses; it does not claim to have reread every proof in every cited source.

## Independently checked points

- **735.2 and 737.3–5:** cross-Gram singular values, ordered angle ranges, and the dimension-forced zero-angle count are correct. The vector/subspace item correctly retains the vector norm and handles the zero vector.
- **735.3 and 737.12–14:** the four intersection dimensions plus the generic positive contraction classify the pair. Injectivity of C and sqrt(1-C squared) excludes endpoint eigenvectors, while allowing endpoints in the continuous spectrum. The fixed-subspace realization dimension constraints are correct.
- **737.6:** the eight one-dimensional membership types and one two-dimensional three-distinct-lines block give the correct finite-type triple-subspace decomposition.
- **737.7–9:** diagonal congruence of the Gram matrix correctly treats unoriented Minkowski lines, including null lines. In Euclidean geometry the O orbit splits under SO exactly when all four intersections vanish. On a generic principal block, the stabilizer acts by the same orthogonal map twice, so its determinant is positive; a nonzero intersection summand supplies a determinant-minus-one reflection. The degenerate-form warning is necessary and present.
- **737.11:** with columns indexed by a tensor a followed by a basis vector and a basis vector followed by b, the cross-Gram matrix is (conjugate(A) B) transpose. Frobenius normalization and the nuclear-norm bound are correct. The stated full range and d=1 exception agree with the independently reviewed chapter development.
- **737.15:** preserving the first two coordinate subspaces forces block diagonality, preserving the diagonal forces equal blocks, and preserving the graph imposes precisely similarity.
- **736.4:** same-point matrix positivity is a restricted necessary test; full reflection positivity needs arbitrary smeared polynomial combinations in a half-space and only semidefiniteness before quotienting null vectors.
- **736.6:** direct tensor transformation gives T^{zz}=2(a+ic) in a traceless real tensor with T11=a, T12=c. Conservation implies partial_z T^{zz}=0. The covariant T_zz is the conventional holomorphic component. Thus the recorded index/chirality correction is sound.
- **736.8–10 and 736.14–16:** the local/global contour distinction, contact-term qualifications, scalar central-term/vacuum assumptions, projective group integration, and discrete-spectrum qualification for direct sums are appropriate. The transformation law explicitly fixes active versus passive convention.
- **738.2:** point evaluation is continuous and disjointly additive, but its first derivative is a Dirac distribution; it refutes the smooth-density conclusion from continuity alone. The stronger smooth-functional theorem is accurately qualified as locally finite jet order.
- **738.6:** the mixed second variation of (integral u) squared in disjoint directions is twice the product of the two integrals, demonstrating nonlocality. General smooth two-point kernels need not have finite separated rank.
- **738.8–11:** upper-bounded formal Laurent symbols give finite sums in each resulting coefficient. The residue cotangent representative has the correct right-hand coefficient placement. The negative commutator part cannot contribute to the trace pairing with a negative-order gradient. The second-bracket constraint requires the D^{-N} cotangent correction; mere substitution is insufficient.
- **738.12:** direct calculation with delta F_n=(1/2)z^{n+1} and J_u=-D^3/2-2uD-u' gives (m-n)F_{n+m}/2-(n^3-n)delta_{n+m,0}/8, exactly the stated correction. No quantum ordering term is needed.
- **738.13:** substituting the two displayed coordinate variations into delta(u3-u2'/2) cancels u2 f'' and f'''' and gives f w3'+3f' w3. The field correction is therefore exact.
- **738.14–17:** the independent-current Miura construction and its constrained reduction are distinguished. The integrating-factor solution presupposes known factors and is valid as a factored differential equation on the stated interval. A nonlinear Poisson algebra is still a Lie algebra, even if the linear span of selected generators is not closed.
- **738.18–20:** opened and read Lukyanov's original Russian paper, especially Proposition 2 and equations (2.11)–(2.17), Theorem 1/equation (1.6), and equations (2.18)–(2.21). These confirm conjugated regularity O(1), regular test functions across the diagonal, the parameter relation nu(nu-1)=h, and ordered-product quadratic closure with hypergeometric coefficient construction. They do not justify treating all handwritten square brackets as commutators or replacing regularity by an unrestricted R-matrix identity.

## Direct primary-source comparison for the last quantum items

S. L. Lukyanov, *Quantization of the Gelfand–Dikii brackets*, Funktsionalnyi Analiz i ego Prilozheniya 22(4) (1988), 1–10. Metadata and full original opened:

- https://www.mathnet.ru/eng/faa1147 — retrieval `turn160view0`.
- https://www.mathnet.ru/php/getFT.phtml?jrnid=faa&option_lang=eng&paperid=1147&what=fullt — retrieval `turn161view0`, detailed section 2/3 read `turn162view0`.

The test-function space is first introduced off the diagonal and then replaced by the space regular on the entire product immediately before Proposition 2; the middle statement uses the latter, correct hypothesis. The conclusion in equation (2.15) is O(1), not zero.
