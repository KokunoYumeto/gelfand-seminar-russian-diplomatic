# GY1976: critical-companion research and production report

**Status date:** 10 November 2026. **Deliverable scope:** the 23 records and 55 scans supplied for the nominal academic year 1976–77, with a separately identified 1977–78 record retained because it was explicitly requested.

## 1. Outcome and scope

The chapter contains **@@TOTAL@@ mathematical occurrences**, **@@PROBLEMS@@ problem-index entries**, **@@REFERENCES@@ bibliography records**, and **@@CORRECTIONS@@ corrections or provenance annotations**. Every requested catalogue record is represented. The original Russian and English transcriptions are preserved unchanged. The companion distinguishes the notebook wording, the modern statement, editorial reconstruction, publication history, present status, and the strength of verification.

There are **@@STRICT@@ occurrences in the 1976–77 core** and **23 occurrences in the miscatalogued record 437**. Its manuscript date is **13 February 1978**, although the supplied catalogue gives 13 February 1977. The structured date has therefore been corrected to `1978-02-13`, and its occurrence IDs are `1977-437.n`, as required by the rule that the prefix denotes the first year of the actual academic year. Its two new problem IDs likewise begin `GP-1977`. The original catalogue value remains in the summary, corrections and source-scope sidecar. The supplied builder already supports adjacent academic-year prefixes; no validation rule was weakened to accommodate this correction.

The generated chapter consequently names both academic years. This is a truthful description of the supplied package, not a claim to cover the whole of 1977–78. Record 437 is an explicit chronological appendix. Its ten A and thirteen E items are excluded from the core column below.

### Historical classification

@@CLASS_TABLE@@

The letters describe historical fate. They do not measure correctness, novelty or difficulty. In particular, E may describe an already circulating physical programme, a classical theorem with an omitted hypothesis, or a known construction copied with a sign error. An F records failure to identify a determinate assertion from the available evidence; it does not mean that an identified problem remains open.

### Coverage by record and nominal speaker

@@RECORD_TABLE@@

Source order is preserved, including the order **414, 416, 415, 417** around P000699. Gelfand's remarks precede Vershik on that page. The manuscript heading 28 March 1977 is used for the latter where it governs the same uninterrupted entry; the supplied catalogue's 4 April date is retained in the provenance record. Speaker headings that contain initials in conflict with the matched publications are explicitly qualified rather than silently reassigned.

### Counts by attributed speaker

@@SPEAKER_TABLE@@

This table uses an item's explicit speaker field when present, otherwise the record's speaker. It therefore differs intentionally from a simple grouping by catalogue record. Attribution of a remark does not imply that its publication or discovery belongs to that person.

### Counts by mathematical area

@@AREA_TABLE@@

Areas are editorial navigation labels, with one primary area per occurrence so that the counts add to the total. They are stored in `code/source_scope.json`, rather than adding unprescribed keys to the seven core files. Cross-disciplinary material can acquire secondary website tags without changing these historical counts.

### Independent assessment dimensions

@@ASSESSMENT_TABLES@@

These counts make the evidential limits inspectable. “Read the result” means that a relevant theorem, construction, formula or argument was inspected, not that every page of the cited book was read. A publication can be verified bibliographically while its particular theorem remains an indirect or unresolved lead. The bibliography's `note={verified}` records opening an actual URL or DOI; it is not a substitute for the occurrence-level verification field.

## 2. Manuscript boundaries and difficult identifications

The most consequential difficulties were source boundaries, mathematical quantifiers and chronology, rather than lack of recognizable topics.

**Catalogue page spans are envelopes.** Gindikin's talk continues through P000662; the September 13 sequence then contains Fuchs, a brief Kirillov intervention and Arnold. The announced Kirillov heading about superalgebras is not a surviving independent exposition. Novikov continues onto the top of P000669, and Migdal begins below him. Bernstein's October talk begins at P000670, while P000673–P000674 retrospectively incorporate notes associated with I. Dorfman's notebook. Those provenance distinctions are retained in the corresponding record summaries.

**The package contains adjacent material.** Of the 55 supplied scans, 46 pages, P000659–P000704, belong to the 1976–77 core; four, P000753–P000756, contain the corrected February 1978 lecture; five are adjoining context. P000705–P000706 begin the next academic year's Drinfeld material. P000752 is a preceding physics tail, and P000757–P000758 start a separately dated lecture on 27 February 1978. These pages were read for boundaries and clarification, but their new mathematical assertions are not manufactured into occurrences of the requested talks. The complete page ledger is `code/source_page_ledger.csv`.

**Names do not establish identity.** The catalogue's V. N. Popov does not match the D. A. Popov on the exact 1975 papers. The detailed mathematical agreement establishes a publication match; it does not, by itself, prove who delivered the lecture. Likewise, the Tyurin publication author's initials are checked against, and distinguished from, the catalogue form. Author authority records are needed in a future data model.

**A formula can settle what a title cannot.** The P000662 projector differs from the published expression by a nonconstant trace factor. The superdeterminant appears with opposite conventions in adjacent notebook formulas. The zeta symmetry requires completion factors. A flatness equation in the Manin material has a sign error that is also present in the printed survey. These are mathematically meaningful discrepancies; they cannot be repaired by citing a paper with a similar title.

**The quantifiers determine the problem.** Point equivalence of a second-order ODE is an assertion on an open set, not merely along a reference solution. A microlocal assertion needs localization in both point and direction. A theorem about algebraically admissible line complexes cannot be promoted to a classification of every geometric family of lines. The inverse spectral correspondence needs its rank, smoothness, local parameter and general-position assumptions. The modern statement and reconstruction fields make each of these choices explicit.

## 3. Which searches located the publications

The most productive route was to combine a distinctive formula or construction with the speaker and date, find a short primary announcement or an author-hosted text, and then work backwards through its references. Math-Net supplied dependable Russian/English publication metadata and short Soviet originals. Numdam supplied dated seminar texts and scanned primary papers. Author-hosted copies were especially valuable for BGG, the Bernstein–Leites Stokes theorem, Manin's survey, Duistermaat–Kolk–Varadarajan and Krichever. arXiv supplied precise first-posting dates for later reconstructions. The individual research logs record the actual URLs, locators, unsuccessful leads and depth of reading.

| Notebook thread | Decisive publication or circulation evidence | Editorial consequence |
|---|---|---|
| Gelfand–Gindikin domains and projectors | Gelfand and Gindikin (1977), equation 22 and Proposition 9; received 6 June 1977 | Exact later construction, with a missing factor in the notebook kernel |
| Arnold's point geometry | Cartan (1924), §§VII–VIII, checked against Kruglikov's 2008 preprint/2009 chapter | Classical E, with the local criterion stated on its proper domain |
| Poincaré superalgebra | Likhtman's author account reproduces a preprint passed for printing on 12 April 1971 | The 2001 reprint is evidence for earlier circulation, not a 2001 discovery |
| Superintegration and Stokes | Bernstein and Leites (1977), §§5, 11–12; received 6 October 1976 | Precise publication match; manuscript receipt is not silently treated as public circulation |
| Einstein–Yang–Mills construction | Popov and Daikhin (1975), Lemma 1 and Theorem 2 | E, including the arbitrary fibre bilinear form in the projected equation |
| Euler products and affine algebras | Demazure's Bourbaki exposition, dated June 1976, printed in 1977 | Circulation before the November talk, even though the collection bears a later year |
| Manin bimodules and nodal curves | Manin (1978 Russian; 1979 English), Chapter III, §§2, 5–6 | Exact reconstruction with documented sign and filtration discrepancies |
| Duistermaat's index formula | Goulaouic–Schwartz exposition, 29 May 1974 | E rather than a new 1977 result |
| Admissible line complexes | Gelfand and Graev (1968), §5, Theorem 6 and its corollary | A pre-existing theorem with restricted algebraic hypotheses |
| Young-diagram fluctuations | Kerov's 1993 announcement and Ivanov–Olshanski's 2002 account, arXiv posting 2003 | Separate limit shape from fluctuation theorem and distinguish the limiting covariance |
| Representation packets | Tyurin (1978), Chapter II, §2, Exercise 10 | A source-backed check against the notebook's universal packet claim |
| Exterior modules and bundles | Bernstein–Gelfand–Gelfand (1978), Theorem 1 and remarks; manuscript received 10 January 1978 | Exact match after correcting the lecture date; distinct from the related Beilinson theorem |

A publisher's modern “published online” timestamp was not treated as the original publication date. A receipt or presentation date was recorded separately from a verified public lecture or preprint date. Where first circulation could not be established, the text reports what is known without inventing it. The citation year follows the edition actually cited; thus the key `manin1978algebraic` points to the English 1979 edition while recording the 1978 original.

The negative searches are deliberately narrower than claims of nonexistence. For example, an identified paper on horospherical inversion does not settle the source's unspecified function-space range question. Identification of van Asch and a plausible modular-form paper does not verify the unexplained exponents 39 and 45. The continuous-order-matrix phrase is not silently replaced by a famous modern operator-algebra problem. These cases remain F, with the reason visible.

## 4. Development decision and mathematical checks

**No C/D item qualified for a new research development.** This is a conclusion about the material supported by the notes and the searches, not a claim that every subject discussed is closed. Most definite questions match established results; the remaining fragments do not supply enough hypotheses for a bounded new theorem. The general word “classify” in record 437 is answered in the specific stable-module sense stated in the lecture and is not inflated into the classification of all later vector-bundle moduli problems.

The required development file nevertheless contains substantial *critical verification*. It explicitly says that these are annotations, counterexamples and checks of the literal record, not newly solved open problems. Every result proved or computed in the development section is marked with the supplied `\ours` or `\oursComputed` convention. Full arguments, rather than sketches, accompany the central corrections.

| Audit | First derivation | Independent check and limitation |
|---|---|---|
| Discrete-series kernel | Sum the elementary weighted geometric series and rewrite using the trace | A separate rational identity and exact finite sums with analytic tails; the trace-plus-two factor cannot be absorbed into a constant |
| ODE normalization | Expand the full point-transformation chain rule to quadratic order | A concrete polynomial transformation and the Lie–Tresse invariant; vanishing along one solution does not imply flatness on an open set |
| Projective vector-field invariant | Derive the Schwarzian transformation law | Two independent Möbius substitutions, with exact arithmetic |
| Auxiliary-field elimination | Solve the two algebraic Euler equations | Complete two squares and substitute three integer parameter sets |
| Real spin matrices | Explicit real Clifford representation | All anticommutators and charge-conjugation bilinear symmetries checked |
| Berezinian and super-coordinate shift | Check the diagonal Berezinian and expand the nilpotent circle and half-line coordinate changes | Independent special cases expose the reciprocal and missing divisor |
| Fourth-order Lax equation | Compose differential operators by the Leibniz rule | Independently act on an exponential test function; three polynomial coefficient instances check every operator coefficient |
| Flatness sign | Commute the two specified connections | A scalar example satisfies the corrected equation and contradicts the printed plus-sign formula |
| Unitary representation packets | Use the harmonic logarithm of a nowhere-vanishing holomorphic section | Re-derive on the universal cover; trivial versus nontrivial characters works for every compatible complex structure and remains a counterexample under a change of marking |
| Exterior-module acyclicity | Construct a contraction with an explicit covector | Re-derive from a complementary subspace; 18 exact matrix cases check the implementation, while the proof handles every dimension |
| Twist and inverse grading | Track both exact sequences and internal degree shifts | Chain and cochain indexing agree; the point case exposes an omitted grading convention without contradicting BGG |

The independently authored check scripts and their complete outputs are included. Finite calculations are used to check implementations and counterexamples, never to infer a theorem for all dimensions or all parameter values. The Tyurin counterexample requires compactness and unitarity, and its proof states both. The inverse BGG point example targets the raw unshifted kernel in the sketch; it is not presented as a failure of the published correspondence.

## 5. Earlier years and the problem index

The supplied `previous_index.md` was searched by objects, constructions and hypotheses, not merely by author name. Earlier occurrence IDs are retained in problem entries only when they refer to the same definite question. The higher-rank inverse problem, for example, reuses its earlier ID while separating an abstract correspondence from a later effective reconstruction. The Krichever and Manin threads also support explicit connections to rank-one spectral-curve constructions. The original index is supplied in `code/inputs` so these decisions can be audited.

The main contextual routes are the 1975 Euler/Macdonald sequence, the 1975 supergeometry talk, the earlier colour-gauge and confinement discussion, and the spectral-curve/inverse-operator sequence. Those routes need not merge problem identities. The affine Serre–Quillen–Suslin question and the projective BGG question differ in base space and demanded answer. The earlier continuum-confinement problem is not declared solved by a new exposition of colour gauge theory. Likewise a general mention of Gelfand–Fuchs cohomology does not become a recurrence of a particular Hamiltonian-cohomology problem.

### Problem entries included

@@PROBLEM_TABLE@@

New problem identifiers are stable labels, not an assertion that the questions were first posed in this seminar. Resolved questions are useful entries because they let a reader follow the notebook's question to its precise answer. Sparse numbering preserves the independently assigned segment identifiers; it carries no mathematical significance.

## 6. What the classification misses and proposed data changes

The current schema's separate correctness, match and verification fields do useful work, but this year exposes additional distinctions.

1. **Keep catalogue and manuscript dates separately.** Add `catalogue_date`, `manuscript_date`, `date_basis`, `date_confidence`, `academic_year` and `included_by_request`. A corrected date should not erase the original finding aid. A false date must not force false occurrence IDs.
2. **Represent boundaries and sources explicitly.** Add precise page regions, source-record envelopes, transcription offsets and an `adjacent_context` role. A page can end one talk and begin another. A year heading should not acquire mathematical content simply because its catalogue envelope overlaps lectures.
3. **Separate person identity from the printed name.** Preserve `catalogue_speaker`, `manuscript_speaker`, an optional verified person ID, and the basis for reconciliation. The Popov discrepancy cannot be solved by editing initials to fit a publication.
4. **Give source matches their own records.** A source link should include the exact theorem/equation locator, original and translated editions, receipt/publication/circulation dates, access date, reading depth and the scope of the match. One scalar `publication_match` field cannot express a source that proves a nearby corrected theorem but also reproduces an error.
5. **Model the relation between assertions.** Distinguish literal statement, corrected statement, special case, counterexample, proof implementation and thematic context. A/B/E and literal correctness are orthogonal; “false as written” should never disappear inside a favourable historical label.
6. **Separate critical verification from new development.** The available value `annotated` is used for these checks. A future `development_kind` could distinguish reconstruction, counterexample, exact computation and genuinely new progress on a C/D question without changing the historical class.
7. **Add typed cross-year links.** Use `same_problem`, `prerequisite`, `same_construction`, `contrast` and `context` relations, each with a short reason. A single problem identifier should not be overloaded to carry every thematic connection.

The seven core files retain the prescribed field sets. The extra scope and area information is supplied as sidecars in `code/`; these are proposals for future ingestion, not undocumented changes to the chapter format.

## 7. Website presentation for this year

A reader entering a talk should first see its manuscript date, actual source pages, a two-paragraph orientation and a visible distinction between the scan, diplomatic Russian, translation and companion. Provenance alerts should appear immediately for records 407, 415, 417 and 437 and for heading-only records. The 1978 appendix needs a persistent academic-year badge so it cannot be cited accidentally as a 1977 announcement.

At an item, offer four clearly named destinations: **Notebook**, **Precise statement**, **Fate and source**, and **Status and critical check**. The notebook view should open the relevant scan region alongside both transcriptions. The source view should jump directly to the theorem or equation locator, show the edition and date distinction, and expose whether the result or only metadata was read. A compact badge can carry A–F; it must not replace the correctness and confidence indicators.

The most useful local links are from the erroneous kernel to its full derivation; from the Berezinian convention to its later use; from the Manin flatness formula to the notebook/publication comparison; from the Young-diagram fluctuation claim to the covariance and scaling; and from Tyurin's packet assertion to the checked rank-one counterexample. The problem index should make the earlier inverse-construction occurrences one click away, while contextual links lead separately to 1975 Euler products, supergeometry and gauge theory.

Search should index Russian wording and mathematical synonyms as well as English titles, including “proper/faithful module,” “geyseron,” “admissible complex,” and “packet.” Filters by historical class, literal correctness and verification depth should remain independent. A reader selecting “unidentified” should see the missing data and search trail, not a misleading list of open problems.

## 8. Reproduction and validation

The archive contains the seven core files, this report, the generated chapter, the test driver and PDF, the supplied builder/style, the attached source package, editorial authoring data, exact-check programs and outputs, source logs and machine-readable validation results. Downloaded third-party paper PDFs used only for inspection are not redistributed; their verified URLs and locators are in the bibliography and research logs.

From the extracted `GY1976` directory, with Python, SymPy and a working XeLaTeX/BibTeX installation:

```bash
python code/validate_chapter.py .
python build_chapter.py GY1976
xelatex GY1976_test
bibtex GY1976_test
xelatex GY1976_test
xelatex GY1976_test
python code/critical_checks.py --output code/output/critical_checks.json
python code/early_checks.py
python code/middle_checks.py
```

`code/compile_chapter.py` provides the same four TeX passes with captured logs. In the supplied runtime, the TeX distribution files were installed but its generated format/database configuration was incomplete. The wrapper generated a local format/cache and did not modify the system installation. This environment repair affects no mathematical content or chapter schema.

@@BUILD_RESULT@@

The validation checks coverage, source order, exact field sets, consecutive occurrence numbers, the corrected academic-year prefix, problem backlinks, cited-key integrity, bibliography verification markers and correction categories. It does not purport to prove the historical identifications; their evidence is in the source logs and occurrence text. Visual inspection checks the produced pages, displayed formulas, references and source labels. The manifest records archive file hashes so later changes can be distinguished from the delivered version.

## Selected primary references

The complete bibliography is `GY1976_references.bib`; the following entries identify the central findings discussed in this report.

- Bernstein, I. N., Gel'fand, I. M., & Gel'fand, S. I. (1978). Algebraic bundles over Pⁿ and problems of linear algebra. *Functional Analysis and Its Applications, 12*(3), 212–214. https://doi.org/10.1007/BF01681435
- Bernstein, I. N., & Leites, D. A. (1977). Integral forms and the Stokes formula on supermanifolds. *Functional Analysis and Its Applications, 11*(1), 45–47. https://doi.org/10.1007/BF01135531
- Cartan, É. (1924). Sur les variétés à connexion projective. *Bulletin de la Société Mathématique de France, 52*, 205–241. https://doi.org/10.24033/bsmf.1053
- Duistermaat, J. J. (1974). L'indice de Morse dans le calcul variationnel. *Séminaire Goulaouic–Schwartz, 1973–1974*, Exposé 25, 1–13. https://www.numdam.org/item/SEDP_1973-1974____A23_0/
- Gel'fand, I. M., & Gindikin, S. G. (1977). Complex manifolds whose skeletons are semisimple real Lie groups, and analytic discrete series of representations. *Functional Analysis and Its Applications, 11*(4), 258–265. https://doi.org/10.1007/BF01077140
- Gel'fand, I. M., & Graev, M. I. (1968). Complexes of straight lines in the space ℂⁿ. *Functional Analysis and Its Applications, 2*(3), 219–229. https://doi.org/10.1007/BF01076123
- Ivanov, V., & Olshanski, G. (2002). Kerov's central limit theorem for the Plancherel measure on Young diagrams. In S. Fomin (Ed.), *Symmetric functions 2001: Surveys of developments and perspectives* (pp. 93–151). Kluwer. https://arxiv.org/abs/math/0304010 (Author preprint posted 2003.)
- Manin, Yu. I. (1979). Algebraic aspects of nonlinear differential equations. *Journal of Soviet Mathematics, 11*(1), 1–122. https://www.its.caltech.edu/~matilde/ManinAlgAspectsPDE.pdf (Russian original published 1978.)
- Popov, D. A., & Daikhin, L. I. (1975). Einstein spaces and Yang–Mills fields. *Doklady Akademii Nauk SSSR, 225*(4), 790–793. https://www.mathnet.ru/eng/dan39441
- Tyurin, A. N. (1978). On periods of quadratic differentials. *Russian Mathematical Surveys, 33*(6), 169–221. https://doi.org/10.1070/RM1978v033n06ABEH003882
