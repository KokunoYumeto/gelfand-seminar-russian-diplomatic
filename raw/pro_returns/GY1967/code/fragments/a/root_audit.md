# Independent audit of the root fragment

Reviewer: `/root/records_131_140`. Date: 9 November 2026.

Scope: `fragments/root/items.json` and its supporting primary texts, as read during final integration; additionally `output/GY1967/GY1967_development.tex`. This audit does not edit the root fragment. Findings below were sent to the parent while the audit was in progress, so the final integrated files may already incorporate them.

## Required chronology correction: 1968-172.6

The displayed classification E is not supported by the argument that Griffiths–Schmid's manuscript was received on 3 April 1969, before Kirillov's 21 April talk. Receipt establishes existence, not public circulation. The author of this seminar report is neither Griffiths nor Schmid. The exact all-chamber, sufficiently-regular L² vanishing result is Theorem 7.8, pp. 293–294, of the eventual Acta paper, whose print date is 23 January 1970. The note's simple-root condition also needs the every-root repair already supplied by the root fragment.

There are genuine earlier publications, but their scope matters:

- Schmid's January 1968 PNAS announcement, pp. 56–57, assumes an antidominant weight relative to a fixed positive system. Page 57 announces concentration of L² cohomology in degree `s = dim_C(K/H)` for sufficiently high tensor powers of the chosen line bundle. This is a published restricted antecedent. Changing the positive system changes the complex structure, so it cannot silently establish the same fixed-domain theorem for every chamber. Theorem 2 on p. 56 concerns ordinary sheaf cohomology; it must not be mistaken for the general L² theorem.
- Griffiths's August 1966 PNAS announcement, §3 p. 415, proves vanishing on compact quotients. Its §4 p. 416 labels L² concentration on the noncompact domain a speculation. Thus it does not supply the missing full antecedent either.

**Recommendation:** classify the full recorded all-chamber vanishing statement B, explicitly mention the restricted Schmid 1968 antecedent, and retain the separate B for irreducibility in 172.7. Alternatively split the restricted antecedent and the full later theorem. No unverified claim of public circulation should remain.

## Earlier source for the degree formula: 1968-172.8

E is defensible here as the previously used degree convention. Griffiths 1966, §2 p. 415, equations (2.1), defines the two signed root counts: positive noncompact roots paired positively, and positive compact roots paired negatively. Their sum occurs as the compact-quotient cohomological degree in §3. Add this earlier exact source alongside Schiffmann 1971 and Griffiths–Schmid. The correction to positive roots and a uniform variable is mathematically appropriate.

The constructions and Borel–Weil–Bott background in 172.1–5 are also pre-existing. A later exposition can verify their content, but its receipt date is unnecessary as an argument for E. The distinctions among compactly supported test forms, completed L² spaces, harmonic forms and reduced cohomology in 172.4 are sound. The F classification for the unspecified decay comparison in 172.9 is appropriately cautious.

## Smooth versus PL finiteness: 1968-171.1 and 173.1

Hsiang–Shaneson was communicated 6 January and published March 1969. Theorem A, p. 687, gives **PL** classification by a finite orbit set. Remark 2, p. 688, says the homotopy tori are smoothable. The exact Moscow smooth-finiteness report dated 22 April follows both seminar dates. It therefore cannot alone establish E.

The missing bridge was subsequently located in pre-1969 primary machinery. Hirsch 1963, Theorems 3.1 and 4.2, gives the skeleton obstruction theory with sphere-smoothing groups as coefficients; Theorem 5.1 identifies these with the relative homotopy groups of BPL and BO. Concordance implies diffeomorphism by Theorem 1.1(a), strengthened in Theorem 4.1. For a finite triangulation, finitely many obstruction-theoretic choices in each of finitely many degrees give finitely many concordance classes once the coefficient groups are finite. High-dimensional finiteness is Kervaire–Milnor; Cerf's 1968 result supplies the low-dimensional Gamma4=0 input. This is an explicit deduction from the cited machinery, not a verbatim finiteness theorem in Hirsch's note.

**Final recommendation, adopted by the parent: retain E**, while stating PL finiteness plus finite smoothing fibres separately. Hambleton 2006 p. 2212 was also reopened and visually checked; it records PL classification and smoothability, but does not itself state this finite-smoothing bridge. At the parent's request, bibliography entries `hirsch1963obstruction` and `cerf1968gamma4` were appended directly to the root bibliography. Cerf's publisher metadata was checked; the original full proof was not read.

## Hörmander, matrix geometry and topology

Hörmander's December 1968 publication precedes the March 1969 talk. The E chronology in record 168 is sound. The root's differential-operator Riesz-mean statement is supported by Theorem 4.5 and pp. 215–216: the finite expansion has the stated remainder exponent `(n−1−α)/m`. The extra rapidly decreasing term occurring for general pseudodifferential operators does not invalidate the root's more restricted differential-operator formulation. The leading averaged Weyl coefficient is correctly multiplied by `m/(m+n)`.

One locator should be corrected: the off-diagonal estimate in 168.3 is **equation (5.4), p. 215**, not (5.2). The sphere multiplicities and the jump obstruction to an unsmoothed full expansion in 168.4–5 are correct.

No mathematical defect was found in the checked Davis/Au-Yeung statements: the complex Hermitian-pair criterion uses convexity correctly, the real two-dimensional exception is separated, and the Gram-matrix transformation is consistent with the declared inner-product convention. The high-dimensional s-cobordism range, distinction between Laurent units and the Whitehead quotient, stable torus splitting, and distinction between rational Pontryagin vanishing and stable normal triviality are also handled properly. These checks are mathematical reviews; they do not claim independent proof-level verification of every cited topology publication.

## Bounded Weyl development

I independently read the complete bounded proof. No defect was found. The finite coefficient argument and generalized Vandermonde identity justify the formal pseudodifferential division ring; the geometric inverse is well defined in its descending order filtration. The centralizer argument works for positive and negative powers in characteristic zero. The normalizer, explicit inverse, and conjugation action retain the correct left coefficient convention. Polynomial preservation in both directions is correctly reduced to affine substitution and a polynomial shear.

The scope is appropriately limited: equality of the coordinate fields is assumed, not deduced for arbitrary division-ring automorphisms; a commutator-one pair is not assumed to generate the division ring. The proof explicitly disclaims novelty and does not treat finite symbolic checks as proof. The more detailed independent review in `fragments/c/proof_review.md` reaches the same conclusion. This audit did not add redundant tests.

## Primary-source audit and reopening information

1. Griffiths–Schmid, *Locally homogeneous complex manifolds*: <https://publications.ias.edu/sites/default/files/locallyhomogeneous.pdf>. Opened/read relevant introduction, Theorem 7.8 and references. Tool refs `turn148view0`, `turn149view0`, `turn149view1`, `turn149view2`, `turn156view1`. Receipt date is printed at the end. A local full-text copy is `work/literature/griffithsschmid1969locally.txt`.
2. Schmid, PNAS 59 (1968), 56–59: <https://www.pnas.org/doi/pdf/10.1073/pnas.59.1.56>. Initially opened as the complete four-page PDF and read (`turn151view0`); later reopens redirected to a cookie page (`turn155view1`, `turn156view0`). Metadata and the thesis-summary note: <https://pubmed.ncbi.nlm.nih.gov/16591593/> (`turn151search1`, `turn160search0`) and <https://pmc.ncbi.nlm.nih.gov/articles/PMC286000/> (`turn151search0`, `turn160search1`; the later direct open `turn160view0` encountered a browser check). The decisive theorem evidence came from the successful original PDF, not metadata.
3. Griffiths, PNAS 56 (1966), 413–416: <https://publications.ias.edu/sites/default/files/someresultsonlocally.pdf> (`turn157search12`, `turn158view0`). Entire four-page primary note read, especially §§2–4. DOI: <https://doi.org/10.1073/pnas.56.2.413>. Metadata date: <https://pubmed.ncbi.nlm.nih.gov/16591369/> (`turn157search0`). Suggested bibliography key: `griffiths1966locally`.
4. Hsiang–Shaneson, *Fake tori, the annulus conjecture, and the conjectures of Kirby*: <https://webhomes.maths.ed.ac.uk/~v1ranick/papers/hsiashan1.pdf> (`turn148view1`, `turn155view0`). Primary text read, specifically Theorem A and the smoothability remark; full text also shows the surgery-method outline.
5. Hörmander, *The spectral function of an elliptic operator*: <https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6063-11511_2006_Article_BF02391913.pdf> (`turn148view2`). Theorem 4.5 and pp. 214–216 checked against the local full text `work/literature/hormander1968spectral.txt`.
6. Hambleton, *The classification of homotopy tori*, Oberwolfach Reports 2006, p. 2212: <https://ems.press/content/serial-article-files/46065> (`turn161view0`, `turn162view0`, `turn162view1`, `turn162view2`, `turn163view0`; actual page screenshot `turn163view1`). Full one-page report read.
7. Hirsch, *Obstruction theories for smoothing manifolds and maps*, Bulletin AMS 69 (1963), 352–356: <https://webhomes.maths.ed.ac.uk/~v1ranick/papers/hirscho.pdf> (`turn164search9`, `turn165view0`). Complete primary note read. The named theorems supply the finite-skeleton bridge above.
8. Cerf, *Sur les difféomorphismes de la sphère de dimension trois (Gamma4=0)*, LNM 53 (1968): <https://link.springer.com/book/10.1007/BFb0060395> (`turn168search0`, `turn169view0`) and first-chapter metadata <https://link.springer.com/chapter/10.1007/BFb0060396> (`turn171view0`). Publisher print year/title and chapter contents verified. No claim to reading the full proof.

Searches in this audit used the exact Schmid and Griffiths article titles and the tensor-power hypothesis, then followed the two earlier-announcement references in Griffiths–Schmid. Unopened search leads are not used as theorem evidence. The audit reports what these sources establish; it does not prove that no other pre-April-1969 circulation ever occurred.

Follow-up smoothing searches used Hirsch/Mazur/Munkres with “finitely many” and “PL/O”, then the exact Hirsch title and Cerf's Gamma4 result. Search-only secondary explanations were used to find the original works, not as proof-level citations. The parent adopted B for 172.6, the earlier Griffiths citation for 172.8, and equation (5.4) for 168.3. No root JSON or authoring script was edited by this reviewer.
