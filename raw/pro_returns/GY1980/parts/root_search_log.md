# Root research ledger

Status date: November 2026. These are research routes and verification levels, not an exhaustive bibliography of each subject.

## Archive and boundaries

- Opened https://old.mccme.ru/gelfand/notes/all-links.html. Its three consecutive entries for Cherednik, I. M. Gelfand, and Khovanskii between 16 and 23 February 1981 are incorrectly dated 23-Feb-91. The actual P000960 heading is 23/II/81. These are records 510--512; omission from the supplied year manifest follows the catalog's decade error. Added all three, retaining original record identifiers and manuscript order (Gelfand before Cherednik on their shared page). Individual record-page retrievals failed; the master catalog and attached scans, rather than imagined successful record-page access, support the correction.
- Read the supplied earlier index: orphan P000916 is the previous year's collective-equations continuation, already covered by 1979-488.1--.7. It is accounted for as boundary material, not counted again as a 1980 talk.
- Inspected all five Novikov scans P000944--P000948 and compared both transcriptions. His actual heading is P000944; the manifest's P000942--P000950 range overlaps the preceding Beilinson and following MacPherson material.

## Record 506: Novikov

Searches used English and Russian title variants, author bibliographies, Math-Net and author-hosted PDFs. Useful route: Novikov/Dubrovin magnetic Bloch -> the two 1980 papers -> the 1981 Novikov continuation.

- Math-Net https://www.mathnet.ru/eng/dan43820: verified 253(6),1293--1297, received 15 April 1980.
- https://people.sissa.it/~dubrovin/Papers/1980/dubrovin_novikov_1980_dan.pdf: full text read, Sections I--IV, equations (3)--(16), theorem (a)--(b). This already proves the ground-state construction and positive-flux multiplicity before the seminar. It also distinguishes charge 2e from e and gives crystal cells about 10^-16 cm^2.
- https://people.sissa.it/~dubrovin/Papers/1980/dubrovin_novikov_1980_jetp.pdf: full text read, especially Sections 2--4. September 1980 issue, received 23 February 1980; translated copy bears a 1981 copyright. Do not move the first result to 1981 merely because of that copyright.
- https://homepage.mi-ras.ru/~snovikov/71.pdf: full text read. Received 2 December 1980, one day after the talk. Section II Lemma 1 says rank N and first Chern number 1. Section III distinguishes codimension three at fixed quasimomentum from codimension one after two quasimomenta vary. Publication metadata cross-checked at https://www.itp.ac.ru/en/publications/1981/.
- APS DOI pages opened for Brown (1964), 10.1103/PhysRev.133.A1038, and Zak (1964), 10.1103/PhysRev.134.A1602. Metadata/abstract verification only for these originals; the formulas were checked in the 1980 full text.
- https://arxiv.org/abs/cond-mat/9411052 and its PDF: read noncommutative Brillouin zone/observable algebra sections and the stated Hall theorem. This is a thematic later framework, not evidence that Gelfand's last, unspecified complex/parabolic prescription was implemented exactly.
- No exact target was recovered for the one-dimensional constant-electric-field aside or the final regularization. They are F, not D. The bare instruction “describe the spectrum” is also a program without a determinate invariant.

## P000970: bounded curve development and independent verification

- Full Dixmier 1968 article opened at https://www.numdam.org/item/BSMF_1968__96__209_0.pdf. Relevant exact source: Lemma 5.4, Proposition 5.5, Remark 5.6 (pp. 221--223), not the unrelated endomorphism question in Section 11.1. Reused cumulative key `dixmier1968weyl`.
- https://arxiv.org/abs/1107.3356 and PDF: first submitted 18 July 2011; Theorems 2--3 and genus-two Example (a), PDF p. 11, read. Publisher https://link.springer.com/article/10.1007/s00222-013-0486-8 confirms online publication 19 October 2013 and Inventiones 197(2),417--431 (August 2014). The key preserves the preprint year while the entry records the journal year.
- https://arxiv.org/abs/1606.01346 and PDF: first submitted 4 June 2016. Read Theorem 1, its parameter-map proof and the appendix. The result concerns a **fixed generic** genus-two spectral curve. It does not assert every special genus-two curve. Published metadata opened at https://kci.go.kr/kciportal/landing/article.kci?arti_id=ART002264550: Bulletin of the Korean Mathematical Society 54(5),1669--1675 (2017).
- Full Makar-Limanov 2021 paper opened at https://www.emis.de/ft/25242. Theorem 1.1 and proof: rank-one centralizers in the polynomial first Weyl algebra embed in K[z]. This does not automatically apply to every rational-coefficient operator or to an arbitrary commutative subfield of the division ring.
- Broad and exact-phrase searches in both search engines: “Gelfand curves Weyl embedding”, “function fields Weyl division curves”, “Gelfand algebraic curve embedding”, “Weyl algebra every curve”, “Weyl arbitrary algebraic curve”, “Weyl skew field curve”, “any algebraic curve Weyl”, “поле любой кривой Вейля”, “алгебры Вейля кривой гипотеза”. A recent-publication pass also covered 2024--2026. Hits primarily concern higher-genus examples, Berest's different orbit conjecture, and the different Gelfand--Kirillov/Dixmier conjectures. The later exact-title search found Oganesyan (2016/2018), which settles all genus-two standard quintics; no checked result settles the exact all-genera function-field quantifier. This is a bounded search limitation, not proof that no such result exists.
- Exact coefficient computation in `code/check_weyl.py`: corrected Dixmier pair, nonzero notebook commutator, genus-two pair, spectral polynomial and discriminant. Rechecked by a separate action-on-polynomials implementation at a=-2,0,1,3 on all monomials through degree 20. Outputs are included. The genus-two family is existing Mironov mathematics; the chapter's contribution is a transparent reconstruction, countercheck and reproducible certificate, not a claim of a new general realization theorem.

## Negative or unused leads

- Direct record-510/511/512 pages were inaccessible in the web reader; master catalog and scans suffice for the concrete provenance decision.
- One old author-homepage endpoint timed out; publisher/arXiv/KCI pages supplied the relevant metadata instead.
- A mistyped Springer DOI ending 0482-1 did not resolve and was not cited; the verified Mironov DOI ends 0486-8.
- Search snippets and third-party aggregators were used only to find primary sources; technical conclusions rest on the opened primary text, attached notebook, or explicitly marked computation.

## Late verification that changed a classification

Oganesyan, arXiv:1608.05146 (18 August2016), full PDF and publisher DOI10.1007/s10688-018-0229-0 opened. Theorem3(2), preprintp5, uses the union of two rational-operator families to realize every monic quintic, with arbitrary coefficients. The genus-two item was changed from provisionalC toB; no open classification question was invented to preserveC. This is a material improvement over stopping at the generic Davletshina--Mironov theorem. All genus≤2 fields are positive subcases of the wider Gelfand conjecture.

Ivlev2026, https://www.mathnet.ru/eng/faa4335, publisher metadata and abstract checked: particular rank-two trigonal genus-three examples. Full text embargoed until2027, so the chapter does not assert the coefficient class.

Second-check findings: Mironov preprint Example(a) displayed M is nine greater than the centered operator satisfying its displayed quintic; the certificate explicitly subtracts9. The notebook formal expression A=L+xL^-1 has cube differential part L³+3xL+6D, not the corrected3D; adding the next formal-square-root term fixes that differential part. All final exact checks passed.
