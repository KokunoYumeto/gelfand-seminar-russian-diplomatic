# Middle records: critical-companion research log

Status date: November 2026. Owner: middle_records. This part covers records **342, 343, 344, 345, 346, 347, 349, 350, 351**. Record **348 is owned by the root agent** and is intentionally absent from these data. The occurrence year is the academic-year identifier **1974**, including every item in this part.

## Deliverables and scope

The data contain **9 talks, 71 distinct mathematical items, 5 problem-index entries, 25 cited bibliography keys, and 19 correction/provenance rows**. Item classes are **A: 12; B: 10; C: 0; D: 0; E: 44; F: 5**. Verification levels are **read the result: 62; publisher metadata checked: 1; indirect: 3; unresolved lead: 5**. “Read the result” means the stated result or the corresponding construction was inspected, not that every proof in every cited work was independently checked. Bibliographic verification of one cited work does not imply full-text verification of that work.

Files are `middle_talks.json`, `middle_items.json`, `middle_problems.json`, `middle_references.bib`, `middle_corrections.csv`, this log, and `middle_audit.tex`, under `work/parts`. Reproducible code is in `work/parts/middle_code`. Source-PDF caches are outside that directory, under `work/source_cache/middle`; they are research intermediates, not proposed distributable artifacts.

The bibliography reuses `novikov1974periodic`, `dubrovinmatveevnovikov1976nonlinear`, and `milnor1968singular` from the cumulative bibliography. `dubrovinnovikov1974periodicity` is shared with early_records. `marchenko1975characterization` and `gesztesy1999infinite` are shared with the root agent. The remaining keys were checked against the cumulative key list before introduction. The final combined bibliography should deduplicate these shared entries by key.

## Passage boundaries and chronology

Catalogue dates and page ranges are preserved in the talk records. Item locators follow the actual source passage, not a mechanical slicing of overlapping catalogue ranges.

| Record | Catalogue date | Mathematical passage actually used | Editorial boundary or chronology decision |
|---|---|---|---|
| 342 | 23 September 1974 | P000564 opening | Gelfand's combinatorial-topology announcement and logarithmic integrals precede the Giusti lecture; Giusti is early_records' record341. |
| 343 | 23 September 1974 | P000566–P000568 | Explicitly a recap of Dubrovin; the entire-function proposal and Dubrovin divisor statement belong to its ending. |
| 344 | 30 September 1974 | P000569–P000571 | The gluing proof continues one page beyond the catalogue's P000570 ending. |
| 345 | 30 September 1974 | Topic heading P000569; detailed discussion P000573–P000574 | The detailed Polyakov/Sinai passage stands under the manuscript's 7 October heading. Preserve the catalogue date and explicitly record this displacement. It does not justify silently deciding whether there were two separate Polyakov presentations. |
| 346 | 7 October 1974 | P000572–P000573 upper portion | Local Newton boundary, local Milnor number and face-ring proof ingredient. |
| 347 | 7 October 1974 | One paragraph on P000573 | Arnold's residue formula, before the Polyakov passage; not the whole catalogue page range. |
| 349 | 21 October 1974 | P000579 upper portion | Global polynomial critical-point count, its Newton polytope at infinity, degree argument, Hochster, and toric remark. |
| 350 | 21 October 1974 | P000579 lower portion | Continuum gauge action, connection/curvature and Pontryagin-form dictionary. |
| 351 | 28 October 1974 | P000580–P000583 | The next meeting begins on P000584, so it is not included in the current-group lecture. |

Chronology affects classification. Novikov's stationary-to-finite-gap theorem was received 18 February 1974 and published in July 1974; the September quasimomentum/hierarchy recap is E. The reverse implication and the explicit divisor formula are in Dubrovin–Novikov's 1974 announcement, received 3 June, and retain A with that precise attribution. Kushnirenko's announcement was received 30 September 1974, before both October lectures, but appeared in 1975; it is the speaker's newly announced result, with submission/circulation and publication dates separated. Graev's detailed continuous tensor-product and logarithmic-kernel constructions were already published in 1973 and are E. Wilson's paper was published 15 October 1974, but its February 1974 CLNS262 preprint predates the recorded lattice-gauge discussion. Balian–Drouffe–Itzykson was received 3 June and published 15 November 1974.

## Mathematical coverage and area mapping

| Record | Items | Area | Distinct content retained |
|---|---:|---|---|
| 342 | 4 | Characteristic classes; special functions | Named combinatorial programme, Rogers antiderivative, erroneous Basel sign, correct golden-ratio definite integral. |
| 343 | 15 | Periodic spectral theory; integrable equations | Hill spectrum, finite-gap characterization, monodromy, bands, scalar closed-gap monodromy, normalization of spectral curve, Riccati variable, amplitude/phase, high-energy densities, quasimomentum, its variation, monodromy expression, divisor polynomial, entire-function programme, and Baker–Akhiezer divisor. |
| 344 | 10 | Algebraic topology; configuration spaces | Electric-field/scanning map, stable homology, classifying-space remark, signed cancellation topology and its corrected target, tangent-bundle scanning, stable manifold theorem, boundary disappearance, local disk calculation, and gluing method. |
| 345 | 10 | Mathematical physics; probability | Link holonomy, Gibbs measure, loop observable, planar integration, gauged spins, Euclidean continuation, Bessel specialization, pressure limit, phase criterion, and limited area/perimeter remark. |
| 346 | 6 | Singularity theory; commutative algebra | Local gradient multiplicity, Newton number, inequality/equality/genericity, edge discriminant, face ideal, Cohen–Macaulay proof ingredient. |
| 347 | 1 | Residues; algebraic geometry | Euler–Jacobi vanishing, with simple affine intersections and no roots at infinity. |
| 349 | 5 | Singularities; Newton and toric geometry | Total critical multiplicity, global Newton upper bound, gradient degree, normal semigroup algebra, unspecified Mumford/toric remark. |
| 350 | 3 | Differential geometry; gauge theory | Whole-curvature square, local connection forms, normalized Pontryagin representative. |
| 351 | 17 | Representation theory; current groups | Current group, finite evaluations, Abelian characters, uniform existence question, complementary series, almost-trivial coefficients, unidentified dimension, symmetric powers, endpoint quotient, uncertain signature sketch, dyadic refinement, multiplicity one, delta embedding, completed limit/extension, centered log Hilbert space, coherent vectors, and scalar cocycle. |

Definitions, constructions, questions, proof methods and explanatory remarks have separate occurrences when they make distinct assertions. Closely equivalent displays are grouped: e.g. the amplitude/phase formulas in343.8, the several local Newton dimensions in346.2, and the two group-spin energies in345.5. A named programme with no theorem is not inflated into several supposed theorems.

## Definite problems, residuals, and development decisions

* **GP-1974-10**: finite-gap spectra versus stationary KdV. Occurrences are 1973-326.15, **1974-340.7** (early_records) and1974-343.2. Solved in the stated real smooth periodic setting. The forward direction is Novikov; the converse is explicit in DN1974 §3. This is different from the supplementary-data inverse problem GP-1973-51 and finite-gap density GP-1973-52.
* **GP-1974-11**: signed particle configurations. The tentative sphere target is replaced by the quotient `(S^n × S^n)/ΔS^n`, with an n-fold based loop space. The source itself already changes to an unnamed 2n-dimensional target; McDuff's publication and Kallel's explicit attribution settle the identification. No new open sphere-equivalence conjecture is retained.
* **GP-1974-12**: local Milnor number from convenient Newton data. The lower bound and equality for face-nondegenerate germs are settled. The boundary does not determine the Milnor number of every degenerate germ.
* **GP-1974-13**: total isolated critical-point multiplicity from the global Newton polytope. The convenient polynomial and finite critical locus are explicit; equality follows from nondegeneracy at infinity. It is kept distinct from the more general mixed-volume theorem discussed elsewhere in the year.
* **GP-1974-14**: existence of a measure-invariant irreducible representation of the interval `PSL2(R)` current group in the uniform topology. Solved by VGG1973. Only the titles of1969-180.1/.2 and GP-1969-01/-02 are available in the supplied prior index, so the new precise occurrence is related in prose without merging or declaring the broader earlier questions solved.

The precise formulation of GP-1974-14 also requires **full interval support**: currents supported in every nonempty open subinterval act nontrivially. This is an explicitly marked reconstruction of “everywhere,” supported by positive Lebesgue measure on every such interval in the VGG construction. Measure-preserving homeomorphisms of an interval alone form too small a symmetry class to exclude finite evaluation examples; the full-support condition prevents that unintended weakening.

No definite **C or D candidate** survived the formulation and source checks. This does not assert that all surrounding subjects are complete. The following entries are F because the notebook does not fix the question sufficiently:

1. **343.14**, arbitrary entire `R,P` of order one: missing normalization, zero/divisor conditions, reality, spectral variable and global regularity. Marchenko–Ostrovskii and Gesztesy give meaningful specified inverse frameworks, but they do not turn this wording into an exact theorem. Root's local compatibility audit proves an elementary criterion and a common-factor obstruction; it is explicitly not a solution of an unspecified global classification.
2. **345.10**, two phases with area/perimeter behavior: dimension, group, matter, action, loops and limit are unspecified. The adjacent planar U(1) example has an area law at every finite positive coupling and analytic pressure. No Yang–Mills mass-gap conjecture is substituted.
3. **349.5**, “Mumford—toric embeddings”: a method is recognizable but no particular theorem or fan is supplied.
4. **351.7**, Kolmogorov dimension/Plancherel multiplier/“one Japanese”: no definition or normalization is given. Formal degree, spectral multiplicity and entropy dimension cannot be conflated. Araki is not identified merely because he is Japanese and appears in current-group references.
5. **351.10**, analytic-continuation negative-square sketch: kernel normalization, domain and quotients are absent. The standard positive continuation for1<λ<2 is verified; the later negative-square counts are not silently promoted to a theorem.

`middle_audit.tex` contains original writeups of **classical verification calculations**, marked `\ours` and `\oursComputed`, without novelty claims. The golden-ratio integral is proved from the Rogers reflection and five-term equations. The Bessel/Haar proposition specifies a planar disk, free boundary, normalized link measure, plaquette count and character convention. These calculations are annotations to E/B/F source items, not Stage2 advances on newly open C/D problems.

## Scan-based corrections and mathematical safeguards

The Russian transcription was the reading authority and the scans were consulted for doubtful signs, diagrams and formulas. Pages directly inspected include P000564,566,567,568,570,572,573,579,581,582,583; P000583 establishes the Cauchy-density error visually. Source boundaries also follow the dated headings in the adjacent Russian page files.

The first integral onP000564 has the positive sign in the handwriting; its value must be negative. The second, symmetric integral really has limits ±(√5−2) and value −π²/6 and is **correct**. It was not “corrected” merely because the first was wrong.

OnP000566, `u(y)` is a faithful error for `u(x)`, and closed gaps do not make all extrema +1. OnP000567 the radical's drawn scope is ambiguous; the whole quotient must be under the radical for single-valuedness. The negative sign in the variational derivative is consistent with the constant-potential check `p=T√(E−u0)`. The opened English DN1974 §3 prints a positive sign; the 1976 survey and this elementary check resolve the sign under the explicitly fixed convention.

The based condition in the configuration-space targets is mathematically necessary. Fixed boundary values of sections and disappearing boundary particles must not be interchanged without changing the target. The general relative McDuff theorem has an indirect/partial verification here because the original full text was blocked; the disk calculation was read directly in Kallel.

OnP000573, Arnold's numerator is legibly `R_(n−4)` both in the formula and in the explanatory bound. This is a valid weaker degree bound, under the stated hypotheses. It is retained, while the classical sharp allowance `deg R ≤2n−3` is supplied as a comparison. Familiarity with the sharper theorem is not evidence of an OCR error.

The angular lattice specialization makes the `I0` expression an Abelian formula; normalized fundamental-trace SU(2) gives `I1(2β)/β`. Site count and plaquette count differ at finite volume. A Fourier transform alone is not imaginary-time continuation. The entire curvature, not just the commutator, must be squared in the continuum action. `SU(2)` denotes a group and `su(2)` its Lie algebra. Component contractions require an exterior product and a normalization before they represent a Pontryagin class.

The Graev line model subtracts the Cauchy density in **t**, not **x**. The latter is constant in t and cannot have finite integral. The exponential kernel requires t1 and t2 in its two factors. The source's real-label convention does not require a complex conjugate on each label; a complex-label version does. The circle-valued Abelian example needs the period condition `ell(1)∈Z` on the interval. The delta embedding belongs to a completed kernel Hilbert space, not ordinary L2.

## Primary sources opened and exact verification locators

Web reference IDs below are retrieval-log identifiers, not substitutes for the stable URLs. The root should reopen any source it cites directly in user-facing web citations.

| Key | Stable opened source | Verification / source locator | Retrieval identifiers |
|---|---|---|---|
| gabrielovgelfandlosik1975computation | https://www.mathnet.ru/eng/faa2234 | Publisher metadata; received2Dec1974; no exact theorem match claimed. | turn32view3; turn123view0 |
| gabrielovgelfandlosik1975calculus | https://www.mathnet.ru/eng/faa2259 | Publisher metadata; received31Mar1975. | turn32view2; turn123view1 |
| zagier2007dilogarithm | https://www.maths.dur.ac.uk/users/herbert.gangl/zagier_dilog.pdf | Full chapter; ChapterII §1.A, pp23–24, Rogers derivative/reflection/five-term/negative continuation. | turn32view0; turn42view0; turn136view2 |
| nist2026polylogarithms | https://dlmf.nist.gov/25.12 | Official equations25.12.1–3. | turn29view3 |
| novikov1974periodic | https://www.mathnet.ru/eng/faa2358 ; https://www.mathnet.ru/php/getFT.phtml?jrnid=faa&option_lang=eng&paperid=2358&what=fullt | Metadata and Russian original opened; §2 Thm2.1. Early/root independently read full relevant result; July publication checked by root at Springer. | turn38view3; turn123view3; early turn118view0/turn120view0 |
| dubrovinnovikov1974periodicity | https://people.sissa.it/~dubrovin/Papers/1974/dubrovin_novikov_1974_dan.pdf | Full author English text opened; §3 divisor formula, converse and quasimomentum identity read; received3Jun1974. Positive variational sign is not accepted without convention audit. | turn106view0; turn107view1 |
| dubrovinmatveevnovikov1976nonlinear | https://people.sissa.it/~dubrovin/Papers/1976/dubrovin_matveev_novikov_1976.pdf ; https://www.mathnet.ru/eng/rm3642 | Full English survey; Chapter2 §1 formulas2.1.10–19 and divisor statement; §§2–3 stationary and inverse framework. | turn14view0; turn10search2 |
| marchenko1975characterization | https://www.mathnet.ru/eng/sm3807 | Root opened metadata and English PDF, Thm5.1 pp535–536 and proof; received3Feb1975. | Root research log and root_references.bib |
| gesztesy1999infinite | https://arxiv.org/html/solv-int/9907009v1 | Root checked v1 submission7Jul1999; Eq2.10, Hyp3.1–3.2, Eq3.14 and lemmas. | Root research log and root_references.bib |
| segal1973configuration | https://webhomes.maths.ed.ac.uk/~v1ranick/papers/gbsloop.pdf | Full paper; §1 p213 electric-field map and stable homology. Repository wrapper pagination differs from actual213–221. | turn32view1; turn58search7; turn59view1 |
| mcduff1975configuration | https://www.sciencedirect.com/science/article/pii/0040938375900385 ; https://celebratio.org/McDuff_D/article/412/ | Publisher/author metadata; full paper inaccessible. Exact signed target checked in Kallel, not fabricated as full McDuff reading. | turn14view4; turn20view1; turn58search0 |
| kallel1998particles | https://arxiv.org/pdf/math/9810067 | Full primary preprint; Thms1.1,1.3, §6, Prop9.1, Lemma11.1, Example11.5. Earlier versionSep1996; v111Oct1998. | turn45view0; turn99view1; turn100view5–6; turn101view7–8 |
| kushnirenko1975newton | https://www.mathnet.ru/eng/faa2223 ; https://www.mathnet.ru/php/getFT.phtml?jrnid=faa&option_lang=eng&paperid=2223&what=fullt | Complete two-page Russian original read; ThmsI–II, genericity and §8. | turn14view1; turn54view0; turn58view0; turn65view5; turn123view2 |
| kouchnirenko1976polyedres | https://www.math.ucdavis.edu/~deloera/MISC/LA-BIBLIO/trunk/Kouchnirenko.pdf | Full original opened; first two printed pages visually inspected, §1.1 Eqs1–3 and introductory local/global statements. Whole proof not independently audited. | turn14view2; local first-page images |
| hochster1972invariants | https://annals.math.princeton.edu/1972/96-2/p05 ; https://www.math.ucdavis.edu/~deloera/MISC/LA-BIBLIO/trunk/Hochster.pdf | Publisher metadata; original pp318–319 viewed; normal monomial semigroup CM theorem onp318. | turn65view0; turn67view1; local first-page images |
| khovanskii1978eulerjacobi | https://www.math.toronto.edu/askold/1978-UMN-6-english.pdf | Both pages read; classical degree corollary, generalized Laurent result and toric proof. | turn45view2; turn65view4; turn123view4 |
| milnor1968singular | https://press.princeton.edu/books/ebook/9781400881819/singular-points-of-complex-hypersurfaces-pdf | Publisher record reopened; cumulative key retained. Direct current-run degree assertion checked in Kouchnirenko §1.1. Prior cumulative full-book verification is distinguished from this run. | turn86view1 |
| wilson1974confinement | https://journals.aps.org/prd/abstract/10.1103/PhysRevD.10.2445 ; https://hep.physics.uoc.gr/Erasmus-IP-2013/files/lectures/Rabinovici/Wilson.pdf ; https://inspirehep.net/literature/89145 | Full primary article; §§I–III, loop criterion/strong coupling; APS dates and INSPIRE February1974 CLNS262 preprint. | turn38view1–2; turn67view0; turn79view0; turn132view0–2 |
| baliandrouffeitzykson1974gauge | https://doi.org/10.1103/PhysRevD.10.3376 ; https://www.academie-sciences.fr/pdf/membre/BalianR_bio0708.pdf | APS metadata/abstract, including received3Jun and published15Nov1974. Author bibliography confirmspp3376–3395. Original proof not read. | turn82view1; turn111view0; turn136view0 |
| hirasawa2020complex | https://d-nb.info/1220202665/34 | Complete primary article; AppendixA.1 EqsA6–A11, AppendixA.3 A27. Exact modern verification, no priority claim. | turn82view2; turn83view0–1 |
| ruelle1967variational | https://www.ihes.fr/~ruelle/PUBLICATIONS/%5B18%5D.pdf | Full6-page paper; Thm1 p325 finite-state pressure. Compact-variable extension stated editorially, not misquoted. | turn86view0 |
| yangmills1954conservation | https://journals.aps.org/pr/pdf/10.1103/PhysRev.96.191 | Full original5-page paper; Eqs3–4 and Lagrangian; publisher history. | turn65view3; turn66view0; turn67view2 |
| chernsimons1974characteristic | https://annals.math.princeton.edu/1974/99-1/p03 ; https://math.mit.edu/juvitop/pastseminars/notes_2019_Fall/Chern-Simons.pdf | Full original; §2 Eq2.10, Thm2.12, Eq5.7. | turn65view1–2; turn79view1 |
| vershikgelfandgraev1973functions | https://www.mathnet.ru/eng/rm4953 ; https://www.mathnet.ru/php/getFT.phtml?jrnid=rm&option_lang=eng&paperid=4953&what=fullteng | Full46-page English primary text; Introduction, §1.1, Thms1.4–1.7, §§2–3, §6.1/6.3, Thm6.2. | turn29view2; turn32view4; turn99view0; turn100view0–4; turn101view0–6; turn105view0–6; turn106view2–5; turn111view1 |
| gelfandgraev1968quaternion | https://www.mathnet.ru/rus/faa2751 | Primary metadata; received16Oct1967, published1968. The VGG1973 introduction and reference1 identify its precursor role. | turn116view0; turn107view0 |

## Search history and unsuccessful leads

Searches used both available engines, with primary/publisher verification after discovery. Query families included the exact Russian and English names/titles for GGL combinatorial classes, Rogers/golden-ratio dilogarithm values, Novikov and Dubrovin finite-gap equations, Segal electric-field configurations, McDuff positive/negative particles, Kushnirenko local/global Newton numbers, Hochster normal monomial rings, Arnold Euler–Jacobi residues, Wilson/Polyakov lattice-gauge chronology, Balian–Drouffe–Itzykson gauge–matter coupling, two-dimensional character expansions and normalized Haar factors, and VGG current groups.

Specific uncertain-lead queries included `"Vershik" "Kolmogorov dimension" representations Plancherel`, `"Kolmogorov dimension" "Plancherel"`, `"Колмогорова" "размерность" "представлений" "Планшереля"`, and `"Kolmogorov dimension" "unitary" representations`. Results concerned unrelated metric dimensions, formal degrees or later Plancherel questions; none identified the notebook's author or kernel. These were not used as substitute references.

McDuff's original PDF at `https://core.ac.uk/download/pdf/81183648.pdf` was indexed but returned HTTP403 on opening and ordinary download. Publisher full text was also blocked. The original paper is therefore metadata-verified only; Kallel is the directly read mathematical source for the signed target. The VGG English PDF was readable through the search-service PDF reader; a local urllib download returned403, so the successful web reader was retained and no bypass attempted. Math-Net's English faa2751 endpoint returned a Unicode-decoding error; the ordinary Russian primary endpoint worked.

A candidate PDF under `helper.ipam.ucla.edu/...gsiws3_19529.pdf` turned out to be modern slides rather than Wilson's1974 original and was rejected as the primary source. The actual journal scan was subsequently opened at the University of Crete lecture-resource URL above. The DOI endpoint for Zagier's chapter was inaccessible, while its full author-hosted chapter was readable; the bibliography uses the verified full-text URL. Search absence is not described as proof that a result was never published.

## Reproducibility and validation

`middle_code/build_middle.py` writes a checkpoint after each record and then applies documented bibliographic/chronology refinements. It preserves source numbering and locates every passage. `finalize_bibliography.py` fills the six shared/reused entries by exact key and checks consecutive IDs, permitted enum values, cited/ref-key inclusion and control characters. Final checks passed with71 items,5 problems and25 bibliography keys. Two accidental Python tab escapes in `textquotesingle` were fixed; no control characters remain in item fields.

`check_dilogarithm.py` and `check_dilogarithm.out` preserve the numerical second check. A90-digit Decimal series gives −1.6449340668482264364724151666460251892189499012067984…; the180-term truncation bound is below1.51×10^−231, separately from rounding. Transformed composite Simpson calculations with20000 and40000 subintervals have double-precision errors approximately−7.37×10^−13 and−4.66×10^−14. The proof, rather than numerical agreement, establishes the exact identity. Golden-ratio substitutions in the five-term relation were checked separately.

`compile_middle.py` made a private `work/build_middle` copy. The kit's schema/bibliography checks passed. The default xelatex process then stopped **before reading the LaTeX source** because the environment lacked `xelatex.fmt`; it is not reported as a successful compile. The root requested that TeX setup be left to its designated agent, and no further setup was attempted. In the private validation copy only, the cross-part occurrence340.7 was omitted to satisfy the kit's same-year reference check; the actual deliverable retains it. Final combined compilation remains the root's responsibility.

The root's entire-data audit was independently reviewed: the Riccati residual, Q sign, exponential reconstruction, common-factor invariance, Wronskian identity and the nonconstant `P=E+x^−2, R=E^3, u=2x^−2` example agree. No substantive correction was found. This cross-check does not change the F classification of343.14.

During the root's combined compile, a raw PDE in343.2's reconstruction was found outside math mode. The stable generator now wraps that display,344.5's `Y_n`, and two analogous correction-row expressions in math delimiters. A reproducible scan added to `finalize_bibliography.py` checks every JSON string and each raw-LaTeX CSV field for unescaped underscore, percent or caret outside math; the final scan passes. Prose-only spacing was corrected through targeted word patterns, including received18, publishedJuly, ClassA and to23, without changing mathematical tokens. The root was notified to rebuild from these stable parts.

A subsequent combined-compile check found section symbols joined to Roman numerals (`\SIII` and `\SII`). The generator now inserts a separating space, and the corresponding audit citation was repaired directly. All five affected item citations and the one audit citation are fixed. The final command-name inventory contains only standard LaTeX/AMS commands and supplied style macros; an apparent `\s` is the second slash of a legitimate matrix row break before `s(T)`, not an undefined control sequence. The validation script now rejects any recurrence of a joined Roman-section command.

## Suggested structured locators

For subsequent years, separate `catalogue_pages` from `passage_pages` and add an optional source locator with page, heading/speaker, paragraph or displayed-formula ordinal, and diagram identifier. The present `pages` strings already carry these locators in prose. A separate manuscript-date field would record displacement such as record345 without overwriting the catalogue date. Bibliography records would benefit from a per-item locator and verification provenance object, since one item can cite a directly read modern theorem and a metadata-only original paper. Typed `related_problem` links would avoid forcing the precise351 existence construction to share an inadequately known1969 problem ID.
