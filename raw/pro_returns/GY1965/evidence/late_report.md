# Late-record audit: records 81–89

**Status date: 9 November 2026.** This part covers all nine catalogued records from the first Agranovich lecture to the final Minlos paragraph. It supplies **83 mathematical occurrences: 16 A, 64 E, and 3 F**. There are no B, C, or D items in this part. One definite problem has final ID **GP-1965-09** after assembly. One genuine transcription/translation correction is entered in the CSV. Mathematical errors already present in the handwriting are assessed and annotated separately.

The deliverables are `late_talks.json`, `late_items.json`, `late_problems.json`, `late_corrections.csv`, `late_references.bib`, this report, and `late_evidence.json`. The independent derivations are in `late_math_checks.tex`; reproducible exact arithmetic and its output are in `late_checks.py` and `late_checks.txt`. The structured-data generator `late_build.py` saves checkpoints record by record and then restores physical source order. All references are keyed in the accompanying bibliography.

## 1. Coverage, boundaries, and counts

The English and Russian transcriptions were compared. Every scan P000125–P000139 was inspected, with the end of P000124 checked for the preceding record's boundary. The catalog's page ranges include overlap and padding. Those ranges must not be mistaken for exact mathematical-content boundaries.

| Record | Catalog range | Actual content | Boundary evidence | Items |
|---|---|---|---|---:|
| 81, Agranovich, 14 February | P000123–P000129 | P000125–P000128 | Dated heading on P125; ends above Gelfand on P128 | 20 |
| 82, Gelfand, 21 February | P000127–P000133 | P000128–P000132 | Starts in lower P128; ends at cancelled calculation before Karpelevich | 10 |
| 83, Karpelevich, 21 February | P000131–P000134 | P000132–P000133 | Final elliptic quadrature continues at top of P133 | 6 |
| 84, Agranovich, 28 February | P000132–P000138 | P000133–P000136 | Dated continuation on P133; stops before Kirillov heading | 20 |
| 85, Kirillov, 28 February | P000136–P000139 | P000137–P000138 | Maximal-torus conclusion precedes March date on P138 | 15 |
| 86, Borovikov and Gelfand comment, 21 March | P000137–P000139 | P000138 | Boundary-cosine formula and following slice-area comment | 2 |
| 87, Lidskii, 21 March | P000137–P000139 | P000138 | Zero-zeta paragraph under Lidskii heading | 4 |
| 89, Gindikin, 21 March | P000137–P000139 | P000138–P000139 | Starts at bottom of P138; continuation before boxed Minlos heading | 4 |
| 88, Minlos, 21 March | P000137–P000139 | P000139 | Boxed Minlos heading and lattice-gas paragraph | 2 |

The source order is **81, 82, 83, 84, 85, 86, 87, 89, 88**. In particular, the catalog numbering puts Minlos before Gindikin, whereas the handwriting puts Gindikin first. A no-TikZ extraction removes the boxed Minlos heading, so the scan is decisive. The isolated random-walk sentence stands above that heading. It is provisionally kept with record 89, with explicit attribution uncertainty.

All nine records have dates and identifiable mathematical material, even where the surviving record is very brief; therefore they are entered as talks. No heading or plan is silently dropped.

### Counts by class and by primary catalog speaker

| Class | Meaning | Count |
|---|---|---:|
| A | Published soon after by the speaker or Gelfand | 16 |
| B | Developed by others | 0 |
| C | Partly developed, with a definite remainder | 0 |
| D | Not developed after a documented search | 0 |
| E | Established before the talk | 64 |
| F | Insufficiently identifiable | 3 |
| **Total** | | **83** |

| Primary record speaker | Items |
|---|---:|
| M. S. Agranovich | 40 |
| I. M. Gelfand | 10 |
| F. I. Karpelevich | 6 |
| A. A. Kirillov | 15 |
| V. A. Borovikov | 2 |
| V. B. Lidskii | 4 |
| S. G. Gindikin | 4 |
| R. A. Minlos | 2 |

The speaker table assigns all material to the primary catalog speaker of its record. It therefore includes Gelfand's explicit interjection in record 81 and explicit comment in record 86 under those host records. The individual occurrence notes preserve the speaker attribution.

### Counts by area

| Area | Items |
|---|---:|
| Pseudodifferential operators | 40 |
| Integral geometry | 12 |
| Algebraic groups | 15 |
| Classical mechanics and elliptic functions | 6 |
| Entire functions and spectral zeta functions | 4 |
| Partial differential equations and cone semigroups | 3 |
| Probability and diffusion | 1 |
| Statistical mechanics | 2 |

The assessment totals are 69 exact publication matches, 11 partial matches, two thematic matches, and one with no identified match. Verification fields read: 76 “read the result,” four “publisher metadata checked,” and three “unresolved lead.” These counts describe the occurrence's principal supporting result; the evidence ledger separately records the reading level of every cited work. A supporting historical citation is not thereby promoted from metadata-only to full-text verification.

## 2. Agranovich: substantial exposition, with source errors to disentangle

Records 81 and 84 are largely E. Agranovich's 1965 survey, Kohn and Nirenberg's 1965 calculus paper, Hörmander's 1965 article, and Seeley's 1965 paper all precede the February 1966 lectures. The strongest result-level verification here comes from Agranovich's original survey and the complete Russian translation of Seeley. Kohn–Nirenberg and Hörmander were verified at publisher-metadata level; they are not used to certify a theorem whose full statement was not read.

Record 81 is split into the quantization definition, basic examples, negative-order regularization, harmonic kernels, cancellation and multiplication, the Fourier-side representation, rough-symbol caveats, Sobolev order, the angular boundedness criterion and its proof, its endpoint interpretation, the kernel version, the Riesz example, a complementary base-derivative criterion, composition, pseudolocality, left/right quantizations, adjoints, Gelfand's unresolved algebra question, and the cotangent symbol.

Agranovich's Proposition 7.1 and Remark 7.1 give the relevant angular threshold. The corrected Schwarz–Plancherel estimate is
\[
 \|Au\|_2^2\le C M\|u\|_2^2
 \sum_m(1+m)^{n-2-2q},\qquad 2q>n-1.
\]
The estimate uses no base-variable regularity. The source's nearby claim that no frequency smoothness is needed cannot literally describe this angular criterion. It is treated as a notebook variable slip, not as a newly discovered theorem. The later, separate compact-base-support argument really does remove angular regularity.

Other substantive repairs are the missing multiplication term in a principal-value representation, the impossible compact support in frequency of a nonzero homogeneous remainder, the missing factor and reversed weights in the displayed estimate, and the need to distinguish local smoothing from one-order improvement. These are mathematical annotations because the scans agree with the problematic handwriting.

Record 84 separately covers the calculus, manifold construction, symbol realization, Sobolev mapping, elliptic Fredholm theory and its converse, parametrices, regularity, index stability, order reduction, Seeley's degree formula, external products, and the oscillatory characterization. Its most consequential qualifications are:

- A vanishing principal symbol does not annihilate an arbitrary full operator; a nonzero smooth-kernel operator is a counterexample.
- The Fredholm equivalence requires a closed compact manifold, with the appropriate bundles and Sobolev spaces.
- The order shift missing from the mapping line must be restored.
- The regularity argument uses the left-parametrix remainder acting on the unknown, not the source's displayed remainder acting on the right-hand side.
- A localized high-frequency test requires shrinking support or a second localization limit; a fixed bump alone does not freeze a variable symbol.
- Seeley's degree formula is a precise equivalence for systems on trivial bundles, with a global matrix-valued symbol and chosen orientations. Appendix A.3, Theorem 2 of the verified translation gives the exact rank condition and the boundary example (Seeley, 1965/1967).
- The product with multiplicative index is the elliptic external product, not ordinary operator composition.

The oscillatory characterization remains a partial match: the exact converse for the notebook's general decreasing sequence of exponents has not been checked from Hörmander's full 1965 theorem.

The F item 1965-81.19 is Gelfand's sentence about replacing polynomials while retaining the same algebra. The objects to be replaced, replacement class, and equivalence of algebras are all missing. Modern pseudodifferential terminology does not license choosing one of several possible questions for him.

## 3. Gelfand's affine-plane transform: an exact later publication with narrower quantifiers

The close publication is Gel'fand, Graev, and Shapiro (1967), *Integral geometry on k-dimensional planes*. Its differential-form construction, range theorem, and cycle inversion closely match record 82. The ten occurrences keep the geometric definitions, polarized determinant, form construction, two theorem claims, current identity, coordinate chart, and incomplete calculation separate.

Two restrictions change the mathematical assessment:

1. The published range theorem uses its rapidly decreasing smooth class and **k < n − 1**. It explicitly excludes the hyperplane case. Closedness of a top-degree form cannot replace global hyperplane moment conditions. The relevant statement is Theorem 1, Russian p. 23, together with its footnotes.
2. Complex inversion has a **suitable cycle with nonzero coefficient**. It does not give a nonzero coefficient for every cycle. The zero or null-homologous class already refutes that universal reading. The exact result is Theorem 2 and its computation, Russian pp. 29–31.

The real k-form and complex (k,k)-form are distinguished, as are the corresponding real cycle dimensions k and 2k. Plane-volume weights and chart redundancies are specified rather than silently suppressed.

The provisional problem GP-1965-09 links the initial reconstruction question to the range and cycle statements. It is resolved within those published hypotheses; it is not labelled as a currently open problem about arbitrary smaller measurement families. The final cancelled line on P000132 is F, even though the surrounding method is known. Gel'fand, Graev, and Shapiro (1969) supplies thematic context but cannot restore an erased equality.

## 4. Karpelevich: exact algebra detects a factor-of-two error

The historical subject is Klein's Princeton lectures, published in 1897. The six occurrences are E: Euler angles, the projective SU(2) description, the recorded Lagrangian, momenta, cubic reduction, and elliptic quadrature.

The scan really contains the two extraneous factors 2 in the cyclic momenta. For the specific equal-inertia normalized kinetic energy written there, differentiating the Lagrangian gives
\[
 n=\dot\varphi+u\dot\psi,\qquad
 e=\dot\psi+u\dot\varphi,\qquad u=\cos\theta.
\]
Consequently,
\[
 \dot u^2
 =2(h-pu)(1-u^2)-n^2-e^2+2neu
 =2pu^3-2hu^2+2(ne-p)u+2h-n^2-e^2.
\]
This is a supplied computation, explicitly marked as such. It is not an invented completion of the handwritten polynomial and does not substitute the general two-inertia symmetric-top model for the displayed one.

A complete elimination is in `late_math_checks.tex`. Exact polynomial arithmetic in `late_checks.py` verifies both momentum identities and the cubic. The parent reviewer independently reproduced these identities in `code/check_annotations.py`. The physical interval and nonnegativity conditions are stated, and multiple-root or degree-drop limits are separated from the nonsingular elliptic case.

## 5. Kirillov: algebraic groups with field and connectedness restored

Record 85 is an exposition related to Borel and Tits (1965), with elementary algebraic-geometric and Chevalley background. Milne (2017) was read for modern exact hypotheses, especially the Barsotti–Chevalley theorem and complete connected groups.

The fifteen items separate schemes, primes in the affine plane, the group definition, Chevalley structure, abelian varieties, homomorphisms, the false torus claim, additive/multiplicative groups, solvable series, radicals, reductivity/semisimplicity, GL/SL, root-system types, a nonsplit real torus, and conjugacy.

The main repairs are substantive. The list of prime ideals omits the zero ideal. An algebraic torus of positive dimension is not an abelian variety. Connectedness is needed in the affine-to-abelian homomorphism statement. Chevalley structure is stated for smooth connected groups over a perfect field. The classical families and exceptional types classify simple root-system types; they do not by themselves classify every group form or central quotient. Maximal tori over an algebraic closure are conjugate, and maximal split tori over the ground field are conjugate under rational points; arbitrary real maximal tori need not be. Borel and Tits's Section 11 supports the split-torus statement.

The handwritten SGL is interpreted as SL, but no invented group is defined. None of these elementary source errors creates a research problem.

## 6. The four short March records

### Borovikov and Gelfand

The boundary-cosine identity in record 86 is correct under the supplied convexity and angle conventions:
\[
 \iint_{\partial K\times\partial K}c_Mc_N\,ds_Mds_N=2\pi|K|.
\]
There is **no missing distance denominator**. For a chord of length l, line coordinates satisfy
\[
 |dp\,d\theta|=\frac{c_Mc_N}{l}\,ds_Mds_N.
\]
Ordered endpoint pairs cover unoriented lines twice, so the original integrand becomes twice chord length integrated over lines; Fubini gives the stated constant. A second independent proof applies the divergence theorem first in the second endpoint, then uses the flux of the logarithmic potential about an interior point. Both complete proofs and a circle check are included and marked as supplied here. The parent reviewer independently checked both proofs, including endpoint signs, the Jacobian multiplicity, the integrable singularity and removed-arc limit, and the final logarithmic flux. A separate 257-point circle quadrature at three radii also confirms the normalization to floating-point precision; it is a check, not a substitute for the proofs.

Santaló's line-space framework is verified from the 1989 chapter, Section 1.2; the 1953 book's metadata establishes the earlier setting. An exact Borovikov publication or priority claim was not verified. The match is therefore partial and confidence medium, despite the independent proof of the formula. No D classification is inferred from the unsuccessful name search.

Gelfand's next one-line formula is F as a historical identification and false under the fixed-direction reading. For an ellipsoid sliced perpendicular to its c-axis,
\[
 \frac{\int |S'(t)|^2dt}{V}=\frac{2\pi ab}{c^2}.
\]
Thus no universal constant can multiply the one-direction integral to give every volume. The averaged identity
\[
 \int_{S^2}\int_{\mathbb R}|\partial_tRf(\omega,t)|^2dt\,d\omega
 =8\pi^2\|f\|_2^2
\]
is proved here from Fourier slice and Plancherel, with ordinary sphere area and plane area. It is offered as a possible repair, not attributed to the missing words of the notebook. The source explicitly calls M a universal constant. Both the counterexample and averaged constant were independently checked by the parent reviewer.

### Lidskii

The exact match is Lidskii and Sadovnichii (1967), *Regularized sums of zeros of a class of entire functions*. The original class K, contour conventions, and Lemmas 2–3 were read. Four A items separate complete sectorial asymptotics, the all-zero sum and branch, entire continuation, and the sine example. A formal Laurent series or arbitrary entire function is insufficient; finite asymptotics only give the corresponding half-plane continuation.

For the illustrative entire function sin(πz)/z and a compatible branch, the all-zero sum is
\[
 (1+e^{-i\pi s})\zeta_{\mathrm R}(s).
\]
The prefactor cancels the pole at s = 1. A sum only over positive zeros retains the pole. This explicit branch calculation is marked as our reconstruction of the compressed remark.

### Gindikin

This search materially improved after reading the Russian terminology and the scans. The initial strongly homogeneous Cauchy-problem paper was only a broad lead. The exact later announcement is Gindikin (1967), *A generalization of parabolic differential operators to the case of multi-dimensional time*, Doklady 173(3), 499–502.

The full four-page paper was read. Section 3 and Theorem 4 identify the V-elliptic homogeneous map and construction from a hyperbolic time polynomial; Theorem 5 and Section 4 give the associated cone-parameter semigroup and parabolic evolutions on rays. These three occurrences are A. Volevich and Gindikin (1969), introduction and Theorem 1.1, document a later variable-coefficient development.

The P000138 scan reads **любой гиперб. оператор**, corroborated by **гиперб. полином** on P000139. The Russian and English transcriptions instead say pseudo-operator. The parent independently rechecked this reading. It is the one genuine transcription correction in the CSV, and it greatly strengthens the 1967 match.

The isolated random-walk sentence is E under the minimal diffusive interpretation. Donsker's original-paper metadata was checked, but its full proof was not read. The walk law, scaling, and exact speaker are not supplied by the notebook.

### Minlos

The two E items are the finite-volume lattice-gas definition and the pressure limit. The sign in the displayed Boltzmann weight is retained: for positive β, a positive occupied-neighbor energy penalizes such pairs. It is not automatically a ferromagnetic convention. The external normalization in the grand-canonical sum must be the number of lattice sites, since the particle number varies across configurations.

Fisher (1964) provides a checked historical thermodynamic-limit reference at abstract/metadata level, not a fully read proof for the precise finite-state lattice reconstruction. The exact statement is therefore a partial match. The previous index already has lattice-gas and thermodynamic-limit occurrences 1964-3.1 and 1964-3.2. These are acknowledged without manufacturing another problem ID or adding phase-transition claims.

## 7. What the classifications miss, and integration recommendations

The A–F classes describe historical fate but cannot alone describe correctness. An E exposition can contain a false literal formula, and an A exact publication match may require a lost hypothesis or an existential quantifier. Conversely, F can mean an erased or underspecified historical statement even when a plausible repaired mathematical statement is elementary and provable. The separate correctness, match, verification, and confidence fields are therefore essential.

No C or D item here has both a precise surviving question and a credible bounded research contribution. The three F items should not be relabelled D merely because their exact publications were not found. The supplied proofs and counterexamples are critical annotations and verification, not claims to solve new problems. Each is marked with `\ours` or `\oursComputed` in the relevant reconstruction or theorem environment.

The evidence ledger is intentionally per source as well as per occurrence. A BibTeX `verified` note means that its citation URL or DOI was opened; it does not mean that every cited paper was read in full. The direct Seeley PDF route did not succeed, but the complete translation supplied the needed theorem. The Hörmander generalized-exponent converse, exact Borovikov attribution, Donsker proof, and exact Fisher lattice theorem retain their stated limits.

For final assembly, preserve physical source order, renumber GP-1965-09, include the independent derivations as annotations, and retain the one genuine transcription correction separately from the source's mathematical errors. The format would benefit from a permanent field distinguishing catalog page range from exact content range, and from a per-reference reading-level field in addition to the coarse BibTeX flag. This ledger supplies both without altering the prescribed JSON schema.

