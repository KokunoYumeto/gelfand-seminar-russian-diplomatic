"""Generate the overview, quantitative report, and coverage ledgers.

The narrative is authored for this chapter. Counts are derived from the final
JSON, rather than copied from intermediate research checkpoints.
"""
from pathlib import Path
from collections import Counter, defaultdict
import csv, json, re

OUT = Path(__file__).resolve().parents[2]
CODE = OUT / "code" / "root"

LABELS = {
    "A": "Published soon after by the speaker or Gelfand",
    "B": "Developed by others",
    "C": "Partly developed",
    "D": "No identified development after a documented search",
    "E": "Known before the talk",
    "F": "Not identifiable from the surviving notes",
}

AREAS = {
    667: "Arithmetic geometry and mathematical physics",
    668: "Strings, determinants, and moduli",
    669: "Algebraic geometry, cohomology, and Hodge theory",
    670: "Strings, determinants, and moduli",
    671: "Strings, determinants, and moduli",
    672: "Arrangements and topology",
    673: "Algebraic geometry, cohomology, and Hodge theory",
    674: "Quantum groups and representation theory",
    675: "Strings, determinants, and moduli",
    676: "Quantum groups and representation theory",
    677: "Quantum groups and representation theory",
    678: "Quantum groups and representation theory",
    679: "Editorial headings and plans",
    680: "Quantum groups and representation theory",
    681: "Quantum groups and representation theory",
    682: "Matrix models, maps, and gauge integrals",
    683: "Integrable systems and spectral theory",
    684: "Quantum groups and representation theory",
    685: "Matrix models, maps, and gauge integrals",
    686: "Quantum groups and representation theory",
    687: "Algebraic geometry, cohomology, and Hodge theory",
    688: "Matrix models, maps, and gauge integrals",
    689: "Integrable systems and spectral theory",
    690: "Quantum groups and representation theory",
    691: "Quantum groups and representation theory",
    692: "Quantum groups and representation theory",
    693: "Integrable systems and spectral theory",
    694: "Algebraic geometry, cohomology, and Hodge theory",
    695: "Matrix models, maps, and gauge integrals",
    696: "Modular lattices and subspace representations",
    697: "Quantum groups and representation theory",
    698: "Matrix models, maps, and gauge integrals",
    699: "Editorial headings and plans",
    700: "Automorphic forms, zeta functions, and arithmetic",
    701: "Automorphic forms, zeta functions, and arithmetic",
    702: "Matrix models, maps, and gauge integrals",
    703: "Automorphic forms, zeta functions, and arithmetic",
    704: "Operator algebras and geometry",
    705: "Integrable systems and spectral theory",
    706: "Matrix models, maps, and gauge integrals",
    707: "Strings, determinants, and moduli",
    708: "Probability and dynamics",
    709: "Operator algebras and geometry",
    710: "Operator algebras and geometry",
    711: "Algebraic geometry, cohomology, and Hodge theory",
    712: "Algebraic geometry, cohomology, and Hodge theory",
}
OVERRIDES = {
    "1986-667.4": "Strings, determinants, and moduli",
    "1986-689.5": "Probability and dynamics",
    "1986-689.6": "Probability and dynamics",
    "1986-706.3": "Arrangements and topology",
}

def primary_area(item):
    return OVERRIDES.get(item["id"], AREAS[item["record"]])

def canonical_speaker(name):
    s = re.sub(r"\s+", " ", name).strip()
    # Preserve substantive attribution qualifiers. Only typography is unified.
    clean = re.sub(r"[\s.\-]", "", s).lower()
    aliases = {
        "imgelfand": "I. M. Gelfand", "aabeilinson": "A. A. Beilinson",
        "vlg inzburg".replace(" ", ""): "V. L. Ginzburg",
        "vakazakov": "V. A. Kazakov", "ivcherednik": "I. V. Cherednik",
        "g iolshanskii".replace(" ", ""): "G. I. Olshanskii",
        "v gdrinfeld".replace(" ", ""): "V. G. Drinfeld",
        "ayumorozov": "A. Yu. Morozov",
    }
    return aliases.get(clean, s)

def source_pages(value):
    result = set()
    for a, b in re.findall(r"P0*(\d+)\s*[-–]\s*P?0*(\d+)", value):
        result.update(range(int(a), int(b) + 1))
    result.update(int(x) for x in re.findall(r"P(\d{6})", value))
    return {x for x in result if 1257 <= x <= 1384}

def table(headers, rows):
    def cell(s):
        return str(s).replace("|", r"\|").replace("\n", " ")
    return "\n".join([
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
        *["| " + " | ".join(cell(s) for s in row) + " |" for row in rows],
    ])

def overview_text(counts):
    c = counts["classes"]
    classrows = "\n".join(
        f"{k} & {LABELS[k]} & {c.get(k, 0)} " + r"\\"
        for k in "ABCDEF"
    )
    return r"""
\noindent\textbf{A source-defined year, with two chronological layers.}
This chapter covers all 46 catalogue records 667--712 and the 128 supplied
pages P001257--P001384. It follows manuscript order while retaining catalogue
record numbers and dates; these are identifiers, not a silently corrected chronology. The manuscript
dates in the opening spring sequence often say 1986 where the catalogue
says 1987, and record 667 has an earlier handwritten year. Such conflicts
are recorded at the affected talks. Shared page ranges are not copied
wholesale into both talks: headings, page layout, and the mathematical
continuity determine the attributed passage. In particular, the Gurevich
heading on P001303 qualifies record 684's catalogue attribution, and the
Beilinson heading on P001319 recovers surviving material for record 694,
whose catalogue entry has no linked pages. A boundary fragment at P001257
is linked to its earlier-year occurrence rather than reassigned to
Kontsevich. The catalogue itself was checked
\citep{mccme2026gelfandcatalogue}.

\medskip
\noindent\textbf{The mathematical lines.}
String measures and determinants, arrangements of real and complex
subspaces, quantum groups and their representations, matrix integrals
and map enumeration, integrable systems, modular lattices, automorphic
forms, and cohomological constructions run through the packet. The
apparently separate talks often share a concrete obstruction: deciding
what remains valid after a deformation, identifying the correct quotient
or completion, or distinguishing a formal generating series from an
analytic integral. The later fate is correspondingly heterogeneous.
Several talks can be matched to near-contemporary publications; others
restate earlier results; a few questions remain meaningful only after
their missing hypotheses and intended output are specified.

\medskip
\noindent\textbf{Inventory and assessment.}
There are """ + str(counts["items"]) + r""" distinct indexed items, """ + str(counts["problems"]) + r"""
problem-index entries, and """ + str(counts["corrections"]) + r""" corrections or provenance notices.
An item is a mathematical unit, not a page or a sentence.
\begin{center}
\begin{tabular}{cl r}
\hline
Class & Historical assessment & Items\\
\hline
""" + classrows + r"""
\hline
\end{tabular}
\end{center}
Class records historical fate; it does not certify literal correctness.
The separate fields retain missing hypotheses, false literal formulas,
partial publication matches, and the actual level of source inspection.
F includes unrecoverable fragments and unsupported precise readings;
it does not mean that their surrounding subject is unknown.
""" + (
        r"No item is assigned D: the searches did not justify an assertion that a precise idea had received no development."
        if c.get("D", 0) == 0 else
        r"The D entries state their limited search coverage; failure to locate a result is not treated as a proof of absence."
    ) + r"""

\medskip
\noindent\textbf{Bounded developments.}
Two class C questions support explicit work. For the quantum KdV spectral
problem, a complete level-two calculation exhibits a genuine Jordan block
in an irreducible, nonunitary Virasoro module. Thus an unrestricted
eigenbasis formulation needs an extra hypothesis; the notebook itself
does not assert semisimplicity. For the two-source unitary integral,
probability Haar normalization gives a regular entire \(U(2)\) formula,
an all-rank convergent moment expansion with a proved tail bound, and
an exact \(U(3)\) counterexample to a specified naive permutation-only
extension. These do not settle an all-grade spectrum or a generic
large-\(N\) asymptotic problem. Two further annotations rederive a known
transverse-plane criterion and certify the notebook's existing answer
of 96 cube regions. Independent derivations or algorithms agree in
every reported test; code and complete outputs accompany the chapter.

\medskip
\noindent\textbf{Questions and continuity.}
The problem index separates construction of quantum KdV charges from
their spectral classification; finite multi-source integrals from the
broader reduced gauge integral; and established special cases from
unrestricted arithmetic conjectures. Earlier problem identifiers are
reused only for exact recurrences, notably the determinant question
GP-1982-40. Other earlier occurrences are linked as antecedents where
their quantifiers differ. Broad thematic resemblance is not an identity.
The toroidal reformulation of the Riemann hypothesis requires the
correct spectral condition, including temperedness; neither an
unrestricted unitarity slogan nor a related theorem settles RH.

\medskip
\noindent\textbf{Status and evidence.}
The cutoff is 12 November 2026. Newly circulated 2026 papers are explicitly
identified as preprints, with the version and theorem actually inspected;
their existence is not presented as independent proof certification.
Every bibliography entry carries a verification note, and unresolved
leads remain distinguishable from results read in the primary source.
The report provides counts by speaker and area, records the difficult
attributions and searches, and specifies how a website should expose
source, reconstruction, literature, and present status separately.
"""

def main():
    talks = json.loads((OUT / "GY1986_talks.json").read_text())
    items = json.loads((OUT / "GY1986_items.json").read_text())
    problems = json.loads((OUT / "GY1986_problems.json").read_text())
    counts = json.loads((CODE / "assembly_counts.json").read_text())
    with (OUT / "GY1986_corrections.csv").open(newline="") as f:
        corrections = list(csv.DictReader(f))
    tmap = {t["record"]: t for t in talks}
    perrecord = Counter(x["record"] for x in items)
    classes = Counter(x["class"] for x in items)
    areas = Counter(primary_area(x) for x in items)
    speakers = Counter(canonical_speaker(x.get("speaker") or tmap[x["record"]]["speaker"]) for x in items)
    records_by_speaker = Counter(canonical_speaker(t["speaker"]) for t in talks)
    allspeakers = sorted(set(speakers) | set(records_by_speaker))
    coverage = defaultdict(list)
    for x in items:
        for page in source_pages(x["pages"]):
            coverage[page].append(x["id"])
    uncovered = [f"P{p:06d}" for p in range(1257, 1385) if p not in coverage]
    coverage_output = {
        "method": "Expand each occurrence's source-page ranges; page overlap is permitted and is not duplicate mathematical content.",
        "pages": {f"P{p:06d}": coverage[p] for p in range(1257, 1385)},
        "pages_without_occurrence_reference": uncovered,
    }
    (CODE / "page_coverage.json").write_text(json.dumps(coverage_output, ensure_ascii=False, indent=2) + "\n")
    with (CODE / "item_areas.csv").open("w", newline="") as f:
        w = csv.writer(f); w.writerow(["item", "primary_area"])
        w.writerows((x["id"], primary_area(x)) for x in items)
    (OUT / "GY1986_overview.tex").write_text(overview_text(counts).strip() + "\n")

    parts = [
        "# GY1986: critical-companion research and validation report",
        "",
        "**Status cutoff:** 12 November 2026. **Coverage:** catalogue records 667–712; supplied source pages P001257–P001384. The final chapter preserves the source-defined academic-year identifier 1986 throughout.",
        "",
        "## 1. Deliverable and principal findings",
        "",
        f"The chapter contains all **{len(talks)} catalogue records**, **{len(items)} mathematical items**, **{len(problems)} problem-index entries**, **{len(corrections)} correction or provenance notices**, and **{counts['references']} bibliographic entries**. The seven standard data files generate the supplied chapter and standalone PDF. Reproducibility materials include the builder and style, mathematical programs with their full outputs, input checksums, quantitative ledgers, and a research log containing queries and source metadata.",
        "",
        "The most consequential finding is that chronology and attribution cannot be read mechanically from the catalogue's page ranges. The opening spring sequence contains manuscript years that disagree with the catalogue. Several pages hold the end of one speaker's material and the beginning of another's. A page-range overlap therefore provides a search window, not an authorship decision. The chapter preserves the catalogue as catalogue metadata and records manuscript evidence in the summaries and corrections.",
        "",
        "The mathematical outcome is similarly differentiated. Many items are expository or can be matched to near-contemporary publications. Definite questions were not manufactured from every unexplained formula. The bounded developments address two partial problems: quantum KdV spectra and multi-source unitary integration. The complex-structure and cube sections are explicit verification annotations to material whose relevant answer was already known. The markers in the chapter identify work performed here without claiming historical originality.",
        "",
        "## 2. Counts and their interpretation",
        "",
        "### 2.1 Items by historical class",
        "",
        table(["Class", "Meaning", "Items"], [(k, LABELS[k], classes.get(k, 0)) for k in "ABCDEF"]),
        "",
        "An item is one distinct mathematical assertion, definition, construction, question, or method. Counts therefore measure the granularity of this critical edition, not the number of independent discoveries or open problems. A theorem and an essential hypothesis correction can occupy one item; a long formula sequence may require several items when its logical claims differ.",
        "",
        ("No item is assigned class D. This is a deliberate evidential decision: a finite search did not justify claiming that an identifiable mathematical idea had received no development. Ambiguous statements remain F; precise but only partly treated questions remain C."
         if not classes.get("D") else
         "Class D records a bounded search outcome rather than an assertion that no relevant work exists. The item-level search descriptions are part of the evidence and should remain visible."),
        "",
        "### 2.2 Items by attributed speaker",
        "",
        "The second column counts catalogue records, including headings and plans under their catalogue labels. The third counts mathematical items using the item-level speaker override when present. Joint and qualified attributions are retained rather than divided fractionally between people. Consequently the two columns answer different questions.",
        "",
        table(["Speaker or attribution", "Catalogue records", "Items"], [(s, records_by_speaker[s], speakers[s]) for s in allspeakers]),
        "",
        "### 2.3 Items by primary area",
        "",
        "Each item is counted once. These broad editorial categories are for navigation, not a claim that the subject boundaries are intrinsic. The item-to-area mapping is supplied separately as code/root/item_areas.csv. Records supply the default category; explicit overrides handle the boundary determinant fragment, the slab and billiard remarks, and the cube count.",
        "",
        table(["Primary area", "Items"], sorted(areas.items(), key=lambda kv: (-kv[1], kv[0]))),
        "",
        "### 2.4 Assessment fields",
        "",
    ]
    for field, title in [
        ("literal_correctness", "Literal correctness"),
        ("publication_match", "Publication match"),
        ("verification", "Source verification"),
        ("development", "Development"),
        ("confidence", "Identification confidence"),
    ]:
        parts.extend(["#### " + title, "", table(["Assessment", "Items"], sorted(counts[field].items())), ""])
    parts.extend([
        "### 2.5 Record coverage",
        "",
        table(["Record", "Catalogue date", "Items", "Title"], [
            (t["record"], t["date"], perrecord[t["record"]], t["title"]) for t in talks
        ]),
        "",
        "The occurrence-page ledger is code/root/page_coverage.json. It expands explicit page ranges and permits shared pages. It is a coverage aid: the mere presence of an occurrence reference does not certify that every mark on a page has been deciphered.",
        "",
        ("All 128 supplied pages occur in the item-level page ledger."
         if not uncovered else
         "Pages without an item-level reference: " + ", ".join(uncovered) + ". Their role must be read together with the record summaries and provenance notices; headings alone do not create mathematical items."),
        "",
        "## 3. Difficult source decisions",
        "",
        "### Chronology is evidence, not a sorting convenience",
        "",
        "The catalogue gives 1987 dates for records 667–678, while numerous manuscript headings in this block give 1986. Record 667 has a further discrepancy in its handwritten year. The near-contemporary Olshanskii announcement supplies an external chronological anchor: its presentation and receipt information belong to May 1986. This supports the manuscript sequence but does not authorize rewriting every catalogue date from inference. Every occurrence keeps the task's academic-year prefix 1986.",
        "",
        "The catalogue's apparent lack of pages for record 694 is also insufficient to conclude that its mathematics is lost. The supplied manuscript contains a dated Beilinson heading and subsequent notes at P001319–P001321. The chapter indexes that surviving material and explicitly distinguishes this editorial allocation from the archive's record-link metadata.",
        "",
        "### Authorship changes inside a page",
        "",
        "The end of the earlier Beilinson discussion at P001257 is not assigned to Kontsevich merely because it lies inside record 667's page window. Its earlier occurrence is linked. The Gurevich heading at P001303 is retained despite record 684's Ginzburg catalogue label. The Gelfand preamble and Beilinson arithmetic discussion around P001355 are separated by the manuscript heading. Item-level speaker fields make those decisions inspectable.",
        "",
        "### Formulas whose conventions decide the result",
        "",
        "The corrections distinguish a transcription error from a faithful reproduction of a mathematical slip. Examples include the positive square versus inverse square in the affine-Hecke evaluation, the Gaussian normalization in the cubic matrix model, a missing cyclic constraint among three angular matrices, the meaning of finiteness in the definition of a preprojective representation, and the spectral-operator matrix whose written square is incompatible with the asserted relation. Each correction identifies the page, the competing readings, and its evidence.",
        "",
        "The spectral-operator correction is particularly diagnostic. With the displayed matrix sign, the claimed commutator is nonzero. With the indicated sign correction, two exact calculations agree that the operators commute: composition by derivative coefficients and their direct action on polynomial vectors at rational arguments. The source scan supports classifying this as a faithful notebook error rather than silently repairing the diplomatic transcription.",
        "",
        "Some uncertainty appropriately survives. In the opened OCR of the Gelfand–Lidskii–Ponomarev announcement, an inequality endpoint is not reliably distinguishable from a lost equality bar. The entry states the safe restricted range and explicitly records the unresolved reading. A remark that a case was unproved in 1987 is not upgraded to a claim that it is open in November 2026.",
        "",
        "## 4. Literature search: what established the matches",
        "",
        "Searches followed the mathematical object and its quantifiers, not only the speaker and a broad topic. Author and year searches located likely publications; primary full texts or publisher records then determined what had actually been verified. The research ledger records successful and failed retrieval attempts. A bibliography note saying verified means that its URL or DOI was opened; the occurrence's verification field separately states whether the result, metadata, or only an indirect lead was inspected.",
        "",
        "Math-Net was particularly useful for Soviet announcements, including the centralizer construction, the KdV geometric formulation, modular lattices, and related representation-theoretic work. Publication dates were compared with receipt and presentation dates where these were visible. This prevented a 1987 publication from being mechanically classified as a development of a supposed 1987 talk when the manuscript and submission chronology point to 1986.",
        "",
        "Backward tracing from later primary papers was decisive in several places. The simultaneous-complex-structure question can be compared with Batzies's four-plane classification (2007, Theorems 1 and 3). The cyclotomic affine-Hecke quotient can be matched to the Ariki–Koike construction through the explicitly stated basis theorem in Mathas's exposition; the dimension assertion does not require generic semisimplicity. The finite-source unitary problem is treated by Holguin, Wang, and Wang (2024, Sections 2.2–2.3 and Appendix A), while the all-rank polynomial moments have a separate precise source in Collins and Śniady (2006, Corollary 2.4).",
        "",
        "The late-2026 status check required version-specific caution. The quantum KdV completeness source is the opened May 2026 version of Masoero and Ruzza, with its stated central charge, highest weights, admissibility conditions, and theorem number. Recent claims concerning the four-strand Burau representation and supermoduli are identified as preprints, not silently represented as settled journal literature. An opened theorem statement establishes the scope of a claimed result; it does not imply that this project independently checked its whole proof.",
        "",
        "The exact sources, titles, publication metadata, links, and verification notes are in GY1986_references.bib and the PDF bibliography. Locators appear at the individual claims. This report deliberately does not replace those precise claims with broad assertions that a topic has been solved.",
        "",
        "## 5. Bounded developments and independent checks",
        "",
        "### 5.1 Quantum KdV: a real obstruction to an unrestricted eigenbasis",
        "",
        "For the BLZ normalization of I3, the level-two Virasoro matrix has nonscalar part [[8h+c,12h],[6,8h+4]] and discriminant (c−4)²+288h. At c=1 and h=−1/32 it has a nonzero square-zero nilpotent part. The chapter proves that grade two survives in the irreducible highest-weight quotient, by excluding singular vectors in grades one and two. This is a counterexample to an unrestricted ordinary-eigenbasis formulation, not to the notebook's request to determine a spectrum.",
        "",
        "The algebraic derivation was checked independently by recursive PBW rewriting. A separate contravariant Gram matrix calculation checks form symmetry, and additional grades and parameter choices test the implementation beyond the exhibited matrix. The example is nonunitary and does not contradict diagonalizability in a positive-definite setting. Generalized eigenspaces and nilpotent actions remain part of the correctly formulated general spectral problem.",
        "",
        "### 5.2 Multi-source unitary integration: exact finite evaluation with scope",
        "",
        "Probability Haar measure gives the U(2) integral as (exp(alpha)−exp(beta))/(alpha−beta), continuously extended at equal endpoints. The proof uses the uniform distribution of the squared first entry. For every N, the chapter derives a convergent moment expansion from the permutation-operator Gram pseudoinverse and proves an explicit exponential-series tail bound. The pseudoinverse is essential when the degree exceeds N.",
        "",
        "Independent checks compare the moment implementation with direct U(2) integration, including complex and coincident endpoints, and with an ordinary rank-one HCIZ determinant at N=3. A separate exact U(3) example shows that a specified naive permutation-only extension has a pole at zero coupling while the true integral is entire and equals one there. Every quadratic factor is also checked by Givens rotations. This addresses a tempting reconstruction; the notes themselves only propose an approximation and are not accused of stating the false exact formula.",
        "",
        "These results do not make the factorial moment algorithm efficient at large N, nor do they settle a compact generic formula or a universal asymptotic regime. The next tractable task is to fix N, source rank, and an error tolerance, exploit symmetries in the moment tensors, and compare a stated approximation against proved tails.",
        "",
        "### 5.3 Two verification annotations",
        "",
        "For pairwise transverse real two-planes in R4, the chapter rederives the common linear complex-structure criterion using three planes in normal form and a two-dimensional centralizer. A full four-by-four invariance calculation checks the criterion independently. A continuous family with constant intersection lattice shows why combinatorial data alone do not decide linear complexifiability. This is credited against the known classification; it is not presented as a new general classification of arrangements.",
        "",
        "For the cube, enumeration of its 56 vertex triples gives 20 distinct planes, of which 14 cut its interior. Exact convex-cell splitting gives 96 regions. A separate intersection-flat and Möbius calculation gives 1+14+47+34=96. The 96 rational interior witnesses and their distinct sign vectors are supplied. The notebook already contains the answer 96, which is confirmed.",
        "",
        "The ancillary high-dimensional slab computation compares an incomplete-beta formula with direct density quadrature at high precision. A half-width 0.01R in dimension 1000 gives approximately 0.2482363770; interpreting 0.01R as full width instead gives approximately 0.1256648689. The convention changes the answer substantially, so the annotation states it explicitly.",
        "",
        "## 6. What the A–F classification misses",
        "",
        "Historical fate and mathematical validity are independent axes. A can contain a theorem accurately published soon after but incorrectly transcribed here. E can contain a difficult, important theorem which was simply already known. B can identify an exact later result for a restricted subcase while a broader problem remains C. F can arise from missing domains or ambiguous notation even when a nearby standard theorem is well understood.",
        "",
        "The quantum KdV records illustrate why construction, commutativity, spectrum, and completeness should not share one class merely because they concern the same charges. The unitary-integral records likewise separate finite-N evaluation, a tractable closed expression, large-N asymptotics, and the broader reduced gauge theory. A convergent series answers one interpretation of evaluation while leaving another legitimate target unresolved.",
        "",
        "The current scheme also lacks a dedicated field for bibliographic certainty distinct from mathematical confidence. A directly opened abstract can verify a work's existence and date without verifying a theorem's hypotheses. The present chapter therefore uses the existing verification and publication-match fields conservatively, with explanatory prose. No class is used to turn a 1987 authorial remark into an unqualified 2026 assertion.",
        "",
        "## 7. Proposed method and format changes",
        "",
        "Add separate catalogue_date, manuscript_date, and date_confidence fields. Retain source-order position independently of chronological sorting. A single date field cannot represent this packet faithfully, and changing the catalogue date silently would break provenance.",
        "",
        "Add source_segments with page, region, and attributed speaker. A whole-page range is insufficient when two or three talks share a sheet. This need not require geometric coordinates immediately: a controlled description such as before heading or lower half already improves reproducibility.",
        "",
        "Add relation objects between occurrences and problems, with types exact recurrence, special case, generalization, antecedent, and thematic connection. Exact recurrences may reuse a problem ID; other relations must not merge different quantifiers. A problem should also distinguish the formulation supported by the notebook from a modern research target.",
        "",
        "Add source_version, theorem_locator, first_circulation_date, inspected_on, and proof_review_status to citation evidence. The global BibTeX note remains useful but cannot encode all these distinctions. For preprints, the verified version should remain fixed even if the abstract URL later points to a revision.",
        "",
        "Add computation metadata: program path, output path, arithmetic model, theorem or example supported, and independent-check method. A numeric experiment and an exact proof certificate should be searchable separately. The present code/root/proof_review.md and output files provide that information in prose.",
        "",
        "Keep corrections typed. A faithful_error must never overwrite the diplomatic Russian source in a website. Show the manuscript reading beside the editorial mathematical emendation. Likewise, ambiguity should remain visible until a source reading or proof resolves it.",
        "",
        "## 8. Website presentation",
        "",
        "A reader arriving at a talk should first see its short mathematical summary, a compact chronology or attribution notice when needed, and a list of item titles. Each item should expose four separately labelled views: notebook wording, modern precise statement, editorial reconstruction, and literature/status. The class badge should sit beside the literal-correctness and verification assessments so it cannot be mistaken for a truth rating.",
        "",
        "The most useful immediate links are the exact source page, any correction affecting the formula, the problem's cross-year trajectory, and the cited theorem locator. Developed items should link directly to the relevant proposition and its computation output. Cube readers should be told immediately that the notebook already gives 96; quantum KdV readers should immediately see the missing representation hypotheses.",
        "",
        "Provide both source-order and chronological browsing, with catalogue and manuscript dates displayed separately. Keep record 694 discoverable through the recovered manuscript heading even though the catalogue has no page links. Speaker search should use the item attribution, while also allowing the catalogue label to be searched.",
        "",
        "The problem index should distinguish precise recurrence from related mathematics. Reused earlier IDs, including GP-1982-40, should be navigable back to the earlier indexed occurrences. Multi-source integral occurrences should connect across records 688, 695, and 698 without conflating them with the general reduced gauge integral. Search facets should include area, class, correctness, verification, source year, and whether a bounded development or executable check is available.",
        "",
        "## 9. Reproduction and validation",
        "",
        "Run python build_chapter.py GY1986 in the extracted archive, then XeLaTeX, BibTeX, and two further XeLaTeX passes on GY1986_test.tex. The standard files are sufficient to rebuild the chapter. The supplied original kit is retained under code/kit_original; any compatibility edits are explained in the build notes. Mathematical programs require Python, SymPy, and mpmath as recorded in the validation output.",
        "",
        "The assembly validator checks all 46 catalogue records, sequential occurrence IDs, mandatory fields and allowed values, the presence of all cited keys, bibliography verification notes, source-page bounds, problem references, and earlier occurrence identifiers against the supplied previous index. The report counts are generated from the final JSON. Final builder, LaTeX, PDF, and archive checks are recorded in code/root/final_validation.json.",
        "",
        "Full retrieved third-party article texts are not redistributed. The research log preserves requests, source URLs and titles, and retrieval failures; the bibliography and annotations preserve the results and locators actually used. The original source attachments remain the authoritative input packet, identified by SHA-256 hashes.",
        "",
        ("Unverified bibliography entries: " + ", ".join(counts["unverified_references"]) + ". These are retained as explicitly labelled leads, not as verified mathematical support."
         if counts["unverified_references"] else
         "Every bibliography entry has a verified URL/DOI note. This statement concerns opening the bibliographic source and must be read with the more granular item-level verification fields."),
        "",
        "The final checks certify the supplied finite calculations and the chapter's internal consistency. They do not certify every proof in the cited literature, resolve every ambiguous mark, or establish historical novelty of the elementary developments.",
        "",
    ])
    (OUT / "GY1986_report.md").write_text("\n".join(parts))
    print(json.dumps({
        "overview_words_approx": len((OUT / "GY1986_overview.tex").read_text().split()),
        "report_words": len((OUT / "GY1986_report.md").read_text().split()),
        "pages_without_occurrence_reference": uncovered,
        "primary_area_counts": dict(areas),
        "speaker_item_total": sum(speakers.values()),
        "area_item_total": sum(areas.values()),
    }, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
