"""Generate transparent counts, source manifests and the final editorial report."""
from pathlib import Path
import collections,csv,json,re
ROOT=Path(__file__).resolve().parents[1]
T=json.loads((ROOT/'GY1967_talks.json').read_text()); I=json.loads((ROOT/'GY1967_items.json').read_text()); P=json.loads((ROOT/'GY1967_problems.json').read_text())
R={t['record']:t for t in T}
with (ROOT/'GY1967_corrections.csv').open(newline='') as f:C=list(csv.DictReader(f))
B=(ROOT/'GY1967_references.bib').read_text()
entries={m[1]:m[0] for m in re.finditer(r'(?ms)^@\w+\s*\{\s*([^,\s]+)\s*,.*?(?=^@|\Z)',B)}
counts=collections.Counter(x['class'] for x in I)
areas={}
for records,area in [([131,157,160,161,172],'Lie groups and representation theory'),
                     ([132,134,135,171,173],'Topology, bundles and manifold classification'),
                     ([137,142],'Functional analysis and moment representations'),
                     ([138,140,166],'Dynamics and hyperbolic counting'),
                     ([139,143,150,151,152,154],'Algebraic/complex geometry, sites and moduli'),
                     ([144,145],'Noncommutative algebra and Lie fields'),
                     ([146,147,153,156,164,168],'PDE, complexes and spectral asymptotics'),
                     ([155,163,167],'Arithmetic geometry and non-Archimedean analysis'),
                     ([159,169,170],'Operator theory and matrix geometry'),
                     ([162],'Differential geometry and differential relations')]:
    areas.update({r:area for r in records})
def area(x):
    if x['record']==133:return 'Mathematical physics and integral identities' if int(x['id'].split('.')[-1])<=2 else 'Dynamics and hyperbolic counting'
    if x['record']==136:return 'Differential geometry and differential relations' if x['id'].endswith('.1') else 'Unidentified programme labels'
    if x['record']==149:return 'Arithmetic geometry and non-Archimedean analysis' if int(x['id'].split('.')[-1])<=2 else 'Differential geometry and differential relations'
    return areas[x['record']]
def speaker(x):return x.get('speaker') or R[x['record']]['speaker']
def matrix_rows(group):
    groups=collections.defaultdict(collections.Counter)
    for x in I:groups[group(x)][x['class']]+=1
    return [[k]+[v[c] for c in 'ABCDEF']+[sum(v.values())] for k,v in sorted(groups.items(),key=lambda kv:(-sum(kv[1].values()),kv[0]))]
def table(headers,rows):
    def cell(x):return str(x).replace('|','\\|')
    return '\n'.join(['| '+' | '.join(map(cell,headers))+' |','| '+' | '.join(['---']*len(headers))+' |']+['| '+' | '.join(map(cell,row))+' |' for row in rows])
def writecsv(name,fields,rows):
    with (ROOT/'audit'/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
writecsv('item_classification.csv',['id','record','speaker','area','class','literal_correctness','verification','problem'],
         [dict(id=x['id'],record=x['record'],speaker=speaker(x),area=area(x),**{k:x[k] for k in ['class','literal_correctness','verification','problem']}) for x in I])
writecsv('record_coverage.csv',['source_order','record','date','speaker','kind','catalogue_pages','actual_item_pages','items'],
         [dict(source_order=n+1,record=t['record'],date=t['date'],speaker=t['speaker'],kind=t['kind'],catalogue_pages=t['pages'],actual_item_pages='; '.join(dict.fromkeys(x['pages'] for x in I if x['record']==t['record'])),items=sum(x['record']==t['record'] for x in I)) for n,t in enumerate(T)])
def field(entry,name):
    m=re.search(r'\b'+name+r'\s*=\s*\{([^{}]*)\}',entry,re.I)
    return m[1] if m else ''
writecsv('reference_manifest.csv',['key','doi','url','note','item_occurrences'],
         [dict(key=k,doi=field(v,'doi'),url=field(v,'url'),note=field(v,'note'),item_occurrences='; '.join(x['id'] for x in I if k in x['refs'])) for k,v in sorted(entries.items())])
status={'records':len(T),'items':len(I),'problems':len(P),'references':len(entries),'corrections':len(C),
        'classes':dict(counts),'items_by_speaker':dict(collections.Counter(speaker(x) for x in I)),
        'items_by_area':dict(collections.Counter(area(x) for x in I)),
        'correction_types':dict(collections.Counter(x['type'] for x in C)),
        'verification_levels':dict(collections.Counter(x['verification'] for x in I)),
        'literal_correctness':dict(collections.Counter(x['literal_correctness'] for x in I)),
        'academic_years':{str(y):{'records':sum((t['record']<=147)==(y==1967) for t in T),'items':sum(x['id'].startswith(str(y)+'-') for x in I)} for y in [1967,1968]}}
(ROOT/'audit/counts.json').write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n')

report=f'''# GY1967 — critical-companion research and build report

**Academic years:** 1967–68 and 1968–69. **Status date:** 9 November 2026.

## 1. Completed deliverable and counting conventions

The chapter covers every supplied MCCME record 131–173: **{len(T)} records, {len(I)} mathematical occurrences, {len(P)} problem-index entries, {len(C)} corrections and {len(entries)} bibliography entries**. All seven required structured/source files are present, together with the generated chapter, standalone driver and compiled PDF. The archive also contains reproducible authoring/integration/checking code, exact computation outputs, the untouched supplied build kit, source-audit notes, independent reviews and build logs.

The unit counted is a distinct *occurrence*, not a unique theorem, published result, speaker contribution or research problem. Repeated results in later talks therefore count again and link through the problem index where the question is genuinely the same. Definitions, constructions, proof methods, counterexamples and substantive programme notices are included. A list of prospective speakers is recorded in the talk summary; it is not expanded into invented talks or theorems. Records 141, 148, 158 and 165 have no separately identifiable mathematical items. There are 37 talk records, 3 plans and 3 headings under the supplied `kind` vocabulary.

{table(['Class','Meaning','Items','Share'],[[c,{'A':'Speaker/Gelfand research published soon afterward','B':'Developed by others; includes a negative resolution','C':'Partial results and a precise residual question','D':'No development found after an adequate search','E':'Known material / established antecedent','F':'Exact assertion, scope or attribution not identifiable'}[c],counts[c],f'{100*counts[c]/len(I):.1f}%'] for c in 'ABCDEF'])}

The two academic-year ID prefixes are substantive: 1967 for records 131–147, 1968 for 148–173. The original builder's one-year assumptions were corrected rather than relabeling the second year incorrectly.

{table(['Academic year','Catalogue records','Items'],[[f'{y}–{str(y+1)[-2:]}',status['academic_years'][str(y)]['records'],status['academic_years'][str(y)]['items']] for y in [1967,1968]])}

### Items by speaker

The speaker is the occurrence's explicit `speaker` when one is supplied, otherwise the talk heading. Joint headings remain one category; they are not counted twice or arbitrarily divided. The Weinstein catalogue identity is retained with its explicit qualification. These are attribution counts, not claims of authorship or priority.

{table(['Speaker / heading','A','B','C','D','E','F','Total'],matrix_rows(speaker))}

### Items by area

Areas are mutually exclusive editorial counting labels, not a claim that the subjects are mathematically disjoint. The dominant area of the source record is used, with item-level distinctions in mixed records 133, 136 and 149. Representation-theory reading programmes are counted in their stated subject; an unidentifiable programme label has its own category. `audit/item_classification.csv` exposes the assignment for every occurrence.

{table(['Editorial area','A','B','C','D','E','F','Total'],matrix_rows(area))}

## 2. Source coverage and provenance

The English and Russian transcriptions were read across the assigned material. The Russian is controlling when a formula, quantifier, name or date matters. The scans were consulted directly for uncertain readings, decisive formulas, diagrams and disagreements. The detailed audits record actual visual coverage: all P208–P228 and P253–P284, plus the specified consequential pages within P229–P252. This is **not** a claim that every graphical stroke in all 77 scans was independently deciphered. The complete text coverage and the narrower scan-reading claims are kept separate.

The supplied catalogue's page ranges overlap and sometimes extend well beyond the actual talk. They remain in `talks.json` as catalogue metadata; `items.json` gives the narrower ownership determined from the source headings. Six initially narrowed c-fragment ranges were restored to the supplied catalogue during integration, without moving their mathematical items. `audit/integration.json` records these changes. In particular, Kazhdan's Dwork exposition continues beyond the catalogue's nominal record 163 endpoint. Clipping it at that endpoint would omit mathematics.

Two source-order inversions are preserved: 164 before 163, and 170 before 169. Bleher's normalized date is resolved to 31 March 1969 from the scan's 31/III and its year block. The catalogue's 27 October 1968 date is retained even though it is a Sunday; the chapter does not silently regularize it to a Monday. Record 159 says “Prof. Weinstein (USA)” in the scan: the methodology matches **Alexander** Weinstein's paper, whereas the catalogue says **Alan**. That is recorded as a probable misidentification, not silently settled from a surname alone.

### The end-boundary discrepancy

All 77 supplied pages were accounted for, but only P208–P282 belong to these records' mathematical content. The actual Buchstaber continuation in record 173 occupies P282. The next page explicitly begins 15 September 1969; P284 also begins 22 September 1969. The catalogue range P280–P284 therefore cannot be treated as a literal assertion that all these passages were spoken on 21 April. The boundary material is inventoried below so that it is neither lost nor falsely assigned.

{table(['Page','Visible heading / attribution','Material present; no in-scope occurrence ID assigned'],[
['P283','15.9.69; B. Vainberg','Hörmander/Borovikov fundamental-solution singularities; integral representations for homogeneous equations; analytic continuation of parameter powers.'],
['P283','Grushin intervention','Distributional boundary values involving P(ξ)±i0 and a partition of unity on the sphere.'],
['P283','Bernstein-problem notice','Entire minimal graphs: the notebook uses ambient dimension n, states n≤8 versus n≥9, and names De Giorgi, Simons and Bombieri. No fate assessment is imported into this chapter.'],
['P283–P284','Kazhdan and Bernstein','Spectral convergence under exhaustion; continuity of spectral-subspace functions, evaluation norms, pointwise spectral measures and the projector kernel.'],
['P284','Kazhdan on M. Artin, Bourbaki','Formal versus convergent solutions of analytic equations and arbitrarily close analytic approximation.'],
['P284','22.9.69; Fichera','The opening of the unilateral-contact/Signorini elasticity problem; equations and boundary traction, continuing beyond the supplied cut.']])}

This boundary decision is also a provenance correction. It does not create additional MCCME records, guess their numbers or erase their text. A chapter for 1969–70 should take up those passages using its own catalogue and the continuation scans.

## 3. What the literature search established

The productive route was usually an exact bibliographic fingerprint followed by a result-level check. Math-Net recovered Soviet announcements and full translations; Numdam supplied French primary papers and seminar reports; author-hosted or journal-archive copies supplied papers otherwise behind broken publisher links. The item fields give theorem/section/page locators and distinguish publication from an earlier announcement, conference, preprint or manuscript receipt. Receipt is recorded as receipt: it is not automatically public circulation.

**Gelfand–Fuchs:** the 1967 topology paper is an unusually close match to the ray quotient, global linear charts, frame universality, cohomology and natural-bundle constructions. The 1968 elementary-object paper has stronger hypotheses than the notes. These are genuine publication matches in the specified Hausdorff/category setting, not a retrospective replacement by ordinary numerable principal bundles. The failed weighted ray selector and the difference between an embedding in a product and an invertible coordinate are retained as substantive qualifications.

**Interpolation:** a tempting positive match to Semenov is insufficient. Sharpley's 1975 primary paper explicitly supplies counterexamples to the underlying fundamental-function interpolation criteria. The chapter separates the exact historical match, the false broad literal claim, valid specializations, and the corrected role of Boyd dilation indices. A publication match is not a truth certificate.

**Dynamics:** Adler–Weiss 1967 provides the exact entropy classification and the particular symbolic recoding already visible in the October notes. Those are E, not a conjecture resolved only after Sinai's lecture. Sinai's own 1968 papers supply the later geometric Markov-partition results. Left and right Perron vectors, the logarithm of the expanding eigenvalue, mod-zero metric isomorphism and topological conjugacy are separated. The nilpotence “if and only if” fails for a concrete Heisenberg lattice; the standard central eigenvalue calculation is included.

**Lie and Weyl fields:** the finite-centre-extension/virtual-Laplace theorem is distinct from the unextended semisimple Gelfand–Kirillov assertion. Premet's counterexamples refute the latter in general. The 2013 G2 commutative rationality theorem is not a noncommutative division-ring solution. The November 2026 status explicitly says which remaining Lie-type claims were not verified, rather than asserting that the 2013 list is current by default. The first Weyl algebra's polynomial automorphisms, its fraction-division automorphisms, and Dixmier-style endomorphism questions are different problems.

**Complex analysis, moduli and differential relations:** Hörmander's exact weighted d-bar statements restore the domain, boundary, degree, weight and Levi hypotheses. The apparent negative bounded-disc assertion is checked against the Cauchy–Green solution. Mumford's actual notes recover the group-action sites, moduli obstruction and level structures; later stack language is labeled as reconstruction. A sheaf on a disjoint union uses a product, not an unrestricted direct sum. Polarization alone does not remove elliptic automorphisms. The Picard calculation in characteristic 3 is separated from Betti cohomology and its later all-field extension. Sweeney/Spencer distinguishes the descending-jet first sequence from the symbol-quotient second sequence. Gromov's theorem needs an open manifold and an open invariant relation; it does not make every formal distribution integrable on every closed manifold.

**Spectral and topological methods:** Davis's exact paper resolves “shell,” relations and spherical caps; Au-Yeung's complex-field condition is essential. Bleher's source is Hörmander's 1968 spectral-function paper, including the sharp sphere example and the effect of smoothing. The homotopy-torus discussion separates K1 from Wh, PL finiteness from the finite-smoothing bridge, normal cobordism from h-cobordism, and homotopy-type variation from smoothings of one topological manifold. The exact Buchstaber–Mishchenko report is a meeting abstract on p. 224, dated 22 April 1969; it is not a standalone paper nor prior evidence for the 21 April talk.

**Discrete series:** a second chronology check found a real distinction. Schmid's January 1968 announcement has a restricted antidominant/high-tensor-power L2 antecedent; Griffiths's 1966 root-count formula and compact-quotient statement are earlier still. Neither establishes the all-chamber theorem on a fixed noncompact domain. That full vanishing item is B, matched to Griffiths–Schmid's later printing, and irreducibility is a separate B. The 1971 sufficiently-regular result is not credited with the unrestricted 1976 theorem. Schmid's own 1978 ICM address, printed 1980, supplies the directly read confirmation of the latter conclusion.

The individual URLs, read-result locators and failed access routes are recorded in `audit/source_audit_a.md`, `source_audit_b.md`, `source_audit_c.md` and `source_audit_root.md`; the reference manifest lists all final keys. The independent reviews supplement, rather than substitute for, those audits.

## 4. Problems and the development decision

The final index has 11 entries: two exact recurrences retaining earlier IDs and nine new historical problem IDs. A resolved question remains useful in this index. The common-fixed-point question, two-torus entropy classification, universal elliptic-family obstruction, Riesz-mean question, Langlands realization and homotopy-torus finiteness are not presented as open today. Earlier occurrences are retained as text and current ones link to their entries.

{table(['ID','Question / programme','Final status and scope'],[
['GP-1966-01','Algebraic classification of Anosov diffeomorphisms','C; general topological conjugacy to an affine infranil model remains unresolved in the audited primary sources. Earlier 1966-94.4 retained.'],
['GP-1965-08','Automorphisms of Weyl division rings','C; full Aut_C(D1) description not supplied by the checked results. Earlier 1965-80.10 retained. Known coordinate stabilizer developed here.'],
['GP-1967-01','Classifying noncompact groups over Hausdorff bases','Answered in the precisely specified bundle category; the elementary-object hypotheses matter.'],
['GP-1967-02','Commuting interval maps','Continuous common-fixed-point assertion false; the C1 fixed/periodic statement has different quantifiers. No extra continuous-periodic conjecture imported.'],
['GP-1967-03','Metric classification of hyperbolic two-torus automorphisms','Established by Adler–Weiss 1967; invertible mod-zero measure isomorphism, not arbitrary measurable intertwining.'],
['GP-1967-21','Unextended semisimple Gelfand–Kirillov conjecture','False in general; exact negative types stated. Central extensions are a different theorem.'],
['GP-1968-01','Universal family for elliptic moduli','Coarse moduli obstruction and rigidification/stack distinction; exact later characteristic claims separated.'],
['GP-1968-20','Pointwise hyperbolic circle remainder','C, expressly reconstructed: full spectral main term removed; target X^(1/2+epsilon), not the notebook’s unspecified literal square-root assertion.'],
['GP-1968-40','Higher spectral terms with fixed smoothing order','Already addressed by the identified 1966/1968 work, with exact smoothing/remainder scope.'],
['GP-1968-41','Langlands harmonic realization','Established; the early sufficiently-regular and later unrestricted results are distinguished.'],
['GP-1968-42','Finiteness of smooth homotopy tori','Established for fixed n≥5; within an h-cobordism class there is exactly one unmarked diffeomorphism type.']])}

**A conservative final reclassification:** occurrence 1967-142.3 was initially drafted as C with a modern universal Radon-representation property. The independent review found that the notebook's algebraic/topological category is underdetermined and that the checked sufficient criteria do not certify a particular recognized open conjecture. The final occurrence is **F**, with that reconstruction still explicitly explained for comparison. The provisional GP-1967-20 is not emitted in the final index. The final JSON and this report supersede the frozen authoring-fragment counts on this point. This is an evidential decision, not a claim that the broad moment programme has been solved.

### The bounded Weyl development

The strongest notebook-supported question is the full division-ring automorphism problem. The bounded question treated here assumes that an automorphism preserves the rational coordinate field C(q). The result is known in the literature: Dumas 2011 § 5.3.3, final Remark, printed p. 66, referring to Alev–Dumas 1998. The formal-series embedding is § 5.2.2, pp. 59–60. The chapter explicitly rederives this special case and makes no novelty claim.

The complete proofs construct the formal pseudodifferential division ring, justify finite coefficient sums and generalized Vandermonde associativity, construct two-sided inverses, and prove the centralizer C_D1(q)=C(q). They then classify q-fixing rational shears and all automorphisms stabilizing C(q), supply the explicit inverse and conjugation action, and prove that polynomial preservation is equivalent to an affine coordinate substitution and a polynomial shear. The rational 1/q shear and inversion example verify the exact boundary between A1 and its division ring. Every result rederived here carries the required editorial proof marker.

Two independent algebraic reviews found no defect. The more detailed review independently derives the pair-composition law, so it checks the potentially treacherous substitution order rather than merely repeating the displayed inverse. The exact symbolic script passes 522 assertions across negative-power commutators, Möbius inverse substitutions, both orders of inverse coefficients, differential-operator tests on rational functions, conjugation and generalized Vandermonde identities. Finite computation checks conventions and examples; it is not the proof of the universal statements. A separate 105-check script verifies editorial arithmetic, and the earlier fragment supplies six further normalization/counterexample families.

The remaining obstruction is explicit: an arbitrary automorphism can move C(q) to a different rational coordinate subfield. A commutator-one pair is not automatically a generating pair. One further bounded run could certify generation by inverse rational expressions and investigate factorization of a specified finite-complexity family; it could not infer global generation of the automorphism group from finitely many examples. No comparable bounded contribution was justified for the general Anosov classification or pointwise hyperbolic-circle exponent. The chapter does not pad its developments with speculative proofs of those problems.

## 5. Corrections and what the classification does not measure

{table(['Correction type','Rows'],sorted(status['correction_types'].items()))}

The 101 rows distinguish transcription/translation mistakes, ambiguous readings, provenance problems and **faithful errors**: mathematics that both transcriptions accurately preserve from the notebook. These are not 101 accusations against the transcriber. Examples include the missing Feynman 2!, the Perron-vector orientation, the repeated rectangle intersection, the square-root determinant sign, the K1/Wh distinction, the sphere binomial and Riesz normalization, and the positive-root restriction in the degree formula. Where the scan does not decide between readings, the row states the ambiguity rather than inventing a diplomatic correction.

{table(['Literal-correctness assessment','Items'],sorted(status['literal_correctness'].items()))}

{table(['Item verification level','Items'],sorted(status['verification_levels'].items()))}

The verification count is a count of assessment labels, **not** a count of original proofs independently checked. “Read the result” may refer to the exact theorem in a primary later exposition while a second cited historical source was checked only through metadata; the fate field and source audits say which. Similarly an F occurrence may cite a read special-case theorem precisely to explain why that theorem does not identify its unrestricted notebook assertion. Every final bibliography entry has an opened URL or DOI and an explicit verification note; the item-level fields carry the stronger scope distinctions.

Classes A–F alone miss at least five important axes this year: literal correctness; attribution confidence; exact versus partial publication matching; public circulation versus manuscript existence; and ambiguity in the category or quantifiers. A includes contemporary research reports whose original formulation needs repair, and E includes classical theorems recorded inaccurately. B can mean a negative resolution, as with the general Gelfand–Kirillov conjecture. F measures an evidential limitation, not mathematical importance or lack of subsequent work. The richer assessment fields are therefore necessary, not optional decoration.

## 6. Method and format recommendations

1. **Retain separate catalogue and actual source intervals.** The existing talk/item distinction works, but an explicit optional `actual_pages` or provenance object would make overlap and boundary disputes easier to index. A scan excerpt crossing a year boundary must not silently expand the catalogue scope.
2. **Represent chronology with typed dates.** Proposed optional fields are `manuscript_received`, `first_public_announcement`, `preprint`, `journal_volume_year` and `printed`. A received date must not populate a public-circulation field. Griffiths–Schmid and the Moscow meeting abstract show why this matters.
3. **Permit a reconstruction qualifier for indexed problems.** The circle problem has a well-defined modern target but the notebook's literal main terms are missing. A flag such as `formulation_origin: editorial_reconstruction` would make that distinction searchable. An underdetermined programme should remain F unless a precise indexed question is defensible.
4. **Record verification per reference/claim where feasible.** One item can use an original metadata record, a full later primary exposition and an independently supplied elementary check. A single item label cannot express that mix; the present source audits compensate.
5. **Keep negative fates and nonnovel developments explicit.** A later counterexample is an informative fate. A complete rederivation of a useful known special case is valuable only when its known status is prominent. Absence from the previous companion index is never evidence of novelty.
6. **Validate reciprocal links and both academic years.** The amended builder and independent validator check sequential IDs, all citation keys, dated statuses, enum values, problem reciprocity, source bounds and empty-record coverage. The builder now renders the supplied problem index rather than silently omitting it. Original kit files are preserved for comparison.

## 7. Reproduction, build and remaining limits

Run `python build_chapter.py GY1967` in the archive root, then `xelatex GY1967_test`, `bibtex GY1967_test`, and XeLaTeX twice. `code/build.sh` provides the same sequence with error stopping and the environment repair used in this workspace. The system TeX binaries were present but their search database/format configuration was incomplete: direct TEXMF search and a scratch-built XeLaTeX format restored the installed distribution. This did not require an external TeX replacement. Four complete DejaVu Serif faces and their license are included for reproducible Cyrillic and italic text.

The build modifications are limited to the dual-year validation/title, problem-index and correction rendering, cross-reference checks, and readable typography. The source data remain the authoritative content. The required XeLaTeX/BibTeX chain completed; the final machine-readable build and visual results are in `audit/final_verification.json` and `audit/visual_review.md`. The visual review addresses page layout, formulas, Cyrillic, bibliography and correction entries; it is not a second independent proof of every theorem.

`code/integrate.py` merges the preserved fragments and cumulative keys, applies the explicit final `editorial_overrides.json`, and writes the deliverables. `code/make_report.py` regenerates these counts and manifests. `code/validate_dataset.py` is an independent cross-reference audit. `code/verify_weyl.py` and `code/verify_editorial_calculations.py` require the pinned SymPy dependency; their exact outputs are included. The six earlier elementary-check families use the standard library. Authoring scripts serialize human/model-authored critical entries; they do not infer mathematical statements automatically.

No downloaded journal PDFs, scanned external literature, browser-cookie pages or installed Python dependency trees are redistributed. User-supplied text inputs, the predecessor index, cumulative bibliography and original kit are retained under `code/inputs` and `code/kit_original`; original scans remain a supplied input, not a second copy in this archive. The main final files are sufficient to rebuild the chapter without any research download.

Remaining limitations are explicit within the entries: incomplete notebook assertions, metadata-only access to certain originals, approximate identification of a visiting Weinstein, qualified reconstruction of the hyperbolic-circle remainder, and current-status audits that are careful searches rather than proofs of exhaustive bibliographic absence. None is silently turned into an undeveloped D item or an invented theorem.
'''
(ROOT/'GY1967_report.md').write_text(report)
print(json.dumps({'status':'report and manifests written','records':len(T),'items':len(I),'problems':len(P),'references':len(entries),'corrections':len(C)},indent=2))
