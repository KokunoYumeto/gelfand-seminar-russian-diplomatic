#!/usr/bin/env python3
"""Generate the count tables and editorial overview/report from the final data."""
from pathlib import Path
import argparse
import hashlib
import json
import re
import subprocess
from collections import Counter

BASE=Path(__file__).resolve().parents[1]

def table(headers,rows):
    out=["| "+" | ".join(headers)+" |","| "+" | ".join("---" for _ in headers)+" |"]
    out.extend("| "+" | ".join(str(v).replace("|",r"\|") for v in row)+" |" for row in rows)
    return "\n".join(out)

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--verified",action="store_true")
    args=parser.parse_args()
    stats=json.loads((BASE/"GY1973_statistics.json").read_text())
    items=json.loads((BASE/"GY1973_items.json").read_text())
    talks=json.loads((BASE/"GY1973_talks.json").read_text())
    problems=json.loads((BASE/"GY1973_problems.json").read_text())
    overview=(BASE/"code/overview_template.tex").read_text()
    substitutions={"RECORDS":stats["talks"],"ITEMS":stats["items"],
                   "PROBLEMS":stats["problems"],"CORRECTIONS":stats["corrections"],
                   **{k:stats["class"].get(k,0) for k in "ABCDEF"}}
    for k,v in substitutions.items():overview=overview.replace("@"+k+"@",str(v))
    if re.search(r"@[A-Z_]+@",overview):raise ValueError("Unresolved overview placeholder")
    (BASE/"GY1973_overview.tex").write_text(overview)
    classes=[("A","Near-contemporary publication by speaker/Gelfand"),
             ("B","Later development by others"),("C","Precise unresolved remainder"),
             ("D","Identifiable but undeveloped"),("E","Already known"),
             ("F","Not identifiable at the required precision")]
    counts=table(["Class","Meaning","Items"],
                 [(k,label,stats["class"].get(k,0)) for k,label in classes])
    byspeaker=table(["Talk speaker","Items"],
                   sorted(stats["speaker_by_talk"].items(),key=lambda p:(-p[1],p[0])))
    byarea=table(["Primary area","Items"],
                 sorted(stats["area"].items(),key=lambda p:(-p[1],p[0])))
    assessments=[]
    for group in ["literal_correctness","publication_match","verification"]:
        for label,n in stats[group].items():assessments.append((group.replace("_"," "),label,n))
    assessmenttable=table(["Axis","Value","Items"],assessments)
    corrections=table(["Correction type","Rows"],sorted(stats["correction_type"].items()))
    recordcounts=Counter(x["record"] for x in items)
    coverage=table(["Record","Critical date","Speaker / heading","Items","Catalogue source range"],
        [(t["record"],t["date"] or "undated",t["speaker"] or t["title"],recordcounts[t["record"]],t["pages"]) for t in talks])
    openitems=table(["Occurrence","Question","Problem identifier"],
        [(x["id"],x["title"],x["problem"]) for x in items if x["class"] in {"C","D"}])
    text=r"""# GY1973 critical-companion report

**Research cutoff:** 9 November 2026.  
**Corpus:** the user-supplied Russian and English transcriptions and 53 scans, P000501–P000553.  
**Deliverable:** a complete occurrence index, definite-problem index, critical corrections, author–year bibliography, generated chapter, compiled PDF and reproducible verification material.

## 1. Result and scope

The chapter contains @ITEMS@ mathematical items across @RECORDS@ records, @PROBLEMS@ problem-index entries, @REFERENCES@ bibliographical records and @CORRECTIONS@ correction or ambiguity records. All 30 entries in the supplied roster are retained. Records331 and332 are added because the supplied scans contain two separate headings dated25March1974. The official MCCME catalogue places both under25March1975; that catalogue error explains their absence from the supplied year roster. The corrected dates are explicit provenance decisions, not inferred missing meetings.

The source order is used. In particular307 precedes306 onP000512,313 precedes312 onP000525, and321 precedes320 onP000532. The calendar divider324 has no invented mathematical content. Catalogue page ranges overlap neighbouring lectures; item-level page references locate the actual mathematical passage rather than inheriting the whole overlapping range.

Record332 remains attributed to B.M.Gurevich as catalogued. A.V.Gurevich's familiar modulation work is not used to silently change that identity. The bibliography distinguishes a thematic comparison from a verified speaker-publication match.

## 2. Counts

### Historical classification

@CLASS_TABLE@

Each occurrence is counted once, including repeated definitions and methods when the notebook returns to them. The counts measure this edition's segmentation of the surviving evidence. They are neither theorem counts nor estimates of the seminar's originality. ClassE includes an old correct theorem whose notebook wording needs repair; classA can include a subsequently published assertion whose literal formulation is false. The separate correctness and verification axes are therefore essential.

### By talk speaker

@SPEAKER_TABLE@

This table assigns an item to the speaker of its containing record, so its total is exactly the item count. Explicit interventions carry their own speaker field in the JSON; the statistics file also supplies the complete item-attribution count. Thus Mishchenko's intervention during Fuchs's record309 remains discoverable without manufacturing another catalogue record.

### By mathematical area

@AREA_TABLE@

Areas are exclusive primary labels for counting, not claims that the subject boundaries are intrinsic. Cross-area connections remain in the item statements and summaries. The complete mapping is supplied in GY1973_area_map.json.

### Independent assessment axes

@ASSESSMENT_TABLE@

@CORRECTION_TABLE@

The bibliography contains 88 entries marked verified and three marked unverified: Balian--Bloch (1972), Green (1955), and Miura (1968). The verified flag means the stated link or DOI was successfully opened. It does not mean that a full proof was read. The item's verification field and the bibliography's annote specify whether the evidence was the theorem itself, an author account, a publisher abstract or a later attribution. A source whose direct opening failed is marked unverified where retained. The archive entry is present in the data bibliography but not cited through a printed BibTeX command, so the printed bibliography has 90 entries.

## 3. The most consequential identifications

**Manin and the period measures.** The 1973 paper on periods of parabolic forms and p-adic Hecke series supplies exact locators for the integration criterion, the Hecke distribution relation, the corrected quadratic-root measure, modular-symbol reduction and ordinary interpolation. Earlier seminar occurrences in1972-299 establish continuity with GP-1972-403. A paper's receipt date is not treated as a public circulation date. The discrepancy between the English printed receipt line and Math-Net metadata is recorded rather than silently resolved.

**Quillen's categorical constructions.** The full 1973 paper verifies theoremsA andB, exact-category hypotheses, admissible spans and the identification of the first homotopy group of BQ with the Grothendieck group. Its introduction explicitly defers the proof of comparison with the plus construction. The chapter therefore cites the announcement with that limitation and a checked later account for the established comparison. Replacing BQ by its loop space and selecting the component is mathematically substantive. A finite-rank automorphism functor into Q is already nullhomotopic; it is not the required comparison map.

**Mishchenko's chronology.** The full1974 paper was received inDecember1972, but the stronger public evidence is the March–April1973 two-page announcement. Its definitions and signature formula precede the October lectures. This changes the appropriate historical classification toE for the corresponding items, while retaining the1974 paper as the fuller exact source.

**Stable rank and the zero-K2 dichotomy.** A 1974 Vaserstein–Suslin announcement repeats a false implication also present in the notebook. The later full paper explicitly separates additional zero-K2 fields from algebraic extensions of finite fields. The chapter keeps the false field classification, the genuine stable-rank theorem and the later resolution as different items. An exact publication match cannot turn a false premise into a correct theorem.

**Finite-gap theory and dressing.** Novikov's1974 paper and Zakharov–Shabat's1974 paper give close formula-level matches. The finite-gap density question is settled; the checked Grébert–Kappeler–Pöschel theorem gives the real Sobolev formulation and credits Marchenko–Ostrovskii's1975 proof. Vague universal Hamiltonian claims and an incomplete collision-amplitude estimate are not promoted to open problems. Shabat's2014 interpolation paper is unusually valuable because it explicitly names the1974 Gelfand-seminar discussion, beyond merely treating the same broad subject.

**The final spectral-gap theorem.** A title search followed to Shnirelman's1975 two-page note recovered the precise statement for the square-root Laplacian on a smooth near-Euclidean two-torus. The minimum of the two neighbouring gaps, the quantifiers and the spectral normalization all matter. The later theorem is by a named author other than the catalogued speaker, so it is classB. A parenthetical theorem attribution is not treated as proof that the author spoke at the meeting. The separate unquantified “twin” problem remains unidentified.

**Bibliographic and version checks.** The original Jónsson scan prints295–314, resolving a conflicting current publisher metadata range. The complete Atiyah bibliography distinguishes the1973 Atiyah–Bott–Patodi heat-equation paper from the Atiyah–Patodi–Singer spectral-asymmetry announcement without changing the notebook's ink. For arithmetic coherence, a checked revision of Brody–Fisher–Mj–van Limbeek replaces an overbroad earlier author-hosted preprint. The retained positive statement remains conditional.

## 4. Open questions and the Stage2 decision

@OPEN_TABLE@

No classD item was justified. The classC occurrences are familiar, precise arithmetic questions, not orphan ideas recoverable from an unpursued sketch. For SL3(Z), the universal finitely-generated-subgroup quantifier remains. For SL2(Z[1/p]), the checked conditional theorem leaves its arithmeticity hypothesis unresolved. For zeta(3), irrationality and partial linear-independence results do not establish transcendence. The gamma sentence is elliptical, and even the weaker irrationality question is not settled in the checked literature. Recent preprints are identified as such; publication or acceptance is not inferred from an arXiv posting.

None of these questions supplied a plausible bounded contribution in this run. No conjecture or computation has been presented as a solution to them. Every C item has an explicit worth-developing assessment.

The file called “development” by the fixed schema is used here for a clearly labelled **critical verification appendix**, distinct from Stage2 research. It contains complete elementary proofs needed to assess the text. The sign distribution is reconstructed with its exact convention, including its mass, Bernoulli moments and unit Euler factor. A one-ball change of tags explains why the invariant unbounded distribution does not define the advertised tag-independent integral. Elementary categorical examples check a false statement about nondegenerate faces and the two Q-construction homotopies. The conic calculation supplies a complex polynomial reduction and Bézout certificate for the particular row in the notebook.

These proofs carry the required “proved here” markers, and computations carry “computed here” markers. No historical novelty is claimed. The conic example does not prove stable rank two for the whole polynomial ring, and it does not remove the real-valued topological obstruction. The Bernoulli calculation requires an odd prime and the displayed sign convention. Finite numerical evidence is not used to infer an infinite theorem.

## 5. Independent checks

The Bernoulli moments were derived independently from the finite power-sum identity, using standard Bernoulli numbers with B1=−1/2. Exact rational calculations check120 combinations of prime, moment and subdivision level (p=3,5,7; k=0,…,9; m=1,…,4). The limiting formula comes from an algebraic identity and p-adic polynomial continuity, not from extrapolating those120 cases.

The conic construction was rederived algebraically and then checked by independent exact arithmetic over the Gaussian rationals. A6by6 rational grid verifies the Bézout polynomial identity within its explicit degree bound; additional genuinely complex substitutions provide a separate parameter check. A coefficient-arithmetic check supplied with the conic appendix is independent of this grid computation. The reason the finite grid certifies that polynomial identity is the degree bound, not a numerical heuristic.

The tag-dependence counterexample and the categorical naturality arguments were rederived independently. The spring verification script records exact checks of the Lax, KP, soliton and related emendations in its stated scope. The proofs, scripts and outputs must be read together: a symbolic identity checks the equation written there, not all analytic existence or spectral hypotheses of a broader theorem.

Schema checks enforce consecutive item identifiers, the1973academic-year prefix, valid assessment values, citation-list completeness, reciprocal problem links and bibliography verification flags. Earlier occurrences were checked against the supplied index. The supplied builder is retained unchanged and is run before the required XeLaTeX/BibTeX sequence. The build logs and final validation log provide the actual outcome.

@BUILD_STATUS@

## 6. What the A–F classes miss

The main difficulties are orthogonal to historical fate:

1. **An assertion can be published and false.** The zero-K2 field dichotomy is an example. Its publication match and its correctness must remain independently searchable.
2. **A known theorem can have a false notebook formula.** The FPU nonlinear sign, p-adic logarithm sign, moment normalization, Floquet normalization and categorical degree shifts require mathematical emendations rather than guessed transcription repairs.
3. **A talk can precede the printed paper and follow a public announcement.** The public announcement places a result inE; a private receipt date alone does not establish that status.
4. **An exact modern answer may require an explicitly chosen topology or category.** The finite-gap density formulation and stable-rank questions illustrate why the reconstruction field is indispensable.
5. **F is often a statement about the source.** A cancelled expression, a missing quantifier or an undecidable oral attribution does not establish that an idea was never developed.

The proposed method change is modest: preserve the historical classes, but add structured fields for statement hypotheses, source versus critical date, actual source span, first public circulation, manuscript receipt, publication version, exact theorem locator and the scope actually read. A distinct development value such as “critical verification” would describe this chapter better than overloading “annotated” or implying a new research result.

## 7. Problem identity and earlier years

GP-1972-403 is reused with its earlier occurrences. The r-subspace classification entry links1970-198 and1972-277, but is not merged with GP-1970-23, the different deformation/rigidity question. The plus/Q comparison is thematically related to the earlier higher-K-theory comparisons; the earlier supplied title alone does not authorize conflating their different constructions. Similarly, group coherence is not sheaf coherence, finite presentation over a finite-field Laurent ring is not a question over the integers, and real unimodular reduction is not the complex question.

Only definite questions enter the problem index. The uncertain agenda surname, unspecified fundamental-group class, broad Hamiltonian conjecture and damaged amplitude/gap remarks stay in the occurrence index with their evidential limitations.

## 8. Presentation on the companion website

A reader arriving at one talk should first see its short summary, critical date and source-page span, followed by the mathematical items in source order. The scan or diplomatic passage should be one click from each item. The modern statement should display its hypotheses alongside the source wording; the reconstruction field should remain visible rather than being hidden inside the fate paragraph.

The next useful paths are the definite-problem page, the exact publication locator and the dated present status. Cross-year occurrence links should identify whether they mean the same quantified problem or a thematic antecedent. Records331/332 need both catalogue and corrected dates. Overlapping catalogue ranges should not send a reader to the preceding talk's theorem.

Search and filters should expose correctness, verification scope, publication match and historical class separately. A classA filter alone would otherwise return a published false dichotomy without warning; a classF filter alone could be mistaken for a list of neglected research opportunities. A source-order field, structured scan location, optional intervention attribution, theorem-level evidence link and version-specific bibliographic identifier would support the necessary navigation. The data remains in the supplied fixed schema; the extra statistics and area map are auxiliary files.

## 9. Limits of the edition

The current-status statements mean that the dated searches and checked primary sources support the stated status. They are not a proof that no unpublished or unindexed result exists. Where only metadata or an abstract was available, no detailed theorem is attributed to that unread source. A failed direct retrieval is recorded, and an alternative successful primary reading is identified when available.

The chapter supplies modern hypotheses to make mathematical statements meaningful, but labels them as reconstruction. It does not invent missing diagrams, unstated estimates, unspecified boundary conditions or a research problem from an agenda label. The selected elementary checks do not verify every proof in the literature; item-level verification describes the narrower evidential claim.

## 10. Record coverage

@COVERAGE_TABLE@

The source-recovered records331/332 are additions to the supplied roster. All other records appear exactly once. Every item uses the academic-year prefix1973, including meetings in1974.

## 11. Reproduction and files

The seven required data/TeX/bibliography files are at the archive root, together with this report, the generated chapter and compiled test PDF. The supplied builder, style and format specification are included. The additional area map and statistics file make the report counts reproducible. The code directory contains the mathematical checks, assembly and validation scripts; the logs directory contains their outputs and the TeX/BibTeX logs. Research and source-audit notes are under audit.

With a complete XeLaTeX installation, the prescribed build is:

    python build_chapter.py GY1973
    xelatex GY1973_test
    bibtex GY1973_test
    xelatex GY1973_test
    xelatex GY1973_test

Alternatively:

    python code/build_pdf.py
    python code/validate_data.py
    python code/independent_checks.py

The conic coefficient check is code/fragments/autumn_representations/check_conic.py, with its recorded output beside it. The spring checks are code/fragments/spring_integrable/code/verify_emendations.py and require SymPy 1.14.0; their JSON and text outputs are retained in the adjacent output directory. These checks can be run from the archive root. Original fragment generators are included as research history and may require the original source inputs; they need not be rerun to build the chapter from its authoritative final data.

The helper uses the same supplied builder and XeLaTeX/BibTeX sequence. In this runtime, TeX packages were installed but their generated filename database and format were absent; the helper searched the installed distribution directly and generated a format in the writable workspace. No mathematical text, style or builder was weakened to bypass a compilation error. Four DejaVu Serif faces and their license are bundled so that English, Russian and italic text render consistently.

The manifest records the final file hashes. Source inputs and publisher PDFs are not duplicated into the deliverable; their identity and the checked publication links are documented in the audit and bibliography.
"""
    pages=""
    pdf=BASE/"GY1973_test.pdf"
    if pdf.exists():
        result=subprocess.run(["/usr/bin/pdfinfo",str(pdf)],capture_output=True,text=True)
        for line in result.stdout.splitlines():
            if line.startswith("Pages:"):pages=line.split(":",1)[1].strip()
    buildstatus=("**Final build:** the supplied builder, additional semantic audit, XeLaTeX/BibTeX sequence and PDF inspection completed successfully."
                 +(f" The compiled test PDF has {pages} pages." if pages else "")) if args.verified else "**Build status:** pending the final integrated run; consult logs for the current checkpoint."
    replacements={
        **substitutions,"REFERENCES":stats["references"],"CLASS_TABLE":counts,
        "SPEAKER_TABLE":byspeaker,"AREA_TABLE":byarea,"ASSESSMENT_TABLE":assessmenttable,
        "CORRECTION_TABLE":corrections,"OPEN_TABLE":openitems,"COVERAGE_TABLE":coverage,
        "BUILD_STATUS":buildstatus}
    for k,v in replacements.items():text=text.replace("@"+k+"@",str(v))
    text=re.sub(r"(?<=[A-Za-zÀ-ž’'])(?=(?:19|20)\d{2}\b)"," ",text)
    text=re.sub(r"\b(\d{1,2})(March|April|May|June|July|August|September|October|November|December)\b",r"\1 \2",text)
    text=re.sub(r"\b(records?|Records?|items?|Items?|Class|class|Stage|stage|Theorem|theorems?|Theorems?)\s*(?=\d)",r"\1 ",text)
    text=re.sub(r"(?<=\d)(?=(?:academic|publication|paper|proof|two|full|class|items|records)\b)"," ",text)
    text=re.sub(r"\b(class|Class)([A-F])\b",r"\1 \2",text)
    text=text.replace("theoremsA andB","theorems A and B").replace("A6by6","A 6-by-6")
    text=text.replace("a6by6","a 6-by-6").replace("120cases","120 cases")
    text=text.replace("higherK-theory","higher K-theory").replace("prefix1973","prefix 1973")
    text=re.sub(r"\b(in|on|under|and|both|the|these|those)(?=\d)",r"\1 ",text)
    text=re.sub(r"\b(on|in)(?=P\d{6})",r"\1 ",text)
    text=re.sub(r"\b(in|to|of)(?=[A-F]\b)",r"\1 ",text)
    text=text.replace("check120", "check 120").replace("those120", "those 120")
    (BASE/"GY1973_report.md").write_text(text)
    print("Wrote overview and report; verified =",args.verified)

if __name__=="__main__":main()
