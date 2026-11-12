# Research audit: records 2–14

Audit date: **12 November 2026**. All present-status fields are dated **November 2026**.

## Scope, counts and reproduction

This contribution covers catalogue records 2–14, with mathematical content on P000001–P000036. The first-run occurrence IDs are retained, and **1964-6.9** is added for the previously unindexed support-of-Radon-measures sentence. The supplied previous_index.md is a same-year first-run index, not evidence of earlier-year recurrence or authority for classification.

The files contain **13 talks, 84 items, four provisional problems, 36 references and 65 correction rows**. Class counts: A10, B6, C1, D0, E59, F8. No item here is labelled “developed in this chapter”; the elementary checks are annotations, not claimed research advances. The single C item is the conditional uniform-SAW interpretation, 1964-3.11. Difficult identification failures are F, not alleged undeveloped problems.

The provisional problem IDs are GP-1964-01 (SAW), GP-1964-A01 (invariant solutions), GP-1964-A02 (invariant fundamental solutions), GP-1964-A03 (SL2(Q) characters). Root will assign final IDs and add the independently researched current SAW bound update.

Reproduction:

    python work/parts/autumn/make_autumn.py > work/parts/autumn/generation_output.txt
    python work/parts/autumn/make_corrections.py > work/parts/autumn/corrections_output.txt
    python work/parts/autumn/audit_autumn.py > work/parts/autumn/audit_output.txt

The builder checkpoints every record and then applies final source corrections. The audit checks schema fields, enums, consecutive IDs, citation/reference closure, date fields, math delimiters and control characters. It is not a mathematical proof checker. Root owns the merged build, LaTeX/BibTeX compilation, final report and deliverable storage.

The saved helpers read_sources.py, normalize_builder.py, fix_builder_quotes.py and fetch_primary.py are retained with outputs. An early source-reader pattern was corrected so that removing the layout command “par” did not remove the prefix of “partial”; en_01_10.txt was regenerated. The bibliography and this log were authored directly.

## Bilingual and scan record

English and Russian texts for P1–36 were read through the supplied individual page files and stripped-diagram excerpts. Russian P1–18 was rechecked in three final bounded batches, saved as ru_01_06_review.txt, ru_07_12_review.txt and ru_13_18_review.txt. The reader removes diagram code and layout wrappers; it does not emend mathematics.

**All 36 scans were visually viewed on 12 November 2026.** This log records the mathematical purpose, not a claim that every unclear stroke was deciphered.

| Pages | Visible date/context | Consequential checks |
|---|---|---|
| P1–3 | 21 September, Gelfand; Dobrushin begins on P3 | Symmetric versus Rees algebra, ideal invertibility, Proj exclusion abbreviation, blowup charts and crossing center; negative bond energy. |
| P4–6 | Dobrushin | Concavity convention, pressure plateau, deviation rate, boundary exponent, inconsistent minus-log asymptotic. |
| P7 | Dobrushin; 24 September Segal notice | Large-contour power and small-contour indices conflict with P10; nonlinear quotient-algebra proposal. |
| P8 | Dobrushin | U changes to positive bond count; zero derivative is written for coexistence. |
| P9–10 | Dobrushin | Q factor/power ambiguity, S3 constant, event braces, contour conditions, subcube denominator. |
| P11 | Walk question; 28 September Segal | Probability1/3, “return” ambiguity, e-count conjecture; skew-adjoint evolution. |
| P12–13 | Segal; 5 October continuation; Schwartz begins | Missing norm square, wrong adjoint word, missing v in variation equation, uncertain CCR, renormalization headings; positive measures explicitly stipulated. |
| P14–15 | Schwartz | Pushforward source/target typo; non-Borel/nonmeasurable distinction; compact regularity quantifier; support sentence. |
| P16–17 | Schwartz; 12 October Gindikin/Weil | Radon/operator spaces, nuclear-space analogy, path measurability, common-modulus error, SL2 shorthand and nondiscrete aside. |
| P18–20 | Schwartz | Hilbert sum norm, contractive order, zero-space edge case, “strictly convex” terminology and antidual. |
| P21–22 | Schwartz | Kernel completion and weak boundedness; missing inverse in H1 kernel. |
| P23–24 | Arnold/Kushnirenko; 19 October entries | Hypersurface entropy estimate and sharper coefficient; Kostant coordinates; reduced free energy. |
| P25–26 | Povzner, Kirillov notice, Schwartz | Wigner marginal question without explicit bilinear formula; Thoma volume84; smooth/distribution vectors. |
| P27–28 | Schwartz | Lorentz component unspecified, extension across origin, affine cocycle, invariant fundamental solution and torus slope. |
| P29–30 | 2 November Kirillov | Normalized tracial characters, additive/multiplicative character confusion, eigenvector-index inconsistency. |
| P31–32 | Kirillov | Pullback action convention, finite affine table, a≠0 versus a≠1, unresolved normal-subgroup lemma, S-infinity. |
| P33–34 | Kirillov | Type-I clause visibly “isom. G”, rational matrix problem, trace/class limitations, local-field formulas and unresolved real brace/name. |
| P35 | Kirillov ends; Vishik begins; Linnik announcement | Direct-sum adele error; content boundary; separate announcement for the16th. |
| P36 | Pyatetskii-Shapiro report | Ilya Iosifovich spelled out, sphere in R3, fixed splitting prime, unexplained48. |

Catalogue spans overlap. Talk metadata preserve them, while item pages locate actual content. Record7 continues P18–22 beyond its catalogue span; record9 is P24–25; record11 is a paragraph on P25; record12 is P25–28; record13 is P29–top P35; record14 is P36. The separate announcement for16November does not automatically redatetime the catalogue report.

## Opened reference register

Every bibliography entry has a URL/DOI, a verified note and an access-scope annote. **Verified means opened**, not that every proof was checked or every computational certificate rerun. Exact modern statements, manuscript readings, and editorial reconstructions are distinguished in each item.

### Geometry and statistical mechanics

1. **stacks2026blowups**: [tag01OF](https://stacks.math.columbia.edu/tag/01OF) and [tag0806](https://stacks.math.columbia.edu/tag/0806) opened. Read Definition31.33.1, Lemma31.33.2 and universal property Lemma31.33.5. An initially considered tag01N7 was irrelevant and is not cited.
2. **grothendieck1961ega2**: [Numdam record](https://numdam.org/item/PMIHES_1961__8__5_0/) opened, DOI10.1007/BF02699291, volume8,5–222,1961. Section8.1 is a historical blowup pointer. The27.4MB scan exceeded retrieval limits and was not read; exact construction was checked in Stacks.
3. **hironaka1964resolution**: [MathNet primary translation record](https://www.mathnet.ru/eng/mat382) opened, giving Annals79(1),109–203,1964 and the1965 Russian translation. Original proof not read. Characteristic zero and strict/total transforms are modern qualifications.
4. **dobrushin1965phase**: [record](https://www.mathnet.ru/eng/tvp518) and [Russian full text](https://www.mathnet.ru/php/getFT.phtml?jrnid=tvp&option_lang=eng&paperid=518&what=fullt) opened. Read Section1, Theorems1–2 and contour lemmas. Russian10(2),209–230; English10(2),193–213, DOI10.1137/1110026. Equations(1.6)–(1.7), printedpp210–211, contain Q. OCR was insufficient for its exact factors; the item gives a fully quantified qualitative theorem and marks the quantitative match partial.
5. **dobrushin1965announcement**: [record](https://www.mathnet.ru/eng/dan30737) and [three-page original](https://www.mathnet.ru/php/getFT.phtml?jrnid=dan&option_lang=eng&paperid=30737&what=fullt) opened. Read theorem and Lemmas1–7, especiallyp1047. Received and presented by Kolmogorov15September1964, published1965 in160(5),1046–1048. Submission/presentation is not established public circulation.
6. **dobrushin1966addendum**: [record](https://www.mathnet.ru/eng/tvp656) and [original letter](https://www.mathnet.ru/php/getFT.phtml?jrnid=tvp&option_lang=eng&paperid=656&what=fullt) opened and both paragraphs read. Russian11(3),548–549; English11(3),486–487, DOI10.1137/1111054. Grossmann, Ginibre and Ruelle found the Lemma4 error. Generalized cycles repair it while preserving the original Q; a simple deletion would weaken Q. The second paragraph corrects inequality(8.8), following Sherman.
7. **ponitz2000bounds**: [journal page](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v7i1r21), DOI10.37236/1499, opened. Published13April2000. Abstract states square-lattice upper bound2.679192495<e. Full computational proof/certificate not rerun. This suffices to refute e without claiming the current best bound.
8. **duminil2013subballistic**: [publisher](https://link.springer.com/article/10.1007/s00220-013-1811-1), [arXiv](https://arxiv.org/abs/1205.0401) and [full preprint](https://arxiv.org/pdf/1205.0401) opened. Theorem1.1 and Corollary1.2 read for uniform fixed-length SAW on Z^d,d≥2: linear maximum displacement is exponentially suppressed and endpoint mean square is o(n²). The annotation says sufficiently large n. Posted2May2012, published13October2013 in CMP324(2),401–423, not Annals.

Root independently supplies Couronné2025 and Tomar2026 current upper-bound references and qualification of the latter's unreviewed certificate. Root also audits the2026 honeycomb-diameter preprint; it does not by itself settle square-lattice endpoint moments.

### Segal, Schwartz and Weil

9. **segal1963global**: [record](https://www.numdam.org/item/BSMF_1963__91__129_0/) and [original](https://www.numdam.org/article/BSMF_1963__91__129_0.pdf) opened. BSMF91,129–135, DOI10.24033/bsmf.1593. Readpp130–132 for skew-adjoint evolution, local Lipschitz hypotheses and global weak existence. Not a blanket quantum-field uniqueness theorem.
10. **segal1965variete**: [record](https://www.numdam.org/item/SJL_1964-1965___3_1_0/) and [full text](https://www.numdam.org/item/SJL_1964-1965___3_1_0.pdf) opened. Academic-year1964–1965 volume,80printed pages. PartsII–V read, especially the theorem onp45 and asymptotic solutionspp51–60. No exact individual lecture date inferred.
11. **segal1965erratum**: [full erratum](https://www.numdam.org/item/SJL_1964-1965___3_0_0.pdf) opened and read. It corrects inconsistent d'Alembertian signs onp45 and introduces a second renormalization constant besides mass. Attached to4.7 and5.1; no one-constant quantum existence theorem inferred.
12. **segal1968dispersion**: [metadata](https://www.numdam.org/item/ASENS_1968_4_1_4_459_0/) opened, ASENS fourth series1(4),459–497, DOI10.24033/asens.1170. Later publication pointer only; proof not read.
13. **courrege1963mesures**: [record](https://www.numdam.org/item/SC_1963__2__A4_0/) and [original](https://www.numdam.org/item/SC_1963__2__A4_0.pdf) opened. Lecture6June1963, Choquet2,exposé5,1–28. Theorem1.1 and Section4 read, including bounded continuous functions in compactification. It does not provide a numbered exact match for every broad record6 assertion.
14. **schwartz1973radon**: [book metadata](https://books.google.com/books/about/Radon_Measures_on_Arbitrary_Topological.html?id=19zuAAAAMAAJ) opened: TIFRStudies6, Oxford/TIFR1973, xii+393, ISBN0195605160. Full book not read. [Primary catalogue](https://www.persee.fr/authority/416864) separately lists Lisbon1964, Paris1964–1965 and TataAugust1965 lectures; exact pre5October publication dates for individual theorems remain unestablished.
15. **schwartz1962hilbert**: [record](https://www.numdam.org/item/SB_1961-1962__7__255_0/) and [original](https://www.numdam.org/item/SB_1961-1962__7__255_0.pdf) opened. May1962, Bourbaki238,255–272. Sections1–3 and Theorem1,p257 read. Expanded1964 paper DOI10.1007/BF02786620 located but not retrieved.
16. **weil1964cohomology**: [original](https://people.brandeis.edu/~ruberman/math221bs16/weil_Remarks%20on%20the%20cohomology%20of%20groups.pdf) opened. Annals80(1),149–157, July1964, DOI10.2307/1970495. Section3 H1-vanishing criterion and Sections4–6 compact surface formula read. Earlier1960/1962 references were identified but not separately read.

### Entropy and invariant operators

17. **kostant1959multiplicity**: [MathNet record](https://www.mathnet.ru/eng/mat210) opened, original TransAMS93(1),53–73,1959, DOI10.1090/S0002-9947-1959-0109192-6. Metadata identify notebook coordinates; original proof not read and notebook contains no explicit multiplicity formula.
18. **wigner1932quantum**: [APS abstract/metadata](https://journals.aps.org/pr/abstract/10.1103/PhysRev.40.749) opened. Received14March, published1June1932,40,749–759. Full original not read. Modern bilinear formula is editorial supplementation; sourceP25 only poses the marginal problem and cites Wigner.
19. **kushnirenko1965entropy**: [record](https://www.mathnet.ru/eng/dan30812) and [two-page original](https://www.mathnet.ru/php/getFT.phtml?jrnid=dan&option_lang=eng&paperid=30812&what=fullt) opened. Doklady161(1),37–38. Theorem1 is n log2(lambda); endomorphisms use full inverse-image hypersurface area. Received1October1964, presented7October1964, published1965. Arnold thanked. The n−1 value is mentioned for examples, not as the general printed theorem.
20. **ruelle1978inequality**: [author original](https://www.ihes.fr/~/ruelle/PUBLICATIONS/%5B51%5D.pdf) opened, Theorem2,p84 read. BolSocBrasilMat9(1),83–87, DOI10.1007/BF02584795. Application to the sharper bound is explicitly editorial. Initially tried publication-number57 was unrelated and is not cited.
21. **garding1947continuous**: [PMC primary record](https://pmc.ncbi.nlm.nih.gov/articles/PMC1079067/) opened, PNAS33(11),331–332, DOI10.1073/pnas.33.11.331. PDF route remained a preparation page. Smoothing argument is editorial, not a claim to have read the proof.
22. **methee1954lorentz**: [publisher](https://link.springer.com/article/10.1007/BF02566932) opened, CommentMathHelv28,225–269,1954; received24October1953. [Original scan route](https://www.e-periodica.ch/cntmng?pid=com-001%3A1954%3A28%3A%3A17) hit a verification wall; follow-up link timed out. Exact invariant-surjectivity theorem not read or asserted.
23. **cerezo1969fundamental**: [record](https://www.numdam.org/item/ASENS_1969_4_2_4_561_0/) and [original](https://www.numdam.org/article/ASENS_1969_4_2_4_561_0.pdf) opened. Introduction and Theorem1,Section4 read. ASENS fourth series2(4),561–581, DOI10.24033/asens.1184. Direct later compact-group criterion.
24. **greenfield1972global**: [author-uploaded original article](https://www.researchgate.net/publication/240472738_Global_Hypoellipticity_and_Liouville_Numbers) opened and all three pages read, not a secondary summary. ProcAMS31(1),112–114, DOI10.2307/2038523. Theoremp112, propositionp113 and Fredholm corollary. Received5November1970, revised10March1971. A guessed AMS DOI failed and is not used.
25. **lerner2000solvability**: [full primary research article](https://www.numdam.org/item/10.5802/aif.1761.pdf) opened; introduction read for Lewy1957 and later distributional nonsolvability distinction. AIF50(2),443–460, DOI10.5802/aif.1761. Lewy original not separately opened.

### Characters, adeles and sphere points

26. **thoma1964classes**: [publisher](https://link.springer.com/article/10.1007/BF01109907) and [archive metadata](https://geodesic.mathdoc.fr/item/MZ_1964__84_170276/) opened. MathZ84,389–402,1964; received27January. Original proof not read. December publisher issue label conflicts with straightforward interpretation of the notebook's19October citation; no public-circulation date invented.
27. **thoma1964symmetric**: [publisher](https://link.springer.com/article/10.1007/BF01114877) opened, MathZ85,40–61,1964; received27January. February issue label cites the volume84 paper labelled December elsewhere; month ordering treated cautiously. Proof not read.
28. **thoma1964unitary**: [publisher](https://link.springer.com/article/10.1007/BF01361180) opened, MathAnn153,111–138,1964; received18January1963, issueApril1964. TypeI/virtually-abelian statement also checked in Peterson–Thom introduction. Original proof not read.
29. **gohm2010characters**: [full primary preprint](https://arxiv.org/pdf/1005.5726) opened; Theorem0.1 and Sections6–8 read. Posted31May2010. Supplies alpha/beta simplex and exact Thoma formula.
30. **petersonthom2016characters**: [author full text](https://math.vanderbilt.edu/peters10/petersonthom2013.pdf), [arXiv](https://arxiv.org/abs/1303.4007) and [publisher](https://www.degruyterbrill.com/document/doi/10.1515/crelle-2014-0009/html) opened. Definition1.1 and Theorem2.4,p11 read. Posted16March2013, revised4February2014, online11March2014, print1July2016,716,207–228. For SL2(Q), trivial plus two center-supported characters. Not an unqualified GL2 classification.
31. **gelfandgraev1963representations**: [record](https://www.mathnet.ru/eng/rm6374) and [Russian original](https://www.mathnet.ru/php/getFT.phtml?jrnid=rm&option_lang=eng&paperid=6374&what=fullt) opened. RMS18(4),29–100, DOI10.1070/RM1963v018n04ABEH001140. Section5.1,eq(5),printedp83/PDF54 read; printedp98 absolute-value convention. Received8April1963. Gelfand–Naimark1947 attribution not independently opened.
32. **prasad2007representations**: [metadata](https://arxiv.org/abs/0712.4051) and [56-page notes](https://arxiv.org/pdf/0712.4051) opened. Posted25December2007 after July lectures. Sections1.6,2.4–2.5,3.6, Exercise3.44 and Lemma3.45 read. Generic parameters exclude exceptional quadratics; regular-semisimple rows are not a full table. Intro dates Jordan/Schur classifications1907; notebook Frobenius1895 remains unverified precise attribution.
33. **gelfand1964adeles**: [record](https://www.mathnet.ru/eng/dan29604) and [original](https://www.mathnet.ru/php/getFT.phtml?jrnid=dan&option_lang=eng&paperid=29604&what=fullt) opened. Section1,p487 read; all places and restricted product. Received8January1964,156(3),487–490.
34. **linnik1957sphere**: [record](https://www.mathnet.ru/eng/sm5081) and [original](https://www.mathnet.ru/php/getFT.phtml?jrnid=sm&option_lang=eng&paperid=5081&what=fullt) opened.43(85)(2),257–276, received11July1956. Theorem1,Section2,p258: m≡1,2,3,5,6mod8; fixed q>3; Legendre(-m/q)=1. Equations(2.1)–(2.2) distinguish all/primitive points. Section3,pp258–260, Theorems3–4 supply reduced two-direction dynamics.
35. **duke1988hyperbolic**: [author original](https://www.math.ucla.edu/~wdduke/preprints/hyperbolic.pdf) opened; pp73–74 sphere application read. InventMath92,73–90, DOI10.1007/BF01393993. Data safely state at least the squarefree removal of the fixed-prime restriction, not equidistribution along powers-of-four countersequences.
36. **ellenberg2010linnik**: [arXiv](https://arxiv.org/abs/1001.0897) and [author manuscript](https://www.math.ias.edu/~akshay/research/gg.pdf) opened. Posted6January2010. Sections1–2,8–9 read. Later publication leads were not verified sufficiently, so the2010 preprint is cited and the provisional2012 key removed.

## Search trails and failures

Research was batched by subject and followed to primary sources. Normalized topic strings, **not a verbatim archive of every original query**, include: Dobrushin1965 Ising Q theorem; Dobrushin1966 letter editor; Segal variété1964–1965 erratum; Schwartz Hilbert antinoyaux1962; Schwartz Radon1964 Lisbon; Weil cohomology1964; Kushnirenko entropy1965; Méthée Lorentz distributions; Cerezo Rouvière elementary solution compact group; Greenfield Wallach Liouville numbers; Thoma Klassenfunktionen1964; Peterson Thom SL2 characters; Linnik sphere1957 fixed prime; self-avoiding walk subballistic upper bounds.

The URLs and locators above are the reproducible trail. Metadata is used for dates; mathematical claims come from primary texts or explicitly labelled editorial derivations.

Material failures and their consequences:

- EGAII full PDF exceeded the27.4MB retrieval limit. Metadata-only historical pointer retained.
- MathNet PDF text opened, but web screenshot output produced image markers without usable images. The saved fetch_primary.py made ordinary downloads from the exact Dobrushin and Linnik URLs; both returned HTTP403, captured in fetch_primary_output.txt. No access bypass or fabricated Q formula followed.
- Méthée's e-periodica wall and timeout prevented the full proof. The modern item gives a framework, not unverified surjectivity.
- Candidate TIFR PDF routes timed out or failed. The1973 book stays metadata-only, with no invented theorem locators.
- EuDML Thoma access failed. Publisher/geodesic metadata worked; original normal-subgroup lemma remains unidentified.
- Schwartz1964 extended-paper DOI did not supply the text; the1962 theorem was accessible.
- Gårding download stayed in preparation; Wigner full text was inaccessible beyond publisher abstract.
- Guessed Greenfield AMS DOI failed; author-uploaded primary article supplied the result.
- Peterson–Thom DOI redirect initially failed, but exact publisher document and author PDF worked.
- Final Numdam HTML route for Lerner failed, while the exact PDF route had already opened.

## Chronology, mathematical scope and unresolved points

**Dobrushin.** The short announcement was received/presented15September1964, the long paper received30September, and both published1965. Receipt is not a public-distribution date. ClassA records the speaker's close publication match. The1966 repair is part of the fate. Exact Q typesetting is a remaining bounded source check; no numerical threshold is asserted.

**Segal.** The1963 classical theorem is prior exposition. The1964–1965 seminar text is the close speaker publication for solution geometry and canonical-field constructions. The notebook's renormalization headings lack sufficient dimension, cutoff, domain and scheme data for an unconditional quantum existence/uniqueness theorem. The erratum changes signs and adds a second constant. Those unidentified stronger claims remain F.

**Radon.** Courrège1963 and Schwartz1962 supply direct prior foundations. Several broad record6 Radon-space assertions are reconstructed through later thematic sources; exact theorem-level pre-talk priority is not independently established. ClassE is expository identification, not a count of uniformly verified earliest-publication claims. The new6.9 uses finite **positive** Hausdorff Borel measures inner regular on all Borel sets. Complement of support is a union of null open sets; compact subsets have finite null subcovers; inner regularity makes that complement null. No signed-measure or weaker-definition extrapolation is made.

**Entropy.** The n−1 bound is a later Ruelle/Lyapunov implication, not Kushnirenko's printed Theorem1. Compact Riemannian manifold, normalized preserved volume and n≥2 are explicit; n=1 has entropy0 separately. Hypersurface expansion bounds the inverse derivative, negative exponents have bounded magnitude, determinant one balances their sum, and Ruelle gives the estimate. This is editorial proof structure, not an asserted historical dependence.

**Invariant equations.** Independent cross-review corrected “proper Lorentz group” to proper orthochronous/identity component when distinguishing time orientations. The source does not choose a component, so this is explicitly editorial. Extension requires an invariant punctured datum and action fixing the origin, plus a common finite invariant jet space and continuity of the cocycle. The unread Méthée theorem is not overstated. The torus discussion separates the unavoidable constant-mode obstruction from reduced small divisors.

**Characters.** Extreme normalized tracial characters correspond to finite factors, not every irreducible unitary representation. The finite/rational affine calculations are directly checked. Restriction to a normal subgroup need not preserve extremality: S3's two-dimensional normalized character restricts to the mean of the two nontrivial A3 characters. The precise intended lemma is unresolved. Thoma publisher issue-month labels conflict with a simple chronological interpretation; notebook evidence establishes knowledge by19October, not an earliest public date. The rational-matrix problem is solved only under the explicit SL2(Q) interpretation.

**Linnik.** The1957 original was read and is not replaced by a modern squarefree simplification. Fixed splitting prime, admissible residues, normalized area and all/primitive distinction are restored. The manuscript48 remains unidentified; the order48 of integral orthogonal symmetries does not prove this is what the note means.

**SAW.** Probability1/3 plus “no return” does not specify uniform fixed-length SAW. Nonbacktracking, kinetic and uniform laws differ. No3/4 exponent is written in the notes. The rigorous sub-ballistic theorem is scoped to uniform SAW; mean square and mean distance are distinguished. The e conjecture is refuted conditionally under the SAW reading, but the exact constant remains separate.

Bounded useful annotations include the crossing blowup, the Radon-support argument, compact-layer modulus counterexample, Sobolev inverse, finite affine normalization and reduced torus criterion. These are standard clarifications. They do not claim to solve the planar exponent or constitute a new research development. Root independently handles a possible nonbacktracking calculation and the main development elsewhere.

## Independent review and final state

Winter's independent cross-review of the original83 entries is saved at work/evidence/autumn_cross_review.md. It found three concrete changes: Lorentz group component in12.3; invariant datum/action fixing origin in12.4; T>0 and finite positive Z_N in9.2. All three are applied to the builder and final JSON. Root independently checked and accepted new6.9. The later Wigner source-fidelity correction makes explicit that the notebook does not display the supplied Fourier formula.

Remaining scholarly limitations are exact Dobrushin Q, full Méthée theorem match, original Thoma normal-subgroup lemma, some manuscript abbreviations, and exact early chronology for broad Radon-space assertions. They are visible in item assessment fields. The contribution is ready for merge and final root build.
