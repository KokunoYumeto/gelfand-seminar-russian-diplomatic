#!/usr/bin/env python3
"""Reproduce the records 667--681 critical-companion data; all prose is editorial.

Run from the shared workspace root. Source and verification inventory is in
parts/A/research_notes.md and parts/A/evidence/*.json. No input file is modified.
"""
import json
from pathlib import Path

OUT = Path(__file__).resolve().parents[1]
TALKS, ITEMS, PROBLEMS = [], [], []

def talk(record, date, speaker, pages, title, summary, kind='talk'):
    TALKS.append(dict(record=record, date=date, speaker=speaker, pages=pages,
                      title=title, kind=kind, summary=summary))

def item(record, pages, kind, title, notes, statement, fate, refs=(), *,
         reconstruction='', cls='E', status='', literal='correct with missing hypotheses',
         match='exact', verification='read the result', development='none',
         problem='', worth='', confidence='high', speaker=None):
    n = 1 + sum(x['record'] == record for x in ITEMS)
    obj = dict(id=f'1986-{record}.{n}', record=record, pages=pages, kind=kind,
               title=title, notes=notes, statement=statement, reconstruction=reconstruction,
               **{'class': cls}, fate=fate,
               present_status=status or r'As of November 2026, the corrected formulation is an established result; no unresolved claim is inferred from this occurrence.',
               literal_correctness=literal, publication_match=match,
               verification=verification, development=development, problem=problem,
               worth=worth, refs=list(refs), confidence=confidence)
    if speaker: obj['speaker'] = speaker
    ITEMS.append(obj)
    return obj['id']

def checkpoint():
    TALKS.sort(key=lambda x: x['record'])
    ITEMS.sort(key=lambda x: tuple(map(int, x['id'].removeprefix('1986-').split('.'))))
    for name, data in [('talks', TALKS), ('items', ITEMS), ('problems', PROBLEMS)]:
        (OUT / (name + '.json')).write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')

talk(667, '1987-02-24', 'M. L. Kontsevich', 'P001257-P001260',
     'Formal uniformization of curves and the Virasoro action',
     r'The mathematical contribution headed Kontsevich occupies P001258: a curve with a marked point and formal coordinate is acted on by Laurent vector fields, and the Virasoro extension lifts the action to determinant lines. P001257 is a continuation of Beilinson, not part of this contribution. The catalogue date is retained, although the heading visibly reads \(24/\mathrm{II}\text{-}85\); neighboring headings consistently read 1986. Consequently the record cannot establish priority relative to the paper received in December 1986.')
item(667, 'P001258', 'construction', 'Infinitesimal uniformization by Laurent vector fields',
     r'The notes define \(\widetilde M_g=(C,p,x)\), \(\mathfrak g=\mathbb C((x))\partial_x\), and \(\gamma\) as Laurent expansions of vector fields on \(C\setminus\{p\}\); the stated action has stabilizer \(\gamma\).',
     r'For smooth connected projective complex curves with a marked point and a formal parameter, Laurent vector fields act infinitesimally on the corresponding moduli stack. At \((C,p,x)\), the tangent space is \(\mathfrak g/H^0(C\setminus\{p\},T_C)\), where the denominator is embedded by its Laurent expansion. This is a formal infinitesimal uniformization, not a claim that the coarse moduli space is globally a quotient by a finite-dimensional Lie group.',
     r'\citet[\S1]{kontsevich1987virasoro} gives this construction and its stabilizer. The paper was received on 3 December 1986 and published in 1987; this is the direct author match, independently of the notebook date discrepancy.',
     ['kontsevich1987virasoro'], cls='A', reconstruction=r'The stack/formal interpretation and smooth projective hypotheses make precise the shorthand “homogeneous space.”')
item(667, 'P001258', 'method', 'Meromorphic lifts and the Kodaira--Spencer quotient',
     r'A family is given a lift \(\nabla_t=\partial_t+F(x,t)\partial_x\). One line identifies the tangent space with \(\mathfrak g/\mathfrak k\), but the following displayed Kodaira--Spencer formula uses vector fields extending off \(p\).',
     r'A meromorphic lift of a base tangent vector, allowed a pole along the section, gives a Laurent vector field modulo vector fields extending over the punctured curve. For the decorated space its quotient is \(\mathfrak g/\gamma\). Quotienting also by coordinate changes gives the appropriate tangent description for the undecorated moduli problem; \(\mathfrak g/\mathfrak k\) alone omits the curve-dependent stabilizer.',
     r'The tangent identification in \citet[\S1]{kontsevich1987virasoro} agrees with the second notebook formula. The isolated \(\mathfrak g/\mathfrak k\) line is a faithful mathematical error, confirmed by the scan.',
     ['kontsevich1987virasoro'], cls='A', literal='false as written', reconstruction=r'The first quotient is emended using the next formula and the published construction; no change to the diplomatic transcription is proposed.')
item(667, 'P001258', 'theorem', 'Virasoro action on determinant lines',
     r'The central extension \(\widetilde{\mathfrak g}\), called the Virasoro algebra, acts on the pullback of the determinant bundle \(d_k\) from \(M_g\).',
     r'Let \(\lambda_k=\det H^0(C,K_C^k)\otimes\det H^1(C,K_C^k)^{-1}\). Its pullback to curves with a formal coordinate admits the corresponding lift of the Laurent-vector-field action to a Virasoro central extension. The central character depends on the determinant and cocycle conventions; the notebook does not specify a numerical normalization.',
     r'This is the determinant-line application in \citet[\S2]{kontsevich1987virasoro}, published in 1987. The brief notebook assertion should not be expanded into an unrecorded central-charge formula.',
     ['kontsevich1987virasoro'], cls='A', reconstruction=r'The determinant of cohomology is explicitly defined here; the notes only name \(d_k\).')
checkpoint()

talk(670, '1987-03-03', 'A. Yu. Morozov', 'P001263-P001269',
     'String amplitudes, Green functions, and the superstring measure',
     r'The continuation headed Morozov starts midway through P001265 and runs through P001267. It connects the string description to gauge fields, discusses explicit bosonic measures and theta functions, and asks how to obtain the superstring measure by eliminating odd variables. The catalogue range includes neighboring contributions; the items below use the actual headings. The manuscript belongs to the \(3/\mathrm{III}\text{-}86\) session.')
item(670, 'P001265', 'remark', 'Ultraviolet motivation and numerical scale estimates',
     r'The notes contrast a string length near \(10^{-33}\,\mathrm{cm}\) with particle scales and describe other theories as inconsistent at short distances.',
     r'This is a physical motivation, not a mathematical theorem. A string length is \(\ell_s=\sqrt{\alpha^{\prime}}\) in a stated unit convention; its relation to a gravitational scale depends on coupling and compactification. No universal assertion that every nonstring quantum field theory is ultraviolet inconsistent follows. The written proton size near \(10^{-35}\,\mathrm{cm}\) also conflicts with the scale comparison recorded on P001269.',
     r'The critical-string framework is identifiable from \citet[Introduction]{grossharveymartinecrohm1985heterotic}, but that paper does not establish the universal assertion. The specific estimate is retained as notebook error rather than promoted to a research problem.',
     ['grossharveymartinecrohm1985heterotic'], cls='F', match='thematic only', literal='false as written', confidence='high',
     status=r'As of November 2026, this passage remains a historically identifiable motivation with an erroneous numerical entry, not a definite unsolved mathematical claim.')
item(670, 'P001265-P001266', 'method', 'Ward identities from integrated longitudinal vertices',
     r'A polarization proportional to momentum turns a vector insertion into a total derivative, and the massless string excitation is connected with Yang--Mills theory.',
     r'For an on-shell open-string vector vertex on a worldsheet boundary, replacing the polarization by its momentum produces a boundary derivative of the exponential vertex. Decoupling in amplitudes requires the usual BRST or physical-state conditions and control of contact and boundary contributions. Chan--Paton labels supply nonabelian gauge factors. Closed-string massless tensor vertices give a different sector, including gravity.',
     r'The distinction between open-string Chan--Paton gauge symmetry and closed-string constructions is already explicit in \citet[Introduction]{grossharveymartinecrohm1985heterotic}; the BRST field-theoretic implementation appears in \citet{witten1986noncommutative}. Both precede the catalogue date.',
     ['grossharveymartinecrohm1985heterotic', 'witten1986noncommutative'], match='partial', reconstruction=r'The boundary, on-shell, and decoupling hypotheses delimit the total-derivative argument.')
item(670, 'P001266', 'construction', 'The scalar Green function through the prime form',
     r'The Green function is expressed using a theta function and an Abelian-integral correction involving \((\operatorname{Im}T)^{-1}\). Some quadratic factors are suppressed.',
     r'For a marked compact Riemann surface with normalized holomorphic one-forms \(\omega\), period matrix \(\Omega\), and prime form \(E\), the standard scalar Green kernel has the local expression \(-\log|E(z,w)|^2+2\pi\,v^{\mathsf T}(\operatorname{Im}\Omega)^{-1}v\), where \(v=\operatorname{Im}\int_w^z\omega\), up to the metric-dependent normalization needed to fix its additive zero mode. The prime form contains half-differential factors; a theta function alone is not a globally defined scalar replacement.',
     r'This construction underlies the vertex-insertion expressions in \citet[\S2]{belavinknizhnik1986complex}. The notebook is a recognizable shorthand, but the missing second vector and half-differentials prevent literal use.',
     ['belavinknizhnik1986complex'], match='partial', reconstruction=r'The complete quadratic form and prime form are editorial reconstructions; no unrecorded normalization is assigned to Morozov.', literal='correct with missing hypotheses')
item(670, 'P001266-P001267', 'claim', 'Explicit low-genus bosonic measures and Mumford forms',
     r'The notes list explicit expressions in low genus, including genus four, and mention Manin\textquotesingle s all-genus description.',
     r'The critical bosonic measure can be expressed as the norm square of a Mumford form with a period-matrix factor. Explicit theta-constant formulas require distinguishing the full Siegel space from its Jacobian locus and accounting for the genus-dependent modular form and its divisor. A low-genus formula is not a claim that the measure is undefined in higher genus.',
     r'\citet{morozov1987explicit} gives explicit one-, two-, three-, and four-loop bosonic vacuum amplitudes; \citet{beilinsonmanin1986mumford} supplies the determinant-line interpretation. The former appeared in 1987, before the catalogue session but after the 1986 manuscript heading; no priority conclusion is drawn from the catalogue alone.',
     ['morozov1987explicit', 'beilinsonmanin1986mumford'], match='exact', verification='indirect', reconstruction=r'The Jacobian-locus and normalization qualifications are supplied. The explicit-formula identification is supported by the authored abstract and bibliographic metadata; the complete formula paper was not read.', confidence='high')
item(670, 'P001267', 'method', 'Variations of regularized determinants',
     r'The proposed calculation varies a determinant using the Green function at coincident points.',
     r'For an admissible smooth family of invertible elliptic operators, the variation of the logarithmic zeta determinant is a regularized trace of \(A^{-1}\delta A\), with local correction terms determined by the regularization convention. The unregularized coincident Green kernel is singular and cannot be substituted into an ordinary trace. Zero modes require a reduced determinant and a separate kernel metric.',
     r'\citet[\S1]{kontsevichvishik1994geometry} formulates determinant variations in a regularized-trace setting. The notebook\textquotesingle s particular theta-function expression is too incomplete for an exact formula match.',
     ['kontsevichvishik1994geometry'], cls='B', match='partial', reconstruction=r'Admissibility, kernel treatment, and regularization are restored; the incomplete displayed theta expression is not certified.', confidence='medium')
item(670, 'P001267', 'question', 'Eliminating odd moduli in the superstring measure',
     r'The notes ask how to integrate over the odd variables of supermoduli and obtain an ordinary-moduli measure; the resulting modular ratio is expected to have weight eight.',
     r'For a smooth super Riemann surface of fixed genus and spin parity, determine the pushforward of the RNS measure along odd moduli wherever a specified projection exists, and its transformation and boundary behavior. A global holomorphic projection from supermoduli to reduced spin moduli is an additional geometric assertion, not an automatic meaning of Berezin integration. Local odd integration remains meaningful after a splitting is chosen.',
     r'\citet[Theorem 1.1]{donagiwitten2015supermoduli}, first circulated in April 2013, proves nonprojectedness in genus at least five. Version 1 of the preprint of \citet[Theorem 1.1]{correadonaginoja2026supermoduli}, submitted 30 September 2026, states the nonvanishing of the primary obstruction on both parity components for every genus \(g\geq3\), algebraically and holomorphically. The latter theorem statement was read; its proof has not been independently checked here.',
     ['donagiwitten2015supermoduli', 'correadonaginoja2026supermoduli'], cls='B', problem='GP-1986-01', match='partial',
     reconstruction=r'The precise global-projection obstruction is a later formulation of one assumption behind the notebook\textquotesingle s proposed calculation.',
     status=r'As of 12 November 2026, a global holomorphic projection is obstructed in the stated genera, including genus three according to the September 2026 preprint. This does not assert that local RNS measures or physical amplitudes cease to exist.')
item(670, 'P001267', 'problem', 'Determining higher-genus superstring measures',
     r'The computational question remains: find the superstring measure after the odd-variable calculation, rather than only its expected weight.',
     r'In the genus-three even-spin case, on the nonhyperelliptic locus where a chosen pushforward is defined, determine the exact coefficients of the RNS top component in the three-function ansatz and prove the claimed normalization and degeneration behavior. This is a modern bounded subproblem of the much broader notebook request, not its verbatim formulation.',
     r'\citet[\S1.7 and \S4.9]{duninbarkowskifedorovsleptsov2025rns}, circulated in May 2025 and published in October 2025, proves membership in a three-dimensional span but labels the coefficient values conjectural. Section 4.9.2 explicitly notes that the numerical computations lack rigorous error bounds. The hyperelliptic polar behavior also prevents identification with an everywhere holomorphic ansatz.',
     ['duninbarkowskifedorovsleptsov2025rns'], cls='C', problem='GP-1986-01', match='partial',
     reconstruction=r'The three coefficient problem is a later precise specialization, clearly separated from the all-genus notebook request.',
     worth=r'Worth developing in a separate run: the three coefficient identities and their normalization are concrete, but a complete RNS derivation and boundary analysis exceed the present bounded verification.',
     status=r'As of 12 November 2026, the cited genus-three coefficient values remain conjectural in the opened publication; no claim of a complete higher-genus solution is made.', confidence='high')
item(670, 'P001267', 'theorem', 'Weight-eight forms and the genus-four Schottky relation',
     r'The notes say that cusp forms of weight eight first occur in genus four and identify a relation relevant to the string measure.',
     r'For scalar Siegel modular forms of weight eight for the full symplectic modular group, the two rank-sixteen even unimodular theta series agree in genera at most three. Their genus-four difference is a multiple of the Schottky form and vanishes on the Jacobian locus. These full-group statements must not be transferred to level subgroups or to spin-dependent modular forms, which have additional forms.',
     r'\citet[\S2]{grushevskysalvatimanni2011superstring} records these classical identities and their failure to force the analogous genus-five cosmological constant to vanish. Its preprint first appeared in September 2008; the identities it uses are older than the notebook.',
     ['grushevskysalvatimanni2011superstring'], reconstruction=r'The full modular group and Jacobian-locus qualifiers are added.', match='partial')
checkpoint()

talk(671, '1987-03-10', 'A. Yu. Morozov', 'P001267-P001274',
     'Compactification, lattice theta series, and heterotic gauge symmetry',
     r'The contribution begins on P001268 and continues through P001273. It combines gauge fields, the string oscillator spectrum, compactification on a sixteen-dimensional torus, modular lattice sums, and root vertex operators. Several formulas mix ordinary bosonic compactification with the chiral heterotic construction. The manuscript date is \(10/\mathrm{III}\text{-}86\), whereas the catalogue says 1987.')
item(671, 'P001268', 'definition', 'Yang--Mills curvature and gauge transformations',
     r'The gauge potential \(A_\mu^a\), its curvature, and infinitesimal transformations are written before the string discussion.',
     r'For a Lie-algebra-valued connection one-form \(A\), \(F=dA+A\wedge A\), or \(F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu+[A_\mu,A_\nu]\), and an infinitesimal gauge transformation is \(\delta_\epsilon A=d\epsilon+[A,\epsilon]\). One must retain both antisymmetric curvature indices.',
     r'The gauge-field conventions are standard background for the low-energy comparison in \citet{grossharveymartinecrohm1985heterotic}; they are not presented as a new theorem. The missing curvature index is a notebook notational slip.',
     ['grossharveymartinecrohm1985heterotic'], reconstruction=r'The matrix-valued convention avoids an unrecorded choice of signs for structure constants.', match='partial')
item(671, 'P001268-P001269', 'claim', 'Massless vector states and allowed Chan--Paton groups',
     r'The first excited string state is interpreted as a vector, and a simple nonabelian gauge group is introduced.',
     r'The open bosonic string has a massless vector at oscillator number one in the critical theory. Nonabelian Chan--Paton factors in the usual oriented or unoriented perturbative construction give unitary, orthogonal, or symplectic families subject to consistency conditions. A generic closed bosonic string on flat \(\mathbb R^{26}\) instead has a massless tensor sector and does not produce this vector by the same construction. Arbitrary simple groups are not obtained merely by adding conventional endpoint labels.',
     r'\citet[Introduction]{grossharveymartinecrohm1985heterotic} explicitly motivates the heterotic construction by the limited Chan--Paton possibilities, including the exceptional-group issue. The notebook merges distinct constructions.',
     ['grossharveymartinecrohm1985heterotic'], literal='false as written', reconstruction=r'The sector and gauge-group qualifications are necessary repairs.')
item(671, 'P001269-P001270', 'construction', 'The sixteen-dimensional lattice in the heterotic string',
     r'The map target is changed from \(\mathbb R^{26}\) to \(T^{16}\times\mathbb R^{10}\), and supersymmetry and the groups \(E_8\times E_8\) and \(SO(32)\) are discussed.',
     r'The ten-dimensional heterotic string combines a chiral bosonic matter sector of central charge 26 with a supersymmetric matter sector of central charge 15; the respective ghost systems cancel these matter anomalies. The sixteen extra chiral bosons have momenta in a positive-definite even unimodular rank-sixteen lattice. The two lattices are \(E_8\oplus E_8\) and \(D_{16}^{+}\), giving gauge Lie algebras \(\mathfrak e_8\oplus\mathfrak e_8\) and \(\mathfrak{so}_{32}\). Ordinary nonchiral compactification of the full bosonic theory does not itself supply spacetime supersymmetry.',
     r'This is the construction of \citet{grossharveymartinecrohm1985heterotic}, published on 11 February 1985 after receipt in November 1984. It predates either plausible date of this talk.',
     ['grossharveymartinecrohm1985heterotic'], reconstruction=r'The chiral construction is made explicit. The global group associated with \(D_{16}^{+}\) is a suitable \(\operatorname{Spin}(32)/\mathbb Z_2\), so the notebook\textquotesingle s \(SO(32)\) is used only at Lie-algebra level.', literal='correct with missing hypotheses')
item(671, 'P001269', 'question', 'A dynamical mechanism for compactification',
     r'Gelfand asks about obtaining compactification dynamically rather than putting in a torus.',
     r'The passage asks for a physical mechanism selecting a lower-dimensional background. It specifies no action including its quantum corrections, no admissible class of backgrounds, and no stability criterion. Those choices change the question, so the notes do not determine a single proposition to prove.',
     r'The toroidal construction in \citet{grossharveymartinecrohm1985heterotic} supplies a background, not the general selection mechanism requested. Searches for heterotic compactification and the original construction identify the context but do not justify equating this broad question with a named unsolved conjecture.',
     ['grossharveymartinecrohm1985heterotic'], cls='F', speaker='I. M. Gelfand', match='thematic only', literal='not determinable', confidence='high',
     status=r'As of November 2026, the notebook question remains under-specified; no new problem-index identifier or class D is assigned.')
item(671, 'P001270', 'construction', 'Classical winding maps on a worldsheet torus',
     r'The boundary conditions are \(x(z+1)-x(z)=\Lambda_2\) and \(x(z+\tau)-x(z)=\Lambda_1\), but equation (18) uses two plus signs in the affine part.',
     r'For real target-space winding vectors and \(\operatorname{Im}\tau>0\), the harmonic affine representative is \[x_{\mathrm{cl}}(z)=\frac{(\Lambda_1-\overline\tau\Lambda_2)z-(\Lambda_1-\tau\Lambda_2)\overline z}{2i\operatorname{Im}\tau}.\] The fluctuation is doubly periodic. This formula satisfies the two stated shifts and is real valued.',
     r'The winding-sector decomposition is the compact-boson calculation used in \citet{grossharveymartinecrohm1985heterotic}. The scan confirms the two plus signs in the notebook; direct substitution into its boundary conditions detects the sign error.',
     ['grossharveymartinecrohm1985heterotic'], literal='false as written', match='partial', reconstruction=r'\oursComputed\ The displayed corrected affine representative is an editorial algebraic reconstruction from the recorded boundary conditions; the check is logged, not claimed as new research.', development='annotated')
item(671, 'P001270-P001271', 'method', 'Winding sums, Gaussian factors, and Poisson summation',
     r'After Gaussian integration the partition function is a double sum over \(\Lambda_1,\Lambda_2\), with an exponential of a quadratic expression divided by \(\operatorname{Im}\tau\). It is then factorized into theta functions.',
     r'For a compact free boson, the classical Euclidean action is a positive multiple of \(\|\Lambda_1-\tau\Lambda_2\|^2/\operatorname{Im}\tau\), so the convergent winding factor has a negative real exponent. Poisson summation rewrites the winding sum as a momentum lattice sum. Holomorphic factorization into a specified finite collection of theta functions needs additional lattice and rationality data; it is not automatic for every real torus metric.',
     r'The compactification and modular lattice calculation is an essential step of \citet{grossharveymartinecrohm1985heterotic}. The notebook suppresses sign and normalization conventions and also mixes a nonchiral absolute-square expression with a chiral lattice sum.',
     ['grossharveymartinecrohm1985heterotic'], reconstruction=r'Positivity of the Euclidean action and the conditions for chiral factorization are restored.', match='partial')
item(671, 'P001271-P001272', 'question', 'What modularity requires of a positive lattice',
     r'Gelfand asks whether the even self-dual lattices are the only ones giving the needed modular behavior.',
     r'For a positive-definite lattice \(L\) of rank \(r\), the theta series \(\Theta_L(\tau)=\sum_{x\in L}e^{\pi i\tau(x,x)}\) of an even unimodular lattice transforms as a scalar modular form of weight \(r/2\) for the full modular group. If one instead allows a congruence subgroup, a multiplier, or a vector of theta series of discriminant cosets, even unimodularity is not a necessary condition. Thus the word “modular” must include the transformation group and representation before an “only” statement is possible.',
     r'The full-group condition is the one imposed in \citet{grossharveymartinecrohm1985heterotic}. Its role is separate from the broader modular theory of nonunimodular lattices. This is an already known modularity criterion, not evidence for an unsolved classification.',
     ['grossharveymartinecrohm1985heterotic'], problem='GP-1986-02', speaker='I. M. Gelfand', reconstruction=r'The qualified full-group formulation is supplied; the unqualified converse is deliberately not asserted.', match='partial', literal='not determinable',
     status=r'As of November 2026, the scalar full-group criterion is classical. The notebook\textquotesingle s unqualified question has different answers for subgroups and vector-valued forms.')
item(671, 'P001272', 'theorem', 'Two rank-sixteen theta series and their higher-genus difference',
     r'The two lattice expressions are compared, with an identity involving powers of theta constants and an absolute square.',
     r'The lattices \(E_8\oplus E_8\) and \(D_{16}^{+}\) have the same genus-one theta series, the weight-eight form \(E_4^2\). Their Siegel theta series agree through genus three; in genus four their difference is the Schottky form up to scale and vanishes on Jacobians. The holomorphic theta identity is distinct from taking the absolute square in a nonchiral partition function, and the powers of two depend on the theta normalization.',
     r'\citet[\S2]{grushevskysalvatimanni2011superstring} supplies the exact comparison and explains the subsequent genus-five distinction. These low-genus identities are classical, despite the later verification source.',
     ['grushevskysalvatimanni2011superstring'], reconstruction=r'The notebook\textquotesingle s absolute-square line is separated from the holomorphic identity; its numerical normalization is not copied as a theorem.', literal='correct with missing hypotheses')
item(671, 'P001272-P001273', 'construction', 'Root vertex operators and the affine Lie algebra',
     r'Exponential operators indexed by lattice roots are said to have commutator given by the operator for the sum of two roots, and zero otherwise.',
     r'For an even root lattice, the lattice vertex construction uses cocycles and a Heisenberg algebra. Root operators for \(\alpha+\beta\) a root bracket to a signed root operator. If \(\beta=-\alpha\), their bracket produces Cartan and central terms rather than zero. The oscillator modes realize the corresponding level-one affine Lie algebra; these cocycle and opposite-root cases are indispensable.',
     r'This is the basic-representation construction identified with \citet{frenkelkac1980basic}. Its publisher metadata was opened, but the full original construction was not read in this run; the exact identification is therefore marked indirect. The displayed “zero otherwise” rule is false in the opposite-root case.',
     ['frenkelkac1980basic'], literal='false as written', verification='indirect', reconstruction=r'The Heisenberg sector, cocycle, and opposite-root term restore the standard construction.')
checkpoint()

talk(668, '1987-02-24', 'A. Yu. Morozov', 'P001258-P001263',
     'Bosonic string measure, determinants, and the conformal anomaly',
     r'The actual talk begins on P001259 and ends on P001261 before Beilinson. It reduces the critical bosonic-string functional integral formally to a moduli integral and explains the determinants, zero modes, and holomorphic factorization underlying that reduction. Gelfand asks about multiplicativity of regularized determinants. The heading reads \(24.2.86\); the catalogue date is preserved with this disagreement recorded.')
item(668, 'P001259', 'construction', 'The genus-g bosonic measure on moduli',
     r'The functional integral over metrics and maps to \(\mathbb R^{26}\) is written as an integral over \(M_p\) of \(|d\mu_p|^2/(\det\operatorname{Im}T)^{13}\) times a vertex-insertion factor.',
     r'On the smooth genus-\(g\) moduli space, after fixing conformal gauge, the critical bosonic integrand has a holomorphic determinant-line factor paired with its conjugate and a period-matrix factor \((\det\operatorname{Im}\Omega)^{-13}\). Punctures and vertex insertions alter the corresponding line bundles and factors. This describes the integrand; it does not define a countably additive functional measure or prove convergence at the Deligne--Mumford boundary.',
     r'\citet[\S\S2--5]{belavinknizhnik1986complex} derive the determinant and holomorphic-factorization expression; \citet{beilinsonmanin1986mumford} identifies the Mumford-form interpretation. Both are 1986 publications, hence precede the catalogue date. Relative to the manuscript date they are contemporaneous.',
     ['belavinknizhnik1986complex', 'beilinsonmanin1986mumford'], reconstruction=r'The distinction between an integrand and a convergent amplitude is essential and is not made in the shorthand formula.')
item(668, 'P001259', 'construction', 'Vertex operators and on-shell insertions',
     r'The scalar vertex is \(\int e^{ikx}\), and a vector vertex is written with one derivative of \(x\).',
     r'The free-boson exponential must be normal ordered. An integrated closed-string vertex must have conformal weights \((1,1)\); a boundary open-string vertex has weight \(1\). A single derivative polarization is the open-string vector vertex. Closed-string massless tensor vertices require both holomorphic and antiholomorphic derivatives. Momentum and polarization obey the corresponding on-shell and transversality conditions.',
     r'The vertex and Green-function insertion calculation is part of \citet[\S2]{belavinknizhnik1986complex}. The notebook does not keep open and closed sectors separate, so the vector formula cannot be read as a complete closed-string state.',
     ['belavinknizhnik1986complex'], match='partial', reconstruction=r'Normal ordering, conformal weights, and the distinction between boundary and bulk vertices are supplied to make the formulas meaningful.')
item(668, 'P001259-P001260', 'method', 'Gaussian matter integration and zero modes',
     r'Integration over \(26\) scalar coordinates produces a power \(-13\) of a scalar Laplacian determinant and a Green-function exponential.',
     r'For a fixed compact worldsheet metric, the Gaussian integral over nonconstant modes of \(D\) real scalar fields contributes \((\det{}^{\prime}\Delta_0)^{-D/2}\). The prime removes the constant kernel. Integrating the constant modes imposes total target-space momentum zero, while the source-dependent term is the Gaussian quadratic form obtained from the inverse of \(\Delta_0\) on mean-zero functions.',
     r'\citet[\S2]{belavinknizhnik1986complex} explicitly separates these determinant and insertion contributions. At \(D=26\) the exponent is \(-13\); omitting the prime would give a zero determinant.',
     ['belavinknizhnik1986complex'], reconstruction=r'The kernel removal and the momentum-conservation condition are restored.')
item(668, 'P001260', 'theorem', 'Cancellation of the conformal anomaly at dimension 26',
     r'The gauge-fixed expression includes the determinant on vector fields and is independent of the conformal factor in dimension \(26\).',
     r'For the bosonic Polyakov system of \(D\) free scalar fields and the reparametrization \(bc\) ghost system of weights \((2,-1)\), the total central charge is \(D-26\). Its vanishing at \(D=26\) cancels the local Weyl anomaly in this system; it does not by itself remove tachyonic or degeneration divergences.',
     r'The critical-dimensional determinant cancellation is established in \citet[\S3]{belavinknizhnik1986complex}. The restricted system and the distinction between local anomaly cancellation and convergence are the needed hypotheses.',
     ['belavinknizhnik1986complex'], reconstruction=r'The ghost weights and the scope of the cancellation are explicit here.')
item(668, 'P001260', 'construction', 'Gram determinants and determinant of cohomology',
     r'The matrices \(N^{(j)}\) are scalar products of zero modes, and the ratio involving \(\det\Delta_j\), \(\det N^{(j)}\), and \(\det N^{(1-j)}\) is used to express the measure.',
     r'For a family of Dolbeault complexes on \(K^j\), the Gram determinants on \(H^0(K^j)\) and its Serre-dual cohomology compensate for changes of zero-mode basis. Together with a zeta determinant of the nonzero spectrum they define a Hermitian norm on the determinant of cohomology. The expression is a line-bundle metric, rather than an invariant numerical determinant without a chosen frame.',
     r'The zero-mode factors occur in \citet[\S3]{belavinknizhnik1986complex}; the determinant-line framework is \citet{quillen1985determinants}. These precede the catalogue date.',
     ['belavinknizhnik1986complex', 'quillen1985determinants'], reconstruction=r'The basis transformation and determinant-line interpretation are supplied.')
item(668, 'P001260', 'method', 'Beltrami differentials as local deformation coordinates',
     r'The complex structure is varied by Beltrami differentials, described as Ahlfors--Bers coordinates.',
     r'For a compact Riemann surface of genus \(g\geq2\), infinitesimal deformations are \(H^1(C,T_C)\), dual to holomorphic quadratic differentials. A Beltrami differential modulo infinitesimal diffeomorphisms represents a tangent vector to Teichm\"uller space. Local holomorphic coordinates on that space descend to orbifold charts on moduli, not necessarily to an ordinary global coordinate system.',
     r'\citet[\S3]{belavinknizhnik1986complex} uses this deformation description in the determinant calculation. The method is expository, not a new claim of Morozov.',
     ['belavinknizhnik1986complex'], reconstruction=r'The genus restriction and the Teichm\"uller/moduli distinction are restored.')
item(668, 'P001260-P001261', 'claim', 'Curvature of determinant metrics and the coefficient 6j squared minus 6j plus 1',
     r'The Belavin--Knizhnik variation is written as a mixed derivative of a determinant ratio equal to \(c_j=6j^2-6j+1\).',
     r'The meaningful local statement concerns the mixed second derivative of the logarithm of the determinant-line norm, with nonzero spectra used. It is a curvature two-form proportional to a universal two-form on moduli, and the coefficient for \(K^j\) is proportional to \(6j^2-6j+1\), with normalization fixed by the curvature convention. A second derivative of an unlogged ratio cannot equal a universal scalar independent of coordinates.',
     r'Compare the variation formulas in \citet[\S3]{belavinknizhnik1986complex} and the determinant-line formulation of \citet{quillen1985determinants}. The scan confirms that the notebook formula itself suppresses the logarithm and differential-form factor.',
     ['belavinknizhnik1986complex', 'quillen1985determinants'], literal='false as written', reconstruction=r'This is a correction of the mathematical shorthand, not a claim that the missing symbols were visible in the manuscript.')
item(668, 'P001261', 'question', 'Multiplicativity of regularized elliptic determinants',
     r'Gelfand asks whether \(\det(A_1A_2)=\det A_1\det A_2\) for elliptic operators and says the orders should be arbitrary.',
     r'For invertible admissible elliptic pseudodifferential operators \(A,B\) of positive orders on a closed manifold, with specified spectral cuts also admissible for \(AB\), determine \(\log\det_\zeta(AB)-\log\det_\zeta A-\log\det_\zeta B\). In general this multiplicative anomaly is nonzero; determinant multiplicativity is not an unrestricted law.',
     r'This repeats GP-1982-40 (1982-587.7). \citet[\S1.1 and the anomaly formulas]{kontsevichvishik1994geometry}, circulated in 1994, gives a systematic treatment, with residue formulas under additional hypotheses and extensions beyond the positive-order setting. The formulation requires spectral cuts, which the notes do not fix.',
     ['kontsevichvishik1994geometry'], cls='B', problem='GP-1982-40', speaker='I. M. Gelfand',
     reconstruction=r'The admissibility and invertibility hypotheses are added to obtain a well-defined zeta-determinant question; arbitrary-order operators require a different determinant framework.',
     status=r'As of November 2026, the unrestricted multiplicativity assertion is false and the multiplicative anomaly is an established part of elliptic determinant theory. The earlier problem identifier is retained.')
checkpoint()

talk(669, '1987-03-03', 'A. A. Beilinson', 'P001261-P001265',
     'Mixed Hodge structures, real splitting, and Green-function periods',
     r'The contribution starts on P001262 and ends at the beginning of P001265. It presents mixed Hodge structures in filtration and split forms, then interprets an extension attached to a punctured curve with two relative marked points through Green functions. The heading reads \(3/\mathrm{III}\text{-}86\), a year earlier than the retained catalogue date.')
item(669, 'P001262-P001263', 'definition', 'Mixed Hodge structures over the integers',
     r'The data are a finitely generated abelian group \(L\), an increasing rational filtration \(W\), and a decreasing complex filtration \(F\), with a pure decomposition on each weight quotient.',
     r'An integral mixed Hodge structure consists of a finitely generated abelian group \(L\), a finite increasing filtration \(W\) on \(L_{\mathbb Q}\), and a finite decreasing filtration \(F\) on \(L_{\mathbb C}\), such that \(\operatorname{Gr}^W_m L_{\mathbb Q}\) with the induced filtration is pure of weight \(m\): \(\operatorname{Gr}^W_m L_{\mathbb C}=\bigoplus_{p+q=m}H^{p,q}\) and \(\overline{H^{p,q}}=H^{q,p}\). Tensoring kills torsion, which is retained only in the underlying integral group.',
     r'This is Deligne\textquotesingle s definition, published in \citet[\S2.3]{deligne1971hodge}. It is exposition in this talk.',
     ['deligne1971hodge'], literal='correct')
item(669, 'P001263', 'construction', 'Real splitting and a lowering endomorphism',
     r'The alternative description uses \(L_{\mathbb C}=\bigoplus L^{p,q}\), conjugate symmetry, an endomorphism \(N\) with \(\overline N=-N\), \(N(L^{p,q})\subset\bigoplus_{a<p,b<q}L^{a,b}\), and \(F=e^N F_{\mathrm{split}}\).',
     r'For a real mixed Hodge structure there is a canonical real-split mixed Hodge filtration and a unique real endomorphism \(\delta\) of strictly negative bidegrees such that \(F=e^{i\delta}F_{\mathrm{split}}\). Thus the notebook\textquotesingle s \(N\) is \(i\delta\). It is nilpotent by the strict bidegree inequalities. It is not the logarithm of geometric monodromy merely because it is denoted \(N\). Rationality is required of \(W\); conjugation alone gives only a real subspace.',
     r'The real-splitting result is stated in \citet[Theorem 1.15]{cattanikaplan1989degenerating}, referring to the 1986 work of Cattani--Kaplan--Schmid. The scan confirms the anti-real condition and the strict double inequality.',
     ['cattanikaplan1989degenerating', 'cattanikaplanschmid1986degeneration'], reconstruction=r'The canonical-splitting interpretation identifies the unnamed lowering operator. The notebook\textquotesingle s apparent inference from real to rational is not valid.', literal='correct with missing hypotheses')
item(669, 'P001263', 'claim', 'Purity for smooth complete varieties and the direction of the weight filtration',
     r'Example 1 says that a smooth complex manifold \(C\) has pure \(H^a\) of weight \(a\), and writes \(W_a=H^a\), \(W_{a+1}=0\).',
     r'For a smooth projective complex variety (or compact K\"ahler manifold), \(H^a\) carries a pure Hodge structure of weight \(a\). With increasing weights the conditions are \(W_{a-1}=0\) and \(W_a=H^a\). Smooth nonproper algebraic varieties generally have mixed cohomology, and arbitrary complex manifolds need not carry the claimed structure.',
     r'\citet[\S\S2.1 and 3.2]{deligne1971hodge} distinguishes the pure proper case from the mixed open case. Both the omitted compactness/projectivity hypothesis and the wrong filtration subscript are visible in the notebook.',
     ['deligne1971hodge'], literal='false as written', reconstruction=r'The compact K\"ahler or smooth projective hypothesis and the subscript \(a-1\) are editorial repairs.')
item(669, 'P001264', 'construction', 'The mixed Hodge structure of a punctured curve with relative points',
     r'The example is \(H^1(C\setminus\{x_1,x_2\},\{y_1,y_2\})\), with three weight pieces, and is drawn as a curve punctured at two points and with two relative endpoints.',
     r'Let \(C\) be a smooth connected projective complex curve of genus \(g\), and let \(x_1,x_2,y_1,y_2\) be pairwise distinct. For \(H=H^1(C\setminus\{x_1,x_2\},\{y_1,y_2\};\mathbb Q)\), one has \(\operatorname{Gr}^W_0H\simeq\mathbb Q(0)\), \(\operatorname{Gr}^W_1H\simeq H^1(C;\mathbb Q)\), and \(\operatorname{Gr}^W_2H\simeq\mathbb Q(-1)\). Hence \(\dim H=2g+2\). The homological version has dual weights and must not be interchanged silently with this cohomological statement.',
     r'This is the relative-curve instance of Deligne\textquotesingle s mixed Hodge structures, \citet[\S3.2]{deligne1971hodge}. The notebook example is explicit; the displayed graded pieces make its intended cohomological convention clear.',
     ['deligne1971hodge'], reconstruction=r'Connectedness and four distinct points are imposed; the cohomology/homology convention is fixed explicitly.')
item(669, 'P001264-P001265', 'method', 'Relative de Rham representatives and residues',
     r'Differentials on the punctured curve are taken modulo differentials of functions with equal values at \(y_1,y_2\); residues at \(x_1,x_2\) describe the upper weight quotient.',
     r'The relative de Rham complex for \((U,Y)\), \(U=C\setminus\{x_1,x_2\}\), \(Y=\{y_1,y_2\}\), computes the relative cohomology. The condition \(f(y_1)=f(y_2)\) removes the endpoint difference of \(df\). The residue theorem leaves one independent residue at the two punctures, giving the one-dimensional \(\mathbb Q(-1)\) weight quotient; the endpoint difference gives the weight-zero quotient.',
     r'The de Rham and weight-filtration construction is covered by \citet[\S3.2]{deligne1971hodge}. The equal-endpoint condition is the distinctive relative feature recorded here.',
     ['deligne1971hodge'], reconstruction=r'The relative complex, rather than an unrestricted quotient of all smooth differentials, is intended.')
item(669, 'P001264-P001265', 'claim', 'Green pairings as mixed-Hodge extension data',
     r'The lowering operator for the relative-curve example is related to an alternating sum of Green functions \(G(x_i,y_j)\).',
     r'For disjoint degree-zero divisors \(D=x_1-x_2\) and \(E=y_1-y_2\), a normalized Green kernel gives the real pairing \(G(D,E)=G(x_1,y_1)-G(x_1,y_2)-G(x_2,y_1)+G(x_2,y_2)\). This is the real height-type invariant of the corresponding biextension mixed Hodge structure. Its equality to a specified matrix coefficient of \(N\) requires choices of Tate generator, orientation, and Green normalization; those choices are not recoverable from the brief notes.',
     r'The identification belongs to Beilinson\textquotesingle s height-pairing theory, published in \citet{beilinson1987height}. This is a partial match: the precise normalization of the displayed notebook coefficient has not been verified in a primary formula.',
     ['beilinson1987height'], cls='A', match='partial', verification='indirect', confidence='medium',
     reconstruction=r'The divisors and alternating pairing are unambiguous; no exact scalar multiplier is attributed to the speaker.',
     status=r'As of November 2026, the height/biextension interpretation is established, while the notebook\textquotesingle s normalization remains an editorial uncertainty, not an open mathematical problem.')
checkpoint()

item(667, 'P001257', 'remark', 'Beilinson boundary fragment: constancy and metric normalization',
     r'The preceding Beilinson continuation says that holomorphic functions on \(M_p\), \(p>2\), are constant, and concludes that the zero-curvature metric is unique and can be obtained from a holomorphic section.',
     r'This fragment is the continuation already indexed as 1985-666.21. Even when global holomorphic functions on the relevant moduli space are constant, multiplying a flat Hermitian norm by a positive constant preserves its curvature. The conclusion is uniqueness up to that constant after the appropriate global trivialization and monodromy conditions have been supplied; zero curvature alone supplies neither trivialization nor normalization. The Mumford form is a section of a determinant-line expression, not a scalar function on unmarked moduli.',
     r'The determinant-line interpretation is \citet{beilinsonmanin1986mumford}; the precise earlier occurrence is 1985-666.21, with the metric qualification also indexed as 1985-666.14. It is included here solely because this is the first catalogue record containing P001257, not because Kontsevich spoke this fragment.',
     ['beilinsonmanin1986mumford'], literal='correct with missing hypotheses', match='partial', verification='publisher metadata checked', speaker='A. A. Beilinson (boundary fragment)',
     reconstruction=r'The record binding is editorial provenance. No new problem is created for an already indexed continuation.')
checkpoint()

talk(672, '1987-03-24', 'D. B. Fuchs', 'P001272-P001278',
     'Topology of real subspace arrangements and complexifiability',
     r'The contribution starts on P001274 and ends on P001276. Fuchs explains the Goresky--MacPherson arrangement theorem through order complexes and stratified Morse theory, including a small example and the special case of \(k\)-arrangements. Gelfand asks about realization, common complex structures, and useful cohomology bases. The manuscript date is \(24.\mathrm{III}.86\), not the catalogue year 1987.')
item(672, 'P001274', 'definition', 'Intersection posets and complements of affine arrangements',
     r'A finite collection of affine subspaces \(L_i\subset\mathbb R^n\) determines its complement and the partially ordered set of intersections.',
     r'For a finite arrangement \(\mathcal A\) of proper affine subspaces, put \(M(\mathcal A)=\mathbb R^n\setminus\bigcup\mathcal A\). Its intersection poset consists of nonempty intersections, including the empty intersection \(\widehat0=\mathbb R^n\), ordered by reverse inclusion and labeled by dimension. Parallel affine subspaces can have empty intersection, so the resulting poset need not be the lattice of a central arrangement.',
     r'The convention is explicit in \citet[\S2]{greenezaslavsky1983whitney} for hyperplanes and underlies the general arrangement treatment of \citet[Part III]{goreskymacpherson1988stratified}.',
     ['greenezaslavsky1983whitney', 'goreskymacpherson1988stratified'], reconstruction=r'Reverse inclusion, the ambient element, and dimension labels are fixed to avoid sign and interval ambiguities.')
item(672, 'P001274', 'theorem', 'Real hyperplane chambers and the Mobius count',
     r'For hyperplanes the complement has only zeroth homology, and the number of regions is given combinatorially.',
     r'For a finite real affine hyperplane arrangement, every chamber is an open convex set and therefore contractible. If \(\chi_{\mathcal A}(t)=\sum_{X\in L}\mu(\widehat0,X)t^{\dim X}\), then the number of chambers is \((-1)^n\chi_{\mathcal A}(-1)=\sum_{X\in L}|\mu(\widehat0,X)|\). Thus \(H_i(M;\mathbb Z)=0\) for \(i>0\), and \(H_0\) is free of this rank.',
     r'\citet{zaslavsky1975facing} first circulated as a 1974 MIT thesis and was published in 1975. The face-count formula is stated again as Theorem A on p.~100 of the opened primary paper \citet{greenezaslavsky1983whitney}.',
     ['zaslavsky1975facing', 'greenezaslavsky1983whitney'], literal='correct')
item(672, 'P001274-P001275', 'theorem', 'The Goresky--MacPherson additive formula',
     r'The homology of the complement is decomposed into contributions from intersections and the cohomology of their order-complex intervals.',
     r'For a finite real affine subspace arrangement and its dimension-labeled intersection poset, the additive formula may be written \[\widetilde H^i(M;\mathbb Z)\simeq\bigoplus_{X\ne\widehat0}\widetilde H_{\operatorname{codim}_{\mathbb R}X-i-2}\bigl(\Delta(\widehat0,X);\mathbb Z\bigr).\] Here \(\Delta(\widehat0,X)\) is the order complex of the open interval. This is a statement about graded groups; it does not identify the ring or assert a canonical splitting.',
     r'The full theorem appears in \citet[Part III]{goreskymacpherson1988stratified}; the stratified-Morse method was announced in the 1983 paper \citet{goreskymacpherson1983stratified}. Its group-versus-ring distinction is verified directly in \citet[Introduction and Theorem 1.2]{ziegler1993difference}, circulated in 1991--1992 and published in 1993.',
     ['goreskymacpherson1988stratified', 'goreskymacpherson1983stratified', 'ziegler1993difference'], verification='indirect', reconstruction=r'The cohomological version fixes integral duality conventions. The original 1988 book was bibliographically verified; the full 25 MB file could not be rendered by the web reader, so this entry does not claim a direct reading of that proof.', match='exact')
item(672, 'P001275', 'construction', 'Order complexes, reduced degree minus one, and the small example',
     r'Chains of a poset form a simplicial complex; an empty interval contributes in degree \(-1\). The example is three coordinate planes and a generic line in \(\mathbb R^3\).',
     r'The order complex has one simplex for each nonempty finite chain. Its augmented reduced homology convention is \(\widetilde H_{-1}(\varnothing;\mathbb Z)=\mathbb Z\), whereas ordinary negative-degree cohomology of a pair is not being used. For the three coordinate planes together with a line through the origin transverse to each plane, the complement has \(b_0=8\), \(b_1=2\), and no higher Betti numbers: the two chambers traversed by the line each lose an open radial ray.',
     r'The empty-interval convention is required by the arrangement formula in \citet[Part III]{goreskymacpherson1988stratified}. The example is explicitly present in the notebook; its stated ranks are consistent with that formula.',
     ['goreskymacpherson1988stratified'], verification='indirect', reconstruction=r'Transversality means that the line is contained in none of the coordinate planes; reduced and ordinary conventions are separated.', match='partial')
item(672, 'P001275', 'question', 'Which ordered sets occur as intersection data?',
     r'Gelfand asks whether an arbitrary partially ordered set can occur.',
     r'An intersection poset carries more data than an arbitrary order: an ambient element, intersection operations where nonempty, and codimensions constrained by linear algebra. The notes do not specify whether affine or central arrangements, dimension labels, fixed ambient dimension, or fixed codimensions are required. These are different realization problems, and the question cannot be assigned one exact classification theorem as written.',
     r'The precise distinction between geometric lattices of hyperplanes and general intersection posets is documented in \citet[\S2]{greenezaslavsky1983whitney} and \citet[Introduction]{ziegler1993difference}. The notebook formulation lacks the constraints necessary for a sharper match.',
     ['greenezaslavsky1983whitney', 'ziegler1993difference'], cls='F', speaker='I. M. Gelfand', literal='not determinable', match='thematic only', confidence='high',
     status=r'As of November 2026, no definite new open problem is extracted from this unqualified realization question.')
item(672, 'P001275-P001276', 'method', 'Stratified Morse attachment and geometric splitting',
     r'The squared distance to a generic point is used as a Morse function. The notes explicitly warn that relative homology alone does not suffice: a geometric splitting must be checked.',
     r'A generic distance function on an arrangement stratification changes sublevel topology at finitely many stratified critical values. Local Morse data determine relative homology, but a direct-sum decomposition of absolute homology needs vanishing of connecting maps and splitting of the resulting extensions. A generic long exact sequence of a pair does not supply this automatically.',
     r'The method is developed in \citet{goreskymacpherson1983stratified} and \citet[Part III]{goreskymacpherson1988stratified}. The notebook\textquotesingle s explicit caveat is mathematically essential and should be preserved.',
     ['goreskymacpherson1983stratified', 'goreskymacpherson1988stratified'], literal='correct', match='exact', reconstruction=r'The modern statement distinguishes local Morse data from the additional splitting argument.')
item(672, 'P001276', 'theorem', 'Degree concentration for k-arrangements',
     r'Each \(L_i\) has codimension \(k\), every nonempty intersection has codimension divisible by \(k\), and a contribution of rank \(m\) is asserted to occur in degree \(m(k-1)\), with rank \(|\mu|\).',
     r'For a central real \(k\)-arrangement with the stated intersection condition, the intersection lattice is geometric with rank \(r(X)=\operatorname{codim}X/k\). Its open intervals have reduced homology concentrated in degree \(r(X)-2\), free of rank \(|\mu(\widehat0,X)|\). The arrangement formula therefore places the contribution of \(X\) in complement-cohomology degree \(r(X)(k-1)\). For \(k=1\), all contributions belong to reduced degree zero, together with the ordinary base \(H^0\).',
     r'The specialization is part of \citet[Part III]{goreskymacpherson1988stratified}; \citet[Introduction]{ziegler1993difference} verifies the geometric-lattice property and additive conclusion for \(k=2\). The question mark over the degree in the scan is resolved by the standard degree shift.',
     ['goreskymacpherson1988stratified', 'ziegler1993difference'], verification='indirect', reconstruction=r'The statement is restricted to central arrangements and its rank convention is stated. The notebook has a question mark over the equality.')
item(672, 'P001276', 'problem', 'A common complex structure for a real codimension-two arrangement',
     r'After the warning that even-dimensional intersections need not give a complex arrangement, Gelfand asks: \ru{при каких усл. сущ. компл. структ., в к-рой все они станут комплексными?}',
     r'Given real codimension-two linear subspaces \(L_i\subset\mathbb R^{2d}\), determine whether there is a real linear endomorphism \(J\) with \(J^2=-I\) and \(J(L_i)=L_i\) for every \(i\). The preceding \(2\)-arrangement hypothesis further requires every intersection to have even codimension. Merely requiring codimension two for the individual subspaces is weaker. Linear complexification is also stronger than asking whether the complement is homeomorphic to that of some complex arrangement.',
     r'\citet[\S2 and Theorem 1.2]{ziegler1993difference} gives explicit distinctions between real and complex arrangements (manuscript dated December 1991; arXiv February 1992; publication 1993). \citet[Theorems 1 and 3]{batzies2007planes} classifies transverse arrangements in \(\mathbb R^4\) by simultaneous conjugation and describes the four-plane complexifiable locus. Thus the four-plane discrimination selected for annotation here is already known, not a new open problem.',
     ['ziegler1993difference', 'batzies2007planes'], cls='B', problem='GP-1986-03', speaker='I. M. Gelfand', match='partial',
     reconstruction=r'The invariant-subspace equation fixes the meaning of “complex structure.” The notebook does not restrict its question to four transverse planes; that is a bounded published specialization.', development='annotated',
     status=r'As of November 2026, the transverse \(\mathbb R^4\) four-plane case has an explicit published answer. The broad finite-family question admits a simultaneous-invariance formulation; no unproved assertion that it remains open is made.')
item(672, 'P001276', 'remark', 'The Pappus diagram and an incompletely specified obstruction',
     r'A diagram headed “Goresky\textquotesingle s example” and “Pappus\textquotesingle theorem” is followed by the assertion that complex perturbations preserve the situation and real ones need not.',
     r'Pappus\textquotesingle incidence theorem holds over both \(\mathbb R\) and \(\mathbb C\), so the sentence cannot mean that ordinary real projective lines violate Pappus. It must refer to treating real codimension-two subspaces as candidates for complex hyperplanes, where the required common complex structure is additional data. The diagram alone does not specify which real subspaces, incidences, or perturbations are intended.',
     r'\citet{ziegler1993difference} gives precise later obstructions in the relevant setting, but does not identify this particular unlabeled diagram. No exact publication match or counterexample is claimed for the fragment.',
     ['ziegler1993difference'], cls='F', literal='not determinable', match='thematic only', confidence='medium',
     status=r'As of November 2026, the illustrative intention is clear but the particular configuration remains unidentified.')
item(672, 'P001276', 'question', 'Finding useful cohomology generators and bases',
     r'Gelfand asks how to find the \ru{правильный базис когомологий}.',
     r'For a complex hyperplane arrangement with an ordering of its hyperplanes, logarithmic one-forms generate the integral cohomology ring, with circuit-boundary relations; no-broken-circuit monomials give a basis depending on that order. For real \(2\)-arrangements, the analogous relation signs carry geometric information not determined by the intersection lattice. Without a criterion for “right,” no canonical basis is demanded by the notes.',
     r'The complex presentation was published in \citet{orliksolomon1980complements}; its exact form and the signed real analogue are reproduced in \citet[Theorems 1.1 and 1.1\textquotesingle]{ziegler1993difference}. The later real result answers a definite part of the request, without manufacturing a canonical-basis conjecture.',
     ['orliksolomon1980complements', 'ziegler1993difference'], cls='B', speaker='I. M. Gelfand', reconstruction=r'An ordering and the distinction between complex and real arrangements are supplied.', match='partial',
     status=r'As of November 2026, explicit generators, relations, and order-dependent bases are available in the stated setting; the notebook does not specify an additional unresolved canonicality requirement.')
checkpoint()

talk(673, '1987-03-24', 'A. N. Varchenko', 'P001276-P001281',
     'Asymptotic mixed Hodge structures and singularity spectra',
     r'The actual contribution is P001277--P001280. It relates mixed Hodge structures to powers and logarithms in singular integrals, develops the Milnor-fibre setting, and describes the asymptotic filtration and semicontinuity of spectra. Gelfand asks for several functions and for pairs of quadrics. These are separated from the established one-function isolated-singularity theorem.')
item(673, 'P001277', 'definition', 'Pure and mixed Hodge structures in families',
     r'Varchenko recalls pure Hodge decompositions, the weight and Hodge filtrations, and the holomorphic variation of the latter.',
     r'For a smooth projective family, the cohomology local system underlies a variation of pure Hodge structure: the Hodge filtration is holomorphic and satisfies Griffiths transversality. For singular or nonproper algebraic varieties the appropriate object is mixed. A locally constant underlying topological system does not make every weight or Hodge datum a topological invariant under arbitrary changes of algebraic structure.',
     r'The foundational structures precede the talk: \citet[\S2]{deligne1971hodge}. The variation statement is background for Varchenko\textquotesingle s asymptotic construction, not a claim first made here.',
     ['deligne1971hodge'], reconstruction=r'The smooth projective and algebraic hypotheses distinguish the pure and mixed cases.', match='partial')
item(673, 'P001277', 'construction', 'An elementary nodal open-curve mixed Hodge structure',
     r'Two points of \(\mathbb C^*\) are identified, yielding two independent one-dimensional cycles and a nontrivial weight filtration.',
     r'Let \(X\) be the algebraic curve obtained from \(\mathbb C^*\) by identifying two distinct points to an ordinary node. The normalization exact sequence gives a weight-zero graph class and a weight-two puncture class: \(\dim H^1(X;\mathbb Q)=2\), \(\operatorname{Gr}^W_0H^1\simeq\mathbb Q(0)\), and \(\operatorname{Gr}^W_2H^1\simeq\mathbb Q(-1)\). The filtration identifies which combination annihilates the normalization cycle; homology carries the dual convention.',
     r'This is an elementary instance of the functorial mixed Hodge construction of \citet{deligne1971hodge}. It illustrates the distinction between topological rank and extension data.',
     ['deligne1971hodge'], reconstruction=r'The algebraic nodal quotient and cohomological convention are made explicit.', match='partial')
item(673, 'P001277-P001278', 'theorem', 'Meromorphic continuation of powers of a function',
     r'Integrals containing \(f^\lambda\) are continued in \(\lambda\), and rational powers and logarithms are related to filtrations.',
     r'For a real polynomial \(f\), use a specified positive region and extend \(f^\lambda\) by zero, or use a specified absolute-value distribution. Initially defined for sufficiently large real part of \(\lambda\), it extends meromorphically as a distribution. A Bernstein functional equation \(P(\lambda)f^{\lambda+1}=b(\lambda)f^\lambda\) gives continuation; resolution controls rational pole locations. A complex-valued \(f^\lambda\) without a chosen branch is not a single-valued distribution.',
     r'\citet[Theorems 1 and 1\textquotesingle]{bernstein1972continuation} gives the algebraic continuation argument (received June 1972, published in the 1972 volume). Its proof deliberately avoids resolution, while the stronger pole information comes from the resolution approach cited there.',
     ['bernstein1972continuation'], reconstruction=r'The sign/branch convention is essential and is supplied.')
item(673, 'P001278', 'theorem', 'Milnor fibres and the plane-curve Betti-number formula',
     r'For \(f:(\mathbb C^n,0)\to(\mathbb C,0)\) with an isolated critical point, the fibre is a bouquet of \(\mu\) spheres. In dimension two the notes write \(\mu=2g-(\text{holes})+1\).',
     r'For sufficiently small \(0<|t|\ll\varepsilon\), the Milnor fibre \(f^{-1}(t)\cap B_\varepsilon\) is homotopy equivalent to a wedge of \(\mu\) spheres of real dimension \(n-1\), with \(\mu=\dim_{\mathbb C}\mathbb C\{z_1,\ldots,z_n\}/(\partial_1f,\ldots,\partial_nf)\). For a plane-curve fibre of genus \(g\) with \(b\) boundary components, \(\mu=2g+b-1\). The notebook has both signs reversed in this last relation.',
     r'This is \citet[Chapters 5--7]{milnor1968singular}; the bouquet statement is also recalled in \citet[\S1]{steenbrink1989spectrum}. The Russian transcription and scan both confirm the erroneous sign pattern.',
     ['milnor1968singular', 'steenbrink1989spectrum'], literal='false as written', reconstruction=r'The fibre is intersected with a Milnor ball, and “holes” means boundary components. The genus formula is an emendation, not a transcription correction.')
item(673, 'P001278', 'question', 'Several functions and mixed Hodge structures',
     r'Gelfand asks about \(\int f_1^{\lambda_1}\cdots f_k^{\lambda_k}\) and whether a map \(\mathbb C^n\to\mathbb C^k\) gives something like a mixed Hodge structure.',
     r'For a specified algebraic map and algebraic fibres, their cohomology carries mixed Hodge structures; variation and degeneration require a stratification and admissibility or nearby-cycle hypotheses. Multivariate powers are governed by systems of functional equations rather than one canonical polynomial in one variable. The notes do not specify whether ordinary fibre cohomology, iterated nearby cycles, or a joint limit along a normal-crossing base is intended, and these objects need not coincide.',
     r'Deligne\textquotesingle s theory already covers algebraic fibre cohomology \citep{deligne1971hodge}; the later mixed-Hodge-module framework supplies functorial direct images and nearby-cycle operations, as stated in \citet[Theorem 1.3]{saito1989introduction}. This is a partial implementation of the request, not an exact solution to an unrecorded multivariable limit problem.',
     ['deligne1971hodge', 'saito1989introduction'], cls='B', match='partial', reconstruction=r'The modern alternatives are explicitly distinguished instead of choosing an unrecorded order of limits.',
     status=r'As of November 2026, the specified algebraic cohomology and functorial operations are established. The notebook does not determine a separate precise unresolved multivariable statement.', confidence='medium')
item(673, 'P001278', 'question', 'A map defined by two quadratic forms',
     r'Gelfand asks what arises for a map given by a pair of quadratic forms.',
     r'Given \(q_1,q_2\) on a complex vector space, one can study the affine fibres of \((q_1,q_2)\), a projective intersection of quadrics, or a pencil and its discriminant. The notebook gives no dimension, nondegeneracy, isolated-complete-intersection hypothesis, or choice among these objects. Each choice leads to a different cohomological problem.',
     r'The immediately preceding several-functions discussion identifies the motivation, but a search of the mixed-Hodge and intersection-of-quadrics context does not identify a unique assertion. The passage is therefore retained as a question with class F, rather than represented as an overlooked open theorem.',
     [], cls='F', speaker='I. M. Gelfand', literal='not determinable', match='none found', verification='unresolved lead', confidence='low',
     status=r'As of November 2026, the intended object and quantifiers cannot be recovered from this sentence.')
item(673, 'P001278-P001279', 'construction', 'Gelfand--Leray periods and logarithmic asymptotics',
     r'A holomorphic top form \(\omega\) gives \(\omega/df\) on a regular fibre, and periods along transported cycles have terms \(t^\alpha(\log t)^k\).',
     r'For an isolated hypersurface singularity and a chosen branch over a punctured disc, the period \(\int_{\delta(t)}\omega/df\) has regular-singular asymptotic expansions with rational exponents and finitely bounded logarithmic powers. Monodromy eigenvalues determine exponents modulo integers; a Jordan block of size \(s\) allows logarithmic degree at most \(s-1\), not \(s\). The exact convention for the exponent depends on using \(\omega/df\) rather than another period normalization.',
     r'This is the period setting of \citet[\S\S1--2]{varchenko1982asymptotic}, whose Russian paper appeared in 1981 and English translation in 1982 after receipt in March 1980; the announcement \citet{varchenko1980asymptotics} appeared in 1980.',
     ['varchenko1982asymptotic', 'varchenko1980asymptotics'], reconstruction=r'The branch, regular-singular condition, and block-size shift are supplied.', literal='correct with missing hypotheses')
item(673, 'P001279-P001280', 'construction', 'The asymptotic Hodge filtration and monodromy weights',
     r'The Jordan form of monodromy determines a weight filtration, while leading asymptotic terms of forms determine a Hodge filtration.',
     r'For the vanishing cohomology \(H^{n-1}\) of an isolated hypersurface singularity, the logarithm of the unipotent monodromy has its monodromy weight filtration centered at \(n-1\) on the nonunit-eigenvalue part and at \(n\) on the eigenvalue-one part. The asymptotic or limiting Hodge filtration contains information beyond the Jordan normal form. Leading exponents with their filtration multiplicities define the spectrum.',
     r'\citet{varchenko1982asymptotic} develops the asymptotic construction; \citet[\S1]{steenbrink1989spectrum} states the Hodge-theoretic definition and relates it to the earlier isolated case. The notebook is reporting established work of the speaker.',
     ['varchenko1982asymptotic', 'steenbrink1989spectrum'], reconstruction=r'The two weight centers and the distinction between a monodromy filtration and the full mixed Hodge structure are restored.')
item(673, 'P001279-P001280', 'claim', 'Bernstein roots, period exponents, and spectral numbers',
     r'Exponents in the period asymptotics are related to roots of a Bernstein polynomial and to the Hodge spectrum.',
     r'Bernstein--Sato roots, monodromy eigenvalues, and spectral numbers are related invariants with different normalizations and multiplicities. Monodromy identifies rational exponents only modulo integers. Spectral numbers also use the Hodge filtration; arbitrary exponents of every term in every asymptotic series are not simply the finite set of Bernstein roots. The precise equality proposed in the abbreviated line cannot be asserted without fixing the polynomial (including reduction), signs, shifts, and choice of leading terms.',
     r'Compare the functional equation in \citet{bernstein1972continuation}, the asymptotic filtration in \citet{varchenko1982asymptotic}, and the spectrum definition in \citet[\S1]{steenbrink1989spectrum}. These sources support the relationship, not an unqualified equality of all three multisets.',
     ['bernstein1972continuation', 'varchenko1982asymptotic', 'steenbrink1989spectrum'], match='partial', literal='correct with missing hypotheses', reconstruction=r'The finite leading invariant is separated from the full asymptotic series.', confidence='medium')
item(673, 'P001280', 'theorem', 'Semicontinuity of the singularity spectrum',
     r'The final statement invokes semicontinuity of the spectrum under perturbation.',
     r'For a deformation of an isolated hypersurface singularity, the number of spectral values in a fixed half-open interval of length one, counted with multiplicity, cannot increase when the original singularity splits into nearby isolated singularities with the same critical value: the count for the central singularity is at least the sum of the nearby counts. The interval endpoints and common-critical-value hypothesis are part of the statement.',
     r'Varchenko announced semicontinuity results in \citet{varchenko1983semicontinuity}; Steenbrink\textquotesingle s 1985 result supplies the general theorem. The precise formulation was read in the author\textquotesingle s later paper \citet[p.~166]{steenbrink1989spectrum}, which cites both works.',
     ['varchenko1983semicontinuity', 'steenbrink1985semicontinuity', 'steenbrink1989spectrum'], reconstruction=r'The interval and splitting hypotheses make the otherwise schematic final sentence precise.', literal='correct with missing hypotheses')
checkpoint()

talk(674, '1987-04-07', 'I. V. Cherednik', 'P001279-P001283',
     'RTT algebras, finite-level Yangians, and PBW questions',
     r'Cherednik starts on P001281 and finishes near the top of P001282. The rational RTT equation defines a homogeneous version of a truncated Yangian, with a finite-level PBW claim and a level-one enveloping-algebra example. Gelfand asks for a broader quadratic-algebra criterion. Kogan begins later on P001282. The manuscript heading reads \(7/\mathrm{IV}\text{-}86\).')
item(674, 'P001281', 'definition', 'The rational RTT presentation with a finite level',
     r'With \(R(u)=I+P/u\), the matrix \(L_n(u)=EI+\sum_{q=1}^nu^{-q}\sum e_{ij}\otimes E_{ji}^{q-1}\) satisfies \(R(u-v)L_1(u)L_2(v)=L_2(v)L_1(u)R(u-v)\); \(E\) is central.',
     r'After specializing the central homogenizing parameter \(E=1\), the coefficient relations define a level-\(n\) or truncated Yangian. The full Yangian allows infinitely many coefficients. The notebook uses a transposed coefficient matrix and the plus-sign \(R\) convention; both must be adjusted together when comparing with the usual \(R(u)=I-P/u\) convention.',
     r'The full RTT algebra is treated in \citet[\S1]{molevnazarovolshanski1996yangians}, first circulated in September 1994; the exact finite-level presentation is recorded in \citet[\S5.2]{futornyovsienko2005kostant}, whose March 2003 preprint credits Cherednik. This identifies the construction without conflating finite and infinite level.',
     ['molevnazarovolshanski1996yangians', 'futornyovsienko2005kostant'], cls='A', match='exact', reconstruction=r'The specialization and convention conversion are made explicit; the central homogeneous presentation is kept distinct from the usual normalized one.')
item(674, 'P001281-P001282', 'theorem', 'PBW and the current-algebra degeneration',
     r'The algebra has the size of a polynomial algebra and is a deformation of a matrix current algebra.',
     r'For the normalized truncated Yangian over characteristic zero, ordered monomials in its \(nN^2\) coefficients form a PBW basis. With coefficient degree \(q\), the associated graded algebra is a polynomial algebra with weighted generators. With degree \(q-1\), its current-algebra degeneration has the truncated current bracket. These filtrations should not be confused with an assertion that all generators have the same degree in a normalized presentation.',
     r'\citet[\S5.2, Proposition 3]{futornyovsienko2005kostant} explicitly states the finite-level polynomial associated-graded theorem and credits Cherednik\textquotesingle s 1989 paper. The two standard filtrations for the full Yangian are described in \citet[Theorem 1.22 and \S1.26]{molevnazarovolshanski1996yangians}.',
     ['futornyovsienko2005kostant', 'molevnazarovolshanski1996yangians', 'cherednik1989hidden'], cls='A', reconstruction=r'The two filtrations and the normalization \(E=1\) replace the shorthand polynomial-size claim.', match='partial')
item(674, 'P001282', 'theorem', 'Level one recovers the general linear enveloping algebra',
     r'At level one the algebra is \(U(\mathfrak{gl}_N)\).',
     r'For \(L(u)=I+u^{-1}(E_{ji})\) and the notebook\textquotesingle s matching \(R\)-matrix convention, the RTT coefficient relations are exactly \([E_{ij},E_{k\ell}]=\delta_{jk}E_{i\ell}-\delta_{i\ell}E_{kj}\). Thus the normalized level-one algebra is \(U(\mathfrak{gl}_N)\). This is an evaluation quotient of the full Yangian, not an isomorphism from the full Yangian.',
     r'\citet[\S1.16]{molevnazarovolshanski1996yangians} states the embedding/evaluation maps; the finite-level identification is explicit in \citet[\S5.2]{futornyovsienko2005kostant}.',
     ['molevnazarovolshanski1996yangians', 'futornyovsienko2005kostant'], literal='correct', match='exact')
item(674, 'P001282', 'question', 'PBW criteria beyond the Yangian example',
     r'Gelfand asks how to describe quadratic algebras with polynomial-type size or the PBW property.',
     r'One precise later version fixes a homogeneous quadratic Koszul algebra \(A=T(V)/(R)\) and asks which filtered relations with leading part \(R\) yield \(\operatorname{gr}U\simeq A\). For relations \(r-\alpha(r)-\beta(r)\), the necessary overlap conditions in degree three are sufficient when \(A\) is Koszul. This is a deformation criterion for a fixed \(A\), not a classification of every quadratic algebra with a specified Hilbert series.',
     r'\citet[Theorem 0.5 and \S3]{bravermangaitsgory1996pbw}, first circulated in November 1994 and published in 1996, establishes the Koszul PBW criterion. It implements a definite part of Gelfand\textquotesingle s broad question; the full unbounded classification is not silently declared solved or open.',
     ['bravermangaitsgory1996pbw'], cls='B', speaker='I. M. Gelfand', match='partial', reconstruction=r'The fixed quadratic algebra and Koszul hypothesis are later specifications, not words supplied by the notebook.',
     status=r'As of November 2026, the stated Koszul deformation criterion is established. The notebook contains no fixed generator number or equivalence relation defining a further classification problem.')
item(674, 'P001282', 'claim', 'Yang--Baxter consistency and a PBW converse',
     r'The notes attribute a general connection between exchange relations, PBW, and the Yang--Baxter equation to Zamolodchikov, and mention trigonometric and elliptic alternatives.',
     r'For a specified exchange algebra with an ordered reduction system, equality of the two reductions of a triple product leads to the Yang--Baxter equation. To deduce a PBW basis one must also control invertibility, admissible ordering, all ambiguities, and possible higher relations. An arbitrary quadratic quotient need not have PBW merely because a displayed operator satisfies Yang--Baxter; a universal converse needs a specified class of presentations.',
     r'The rational RTT case is proved in \citet[Theorem 1.22]{molevnazarovolshanski1996yangians}; the Koszul deformation theorem \citep{bravermangaitsgory1996pbw} shows why an extra structural hypothesis matters. No exact all-\(R\) biconditional corresponding to the unqualified sentence was identified.',
     ['molevnazarovolshanski1996yangians', 'bravermangaitsgory1996pbw'], cls='F', literal='not determinable', match='thematic only', reconstruction=r'The supported triple-overlap mechanism is separated from an unsupported universal equivalence.', confidence='medium',
     status=r'As of November 2026, the specific rational construction is established; the universal formulation remains under-specified in these notes.')
item(674, 'P001282', 'remark', 'Associativity and a three-cocycle remark',
     r'A brief remark associates a failure of associativity and a three-cocycle with Jackiw.',
     r'A group action associative only up to a phase can lead to a three-cocycle as an associativity obstruction after the relevant objects and multiplication law are specified. Here no group, coefficient module, operators, or cocycle formula is recorded. The sentence cannot be identified with a unique theorem about the RTT algebra.',
     r'Searches around the named associativity and cocycle remark locate a broad physics context but no exact notebook formula. It is retained as an unidentified remark rather than folded into the PBW theorem.',
     [], cls='F', literal='not determinable', match='none found', verification='unresolved lead', confidence='low',
     status=r'As of November 2026, the intended three-cocycle construction is not determined by the fragment.')
checkpoint()

talk(675, '1987-04-07', 'Yan I. Kogan', 'P001281-P001287',
     'Covariant bosonic string states, constraints, and string fields',
     r'The talk begins midway through P001282 and continues through P001286. It derives the oscillator and Virasoro description, explains the mass tower and physical-state constraints, and moves toward gauge symmetry and interacting string fields. Several sign, mode-index, and level labels are faithfully wrong in the notebook and are emended explicitly. The shared heading reads April 1986.')
item(675, 'P001282-P001283', 'remark', 'Regge trajectories, tension, and the field-theory limit',
     r'The string slope controls an approximately linear relation of spin and squared mass, and the limit of small slope recovers a field theory.',
     r'For the idealized string spectrum, the leading trajectory has \(J=\alpha^{\prime}M^2+a\), with tension \(T=1/(2\pi\alpha^{\prime})\) in the standard convention. The limit \(\alpha^{\prime}\to0\) at fixed low external energies suppresses massive string states; the surviving effective theory depends on the open/closed sector and gauge labels. This is a controlled low-energy expansion, not equality of complete theories at finite slope.',
     r'The low-energy gauge and gravity interpretation is already part of \citet{grossharveymartinecrohm1985heterotic}. The covariant bosonic construction in \citet{witten1986noncommutative} realizes the interacting open-string setting discussed at the end of the talk.',
     ['grossharveymartinecrohm1985heterotic', 'witten1986noncommutative'], match='partial', reconstruction=r'The sector and low-energy regime are specified.')
item(675, 'P001283', 'construction', 'The Polyakov action and conformal-gauge constraints',
     r'The action for \(x^\mu\) and the worldsheet metric is reduced to free equations with constraints after conformal gauge fixing.',
     r'The Polyakov action is \(S=(4\pi\alpha^{\prime})^{-1}\int\sqrt{|h|}h^{ab}\partial_aX^\mu\partial_bX_\mu\,d^2\sigma\). Variation of \(h\) gives the vanishing stress tensor. Gauge fixing the metric leaves this constraint and the associated ghosts; a target with one timelike coordinate gives an indefinite oscillator inner product before physical-state reduction.',
     r'This is the critical-string starting point of \citet{polyakov1981quantum}. Its quantized BRST form is written explicitly in \citet[eqs.~(1)--(7)]{furuuchiohta2006noghost}.',
     ['polyakov1981quantum', 'furuuchiohta2006noghost'], reconstruction=r'The action normalization and the distinction between gauge fixing and discarding constraints are restored.')
item(675, 'P001283-P001284', 'construction', 'Oscillator quantization and the stress-tensor modes',
     r'The modes satisfy a Heisenberg relation with the target metric, and \(L_n\) is written as a quadratic oscillator sum.',
     r'For the open bosonic string, \([\alpha_n^\mu,\alpha_m^\nu]=n\delta_{n+m,0}\eta^{\mu\nu}\). The normal-ordered matter stress-tensor modes are \(L_n=\tfrac12\sum_m:\alpha_m\cdot\alpha_{n-m}:\). The two oscillator indices must add to \(n\); the notebook line with a fixed first index \(n\) does not define the intended operator.',
     r'The exact oscillator and quadratic-mode formulas are given in \citet[eq.~(3)]{furuuchiohta2006noghost}; they are much older expository material, independently visible in the earlier seminar oscillator discussion 1985-662.1--9.',
     ['furuuchiohta2006noghost'], literal='false as written', reconstruction=r'The summation index and normal ordering are repaired; this does not change the diplomatic reading.')
item(675, 'P001284', 'theorem', 'The open-string mass spectrum and the level-one vector',
     r'The vacuum is tachyonic, the next state is massless, and higher oscillator levels form a massive tower.',
     r'With intercept one, the open critical bosonic string satisfies \(\alpha^{\prime}M^2=N-1\), where \(N=\sum_{n>0}\alpha_{-n}\cdot\alpha_n\) after the usual transverse reduction. Thus \(N=0\) is tachyonic and \(N=1\) is massless. A formula with mass itself proportional to \(N-1\), or without the square-root/sign convention, is not the same statement.',
     r'The intercept and on-shell operator are explicit in \citet[eq.~(2)]{furuuchiohta2006noghost}; the spectrum is the conventional Veneziano spectrum referred to by \citet{witten1986noncommutative}.',
     ['furuuchiohta2006noghost', 'witten1986noncommutative'], match='partial', reconstruction=r'The notebook\textquotesingle s mass normalization is replaced by the conventional squared-mass relation.')
item(675, 'P001284', 'claim', 'The Virasoro commutator and its mode index',
     r'The Virasoro commutator is displayed with \(L_{n-m}\) instead of \(L_{n+m}\).',
     r'The matter oscillators of \(D\) free bosons give \([L_n,L_m]=(n-m)L_{n+m}+\tfrac{D}{12}(n^3-n)\delta_{n+m,0}\). The sum of mode indices is forced by the stress-tensor Fourier grading. The ghost system changes the total central charge to \(D-26\).',
     r'The oscillator realization used in \citet[eqs.~(2)--(4)]{furuuchiohta2006noghost} and the anomaly calculation in \citet{belavinknizhnik1986complex} support the corrected formula. The scan shows the incorrect subscript in the notebook.',
     ['furuuchiohta2006noghost', 'belavinknizhnik1986complex'], literal='false as written', reconstruction=r'The subscript \(n+m\) is an editorial correction.')
item(675, 'P001284-P001285', 'theorem', 'Physical states, null states, and the no-ghost theorem',
     r'Physical states satisfy positive-mode constraints and the \(L_0\) equation; negative-norm states are removed in the critical dimension.',
     r'At \(D=26\) and intercept one, the physical matter subspace satisfies \(L_n\psi=0\) for \(n>0\) and \((L_0-1)\psi=0\), then is quotiented by null spurious states. In the BRST formulation, one takes the relevant cohomology of a nilpotent BRST operator. The no-ghost theorem identifies the physical space with a nonnegative-norm transverse sector, under the usual momentum hypotheses; it does not say the unreduced covariant Fock space is positive.',
     r'The theorem originates with the early no-ghost work; the opened primary proof \citet{furuuchiohta2006noghost}, first circulated in July 2006, gives the similarity-transformation argument and explicitly assumes nonzero light-cone momentum. That hypothesis is retained here.',
     ['furuuchiohta2006noghost'], reconstruction=r'The null quotient and the momentum qualification are stated explicitly.')
item(675, 'P001285', 'construction', 'Component fields and constraints at the first two levels',
     r'The string field is expanded as a scalar, a vector coefficient of \(\alpha_{-1}\), a tensor coefficient of two \(\alpha_{-1}\) modes, and a vector coefficient of \(\alpha_{-2}\). A later constraint uses the earlier vector label.',
     r'A string field has independent component fields at each oscillator level. The level-one positive-mode condition gives the massless vector transversality condition. At level two, a state \((B_{\mu\nu}\alpha_{-1}^\mu\alpha_{-1}^\nu+C_\mu\alpha_{-2}^\mu)|p\rangle\) has constraints relating \(B\) and \(C\); it does not involve the separate level-one field \(A_\mu\). The numerical factors depend on the normalization of the symmetric tensor coefficient.',
     r'The level preservation follows from the oscillator and Virasoro definitions, as used in \citet{furuuchiohta2006noghost}. The component-field interpretation is part of the string-field framework \citep{witten1986noncommutative}.',
     ['furuuchiohta2006noghost', 'witten1986noncommutative'], literal='false as written', match='partial', reconstruction=r'The level-two vector is renamed \(C\) to prevent the notebook\textquotesingle s conflation; unverified numerical factors are not copied.')
item(675, 'P001285-P001286', 'claim', 'Null-state gauge transformations and interacting nonabelian terms',
     r'The vector state changes by a momentum multiple, and the notes connect this with Yang--Mills gauge transformations including a commutator.',
     r'At the linearized massless level, a null-state or BRST-exact change induces \(\delta A_\mu=\partial_\mu\epsilon\). The nonabelian term \([A_\mu,\epsilon]\) requires interacting string fields and Chan--Paton algebra data. It cannot be deduced solely from the free positive-mode constraints.',
     r'\citet{witten1986noncommutative} constructs a nonlinear gauge-invariant open-string field theory. The distinction between its interaction and the free BRST reduction is explicit in the respective settings; the notebook elides that step.',
     ['witten1986noncommutative', 'furuuchiohta2006noghost'], literal='correct with missing hypotheses', match='partial', verification='publisher metadata checked', reconstruction=r'The free and interacting transformations are separated.')
item(675, 'P001286', 'construction', 'Associative string products and BRST string-field gauge symmetry',
     r'The talk closes with string fields, BRST ideas, and a connection with noncommutative geometry.',
     r'In the cubic open bosonic theory, the graded associative string product, a cyclic pairing, and a nilpotent BRST derivation permit an action of the form \(S=\tfrac12\langle\Psi,Q\Psi\rangle+\tfrac13\langle\Psi,\Psi*\Psi\rangle\), with gauge transformation \(\delta\Psi=Q\Lambda+\Psi*\Lambda-\Lambda*\Psi\) in the appropriate ghost degrees. Analytic definitions and normalization of the string product are additional structure; ordinary multiplication of component fields is not enough.',
     r'This identifies the framework of \citet{witten1986noncommutative}, published 5 May 1986. Only its institutional primary metadata and abstract were accessible here; the complete construction is not claimed as directly read. It predates the catalogue date but follows the manuscript April 1986 heading.',
     ['witten1986noncommutative'], match='partial', verification='publisher metadata checked', reconstruction=r'The standard cubic formulation is supplied as a contextual reconstruction, not an exact formula transcribed from this page.', confidence='medium')
checkpoint()

talk(676, '1987-04-28', 'I. V. Cherednik', 'P001285-P001290',
     'Quantum determinants, centers, and fusion',
     r'The actual talk occupies P001287--P001289. It repeats the finite-level RTT construction, defines its determinant by antisymmetrization, states the polynomial-center theorem, and uses tensor products and Young diagrams to build representations. Matrix size \(N\) and level \(n\) are repeatedly interchanged in the notebook. The date visibly reads 28 April 1986.')
item(676, 'P001287', 'definition', 'Finite-level RTT relations and a stray spectral minus sign',
     r'The normalized \(L\) has \(n\) negative powers and size \(N\). In the RTT equation only the left side has \(L^2(-\lambda_2)\).',
     r'The level-\(n\) RTT relation uses the same \(L_2(v)\) on both sides. With the single unmatched minus sign, comparison of leading coefficients generally forces unintended relations and does not give the displayed coefficient algebra. The corrected definition is the normalized one from 1986-674.1.',
     r'\citet[\S5.2]{futornyovsienko2005kostant} gives the exact truncated presentation. The Russian evidence note and scan confirm that the unmatched minus is in the manuscript.',
     ['futornyovsienko2005kostant'], cls='A', literal='false as written', reconstruction=r'The minus sign is emended from the consistency of the two sides and the immediately following coefficient relations.')
item(676, 'P001287', 'construction', 'Quantum determinant by rank-N antisymmetrization',
     r'The determinant is the scalar of the shifted tensor product \(L(\lambda+N-1)\otimes\cdots\otimes L(\lambda)\), but the projector is labeled \(\mathcal P_-^n\).',
     r'For \(N\times N\) matrices in the RTT algebra, the top exterior power \(\bigwedge^N\mathbb C^N\) is one-dimensional. With the compatible shift convention, its antisymmetrizer \(A_N\) satisfies \(A_NL_1(\lambda+N-1)\cdots L_N(\lambda)A_N=H(\lambda)A_N\). It is \(N\), the matrix size, that determines the number of factors and the exterior projector, regardless of the level \(n\).',
     r'\citet[\S\S2.2--2.7]{molevnazarovolshanski1996yangians} develops the quantum determinant. The finite-level version is explicit in \citet[eq.~(5), \S5.2]{futornyovsienko2005kostant}.',
     ['molevnazarovolshanski1996yangians', 'futornyovsienko2005kostant'], cls='A', literal='false as written', reconstruction=r'Both occurrences of the projector degree and the tensor-power exponent must be \(N\).')
item(676, 'P001287-P001288', 'theorem', 'The center of a truncated Yangian',
     r'The principal parts of \(H(\lambda)\) at \(\lambda=-i\) generate the center, with \(q=1,\ldots,n\) and the written range \(i=0,\ldots,n-1\).',
     r'For the level-\(n\) Yangian of \(\mathfrak{gl}_N\) over \(\mathbb C\), multiply the rational determinant by \(\prod_{i=0}^{N-1}(\lambda+i)^n\). The result is a monic degree-\(nN\) polynomial whose \(nN\) nonleading coefficients are algebraically independent generators of the center. Equivalently, the \(nN\) principal-part coefficients at \(0,-1,\ldots,-(N-1)\), of orders \(1,\ldots,n\), generate freely. The notebook\textquotesingle s range of pole locations must use \(N-1\).',
     r'The finite-level center theorem is stated exactly in \citet[\S5.2, after eq.~(5)]{futornyovsienko2005kostant}, crediting \citet{cherednik1989hidden} and Molev. This gives an author-publication continuation, while the original Cherednik chapter was not directly accessible in this run.',
     ['futornyovsienko2005kostant', 'cherednik1989hidden'], cls='A', literal='false as written', reconstruction=r'The partial-fraction and polynomial presentations are distinguished, and matrix size is restored in the pole range.')
item(676, 'P001288', 'construction', 'Evaluation representations and tensor products',
     r'A representation \(V\) of \(\mathfrak{gl}_N\) supplies a matrix \(L_V\); tensor products are formed by multiplying such matrices with spectral shifts.',
     r'The evaluation homomorphism from the full Yangian to \(U(\mathfrak{gl}_N)\), followed by a representation and a spectral-translation automorphism, gives an evaluation module. The coproduct \(\Delta T_{ij}(u)=\sum_aT_{ia}(u)\otimes T_{aj}(u)\) realizes tensor products as matrix products. A product of finite-level matrices has degree equal to the sum of their levels; a fixed-level quotient is not automatically a Hopf algebra.',
     r'The evaluation and coproduct statements are \citet[\S1.16 and Theorem 1.28]{molevnazarovolshanski1996yangians}. The final finite-level caution prevents carrying the full Hopf structure to the wrong quotient.',
     ['molevnazarovolshanski1996yangians'], reconstruction=r'The shift automorphism and full-versus-truncated distinction are supplied.', literal='correct with missing hypotheses')
item(676, 'P001288-P001289', 'construction', 'Young diagrams and the rational fusion procedure',
     r'A Young diagram supplies spectral shifts equal to row minus column; a product of elementary \(R\)-matrices and a Young operator produces the associated representation.',
     r'For a standard tableau of a partition of \(r\), take its contents with a fixed sign convention and ordered tensor products of fundamental evaluation modules at those contents. Fusion requires regularizing the rational products at coincident contents and applying a properly normalized tableau idempotent. The resulting subquotient realizes the corresponding polynomial \(\mathfrak{gl}_N\) representation when the number of rows is at most \(N\). A bare unnormalized row-column symmetrizer is not interchangeable with every orthogonal tableau idempotent.',
     r'This is the line of \citet{cherednik1987gelfand}, published in 1987; its role in Gelfand--Tsetlin bases and Yangian representations is specifically documented in \citet[Introduction]{molevnazarovolshanski1996yangians}. The original Duke text was blocked, so exact fusion normalizations are not certified from it.',
     ['cherednik1987gelfand', 'molevnazarovolshanski1996yangians'], cls='A', match='partial', verification='indirect', reconstruction=r'Tableau choice, regularization, dimension, and normalization are necessary additions.', confidence='medium')
item(676, 'P001289', 'remark', 'Symmetric-group normalization in the Young operator',
     r'The order of the symmetric group is written as \(n\) in a normalization discussion.',
     r'The symmetric group on \(n\) letters has order \(n!\). Averaging over a finite group uses its actual order; Young symmetrizers also require their own hook-length normalization to become idempotents. Replacing every such normalization merely by \(n!\) would therefore overcorrect the passage.',
     r'The tensor and tableau context is the fusion construction of \citet{cherednik1987gelfand}. The group-order slip is elementary and visible in the manuscript; no new theorem is claimed.',
     ['cherednik1987gelfand'], literal='false as written', match='partial', verification='indirect', reconstruction=r'Only the group order is emended; the particular projector normalization remains convention dependent.')
checkpoint()

talk(677, '1987-05-05', 'G. I. Olshanskii', 'P001288-P001292',
     'A strong-limit enveloping algebra and its Yangian factor',
     r'The talk occupies P001290 and the beginning of P001291. It defines an enlargement of the enveloping algebra through bounded-degree, tail-invariant sequences acting on tensor representations, then identifies its central factor and Yangian factor. The exact 1987 Doklady note was presented by Gelfand on 5 May 1986, matching the manuscript heading and independently corroborating the date discrepancy.')
item(677, 'P001290', 'construction', 'The strong-limit completion on tame tensor representations',
     r'Sequences in \(U(\mathfrak o(n))\) have bounded degrees, commute with a fixed tail orthogonal subgroup, and converge strongly in every tensor representation; sequences are identified by their limits.',
     r'Fix \(m\). Consider uniformly bounded PBW-degree sequences in the tail centralizers whose actions have strong limits in every specified tame tensor representation of the infinite classical group. Quotient by equality of all these representation limits; componentwise operations give an algebra \(A_m\), and \(A=\bigcup_mA_m\). The representation family and the bounded-degree condition are part of the definition, not dispensable analytic decoration.',
     r'\citet[\S1, Theorems 1--2]{olshanskii1987extension} gives precisely this strong-limit construction and an equivalent bounded-degree projective-limit construction using \(\mathfrak{gl}_n\) centralizers. It was presented 5 May 1986, received 22 May 1986, published in Russian in 1987, and translated in 1988.',
     ['olshanskii1987extension'], cls='A', literal='correct with missing hypotheses', reconstruction=r'The exact tame representation class from the paper supplies the unspecified universal quantifier over representations.')
item(677, 'P001290-P001291', 'theorem', 'The polynomial central factor and the ordinary Yangian',
     r'The stable algebra with \(m\) distinguished coordinates is written as a polynomial algebra in central elements tensored with \(Y(\mathfrak{gl}_m)\).',
     r'For the preceding strong-limit completion, \(A_0=Z(A)\) is a polynomial algebra in the stable shifted power sums, and \(A_m\simeq A_0\otimes Y(\mathfrak{gl}_m)\). This is the ordinary type-A Yangian, despite the initial orthogonal-group description. It is not the different projective-limit orthogonal centralizer construction that yields twisted Yangians.',
     r'\citet[Theorems 3 and 10]{olshanskii1987extension} states both assertions exactly. The 1987 paper, with its 1986 presentation date, settles the identification directly; the later twisted-Yangian framework must not be substituted for its completion.',
     ['olshanskii1987extension'], cls='A', literal='correct', reconstruction=r'The completion is explicitly tied to 1986-677.1 to prevent a false type correction.')
item(677, 'P001291', 'theorem', 'Orthogonal, symplectic, and unitary versions',
     r'The same algebra \(A\) arises for orthogonal and symplectic infinite groups, while the unitary case gives \(A\otimes A\).',
     r'In the tame strong-limit enlargement described in the cited paper, the \(SO(\infty)\) and \(Sp(\infty)\) constructions give the same abstract algebra \(A\); the corresponding \(U(\infty)\) enlargement has two factors. This comparison concerns that representation-theoretic completion, not an isomorphism between the finite-rank Lie algebras or their ordinary enveloping algebras.',
     r'The assertion appears explicitly in the opening paragraph of \citet{olshanskii1987extension}. The exact primary text confirms what might otherwise look like a transcription error.',
     ['olshanskii1987extension'], cls='A', literal='correct with missing hypotheses', reconstruction=r'The domain of the comparison is restored.')
item(677, 'P001291', 'method', 'The small-m cases as a test of the construction',
     r'Gelfand asks first for \(m=0\) and \(m=1\).',
     r'The \(m=0\) case isolates the stable central algebra. In the ordinary RTT presentation, \(Y(\mathfrak{gl}_1)\) is commutative, so \(m=1\) tests the first nontrivial centralizer without matrix commutator complications. This is a request for explanatory base cases, not an unresolved classification.',
     r'The central description and factorization are \citet[Theorems 3 and 10]{olshanskii1987extension}; the rank-one observation follows from the displayed scalar RTT relation.',
     ['olshanskii1987extension'], cls='A', speaker='I. M. Gelfand', match='exact', reconstruction=r'The two base cases are interpreted within the published completion.')
checkpoint()

talk(678, '1987-05-05', 'I. V. Cherednik', 'P001290-P001294',
     'Highest weights and quantum characteristic polynomials',
     r'The continuation starts midway through P001291 and runs to the end of P001292. It evaluates the quantum determinant in a highest-weight representation and compares it with ordinary determinants, including a two-dimensional antisymmetrizer calculation. The later year heading and September material on the catalogue range are separate records.')
item(678, 'P001291', 'definition', 'Polynomial highest weights and the highest-weight line',
     r'A representation is labeled by \(m_1\geq\cdots\geq m_N\geq0\), and a vector invariant under upper triangular unipotents is described as unique.',
     r'Finite-dimensional polynomial irreducible \(GL_N(\mathbb C)\) representations are indexed by partitions with at most \(N\) parts. The upper-unipotent invariants form a one-dimensional highest-weight space. A nonzero vector in that space is unique only up to multiplication by a scalar; a literal unique vector requires a normalization.',
     r'This is the classical highest-weight setup used in the central-character calculation of \citet[\S2.11]{molevnazarovolshanski1996yangians}.',
     ['molevnazarovolshanski1996yangians'], literal='correct with missing hypotheses', reconstruction=r'“Unique” is replaced by “unique line.”')
item(678, 'P001291-P001292', 'theorem', 'The quantum determinant on a highest-weight module',
     r'The central series acts by \(\prod_i(\lambda+N+m_i-i)/(\lambda+N-i)\).',
     r'For the level-one evaluation matrix with the notebook\textquotesingle s transpose and positive-shift convention, the normalized quantum determinant acts on highest weight \((m_1,\ldots,m_N)\) by \[\prod_{i=1}^N\frac{\lambda+N-i+m_i}{\lambda+N-i}.\] Removing the denominator gives the shifted characteristic polynomial; the shifts are essential and are not the ordinary determinant of a matrix of commuting entries.',
     r'The evaluation of the central quantum determinant and its Harish--Chandra interpretation appear in \citet[\S2.11]{molevnazarovolshanski1996yangians}, with the corresponding conventional change of spectral variable. The use in Gelfand--Tsetlin bases belongs to \citet{cherednik1987gelfand}.',
     ['molevnazarovolshanski1996yangians', 'cherednik1987gelfand'], cls='A', literal='correct with missing hypotheses', reconstruction=r'The evaluation, normalization, and weight convention are explicit.')
item(678, 'P001292', 'claim', 'The scalar of a two-factor antisymmetrization',
     r'For two \(2\times2\) matrices \(A,B\), the compressed operator \(\mathcal P_-(A\otimes B)\mathcal P_-\) is computed, but the displayed scalar has an inconsistent factor.',
     r'With the normalized projector \(\mathcal P_-=(I-P)/2\), the scalar on \(\bigwedge^2\mathbb C^2\) is \[\tfrac12(a_{11}b_{22}+a_{22}b_{11}-a_{12}b_{21}-a_{21}b_{12}).\] In particular \(A=B=I\) gives scalar \(1\). A factor \(1/4\), or no factor at all, cannot satisfy this normalization.',
     r'The compression is the rank-two instance of the determinant construction in \citet[\S2]{molevnazarovolshanski1996yangians}. The scalar normalization is independently checked by the identity-matrix substitution; the notebook formula is emended, not retranscribed.',
     ['molevnazarovolshanski1996yangians'], literal='false as written', match='partial', reconstruction=r'\oursComputed\ The projector normalization determines the factor. The explicit check is recorded as editorial verification.', development='annotated')
item(678, 'P001292', 'construction', 'Capelli-type central coefficients and the classical limit',
     r'The coefficients of the quantum determinant are central, and their relation to familiar determinant or trace expressions is discussed.',
     r'In \(U(\mathfrak{gl}_N)\), the coefficients of the shifted quantum characteristic polynomial are central and algebraically independent; their leading PBW symbols are the elementary invariant polynomials on matrices. Other central generators, such as properly interpreted power-sum invariants, are polynomially related to them. Unshifted determinants of noncommuting matrix entries are not automatically central.',
     r'\citet[\S2.11 and the comments in \S2.24]{molevnazarovolshanski1996yangians} identifies the Capelli and Harish--Chandra formulas and their classical antecedents. This is established invariant theory, with the Yangian packaging emphasized in Cherednik\textquotesingle s talk.',
     ['molevnazarovolshanski1996yangians'], reconstruction=r'The associated-graded meaning of the classical determinant is supplied.', literal='correct with missing hypotheses')
checkpoint()

talk(679, '', '', 'P001292-P001294', '1986',
     r'This catalogue record is a year heading, not a separate mathematical talk. The preceding page ends the May quantum-determinant discussion, while P001293 begins the explicitly dated 1 September 1986 session. The overlapping catalogue range does not transfer either contribution to this heading.', kind='heading')
checkpoint()

talk(680, '1986-09-01', 'I. M. Gelfand', 'P001292-P001296',
     'Matroids, Coxeter groups, and quadratic duality',
     r'The actual contribution begins on P001293. Gelfand discusses work with Serganova on matroids and torus strata, explains the Coxeter-group extension, and then presents quadratic algebras in connection with Beilinson and Ginzburg. The agenda also names Cherednik, but it contains no separate Gelfand--Tsetlin result on these pages. Several elementary examples retain useful manuscript errors: intersection-preserving closure, two-generator finiteness, and the distinction between the two groups of order 120.')
item(680, 'P001293', 'definition', 'Matroid closure and the exchange axiom',
     r'The closure operation is extensive and idempotent, and an exchange axiom is inserted above a deleted line. The first axiom instead asserts \(\overline{A\cap B}=\bar A\cap\bar B\).',
     r'A finite matroid closure \(\operatorname{cl}:2^E\to2^E\) is extensive, monotone, and idempotent, and satisfies exchange: if \(b\in\operatorname{cl}(A\cup\{a\})\setminus\operatorname{cl}(A)\), then \(a\in\operatorname{cl}(A\cup\{b\})\). Equality between the closure of an intersection and the intersection of closures is not an axiom and fails for ordinary vector matroids. The condition \(\operatorname{cl}(\varnothing)=\varnothing\) means loopless; it does not exclude parallel elements.',
     r'The classical closure and independence formulations are reviewed in \citet{oxleybriefly}. The notebook has substituted a stronger, false identity for monotonicity; its later linear-span example identifies the intended definition.',
     ['oxleybriefly'], literal='false as written', reconstruction=r'The exchange line is preserved, while monotonicity replaces the incorrect intersection identity.')
item(680, 'P001293', 'construction', 'Vector matroids and closed singletons',
     r'For vectors \(e_1,\ldots,e_k\), closure means membership in their linear span. The notes also write \(\bar e_i=e_i\).',
     r'A finite indexed vector configuration over a field defines a matroid on its index set by linear independence, with \(\operatorname{cl}(A)=\{i:e_i\in\operatorname{span}(e_j:j\in A)\}\). A zero vector is a loop; proportional nonzero vectors give parallel elements. For a loopless representation, every singleton is closed precisely when there are no parallel pairs; together these conditions mean simplicity. The labels, rather than the possibly repeated vectors as an unindexed set, form the ground set.',
     r'This is the standard representable-matroid construction in \citet{oxleybriefly}, and the starting case of \citet[\S2]{gelfandserganova1987combinatorial}.',
     ['oxleybriefly','gelfandserganova1987combinatorial'], literal='correct with missing hypotheses', reconstruction=r'The extra simplicity hypothesis needed by the singleton assertion is separated from looplessness.')
item(680, 'P001293-P001294', 'theorem', 'Grassmannian strata determined by Pluecker support',
     r'The Grassmannian is partitioned into strata by grouping similar diagonal-torus orbits, and a matroid determines each stratum.',
     r'For \(U\in\operatorname{Gr}(k,n)\) over a fixed field, let \(\mathcal B(U)\) be the \(k\)-subsets whose Pluecker coordinates are nonzero. These are the bases of a rank-\(k\) representable matroid. The locally closed loci with fixed \(\mathcal B(U)\) are the matroid strata. A stratum generally contains many torus orbits; arbitrary abstract matroids need not yield nonempty strata over the chosen field.',
     r'\citet[\S\S1--2]{gelfandserganova1987combinatorial}, received 30 July 1986 and published in 1987, develops precisely the common-refinement/torus-stratum interpretation. The notebook names Goresky and MacPherson as collaborators on the Grassmannian result; this attribution is retained without treating each stratum as one orbit.',
     ['gelfandserganova1987combinatorial'], cls='A', reconstruction=r'Fixed field, nonzero Pluecker support, and the distinction between a stratum and an orbit are explicit.')
item(680, 'P001294', 'definition', 'Coxeter presentations and the rank-two finiteness question',
     r'The generators satisfy \(s_i^2=1\) and \((s_is_j)^{m_{ij}}=1\). The two-generator example says the group can already be infinite although \(m_{12}\) is specified as an integer.',
     r'A Coxeter matrix has \(m_{ii}=1\) and \(m_{ij}=m_{ji}\in\{2,3,\ldots\}\cup\{\infty\}\) for \(i\ne j\); \(m_{ij}=\infty\) means no product-order relation. The rank-two group is dihedral of order \(2m_{12}\) when \(m_{12}<\infty\), and infinite dihedral when \(m_{12}=\infty\). Thus the written finite-integer example cannot be infinite.',
     r'\citet[Introduction and \S8]{coxeter1934discrete} gives the finite dihedral presentation and the general reflection-group presentation. The elementary finiteness question is settled, not a candidate open problem.',
     ['coxeter1934discrete'], literal='false as written', reconstruction=r'The allowed value \(\infty\) restores the intended infinite example.')
item(680, 'P001294', 'remark', 'Icosahedral reflections, the binary group, and the 600-cell',
     r'The notes pass from \(H_3\) of order 120 to the double cover of the order-60 rotation group in \(SU(2)\), then to 120 vertices in \(S^3\) and \(H_4\) of order \(120^2\).',
     r'The full icosahedral reflection group \(H_3\) has order 120. The rotational subgroup has order 60; its inverse image in \(SU(2)\) is the binary icosahedral group, also of order 120 but a different group. The resulting quaternionic vertices form the 600-cell, whose 600 facets are tetrahedra and whose full reflection symmetry group \(H_4\) has order 14400. The Coxeter generators are reflections, not rotations about vertices.',
     r'The finite reflection groups and their orders occur in \citet[\S9 and the table on p.~618]{coxeter1934discrete}. The notebook changes from a reflection group to a binary rotation group without marking the change; the English word “faces” must be understood as three-dimensional facets here.',
     ['coxeter1934discrete'], literal='correct with missing hypotheses', match='partial', reconstruction=r'The two order-120 groups and the dimension of the tetrahedral facets are distinguished.')
item(680, 'P001294', 'definition', 'Bruhat order and Coxeter matroids',
     r'A reduced decomposition of \(a\) occurs inside a reduced decomposition of \(b\), defining Bruhat order; \(a<^w b\) means \(w^{-1}a<w^{-1}b\). A finite subset is a flag matroid when it has a minimum for every such order.',
     r'For a finite Coxeter group \(W\), Bruhat order is characterized by a reduced expression occurring as a subsequence, not necessarily a contiguous substring. A nonempty subset of \(W\), or more generally of \(W/W_J\) for a standard parabolic subgroup, is a Coxeter matroid when it has a unique minimum in each translated Bruhat order. In the quotient case use minimal coset representatives and the induced quotient order. A merely minimal element in each finite poset would impose no meaningful condition.',
     r'\citet[\S8]{gelfandserganova1987combinatorial} introduces the Weyl/Coxeter-group generalization and its translated-order characterization. The construction was submitted before the September 1986 talk and published in 1987.',
     ['gelfandserganova1987combinatorial'], cls='A', reconstruction=r'“Minimum” is read as least element; the subword criterion and parabolic quotient are made explicit.')
item(680, 'P001295', 'theorem', 'The bases determine a finite matroid',
     r'The vector matroid is completely determined by its maximal linearly independent subsets.',
     r'For any finite matroid, the independent subsets are exactly the subsets of its bases, so its collection of bases determines its independence, rank, and closure data. Conversely a nonempty family of subsets of one ground set is a matroid basis family precisely when it satisfies the basis-exchange axiom. No realizability hypothesis is needed for this reconstruction.',
     r'The equivalence of basis and independence axioms is standard and stated in \citet{oxleybriefly}. The notebook explains the representable example, and the same assertion holds abstractly.',
     ['oxleybriefly'], literal='correct', reconstruction=r'The extension from vector matroids to arbitrary finite matroids is stated as background, not attributed as a new seminar theorem.')
item(680, 'P001295', 'claim', 'The seven-point Fano example and dependence on the field',
     r'A seven-point diagram and the seven triples \(123,165,345,275,174,376,246\) accompany the assertion that not every matroid is vector-representable.',
     r'Those triples are the lines of the Fano matroid \(F_7\). It is representable over a field exactly when that field has characteristic two. Thus it supplies a counterexample over \(\mathbb R\) or \(\mathbb C\), the preceding setting, but does not show nonrepresentability over every field. The listed triples identify the matroid more securely than the partly interrupted diagram.',
     r'\citet[Theorem 4.1]{oxleybriefly} states the exact characteristic-two criterion. The diagram is therefore a settled field-dependent example; no universal nonrepresentability claim is assigned to it.',
     ['oxleybriefly'], literal='correct with missing hypotheses', reconstruction=r'The field is restored and the combinatorial identification uses the written triples.')
item(680, 'P001295', 'definition', 'Quadratic algebras and their quadratic duals',
     r'The work of Beilinson and Ginzburg is introduced by \(A=T(V)/(W)\), with \(W\subset V\otimes V\), and \(A^!=T(V^*)/(W^\perp)\).',
     r'For a finite-dimensional vector space \(V\) over a field \(k\) and \(R\subset V\otimes V\), a connected quadratic algebra is \(A=T_k(V)/(R)\), where \((R)\) is the two-sided homogeneous ideal generated in degree two. Its quadratic dual is \(A^!=T_k(V^*)/(R^\perp)\) under the ordinary tensor pairing. The equality of this algebra with an Ext algebra requires Koszulness and is not part of the definition.',
     r'The construction predates the talk: \citet[\S2, Theorem 2.5]{priddy1970koszul} treats the cohomology relations for Koszul algebras. The exact modern convention is stated in \citet[\S2]{beilinsonginzburgsoergel1996koszul}. The notes contain definitions, not enough data to identify a particular new representation-theoretic duality theorem.',
     ['priddy1970koszul','beilinsonginzburgsoergel1996koszul'], literal='correct', reconstruction=r'The distinction between quadratic duality and the Koszul Ext identification prevents overattribution.')
item(680, 'P001295', 'construction', 'Symmetric and exterior algebras as quadratic duals',
     r'The polynomial algebra has commutator relations and its dual is the Grassmann algebra; one displayed commutator uses mismatched indices.',
     r'Over a field of characteristic different from two, the annihilator of the alternating relation space of \(S(V)\) is the symmetric relation space in \(V^*\otimes V^*\), giving \(S(V)^!=\bigwedge V^*\); dually \((\bigwedge V)^!=S(V^*)\). The exterior relations include the squares \(y_i^2=0\), as well as pairwise anticommutation. They cannot be omitted when merely writing the off-diagonal commutator pairing.',
     r'\citet[\S2.2(2)]{priddy1970koszul} records the polynomial/exterior dual cohomology calculation. The notebook is an elementary illustration of the preceding definition.',
     ['priddy1970koszul'], literal='correct with missing hypotheses', reconstruction=r'The displayed first product should be \(x_ix_k\), and diagonal relations are included. The characteristic restriction avoids a misleading symmetric-tensor shorthand in characteristic two.')
item(680, 'P001296', 'construction', 'A quadratic hypersurface and its homogenized Clifford dual',
     r'For \(A=S(V)/(\sum x_i^2)\), the orthogonal relation space consists of symmetric trace-zero matrices. The resulting relations are \(y_iy_j+y_jy_i=2\delta_{ij}h\), with \(h=y_i^2\) central.',
     r'Let \(k\) have characteristic different from two and \(V\) have basis \(x_1,\ldots,x_d\). The quadratic dual of \(S(V)/(x_1^2+\cdots+x_d^2)\) has generators \(y_i\) of degree one, off-diagonal anticommutation, and equal squares. Equivalently it is the graded Clifford algebra with a central degree-two parameter \(h\) and relations \(y_iy_j+y_jy_i=2\delta_{ij}h\). Specializing \(h=1\) gives the usual Clifford algebra; \(h\) is not set to one in the graded dual.',
     r'This is a direct example of the quadratic-dual definition in \citet[\S2]{beilinsonginzburgsoergel1996koszul}, already computed in the manuscript. No later new theorem is needed to settle it. The claim of centrality is part of the notebook calculation and follows from the equality of all squares.',
     ['beilinsonginzburgsoergel1996koszul'], literal='correct with missing hypotheses', match='partial', reconstruction=r'The ground field and degree of \(h\) are specified; the summand \(a_{ij}x_ix_k\) is read as \(a_{ij}x_ix_j\).')
checkpoint()

talk(681, '1986-09-29', 'V. L. Ginzburg', 'P001297-P001299',
     'Complete symmetric varieties and polynomial quotients of affine Hecke algebras',
     r'Ginzburg presents the De Concini--Procesi compactification of symmetric varieties, then a finite and affine Hecke-algebra construction. The top of P001298 records a problem attributed explicitly to Cherednik: replace the evaluation of the last lattice generator by a polynomial relation. Ovsienko and Kazakov start separate contributions lower on that page and are indexed with their own records. The catalogue initial is preserved although the mathematical attribution to the speaker known as Victor Ginzburg is conventional.')
item(681, 'P001297', 'construction', 'The wonderful compactification of an adjoint symmetric space',
     r'The space \(M=G/H\), with \(H\) a normalizer, has a minimal compactification \(\bar M\). The abbreviation for \(K\) is “compact subgroup”, and \(H/K\) is written as an elementary two-group.',
     r'Let \(G\) be an adjoint semisimple complex algebraic group and \(\sigma\) an involution. For the appropriate normalizer of the connected fixed subgroup, the symmetric homogeneous space admits the De Concini--Procesi wonderful projective compactification. The construction uses an algebraic symmetric subgroup; a literal arbitrary compact subgroup of a complex group does not meet these hypotheses. Finite central isogenies and the choice between connected fixed subgroup, full fixed group, and its normalizer must be specified before asserting a quotient formula.',
     r'\citet{deconciniprocesi1983complete}, published in 1983 from the 1982 Montecatini setting, is the original construction. Its exact adjoint-group setup is recalled in \citet[\S1]{chirivimaffei2004projective}. The notebook therefore presents established geometry; the isolated abbreviation does not determine an alternative real-form theorem.',
     ['deconciniprocesi1983complete','chirivimaffei2004projective'], reconstruction=r'The algebraic symmetric-space hypotheses are reconstructed. The unqualified formula for \(H/K\) is not certified for arbitrary \(K\).', match='partial', confidence='medium')
item(681, 'P001297', 'theorem', 'Boundary divisors and the orbit stratification',
     r'The compactification is smooth, has finitely many orbits, its boundary has normal crossings, and there is a unique closed orbit \(G/P\).',
     r'For the preceding wonderful compactification of rank \(r\), the boundary consists of \(r\) smooth \(G\)-stable divisors meeting with simple normal crossings. Orbit closures are precisely their partial intersections, including the empty intersection \(X\); the total intersection is the unique closed orbit, a partial flag variety \(G/P\). At a point on exactly \(k\) boundary components, suitable local coordinates give their union by \(z_1\cdots z_k=0\), and their intersection by \(z_1=\cdots=z_k=0\). The codimension of the entire boundary is one, not \(k\).',
     r'These are \citet[Theorem 3.1]{deconciniprocesi1983complete}, reproduced explicitly as \citet[Proposition 1.1]{chirivimaffei2004projective}. The latter primary text was read directly.',
     ['deconciniprocesi1983complete','chirivimaffei2004projective'], literal='correct with missing hypotheses', reconstruction=r'The union/intersection distinction repairs the notebook parenthesis defining normal crossings.')
item(681, 'P001297', 'claim', 'Restriction of line bundles to the closed orbit',
     r'The last numbered property writes an isomorphism between line bundles on \(\bar M\) and those on \(G/P\).',
     r'Restriction gives an injection \(\operatorname{Pic}(X)\hookrightarrow\operatorname{Pic}(G/P)\); the image is a specified sublattice of the weight lattice. Surjectivity onto all line bundles of the closed orbit does not hold in general. The corrected assertion determines a line bundle on \(X\) uniquely by its restriction, without claiming that every line bundle on the closed orbit extends.',
     r'The precise theorem is \citet[Proposition 8.1]{deconciniprocesi1983complete}, restated as \citet[Propositions 1.2--1.4]{chirivimaffei2004projective}; these propositions distinguish the injective restriction from its image. Thus the notebook isomorphism is an overstatement.',
     ['deconciniprocesi1983complete','chirivimaffei2004projective'], literal='false as written', reconstruction=r'The arrow is emended from isomorphism to injection.')
item(681, 'P001297', 'definition', 'The finite Hecke algebra and its commuting generators',
     r'The generators satisfy the quadratic and braid relations, with commuting condition \(j\ne i,i+1\).',
     r'For \(q\ne0\), the type-A Hecke algebra has generators \(T_1,\ldots,T_{n-1}\), relations \((T_i+1)(T_i-q)=0\), the adjacent braid relation, and \(T_iT_j=T_jT_i\) for \(|i-j|>1\). It has basis \(T_w\) indexed by \(S_n\), and at \(q=1\) specializes to the symmetric-group algebra. The written condition incorrectly permits commuting with \(T_{i-1}\).',
     r'The finite type-A case is included in \citet[\S2]{mathas2004matrix}, whose generators use the alternate convention \(T_i\mapsto-T_i\). The notebook relation requires the absolute-distance condition.',
     ['mathas2004matrix'], literal='false as written', reconstruction=r'The generator normalization is explicitly matched rather than silently changing the quadratic relation.')
item(681, 'P001297-P001298', 'construction', 'Affine Hecke generators and the evaluation map',
     r'Commuting lattice generators \(x_i\) are adjoined, with \(x_iT_i=T_ix_{i+1}-(q-1)x_{i+1}\). The proposed evaluation has \(x_n\mapsto1\), \(x_{n-1}\mapsto qT_{n-1}^2\).',
     r'For the affine Hecke algebra of \(GL_n\), use commuting invertible \(X_i\), the finite Hecke generators, and the Bernstein relations. With the written convention they imply \(T_iX_iT_i=qX_{i+1}\), together with \(T_iX_j=X_jT_i\) for \(j\ne i,i+1\). Thus evaluation \(X_n=1\) recursively gives \(X_i=qT_i^{-1}X_{i+1}T_i^{-1}\), in particular \(X_{n-1}=qT_{n-1}^{-2}\). The displayed positive square is incompatible with the displayed exchange relation.',
     r'The Jucys--Murphy elements in \citet[\S2]{mathas2004matrix} give the equivalent finite-algebra realization after reversing the indices and matching generator conventions. The inverse-square correction is an editorial consistency check of the notebook relations, not a new representation-theoretic theorem.',
     ['mathas2004matrix'], literal='false as written', match='partial', reconstruction=r'\oursComputed\ Invertibility and the nonadjacent Bernstein relation are supplied; the evaluation recursion is stated in the notebook convention.', development='annotated')
item(681, 'P001298, upper section', 'problem', 'Polynomial quotients of the affine Hecke algebra',
     r'Cherednik asks for the target algebra and homomorphism when \(x_n^2\mapsto1\), or more generally when a polynomial relation in \(x_n\) is imposed. The problem is marked unsolved.',
     r'Over \(\mathbb C\), let \(q\ne0\) and let \(p(z)=\prod_{a=1}^r(z-Q_a)\) be monic with every \(Q_a\ne0\). The quotient of the affine type-A Hecke algebra by the two-sided ideal generated by \(p(X_n)\) is a cyclotomic Hecke algebra of type \(G(r,1,n)\), after reversing the affine convention. It has dimension \(r^n n!\), with a PBW basis of bounded powers of its commuting Murphy elements times \(T_w\). Repeated roots and nonsemisimple parameters do not invalidate this basis theorem. For \(r=2\) it is the type-B Hecke case, including \(p(z)=z^2-1\).',
     r'\citet{arikikoike1994hecke} and the independent cyclotomic construction of Broue--Malle supplied this later answer. The exact presentation and Ariki--Koike basis theorem are read in \citet[\S2, (2.2)]{mathas2004matrix}, first circulated in August 2001 and published in 2004. This identifies the universal quotient; it does not claim that every such quotient admits an evaluation back into the original \(n!\)-dimensional finite Hecke algebra.',
     ['arikikoike1994hecke','mathas2004matrix'], cls='B', speaker='I. V. Cherednik', problem='GP-1986-04', literal='correct',
     reconstruction=r'The polynomial is interpreted as a universal quotient relation, which gives a definite later solution to the question of its target. Nonzero roots match the invertible affine generators.',
     status=r'As of 12 November 2026, the universal polynomial-quotient problem is settled by cyclotomic Hecke algebras and their basis theorem. No generic semisimplicity assumption is needed for this answer.')
checkpoint()
