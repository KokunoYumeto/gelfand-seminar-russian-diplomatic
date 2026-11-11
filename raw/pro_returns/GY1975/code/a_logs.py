"""Reproducible inspection and source ledger for records 363--374."""
import csv
import json
import re
from collections import Counter
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
OUT = BASE / "fragments"
CHECKED = "2026-11-10"
items = json.loads((OUT / "a_items.json").read_text())
talks = json.loads((OUT / "a_talks.json").read_text())
problems = json.loads((OUT / "a_problems.json").read_text())
sources = []

def source(key, verification, urls, refs, locators, scope, chronology="", limitations=""):
    sources.append(dict(
        key=key, verification=verification, opened_urls=urls,
        source_result_refs=refs, read_locators=locators, scope=scope,
        chronology=chronology, limitations=limitations, checked_on=CHECKED,
        occurrences=[x["id"] for x in items if key in x["refs"]],
        problems=[x["id"] for x in problems if key in x["refs"]]))

source("browndouglasfillmore1973unitary", "publisher metadata checked",
 ["https://link.springer.com/chapter/10.1007/BFb0058917"],
 ["turn10view5"], ["LNM 345 (1973), pp. 58--128; publisher record"],
 "The pre-talk BDF classification and extension-theory setting.",
 "Conference April 1973; collected publication October 1973.",
 "The full theorem and proof were not read in this run. The notebook-to-publication identification is partial.")
source("browndouglasfillmore1977extensions", "publisher metadata checked",
 ["https://annals.math.princeton.edu/1977/105-2/p03"],
 ["turn10view6"], ["Annals 105(2), pp. 265--324; publisher record"],
 "Later systematic BDF extension theory and the K-homology connection.",
 "Journal publication 1977.",
 "The stable compact-metrizable formulation is a modern reconstruction; metadata do not independently verify every hypothesis.")
source("macdonald1972affine", "publisher metadata checked",
 ["https://www.mathnet.ru/eng/mat648"],
 ["turn10view4"], ["Russian translation record, Matematika 16(4), pp. 3--49; original Inventiones 15 (1972), pp. 91--143"],
 "The affine-root denominator-identity background for Euler-product powers.",
 "Original publication 1972.",
 "The original proof was not read; the more specific Dyson identity was checked separately in full text.")
source("dyson1972missed", "read the result",
 ["https://www.marktomforde.com/academic/miscellaneous/images/Missed-Opportunities-Dyson.pdf"],
 ["turn57view1"], ["Section 2, pp. 636--638, equations (1)--(3)"],
 "The five-integer formula and its modular/root-system context.",
 "Lecture 17 January 1972; Bulletin AMS publication September 1972.",
 "No priority claim beyond the source's dated account.")
source("nist2026beta", "read the result",
 ["https://dlmf.nist.gov/5.12"], ["turn44view3"], ["Equations 5.12.1 and 5.12.4"],
 "Euler beta integrals and the Gamma-factor normalization in Feynman parametrization.",
 "Online reference accessed 10 November 2026.",
 "Used to check the scalar identity, not to prove convergence of a quantum-field integral.")
source("nist2026dlmf", "read the result",
 ["https://dlmf.nist.gov/27.14"], ["turn52view1"],
 ["Equations 27.14.3--5, 27.14.8--11, 27.14.12--14"],
 "Pentagonal numbers, partition recurrence, Hardy--Ramanujan--Rademacher normalization, and eta.",
 "Online reference accessed 10 November 2026.",
 "Reused the cumulative bibliography's broad DLMF key; no later-in-November version is asserted.")
source("manin1973periods", "indirect",
 ["https://www.mathnet.ru/eng/sm3354",
  "https://www.mathnet.ru/php/getFT.phtml?jrnid=sm&option_lang=eng&paperid=3354&what=fullteng"],
 ["turn28view0", "turn89view4", "turn99view0", "turn100view0"],
 ["Section 1.3, English pp. 373--374; metadata"],
 "Period-polynomial formulas for tau and the boundary half-weight in the summation region.",
 "Russian original 1973; English journal volume is 1973 with a 1975 translation copyright. Receipt information differs between extracted records and is not used to infer circulation.",
 "The full English PDF was opened and the summation discussion read, but OCR did not securely recover the printed polynomial. The repaired factorization was independently checked only for 1<=n<=50; it is not presented as a newly proved all-n identity.")
source("brouwerleech", "read the result",
 ["https://aeb.win.tue.nl/2WF02/Leech.pdf"], ["turn91view0"],
 ["Theorems 1.1--1.3; Section 3"],
 "Even unimodular theta series, Leech lattice, and the weight-12 basis/normalization.",
 "Undated author notes; access 10 November 2026.",
 "Used for the structural facts and normalization; a proof of the full Niemeier classification is unnecessary and not claimed to have been checked.")
source("novikov1974periodic", "read the result",
 ["https://www.mathnet.ru/eng/faa2358",
  "https://www.mathnet.ru/php/getFT.phtml?jrnid=faa&option_lang=eng&paperid=2358&what=fullt"],
 ["turn147view0", "turn147view1", "turn148view0", "turn149view0"],
 ["Russian Section 2, Theorem 2.1, pp. 59--60; n=1 example p. 63"],
 "Stationarity implies finite-gap behavior, including the one-gap periodic case.",
 "Received 18 February 1974; published 1974.",
 "The source's own attribution to Ince is retained as historical context rather than an independently read Ince proof.")
source("vey1975deformation", "publisher metadata checked",
 ["https://eudml.org/doc/139633"], ["turn32view2"],
 ["Commentarii Mathematici Helvetici 50 (1975), pp. 421--454; bibliographic record"],
 "The named publication behind the Vey deformation report.",
 "Published 1975; month not verified. The notebook itself reports an existing theorem.",
 "The exact H^3 obstruction statement was not read in the original. Later general existence does not verify every detail of the 1975 formulation.")
source("kirillov1976local", "publisher metadata checked",
 ["https://www.mathnet.ru/eng/rm3760"], ["turn52view0"],
 ["Publisher abstract and metadata"],
 "Local Lie algebras and the differential/locality hypotheses missing from the notebook's broad wording.",
 "Received 25 November 1975; published 1976.",
 "The abstract gives a close subsequent match, not a verified exact formulation or proof.")
source("emmrichweinstein1993differential", "read the result",
 ["https://arxiv.org/pdf/hep-th/9311094"], ["turn69view0", "turn82view3"],
 ["Sections 1--2"],
 "The local Weyl/Moyal product and general symplectic deformation construction.",
 "Preprint dated November 1993; the opened version header is 19 November 1993.",
 "A generated-PDF timestamp is not treated as the date of circulation. This later exposition is used for a concise mathematical check, not for 1975 priority.")
source("kostant2003euler", "read the result",
 ["https://arxiv.org/abs/math/0309232", "https://arxiv.org/pdf/math/0309232"],
 ["turn1view1", "turn18view5"], ["Introduction; Theorems 0.1 and 2.1"],
 "Character/Casimir Euler-product identity and restatement of Kostant's original 1976 theorem.",
 "First arXiv submission 14 September 2003; source explicitly refers back to its 1976 Theorem 3.1.",
 "The original 1976 paper was not independently opened. The spectral-zeta shorthand and unspecified complex-exponent question are only thematic matches.")
source("gelfanddikii1976fractional", "read the result",
 ["https://www.mathnet.ru/eng/faa2188",
  "https://www.mathnet.ru/php/getFT.phtml?jrnid=faa&option_lang=eng&paperid=2188&what=fullt"],
 ["turn10view1", "turn18view6"], ["Sections 8--12; Section 10, equation (24)"],
 "Differential polynomials, evolutionary derivations, and formal fractional operators.",
 "Received 22 June 1976; published 1976.",
 "The pre-existing formal KdV hierarchy is classified E at 373.1; this later paper is not used to make the hierarchy a new 1975 theorem.")
source("tong2006qft", "read the result",
 ["https://davidtong.org/teaching/quantum-field-theory/",
  "https://davidtong.org/pdfs/teaching/quantum-field-theory/qft.pdf",
  "https://davidtong.org/pdfs/teaching/quantum-field-theory/qft3.pdf",
  "https://davidtong.org/pdfs/teaching/quantum-field-theory/qft4.pdf",
  "https://davidtong.org/pdfs/teaching/quantum-field-theory/qft5.pdf",
  "https://davidtong.org/pdfs/teaching/quantum-field-theory/qft6.pdf"],
 ["turn38view0", "turn38view1", "turn38view2", "turn38view3",
  "turn82view0", "turn82view1", "turn82view2", "turn83view0", "turn83view1",
  "turn83view2", "turn83view3", "turn155view1", "turn156view0", "turn157view0"],
 ["Section 3.3; Sections 4.1--4.4; Section 5.5; Sections 6.1, 6.3.1, and 6.5; full-PDF title page"],
 "Checks of spinors, Dirac and Maxwell conventions, Wick expansion, propagators, gauge coupling, and diagrams.",
 "Title page: Michaelmas terms 2006 and 2007.",
 "This is later verification of standard material. Wick expansion does not establish an infinite-dimensional Lebesgue measure or the unresolved constrained path-integral formula.")
source("weinberg1967leptons", "read the result",
 ["https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.19.1264",
  "https://journals.aps.org/prl/pdf/10.1103/PhysRevLett.19.1264"],
 ["turn46view3", "turn73view0"], ["Equations (1)--(4), (8), (10)--(16)"],
 "The lepton doublet/singlet, hypercharge, Higgs, and neutral-field mixing model.",
 "Received 17 October 1967; published 20 November 1967.",
 "A bare neutral rotation in the notebook is not equated with the complete electroweak construction.")
source("grosswilczek1973ultraviolet", "read the result",
 ["https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.30.1343",
  "https://journals.aps.org/prl/pdf/10.1103/PhysRevLett.30.1343"],
 ["turn46view4", "turn84view0"], ["p. 1344, equations (8)--(9)"],
 "One-loop non-Abelian beta-function sign and its matter dependence.",
 "Published 25 June 1973.",
 "The appended beginning of the Politzer article is a separate work. No claim that every strong-interaction theory is asymptotically free is retained.")
source("fukuda1998oscillation", "publisher metadata checked",
 ["https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.81.1562"],
 ["turn46view5"], ["Publisher abstract and metadata"],
 "Observational neutrino oscillation evidence correcting the historical zero-mass table.",
 "Physical Review Letters 81 (1998), pp. 1562--1567.",
 "Abstract-level evidence only; no neutrino absolute-mass value or detailed statistical reanalysis is claimed.")
source("deligne1971modulaires", "read the result",
 ["https://www.numdam.org/item/SB_1968-1969__11__139_0.pdf"],
 ["turn46view1", "turn102view2"], ["Sections 3--5; Theorems 4.9 and 5.6"],
 "The two-dimensional l-adic modular-form representation and the conditional weight bound.",
 "Bourbaki talk February 1969; collected publication 1971.",
 "The representation target is GL_2, not SL_2. Purity is completed by the separately checked 1974 theorem.")
source("deligne1974weil", "read the result",
 ["https://www.numdam.org/item/PMIHES_1974__43__273_0/",
  "https://www.numdam.org/item/PMIHES_1974__43__273_0.pdf"],
 ["turn18view4", "turn25view3", "turn102view1", "turn155view2", "turn156view2"],
 ["Introduction; Theorem 1.6"],
 "Purity needed for the tau prime bound, together with Deligne's modular-form construction.",
 "Source describes Cambridge lectures in July 1973; received 20 September 1973; journal publication 28 December 1974.",
 "The tau consequence combines this theorem with the separate 1969/1971 modular-form construction. Receipt is not the sole evidence of public circulation.")
source("milne2017modular", "read the result",
 ["https://www.jmilne.org/math/CourseNotes/MF.pdf"],
 ["turn87view0", "turn89view1", "turn89view2", "turn102view3"],
 ["Proposition 4.16; Corollary 5.20; p. 78"],
 "Ring of level-one modular forms and Hecke recurrences.",
 "Version 1.31, dated 22 March 2017.",
 "The source uses E_2,E_3 for conventional E_4,E_6. Its printed weight-12 coefficient 54600/691 is not adopted; Brouwer and direct normalization give 65520/691.")
source("degosson1990maslov", "read the result",
 ["https://www.numdam.org/articles/10.5802/aif.1223/",
  "https://aif.centre-mersenne.org/item/10.5802/aif.1223.pdf"],
 ["turn66view2", "turn68view1"],
 ["Section 1, equations (1.1)--(1.5); Theorems 1 and 2"],
 "Quadratic metaplectic operators, double-cover phases, and composition/Maslov indices.",
 "Annales de l'Institut Fourier 40(3), 1990. The article explicitly reviews the earlier Weil--Leray framework.",
 "The arbitrary unitary implementer group has U(1) kernel. A double cover requires the additional phase convention.")
source("khastgirsasaki2001liouville", "read the result",
 ["https://arxiv.org/abs/hep-th/0005278",
  "https://arxiv.org/pdf/hep-th/0005278",
  "https://arxiv.org/html/hep-th/0005278v1"],
 ["turn66view0", "turn68view2", "turn68view3", "turn69view1", "turn69view2"],
 ["pp. 3--5; Table I and involution proof"],
 "Liouville integrability for the stated root-system Calogero--Moser scope.",
 "First public preprint 30 May 2000; journal publication 29 January 2001.",
 "Applied only to the stated reduced crystallographic, Weyl-orbit coupling scope and elliptic degenerations. The harmonic confinement case is excluded from this theorem; the notebook's arbitrary nonreduced variants are not automatically covered.")
source("sasaki2006explicit", "read the result",
 ["https://arxiv.org/pdf/hep-th/0510035"],
 ["turn125view0", "turn127view3", "turn129view0", "turn141view0"],
 ["Introduction; Section 2, equations (2.11)--(2.12); Section 3, equations (3.1)--(3.8); Sections 4--5 and 7; reference 6"],
 "Full-initial-matrix solutions, harmonic matrices, and higher commuting particle flows.",
 "Public preprint 2005; journal publication 2006.",
 "The source credits the A-type solution to Olshanetsky--Perelomov 1976. That original was not independently read; 372.11 is A under actual-speaker attribution, with indirect original verification and a partial match.")
source("olshanetskyperelomov1978radial", "read the result",
 ["https://www.mathnet.ru/eng/faa1984",
  "https://www.mathnet.ru/php/getFT.phtml?jrnid=faa&option_lang=eng&paperid=1984&what=fullt"],
 ["turn127view0", "turn129view2", "turn130view2"],
 ["Section 2; Section 3, Lemma 1; Theorems 1--2 and Corollary 1"],
 "Potential families, domains, radial conjugation, and integrability at the group-derived couplings.",
 "Received 16 June 1977; published 1978.",
 "The radial-conjugation identification does not cover arbitrary continuous couplings merely by naming a symmetric space.")
source("coleman1975equivalence", "publisher metadata checked",
 ["https://journals.aps.org/prd/abstract/10.1103/PhysRevD.11.2088"],
 ["turn127view2"], ["Publisher abstract and metadata"],
 "Quantum sine-Gordon/Thirring correspondence in the neutral sector described by the abstract.",
 "Received 6 January 1975; published 15 April 1975.",
 "Full PDF opening returned 401 (turn129view3). No exact coupling formula or proof outside the checked abstract is asserted.")
source("amitsur1958commutative", "read the result",
 ["https://msp.org/pjm/1958/8-1/pjm-v8-n1-p01-p.pdf"],
 ["turn46view2"], ["Theorem 1"],
 "Commutativity and finite-module structure of the centralizer of a positive-order scalar differential operator.",
 "Received 14 November 1957; published March 1958.",
 "The positive-order hypothesis excludes a scalar identity operator. No earliest-priority claim is assigned to the 1975 intervention.")
source("krichever1976zakharov", "read the result",
 ["https://www.mathnet.ru/eng/dan40219",
  "https://www.mathnet.ru/php/getFT.phtml?jrnid=dan&option_lang=eng&paperid=40219&what=fullt"],
 ["turn10view2", "turn18view7"], ["Lemma and operator construction, pp. 291--292"],
 "One-point Baker--Akhiezer existence and the commuting-operator construction.",
 "Received 8 October 1975; presented 24 October 1975; journal publication 1976.",
 "Neither receipt nor presentation is evidence of public availability before the notebook's 20 October talk. Shared key coordinated with the adjoining block.")
source("krichever1977methods", "read the result",
 ["https://www.math.columbia.edu/department/krichever/pdfs/1975-1979/1977-MOAGITTONE0.pdf"],
 ["turn10view0", "turn25view1", "turn147view2", "turn148view1", "turn148view2", "turn149view1"],
 ["Section 1, Lemma 1.1, coefficient formula p. 188, theta formula pp. 189--190; Section 2, Theorems 2.1--2.2"],
 "Rank-one spectral data, initial-jet polynomial relation, operator ring, theta normalization, and converse framework.",
 "Publication 1977; introduction retrospectively names November--December 1975 seminar talks.",
 "The notebook's 20 October date is retained and the discrepancy logged. The exact bare numerical genus criterion is not claimed as verified; rank, full ring, smoothness/singularities and divisor hypotheses remain essential.")
source("cannas2007introduction", "read the result",
 ["https://www.math.ist.utl.pt/~acannas/Books/impa.pdf"],
 ["turn138view0", "turn140view0", "turn140view1", "turn155view0", "turn156view1"],
 ["Section 4.4, Theorem 4.11; Section 4.5; Appendix C.4, pp. 131--134"],
 "Liouville/action-angle regularity, pendulum quadrature, and the regular Legendre transform.",
 "IMPA course February 2002; revision November 2007.",
 "Appendix C.4 treats the regular convex case; it is not a proof of the full singular-constraint algorithm in the notebook.")
source("henon1974integrals", "publisher metadata checked",
 ["https://journals.aps.org/prb/abstract/10.1103/PhysRevB.9.1921"],
 ["turn135view1"], ["Publisher abstract and metadata"],
 "Pre-talk existence of Toda conserved integrals.",
 "Received 13 August 1973; published 15 February 1974.",
 "Full PDF inaccessible (401, turn138view1). Existence of conserved quantities is distinguished from the separate involution question.")
source("kawasaki1976involution", "publisher metadata checked",
 ["https://academic.oup.com/ptp/article/55/5/1668/1925490",
  "https://oup.silverchair-cdn.com/article-minimal/1925490"],
 ["turn135view2"], ["Publisher metadata, title, pp. 1668--1669"],
 "A subsequent publication specifically devoted to involution of the Toda integrals.",
 "Received 8 January 1976; published 1 May 1976.",
 "The proof and earliest-priority chronology were not independently read. The fate is therefore metadata-level verification.")
source("fradkinfradkina1978quantization", "unresolved lead",
 ["https://www.sciencedirect.com/science/article/pii/0370269378901351",
  "https://www.sciencedirect.com/science/article/abs/pii/0370269378901351",
  "https://inspirehep.net/literature/121055",
  "https://inspirehep.net/api/literature/121055",
  "https://doi.org/10.1016/0370-2693(78)90135-1"],
 ["turn129search0", "turn129search1", "turn129search2",
  "turn125view2", "turn130view0", "turn130view1", "turn131view0", "turn135view3", "turn138view2"],
 ["Search-returned publisher abstract and bibliographic metadata only"],
 "A thematic publication lead for systems with Bose/Fermi first- and second-class constraints.",
 "Search metadata: August 1977 report Print-77-0793 and journal publication 2 January 1978. These dates remain search-level evidence.",
 "Opening the publisher returned 403; INSPIRE returned a JavaScript shell, and the API/DOI routes did not expose the article. Listed URLs are opening attempts, not successful full-text verification. BibTeX remains unverified. The exact term A and delta(0) cancellation are not matched to a read result.")

scan_observations = [
 (603, "Kirillov/Vey paragraph, planar bracket, H^3 condition and final pq-qp=t.", "Mixed derivatives are absent in the visible formula; the final line is too short for a definite problem."),
 (604, "Polyakov heading; historical masses and interaction table; Pauli-spinor rotation.", "Neutrino zero masses and numerical interaction strengths are historical claims, not modern exact values."),
 (605, "Lorentz/spinor transformations, covering diagram, chirality and parity.", "Cover direction and spinor hypotheses checked against the handwriting."),
 (606, "Left/right mass term, gamma anticommutator, Lorentz metric, local U(1) phase and coupling.", "Gauge coupling requires a consistently contracted covariant derivative; sign conventions are supplied explicitly."),
 (607, "Gauge transformation, Maxwell term, formal scattering integral, Gaussian/cubic example and Feynman parameter.", "The positive Maxwell sign is visible; the real cubic perturbation is not a convergent integral in general; Gamma/beta normalization is checked separately."),
 (608, "Propagator and diagram kernels, antiparticle and ordering discussion.", "The reconstructed kernel retains convention dependence and identical-fermion antisymmetrization."),
 (609, "Charge-renormalization diagrams and physical/bare charge inequalities.", "Comparison requires a scale/scheme convention; non-Abelian beta-sign claims require the matter-content hypothesis."),
 (610, "BDF statement, Euler/Jacobi/Delta identities, Kostant character sum, spectral-zeta fragment and psi^z question.", "Pentagonal exponent is visibly wrong; spectral and complex-exponent fragments remain underdetermined."),
 (611, "Lepton symmetry transformations and non-Abelian gauge construction.", "The SU(2) sign/representation conventions are checked without silently adding a complete electroweak model."),
 (612, "Charged-current terms, neutral-field mixing, extra gauge field and four-flavor/three-color line.", "Hypercharge/Higgs data are necessary for a complete model; twelve quarks means four historical flavors times three colors."),
 (613, "Manin's opening tau definition, inserted Gelfand/Povzner differential-polynomial discussion, and Manin's numbered formulas.", "Catalogue records 368, 369 and 370 overlap on this page but their mathematical occurrences are distinct."),
 (614, "Dyson/Ramanujan/Manin formulas, partitions and associated modular expressions.", "Coefficient bounds, summation weight, phase, and normalization errors are separated from transcription issues."),
 (615, "Hecke and prime-power expressions, l-adic target, root magnitude, eta factor, modular ring and repeated Kostant formula.", "The GL2 target, nonreal roots, eta prefactor and omitted power are emendations of visible notebook expressions."),
 (616, "Leray heading, distributions and position/momentum normalizer.", "Real linear span, complex-linear continuous implementer and invariant Schwartz domain are supplied."),
 (617, "Quadratic integral transforms, constants, unitarity and Maslov signs.", "Unitarity leaves a U(1) phase; a metaplectic double cover needs a further convention."),
 (618, "Particle systems, Liouville discussion, Toda potential, five-family list and elliptic question.", "The first Toda expression is not a potential; phase spaces and center-of-mass degree are made explicit."),
 (619, "Corrected Toda line, root-system/Lax/harmonic matrices, inverse data, quantum group construction, sine-Gordon and Fermi variables.", "Classical odd coordinates do not have quantum anticommutator one; trace data alone do not recover a trajectory."),
 (620, "Constraint classes, source functional, crossed-out measure, term A and delta(0) cancellation; following record boundaries.", "Constraint matrix invertibility is essential; ambiguous exponent/Berezinian grouping is retained rather than guessed."),
 (621, "Gelfand fractional powers and stationary equation; Krichever coefficient recursion.", "Square-root branch/sign is explicit; second-operator coefficient letters and common gauge are distinguished."),
 (622, "Shabat polynomial relation, n+1 degree, spectral curve, marked point and Baker--Akhiezer normalization.", "Characteristic degree is n; local coordinate is at P0 rather than x0; scalar rank-one hypotheses are restored."),
 (623, "Function ring, coefficient-dependence bounds, pole-order residues, genus sum and algebraic-independence assertion.", "Need least orders, corrected coefficient bounds and relations among algebra generators; g algebraically independent elements are impossible for g>1."),
 (624, "End of genus criterion, centralizer intervention, theta series and final Baker--Akhiezer formula.", "Positive-order centralizer hypothesis; theta convention, exponential parameter and normalization factors are supplied."),
]

searches = [
 dict(topic="Vey obstruction theorem", queries=["Vey 1975 déformation crochet Poisson H3 symplectique"], outcome="Bibliographic record found and opened; exact original obstruction proof not obtained.", next_query=None),
 dict(topic="Unspecified complex Euler-product power", queries=["Euler product psi exponent complex z zero coefficients Kostant"], outcome="General-power literature found, but no precise question is specified by the notebook.", next_query=None),
 dict(topic="Fradkin--Fradkina formula and delta(0)", queries=["Fradkin Fradkina 1978 constraints delta(0) S matrix cancellation"], outcome="Publisher abstract surfaced; opening full text failed. Exact notebook formula remains unverified.", next_query=None),
 dict(topic="Numerical genus criterion", queries=["Krichever 1975 algebraic operator genus gaps mu sum", "commuting differential operators order semigroup genus smooth singular"], outcome="Rank-one spectral-data classification read; no exact iff with only the notebook's numerical hypotheses was established.", next_query=None),
 dict(topic="Bernstein's untitled 1967 reference", queries=[], outcome="No exact title or bibliographic identity recovered; it is not cited as a verified publication.", next_query="Bernstein 1967 polynomial coefficient commuting ordinary differential operators algebraic dependence"),
 dict(topic="Manakov dissertation attribution", queries=[], outcome="The untitled dissertation and its exact first-two-model scope were not independently identified.", next_query="Manakov dissertation 1975 integrable particle systems higher Hamiltonian flows"),
 dict(topic="Schroer attribution in the constrained report", queries=[], outcome="The notebook does not specify an identifiable paper or precise equivalence theorem.", next_query="Schroer Fradkin 1975 sine Gordon Thirring canonical equivalence"),
]
consulted = [
 dict(url="https://physics.ucsc.edu/~sriram/Courses_All/Physics210-Fall2018/Handouts-Interesting-Papers/Moser-Calogero-Sutherland.pdf", result="Opening failed with 502 twice. Moser 1975 is not cited; the required formulas were checked in Sasaki--Takasaki.", source_result_refs=["turn56search36"]),
 dict(url="https://hrcak.srce.hr/en/338788", result="Opened catalogue identifies a 1986 reprint of Senjanovic. It is not treated as the original publication.", source_result_refs=["turn129view1"]),
 dict(url="https://hrcak.srce.hr/file/489576", result="Full-text retrieval returned 418; no source result is credited to a read PDF.", source_result_refs=["turn127view1", "turn130view3"]),
 dict(url="https://www.damtp.cam.ac.uk/user/md327/ISlecture_notes_2012.pdf", result="Timed out; replaced by the opened Cannas da Silva notes.", source_result_refs=["turn135view0"]),
 dict(url="https://arxiv.org/pdf/hep-th/9905011", result="Universal-Lax paper consulted; not needed in the final cited set.", source_result_refs=["turn44view1"]),
]
ledger = dict(
    block="records 363--374", academic_year=1975, status_date=CHECKED,
    method="Primary sources preferred. A source marked verified in BibTeX has been opened; theorem-level verification is narrower and is stated separately. Receipt/submission is not equated with public circulation.",
    sources=sources, unresolved_searches=searches, consulted_but_not_cited=consulted,
    scan_inspection=[dict(page=f"P{n:06d}", path=f"work/scans/GELFAND-P{n:06d}.png", inspected_on=CHECKED, features=features, consequence=effect) for n,features,effect in scan_observations])
assert {x["key"] for x in sources} == {k for x in items+problems for k in x["refs"]}
(OUT / "a_sources.json").write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")

classes = Counter(x["class"] for x in items)
areas = Counter(x["area"] for x in items)
by_record = Counter(x["record"] for x in items)
by_speaker = Counter(x.get("speaker", next(t["speaker"] for t in talks if t["record"]==x["record"])) for x in items)
with (OUT / "a_corrections.csv").open() as f:
    corrections = list(csv.DictReader(f))
text = """# Research and inspection log: GY1975, records 363–374

Status date: **10 November 2026**. All mathematical status claims refer to that date; a November date later than the tenth is not assumed.

## Completed scope

The fragment covers all twelve assigned catalogue records, with **93 distinct mathematical items**, **7 problem entries**, **43 corrections**, and **33 cited bibliography keys**. The items include the small formulas, methods, physical constructions and ambiguous suggestions, as well as the prominent theorems. Broad catalogue ranges are retained in the talk catalogue; item ranges identify the actual manuscript pages. The authoring script checkpoints at each record and preserves the two distinct Manin records.

The files are a_talks.json, a_items.json, a_problems.json, a_corrections.csv, a_references.bib and a_sources.json. Reproducible authoring, bibliography, ledger and finite-arithmetic scripts are in work/code. The source ledger records every cited work's opened URLs, source-result references, read locators, chronology and verification limits. An opened bibliographic page is never described there as a read theorem. Fradkin–Fradkina 1978 is explicitly an unverified publication lead after failed full-text retrieval.

## Coverage and boundaries

| Record | Items | Boundary and attribution decision |
|---|---:|---|
| 363 | 4 | Kirillov/Vey material is on P000603 after the introductory physics announcement. |
| 364 | 14 | Polyakov's first physics lecture occupies P000604–P000609; Gelfand's finite-dimensional integral intervention has its own speaker field. |
| 365 | 2 | BDF material is on P000610, separate from the following Euler-product report. |
| 366 | 6 | Kostant/Euler-product material and Gelfand's final suggestions share P000610. |
| 367 | 5 | Polyakov's continuation is on P000611–P000612; historical quark counts are retained as historical. |
| 368 | 3 | Gelfand/Povzner differential-polynomial discussion is inserted on P000613. |
| 369 | 1 | Manin's opening tau definition precedes the Gelfand intervention on the same page. |
| 370 | 18 | Manin's numbered formulas continue through P000615; each distinct identity or construction is assessed. |
| 371 | 4 | Leray's metaplectic discussion occupies P000616–P000617. |
| 372 | 23 | Particle systems and constrained quantization occupy P000618–P000620; Perelomov and Gelfand interventions are attributed at item level. |
| 373 | 3 | Gelfand's introduction on P000621 precedes Krichever's construction. |
| 374 | 10 | Krichever's report continues through P000624. P000625 starts Dubrovin's next report and belongs to record 375, not this block. |

The final boundary was coordinated with the next agent. Overlapping catalogue links do not create duplicate mathematical items.

## Classification

"""
text += "| Class | Count |\n|---|---:|\n"
for c in "ABCDEF":
    text += f"| {c} | {classes[c]} |\n"
text += """

No item in this block supports a defensible C/D classification together with a precise bounded new contribution. The incomplete fragments are F because the intended assertion is not recoverable, not because a failed search proves they were never developed. The elementary corrections and finite arithmetic are annotations rather than manufactured open problems.

The actual-speaker rule matters: the inverse-data solution in 372.11 is A because the checked later source credits Olshanetsky–Perelomov's 1976 work and Perelomov makes the intervention. This is still an indirect check of the original and only a partial match to the trace-only notebook wording. The generic generating-functional mechanism in 372.21 is E. The exact unrecovered constraint term in 372.22 is F. The formal KdV hierarchy in 373.1 is E, continuing the 1973 discussion; a later Hamiltonian formulation does not change the classification of what the notes actually state.

### Counts by area

| Area | Items |
|---|---:|
"""
for area, count in sorted(areas.items()):
    text += f"| {area} | {count} |\n"
text += "\n### Counts by actual attributed speaker\n\n| Speaker | Items |\n|---|---:|\n"
for speaker, count in sorted(by_speaker.items()):
    text += f"| {speaker} | {count} |\n"
text += """

## Inspection of the manuscript scans

All scans P000603–P000624 were visually inspected. The English and Russian transcriptions were compared with the images at the ambiguous or mathematically consequential points. The final five checks (604, 606, 607, 609, 612) used proportional inspection copies; the unchanged originals remain the authoritative images. The ledger lists the exact source paths.

| Page | Features inspected | Editorial consequence |
|---|---|---|
"""
for n, features, effect in scan_observations:
    text += f"| P{n:06d} | {features} | {effect} |\n"
text += """

The corrections distinguish faithful notebook errors from transcription/translation changes and unresolved ambiguities. In particular, the beta/Gamma factor, Toda potential, characteristic-polynomial degree, algebraic-independence wording and theta normalization are not silently blamed on the transcriber. The source itself often contains the problem.

## Mathematical reconstructions and their limits

The main scope repairs concern locality of Lie brackets; the real symplectic span, complex-linear implementer and common Schwartz domain in the metaplectic discussion; regular collision-free particle phase spaces; fixed center-of-mass conventions; group-derived versus arbitrary couplings in radial conjugation; generic rank one in the scalar spectral-curve construction; nonspecial pole bounds rather than an exact pole divisor for every parameter; and positive operator order in the centralizer theorem.

The unreduced n-particle elliptic system needs n independent integrals, including the center-of-mass momentum. Removing that canonical pair leaves an A_(n−1) relative system with n−1 integrals. The proof checked for the elliptic root-system question excludes harmonic confinement. The corrected rational initial-value reconstruction uses full initial matrices, not traces alone. Regularity away from potential poles and generic independence are stated.

For the Baker–Akhiezer construction, the local x-domain excludes parameter poles, the divisor is effective and nonspecial and is disjoint from the marked point, and the normalized function is 1 at x=x0. The coefficient formula u_(n−2) is restricted to n>=2, with order-zero and order-one cases handled separately. The theta formula has a consistent period convention, regularized second-kind integral, the time in the exponential and the scalar normalization factor. The numerical genus criterion remains a partial reconstruction because available orders alone do not specify the full ring, rank, singularities and divisor data.

Supplied elementary proof arguments in 368.2, 374.2 and 374.6 are marked with the supplied “proved here” macro. The initial-jet argument is a condensed reconstruction of the proof actually read in Krichever's Theorem 2.1, not a claim of an original algebraic-dependence theorem. Independent review by the adjoining agent checked the signs and theta normalization in 374 and identified the n>=2 coefficient guard, which has been applied.

## Chronology and verification

Krichever's received date, 8 October 1975, is earlier than the notebook's 20 October talk; it is not proof of public circulation. Presentation on 24 October and publication in 1976 are recorded separately. The 1977 article retrospectively mentions November–December 1975 talks; the notebook date is preserved and the discrepancy logged. Similarly, Kirillov's and Gelfand–Dikii's receipt dates are not used to prove prior public knowledge.

Coleman's paper was published on 15 April 1975 and is therefore a genuine pre-talk publication, although only its publisher abstract was read. The Toda involution paper was published on 1 May 1976; its title and metadata are checked, but its proof and earliest-priority chronology remain unverified. The general root-system involution proof was first publicly submitted on 30 May 2000 and published in 2001. Kostant's original 1976 identity is read through the explicit restatement in his 2003 preprint; this indirect-original limitation is kept visible.

Full-source checks resolved the strongest ambiguities: Dyson's five-tuple identity, Deligne's modular-form representation and purity, the metaplectic phase convention, the radial-conjugation restrictions, and Krichever's rank-one construction. Searches of MathNet, author PDFs and later reference lists were especially useful. Failed retrievals were not converted into positive verification: Moser's mirror failed, Senjanovic's accessible record was a later reprint with an inaccessible PDF, and the Fradkin–Fradkina publisher/INSPIRE routes did not expose full text.

The unresolved targets and actual search strings are recorded separately from proposed follow-up queries in a_sources.json. They include Vey's exact H^3 formulation, the unspecified complex power and spectral-zeta questions, the ambiguous constraint term A and delta(0) cancellation, the bare numerical genus criterion, Bernstein's untitled 1967 reference, Manakov's untitled dissertation and the Schroer attribution. No exact result or priority is invented for them.

## Independent finite arithmetic

The portable script work/code/a_tau_check.py writes work/computations/a_tau_check.json relative to its own location. It computes tau(n) for 1<=n<=50 independently by the truncated Euler product and a logarithmic-derivative divisor recurrence. Ramanujan's convolution identity and the corrected Manin factorization, with the boundary half-weight, agree with both arrays throughout that finite range.

Three literal notebook expressions fail at small inputs: the unweighted partition sum gives −1 instead of tau(2)=−24; the written Manin polynomial, even with the favorable half-weight, gives −841 instead of −24; and the written prime-power sum gives −3520 instead of tau(4)=−1472. These are exact integer/rational computations. Agreement through 50 is finite evidence only, not a proof of an all-n identity or a new algorithmic-complexity result.

## What the classification misses; website implications

The A–F field records historical development but cannot convey literal correctness, quality of publication match or level of verification by itself. Those independent fields are essential here: a famous established subject may have a false notebook formula; a later exact theorem may have hypotheses absent from the notes; and a valid formula may have an unverified attribution. The entry page should show those three assessments before offering a literature link.

A reader arriving at one talk should first reach the exact scan page and parallel-language passage, then the reconstructed statement and its scope repairs. Strong links are the 1973 higher-KdV problem to 373.1, the 1974 finite-gap problem to 373.2, the repeated Kostant formulas in 366/370, the center-of-mass and inverse-data distinctions within 372, and the rank-one spectral construction continuing into the adjoining 375–385 block. An optional source-level verification/locator field and an explicit manuscript/circulation/publication chronology would avoid flattening all “verified” references into the same evidentiary status.

## Final QA

The quoting defect that once embedded Python keyword fragments into fate strings was fixed at its source and all affected assessments regenerated. The final validation checks field presence, enum values, contiguous occurrence numbers, nonempty areas, exact equality of cited and listed references, missing bibliography keys, control characters and leaked keyword fragments. The unsupported slashed macro was removed. The two reported overfull inline formulas were moved to display math. Root performs the integrated chapter build and final visual inspection.
"""
(OUT / "a_research.md").write_text(text)
print(f"Wrote {len(sources)} source records and {len(scan_observations)} scan inspections.")
