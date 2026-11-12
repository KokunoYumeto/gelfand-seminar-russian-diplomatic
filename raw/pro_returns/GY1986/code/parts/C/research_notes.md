# Records 698–712: editorial and research audit

Status date: 12 November 2026. This is the final slice audit. The JSON data are checkpointed by `code/build_slice.py`; bilingual source extracts, the compact search index and the verification ledger are in `evidence/`.

## Source priority and boundaries

The English transcription has been read through P001329–P001384. The Russian transcription was consulted for the mathematical and attribution passages under review; complete bilingual page extracts were saved for reproducibility. This is not a claim of a new line-by-line diplomatic edition of the entire Russian transcription. Formula-sensitive passages were checked against the page scans as recorded below. Explicit manuscript speaker headings control attribution, while the catalogue dates and page spans remain in `talks.json`.

* Record 698 begins partway through P001330; P001329 belongs to the preceding Zelevinsky discussion. It ends on P001332.
* Record 699 is only the catalogue's YEAR 1987 heading, not an independent lecture.
* Record 700 starts at the dated 9 February 1987 heading on P001333 and ends at the 16 February heading on P001343. Record 701 ends on P001348.
* Record 702 occupies P001349–P001354. The subsequent Gelfand preamble is on P001355.
* Record 703 starts at the explicit Beilinson heading on P001355 and continues through P001358; its catalogue endpoint P001356 is too short. Record 704 contains the Gelfand preamble, not the Artin discussion.
* The Migdal heading on P001363 separates 705 from 706. The next meeting begins on P001368.
* The manuscript discusses Sinai before Schwarz, although the catalogue numbers place Schwarz first. Schwarz's heading is on P001369, with continuation through P001371; Alekseevskii then begins on P001371.
* Beilinson's 20 April heading on P001376 separates 711 from Kirillov's lecture. The explicit 27 April heading on P001378 begins 712.

## Verification ledger

Opened original mathematical texts include Harer–Zagier (1986), Kohnen–Zagier (1984), Zagier (1977, 1981, 1982), Holguin–Wang–Wang (2023 preprint/2024 article), Bessis–Itzykson–Zuber (1980), Itzykson–Zuber (1980; PDF scan with minimal OCR), Borel (1977), Salamon (1986), Jones (1987), and Esnault–Viehweg (MPI 87-2). The later stages additionally opened Zakharov–Shabat (1974), Burtsev–Zakharov–Mikhailov (1987), Zakharov–Manakov (1984), Fokas–Zakharov (1992), Crane–Rabin (1988), Witten's super-Riemann-surface notes, Panchenko's ultrametricity paper, Auffinger–Chen's ground-state theorem, Sudbery (1979), Suslin's original English scan, Goncharov (2016), Mazza–Voevodsky–Weibel (2006), and Garkusha's full author preprint. Exact searches and openings are indexed in `evidence/search_index.md`; per-item limits are in `evidence/verification_ledger.csv`. The 42 raw retrieval logs are local analysis evidence. A metadata/abstract opening is not described as reading a proof.

Kazakov's Physics Letters A paper is identified by title, authorship, date, pages and DOI. The publisher full text returned a restriction. Its entry initially remains `unverified`, and items depending on the exact parametrization explicitly state the verification limit. Bibliographic identification must not be promoted to an exact normalization check.

An exploratory opening of arXiv:1606.05361 returned an unrelated energy-storage article. That identifier is discarded and is not cited. The raw log is retained to make the correction reproducible.

## Development coordination

The multi-source integral is `1986-698.1`, problem `GP-1986-60`. The parent develops a normalized-Haar rank-two formula, a convergent Weingarten expansion with a tail estimate, and independent low-order checks. These are labelled rederivations/computations by the present authors, with no novelty claim. The two-source integral is exactly identified in Holguin–Wang–Wang; their angular convention in equation (2.16) has total mass one quarter, so comparison with normalized Haar includes an overall factor. Neither the existence of a series nor the rank-two formula settles every possible compact-form or large-N target.

The cube problem on P001364 already gives answer 96. It is an annotation, not a newly open class-C problem. The parent independently found 20 distinct planes (six faces and fourteen interior cuts), 96 rationally witnessed interior cells, and characteristic-lattice count 1+14+47+34=96. The exact interpretation is all distinct affine planes through triples of distinct vertices of a nondegenerate cube, counting connected components of its open interior after removing those planes.

The commuting partial-isometry question on P001374 does not specify domains or the meaning of extension. It must not be replaced silently by Ando's unitary dilation theorem for two everywhere-defined commuting contractions. It remains class F unless the missing formulation is recovered.

## Reuse and non-identifications

The cumulative bibliography is checked before assigning new keys. Known reused keys include `eguchikawai1982reduction`, `borel1977zeta`, `kubotaleopoldt1964`, `zakharovshabat1974scheme`, `connes1986indice`, and `zagier2007dilogarithm` when cited.

Prior matrix occurrences 1982-565.1–1982-565.7 are antecedents. GP-1982-02 asks for the global free energy of a specific four-unitary integral; the two-source angular integral is a distinct question and receives a new identifier. The cube-plane problem is distinct from the earlier four-cube section problem GP-1985-03. Earlier dilogarithm and regulator occurrences (1979-476 and 1979-477) are cross-referenced as antecedents without conflating a general motivic-complex conjecture with the five-term identity.

## Scan log

* P001330–P001332: inspected directly. The missing HCIZ normalization and monic-determinant denominator are omissions in the manuscript, not English translation errors.
* P001355: speaker boundaries and the III-type factor notation inspected; the Gelfand preamble precedes Beilinson's explicitly named talk.
* P001359–P001360: KdV/KP operator conventions inspected. The generic KP reconstruction supplies a missing nonlocal coefficient explicitly rather than silently editing the notebook.
* P001362: the displayed matrix has positive off-diagonal entries. It squares to the identity, contradicting the adjoining condition A² = −1. This is a faithful mathematical error, not an OCR sign correction.
* P001364: the cube problem and the already written answer 96 inspected directly. Every distinct plane through a triple of cube vertices is intended; the six supporting face planes do not cut the open cube.
* P001365–P001366: the resolvent quadratic, jump formulas and square-root branch inspected in paired reduced scans. The radicand sign and missing factors of i are mathematical emendations of the displayed formulas.
* P001371–P001372: the quaternionic projective space is twice written CP, the sphere exponent is 3, and both automorphism-group formulas begin with G. These readings are faithful to the manuscript. HP, the global-frame qualification, and the metric/general-linear distinction are editorial corrections. The possible intended S⁴ is only a conjectured repair; it is not substituted as a secure reading.
* P001374: the partial-isometry question explicitly says that the maps are not everywhere defined. The record cannot be identified with the usual two-contraction dilation theorem without changing the question.
* P001379 and P001381: the right-integer product is visibly nonzero as transcribed; equation (19) includes α₀ although the preceding homotopy sum starts at α₁; the last logarithm says deg although the determinant occurs earlier. These are faithful errors or unresolved normalization conventions, not mistranslations.
* P001383–P001384: the Bloch-complex boundary, five-point cross-ratio relation, logarithmic regulator diagram and two Chern components inspected. The diagram visibly needs logarithmic/dilogarithmic branch conventions and general-position assumptions; the item states these as reconstructions.

## Classification discipline

No class D is assigned merely because searches fail. Unspecified proposals remain F. Class C statements name the unresolved target and distinguish established special cases. A theorem already published before the dated talk is E even when the speaker helped prove it. Historical attribution and first public circulation are separated from the publication date when verified.

## Final inventory and source ordering

The completed slice has 15 catalogue records, 136 distinct items, nine problem entries, 61 correction/provenance rows, and 50 bibliography entries. The classifications are A = 8, B = 7, C = 6, D = 0, E = 100, F = 15. Record 699 is a heading and intentionally has no mathematical items.

| Record | Items | Main boundary or qualification |
|---|---:|---|
| 698 | 8 | Starts on P001330; preceding P001329 is not Kazakov's talk. |
| 699 | 0 | Calendar heading only. |
| 700 | 17 | Ends at the 16 February heading on P001343. |
| 701 | 9 | Rational periods; separate colour-map opening. |
| 702 | 8 | Polygon enumeration through P001354. |
| 703 | 14 | Beilinson continues beyond the catalogue endpoint to P001358. |
| 704 | 4 | Gelfand's preamble occurs before 703 in the manuscript. |
| 705 | 12 | Ends partway down P001363; four final proposals indexed separately. |
| 706 | 10 | Migdal plus the attributed cube interruption. |
| 707 | 10 | Schwarz follows Sinai in the manuscript. |
| 708 | 6 | Sinai precedes Schwarz; exact finite-N degeneracy distinguished from asymptotic states. |
| 709 | 8 | Alekseevskii begins on P001371. |
| 710 | 9 | Includes Gelfand's separately attributed partial-isometry question. |
| 711 | 4 | Beilinson begins on P001376. |
| 712 | 17 | Explicit 27 April heading on P001378. |

For the integrated source order, put 704 before 703 and 708 before 707, retaining all record numbers and catalogue dates. No further order adjustment was identified. The local builder remains in catalogue numerical order so its per-record checkpoints are easy to compare; root performs the two integration swaps.

## Precise status decisions

The problem index uses GP-1986-60 for the multi-source unitary integral, GP-1986-61 for RH, GP-1986-62 for polygon gluings, GP-1986-63 for coloured maps, GP-1986-64 for Artin holomorphy, GP-1986-65 for the mean-field spin-glass ground energy, GP-1986-66 for ultrametricity, GP-1986-67 for explicit characteristic-class comparison, and GP-1986-68 for Beilinson–Soulé vanishing. GP-1986-60 includes the other agents' confirmed exact occurrences 1986-688.5 and 1986-695.11 as well as 1986-698.1. The phase-specific gauge free-energy questions remain separate.

The toroidal RH strategy requires a restriction to tempered constituents; unitarity by itself permits complementary series. The corrected item does not suggest that a positive invariant pairing alone proves RH. The modern toroidal spectrum result is a genuine partial development, not a solution.

The four final Zakharov proposals were separated into 705.9–12: the analytic common-solution problem for higher spectral derivatives, soliton degeneration to rational kernels, the claim about dissipative systems, and operator-valued coefficients of the evolution derivatives. Each lacks different defining data. They remain F and receive no invented problem IDs. The unavailable 1988 conference text is an unresolved bibliographic lead, not evidence of an undeveloped subject.

For super Riemann surfaces, the moduli dimension is stated for genus at least two, the distribution bracket is nondegenerate, uniformization is restricted to the topology in Crane–Rabin's theorem, and super period matrices require exclusion or analysis of the Dirac-zero locus. The later super Riemann–Roch and Selberg papers are bibliographically identified, but the original Rosly and Baranov–Manin–Frolov–Schwarz proofs were not obtained. Their items explicitly have metadata-level verification. Witten's modern notes supply inspected qualifications; they are not substituted for evidence of first publication.

Panchenko's theorem assumes the Ghirlanda–Guerra identities for the asymptotic overlap structure. It is not a claim that the list of exact finite-size ground configurations is ultrametric. Auffinger–Chen's ground-energy theorem is stated for its mean-field mixed-p-spin setting, not for all finite-range Edwards–Anderson models. Talagrand's free-energy theorem is likewise not a universal solution of all spin-glass phase questions.

The finite-N zero-field Gaussian ground-state observation is an explicitly labelled proof by the present authors. For the complete-graph SK Hamiltonian with independent nondegenerate Gaussian pair couplings and N ≥ 2, all configurations outside a global spin-flip pair have distinct energies almost surely. A nontrivial pair-product difference is a nondegenerate Gaussian energy difference; a finite union removes accidental equality. The independent check supplied by root proves that equality of all pair products forces the coordinate ratios to be constant, hence the two configurations differ only by global flip. N = 1 is trivial. This annotation does not address near-ground states, pure states, or the thermodynamic metastate.

The quaternionic lecture is compared with the established quaternionic-differentiability rigidity theorem and Salamon's torsion-free theory. A simply connected manifold carrying affine quaternionic transition maps is not automatically all of quaternionic affine space; completeness and global developing-map hypotheses would be needed. An almost quaternionic structure is a rank-three bundle of imaginary endomorphisms, or equivalently the rank-four algebra including the identity, and need not have a globally chosen hypercomplex frame. Quaternionic-Kähler metric holonomy is a stronger condition.

The Hecke trace has a second parameter and must be distinguished from a positive trace or a von Neumann factor representation. Jones explicitly treats roots of unity; the notebook's blanket exclusion is false. The question at q = ±1 is normalized explicitly in terms of the Jones polynomial, without assuming an unrecorded parameter identification.

For the Chern lectures, trace powers give components of the Chern character, while Chern classes use elementary invariant polynomials. Deligne Chern classes exist functorially; that does not mean that every fixed topological Chern class has a unique arbitrary lift on a fixed manifold. Hodge decompositions and intermediate-Jacobian descriptions are given under compact Kähler hypotheses, and the Tate lattice and integral torsion preimage are retained. The asymmetric Deligne cup product, total-complex sign and cochain degrees are treated separately.

The announced 1987 paper is by Beilinson, MacPherson and Schechtman. Its metadata was checked through MacPherson's IAS publication list, but its full original proof was not recovered. Goncharov's inspected weight-two construction supplies an exact modern comparison for the final cross-ratio sketch; it is not claimed to be the first discovery. The abstract existence of motivic complexes is separated from a particular explicit polylogarithmic formula and from Beilinson–Soulé vanishing.

Suslin's introduction on p. 217 explicitly dates most of his results to 1982. The 1987 notebook already attributes the Bloch–K-theory connection to him. The later Russian publication is 1990; the English issue is dated 1991 and bears copyright 1992. Theorem 5.2 on p. 237 was inspected directly and requires an infinite field. Item 712.15 is therefore E, recording prior circulation, with a caveat that the introduction does not assign a separate completion date to every refinement of the final theorem.

Garkusha's Theorem 4.1 gives criteria equivalent to the vanishing conjecture, not a proof for all fields. The publisher's indexed metadata gives IMRN volume 2023, issue 24, pp. 22069–22095, DOI 10.1093/imrn/rnac343, online 20 December 2022. The direct publisher open hit a Silverchair access failure; the full author preprint was read. Soulé's IHES interview is dated 4 November 2026 and explicitly retains the conjecture, providing near-cutoff confirmation without replacing the technical mathematical source.

## Independent checks and limits

`code/check_spectral_operators.py` uses two different verifications. First it composes differential operators coefficient-by-coefficient with the Leibniz rule. Second it acts directly on polynomial test vectors at exact rational spectral values. The corrected matrix gives zero commutator; the manuscript matrix gives 2I/λ³. All 112 direct-action comparisons pass. The output is in `evidence/check_spectral_operators.out`.

The parent unitary development was read independently in full. Checks covered the trace-to-entry indexing, probability-Haar normalization, the entire U(2) divided-exponential formula and its removable diagonal, the row-maximum exponential-series tail bound, the use of a Moore–Penrose inverse of the permutation Gram matrix when m > N, and the rationality of the resulting exact coefficients. The U(3) counterexample's numerical identities were manually recomputed: the diagonal and transposition denominators, reciprocal sum −125/72, and second-order coefficient 71/24 agree. No unsupported compact general formula was found in the prose. An additional authorship marker was requested on the paragraph of independent low-degree identities, and root reports that it was added. This review is independent reasoning; it is not represented as a second execution of root's scripts.

Root provides the cube's two independent exact enumerations and the unitary-integral symbolic/moment checks under the integrated `deliverable/code/root/` directory. The cube is an annotation of an existing answer. The unitary work is the bounded C development, with no novelty claim and no assertion that the general compact-form or large-N question has been solved.

The local slice validator passes required-field, enumeration, consecutive-ID, problem-link, citation-key, bibliography and TeX-delimiter checks. All 136 items have consistent references. The integrated chapter build and PDF review are root's responsibility; root reported a successful full compile, with only presentation warnings at the time of handoff.

## Reproduction and packaging

Run `python parts/C/code/build_slice.py`, then `python parts/C/code/complete_bibliography.py`, then `python parts/C/code/validate_slice.py`. The first script checkpoints after each record. `extract_pages.py` reproduces all 56 bilingual page extracts. `build_evidence_index.py` produces the compact query/open index and the verification CSV. `generate_review_images.py` reproduces the paired analysis previews. `read_suslin.py` documents the source download and OCR commands used to inspect the introduction and theorem.

For the user-facing research log, the compact `search_index.md`, `verification_ledger.csv`, this audit, and exact computational outputs supply the requested queries, opened URLs, verification levels and reproducibility information. Downloaded source PDFs, OCR page images/text and raw retrieval responses are analysis caches and should not be redistributed as a collection of third-party articles. The supplied notebook's original scans remain untouched.
