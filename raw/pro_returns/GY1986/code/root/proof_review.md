# Independent mathematical verification

Review date: 2026-11-12. These notes record findings, not claims of historical novelty.

## Quantum KdV

The first derivation used the four elementary Virasoro commutators in the chapter. The separate program reconstructed the action by recursive PBW rewriting, checked the contravariant form, and repeated form-symmetry checks at other grades and parameter values. A second reviewer independently checked the level-two matrix, discriminant, nonzero nilpotent matrix, and survival in the irreducible quotient. The reviewer confirmed the argument and suggested making L0 invariance and grading explicit; that sentence was added. No positivity assumption is used. The example is explicitly nonunitary.

## Unitary integral

The proof uses Haar invariance and the distribution of a normalized complex Gaussian column. The independent implementation uses exact Gram pseudoinverses for permutation tensors. It agrees with direct U(2) integration, including complex and coalescing endpoints, and with a separately expanded ordinary HCIZ determinant for U(3). Singular Gram matrices for degree greater than N were explicitly checked; an ordinary inverse was not substituted.

The proposed permutation-only U(3) formula was evaluated by exact arithmetic. Each of its eighteen quadratic factors was independently verified by differentiating a Givens-rotation curve. Its pole at zero coupling disagrees with entireness and normalization of the true integral. Exact Haar moments provide a separate small-coupling check. This disproves the specified extension, not a claim made in the notebook.

A second reviewer independently checked the full written proof, including trace indexing, Haar normalization, the removable diagonal, the row-sum tail bound, singular Gram projection, and rational pseudoinverse. Manual substitution confirmed representative denominators, their reciprocal sum, and the second Taylor coefficient of the counterexample. The reviewer found no scope error and requested an explicit work marker on the independently checked low-degree identities; it was added.

## Simultaneous complex structures

The proof uses the normal form of three transverse planes and a two-dimensional real centralizer. The independent implementation solves full 4 by 4 invariance equations. A second reviewer confirmed the finite-family criterion, the vacuous three-plane case, all determinant hypotheses, and the deformation example. It matches the known Batzies classification. No statement about nonlinear or topological complexifiability is inferred.

## Cube

Exact convex-cell splitting gives 96. Independent intersection-flat enumeration and Mobius inversion gives 1 + 14 + 47 + 34 = 96. The computations exclude flats meeting only the boundary. All 96 rational interior witnesses and their distinct nonzero sign vectors are supplied. The notebook's existing answer is confirmed.

## Additional finite-volume and operator annotations

For the zero-field complete-graph Gaussian SK model at finite N, a second reviewer checked the argument that exact ground states form only one global-spin-flip pair almost surely. Equality of every pair product forces the spin ratio to be constant; any pair not related by a global flip has a nondegenerate Gaussian energy difference. A finite union of null events proves the claim. This says nothing about a chosen near-ground energy window.

The spectral-operator correction is checked by two exact methods in the C-slice program: composition of differential operators by their coefficients, and direct action on polynomial vectors at rational arguments. The original sign yields a nonzero commutator; the specified corrected sign yields zero. The notebook scan fixes the classification as a faithful error.
