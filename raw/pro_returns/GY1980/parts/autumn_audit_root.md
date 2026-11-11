# Independent focused audit of record 506

Audit date: 10 November 2026. Reviewed all 17 objects in `root_items.json`, compared the supplied EN and RU text of P000944–P000948, and inspected the actual P000946 and P000947 scans (1300-pixel derivatives). No files owned by the root agent were modified. The parent had already read the primary Novikov papers; this audit checks mathematical consistency and source/reconstruction boundaries rather than repeating that literature search.

## Findings requiring attention

1. **1980-506.16: use the endomorphism bundle.** The general-position argument is mathematically sound, but its application to the Bloch bundle must use a smooth section of the bundle of Hermitian endomorphisms, with transversality to the fiberwise multiplicity strata. A global map from the torus into one fixed matrix space presupposes a global frame. That would conflict with the nonzero first Chern class established in 506.13. The codimension-three calculation, the absence of crossings on a two-dimensional base, and the eigenline decomposition all work in local unitary frames and therefore in the bundle formulation.

2. **Unrepresented P947 aside.** The scan contains an uncancelled parenthesis saying that in the one-dimensional case the family is never in general position because the operator is second order. The present 506.16 does not retain it. Its intended class of operators or constraints is not specified; it is not a valid universal assertion about one-parameter Hermitian families. Preserve it as an uncertified qualification/aside, or a separate F item if the precise intended statement cannot be identified. The nearby question “where does degeneracy come from?” really is crossed out and need not become an independent open problem.

## Checks passed

- The Pauli normalization is internally consistent once the modern curvature convention is separated from the notebook convention.
- Physical line-bundle degree N and reciprocal-torus zero-mode bundle rank N / Chern number of absolute value 1 are correctly distinguished. P946 visibly has c1=N, so this is a faithful-error correction.
- Rational-to-integral reduction by a finite-index sublattice and the determinant obstruction for irrational finite-dimensional representations are correct.
- Positive-flux Dolbeault zero modes do not need pointwise positivity of the magnetic field. The H1 vanishing and Riemann–Roch proof correctly use positive degree.
- The scalar-spin restriction now present in 506.14 resolves the extra positive-energy multiplicity of the full two-sector Pauli operator. The fixed-sector statement and creation-operator comparison are correct.
- Weak electric compression is clearly identified as first-order perturbation theory with a uniform isolated cluster, not the exact perturbed operator.
- The zero-mode divisor parameters are not incorrectly treated as free global linear coordinates.
- The final irrational regularization and the constant-electric-field aside retain their unresolved hypotheses rather than being assigned invented theorems.

No further substantive mathematical error was found in the reviewed 17 items. This is a focused consistency audit, not certification that every historical publication proof was reread.
