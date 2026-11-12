# Spring source audit: records 36–50

Audit date: 12 November 2026. Owner: spring researcher, with independent checks and bibliographic support from the root researcher. This file records the evidence behind the generated data and the limits of the audit. It is not a substitute for the item-by-item notes, reconstruction, and fate fields.

## Scope and provenance

The block contains 15 catalog records and 73 occurrence items, retaining the defensible numbering of the supplied same-year first-run index. The supplied `previous_index.md` is **not** evidence of occurrences in previous academic years. Record 50’s catalog page envelope extends to P000090, but the scan of P000090 opens with `20/IX` and `Kohn`; its mathematics belongs to September 1965 and is excluded from the 1964–65 chapter. The envelope is retained in the talk record with an explicit explanation.

`build_data.py` saves all JSON and CSV files after each record, then applies a documented final primary-source audit and writes the corrections. `build_references.py` reproduces the bibliography. `extract_sources.py` and its output record the initial page extraction. The raw `web_*.json` files retain early web-tool results; later opened sources and theorem locators are recorded below and in each bibliography entry’s `annote`. No inaccessible article is described as a personally read theorem.

Final block counts before root merge: A 8; B 9; C 3; D 0; E 42; F 11. There are 8 problem records, 33 correction rows, and 50 local bibliography entries, with additional root-owned keys resolved at the global merge. The only item marked developed in the chapter is 1964-50.21. The final three C items are the general Hilbert invariant-subspace problem, universal irrational Bishop invariant subspaces, and universal irrational Bishop cyclicity. There is no D assignment based merely on failed retrieval.

## Sources and scan checks

The English and Russian transcriptions of pages 62–90 were extracted and read. Consequential operator material on pages 84–89 was reread directly from the page files; the full Russian P000087 proof fragment and P000089–P000090 boundary material were checked again during finalization. The Russian transcription remains the authority for wording. A modern repair is placed in `statement` or `reconstruction`, not silently substituted into `notes`.

Scans actually displayed and inspected in this audit:

| Scan | Consequential observation |
|---|---|
| P000065 | Viktor Nikolaevich begins the enveloping-algebra discussion; the two-dimensional examples and the unrestricted Baxter/Lie-ideal sentence are visible. The latter is faithfully transcribed and mathematically false. |
| P000066 | Common-n nilpotence paragraph; one canonical Weyl pair versus two; circular ensembles and their logarithmic interaction. Field and nil/nilpotent distinction remain unspecified. |
| P000067 | Exact equality sign in the cosine-power gap claim. The finite-N statement fails already at N=1. |
| P000068 | Positive free-energy exponent, single exponential of a phase difference in one W formula, then the correct difference of exponentials in the integral. These are distinct sign/interaction defects. |
| P000073 | The power is visibly 17/8, not a harmless transcription of -1/8. The m,n relation is ambiguous; t=alpha n is underlined. The sphere bundle definition fixes the real fibre dimension independently of its notation. |
| P000076 | The regularized-trace RHS really has y-prime at both ends. The annotation says the integral is a jump. The statement delta(0)=0 is visible and is a formal error, not a legitimate distributional equality. |
| P000078 | Incomplete continuous-parameter Weil kernel and subsequent linear/Radon specialization. No missing denominator power or cycle is guessed. |
| P000081 | The passage-to-a-limit explanation of lost exactness is present in the handwriting. Filtered colimits are exact; the obstruction is already the section complexes. |
| P000082 | Presheaf label under the subscripted objects; no basis for silently calling p a stalk. Ideal of two points on the sphere and truncated differential-form sequence are visible. |
| P000084 | Overwritten necessary-and-sufficient subnormality assertion; coherent commutator sign; nonzero polynomial requirement; original row/column matrix convention. |
| P000085 | Reversal of matrix-coefficient indices in one line, while subdiagonal products use the previous convention. |
| P000086 | A vector is omitted in one displayed norm limit. Threshold directions and projection placements need comparison with the published Halmos proof. |
| P000087 | Cancellation of the monotonicity assertion; weak projector limits; strong convergence of compact images; final rank-one argument. No monotonicity is supplied editorially. |
| P000088 | Ambiguous strict/non-strict contraction glyph; both non-stability arrows are crossed; Donoghue third weight remains 1/8 versus 1/6; integer-chain question and two-sided measure-Volterra lower limit zero. |
| P000089 | Irrational Bishop formula, every-vector and no-known-cyclic-vector statements, Ornstein anecdote; overwritten F-name; Hardy integral lacks its upper bound but has the correct positive Fourier exponent. |
| P000090 | September 20 Kohn heading confirms the academic-year boundary. |

An earlier oversized image batch did not reliably display P000065, P000068, P000072 and P000074. P000065 and P000068 were therefore displayed again and are included above. P000072 and P000074 are **not** claimed as visually inspected by this agent. Their statements were checked in the transcriptions and, where needed, the literature. Root may have additional independent scan checks.

The 33 correction rows distinguish `faithful_error`, `ambiguity`, and `provenance`. A page with a faithfully copied mathematical error does not justify editing the diplomatic Russian without an editorial mark. No uncertain glyph is upgraded to certainty because a known theorem would be easier to cite.

## Search record and exact matches

The following lists the query families used. They are a record of topics and representative formulations, not a purported verbatim export of every search request. Raw returned results are retained in the early `web_*.json` checkpoints. The final four exact query strings and their complete response are in `web_final_gap_search.json`:

1. `Ornstein operator "cyclic" "L2" invariant subspaces`
2. `"Latyshev" "Kostrikin" "nilpotent" associative Lie`
3. `"Gromov" "spherical harmonics" "Dvoretzky" 1965`
4. `"Sakhnovich" "trace class" "invariant subspaces"`

Additional exact final queries were `"Basicity and unicellularity" "necessary"` and `Никольский 1968 базисность одноклеточность необходимыми достаточными`. Their hits led to the primary Math-Net record and the Geodesic mirror of its metadata; both original-language and translation PDF attempts failed.

### Records 36–38: dynamics, primitive envelopes, and Weyl rank

Searches combined Stepin, dyadic rationals, continuous spectrum, locally compact time, 1965/1966, and Math-Net. The exact continuation is Stepin 1966, Section 2, pages 774–776: a dyadic torsion-group action with pure-point even part and simple singular-continuous odd part. The manuscript’s continuous component is not promoted to Lebesgue spectrum. The elementary constant-modulus eigenfunction statement in record 36 is already used in Stepin’s normalization.

Primitive-enveloping-algebra searches included Latyshev, Jacobson, Harish-Chandra, Ooms, primitive U(g), and Dixmier–Moeglin. Ooms 1974 is real, but its institutional repository returned 503 and the publisher route failed. It is marked unverified and does not certify the final criterion. The opened Bell–Launois–León Sánchez–Moosa 2017 primary paper, page 2020, explicitly states the exact finite-dimensional complex Dixmier–Moeglin equivalence. For the zero ideal, rationality is the assertion that the quotient division ring has center C. This resolves the reconstructed complex case; the notebook does not specify the field or dimension. The two-dimensional nonabelian example was also checked directly on C[t] using multiplication by t and translation by one.

Baxter title/DOI/PDF searches did not produce an accessible original. The unrestricted simplicity sentence is nevertheless definitely false by M_2(C), and no exact missing quotient or involution is invented. Searches on Kostrikin, restricted Burnside, uniform associative nilpotence on Lie-generated subalgebras, and Latyshev did not identify the recorded statement under its omitted field/characteristic assumptions. The final search found unrelated commutator-product identities; they were not substituted for the source problem.

Gelfand–Kirillov 1966 was opened in full at Numdam. Section 4, Lemma 5 and Theorem 2, pages 11–14, distinguish the differential-operator algebras by growth. The received date is 19 January 1966. This exactly answers A_1 versus A_2 and must not be replaced by the fixed-rank Dixmier endomorphism conjecture. GP-1964-04 retains the correct quantifiers.

### Records 39, 41, 42 and 46: circular ensembles and gaps

Queries used Dyson statistical theory I/III, circular orthogonal/unitary ensembles, exact cosine power, gap probability, even sine kernel, Dyson constant, and Brownian eigenvalues. Dyson I was read in the Rutgers-hosted primary scan; Dyson III and the 1962 Brownian paper remained inaccessible through the attempted publisher routes and are explicitly unverified leads. The modern gap-to-Palm-spacing relation and matrix Brownian equation are marked reconstructions, not claims of reading those original proofs.

Ehrhardt’s primary arXiv version was opened and its introductory even/odd sine-kernel asymptotics read. It first circulated in April 2006 and was published in 2007. It confirms the -1/8 logarithmic power, with the leading -s²/4-s/2 terms for the even kernel. It does not prove the manuscript’s finite-N cosine-power equality; that is refuted by the uniform one-angle case. The source’s finite cosine matrix and its uncertain m,n scaling are kept separate from the continuum normalization. The unnamed replacement ensemble in record 42 remains F.

Altland–Zirnbauer’s primary abstract was opened to verify the later symmetric-space classification direction. It supports a developed framework, not an exact all-symmetric-space gap formula. Jordan 1875 was opened in full at Numdam; the introductory discussion of Sections IV–V verifies the long-established principal-angle theory. Dyson Brownian metadata is not conflated with a particular free versus Ornstein–Uhlenbeck normalization.

### Records 40 and 49: sites and cohomology

Searches followed SGA 4, slice categories, Grothendieck sites, field Galois sheaves, Čech refinements, filtered-colimit exactness, and derived sheaf cohomology. SGA 4 volume I’s publisher contents and dates were opened, but not its entire text. The live Stacks Project statements at Tags 00VH, 00VL, 03QR, 01FP and 01GZ were read for the precise categorical reconstructions. The Frobenius trace formula is a later precise reconstruction whose proof is not attributed to the foundations volume alone.

Grothendieck’s 1957 Tohoku publisher record was opened. The PDF timed out; a discrepancy in the indexed page range is recorded in the bibliography and pages are omitted rather than selecting an unverified range. The fixed-cover exactness defect, stalk/section distinction, and two-point ideal example were checked mathematically. In particular filtered colimits cannot be the reason that a compatible system of exact sequences ceases to be exact. The truncated differential-form sequence remains F because its final sheaf is not defined.

### Records 44–45: convex geometry

Queries followed Funk sections, Aleksandrov brightness, origin-symmetric reconstruction, Dvoretzky, Gromov spherical harmonics, Grassmann bundles, and the geometric Banach conjecture. Funk’s publisher metadata was opened; Gardner’s author-maintained tomography discussion verifies the brightness theorem’s scope. Dvoretzky’s conference metadata was checked through the translation journal, and Figiel’s 1976 primary theorem was read for a precise statement. Gromov’s 1967 paper was read; its isometric-section/Banach-conjecture theorem is not the same quantified statement as the notebook’s low-harmonic vanishing proposal. That thematic match is not promoted to A or a proof of the recorded claim.

### Records 47–48: scattering traces and several complex variables

Searches used Faddeev inverse scattering/Jost functions, Buslaev–Faddeev traces, Gelfand regularized traces, commutator traces, Hefer decomposition, Cauchy–Weil formulas, Cartan analytic polyhedra, and Gindikin holomorphic Radon transforms.

Faddeev 1959 was opened in Russian; Sections 1, 2 and 6 and the whole-line supplementary discussion were read. The translation publication date (1963) is separated from the original (1959), and Math-Net’s malformed automatically combined citation is not copied. Buslaev–Faddeev 1960 was opened in full: Theorem 1, page 13, supplies the relative-resolvent/Jost derivative identity; Section 2, pages 14–15, supplies contour and Mellin regularization; page 16 treats finite-interval **Dirichlet** ends. The latter is not silently treated as the notebook’s **Neumann** boundary expression. Gesztesy–Mitrea–Zinchenko’s primary preprint Theorem 1.1 supplies a checked modern Jost/Fredholm formulation. Gelfand 1956 metadata was opened but not the original proof. The undefined y-prime difference remains F.

Helton–Howe 1975 was opened in the Tsinghua institutional archive, and its introduction was read for subsequent nonzero trace-of-commutator theory. The direct unilateral-shift example independently shows why trace class of the commutator is insufficient for trace zero.

Hefer 1950 publisher metadata was opened. Norguet 1961 was opened in full, and Sections 17–18, especially pages 72–78, were read for the exact kernel architecture and global Hefer coefficients. Cartan 1950 was opened at the working Numdam **article** URL; its introduction and account of Sections VII–VIII were checked for polyhedral foundations. Gindikin 1965 was opened in full; formula (2) and its convex tube/regularity/decay hypotheses match the final linear specialization. The footnote dates its Moscow Mathematical Society presentation to 23 February 1965, before the seminar, and publication to 1965. It does not repair the unfinished general continuous-parameter formula.

### Record 50: invariant subspaces and modern status

The exact polynomial-compactness papers by Bernstein–Robinson and Halmos were opened and read. Received dates in 1964 are separated from publication in 1966. The coauthor Allen R. Bernstein is distinguished from seminar speaker I. N. Bernstein. Halmos pages 433–437 supply the correction of the matrix convention, compression lemma, vector norm and adjacent-flag argument.

The original 1964 de Branges–Rovnyak announcement and 1965 correction were **not** read in full. Rovnyak’s author bibliography explicitly calls the correction a retraction; de Branges’s Purdue bibliography verifies its exact title. This is author-bibliography verification, not a claim of independently analyzing the failed original proof. The compact-defect assertion is kept F because the norm sign is uncertain and the claimed surviving corollary has not been verified from an original result.

Brown 1978 publisher metadata and abstract explicitly give the affirmative subnormal theorem. Lambert 1984 was read in full for subnormality and the stronger positivity framework. Bram’s original remains inaccessible; its bibliography was identified in Lambert. The weights 1,1,2,2,... give a directly checked hyponormal/non-subnormal counterexample to the notebook’s biconditional.

Root located and read Sz.-Nagy–Foiaş VIII, IX and the 1965 corrections at the Szeged archive. Exact locators: VIII Theorem 1 p.50 and Theorem 3 p.58 for the model and complete unitary invariant; IX Theorem 1 and formulas (3.16)–(3.17), pp.294–295 for the functional model/factorization; IX Section 6 Theorem 3 and Remark (ii), p.314, for the two non-stable power sequences. The correction p.193 explicitly says the Proposition 5.4 error does not affect Theorem 3 or its proof. These are team-verified full primary results; root owns their bibliography entries. Our fresh open attempts failed, and this shared provenance is stated rather than claiming independent full-text retrieval.

Donoghue 1957 was read in full, including Examples 1–2 and the Volterra Example 3. Harrison 1971’s primary PDF was read. Nikol’skii 1967’s Russian original was read for sufficient conditions and nonunicellularity constructions. Nikol’skii 1968 metadata and abstract were opened, but both PDF routes failed; the primary NYJM 2023 paper by Lata–Pokhriyal–Singh explicitly credits the 1967/1968 papers with additional necessary and sufficient conditions. Yakubovich 1985’s primary abstract verifies that monotone moduli tending to zero suffice; its English translation is 1987. The broad notebook request for conditions is therefore B/partial. The audit does **not** declare a universal arbitrary-weight characterization open merely because it was not ascertained.

Root followed Shkarin’s bibliography to Domar 1981. The root downloaded the original and rendered pages 133–135; this agent independently inspected those images. Theorem 2’s hypotheses and conclusion were checked twice. For w_n=exp(-2n|n|), the decreasing weights have the required convex/concave logarithm, summable w_n^(1/n), and quadratic limits +2 and -2 satisfying the log 3 alternatives. Multiplication by w_n is unitary from Domar’s weighted l² to ordinary l² and conjugates right translation to weights exp(-2|2j+1|). Thus 50.17 is B/exact and GP-1964-S04 is solved. The bibliography entry is root-owned.

The literal measure-Volterra conjecture is disproved by the atomless probability measure one half Lebesgue measure on [-1,1], with the displayed oriented lower-limit-zero integral. The two half-interval support spaces are nonzero proper closed invariant subspaces and incomparable. A positive continuous one-sided density with the lower endpoint as base is instead transformed by its cumulative distribution to the classical Volterra case. This short annotation does not manufacture an unresolved measure classification or a C item.

Chamizo et al. 2020 and Béhani 2023 were read in their complete primary arXiv versions. Theorem 3.7 of the former covers log(q_{j+1})=O(q_j/(log q_j)^3); it does not cover every irrational parameter. Béhani Theorems 4.4–4.5, 4.9, 4.16 and Question 5.4 delimit rational cyclicity, the co-meager parameter set, sufficient approximation conditions and the explicit-threshold question. Root’s bounded development supplies finite rational certificates and continuity estimates, with no universal irrational conclusion and no novelty claim for the known rational mechanism. The Ma 2026 primary abs/PDF/HTML routes returned disabled errors. It remains an inaccessible lead, under root’s key `ma2026rational`; no theorem is accepted from it.

Current-status searches included the general Hilbert invariant-subspace problem, 2026 claims, the Kim–Pearcy–Shields problem, Bishop operators and cyclicity. Marcoux–Radjavi–Yahaghi–Zhang arXiv:2608.21154 was opened in full: its abstract and Introduction pp.1–2 explicitly call the complex separable infinite-dimensional Hilbert problem unsolved, with v1 dated 21 August 2026. Szczepanski’s August 2026 primary article gives partial results, not a general solution. Enflo/Neville and later 2026 claimed-proof leads were not treated as accepted theorems. A tertiary status page was used only to discover a primary reference; it is not evidence for a theorem or for a withdrawal. The final status is the qualified statement that no generally accepted general solution was verified through 12 November 2026.

The Ornstein L^(2+epsilon) anecdote lacks the operator, parameter quantifier and measure class. Searches did not identify an exact primary result, so it stays F.

The final bounded small-imaginary-part search followed Dym–Katsnelson, *Contributions of Issai Schur to Analysis*, arXiv:0706.1868, Section 7, pages 54–59 and bibliography pages 64–66. The complete primary author survey was opened. It attributes a Hilbert–Schmidt-imaginary-part implication to Sakhnovich 1959. The seven-page Russian original at Math-Net `ivm2426` was then opened and read: Definition 2, page 180, states the invariant-subspace interpolation property, and its theorem on page 181 constructs a triangular model under that property. Its introduction explicitly recalls Livšic’s trace-class result, but no proof of the survey’s Hilbert–Schmidt implication was located in that original. This scope discrepancy is retained rather than papered over.

Livšic’s 1954 Russian original at Math-Net `sm5241` was then opened. The introduction, page 145, defines the class by trace-class imaginary part. Section 11, Theorem 4, pages 180–181, explicitly states unitary equivalence of the non-self-adjoint component to the corresponding component of the triangular model; Section 1 defines the additional reducing self-adjoint part. Those statements were read, while the entire 55-page proof was not rechecked line by line. The introduction and references identify preliminary announcements in two 1952 Doklady notes. Thus 50.13 is E/partial, with exact trace-class hypotheses in its reconstruction and no unsupported attribution of the survey’s stronger criterion. Primary URLs and verification depths are included in the inventory below.

## Proposed report and presentation decisions

- Separate literal correctness from publication fate. A false equality can occur inside a fruitful published program; B is not a certification that the source’s formula is correct.
- Preserve the scope of negative audit statements. “Not ascertained” describes the audit, whereas “open” describes a mathematical state of knowledge. The Donoghue-weight revision is a concrete example.
- Display the original formulation, modern reconstruction and literature result in adjacent, clearly labeled fields. Link the Weyl-rank question directly to its exact growth theorem rather than to a same-name conjecture.
- Give current status an explicit date and a verification-depth display. Author metadata, an abstract, a read theorem, an inaccessible lead and a root-verified original must remain distinguishable.
- Link item 50.21 to the bounded Bishop development and its executable certificates. Show its unresolved universal quantifier before any finite computation, so finite evidence is not mistaken for a universal result.
- Keep speaker identity separate from mathematical identification. The model theorem is exact even though the F-name visitor remains uncertain.
- Make academic-year boundary and catalog-envelope notes visible from the talk page. Do not duplicate Kohn’s September 1965 mathematics in this chapter.

## Primary-source URL and locator inventory

The following inventory is generated from the checked bibliography. Each entry records the verification depth. Root-owned Domar, Sz.-Nagy–Foiaş and Ma entries are described above and resolved during the global bibliography merge.

### altlandzirnbauer1997

Novel Symmetry Classes in Mesoscopic Normal-Superconducting Hybrid Structures (1997). **verified**.

https://arxiv.org/abs/cond-mat/9602137

DOI: 10.1103/PhysRevB.55.1142

Primary arXiv metadata and abstract read; correspondence to Cartan symmetry classes checked at abstract level. Preprint first submitted 27 February 1996. No universal gap formula is attributed to this paper.

### aronszajnsmith1954

Invariant subspaces of completely continuous operators (1954). **verified**.

https://www.mathnet.ru/php/archive.phtml?jrnid=mat&option_lang=eng&paperid=37&wshow=paper

Primary translation-journal metadata checked; Russian translation Matematika 2(1) (1958), 97--102. The complete original proof was not read.

### baxter1956lie

Lie simplicity of a special class of associative rings (1956). **unverified**.

https://www.ams.org/journals/proc/1956-007-05/S0002-9939-1956-0082481-2/

DOI: 10.1090/S0002-9939-1956-0082481-2

Bibliographic lead only; AMS landing page, DOI and PDF were not successfully opened. It is not used to certify an unrestricted Lie-simplicity theorem.

### behani2023bishop

A study of Bishop operators from the point of view of linear dynamics (2023). **verified**.

https://arxiv.org/pdf/2207.11419

DOI: 10.1016/j.jmaa.2023.127204

Full primary author preprint read: Theorems 4.4--4.5, 4.9, 4.16 and Question 5.4. First submitted 23 July 2022; journal issue 1 October 2023.

### bell2017poisson

Poisson algebras via model theory and differential-algebraic geometry (2017). **verified**.

https://ems.press/content/serial-article-files/32221

DOI: 10.4171/JEMS/712

Primary paper opened and introduction page 2020 read for the exact Dixmier--Moeglin equivalence for finite-dimensional complex Lie algebras; the original 1977--1980 proofs were not read.

### bernsteinrobinson1966

Solution of an invariant subspace problem of K. T. Smith and P. R. Halmos (1966). **verified**.

https://msp.org/pjm/1966/16-3/pjm-v16-n3-p04-s.pdf

DOI: 10.2140/pjm.1966.16.421

Primary paper opened and Theorem 1.1 read. Received 5 July 1964; revised 10 December 1964. Allen R. Bernstein is distinct from I. N. Bernstein in the seminar catalog.

### bram1955subnormal

Subnormal operators (1955). **unverified**.

https://doi.org/10.1215/S0012-7094-55-02207-9

DOI: 10.1215/S0012-7094-55-02207-9

Original DOI access failed. Metadata identified in the opened bibliography of Lambert 1984. Original theorem not read; the modern discussion in Lambert is the verified support.

### brown1978subnormal

Some invariant subspaces for subnormal operators (1978). **verified**.

https://link.springer.com/article/10.1007/BF01682842

DOI: 10.1007/BF01682842

Publisher metadata and abstract explicitly stating the subnormal invariant-subspace theorem were read; subscription full text not read. Received 21 July 1978, published September 1978.

### buslaevfaddeev1960traces

Formulas for traces for a singular Sturm--Liouville differential operator (1960). **verified**.

https://www.mathnet.ru/eng/dan28038

Full primary Russian note opened: Theorem 1 on page 13, contour/Mellin continuation on pages 14--15, finite-interval Dirichlet discussion on page 16. Received 17 December 1959, presented 3 January 1960. English translation Soviet Mathematics Doklady 1 (1960), 451--454.

### cartan1950ideaux

Idéaux et modules de fonctions analytiques de variables complexes (1950). **verified**.

https://www.numdam.org/article/BSMF_1950__78__29_0.pdf

DOI: 10.24033/bsmf.1409

Full primary paper opened; introduction pages 29--30 and its account of polyhedral/global results in Sections VII--VIII read. Used for the historical framework, not an asserted exact reconstruction of every notebook sentence.

### chamizo2020bishop

Invariant subspaces for Bishop operators and beyond (2020). **verified**.

https://arxiv.org/pdf/1812.08059

DOI: 10.1016/j.aim.2020.107365

Full primary author preprint read, particularly Theorem 3.7 and the precise continued-fraction growth condition. First submitted 19 December 2018; journal issue 2 December 2020.

### debrangesrovnyak1964existence

The existence of invariant subspaces (1964). **verified**.

https://uva.theopenscholar.com/james-rovnyak/selected-works

Metadata and explicit identification of the 1965 retraction checked in Rovnyak’s author bibliography; original announcement not read.

### debrangesrovnyak1965correction

Correction to ``The existence of invariant subspaces'' (1965). **verified**.

https://www.math.purdue.edu/people/profile/branges.html

Title and metadata checked in coauthor bibliography; Rovnyak’s author bibliography explicitly identifies it as a retraction; original correction not read.

### donoghue1957lattice

The lattice of invariant subspaces of a completely continuous quasi-nilpotent transformation (1957). **verified**.

https://msp.org/pjm/1957/7-2/pjm-v7-n2-p01-s.pdf

DOI: 10.2140/pjm.1957.7.1031

Primary paper read: Examples 1--2 give weighted-shift lattices and Example 3 the Volterra lattice. Received 25 June 1956.

### dvoretzky1961convex

Some results on convex bodies and Banach spaces (1961). **verified**.

https://www.mathnet.ru/eng/mat296

Primary translation-journal metadata opened; Russian translation in Matematika 8(1) (1964), 73--102, translated by B. S. Mityagin. Original conference paper not read; exact theorem checked through Figiel 1976.

### dymkatsnelson2007schur

Contributions of Issai Schur to Analysis (2007). **verified**.

https://arxiv.org/pdf/0706.1868

Primary author survey version opened, especially Section 7, pages 54--59, and bibliography pages 64--66. ArXiv version first submitted 13 June 2007; bibliographic reference identifies the earlier 2003 book chapter, whose complete publisher metadata were not separately verified. The Hilbert--Schmidt implication attributed to Sakhnovich is used only as a source trail; its exact original proof was not confirmed in the cited 1959 paper.

### dyson1962brownian

A Brownian-Motion Model for the Eigenvalues of a Random Matrix (1962). **unverified**.

https://doi.org/10.1063/1.1703862

DOI: 10.1063/1.1703862

Indexed publisher metadata located but original article access failed. Modern stochastic equation in the item is explicitly an editorial reconstruction, not a quotation of this unread result.

### dyson1962statisticalI

Statistical theory of the energy levels of complex systems. I (1962). **verified**.

https://sites.math.rutgers.edu/~zeilberg/akherim/dyson1962.pdf

DOI: 10.1063/1.1703773

Primary paper read in Rutgers-hosted scan, including circular ensembles and eigenangle measures. Received 15 September 1961.

### dyson1962statisticalIII

Statistical theory of the energy levels of complex systems. III (1962). **unverified**.

https://doi.org/10.1063/1.1703775

DOI: 10.1063/1.1703775

Indexed metadata located; original publisher article could not be opened and INSPIRE returned a JavaScript wall. Exact source theorem not read.

### ehrhardt2007dyson

Dyson's constant in the asymptotics of the Fredholm determinant of the sine kernel (2007). **verified**.

https://arxiv.org/pdf/math/0605003

DOI: 10.1007/s00220-007-0239-x

Primary author preprint read, including the even and odd sine-kernel large-gap formulas. First submitted 28 April 2006, revised 9 November 2006; journal publication 2007.

### faddeev1959inverse

The inverse problem in the quantum theory of scattering (1959). **verified**.

https://www.mathnet.ru/eng/rm7335

Full Russian primary paper opened: Jost solutions in Section 1, expansion in Section 2, Wronskians in Section 6, whole-line supplementary remarks. Received 12 February 1959. English translation Journal of Mathematical Physics 4 (1963), 72--104, DOI 10.1063/1.1703891; Math-Net automatic combined citation has a chronology/volume inconsistency, not adopted here.

### figiel1976dvoretzky

A short proof of Dvoretzky's theorem on almost spherical sections of convex bodies (1976). **verified**.

https://www.numdam.org/item/CM_1976__33_3_297_0.pdf

Primary paper read, especially theorem on page 297 and reference to original Dvoretzky paper.

### funk1913flachen

Über Flächen mit lauter geschlossenen geodätischen Linien (1913). **verified**.

https://link.springer.com/article/10.1007/BF01456044

DOI: 10.1007/BF01456044

Publisher metadata opened; complete article not read. The journal article is dated June 1913; its first three chapters derive from the 1911 Göttingen dissertation.

### gardner2026tomography

Geometric Tomography: author website and brightness discussion (2026). **verified**.

https://geometrictomography.com/

Author-maintained exposition opened, including brightness and the Aleksandrov uniqueness result for origin-symmetric bodies, with reference to book Theorem 3.3.1. Accessed November 2026; this is not an original 1937 source.

### gelfand1956identities

On identities for eigenvalues of a differential operator of second order (1956). **verified**.

https://www.mathnet.ru/php/archive.phtml?jrnid=rm&option_lang=eng&paperid=7749&wshow=paper

Publisher metadata opened; full-text request failed. The notebook boundary expression is not claimed to match a read theorem in this paper.

### gelfandkirillov1966corps

Sur les corps liés aux algèbres enveloppantes des algèbres de Lie (1966). **verified**.

https://www.numdam.org/item/PMIHES_1966__31__5_0.pdf

DOI: 10.1007/BF02684800

Full primary paper read, especially Section 4, Lemma 5 and Theorem 2, pages 11--14; received 19 January 1966.

### gesztesy2007jost

Variations on a theme of Jost and Pais (2007). **verified**.

https://arxiv.org/pdf/0705.3510

Primary author preprint opened and Theorem 1.1 read for the half-line Jost/Fredholm determinant identity. First submitted 24 May 2007. This entry deliberately cites the verified preprint rather than unverified later journal metadata.

### gindikin1965radon

Radon transform for holomorphic functions of several variables and related integral formulas (1965). **verified**.

https://www.mathnet.ru/php/archive.phtml?jrnid=rm&option_lang=eng&paperid=6039&wshow=paper

Primary Russian note opened and formula (2) read. Its footnote records presentation to the Moscow Mathematical Society on 23 February 1965. Convex tube, regularity and decay hypotheses are retained in the reconstructed statement.

### gromov1967banach

A geometrical conjecture of Banach (1967). **verified**.

https://www.mathnet.ru/eng/im2577

DOI: 10.1070/IM1967v001n05ABEH000599

Primary paper opened and Theorem 1 read; Russian original Izvestiya AN SSSR Ser. Mat. 31(5), 1105--1114. Received 14 September 1966. The theorem does not exactly match the notebook harmonic-vanishing fragment.

### grothendieck1957tohoku

Sur quelques points d'algèbre homologique (1957). **verified**.

https://www.jstage.jst.go.jp/article/tmj1949/9/2/9_2_119/_article

DOI: 10.2748/tmj/1178244839

Publisher metadata opened; PDF timed out. Page range omitted because opened J-STAGE record and canonical bibliographic range conflict. Received 1 March 1957. The original proof was not read in this audit.

### halmos1966polynomial

Invariant subspaces of polynomially compact operators (1966). **verified**.

https://msp.org/pjm/1966/16-3/pjm-v16-n3-p05-s.pdf

DOI: 10.2140/pjm.1966.16.433

Entire primary proof read, including Hessenberg reduction, compression lemma and limiting projections. Received 10 October 1964, before the May 1965 seminar; published 1966.

### harrison1971unicellularity

On the Unicellularity of Weighted Shifts (1971). **verified**.

https://www.cambridge.org/core/services/aop-cambridge-core/content/view/8FFC4438450E7AE018376EB51A08142C/S1446788700009800a.pdf/on_the_unicellularity_of_weighted_shifts.pdf

DOI: 10.1017/S1446788700009800

Full primary paper read, Section 1 and Lemmas 2.1--2.2 in particular. Received 10 July 1969. Cambridge online date 2009 is not the publication year.

### hefer1950zerlegung

Zur Funktionentheorie mehrerer Veränderlichen. Über eine Zerlegung analytischer Funktionen und die Weilsche Integraldarstellung (1950). **verified**.

https://link.springer.com/article/10.1007/BF01342970

DOI: 10.1007/BF01342970

Publisher metadata checked; original proof not read. Exact decomposition and its use independently checked in Norguet 1961, page 78.

### heltonhowe1975traces

Traces of commutators of integral operators (1975). **verified**.

https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6197-11511_2006_Article_BF02392022.pdf

DOI: 10.1007/BF02392022

Full primary paper opened in the institutional archive; introduction and trace-formula setting read. Used for subsequent development, not as proof of an unrestricted zero-trace assertion.

### jordan1875geometrie

Essai sur la géométrie à n dimensions (1875). **verified**.

https://www.numdam.org/item/10.24033/bsmf.90.pdf

DOI: 10.24033/bsmf.90

Full primary scan opened; introduction pages 104--105 and scope of Sections IV--V read for angles between linear varieties. Presented 12 May 1875.

### lambert1984subnormal

A characterization of subnormal operators (1984). **verified**.

https://www.cambridge.org/core/services/aop-cambridge-core/content/view/4320312A6B7CAEED28EC41B94DAFCB31/S0017089500005474a.pdf/div-class-title-a-characterization-of-subnormal-operators-div.pdf

DOI: 10.1017/S0017089500005474

Full primary paper read, especially definition and Bram context on page 99 and criterion on page 100. Received 18 October 1982.

### latapokhriyalsingh2023powers

Invariant subspaces of powers of some unicellular operators (2023). **verified**.

https://nyjm.albany.edu/j/2023/29-10p.pdf

Primary paper opened and introduction page 232 read, including its credit to Nikol’skii 1967 and 1968 for additional necessary and sufficient weight conditions. Received 4 July 2022. This historical statement does not itself certify a complete criterion for arbitrary weight sequences.

### livsic1954spectral

On the spectral decomposition of linear non-selfadjoint operators (1954). **verified**.

https://www.mathnet.ru/php/getFT.phtml?jrnid=sm&paperid=5241&what=fullt

Full Russian original opened. Introduction page 145 defines the trace-class imaginary-part hypothesis; Section 11, Theorem 4, pages 180--181, gives the unitary triangular model for the completely non-self-adjoint component. The full proof was not rechecked line by line. Introduction and references identify preliminary announcements in Doklady 84 (1952), 873--876 and 1131--1134; English translation AMS Translations Series 2, volume 5 (1957), 67--114.

### marcoux2026generators

Fully non-zero matrices and generators of full algebras of operators (2026). **verified**.

https://arxiv.org/pdf/2608.21154

Primary preprint opened and read, abstract page 1 and introduction page 2 explicitly describing the complex separable infinite-dimensional Hilbert invariant-subspace problem as unsolved. Version 1 dated 21 August 2026. Used as current expert evidence, not as proof of a negative bibliographic universal.

### nikolskii1967weighted

Invariant subspaces of weighted shift operators (1967). **verified**.

https://www.mathnet.ru/eng/sm4157

DOI: 10.1070/SM1967v003n02ABEH002367

Primary Russian paper opened: sufficient conditions in Theorem 1 and nonunicellularity constructions read. Received 21 March 1966. English translation Mathematics of the USSR-Sbornik 3(2) (1967), 159--176. The bilateral question near page 190 is historical, not evidence of current openness.

### nikolskii1968basicity

Basicity and unicellularity of weighted shift operators (1968). **verified**.

https://www.mathnet.ru/php/archive.phtml?jrnid=im&option_lang=eng&paperid=2508&wshow=paper

DOI: 10.1070/IM1968v002n05ABEH000703

Primary metadata and abstract opened; Russian and English full-text requests failed. Original Russian Izvestiya AN SSSR Ser. Mat. 32(5), 1123--1137; received 15 December 1967. The specific necessary/sufficient conditions are not reported as personally read.

### norguet1961formes

Problèmes sur les formes différentielles et les courants (1961). **verified**.

https://www.numdam.org/item/AIF_1961__11__1_0.pdf

DOI: 10.5802/aif.108

Full primary paper read in relevant portions: Section 17 on Weil formulas, Theorem 18.4 and Corollary 18.2, pages 72--78; Hefer coefficients on page 78.

### ooms1974primitive

On Lie Algebras Having a Primitive Universal Enveloping Algebra (1974). **unverified**.

https://documentserver.uhasselt.be/handle/1942/37476

DOI: 10.1016/0021-8693(74)90154-9

Real article located through indexed publisher and institutional metadata; repository returned 503 and publisher access failed. Full theorem not read. Received 15 June 1973 according to indexed record.

### sakhnovich1959triangular

On the reduction of non-selfadjoint operators to triangular form (1959). **verified**.

https://www.mathnet.ru/php/getFT.phtml?jrnid=ivm&paperid=2426&what=fullt

Full seven-page Russian original opened and read: Definition 2 page 180 gives the invariant-subspace interpolation condition, and the theorem page 181 gives triangularization under that condition. Introduction explicitly recalls Livshits trace-class imaginary-part theorem. No Hilbert--Schmidt sufficient condition was located in this original, despite a later survey attribution. Received 6 December 1957.

### sga4I1972

Théorie des topos et cohomologie étale des schémas. Tome 1 (1972). **verified**.

https://link.springer.com/book/10.1007/BFb0081551

DOI: 10.1007/BFb0081551

Publisher metadata and contents checked, not the complete book. SGA 4 seminar 1963--1964; Exposés I--IV concern categorical and site foundations. This volume alone is not cited as a full proof of the étale trace formula.

### stacks2026cohomology

The Stacks Project: Čech and hypercover cohomology (2026). **verified**.

https://stacks.math.columbia.edu/tag/01FP

Live primary exposition read: Tag 01FP, Section 20.25 and refinement construction; Tag 01GZ, Section 25.10, Theorem 25.10.1. Accessed November 2026.

### stacks2026sites

The Stacks Project: Sites, coverings, and the étale site of a field (2026). **verified**.

https://stacks.math.columbia.edu/tag/00VH

Live primary exposition read: Tags 00VH and 00VL for sites and coverings, and Tag 03QR for the field and Galois interpretation. Accessed November 2026.

### stepin1966spectra

Properties of spectra of ergodic dynamic systems with locally compact time (1966). **verified**.

https://www.mathnet.ru/eng/dan32452

Math-Net metadata and full Russian primary PDF opened; Section 2, pages 774--776 read. Presented 23 November 1965.

### szczepanski2026chain

On the chain of commuting operators on Banach spaces (2026). **verified**.

https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/blms.70471

DOI: 10.1112/blms.70471

Primary full HTML opened, Introduction Problem 1.1 and Theorem 1.2 read. First published 20 August 2026. A partial result, not a general solution or independent definitive survey of the Hilbert problem.

### yakubovich1985weighted

Invariant subspaces of weighted shift operators (1985). **verified**.

https://www.mathnet.ru/eng/znsl4181

DOI: 10.1007/BF01327041

Primary publisher metadata and abstract read; full article not read. Abstract gives monotone moduli tending to zero as a sufficient condition on l-p, 1<=p<infinity. English translation Journal of Soviet Mathematics 37(5) (1987), 1323--1346; DOI identifies that translation.

