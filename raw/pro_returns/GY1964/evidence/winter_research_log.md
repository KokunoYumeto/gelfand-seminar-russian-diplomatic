# Winter source audit: records 15–35

Audit date: 12 November 2026. Working corpus: the attached English and Russian GY1964 transcriptions, the supplied talk catalogue, the original page scans extracted in work/scans, and the same-year first-run occurrence index supplied as work/previous_index.md. The latter is not an index of earlier academic years. No genuine earlier-year occurrence or problem identifier was inferred from it.

## Scope, files, and verification

The data cover all 21 records numbered15–35, including the undated plan23, and all91 pre-existing occurrence IDs in this interval. All required assessment fields are populated. Final counts are A6, B7, C1, D0, E59, F18. Classifications were reassessed independently; in particular33.3 is F, not C, because the notebook does not state a definite finite/simple-spectrum existence problem. No D classification was used merely because a publication search failed.

The generated files are talks.json, items.json, problems.json, references.bib, and corrections.csv. The explicit editorial data and record-by-record saves are in write_winter.py. The generator output is write_winter_output.txt. The separate validator and its output are validate_winter.py and validation_output.txt. Validation checks the exact supplied occurrence-ID set, all schema enums and fields, record ordering, mandatory worth sentences for C/D, dated statuses, citation-key coverage, problem links, math delimiters, and accidental control characters. It passes with zero errors. There are38 bibliography entries, five problem-index records, and21 correction rows.

The provisional problem identifiers W01–W04 are for root-level renumbering. They concern nonlinear Fredholm maps, continuous Fredholm families, the ball-algebra Gleason question, and finite-group spectral reconstruction. GP-1964-02 is the shared Hilbert invariant-subspace problem; its recurrence in record50 is to be merged by the spring/root contributions. No GP-1964-03 is assigned to the inferred Banach comparison.

Bibliography note=verified means that the linked primary record was successfully opened. It does not mean that the original theorem or proof was read. The item assessment fields and the table below distinguish full-result inspection, an abstract, author/publisher metadata, and indirect historical verification. A primary endpoint that returned only an error or a security page did not count as verification. No inaccessible lead was silently converted into a verified reference.

## Source and scan checks

The English and Russian source passages in the working excerpts were compared. Original scans were inspected for consequential formula, attribution, sign, and scope doubts, including P000035, P000037, P000038, P000039, P000040, P000041, P000042, P000043, P000044, P000045, P000046, P000047, P000048, P000049, P000050, P000051, P000052, P000053, P000054, P000055, P000056, P000057, P000058, P000059, P000060, P000061, P000062, P000063, P000064 and P000065.

The catalogue page envelopes overlap neighbouring talks. They are retained in talks.json for provenance; each item has its actual passage locator. In particular record34 continues through P000065 even though its catalogue envelope ends at P000064. Record35 physically precedes Kirillov’s text on P000063 but retains its supplied record number and order. Record23 is a real plan/heading entry and is not discarded merely because it has no separate mathematical occurrence.

### Important source observations

- P000035: the isolated coker K follows an operator T, with no second operator introduced. The index classification needs an ambient operator space and topology; numerical index does not classify arbitrary parameter families.
- P000037: the manuscript’s Povzner given name conflicts with the catalogue A. Ya. attribution. This is preserved as a provenance conflict. The particle-potential sketch lacks sufficient hypotheses for a confinement theorem. The emphatic invariant-subspace announcement records a claim later retracted, not a solution.
- P000039: the scan explicitly says “Тесты подобные” and defines constant rejection probability on the null. Both transcriptions are faithful. A separate abbreviated invariant-test line does not justify alleging a conflation. An interim correction row making that allegation was removed after a fresh scan check.
- P000042: the displayed Schrödinger scaling/sign, positive-phase ansatz, abbreviated action integral, and classical p=xdot relations do not form one consistent normalization. The companion supplies a coherent modern model and labels it reconstruction. The caustic/topological argument is separate from an elementary local WKB substitution.
- P000045: the displayed negative free eigenvalue conflicts with the chosen negative-second-derivative operator. One-based and zero-based indices are mixed. The Slater determinant argument needs a chamber ground-state argument and a separate multiplicity treatment.
- P000047: the rank-one power quotient has small finite cases and is an orbifold group; it cannot uniformly be called an infinite-index surface-group quotient.
- P000048: an independent Hermitian upper-right block with arbitrary SL2(C) diagonal block is not closed under the displayed matrix multiplication. The semidirect-product realization corrects this.
- P000048–P000050: the prime/primary letter roles are inconsistent, and P000050 itself notes their interchange. General differential operators must not be confused with first-order derivations.
- P000052: principal symbols live on the cotangent bundle unless a metric identification is explicitly supplied. Solution-sheaf finiteness and a two-term fine resolution require exactness/compatibility hypotheses absent from the broadest notebook sentence.
- P000057–P000059: multiplying the sphere ambient dimension by16, not6, adds8 to the Hurwitz–Radon number. The sphere group is reduced KO. The projective reduced class has order2^phi(k), not phi(k).
- P000060: essential self-adjointness uses the nonreal range criteria, not density at every complex parameter, including real eigenvalues.
- P000061: genus four is correct. Nelson’s original example, read through its Russian translation, explicitly has genus four minus a point. No genus emendation was made. Formal/core commutation is not strong commutation. Failure of essential self-adjointness of the Laplacian on the selected domain does not rule out self-adjoint extensions.
- P000062: simple eigenspaces of an ergodic action do not mean simple continuous spectrum. Probability-preserving Lebesgue-spectrum assertions concern L2_0, not the constants. Absolute continuity, equivalence to Lebesgue maximal type, and homogeneous multiplicity are different conditions.
- P000062–P000063: Sinai’s “all known examples” sentence is historical. No explicit Banach problem, finite-multiplicity existence question, or fixed time group is written. The modern comparison is therefore editorial and receives F, with no problem-index entry. Flow and transformation versions have different present statuses.
- P000063: finite support means a direct sum of binary groups, not a full product. No precise attributed Gordin/Whitehead theorem or dyadic action can be recovered.
- P000064: the full affine group with negative as well as positive dilations has one infinite-dimensional irreducible; its positive component has two. The source’s “one” should not be corrected to “two.” The full group representation on a compact hyperbolic quotient is discrete, whereas the geodesic one-parameter flow has continuous Lebesgue spectrum.
- P000064–P000065: scalar cocycles correspond to stabilizer characters; higher-dimensional representations require vector-valued cocycles. An unspecified “cohomology determines the system” question is not promoted to a modern open conjecture.
- P000065: even transitive finite actions can share the same Koopman representation without being isomorphic. The seven-point GL3(F2) point/dual-point example is editorial and independently verified by the root’s exact168-matrix computation. The icosahedral rotation group is PSL2(F5), not SL2(F5). Multiplicative observable structure, including the probability state, retains information forgotten by a Hilbert-space spectrum.

## Primary references successfully opened

Dates below separate a documented submission, preprint, or lecture date from formal publication where the evidence permits it. “First circulation unknown” is retained when no primary source established an earlier date.

| Key | Opened primary URL | Passage inspected and limits |
|---|---|---|
| smale1965sard | https://people.math.harvard.edu/~dafr/M392C-2018-MorseTheory/Readings/Smale.pdf | Full six-page paper; Theorems1.1 and1.3, Section2. Received2Nov1964, the seminar day; published1965. No causal connection inferred. |
| janich1965fredholm | https://link.springer.com/article/10.1007/BF01360851 | Publisher record, MathAnn161,129–142, April1965. Exact full theorem text not acquired; family/classifying-space match assessed as metadata/indirect. |
| atiyahsinger1963index | https://webhomes.maths.ed.ac.uk/~v1ranick/papers/atiyahsing.pdf | Full announcement; pp422–423 for elliptic symbol over cotangent sphere, finite kernel/cokernel and K-theoretic framework. Communicated1Feb1963, published1963. |
| ruelle1963classical | https://www.ihes.fr/~ruelle/PUBLICATIONS/Publications.html | Author’s bibliography confirms HPA36,183–197 and adjacent1963–64 statistical-mechanics papers. Exact proposed seminar reading list and original theorem not identified. |
| schur1918formen | https://link.springer.com/article/10.1007/BF01203611 | Publisher metadata, MathZ1,184–207, June1918. Original proof not read. The character-immanant interpretation adds hypotheses absent from the note. |
| arnold1967characteristic | https://www.mathnet.ru/eng/faa2802 ; https://webhomes.maths.ed.ac.uk/~v1ranick/papers/arnold3.pdf | Full English paper opened; Introduction and Sections1–3. Received28Sep1966, published1967. Notebook supplies November1964 oral evidence. Introduction is contextual for WKB; Section1 is not cited as a transport-equation derivation. |
| linnik1965cotest | https://www.mathnet.ru/eng/dan30892 ; https://www.mathnet.ru/php/getFT.phtml?jrnid=dan&option_lang=eng&paperid=30892&what=fullt | Full three-page Russian note read; p520 definitions, analytic cotest-ideal argument. Received7Dec1964, published1965, closely following seminar. |
| gleason1964ideals | https://www.mathnet.ru/eng/mat370 | Verified metadata for original JMathMech13(1),125–132,1964 and Russian translation. Original proof not read; this is an antecedent, not the exact ball-algebra solution. |
| backlundfallstrom1998gleason | https://www.numdam.org/item/ASNSP_1998_4_26_3_595_0.pdf | Full paper, pp595–596 and Theorem2.2. Intro attributes the positive ball result to Leibenzon via Henkin1971. The exact early circulation of Leibenzon’s proof was not established. |
| berardhelffer2020gelfand | https://arxiv.org/abs/1807.03990 ; https://arxiv.org/pdf/1807.03990 | Abstract and full paper opened; Gelfand strategy and chamber/fermion treatment, Sections3–6. First arXiv11Jul2018; journal2020. |
| berardhelffer2020sturm | https://arxiv.org/abs/1706.08247 ; https://arxiv.org/pdf/1706.08247 | Full paper opened; main Sturm linear-combination theorem and historical identification with1836 work. First arXiv26Jun2017; journal2020. |
| serre1968congruence | https://numdam.org/item/SB_1966-1968__10__275_0/ ; https://www.numdam.org/item/SB_1966-1968__10__275_0.pdf | Full Bourbaki report, Sections1.2–1.3, Theorem1 and historical remark; integer case attributed to Bass–Lazard–Serre/Mennicke1964. LectureJune1967, printed1968. |
| colemanmandula1967symmetries | https://www.physics.mcgill.ca/~keshav/675/colemanmandula.pdf | Full paper; p1251 theorem and five assumptions. ReceivedMarch1967, publishedJuly1967. Match restricted to the explicit scattering-symmetry formulation. |
| palamodov1961ideals | https://www.mathnet.ru/eng/dan25918 ; https://www.mathnet.ru/php/getFT.phtml?jrnid=dan&option_lang=eng&paperid=25918&what=fullt | Full Russian note, Theorems1–2; smooth-function/formal-ideal result. Received8Jul1961. Not conflated with an unrestricted holomorphic growth theorem. |
| palamodov1970operators | https://link.springer.com/book/9783642462214 | Publisher book record/preface, Grundlehren168, English1970. PartI analytic-algebraic treatment identified, exact chapter theorem and first publication of the seminar formulation not verified. |
| palamodov1966statistics | https://www.mathnet.ru/eng/dan32367 ; https://www.mathnet.ru/php/getFT.phtml?jrnid=dan&option_lang=eng&paperid=32367&what=fullt | Full note, p1251 Theorem1; polynomial boundary-growth holomorphic functions on a polydisc and polynomial-matrix image. Received2Aug1965, published1966. The source’s unspecified function space prevents an exact item27.2 match. |
| cidruizhomssturmfels2021primary | https://arxiv.org/abs/2001.04700 ; https://arxiv.org/pdf/2001.04700 | Full paper; Theorem2.1, equation17, historical Introduction. Finite Noetherian operators in characteristic0 have polynomial coefficients. First arXiv14Jan2020; journal2021. |
| peetre1959differential | https://journals.msp.org/mscand/article/view/2772 | Publisher record, MathScand7,211–218; DOI10.7146/math.scand.a-10574. Original theorem PDF viewer did not yield text; metadata only. |
| peetre1960correction | https://journals.msp.org/mscand/article/view/2743 | Publisher record, MathScand8,116–120; DOI10.7146/math.scand.a-10598. Correction metadata checked, original text not read. |
| adams1962vector | https://www.math.ens.psl.eu/~benoist/refs/Adams.pdf | Full paper; Section1, Theorems1.1–1.2 and projective-space K-theory reduction. ReceivedNovember1961, published1962. Maximum rho(m)-1 verified. Exact individual projective-KO theorem number not assigned without verification. |
| nelson1959analytic | https://www.mathnet.ru/eng/mat222 ; https://www.mathnet.ru/php/getFT.phtml?jrnid=mat&option_lang=eng&paperid=222&what=fullt | Full Russian translation, especially Sections9–10 and translationpp121–123. Genus four explicitly verified, as are almost-everywhere complete fields and failure of strong commutation. Original AnnMath70(3),572–615,1959; translation1962. |
| mackey1963ergodic | https://pmc.ncbi.nlm.nih.gov/articles/PMC221293/ | Full primary record/author metadata, PNAS50(6),1184–1191,December1963. PMC PDF route did not expose text. Page-image links opened; interpretation of programme additionally verified from the full1966 paper. |
| prikhodko2020flows | https://www.mathnet.ru/eng/sm8147 | Publisher abstract explicitly announces probability-preserving flows with simple Lebesgue spectrum. ReceivedJune2012, revisedOctober2019, published2020. Original complete proof was not independently checked; flow result is published, unlike the new transformation lead. |
| openai2026lebesgue | https://github.com/openai/math/blob/main/preprints/A-smooth-three-torus-diffeomorphism-with-simple-Lebesgue-spectrum-September-23-2026/build/sections/01-introduction.tex | Official repository introduction successfully opened and main theorem inspected: smooth volume-preserving three-torus diffeomorphism with a bilateral Koopman orbit an ONB of L2_0. Dated23Sep2026. Proof not independently verified; no accepted resolution is asserted. Match to notebook is thematic/editorial only. |
| cartan1954finitude | https://www.numdam.org/article/SHC_1953-1954__6__A17_0.pdf | Full exposé; p17-1 compact-complex coherent finiteness theorem; Section1 Proposition1 fine resolutions/deRham. Lecture3May1954; cites Cartan–Serre1953 announcement. |
| bott1959stable | https://webhomes.maths.ed.ac.uk/~v1ranick/papers/bott4.pdf | Full paper; Introduction/stable classical-group periodicity. Received17Nov1958, publishedSeptember1959. Used with careful KO-degree convention. |
| sakita1964supermultiplets | https://journals.aps.org/pr/abstract/10.1103/PhysRev.136.B1756 | Publisher metadata and abstract opened successfully on a later attempt. Received7Aug1964, published21Dec1964. PhysRev136,B1756–B1760. |
| gurseyradicati1964spin | https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.13.173 | Publisher metadata/abstract; received15Jul1964, published3Aug1964. PRL13,173–175. Distinguished from the three-author Gürsey–Pais–Radicati paper at13,299. |
| sinai1961lebesgue | https://www.mathnet.ru/eng/im3438 ; https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=3438&what=fullt | Full Russian paper opened; Introductionpp899–900 distinguishes discrete-time K-automorphisms and continuous-time K-flows and recalls prior algebraic examples. Received25Jun1960, published1961. |
| hermlekreidler2023halmos | https://link.springer.com/article/10.1007/s10485-023-09743-y | Full author paper in HTML. Introduction, Section1.2, Theorems4.8/5.5, Remark6.44(iii) inspected. The latter explicitly locates Mackey1964’s warning and Todd1950’s counterexample. Received1May2022, published8Sep2023. |
| bruhat1954induced | https://www.numdam.org/item/SB_1951-1954__2__185_0/ ; https://www.numdam.org/item/SB_1951-1954__2__185_0.pdf | Full exposé68, Sections2–3 on induced representations and Kronecker products. LectureDecember1952; printed1954. References Mackey1949/1951/1952. |
| mackey1966virtual | https://m.mathnet.ru/php/archive.phtml?jrnid=mat&option_lang=eng&paperid=499&wshow=paper ; https://m.mathnet.ru/php/getFT.phtml?jrnid=mat&option_lang=eng&paperid=499&what=fullt | Full Russian translation opened through mobile MathNet after full-site route failures. Sections2–3 transitive actions, Section5 cocycle/cohomology and stabilizer homomorphisms, Sections9–11 groupoids. Original MathAnn166,187–207,1966; translation1969. |
| choighandehari2021affine | https://link.springer.com/article/10.1007/s11785-021-01100-y | Full author paper in HTML; Sections2.2–2.3 explicitly give the full real affine group and its unique infinite-dimensional irreducible; Section5 contrasts positive dilations. Published22May2021. The classification is recalled as classical Mackey theory. |
| gelfandfomin1952geodesic | https://www.mathnet.ru/eng/rm8283 ; https://www.mathnet.ru/php/getFT.phtml?jrnid=rm&option_lang=eng&paperid=8283&what=fullt | Full original Russian paper; Sections2–3, particularly p132 countable Lebesgue geodesic spectrum. This verifies the distinction between the full group and its one-parameter subgroup. The full-group compact-kernel argument in item34.7 is editorial reconstruction. |
| weyl1911eigenvalues | https://geodesic.mathdoc.fr/item/NGWGMP_1911__1911_58792/ | Digitized original-article catalogue record, pp110–117,1911. Metadata only; the original full theorem was not read. The modern confining Schrödinger formula is not falsely identified with that exact1911 statement. |
| debrangesrovnyak1964existence | https://uva.theopenscholar.com/james-rovnyak/selected-works | Author bibliography explicitly gives BullAMS70,718–721,1964 and names the retraction. Full original proof not read. |
| debrangesrovnyak1965correction | https://www.math.purdue.edu/people/profile/branges.html | Coauthor institutional bibliography entry65 gives the exact correction title and BullAMS71,396,1965. Rovnyak’s page independently identifies it as a retraction. Original correction not read. |
| marcoux2026generators | https://arxiv.org/pdf/2608.21154 | Full primary preprint opened. Abstractp1 and Introductionp2 explicitly call the separable infinite-dimensional complex Hilbert invariant-subspace problem unsolved and state its exact quantifiers. First version21Aug2026. Used for calibrated current status, not to certify all later claims. |

## Search strategy, queries and failures

Research proceeded in record batches rather than searching for a famous modern problem first. English and Russian author/title variants were used where appropriate; technical claims were matched to primary papers or primary author/publisher records.

### Successful query families

- Vishik, nonlinear Fredholm index, families, Smale infinite-dimensional Sard, Jänich Fredholm operators, Atiyah–Singer symbol/index.
- Ruelle/Povzner statistical mechanics and pair-potential minimizers; historical Ruelle publication list.
- Schur positive Hermitian generalized determinants and immanants.
- Arnold characteristic class quantization, Maslov caustic phase, Lagrangian Grassmannian.
- Linnik tests unbiased estimates cotest ideals; Palamodov analytic problem arising in statistics.
- Gleason ball algebra, Leibenzon, Henkin and Backlund–Fällström counterexamples.
- Gelfand Sturm eigenfunction combinations fermionic/Slater determinant; Bérard–Helffer implementation.
- Bass–Lazard–Serre/Mennicke congruence problem and SL2 triangle-group exceptions.
- Gürsey Radicati SU6, Sakita supermultiplets, Coleman–Mandula theorem hypotheses.
- Palamodov polynomial ideals differential operators primary quotient; modern Noetherian operators and differential equations.
- Peetre local sheaf morphisms; Cartan compact-coherent finiteness; Adams vector fields and projective KO; Bott stable groups.
- Nelson analytic vectors, commutation and genus-four punctured surface.
- Exact query: Sinai “Dynamical systems with countable Lebesgue spectrum”1961. This found MathNet im3438 and its full original PDF.
- Exact queries: Mackey “Ergodic transformation groups with a pure point spectrum”1964; Todd “On a conjecture in group-theory”1950. Original endpoints were blocked; the precise historical locator was verified in the full primary Hermle–Kreidler paper.
- Full real affine group, unique infinite-dimensional irreducible, Mackey classification. This found Choi–Ghandehari’s exact full-group discussion.
- Gelfand Fomin geodesic1952; full paper then opened through MathNet.
- Current-state searches for simple Lebesgue spectrum distinguished Prikhodko’s published flow construction from the dated2026 transformation claim.
- Cross-agent current ISP research supplied Marcoux et al.2026; its PDF was independently opened here before citation.

### Primary endpoints that failed or gave insufficient content

- Jänich full-text/GDZ route did not expose the result; Springer metadata did.
- Schur Digizeitschriften PDF attempt failed; Springer metadata succeeded.
- Direct AMS routes for the original congruence announcement and some historical operator papers did not open. Serre’s full primary Bourbaki account and author bibliographies are explicitly used instead.
- Peetre PDF links led to viewers without usable theorem text.
- Direct JSTOR Halmos–von Neumann and Mackey induced-representation pages produced tag-manager/empty content, not verification of the original results.
- Mackey1964 DOI10.1215/ijm/1256059458 failed; the Project Euclid full page contained only an iframe, which led to an additional-security-check notice. No bypass was attempted. The original paper is not included as a verified separate bibliography entry.
- Todd1950 DOI10.1112/jlms/s1-25.4.246, Oxford article/PDF routes, and Wiley DOI route failed or redirected to an inaccessible endpoint. The search metadata matched title/year; the direct original theorem was not read. Its historical role is attributed through Hermle–Kreidler’s explicit citation, not presented as direct verification.
- Mackey1966 full-site MathNet routes failed; the mobile record and linked mobile PDF succeeded. The successful URLs, not failed ones, appear in the table.
- PMC’s Mackey1963 PDF route did not provide text; page-image links opened but did not substitute for reading the full result. The1966 systematic paper supplies inspected content.
- Wallach1976 compact-quotient trace-formula DOI10.1090/S0002-9904-1976-14022-0 and AMS PDF routes failed. That paper is not in the verified bibliography.
- Initial APS Sakita request failed; a subsequent exact publisher request succeeded. Its final verification is therefore metadata/abstract, not an unresolved lead.
- The August2026 Bishop determinant preprint was a root/spring unverified lead. Its primary endpoint remained inaccessible. It is not used as a proved result in the development.

### F items and the exact information missing

The F classification indicates inadequate identification, not a claim that nobody developed the topic.

| Occurrence | Reason exact fate cannot be assigned |
|---|---|
| 16.2 | Potential assumptions, self-interactions, particle-number dependence of the confinement radius, and existence of a minimizer absent. Ruelle/Povzner and ground-state/confinement query families did not locate the exact sketch. |
| 19.6 | The primary-ideal-on-a-ball question lacks a precise function algebra, ideal class and desired assertion. |
| 24.4 | Matrix entries, elementary operation and intended congruence normal form are missing. |
| 25.4 | Proposed enlargement/unification programme lacks a precise symmetry category and dynamical assumptions; Coleman–Mandula answers only the reconstructed restricted formulation. |
| 26.5 | The phrase that a solution should be an ideal does not specify the algebraic object, multiplication or intended equivalence. |
| 27.2 | Function space, topology and growth are not fixed; Palamodov1966 provides a nearby precise theorem with additional hypotheses. |
| 28.3 | The broad solution-sheaf finiteness claim does not specify a compatible elliptic resolution/local exactness. |
| 29.2 | Sheaf-section topologies, compactness, cohomology topology and index are absent. |
| 29.3 | Infinite-order symbol class and function/growth category are absent. |
| 29.4 | Continuous-coefficient operator order, weak-solution interpretation and target regularity are absent. |
| 33.3 | Historical “all known examples” sentence has no explicit finite/simple-multiplicity existence question or time group. |
| 34.3 | Finite-support group identifiable; action/topology and named theorem attribution are not. |
| 34.5 | Dyadic action and measure absent. |
| 34.11 | Degree, coefficients, retained structure and equivalence in “cohomology determines” absent. |
| 35.1 | Noncommutative algebraic-geometry programme has no chosen algebra/object category or target result. |
| 35.2 | Algebraic differential-equation programme has no specified equations or module/differential-ring framework. |
| 35.3 | Small parameter has no equation, limit or estimate. |
| 35.4 | Multivariable functions have no selected family or classification target. |

Each of these eighteen occurrences retains its original occurrence ID and has an individual search/fate assessment in items.json.

## Current-status caution and report observations

1. The sole C item in this contribution is the unrestricted Hilbert invariant-subspace question, with its exact bounded/complex/separable/infinite-dimensional/closed-subspace hypotheses. August2026 primary literature explicitly calls it unsolved. The final status is calibrated: no generally accepted solution was verified in the literature checked through12Nov2026. Later claims are not treated as accepted solutions.
2. The ball-algebra question is solved, whereas unspecified general Banach/holomorphic ideal formulations need independent hypotheses. Its affirmative fate is verified indirectly through a later primary paper’s explicit historical reference.
3. Palamodov’s1961 smooth theorem, the holomorphic coherent-quotient formulation, and the1966 polynomial-growth polydisc theorem are distinct. Their common topic does not make every statement an exact publication match.
4. Sinai’s historical remark should not create a false new conjecture. Published simple-Lebesgue flow constructions already prevent a blanket open-status claim. The official23Sep2026 transformation preprint has an inspected theorem statement but no independently checked proof in this audit.
5. A concrete bounded addition arose from Kirillov’s finite-group reconstruction question: GL3(F2) acts transitively on nonzero vectors and nonzero covectors, the characters agree, but stabilizers prevent equivariant identification. The root independently rederived and exactly enumerated this example; the evidence is work/evidence/finite_action_check.json. This is verification of a classical obstruction, not a novelty claim.
6. No genuine preceding-year corpus was available. Connections may be described thematically, but earlier occurrence IDs or priority claims must not be fabricated.

## Independent development review

The root’s Bishop development was read in full and logically checked after the winter data were completed. A separate written audit is saved at work/evidence/development_proof_review.md. No gap was found in the endpoint determinant, rational cyclicity, finite-orbit continuity, sufficient computable gap rule, or generic conclusion. A minor negative-shift clarification was sent to root. The two root-owned exact arithmetic implementations were not redundantly rerun. The inaccessible2026 lead remains excluded from assumptions and prevents a novelty claim for the overlapping finite example.
