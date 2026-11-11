import pathlib,json,collections
D=pathlib.Path(__file__).parent
items=json.loads((D/'items.json').read_text());talks=json.loads((D/'talks.json').read_text());problems=json.loads((D/'problems.json').read_text())
sources=json.loads((D/'source_audit.json').read_text())
areas={586:['Integrable systems','Periodic spectral theory','Hamiltonian perturbations'],587:['Spectral zeta functions','Finite gap operators','Regularized determinants'],588:['Symplectic topology','Variational calculus','Many-valued actions'],589:['Poisson geometry','Classical r-matrices','Integrable systems'],590:['Index theory','Spectral asymmetry','Pseudodifferential operators'],591:['Loop groups','Infinite-dimensional Grassmannians','Integrable systems'],592:['KP hierarchy','Algebraic curves','Determinant lines'],594:['KP hierarchy','Formal pseudodifferential operators'],593:['Equivariant cohomology','Symplectic localization'],596:['Hamiltonian torus actions','Moment-map convexity'],595:['Arithmetic geometry','Hasse–Weil zeta functions','Automorphy'],598:['Arithmetic zeta functions','Polynomial Dirichlet series']}
(D/'area_by_record.json').write_text(json.dumps({str(k):v for k,v in areas.items()},ensure_ascii=False,indent=2)+'\n')
segments=json.loads((D/'source_segments.json').read_text())
for x in segments:
 if x['record']==594:x['start']='Wilson heading in lower written strip; upper scan area is blank'
 if x['record']==595:x['segments']=[{'page':'P001113','from':'Beilinson heading in lower portion','to':'end'}, {'page':'P001114','from':'top, local zeta definition','to':'before Wodzicki heading'}, {'page':'P001114','from':'B. heading after third divider','to':'end'}]
 if x['record']==598:x['segments']=[{'page':'P001114','from':'Wodzicki heading after second divider','to':'third divider before B. heading'}]
(D/'source_segments.json').write_text(json.dumps(segments,ensure_ascii=False,indent=2)+'\n')
intro=r'''# Research and scan audit: spring / integrable systems shard

**Scope and audit date:** records 586, 587, 588, 589, 590, 591, 592, 594, 593, 596, 595, 598; verified through **11 November 2026**. Read CHAPTER_FORMAT.md before authoring and the complete GY1982_prompt.md. Both English and Russian transcriptions were consulted throughout the assigned material. Russian was reread page by page for formula-heavy portions and every ambiguity below. Original scans, not transcription typography alone, determine emendations.

## Deliverable and reproducibility

The six required shard files are talks.json, items.json, problems.json, corrections.csv, references.bib, and this audit. The authoring script write_records.py saves after every record. The bibliography script preserves cumulative keys and produces source_audit.json. The audit script produces this document and area_by_record.json. independent_checks.py and checks_output.json contain exact elementary checks. Root owns the joint chapter, substantive development, final build and delivery.

source_segments.json is the website/source attribution map. Catalogue ranges are retained verbatim in talk metadata; exact item locations do not inherit those overlaps.

| Record | Actual source segment | Boundary decision |
|---|---|---|
| 586 | P001087 to upper P001089 | Ends before Wodzicki; P001086 ends Arnold, record 585. |
| 587 | Lower P001089–P001092 | Includes determinant and Clausen interventions. |
| 588 | P001093 to upper P001094 | Ends at Semenov-Tian-Shansky heading. |
| 589 | Lower P001094–P001095 | Drinfeld pointer belongs to this heading. |
| 590 | P001096–P001098 | Includes Fedosov and Gelfand interventions. |
| 591 | P001099–P001100 | Includes Krichever’s final KP intervention. |
| 592 | P001101–P001107 | Detailed Wilson lecture. |
| 594 | Written strip of P001108 | Before record 593 in notebook order. |
| 593 | P001109–P001112 | Extends beyond its catalogue end. |
| 596 | P001113 above Beilinson | Before 595; opening Levinson plan has no specified theorem. |
| 595 | Lower P001113, then P001114 around Wodzicki | Resumed “B.” paragraph belongs to Beilinson. |
| 598 | Middle interruption of P001114 | Ends before “B.”; not the full catalogue range. |

P001115 starts **5 September 1983**, with Deligne on Faltings/families/Néron-type degeneration. It is outside this academic-year shard. Overlapping catalogue ranges for 596 and 598 do not attribute September material to either speaker. This is a provenance correction.

## Scan inspection register

All source scans **P001087–P001115** were visually inspected. P001087–P001091 were inspected at original resolution in the early pass; P001092–P001115 as full-page 1150-pixel previews, with original/cropped inspection where needed. Reduced images are in scan_review; originals remain in work/scans. P001115 is inspected to verify exclusion.

| Scan | Details checked visually |
|---|---|
| P001087 | Krichever heading/date; perturbed KdV; incompatible \(I_3\) density and variational derivative. |
| P001088 | Old edges/double points; Hessian; gap numerator/denominator; higher-variation request. |
| P001089 | Speaker boundary; logarithmic theta expression; repeated pairing index; Hill zeta; rational-shift question; malformed binomial series. orthogonality.png confirms repeated \(s\) versus \(s'\). |
| P001090 | Quasimomentum graph; universal polynomials; factorial/denominator ambiguity. No unsupported factorial restoration. |
| P001091 | Explicit \(T=2\pi\); Bernoulli factor; opposite \(g_3\) signs; period diagram. Sign pair is compatible with \(E=-\wp(a)\). |
| P001092 | Determinant query; even-zeta normalization; \(B_2\) in cube sum; D-module diagram; Clausen definitions and \(\zeta(-5)\). |
| P001093 | Novikov’s closed-form action and monopole; tentative Witten/chiral-field aside. |
| P001094 | Target-chart covering; physical phase; Semenov heading; Drinfeld issue “5”; unhalved bracket and factorization. |
| P001095 | Modified equation; \(R\pm1\); double and hierarchy; no skew restriction in Gelfand’s \(sl_2\) query. |
| P001096 | Wodzicki/Fedosov boundary; APS projection; unsquared cutoff partition versus squared matrix entries. |
| P001097 | Incomplete/full projectors; \(a=f_1\sigma\); Todd conventions; overwritten zero. cutoff1097b.png is useful; first crop cutoff1097.png was inadequate. |
| P001098 | Local index; formal cohomology; boundary signature operator; APS I–III; coefficient K-groups. |
| P001099 | Continuous loops; Fredholm/compact projections; “unsolved” criterion; dense Krichever locus. |
| P001100 | Miura flag; central extension; Krichever zero-curvature operators and tau sign. |
| P001101 | Full Grassmannian/index-zero annotation; components and admissible frames. Reinspected in final pass. |
| P001102 | Block determinant; transversality; tau normalization/nonvanishing; charge-zero sets. |
| P001103 | Schur/Plücker; GL(n) query; curve/sheaf/disc; index \(\chi(\mathcal L)-1\). |
| P001104 | Čech diagram; theta factorization; broad abelian-variety programme; Baker uniqueness/meromorphic qualification. |
| P001105 | Miwa shifts; vertex operator; positive-part notation; finite poles; missing factor 2. |
| P001106 | Frame bundle \(\mathcal P\), changes \(\mathcal T\), pairs \(\mathcal E\) are distinct. |
| P001107 | Miura factor order; analytic cell/meromorphic flags; Galois analogy. |
| P001108 | April 11/Wilson; short conclusion; \(2q_1\); upper region blank. |
| P001109 | Ginzburg; cited authors; volume/Pfaffian shorthand; polynomial versus piecewise polynomial. |
| P001110 | Borel double fibration; localization; circle coefficient ring and degree. |
| P001111 | Extra \(u\) in \(d_1^2\); correction to invariant forms; parity grading; group-free query. |
| P001112 | Successful repair \(\beta=\alpha(1+d\alpha)^{-1}\); correct contracting identity. |
| P001113 | April 18; Levinson plan; Ginzburg/Beilinson boundary; Hamiltonian insertion; convexity credit; good reduction at every prime. |
| P001114 | Local exponential and \(1/n\) absent; zero variable; global questions; Wodzicki interruption; Beilinson completion. |
| P001115 | September 5, 1983, Deligne: excluded. |

## Research decisions and scope controls

### Finite gap theory and spectral zeta

Krichever’s 1983 paper exactly matches the Hessian and first-order gap basis. Submission preceded the talk, but submission is not public circulation: matching new results remain A. Stationary hierarchy and quasimomentum are E. Higher variations are F because the requested spectral coordinates or target identity are unspecified; ordinary derivatives do not justify inventing an open conjecture. The printed mode is a theta quotient with doubled Abel shifts, not the notebook’s single-theta logarithm; the genus-zero limit confirms a real difference.

Wodzicki’s 1984 paper explicitly records a Manin seminar presentation in November 1982. The universal-polynomial theorem matches, but ambiguous notebook factorial conventions are not certified. The determinant-derivative identity gives an exact computational formulation. Lamé’s reflected spectral coordinate explains the opposite cubic signs. The full Clausen expression was not found there; only the free specialization and definition are verified. The arithmetic query and D-module extension diagram lack sufficient data for definite later problems.

The multiplicative-anomaly formula is restricted to **commuting, positive, invertible, classical elliptic self-adjoint operators**, positive real orders, same bundle, closed manifold. The primary 2015 paper states these assumptions; Kontsevich–Vishik covers admissibility and cuts. Logarithms of positive-order operators have logarithmic symbol terms; \(b\log A-a\log B\) cancels the leading log term and is classical of order zero. No arbitrary product is assumed cut-admissible.

### Classical r-matrices

Semenov-Tian-Shansky’s paper was received 15 April 1983 and revised 16 May, after the March lecture. The unhalved bracket requires \(2t\). Local factorization and common-quotient compatibility do not imply global decomposition. The quadratic theorem needs associative multiplication, invariant nondegenerate trace pairing and skew \(R\) satisfying the modified equation.

The \(sl_2\) question concerns all operators, without skewness. Gubarev–Kozlov Proposition 2.5 supplies weight-one Rota–Baxter normal forms via \(R=2B+I\). Conjugacy, the involution \(B\mapsto-I-B\), and trivial cases are retained. The code verifies solutions and conventions, not completeness. Drinfeld’s separate pointer is Doklady 268(2), 285–287, received June 4, 1982; issue 5 is wrong. His compatible dual bracket/cobracket is distinct from a bare double Lie algebra.

### Index theory, loops and KP

APS retains the kernel term and product collar. Eta regularity reuses GP-1981-43: APS III gives odd dimension; Gilkey 1981 gives all dimensions. Global regularity does not imply pointwise zero local residue. GP-1981-44 is E: Seeley’s 1968 translated preprint already gives non-self-adjoint calculus under a principal-symbol ray condition. Excluding discrete global spectrum near the imaginary axis does not specify a complete boundary problem.

Fedosov’s orthogonal block needs \(f_1^2+f_2^2=1\) and unitary normalization. His later pair is algebraically idempotent even for arbitrary auxiliary maps. The literal \(a=f_1\sigma\) issue concerns support of the difference, **not idempotence**. The ambiguous subscript is not declared an OCR error.

The loop reconstruction is only for essentially bounded **unitary** matrix loops. For a unitary block multiplier \(U=(a,b;c,d)\), compact \(c\) gives \(a^*a=1\) in the Calkin algebra; Fredholm \(a\) is invertible there, so \(aa^*=1\), hence \(bb^*=0\) and \(b\) compact. Conversely compact \(b,c\) make \(a\) essentially unitary. Hartman then yields entries in \(QC=(H^\infty+C)\cap\overline{H^\infty+C}\). This marked own deduction is not a novelty claim or a solution for all unspecified GL-valued loops.

Segal–Wilson results were checked individually. Continuous based unitary loops are dense, not all of the completed loop Grassmannian. Frames and determinants use index zero. Proposition 6.1 gives \(\chi(\mathcal L)-1\) in the printed polarization. Theta comparison is **Theorem 9.11**. Finite-pole Fuchs bounds do not address infinity. Miura flags are local; periodic global factors need monodromy conditions. The all-abelian-variety programme and differential-Galois diagram remain F.

### Localization and arithmetic status, November 2026

Duistermaat–Heckman is 1982 background. Atiyah–Bott appeared in 1984, but was received December 1982 and cites 1982 Berline–Vergne and DH-addendum preprints. Nonisolated fixed components need the full equivariant Euler class. Reduced **cohomology classes** vary affinely; densities are polynomial **on chambers**. Convexity needs a compact connected Hamiltonian torus manifold. Credit is Atiyah and Guillemin–Sternberg; the notebook conflates this with Atiyah–Bott localization. The April report is related to Ginzburg’s autumn representation/microlocal line, but not the same questions as 568 or 570.

P001112 repairs its own failed angular-form requirement. Independently, \(D\alpha=1+d\alpha\), \(D(d\alpha)=0\), so \(D\beta=1\); the parity Leibniz rule gives the contracting identity. This check is marked in the item. No new localization theorem is claimed.

Beilinson’s heading records no BSD rank equality, leading coefficient, regulator determinant or specified special value. Continuation (GP-1982-42) and actual automorphy (GP-1982-43) are distinct. The local factor needs the exponential and \(1/n\); a smooth model exists outside finitely many primes. Finite-field purity does not prove the global assertion. The elliptic completion needs \(L(H^1(E),s)\), conductor \(N^{s/2}\) and root number.

The current result was checked in **BCGP 2021 itself**. Theorem 1.1.2 gives meromorphic continuation/functional equation for every genus-two curve or abelian surface over a totally real field; 1.1.3 gives potential automorphy. Page 157 explicitly denies control of poles over the original field. Preprint end of 2018; IHES publication 2021. The 2025 Theorem B proves actual modularity for a **smooth genus-two curve \(y^2=f(x)\) over Q, degree 5, surjective mod-3 GSp4 image, good ordinary reduction of the curve at 2 and 3**. It is not universal modularity of abelian surfaces. Gee’s 2026 ICM article is the primary current account; **Remark 2.7**, not section 2.7, gives chronology.

Shintani’s totally real cone method is verified through Cassou-Noguès’s primary 1981 report, published 1982. It does not verify an ordinary elliptic torus-operator realization. The original 1976 paper was not obtained; NII returned a robot page and is not counted as original-paper verification. An AIF 1981 metadata record names “Philippe” while its scan says “Pierrette”; that entry was not imported. The cited 1982 primary PDF clearly identifies Pierrette.

## Search audit and unresolved identifications

Adaptive searches used MathNet, Numdam, author PDFs, publisher sites and arXiv. The following are actual query families, not claims of exhaustive searches.

| Item | Query family / result sought | Outcome |
|---|---|---|
| 586 | Krichever Hessians, finite-gap perturbation, third/higher variations | Exact 1983 paper; no exact higher-variation spectral-coordinate theorem identified. |
| 587 | Wodzicki Hill finite-zone positive zeta, Lamé, Clausen negative derivatives | Exact 1984 theorem; no full branch-sensitive Clausen match. |
| 587 determinant | Multiplicative anomaly, Wodzicki formula, KV cuts | Exact commuting formula and admissibility verified. |
| 588 | Novikov many-valued Morse, Dirac map-space actions | Exact 1982 survey; chiral-field aside remains tentative. |
| 589 | Semenov classical r-matrix, sl2 modified equation, weight-one Rota–Baxter | Exact exposition and unrestricted operator classification; skew-tensor-only results rejected as substitutes. |
| 590 | APS no-filling eta, Gilkey residue, cuts, Seeley powers | Exact pre-talk sources; metadata limits explicit. Formal combined cohomology remains underspecified. |
| 591–592 | Segal Wilson KdV, compact Hankel QC, Miura flags, abelian theta, Shiota | Exact construction; precise unitary-loop reconstruction; Shiota metadata only and thematic. |
| 593–596 | DH localization, Atiyah Bott Cartan, Vergne primitive, convexity | Full contemporary localization paper and original convexity theorem. DH author metadata; theorem checked in AB. |
| 595 | Hasse–Weil curves current 2026, genus-two potential modularity, 2025 abelian surfaces, Gee ICM | Original 2021/2025 theorem statements plus 2026 account; no blanket holomorphy. |
| 598 | Shintani Dedekind torus constant coefficients pseudodifferential, negative integers | Exact cone arithmetic scope; no exact ordinary elliptic operator theorem. |

No D label is assigned merely because a search failed. F means the proposition or intended version is not identifiable. Both C items specify what remains open.

## Earlier-year matching

Exact GP reuse: **GP-1981-43**, global eta without a filling; **GP-1981-44**, removal of self-adjointness. Earlier 1981-559 occurrences are retained. Repeated APS/local-index background links to 1981-558.1–4, 558.7–8, 558.11–12 and 559.2, 559.10–11. Convexity links to 1981-556.12 and 1980-508.15. Theta background links to 1977-431.3; brackets to 1977-426.5/426.10 without reusing the different first-bracket Jacobi problem. Beilinson 1979-476.11 is thematic only. The supplied index contains no exact prior GP for the four new questions 40–43.

## Independent checks and limits

independent_checks.py passed exact SymPy identities and 60-digit mpmath comparisons: Euler–Lagrange derivatives; Hermitian 2x2 discriminant; orthogonal projector normalization; both noncommutative idempotents and bad-cutoff limit; sl2 representatives/involutions; free-circle zeta derivative at periods 1, 2π, 7/3; second-order Miura factor order. It does not prove classification completeness, the full spectral expansion or any arithmetic conjecture. The Calkin and Vergne checks above are separate short proofs. Own computations and deductions are marked in item text.

validate_shard.py and validation_report.json additionally check fields, enums, source order, consecutive IDs, citation/refs consistency, raw LaTeX math delimiters and an explicit correction-row map for every item marked false as written. All pass. A separate second-reader review of the root four-unitary development is in development_review.md, with an independent character calculation and isolated rerun of the root checker. Its coefficients and local-theorem application pass; no shared parent output was edited.

## Per-reference opened-source audit

Every key below has a real URL opened in this run. Metadata checking is not promoted to reading a result. Where an original was unread, the mathematical source is identified separately. source_audit.json is the structured equivalent.

'''
lines=[intro]
for key in sorted(sources):
 a=sources[key]
 lines.append(f"### {key}\n\n- Opened: {a['opened_url']}\n- Verification: **{a['verification']}**.\n- Locator and scope: {a['locator_and_scope']}\n\n")
counts=dict(collections.Counter(x['class'] for x in items))
lines.append('## Structured counts\n\n'+json.dumps({'talks':len(talks),'items':len(items),'problems':len(problems),'classes':counts,'references':len(sources)},indent=2)+'\n')
(D/'research_notes.md').write_text(''.join(lines))
print('Audit written:',len(''.join(lines).split()),'words')
