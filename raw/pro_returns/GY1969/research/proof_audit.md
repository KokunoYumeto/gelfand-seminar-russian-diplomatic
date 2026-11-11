# Independent proof audit

Audit date: 2026-11-09. All results below are presented as proofs supplied in
this companion; no mathematical novelty or historical priority is claimed.

## Paired evaluation current-group representation

An independent reader checked the complete proof, not only the initial
outline, against the final first subsection of `development.tex`.

- The smooth bump has derivative bounded by 8/e < 3.
- Finite interpolation uses disjoint supports and logarithms of SU(2)
  matrices of norm at most pi; the constant is independent of the prescribed
  matrix values.
- The choice of each pair length uses only previously determined constants,
  so the construction is inductive rather than circular.
- The infinite tensor product is defined on a specified incomplete tensor
  sector. Strong limits and strong limits of inverses yield unitary operators
  and preserve the group law.
- C1 strong continuity is proved on dense finite-excitation vectors and then
  extended by unitarity.
- Smooth finite interpolation approximates independent finite local matrix
  actions, despite the infinite evaluation set being dense.
- The commuting local projections converge to the vacuum projection; the
  vacuum is cyclic for local matrices. This proves the commutant is scalar.
- Support is checked through nontrivial conjugation of a local algebra, not
  by trying to isolate a point from a dense set.
- The uniform-topology countersequence bounds the entire vacuum coefficient
  by its first N factors regardless of the tail.
- The connectedness homotopy in the norm-continuous corollary is legitimate
  because no endpoint conditions have been imposed.

Outcome: no mathematical error found. The conclusion is explicitly confined
to the C1/strong and smooth/strong categories; it does not classify all
representations or identify the notebook's unstated category.

## Exact arithmetic counterexample

The code implements the partial trace directly by basis indices and separately
implements the block formula. Both are compared on all sixteen subsets of a
four-site system, followed by all 256 ordered commutators. The full check is
run with p=1/2 and p=2/3; eigenvectors and partial-transpose eigenvalues are
verified exactly using fractions. A repeated execution produced byte-identical
JSON output, recorded as `verify_annotations_rerun.json`.

This finite check does not prove the infinite-system assertion. That assertion
is proved separately by the block structure and consistency under partial trace.

## Bell-block and four-subspace proof review

A second independent reader verified the full Bell proof, including disconnected
subsets and partially occupied pairs. All embedded block factors commute, the
partial traces compose consistently, and the top eigenvector is entangled with
a simple eigenvalue for every 0<p<1. The simple-spectrum repair using polynomial
spectral projections is valid.

The same reader checked the complete four-subspace argument: the annihilator
relation is -l1+l2-l3=l4; End(R)=C; the orbit dimension is 32 in the irreducible
32-dimensional product Gr(4,6)^4; a generic affine line gives a holomorphic
family for all sufficiently small nonzero parameters. The special and generic
common-intersection dimensions are 1 and 0, respectively. No reversal of the
degeneration direction was found. The exact independent script gives the
expected endomorphism dimensions 1, 1, 1, 7, 4.

## Wavelet uncertainty check

An independent reader checked the change-of-variable proof and the two unitary
conjugation identities. The scaling factors for centered deviations are 2^-j
and 2^j; they cancel in the product. The argument does not bound the individual
deviations over all scales or justify the proposed Gram–Schmidt ordering.
The cited Meyer, Bourgain, and Gröchenig–Malinnikova full texts were also
independently reopened and their scope confirmed.

## Affine and projective cohomology peer review

A separate reader re-derived the Laurent monomial cohomology and residue
action, checked the punctured-elliptic Picard quotient, and reopened the
relevant Stacks and Deligne results. No mathematical error was found. Two
precision suggestions were incorporated: the primitive in the localization
proof is expressed through chosen lifts, and the restricted-dual piece
Hom_k(R_d,k) is explicitly placed in degree -d-n.
