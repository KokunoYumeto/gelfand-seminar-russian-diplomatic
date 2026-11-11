#!/usr/bin/env python3
"""Generate audited counts, the short overview, and the editorial report."""
from pathlib import Path
import collections
import csv
import json
import re

ROOT = Path(__file__).resolve().parent.parent
D = ROOT / "deliverable"
T = json.loads((D / "GY1969_talks.json").read_text())
I = json.loads((D / "GY1969_items.json").read_text())
P = json.loads((D / "GY1969_problems.json").read_text())
C = list(csv.DictReader((D / "GY1969_corrections.csv").open()))
byrecord = {t["record"]: t for t in T}
classes = collections.Counter(x["class"] for x in I)
total = len(I)


def speaker(x):
    value = x.get("speaker") or byrecord[x["record"]]["speaker"]
    value = re.sub(r"\.\s*(?=[A-Z])", ". ", value)
    return value.strip() or "Unattributed"


def area(x):
    r, n = x["record"], int(x["id"].rsplit(".", 1)[1])
    if r in {174, 176, 188, 203, 223, 224} or (r == 175 and n <= 2):
        return "Analysis, differential equations, and linear dynamics"
    if r == 183:
        return "Harmonic analysis"
    if r in {179, 195, 197, 200}:
        return "Operator algebras and quantum statistical mechanics"
    if r in {178, 180, 198, 213, 218, 228}:
        return "Representation theory, quantization, and linear algebra"
    if r == 191 or (r == 192 and n <= 3):
        return "Combinatorics and finite groups"
    if r in {206, 208, 209, 210, 211, 212, 217, 221, 225} or (r == 192 and n >= 4):
        return "Geometry, topology, and quadratic forms"
    if r == 215 and n >= 5:
        return "Geometry, topology, and quadratic forms"
    if r == 219:
        return "Inverse scattering and integrable systems"
    if r == 216:
        return "Representation theory, quantization, and linear algebra"
    if r in {185, 186, 202}:
        return "Seminar programme and mathematical pedagogy"
    return "Algebraic geometry, sheaves, singularities, and periods"


speaker_counts = collections.Counter(speaker(x) for x in I)
area_counts = collections.Counter(area(x) for x in I)
verify_counts = collections.Counter(x["verification"] for x in I)
literal_counts = collections.Counter(x["literal_correctness"] for x in I)
correction_counts = collections.Counter(x["type"] for x in C)
developed = [x["id"] for x in I if x["development"] == "developed in this chapter"]
with (D / "research/item_areas.csv").open("w", newline="") as stream:
    writer = csv.writer(stream)
    writer.writerow(["item_id", "attributed_speaker", "primary_area"])
    writer.writerows((x["id"], speaker(x), area(x)) for x in I)


def table(counts, first="Category", by_count=True, count_label="Items"):
    rows = sorted(counts.items(), key=(lambda kv: (-kv[1], kv[0])) if by_count else (lambda kv: kv[0]))
    return "| " + first + " | " + count_label + " |\n|---|---:|\n" + "\n".join(f"| {k} | {v} |" for k, v in rows)


class_descriptions = {
    "A": "Published soon after by the speaker or Gelfand",
    "B": "Developed by others into established results",
    "C": "Partial development or a qualified partial literature match",
    "D": "Not developed after an adequate search",
    "E": "Already known before the seminar occurrence",
    "F": "The intended mathematical result is not securely identifiable",
}
class_table = "| Class | Meaning in this audit | Items | Share |\n|---|---|---:|---:|\n" + "\n".join(
    f"| {k} | {class_descriptions[k]} | {classes[k]} | {100*classes[k]/total:.1f}% |" for k in "ABCDEF")
earlier_occurrences = sorted({o for p in P for o in p["occurrences"] if int(o.split("-")[0]) < 1969})
stats = {"talks": len(T), "items": total, "problems": len(P), "corrections": len(C),
         "classes": {k: classes[k] for k in "ABCDEF"}, "speakers": dict(sorted(speaker_counts.items())),
         "areas": dict(sorted(area_counts.items())), "verification": dict(verify_counts),
         "literal_correctness": dict(literal_counts), "correction_types": dict(correction_counts),
         "developed_item_ids": developed, "earlier_problem_occurrences": earlier_occurrences}
(D / "research/counts.json").write_text(json.dumps(stats, ensure_ascii=False, indent=2) + "\n")

overview = r"""This chapter follows all 55 catalogue records, 174--228, through the supplied
leaves for 1969--70 and 1970--71. Source order is decisive: Hewitt's November
1969 lecture precedes the February 1970 monodromy entry, and the finite-field
Ramsey question precedes the next sheaf lecture despite its higher record
number. The opening Buchstaber fragment on P000282 belongs to the preceding
year; the Kirillov leaf on P000360 belongs to the following one. Both are
documented as boundary evidence rather than assigned to adjacent speakers
\citep[catalogue, records 173--229]{mccme2026gelfand}.

The principal continuous thread is Kazhdan's course in schemes, sheaves,
affine cohomology and projective constructions, joined to Griffiths's
periods by monodromy, residues and vanishing cycles. A second thread passes
from McDuff's factors and Sinai's quantum chains to Gelfand's current-group
questions and Perelomov's coherent states. Finite groups, four subspaces,
matrix deformations, real curves, characteristic numbers, torsion and
inverse scattering repeatedly connect these strands. Announcements and
reading programmes remain catalogue entries even when they contain no
identifiable mathematical assertion.

The occurrence index contains COUNTITEMS items and the problem index
COUNTPROBLEMS definite questions or conjectures. Counts measure editorial
segmentation, not originality. The historical classes are:
\begin{center}
\begin{tabular}{lrrrrrr}
\toprule
Class&A&B&C&D&E&F\\
\midrule
Items&CLASSA&CLASSB&CLASSC&CLASSD&CLASSE&CLASSF\\
\bottomrule
\end{tabular}
\end{center}
Class E dominates: the seminar mixed exposition, verification and
research questions. Chronology matters.
McDuff's continuum of factors had appeared before her October lecture;
Griffiths's period results had circulated before their 1970 journal issue;
Perelomov's lattice completeness paper preceded his April lecture.
Conversely, later general solutions must not be substituted for narrower
seminar constructions. The general modularity theorem, the Gudkov
congruence and analytic--combinatorial torsion are followed through
their later literature in their respective entries.

Two bounded developments are supplied with complete proofs and independent
checks. For current groups, an infinite tensor product of closely paired
evaluations gives a strongly continuous irreducible representation of
$C^1([0,1],SU(2))$, still irreducible on smooth currents, with support
$[0,1]$. A countersequence shows why its topology cannot be weakened to
uniform continuity. Operator-norm-continuous smooth representations have
finite support by the checked classification
\citep{janssensneeb2015norm}; the notebook's unspecified category remains
an explicit qualification. For the four-subspace question, the orbit of
$S(3,2)^{\oplus2}$ is open dense in
$\operatorname{Gr}(4,6)^4$, giving the requested deformation of
$S(5,2)\oplus S(1,2)$. Its mathematical conclusion is settled here;
the exact historical attribution of that elementary proof is not.
Neither development claims novelty.

Two further annotations audit settled material. A faithful Bell-block
state disproves the claim that commuting finite marginals necessarily
have compatible one-site product eigenbases. Exact rational computations
check all four-site marginals and commutators at two parameter values.
Wavelet scaling verifies the positive answer to the product-uncertainty
question, without validating the separate proposed Gram--Schmidt method.
The arbitrary-sequence coherent-state completeness problem remains
qualified: checked partial criteria do not settle all irregular sets,
and an inaccessible September 2026 preprint prevents a certified global
openness or resolution claim as of 9 November 2026.

The COUNT CORRECTIONS corrections distinguish transcription, translation,
ambiguity, provenance and faithful mathematical error. Earlier-year links
are retained where supported; related themes are not merged into one
problem merely because their titles resemble one another. In particular,
the earlier distribution/foliation slogan is a contextual link, while
the Buchstaber carryover keeps its existing identity. Throughout, the
notes, modern reconstruction, publication match and present mathematical
status are separately visible.
"""
overview = overview.replace("COUNTITEMS", str(total)).replace("COUNTPROBLEMS", str(len(P))).replace("COUNT CORRECTIONS", str(len(C)))
for k in "ABCDEF":
    overview = overview.replace("CLASS" + k, str(classes[k]))
(D / "GY1969_overview.tex").write_text(overview)

report = f"""# GY1969: editorial and research report

**Scope:** the academic years 1969–70 and 1970–71; MCCME records174–228.  
**Status and access date:** 9 November2026.  
**Deliverable:** one data-driven critical companion, generated chapter, compiled PDF, correction ledger, source-check records, and reproducible mathematical checks.

## 1. Coverage and editorial unit

All **{len(T)} catalogue records** are represented. The index contains **{total} mathematical occurrences**, **{len(P)} problem entries**, and **{len(C)} correction records**. Every distinguishable assertion, construction, definition, exercise, conjecture, explicit question and substantive mathematical intervention was considered. Repeated equivalent formulas within one argument are kept together; distinct hypotheses, conclusions and changes of speaker are separated when they change the mathematical content. These counts therefore describe the companion's segmentation of the supplied evidence, not the seminar's mathematical productivity or a count of new theorems.

The packet contains79 scanned leaves, P000282–P000360. Its main in-scope content is P000283–P000359. P000282 carries over Buchstaber material already indexed as1968-173.1–3, with problem GP-1968-42; it is not a new Vainberg occurrence. P000360 starts the subsequent Kirillov quantization material after the closing announcement on P000359. The following catalogue record229 supplies supporting boundary evidence. The original diplomatic material is not rewritten to conceal either boundary.

The catalogue page ranges overlap extensively. Actual headings and separators in the Russian transcription and scans therefore control attribution. Source order is preserved even where it differs from record number or calendar order: Hewitt183 occurs before the1970 heading181 and Kazhdan182; the programme186 precedes the September course heading; Gelfand191's Ramsey item precedes Kazhdan190's sheaf lecture. The report does not reinterpret the incidental numbering of web links as catalogue record numbers. These decisions are recorded in the provenance corrections and source summaries, with the [MCCME catalogue](https://old.mccme.ru/gelfand/notes/all-links.html) as the external identification source.

Date normalization is conservative. Record201's catalogue string `16_Nov-70` becomes `1970-11-16`, with a provenance note. A manuscript/catalogue disagreement such as the November programme's22/23 November notation is exposed rather than silently harmonized. Headings and plans retain their own records; an unidentifiable Kazhdan block in207 does not become an invented mathematical lecture.

## 2. Counts and what they mean

### 2.1 Historical class

{class_table}

The classes are not an epistemic ranking. A correct old theorem can be E even when its proof was not available in the opened source. An A item can contain a faithful manuscript error corrected in the subsequent publication. A mathematically precise reconstruction does not license an exact publication match. The separate literal-correctness, publication-match, verification, development and confidence fields carry these distinctions.

There are no D assignments. Failure to find a result in the first searches was not treated as evidence that an idea was never developed. Where the surviving statement lacks enough structure to identify the intended theorem, F is used with an explicit description of the missing information. Where a precise question has verified partial results but the full modern status cannot be certified, C is retained with a conspicuous limitation.

### 2.2 Attributed speaker

The following totals use the item's explicit speaker override where present and otherwise the catalogue speaker for the containing record. They count occurrences, including interventions, rather than lectures. Administrative records with no mathematical item contribute to the55-record total but not to the item total. The reproducible mapping is in `research/item_areas.csv`.

{table(speaker_counts, 'Attributed speaker')}

### 2.3 Primary area

Each occurrence receives exactly one primary area for this report, so the area totals sum to{total}. Mixed talks are split when their items belong to different subjects—for example, Kazhdan175's spectral material and Artin approximation, Thompson/Conway material in192, and the torsion discussion in215. These area tags are an editorial navigation aid; they do not replace the fixed item schema or assert that a subject has only one mathematical connection.

{table(area_counts, 'Primary area')}

### 2.4 Verification and literal correctness

{table(verify_counts, 'Verification level')}

`Read the result` means that the relevant theorem, formula, proof passage or explicit statement was actually inspected in an opened text. It does not mean that every page of the publication was read or its entire proof independently re-proved. `Publisher metadata checked` verifies identity and chronology, not an inaccessible theorem. `Indirect` identifies a result through an explicit later mathematical source. `Unresolved lead` is a real limitation, not a negative result. The bibliographic `note = {{verified}}` records an opened URL or DOI; it is intentionally weaker than result-level verification.

{table(literal_counts, 'Literal correctness')}

Correctness is assessed against the actual mathematical quantifiers and conventions. Missing compactness, smoothness, finite generation, characteristic, normalization, spectrum simplicity or continuity is stated, rather than supplied without notice. A false literal notebook sentence can remain historically E or A because those classes describe its subject's publication trajectory; the corrected statement and emendation are independently visible.

## 3. Which searches were decisive

### Primary Soviet announcements and exact chronology

Math-Net's short original announcements were especially valuable. The1971 Gelfand–Ponomarev note identifies the finite four-subspace normal forms, including odd-dimensional defect-zero systems that the notebook explicitly excludes. Its receipt date,21 October1970, and1971 publication date are kept distinct from the2 November seminar. This is substantially stronger evidence than matching a later survey's general title (Gelfand & Ponomarev,1971; `gelfandponomarev1971quadruples`).

The earlier Faddeev scattering paper identifies the three-dimensional factorization as pre-seminar work, while the Zakharov–Faddeev paper matches the KdV Hamiltonian and canonical-coordinate continuation. The resulting split between E and A is mathematical and chronological, not a decision to label the whole talk by its most famous later outcome. Original Gohberg material matches the piecewise-continuous Toeplitz/Fredholm discussion, and original Geronimus notes identify the precise site and representation-theoretic construction behind Kirillov's compressed lecture.

The bibliography of a speaker or a later exact theorem also resolved misleading names. The cited1960 authors are Pokornyi and Rybin, not the diplomatic candidate “Rybkin.” Their scalar formal-implicit-function construction is a qualified antecedent, not a priority claim for the full Artin approximation theorem. Melamed's1965 analytic Banach-space equation result likewise has a different parameter and operator scope. Artin's finite-jet analytic approximation is stated with its own hypotheses (Artin,1968; `artin1968analytic`).

### Publication date is not the only date

McDuff's paper appeared in the September1969 Annals issue before her6 October lecture; its principal result is consequently E despite the speaker's authorship. Griffiths's1970 period article records an earlier lecture and manuscript history, preventing the March1970 print issue from making the February seminar automatically A. Perelomov's lattice completeness result was already published before his April1971 talk. Conversely, a manuscript's receipt date alone is not equated with public circulation when no evidence of distribution was found. These decisions are explicit in the relevant fate fields (McDuff,1969; Griffiths,1970; Perelomov,1971).

Hewitt's compact-group equality case illustrates indirect verification. The exact all-compact statement was checked in Russo's later theorem, which expressly credits Hewitt–Ross, while the relevant1970 book's metadata were checked. The1954 abelian result is not silently promoted to a theorem for all compact groups. This item has a qualified publication match and verification assessment rather than a fictitious claim to have read the inaccessible book passage (Hewitt & Ross,1970; Russo,1974).

### Exact quantifiers prevented false resolutions

For current groups, a norm-continuous finite-evaluation classification is not a classification of all strongly continuous representations. Ismagilov's energy-representation irreducibility theorem requires a base of dimension at least five; his segment note proves that the interval energy representation is reducible. Neither settles the general interval-support question by itself. Araki's measurable current category and continuity along one-parameter subgroups are also not silently identified with a C∞ mapping-group topology (Ismagilov,1976,1981; Janssens & Neeb,2015).

For coherent states, lattice completeness, arbitrary discrete uniqueness sets, unrestricted orthonormal bases, regular Gabor systems, and a particular Gram–Schmidt ordering are different questions. A bounded uncertainty product is weaker than bounds for both deviations separately. The Meyer wavelet implication, Bourgain's stronger existence result, and the higher-moment obstructions were checked with those differences in view (Meyer,1987; Bourgain,1988; Gröchenig & Malinnikova,2013).

The arbitrary-sequence problem has an explicit current-status boundary. Verified lattice and perturbative criteria leave general irregular configurations untreated. A September2026 Hou–Ma arXiv lead announces a variational characterization of exact Fock zero sets, but its primary abstract/full-text pages could not be opened in this run. Search metadata were independently corroborated. It is marked unverified, and no secondary AI summary is substituted for the paper. Exact zero sets and uniqueness sets also require a quantifier comparison before transferring a result. The companion therefore makes no global claim that this problem is still open or fully resolved in November2026.

## 4. Developments and independent checks

### 4.1 Full interval support in an explicit strong-continuity category

Item1969-180.2 / GP-1969-02 is developed for C¹ maps from[0,1] to SU(2), with strongly continuous unitary representations. The representation remains irreducible on smooth maps with their usual topology. It uses two evaluations per tensor factor and the diagonal-invariant vector in C² tensor its conjugate. Pair distances are chosen after each finite interpolation bound has been fixed; the remaining tail then tends to zero fast enough to approximate arbitrary local matrix operations.

The chapter proves existence of the infinite tensor product, the group law and unitarity, strong continuity, scalar commutant, and exact full support. It also proves failure of strong continuity for the uniform topology by an explicit sequence whose first N vacuum coefficients multiply to a limit bounded away from one. The norm-continuous class is treated separately using the finite-evaluation theorem. Thus the development answers a precise reconstructed version of the support question; it does not classify all representations or identify an omitted notebook convention (Janssens & Neeb,2015, arXiv Theorems4.11 and4.15).

An independent reader checked the complete proof. The most significant risks were circular dependence in the tail choice, illegitimate isolation of a point in a dense evaluation set, and a mistaken use of irreducibility of a factor representation. None occurs: the induction uses earlier constants only, support is checked by conjugation on a local algebra, and irreducibility follows from the full local matrix algebras and the rank-one vacuum projection. No novelty or historical priority is claimed.

### 4.2 The four-subspace deformation requested in the notes

Item1970-198.12 / GP-1970-23 is proved over the complex numbers in the fixed-dimension product Gr(4,6)^4. For R=S(3,2), the annihilator lines of its four planes form a projective frame, so End(R)=C. Consequently End(R⊕R)=M₂(C), its stabilizer has dimension4, and its GL₆ orbit has dimension32, equal to the ambient irreducible configuration space. The orbit is open dense. A generic line in a local Grassmann chart supplies a holomorphic one-parameter family through S(5,2)⊕S(1,2) whose nearby nonzero fibres lie in that orbit.

This is a complete bounded answer to the requested deformation. The exact historical publication of this elementary proof was not located in the checked announcements; that bibliographical limitation is not called a remaining mathematical obstruction. The C label records the partial historical match before the supplied development. The present-status field expressly states that the bounded question is settled in this chapter.

An independent mathematical review checked the annihilator relation, orbit dimension, density argument, analytic family, and direction of degeneration. A separate exact rational linear-system computation gives endomorphism dimensions1,1,1,7,4 for S(1,2), S(3,2), S(5,2), the special direct sum, and the generic direct sum. Thus the two latter orbit dimensions are29 and32. Code and full output are included.

### 4.3 Faithful commuting marginals without a product eigenbasis

The quantum-state annotation is a correction of an E item, not a fabricated open problem. Put a strictly positive mixture of a Bell projection and the identity on each pair of a period-two qubit chain. Every finite density matrix is a product of complete Bell blocks and maximally mixed single-site factors. After embedding any two finite marginals into their common local algebra, every block is either the same pair density or a scalar identity, so the matrices commute. Their consistency follows by partial trace. Yet the pair density has a simple entangled top eigenvector and cannot be diagonal in any product of one-site bases.

The proof covers all finite subsets, including disconnected ones; no one-site translation-invariance assumption is introduced. It also proves the valid repair when all one-site spectra are simple. The exact code independently computes all16 four-site marginals by basis-index partial traces, compares them with the block formula, checks all256 ordered commutators, and repeats at p=1/2 and p=2/3. The spectrum and partial-transpose checks pass exactly. A repeat run produced byte-identical output. The finite computation checks the algebra; the separate block proof establishes the infinite-chain claim.

### 4.4 Wavelet uncertainty as an audit of a settled question

For a Schwartz orthonormal wavelet, position and momentum deviations scale by2^-j and2^j, so their product is constant across the basis. The calculation is proved by centered moments and independently checked by conjugating the two operators with the dilation–translation unitary. This does not bound the two individual deviations over all scales and does not justify a proposed coherent-lattice Gram–Schmidt order. The historical existence result is B; the calculation is an annotation, not a claim of new mathematics (Meyer,1987; Bourgain,1988).

## 5. Corrections and manuscript authority

The Russian diplomatic transcription controls readings; formula-critical, contradictory and doubtful passages were checked against the scans. Every correction states its page, location, recorded reading, proposed critical reading, evidence, language scope and type. The original wording is preserved in the ledger even when mathematically wrong.

{table(correction_counts, 'Correction type', count_label='Entries')}

Particularly consequential examples are the two incompatible sphere/prequantization normalizations; the absent central quotient in the identification of Conway's simple group; the direct-sum sign where quantum local Hilbert spaces must be tensor products; the degenerate-spectrum diagonalization claim; reversed defect signs and omitted odd-dimensional four-subspace families; the wrong quantifier in a factor-state criterion; an R-linear Hom where residue duality requires a restricted coefficient-linear dual; the reversed Proj containment; strict versus weak Schur-complement inequalities; the KdV Hamiltonian coefficient; the omitted image in the tube exact sequence; and the internally inconsistent Palamodov system.

The y³ appearing in the elliptic-curve note is handled carefully. A smooth plane cubic with an appropriate rational point can still be an elliptic curve; the handwritten exponent does not justify declaring the curve nonelliptic. The apparent intended Weierstrass y² convention is an ambiguity or reconstruction, not an automatic mathematical refutation. Likewise, a crossed-out or overwritten symbol is not recovered solely because a familiar theorem would require it.

## 6. What the A–F scheme misses

First, chronology, truth and verification are independent. “Already known” does not mean “correct exactly as copied,” and a later author's same-subject paper is not an exact match. The current schema's separate assessment fields are indispensable and should remain visible in every display.

Second, the taxonomy has no clean class for an identifiable question whose bounded answer is proved in the companion but whose precise historical publication is unlocated. The four-subspace entry keeps C, a partial literature match, alongside an explicit solved present status and `developed in this chapter`. This use must not be read as a claim of continuing mathematical openness. A future schema should add separate `historical_fate`, `mathematical_status`, and `status_evidence_date` fields rather than overloading a single letter.

Third, modern uncertainty is not nonidentifiability. The arbitrary coherent-sequence question is identifiable and has verified partial results; its2026 status is not certified because an important recent lead was inaccessible. It therefore stays C with a dated limitation, not F or D. By contrast, the incomplete elliptic-system programme lacks a domain, equation class, boundary data and a meaning of “number of solutions modulo2”; this genuinely does not determine one mathematical problem. It is not expanded into an attractive but unsupported index-theoretic conjecture.

Fourth, thematic continuity is not identity of problems. Earlier quantization, periods, affine sheaf constructions, fixed-point formulas and distribution/foliation remarks are linked as context. Earlier problem IDs are reused only when the same question and quantifiers are supported by the supplied previous index. The opening Buchstaber fragment keeps its earlier occurrence identity; it is not counted again. A future cross-year graph should distinguish `same_problem`, `prerequisite`, `same_construction`, `generalization`, `counterexample`, and `historical_context` edges.

Finally, a verified bibliography record is not a verified theorem. A URL-open flag should be supplemented with the exact passage, source type, primary/secondary relation, first-circulation evidence, publication date and access limitations. The supplied `research/source_checks.json` records these details where available without changing the required seven-file schema.

## 7. Presentation on the companion website

A reader entering a talk should first see its date and speaker, the actual source-page span, a short mathematical synopsis, and a conspicuous provenance note if catalogue and source order differ. The next view should list item titles with both historical class and literal-correctness badges. It should take one action to compare “notes,” “precise statement,” and “reconstruction,” and one action to reach the scanned page and the exact cited passage. A large A/B/E badge must not hide a false literal formula.

Problem pages should show the precise current formulation before their chronology. The current-group page needs an explicit comparison of function regularity and representation continuity. The coherent-state page needs separate tabs or sections for lattice completeness, irregular uniqueness sets, uncertainty products, and the proposed orthogonalization method. The four-subspace page should put the requested degeneration next to the direct proof, with the historical-attribution qualification visible. The quantum-state item should link directly to the Bell-block counterexample and its corrected simple-spectrum statement.

The course sequence should be navigable as a chain: Spec and localization → quasi-coherent sheaves → affine acyclicity → punctured affine cohomology → Proj and twisting → rational periods and residue reduction. Parallel links should connect four subspaces to matrix deformations, real curves to unimodular forms and characteristic numbers, and torsion to the earlier determinant/cohomology material. A date-only timeline would obscure these mathematical paths and mishandle the physically displaced Hewitt leaf.

Useful additional fields are `source_order`, `source_anchor`, `catalogue_pages`, `actual_pages`, `date_as_written`, `date_normalized`, `attribution_basis`, `primary_area`, `secondary_areas`, typed cross-item relations, theorem locator, first-public-circulation date with evidence, publication date, and a distinct modern-status certification flag. Preserve stable IDs and anchor links when a reading changes. The correction ledger should be versioned separately from the diplomatic transcription; a reader should be able to see the old reading and the evidence for its emendation.

Search should index Russian quotations, normalized author names and transliteration variants, mathematical synonyms, original notation and modern formulations. Filters should distinguish unverified leads from claims of openness. An accessible text view should accompany formulas and scans, and the JSON and bibliography should remain downloadable for reproducible scholarly use. These are presentation recommendations; no website or external publication was created by this task.

## 8. Reproduction and limits

The fixed-format data files are authoritative. `build_chapter.py GY1969` regenerates the chapter and test driver. The supplied style is preserved; bundled DejaVu Serif font files provide consistent regular, bold, italic and bold-italic rendering. `code/build.sh` runs the builder, XeLaTeX, BibTeX and the two resolving XeLaTeX passes, and includes a local-format fallback for installations whose TeX files exist but filename databases or formats have not been initialized. It does not require system installation or an elevated write.

`code/check_dataset.py` supplements the supplied checks with all55 record identities, assessment enums, dated statuses, citation/ref consistency, reciprocal problem links, control-character detection and coverage counts. The exact mathematics scripts require only the Python standard library. Their outputs and the build/validation logs are included. `research/proof_audit.md` records the independent mathematical review. The final PDF was rendered for layout inspection; final build results are recorded in `output/build_summary.json`.

The main limitations are explicit: not every cited full publication was accessible; some results are known only through an exact later source or publisher metadata; several fragments do not determine a theorem; the arbitrary coherent-sequence problem has an uncertified November2026 global status; and neither supplied development claims novelty. The source ledger distinguishes these limitations from verified positive matches. The packet is a completed bounded critical audit of the supplied records, not an assertion that every historical attribution in this research area has been exhausted.

## Selected references for this report

The full linked bibliography is `GY1969_references.bib`, and the PDF renders the cited entries in the supplied author–date style. The keys below identify the exact records used above; their DOI/URL fields and the source ledger give the checked access points.

- Artin,M. (1968). *On the solutions of analytic equations*. `artin1968analytic`.
- Bourgain,J. (1988). *A remark on the uncertainty principle for Hilbertian basis*. `bourgain1988uncertainty`.
- Gelfand,I.M., & Ponomarev,V.A. (1971). *Problems of linear algebra and classification of quadruples of subspaces in a finite-dimensional vector space*. `gelfandponomarev1971quadruples`.
- Griffiths,P.A. (1970). *Periods of integrals on algebraic manifolds*. `griffiths1970periods`.
- Gröchenig,K., & Malinnikova,E. (2013). *Phase space localization of Riesz bases for L²(Rᵈ)*. `grochenigmalinnikova2013localization`. https://doi.org/10.4171/RMI/715
- Hewitt,E., & Ross,K.A. (1970). *Abstract harmonic analysis* (Vol.II). `hewittross1970abstract`.
- Ismagilov,R.S. (1976). *On unitary representations of the group C∞₀(X,G), G=SU₂*. `ismagilov1976unitary`. https://doi.org/10.1070/SM1976v029n01ABEH003654
- Ismagilov,R.S. (1981). *Representations of the group of smooth mappings of a segment into a compact Lie group*. `ismagilov1981segment`. https://doi.org/10.1007/BF01082288
- Janssens,B., & Neeb,K.-H. (2015). *Norm continuous unitary representations of Lie algebras of smooth sections*. *International Mathematics Research Notices,2015*(18),9081–9137. https://doi.org/10.1093/imrn/rnu231
- McDuff,D. (1969). *Uncountably many II₁ factors*. `mcduff1969uncountably`.
- Meyer,Y. (1987). *Principe d'incertitude, bases hilbertiennes et algèbres d'opérateurs*. `meyer1987uncertainty`.
- Perelomov,A.M. (1971). *On the completeness of a system of coherent states*. `perelomov1971completeness`.
- Russo,B. (1974). *The norm of the Lᵖ-Fourier transform on unimodular groups*. `russo1974fourier`.
"""
# Normalize compressed prose spacing while protecting code identifiers and URLs.
segments = re.split(r"(`[^`]*`|https?://\S+|GY1969)", report)
for n in range(0, len(segments), 2):
    segments[n] = re.sub(r"(?<=[a-zA-Z])(?=\d)", " ", segments[n])
    segments[n] = re.sub(r"(?<=\d)(?=[a-zA-Z])", " ", segments[n])
    segments[n] = re.sub(r",(?=[A-Z0-9])", ", ", segments[n])
    segments[n] = re.sub(r"P\s+(000\d{3})", r"P\1", segments[n])
report = "".join(segments)
report = report.replace("from[0, 1]", "from [0, 1]")
selected_references = ROOT / "work/parts/middle/report_selected_references.md"
if selected_references.exists():
    report = report.split("## Selected references for this report", 1)[0]
    report += selected_references.read_text().strip() + "\n"
(D / "GY1969_report.md").write_text(report)
print(json.dumps({"items": total, "speakers": sum(speaker_counts.values()),
                  "areas": sum(area_counts.values()), "overview_words": len(overview.split()),
                  "report_words": len(report.split())}, indent=2))
