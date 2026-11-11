# Winter records: research and verification log

Audit date: **10 November 2026**. Scope: records 452–456 and the explicitly added, source-established partial record 457. This log describes work performed during the task; the companion generator itself does not browse or inspect images.

## Source reading and boundary decisions

The chapter format and complete task prompt were read before authoring. Every line of the assigned source, P812–P825 and P829, was read in **both** the English and Russian files. The fifteen corresponding scanned pages were visually inspected, with the formulas, ambiguous names, dates and transitions decisive for the mathematics checked against the handwriting. `scans_reviewed.json` records the files, hashes, findings and limits. `coverage_manifest.json` maps every substantive page segment to the occurrence data. It includes the unwrapped paragraphs that lie outside the diplomatic evidence environments; parsing only those environments would omit, for example, the spin-half sentence on P818, the Hamiltonian/contact families on P824 and the period-three example on P829.

The actual lecture boundaries differ from the overlapping catalogue ranges. Record452 is the upper-P812 reading programme and has no mathematical occurrence. Record453 starts at the separate Belavin heading on P812 and ends on P815. Record454 starts with 19/II-79 on P816 and ends with the incomplete line on P820. Record455 is the S. Gelfand report from Manin on P821–P822. Beilinson's record456 occupies only P823; its 26February date comes from the catalogue and preceding dated session, not an independently written date on that page.

P824 establishes a new Fuchs lecture, dated 5March1979. The root editor explicitly authorized treating it as a transparent **fifteenth entry: fourteen commissioned records plus one source-established partial addition**. Its available extent is P824–P825 and P829. P826–P828 are absent. The first evidence wrapper preceding P829 incorrectly says P826, while the `SourcePage` marker, actual filename and inspected scan say P829. Neither this wrapper nor titles in the previous index license reconstruction of missing pages. The record457 catalogue URL was attempted but inaccessible; date/speaker identification rests on the visible source heading. P830 begins the independently dated Ogievetsky lecture, assigned to the spring owner.

`source_provenance.md` gives the exact aliases. The prior index misassigns the P812 ADHM/gauge paragraphs to 1977-451.11–13 and mixes Beilinson, Fuchs and Ogievetsky under 1977-457. Its items1–3 are Beilinson; items4–7 and17–19 are the available Fuchs segments; items8–16 are not supplied as developed statements; items20–25 are Ogievetsky. These are **source-provenance aliases, not historical recurrences in two academic years**.

## Search record and negative identification checks

Search was used for niche mathematical identifications, exact formulas, bibliographic dates and present-status checks. Primary papers, author-hosted papers, publisher records, and author-institution publication lists were preferred. An opened bibliographic page is not represented as a read proof. The exact checked extent and locator for each cited work are recorded below and in its BibTeX `annote`.

The following exact query strings are retained from the available execution record. Earlier topic-directed searches located ADHM, Elitzur, the 1975 bosonization papers, Baxter, higher-spin chains, the cubic R-matrix condition, ambitwistors and Kac. Their precise query wording is not reconstructed retrospectively.

| Exact query | Result and use |
|---|---|
| `Baxter 1973 "III. Eigenvectors" "anu"` | Weak repository results; no accessible PartIII text. |
| `Baxter "1973" "Eigenvectors of the transfer matrix and Hamiltonian"` | Publisher title, abstract and bibliographic data found; direct opens returned403. |
| `"Non-self-dual gauge fields" Green Isenberg Yasskin 1978 462` | Publisher metadata and Yasskin's institutional CV identified the exact1978 paper. The CV was opened; original full text was unavailable. |
| `Cartan prolongation g_k symmetric Hom V g0 Yamaguchi 1993 pdf` | Led to the classical prolongation literature; precise tensor definition was read in Fu–Hwang Definition2.1. |
| `Singer Sternberg On the infinite groups of Lie and Cartan 1965 pdf` | Historical leads only; no claim to have read the full Singer–Sternberg paper. |
| `"An interpretation of classical Yang-Mills theory" pdf Witten` | Exact1978 paper identified at the publisher and Princeton. Institution metadata/abstract opened; full original proof was not obtained. |
| `Baxter "Eigenvectors of the transfer matrix and Hamiltonian" site:anu.edu.au` | ANU PartI was accessible, but PartI was not substituted for the requested PartIII. |
| `"Twistor theory: An approach to the quantisation" 1973 241 315` | Confirmed publisher issue metadata1973,241–315, versus the supplied university scan's1972,241–316 header. The discrepancy is recorded explicitly. |
| `"Eight-Vertex Model in Lattice Statistics" 1971 832 833` | Confirmed1971 announcement, exact APS record and dates. |
| `Belavin Manin Gelfand 1979 algebra quadruples elliptic curve torsion nonassociative` | Only broad later elliptic/Yang–Baxter and algebraic leads; no specified multiplication or exact realization problem matching the notebook. |
| `Belavin Gelfand Maurer Cartan Yang Baxter 1979` | Thematic Belavin–Drinfeld and related material, without an exact formulation matching Gelfand's sentence. |
| `Ландау лагранжиан труп Гельфанд` | Memoir/biographical leads, without authentication of the exact attributed quotation. The notebook remains the evidence for the attribution. |

The final three negative searches yielded leads to Belavin–Drinfeld's1982 classical Yang–Baxter paper, a1985 embedded-elliptic-curves paper, Belavin's publication page and a memoir. Opens were attempted, but their outputs were not retained as read evidence. Those works are **not** cited as resolutions of the unformulated quadruple algebra, SL(2,R) or Maurer–Cartan remarks. Failure to find an exact match is not evidence that a precise open problem exists.

Access limitations encountered: direct ScienceDirect routes for Baxter PartIII, Witten and Isenberg–Yasskin–Green returned403; the CiNii alternative was blocked; a Bytsko institutional PDF timed out, while arXiv succeeded; Yamaguchi's DOI10.2969/aspm/02210413 redirected to an unavailable Euclid route; the Guillemin–Quillen–Sternberg full text was not accessible beyond metadata. The Penrose–MacCallum scan exceeded the browsing renderer's size limit, but the exact university URL was downloaded and inspected locally as page images/OCR. None of these access failures is converted into a classD finding.

## Bibliographic URLs, read extent and chronology

Every URL below was opened or, for the explicitly unverified Baxter PartIII entry, directly attempted. `verified` means that the linked resource was opened; it does **not** mean the full proof was read. The annotations delimit exactly what supports the occurrence's match/verification assessment. All cumulative keys already present in the previous bibliography were retained.

### `atiyahhitchindrinfeldmanin1978instantons`

- URL: https://strings.itp.ac.ru/Papers/atiyah1978.pdf
- DOI: 10.1016/0375-9601(78)90141-X
- Bibliographic year: 1978; resource status: **verified**.
- Checked extent and chronology: Full three-page primary PDF opened and read, pp.185--187: rank/isotropy, reality, equivalence groups, all-instanton assertion, parameter count. Received16December1977; published6March1978. Row versus column quaternion placement explicitly audited.

### `atiyahhitchinsinger1977deformations`

- URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC431234/
- DOI: 10.1073/pnas.74.7.2662
- Bibliographic year: 1977; resource status: **verified**.
- Checked extent and chronology: Primary PMC record and abstract opened. Dimension theorem identified; this run does not claim rereading the full two-page proof. Contributed20April1977; publishedJuly1977.

### `baxter1971eight`

- URL: https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.26.832
- DOI: 10.1103/PhysRevLett.26.832
- Bibliographic year: 1971; resource status: **verified**.
- Checked extent and chronology: Publisher abstract and metadata opened. Received25February1971; published5April1971. Exact zero-field eight-vertex solution identified; no full-paper proof reading is claimed.

### `baxter1973eigenvectors`

- URL: https://www.sciencedirect.com/science/article/pii/0003491673904417
- DOI: 10.1016/0003-4916(73)90441-7
- Bibliographic year: 1973; resource status: **unverified**.
- Checked extent and chronology: Publisher search results expose title, abstract, volume and pages, but every direct publisher open returned403. Author-repository PartI is accessible, but is not substituted for PartIII. This entry is deliberately unverified under the required open-URL rule; no completeness theorem for exceptional parameters is asserted from it.

### `belavin1980discrete`

- URL: https://www.mathnet.ru/eng/faa1849
- DOI: 10.1007/BF01078301
- Bibliographic year: 1980; resource status: **verified**.
- Checked extent and chronology: MathNet primary metadata and full Russian article opened. Original Funktsionalnyi Analiz i ego Prilozheniya14(4),18--26. Equations1--17, especially Yang--Baxter, transfer matrices and discrete-group ansatz read. Received12June1980; publication1980. Transfer construction is recalled as earlier work.

### `belavin1981dynamical`

- URL: https://www.itp.ac.ru/en/persons/belavin-aleksander-abramovich/
- DOI: 10.1016/0550-3213(81)90414-4
- Bibliographic year: 1981; resource status: **verified**.
- Checked extent and chronology: Author-institution publication list opened and exact article metadata checked. Publisher direct full-text route returned403. This is a thematic lead for the unformulated algebra and SL(2,R) remarks, not an exact resolution of either.

### `bytsko2003xxz`

- URL: https://arxiv.org/pdf/hep-th/0112163
- DOI: 10.1063/1.1591054
- Bibliographic year: 2003; resource status: **verified**.
- Checked extent and chronology: Author preprint and arXiv metadata opened. Section5 equations52--55, relation to the Fateev--Zamolodchikov spin-one model and isotropic limit read. First posted18December2001; revised14January2002; publication2003. Used to distinguish the published ratio from the notebook's literal coefficient.

### `coleman1975equivalence`

- URL: https://journals.aps.org/prd/abstract/10.1103/PhysRevD.11.2088
- DOI: 10.1103/PhysRevD.11.2088
- Bibliographic year: 1975; resource status: **verified**.
- Checked extent and chronology: Publisher abstract and metadata opened; neutral-sector formulation inspected. Full publisher PDF unavailable in this run. Received6January1975; published15April1975.

### `elitzur1975local`

- URL: https://harvest.aps.org/v2/journals/articles/10.1103/PhysRevD.12.3978/fulltext
- DOI: 10.1103/PhysRevD.12.3978
- Bibliographic year: 1975; resource status: **verified**.
- Checked extent and chronology: Full primary APS PDF opened; sectionsI andIV read. Received29July1975; published15December1975. Vanishing gauge-variant expectations is separated from a gauge-invariant confinement theorem.

### `faddeev1996bethe`

- URL: https://arxiv.org/pdf/hep-th/9605187
- Bibliographic year: 1996; resource status: **verified**.
- Checked extent and chronology: Full author lecture notes opened. Section3, equations44--65, read for local fundamental relation, multiplication, auxiliary trace and regular transfer derivative. Lectures delivered1995; first arXiv posting26May1996. Cited as preprint rather than guessing book-production chronology.

### `faddeevkorepin1978quantum`

- URL: https://researchconnect.stonybrook.edu/en/publications/quantum-theory-of-solitons/
- DOI: 10.1016/0370-1573(78)90058-3
- Bibliographic year: 1978; resource status: **verified**.
- Checked extent and chronology: Author-institution record and abstract opened; this run does not claim a full-paper reading. PublishedJune1978. Used for the pre-talk semiclassical soliton programme, not a precise mass formula absent from the notebook.

### `feynmanhibbs1965path`

- URL: https://www2.oberlin.edu/physics/dstyer/FeynmanHibbs/
- Bibliographic year: 1965; resource status: **verified**.
- Checked extent and chronology: The emended edition's editor Dan Styer's institutional page opened. It identifies the original1965 authors and the2010 emended edition. Used only to correct notebook Gibbs to Hibbs, not to assert mathematical contents of the reading list.

### `fuhwang2010prolongation`

- URL: https://arxiv.org/pdf/1011.4751
- Bibliographic year: 2010; resource status: **verified**.
- Checked extent and chronology: Full author preprint opened; Definition2.1, the introduction's classical-prolongation history and section5 interpretation inspected. Posted22November2010. Used only to verify the classical tensor-intersection definition, not to claim a new fate for Fuchs's missing pages.

### `guilleminquillensternberg1967infinite`

- URL: https://link.springer.com/article/10.1007/BF02798038
- DOI: 10.1007/BF02798038
- Bibliographic year: 1967; resource status: **verified**.
- Checked extent and chronology: Publisher metadata opened: received7January1966, publishedDecember1967. Full article not accessed. The precise tensor definition used in the chapter was read separately in Fu--Hwang, Definition2.1.

### `isenbergyasskingreen1978nonselfdual`

- URL: https://people.tamu.edu/~yasskin/resume/res-93.pdf
- DOI: 10.1016/0370-2693(78)90486-0
- Bibliographic year: 1978; resource status: **verified**.
- Checked extent and chronology: Primary author CV opened, publicationsp.5, corroborating title, authorship, journal and pages; original publisher search record supplies9October1978. Publisher direct open returned403. Original theorem proof was not read; exact formulation is checked separately in Mason--Skinner with a holomorphic-triviality correction.

### `kac1968graded`

- URL: https://www.mathnet.ru/eng/im2519
- DOI: 10.1070/IM1968v002n06ABEH000729
- Bibliographic year: 1968; resource status: **verified**.
- Checked extent and chronology: Primary MathNet metadata and full English PDF opened. Introduction, ChapterI section1 definitions, ChapterII section6 Definition9/Lemmas21--22/Proposition10, ChapterIII section1 and Theorem4, ChapterIV Theorem5 read. Homogeneous simplicity, local generation, irreducibility and growth restrictions retained. Received13February1968; publication1968.

### `liebschultzmattis1961soluble`

- URL: https://collaborate.princeton.edu/en/publications/two-soluble-models-of-an-antiferromagnetic-chain/
- DOI: 10.1016/0003-4916(61)90115-4
- Bibliographic year: 1961; resource status: **verified**.
- Checked extent and chronology: Author-institution metadata and abstract opened. PublicationDecember1961. Full proof not read; elementary Pauli/Jordan--Wigner normalization corrections are checked directly from the notebook matrices.

### `luther1976eigenvalue`

- URL: https://journals.aps.org/prb/abstract/10.1103/PhysRevB.14.2153
- DOI: 10.1103/PhysRevB.14.2153
- Bibliographic year: 1976; resource status: **verified**.
- Checked extent and chronology: Publisher abstract and metadata opened. Received19April1976; published1September1976. Chain/continuum excitation-spectrum identification checked at abstract level, not as an operator-topology convergence theorem.

### `mandelstam1975soliton`

- URL: https://journals.aps.org/prd/abstract/10.1103/PhysRevD.11.3026
- DOI: 10.1103/PhysRevD.11.3026
- Bibliographic year: 1975; resource status: **verified**.
- Checked extent and chronology: Publisher abstract and metadata opened. Received24February1975; published15May1975. Full paper unavailable. Notebook vertex formula is corrected only schematically with an explicit regulator/convention qualification.

### `masonskinner2006ambitwistor`

- URL: https://arxiv.org/pdf/hep-th/0510262
- DOI: 10.1016/j.physletb.2006.02.061
- Bibliographic year: 2006; resource status: **verified**.
- Checked extent and chronology: Full author PDF opened. Section2, Theorems1--2 and footnote1 read, as well as the incidence equation and O(I^4) convention. First arXiv posting31October2005; publication2006. Fibrewise holomorphic triviality is required in our formulation; the review's overbroad Chern-class shorthand is explicitly not repeated.

### `onsager1944crystal`

- URL: https://www.phys.ens.psl.eu/~langlois/Onsager43.pdf
- DOI: 10.1103/PhysRev.65.117
- Bibliographic year: 1944; resource status: **verified**.
- Checked extent and chronology: Primary PDF opened; abstract and transfer-operator construction inspected. Received4October1943; published1944. The chapter separately derives its finite row-transfer trace identity, and does not verify the notebook's unexplained1965 priority attribution.

### `penrosemaccallum1973twistor`

- URL: https://www.phys.lsu.edu/staff/karen/paper/TwistorTheory-Penrose%3AMacCallum.pdf
- DOI: 10.1016/0370-1573(73)90008-2
- Bibliographic year: 1973; resource status: **verified**.
- Checked extent and chronology: Full original scanned PDF downloaded from the university-hosted URL and opened locally. Sections1.1--1.2, pp.245--248, and2.1--2.2, pp.256--261, inspected by page images/OCR. Scan header says1972 and241--316; publisher issue metadata saysFebruary1973 and241--315. Received9June1972; based on1970 lectures. The bibliography follows publisher metadata and records the discrepancy.

### `sklyaninfaddeev1978quantum`

- URL: https://www.mathnet.ru/eng/dan42231
- Bibliographic year: 1978; resource status: **verified**.
- Checked extent and chronology: Full four-page Russian primary article opened and sections1--4 read. The logarithm of A generates quantum charges; the authors explicitly state that a full classical comparison for sine-Gordon has not yet been made. Received28July1978; publishedDecember1978. Not used as if it already contained every later RTT formulation.

### `witten1978interpretation`

- URL: https://collaborate.princeton.edu/en/publications/an-interpretation-of-classical-yang-mills-theory/
- DOI: 10.1016/0370-2693(78)90585-3
- Bibliographic year: 1978; resource status: **verified**.
- Checked extent and chronology: Primary author-institution metadata and abstract opened; published28August1978. Original full text not read in this run. The precise third-formal-neighbourhood statement was checked in the identified later primary research exposition.

### `woit2021euclidean`

- URL: https://www.math.columbia.edu/~woit/twistorunification/euclidean-twistors.pdf
- Bibliographic year: 2021; resource status: **verified**.
- Checked extent and chronology: Full author-institution PDF dated11April2021 opened. Only the classical geometry review in sections3.1 and3.3.2 is used: Grassmannian graph coordinates, determinant metric, SU(2,2) real form, incidence and U(2) compactification. Its speculative unification proposal is not used as established physics.

### `zamolodchikov1977exact`

- URL: https://link.springer.com/article/10.1007/BF01626520
- DOI: 10.1007/BF01626520
- Bibliographic year: 1977; resource status: **verified**.
- Checked extent and chronology: Publisher abstract and metadata opened on10November2026. Exact two-particle S-matrix claim and agreement with semiclassical results inspected; full CMP article not read in this run. PublishedJune1977.

### `zamolodchikovfateev1980spin`

- URL: https://www.itp.ac.ru/en/persons/fateev-vladimir-aleksandrovich/
- Bibliographic year: 1980; resource status: **verified**.
- Checked extent and chronology: Author-institution publication list opened and exact article identified. Original Russian Yadernaya Fizika32(2),581--590. Original full article and pre-publication circulation date not verified. Explicit Hamiltonian and isotropic limit checked in Bytsko section5; match to notebook is only partial because of the coefficient discrepancy.

### `zamolodchikovzamolodchikov1978on`

- URL: https://kamecke.userpage.physik.fu-berlin.de/ps/zam3.pdf
- DOI: 10.1016/0550-3213(78)90239-0
- Bibliographic year: 1978; resource status: **verified**.
- Checked extent and chronology: Primary PDF introduction and sections2--3 read. CDD ambiguity and limited model-identification claims retained. Received22August1977; revised14November1977; published27February1978.

### `zhang2025bootstrap`

- URL: https://arxiv.org/pdf/2504.17773
- DOI: 10.21468/SciPostPhys.20.4.102
- Bibliographic year: 2026; resource status: **verified**.
- Checked extent and chronology: Full author preprint version7 dated6February2026 and arXiv metadata opened; section2 equations1--6 read. First posted24April2025; arXiv record reports SciPostPhysics20,102(2026). Publisher direct route failed. Used only for the necessary cubic condition, whose derivation is independently given; no assertion about general sufficiency as of November2026 is made.

### Additional exact full-text routes opened

The MathNet landing pages in the bibliography were accompanied by the actual original-paper links: Kac's English translation at `https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=2519&what=fullteng`, and Sklyanin–Faddeev's Russian original at `https://www.mathnet.ru/php/getFT.phtml?jrnid=dan&option_lang=eng&paperid=42231&what=fullt`. Belavin's1980 Russian full paper was opened from its MathNet record and equations1–17 inspected. Zhang's current bibliographic status was checked at `https://arxiv.org/abs/2504.17773`; its current record reports SciPostPhysics20,102(2026), while the actual version read is dated6February2026. The direct SciPost DOI route was unavailable. A search also surfaced a July2026 follow-up on necessary/sufficient conditions, but it was not read or used: the chapter proves only the necessary obstruction and makes no claim about general sufficiency as of November2026.

## Mathematical audit decisions

### ADHM and gauge theory

The affine quaternionic matrix must satisfy nondegeneracy/rank conditions, with framed and unframed moduli distinguished. The8N−3 count concerns the unframed irreducible charge-N case; a framed version has a different dimension. The notes' row convention `M(x)=xA+B`, left real `GL(N,R)` and right quaternionic `Sp(N+1)` action is compatible with associativity: `G(xA+B)V=x(GAV)+GBV`. It does **not** require commuting x through V. Passing to a transposed/adjointed convention conjugates the scalar and can change the self-dual/anti-self-dual orientation convention. The actual general theorem is read in the original three-page ADHM paper; the AHS dimension record was checked at abstract/metadata extent only.

The words “beautiful parametrization” do not specify rationality, global coordinates, connectedness, algorithms or an equivalence criterion. Item453.3 is therefore F, not a new open instanton problem. GP-1977-05 is not reused because its fixed-charge classification/connectedness question is more specific and different. Gauge averaging in453.4 has an explicit finite compact-lattice reconstruction; the gauge-variant vanishing is valid there. The proposed confinement inference453.5 does not follow and is separated from the valid statement.

### Fermions, factorization and transfer matrices

Direct matrix checks establish the Pauli factor2i and the factor1/2 needed in the Jordan–Wigner operators. The chain-to-continuum passage is not asserted as a theorem of operator convergence from Luther's abstract. Scaling, regulators, parity-sector boundaries and normal-ordering/Klein-factor conventions are marked as reconstructions. Massive Thirring/sine-Gordon equivalence is not promoted to an unqualified bare-field identity. Ordered exchange-algebra consistency requires nondegeneracy/independence assumptions; an arbitrary quotient of a free associative algebra is already associative.

The sample functional equation on P817 is materially false with its own regularity convention: setting the second spectral parameter to zero forces the eight-vertex d-weight to vanish identically. Its intended correction is not guessed. The ODE fragment lacks two equations and algebraic constraints, so no sufficiency result is inferred. Raw second Taylor coefficients of the transfer matrix contain disconnected products; the local three-site density belongs to the logarithmic derivative. The finite-dimensionality of the chain prevents infinitely many algebraically independent matrix integrals.

GP-1977-10/1977-436.16 is a thematic predecessor for the quantum inverse-scattering programme, not the same finite XYZ spectral problem or the same literal spin-one deformation question. The initially suggested record1977-431 concerns commuting ordinary differential operators and is not the relevant occurrence. The new finite-chain entry is GP-1978-11. Its status expressly avoids a blanket exceptional-parameter completeness claim from the inaccessible Baxter PartIII.

### Completed critical algebraic audit, not an open-problem development

For the literal real generators `[S^a,S^b]=epsilon_abc S^c`, `X=sum S^a tensor S^a` and `h=X²−2X`, the necessary cubic condition for an **analytic regular difference-form braided R-matrix** fails. `critical_audit.tex` gives the complete Taylor-coefficient derivation, including the scalar second-order normalization, every u²v word, and `Q=r3−h³`. It proves the explicit forbidden matrix entry

`<001|[h12+h23,[h12,h23]]|212> = −6`.

The right-hand side of any `Q23−Q12` has zero at that entry. For `h_t=X²+tX`, the same exact witness is `t(t−1)(t+1)`. The handwritten generator convention matters: Hermitian `J=iS` gives `J·J=−X`, so the standard isotropic spin-one density `J·J−(J·J)²` is `−X−X²`, not an overall rescaling of `X²−2X`.

`check_spin1.py` and `check_spin1_output.txt` contain exact SymPy calculations, a second Levi–Civita index-contraction check, the full six-word proof table and passing/failing controls. The root editor independently constructed permutation/contraction tensors in `work/root/check_independent.py` and obtained the same polynomial and−6; the root also independently re-expanded the cubic Yang–Baxter coefficient and confirmed its sign. The finite six-word proof is included so the conclusion does not depend on trusting software. Passing necessary-condition controls at t=−1,0,1 are not claimed to prove sufficiency.

The Fateev–Zamolodchikov1980 anisotropic model is a partial match to the nearby corrected question, with the exact isotropic formula checked in Bytsko. The original1980 paper was bibliographically verified through the author's institution; its proof and pre-publication circulation date were not read. GP-1978-10 therefore records a closed negative literal result and an established corrected construction. No classC residual is manufactured. The audit's scope excludes broader, unspecified meanings of integrability; it does not claim that every imaginable integrability criterion fails. In the six-class taxonomy, F is used for the intended published assertion behind a false literal formula when that intended assertion cannot be identified; `literal_correctness` separately records “false as written.” The taxonomy has no separate “false claim” class.

### Ambitwistor hypotheses and source criticism

The real homogeneous quotient in the notes has the wrong dimension. The stabilizer must be the relevant eleven-dimensional parabolic, with Lie algebra `(so(3,1)+R) semidirect R^(3,1)`; `SU(2,2)` is the spin double cover of the identity component of `SO(4,2)`. Null twistor two-planes form the U(2) compactification, not the affine real Minkowski chart. The curvature convention `F=dA+A wedge A` fixes the covariant derivative order `[A,F]`, contradicting the printed reversed commutator.

The full Yang–Mills/ambitwistor correspondence uses an appropriate local domain, connected simply connected intersections with null geodesics, and holomorphic bundles trivial on every incidence quadric. Extension to the third formal neighbourhood means modulo `I^4`. Witten1978 and Isenberg–Yasskin–Green1978 were checked at primary metadata/abstract or primary-author bibliography extent; the detailed formulation was read in Mason–Skinner Section2, Theorems1–2 and footnote1. The checked paper's Chern-class shorthand is too weak if interpreted literally: on `P1×P1`, `O(1,0) direct-sum O(−1,0)` has c1=c2=0 because the first ruling class squares to zero, but restricts to `O(1) direct-sum O(−1)` on a ruling and is not holomorphically trivial. This is an elementary editorial counterexample, independently checked by the root, not a novelty claim. The actual P823 condition of fibrewise **holomorphic triviality** is retained in455.14 and456.4. No claim is made to have reread the original1978 proofs.

### Fuchs classification and the missing middle

Kac's introduction and explicit conventions distinguish graded simplicity, ordinary simplicity, finite-dimensional graded pieces, local generation, irreducibility and finite growth. These hypotheses cannot be discarded to validate the source's broad four-series/exhaustion wording. The Cartan prolongation constructed from a finite-dimensional faithful pair is maximal; arbitrary transitive extensions embed in it and need not equal it. Contact type has a weighted depth-two grading and is not covered unchanged by the later depth-one simplification.

The period-three rule has the explicit isomorphism `epsilon_3k -> H z^k/2`, `epsilon_(3k+1) -> E z^k`, `epsilon_(3k−1) -> F z^k/2`. Nine residue-pair checks verify all structure constants. Evaluation at z=1 gives a proper ungraded ideal. The three degrees−1,0,1 span only constant sl2 and therefore fail the local-generation convention relevant to Kac's classification. The root independently verified the residue-pair identities and exponents. This is a simple identification of the recorded bracket, not a newly discovered classification theorem. The final list of “three” is incomplete, and the missing pages cannot be supplied from earlier-index titles.

## Candidate screening and limits

The winter material contains no defensible classC or D item for a new open-problem development. Identified constructions are established; ambiguous suggestions lack the operations or quantifiers necessary for a mathematical problem; literal false assertions receive direct corrections and finite checks. Further searches of independent1979 seminar records might identify the intended spin-one coefficient, the quadruple algebra or the missing Fuchs qualifications, but those would be historical source investigations. They are not evidence that the corresponding general mathematics remains open.

The completed exact audit is kept separate from Stage2 candidate screening. It is labeled as a critical algebraic audit and uses the required authorship markers for the derivation/computation performed here. No theorem is called proved here when only publisher metadata was inspected. Complete-original-text reading is claimed only to the extent specified above.

## Output and reproducibility

The talk/item JSON files, `refs.bib`, `problems.json`, `corrections.json`, `critical_audit.tex`, this log, `source_provenance.md`, the two JSON ledgers, and the authored exact-check code/output are the merge deliverables. Downloaded literature PDFs, OCR outputs and resized working scans are **intermediate research material**, not deliverable source files and should not be repackaged as authored work. The root editor performs the integrated kit build and final PDF checks.

Final owned counts: 76 mathematical occurrences; A=0, B=1, C=0, D=0, E=62, F=13. There are 29 cited bibliographic entries, of which one is explicitly unverified because its direct URL remained inaccessible; two problem entries; forty correction/provenance rows; fifteen reviewed supplied scan pages.
