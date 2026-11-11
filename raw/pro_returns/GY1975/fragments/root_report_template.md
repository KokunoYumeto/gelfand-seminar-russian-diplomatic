# GY1975 critical companion: research and verification report

**Coverage:** records 363–396, academic year 1975–76; attached source pages P000603–P000658.  
**Status date:** 10 November 2026.  
**Deliverable:** the seven chapter data files, generated chapter and PDF, reproducible computations, build tools, and audit records.

## 1. Coverage and counting conventions

The chapter covers all **34 catalogue records** and **56 scanned source pages**, with **@@ITEMS@@ distinct mathematical occurrences**, **@@PROBLEMS@@ problem-index entries**, **@@REFERENCES@@ bibliography entries**, and **@@CORRECTIONS@@ corrections or critical qualifications**. Record 378 is the heading “YEAR 1976”; it has a talk-index entry and no fabricated mathematical item. The supplied catalogue order is preserved even where page envelopes overlap. A repeated theorem or definition receives a separate occurrence when the notes return to it; a problem is indexed once only when its mathematical identity can be established.

The unit counted is a distinct assertion, construction, definition, question, or substantive intervention. Closely linked hypotheses and a theorem are kept together. Conversely, a definition, its proposed use, and a separate question are split when they have different fates. These are editorial counts, not estimates of how many new theorems the seminar produced. The JSON files, rather than this report, are the authoritative occurrence index.

### Items by class

@@CLASS_TABLE@@

Class A follows the supplied speaker-or-Gelfand rule. Thus a result reported by Novikov but published by Brodskii is not automatically A. “Soon after” is interpreted as a documented near-contemporary publication sequence, normally 1976–1978 here, not an arbitrary rolling numerical threshold. A later exposition of an old theorem remains E. Where an A or E occurrence also contains an inaccurate formula, its literal-correctness field records that independently.

### Items by catalogue speaker

@@SPEAKER_TABLE@@

This table is additive and follows the record metadata. It does not silently transfer catalogue record 383 to Drinfeld. Item-level attribution provides a second view, particularly for Gelfand, Perelomov, Fuchs, Arnold, and Shnirelman interventions. The complete unnormalized attribution counts are in `audit/counts.json`; compound attributions remain explicit rather than being counted twice.

### Items by attributed speaker

@@ATTRIBUTION_TABLE@@

Here an item-level speaker overrides the catalogue attribution. An unresolved initial and an explicit joint attribution remain separate categories; each occurrence is counted once. Parenthetical qualifications are retained so that a reader can see the evidence limit behind a name.

### Items by mathematical area

@@AREA_TABLE@@

Each occurrence has one primary area for this table; the choice does not exclude connections with other fields. The supplementary `audit/area_assignments.json` preserves these decisions without adding an undocumented field to the required seven-file schema.

### Independent assessment dimensions

@@ASSESSMENT_TABLES@@

These dimensions are more informative than a single novelty label. “Read the result” means the relevant mathematical passage was inspected, not that every cited work was read cover to cover. “Publisher metadata checked” records a real but more limited verification. An exact mathematical identification can have only bibliographic verification; the two fields deliberately do not collapse into one confidence score.

## 2. Principal findings and how the publications were identified

### Integrable systems: keep rank, regularity, and geometric data separate

The most sustained sequence runs from the autumn finite-gap discussions to the February and March explanations of commuting differential operators. The useful match is not simply “this later became the Krichever correspondence.” The entries identify the coefficient algebra, smoothness or germ interpretation, unit leading coefficients, the filtration shifts, the degree of the line bundle, its acyclicity, and the extra leading-coefficient datum. An arbitrary Jacobian point is not automatically admissible, and an arbitrary differential algebra does not automatically have evaluation at zero.

Drinfeld's short 1977 article was especially effective because its propositions and corollaries match the filtration/sheaf/connection discussion closely. The source ledger records the exact locators. Receipt on 14 April 1976 establishes that a manuscript existed by that date; it is not described as a public preprint date. The dated notebook records an oral presentation of this material; it does not establish circulation of the later complete manuscript. Krichever's 1978 paper was used for the higher-rank inverse construction, with its generic smooth-curve and auxiliary-data restrictions retained. The rank is the greatest common divisor of the orders in the full commuting algebra; choosing two noncoprime orders does not by itself prove that the algebra has higher rank. These distinctions prevent several apparently unresolved notebook lines from becoming invented modern open problems (Drinfeld, 1977; Krichever, 1978; see the chapter bibliography and item locators).

### Arithmetic and quantization: many corrections are mathematical emendations

The arithmetic material includes several places where a missing coefficient, exponent, sign, or normalization changes the statement. The tau-function identity is checked against an independent product expansion, with exact integer output supplied. This is an audit of the recorded formula, not a new formula attributed to Manin. Euler products, prime-power recurrences, spectral root statements, and gamma factors are treated similarly: a faithful record of a false formula is labelled `faithful_error`, while uncertain handwriting remains `ambiguity`.

The quantization and local-bracket entries state which formal parameter, differential operator class, and geometric hypotheses are being supplied by reconstruction. A vague request involving complex powers does not identify a unique mathematical problem. Likewise, the supergeometry discussion is not expanded into a theorem about every possible even or odd bracket. The particular formal Lie correspondence is matched to Berezin and G. I. Kac, with the identity of Kac checked rather than inferred from a familiar surname.

### Gauge theory: exact constructions and unresolved limits

The chapter distinguishes classical Yang–Mills definitions, perturbative rules, a canonical constraint calculation, a finite product of Haar measures, and the proposed continuum theory. Correcting a sign in the Gauss equation or a factor in the Hamiltonian does not solve a quantum field-theoretic existence problem. The Wilson lattice mechanism predates the 1975–76 exposition. Its strong-coupling conclusions do not establish a positive continuum string tension (Wilson, 1974).

The confinement problem is formulated for four-dimensional, zero-temperature, infinite-volume pure gauge theory with specified external charges. Screening by dynamical fundamental matter and the subtraction of static self-energies are stated explicitly. The manuscript's four-dimensional integral is preserved as source evidence, rather than replacing the problem by a lower-dimensional example. The distinction between instantaneous color-Coulomb energy and the fully relaxed static-source energy is essential to the spring continuation. These entries remain C where a definite unresolved continuum assertion is present. No toy calculation is presented as a contribution to four-dimensional confinement. The related Yang–Mills existence-and-mass-gap problem is distinguished from confinement in the cited formulation (Jaffe & Witten, n.d.). The official PDF inspected is undated; the 2000 announcement of the Millennium problems is not used to assign a date to that particular version.

### Roiter: following a later reference recovered the exact theorem

The arithmetic condition “q(x) divides every a_i x_i” initially resisted a narrow title search. The useful route was a later paper about Weyl roots, followed backward to Roiter's 1978 original. Condition (*) on p. 202 and Proposition 4 on p. 205 match the notebook criterion. The condition includes q(x)>0; positivity on proper coordinate subspaces supplies the sufficient hypothesis. Connected classical nonnegative forms are covered by Lemma 6. This yields an exact match for the finite and connected affine cases, rather than a claim about arbitrary indefinite forms (Roiter, 1978).

An independent descent argument checked the positive-definite classical case: the divisibility condition is reflection invariant; separated positive and negative supports contradict positivity; a suitable reflection reduces height until a coordinate root is reached. The argument is recorded in the research log as a check, with no novelty claim. This identification is an example of why a failed initial search cannot justify class D or even a final class F.

### Short interventions can contain substantial mathematics

The catalogue speaker is not always the mathematical speaker on the page. The March record catalogued as Novikov has a manuscript heading naming Drinfeld. A short S. Gelfand intervention is followed by an explanation marked only “G.”; the latter initial is not silently resolved. Shnirelman's spectral and nodal discussion occupies several pages inside a Krichever record. Perelomov's root-system and many-particle-system discussion similarly requires item-level attribution.

Novikov's radial inverse problem is matched to Brodskii's scalar equation and joint frequency array, including the endpoint convention and Abel normalization. The result is not described as recovery of all elastic parameters of a general solid. A necessary asymptotic compatibility condition is not promoted into a complete range theorem for exact spectra. The bibliographic match was found in a two-page *Uspekhi* announcement, demonstrating the value of searching short contemporary publications before relying on retrospective general accounts.

A 1975 Brodskii article on asymptotic methods for torsional oscillations is an earlier lead. Its existence is supported by the checked retrospective bibliography, but its original full text was not recovered in this run. The B/E chronology of the exact scalar theorem is therefore explicitly provisional; B does not assert that Novikov originated an idea later taken over by Brodskii.

## 3. Bounded mathematical developments

### Fuchs–Perchik: a certified finite Euler calculation

The exact problem is whether infinitely many positive-weight **relative** Euler characteristics of the formal Hamiltonian Lie algebra of the plane are nonzero. It is not the stable-rank graph-homology question, the cohomology after removing constant vector fields, or the weaker claim that infinitely many cohomology classes exist. The star and the negative-weight factors therefore matter mathematically.

Harvard's dissertation catalogue dates Perchik's work to 1975, while the journal article appeared in 1976. The formula's class E assignment is provisional on that documented earlier dissertation; the catalogue does not by itself establish the exact formula's public circulation before the seminar. This chronology qualification is separate from the exact mathematical identification of the series.

The development proves that coefficients through t^N require the positive product only through N+2. It gives a separate invariant-character check of the factor one-half, proves integrality and parity, and implements two exact algorithms: descending factor multiplication and a logarithmic-derivative recurrence. Equality is checked for **every Laurent coefficient** in every retained positive-product row, not just for the final Euler sequence. The largest run retains degrees through 302 and gives Euler coefficients through weight 300, or m=150.

All two-algorithm comparisons pass. The recurrence checks 137,561 exact integer divisions. Independent cutoffs at m=40 and m=90 agree with the prefix of the m=150 run. There are **135 nonzero coefficients among m=1,…,150**, and their absolute values sum to **9,701,705,312**. The sum from m=−1 through 35 is **57**, reproducing the notebook's count under the relative interpretation; positive weights alone contribute 54. The resulting cohomological lower bounds are finite and do not count primitive generators.

Mohammadzadeh and Fuchs (2014, §2) explicitly retain the coefficient-infinitude question. The targeted later searches did not identify a resolution as of the status date. That negative search result is reported with its limits. The independently computed coefficient E(86)=−22,044 differs from the retrieved PDF text “−2204”; the page-image check was not available through the successful retrieval route. This remains an **extraction discrepancy**, not a claimed printed erratum. No literature table is silently corrected.

### Shnirelman: convergence requires a uniform estimate

The second development isolates the difference between fixed Fourier-mode limits and convergence as a periodic distribution. It proves the relevant necessary-and-sufficient criterion: coefficientwise convergence together with a uniform polynomial bound on all coefficients. The complete circle calculation then gives zero for an irrational ratio a/(2πR), and an explicit mean-zero q-point atomic comb for a rational ratio p/q. The coefficient normalization is checked a second way by grouping the spectral terms into residue classes.

For the unit round two-sphere at a=2π, the first Fourier coefficient diverges as −1/(πε)+O(1). A complete estimate is supplied, including the spherical-harmonic multiplicities and the uniformly controlled phase error. The sphere has degenerate continuous families of equal-length closed geodesics, so this is explicitly **not a counterexample under the notebook's generic-geodesic hypotheses**. It shows why those hypotheses cannot simply be dropped.

The separate numerical script checks the circle formula against direct spectral summation and the sphere asymptotic at decreasing Abel parameters. Floating-point agreement is a diagnostic; the written proofs establish the claims. The general question still requires a uniform estimate in the sampled times ma and a precise treatment of possible cancellations. The local nondegenerate wave-trace expansion supports the mechanism but does not supply that global estimate by itself (Zelditch, 1998).

### Why the other C items were not inflated into projects

The full fixed-rank Hamiltonian cohomology problem is broader than the finite Euler development and includes graded dimensions, representatives, and products. The confinement entries lack a bounded route from the notebook calculation to the missing continuum theorem. Their `worth` fields explain what a future investigation would need. No claim was promoted to D to create a development quota, and elementary exercises already answered in the literature remain A, B, or E as appropriate.

## 4. Corrections, uncertainty, and source verification

@@CORRECTION_TABLE@@

The correction file is a proposed critical apparatus, not an overwrite of the supplied diplomatic Russian. Its categories have distinct meanings:

- **Transcription:** the scan supports a different reading of the written marks.
- **Translation:** the Russian/source wording was rendered incorrectly or too strongly in English.
- **Ambiguity:** the evidence does not determine a unique reading.
- **Faithful error:** the transcription faithfully preserves a mathematical error or shorthand requiring emendation.
- **Provenance:** attribution, record boundary, chronology, or source ownership requires qualification.

Scans were inspected where formula, diagram, attribution, or doubt determined the interpretation; the block research logs identify the pages and decisions. The attached Russian was the textual authority. A mathematical formula supplied to repair a false literal statement is not claimed to have been deciphered from the handwriting. Some corrections cover both languages because both preserve the same notebook formula. Different errors on one page remain separate entries.

All bibliography entries have an opened URL or DOI recorded by the researchers, or are explicitly marked `unverified`. Keys from the cumulative bibliography are reused, with DOI matching checked during assembly. The source ledgers distinguish publisher metadata, relevant full-text passages, and unresolved leads. A work's existence, its contents, and the asserted match are different verification questions. For example, a publisher record may verify a date and title without supporting a theorem number. The chapter avoids assigning a full-result verification to an inaccessible source merely because its title is persuasive.

The most important chronology rule is to keep **seminar occurrence, manuscript receipt, public circulation, original publication, translation, and later repository deposit** separate. A receipt date is not proof of public circulation. An English translation can postdate the original by years. The 2000 arXiv deposit of Zelditch's 1998 paper is a later access route, not its first-publication date. Where first public circulation could not be established, the chapter says only what the checked evidence supports.

## 5. What the A–F classes miss, and proposed method changes

The classes mix chronology, authorship, identification, and mathematical completion. Several refinements would improve a multi-year companion:

1. **Separate item identity from its formulation.** A classical theorem with a wrong coefficient can be E and false as written. A precisely restricted modern reconstruction can be correct while only partially matching the notes. Both facts should remain visible.
2. **Represent publication events explicitly.** Add structured dates with an event type: seminar, receipt, preprint circulation, publication, translation, repository deposit. Store the supporting source for each event. Do not sort all of these under one date.
3. **Separate catalogue and manuscript attribution.** Keep the catalogue record stable and add item-level speaker, evidence page, and attribution confidence. An initial alone should remain unresolved where the page does not identify the person.
4. **Record hypothesis deltas.** A machine-readable list of added, corrected, or excluded hypotheses would make partial matches more transparent: smoothness, rank, acyclicity, pure gauge matter content, boundary conditions, fixed symplectic rank, and primitive-geodesic conventions are recurring examples.
5. **Distinguish research status from search status.** “No exact source located” is not “open,” and “not developed” requires a documented search. A current-status field should contain the precise statement assessed, the latest directly verified status source, the search date, and unresolved leads.
6. **Add an optional primary-area field.** This chapter keeps it in an auxiliary audit file to preserve the required schema. A future format could make it a controlled vocabulary with optional secondary areas.
7. **Make verification source-specific.** One item can cite an original announcement checked bibliographically and a later exposition read in full. An aggregate item-level label loses this distinction; the supplied source ledgers retain it.

The process should continue to require an independent second check for every supplied proof or numerical result. In this year it prevented the finite Euler extension from being presented as an infinitude result, preserved the sphere example's failed hypotheses, and exposed the difference between direct source identification and broad thematic similarity.

## 6. Presentation on the companion website

A reader arriving at a talk should first see the catalogue date and speaker, the manuscript-attribution qualification when relevant, the actual page span, and a compact summary. The next level should expose the item statement and assessment; the original wording, reconstruction, fate, and current status should remain separately labelled. A class letter alone is insufficient as the headline.

For this year, the most useful links are:

- The finite-gap sequence across earlier years and the autumn, February, and March commuting-operator records, with separate paths for rank one and higher rank.
- The repeated gauge-theory discussion, the earlier Wilson-lattice occurrence, and the single precisely scoped confinement problem.
- Roiter's notebook criterion directly to the verified theorem and its finite/affine hypotheses.
- Shnirelman's intervention inside record391 to the earlier wave-trace occurrences, the spectral-phase problem, and the new bounded development.
- Fuchs's relative Euler product to the coefficient-infinitude problem, the full-cohomology problem, the exact coefficient table, and the reproducible computation.
- Each correction to its source page and to the item whose mathematical assessment changes.

Problem pages should show a chronology of exact occurrences and a separate list of thematic relatives. A reader should be able to filter by false-as-written statements, omitted hypotheses, partial publication matches, and unresolved identifications. The finite computation needs a visible range label and downloadable CSV; zero coefficients must not be displayed as vanishing cohomology. Development results should display the supplied-proof or supplied-computation marker and their exact scope.

No website was built or published in this task. The seven data files are retained in the agreed schema. Suggested additional fields are described above; the auxiliary audit files can inform a future schema revision without forcing it into the current chapter.

## 7. Reproduction and final checks

The supplied builder and style are included. The chapter is generated from the seven data files; the generated TeX should not be edited directly. In an ordinary TeX installation, run:

```text
python build_chapter.py GY1975
xelatex GY1975_test
bibtex GY1975_test
xelatex GY1975_test
xelatex GY1975_test
```

`code/build_pdf.py` runs these steps with logs and includes a process-local fallback for the execution image's missing TeX filename database and format. It uses the installed TeX distribution and writes only a private cache. No system files or mathematical content are changed. `code/audit_chapter.py` supplies additional checks for exact schema fields, 34-record coverage, consecutive academic-year IDs, citation/ref consistency, problem links, bibliography verification flags, control characters, and source-page ranges.

@@BUILD_RESULT@@

The mathematical programs and their outputs are under `code/` and `computations/`. `audit/` contains counts, area assignments, research and source ledgers, and machine-readable validation output. The original source scans are not duplicated in this zip; they are the supplied inputs identified above. No inaccessible reference PDF is redistributed. The generated chapter and test PDF contain the full companion, rather than a summary of work left to complete.

## Selected references for this report

The chapter bibliography contains the complete entries, opened URLs, and verification notes. This abbreviated list identifies the main sources discussed above in author–date form.

- Drinfeld, V. G. (1977). Commutative subrings of certain noncommutative rings. *Functional Analysis and Its Applications, 11*, 9–12. See the verified original/translation metadata in `GY1975_references.bib`.
- Jaffe, A., & Witten, E. (n.d.). *Quantum Yang–Mills theory*. [Clay Mathematics Institute problem description](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf).
- Krichever, I. M. (1978). Commutative rings of ordinary linear differential operators. *Functional Analysis and Its Applications, 12*, 175–185. [Author's full text](https://www.math.columbia.edu/department/krichever/pdfs/1975-1979/1978-CROOLDO0.pdf).
- Mohammadzadeh, S., & Fuchs, D. B. (2014). Cohomology of the Lie algebra H₂: Experimental results and conjectures. *Functional Analysis and Its Applications, 48*, 128–137. https://doi.org/10.1007/s10688-014-0053-0
- Roiter, A. V. (1978). Roots of integral quadratic forms. *Trudy Matematicheskogo Instituta imeni V. A. Steklova, 148*, 201–210. [Primary record and full text](https://www.mathnet.ru/eng/tm2511). English translation published in 1980.
- Wilson, K. G. (1974). Confinement of quarks. *Physical Review D, 10*, 2445–2459. https://doi.org/10.1103/PhysRevD.10.2445
- Zelditch, S. (1998). Wave invariants for non-degenerate closed geodesics. *Geometric and Functional Analysis, 8*, 179–217. [Author's later repository copy](https://arxiv.org/abs/math/0002037).
