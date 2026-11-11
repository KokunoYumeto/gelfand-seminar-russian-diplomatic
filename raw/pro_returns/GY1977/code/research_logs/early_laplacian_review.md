# Independent review: positive-Witt Laplacian verification

Date: **10 November 2026**. Reviewed the second subsection of `work/parts/root/development.tex`, `work/code/check_laplacian.py`, and `work/code/output/laplacian_checks.json`. No root file was edited.

## Verdict

**The mathematical claims of the development subsection are correct, and the saved computation supports its stated finite scope.** The weight25 collision has total multiplicity12 across exterior degrees. I independently confirmed the exact multiplicities at eigenvalue320 using a separately written boundary construction and rational matrix ranks, without repeating all characteristic-polynomial calculations.

Two audit qualifications and one bibliographic correction were sent promptly to the parent:

1. The cited paper's correct title is **“Laplacian spectrum for the nilpotent Kac–Moody Lie algebras,”** with pages **323–334**, not the title and starting page previously appearing in the report. Theorem2 is indeed onp.324. The correct DOI is **10.2140/pjm.2010.247.323**.
2. The chapter implementation computes each degree's characteristic polynomial, but its comparison with the gap-partition formula is **aggregated over exterior degree at fixed weight**. The development says this accurately; the report's earlier phrase “agree … at every degree” should be qualified accordingly.
3. The code's field `first_collision` initially means the first collision among the checked weights1–22,25. Its fallback search of23–80 does not execute after a collision at25 has already been found. Thus the script alone did not certify that23 and24 have no collision. My independent enumeration of every weight1–25 fills this gap and confirms that25 really is the first. The development does not rely on minimality, so the gap does not invalidate its example.

## Source verification and bibliography

Fuchs, D., & Wilmarth, C. (2010). Laplacian spectrum for the nilpotent Kac–Moody Lie algebras. *Pacific Journal of Mathematics,247*(2),323–334. https://doi.org/10.2140/pjm.2010.247.323

Opened and read the publisher's complete PDF, especially the definition of the metric and weight grading, Theorem2 onp.324, and the surrounding attribution to Gel'fand–Feigin–Fuchs1978 and Weinstein1993:

https://msp.org/pjm/2010/247-2/pjm-v247-n2-p04-p.pdf

The PDF itself confirms the exact title, authors, October2010 issue, first printed page323, final printed page334 and receipt on5December2008. The DOI was independently confirmed in the opened Fuchs collected bibliography, entry162:

https://celebratio.org/Fuchs_DB/article/941/

The notebook's P785 image was also visually inspected. It explicitly forms C_(∗,n) by summing the exterior degrees and then says that the number of **different** eigenvalues equals the number of gap-three decompositions. Thus the correction concerns the notebook's actual total-weight statement; it is not based on mistakenly reading a degree-specific multiplicity statement as a total one.

## Exact published multiplicity rule

For an increasing positive-integer sequence I=(i1,…,ir) whose adjacent gaps are at least3, define

E(I)=Σ_s binom(i_s,3)−Σ_(s<t)i_s i_t.

The exponent α(I) is the sum of:

- 1 if i1≥3, otherwise0;
- 1 for each adjacent gap strictly greater than3, otherwise0.

Theorem2 gives contribution **2^α(I)** to the spectrum on the total chain complex. It explicitly instructs the reader to add these contributions when different sequences yield the same numerical energy. This is the formula implemented by `expected`; its integer threshold and strict-gap test match the published definition exactly.

The multiplicity is total across exterior degrees. It is not a claim that each contributing partition lies in a single eigenspace of dimension2^α inside its own exterior degree. The development's use of “total multiplicities” is therefore essential and correct.

## The weight25 collision

Both sequences have weight25 and adjacent gaps at least3:

| Sequence | Adjacent gaps | α | E | Contribution |
|---|---|---:|---:|---:|
| (1,10,14) |9,4|2|320|4|
| (3,7,15) |4,8|3|320|8|

For the first, E=0+120+364−(10+14+140)=320. For the second, E=1+35+455−(21+45+105)=320. The arithmetic and the two multiplicities in the development are correct.

Independent enumeration found36 gap-three labels and35 distinct numerical energies at weight25; the pair above is its only collision. The sum of all spectral multiplicities is142, equal to the number of partitions of25 into distinct positive parts and hence the dimension of the full weight25 exterior complex.

The independently computed nullities of Δ_q−320I are:

| Exterior degree q | Dimension of C_(q,25) | Multiplicity of320 |
|---:|---:|---:|
|1|1|0|
|2|12|0|
|3|40|2|
|4|54|5|
|5|30|4|
|6|5|1|
| **Total** | **142** | **12** |

These agree with every corresponding degree block in the saved output. The claim “multiplicity12” is therefore correct as a total-weight claim and would be incorrect if understood as a single-degree multiplicity.

## Boundary and Laplacian implementation

The code's ordered basis consists of increasing tuples of distinct positive indices with the specified weight. These are precisely the increasing wedge monomials declared orthonormal. The recursive partition function respects the required weight and strict increase.

For zero-based positions i<j, the boundary first places the bracket at the front with sign(−1)^(i+j−1), then moves its index into the increasing order. The additional count of remaining indices less than the merged index is exactly the number of swaps needed. Its coefficient I[j]−I[i] matches the bracket convention [e_a,e_b]=(b−a)e_(a+b). A repeated index is correctly discarded because the wedge vanishes.

For each positive weight, degree0 is empty, and the code constructs the zero maps below and above the occupied complex with the correct shapes. It checks consecutive boundary products and forms

Δ_q=d_q^T d_q+d_(q+1)d_(q+1)^T.

Because the basis is orthonormal, transpose is the required adjoint. Characteristic polynomials and their factorization are carried out over exact integer/rational arithmetic. The code requires every factor to be linear and every root to be a nonnegative integer. Multiplicities are taken from exact factor exponents; no floating-point diagonalization or rounding is used.

The second algorithm evaluates the published gap formula without using boundary coefficients. It shares the elementary recursive partition generator with the first algorithm, so it is independent of the boundary construction but not of every utility function. The development's narrower statement that it shares no boundary-matrix code is accurate. My review additionally used `itertools.combinations` rather than that recursive generator to remove this shared enumeration dependency.

## Scope of the saved checks

The full characteristic-polynomial computations cover **all nonempty exterior degrees at weights1–22 and25**, exactly as listed in the output and development. Weights23,24 and26 are not part of that full spectral run.

The harmonic-vector loop checks both shiftsa=1,2 in exterior degreesq=1,…,4. The eight weights are1,2,5,7,12,15,22,26. In particular, the degree4, shift2 vector is checked at weight26 even though a full weight26 spectrum is not factored. The saved output records nonzero coefficient counts1,1,2,2,5,5,16,16; these are nonzero vectors, so the harmonic assertions are not vacuous.

Extracting coefficients at strictly increasing exponent tuples is consistent with identifying alternating polynomials with exterior vectors. The Vandermonde cube is alternating, and multiplication by the symmetric product of the variables to powera preserves that property. An overall normalization of the alternating-polynomial identification would not affect vanishing of the boundary or adjoint boundary.

As a separate small check, in exterior degree2 the two vectors are

−e1∧e4+3e2∧e3, and −e2∧e5+3e3∧e4.

My independent boundary construction annihilates both, and its adjoint upward boundary also annihilates both. This checks the coefficient/sign convention directly. I did not repeat every degree3 and degree4 polynomial expansion; the inspected original implementation and saved output support those finite checks.

## Independent targeted audit files

- `laplacian_review_check.py` does not import the chapter's implementation. It uses combinations for partition enumeration; bracket insertion at the original first position plus a full inversion count for the alternating sign; and exact DomainMatrix rank at eigenvalue320.
- `laplacian_review_checks.json` records the successful results: all weight1–25 gap enumerations, agreement of all saved aggregate spectra and block dimensions, the six exact weight25 nullities, and the two independent degree2 harmonic checks.

This targeted audit avoided rerunning the expensive complete family of characteristic-polynomial factorizations. Its matrix calculations independently verify the correction's decisive weight25 multiplicity. The general all-weight spectrum remains a cited published theorem, not something inferred from the finite check.

## Recommended disposition

Retain the development's mathematical claims. Correct the bibliography and qualify the report's aggregate-versus-degree comparison. Repair or rename the script's minimality field if desired; the additional independent enumeration now supplies the missing evidence for its actual value. The notebook's distinct-eigenvalue count is a faithful mathematical error, confirmed both by the scan and the exact collision, while the eigenvalue formula itself is correctly recognized.
