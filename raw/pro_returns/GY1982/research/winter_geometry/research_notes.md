# Winter geometry research audit: records 574–585

Audit date: 11 November 2026. The academic-year prefix remains **1982** for the February 1983 records. The shard contains **12 catalogue records, 117 mathematical items, 4 problem entries, 37 correction rows and 44 bibliography entries**. Classes: **A 21, B 5, C 0, D 0, E 82, F 9**. Twenty-eight items are marked false as written; every one has a correction-row crosswalk in `correction_map.json`. Thirty-three correction rows are faithful notebook errors, and four identify ambiguities. They are not presented as transcription mistakes when the scan supports the transcription.

`write_shard.py` regenerates the five substantive data files and saves after each record. `checks.py` and `checks_output.txt` preserve the independent editorial checks. `area_by_record.json` supplies the area and per-item mapping for the combined report. The root agent performs the final chapter build and upload.

## Record boundaries and coverage

Catalogue ranges are preserved in `talks.json`; the narrower ranges below govern occurrence items. The original Russian transcription was consulted at mathematical, lexical and normalization issues, and the handwritten page was inspected wherever a formula, diagram or doubtful reading decided the issue.

| Record | Actual mathematical pages | Items | Principal subject |
|---|---|---:|---|
| 574 | P001060 | 5 | Regular singular D-modules and gluing |
| 575 | Top of P001061 | 4 | Schubert geometry and continuous-dimensional flags |
| 576 | P001061–P001063 | 10 | Superspaces, flags and gauge geometry |
| 577 | P001064–P001069 | 22 | Classical and quantum Liouville theory |
| 578 | P001070–P001073 | 10 | Domain walls, vortices and strings |
| 579 | Heading on P001074 | 0 | Year 1983 heading only |
| 580 | Upper P001074 | 5 | Near-unitary actions and Gaussian/Fock representations |
| 581 | Lower P001074–P001075 | 8 | String constraints and semi-infinite homology |
| 582 | P001076–P001077 | 10 | Circle representations and endpoint forms |
| 583 | P001078–upper P001079 | 14 | Symplectic reduction and exact stationary phase |
| 584 | Lower P001079–P001080 | 5 | SU(3) orbits and weight multiplicities |
| 585 | P001081–P001086 | 24 | Hill gaps and perturbation diagrams |

The large supplied ranges overlap and include adjacent talks. In particular, P001080 belongs to Kirillov, P001081 starts Arnold, and P001087 starts Krichever. No mathematical content from the neighboring talks is assigned to heading 579.

## Scan audit

All pages **GELFAND-P001060 through GELFAND-P001086 inclusive** were visually inspected, using the original scans or the resized copies in `scan_views`. The following are the decisive checks, not a claim that every handwriting uncertainty can be solved:

- **P001060:** two-map convention, invertibility sign and incomplete final nearby-cycle tuple; the final “something” is not silently completed as a literal theorem.
- **P001061–P001063:** Schubert-cell dimension, Gelfand/Manin boundary, tautological-bundle diagram, the odd projective-coordinate index, and the odd bilinear form. The flag-classification question is distinct from the subsequent cohomology question.
- **P001064–P001069:** Liouville normalization, the incorrect Schwarzian denominators, reuse of the stress-tensor symbol for the ODE coefficient, reality of accessory parameters, momentum derivative, Laurent modes and missing central Kronecker delta, area versus contour charge, three missing primary-field powers, incomplete descendant projector, missing oscillator factor one-half, and the final differential operator. The scan confirms these omissions; the corrections are mathematical emendations.
- **P001070–P001073:** scalar-potential derivative, wall profile and width, gauge-transform sign, Lorentzian “minimum,” and mixed final colour-field conventions.
- **P001074–P001075:** the manuscript explicitly corrects “unitarily” beside the weighted pullback; the new Gaussian/Fock action is a different representation space. Feigin’s physical-state image and the closing p-adic request are separate items.
- **P001076–P001077:** unrestricted power-kernel parameter, sign of the logarithmic form, unnormalized Hardy projections, proposed delta derivative, and the uncertain second argument of the analytic sequence.
- **P001078–P001080:** level set versus reduced-space volume, nonisolated fixed-point denominator, missing stationary-phase power, Casimir map versus diagonal moment map, hexagon geometry, and the final isolated weight-multiplicity request.
- **P001081–P001086:** the asymptotic-equivalence symbol and ambiguous integer brackets in the gap estimate; unsupported exponential decay for generic smooth potentials; the handwritten 138, truncated Catalan convolution, and polygon index; invariant-graph maps and diagram denominator signs; Fourier-block signs, which are correct under the stated source-to-target convention; the remote-loop argument; and the explicit dual-word example on P001086.

## Chronology, exact matches and limits of classification

1. **Beilinson:** the 1987 printed chapter explicitly follows S. I. Gelfand’s 1982 notes and identifies a spring 1981 construction with Bernstein. The late publication date is not treated as the date the gluing idea first circulated.
2. **Manin:** the 1983 chapter is a close publication match, but only publisher metadata and abstract were available. Its full classification theorem was not independently read. `GP-1982-20` therefore records a verification limit, not an assertion that the classification remains open.
3. **Polyakov:** the classical accessory-parameter conjecture has an exact subsequent theorem, with a necessary sign and normalization convention. The 1985 announcement, 1987 Russian full paper and 1988 English translation are distinguished. BPZ was received in November 1983 and published in 1984, after the November 1982 seminar. Modern rigorous Liouville theorems are stated only in their verified coupling and insertion ranges.
4. **Neretin/Feigin:** the 1982 complementary-series paper predates the February 1983 report; the later bosonic group realization and semi-infinite homology note are separately dated. Neretin’s 1983 paper attributes the bosonic Lie-algebra construction to Chodos–Thorn (1974); that antecedent is explicitly indirect because the 1974 primary text was not obtained. Feigin’s note was received in January 1983 and published in 1984; receipt is not proof of public preprint circulation.
5. **Duistermaat–Heckman/localization:** the original variation paper is from 1982. Atiyah–Bott’s 1984 published text explicitly cites 1982 preprints of the Addendum and Berline–Vergne, supporting pre-talk circulation of those ideas. Journal receipt alone is not used for this inference. The handwritten attribution to Semenov-Tian-Shansky is identified as his 1973 compact semisimple stationary-phase paper; the Vergne attribution is identified as the 1979 proof of Rossmann’s discrete-series formula. These are more precise than assigning all of the page to a general localization theorem.
6. **Kirillov:** `GP-1981-41` is reused after checking the previous index’s weight-multiplicity question and occurrences `1981-556.1` and `1981-556.6`. Convexity alone is not equated with a multiplicity formula. Reduced volume, reduced-space index and the orbit’s shifted character formula are separated.
7. **Arnold:** the paper closely matches the notebook and was received on 1 February 1983, before the 21 February talk. Its **Supplement dated 30 March 1983** explicitly credits **Bloch (1958) for Theorems 1, 2 and 4–6; Levy–Keller (1963) for Theorem 3; Hochstadt (1964) for Theorem 7**. The old mathematical results are E; the particular verified diagrammatic presentation and involution proof are A. The older papers’ theorem comparison is attributed to Arnold because only their metadata was independently verified.
8. **Gelfand’s one-gap question:** item `1982-585.6` stays F because the perturbation class and desired conclusion are absent. Its forward link to `1982-586.3–6` is expressly thematic. Krichever’s precise first-order framework is read in the original paper; it is not asserted to answer every interpretation of the question, and no shared GP identity is invented.

There is **no defensible C or D candidate in this range**. The unresolved items are underidentified questions or verification limitations, not evidence of unworked mathematics. No broad field is declared solved and no open problem is manufactured from a missing normalization or an inaccessible chapter.

## Search and cross-year audit

Searches combined speaker/date/topic queries with Math-Net, author bibliographies and the references of the eventual matching papers. Productive searches included “Beilinson how to glue perverse sheaves 1982 notes,” “Manin flag superspaces supersymmetric Yang Mills,” “Polyakov accessory parameters Zograf Takhtajan,” “Neretin complementary series diffeomorphism 1982,” “Feigin semi-infinite homology 1984,” “Neretin p-adic projective line,” “Semenov-Tian-Shansky Kirillov formula stationary phase 1973,” “Vergne Rossmann 1979,” and “Arnold perturbation theory Mathieu 1983.”

The earlier occurrence index and cumulative bibliography were searched by exact mathematical topic and hypotheses. The convexity occurrences `1980-508.15` and `1981-556.12` are relevant background; they are not a replacement for the distinct multiplicity problem. The cumulative keys are reused for Beilinson–Bernstein, Gross–Wilczek, Atiyah convexity, Kirillov characters, Gelfand–Tsetlin, Meinrenken–Sjamaar and Grébert–Kappeler–Pöschel. Coordinated keys for BPZ, Feigin–Fuchs, Gelfand–Fuchs, DKRV and Krichever are shared with the neighboring agents.

Records 568 and 570 were compared with record 583 in coordination with the autumn agent. Orbital integrals and characteristic/null foliations are thematic connections, but the later finite-dimensional reduction/localization exposition does not supply an exact repeated problem requiring a shared GP.

For the broad one-gap question, a current primary-source search with a recent-time filter included “site:arxiv.org Hill one gap potential perturbation gap opening 2024 2025 2026” and weighted-regularity/gap-decay variants. It found related Hill/KdV and inverse-spectral literature, but no source supplying the missing historical quantifiers. This negative search is not offered as evidence of an open problem. Similar caution applies to continuous-dimensional Schubert topology, the unspecified odd cohomology theory, the coalescence question, the endpoint smoothness threshold, and the unspecified monopole model.

## Bibliography opening and result-verification audit

Every key below occurs in `references.bib`. “Opened” means an actual successful retrieval during this task, not just a remembered citation. The note `verified` certifies the opening; the separate result-verification level records what was actually read. Failed full-text retrievals are reported explicitly.

### gelfandponomarev1968lorentz

Opened [Math-Net record](https://www.mathnet.ru/eng/rm5609) and its linked English full text. Read the introduction and the finite compact-type multiplicity hypotheses of the classification. This is the exact 1968 work Gelfand names. The category is not all arbitrary Hilbert representations of the Lorentz group.

### beilinson1987glue

Opened [full author-hosted chapter](https://people.mpim-bonn.mpg.de/gaitsgde/grad_2009/Beilinson%20--%20How%20to%20glue%20perverse%20sheaves.pdf). Read the introduction, Proposition 3.1 and Corollary 3.2. The introduction supplies the 1982 Gelfand-note provenance and spring 1981 Bernstein collaboration. Printed publication is 1987; an online upload date is not substituted for it.

### beilinsonbernstein1981localisation

Opened [Bernstein’s publication list](https://www.math.tau.ac.il/~bernstei/Publication_list/Publication_list.html). The [full PDF URL](https://www.math.tau.ac.il/~bernstei/Publication_list/publication_texts/BernBeil_Localization_of_g-modules.pdf) exceeded the retrieval size limit. **Metadata verification only.** The geometric block/equivariance conditions in item 574.2 are labeled reconstruction; no full theorem rereading is claimed.

### vonneumann1960continuous

Opened the [Princeton publisher page](https://press.princeton.edu/books/paperback/9780691058931/continuous-geometry) and [publisher preview](https://api.pageplace.de/preview/DT0400.9781400883950_A26870033/preview-9781400883950_A26870033.pdf). Checked original 1960 publication and the 1935–1937 lecture origin against the later reprint. This is background for continuous projection dimension, not a resolution of Gelfand’s unspecified Schubert-topology programme.

### etingof2024lie

Opened [full MIT 2024 notes](https://live.ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf). **Section 47.2, Exercise 47.4 and Corollary 47.7** give the relevant Schubert-cell description. An earlier online edition at `math.mit.edu/~etingof/lnlg.pdf` had different numbering; the final locator follows the reopened 2024 edition. Used as a modern exposition of an old result, not as a priority claim.

### manin1981holomorphic

Opened [Math-Net](https://www.mathnet.ru/eng/intd47) and [Russian full text](https://www.mathnet.ru/php/getFT.phtml?jrnid=intd&option_lang=eng&paperid=47&what=fullt). Read the introduction and §1 Grassmannian geometry. The Russian original is 1981; the English translation is *Journal of Soviet Mathematics*, 21(4), 465–507 (1983), DOI 10.1007/BF01084284.

### manin1983flags

Opened [Springer chapter metadata and abstract](https://link.springer.com/chapter/10.1007/978-1-4757-9286-7_10). **Full chapter not obtained.** Bibliographic match is close; the complete flag-classification theorem is not claimed as independently verified. This limitation is explicit in the item and problem status.

### voronovmanin1990supercells

Opened [full author-hosted text](https://www-users.cse.umn.edu/~voronov/papers/Manin.Voronov.1990.spofs.pdf). Read the introduction, §§1–2 and §§5–6. Russian original: *Itogi*, 32, 27–70 (1988); English translation: *Journal of Soviet Mathematics*, 51(1), 2083–2108 (1990). General superflag and Schubert theory does not automatically identify the odd cohomology theory Gelfand intended.

### zograftakhtajan1985action

Opened [Math-Net](https://www.mathnet.ru/eng/faa1385) and linked full Russian announcement. Read the accessory-parameter claim and normalization. Received 29 March 1985; published 1985. Receipt is not a public-preprint date.

### zograftakhtajan1988liouville

Opened [Math-Net](https://www.mathnet.ru/eng/sm1767) and [full English paper](https://www.mathnet.ru/php/getFT.phtml?jrnid=sm&option_lang=eng&paperid=1767&what=fullteng). Read §1 uniformization, §3 Theorem 1 and Remark 7. The coefficient is for the full Schwarzian projective connection; the ODE coefficient is half of it. Russian full paper 1987, English 1988, received 1 April 1986; the introduction identifies the 1985 announcement and Polyakov’s conjecture.

### davidkupiainenrhodesvargas2016liouville

Opened [arXiv record](https://arxiv.org/abs/1410.7318) and [full preprint](https://arxiv.org/pdf/1410.7318). Read Theorems 3.2, 3.5 and 3.11: the Seiberg bounds and Weyl-anomaly normalization are essential. First arXiv circulation 27 October 2014; *Communications in Mathematical Physics* publication 2016. No unrestricted coupling claim is made.

### guillarmoukupiainenrhodesvargas2024bootstrap

Opened [arXiv record](https://arxiv.org/abs/2005.11530) and [full preprint](https://arxiv.org/pdf/2005.11530), reading Theorem 1.1 and §8 on blocks and spectral resolution. First arXiv circulation 23 May 2020. The [author’s institutional publication record](https://researchportal.helsinki.fi/en/publications/conformal-bootstrap-in-liouville-theory/) verifies *Acta Mathematica*, 233(1), 33–194 (2024), DOI 10.4310/ACTA.2024.v233.n1.a2. Direct publisher-PDF retrieval returned 403; the publisher PDF is not claimed as read. The item preserves the theorem’s real-coupling and channel insertion bounds.

### neretin1983highest

Opened [Math-Net](https://www.mathnet.ru/eng/faa1567) and [full author-hosted paper](https://mat.univie.ac.at/~neretin/papers/highest.pdf), with local scan rendering/OCR. Read Theorems 1–2 and the preceding oscillator formula. Exact title: “Unitary representations with highest weight of the group of diffeomorphisms of a circle”; *Functional Analysis and Its Applications*, 17(3), 235–237 (1983), DOI 10.1007/BF01078115. Received 31 March 1983. Chodos–Thorn (1974) is an **indirect antecedent through Neretin**, not a directly inspected primary source.

### belavinpolyakovzamolodchikov1984infinite

Opened [full primary paper](https://qft.itp.ac.ru/BPZ.pdf). Read §§2–4, especially (2.18), (2.20), (2.21), primary-field covariance, Gram descendants and conformal blocks. Received 22 November 1983; published 1984. This cannot establish publication by the seminar’s 22 November 1982 date.

### gelfandfuchs1968circle

Opened [Math-Net metadata](https://www.mathnet.ru/eng/faa2800). The concrete cocycle/mode normalization was checked in the full Feigin–Fuchs 1982 and BPZ 1984 texts. Original-result verification is therefore **indirect**, although the 1968 bibliographic entry is verified.

### feiginfuchs1982invariant

Opened [Math-Net](https://www.mathnet.ru/eng/faa1619) and [full Russian paper](https://www.mathnet.ru/php/getFT.phtml?jrnid=faa&option_lang=eng&paperid=1619&what=fullt). Read §§3–4 on Verma modules, contravariant forms, determinant and semi-infinite constructions. This is not cited as a printed bosonic oscillator formula; its relevant construction is fermionic. Bibliographic key coordinated with the autumn agent.

### zeldovichkobzarevokun1975walls

Opened [full JETP translation](https://www.jetp.ras.ru/cgi-bin/dn/e_040_01_0001.pdf). Read §§2–3, including the normalized tanh profile. The printed Russian source is *ZhETF*, 67, 3–11, July 1974; English *Soviet Physics JETP*, 40(1), 1–5, 1975. Received 31 January 1974. The printed header resolves inconsistent later web-page dating.

### nielsenolesen1973vortex

Opened [full primary PDF through the indexed source](https://infomall.org/sites/dsc/jpac/QCDRef/1970s/Vortex-line%20models%20for%20dual%20strings%20-%20Nielsen%2C%20Olesen%20-%201973.pdf). Initial direct retrieval returned 502; reopening its retrieved search reference yielded the full text. Read §2, (2.1)–(2.13), and §3, (3.1)–(3.6). Received 6 June 1973; publication 24 September 1973. Thin-core claims are restricted to the effective approximation.

### tong2009string

Opened [arXiv record](https://arxiv.org/abs/0908.0333) and [author’s full first chapter](https://davidtong.org/pdfs/teaching/string-theory/string1.pdf). Read §§1.2–1.2.2. First arXiv upload 3 August 2009. This is a modern primary lecture exposition of Nambu–Goto geometry, not a claim that the construction originated in 2009.

### kobayashi1974monopoles

Opened [publisher metadata](https://academic.oup.com/ptp/article/51/5/1636/1939935). Received 11 January 1974, published May 1974. **Full result not read.** The title identifies an earlier lead, but does not fix which smooth monopole or defect model the notebook’s sketch intended.

### grosswilczek1973ultraviolet

Opened [APS metadata](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.30.1343). Received 27 April 1973; published 25 June 1973. Cumulative key reused. Only the pre-talk gauge-theory context is used; no confinement theorem or fresh full-paper reading is claimed.

### witten1982supersymmetry

Opened [full primary paper](https://math.berkeley.edu/~gbeiner/texts/Witten_Morse_Theory.pdf). Read §3, especially (44)–(45), on supersymmetric localization and fixed-point contributions. Received 26 March 1982; published in *Journal of Differential Geometry*, 17(4), 661–692 (1982). The unnamed lectures themselves are not uniquely identified.

### neretin1982complementary

Opened [Math-Net](https://www.mathnet.ru/eng/rm3634) and [complete English paper](https://www.mathnet.ru/php/getFT.phtml?jrnid=rm&option_lang=eng&paperid=3634&what=fullteng). Read Theorem 1, the following proposition, Gaussian construction in §1, weighted pullbacks in §2 and endpoints in §4. Positive completion requires the stated parameter range. Received 11 May 1981; published 1982, before records 580 and 582.

### neretin1983boson

Opened [Math-Net](https://www.mathnet.ru/eng/dan9941) and [full Russian four-page paper](https://www.mathnet.ru/php/getFT.phtml?jrnid=dan&option_lang=eng&paperid=9941&what=fullt). Read Theorems 1–5 and the holomorphic sequence model. The [author’s bibliography](https://www.mat.univie.ac.at/~neretin/CV/CVpapers.html) confirms the English translation in *Soviet Mathematics Doklady*, 28, 411–414. Presented 17 January 1983; received 20 January 1983; published 1983. Administrative dates are not equated to public preprint dates.

### feigin1984semiinfinite

Opened [Math-Net](https://www.mathnet.ru/eng/rm2354) and [complete English note](https://www.mathnet.ru/php/getFT.phtml?jrnid=rm&option_lang=eng&paperid=2354&what=fullteng). Read Constructions 1–2, the theorem in Example 1 and the final physical-state paragraph, including the charge sum 26 and the zero-mode condition. Received 15 January 1983; published 1984; earlier public release not independently established.

### neretin1984padic

Opened [Math-Net](https://www.mathnet.ru/eng/faa1505) and [complete author-hosted scan](https://mat.univie.ac.at/~neretin/papers/p-line.pdf). Local rendering/OCR was used for the two-page text. Read the introduction’s explicit Gelfand attribution, Theorem 1 and the tree/Gaussian construction. Received 10 January 1984; published 1984. This identifies the analytic diffeomorphisms of the p-adic projective line as a precise answered version of the request.

### marsdenweinstein1974reduction

Opened [Caltech author repository record](https://authors.library.caltech.edu/records/8k5v6-4pa21) and its primary abstract. The [full PDF](https://www.cds.caltech.edu/~marsden/bib/1974/01-MaWe1974/MaWe1974.pdf) returned 502. **Original full theorem not reread.** Regular-value/free/proper hypotheses are editorial reconstruction, also checked against the later full Meinrenken–Sjamaar treatment. Received 15 September 1972; published February 1974.

### duistermaatheckman1982variation

Opened [publisher metadata](https://link.springer.com/article/10.1007/BF01399506). Publication is June 1982, *Inventiones Mathematicae*, 69, 259–268. Full original paper was not obtained. The mathematical result is read through the authors’ full Addendum and Atiyah–Bott §7; original-paper verification is **indirect**.

### duistermaatheckman1983addendum

Opened [complete Addendum](https://link.springer.com/content/pdf/10.1007%2FBF01389132.pdf). Read the introduction and Theorem 1.5, including the curvature-dependent Euler denominator for nonisolated fixed components. Published February 1983, *Inventiones Mathematicae*, 72, 153–158. Its 1982 Utrecht preprint is explicitly listed as reference 12 in the full Atiyah–Bott paper.

### atiyahbott1984moment

Opened [complete primary paper](https://www.math.stonybrook.edu/~mmovshev/MAT570Spring2008/BOOKS/atiyahbott_moment.pdf). Read §§3, 6–7, especially (3.8), (7.4), (7.5) and pp. 22–23. References 5 and 12 explicitly identify 1982 preprints of Berline–Vergne and the Duistermaat–Heckman Addendum. Received 20 December 1982; published 1984. The explicit preprint references, not the receipt date alone, support the earlier circulation.

### berlinevergne1983zeros

Opened [complete author-hosted paper](https://webusers.imj-prg.fr/~michele.vergne/publications/83zerosdunchampdevecteurs.pdf). Read the introduction and Theorem 1.6. *Duke Mathematical Journal*, 50(2), 539–549, June 1983; received 7 January 1983. The introduction cites the 1982 *Comptes Rendus* announcement. The 1982 announcement is not separately claimed as directly opened.

### atiyah1982convexity

Opened [complete primary paper](https://www.math.stonybrook.edu/~azinger/mat562/Atiyah82.pdf). Read the introduction’s Schur–Horn discussion and Theorems 1–2. Received 27 March 1981; *Bulletin of the London Mathematical Society*, 14(1), 1–15 (1982). Cumulative key and earlier occurrence links retained.

### kirillov1968characters

Opened [Math-Net](https://www.mathnet.ru/eng/faa2766) and [full Russian text](https://www.mathnet.ru/php/getFT.phtml?jrnid=faa&option_lang=eng&paperid=2766&what=fullt). Read §3, Theorem 2, (26)–(28), pp. 52–53: the shifted orbit, Jacobian factor and normalized orbital volume are explicit. Received 18 October 1967; published 1968. Cumulative key reused.

### semenovtianshansky1973kirillov

Opened [Math-Net](https://www.mathnet.ru/eng/znsl2637) and [complete Russian paper](https://www.mathnet.ru/php/getFT.phtml?jrnid=znsl&option_lang=eng&paperid=2637&what=fullt). Read introduction pp. 53–54, Lemma 2.7, Proposition 2.8 and the §4 theorem. *Zapiski Nauchnykh Seminarov LOMI*, 37, 53–65 (1973). The exact stationary-phase assertion concerns the compact semisimple setting; it is not enlarged to arbitrary noncompact regularizations.

### vergne1979rossmann

Opened [complete author-hosted paper](https://www.cmls.polytechnique.fr/perso/vergne/publications2/Remplacer/79onrossmanncharacter.pdf). Read §§2–4 and the compact-Cartan oscillator argument. *Inventiones Mathematicae*, 54, 11–14 (1979), DOI 10.1007/BF01391173; received 2 March and revised 5 July 1979. A later repository timestamp is not substituted for the publication date.

### meinrenkensjamaar1999singular

Opened [complete primary preprint](https://arxiv.org/pdf/dg-ga/9707023). Read the introduction, §2.1, Definition 2.3, Theorem 2.9 and Corollary 2.11, including compactness/properness and the shifted quotient line bundle. First arXiv release 30 July 1997; *Topology*, 38(4), 699–762 (1999). Cumulative key reused. The result concerns reduced-space indices, not equality of raw volume with finite multiplicity.

### gelfandtsetlin1950unimodular

Opened [complete four-page primary scan](https://www.math.ucdavis.edu/~deloera/MISC/LA-BIBLIO/trunk/Gelfand/Gelfand7.pdf), including a rendered image of §3, formula (3), for the interlacing rule. Original *Doklady*, 71, 825–828 (1950); submitted 16 February 1950. Cumulative key reused; the scanned translation’s pagination differs from the Russian original.

### arnold1983mathieu

Opened [Math-Net](https://www.mathnet.ru/eng/rm2950) and [complete English primary paper](https://www.mathnet.ru/php/getFT.phtml?jrnid=rm&option_lang=eng&paperid=2950&what=fullteng). Read §§1–5, Theorems 1–7, the Catalan/Griffiths–Harris footnote on p. 222, Supplement dated 30 March 1983 on p. 232, and references on p. 233. Received 1 February 1983; published later in 1983. The Supplement controls the A/E distinction. Griffiths–Harris’s book was not independently opened; its precise even-genus pencil example is reported indirectly through this footnote.

### bloch1958perturbations

Opened [publisher preview of Bloch’s collected works](https://api.pageplace.de/preview/DT0400.9780444601148_A23669232/preview-9780444601148_A23669232.pdf), whose contents p. xvii identifies the original article, *Nuclear Physics*, 6, 329–347 (1958). The [original article URL](https://www.sciencedirect.com/science/article/pii/0029558258901160) returned 403; its publisher abstract was retrieved in search. **Metadata checked; theorem comparison is indirect through Arnold’s explicit Supplement.**

### levykeller1963instability

Opened [publisher abstract/metadata](https://onlinelibrary.wiley.com/doi/abs/10.1002/cpa.3160160406). It confirms *Communications on Pure and Applied Mathematics*, 16(4), 469–476, November 1963. Full-PDF request returned the metadata page. **Original proof not read; exact antecedent comparison is Arnold’s explicit statement concerning his Theorem 3.**

### hochstadt1964instability

Opened [publisher abstract/metadata](https://onlinelibrary.wiley.com/doi/abs/10.1002/cpa.3160170209). It confirms *Communications on Pure and Applied Mathematics*, 17(2), 251–255, May 1964. Full-PDF request returned metadata. **Original proof not read; the relation to Arnold’s Theorem 7 is indirect through the dated Supplement.**

### grebertkappelerposchel2004gaps

Opened [full author-hosted primary paper](https://www.math.sciences.univ-nantes.fr/~grebert/GKP-IMRN.pdf). Read §1, Theorems 1.1–1.2, and §2 spectral preliminaries. Received 15 September 2003; inspected version April 2004; published *International Mathematics Research Notices*, 2004(50), 2703–2717. Cumulative key reused. Regularity and finite-gap density are not a unique answer to an unspecified one-gap perturbation request.

### poschel2004weighted

Opened [arXiv record](https://arxiv.org/abs/0908.0491) and [full preprint](https://arxiv.org/pdf/0908.0491). Read §1, Theorems 1 and 3, and the distinction between smooth/rapid and analytic/exponential spectral decay. Title page gives version 4.3, August 2004, *Stuttgarter Mathematische Berichte* 2004/12; arXiv upload 4 August 2009 is not first circulation. The preprint edition is cited rather than assigning unverified later journal metadata.

### krichever1983hessians

Opened [Math-Net](https://www.mathnet.ru/eng/dan46140) and [complete Russian paper](https://www.mathnet.ru/php/getFT.phtml?jrnid=dan&option_lang=eng&paperid=46140&what=fullt), reopening both for the final forward link. Read Theorems 1–3, Lemma 3, fixed-period relation (5), Hessian formula (6), and gap-opening/first-order perturbation formulas (13)–(19). Presented 19 October 1982; received 23 November 1982; *Doklady*, 270(6), 1312–1317 (1983). No public circulation date is inferred from presentation or receipt. The broad question at 585.6 receives only a thematic link to next meeting 586.3–6. The final long-time assertion is outside the claim made by this shard.

## Independent checks and their scope

`checks.py` makes thirteen checks and records every result. Symbolic Liouville curvature and Schwarzian identities were verified both in the half-plane coordinate and with three rational developing maps. The Virasoro vacuum commutator was checked for modes 1–8 as a polynomial in the parameters and against an independent finite-sum expression. The wall profile was checked by its differential equation and by its first integral, with additional parameter substitutions; gauge covariance and the circular-string equation and conserved energy were checked separately. Hilbert-transform projector algebra and logarithmic Fourier coefficients were tested independently of the handwritten formula. Two quadrature grids check the latter’s sign and scaling.

The SU(3) calculation uses an explicit conjugate pair with equal Casimirs and different diagonals, followed by direct hexagon angle/side checks. Catalan numbers from convolution and factorial formula agree through index 12. Bounded path enumerations check the ceiling for indices through 36 and the remote-loop criterion on 4,232 small closed walks; they are explicitly **finite checks, not proofs of universal spectral estimates**. The exact P001086 bracket example is checked twice under the involution, with attached closing-parenthesis multiplicities preserved. General results are attributed to the read primary papers; no new theorem is claimed from these examples.

## Suggested format and website improvements

- Separate **first documented circulation**, **journal receipt**, **publication**, and **translation** dates. A single year field cannot represent Beilinson, BPZ, Neretin or Arnold correctly.
- Store **reference-level and claim-level verification** separately. One item can have a directly read 1983 proof and a historically important 1958 antecedent known only through that proof’s explicit attribution. “Verified bibliography” alone does not certify all theorem-level comparisons.
- Add **correction IDs and occurrence links**. `correction_map.json` demonstrates why a single correction may repair several occurrences, and one false item may require several distinct formula corrections.
- Preserve **catalogue page range** and **actual content span** separately. A reader opening heading 579 should see no neighboring mathematics; a reader opening Arnold should land on P001081.
- Allow **relation types** such as exact recurrence, thematic continuation, source reconstruction and historical antecedent. The exact `GP-1981-41` recurrence and the thematic 585.6 → 586.3–6 link must not look identical.
- Present notebook wording, precise reconstruction and later theorem as separate visible blocks. For Polyakov, a reader should first reach the normalization ledger and accessory-parameter problem; for Kirillov, the distinction between a level set, reduced space and index; for Arnold, the gap upper bound and dated priority Supplement. The scan link and exact source locator should remain one step away.

These changes are recommendations for the common format, not unauthorized modifications of the supplied builder.
