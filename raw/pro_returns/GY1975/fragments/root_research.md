# Integration and independent development log

## Source inspection

- Directly inspected the attached PNGs P000655 and P000656. The former has the two negative-weight factors, the Weyl-factor pair and the first positive row. It also switches between chi and chi-star around the factorization by H(S^3).
- P000656 visibly prints the count 57, the coefficient 10 at weight70, and an ambiguous middle t exponent in the general row. The corrected uniform exponent ell is a mathematical emendation supported by the weight rule, not a claimed certain decipherment of the handwriting.
- The reference to W_n within the larger Hamiltonian complex must not be read as saying the known cohomology of formal vector fields was still wholly uncomputed in1976.

## Development decision

GP-1975-20 is precise and permits a bounded, independently checkable contribution. The work supplies a formal truncation proof, exact finite computation, correction of the absolute/relative ambiguity, and finite cohomological lower bounds. No claim to solve infinite nonvanishing or to have computed cocycle representatives is made.

Two independent exact algorithms were implemented: descending multiplication of exterior factors, and a logarithmic-derivative divisor recurrence. All Laurent coefficients, not just the final Euler coefficients, agree. Separate m40, m90, and m150 runs agree on overlapping prefixes. The true positive-product cutoff is 2m+2, because there are two negative-degree factors.

## Literature and search limits

Opened and read Mohammadzadeh--Fuchs2014, Sections1--2 and4, with locators in root_sources.json. It explicitly retains the infinite question and tabulates through129. Opened Morita--Sakasai--Suzuki2015 and screened its stable-rank graph-homology questions; these do not resolve the fixed-rank question. Opened Mikami--Kodama--Nakae arXiv1210.1662 abstract; its omission of constant fields changes the algebra. Searched both web engines with exact-title, author, Perchik/Euler/infinite-nonzero strings and a recent2024--2026 query. The results did not establish a later resolution. A 2026 H_2 action in a P=W proof is about a different cohomological problem and was not treated as a solution.

The retrieved2014 PDF text gives E(86)=-2204, whereas both independently implemented algorithms give -22044. A rendered PDF image was not returned by the web screenshot service, and the ordinary public PDF request returnedHTTP403. This is therefore retained as an extraction discrepancy pending visual confirmation, not declared a printed erratum.

## Typesetting environment

The installed XeTeX engine lacked a discoverable format because the installed distribution's filename database was absent. No packages were downloaded and no system paths were edited. A workspace-local format was generated from the existing TeX tree, and process-local TEXMF paths allow normal XeLaTeX and BibTeX commands. The reproducible wrapper is code/build_pdf.py. The supplied chapter builder and style are retained.

## Roiter identification and independent check

A narrow search for the arithmetic divisibility criterion first returned only general root-system results. A broader exact-topic search located Mróz and Zając (2022), DOI 10.1016/j.laa.2022.06.007. Its publisher abstract refers to Roiter's 1978 problem. Following that lead located the primary Roiter paper, Math-Net tm2511. The complete Russian text was opened and read. Condition (*) is q(x)>0 together with q(x) dividing a_i x_i for every coordinate. Proposition 4 covers forms positive on every proper coordinate subspace; this includes finite and affine Dynkin forms. Lemma 6 supplies that positivity for a connected classical nonnegative form. No arbitrary indefinite extension is inferred. This turns occurrence1975-388.6 from a provisional identification gap into an exact publication match, class A.

As an independent check in the positive-definite classic case, the divisibility condition is invariant under integral reflections. Writing a candidate as x=u−v with disjoint nonnegative supports shows that d=q(x) divides both q(u) and q(v). Since cross terms are nonpositive, both u and v nonzero would imply d=q(x)≥2d, a contradiction. Thus the vector has one sign. After negating if needed, choose a reflection with positive root pairing; it reduces the sum of coordinates while preserving nonnegativity unless the support has one element. At the final vector k e_i, a_i k² dividing a_i k forces k=1. This re-derivation checks the finite statement without assuming a classification list. It is not offered as a new result or as a proof of the wider theorem.

## Spectral-phase bounded development

Inspected the complete P000652 scan. The epsilon factor, zero-mode subtraction, and generic length wording are visible. Distinctness and incommensurability need a primitive unoriented convention because iterates automatically violate the literal unrestricted wording. The small-divisor requirement is actually written in the source and must not be called a wholly omitted hypothesis.

The added development proves a Fourier distributional-convergence criterion, the exact circle limit, and a sphere counterexample outside the generic-geodesic hypotheses. The Fourier normalization was independently checked by pairing the atomic comb and by grouping circle modes into residue classes. The sphere estimate was checked by rationalizing the difference sqrt(l(l+1))−(l+1/2) and summing the main geometric derivative exactly. Numerical checks agree with the circle closed formula to maximum error8.92e-15; they are explicitly diagnostics, not interval-arithmetic certificates. The sphere scaled first coefficient tends toward−1/pi as predicted.

The original Zelditch PDF and metadata were opened: publication1998 and repository deposit2000, not the reverse. Duistermaat–Guillemin1975 was checked at publisher-metadata level; the local expansion used in the discussion was read in Zelditch. No new assertion of global convergence under the notebook's general hypotheses is made.

## Independent mathematical review

The reviewer of the final block independently checked both development files and the finite Roiter descent. No mathematical error was found. One terminology correction was made: the symmetric-power component has Hamiltonian weight ell and polynomial degree ell+2. The reviewer separately verified the Euler cutoff, Weyl projection, parity, recurrence, support bound, and finite-dimensional lower bounds; and the spectral Fourier normalization, circle comb mass, uniform bound, and sphere remainder. The sphere's failure of the generic hypotheses is retained explicitly.

## Correction-table typesetting

Some authoring fragments expressed formulas as plain-text transliterations. Root supplied math delimiters and mathematical symbols for the central formulas without changing their assessments. Remaining literal transliterations have TeX special characters escaped outside marked math spans. The formatting overrides are recorded in root_correction_formatting.json and applied reproducibly by the assembly script.

## Further independent checks of supplied elementary arguments

The final block's marked calculations were re-derived independently during integration. Lagrange inversion of exp(x0(T−1)), with T=z exp(alpha(T−1)), gives the displayed generalized Poisson probabilities for n≥1 and the n=0 atom exp(−x0); monotone iteration selects the mass-one subcritical branch. The composition-length bound follows by iterating the cited inclusion bound along a Gabriel–Roiter filtration. Completing the star-form squares gives the sign change at four leaves. The three orbit amplitudes follow from multiplying the reciprocal multiplier factors; negative hyperbolic odd iterates give cosh rather than a mere alternating sign. The Abel delta-comb coefficient is the displayed geometric series, with a uniform polynomial bound under the stated small-divisor hypothesis.

For the Hamiltonian complex, continuous finite-jet cochains have finite support in the grading, and the finite exterior powers of the negative and zero weights bound the number of positive-weight factors at a fixed total weight. Cartan's homotopy identity kills a nonzero diagonal-weight eigenspace. The inverse-metric variation, the Maxwell stress sign for (+---), the two perfect-fluid projections, and the rest-frame sound-wave linearization were checked algebraically. Differentiating UV=(1−r/r_s)exp(r/r_s) at r=r_s gives the coefficient −r_s/e in the bifurcation expansion. Composing translations by d_i c_i Y gives translation by Y when the coefficients sum to one; the substantive unit-ideal construction remains a cited input. These checks support the restricted statements; they do not upgrade their publication matches or turn them into new research results.
