# Research and verification log: records 530–537

Status date: 2026-11-11. This is a bounded audit, not a claim of exhaustive literature coverage. A bibliographic item marked `verified` means that the identified URL or full work was opened; the annotation states whether only metadata, a result statement or a proof was actually read. Indirect verification and thematic matches remain explicit in the occurrence data.

## Source ownership and scan checks

The English and Russian diplomatic files were read, with the Russian controlling doubtful formulas. Actual scans P000981–P000994 were inspected, including the decisive signs, exponents, diagrams, table entries and dated boundaries. Catalog ranges overlap and do not determine ownership of content.

| Record | Actual content boundary | Result |
|---|---|---|
| 530 | First heading on P000981, before 21 September | Heading only; no mathematical item invented |
| 531 | 21 September on P000981 to Rudakov heading P000984 | 14 distinct items |
| 532 | Rudakov P000984 to return arrow to S. I. Gelfand P000986 | 7 items, including two separately recorded Rogers–Ramanujan identities |
| 533 | Return arrow P000986 to next dated heading P000987 | 4 items |
| 534 | 28 September P000987 to Zelevinsky heading P000989 | 11 items |
| 535 | Zelevinsky P000989 to 19 October P000990 | 7 items |
| 536 | 19 October P000990 through P000991 | 7 items |
| 537 | 16 November P000992 through P000994, before 23 November | 8 items |

The scans confirm that several errors are faithful to the manuscript: order of S_n, root versus weight lattice, affine-case contradiction, negative rho shift, the number-of-representations gloss on the interlacing question, and the preliminary minus-one-half Levi density. These are marked `faithful_error`, not transcription mistakes. The later 4/3 and -1/3 density is an internal correction in the notes. The Hilbert formula c_k/k is also visible and is correct under c_k=k dim V_k; it was deliberately retained. Every editorial correction or unresolved interpretation is separately logged in corrections.csv.

## Earlier index and problem identity

The supplied earlier index was searched with `rg` for root multiplicities, Kac–Moody, Verma, Bruhat, quiver, finite-type, p-adic, Zelevinsky, Kazhdan, Gelfand–Tsetlin, interlacing and Young-graph terms. Relevant exact occurrence labels include 1972-277.8 (finite-type quivers), 1972-278.9 (tame extended Dynkin quivers), 1976-415.5 (Young-graph/tableau basis), 1979-483.1 (Bruhat), 1979-483.6 and 1979-484.4 (Verma multiplicities/IC), and 1980-520.1–2 (Verma modules). GP-1972-301, GP-1976-24 and GP-1979-41 are related problems but not identical to the new questions here. In particular the p-adic GL_n formula is not silently merged with the Verma-module KL conjecture; integer Gelfand–Tsetlin patterns are not the same branching problem as Young-graph standard-tableau paths. New identifiers are GP-1981-01 (root words/multiplicities), -02 (three matrix double quotients), -03 (fixed-top-row interlacing count), and -04 (identified p-adic multiplicity formula). No previous exact problem identity was found in the supplied index for these four.

## Search strategy and negative results

Routine bibliographic discovery used system2; primary/authoritative verification used system1, Math-Net metadata/full-text links, author bibliographies, author-hosted papers, arXiv versions and publisher metadata. Search families included the notebook reading-list authors; Kac/BGG exact titles; Berman–Moody root multiplicities; Seifert Bruhat/transformation-group axioms and tree papers; Abeasis–Del Fra–Kraft A_m; rank-two Serre presentations; Schwarz supergravity/complex geometry/SCR; Zelevinsky graded nilpotent classes and the p-adic KL hypothesis.

Exact late-stage queries included `Gelfand Novikov Lorentz representations neutrino mass deformation`, `Zelevinsky "p-adic analog" "1981"`, `"Supergravity and field space democracy" "Received"`, the latter title with `site:projecteuclid.org` and `site:link.springer.com`, and `"Supergravity and complex geometry" Schwarz 1144 1981`. The Lorentz query returned Gelfand–Ponomarev's indecomposable Lorentz representations and much later neutrino/little-group papers, but no source specifying the notebook's approximate-representation/topology/mass-mechanism claim. Those search results are not treated as solutions, and are not cited as theorem sources. The lexicographic word fragment specifies no selection or reduction rule; a Hall/Lyndon completion is labelled a possible reconstruction, not an identified algorithm. Seifert's unnamed exceptions remain unidentified. Thus the three F items are identification gaps, not evidence for open mathematical conjectures.

No C or D item was manufactured. Berman–Moody requires symmetrizability; the wider literal root-space computation is instead justified by the explicit recursive lowering proof. The rank-two question marks were already settled by old classification. The p-adic statement required following the exact conjecture and standard-object comparison, rather than declaring the 1985 Schubert map a proof of a representation-theoretic multiplicity theorem.

## Full-text routes and decisive locators beyond bibliographic landing pages

- Kac English full text: https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=2519&what=fullteng . Chapter II sections 1–2 and 4–7 read. The paper intentionally allows a “zero root” convention; modern exclusion of zero is labelled a convention change.
- BGG Russian full text: https://www.mathnet.ru/php/getFT.phtml?jrnid=faa&option_lang=eng&paperid=2556&what=fullt . Section 2 finite-dimensional semisimple scope, section 3 shifted highest-weight parameter and Hom theorem, condition (A) and necessity/sufficiency theorems read.
- Macdonald: https://numdam.org/item/SB_1980-1981__23__258_0.pdf . Exposé 577 is dated June 1981; the archive catalogues the collection in 1981. Pages 259–264 were used for classical roots/weights/characters and Kac–Moody setup. Later digital dates are irrelevant to the seminar chronology.
- Berman–Moody complete primary text: https://www.researchgate.net/publication/238868888_Lie_Algebra_Multiplicities . Uploaded by author Robert Moody; section 2 explicitly assumes symmetrizable A, Theorem 2 p.225 gives multiplicities, p.226 gives free-Lie/Witt specialization. The earlier JSTOR open exposed only tag-manager content; that failed attempt was not counted as theorem verification.
- Abeasis–Del Fra–Kraft author bibliography: https://kraftadmin.wixsite.com/hpkraft/copy-of-home . The linked full PDF is https://da54b6ee-8535-497a-8098-bc8e3f6f49a1.filesusr.com/ugd/68dc5d_91bb91f97a9f45d9927e066b4f90515f.pdf . Downloaded and rendered; Theorem 0.2 p.401 states normality, Cohen–Macaulayness and rational singularities; section 1.1 p.403 states algebraically closed characteristic zero; Proposition 2.2 and section 2.3 p.404 give rank degeneration and interval multiplicities.
- Zelevinsky 1981 Russian full text: https://www.mathnet.ru/php/getFT.phtml?jrnid=faa&option_lang=eng&paperid=1707&what=fullt . The introduction explicitly formulates the IC-stalk equality as a conjecture; sections 1.4 onward specify the nonarchimedean group and multisegment conventions. The exact §1.9 identification is also cross-checked in Balodis. English introduction transcription: https://math.soimeme.org/~arunram/Resources/PAAOTKLHIntroduction.html . It is an attributed excerpt of the primary article, not a secondary claim.
- Zelevinsky 1985 primary English transcription: https://math.soimeme.org/~arunram/Resources/TwoRemarksOnGradedNilpotentClasses.html . Theorem 1 and Corollary 1 read; source metadata at https://www.mathnet.ru/eng/rm2155 supplies receipt 4 April 1983 and 1985 publication. The corresponding PDF was not accessible. The precise statement is about an open Schubert patch, not that every quiver orbit is an affine cell.
- Lakshmibai–Magyar full preprint: https://arxiv.org/pdf/alg-geom/9709018 . Sections 1.1, 1.3 and 2.2 distinguish the earlier bijection from the scheme-theoretic theorem. The block map and boundary ranks were read.
- Solleveld current full preprint: https://arxiv.org/pdf/2106.03196 . Version 3, January 2025, Theorem 5.4(b), printed p.29, explicitly includes inner forms of GL(n). The original 2021 version had incorrect sections removed in the major May 2022 revision; the current statement was used.
- Solleveld comparison: https://arxiv.org/pdf/2309.10401 . Version 3, April 2026, Theorem 6.1 and Lemma 6.2 with proof, printed pp.32–33. The arXiv history warns that a claim about arbitrary tempered constituents being subrepresentations was removed after counterexamples; that claim is not used here. The standard-module comparison lemma survives in the current version and was checked directly.
- Balodis: https://arxiv.org/pdf/2510.09788 . Version 2, submitted 28 February 2026, PDF dated 3 March 2026. Section 1.4 p.4 credits Solleveld's earlier route; Theorem 3.9 p.46 is the precise standard-quotient/IC-stalk statement. The old v1 theorem number 3.10 was not retained. This preprint is not described as the first proof.
- Gelfand–Tsetlin: https://www.math.ucdavis.edu/~deloera/MISC/LA-BIBLIO/trunk/Gelfand/Gelfand7.pdf . Full four-page English collected-paper reprint was downloaded and visually read; section 3, formula (3), reprint p.655, states arbitrary-rank integer interlacing basis. Its first page identifies the 1950 original and submission date 16 February 1950.
- Berezin–Leites: https://www.mathnet.ru/php/getFT.phtml?jrnid=dan&option_lang=eng&paperid=39282&what=fullt . All four original Russian pages opened. Definitions 1–4, density transformation (3), Theorems 1–2 and group-object definition read. This supplements the cumulative entry, whose earlier audit had checked only metadata.
- Schwarz complete primary author upload: https://www.researchgate.net/publication/225269051_Supergravity_complex_geometry_andG-structures . Read section 1 functorial setup; section 3, printed pp.44–48, Levi equations (3), (7), (8), both covariance checks and the paragraph after equation (9) asserting restricted uniqueness; sections 4–6 SCR frames and the explicit attribution of the uniqueness proof to reference 3 at p.58. The full-text OCR separates many words into syllables but the mathematical formulas, prose and printed page labels are identifiable.
- Konechny–Schwarz: https://arxiv.org/pdf/hep-th/9609081 . Sections 1–3 read. First circulation September 1996 versus journal 1997 is recorded. This is a later SCR gauge-theory application, not the first action construction.

## Access limitations and remaining identification gaps

Seifert 1984 DOI https://doi.org/10.1112/jlms/s2-29.3.441 , OUP https://academic.oup.com/jlms/article-abstract/s2-29/3/441/914794 and Wiley https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/jlms/s2-29.3.441 returned failures/403. Publisher search metadata and Seifert's full 1986 paper reference S.1 establish the publication lineage, but not the exact four-axiom theorem. It remains `note={unverified}` for direct reference access and occurrence verification `indirect`. Its correct title is “Transitivity Properties, Bruhat Decomposition and Tits Systems for Transformation Groups”; a preliminary guessed title was discarded. The full 1986 paper is “Highly transitive group actions on trees and normalizing Tits systems,” pp.447–458, not the initially guessed generic title/page range. Its introduction explicitly distinguishes its hypotheses and proof from the earlier work.

Schwarz's Euclid PDF https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-87/issue-1/Supergravity-complex-geometry-and-G-structures/cmp/1103921903.pdf and the older download/pdf_1 route returned a challenge, not a paper. The failed local download is HTML and is excluded from the final deliverables. Full verification instead used the author-uploaded primary text. Gayduk–Romanov–Schwarz 1981, DOI https://doi.org/10.1007/BF01209310 , remained inaccessible in full (publisher failure; ResearchGate 403/429). Its metadata and abstract were read in the author bibliography, and the exact proof attribution was read in Schwarz 1982. This is an explicit proof-access limitation. No month was inferred from ResearchGate's generic “December 1981” indexing. The incomplete Nuclear Physics 1981 notebook citation remains unresolved: the securely identified matching earlier Schwarz field-space paper is Nuclear Physics B171 (1980),154–166. October 1981 Yadernaya Fizika N=10 is interpreted bibliographically as month 10, volume34 issue4, rather than issue10.

The Rogers–Ramanujan article was checked at metadata/abstract level (February1981, affine A1 interpretation), not by reading its complete proof. The classical formulas themselves are not claimed as a discovery of that paper. A repeat PMC open later returned a challenge. The Humphreys chapter was likewise identified at metadata level only. These limitations are reflected in the respective fields.

## Proof and computation checks

The appendix labels all supplied proofs `ours`, and all supplied finite calculations `oursComputed`, without a novelty claim. It gives the complete recursive lowering argument, the infinite faithful transitive stabilizer counterexample, the degree-two double-transitivity exception, interval inversion, the explicit sl2 rho-sign test, and determinant covariance. Each is also checked by an independent method or parameter specialization. The Python code and complete output are retained: necklaces versus Witt (65 bidegrees), Catalan recurrence versus specialization (n=0–12), GT recursion versus product (210 top rows plus displayed examples), explicit arrow matrices versus interval inversion (120 supports), lowering recursion versus independently generated Serre ideals (five rank-two matrices through height8), and Euler-product expansion versus logarithm through degree14. All checks passed. No finite calculation is used as evidence of a general theorem without the separate proof or identified literature result.

The generator writes sorted talk/item data and consecutive record-local occurrence numbers. A final schema/citation audit checks records, fields, enums, problem links and bibliography keys. Temporary copies of copyrighted source PDFs/images are excluded from final deliverables; they were used only for verification.

## Bibliographic opening audit

The entries below are generated from the final bibliography so that metadata-only versus proof-level access remains visible alongside the exact opened bibliographic URL. More detailed full-text routes are given above.

- **kac1968graded** (verified): https://www.mathnet.ru/eng/im2519
  Cumulative key reused. Primary metadata and complete English PDF opened. Chapter II sections 1--2 (construction and roots), sections 4--7 (finite and affine classification) read. Received 13 February 1968. Checked 2026-11-11.

- **berezinleites1975supermanifolds** (verified): https://www.mathnet.ru/eng/dan39282
  Cumulative key reused. Primary metadata and complete four-page Russian PDF opened on 2026-11-11. Read section 2 Definitions 1--4, section 3 density rule (3) and Theorem 1, section 4 Theorem 2, and section 5 supergroups. Received 24 March 1975.

- **macdonald1981affine** (verified): https://numdam.org/item/SB_1980-1981__23__258_0/
  Archive catalogue year 1981; expose 577 delivered June 1981. Metadata and full PDF opened. Sections 1--3 read, especially pp 259--264, root and weight lattices, character and denominator formulas, Cartan realization and symmetrizability. This is the notebook's exact Bourbaki reading-list reference.

- **humphreys1980highest** (verified): https://link.springer.com/chapter/10.1007/BFb0089779
  Publisher metadata and references opened, full chapter not read. Original 1980 publication distinguished from 2006 online date. Exact reading-list identification only.

- **serre1987complex** (verified): https://prclare.people.wm.edu/m410f23/Serre_Complex_semisimple_Lie_algebras.pdf
  Complete English translation opened. Preface identifies the Algiers lecture course of 10--21 May 1965. Read II.2, III.5, V.3--13, VI.4 and Appendix, VII.1--8, VIII.4 and VIII.7. Later translation is used for old results, not as their first publication.

- **bernsteingelfandgelfand1971structure** (verified): https://www.mathnet.ru/eng/faa2556
  Primary metadata and complete Russian original (5(1),1--9) opened. Section 2 fixes finite-dimensional complex semisimple scope; section 3 Definition 1, Lemma 1 and Theorem 1, section 4 condition(A) and Theorem 2, section 5 Theorem 3 read. Received 5 October 1970. The shifted parameter is separated from the notebook's unshifted highest weight.

- **polo2026realizations** (verified): https://webusers.imj-prg.fr/~patrick.polo/CMI-KM/KMch1-feb2.pdf
  Author-hosted complete twelve-page PDF opened. Definition 1.1, Proposition 1.3 and Definition 1.4 read. The chapter description in the title is descriptive; no journal publication is claimed.

- **bermanmoody1979multiplicities** (verified): https://www.researchgate.net/publication/238868888_Lie_Algebra_Multiplicities
  Complete primary text in author-uploaded copy (Robert Moody) opened and read. Section 2 explicitly assumes symmetrizability. Theorem 2 and its logarithmic/Mobius proof, p 225, free-Lie specialization p 226, and Theorem 3 checked. Received 28 September 1978; published September 1979. JSTOR DOI 10.2307/2042993 identifies the same article; JSTOR access alone did not expose the full result.

- **lepowskywilson1981rogers** (verified): https://pmc.ncbi.nlm.nih.gov/articles/PMC319869/
  Metadata and abstract opened in this run; the full three-page article was not read. February 1981 date and affine A 1 vacuum-state interpretation checked. A later repeat of the same PMC open returned a browser challenge. The classical identities themselves are checked independently as formal products/sums.

- **seifert1984transitivity** (unverified): https://academic.oup.com/jlms/article-abstract/s2-29/3/441/914794
  Primary publisher search-index metadata checked (received 5 March 1983; publication 1 June 1984), and the author's 1986 paper referenceS.1 read. Direct DOI/OUP/Wiley opens failed. Full theorem hypotheses and proof have not been read; exact notebook axiom match is not certified. An initially guessed title was discarded before final delivery.

- **seifert1986highly** (verified): https://msp.org/pjm/1986/125-2/pjm-v125-n2-p12-s.pdf
  Complete primary paper opened; introduction, Theorem 2.2 and referenceS.1 read. The introduction distinguishes its tree-action hypotheses/proof from the earlier transformation-group work. Received 4 April 1984, revised 1 September 1985; October 1986 issue.

- **abeasisdelfrakraft1981geometry** (verified): https://link.springer.com/article/10.1007/BF01679706
  Publisher metadata opened; received 1 April 1981, September 1981 issue. Author bibliography linked to the complete author-hosted PDF, downloaded and visually read: Theorem 0.2 p 401, characteristic-zero convention section 1.1 p 403, rank invariants/Proposition 2.2 and interval decomposition section 2.3 p 404. Exact notebook report, not a later solution.

- **zelevinsky1981padic** (verified): https://www.mathnet.ru/eng/faa1707
  Primary metadata and complete 13-page Russian original (15(2),9--21) opened. Introduction, sections 1.4--1.9 and determinantal discussion in section 3 read. Received 27 November 1980; April--June 1981 original. English introduction also read in ArunRam's explicitly attributed primary-text transcription. This is a conjectural multiplicity formula, not the later 1985 purely geometric result.

- **zelevinsky1985graded** (verified): https://www.mathnet.ru/eng/rm2155
  Primary MathNet metadata opened; received 4 April 1983. Original Russian UMN 40(1),199--200. Primary article's English transcription read at https://math.soimeme.org/~arunram/Resources/TwoRemarksOnGradedNilpotentClasses.html, especially Theorem 1 and Corollary 1. PDF access failed. Later scheme refinement checked separately in Lakshmibai--Magyar.

- **lakshmibaimagyar1997degeneracy** (verified): https://arxiv.org/abs/alg-geom/9709018
  Metadata and complete primary preprint opened. Section 1.1 ranks and interval inversion, section 1.3 Zelevinsky block map and set bijection, and section 2.2 scheme theorem read. Abstract distinguishes scheme isomorphism from the earlier bijection and gives arbitrary-characteristic reducedness/Cohen--Macaulayness. No unverified journal publication data supplied.

- **solleveld2021graded** (verified): https://arxiv.org/abs/2106.03196
  First submitted 6 June 2021; major corrected version 2,16 May 2022, changed title and removed incorrect old sections 7--8; version 3, 17 January 2025. Current 38-page PDF read at section 5 Theorem 5.4, p 29, especially part(b), unconditional for inner forms of GL(n). Distinguishes preprint chronology from formal publication; no unverified journal claim.

- **solleveld2023submodules** (verified): https://arxiv.org/abs/2309.10401
  First submitted 19 September 2023; version 2,16 May 2024; version 3, 24 April 2026. Current 41-page PDF (dated 27 April 2026) read at Theorem 6.1 and Lemma 6.2 with proof, pp 32--33. The current version removed claims about all tempered constituents being subrepresentations; that removed claim is not used. The surviving lemma compares Langlands standard representations.

- **balodis2025padic** (verified): https://arxiv.org/abs/2510.09788
  First submitted 10 October 2025; version 2 submitted 28 February 2026 (PDF dated 3 March 2026). Complete 48-page PDF opened. Section 1.4 p 4 credits Solleveld's earlier graded-Hecke proof and standard-object comparison; Theorem 3.9 p 46 states the precise multiplicity/IC-stalk equality. Do not call this the first proof or use the old version 1 theorem number 3.10.

- **gelfandtsetlin1950unimodular** (verified): https://www.math.ucdavis.edu/~deloera/MISC/LA-BIBLIO/trunk/Gelfand/Gelfand7.pdf
  Complete English collected-paper reprint pp 653--656 opened, downloaded and visually read. First page gives original citation and submitted 16 February 1950; section 3 formula(3), reprintp 655, gives arbitrary-rank integer interlacing patterns indexing a basis.

- **schwarz1980equal** (verified): https://celebratio.org/Schwarz_Albert/article/940/
  Author collected bibliography and abstract opened; full original not obtained. Also identified as reference 9 in Schwarz 1982. The notebook's incomplete NuclearPhysics 1981 allusion is not silently equated with this 1980 article.

- **schwarz1981complex** (verified): https://celebratio.org/Schwarz_Albert/article/940/
  Author collected bibliography opened, original citation and English translation SovietJournalofNuclearPhysics 34(4),635--637 verified. October 1981 announcement; full article not read. Notebook N=10 is interpreted as month, not issue 10.

- **gaydukromanovschwarz1981democracy** (verified): https://celebratio.org/Schwarz_Albert/article/940/
  Metadata and abstract in author bibliography opened; the exact original proof was inaccessible. Schwarz 1982 section 3 p 48 and section 6 p 58 explicitly credit this reference 3 for the uniqueness argument. No specific month inferred from unreliable generic December indexing. The verification of full uniqueness is indirect.

- **schwarz1982supergravity** (verified): https://www.researchgate.net/publication/225269051_Supergravity_complex_geometry_andG-structures
  Publisher metadata and full primary author-uploaded text opened. Received 15 February 1982. Read section 1 functor setup; section 3 pp 44--48, equations 3,7--9, Levi form, compensator and both covariance checks; uniqueness paragraph p 48, and G/SCR construction sections 4--6 including p 58. Primary text is an author upload, not a secondary summary. Euclid downloads returned a challenge and were not counted as reading.

- **konechnyschwarz1997geometry** (verified): https://arxiv.org/abs/hep-th/9609081
  Primary metadata and complete 16-page PDF opened. First arXiv submission 10 September 1996, revised 12 September 1996, journal 1997. Sections 1--3 read: SCR geometry induced by complex structure plus volume and its gauge-theory application. This is a later application, not a substitute for the 1981 action theorem.

## Final integration checks

Final counts: 8 records (one heading only), 58 items (E47, A7, B1, F3), 4 problems, 35 correction rows, and 24 references. All citation keys are present and used. The final schema audit passed. Formula-bearing correction cells are normalized by normalize_corrections.py, including raw subscript/superscript notation in headings. The first aggregate XeLaTeX run found raw underscore strings and one overlong six-factor GT display; the generator and JSON/CSV were corrected, the GT expression was split into a compact product plus two aligned numerator lines, and the weight-lattice definition was moved into a display. Aggregate compilation and final visual inspection are owned by the integrating agent. Temporary source downloads remain solely as a verification cache and are not intended for the ZIP.
