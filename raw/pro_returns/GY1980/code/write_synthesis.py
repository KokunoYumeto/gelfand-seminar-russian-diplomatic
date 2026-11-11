"""Write the overview, report and build README from final audited counts."""
import argparse,collections,csv,json
from pathlib import Path
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--report-only',action='store_true',help='Refresh only the report and README, preserving the overview and area-classification CSV.')
args=parser.parse_args()
ROOT=Path(__file__).resolve().parents[1]
counts=json.loads((ROOT/'checks/counts.json').read_text())
items=json.loads((ROOT/'GY1980_items.json').read_text())
talks=json.loads((ROOT/'GY1980_talks.json').read_text())
problems=json.loads((ROOT/'GY1980_problems.json').read_text())
areas=json.loads((ROOT/'checks/item_areas.json').read_text())

def broad(f):
    s=f.lower()
    if any(t in s for t in ['d-module','sheaf','homological','category theory']):return 'D-modules, sheaves and homological algebra'
    if any(t in s for t in ['kinetic','hydrodynamic','fluid','partial differential','geometric mechanics']):return 'Kinetic theory, fluid mechanics and PDE'
    if any(t in s for t in ['integrable','spectral','operator theory','mathematical physics']):return 'Integrable systems, spectral and operator theory'
    if any(t in s for t in ['newton','toric','toroid','exponential','fewnomial','mixed volume','convex geometry','algebraic and convex','lattice geometry','sparse polynomial']):return 'Newton polyhedra, convex and exponential geometry'
    if any(t in s for t in ['intersection homology','algebraic topology']):return 'Topology and intersection homology'
    if any(t in s for t in ['lie','representation','noncommutative','nonassociative','group theory','matrix']):return 'Lie theory, representation theory and algebra'
    if any(t in s for t in ['algebraic geometry','algebraic curves','k-theory']):return 'Algebraic geometry and K-theory'
    if any(t in s for t in ['integral geometry','special functions','characteristic classes']):return 'Integral geometry and special functions'
    if any(t in s for t in ['analysis','probability','stochastic']):return 'Analysis, probability and stochastic methods'
    return 'Differential, complex, projective and symplectic geometry'
area_counts=collections.Counter(broad(areas[x['id']]) for x in items)
if not args.report_only:
    with (ROOT/'checks/item_area_classification.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['id','primary_area','detailed_area'])
        for x in items:w.writerow([x['id'],broad(areas[x['id']]),areas[x['id']]])

def table(data,label='Category',count_label='Items'):
    return '| '+label+' | '+count_label+' |\n|---|---:|\n'+'\n'.join('| '+k+' | '+str(v)+' |' for k,v in data.items())
classes={k:counts['classes'].get(k,0) for k in 'ABCDEF'}
row=' & '.join(str(classes[k]) for k in 'ABCDEF')
overview=r'''\noindent\textbf{Scope and source order.}
This chapter covers all 36 records in the supplied 1980--81 manifest and restores three omitted records, 510--512: the archive catalog dates them 23 February 1991, while the autograph P000960 reads 23 February 1981. The resulting 39 records comprise 38 talks or interventions and one catalog year divider. They are ordered by first appearance in the manuscript, including Gelfand's introductions before Beilinson and the Gelfand--Cherednik sequence on P000960. Overlapping catalog page ranges have been replaced by observed footprints. P000916 is a preceding-year continuation already indexed as 1979-488.1--.7; it is accounted for without being counted again (\citealp{mccme2026gelfand}).

\noindent\textbf{What the year contains.}
The {{ITEMS}} mathematical occurrences range from classroom exercises to announcements. Autumn's intersection homology, Segre families and regular holonomic systems lead into Beilinson's sustained exposition of localization, transfer bimodules and derived direct image. The chronology matters: an announcement circulating before a talk is distinguished from a later full proof, and a later geometric implementation does not automatically make an old formula new. The categorical affinity question is followed from its November introduction to its answer in the continuation.

Novikov's December lecture combines already published Pauli zero modes with the topological discussion appearing in a paper received the following day. The physical line bundle has degree \(N\); the reciprocal-torus zero-mode bundle has rank \(N\) and Chern number of absolute value one. The notebook conflates these numbers. MacPherson's Grassmannian constructions lead to positive torus orbits, harmonic forms and convexity; Khovanskii and Kazarnovskii connect Newton polyhedra, toric geometry and zero counting. Nondegeneracy, regularity and normalization conditions are restored explicitly.

Spring brings Yang--Baxter equations, commuting differential operators, algebraic geometry and \(K\)-theory, Hamiltonian kinetic theory, eigenvalue inequalities, gas dynamics and Lie semigroups. The transfer-matrix argument needs the correct auxiliary trace legs; the Weyl-operator examples need noncommutative calculation; the kinetic constructions need their actual functional and coefficient classes. The classification records the fate of the qualified statement and separately assesses the literal notebook claim.

\begin{center}
\begin{tabular}{lrrrrrr}
\toprule
Class & A & B & C & D & E & F\\
\midrule
Occurrences & {{ROW}}\\
\bottomrule
\end{tabular}
\end{center}
A denotes a subsequent speaker publication; B a later development by others; C a partly developed precise question; D an undeveloped identified question; E prior knowledge; F an insufficiently identified statement. There are {{PROBLEMS}} problem identities, {{REFS}} bibliography entries and {{CORRECTIONS}} correction rows. Counts describe occurrences, so a theorem repeated in several talks is counted several times. No D classification is justified by the search evidence.

\noindent\textbf{The bounded development and its limits.}
The remaining class-C item is Gelfand's conjecture that every complex algebraic curve's function field embeds in the first Weyl division ring. All genus-one and genus-two fields are positive cases: in particular Oganesyan's 2016 preprint, published in 2018, realizes every standard genus-two quintic by rational-coefficient commuting operators (\citealp[Theorem~3]{oganesyan2016rational}). The genus-two item is therefore B. The development proves an elementary obstruction for a prescribed positive-genus affine model with a nonconstant unit, supplies a complete exact certificate for a known genus-two family, and proves the injectivity step from operators to a function field. These are bounded clarifications, not a solution of the universal conjecture or a novelty claim for the known family. Independent checks caught both a notebook formal-expression error and a scalar normalization in the checked Mironov preprint.

\noindent\textbf{Continuity and evidence.}
The unextended Gelfand--Kirillov conjecture recurs under its existing identity GP-1967-21; its general form is false, with surviving simple-type cases stated cautiously. The preceding year's collective-field remarks connect to the Vlasov and hydrodynamic material without being equated with its later precise brackets. The field-embedding question is kept separate from automorphism and different-rank Weyl-field problems. The report and research ledgers identify full-text, metadata-only and unresolved evidence; a verified bibliographic link alone is never presented as a verified proof.
'''
for key,value in {'ITEMS':counts['items'],'ROW':row,'PROBLEMS':counts['problems'],'REFS':counts['references'],'CORRECTIONS':counts['corrections']}.items():overview=overview.replace('{{'+key+'}}',str(value))
if not args.report_only:
    (ROOT/'GY1980_overview.tex').write_text(overview)

pages='pending final compilation'
pdf=ROOT/'GY1980_test.pdf'
if pdf.exists():
    import fitz
    pages=str(len(fitz.open(pdf)))
report=r'''# GY1980 critical companion: research and verification report

**Status date: November 2026.** This report documents the research, editorial decisions and verification behind the seven schema files and the generated chapter. The PDF page count below reflects the current compilation state. The apparatus distinguishes evidence from the notebook, the diplomatic Russian transcription, the English translation, published literature and deductions made in this chapter.

## 1. Scope and completed inventory

The supplied manifest contains 36 records. The live MCCME master catalog and the attached P000960 date heading identify three additional records belonging to the same academic year: **510, 511 and 512**, cataloged under the erroneous date **23-Feb-91**. The autograph reads **23/II/81**. These records have been restored with the date **1981-02-23**, retaining their original record numbers. The chapter therefore contains **39 records: 38 mathematical talks or interventions and one nonmathematical catalog year divider**. The data and corrections document the discrepancy. Source: [MCCME seminar catalog](https://old.mccme.ru/gelfand/notes/all-links.html).

The records follow their first appearance in the manuscript. Gelfand's introductions precede Beilinson on 3, 10 and 17 November. On 24 November, the Fuchs and Lomonosov interventions precede the Beilinson continuation. On 23 February, Gelfand precedes Cherednik, reversing their catalog-number order. Interleaved continuations remain grouped with the identified talk and are described in its summary. The page fields specify the portions observed in the manuscript, resolving the manifest's overlapping ranges.

**P000916** is an undated continuation from the previous year, already represented by **1979-488.1–.7** in the supplied earlier index. It is accounted for as boundary material with links across years; it does not create a new September 1980 occurrence. **Record 507** is a catalog divider rather than an independently verified manuscript lecture. Every mathematical source page from P000917 through P000980 is represented in the current year's coverage ledger.

| Deliverable measure | Count |
|---|---:|
| Records | {{RECORDS}} |
| Mathematical occurrences | {{ITEMS}} |
| Problem identities | {{PROBLEMS}} |
| Bibliography entries | {{REFS}} |
| Correction rows | {{CORRECTIONS}} |
| Compiled PDF pages | {{PAGES}} |

The JSON files are the occurrence and problem indices. `GY1980_chapter.tex` is generated from them, the overview, development and corrections. The PDF includes the full chapter, problem index, correction apparatus and bibliography. The `checks` directory records validation, source-page coverage, mathematical computations and build results. Batch research ledgers in `parts` preserve the source-identification and verification history.

## 2. Counts and their interpretation

### By fate class

{{CLASS_TABLE}}

A means a relevant result subsequently published by the speaker or Gelfand; B a subsequent development by others; C a precise question partly developed; D a defensibly identified but undeveloped question; E prior knowledge; F content whose intended statement cannot be sufficiently recovered. **No D item is asserted.** Failure to retrieve an exact source is not enough to call mathematics undeveloped. Repeated exposition is counted as repeated occurrence, not as a new theorem. These totals therefore measure the notebook's structure and the editorial decomposition, not research productivity.

The single class-C occurrence is **1980-519.3**, the question of embedding the function field of every complex algebraic curve in the first Weyl division ring. Its status is limited to what the checked literature establishes. The genus-two occurrence **1980-519.2** was changed from a provisional C classification to B after a further primary-source search located Oganesyan's theorem for arbitrary genus-two quintics. The final assessment thus distinguishes a complete genus-two result from earlier generic examples.

### By attributed speaker

An explicit item-level intervention overrides the primary talk speaker. Otherwise the item is counted under its record's primary speaker. A joint attribution retained in one row is counted once, so the table totals the number of occurrences. Attribution is not a claim of authorship of every theorem discussed.

{{SPEAKER_TABLE}}

### By mathematical area

Each occurrence is assigned one primary area for counting. The more detailed labels are preserved in `checks/item_area_classification.csv`. An occurrence spanning several subjects is counted once.

{{AREA_TABLE}}

### Assessment dimensions

The fate class is independent of literal correctness and strength of verification. A pre-existing theorem can be miscopied or stated without indispensable hypotheses; a perfectly legible notebook sentence can be false.

{{CORRECTNESS_TABLE}}

{{VERIFICATION_TABLE}}

{{MATCH_TABLE}}

Correction types are likewise distinct:

{{CORRECTION_TABLE}}

## 3. Main mathematical findings

### D-modules, intersection homology and categorical affinity

The autumn and November talks form a sustained sequence on D-modules and their geometric applications. The apparatus distinguishes ordinary and derived inverse image, left and right modules, transfer bimodules, cohomological shifts and simple regular holonomic objects. A torsion-free D-module is not thereby a connection; reducible support requires qualifications beyond an irreducible minimal-extension theorem; arbitrary coherent D-modules need not have finite length. The notebook's middle-perversity formulas also require corrections. Because the errors are legible in the manuscript, they are classified as faithful notebook errors. The statements and precise source locators accompany occurrences 1980-490.1–.5 and 1980-493.3–.13, and the items in records 496, 498, 500 and 503.

Kashiwara's April 1980 Riemann–Hilbert announcement predates the October discussion; the apparatus separately dates the later full treatments. The categorical converse left uncertain on 3 November is answered in the continuation on 10 November, with the compact projective generator and opposite-ring qualifications made explicit. The two occurrences share one problem identity.

### Magnetic translations and Bloch bundles

Novikov's lecture on 1 December draws on Dubrovin and Novikov's already published 1980 zero-mode results. The paper received **2 December 1980** supplies the closely matching topological continuation. The physical line bundle has degree \(N\), while the reciprocal-torus zero-mode bundle has **rank \(N\) and Chern number of absolute value one**. The conflation of these quantities on P000946 is a substantive faithful notebook error. The genericity argument is formulated in the bundle of Hermitian endomorphisms, so it does not assume an unavailable global trivialization. Landau multiplicity \(N\) refers to one scalar spin sector. The uncancelled one-dimensional aside is retained as a separate F item. See Dubrovin and Novikov (1980, Section III), [full text](https://people.sissa.it/~dubrovin/Papers/1980/dubrovin_novikov_1980_dan.pdf), and Novikov (1981, Section II, Lemma 1; Section III, Lemma 2 and Theorem 2), [full text](https://homepage.mi-ras.ru/~snovikov/71.pdf).

### Grassmannians, Newton polyhedra and exponential sums

MacPherson's constructions require genericity and a distinction among a complex torus orbit, its positive real part and a compact Hamiltonian torus orbit. The last is mapped to a point by its commuting Hamiltonians and therefore cannot itself have the nontrivial polytope image drawn in the notebook. Statements about harmonic forms need degree and parity qualifications. Khovanskii's genus and root-count formulas require the appropriate toric compactification and nondegeneracy conditions. Kazarnovskii's zero asymptotic for a fixed system is checked against the regularity definition in the 1981 paper; a later result about averaged currents addresses a different statement. Precise theorem locators appear in records 508, 509, 512 and 513.

### Commuting operators: a resolved genus-two problem and a wider conjecture

A decisive source identification was Oganesyan's theorem: **every monic genus-two quintic** occurs as the spectral curve of rational-coefficient commuting operators of orders 4 and 10, using the union of two families. The result first circulated on **18 August 2016** and was published in **2018**. It resolves the genus-two question when interpreted as realization of an abstract curve or its standard quintic model. The stronger assertion about every affine coordinate ring is treated separately. See Oganesyan (2018), [published article](https://doi.org/10.1007/s10688-018-0229-0), and Theorem 3(2) of the [2016 author preprint](https://arxiv.org/abs/1608.05146).

Gelfand's separately recorded assertion asks whether the function field of **every complex algebraic curve** embeds in the **first Weyl division ring**. This is distinct from the Dixmier endomorphism conjecture, isomorphism questions for Weyl fields of unequal ranks and the Gelfand–Kirillov conjecture. All cases of genus at most two are positive. The checked constructions in higher genus establish selected families. The C classification records this limit of the evidence; it does not claim that the search exhausts the literature on the universal assertion.

### Kinetic and spectral problems

The pure Vlasov functional bracket already appears in Morrison's 1980 paper, equation (12), before Arnold's March 1981 talk. The later coadjoint-orbit and gauge formulations have their own chronology. The original Maxwell coupling and its subsequent correction for the Jacobi identity are distinguished from the correct pure Vlasov bracket, with mass normalization stated explicitly. Bobylev's Fourier and isotropic hierarchy results are qualified by the collision model and analytic class. The broad hydrodynamic-limit program remains F because the notes do not specify a theorem-level target.

Lidskii's recursive inequalities match a 1982 announcement. The apparatus distinguishes that announcement, the absence of a supporting published proof reported in the checked historical account, and the later resolution of the Horn problem. The trace equality, recursive index conditions and tensor-product saturation statement appear in 1980-526.1–.3. Record 528 separately treats Olshanskii's global and local semigroups, proper cones, orientation choices and factorization for the **minimal cone**. Each qualification affects the scope of the corresponding assertion.

## 4. Bounded development and verification

The development addresses the remaining universal question about function-field embeddings. Its genus-two subsection verifies a known positive case and clarifies the difference between realizing a function field and realizing a prescribed affine coordinate ring.

1. **Affine-unit obstruction.** For a smooth irreducible affine complex curve of positive genus with a nonconstant unit, there is no injective unital complex-algebra map from its coordinate ring into \(\mathbb C(x)[D]\). Units of this operator ring have order zero. Injectivity would force the image of the nonconstant unit to be a nonconstant rational multiplication operator, whose centralizer is \(\mathbb C(x)\). The resulting curve-field embedding into \(\mathbb C(x)\) would induce a finite nonconstant map from \(\mathbb P^1\) to a compact curve of positive genus, contradicting Riemann–Hurwitz. The proof states all hypotheses explicitly.
2. **A concrete genus-two example.** The smooth affine curve \(zw^2-z^4-1=0\) has invertible coordinate \(z\). Its function field is that of \(Y^2=z^5+z\), a squarefree genus-two quintic. The obstruction applies to its affine coordinate ring, while Oganesyan's theorem provides an embedding of its function field. The proof explains why realizing the original coordinate \(w\) requires passage to a quotient operator.
3. **The notebook's false operator formulas.** The literal sixth-order expression has a nonzero commutator with \(D^5\) coefficient \(48x-12\). The corrected Dixmier pair passes the exact check. For the notebook's two-term formal expression \(A\), the differential part of \(A^3\) is \(L^3+3xL+6D\); the corrected commuting pair instead has the term \(3D\). The next term in the formal square root supplies the correction.
4. **A known genus-two certificate.** With \(L=D^2+x^3+a\), the included operators \(P=L^2+6x\) and \(M\) satisfy \([P,M]=0\) and \(M^2=P^5+27aP^2+81\). Both the symbolic discriminant and direct elimination of common roots give the smoothness condition \(2916a^5+3125\ne0\). The construction is an existing Mironov family; the chapter supplies a reproducible certificate for it.
5. **The injectivity step.** Since \(P\) and \(M\) have differential orders 4 and 10, nonzero terms \(f(P)\) and \(g(P)M\) have orders congruent to 0 and 2 modulo 4, respectively. They cannot cancel, proving that the spectral coordinate-ring map is injective. The proof then extends the map to the curve's function field, with values in the Ore division ring.

Results proved or computed in the chapter are marked `\ours` or `\oursComputed`. The operator computation uses exact polynomial arithmetic over \(\mathbb Q[a,x]\). A second implementation checks direct action on every monomial through degree 20 at four parameter values. A triangular coefficient argument makes each finite check complete at its parameter value; the theorem for all parameters rests on the symbolic coefficient identities. A separate proof audit checked the unit obstruction and the hypotheses concerning algebraic curves. The formal pseudodifferential computation uses a justified cutoff. The code and its actual outputs are included.

Comparison with the 2012 version of Mironov's preprint identified a scalar normalization: the displayed tenth-order operator equals the centered operator plus \(9I\), while the displayed hyperelliptic equation uses the centered operator. Both operators commute with \(P\), and shifting the spectral coordinate reconciles the formulas. The chapter identifies the preprint version checked; the final journal typesetting was not checked for this issue. The initial assertion of literal equality failed the computation, and the corrected normalization passed the final run.

## 5. What was difficult and which searches worked

**Provenance before bibliography.** Broad catalog page ranges overlap several speakers. Explicit manuscript dates and speaker headings, together with the live catalog, determine attribution. Recovering records 510–512 established the February setting of material that might otherwise have been assigned to the March talks. P000916 required a decision about the boundary between academic years before its mathematical content could be classified.

**Exact-title searches and authors' bibliographies.** Submission dates on Math-Net and translations of Soviet papers hosted by their authors were especially useful for Novikov, Khovanskii, Grinevich, Kazarnovskii and Olshanskii. Contemporary seminar expositions and publisher metadata distinguished first announcements from final articles. Following references in primary sources identified the regularized diffusion setting of Gaveau's work. A targeted search for rational-coefficient commuting operators found Oganesyan's theorem and changed a provisional classification. The batch research ledgers preserve URLs, precise result locators, unsuccessful leads and access limitations.

**False statements and incomplete statements.** The correction apparatus distinguishes errors faithfully transcribed from the notebook from missing hypotheses. It also distinguishes mathematical emendations from the manuscript's actual wording. Some insufficiently specified programs remain in class F: an unspecified regularization, a comparison of operator restrictions with unclear spectral subspaces, a regularized Burgers step for an arbitrary polynomial without a stated solution class, and a request to extend semigroup ideas beyond the stated Lie-group setting.

**Verification limits.** `note={verified}` means that a bibliography link or DOI was opened; it does not mean that every original proof was read. Item-level verification and the research ledgers state the evidence actually checked. Some exact matches rest on publisher metadata together with a separate primary exposition. **Hilbert's 1901 article is the sole unverified entry among the {{REFS}} references**: the direct source remained inaccessible, and the associated item is classified as indirectly verified. Ivlev's 2026 paper was checked only through its metadata and abstract because the full text was embargoed. The search was broad and targeted, but it was not a systematic review of every publication through November 2026.

## 6. What the A–F scheme misses and proposed method changes

The single fate letter compresses several independent questions. An old formula can receive a new proof or geometric realization; an announcement can precede a complete proof by years; a refuted broad conjecture can retain open subcases; a precise theorem can coexist with a false handwritten formula in the same occurrence. This year therefore relies heavily on the separate literal-correctness, publication-match, verification and development fields. No extra state was silently introduced into the required schema.

For future chapters, useful optional additions would include separate catalog and manuscript dates; an anchor identifying the relevant region of a source page; a chronology distinguishing submission, circulation, online publication and journal issue dates; precise source locators and verification scopes for each reference; and typed links distinguishing recurrence, proof, special case, correction and thematic connection. Explicit `abstract_curve`, `affine_model` and `coefficient_ring` scope fields would prevent the genus-two ambiguity encountered here. A `primary_area` field would make area totals reproducible across chapters. These are proposals for future revisions; the delivered chapter uses the required schema.

Problem identities should follow exact statements. The existing identity GP-1967-21 is reused. Resolved exercises can have problem entries when the notes pose a definite question, with their resolved status stated explicitly. The field-embedding conjecture retains its own identity, separate from earlier questions about Weyl algebras. A search that finds no exact match does not by itself establish an undeveloped idea.

## 7. Presentation on the companion website

A reader arriving at a talk should first see its actual date, source-page footprint and provenance warning when those differ from the catalog. The next step should be the short summary and item list, with each item opening four clearly labeled panes: notebook wording, precise statement/reconstruction, fate and present status. A correction should be reachable directly from the sentence or formula it qualifies. The original scan and both transcriptions should be one click away where their hosting permits it.

Priority links should connect the November D-affinity question to its continuation; the repeated Cherednik talks to one another; records 511 and 518 to the corrected operator formulas and record 519; and the distinct genus-two and all-curves problem identities. The MacPherson, Khovanskii and Kazarnovskii talks merit links between their related polytope constructions. The collective-field material on P000916 should link to 1980-523.1 and 1980-524.2–.4. The recurrence of GP-1967-21 must resolve across years. Earlier questions about automorphisms or Weyl fields of different ranks should carry explicit thematic links while retaining their own identities.

Search should support mathematical expressions as well as titles and names. Filters should expose fate, literal correctness and verification separately; a green “verified” badge based only on an opened DOI would mislead. Useful navigational metadata include source anchors, primary areas, typed links and publication chronology. A stable item URL should retain the academic-year/record/item identifier even when a catalog date is corrected. Readers of the development should be able to inspect its proof, code and actual check output together.

## 8. Build, reproducibility and acceptance checks

The required builder is included and has been run on the seven integrated schema files. A supplementary validator checks all required enumerated values and fields, consecutive occurrence numbers, all 39 record identities, reciprocal problem links, earlier occurrence identifiers against the supplied index, citation-key inclusion and bibliography verification tags. The supplied cumulative bibliography contains repeated keys; integration selects one entry per used key and reuses existing identities. Key-reuse decisions and source coverage are recorded in `checks`.

The reproducible build uses XeLaTeX and BibTeX through the included build script, which records each pass and can generate missing TeX formats locally. {{BUILD_ACCEPTANCE}} The mathematical scripts and their outputs are included separately from the scholarly prose. See `README.md` for the exact build and computation commands. The seven schema files are the authoritative chapter inputs, and the generated chapter and PDF present their integrated contents.
'''
replace={
 'RECORDS':counts['records'],'ITEMS':counts['items'],'PROBLEMS':counts['problems'],'REFS':counts['references'],
 'CORRECTIONS':counts['corrections'],'PAGES':pages,
 'CLASS_TABLE':table(classes,'Class'),'SPEAKER_TABLE':table(counts['speakers'],'Attributed speaker'),
 'AREA_TABLE':table(dict(sorted(area_counts.items())),'Primary mathematical area'),
 'CORRECTNESS_TABLE':table(counts['literal_correctness'],'Literal correctness'),
 'VERIFICATION_TABLE':table(counts['verification'],'Verification level'),
 'MATCH_TABLE':table(counts['publication_match'],'Publication match'),
 'CORRECTION_TABLE':table({k.replace('_',' '):v for k,v in counts['correction_types'].items()},'Correction type','Rows')}
acceptance='Final acceptance requires stable cross-references and visual inspection of the rendered PDF. The logs and audit files in `checks` record the completed work.'
audit_path=ROOT/'checks/pdf_audit.json'
visual_path=ROOT/'checks/visual_review.md'
if audit_path.is_file() and visual_path.is_file():
    audit=json.loads(audit_path.read_text())
    if audit.get('structural_result')=='PASS' and '**Acceptance: PASS.**' in visual_path.read_text():
        acceptance=(f"**Final acceptance passed on 11 November 2026.** The {audit['pages']}-page PDF contains all 39 record labels and all 246 occurrence identifiers. Cross-references are stable, and the final logs contain no LaTeX errors, unresolved citations or references, missing glyphs, overfull boxes, duplicate labels or BibTeX warnings. The overview occupies parts of pages 1–2. The combined visual inspection covers every page on contact sheets and selected enlarged pages, including all development pages and the final corrected passages. No clipping, overlap or missing-glyph boxes were observed. Eleven underfull-line diagnostics remain; the inspected spacing is readable. `checks/pdf_audit.json` and `checks/visual_review.md` record the scope and final PDF checksum.")
replace['BUILD_ACCEPTANCE']=acceptance
for key,value in replace.items():report=report.replace('{{'+key+'}}',str(value))
(ROOT/'GY1980_report.md').write_text(report)

readme='''# GY1980 — critical companion to the Gelfand seminar, 1980–81

Start with `GY1980_test.pdf` for the complete typeset chapter or `GY1980_report.md` for the research findings, counts, evidence limitations and methodological decisions.

## Main files

The seven schema files are:

- `GY1980_talks.json`: records, speakers, dates and source-page footprints.
- `GY1980_items.json`: mathematical occurrences and their assessments.
- `GY1980_problems.json`: problem identities, occurrences and present status.
- `GY1980_overview.tex`: the chapter overview.
- `GY1980_development.tex`: proofs, computations and their limitations.
- `GY1980_corrections.csv`: the correction apparatus.
- `GY1980_references.bib`: the chapter bibliography.

`GY1980_chapter.tex` and `GY1980_test.tex` are generated files. The supplied format specification is also included.

## Build the chapter

From this directory, using Python 3 and an installation of XeLaTeX and BibTeX:

```sh
python code/finalize_typesetting.py
python code/format_corrections.py
python code/validate.py
python build_chapter.py GY1980
python code/build_pdf.py
```

The two formatting scripts are idempotent. The build script runs XeLaTeX, BibTeX and two further XeLaTeX passes, with additional passes if needed for stable cross-references, preserving a log for each pass. It uses a normal TeX installation when available and can generate missing formats in a local runtime directory from installed TeX sources.

The supplied style requires the standard AMS, natbib and hyperref packages and a font supporting Cyrillic, such as CMU Serif or DejaVu Serif. The `checks` directory holds the build logs and records completed validation and PDF audits. The supplied cumulative bibliography and earlier index are preserved as read-only inputs to the integration and audit scripts. The chapter has its own bibliography and problem index among the seven schema files listed above.

To refresh the report and README after compilation while preserving the overview and area-classification CSV:

```sh
python code/write_synthesis.py --report-only
```

The report reads the audited counts and detects the current PDF page count automatically. PyMuPDF is required for page counting when the PDF is present. `requirements.txt` records the Python package versions used. To repeat the PDF structure checks and generate contact sheets and enlarged page images, run `python code/audit_pdf.py`; this also requires Pillow and the Poppler commands `pdftoppm` and `pdffonts`.

## Reproduce the mathematical checks

The computations use Python 3 and SymPy 1.14.0, with exact coefficients:

```sh
python code/check_weyl.py > checks/weyl_output.txt
python code/check_formal.py > checks/formal_output.txt
python code/check_curve_models.py > checks/curve_models_output.txt
```

The first script checks the notebook counterexample, the corrected Dixmier pair, the centered genus-two pair, its spectral polynomial and discriminant; it also runs the independent checks of operator action. The second checks the formal pseudodifferential expression. The third checks the affine coordinate identity, squarefreeness and absence of affine singularities. Mathematical proofs and limitations appear in `GY1980_development.tex` and the PDF.

## Research and authoring audit

The `parts` directory contains batch data for the records, bibliography and search ledgers, scan-coverage notes and authoring scripts, making the research process inspectable. The seven top-level schema files are the authoritative chapter inputs. The integration and synthesis scripts combine and summarize the audited batches; rebuilding the chapter from those seven files does not require rerunning them.

The `inputs` directory preserves the original English and Russian source files, the manifest and prompt, and the original `GY1980_scans.zip` archive. The supplied earlier index and cumulative bibliography are also included. Extracted scan images and individual source-page files are omitted to avoid duplicating the source archive and transcriptions. To reproduce those working files from the preserved inputs:

```sh
python code/extract_sources.py
```

This script reconstructs the 65 page blocks in each language and the 65 notebook scans, checks their expected range, and records source-file checksums. A separate page-coverage ledger records the source regions used in the chapter.

All 39 records, numbered 490–528, are included. This restores records 510–512, which were wrongly dated 1991 in the source catalog. Status judgments are dated November 2026. The general curve-field embedding conjecture remains the subject of a qualified class-C assessment; the development establishes the bounded results described in the report.

`checks/manifest_sha256.txt` records the payload checksums. `code/package.py` rebuilds the ZIP after successful schema, mathematical, PDF and visual checks; it verifies every archived payload against that manifest and checks the archive CRCs. The manifest excludes itself and the packaging log to avoid circular hashes.
'''
(ROOT/'README.md').write_text(readme)
written='report, README' if args.report_only else 'overview, report, README, area-classification CSV'
print('WROTE '+written+'; counts',counts['items'],'items;',pages,'PDF pages')
