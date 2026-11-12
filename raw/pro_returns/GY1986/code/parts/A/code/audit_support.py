#!/usr/bin/env python3
"""Validate slice A and generate source/query inventories and research notes."""
from pathlib import Path
from collections import Counter
import csv, json, re, hashlib

OUT=Path(__file__).resolve().parents[1]
ROOT=OUT.parents[1]
talks=json.loads((OUT/'talks.json').read_text())
items=json.loads((OUT/'items.json').read_text())
problems=json.loads((OUT/'problems.json').read_text())
corrections=list(csv.DictReader((OUT/'corrections.csv').open()))
bibtext=(OUT/'references.bib').read_text()

def blocks(text):
    result={}
    for m in re.finditer(r'@\w+\s*\{\s*([^,]+),',text):
        start=m.start(); depth=1; pos=m.end()
        while depth and pos<len(text):
            if text[pos]=='{' and text[pos-1]!='\\': depth+=1
            if text[pos]=='}' and text[pos-1]!='\\': depth-=1
            pos+=1
        assert depth==0
        key=m.group(1).strip()
        assert key not in result, key
        result[key]=text[start:pos]
    return result

def field(block,name):
    m=re.search(r'\b'+re.escape(name)+r'\s*=\s*\{',block)
    if not m: return ''
    start=pos=m.end(); depth=1
    while depth and pos<len(block):
        if block[pos]=='{' and block[pos-1]!='\\': depth+=1
        if block[pos]=='}' and block[pos-1]!='\\': depth-=1
        pos+=1
    return block[start:pos-1]

bib=blocks(bibtext)
oldkeys=set(re.findall(r'@\w+\s*\{\s*([^,]+),',(ROOT/'work/references_cumulative.bib').read_text()))
assert [t['record'] for t in talks]==list(range(667,682))
assert len(items)==101 and len(problems)==5
assert len({x['id'] for x in items})==len(items)
assert len({x['id'] for x in problems})==len(problems)
required={'id','record','pages','kind','title','notes','statement','reconstruction','class','fate','present_status','literal_correctness','publication_match','verification','development','problem','worth','refs','confidence'}
enums={
 'kind':{'definition','construction','theorem','claim','conjecture','question','problem','method','remark'},
 'class':set('ABCDEF'),
 'literal_correctness':{'correct','correct with missing hypotheses','false as written','not determinable'},
 'publication_match':{'exact','partial','thematic only','none found'},
 'verification':{'read the result','publisher metadata checked','indirect','unresolved lead'},
 'development':{'none','annotated','developed in this chapter'},
 'confidence':{'high','medium','low'}}
allrefs=set()
allids={x['id'] for x in items}
problemids={x['id'] for x in problems}
for rec in range(667,682):
    ids=[x['id'] for x in items if x['record']==rec]
    assert ids==[f'1986-{rec}.{i+1}' for i in range(len(ids))],rec
for x in items:
    assert required<=x.keys(),x['id']
    for f,vs in enums.items(): assert x[f] in vs,(x['id'],f,x[f])
    if x['class'] in {'C','D'}: assert x['worth'],x['id']
    assert not x['problem'] or x['problem'] in problemids,x['id']
    for key in x['refs']: assert key in bib,(x['id'],key)
    allrefs.update(x['refs'])
    assert '2026' in x['present_status'],x['id']
    for v in x.values():
        if isinstance(v,str):
            assert not re.search(r'[\x00-\x08\x0b\x0c\x0e-\x1f]',v),x['id']
            for cited in re.findall(r'\\cite\w*(?:\[[^]]*\])*\{([^}]+)\}',v):
                for key in cited.split(','):
                    assert key.strip() in x['refs'],(x['id'],key)
for x in problems:
    assert x['status_date']=='2026-11'
    assert x['occurrences']
    for occurrence in x['occurrences']:
        if occurrence.startswith('1986-'): assert occurrence in allids,(x['id'],occurrence)
    assert set(x['refs'])<=set(bib),x['id']
assert allrefs==set(bib)
for key,block in bib.items():
    assert field(block,'note') in {'verified','unverified'},key
    assert field(block,'url') or field(block,'doi'),key
for x in corrections:
    assert x['applies_to'] in {'ru','en','both'}
    assert x['type'] in {'transcription','translation','ambiguity','faithful_error','provenance'}
    assert all(x.values())

# Keep the substantive search strings and all opened targets reproducible.
# Opened targets include rejected/error results: their status is visible in the
# corresponding raw response and they are not automatically evidence for a claim.
queries=[]; opened=[]; retrievals=[]
for path in sorted((OUT/'evidence').glob('*.json')):
    try: data=json.loads(path.read_text())
    except json.JSONDecodeError: continue
    if not isinstance(data,dict) or 'q' not in data or 'r' not in data: continue
    q=data['q']; retrievals.append(path.name)
    for engine in ['system1_search_query','system2_search_query']:
        for entry in q.get(engine,[]) or []:
            queries.append({'log':path.name,'engine':engine,'query':entry.get('q','')})
    for entry in q.get('open',[]) or []:
        opened.append({'log':path.name,'operation':'open','target':entry.get('ref_id','')})
    for entry in q.get('click',[]) or []:
        opened.append({'log':path.name,'operation':'click','target':entry.get('ref_id','')+':'+str(entry.get('id'))})
    for entry in q.get('find',[]) or []:
        opened.append({'log':path.name,'operation':'find','target':entry.get('ref_id','')+' :: '+entry.get('pattern','')})
with (OUT/'evidence/query_inventory.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['log','engine','query']);w.writeheader();w.writerows(queries)
with (OUT/'evidence/open_inventory.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['log','operation','target']);w.writeheader();w.writerows(opened)

classes=Counter(x['class'] for x in items)
speakers=Counter(x.get('speaker') or next(t['speaker'] for t in talks if t['record']==x['record']) for x in items)
areas={667:'Curves and determinant lines',668:'String measures and determinants',669:'Mixed Hodge structures',670:'String measures and supermoduli',671:'Lattices and string compactification',672:'Subspace arrangements',673:'Singularities and Hodge theory',674:'RTT algebras and PBW',675:'String quantization and fields',676:'Yangians and fusion',677:'Infinite classical Lie algebras',678:'Quantum determinants',679:'Heading',680:'Matroids and quadratic algebras',681:'Symmetric varieties and Hecke algebras'}
validation={
 'date':'2026-11-12','talks':len(talks),'items':len(items),'problems':len(problems),
 'references':len(bib),'reused_reference_keys':sorted(set(bib)&oldkeys),
 'corrections':len(corrections),'classes':dict(sorted(classes.items())),
 'verification':dict(Counter(x['verification'] for x in items)),
 'literal_correctness':dict(Counter(x['literal_correctness'] for x in items)),
 'publication_match':dict(Counter(x['publication_match'] for x in items)),
 'speakers_including_interventions':dict(speakers),
 'area_counts':{areas[r]:sum(x['record']==r for x in items) for r in range(667,682)},
 'correction_types':dict(Counter(x['type'] for x in corrections)),
 'retrieval_logs':len(retrievals),'substantive_queries':len(queries),'open_click_find_operations':len(opened),
 'checks':'All schema, enumeration, citation, date, bibliography-note, cross-reference, and control-character assertions passed.',
 'files_sha256':{n:hashlib.sha256((OUT/n).read_bytes()).hexdigest() for n in ['talks.json','items.json','problems.json','corrections.csv','references.bib']}}
(OUT/'evidence/validation.json').write_text(json.dumps(validation,ensure_ascii=False,indent=2)+'\n')
(OUT/'code/audit_support.out').write_text(json.dumps(validation,ensure_ascii=False,indent=2)+'\n')

source_lines=['# Source verification inventory — slice A','',
 'Date checked: 12 November 2026. `verified` means the linked source or its official/authored metadata was opened. It does **not** mean that every proof in it was read. The item-level verification field and the scope notes below carry that distinction. Cumulative keys are retained unchanged; where an inherited entry lacks a detailed annote, the per-record research notes explain the access level in this run.','']
for key in sorted(bib):
    block=bib[key]
    url=field(block,'url') or 'https://doi.org/'+field(block,'doi')
    source_lines += ['## '+key,'',field(block,'author')+' ('+field(block,'year')+'). '+field(block,'title')+'.','',
        '- Source: '+url,
        '- Bibliographic access flag: '+field(block,'note')+'.',
        '- Cumulative key reused: '+('yes' if key in oldkeys else 'no')+'.',
        '- Verification scope: '+(field(block,'annote') or 'Inherited cumulative reference; see the record-level discussion in research_notes.md.'),'']
(OUT/'evidence/source_inventory.md').write_text('\n'.join(source_lines)+'\n')

notes=r'''# Research notes for records 667–681

**Status date: 12 November 2026.** This is the complete slice-A support packet for the critical companion. It contains record-level metadata, every identified distinct mathematical occurrence on the assigned manuscript portions, five precise problem-index entries, a correction/provenance ledger, and a bibliography. It makes no claim to a new research theorem.

## Scope and reproducibility

Read first: the attached task prompt and `work/kit/CHAPTER_FORMAT.md`. The Russian diplomatic text was treated as the reading authority; the English was checked against it whenever a formula or interpretation mattered. The original scans were inspected for decisive formulas and ambiguities. Per-page extracts of both languages are preserved under `evidence/Pnnnnnn_{en,ru}.tex`; these are reading aids, not altered source editions. The original uploads and the kit were not modified.

`code/author_data.py` is the full authored dataset and checkpoints after each record. Because that script initially writes an empty problem array, always follow it with `code/finish_support.py`. A complete reproduction is:

```sh
python parts/A/code/author_data.py
python parts/A/code/finish_support.py
python parts/A/code/write_corrections.py
python parts/A/code/check_editorial.py
python parts/A/code/audit_support.py
```

The final two programs save exact computation and validation results under `evidence/`. `code/prepare_evidence.py` reproduces the page extracts. The source queries and full retrieved tool responses are saved as JSON with `q` and `r` fields. `evidence/query_inventory.csv` extracts substantive search strings; `evidence/open_inventory.csv` lists open, click, and find operations. The latter includes unsuccessful attempts and must not be read as a list of accepted evidence. The bibliography and `evidence/source_inventory.md` record accepted sources and access levels.

The integrating researcher handles the complete chapter build, BibTeX/XeLaTeX checks, overview, report, and final package. Slice A was checked for schema, consecutive item numbers, matching citations and bibliography keys, linked problem occurrences, allowed classification values, dated status, and accidental control characters. It does not duplicate the complete chapter build.

## Provenance and the disputed dates

The catalogue dates are preserved exactly. Records 667–678 are catalogued in February–May 1987, but the manuscript headings for the corresponding sessions generally read 1986. They are not interchangeable priority dates. The 1986 month/day combinations are Mondays, matching the seminar's stated meeting day, whereas the 1987 combinations are Tuesdays. Most decisively, the original Olshanskii Doklady announcement says it was presented by Gelfand on **5 May 1986**, then received on **22 May 1986**, before its 1987 Russian publication. This independently agrees with P001290. Kontsevich's P001258 heading is a separate problem: the scan visibly reads **24/II-85**, while the next Morozov heading reads **24.2.86**. The companion retains this three-way conflict rather than deriving publication priority from a silently repaired year.

Overlapping catalogue ranges are not speaker attributions. Actual item pages are delimited by manuscript headings. In particular, P001257 is a Beilinson continuation at the boundary of the previous academic-year material. It is bound to record 667 for containment only, with the explicit item speaker `A. A. Beilinson (boundary fragment)`. It links to **1985-666.21** (constancy) and **1985-666.14** (curvature does not by itself fix metric normalization). It is not presented as Kontsevich's contribution. Record 679 is an academic-year heading and properly has no mathematical items. On P001298 the Cherednik problem ends before Ovsienko and Kazakov begin; those lower contributions belong to the next assigned slice. The catalogue initial `V. L. Ginzburg` is retained rather than silently rewritten from conventional biographical knowledge.

## Record-level findings and precise source matches

### 667 — Kontsevich, with the Beilinson boundary fragment

The Laurent-vector-field action, curve-dependent stabilizer, and Virasoro lift to determinant lines match Kontsevich's 1987 paper, sections 1–2. Its receipt date is 3 December 1986. The quotient `g/k` in the manuscript omits the curve-dependent stabilizer and conflicts with the immediately following Kodaira–Spencer formula; this is a mathematical emendation of the faithful text. The modern stack/formal interpretation is explicitly editorial. A numerical central character was not invented from the abbreviated determinant-line notation. The boundary Beilinson paragraph is indexed separately and linked backward, with no fresh problem ID.

### 668 — Morozov: bosonic measures and determinants

Belavin–Knizhnik's full primary paper supplies the determinant ratios, zero-mode Gram factors, conformal-anomaly cancellation, and deformation formulas. Quillen supplies the determinant-line interpretation; its publisher metadata was checked in this run, while the opened Belavin–Knizhnik formulas provide direct mathematical evidence. The curvature identity on P001260 cannot literally be a derivative of an unlogged ratio equal to a coordinate-independent scalar: the logarithm and curvature-form factor are restored only in the reconstruction. Gelfand's multiplicativity question exactly repeats **GP-1982-40**, earlier occurrence **1982-587.7**. Kontsevich–Vishik's 1994 preprint supplies the anomaly framework, with orders, spectral cuts, invertibility, and kernel treatment spelled out. Unrestricted multiplicativity is not asserted.

### 669 — Beilinson: real splitting and height data

The mixed-Hodge axioms are compared with Deligne. For the splitting formulation, the directly read primary source is Cattani–Kaplan (1989), Theorem 1.15, which cites Cattani–Kaplan–Schmid (1986); the 1986 publisher metadata was checked. The anti-real lowering operator in the notebook is kept distinct from a real delta convention by the appropriate multiplication by `i`. Rationality of the weight filtration is an additional condition and is not inferred from complex-conjugation symmetry. Smoothness alone does not imply purity; the proper/Kahler hypothesis is restored. The relative curve and Green-pairing interpretation is identifiable, but the exact coefficient depends on Tate-generator and Green-function normalizations missing from the notes. Beilinson's 1987 height chapter could not be opened; its identity was corroborated by later primary bibliographies. That entry remains `unverified`, and the item is `indirect` and `partial` rather than pretending that its exact normalization was read.

### 670 — Morozov: explicit measures and the odd-moduli question

The scalar Green formula requires a prime form and a full Abelian quadratic correction. Morozov's 1987 authored abstract confirms explicit low-loop formulas, and Beilinson–Manin supplies the Mumford-form interpretation; the original explicit-formula paper was not read in full. The general odd-variable question separates two issues. Global holomorphic projection is obstructed by Donagi–Witten, first circulated in April 2013 and published in 2015, for genus at least five. The September 2026 Correa–Donagi–Noja preprint states the obstruction on both parity components in every genus at least three; its theorem statement and scope were read, not independently proved here. This recent preprint status is visible in the item.

There is one precise **class C** remainder: the 2025 Dunin-Barkowski–Fedorov–Sleptsov genus-three RNS calculation proves a three-term span but retains conjectural coefficient values. Sections 1.7 and 4.9 were read; section 4.9.2 does not supply a rigorous numerical error bound. The bounded coefficient problem is explicitly a later specialization of the notebook's broader request. No claim is made that arbitrary higher-genus measures have been solved, or that nonprojectedness forbids local odd integration. The coefficient calculation is not developed in this slice because a justified derivation and boundary normalization require more than a short algebraic check.

### 671 — Morozov: compactification and lattice sums

The original Gross–Harvey–Martinec–Rohm paper was opened in full. It distinguishes open-string Chan–Paton factors from the heterotic chiral lattice construction, and supports the rank-sixteen even-unimodular setting. The notebook sometimes merges those different constructions. Grushevsky–Salvati Manni provides the precise lower-genus theta identities and the genus-four Jacobian-locus condition, while its genus-five result prevents extrapolation. Gelfand's modularity question is indexed as **GP-1986-02**, with the group and scalar/vector-valued representation specified. It is not converted into an open classification based on the bare word 'modular'. The dynamical compactification sentence has no specified model or mathematical quantifiers and is class F.

The winding formula's two plus signs were confirmed in the scan. The corrected expression was checked exactly from the two shifts and independently in real lattice coordinates; the computation is marked `oursComputed`. The sign in the original action (12) is problematic, but the subsequent Gaussian winding factor (21) already has the correct negative sign. The root-operator rule needs the opposite-root Cartan and central term. Frenkel–Kac's publisher metadata was checked, but the original full construction was inaccessible; this item therefore states its indirect access level.

### 672 — Fuchs: arrangements and the complexification question

The count of real chambers is checked in Greene–Zaslavsky (1983), Theorem A, with Zaslavsky's 1975 Memoir identified through the author's bibliography. The Goresky–MacPherson 1983 announcement was read, but the full 1988 book was inaccessible. Its additive arrangement formula and geometric-lattice specialization are consequently marked indirect where appropriate, with later primary arrangement literature used for the exact conventions. Reduced homology in degree -1 and the ordinary base H0 are kept distinct.

The key later comparison is Ziegler (manuscript December 1991; arXiv February 1992; publication 1993), whose full primary paper separates complex arrangements from real 2-arrangements, including their cohomology rings. An individual real codimension-two condition does not imply the even-codimension intersection condition. Batzies (2007), Theorems 1 and 3, supplies a classification by simultaneous conjugation for transverse planes in R4 and an explicit four-plane complexifiable locus. The integrating researcher opened and checked that primary PDF. This is a **partial publication match**, class B, for the broader notebook question **GP-1986-03**. The bounded linear-algebra annotation is known mathematics. It does not settle arbitrary topological equivalence, and no claim that all higher-dimensional classification is open is inferred.

The parent development was independently read for the following checks: after fixing two coordinate planes and a diagonal third plane, preservation forces a block-diagonal common complex structure diag(B,B); every additional graph requires BA=AB and B squared equal to minus the identity. In real dimension two, a nonscalar commuting A has negative discriminant precisely in the complexifiable case. For several A's, one nonscalar negative-discriminant member together with pairwise commutation with that member suffices; if all are scalar, any B works. The family diag(2,2+t), 0<=t<=1, stays transverse to the coordinate/diagonal planes but loses linear complexifiability for t>0. These are annotations to the cited classification, not a novelty claim. Root owns the written proof and independent computations.

The poset-realization sentence and the Pappus-labelled diagram do not specify sufficient data for unique modern problems; they are class F, without invented GP identifiers. Pappus itself holds over both real and complex fields. The Orlik–Solomon ring and no-broken-circuit basis answer a precise generator/basis problem for complex hyperplanes, with that scope retained.

### 673 — Varchenko: singularities and mixed Hodge theory

Bernstein's continuation theorem was read with the choice of sign region or branch made explicit. Milnor's local fibre requires the ball restriction; the plane-curve relation is `mu=2g+b-1`, not the manuscript's reversed signs. Varchenko's 1980 Doklady announcement and full 1981 Russian/1982 English article were opened, with receipt dates distinguished from publication. The original asymptotic-Hodge comparison establishes its stated special cases; later general formulations are supported separately by Steenbrink, not silently attributed to the first proof. The monodromy-filtration centers differ between eigenvalue one and the other eigenvalues. A Jordan block of size s allows logarithmic degree at most s-1.

Steenbrink's original 1985 paper was finally opened in full, and its 1989 exposition was also read. General half-open length-one intervals must be distinguished from the earlier Varchenko open-interval result in the specified quasihomogeneous deformation setting. The question about several functions has meaningful later implementations through Saito's mixed Hodge modules, whose Theorem 1.3 was read, but no unique unspecified multivariable limiting object is asserted. The pair-of-quadrics question lacks dimension, fibre/projective interpretation, and nondegeneracy conditions; it remains class F, not a newly discovered open problem.

### 674 and 676 — Cherednik: finite-level RTT algebras, center, and fusion

Molev–Nazarov–Olshanski, first circulated in September 1994 and published in 1996, supplies exact RTT, evaluation, coproduct, quantum-determinant, and central-character conventions. Futorny–Ovsienko, first circulated in March 2003 and published in 2005, section 5.2 and Proposition 3, supplies the finite-level PBW and polynomial-center statements and identifies the older Cherednik work. The normalized truncated algebra is distinguished from its homogeneous presentation, and coefficient-degree versus current-degree filtrations are not interchanged. The level-one quotient is U(gl_N); the full Yangian is not isomorphic to that quotient. A fixed finite-level quotient does not inherit the full Yangian Hopf structure merely by notation.

The original Cherednik 1987 Duke article and 1989 proceedings chapter were blocked. Their bibliographic identities and roles are corroborated by the opened primary later works, but their entries remain `unverified`. Fusion and Gelfand–Tsetlin normalization matches are explicitly indirect or partial. The manuscript minus sign in only one RTT factor, the use of level n in place of matrix size N in the top antisymmetrizer/pole range, and the symmetric-group order are ledgered as faithful errors. No guessed chapter DOI remains in the bibliography. The 1989 chapter's URL points to the primary source carrying its reference, and that limitation is recorded.

Gelfand's broad PBW request has a precise later theorem under the Koszul and compatibility hypotheses in Braverman–Gaitsgory, first circulated in November 1994 and published in 1996. Its Theorem 0.5 was read. A bare Yang–Baxter-if-and-only-if-PBW slogan and the Jackiw three-cocycle aside do not specify a theorem and remain class F. They are not assigned class D because searches fail to identify an exact conjecture.

### 675 — Kogan: oscillator and string-field constructions

The primary proof of Furuuchi–Ohta (2006) supplies an explicit, readable oscillator/BRST/no-ghost convention. Its nonzero light-cone momentum hypothesis is retained. The physical matter subspace, null quotient, and BRST cohomology are distinguished; positivity is not assigned to the unreduced covariant Fock space. The Virasoro commutator has mode n+m, and the level-two component constraint cannot involve the separate level-one vector. The free vector gauge variation does not by itself supply the interacting nonabelian term.

Witten's 1986 string-field article was identified through official institutional metadata and authored abstract, with its original full text blocked. The corresponding item says so. Its publication on 5 May 1986 is after the manuscript April session and before the catalogue's 1987 date; the class therefore must not be used as evidence of manuscript priority. The earlier oscillator discussion links to 1985-662.1–9, without recycling a problem ID for expository material.

### 677 and 678 — Olshanskii and Cherednik

Olshanskii's original Russian Doklady text, Theorems 1–3 and 10, was opened and read. It is the strong-limit/tail-invariant completion acting on the stated tensor representations, with an ordinary Yangian factor in the theorem quoted in this notebook. It must not be replaced by a different later orthogonal/symplectic centralizer construction using twisted Yangians. The exact 1986 presentation/receipt dates provide unusually strong independent provenance evidence. Low-m remarks are kept as tests of that construction.

Cherednik's highest-weight determinant formula is compared with the quantum determinant and Harish–Chandra/Capelli formula in Molev–Nazarov–Olshanski, section 2.11. Spectral shifts, denominators, matrix transpose, and highest-weight-line normalization are stated. The two-dimensional antisymmetrizer coefficient in the scan is 1/4. The normalized projector gives 1/2; exact tensor-matrix multiplication and a separate trace extraction agree, including the identity-matrix check. This editorial computation is marked `oursComputed`.

### 679 and 680 — Heading; Gelfand on matroids and quadratic algebras

The heading has one record and zero mathematical items. Gelfand's mathematical pages start at P001293. The original Gelfand–Serganova paper, received 30 July 1986 and published in 1987, was read in the cached primary PDF, sections 1, 2, and 8. A later reopening of its author-hosted URL redirected to a homepage; that response is excluded as mathematical evidence. The support of Pluecker coordinates defines a matroid stratum, which generally contains many torus orbits. The Coxeter-matroid criterion uses a least element for each translated order, not merely a minimal element.

The closure-intersection identity is false; the manuscript's span example makes the intended monotonicity clear. Closed singletons require simplicity. The Fano triples establish characteristic-dependent nonrepresentability, not nonrepresentability over all fields. Coxeter's original 1934 paper was opened and its order table checked: finite rank-two groups have order 2m, H3 has order 120, and H4 has order 14400. The binary icosahedral group and H3 must not be identified merely because their orders agree.

Priddy's original 1970 paper, section 2.2 and Theorem 2.5, and Beilinson–Ginzburg–Soergel's full 1996 paper, section 2, distinguish old quadratic duality from later representation-theoretic Koszul theorems. The notebook supports the definitions and the polynomial/exterior and homogenized-Clifford examples, not an unrecorded specific duality theorem. The parameter h is central of degree two and is not set to one before specializing to an ordinary Clifford algebra.

### 681 — Ginzburg: symmetric compactifications and a Cherednik Hecke problem

De Concini–Procesi's original metadata was checked through an author institution. The exact geometry was read in Chirivi–Maffei (2004), Propositions 1.1–1.4, which explicitly states the relevant original theorems. The algebraic symmetric subgroup, connected/fixed/normalizer distinctions, normal-crossing union versus intersection, and injective Picard restriction are all essential. The manuscript's asserted Picard isomorphism is too strong.

Mathas's full primary preprint, first submitted in August 2001 and published in 2004, section 2, was opened. The basis theorem is **(2.2)**, not (2.1), and it cites the original Ariki–Koike locator (3.10). The universal polynomial quotient by a monic degree-r polynomial in the invertible affine generator, with nonzero constant coefficient, is the cyclotomic Hecke algebra of dimension r^n n!. Repeated roots and nonsemisimple parameters do not invalidate the basis theorem. The r=2 case is type B. This is the bounded precise later answer to **GP-1986-04**. It is not an assertion that every polynomial quotient maps back into the original n!-dimensional type-A finite Hecke algebra. The original Ariki–Koike publisher text was blocked and remains `unverified`; the exact basis result was read in Mathas.

The affine evaluation must be matched to the exchange relation actually written in the notes. It forces T_i X_i T_i=q X_{i+1}, hence X_{n-1}=q T_{n-1}^{-2} under X_n=1. The scan has the positive square. Exact polynomial reduction and independent two-dimensional regular-representation checks at q=2,-2,3/2 confirm the inverse-square correction; this is marked `oursComputed` and is not offered as a new theorem.

## Unsuccessful leads, access limitations, and classification discipline

The raw logs deliberately retain failed retrievals and rejected matches. Two guessed MathNet identifiers returned unrelated papers (Myasnikov at `dan43963`, Petrenko at `dan44147`); neither is cited. The Bath redirect is not substituted for the cached Gelfand–Serganova paper. Blocked publisher/AMS requests do not become a claim to have read a proof. An inherited `verified` bibliography flag is not upgraded into `read the result` without mathematical support elsewhere. Important indirect accesses are named in the items and in the source inventory.

Seven F items represent insufficiently identified claims or questions, including physical motivation, unspecified compactification, a poset-realization request, the Pappus-labelled obstruction, a pair of quadrics, a Yang–Baxter/PBW converse, and the three-cocycle remark. None is labelled D. The one C item has an affirmative primary-source statement that coefficients remain conjectural; it does not rest on absence of search hits. The arrangement question is B with a partial match, and its bounded four-plane annotation is already in the literature. No new theorem, conjecture, or universal classification is manufactured from an abbreviated sentence.

## Corrections, checks, and display recommendations

The ledger distinguishes provenance, ambiguity, and faithful notebook error. No diplomatic text is silently rewritten. The three explicit editorial calculations were run symbolically and checked independently as described above; `evidence/editorial_checks.json` records their successful outputs. The broader arrangement and chamber-count annotations are owned by root and have separate independent checks there.

A website should put the actual manuscript passage, the precise reconstructed statement, and the fate next to each other. Dates need separate catalogue and manuscript fields, with a confidence/provenance explanation. Display actual item page intervals rather than using an overlapping catalogue range as a speaker boundary. A reader at the determinant question should reach GP-1982-40 and 1982-587.7; a reader at P001257 should reach the Beilinson boundary predecessor. A reader at the Hecke question should see immediately that the universal quotient interpretation is explicit and that generic semisimplicity is unnecessary. Source access level, publication-match scope, and recent-preprint status should be visible before an external reference is opened.

Suggested additional data fields for a later schema revision are `catalogue_date`, `manuscript_date`, `date_evidence`, `actual_talk_span`, and a per-reference access record distinguishing full result, authored abstract, official metadata, and indirect citation. The existing fields are sufficient for this deliverable because these distinctions are written into the summaries, fate, reconstruction, and bibliography annotations.
'''

count_lines=['','## Final slice counts','',
 f'- Catalogue records: {len(talks)}; mathematical occurrences: {len(items)}; problem entries: {len(problems)}.',
 f'- Bibliography entries: {len(bib)}, including {len(set(bib)&oldkeys)} cumulative keys reused.',
 f'- Correction/provenance entries: {len(corrections)}.',
 '- Classes: '+', '.join(f'{c}={classes.get(c,0)}' for c in 'ABCDEF')+'.',
 f'- Raw retrieval logs: {len(retrievals)}; substantive search queries: {len(queries)}; open/click/find operations: {len(opened)}.','',
 '| Record | Area | Items |','|---|---|---:|']
for r in range(667,682): count_lines.append(f'| {r} | {areas[r]} | {sum(x["record"]==r for x in items)} |')
count_lines += ['','### Speaker counts, with interventions attributed separately','','| Speaker | Items |','|---|---:|']
for speaker,n in speakers.most_common(): count_lines.append(f'| {speaker} | {n} |')
(OUT/'research_notes.md').write_text(notes+'\n'.join(count_lines)+'\n')
print(json.dumps(validation,ensure_ascii=False,indent=2))
