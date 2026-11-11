# Early-record evidence and handoff

Status date: **9 November 2026**. Scope: records **272, 273, 274, 275, 280, 281** only. Files were saved incrementally after each record. No chapter assembly, PDF build, or final upload was performed by this agent.

## Saved counts and scope

| Record | Actual source boundary | Speaker | Items | Classes |
|---|---|---|---:|---|
| 272 | P000450–P000451 | A. M. Gabrielov | 8 | 8 E |
| 273 | P000452–P000453 | Yu. I. Manin, explicitly a retelling | 7 | 7 E |
| 274 | P000454–P000455 | D. A. Kazhdan | 8 | 8 E |
| 275 | P000456–P000458 | A. M. Gabrielov | 9 | 9 E |
| 280 | P000468 to the tolerance question on P000470 | L. N. Vasserstein | 20 | 16 E, 4 A |
| 281 | Derived-category heading on P000470 to before Buchstaber on P000471 | D. A. Kazhdan | 4 | 4 E |

Total: **6 talks, 56 items, 52 E, 4 A, one problem, 15 references, 25 correction/ambiguity/provenance rows**. By speaker: Gabrielov 17, Manin 7, Kazhdan 12, Vasserstein 20. By area: Hodge structures/period domains 17, local-field tree 7, local ramification 8, algebraic K theory 20, derived categories 4. Seven items are assessed false as written, 18 correct with missing hypotheses, and 31 correct. Development: 43 none, 12 annotated, one developed in the corrective appendix.

The four A occurrences are 1972-280.9 (the explicit stabilization implementation), .13 (cone vanishing in this model), .15 (the idempotent nonunital commutator extension), and .20 (the exact published tolerance assertion). The first three distinguish the speaker's subsequent implementation or extension from the older ideas it uses. The last distinguishes publication from correctness.

## Source handling and boundaries

`CHAPTER_FORMAT.md` was read first, followed by the task, English/Russian source, prior occurrence index, and cumulative bibliography. The Russian source is authoritative for what the notes say. All mathematically relevant original scans in these record ranges were actually inspected: **P000450 through P000458, and P000468 through P000471**. The original page images decide the following important points.

- P000450 has the dated Gabrielov heading. P000449 is preceding material and is not allocated to record272 just because the catalogue's linked range includes it.
- P000452 explicitly says “пересказ”. The cancelled equal-characteristic alternative is not treated as uncancelled lecture content.
- P000453 explicitly requires the initial normalized inclusion of lattices. The later unqualified quotient variant is interpreted only after scaling to an inclusion.
- P000454 uses `G_i={g: g(x)-x in m_L^i for all integral x}`, so notebook `G_0=G`, `G_1=inertia`, `G_2=wild inertia`. This shift is intentional, not a transcription correction.
- P000455 has the old phrase translated “weakly ramified” for `G_2=1`; modern tame and modern weak ramification are distinguished in the annotation.
- P000451 really has `Q(F^p,F^{n-p})=0` without `+1`; P000458 writes the correct index. The earlier formula is a faithful mathematical error.
- P000458 really reverses the symmetric/alternating weight parity. The source also specifically says the identity component acts transitively, requiring a connected-component qualification.
- P000458 ends with two bare continuation headings for Manin and Kazhdan, without mathematical content. These are preserved in the talk summary and do not generate invented items or records.
- P000468 really says “any map” of the index set gives a matrix endomorphism. Noninjective maps fail; the published treatment correctly uses embeddings. Its “upper triangular” word and written strict-lower inequality are both visible.
- **P000469 explicitly says the ring has an identity before the homotopy definition of K groups and the five-block proof.** There is no missing-unit correction here. The initial nonunital scope must not be propagated past this hypothesis.
- P000469's first source prime in the contiguity definition is a short doubtful stroke, so its correction is filed as ambiguity, not confidently as a faithful mathematical error.
- P000470 has the explicit tolerance task and then a genuine speaker change to Kazhdan. P000471 completes the derived-category item before Buchstaber's heading.

## Opened primary sources and exact verification

Every reference in `references.bib` has an opened URL and `note={verified}`. “Verified” does not imply that a paywalled historical theorem was read: metadata-only checks are explicitly distinguished below and in the BibTeX annotations. Existing cumulative keys were reused for the same works. The cumulative bibliography itself contains duplicate entries; this batch has no duplicate keys.

| Key | Opened URL and locator | Verification / chronology |
|---|---|---|
| griffiths1968periods1 | https://publications.ias.edu/sites/default/files/periodsofintegralI68.pdf ; author record https://publications.ias.edu/pg/paper/179 | Full text: §1 equations (1.7)–(1.15), polarization parity, Hodge decomposition and Weil operator. Author record confirms AJM90 (1968),568–626. This is not the different 1969 rational-integral paper. |
| griffiths1970periods | https://publications.ias.edu/sites/default/files/periodsofintegral.pdf | Full text: §2,232–235, equations(2.1),(2.3), connection/transversality/period-domain fibration. First page distinguishes lecture29Aug1968, receipt18Sep1969, March1970 issue. |
| mumford1972degenerating | https://www.numdam.org/item/CM_1972__24_2_129_0.pdf | Full primary paper: introduction130–131, §1 tree and neighbours; final printed page174 says received16-III-71. Published1972. Its uniformization results are not imported into Manin's notes. |
| serre1977arbres | https://smf.emath.fr/publications/arbres-amalgames-sl2-3e-edition | Official metadata: original Astérisque46 (1977), based on course1968/69 with Bass; ChapterII local-field tree. Current product is third edition, so no claim that third edition itself dates1977. Exact tree content independently read in Mumford. |
| tate1967pdivisible | https://www.mathnet.ru/rus/mat500 ; full translation https://www.mathnet.ru/php/getFT.phtml?jrnid=mat&option_lang=rus&paperid=500&what=fullt | Metadata and Russian full text; exact target§3, Matematika13(2)(1969),3–25, translated by Manin, from English proceedings1967,158–183. https://link.springer.com/book/10.1007/978-3-642-87942-5 verifies1966 conference/1967 volume and title. No unstated Cp theorem added. |
| serre1979local | https://link.springer.com/book/10.1007/978-1-4757-5673-9 | Publisher metadata, copyright1979, ChapterIV61–79. Original French1962 date checked in Milne bibliography. Historical chapter not fully read; exact theorem proof verified in Milne. |
| milne2020ant | https://www.jmilne.org/math/CourseNotes/ANT.pdf | Full author text v3.08 (19July2020); printed130–131, Lemma7.57, Theorem7.58, Corollary7.59 and following tame paragraph. Exact residue/tame/higher quotient maps and solvability checked. |
| johnston2012weak | https://arxiv.org/abs/1204.2133 ; https://arxiv.org/pdf/1204.2133 | Primary record/full PDF, §1p1: modern weak means conventionalG2=1, tameG1=1. First posted10Apr2012; revised16Sep2014. Used for terminology only. |
| vaserstein1973foundations | https://www.mathnet.ru/eng/rm4870 ; https://www.mathnet.ru/php/getFT.phtml?jrnid=rm&option_lang=eng&paperid=4870&what=fullt | Both original pages read. Definitions including left-translation simplices; five theorem blocks. Receipt14Nov1972, exactly the day after record280. |
| vaserstein1976foundations | https://www.mathnet.ru/eng/rm3762 ; https://www.mathnet.ru/php/getFT.phtml?jrnid=rm&option_lang=eng&paperid=3762&what=fullteng | Full English primary text: §§1–6; §11 definition and Remarks(b,c),110–111; §13,112–114; §15,117–118; §18,122–123. Received26Feb1975; published1976. Exact tolerance assertion at §11Remark(c),p111. |
| volodin1971extraordinary | https://www.mathnet.ru/eng/im2061 ; https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=2061&what=fullteng | Metadata/full paper opened; §1 module-flag simplicial setup. Received27July1970/published1971. Vaserstein1976Theorem15.2 explicitly credits Volodin for path/Steinberg theorem. Do not equate its broader flag formulation word-for-word with every later coordinate model. |
| milnor1972introduction | https://press.princeton.edu/books/paperback/9780691081014/introduction-to-algebraic-k-theory | Publisher metadata only, publication21Jan1972. No claim to have read a theorem solely from this page. Used for chronology; mathematical statements checked in Weibel. |
| weibel2013kbook | https://sites.math.rutgers.edu/~weibel/Kbook.html ; https://www.math.rutgers.edu/~weibel/Kbook/Kbook.III.pdf | Author page and full ChapterIII: Whitehead1.3.3; Steinberg5.1; universal extensions5.3; recognition5.4; Kervaire–Steinberg5.5 and proof. |
| hartshorne1966residues | https://link.springer.com/book/10.1007/BFb0080482 | Publisher/contents only: Harvard1963/64, publication1966, ChapterI19–84. The exact cancellation result was read in Stacks, not inferred from contents. |
| stacks2026foundations | https://stacks.math.columbia.edu/tag/05R1 ; https://stacks.math.columbia.edu/tag/05RR | Lemma13.5.5 and its mapping-cone proof; Lemma13.11.2, Definition13.11.3, Remark13.11.4. Includes size qualification for unbounded derived categories. Cumulative project key reused. |

For parent retrieval/citation convenience, current-session source refs include `turn78view0`/`turn83view3`/`turn62view3` for Vaserstein1976, `turn85view2` for1973, `turn83view0` for Weibel's central extension theorem, `turn52view3` for Milne, `turn102view0` and `turn102view1` for Stacks, `turn104view0` for Griffiths1968 metadata, `turn106view2` and `turn120view0` for Mumford, `turn106view0` for Johnston, `turn117view0` for the1966Tate conference volume, and `turn102view2` for Hartshorne. Earlier full-text refs were `turn14view2` (Griffiths1968), `turn34view0` (Griffiths1970), `turn19view4` (Volodin), `turn33view0` (Tate translation). The parent independently opened and read the decisive Vaserstein passage as its `turn41view0`.

## Tolerance question: exact published match, counterexample, and audit

The notebook's definition has a single common translation and a single coordinate order for the entire finite set. The published definition in §11 has the same requirement in the right-translation convention; Remark(b) explicitly relates the conventions by inversion. Remark(c) asserts the pairwise-to-simplex implication and says it is not used in the paper. Thus the problem is **A, publication_match exact, literal_correctness false as written**, not D.

In ordinary coordinates take `a=I+E12`, `b=I+E23`, `c=I+E31`. The left relative matrices are:

- `a^-1 b = I-E12+E23-E13`, ordered1<2<3.
- `a^-1 c = I-E12+E31`, ordered3<1<2.
- `b^-1 c = I-E23+E31-E21`, ordered2<3<1.

The first two simultaneously require1<2<3<1, so the triple is not a simplex. All decisive coefficients are±1, nonzero in any nonzero unital ring, including characteristic2. Stabilization only adds isolated coordinates. The appendix gives the equivalent right-coset computation explicitly as well.

`development.tex` contains three fully proved, explicitly marked results: the acyclic-support criterion for arbitrary finite vertex sets, the universal-ring three-vertex counterexample, and minimal coordinate rank. Rank2 is independently checked by translating a base vertex toI; two nonidentity vertices of opposite triangular orientations have a relative quotient with both off-diagonal entries nonzero, even if their product is zero. Hence a pairwise-adjacent rank2 set uses one common orientation and is a simplex.

`check_tolerance.py` uses exact integer and modular arithmetic and enumerates all coordinate permutations. `tolerance_output.json` contains **30 parameter cases**: coefficient ringsZ,F2,F3,F5,F7; dimensions3,4,5; both left/right models. Every pair is a simplex and no triple is a simplex in all cases. This computation was rerun. The parent separately wrote `batches/root/independent_flag_check.py` and audited24 finite-field cases independently, agreeing in every case. It independently confirmed the general support-cycle proof and the rank2 minimality argument. No finite evidence is extrapolated as the general-ring theorem.

Targeted searches included Vaserstein/Vasershtein Foundations and his publication list, Volodin1971, “Vaserstein tolerance K-theory”, and “Volodin flag counterexample simplicial”; the last two were checked with the stronger search engine, including recent indexing. These searches found the exact published assertion and modern definitions, but did not settle the history of a later erratum. **No priority claim is made for the counterexample and no claim that an erratum does not exist.** The source itself says the assertion is unused, so no inference against the K-theory comparison theorems is warranted.

The strongest valid replacement is the common acyclic-support criterion. There is no remaining open mathematical question in the literal notebook assertion. A further bibliographic check for past corrections is possible but is not packaged as a manufactured research problem.

## C/D review and earlier links

No C or D item survives source identification in these six records. Hodge and derived-category exposition, the lattice tree, and local ramification are all established before the talk. The specific K-theory methods and extension are published in the speaker's Foundations papers. The one apparent development candidate is published, so the appendix is transparently a correction of A, not an orphan result smuggled into D.

Hodge links: 1969-182.2 and1971-251.1–5. K-theory links:1971-253.1,.4,.5,.14;1971-256.1–3;1971-257.2. GP-1971-20 (universal elementary relations) and GP-1971-21 (comparison of early constructions) were checked; this talk gives exposition/identifications and does not repeat their exact research questions, so their identifiers are mentioned for context rather than spuriously assigned to a new question. GP-1972-101 is new and uniquely attached to1972-280.20.

## Remaining limits and website presentation

The brief A.Weil allusion in Manin's notes cannot be identified to a particular work from the supplied wording. It is explicitly left unresolved inside a mathematically identified analogy item; no invented reference or extra F theorem is added. The exact historical Hartshorne and Serre book chapters were not fully accessed, but each mathematical claim is checked against an opened modern author/project source. These are disclosed verification limits, not gaps in item coverage.

For a reader landing on these talks, show the scanned page boundary and modern statement first, with the correction beside the exact literal wording. The website particularly needs distinct display fields for **publication provenance** and **literal correctness**: an A label must not imply that the published tolerance statement is true. Link the repeated Hodge definitions across records272/275 and back to1969/1971; expose the ramification index-conversion table; link the tolerance item directly to the common-order definition, exact1976passage, full proof, and computation. Model/convention fields for unital scope, circle versus multiplicative coordinates, and left/right cosets would prevent false matches.

## Local validation

The batch passed checks for required schema fields, consecutive occurrence identifiers, exact six-record coverage, dated status fields, unique BibTeX keys, every cited key present in both the item refs list and the bibliography, and bidirectional problem links. No chapter build was attempted, as instructed by the parent. The final assembly process should include the schema files, bibliography, corrections, proof appendix and two computation files, not the intermediate page extracts or authoring script unless desired for provenance.

## Additional independent cross-batch review requested by the parent

This section records read-only review of other agents' data. It does not change this batch's six-record scope or its counts. All proposed edits were sent to the parent, who owns the affected files.

### Records 290, 292 and 291

The Lomonosov argument in the root data was checked step by step. The corrected scaling separates the compact image from zero, the finite partition of unity has positive denominator, and the fixed point belongs to the ball away from zero. The finite-dimensional eigenspace occurs under the temporary transitivity assumption; the final invariant-subspace theorem does not promise a finite-dimensional subspace. The locally convex version explicitly uses completeness, Hausdorffness, and relative compactness of the image of a zero-neighbourhood. No further mathematical correction was identified in these reconstructed statements.

For Henkin 292.3 the clause “F(U) is closed in Omega” should be replaced by “F(D)=F(U) intersect Omega is a closed complex submanifold of Omega.” The open neighbourhood U extends across the boundary, so F(U) is not itself a subset of Omega. The local Stein neighbourhood can be chosen with closure D holomorphically convex in U. This aligns with the precise hypotheses of Forstneric's Theorem 1, independently opened at https://users.fmf.uni-lj.si/forstneric/papers/2026FH.pdf, p.1 (`turn135view0`). The parent accepted the correction. The other five Henkin statements were checked for domain, regularity, transverse extension, norm and compactness hypotheses.

Berezin P484/P486/P487 were independently inspected as images. They confirm the source's conjugated test function, omitted h in the annihilation operator, reciprocal cross-ratio, positive Hilbert weight and positive disk-kernel exponent. The root's corrected Fock ordering, h/4 Berezin heat transform, h/8 Weyl midpoint, normalized overlap, negative weight and disk parameter beta=2/h>1 are consistent. The operator-symbol trace identities and scalar convexity inequality were independently read in Berezin1972, §§1–2, https://www.mathnet.ru/php/getFT.phtml?jrnid=im&paperid=2347&what=fullteng (`turn135view2`). The 1974 discussion of the nonhomogeneous obstruction was read in §2.8, printed1133, https://www.math.stonybrook.edu/~leontak/Berezin-Quantization.pdf (`turn135view1`).

Recommendation accepted by the parent: reclassify 291.19 from C to F and remove GP-1972-401. The notebook does not determine the analytic domain class, symbol algebra, admissible parameters, convergence requirements or allowed kernel modifications. A precise formal unital deformation theorem is contextual comparison; it does not partly resolve a uniquely recovered analytic problem. The parent also corrected the homogeneous-domain locator from §4 to §5 and narrowed the compact published match to the classical symmetric cases.

### Bernoulli and p-adic interpolation checks

`independent_audit_checks.py` imports no root code and uses exact rational arithmetic. Its JSON output checks four levels i=0,1,2,3 of k_i=1+2*5^i. The valuation v5(zeta(1-2k_i)-1/3) is respectively1,2,3,4, whereas v5(zeta(1-2k_i)+1/12)=1 throughout. The corrected values satisfy the corresponding congruences. The general argument is continuity on the n=2k congruent2 modulo4 tame-character branch, together with 5^(n-1) tending to zero. Its raw limit is1/3, whereas the constant sequence at k=1 has value-1/12, a difference5/12. Thus 298.8's counterexample is correct; finite calculations supplement rather than prove the limit.

The same script independently checks65 power-sum cases and65 mixed-polynomial triangular systems, degrees0–12 at endpoints0,1,2,5,11. All pass. The first inverse row is B_r/r!, with B1=-1/2, exactly as in300.4. In300.1 the endpoint B_{k+1}(1) is essential: k=0 gives n, including n=0, whereas substituting B1(0) would give n+1. The finite Taylor and Cramer formulas in300.2–.3 are correct. DLMF https://dlmf.nist.gov/24.2 and https://dlmf.nist.gov/24.4, especially24.4.1, were independently opened (`turn140view0`, `turn140view1`).

### Buchstaber's reconstructed C item

The lone C occurrence is287.11. I recommend retaining C with medium confidence and explicit designation as a reconstructed all-degree computation programme. The antecedent of “not done” on P479 is the computation of homotopy groups of the representing space; the subsequent chosen trivialization data identify the smooth refinement with G/O. Thus the target is recoverable, unlike the unspecified analytic category in291.19. The remaining numerical task is to determine all pi_q(G/O), via the short exact sequence from coker J_q to pi_q(G/O) to ker J_{q-1}. The existence of the exact sequence is already E, and no particular presently unknown finite-degree group is invented. Absence of a bounded target prevents selecting this programme for new development, rather than forcing an F identification.

Ranicki's full text, §9.2, Proposition9.21 and table9.22, was independently read at https://webhomes.maths.ed.ac.uk/~v1ranick/books/surgery.pdf (`turn141view1`). Burklund–Isaksen–Xu's introduction and Theorem1.1 were independently read at https://link.springer.com/article/10.1007/s42543-025-00098-y (`turn142view0`, `turn142view2`); these establish the specified82nd/83rd2-primary computations and support only finite progress, not an all-degree answer. This is a review recommendation, not a modification to the Buchstaber batch.
