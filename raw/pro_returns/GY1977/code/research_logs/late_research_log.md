# Late-record research and verification log

Status cutoff: **10 November 2026**. Assigned catalogue envelopes: **438–445, 451, 457**. The supplied catalogue dates remain in `talk.date`; source dates and adjacent speakers are recorded explicitly in summaries, occurrence overrides, and provenance corrections. The source cohort is not a homogeneous chronological academic year.

## Completed checkpoint

The final checkpoint contains **10 catalogue entries and 124 mathematical occurrences**, distributed as **A 28, B 6, C 1, D 0, E 78, F 11**. Record counts are 438:17, 439:12, 440:10, 441:7, 442:10, 443:14, 444:12, 445:4, 451:13, 457:25. There are three definite indexed questions/exercises: GP-1977-40 (formal substitutions), GP-1977-41 (BGG representation of projective bundles), and GP-1977-42 (the line-bundle exercise). No open problem is inferred from an aesthetic request or an incomplete announcement.

`build_late.py` constructs and saves record-by-record checkpoints. The final machine data are `talks.json`, `items.json`, `problems.json`, `corrections.csv`, and `areas.json`. `references.bib` contains 32 local entries, while `references.json` audits all 34 cited works; the two recent formal-substitution entries belong to the parent's `work/parts/root/references.bib`. All keys used by the late items and problems have audit entries. Exact source URLs, opening evidence, verification levels and locators are in that audit, rather than hidden behind a blanket “verified” label.

## Source reading and actual boundaries

The format and task instructions, supplied catalogue, full relevant English source-page content, and Russian text at decisive formulas and doubtful readings were consulted. The late page extracts are retained as `page756.txt` through `page787.txt`, `page810.txt`–`page812.txt`, and `page823.txt`–`page831.txt`. Page 755 is absent from the attachment and is not reconstructed as though read. The preceding 753–754 pages were additionally read and coordinated with the middle-record agent.

| Envelope | Actual supplied content retained |
|---|---|
| 438 | P753–754 and P756 continue S. I. Gelfand's 13 February 1978 BGG precursor; P757–762 are the 27 February lecture. The omitted catalogue 437 is not invented as a 29th required record, and the precursor is not attributed to Faddeev. |
| 439 | P763–766: Aomoto's neutral fermions and holonomic fields, with Gelfand's initial ideal question and final Painlevé discussion. P767 belongs to the next lecture. |
| 440 | P767–771: hypergeometric arrangement integrals, local systems, discriminants, logarithmic complex, periods and fractional calculus. |
| 441 | P772–773: Buchstaber, formal substitutions and complex bordism; the explicit Diff1(Z) cohomology question is on P773. |
| 442 | P774–776: Calogero–Degasperis; lower P776 switches to V. P. Palamodov's Mathematical Society lecture of 21 March 1978 on fronts and caustics. |
| 443 | P777–781: second Calogero lecture, ending with root dynamics and Hermite matrices. |
| 444 | P782–785: Fuchs, heading 3 April 1978. Catalogue date 4 April is retained only as identifier. P785 announces the next meeting on 4 April. |
| 445 | P786–787: substantive Kruskal surreal-number lecture, despite catalogue year heading. Date reads 30 October 1978, with the month paleographically uncertain; November remains a disclosed alternative. |
| 451 | P810–811: unidentified preceding lecture on representations and cohomology. P812: dated 12 February 1979, reading programme followed by Belavin's ADHM parameter question and gauge/confinement fragment. |
| 457 | P823: preceding Beilinson ambitwistor intervention. P824–829: Fuchs, 5 March **1979**. P830–831: Ogievetsky, 19 March **1979**, super-Poincaré algebra and superspace under a “Supergravity” heading. Catalogue date 1978-03-05 is retained solely as the supplied envelope identifier. |

Scans inspected directly with the image viewer for decisive handwriting/formulas include **P761, P765, P766, P770, P773, P776, P780, P781, P785, P786, P810, P811, P812, P823, P824, P827, P828, P829, P830, P831**. The last seven have smaller view copies beside the data. These views distinguish transcription ambiguities from mathematical errors faithfully present in the manuscript. Parent/middle-agent independent source-boundary checks additionally covered P753–754 and the date headings. In particular, no missing Koszul sign, phase normalization, Bianchi sign, central extension, or supersymmetry sign was “recovered” from a mark that is not actually present.

## Search routes and results

The following lists the query families and source chains used. It is a research log, not a claim that every returned hit was read. The accompanying `references.json` is the work-by-work record of what was actually opened and inspected. Search-index extracts, publisher abstracts, primary results, and independent calculations remain separate evidence categories.

### 438 — projective bundles and Koszul duality

Queries combined **Bernstein Gelfand Gelfand algebraic bundles Pn 1978**, **BGG exterior algebra proper module**, and **Serre faisceaux algébriques cohérents 1955**. The author-hosted BGG paper was opened at <https://www.math.tau.ac.il/~bernstei/Publication_list/publication_texts/BGG-3.pdf>; definitions and both theorems were read. MathNet faa2008 supplied the 10 January 1978 receipt date. Serre's primary FAC scan was read at <https://www.college-de-france.fr/media/jean-pierre-serre/UPL5435398796951750634_Serre_FAC.pdf>. Hartshorne's publisher page <https://link.springer.com/book/10.1007/BFb0080482> verified the 1963–1964 seminar/1966 publication and derived-category chapter; its full chapter was not obtained.

Results: BGG provides the stable-module representation, not a complete explicit moduli classification. Free exterior modules produce the zero bundle. The whole doubly infinite section module need not be finitely generated, so a sufficiently high truncation is specified. The unsigned total differential and proposed unit value are retained as faithful notebook defects. A nonzero trivial module supplies the decisive counterexample to the latter.

### 439 — neutral fermions, Ising and Painlevé

Queries combined **Aomoto 1978 holonomic quantum fields neutral fermions**, **Sato Miwa Jimbo Holonomic quantum fields I IV**, **Wu McCoy Tracy Barouch Ising 1976**, and **Garnier 1912 four singular points Painlevé VI**. The 1978 Sato–Miwa–Jimbo publisher abstract was opened; the complete 1979 part IV at <https://ems.press/content/serial-article-files/41996> was read in its neutral-field, twist and deformation sections. The APS Ising record <https://journals.aps.org/prb/abstract/10.1103/PhysRevB.13.316> establishes the original 1976 paper and the fourth author Barouch; its author-hosted scan was opened but not read at formula level.

Garnier's large primary file initially exceeded web-reader limits. A later direct retrieval of <https://www.numdam.org/article/ASENS_1912_3_29__1_0.pdf> succeeded (16,299,060 bytes), and the introduction pp. 1–6 was read locally. Pages 2–3 distinguish meromorphy from absence of all movable poles and state the restricted classification; p. 5 explicitly describes four essential singular points and one apparent point yielding VI. The notebook's full coefficient dictionary and crossed-out sign remain unchecked. The algebraic expression missing its differential operator cannot replace the Dirac equation.

### 440 — arrangement local systems

Queries combined **Aomoto vanishing cohomology many valued meromorphic functions 1975**, **Aomoto structure integrals power product linear functions 1977**, and **Esnault Schechtman Viehweg local systems hyperplanes erratum**. Aomoto 1975 was read at <https://www.jstage.jst.go.jp/article/jmath1948/27/2/27_2_248/_pdf>, including the boundary and critical-point assumptions. The closer 1977 repository file <https://repository.dl.itc.u-tokyo.ac.jp/record/41043/files/scp027007.pdf> repeatedly returned 429/503; only indexed excerpts and bibliographic leads were available. That entry is explicitly **unverified**, and no exact theorem-level match is claimed from the index alone.

The original Esnault–Schechtman–Viehweg 1992 paper and **separate** 1993 erratum were read from the author's website, including rendered pages 558–559 and the erratum page 447. The erratum repairs a subspace dimension and does not invalidate the theorem/corollary proof. Zero residues satisfy the notebook's strictly-positive-integer exclusion but yield nonzero H0; this is a direct counterexample to the literal concentration assertion. The Euler-characteristic sign is an independent omission.

### 441 — formal substitutions and bordism

Queries combined **Buchstaber Shokurov Landweber Novikov formal vector fields 1978**, **Diff1 Z cohomology formal power series integer**, **Babenko Bogatyi 2008 substitutions**, and **Pavez Cornejo abelianization formal power series**. MathNet faa2000 and its full Russian primary text establish the 1978 result and May 1977 submission. The exact statement concerns the Landweber–Novikov subalgebra and its integral operator lattice, not arbitrary natural operations or a naive integral enveloping algebra.

The parent independently read the full Babenko–Bogatyi and Pavez-Cornejo sources. **Babenko–Bogatyi Theorem 1.2 is the closed-commutator abelianization; Theorem 1.5 is real cohomology with uniformly locally constant supports.** Pavez-Cornejo's 2024 preprint/2025 publication also uses closure in its commutator convention. Neither permits identifying ordinary abstract abelianization. The original question leaves coefficients/topology unstated. Its real finite-jet version has a solution; the item is C only for the explicitly chosen integral/full-ring refinement. Parent's development proves bounded integral finite-jet consequences, not the whole integral ring and not unrestricted abstract group cohomology.

### 442–443 — spectral transforms and solvable root systems

Queries combined **Calogero Degasperis extension spectral transform 1978**, **conservation laws classes nonlinear evolution equations spectral transform 1978**, **Calogero Degasperis nonlinear evolution equations inverse spectral transform 1976**, **Calogero motion poles zeros special solutions 1978 Hermite**, and the actual operator/Bäcklund formulas. Springer primary publisher records verified the publications, received dates, and, for the 1978 extension, a June 1977 Rome precursor in its editorial footnote. The full Calogero papers were not obtained. Accordingly formula-level publication matching is partial, even where the notebook equation can be verified independently.

Independent exact work identifies the factor-of-two phase error, moment weights 2n+1, the Bianchi denominator order, and the missing identity matrix in the Hermite linearization. Scattering reflection alone does not determine discrete bound-state data. Arbitrary functions of differential operators require a domain/functional calculus. The adjacent Palamodov front fragment does not support a universal 4/3 law; its unspecified geometric model remains F. No D classification is inferred from unsuccessful searches for that fragment.

### 444 — positive Witt cohomology and Laplacians

Queries combined **Gelfand Feigin Fuchs cohomology Laplace operators 1978**, **Goncharova cohomology formal vector fields line 1973**, **Fuchs Wilmarth Laplacian spectrum nilpotent Kac Moody 2010**, and **Weinstein correction 1993 Laplace L1**. Full Russian primary texts at MathNet faa2023 and faa2411 were opened and read. The exact 2010 MSP paper <https://msp.org/pjm/2010/247-2/pjm-v247-n2-p04-p.pdf> has title *Laplacian spectrum for the nilpotent Kac–Moody Lie algebras*, volume 247(2), pp. 323–334, DOI 10.2140/pjm.2010.247.323; Theorem 2 is on p. 324.

The parent independently constructed exact finite-weight Chevalley–Eilenberg matrices, checked the corrected spectrum through weight 22, verified the displayed harmonic chains in low degrees, and checked the first partition-label collision at weight 25. Labels (1,10,14) and (3,7,15) both give E=320; the multiplicities add to 12. Hence “distinct eigenvalues = number of labels” is false, even after repairing the eigenvalue formula. The parent's code/output and proof accompany the assembled chapter.

### 445 — surreal numbers

Queries combined **Kruskal Conway surreal sign sequences simplicity addition** and **Conway On Numbers and Games first chapter**. The primary book excerpt at <https://sites.math.rutgers.edu/~zeilberg/EM13/onag1.pdf> was downloaded and pages rendered. Cuts, recursive addition and negation, and the uniqueness/simplicity construction were read on book pp. 4–7. The cited original publication is 1976; the opened excerpt is the 2001 second edition. The sign-sequence description is only indirectly matched to this excerpt. No question deserving speculative development is present.

### 451 — cohomology, ADHM and a gauge fragment

Queries combined **Delorme 1 cohomologie représentations unitaires 1977 affine group**, **Blanc cohomologie continue smooth vectors 1979**, **Atiyah Hitchin Drinfeld Manin construction instantons 1978 quaternion matrices 8k-3**, and **Wilson confinement 1974**. Delorme's complete primary article was read at <https://www.numdam.org/article/BSMF_1977__105__281_0.pdf>, particularly definitions, V.4, V.6 and the K-finite discussion. Author is Patrick Delorme. Blanc's primary paper at <https://www.numdam.org/article/ASENS_1979_4_12_2_137_0.pdf> gives the smooth-vector comparison in Theorem 5.2, pp. 152–153; author is Philippe Blanc. The second van Est arrow is not claimed verified under unrestricted coefficients.

The complete three-page ADHM paper was read at <https://strings.itp.ac.ru/Papers/atiyah1978.pdf>, including nondegeneracy, quaternionic reality, the equivalence group, and parameter count. Its December 1977 receipt/March 1978 publication precedes the actual February 1979 source entry. “Find a beautiful parameterization” lacks a definite success criterion, so it is not manufactured into an open problem. The final gauge lines, under Belavin's heading, imply no confinement theorem. The Wilson citation is thematic and publisher-level here.

### 457 — ambitwistors, prolongations, affine algebras and supersymmetry

Queries combined **Beilinson ambitwistor connection CP1 CP1**, **Mason Skinner ambitwistor Yang Mills third formal neighbourhood**, **Guillemin Quillen Sternberg infinite type rank one**, **Ottazzi Warhurst Singer Sternberg prolongation**, **Kac 1968 simple irreducible graded finite growth**, **Haag Lopuszanski Sohnius 1975**, and **Salam Strathdee superfields Fermi Bose symmetry 1975**.

Mason–Skinner's full primary paper <https://arxiv.org/pdf/hep-th/0510262> was read in Section 2: local correspondence, incidence-fiber assumptions, and the distinct third-formal-neighborhood field-equation condition. The older Isenberg–Yasskin–Green source was not successfully opened; its result is not independently cited as read. Guillemin–Quillen–Sternberg's original 1967 publisher metadata was opened, and the exact rank-one criterion and proof were read in the full primary Ottazzi–Warhurst article <https://www.heldermann-verlag.de/jlt/jlt21/ottala2e.pdf>, Theorem 2.3 and Sections 2.2–2.4.

Kac's full English primary text was successfully opened using <https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=rus&paperid=2519&what=fullteng>. The `eng` routing parameter sometimes redirected to metadata; it was not mistaken for a full read. Introduction, Chapter II, Chapter III Section 1, and Theorems 4–5 were read. The exact scope includes graded simplicity and finite growth; the manuscript's stronger indefinite/exponential wording was not theorem-level verified. The two omitted one-dimensional brackets and the last unqualified exhaustion claim remain F.

The complete Haag–Łopuszański–Sohnius primary article was read at <https://www.physics.mcgill.ca/~keshav/675/haag.pdf>, particularly assumptions, odd brackets, central charges and massive/massless distinctions. The APS Salam–Strathdee abstract and dates were opened at <https://journals.aps.org/prd/abstract/10.1103/PhysRevD.11.1521>; its full text required authorization. The superspace signs are instead checked by the explicit exterior-algebra calculation below. The notebook heading “Supergravity” is not evidence of a constructed supergravity action.

## Prior-index recurrence check

`work/previous_index.md` was searched for BGG, Aomoto, Garnier, Landweber, Goncharova, surreal numbers, formal vector fields, and the directly relevant 1975 occurrences. The parent's independent comparison agrees: **GP-1975-21** is the full cohomology of formal **Hamiltonian** vector fields, and **GP-1975-20** concerns Perchik's relative Euler series. Neither is the positive Witt/integral-substitution question, so neither ID is reused. Earlier Ising occurrences **1975-390.1–.4**, supergeometry **1975-389.1–.7**, and integrable many-body material **1975-372** are thematic links. **GP-1975-10** is a definite continuum confinement problem; the two unfinished gauge lines at P812 are insufficient to assert an exact recurrence. No exact earlier problem recurrence was identified for the three late-record problem entries.

## Independent calculations and second checks

`verify_emendations.py` and `verification_results.json` are reproducible exact SymPy code and output. `development.tex` gives the accompanying mathematical derivations, all explicitly marked as computed here, without novelty claims.

1. **Transmission:** the left-Jost Volterra equation, a uniform Gronwall bound, and the physical relation T=1/A give phase coefficient −c0/4 for real continuous integrable potentials. Independent exact reflectionless potential u=−2r²sech²(rx) has T=(k+ir)/(k−ir), c0=−4r. Schrödinger residual is exactly zero, and the log-T expansion agrees. **The parent's independent review caught a reciprocal error in the draft proposition's boundary normalization**: the actual notebook and the exact soliton have coefficient T, not 1/T, at negative infinity. The proposition and proof were corrected, and the code now explicitly checks the two endpoint coefficient ratios. The final −c0/4 coefficient is unchanged.
2. **Moment weights:** the operator conjugation/homogeneity proof gives 2n+1 for every defined moment. Independently c0=∫u and c1=−3∫u² by integration by parts; exact Gaussian-family integration gives weights 1 and 3 and residuals zero.
3. **Bianchi sign:** eliminating derivatives around the four Riccati edges solves for the rational upper vertex. Independently differentiating that answer and substituting into each upper edge gives two exact zero residuals.
4. **Hermite matrix:** direct differentiation of the nonlinear force gives −I−A, with no linear velocity term. Independently the invertible root/coefficient differential conjugates I+A to diag(1,…,n). The code verifies the n=3 matrix/characteristic polynomial exactly and all 36 Hermite mode identities with 1≤m≤n≤8.
5. **Periodic loop bracket:** exact 2×2 loop-matrix commutators verify all nine residue cases, including the **positive** f/2 normalization. A separate structure-constant calculation verifies all 27 Jacobi residue triples.
6. **Supertranslations:** a direct Grassmann anticommutator derivation gives −2iσ·∂. Independent 16×16 exterior-algebra matrices verify all 12 mixed/same-chirality pairs with four generic derivative symbols.

The parent additionally re-derived c1=−3∫u² and the root/PDE Hermite linearization signs independently and agreed. The run passed every assertion. Exact output groups are `transmission`, `scaling`, `Bianchi`, `Hermite`, `loop_bracket`, `supertranslations`, and the decisive elementary-counterexample descriptions. The parent's independent cohomology/Hodge computation is separate and is not relabelled as having been carried out by this script.

## Material limits retained in the data

The closer Aomoto 1977 paper remains inaccessible and explicitly unverified. Calogero article matching is at publisher/abstract level; the relevant notebook identities are checked directly. Exact parameter/sign matching to Garnier, the original 1885 Stieltjes bibliography, the Wilson attribution in the prolongation lemma, the unnamed SL2 counterexample, the infinite-dimensional prolongation example, and the final unqualified one-generator classification remain unresolved or partial. These limitations determine F/partial/indirect labels rather than being converted into evidence of an undeveloped research problem.

No chronology, theorem-level verification, exact match, or claim of openness rests on a metadata-only page. Literature dates refer to the original publication or documented manuscript/lecture circulation, not modern digitization dates. Final assembly, chapter build, PDF inspection, and the complete mixed-year statistics belong to the parent task.

## Final correction-table LaTeX repair

The supplied builder inserts correction display cells directly as LaTeX. All 42 rows were reviewed, and mathematical expressions in the place, transcription, proposed correction and evidence cells were placed in explicit math delimiters. The repair is implemented deterministically inside `build_late.py` as `repair_correction_latex`. The three plain-text mathematical reconstructions in items 1977-440.5, 1977-440.10 and 1977-443.1 were repaired as well. A scan of every correction cell and every item LaTeX field found zero unescaped underscore, caret, percent, ampersand, hash or dollar characters outside math. All correction inline-math delimiters balance. Regeneration produces identical machine-data hashes; occurrence and correction counts remain 124 and 42. Output is recorded in `latex_repair_validation.json`.
