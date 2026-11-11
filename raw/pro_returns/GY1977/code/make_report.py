"""Generate the editorial report and two-page overview from canonical counts."""
from pathlib import Path
import json,sys

D=Path(sys.argv[1]);ROOT_PART=Path(sys.argv[2]) if len(sys.argv)>2 else None
S=json.loads((D/'code/output/chapter_counts.json').read_text())
I=json.loads((D/'GY1977_items.json').read_text())
T=json.loads((D/'GY1977_talks.json').read_text())
P=json.loads((D/'GY1977_problems.json').read_text())

def table(mapping,heading):
    return f'| {heading} | Items |\n|---|---:|\n'+''.join(f'| {k} | {v} |\n' for k,v in mapping.items())

def problem_for(occurrence):
    return next((p['id'] for p in P if occurrence in p['occurrences']),'see occurrence index')

overview=r'''\noindent\textbf{Scope and editorial date.}
This chapter covers all 28 requested catalogue records and all 94 supplied
source pages, with status assessed on 10 November 2026. It indexes @ITEMS@
mathematical occurrences, not @ITEMS@ independent discoveries. The packet is
not a perfectly delimited academic year. Its record envelopes overlap;
record 422 is a presence/heading rather than a second Kirzhnits lecture;
the omitted catalogue record 437 survives on pages 753--754 and is treated
as an explicitly attributed precursor to 438. Records 445, 451 and 457
contain @ADJACENT@ occurrences from 1978--79. Their requested identifiers
are retained, with the actual notebook dates explained. The date field
preserves the supplied catalogue date; it must be read with the provenance
notice, especially for Manin's 21 November 1977 and Fuchs's 3 April 1978
and 5 March 1979 lectures. P000705 retains an unresolved April/September
date conflict. One truncated attachment, P000722, was recovered
from MCCME and checked against its intact neighbors and the uploaded prefix.

\begin{center}
\begin{tabular}{@{}lrrrrrrr@{}}
\toprule
Class & A & B & C & D & E & F & Total\\
\midrule
Occurrences & @A@ & @B@ & @C@ & @D@ & @E@ & @F@ & @ITEMS@\\
\bottomrule
\end{tabular}
\end{center}
Here A means near-contemporary publication by the speaker or Gelfand;
B, later development by others; C, a precisely delimited partial result;
D, an undeveloped identifiable problem; E, prior established material;
and F, insufficiently identifiable content. These are historical fates,
not correctness ratings. A published thread can contain a false displayed
formula, and an F entry is not evidence of an orphan research idea.

\paragraph{The main lines.}
The strongest connected sequences concern local algebra models for
Harish--Chandra modules, self-dual gauge fields and their finite-dimensional
data, and spectral methods for nonlinear evolution equations. The local
representation-theory announcements match
\citet[Theorems~1--2]{bernsteingelfandgelfand1978local1} and
\citet[Theorem~1]{bernsteingelfandgelfand1978local2}; their small-domain
and regular-central-character qualifications are essential. Manin's talk
precedes the receipt of \citet{drinfeldmanin1978selfdual} by six days.
The instanton construction does not classify every finite-action
Yang--Mills critical point. The current comparison includes
\citet[Theorems~1.1--1.2]{dayapremawaldron2026parabolic}, with their stated
energy and moduli-space scopes kept separate.

Krichever's rational KP theorem, received in September 1977 and published
in 1978, is a close match to the November announcement
\citep[Theorem~3]{krichever1978rational}. Its pole dynamics require a
consistent choice of time and Hamiltonian normalization. Dickey's Poisson
bracket, Faddeev's classical and quantum scattering discussion, and the
Calogero--Degasperis lectures connect infinite-dimensional equations with
finite spectral or particle data. BGG's exterior-algebra account of bundles,
Aomoto's hypergeometric and Ising lectures, Buchstaber's substitution groups,
and Fuchs's vector-field cohomology supply additional substantial lines.
Margulis, Kirzhnits and the counterfeit-coin discussion contain much
established material whose hypotheses still need careful reconstruction.

\paragraph{Questions and development.}
The @PROBLEMS@ problem entries include questions answered before the talk,
near-contemporary solutions and surviving restricted questions; they are
not a count of currently open problems. Nonarithmetic lattices in complex
hyperbolic dimension at least four remain open in the located literature
\citep[Introduction]{falbelpasquinelli2023hybrid}; an October 2026 preprint
still reports examples only in dimensions two and three
\citep[Introduction]{yu2026mirror}. The broad Yang--Mills
critical-point classification and the exact scope of soliton-resolution
statements must not be replaced by narrower solved assertions. Buchstaber's
integer-substitution question omits coefficients and cochain topology.
\citet[Theorems~1.2 and~1.5]{babenkobogatyi2008substitutions} resolve its
real finite-jet version and compute a closed-commutator quotient. For an
explicit integral finite-jet interpretation, this chapter proves degree
one is \(\mathbb Z^2\), all degree-two torsion is \((\mathbb Z/2)^2\),
and all products of degree-one classes vanish. These are elementary
consequences and explicit calculations, with no priority claim and no
assertion about the full discrete cohomology ring.

\paragraph{Continuity and critical findings.}
The supplied earlier index connects the spectral-curve material to the
1975 rank-one correspondence and particle systems, gauge theory to the
1975 connection lectures, and the cohomology material to earlier
formal-vector-field discussions. Higher-rank commuting operators and
Hamiltonian-vector-field cohomology are related but different problems;
their old problem IDs are not silently reused. The earlier index is
incomplete as a year-by-year inventory, so a missing match establishes
only that no exact recurrence was identifiable there.

There are @CORRECTIONS@ critical entries, separating transcription,
translation, ambiguity, provenance and faithful mathematical error.
Among the independently checked cases, thirteen coins is correct for
identity-only detection; the KP coefficients change with convention;
the Calogero equilibrium linearization needs an identity matrix; and two
weight-25 spectral labels coincide, so gap partitions cannot count
distinct Laplace eigenvalues. Exact computations and their outputs are
provided. No D item is inferred from an unsuccessful search. The detailed
report explains the search limits, verification levels and requirements
for presenting these distinctions on the companion website.
\nocite{mccme2026gelfand}
'''
replacements={'@ITEMS@':S['items'],'@ADJACENT@':S['adjacent_1978_79_items'],
              '@PROBLEMS@':S['problems'],'@CORRECTIONS@':S['corrections']}
replacements.update({f'@{k}@':S['by_class'][k] for k in 'ABCDEF'})
for k,v in replacements.items():overview=overview.replace(k,str(v))
for k,v in S['bibliography_key_map'].items():overview=overview.replace('{'+k+'}','{'+v+'}')
(D/'GY1977_overview.tex').write_text(overview)
if ROOT_PART:
    ROOT_PART.mkdir(parents=True,exist_ok=True)
    (ROOT_PART/'overview.tex').write_text(overview)

classes={'A — near-contemporary publication by the speaker or Gelfand':S['by_class']['A'],
         'B — subsequent development by others':S['by_class']['B'],
         'C — partial, with a specified remaining scope':S['by_class']['C'],
         'D — identifiable but not developed':S['by_class']['D'],
         'E — established before the talk':S['by_class']['E'],
         'F — identification or exact statement unresolved':S['by_class']['F']}
record_rows='| Record | Catalogue date | Catalogue speaker / heading | Items |\n|---:|---|---|---:|\n'+''.join(
    f'| {t["record"]} | {t["date"] or "undated"} | {t["speaker"] or "heading / adjacent material"} | {S["by_record"][str(t["record"])]} |\n' for t in T)
problem_rows='| Problem | Title | Current occurrence(s) |\n|---|---|---|\n'+''.join(
    f'| {p["id"]} | {p["title"]} | {", ".join(o for o in p["occurrences"] if o.startswith("1977-"))} |\n' for p in P)
open_rows='| Occurrence | Class | Precisely limited issue |\n|---|---|---|\n'+''.join(
    f'| {i["id"]} | {i["class"]} | {i["title"]} |\n' for i in I if i['class'] in ['C','D'])
earlier_ids=sorted({o for p in P for o in p['occurrences'] if not o.startswith('1977-')})
old_gp=sorted(p['id'] for p in P if not p['id'].startswith('GP-1977-'))
build_path=D/'code/output/build_validation.json'
build=json.loads(build_path.read_text()) if build_path.exists() else {}
pdf_pages=build.get('pdf_pages','to be recorded after compilation')

report=f'''# GY1977: editorial and verification report

**Status date:** 10 November 2026.  
**Scope:** the 28 catalogue envelopes requested in `GY1977_talks.md`, the 94 supplied page images, and their Russian and English transcriptions.  
**Delivered chapter:** `{S['items']}` occurrence entries, `{S['problems']}` problem entries, `{S['references']}` bibliography entries, and `{S['corrections']}` critical corrections.  
**Compiled PDF:** {pdf_pages} pages. The exact build, data-validation and computational results are under `code/output/`.

## 1. What this chapter establishes

The packet contains several closely identifiable publications and a substantial amount of exposition. It does not support a claim that a large stock of forgotten, precise open problems has been recovered. The distinction matters: the number of occurrence entries measures what the notes say, including definitions, intermediate constructions, errors and interventions. It is neither a count of independent theorems nor a count of research problems.

The best publication matches are the local algebraic description of Harish–Chandra categories; the Drinfeld–Manin construction of instantons; the exterior-algebra description of bundles; Krichever's rational KP correspondence; the coefficient-linear first Gelfand–Dickey bracket and its later Volterra/coadjoint proof; the Calogero–Degasperis spectral constructions; and the positive-Witt Laplacian calculation. Several were circulating before their journal year. The chapter therefore distinguishes a seminar announcement, a manuscript receipt date, a preprint date and a publication date whenever the opened evidence supplies them. It does not infer an exact day of first private circulation from a receipt date.

The principal bounded development is attached to {problem_for('1977-441.7')}, the integral formal-substitution question. After stating an explicit finite-jet cochain convention, the chapter proves the first integral cohomology, all torsion in degree two and a cup-product identity. The full integral ring and the unrestricted discrete group theory remain outside that result. Additional proofs and computations are verification annotations on established material, including the coin construction and normalization checks; they are not presented as newly discovered open problems.

## 2. Counts and their interpretation

### Historical classes

{table(classes,'Historical fate')}

The class total is {S['items']}. Class A follows the historical mathematical thread, not every literal symbol in its transcription. A class-A entry can consequently have `literal_correctness = false as written`. Class E includes a theorem that was already available before the seminar even when a better exposition or a later survey is used to verify it. Class F means the precise intended object or claim cannot be identified securely. It is not a weaker spelling of D. No D classification was manufactured from failure to obtain a first search result.

### Speaker attribution

{table(S['by_speaker'],'Speaker attribution used for counting')}

Each item is counted once. The optional item-level speaker overrides the record heading when an intervention or an adjacent lecture is identifiable. Joint labels are retained as one attribution rather than fractionally distributed. Equivalent Calogero–Degasperis labels and the Palamodov date annotation are normalized for this table. The catalogue speaker remains in `talks.json`, so attribution can be audited without losing the original envelope. “With” and joint-author labels do not establish who uttered every sentence.

### Primary mathematical area

{table(S['by_area'],'Editorial primary area')}

Every occurrence receives one primary area, so these counts also sum to {S['items']}. The grouping is an editorial navigation aid; gauge theory, algebraic geometry, representation theory and integrability overlap substantially. `code/output/areas.json` records the item mapping, and `areas_original_labels.json` preserves the more granular working labels. The brief Vishik intervention is isolated as seminar method because its target algorithm and theorem are not recoverable.

### Record coverage

{record_rows}

Record 422 has no independent mathematical item because its name/presence line does not establish a second Kirzhnits lecture. It is nevertheless retained and explained. All other mathematical content in the requested page packet is assigned, including the substantive material under nominal headings and year-boundary records. The page-coverage audit reports the exact set of page identifiers covered by occurrence locators; it is a mechanical coverage check, not a substitute for reading the pages.

### Assessment fields

{table(S['by_verification'],'Verification level')}

{table(S['by_literal_correctness'],'Literal correctness')}

{table(S['by_publication_match'],'Publication match')}

The bibliography's `note = {{verified}}` means a linked source was actually opened. It does not automatically mean that every theorem in it was read. The item-level `verification` field provides that stronger distinction, and `code/output/reference_audit.json` gives the checked location and access evidence where recorded. A metadata check establishes identity and chronology; an indirect match must not be advertised as a read proof.

## 3. Provenance: a packet is not a clean academic year

There are {S['substantive_requested_year_items']} occurrences in the requested-year portion of the envelopes and {S['adjacent_1978_79_items']} occurrences assigned to the clearly adjacent 1978–79 records 445, 451 and 457. These numbers are deliberately reported separately. They avoid counting later material as evidence for the intellectual chronology of autumn 1977 or spring 1978.

The fixed schema has only one date field. This edition retains the supplied catalogue date there and places the actual notebook date in the talk summary and the provenance corrections. Thus the generated section heading alone is insufficient evidence for chronology. The most important discrepancies and boundary repairs are:

- The handwritten month on **P000705** appears to be IV, whereas the catalogue assigns **5 September 1977**. This conflict remains unresolved. The class-E chronology of the Atiyah–Ward correspondence in record419 uses the supplied September date and is conditional on it: the identified article was received31May and publishedJune1977. An uncertain handwritten date is not silently replaced by a convenient chronology.

- Manin's notebook heading is **21 November 1977**, while the supplied catalogue says 21 September. The Drinfeld–Manin paper was received on 27 November 1977, a useful and independently checkable chronological constraint (Drinfeld & Manin, 1978).
- Fuchs's spring lecture is **3 April 1978**, not the catalogue's 4 April. The later Fuchs lecture in record 457 is **5 March 1979**, not 5 March 1978.
- The apparently empty 1978–79 heading in record 445 actually introduces **Kruskal on surreal numbers, 30 October 1978**. Its mathematics is indexed instead of being discarded as a title page.
- Record 451 includes an extension-theory tail and **Belavin's 12 February 1979** bibliography and instanton-parameterization question. A reading list is not treated as evidence that all listed papers' theorems were stated in the seminar.
- Record 457 includes the end of a **Beilinson** discussion, the 1979 Fuchs talk and an **Ogievetsky, 19 March 1979** supersymmetry discussion. Item-level attribution keeps these distinct.
- Pages 753–754 are the beginning of the omitted catalogue record 437, dated **13 February 1978** in the notebook. They continue on page 756 and are retained as a clearly attributed precursor within the requested record-438 envelope. No unrequested twenty-ninth catalogue record is invented.
- Page 776 contains an adjacent **Palamodov** lecture on caustics, wave fronts and the Cauchy problem. It is not attributed to Calogero merely because it lies inside that catalogue range.

Several earlier page ranges also overlap: the bottom of 707 begins Krichever, the counterfeit-coin intervention spans 713–714 within Kirzhnits's envelope, and the Dickey discussion continues on 718 before S. I. Gelfand starts on 719. Each was segmented by the manuscript rather than duplicated under every encompassing range.

### The damaged page

PNG verification and complete decoding found one damaged attachment: `GELFAND-P000722.png` contains only 10,722 bytes. A normal read of the public MCCME record-429 page identified the original image sequence. The recovered page has 169,042 bytes, and the damaged upload is an exact byte prefix of it. Public images immediately before and after it match the supplied P000721 and P000723 byte for byte. This is much stronger provenance than a visually similar replacement. The original attachment was not overwritten. The recovery script, URL, hashes, validation output and recovered image accompany the chapter.

The complete page matters mathematically: it permits a direct inspection of the displayed rank-one generators and the Casimir sign. The critical entry records a faithful notebook error under the stated generator convention, rather than attributing an absent minus sign to the AI transcription.

## 4. Search methods, successful matches and limits

The working rule was to start from a specific formula, theorem, speaker and date, then require a primary result that matches its quantifiers. The searches used Math-Net, arXiv, publishers, author publication lists and collected papers, supplemented by targeted zbMATH, Scholar and MathOverflow queries where they were useful. A search-engine hit and an opened paper are different evidence. Paywalls, broken historical links and indexing gaps are recorded as access limits; they do not establish that a result does not exist. The detailed per-range research logs are included under `code/research_logs/`.

**Local Harish–Chandra algebra.** Bernstein's author bibliography led to the two original French announcements, which were downloaded and read page by page. Their shared Academy presentation date was 9 January 1978; the issues are dated 13 and 20 March. The second paper's actual pagination is 495–497, despite a repeated first-paper range in the author list. The read theorem restricts the nice-algebra description to a sufficiently small neighborhood of a regular infinitesimal character. Neither arbitrary singular blocks nor all unrestricted modules over a finite algebra are silently substituted for this statement (Bernstein et al., 1978a, 1978b).

**Instantons and Yang–Mills.** Math-Net gave the exact Drinfeld–Manin note and its receipt date; the primary Atiyah–Hitchin–Singer announcement fixed the dimension and historical family claims. The later comparison was checked against Dayaprema and Waldron's 2026 paper. Its path-connectedness theorem concerns instanton moduli; its flow theorem assumes an explicit energy range. These are not a classification of every finite-action critical connection. The universal-connection question had already been answered by Narasimhan and Ramanan, so its appearance in a 1977 lecture does not make it newly open.

**KP and Hamiltonian normalization.** Krichever's author archive yielded the three-page 1978 paper, including the received date of 6 September 1977. Comparing a title or a pole ansatz alone would have missed a coefficient problem. The exact equation printed in the notebook, its Laurent expansion and the differential-operator commutator were checked separately. The chapter gives a normalization that is internally consistent and distinguishes that reconstruction from the notebook's coefficient and from the published formula's conventions (Krichever, 1978).

**Dickey's requested simpler proof.** Lebedev and Manin (1979), §§5–6, give a conceptual proof of the relevant Jacobi identity through the coadjoint representation of the Volterra group. This matches the coefficient-linear first bracket in the notebook; it is not an indiscriminate reference to the different quadratic or second Adler–Gelfand–Dickey bracket. It is a definite solved request, not merely a later paper about Poisson brackets, and receives a problem entry because the notebook actually asks for the improvement.

**Classical and quantum scattering.** The Faddeev pages explicitly include breathers. A counterexample based solely on the existence of breathers would therefore misread the source. Chen, Liu and Lu's precise theorem instead identifies a real limit of the match: for the stated weighted generic-data class, radiation has modified scattering inside the light cone. That is not the same as an unrestricted assertion of free linear radiation in the energy topology. The exact particle mass formulas likewise require a declared bare or physical mass convention; “no further correction” is not transferred between those normalizations.

**Aomoto and cohomology.** The Ising and holonomic-field notes were compared with the Sato–Miwa–Jimbo program, while the arrangement statements were checked with nonresonance qualifications and the later erratum where relevant. The zero-weight example prevents an unqualified assertion of top-degree concentration. For the positive Witt algebra, the later Fuchs–Wilmarth theorem gives the corrected multiplicity convention and explicitly discusses the earlier calculation (Fuchs & Wilmarth, 2010).

**Integral substitution groups.** The productive search chain ran backward from Pavez-Cornejo's 2024 preprint/2025 publication to Babenko and Bogatyi (2008). A stale PDF link failed, but Math-Net's current full-text route succeeded. The 2025 publisher denied the web reader full text; the author's arXiv version supplied the statement. Both works use a closed commutator subgroup in the relevant topological abelianization. This prevents an unjustified assertion about the ordinary abstract abelianization. The real finite-jet cohomology is computed in the 2008 paper. The stronger integral ring is not computed by those cited theorems. No claim of universal absence from the literature follows from the negative exact searches.

**Rank-one arithmeticity.** The source's broad expectation was separated into the real, complex, quaternionic and exceptional cases. Falbel and Pasquinelli's 2023 primary paper explicitly states the remaining complex-hyperbolic question for dimension at least four. Yu's preprint, submitted 30 October 2026, still says known examples occur only in dimensions two and three and adds a new two-dimensional example. Its introduction provides a current positive check on the research landscape. A targeted search did not locate a solution in higher dimensions. The status is phrased as open in the literature located as of the review date, rather than as a mechanically certified exhaustive negative result.

## 5. Problem index and continuity with earlier years

{problem_rows}

The index has {S['problems']} entries because a definite historical question can remain worth following after it is solved. It does not create a research problem for every definition or method. An explicitly asked local-trivialization exercise can be recorded as a resolved question; an unidentified intervention receives no fabricated conjecture.

The C/D occurrences, which require a separate remaining-scope assessment, are:

{open_rows}

The supplied earlier index is an index of selected completed chapters, not the text of every previous talk. Its main headings cover GY1964, GY1965, GY1966, GY1967, GY1969, GY1971, GY1972, GY1973, GY1974 and GY1975; combined-year entries occur within it, but no complete 1976–77 inventory is supplied. A missing exact match therefore means “not identifiable in this supplied index,” not “never discussed before.” Earlier problem IDs reused in this chapter: {', '.join(old_gp) if old_gp else 'none after the exact-scope comparison'}. Earlier occurrences explicitly included in the problem arrays: {', '.join(earlier_ids) if earlier_ids else 'none; related earlier occurrences are identified in the item discussions and research logs'}.

The important cross-year navigation is nevertheless substantial. The 1975 rank-one spectral-curve constructions, including 1975-383.9–383.12 and 1975-385.1 and 385.4–385.8, give background to the Krichever announcements. GP-1975-26 concerns higher-rank, non-coprime commuting operators; the short 1977 announcement explicitly restricts to relatively prime orders, so treating it as a recurrence would change the question. The older particle-integrability entries 1975-372.7 and 372.12 do not by themselves state the rational-KP classification. The tautological universal connection in 1975-382.5 is a useful geometric neighbor of Manin's projection question, but the two formulations must be distinguished.

Similarly, GP-1975-21 is about formal **Hamiltonian** vector fields, and GP-1975-20 about Perchik's Euler series. Neither is the cohomology of the positive Witt algebra or of the integer substitution group. Earlier Ising-transfer and supersymmetry entries can help a reader, but they do not authorize importing all of their problems into the 1977 index. These decisions favor exact mathematical continuity over a larger apparent recurrence count.

## 6. Development, independent checks and what remains

### Integral finite-jet cohomology

The notebook asks to compute the cohomology of the group of integral formal substitutions and does not name the coefficient module or cochain topology. The chosen development is therefore explicitly editorial: cochains with trivial discrete coefficients that factor through one finite jet in all arguments. Filtered inflation makes this a cochain complex and gives its coefficient long exact sequences.

The one substantial literature input is the topological abelianization

`J / closure([J,J]) = Z² ⊕ (Z/2)²`.

Its explicit characters depend on the seventh jet. Hence finite-jet one-cocycles with a discrete target are exactly homomorphisms from that quotient. The coefficient sequence `0 → Z → Q → Q/Z → 0` then proves that **all** torsion in integral degree two is `(Z/2)²`: its connecting image is exactly the kernel of the rational-coefficient map, and the rational target is torsion-free. The two parity characters supply explicit integral Bockstein cocycles. This is a proof, not an inference from computed low jets.

For `f(t)=t+at²+bt³+ct⁴+…`, set `x=a`, `y=b−a²` and `w=c−3ab+2a³`. The identity `δw(f,g)=x(f)y(g)` gives a primitive for the mixed degree-one cup product. Squares vanish by the integer-valued binomial primitive. A second coordinate calculation identifies the fourth-jet quotient with an integer Heisenberg group and checks the sign independently. These particular cup identities also hold for the underlying discrete group; the degree-one and degree-two classification is asserted only for the declared finite-jet theory.

The computation checks symbolic substitution, independent integer convolution, 1,500 seeded triples, 1,024 and 4,096 exhaustive residue pairs, and 3,000 Bockstein cocycle equations. The proof was also checked against the mod-two coefficient sequence. That second sequence confirms the two-dimensional 2-torsion subgroup but cannot alone exclude higher or odd torsion; the rational argument remains necessary. The included independent proof review records any qualifications found.

What remains is the torsion-free integral part in degree two, the higher integral groups and their ring structure, and any comparison with all continuous or unrestricted discrete cochains. A bounded further run could compute integral resolutions and inflation maps for successive central jet extensions. Finite stabilization evidence would not prove an infinite stabilization theorem. The sources do not document why the original speaker left the integral question open; the chapter does not invent a historical explanation.

### Verification annotations

- **Counterfeit coins:** the distinction between identifying the coin and identifying both the coin and heavy/light orientation is checked constructively. The physical pan assignments and all heavy/light outcomes are enumerated for the 13-coin case. This verifies the notebook's potentially surprising count under the explicit identity-only interpretation.
- **KP:** an independent Laurent-coefficient calculation and differential-operator composition reproduce the corrected normalization. The notebook equation gives `q_yy = −8 Σ(q_i−q_j)^−3`; with `p=q_y`, the corresponding Hamiltonian is `½Σp² − 4Σ_(i<j)(q_i−q_j)^−2`. These constants are tied to that equation and time convention.
- **Witt Laplacian:** exact integer boundary matrices satisfy `d²=0`, and characteristic polynomials are computed for every exterior degree in weights 1–22 and 25. The aggregate spectrum at each weight agrees with a separately coded gap-partition rule; no separate theorem about the distribution among degrees is inferred from that aggregate comparison. The labels `(1,10,14)` and `(3,7,15)` both give eigenvalue 320 at weight 25, with total multiplicity 12. Thus the notebook's count of distinct eigenvalues fails. A separate enumeration checks every weight 1–25 before calling this the first collision. Vandermonde-cubed representatives are also checked as cycles and cocycles in degrees 1–4. No rounded numerical spectrum is used.
- **Calogero annotations:** independent symbolic routes check the leading transmission phase, the `2n+1` scaling of the moments, the Bianchi superposition sign, and the missing identity in the Hermite-root equilibrium linearization. A final independent read caught an interchange of T and its reciprocal in the first verification draft's boundary conditions. The notebook's actual incoming/transmitted convention was restored, a Volterra estimate supplied a complete leading-order argument, and endpoint-ratio assertions were added to the exact soliton check. The corrected phase coefficient remains `−c0/4`. This was a correction to our initial proof, distinct from the notebook's factor-of-two error. These calculations test explicit formulas; they do not infer the general published inverse-scattering theorems from small examples.

Every new proof or computation in the LaTeX development is marked with `\\ours` or `\\oursComputed`. Published statements retain their citations. The annotations make no research-priority claim.

## 7. Corrections and what the A–F classes miss

{table(S['by_correction_type'],'Correction type')}

The correction register is deliberately critical rather than an indiscriminate rewrite of the transcription. A **transcription** correction records a mismatch with the handwriting. A **translation** correction changes the English interpretation of the Russian. An **ambiguity** preserves a choice that the image does not decide. A **faithful error** records a mathematical defect already present in the notebook. A **provenance** correction identifies a date, attribution or boundary problem. These distinctions should remain visible in any exported edition.

Several examples show why the separate assessment fields matter. The BGG bundle thread is correctly identified even where the notes confuse a free exterior module with a nonzero trivial bundle. The Casimir display has a sign inconsistency under the given generators, although the local-algebra program is published and established. The final Faddeev page says that massive particles **scatter** like solitons; the Russian and English transcriptions' “appear” changes the mathematical claim. The reading was independently checked against the image. A broad black-hole information remark does not contain enough hypotheses to become a precise modern information-loss conjecture.

A single historical letter cannot simultaneously encode attribution, chronology, correctness, exact scope, publication identity, access level and current status. The schema's existing additional fields are therefore essential rather than bureaucratic metadata. In particular, the numerical C count depends on whether a broad historical question is indexed at its literal scope or at a chosen modern refinement; this chapter says when the latter is editorial.

## 8. Proposed improvements to method and data format

The present JSON schema is preserved for compatibility. The following additive fields would reduce repeated prose and prevent future aggregation errors:

1. **Separate dates:** `catalogue_date`, `source_date`, `source_date_confidence`, and a structured `date_evidence` locator. Retain a display date only as a derived field. Do not force a year-boundary item into the wrong intellectual chronology to satisfy an identifier validator.
2. **Source segments:** a list of page/region ranges with `attributed_speaker`, `catalogue_record`, `actual_event`, and `boundary_reason`. This would represent a half-page intervention and a multi-record continuation directly, and prevent duplicate counting across overlapping envelopes.
3. **Relation types:** distinguish `same_problem`, `earlier_background`, `special_case`, `stronger_refinement`, `publication_of`, and `correction_of`. A generic “related” link hides the exact-quantifier decisions that are central to this companion.
4. **Theorem-level verification:** store the opened URL, access date, proposition/theorem locator, checked hypotheses, scope of the match and whether proof or only metadata was read. A bibliography-wide verified flag is too coarse by itself.
5. **Search boundaries:** attach search date, exact principal queries, successful chains and unavailable sources to C, D and F decisions. Negative searches should never acquire the authority of an existence theorem.
6. **Computation provenance:** record script, exact output, parameters, arithmetic type and independence of the second check. Distinguish a proof using a published theorem from a symbolic identity check and from finite numerical evidence.
7. **Stable occurrence identity:** preserve these packet-based IDs, but allow an actual academic-year field and a cross-chapter ownership rule. When 1978–79 is edited, the adjacent material here should be linked or migrated with aliases rather than independently counted again.

The supplied builder and style are kept with the deliverable. Any necessary local typography repairs are documented alongside the original files; mathematical JSON remains the source of truth. The overview is constrained to two pages even though the occurrence chapter is long.

## 9. Presentation on the companion website

A reader arriving at one talk should first see its mathematical subject, the catalogue-versus-notebook date notice when relevant, the actual speaker attribution, and direct access to the relevant scan and both transcriptions. The occurrence list should follow immediately. Each entry should expose **notes**, **precise statement**, **editorial reconstruction**, **fate** and **status** as separate views. A historical class badge must be accompanied by the literal-correctness and verification fields; color alone must not suggest that class A means every formula is correct.

For this packet, the most valuable navigation is a connected sequence of the three Harish–Chandra lectures; the Drinfeld–Novikov–Manin–Belavin instanton material; the Krichever, Dickey, Faddeev and Calogero integrability discussions; and the Buchstaber–Fuchs cohomology material. Each sequence should retain item-level speaker changes and the differing mathematical scopes. Earlier-year background links should be labeled as background. The rational-KP question must not redirect to a different Calogero–Moser involution problem merely because their formulas resemble one another.

The problem page should give its precise formulation first, then occurrences in source order, then a dated statement of what is solved and what is not. For the integral substitution problem it should offer a visible coefficient/topology selector or explanatory notice, with the real finite-jet theorem, the integral partial result and the unrestricted discrete question as distinct scopes. The 13-coin entry likewise needs its information requirement visible before the count.

Corrections should be available beside the original line, with separate labels for handwriting mismatch and faithful mathematical error. The repaired P000722 image should carry its public-source and prefix-validation provenance. Search should cover mathematical notation, modern synonyms, Russian names and transliteration variants, bibliography keys and page IDs. A date filter should use the actual-event field once added, while a packet filter should continue to reproduce this deliverable exactly.

## 10. Build and reproducibility

The canonical seven files are the two indices and talk JSON, the overview and development TeX, the corrections CSV and the bibliography. `build_chapter.py GY1977` generates the chapter and standalone test driver. The prescribed XeLaTeX → BibTeX → XeLaTeX → XeLaTeX sequence produces the delivered PDF. A separate validator checks schema values, consecutive identifiers, the exact 28-record list, bibliography and citation targets, problem links, dated statuses and source-page coverage. Build logs and a final validation summary are included.

The supplied builder and style are unchanged. Long prose and two formulas were reflowed in their canonical source fields, and explicit delimiters preserve spaces after proof/computation markers. These deterministic typography repairs change no mathematical claim or classification. The installed TeX packages lacked their lookup databases and a usable format file; the included runtime launcher generated workspace-local lookup files, font maps and a format from those installed packages. No system modification or package download was required. The PDF embeds all 22 fonts, including the Cyrillic-capable DejaVu Serif fallback selected by the supplied style.

The PDF is visually inspected after compilation, including the overview, representative occurrence pages, developments, problem index, corrections and bibliography; an all-page contact-sheet pass checks for abnormal blank pages and gross layout defects. Errors and unresolved citations must be cleared before packaging. Finite computations are rerunnable with Python and SymPy, with Pillow used for the image integrity check. Some archival access scripts require the separately supplied source attachments and network access; the included README identifies those dependencies. The chapter itself rebuilds from the ZIP without downloading research papers.

The bibliography is checked against the cumulative file, reusing existing keys and remapping duplicate DOI identities. Every new source has an opened link or is explicitly marked unverified. Full copies of downloaded third-party research papers are not included in the archive; citations, theorem locators and verification logs preserve the evidence trail without redistributing a paper collection. The one recovered manuscript image is included because it repairs an incomplete page in the user-supplied source packet.

## Selected primary sources for the report

The complete, canonical bibliography is `GY1977_references.bib`; the PDF supplies the generated author–year bibliography. The following links identify the principal sources discussed above.

- Babenko, I. K., & Bogatyi, S. A. (2008). On the group of substitutions of formal power series with integer coefficients. *Izvestiya: Mathematics, 72*(2), 241–264. https://doi.org/10.1070/IM2008v072n02ABEH002399
- Bernstein, I. N., Gelfand, I. M., & Gelfand, S. I. (1978a). Structure locale de la catégorie des modules de Harish-Chandra. *Comptes rendus de l'Académie des sciences de Paris, Série A, 286*, 435–437. https://www.math.tau.ac.il/~bernstei/Publication_list/publication_texts/BGG_Harish-Chandra_modules_1.pdf
- Bernstein, I. N., Gelfand, I. M., & Gelfand, S. I. (1978b). Structure locale de la catégorie des modules de Harish-Chandra, II. *Comptes rendus de l'Académie des sciences de Paris, Série A, 286*, 495–497. https://www.math.tau.ac.il/~bernstei/Publication_list/publication_texts/BGG_Harish-Chandra_modules_2.pdf
- Dayaprema, A., & Waldron, A. (2026). Parabolic gap theorems for the Yang–Mills energy. *Mathematical Physics, Analysis and Geometry, 29*, Article 12. https://doi.org/10.1007/s11040-026-09549-z
- Drinfeld, V. G., & Manin, Yu. I. (1978). Self-dual Yang–Mills fields over a sphere. *Functional Analysis and Its Applications, 12*(2), 140–142. https://doi.org/10.1007/BF01076262
- Falbel, E., & Pasquinelli, I. (2023). Complex hyperbolic orbifolds and hybrid lattices. *Geometriae Dedicata, 217*, Article 28. https://doi.org/10.1007/s10711-022-00762-y
- Fuchs, D., & Wilmarth, C. (2010). Laplacian spectrum for the nilpotent Kac–Moody Lie algebras. *Pacific Journal of Mathematics, 247*(2), 323–334. https://msp.org/pjm/2010/247-2/pjm-v247-n2-p04-p.pdf
- Krichever, I. M. (1978). Rational solutions of the Kadomtsev–Petviashvili equation and integrable systems of N particles on a line. *Functional Analysis and Its Applications, 12*(1), 59–61. https://www.math.columbia.edu/department/krichever/pdfs/1975-1979/1978-RSOTKSEATISONPOAL0.pdf
- Lebedev, D. R., & Manin, Yu. I. (1979). The Gel'fand–Dikii Hamiltonian operator and the coadjoint representation of the Volterra group. *Functional Analysis and Its Applications, 13*(4), 268–273. https://doi.org/10.1007/BF01078365
- Pavez-Cornejo, J. (2025). On the abelianization of certain groups of formal power series. *Communications in Algebra, 53*(11), 4520–4545. https://doi.org/10.1080/00927872.2025.2488038 (Preprint first posted 19 July 2024: https://arxiv.org/abs/2407.14019.)
- Yu, C. (2026). *A nonarithmetic lattice from a mirror in the Couwenberg–Heckman–Looijenga construction* [Preprint]. arXiv. https://arxiv.org/abs/2611.00270
'''
(D/'GY1977_report.md').write_text(report)
print(json.dumps({'overview_words':len(overview.split()),'report_words':len(report.split()),'pdf_pages':pdf_pages},indent=2))
