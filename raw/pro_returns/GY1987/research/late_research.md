# Late-record research and evidence log

**Scope:** records 739–751, academic year 1987–88. **Status date:** 11 November 2026. Russian transcription is authoritative; English is a translation to audit, not an independent source of mathematical hypotheses. This is a bounded literature and source audit, not a claim of exhaustive bibliographic coverage.

## Files and checkpoint

The completed shard contains 13 talk entries, 98 mathematical occurrences, six new problem entries GP-1987-41 through GP-1987-46, 31 correction rows, and 39 bibliography entries. Counts: E 74; A 8; F 7; B 7; C 2; D 0. `late_validation.json` records the mechanical validation. `late_areas.json` maps all occurrence IDs to subject areas. The reproducible builders are `write_late.py`, `write_late_references.py`, and this script. No earlier exact problem ID was reused; earlier quiver, matroid and exceptional-object material is mentioned as context without equating distinct questions.

The two C items are the named Riemann hypothesis and the explicit geometric essential-image problem for microlocal perverse data. The latter is not the solved codimension-three extension conjecture. No underspecified fragment was promoted to a D item or to a definite new open problem.

## Actual source boundaries

| Record | Actual pages | Boundary reason |
|---|---|---|
| 739 | P001444–P001445 | P001442–P001443 continue Radul. Local Kapranov heading has no date; catalogue supplies 21 March 1988. |
| 740 | P001446–upper P001447 | Zelevinsky, matroidal transversals. |
| 741 | lower P001447 | Gelfand's five historical examples. |
| 742 | upper P001448 | Rudakov, exceptional bundles and Markov data. |
| 743 | lower P001448–upper P001449 | Gelfand's representation/mutation discussion. |
| 744 | lower P001449–P001452 | S. Gelfand's microlocal/perverse account. |
| 745 | P001453–upper P001457 | Fuchs four-colour report. |
| 746 | lower P001457–P001459 | Microlocal/perverse continuation. |
| 747 | upper P001461 | Beilinson on strongly indefinite Morse theory. P001460 is a Bourbaki reading list, contextual only. |
| 748 | middle P001461 | Gelfand's circle polarization remark. |
| 749 | lower P001461–P001467 | Reshetikhin quantum groups and links. |
| 750 | P001468–upper P001472 | Ushveridze Riccati/quasi-exact solvability. |
| 751 | lower P001472–P001477 | Beilinson, Atiyah and gauge theory. |

P001478 explicitly begins a session dated 12 September 1988; P001479 continues with G. Moore. Parent independently inspected both scans. They are excluded from this academic year's mathematical inventory, with a provenance correction retained.

## Scan and formula checks

Russian/English source segments were compared throughout. Selected scans were viewed where symbols or diagrams matter, including P001449 mutation order, P001450 zero-section insertion, P001455 Birkhoff diamond, P001462 coproduct/antipode, P001463 R-series and coproduct order, P001467 framing correction, P001468 kernel identities and root equations, and P001471–P001472 electrostatics/Morse boundary. Parent independently viewed P001475 and P001478–P001479. The P001465 crossing-label correction follows the immediately preceding definition and the transcribed displayed formula; it is not described as a fresh independent scan inspection.

The P001455 configuration is the Birkhoff diamond: the ring and four internal vertices identify the classical reducible configuration. Fuchs's failure to reproduce its proof is not a statement that it remains an open problem. The numbered parallel-computer question is a definite implementation question, not a new four-colour conjecture; finite reducibility tests are established, while no unique machine architecture or performance target is specified.

## Search routes and exact scope

Searches used author/title/formula combinations, then opened the primary paper or official bibliographic record. Representative queries included Parthasarathy t-structures quivers 1988; Rudakov Markov exceptional bundles/quadric; Gelfand MacPherson Vilonen microlocal perverse sheaves; Kashiwara Vilonen codimension two essential image; Fuchs Birkhoff diamond Appel Haken reducibility; Reshetikhin 1987 preprint Yang–Baxter invariants links; Ushveridze Riccati electrostatic quasi-exactly solvable 1988/1989; and Atiyah 1987/1988 new invariants Floer.

For the final current-status check, searches for `"Kashiwara" "Vilonen" "Problem 9.3" perverse codimension two` and `"microlocal perverse sheaves" "codimension two" conditions essential image` with a two-year recency filter located the original paper, special-case descriptions, and Vilonen's institutional research page. The latter search excerpt says the problem reduces to codimension-two interactions, but both web OPEN and direct retrieval returned HTTP 502, so it is retained only as an unverified lead and is not a cited authority. Search timestamps are not publication dates: an old Braden paper was indexed as recent and was not treated as a new result. The directly opened 2025 Guminov article supplies a recent, explicitly restricted family, not a uniform solution.

The official Clay page was opened and still says the Riemann hypothesis is unsolved. No seminar-specific partial proof or bounded new project is present. The seven F items are the unexplained three-versus-four distinction (739.6), missing quadric numerical converse (742.6), geometric configuration fragment (744.1), unspecified replacement of the circle (748.2), unspecified meaning of SL2 invariants 'sufficing' (749.15), unrestricted kernel classification (750.4), and two bare nonlinear-Schrodinger/oscillator analogies (750.9). Each is explicitly restricted rather than silently completed into a research claim.

## Mathematical decisions and independent checks

1. **Quivers:** source/sink reflection gives derived equivalences, and finite trees allow passage between orientations. The general statement for arbitrary graph orientations is not inferred from the sketch. Parthasarathy's exact results concern finite acyclic quivers over an algebraically closed field, specified t-structures and a Dynkin completeness theorem.
2. **Exceptional objects:** positive ranks are required in the Markov equation. The notebook does not state the Markov uniqueness conjecture. The missing quadric numerical system is kept unidentified even though Rudakov's precise constructibility theorems were found. The claimed kernel mutation pair `(F,R)` is disproved by the evaluation map O^2→O(1) on P1: R=O(-1), and Hom(R,F) is nonzero. Correct pair order is `(R,E)` under the exact-sequence hypotheses.
3. **Open orbit:** simultaneous conjugation of matrix pairs has nonconstant invariant tr(A), so an orbit cannot be dense in the full affine parameter space. This refutes the unrestricted open-orbit slogan without claiming every wild stratum lacks rigid objects. The calculation was independently re-derived by the parent and marked `\ours`.
4. **Microlocal sheaves:** microsupport contains the zero covectors over support, not the whole zero section for every nonzero sheaf. Involutivity alone gives coisotropy and needs pure half-dimension to imply Lagrangian. Arbitrary compatible stratifications are not recovered uniquely. Test-function Hessians carry Maslov/orientation data. The exact perverse criterion in KS1985 is Theorem 9.5.2, printed pp. 171–172, not Chapter 10. GMV Theorems 5.1/6.4 and KV Theorem 1.1 do not give the codimension-two essential image; KV Problem 9.3, published p. 617, explicitly asks for it. Complex coefficients and a complex manifold are specified.
5. **Quantum formulas:** with L=q^(H/4), the printed coproduct forces S(X)=-LXL^(-1). The notebook misses the minus sign and doubles the exponent. K=q^(H/2) changes the commutator denominator to q^(1/2)-q^(-1/2) unless generators/parameter are rescaled. Both printed R-coproduct orders are reversed for the stated intertwining convention. Drinfeld §10 and Reshetikhin I Theorem 1.3 confirm the corrected order. The R-series must have nilpotent coefficients vanishing to the appropriate h order; no unique missing q exponent is guessed. Parent independently checked the antipode sign/exponent. Framing corrections use each colour's twist and signed self-writhe.
6. **Riccati residues:** for the rational kernel and distinct roots avoiding fixed poles, all double poles cancel. Root residues give sum_{j≠i}1/(lambda_i-lambda_j)+sum_alpha b_alpha/(lambda_i-a_alpha)=0, and fixed-pole residues give c_alpha=2b_alpha sum_i1/(lambda_i-a_alpha). The proper rational residual is then zero. Parent independently re-derived this exact specialization.
7. **Addition identity:** omega cot(omega z) requires Omega=-omega^2/3 in the notebook's plus-Omega convention. The Weierstrass example requires Omega=(zeta^2-wp)/2. Parent independently checked both. A simple pole of residue one and the regularity of Omega at zero are needed for the normalized Riccati limit. An unrestricted classification of all kernels is not inferred.
8. **Liouville calculation:** x'=A^(-1/2), P=2B sqrt(A)-A'/(2 sqrt(A)), Psi=A^(-1/4)exp(integral B)f, and V=P_x/2+P^2/4-AC. Parent independently re-derived the formula. For rational A a product of N linear factors, AC has degree at most N-2; only N=2 gives a single constant without fixing further coefficients.
9. **Electrostatics:** the repulsive minimum argument uses negative logarithms. For two ordered real fixed points, positive b1,b2 and integer M≥0, convexity gives the Jacobi configuration with eigenvalue M(M-1+2b1+2b2) and weight (lambda-a1)^(2b1-1)(a2-lambda)^(2b2-1). The exterior bound is sufficient, not generally necessary: M=1, a1=0, a2=1, b1=-1, b2=1/2 gives U=log(lambda)-(1/2)log(lambda-1), a strict minimum at 2 while b1+b2+M=1/2. Parent independently checked the example. It does not refute sufficiency. Ushveridze p. 1212 explicitly distinguishes classical and quantum thresholds.
10. **Gauge theory:** ordinary integral first homology is not equivalent to twisted first cohomology vanishing. Parent's development subsection `dev:twisted-h1` proves both failures: RP3 has vanishing H1 for all finite-dimensional real/complex local systems by finite-group averaging, yet integral H1=Z/2. For the connected sum of two Poincare spheres, the representation obtained from the binary icosahedral inclusion on both free factors is irreducible and has H1(ad rho) of real dimension three. I independently audited the group-cocycle and twisted Mayer–Vietoris computations and triviality of SU2 bundles over a 3-dimensional CW complex. The relation matrix rows are (5,-3),(-2,1), determinant -1. These are annotations/corrections, not a claimed new C/D development.

New calculations and counterexamples in the shard carry `\ours` or `\oursComputed` in reconstruction fields; these mark work performed here, not mathematical novelty. The parent owns the full formal development and its computational verification output.

## Chronology safeguards

- Parthasarathy: received 15 February 1988, revised 13 May, publication December 1988; the talk reports his work rather than claiming Kapranov's priority. Item 739.3 is B for the precise later t-structure-data realization refinement. Happel 1987 Theorem 5.12 already establishes the Dynkin/iterated-tilted endpoint, announced at Ottawa 1984; receipt of Parthasarathy establishes existence, not public pre-talk circulation of his criterion.
- Rudakov Markov: received April 1986, Russian publication 1988, English translation 1989. Quadric: received 6 July 1986, Russian issue 4 of 1988, English translation 1989.
- GMV: arXiv September 2005; this does not erase the notebook's 1988 report of the programme. KV: 2010 announcement, 2012 full preprint, 2014 publication.
- Reshetikhin scans: E-4-87 and E-17-87, with 1988 imprints. II explicitly records recommendation 6 June 1987. The exact public-circulation day is unestablished. Stable keys retain 1987, but BibTeX year follows the imprint. Drinfeld's 1986 lecture/1987 paper independently anchors the established core quantum-group material.
- Ushveridze: 1989 review cites 1988 FIAN announcements. No claim that 1989 was the first announcement is made.
- Atiyah: a 1987 preprint/lecture is documented separately from the 1988 publication; Floer's instanton paper was received 3 May and published June 1988.

## Opened-source register

`verified` in BibTeX means the named record or text was opened; the scope below and each item's verification field distinguish metadata, a result read, and an indirect match. A successful direct PDF download followed by a local text/image read is recorded as such. Failed web-reader attempts are not disguised as successful full-text reading. The source-reference IDs below are retrieval locators for the parent, not substitutes for URLs.

### appelhakenkoch1977reducibility

**Every planar map is four colorable. Part II: Reducibility**

URL: https://api.crossref.org/works/10.1215/ijm/1256049012

Evidence: Publisher-deposited Crossref metadata opened and saved locally. Author bibliography also opened at https://celebratio.org/Appel_KI/article/739/. Full original proof was not read; the argument structure was checked in Gonthier. The 1976 announcement and 1977 publication are distinguished.

Retrieval locators: turn110view3; local late_crossref.json; web API open turn141view1 failed but direct retrieval succeeded.

### atiyah1988invariants

**New invariants of 3- and 4-dimensional manifolds**

URL: https://math.berkeley.edu/~gbeiner/texts/Atiyah_Invariants.pdf

Evidence: Full primary text opened. Sections 2--5 and 7 read: Morse complex, Chern--Simons functional, mod-eight relative index and perturbations (p. 289), symplectic interpretation, and cutting/gluing. A 1987 preprint is cited by Floer 1988; publication is 1988. This is a programme/exposition, not a proof of every Floer-theoretic analytic assertion.

Retrieval locators: turn13view0, turn85view1, turn87view0, turn87view2.

### beilinson1978coherent

**Coherent sheaves on {$P^n$} and problems of linear algebra**

URL: https://www.mathnet.ru/eng/faa2009

Evidence: Math-Net bibliographic record opened; received 10 January 1978. Used as a thematic source for projective-space linear algebra; no inherited assertion of reading its theorem is made in this late-record audit.

Retrieval locators: turn108view0.

### beilinson1987glue

**How to glue perverse sheaves**

URL: https://people.mpim-bonn.mpg.de/gaitsgde/grad_2009/Beilinson%20--%20How%20to%20glue%20perverse%20sheaves.pdf

Evidence: Primary typed text opened; introduction read. It dates S. I. Gelfand notes to 1982 and the nearby-cycle work with Bernstein to spring 1981. Used as gluing/intermediate-extension context. Detailed proof of the gluing equivalence was not reread in this shard.

Retrieval locators: turn108view1.

### beltrami1869interpretation

**Essai d’interprétation de la géométrie non-euclidienne**

URL: https://www.numdam.org/item/ASENS_1869_1_6__251_0/

Evidence: Numdam primary-publication metadata opened. This is the 1869 French version of the 1868 Italian work. The full proof was not read; the item is explicitly a historical/relative-consistency reconstruction.

Retrieval locators: turn46view2.

### berezingelfand1956spherical

**Some remarks on the theory of spherical functions on symmetric Riemannian manifolds**

URL: https://www.mathnet.ru/eng/mmo51

Evidence: Math-Net record opened and received date 28 June 1955 checked. The exact cosine product formula used in the item was verified directly; the source is a thematic historical match, not a claim of its exact example or a personal invention chronology.

Retrieval locators: turn108view2.

### bernhart1977digest

**A digest of the four color theorem**

URL: https://onlinelibrary.wiley.com/doi/abs/10.1002/jgt.3190010305

Evidence: Publisher abstract opened. It reports 1200 computer hours and nearly 1900 configurations. Used only to assess the manuscript 12000-hours figure and its own 1200-question mark; not attributed to the original Appel--Haken paper.

Retrieval locators: turn76view0.

### bernsteingelfandponomarev1973coxeter

**Coxeter functors and Gabriel's theorem**

URL: https://www.math.tau.ac.il/~bernstei/Publication_list/publication_texts/BGG-CoxeterF-Usp.pdf

Evidence: Author-hosted complete English text opened. Introduction and section 1 reflection functors, especially pp. 20--21, read. Reflection at a source/sink and the Dynkin finite-type scope were checked; an unrestricted orientation-independence claim for every graph is not inferred.

Retrieval locators: turn24view3.

### clay2026riemann

**Riemann Hypothesis**

URL: https://www.claymath.org/millennium/riemann-hypothesis/

Evidence: Official problem page opened and read; it explicitly labels the problem unsolved. The year is the access year. No unverified numerical zero count is used.

Retrieval locators: turn41view1, turn69view3.

### drinfeld1987quantum

**Quantum groups**

URL: https://ncatlab.org/nlab/files/Drinfeld-QuantumGroups.pdf

Evidence: Full scan of the primary congress report opened. Copyright 1987 on p. 798; sections 1, 6 (p. 807), 10 (pp. 811--812), and 13 (pp. 816--817) read for the Hopf axioms, symmetric coproduct, quasitriangular identities and rank-one R-series with h powers. Math-Net also confirms the extended Russian version appeared in LOMI 155 (1986), pp. 18--49: https://www.mathnet.ru/eng/znsl5159. This independently establishes pre-seminar existence of the core framework.

Retrieval locators: turn122view0, turn123view0, turn139view0; Russian publication metadata turn121view0.

### duistermaat1974morse

**L'indice de {Morse} dans le calcul variationnel**

URL: https://www.numdam.org/item/SEDP_1973-1974____A23_0.pdf

Evidence: Full primary PDF opened. Introduction and sections 1--3 inspected for Hessian/Morse index, conjugate points, Lagrangian crossings and endpoint conventions. No infinite-index subtraction is justified merely by two infinite-dimensional negative subspaces.

Retrieval locators: turn73view1.

### floer1988instanton

**An instanton-invariant for 3-manifolds**

URL: https://link.springer.com/article/10.1007/BF01218578

Evidence: Publisher metadata and abstract opened: received 3 May 1988 and published June 1988. The abstract describes the graded homology-sphere invariant. Full analytic proof was not read in this audit. The source cites Atiyah as a 1987 preprint.

Retrieval locators: turn50view5.

### gelfandmacphersonvilonen2005microlocal

**Microlocal perverse sheaves**

URL: https://arxiv.org/pdf/math/0509440

Evidence: Abstract record and full primary preprint opened. First arXiv circulation 19 September 2005. Section 1 and Theorems 5.1 and 6.4 read: equivalence away from the codimension-two locus and global fully faithful embedding into melded Morse data. Essential surjectivity at arbitrary singular loci is not asserted.

Retrieval locators: turn13view1, turn13view2, turn17view6; parent independently reopened full text.

### gonthier2005fourcolour

**A computer-checked proof of the Four Colour Theorem**

URL: https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/gonthier-4colproof.pdf

Evidence: Full 57-page primary report opened. Sections 2--3 read for graph/map conventions, Kempe changes, the Birkhoff diamond, reducibility, unavoidability and discharging; the introduction says the formal proof is largely based on Robertson et al. The report is undated internally and commonly catalogued as 2005, not 2016 (the URL upload date).

Retrieval locators: turn51view1, turn73view3, turn76view2, turn119view2, turn139view1.

### goreskymacpherson1983intersection

**Intersection homology II**

URL: https://www.math.ias.edu/~goresky/pdf/IH2.pdf

Evidence: Author-hosted primary PDF opened, but text extraction was unavailable and the exact theorem proof was not read in this shard. Used as the foundational intersection-cohomology source with indirect verification, not an inherited proof-reading claim.

Retrieval locators: turn110view0.

### gorodentsevrudakov1987exceptional

**Exceptional vector bundles on projective spaces**

URL: https://publications.hse.ru/en/articles/74955462

Evidence: Institutional publication record opened; full-text retrieval did not succeed. Exceptional-pair and mutation statements were matched in the other opened Rudakov originals. No exact reading of this article is claimed.

Retrieval locators: turn51view2.

### guminov2025perverse

**Perverse sheaves on smooth toric varieties and stacks**

URL: https://www.mathnet.ru/eng/im9687

Evidence: Primary full HTML opened. Introduction and Theorem 1 read: orbit-constructible perverse sheaves on a smooth complex toric variety are described by finite-dimensional modules over an explicit algebra. Introduction explains the limited families with known explicit descriptions. Received 27 December 2024, revised 18 March 2025, published 19 November 2025. This is context for scope, not a claim to solve arbitrary microlocal codimension-two compatibility.

Retrieval locators: turn41view0, turn116view0.

### hall1935representatives

**On Representatives of Subsets**

URL: https://deltadbu.github.io/UCAS_algorithm_course/Lectures/Hall1935.pdf

Evidence: Original five-page paper downloaded and read locally after the web reader failed. Theorem 1 and constructive proof, and Theorem 3 with equal-block corollary on pp. 29--30, read. Received 23 April 1934; read 26 April 1934; publication January 1935 confirmed with opened publisher-deposited Crossref metadata. The equal-block result is credited to Konig by Hall.

Retrieval locators: direct primary PDF retrieval and local read primary/hall1935.txt; local late_crossref.json.

### hatcher2002algebraic

**Algebraic Topology**

URL: https://pi.math.cornell.edu/~hatcher/AT/ATch2.pdf

Evidence: Author-hosted Chapter 2 opened. Parent chapter audit checked Examples 2.38 and 2.42--2.43 for the Poincare homology sphere and lens-space/projective-space homology. The connected-sum local-system calculation is an independent proof in dev:twisted-h1, not a claimed theorem quoted from Hatcher. Earlier cumulative Chapter 0 verification is not inherited.

Retrieval locators: turn110view2; parent independent Chapter 2 read.

### kashiwara1980constructible

**Faisceaux constructibles et syst\`emes holonomes d'\'equations aux d\'eriv\'ees partielles lin\'eaires \`a points singuliers r\'eguliers**

URL: https://www.numdam.org/item/SEDP_1979-1980____A20_0.pdf

Evidence: Primary PDF opened. Main theorem on XIX.1--2 read, giving the regular-holonomic/constructible derived equivalence. Title page dates the lecture 22 April 1980. The source is A20; the neighboring A19 is not this lecture.

Retrieval locators: turn69view2.

### kashiwara1984riemann

**The Riemann--Hilbert problem for holonomic systems**

URL: https://ems.press/journals/prims/articles/3160

Evidence: Publisher record opened, with received date 4 March 1983 and publication 30 April 1984. The exact derived-equivalence statement was read in the 1980 primary announcement; this shard does not inherit the earlier cumulative claim of reading the full 1984 proof.

Retrieval locators: turn110view1.

### kashiwaraschapira1985microlocal

**Microlocal study of sheaves**

URL: https://www.numdam.org/item/AST_1985__128__1_0.pdf

Evidence: Complete 238-page primary PDF downloaded from Numdam after the web-reader size limit, and text read locally. Definition 0.1, section 3.1, involutivity Theorem 6.4.1, constructibility discussion in Chapter 8, and perverse criterion Theorem 9.5.2 on printed pp. 171--172 checked. The relevant perverse criterion is in section 9.5, not Chapter 10 of this volume.

Retrieval locators: direct primary PDF retrieval and local read primary/kashiwaraschapira1985.txt; web reader exceeded size limit.

### kashiwaravilonen2014codimension

**Microdifferential systems and the codimension-three conjecture**

URL: https://arxiv.org/pdf/1209.5124

Evidence: Full primary preprint and Annals publication record opened. Theorem 1.1 and coefficient qualification read; Problem 9.3 is the exact codimension-two essential-image problem (published p. 617; preprint p. 46). Introduction says results were announced in 2010; full preprint appeared in 2012 and final publication in 2014. The item uses complex coefficients; arbitrary-coefficient extension is not asserted.

Retrieval locators: turn17view0, turn36view3, turn73view2, turn117view1, turn118view0, turn118view1; parent read published Problem 9.3 p. 617.

### lindemann1882pi

**Ueber die Zahl {$\pi$}**

URL: https://link.springer.com/article/10.1007/BF01446522

Evidence: Primary publisher metadata opened and checked. The full original proof was not read; attempted digitization URL failed and a search hit at SFU proved to be a different lecture PDF. This entry is verified only at the publication-record level.

Retrieval locators: turn119view0; full-proof lead unresolved.

### nist2026dlmf

**Digital Library of Mathematical Functions**

URL: https://dlmf.nist.gov/

Evidence: Opened and read exact sections https://dlmf.nist.gov/5.18 (q-gamma definition/recurrence), https://dlmf.nist.gov/14.30 (scalar spherical harmonics), and https://dlmf.nist.gov/23.10 (Weierstrass addition identities). Access year, not discovery date. The reused cumulative key previously named only section 18.5; this entry broadens the source title without claiming an independent rereading of that section.

Retrieval locators: turn85view0 (5.18), turn86view0 (14.30), turn86view1 (23.10).

### oxleybriefly

**Briefly, what is a matroid?**

URL: https://www.math.lsu.edu/~oxley/matroid_intro_summ.pdf

Evidence: Full author PDF opened. Definitions 1.2 and 1.4 and Example 1.5 checked for independence and representability. No publication date is inferred for the undated file; it is a modern reference for classical matroid facts.

Retrieval locators: turn108view3.

### parthasarathy1988tstructures

**t-structures in the derived category of representations of quivers**

URL: https://repository.ias.ac.in/82619/1/1-Pub.pdf

Evidence: Full primary PDF initially opened and read: Propositions 1.4 and 1.6, Theorem 3.3, Theorem 7.1, and Theorem 8.5. Received 15 February 1988, revised 13 May 1988, published December 1988. Later attempts returned 403, but the initial successful read is retained in the evidence log. Scope is an algebraically closed field, a finite acyclic quiver, specified t-structure data and the Dynkin completeness case.

Retrieval locators: turn5view0 initial successful full-text read; repeat opens turn116view1 and turn117view0 returned 403; search turn118search5 reconfirmed metadata.

### rado1942independence

**A theorem on independence relations**

URL: https://api.crossref.org/works/10.1093/qmath/os-13.1.83

Evidence: Publisher-deposited Crossref metadata opened and saved in late_crossref.json. The publisher article URL was located but its full text was not retrieved. The precise matroid-transversal rank formula is identified as the classical theorem; this audit is not a reading of its original proof.

Retrieval locators: local late_crossref.json from direct Crossref retrieval; web API open turn141view0 unavailable; publisher search turn54search0.

### reshetikhin1987quantizedi

**Quantized universal enveloping algebras, the Yang--Baxter equation and invariants of links, I**

URL: https://math.berkeley.edu/~reshetik/Publications/QGInv-1-1987.pdf

Evidence: Full author-hosted scan downloaded and cover viewed: E-4-87 is the series identifier; scanned imprint is Leningrad 1988. Typed primary transcription also opened at https://math.soimeme.org/~arunram/Resources/Reshetikhin/QUEAYBEILI1.html; Definition 1.1, Theorems 1.1--1.3, Propositions 1.1--1.2 and tensor-product discussion checked. June 1987 recommendation is not an independently established first public-circulation date. Stable key retains 1987 for continuity, while the bibliographic year follows the scanned imprint.

Retrieval locators: turn50view1 original scan; turn69view0, turn85view2 typed primary transcription; local rescoveri.png.

### reshetikhin1987quantizedii

**Quantized universal enveloping algebras, the Yang--Baxter equation and invariants of links, II**

URL: https://math.berkeley.edu/~reshetik/Publications/QGInv-2-1987.pdf

Evidence: Full author-hosted 24-page scan opened and downloaded; cover visually read. It states E-17-87, recommendation for publication 6 June 1987, and Leningrad 1988 imprint. Link-invariant programme matched with Part I introduction and the later ribbon-graph paper; no claim to have read every scanned coefficient formula. First public-circulation date is not inferred solely from the number or recommendation.

Retrieval locators: turn50view0 original scan; local rescoverii.png.

### reshetikhinturaev1990ribbon

**Ribbon graphs and their invariants derived from quantum groups**

URL: https://people.math.harvard.edu/~opie/Reshetikhin_Turaev.pdf

Evidence: Complete primary article opened. Section 3 equations (3.1.1)--(3.1.3), section 5 ribbon-graph functor, and section 6 link invariants read. Framed-link evaluation and twist correction are distinguished from the manuscript unweighted under/over count. This is a precise later publication match, not proof of a 1987 circulation date.

Retrieval locators: turn24view1.

### rudakov1988markov

**The Markov numbers and exceptional bundles on the projective plane**

URL: https://www.mathnet.ru/eng/im1170

Evidence: Math-Net record and full English primary translation opened and downloaded. Introduction and Theorems 3.2 and 4.2 read. Received 22 April 1986. Original Russian publication is 1988; English translation is Mathematics of the USSR-Izvestiya 32(1), 99--112 (1989), whose DOI is supplied. Positive Markov triples are distinguished from an unstated Markov uniqueness conjecture.

Retrieval locators: turn13view3, turn17view3; local primary/rudakov1988markov.txt.

### rudakov1988quadric

**Exceptional collections on a quadric**

URL: https://www.mathnet.ru/eng/im1205

Evidence: Math-Net record and complete English primary translation opened and downloaded. Theorem 6.3 rank equation, Theorem 7.1 constructibility of helices, and Theorem 10.1 constructibility of exceptional bundles read. Received 6 July 1986, as printed on the last page. English translation: Mathematics of the USSR-Izvestiya 33(1), 115--138 (1989). These theorems do not identify every equation of the omitted notebook numerical system.

Retrieval locators: turn5view1, turn17view2; local primary/rudakov1988quadric.txt.

### stoimenowtanaka2008mutation

**Mutation and the colored Jones polynomial**

URL: https://arxiv.org/pdf/math/0607794

Evidence: Primary preprint version 3, dated 24 September 2008, opened. Theorem 1.1 read: infinitely many pairs of hyperbolic knots with the same colored Jones polynomials that are not mutants. First-version footnote says 11 December 2005; first arXiv circulation is 2006. Used only against the explicitly conditional knot-separation reading of the ambiguous seminar phrase. Appendix by Daniel Matei.

Retrieval locators: turn69view1.

### ushveridze1989quasiexact

**Quasi-exactly solvable models of quantum mechanics**

URL: https://www1.jinr.ru/Archive/Pepan/1989-v20/v-20-5/pdf_obzory/v20p5-4.pdf

Evidence: Complete 61-page primary Russian review downloaded, selected scan pages viewed, and Russian OCR read. Section 3 Theorem 4 pp. 1197--1198; section 4 pp. 1199--1201; section 5 pp. 1210--1212; section 9 equation (113) p. 1232; and sections 11--12 pp. 1235--1237 checked. The bibliography cites the author's 1988 FIAN announcements. The review explicitly distinguishes classical and quantum stability thresholds; the notebook unrestricted biconditional is not adopted.

Retrieval locators: direct original JINR PDF retrieval; local ushveridze1989.pdf, qes_ocr/*.png, ushveridze1989_ocr.txt.

### wantzel1837constructions

**Recherches sur les moyens de reconna\^{i}tre si un probl\`eme de g\'eom\'etrie peut se r\'esoudre avec la r\`egle et le compas**

URL: https://www.numdam.org/item/JMPA_1837_1_2__366_0.pdf

Evidence: Primary original opened. Section I quadratic-construction criterion and its application to general angle trisection read. This does not itself prove transcendence of pi or the impossibility of circle quadrature.

Retrieval locators: turn46view1.

### wiles1995modular

**Modular elliptic curves and Fermat's Last Theorem**

URL: https://annals.math.princeton.edu/1995/141-3/p01

Evidence: Primary publisher record opened and publication metadata checked. The full proof was not read. The 1993 announcement is distinguished from final 1995 publication after repair with Taylor; Faltings finiteness is not equated to Fermat nonexistence.

Retrieval locators: turn46view0.

### witten1982supersymmetry

**Supersymmetry and Morse theory**

URL: https://math.berkeley.edu/~gbeiner/texts/Witten_Morse_Theory.pdf

Evidence: Full primary PDF opened; introduction and the Morse-theoretic interpretation inspected. The specific gradient-trajectory chain complex was also read in Atiyah section 2. This shard does not inherit an earlier cumulative claim of reading all analytic sections of Witten.

Retrieval locators: turn73view0.

### happel1987derived

**On the derived category of a finite-dimensional algebra**

URL: https://gdz.sub.uni-goettingen.de/download/pdf/PPN358147735_0062/LOG_0020.pdf

Evidence: Full primary scan opened and downloaded. Printed pp. 339, 344 and 358 read via local OCR: section 1.7 Corollary gives tilting-derived equivalence; Theorem 5.12 gives the Dynkin/iterated-tilted classification. Introduction states these results were announced at Ottawa in 1984. Used to distinguish the pre-existing Dynkin classification from Parthasarathy 1988 specific t-structure-data realization criterion.

Retrieval locators: turn152view0; original scan read via local OCR primary/happelpage2.txt, happelpage7.txt, happelpage21.txt.

## Validation and access limits

The data validation checked consecutive item numbering in each of the thirteen records; all problem occurrences resolve; all C/D items have worth statements; all LaTeX citation keys are listed in refs; all 39 referenced keys exist in the 39-entry bibliography; no unused bibliography entries or control characters remain. Every reused bibliography entry was rewritten with this shard's actual opening/reading scope rather than inheriting prior verification prose. A Python escape issue that produced TAB followed by `extquotesingle` is normalized in the builder before saving, so it cannot recur on rebuild.

The original Rado proof, the complete Gorodentsev–Rudakov Duke article, and the full Lindemann proof were not successfully read. Their metadata records are identified honestly. Goresky–MacPherson's original PDF opened but text extraction was unavailable; no exact proof-reading claim is made. These limits do not turn established classical statements into D items. LaTeX compilation and integration are owned by the parent, whose build environment initially lacked its TeX macro tree.
