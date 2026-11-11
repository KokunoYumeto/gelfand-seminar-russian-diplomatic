# Research and verification log: records 538–544

Status date: 11 November 2026. Scope is the seven named manuscript sections, not the overlapping MCCME catalog page spans. This part supplies 42 mathematical occurrences, four problem-index entries, and a separate correction/provenance log. The classification records whether a result was already known, published soon afterward, developed later, or too poorly specified; it is not a priority claim for the seminar.

## Source boundaries and manuscript examination

Both uploaded TeX transcriptions were read. The Russian was consulted whenever terminology or a formula mattered. The original images `GELFAND-P000995.png` through `GELFAND-P001000.png` were all opened and visually inspected. Their actual headings yield these boundaries:

| Record | Actual section | Decisive evidence inspected |
|---|---|---|
| 538 | P000995 to upper P000996 | Simple-generator brackets; first highest-vector definition; `M(psi)` in the first multiplicity question; following `L(psi)` formula; dominant weight and rho conventions. |
| 539 | Middle P000996 | Named Beilinson heading, category-O nilradical signs, marginal correction, restricted-dual sentence. |
| 540 | Foot of P000996 to lower P000997 | Compressed contravariant-form indices, fixed-vector filtration definition, explicit change-rho question, reversed multiplicity bracket, local-cohomology sketch. |
| 541 | Lower P000997 to middle P000998 | New Zelevinsky heading; Gelfand intervention; determinant exponents; Cauchy minus denominator; affine indices; entirely cancelled Kac–Moody formula. |
| 542 | Lower P000998 | Irreducibility insertion in definition of primitive; last-column-zero convention; gl2/V4 example; gamma aside; cancelled word before simple. |
| 543 | P000999 to upper P001000 | Reeb/Cartier heading; van der Pol/Rayleigh signs; genuinely round probability codomain brackets; zero-one equivalence; arrow-halving parenthesis and infinite hats. |
| 544 | Foot of P001000 | Krichever heading, collaborator spelling with `o`, ascending union without a specified algebraic law, sigma product and zeta exponent. |

The catalog page ranges are retained in `talks.json`, with the actual boundaries explained in the summaries. No contents of the adjacent Schwarz or Müller sections were reassigned to these records. The correction CSV separates mathematical errors faithfully reproduced by the transcriptions from genuine uncertainties and provenance matters. In particular, the last-column-zero affine realization is **not** silently “corrected” to a last-row-zero realization: minus transpose gives an isomorphic Lie algebra.

## Searches and opened primary sources

The research used routine web searches followed by stronger `system1_search_query` verification for decisive sources and negative identifications. Representative routes included Jantzen deformation direction and regular/non-dominant counterexamples; Elashvili Frobenius Lie algebras primitive envelopes; Cartier Bourbaki November 1981 nonstandard perturbation; Lusztig affine weight multiplicities; Krichever 1982 Peierls and elliptic matrix functions; and surreal sign sequences. Search results alone were not treated as proof of a theorem. The following links were actually opened during this run.

### Verma modules, category O, and the Kazhdan–Lusztig theorem

1. **Brylinski (1981), full primary exposition.**
   <https://www.numdam.org/item/AST_1981__87-88__43_0.pdf>
   Introduction and §1, especially pp. 43–47, were read for the 1980 lecture provenance, central characters, the dot action, and the then newly proved multiplicity theorem. The article records the Toruń meeting of 27 August–3 September 1980. This is evidence of circulation before the November 1981 seminar, distinct from its 1981 publication.

2. **Beilinson–Bernstein (1981), author bibliography.**
   <https://www.math.tau.ac.il/~bernstei/Publication_list/Publication_list.html>
   Bibliographic identity checked: C. R. Acad. Sci. Paris, Série I, 292, 15–18. The complete 1981 proof was not read here. The proof attribution is independently corroborated in Brylinski’s primary account and Lusztig §3. No unsupported precise month is assigned to this announcement.

3. **Brylinski–Kashiwara (1981), publisher record.**
   <https://link.springer.com/article/10.1007/BF01389272>
   Metadata checked: Inventiones Mathematicae 64, 387–410; publisher date October 1981. The full Inventiones proof was not accessible in this route. This supports chronology and attribution, while exact theorem conventions were checked in the readable primary expositions.

4. **Bernstein–Gelfand–Gelfand (1976), full Russian original.**
   <https://www.mathnet.ru/eng/faa2144>
   <https://www.mathnet.ru/php/getFT.phtml?jrnid=faa&option_lang=eng&paperid=2144&what=fullt>
   §1 was inspected for category O and its duality. DOI 10.1007/BF01077933; original 10(2), 1–8; translation 87–92. Received 22 December 1975. This source clarifies why the choice of positive nilradical and restricted anti-involution-twisted dual are essential.

5. **Gabber–Joseph (1981), full original.**
   <https://www.numdam.org/item/10.24033/asens.1406.pdf>
   Introduction and §1 were read for finite length, deformed modules and forms, and the distinction between the Jantzen refinement and the ungraded KL theorem. DOI 10.24033/asens.1406. The cumulative key is reused. The source’s shifted/antidominant conventions were not copied without translating them to the dominant-weight indexing of the notebook.

6. **Shapovalov (1972), publisher metadata.**
   <https://www.mathnet.ru/eng/faa2537>
   DOI 10.1007/BF01077650; original pp. 65–70, English pp. 307–312; received 15 March 1972. The apparent full-text click redirected to metadata in this attempt. Consequently the entry says the original proof was not read, despite the verified URL. The actual form construction was checked through Gabber–Joseph and the later Williamson exposition.

7. **Jantzen (1979), publisher record and contents.**
   <https://link.springer.com/book/10.1007/BFb0069521>
   LNM 750, published 1979. Translation principle pp. 42–77; parameter-algebra modules pp. 112–143; filtrations pp. 144–181. Full book not read. This is used for original chronology, not as a claim to have inspected every proof.

8. **Kazhdan–Lusztig (1980), primary institutional metadata.**
   <https://cris.huji.ac.il/en/publications/schubert-varieties-and-poincar%C3%A9-duality/>
   Geometry of the Laplace Operator, PSPM 36, 185–203; DOI 10.1090/pspum/036/573434. Conference 27–30 March 1979, publication 1980. The conference date alone is not assigned as the first date of every theorem. The full theorem normalization was verified in Lusztig (1983), Theorem 4.1.

9. **Lusztig (1983), full original and metadata.**
   <https://www.numdam.org/item/AST_1983__101-102__208_0.pdf>
   <https://www.numdam.org/item/AST_1983__101-102__208_0/>
   §2 defines the extended affine group and the longest double-coset elements; Theorem 3.1 gives the character formula, Theorem 4.1 the intersection-cohomology interpretation, and Theorem 6.1 the exact finite weight-multiplicity formula. These results were read. The volume belongs to the 6–10 July 1981 meeting, but the exact first circulation of Theorem 6.1 was not independently established. The notebook itself establishes knowledge by November 1981. Record 541.4 is therefore classified B with explicit chronological qualification, not with an invented claim of seminar priority.

10. **Krattenthaler (1999), full primary exposition.**
    <https://arxiv.org/pdf/math/9902004>
    <https://arxiv.org/abs/math/9902004>
    §2.1, equation (2.7), gives Cauchy’s double alternant; substituting `Y_j=-mu_j` checks the sign. The text also connects alternants with Schur characters. First arXiv version 1 February 1999; final 31 May 1999; Sém. Lothar. Combin. 42, B42q. It is a later checked exposition of a classical exercise, not the origin of the identity.

### The Jantzen direction question: a precise negative answer

11. **Beilinson–Bernstein (1993), original full scan.**
    <https://www.math.tau.ac.il/~bernstei/Publication_list/publication_texts/Ber-Beil_ProofJatzenConj.pdf>
    The first pages and statement setup were visually inspected. This is the 50-page Advances in Soviet Mathematics 16, Part 1, pp. 1–50 publication. Not all proofs were read. The exact dominant-direction consequences are also stated in Williamson §1.4. No earlier date for circulation of the complete theorem was verified, so the chapter does not invent one.

12. **Williamson, Local Hodge theory of Soergel bimodules.**
    <https://arxiv.org/abs/1410.2028>
    <https://arxiv.org/html/1410.2028v3>
    <https://arxiv.org/pdf/1410.2028>
    <https://link.springer.com/article/10.1007/s11511-017-0146-8>
    <https://www.maths.usyd.edu.au/u/geordie/papers.html>
    Full §§1.4–1.6 and 8.4 were read. The exact counterexample is in type A3, highest weight `-alpha_1-alpha_3`, at weight difference `(2,3,2)`, with a 13-dimensional PBW weight space. The rho-direction layers have dimensions `(7,3,2,1)`; a regular direction with `gamma(h1+2h2+h3)=0` gives `(7,2,4,0)`. This answers the literal unrestricted expectation negatively; dominant-direction results are separate. First preprint 8 October 2014; v3 14 September 2016; journal Acta Mathematica 217(2), 341–404 is dated 2016, whereas Springer displays online publication 7 July 2017. The DOI route initially failed, but the direct publisher article URL succeeded. A typographical repeated alpha_s in the HTML expression for rho was not propagated; the calculations use Dynkin coordinates.

The original unrestricted question is indexed separately as GP-1981-10. The ordinary multiplicity and coefficient questions retain GP-1979-41, with the prior occurrences 1979-483.6 and 1979-484.4. The erased Kac–Moody formula is not identified with a later theorem simply because both involve KL polynomials.

### Primitive envelopes and Frobenius algebras

13. **Elashvili (1982), complete original announcement.**
    <https://www.mathnet.ru/eng/faa1687>
    <https://www.mathnet.ru/php/getFT.phtml?jrnid=faa&option_lang=eng&paperid=1687&what=fullt>
    Both Russian pages, including the classification table, were inspected; the second page was also viewed as an image. §0 states the Ooms equivalence between primitivity, an open coadjoint orbit, and a nondegenerate Kirillov form. §1 gives the abelian-radical stabilizer criterion. §2 gives castling and ten reduced families. Received **30 November 1981**, seven days after this seminar; published 1982, original 16(4), 94–95, translation 326–328, DOI 10.1007/BF01077870. This is an exact speaker/publication match for the examples and a partial match for the notebook’s much more compressed classification.

14. **Ooms (1976), attempted original routes.**
    DOI attempted: <https://doi.org/10.1090/S0002-9939-1976-0430007-6>
    Institutional attempt: <https://documentserver.uhasselt.be/handle/1942/37477>
    The DOI route was inaccessible and the institutional record returned HTTP 503. An AMS full-text route also failed. The original article was therefore **not** marked as read or added as a verified bibliography entry. Its title, year, volume and pages are reported only through Elashvili’s explicit reference: “On Lie algebras with primitive envelopes, supplements,” Proc. AMS 58 (1976), 67–72. The exact theorem is genuinely printed in Elashvili §0, not inferred from a title.

The new GP-1981-12 problem entry links the earlier 1964-37.1 and 1964-37.2 occurrences. No prior GP ID for that question was present in the supplied earlier index. “Last year” under Jacobson is retained as ambiguous manuscript evidence, not a defensible origin date.

The gamma-function aside remains F. Stronger searches explicitly included `Elashvili "gamma" "Frobenius"` and `"Elashvili" "binary cubic" gamma`; they found the Frobenius classification and related representation literature, but no exact function. The original short paper contains no gamma formula. No orphan research claim is inferred from this failure.

### Cartier, nonstandard analysis, and surreal arrows

15. **Cartier, Bourbaki exposé 580.**
    <https://www.numdam.org/item/SB_1981-1982__24__21_0/>
    <https://www.numdam.org/item/SB_1981-1982__24__21_0.pdf>
    Title page confirms Pierre Cartier as speaker in **November 1981**; Astérisque 92–93 (1982), pp. 21–44 is the publication. Introduction, §2 nos. 3–4, and §5 nos. 21–23 were read; the pages containing the zero-one assumptions and phase diagrams were viewed as images. The exact measure assumptions are values **zero or one**, normalization, and finite additivity. This makes the intended codomain `{0,1}`, not merely `[0,1]`. The van der Pol/Rayleigh relation, reduced branches and matched relaxation cycle are explicit in §5. The manuscript’s broad limit question is indexed narrowly enough to state a verified answer, without importing unspecified rates or canard claims.

16. **Conway (1976), opened later-edition excerpt.**
    <https://sites.math.rutgers.edu/~zeilberg/EM13/onag1.pdf>
    The available PDF is a scanned excerpt from the 2001 second edition, not the complete 1976 first edition. This limitation remains in the bibliography. The first-edition identity comes from the cumulative verified record and the primary modern survey. No claim to a complete reading of Conway’s book is made.

17. **Gonshor (1986), publisher record and contents.**
    <https://www.cambridge.org/core/books/an-introduction-to-the-theory-of-surreal-numbers/312AE504A3E88E804054BFB390446374>
    DOI 10.1017/CBO9780511629143. Definition, operations, reals/ordinals and normal forms are Chapters 2–5. Full book not read in this run. The bibliography’s annotation was updated to distinguish this run’s metadata inspection from any fuller reading recorded in the supplied cumulative file.

18. **Mantova–Matusinski, primary survey preprint.**
    <https://arxiv.org/pdf/1608.03413>
    <https://arxiv.org/abs/1608.03413>
    §§2.1–2.3 were read for sign expansions, order, field operations, ordinals and infinitesimals. First preprint 11 August 2016, revised 23 October 2016; proceedings publication 2017. The finite halving rule was independently checked by a simplest-dyadic-cut implementation. Infinite blocks are interpreted via canonical cuts, not as real limits. A double hat without an ordinal length remains ambiguous; it is not silently assigned a unique transfinite operation.

### The Krichever fragment

19. **Krichever (1983), full 1985 English translation.**
    <https://www.math.columbia.edu/department/krichever/pdfs/1980-1984/1983-NEAEC0.pdf>
    <https://www.math.columbia.edu/department/krichever/pubs.html>
    <https://www.itp.ac.ru/en/persons/krichever-igor-moiseevich/>
    Original Russian survey: Itogi Nauki i Tekhniki 23 (1983), 79–136. Inspected translation: J. Soviet Math. 28(1) (1985), 51–90. §1.3, equations (1.91)–(1.94), defines `G(Gamma,z)` as an infinite-dimensional **algebra** of matrices with prescribed exponential singularities, and supplies sigma kernels. This is a close but partial identification of the ascending union and formula. The notebook never specifies a group law, a Lax equation, or a Peierls Hamiltonian. Those are not filled in from the later survey.

20. **Brazovskii–Dzyaloshinskii–Krichever (1982), full original translation.**
    <https://www.math.columbia.edu/department/krichever/pdfs/1980-1984/1982-DPMWES.pdf>
    Soviet Phys. JETP 56(1), 212–225, submitted 9 February 1982. The collaborator names and broad Peierls context were checked. This is **thematic only** as a match to the notebook formula. The English title page itself prints “N. E. Dzyaloshinskii,” but the original and Landau Institute bibliographic record identify I. E. Dzyaloshinskii; the normalized entry records this discrepancy in its annotation. “Брозовского” is a faithful manuscript spelling with the bibliographic identification Brazovskii, not a scan reading silently overwritten.

## Verification files and scope

`verify_annotations.py` computes the A3 Shapovalov matrices directly from gl4 commutators on PBW monomials. It uses Dynkin highest weight `(-2,2,-2)`, weight difference `(2,3,2)`, and the directions `(1,1,1)`, `(1,-2,3)`, `(3,-2,1)`. It compares elementary-divisor orders obtained by rational power-series elimination modulo t^5 with independent exact rational ranks of block matrices modulo t, t², t³, t⁴. Stable nullities certify that no unobserved higher layer remains. The second non-dominant direction checks the Dynkin-diagram-reflected case. This is a reproduction of an already published counterexample, not a new C/D development.

The same script checks Cauchy determinant signs at sizes 1–5 plus a repeated-row edge case, differentiates the Rayleigh equation and verifies the inverse transformation symbolically, checks an explicit full-rank Kirillov pairing for the binary-cubic example, and compares all 511 finite sign sequences of length at most eight by two independent constructions. The saved JSON and text output are the reproducible evidence. An initial exact-rational-function elimination was stopped because intermediate expressions grew unnecessarily; the finite-precision DVR algorithm preserves all needed orders and is checked independently by ranks.

No C or D item was created in this batch. The items marked F are the cancelled/unspecified all-Kac–Moody extension and the unnamed gamma function. The Krichever fragment is treated as partial identification with medium confidence, not as an unbounded lost theorem. The supplied source and later publications are always kept separate from the companion’s explicit reconstructions.
