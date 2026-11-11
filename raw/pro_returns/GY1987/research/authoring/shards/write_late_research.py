from pathlib import Path
import ast, json

P=Path(__file__).parent
tree=ast.parse((P/'write_late_references.py').read_text())
entries=[]
for node in tree.body:
    if isinstance(node,ast.Expr) and isinstance(node.value,ast.Call) and isinstance(node.value.func,ast.Name) and node.value.func.id=='add':
        c=node.value
        entries.append((ast.literal_eval(c.args[1]),{x.arg:ast.literal_eval(x.value) for x in c.keywords}))
web={
'happel1987derived':'turn152view0; original scan read via local OCR primary/happelpage2.txt, happelpage7.txt, happelpage21.txt',
'appelhakenkoch1977reducibility':'turn110view3; local late_crossref.json; web API open turn141view1 failed but direct retrieval succeeded',
'atiyah1988invariants':'turn13view0, turn85view1, turn87view0, turn87view2',
'beilinson1978coherent':'turn108view0',
'beilinson1987glue':'turn108view1',
'beltrami1869interpretation':'turn46view2',
'berezingelfand1956spherical':'turn108view2',
'bernhart1977digest':'turn76view0',
'bernsteingelfandponomarev1973coxeter':'turn24view3',
'clay2026riemann':'turn41view1, turn69view3',
'drinfeld1987quantum':'turn122view0, turn123view0, turn139view0; Russian publication metadata turn121view0',
'duistermaat1974morse':'turn73view1',
'floer1988instanton':'turn50view5',
'gelfandmacphersonvilonen2005microlocal':'turn13view1, turn13view2, turn17view6; parent independently reopened full text',
'gonthier2005fourcolour':'turn51view1, turn73view3, turn76view2, turn119view2, turn139view1',
'goreskymacpherson1983intersection':'turn110view0',
'gorodentsevrudakov1987exceptional':'turn51view2',
'guminov2025perverse':'turn41view0, turn116view0',
'hall1935representatives':'direct primary PDF retrieval and local read primary/hall1935.txt; local late_crossref.json',
'hatcher2002algebraic':'turn110view2; parent independent Chapter 2 read',
'kashiwara1980constructible':'turn69view2',
'kashiwara1984riemann':'turn110view1',
'kashiwaraschapira1985microlocal':'direct primary PDF retrieval and local read primary/kashiwaraschapira1985.txt; web reader exceeded size limit',
'kashiwaravilonen2014codimension':'turn17view0, turn36view3, turn73view2, turn117view1, turn118view0, turn118view1; parent read published Problem 9.3 p. 617',
'lindemann1882pi':'turn119view0; full-proof lead unresolved',
'nist2026dlmf':'turn85view0 (5.18), turn86view0 (14.30), turn86view1 (23.10)',
'oxleybriefly':'turn108view3',
'parthasarathy1988tstructures':'turn5view0 initial successful full-text read; repeat opens turn116view1 and turn117view0 returned 403; search turn118search5 reconfirmed metadata',
'rado1942independence':'local late_crossref.json from direct Crossref retrieval; web API open turn141view0 unavailable; publisher search turn54search0',
'reshetikhin1987quantizedi':'turn50view1 original scan; turn69view0, turn85view2 typed primary transcription; local rescoveri.png',
'reshetikhin1987quantizedii':'turn50view0 original scan; local rescoverii.png',
'reshetikhinturaev1990ribbon':'turn24view1',
'rudakov1988markov':'turn13view3, turn17view3; local primary/rudakov1988markov.txt',
'rudakov1988quadric':'turn5view1, turn17view2; local primary/rudakov1988quadric.txt',
'stoimenowtanaka2008mutation':'turn69view1',
'ushveridze1989quasiexact':'direct original JINR PDF retrieval; local ushveridze1989.pdf, qes_ocr/*.png, ushveridze1989_ocr.txt',
'wantzel1837constructions':'turn46view1',
'wiles1995modular':'turn46view0',
'witten1982supersymmetry':'turn73view0'
}

preface=r'''# Late-record research and evidence log

**Scope:** records 739–751, academic year 1987–88. **Status date:** 11 November 2026. Russian transcription is authoritative; English is a translation to audit, not an independent source of mathematical hypotheses. This is a bounded literature and source audit, not a claim of exhaustive bibliographic coverage.

## Files and checkpoint

The completed shard contains 13 talk entries, 98 mathematical occurrences, six new problem entries GP-1987-41 through GP-1987-46, 31 correction rows, and 39 bibliography entries. Counts: E 74; A 8; F 7; B 7; C 2; D 0. `late_validation.json` records the mechanical validation. `late_areas.json` maps all occurrence IDs to subject areas. The reproducible builders are `write_late.py`, `write_late_references.py`, and this script. No earlier exact problem ID was reused; earlier quiver, matroid and exceptional-object material is mentioned as context without equating distinct questions.

The two C items are the named Riemann hypothesis and the explicit geometric essential-image problem for microlocal perverse data. The latter is not the solved codimension-three extension conjecture. No underspecified fragment was promoted to a D item or to a definite new open problem.

## Actual source boundaries

| Record | Actual pages | Boundary reason |
|---|---|---|
| 739 | P001444–P001445 | P001442–P001443 continue Radul. Local Kapranov heading has no date; catalogue supplies 21 March 1988. |
| 740 | P001446–upper P001447 | Zelevinsky, matroidal transversals. |
| 741 | lower P001447 | Gelfand's five historical examples. |
| 742 | upper P001448 | Rudakov, exceptional bundles and Markov data. |
| 743 | lower P001448–upper P001449 | Gelfand's representation/mutation discussion. |
| 744 | lower P001449–P001452 | S. Gelfand's microlocal/perverse account. |
| 745 | P001453–upper P001457 | Fuchs four-colour report. |
| 746 | lower P001457–P001459 | Microlocal/perverse continuation. |
| 747 | upper P001461 | Beilinson on strongly indefinite Morse theory. P001460 is a Bourbaki reading list, contextual only. |
| 748 | middle P001461 | Gelfand's circle polarization remark. |
| 749 | lower P001461–P001467 | Reshetikhin quantum groups and links. |
| 750 | P001468–upper P001472 | Ushveridze Riccati/quasi-exact solvability. |
| 751 | lower P001472–P001477 | Beilinson, Atiyah and gauge theory. |

P001478 explicitly begins a session dated 12 September 1988; P001479 continues with G. Moore. Parent independently inspected both scans. They are excluded from this academic year's mathematical inventory, with a provenance correction retained.

## Scan and formula checks

Russian/English source segments were compared throughout. Selected scans were viewed where symbols or diagrams matter, including P001449 mutation order, P001450 zero-section insertion, P001455 Birkhoff diamond, P001462 coproduct/antipode, P001463 R-series and coproduct order, P001467 framing correction, P001468 kernel identities and root equations, and P001471–P001472 electrostatics/Morse boundary. Parent independently viewed P001475 and P001478–P001479. The P001465 crossing-label correction follows the immediately preceding definition and the transcribed displayed formula; it is not described as a fresh independent scan inspection.

The P001455 configuration is the Birkhoff diamond: the ring and four internal vertices identify the classical reducible configuration. Fuchs's failure to reproduce its proof is not a statement that it remains an open problem. The numbered parallel-computer question is a definite implementation question, not a new four-colour conjecture; finite reducibility tests are established, while no unique machine architecture or performance target is specified.

## Search routes and exact scope

Searches used author/title/formula combinations, then opened the primary paper or official bibliographic record. Representative queries included Parthasarathy t-structures quivers 1988; Rudakov Markov exceptional bundles/quadric; Gelfand MacPherson Vilonen microlocal perverse sheaves; Kashiwara Vilonen codimension two essential image; Fuchs Birkhoff diamond Appel Haken reducibility; Reshetikhin 1987 preprint Yang–Baxter invariants links; Ushveridze Riccati electrostatic quasi-exactly solvable 1988/1989; and Atiyah 1987/1988 new invariants Floer.

For the final current-status check, searches for `"Kashiwara" "Vilonen" "Problem 9.3" perverse codimension two` and `"microlocal perverse sheaves" "codimension two" conditions essential image` with a two-year recency filter located the original paper, special-case descriptions, and Vilonen's institutional research page. The latter search excerpt says the problem reduces to codimension-two interactions, but both web OPEN and direct retrieval returned HTTP 502, so it is retained only as an unverified lead and is not a cited authority. Search timestamps are not publication dates: an old Braden paper was indexed as recent and was not treated as a new result. The directly opened 2025 Guminov article supplies a recent, explicitly restricted family, not a uniform solution.

The official Clay page was opened and still says the Riemann hypothesis is unsolved. No seminar-specific partial proof or bounded new project is present. The seven F items are the unexplained three-versus-four distinction (739.6), missing quadric numerical converse (742.6), geometric configuration fragment (744.1), unspecified replacement of the circle (748.2), unspecified meaning of SL2 invariants 'sufficing' (749.15), unrestricted kernel classification (750.4), and two bare nonlinear-Schrodinger/oscillator analogies (750.9). Each is explicitly restricted rather than silently completed into a research claim.

## Mathematical decisions and independent checks

1. **Quivers:** source/sink reflection gives derived equivalences, and finite trees allow passage between orientations. The general statement for arbitrary graph orientations is not inferred from the sketch. Parthasarathy's exact results concern finite acyclic quivers over an algebraically closed field, specified t-structures and a Dynkin completeness theorem.
2. **Exceptional objects:** positive ranks are required in the Markov equation. The notebook does not state the Markov uniqueness conjecture. The missing quadric numerical system is kept unidentified even though Rudakov's precise constructibility theorems were found. The claimed kernel mutation pair `(F,R)` is disproved by the evaluation map O^2→O(1) on P1: R=O(-1), and Hom(R,F) is nonzero. Correct pair order is `(R,E)` under the exact-sequence hypotheses.
3. **Open orbit:** simultaneous conjugation of matrix pairs has nonconstant invariant tr(A), so an orbit cannot be dense in the full affine parameter space. This refutes the unrestricted open-orbit slogan without claiming every wild stratum lacks rigid objects. The calculation was independently re-derived by the parent and marked `\ours`.
4. **Microlocal sheaves:** microsupport contains the zero covectors over support, not the whole zero section for every nonzero sheaf. Involutivity alone gives coisotropy and needs pure half-dimension to imply Lagrangian. Arbitrary compatible stratifications are not recovered uniquely. Test-function Hessians carry Maslov/orientation data. The exact perverse criterion in KS1985 is Theorem 9.5.2, printed pp. 171–172, not Chapter 10. GMV Theorems 5.1/6.4 and KV Theorem 1.1 do not give the codimension-two essential image; KV Problem 9.3, published p. 617, explicitly asks for it. Complex coefficients and a complex manifold are specified.
5. **Quantum formulas:** with L=q^(H/4), the printed coproduct forces S(X)=-LXL^(-1). The notebook misses the minus sign and doubles the exponent. K=q^(H/2) changes the commutator denominator to q^(1/2)-q^(-1/2) unless generators/parameter are rescaled. Both printed R-coproduct orders are reversed for the stated intertwining convention. Drinfeld §10 and Reshetikhin I Theorem 1.3 confirm the corrected order. The R-series must have nilpotent coefficients vanishing to the appropriate h order; no unique missing q exponent is guessed. Parent independently checked the antipode sign/exponent. Framing corrections use each colour's twist and signed self-writhe.
6. **Riccati residues:** for the rational kernel and distinct roots avoiding fixed poles, all double poles cancel. Root residues give sum_{j≠i}1/(lambda_i-lambda_j)+sum_alpha b_alpha/(lambda_i-a_alpha)=0, and fixed-pole residues give c_alpha=2b_alpha sum_i1/(lambda_i-a_alpha). The proper rational residual is then zero. Parent independently re-derived this exact specialization.
7. **Addition identity:** omega cot(omega z) requires Omega=-omega^2/3 in the notebook's plus-Omega convention. The Weierstrass example requires Omega=(zeta^2-wp)/2. Parent independently checked both. A simple pole of residue one and the regularity of Omega at zero are needed for the normalized Riccati limit. An unrestricted classification of all kernels is not inferred.
8. **Liouville calculation:** x'=A^(-1/2), P=2B sqrt(A)-A'/(2 sqrt(A)), Psi=A^(-1/4)exp(integral B)f, and V=P_x/2+P^2/4-AC. Parent independently re-derived the formula. For rational A a product of N linear factors, AC has degree at most N-2; only N=2 gives a single constant without fixing further coefficients.
9. **Electrostatics:** the repulsive minimum argument uses negative logarithms. For two ordered real fixed points, positive b1,b2 and integer M≥0, convexity gives the Jacobi configuration with eigenvalue M(M-1+2b1+2b2) and weight (lambda-a1)^(2b1-1)(a2-lambda)^(2b2-1). The exterior bound is sufficient, not generally necessary: M=1, a1=0, a2=1, b1=-1, b2=1/2 gives U=log(lambda)-(1/2)log(lambda-1), a strict minimum at 2 while b1+b2+M=1/2. Parent independently checked the example. It does not refute sufficiency. Ushveridze p. 1212 explicitly distinguishes classical and quantum thresholds.
10. **Gauge theory:** ordinary integral first homology is not equivalent to twisted first cohomology vanishing. Parent's development subsection `dev:twisted-h1` proves both failures: RP3 has vanishing H1 for all finite-dimensional real/complex local systems by finite-group averaging, yet integral H1=Z/2. For the connected sum of two Poincare spheres, the representation obtained from the binary icosahedral inclusion on both free factors is irreducible and has H1(ad rho) of real dimension three. I independently audited the group-cocycle and twisted Mayer–Vietoris computations and triviality of SU2 bundles over a 3-dimensional CW complex. The relation matrix rows are (5,-3),(-2,1), determinant -1. These are annotations/corrections, not a claimed new C/D development.

New calculations and counterexamples in the shard carry `\ours` or `\oursComputed` in reconstruction fields; these mark work performed here, not mathematical novelty. The parent owns the full formal development and its computational verification output.

## Chronology safeguards

- Parthasarathy: received 15 February 1988, revised 13 May, publication December 1988; the talk reports his work rather than claiming Kapranov's priority. Item 739.3 is B for the precise later t-structure-data realization refinement. Happel 1987 Theorem 5.12 already establishes the Dynkin/iterated-tilted endpoint, announced at Ottawa 1984; receipt of Parthasarathy establishes existence, not public pre-talk circulation of his criterion.
- Rudakov Markov: received April 1986, Russian publication 1988, English translation 1989. Quadric: received 6 July 1986, Russian issue 4 of 1988, English translation 1989.
- GMV: arXiv September 2005; this does not erase the notebook's 1988 report of the programme. KV: 2010 announcement, 2012 full preprint, 2014 publication.
- Reshetikhin scans: E-4-87 and E-17-87, with 1988 imprints. II explicitly records recommendation 6 June 1987. The exact public-circulation day is unestablished. Stable keys retain 1987, but BibTeX year follows the imprint. Drinfeld's 1986 lecture/1987 paper independently anchors the established core quantum-group material.
- Ushveridze: 1989 review cites 1988 FIAN announcements. No claim that 1989 was the first announcement is made.
- Atiyah: a 1987 preprint/lecture is documented separately from the 1988 publication; Floer's instanton paper was received 3 May and published June 1988.

## Opened-source register

`verified` in BibTeX means the named record or text was opened; the scope below and each item's verification field distinguish metadata, a result read, and an indirect match. A successful direct PDF download followed by a local text/image read is recorded as such. Failed web-reader attempts are not disguised as successful full-text reading. The source-reference IDs below are retrieval locators for the parent, not substitutes for URLs.

'''

lines=[preface]
for key,f in entries:
    lines.append(f"### {key}\n\n**{f['title']}**\n\nURL: {f['url']}\n\nEvidence: {f['annote']}\n\nRetrieval locators: {web.get(key,'See local source read.')}.\n\n")
lines.append(r'''## Validation and access limits

The data validation checked consecutive item numbering in each of the thirteen records; all problem occurrences resolve; all C/D items have worth statements; all LaTeX citation keys are listed in refs; all 39 referenced keys exist in the 39-entry bibliography; no unused bibliography entries or control characters remain. Every reused bibliography entry was rewritten with this shard's actual opening/reading scope rather than inheriting prior verification prose. A Python escape issue that produced TAB followed by `extquotesingle` is normalized in the builder before saving, so it cannot recur on rebuild.

The original Rado proof, the complete Gorodentsev–Rudakov Duke article, and the full Lindemann proof were not successfully read. Their metadata records are identified honestly. Goresky–MacPherson's original PDF opened but text extraction was unavailable; no exact proof-reading claim is made. These limits do not turn established classical statements into D items. LaTeX compilation and integration are owned by the parent, whose build environment initially lacked its TeX macro tree.
''')
(P/'late_research.md').write_text(''.join(lines))
print('Wrote late_research.md')
