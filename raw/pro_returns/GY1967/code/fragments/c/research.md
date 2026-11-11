# Research audit: MCCME records 155–166

Audit date: **9 November 2026**. Owner: `/root/records_155_166`. The parent integrates, compiles, packages and delivers the chapter. `write_c.py` regenerates the JSON and correction files, saving checkpoints during authoring.

## Coverage and provenance

Read the chapter-format specification, both transcriptions, the catalogue, previous occurrence/problem index and cumulative bibliography. The English transcription was read throughout the assigned material. **Every Russian handwritten scan P000253–P000272 was inspected.** The Russian manuscript controls formulas and attribution. Errors faithfully copied in both transcriptions are labeled mathematical emendations, not transcription errors.

Catalogue page ranges are preserved in `talks.json`; exact headings determine item ownership:

| Record | Actual content | Treatment |
|---|---|---|
| 155 | P253 | Kazhdan’s Ihara introduction; P252 belongs to preceding material. |
| 156 | P254–255 | Palamodov and Gelfand on jets and Spencer sequences. |
| 157 | P256 | Kirillov’s kernel-trace statement. |
| 158 | P256 schedule notices | Catalogue record retained as a plan; no separately attributable Gelfand mathematics fabricated. |
| 159 | P256–257 | Weinstein variational methods; separate Rolewicz notice. |
| 160 | P257–260 | Kirillov’s character formulas and examples. |
| 161 | P261–upper P263 | Gelfand’s graded reading programme. Bibliographic entries are not expanded into unstated theorems. |
| 162 | Lower P263–266 | Gromov’s differential relations and metric examples. |
| 164 | P267 and opening P268 | Oleinik and Gelfand’s integrability intervention; **precedes163 in source order**. |
| 163 | Heading P268–271 | Kazhdan on Dwork rationality. |
| 165 | P272 | Year heading1969; no items. |
| 166 | Opening P272 only | Margulis; Gelfand’s 3-adic arithmetic on the same page is167, and P273 begins168. |

The catalogue date27October1968 is retained despite falling on a Sunday. Record159’s scan gives only “Prof. Weinstein (USA)”; the catalogue says Alan, while the exact methodological paper is by Alexander. This is flagged rather than silently renamed.

Final counts: **12 records, 76 items, 19 corrections, 22 references, one problem**. Classes: A8, B0, C1, D0, E54, F13. New **GP-1968-20** occurs at **1968-166.2**. It is explicitly a qualified modern reconstruction with full spectral main terms and epsilon loss, not the notebook’s exact conjecture. No D item is manufactured from incomplete references or broad programmes.

## Opened literature and result-reading levels

Web IDs record the research session; URLs are durable. BibTeX “verified” means a page/file was opened; item-level verification separately distinguishes read results from metadata.

1. **ihara1968monodromy** — [full paper](https://www.jstage.jst.go.jp/article/jmath1948/20/1-2/20_1-2_107/_pdf), `turn13view3`. JMSJ20(1–2),107–121; DOI10.2969/jmsj/02010107. Introduction and §0 read. Received31August1967, published1968. Exact bibliographical fingerprint. The three monodromy conjectures are not written in the notebook and are not imported.

2. **sweeney1968neumann** — [full paper](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6055-11511_2006_Article_BF02394611.pdf), `turn17view1`, exact recheck `turn113view0`/`turn113view1`. ActaMath120,223–277; DOI10.1007/BF02394611. ChapterI §§1–8 read. **Proposition6.2,p238 proves the exact first Spencer sequence with descending jet orders and negative orders zero.** The symbol-quotient construction belongs to the second sequence. Final authoring refinement corrects an earlier draft qualification. Archive1966.9 is receipt, not publication. General PDE exactness has extra hypotheses in §§7–8.

3. **kirillov1968characters** — [metadata](https://www.mathnet.ru/eng/faa2766), `turn13view0`; [full Russian text](https://www.mathnet.ru/php/getFT.phtml?jrnid=faa&option_lang=eng&paperid=2766&what=fullt), `turn16view0`. FAA2(2),133–146; Russian40–55; DOI10.1007/BF01075947. Received18October1967; published before these1968 talks. **Lemma8,pp49–50 exactly matches157.** Introduction and §§1–3 read. Section3,Theorem2 is the compact semisimple shifted formula; §2 has restricted exponential-unimodular calculations. No universal all-group theorem is inferred. Shared key/scope coordinated with record131’s author.

4. **kirillov1962unitary** — [metadata](https://www.mathnet.ru/eng/rm6513), `turn64view3`; [full English text](https://www.mathnet.ru/php/getFT.phtml?jrnid=rm&option_lang=eng&paperid=6513&what=fullteng), `turn67view2`. RMS17(4),53–104; DOI10.1070/RM1962v017n04ABEH004118. Received17October1961. Introduction, Theorems5.1–5.2 and7.4 checked. Cumulative entry/key reused. Simply connected nilpotent scope is preserved.

5. **weinstein1963intermediate** — [full Russian translation](https://www.mathnet.ru/php/getFT.phtml?jrnid=mat&option_lang=eng&paperid=332&what=fullt), `turn76view2`/`turn80view2`. JMathMech12(2),235–245; DOI10.1512/iumj.1963.12.12016. Translation Matematika8(5)(1964),91–101. **Sections1–4 read.** Title explicitly identifies Alexander. This resolves the method, not conclusively the visiting speaker. Missing determinant is explicitly reconstructed off the original spectrum. Item verification upgraded after full-text access succeeded.

6. **przeworskarolewicz1968periodic** — [publisher issue](https://www.impan.pl/en/publishing-house/journals-and-series/studia-mathematica/all/31/5), `turn64view0`/`turn65view0`. DanutaPrzeworska-Rolewicz,Studia31(5),507–511; DOI10.4064/sm-31-5-507-511. **Metadata only**; PDF returned403 (`turn67view0`). No exact periodic-delay reduction read.

7. **przeworskarolewiczrolewicz1969control** — [publisher issue](https://www.impan.pl/en/publishing-house/journals-and-series/studia-mathematica/all/32/2), `turn64view1`/`turn65view1`. DanutaPrzeworska-Rolewicz and StefanRolewicz,Studia32(2),149–152; DOI10.4064/sm-32-2-149-152. **Metadata only**; PDF403 (`turn67view1`). Only a thematic lead; neither exact theorem nor speaker identity certified.159.4 remains F.

8. **perelomovpopov1968casimir** — [publisher page](https://www.mathnet.ru/eng/im2520), `turn64view5`. MathUSSR-Izv2(6),1313–1335; DOI10.1070/IM1968v002n06ABEH000731. Received26June1967. **Abstract/metadata checked.** No exact match to the matrix/tensor-product diagram; no Horn or random-matrix theorem guessed.

9. **nist2026dlmf** — [official18.5](https://dlmf.nist.gov/18.5), `turn64view4`. Rodrigues formulas §18.5(ii),Table18.5.1 and Jacobi hypergeometric formulas §18.5(iii) checked.2026 is access year, not discovery. Fractional-calculus example is an explicitly supplied Riemann–Liouville reconstruction via the beta integral.

10. **gelfandkirillov1966corps** — [full paper](https://www.numdam.org/item/PMIHES_1966__31__5_0.pdf), `turn75view1`. PMIHES31,5–19; DOI10.1007/BF02684800. Introduction checked for programme context, not every theorem. Cumulative entry/key reused. A reading-list citation does not reactivate every earlier conjecture.

11. **gromov1969stable** — [metadata](https://www.mathnet.ru/eng/im2178), `turn13view1`; [full English paper](https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=2178&what=fullteng), `turn16view1`/`turn78view3`. MathUSSR-Izv3(4),671–694; DOI10.1070/IM1969v003n04ABEH000796. **Received8July1968, published1969.** Sections3–4 read. Theorem4.1.1,pp680–681 requires open manifold, natural bundle and open invariant relation; genuine-to-formal solution map is a weak homotopy equivalence.4.2.1 treats rank conditions;4.4.2–4.4.3 add foliation hypotheses. No unrestricted plane-field foliation theorem certified. Coordinated key/scope with149.4, an earlier programme occurrence without a problemID.

12. **nash1956embedding** — [PDF opened](https://mccuan.math.gatech.edu/courses/6455/nash55.pdf), `turn68view2`. AnnMath63(1),20–63; DOI10.2307/1969989. No usable text extraction. **Identity/scope checked, not a numbered theorem read**; explicitly limited in162.5.

13. **choquet1958nash** — [Bourbaki page](https://numdam.org/item/SB_1956-1958__4__139_0/), `turn75view0`/`turn50view2`. Volume4,Exposé147,139–149. **Metadata/bibliography read**; alternate PDF routes failed. References identify Nash1954,Kuiper1955,Janet1926,Cartan1927; originals not opened. Their attribution is marked metadata/indirect. Modern statement supplies analytic, shortness and embedding hypotheses.

14. **hormander1967hypoelliptic** — [full paper](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6044-11511_2006_Article_BF02392081.pdf), `turn39view0`. ActaMath119,147–171; DOI10.1007/BF02392081. Theorem1.1,p149 and Sobolev-gain proof checked. Volume1967; printed7February1968, before the talk. Classified E.

15. **radkevich1969hormander** — [metadata](https://www.mathnet.ru/eng/rm5484), `turn75search0`; [full Russian paper](https://www.mathnet.ru/php/getFT.phtml?jrnid=rm&option_lang=eng&paperid=5484&what=fullt), `turn76view1`. UMN24(2(146)),233–234. **Received19November1968**, six days before the talk; published1969. Theorems1–3 read. Stronger vector-field estimate and symbol-commutator criterion; the full general nonnegative-quadratic-form statement is tied precisely to1971, not asserted identical to this note.

16. **oleinikradkevich1971local** — [metadata](https://www.mathnet.ru/eng/rm5195), `turn13view2`; [full English paper](https://www.mathnet.ru/php/getFT.phtml?jrnid=rm&option_lang=eng&paperid=5195&what=fullteng), `turn16view2`/`turn79view2`/`turn80view0`. RMS26(2),139–156; DOI10.1070/RM1971v026n02ABEH003821. **Theorem6,pp145–147** and coefficient hypotheses read. Theorem2 shows smooth bracket rank is not necessary in blanket form; analytic necessity has extra hypotheses. References14–18 locate1969 announcements and1971 monograph. The ambiguous notebook necessity line does not become a fabricated precise problem.

17. **dwork1960rationality** — [metadata](https://www.mathnet.ru/eng/mat201), `turn17view3`; [full Russian translation](https://www.mathnet.ru/php/getFT.phtml?jrnid=mat&option_lang=eng&paperid=201&what=fullt), `turn50view3`/`turn94view3`. AmerJMath82(3),631–648; DOI10.2307/2372974. Translation Matematika5(6)(1961),55–72. Sections1 and4 read. **§4,Theorem2,p68** needs compatible radii with product>1; bare nonzero radii do not suffice. Propositions1–3 and Shnirelman discussion support the non-Archimedean analysis.1960 theorem predates this talk.

18. **serre1962endomorphismes** — [full paper](https://www.numdam.org/article/PMIHES_1962__12__69_0.pdf), `turn38view1`/`turn98view0`. PMIHES12,69–85; DOI10.1007/BF02684276. Received18December1961. Sections1,4–5 read. Proposition7 gives the entire Fredholm determinant under the stated completely-continuous and Banach-space hypotheses. Norm-limit finite rank is distinguished from mere boundedness; orthonormalizability and the discrete-valuation equivalent-norm reduction are explicit.

19. **thorne2010padic** — [author-hosted notes](https://www.dpmms.cam.ac.uk/~jat58/all.pdf), `turn38view3`/`turn94view1`. Harvard summer tutorial2010,35pages. Theorems6.8–6.9 checked for Borel–Dwork/Hankel criteria. Modern clarification, not historical novelty.

20. **margulis1969applications** — [metadata](https://www.mathnet.ru/eng/faa2746), `turn17view0`; [full Russian paper](https://www.mathnet.ru/php/getFT.phtml?jrnid=faa&option_lang=eng&paperid=2746&what=fullt), `turn50view1`/`turn94view0`/`turn79view0`. FAA3(4),335–336; Russian89–90; DOI10.1007/BF01076325. **Received6June1969**, after theFebruary seminar. Theorems1–2 give leading count/constant; Theorem5 and Remark6 give the horospherical method. Theorem6 separates complementary-series contributions. One fractional exponent in OCR is illegible: **its exact value is not quoted**. Web screenshots returned placeholders and direct PDF download403. The leading theorem only partially matches the notebook’s unspecified area-plus-boundary expression.

21. **chatzakosetal2025hyperbolic** — [arXiv record](https://arxiv.org/abs/2506.13883), `turn38view2`; [full HTML](https://arxiv.org/html/2506.13883v1), `turn39view3`/`turn42view2`. Chatzakos,Cherubini,Lester,Risager,first posted16June2025; DOI10.48550/arXiv.2506.13883. Introduction,Eqs1.3–1.4 and Theorem1.1 read. General pointwise conjecture is half-plus-epsilon after full spectral subtraction. The theorem is a logarithmic improvement over two-thirds for specified Heegner points. SL2/PSL2 and group-element/orbit-point conventions affect constants and must be fixed explicitly.

22. **biro2026localsquare** — [arXiv record](https://arxiv.org/abs/2604.11205), `turn109view0`; [full HTML](https://arxiv.org/html/2604.11205v1), `turn109view1`. First posted13April2026; DOI10.48550/arXiv.2604.11205. Introduction,§1.1,Theorems1.1–1.2 read. Modular-group local square mean, with conditional exponent improvement under a twisted Linnik–Selberg/Salié-sum conjecture. **Not a general pointwise square-root bound.** Introductory lack-of-improvement wording concerns the power exponent, compatible with the2025 logarithmic special-point result. Latest directly checked status source.

## Searches, failed routes, and unresolved identifications

Queries combined author, exact journal/year/page fingerprint and mathematical statement: Ihara congruence monodromy107–121; Sweeney Acta120 Spencer; Kirillov1968 traces/compact characters; Weinstein intermediate eigenvalues; Rolewicz periodic differential-difference equations/control; Perelomov–Popov convex region/matrix spectra; Gromov1969 stable mappings/open invariant differential relations; Oleinik–Radkevich1968/1969 hypoellipticity; Dwork/Borel–Dwork rationality; Serre completely continuous endomorphisms; Margulis1969 count; hyperbolic circle problem latest2025/2026. Publisher, author-hosted, MathNet, Numdam and arXiv sources were preferred. Stronger search was used for attribution, exact hypotheses and recent status. Snippets were discovery leads, not read-result evidence.

- MCCME live record fetches failed. Supplied scans and transcriptions remain primary authority.
- IUMJ Weinstein issue route returned502; the later MathNet full translation succeeded. This resolved the method and author name, not the notebook speaker’s first name.
- Rolewicz publisher download links403. Two verified titles remain thematic F leads, not exact A matches.
- Universal orbit formula, generic Haar factor, unrestricted root product, integral-orbit representation count, matrix/tensor duality and fractional-derivative convention lack enough scope for exact identification. Verified special cases are separated; no open problems invented.
- Berezin’s “existence of all representations” lacks the group and category. Volume-level lead retained; exact theorem unresolved.
- Gromov’s final two approximation statements lack legible/sufficient dimension and topology hypotheses. They remain F. The open invariant theorem is separately precise and is not applied to arbitrary closed metric relations or arbitrary bundles with nonempty fibres.
- Oleinik’s necessity line and Gelfand’s integrability question have insufficient quantifiers. A clearly marked interpretation is supplied without claiming a determinate general solved/open theorem.
- Duflo–Moore1976 nonunimodular Plancherel was searched as a scope check. Primary abstract identified formal-degree corrections, but full text was blocked; not cited as a read result or newly matched fate.
- Kirillov1969 reduction metadata opened at https://www.mathnet.ru/eng/faa2696 (`turn51view1`), received28May1968; no closer unrestricted match, so not cited.
- Linnik’s line is an analogy only. Earlier1964-14.2 is context, not an exact new recurrence of an indexed conjecture.
- November2026 C status means no solution to the stated general pointwise problem was found in the checked literature, supported by explicit2025/2026 sources; it does not claim an exhaustive search of inaccessible/unpublished work.

## Principal mathematical decisions

Closed/geometric points and separability in the finite reduced-fibre criterion are distinguished. Taylor derivative variables on P254 are interchanged in the manuscript. The many-point jet passage supplies no alternating convention. The first Spencer sequence is exact with negative-order bundles zero, while arbitrary linear PDE systems need extra regularity/exactness hypotheses.

Kirillov’s kernel theorem is E because it was already printed. Nilpotent and compact shifted-orbit results are established, but compact orbits are not all regular: the zero orbit is singular. The SU2 sphere integral needs factor2 under the stated measure. The2×2 skew determinant is positivea²; the Pfaffian is a classical exercise. Rodrigues formulas need normalization and a Jacobi weight divisor. All-group Plancherel is qualified rather than accepted literally.

Genuine differential-relation solutions require jet prolongation. Immersion rank is an open local jet condition; global embedding is not. A C1 immersion does not become an embedding merely by changing its induced metric. Janet–Cartan requires analytic metrics. Gromov’s received/publication dates are separated.

Formal Euler factors do not locate poles after analytic continuation. Borel–Dwork needs compatible radii. Qp’s unit ball is compact, contrary to the manuscript; Cp is not locally compact. A nonzero entire Cp function has finitely many zeros in a bounded closed disc without compactness. Integral reciprocal roots require a **reduced** rational quotient; canceled factors otherwise give counterexamples.

Both hyperbolic-disc area and boundary length grow like πexp(R). Their notebook sum does not specify a leading term plus a lower-order boundary correction. Published leading counting is separated from the reconstructed error conjecture, which needs small-eigenvalue subtraction and is weaker than a literal square-root big-O claim.

## Reproducibility and validation

`write_c.py` regenerates JSON/CSV incrementally. `validate_c.py` checks schema, enums, consecutive IDs, counts, empty heading/plan records, citation-key availability, reference lists, problem links, LaTeX braces/math delimiters, control characters and correction types. Output is `validation.txt`. The parent performs integrated chapter-builder and XeLaTeX/BibTeX checks; this fragment does not claim an independent final-document compilation.
