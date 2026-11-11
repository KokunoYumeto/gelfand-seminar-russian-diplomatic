"""Author the late-record research fragments; all claims are explicit editorial decisions.
Run from this directory. Sources and checks are recorded in accompanying files.
"""
import json,csv
from pathlib import Path

HERE=Path(__file__).resolve().parent
talks=[]; items=[]; problems=[]; corrections=[]

def talk(record,date,speaker,pages,title,summary,kind='talk'):
    talks.append(dict(record=record,date=date,speaker=speaker,pages=pages,title=title,kind=kind,summary=summary))

def item(record,pages,kind,title,notes,statement,reconstruction,fate,refs,*,cls='E',literal='correct with missing hypotheses',match='exact',verification='read the result',status=None,confidence='high',speaker=None,problem='',development='annotated',worth=''):
    n=1+sum(x['record']==record for x in items)
    x=dict(id=f'1985-{record}.{n}',record=record,pages=pages,kind=kind,title=title,notes=notes,statement=statement,reconstruction=reconstruction,**{'class':cls},fate=fate,present_status=status or r'As of November 2026: established in the stated scope; the qualifications above are essential.',literal_correctness=literal,publication_match=match,verification=verification,development=development,problem=problem,worth=worth,refs=refs,confidence=confidence)
    if speaker:x['speaker']=speaker
    items.append(x)

def correction(page,place,reads,should,evidence,typ='faithful_error',applies='both'):
    corrections.append(dict(page=page,place=place,transcription_reads=reads,should_read=should,evidence=evidence,applies_to=applies,type=typ))

def save():
    for name,value in [('talks',talks),('items',items),('problems',problems)]:
        (HERE/(name+'.json')).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
    with (HERE/'corrections.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=['page','place','transcription_reads','should_read','evidence','applies_to','type']);w.writeheader();w.writerows(corrections)

talk(663,'1985-12-16','S. P. Novikov','P001245-P001248 (upper)','Two-dimensional Schrödinger operators at one energy',
     r'The talk moves from the failure of a naive all-energy analogy with one-dimensional inverse scattering to Manakov triples and the two-point Baker--Akhiezer construction. It explains potential and reality reductions by involutions of the spectral curve, Prym theta functions, and the two-dimensional analogue of KdV. The main constructions were published in 1976 and 1984. Several derivatives in the notebook are internally inconsistent; these are mathematical emendations of faithfully transcribed formulas. The final rapidly decaying assertion is less precise than the periodic construction. The actual heading is on P001245; P001244 still belongs to Feigin.')

item(663,'P001245','claim','The blanket exclusion of ordinary Lax pairs',
     r'For \(L=-\partial\bar\partial+U=-\Delta+U\), the notes say \ru{не бывает пар Лакса} and infer that \(L_t=[A,L]\) gives only Euclidean motions.',
     r'This universal assertion is false without restrictions on \(U\) and \(A\). For a smooth solution of \(u_t=6uu_x-u_{xxx}\), take \(L=-\partial_x^2-\partial_y^2+u(x,t)\) and \(A=-4\partial_x^3+6u\partial_x+3u_x\). Then \(L_t=[A,L]\), including nontravelling KdV solutions. What motivates the talk is instead the richer genuinely two-dimensional fixed-energy equation \(L_t=[A,L]+BL\).',
     r'The counterexample and its differential-operator check are ours, not a reported seminar intervention. The equality \(\partial\bar\partial=\Delta\) also requires the notebook normalization; with Wirtinger derivatives it equals \(\Delta/4\).',
     r'The one-dimensional Lax mechanism already existed; the two-dimensional fixed-energy replacement is in \citet[pp.~245--246]{manakov1976inverse}. This is not evidence for an unrestricted no-Lax theorem.',
     ['manakov1976inverse'],literal='false as written',match='partial',status=r'As of November 2026: the unrestricted wording is refuted by the displayed reduction; the intended genuinely two-dimensional obstruction is not specified sufficiently to recover a theorem.')

item(663,'P001245','remark','Counting the variables of scattering data',
     r'The scattering amplitude \(S(k_1,k_2)\), with \(|k_1|=|k_2|\), has \(2n-1\) variables; at fixed energy and \(n=2\) it has two.',
     r'For real positive energy \(E\), incoming and outgoing momenta belong to \(S_E^{n-1}\times S_E^{n-1}\), of dimension \(2n-2\). Allowing \(E>0\) adds one parameter. Thus the fixed-energy data in two dimensions and the potential on \(\mathbb R^2\) both depend on two real variables. For an actual scattering amplitude one must additionally impose sufficient decay and regularity, e.g. a smooth compactly supported real potential.',
     r'The dimension count is exact. It is not a proof of injectivity, surjectivity, or compatibility of inverse-scattering data; the notes supply none of these analytic hypotheses.',
     r'The fixed-energy viewpoint precedes the talk in \citet[\S1]{dubrovinkrichevernovikov1976schrodinger}; later analytic inverse-scattering results are discussed by \citet{novikovhenkin1987dbar}.',
     ['dubrovinkrichevernovikov1976schrodinger','novikovhenkin1987dbar'],match='partial')

item(663,'P001245','method','The Manakov L-A-B triple preserves a kernel',
     r'The notebook replaces \(L_t=[A,L]\) by \(L_t=[A,L]+BL\), or equivalently \(C_1L+LC_2\), and imposes \(L\psi=0\).',
     r'Let \(L,A,B\) be time-dependent differential operators on a common class of smooth functions. If \(L_t=[A,L]+BL\) and \(\psi_t=A\psi\), then \(\partial_t(L\psi)=(A+B)L\psi\). Consequently the zero-energy equation is formally compatible with the evolution. At energy \(E_0\), replace every occurrence of \(L\) in the right ideal by \(L-E_0\). This is a formal compatibility assertion, not a claim that the entire spectrum is isospectral.',
     r'The equation for \(\psi_t\) and the distinction between one level and the whole spectrum are supplied to make the recorded method precise.',
     r'Published before the talk in \citet{manakov1976inverse}; \citet[\S4]{dubrovinkrichevernovikov1976schrodinger} gives operator identities modulo the Schrödinger operator.',
     ['manakov1976inverse','dubrovinkrichevernovikov1976schrodinger'],literal='correct')

item(663,'P001245-P001246','construction','Two-point Baker--Akhiezer data and uniqueness',
     r'A genus-\(g\) curve \(\Gamma\), two marked points \(\infty_1,\infty_2\), local parameters \(w_i=k_i^{-1}\), and a degree-\(g\) pole divisor determine \(\psi\) with exponential singularities \(c_1e^{ik_1z}\), \(c_2e^{ik_2\bar z}\). The normalization is \(c_1=1\).',
     r'Let \(\Gamma\) be a smooth compact connected complex curve; let the distinct marked points and the effective nonspecial degree-\(g\) divisor \(D\) be disjoint. Prescribe the two indicated exponential germs and at most the poles \(D\). For parameter values where the corresponding evaluation problem is nonspecial, the normalized Baker--Akhiezer function exists uniquely. Its dependence on the flow parameters is meromorphic; exceptional theta-divisor values must be excluded from a local uniqueness assertion.',
     r'The nonspecialness condition and the exclusion of exceptional parameter values are reconstructed. Distinct poles alone do not supply them. Earlier occurrence 1975-374.4 concerns the one-point construction, not an identical two-point inverse problem.',
     r'\citet[\S3, Lemma~1]{dubrovinkrichevernovikov1976schrodinger} supplies the two-point construction (received 19 February 1976).',
     ['dubrovinkrichevernovikov1976schrodinger'])

item(663,'P001246','construction','Gauge normalization and recovery of the operator',
     r'Equations (9)--(10) read \(L=\partial\bar\partial+A\partial+B\), \(A=\bar\partial\log c_2\), following \(c_1=1\).',
     r'Fix \(\partial=\partial_z\), \(\bar\partial=\partial_{\bar z}\) and the displayed exponential asymptotics. In the gauge \(\psi\sim e^{ik_1z}(1+\xi_1/k_1+\cdots)\), \(\psi\sim c_2e^{ik_2\bar z}(1+\cdots)\), the compatible operator with leading term \(\partial\bar\partial\) is \(L=\partial\bar\partial+a\bar\partial+b\), with \(a=-\partial\log c_2\) and \(b=-i\bar\partial\xi_1\). Multiplication \(\psi\mapsto c\psi\), \(c\ne0\), conjugates the operator by \(c\).',
     r'The signs and derivative placements are rederived by cancelling the leading Laurent terms at each puncture, rather than copied from a potentially differently normalized publication. The source has both the unbarred derivative after \(A\) and the positive coefficient as transcribed.',
     r'The construction is the pre-existing one of \citet[\S3, Lemma~2]{dubrovinkrichevernovikov1976schrodinger}; the notebook formula is not consistent with its own normalization.',
     ['dubrovinkrichevernovikov1976schrodinger'],literal='false as written',match='partial')

item(663,'P001246','claim','Quasiperiodicity does not guarantee a smooth potential',
     r'\(A,B\) are called quasiperiodic for a Riemann surface in general position.',
     r'In the algebro-geometric construction the coefficients are restrictions of meromorphic theta expressions to an affine plane \(Uz+V\bar z+Z\) in a Jacobian. Periodic or quasiperiodic dependence follows when the relevant real flow lies on a real compact torus. Smooth bounded real coefficients additionally require that the real flow avoid the denominator theta divisor. General complex spectral data need not give a globally smooth or bounded real potential.',
     r'The distinction between meromorphic theta dependence and real quasiperiodicity is essential; neither smoothness nor reality follows from the notebook phrase alone.',
     r'\citet[\S3, Lemma~3 and Theorem~1]{dubrovinkrichevernovikov1976schrodinger} separates real-oval regularity from the theta formulas.',
     ['dubrovinkrichevernovikov1976schrodinger'],match='partial')

item(663,'P001246','claim','Zero magnetic flux in a periodic vector-potential gauge',
     r'The magnetic field is required to have zero flux through a period cell; the condition is called \ru{паразитное}.',
     r'If a smooth magnetic potential \(A_1dx+A_2dy\) is globally periodic on a two-torus, then its curvature \(B=\partial_xA_2-\partial_yA_1\) has integral zero over a fundamental cell, by cancellation of opposite boundary integrals. This does not exclude nonzero quantized flux for a connection on a nontrivial line bundle, which has no globally periodic vector potential of this form.',
     r'The bundle qualification is reconstructed to avoid interpreting a gauge restriction as a prohibition on magnetic flux in general.',
     r'This is an explicit starting assumption of \citet[\S1]{dubrovinkrichevernovikov1976schrodinger}, not an unresolved mathematical obstruction.',
     ['dubrovinkrichevernovikov1976schrodinger'],literal='correct with missing hypotheses')

item(663,'P001246','definition','The fixed-energy complex Fermi curve',
     r'Bloch functions form a complex set; its fixed-energy level is called the Fermi surface. A two-dimensional operator is finite-gap when that surface has finite genus.',
     r'For a doubly periodic two-dimensional elliptic Schrödinger operator, consider Bloch solutions \(\psi(x+\ell)=\chi(\ell)\psi(x)\) with complex characters \(\chi:\Lambda\to\mathbb C^*\), at a fixed energy \(E_0\). The resulting analytic spectral locus is generically a complex curve, possibly singular. In the rank-one algebro-geometric class its normalization compactifies to a finite-genus curve by adding the prescribed asymptotic points. This is a fixed-energy definition; it does not mean finitely many gaps in the full two-dimensional spectrum.',
     r'Normalization, compactification and rank-one hypotheses are made explicit. A literal finite-genus assertion about an arbitrary singular analytic set is insufficient.',
     r'\citet[\S2, Definitions~1--2]{dubrovinkrichevernovikov1976schrodinger} distinguishes algebraic and weakly algebraic operators.',
     ['dubrovinkrichevernovikov1976schrodinger'])

item(663,'P001246-P001247','theorem','The holomorphic involution removes the magnetic term',
     r'For \(\sigma^2=1\), \(\sigma(\infty_i)=\infty_i\), \(\sigma(w_i)=-w_i\), impose \(D+\sigma D\sim K+\infty_1+\infty_2\). The notes say the first-order term can then be removed.',
     r'In the smooth two-point, rank-one Baker--Akhiezer setup, assume a holomorphic involution with exactly the two marked fixed points, odd local parameters, and an admissible nonspecial divisor satisfying the displayed linear equivalence. Equivalently, the required meromorphic differential has simple poles of opposite residues at the marked points and zero divisor \(D+\sigma D\). Its residue identity forces the second leading coefficient to be constant after normalization; the constructed operator is purely potential, on the locus where the coefficients are regular.',
     r'The precise fixed-point and admissibility conditions are supplied. These are sufficient spectral-data conditions; necessity is not asserted for arbitrary operators or arbitrary redundant spectral data.',
     r'Already published in \citet[Theorem~1, smooth \(k=0\) case]{veselovnovikov1984potential}, received 5 March 1984.',
     ['veselovnovikov1984potential'],match='partial')

item(663,'P001247','theorem','Reality requires the compatible antiholomorphic involution',
     r'The commuting involutions \(\sigma,\tau\) satisfy \(\tau\infty_1=\infty_2\), \(\tau D=D\) and \(\tau w_1=\pm\overline{w_2}\). Conditions (17)--(19) are called necessary and sufficient for reality and potentiality.',
     r'With the preceding admissible potential spectral data, let \(\tau\) be an antiholomorphic involution commuting with \(\sigma\), exchanging the punctures, preserving \(D\), and satisfying the sign convention \(\tau^*w_1=-\overline{w_2}\) for the chosen oscillatory exponentials. The reconstructed potential is real wherever nonsingular. Smoothness on all of \(\mathbb R^2\) requires additional admissibility/real-locus conditions. A necessity claim must specify minimal spectral data and the involutions induced by the operator; the notebook does not do so.',
     r'The sign is not a free choice once the exponential and operator conventions are fixed. The universally quantified necessary-and-sufficient wording is therefore not retained.',
     r'The sufficient statement is exactly the smooth specialization of \citet[Theorem~2]{veselovnovikov1984potential}; the notebook is broader than that checked theorem.',
     ['veselovnovikov1984potential'],match='partial',confidence='medium')

item(663,'P001247','construction','Prym theta functions and potential spectral data',
     r'The eigenfunction is expressed through Prym theta functions, described as more numerous than Jacobian theta functions.',
     r'For the involution \(\sigma\) in the potential reduction, the connected kernel of the norm map \(\operatorname{Jac}(\Gamma)\to\operatorname{Jac}(\Gamma/\sigma)\) is the Prym variety. When the double cover is ramified at exactly two points, the admissible divisor classes form a translate of this Prym, whose dimension is half the genus of \(\Gamma\). The potential and Baker--Akhiezer function admit theta formulas on that variety, away from their polar loci.',
     r'The informal comparison with Jacobians is not a numerical count. The Prym description of the divisor family is the recoverable assertion.',
     r'\citet[Theorem~1(2)]{veselovnovikov1984potential} and \citet{veselovnovikov1984explicit} published the reduction and explicit formulas in 1984.',
     ['veselovnovikov1984potential','veselovnovikov1984explicit'])

item(663,'P001247','remark','An underspecified higher-dimensional finite-gap criterion',
     r'Under \ru{Многомерный случай}, finite-gapness is described by the existence of a nontrivial algebraic curve among all Bloch functions at arbitrary energies.',
     r'No sufficient definition is recoverable from this sentence alone. It omits the parameter space, compactification, rank, puncture asymptotics and the sense in which the curve determines the operator. Merely containing some algebraic curve is weaker than reconstructing an operator from complete spectral data on it.',
     r'The omission is retained; no classification theorem or open inverse problem is supplied on the speaker\textquotesingle s behalf.',
     r'\citet[final paragraph]{dubrovinkrichevernovikov1976schrodinger} states the need for spectral data on a curve that uniquely determine the operator. This is only a thematic comparator for the notebook shorthand.',
     ['dubrovinkrichevernovikov1976schrodinger'],cls='F',literal='not determinable',match='thematic only',confidence='low',status=r'As of November 2026: this notebook occurrence remains too underspecified for an exact theorem or a definite research problem.')

item(663,'P001247-P001248','theorem','The Novikov--Veselov evolution and exchanged derivatives',
     r'With \(L=\partial\bar\partial+V\), \(A=\partial^3+u\partial\), the notes give \(\partial u=3\bar\partial V\), \(B=\partial\bar u+\bar\partial u\), and \(V_t=(\partial^3+\partial u)V+\mathrm{c.c.}\).',
     r'For smooth real \(V\) and complex \(u\) satisfying \(\bar\partial u=3\partial V\), set \(P=\partial^3+\bar\partial^3+u\partial+\bar u\bar\partial\) and \(B=\partial u+\bar\partial\bar u\). Then \([P,L]+BL\) is multiplication by \(\partial^3V+\bar\partial^3V+\partial(uV)+\bar\partial(\bar uV)\). Thus \(L_t=[P,L]+BL\) is equivalent to this evolution of \(V\), with the auxiliary equation and boundary/normalization conditions for \(u\).',
     r'The derivative placements are corrected by a full commutator expansion. In the final expression \(\partial u\) must mean composition \(\partial\circ M_u\), not only multiplication by \(\partial u\). The symbolic check and independent polynomial substitutions are supplied in \texttt{code/check\_mathematics.py}.',
     r'The hierarchy was published before the seminar in \citet{veselovnovikov1984explicit}. The calculation here verifies the convention in this chapter, not a new evolution equation.',
     ['veselovnovikov1984explicit'],literal='false as written',match='partial')

item(663,'P001248 (upper)','claim','Rational fixed-energy soliton potentials',
     r'The talk ends by mentioning exact rational soliton solutions.',
     r'The identifiable topic is rational or determinant-form potentials for the two-dimensional Schrödinger problem at one fixed energy, with associated Novikov--Veselov evolutions. It is not the assertion that every one-dimensional multisoliton construction extends to arbitrary two-dimensional scattering data. No particular rational formula or parameter conditions are recorded here.',
     r'A specific family is not reconstructed because the note supplies none. The bibliographic identification is to a construction, not to a missing individual solution.',
     r'\citet{grinevichnovikov1985analogs} appeared in the 1985 fourth issue; \citet{grinevich1986rational} explicitly identifies rational Novikov--Veselov solitons with reflectionless fixed-energy potentials. R.~G.~Novikov here is distinct from the seminar speaker S.~P.~Novikov.',
     ['grinevichnovikov1985analogs','grinevich1986rational'],cls='B',literal='correct with missing hypotheses',match='partial',verification='publisher metadata checked',confidence='medium',status=r'As of November 2026: established explicit families; the particular solution alluded to in the notebook cannot be identified. Exact pre-talk appearance of the 1985 issue has not been established, so the chronology is not reduced to a year alone.')

item(663,'P001248 (upper)','claim','The rapidly decaying inverse problem is said to be essentially solved',
     r'\ru{Быстроубыв. задача тоже по существу решена} is followed by R.~Novikov, P.~Grinevich, Manakov.',
     r'The sentence does not specify energy, decay rate, reality, exceptional points, smallness, admissible data or uniqueness class. Therefore it does not support a theorem solving the unrestricted two-dimensional inverse-scattering problem. Fixed-energy results below the ground state and results using generalized analytic functions are distinct precisely formulated successors.',
     r'No unstated analytic hypothesis is attributed to the 1985 talk. Later work is used only to delimit the announcement.',
     r'Compare \citet{novikovhenkin1987dbar} (received 23 October 1986) and \citet{grinevichnovikov1988negative}. They do not retroactively establish all possible meanings of the notebook sentence.',
     ['novikovhenkin1987dbar','grinevichnovikov1988negative'],cls='F',literal='not determinable',match='thematic only',verification='publisher metadata checked',confidence='low',status=r'As of November 2026: the recorded global claim has no recoverable quantifiers; the checked literature treats specified energy and potential classes. It is not classified as an undeveloped problem.')

correction('P001245','Equation (1), derivative normalization',r'\(-\partial\bar\partial=-\Delta\)',r'With standard Wirtinger derivatives, \(\partial\bar\partial=\Delta_{\mathbb R^2}/4\); alternatively state a rescaled Laplacian convention.',r'The scan and Russian both contain the equality. This is a convention defect, not an OCR correction.')
correction('P001245','Equations (1)--(2), exclusion of Lax pairs',r'\ru{не бывает пар Лакса}; only rigid motions',r'Restrict the intended operator class, or retain as a heuristic; the unrestricted assertion is false.',r'The scan confirms the wording. The \(y\)-independent KdV counterexample in 1985-663.1 and code/check_mathematics.py refutes the unqualified statement.')
correction('P001246','Equations (9)--(10)',r'\(L=\partial\bar\partial+A\partial+B\), \(A=\bar\partial\log c_2\)',r'For the written asymptotics and \(c_1=1\): \(L=\partial\bar\partial-(\partial\log c_2)\bar\partial+b\).',r'Both original derivative placements were inspected in the scan. The order-\(k_1\) and order-\(k_2\) terms at the two punctures give the correction; overall sign and local-parameter rescalings must be kept consistent.')
correction('P001247','Equation (22), auxiliary coefficient and B',r'\(\partial u=3\bar\partial V\), \(B=\partial\bar u+\bar\partial u\)',r'With \(A=\partial^3+u\partial\): \(\bar\partial u=3\partial V\), \(B=\partial u+\bar\partial\bar u\).',r'The scan confirms the transcript. Comparing the coefficients of \(\partial^2\), \(\bar\partial^2\), and \(\partial\bar\partial\) in the commutator fixes the placements. Two independent symbolic checks are included.')
correction('P001248','Knizhnik heading',r'\ru{Д. Книжник. (Дима)} / D. Knizhnik (Dima)',r'Keep the notebook wording diplomatically; identify catalogue record664 as V. G. Knizhnik, without silently changing the handwritten initial or nickname.',r'The original heading visibly reads Д., and the supplied catalogue names V. G. Knizhnik. The title and content match the latter\textquotesingle s publications. The nickname conflict is unresolved provenance, not evidence for a different mathematician.','provenance')
save()

talk(664,'1985-12-16','V. G. Knizhnik','P001248 (middle)-P001252','Strings, moduli and quadratic differentials',
 r'The second talk of 16 December constructs the critical bosonic-string measure in conformal gauge, explains the role of quadratic and Beltrami differentials, and works through the torus determinant before sketching higher-genus theta formulas. Novikov intervenes about the Schottky problem. The notes combine classical geometry, Polyakov\textquotesingle s 1981 formalism, and material soon published by Belavin and Knizhnik. They do not provide a rigorous measure on all embedded surfaces. The heading says \ru{Д. Книжник. (Дима)}; the catalogue identification as V.~G.~Knizhnik is retained with the discrepancy explicit.')

item(664,'P001248','construction','The Polyakov partition function is a formal gauge integral',
 r'The sum \(Z_g=\sum_{\text{surfaces of genus }g}e^{-A}\) is rewritten as \(\int\mathcal Dg\,\mathcal DX\,e^{-\int\sqrt g g^{ab}\partial_aX\cdot\partial_bX}\).',
 r'For a fixed closed oriented smooth surface \(\Sigma\), a Riemannian metric \(g\), and a smooth map \(X:\Sigma\to\mathbb R^D\), the Polyakov action is the Dirichlet energy, with a chosen positive normalization. It is invariant under pullback by diffeomorphisms and under \(g\mapsto e^{2\sigma}g\) in dimension two. Eliminating \(g\) classically at an immersion gives the area action, up to normalization. The functional integral is a perturbative prescription modulo those symmetries, not a defined Lebesgue measure on embeddings.',
 r'Maps rather than only embeddings, the gauge quotient and the distinction between a classical equivalence and a quantum integration prescription are supplied.',
 r'Pre-existing in \citet[eqs.~(3)--(12)]{polyakov1981quantum}. Earlier occurrence 1982-569.9 already treated conformal gauge and residual moduli.',
 ['polyakov1981quantum'],match='partial')

item(664,'P001248','theorem','Critical dimension and conformal gauge leave moduli',
 r'After coordinate gauge fixing \(g_{ab}=\rho\delta_{ab}\), the notes set \(D=26\) and use the additional conformal symmetry to reduce the integral to \(M_g\).',
 r'Locally every oriented two-dimensional metric has isothermal coordinates. Globally one chooses a reference conformal structure and retains Teichm\"uller parameters, then divides by the mapping class group and residual automorphisms. In the flat-target bosonic model the matter central charge is \(D\), and that of the reparametrization ghosts is \(-26\); cancellation occurs at \(D=26\). This cancels the local Weyl anomaly, not divergences at the boundary of moduli space.',
 r'The genus-dependent automorphisms and the local/global distinction are missing from the shorthand gauge statement.',
 r'\citet[eqs.~(17)--(26)]{polyakov1981quantum}; the higher-genus implementation appears in \citet[\S2]{belavinknizhnik1986complex}.',
 ['polyakov1981quantum','belavinknizhnik1986complex'])

item(664,'P001248-P001249','construction','Quadratic differentials and their Gram matrix',
 r'Holomorphic quadratic differentials \(f^i(dz)^2\) enter the denominator \(\det(f^i,f^j)\); the written integrand in (5) is \(\rho^{-1}\overline{f^i}f^i\).',
 r'For a smooth compact curve \(C\) with metric \(\rho|dz|^2\), the Hermitian Gram matrix of a basis \(f^1,\ldots,f^N\) of \(H^0(C,K_C^2)\) is \(G_{ij}=\int_C\rho^{-1}\overline{f^i}f^j\,d^2z\), using a consistent positive area convention. For \(g\ge2\), \(N=3g-3\). The determinant transforms by \(|\det A|^2\) under a basis change and cancels the corresponding coordinate-volume factor.',
 r'The repeated \(i\) on the right of (5) is a genuine notebook error; without changing the second index to \(j\), the alleged Gram matrix has identical columns.',
 r'Classical deformation theory is used in \citet[eqs.~(2.13)--(2.19)]{belavinknizhnik1986complex}; the pairing itself predates the talk.',
 ['belavinknizhnik1986complex'],literal='false as written',match='partial')

item(664,'P001249','theorem','Products of Abelian differentials and the hyperelliptic exception',
 r'In genus two, \(\omega_1^2,\omega_1\omega_2,\omega_2^2\) form the quadratic differentials. They are said always to be obtained this way, with a surplus for \(g\ge4\).',
 r'For a smooth compact connected complex curve of genus \(g\ge2\), the multiplication map \(\operatorname{Sym}^2H^0(K_C)\to H^0(K_C^2)\) is surjective for \(g=2\), and for nonhyperelliptic \(g\ge3\). Its kernel then has dimension \((g-2)(g-3)/2\). For hyperelliptic \(g\ge3\), its image instead has dimension \(2g-1\), so the cokernel has dimension \(g-2\). Thus the unrestricted word “always” is false.',
 r'The omitted nonhyperellipticity hypothesis is decisive. On \(y^2=f(x)\), \(\deg f=2g+2\) with simple roots, the products span \(x^k(dx)^2/y^2\), \(0\le k\le2g-2\); the additional holomorphic forms \(x^j(dx)^2/y\), \(0\le j\le g-3\), prove the defect. The local calculation is included in the mathematical-check appendix.',
 r'This is Max Noether\textquotesingle s pre-existing theorem, explicitly restated in \citet[\S3.1, before Proposition~3.2]{matonevolpato2013determinantal}. That later source is a checked formulation, not the discovery date.',
 ['matonevolpato2013determinantal'],literal='false as written',match='partial')

item(664,'P001249','question','Novikov identifies the Schottky recognition problem',
 r'In the margin the Schottky problem is queried; S.~P.~Novikov says that writing the relations is equivalent to it.',
 r'Given a symmetric matrix \(\tau\) with positive definite imaginary part and the principally polarized abelian variety \(A_\tau\), characterize when it is the Jacobian of a smooth compact curve. In the KP characterization one requires \(A_\tau\) indecomposable and vectors \(U\ne0,V,W\) such that \(u=-2\partial_x^2\log\theta(Ux+Vy+Wt+Z\mid\tau)\) satisfies \(3u_{yy}=(4u_t+6uu_x-u_{xxx})_x\), as a meromorphic identity for the phase parameter \(Z\).',
 r'The recognition question is clearly identified; the KP criterion is later precision, not a formula in this occurrence. Quadratic relations on an already given canonical curve do not by themselves provide equations cutting out the Jacobian locus. The all-abelian-varieties question 1982-592.6 is related but not the same problem.',
 r'\citet{shiota1986characterization} published the KP characterization in 1986; its bibliography records separate Kyoto notes circulated in 1983. The original proof was not accessible here. The precise theorem and a later refinement were read in \citet[Introduction and Theorem~1.1]{krichever2006linear}.',
 ['shiota1986characterization','krichever2006linear'],cls='B',match='partial',speaker='S. P. Novikov',problem='GP-1985-60',status=r'As of November 2026: the recognition problem has established KP and auxiliary-linear-equation characterizations. This does not identify an unspecified finite list of the notebook\textquotesingle s relations with a full set of projective Schottky equations.')

problems.append(dict(id='GP-1985-60',title='Recognizing Jacobians among principally polarized abelian varieties',statement=r'Characterize the period matrices of smooth compact connected complex curves among symmetric matrices with positive definite imaginary part, modulo the symplectic group. Require indecomposability in the KP formulation; distinguish this recognition problem from finding a chosen explicit ideal of the Jacobian locus.',occurrences=['1985-664.5'],status=r'As of November 2026: solved in the KP-recognition sense by Shiota, with earlier circulation documented separately, and refined by Krichever\textquotesingle s auxiliary linear equation. The exact unnamed relations in the seminar margin cannot be reconstructed. Earlier items 1974-336.5 and 1982-592.6 are contextual links, not asserted occurrences of this precise question.',status_date='2026-11',refs=['shiota1986characterization','krichever2006linear']))

item(664,'P001249','construction','Beltrami coordinates are dual to quadratic differentials',
 r'Equation (6) writes \(\int\eta_i f^i dz\wedge d\bar z=\delta_i^j\), followed by \(\rho|dz+y^i\eta_i d\bar z|^2\).',
 r'The tangent space to Teichm\"uller space is \(H^1(C,T_C)\), dual by Serre duality to \(H^0(C,K_C^2)\). Choose Beltrami representatives \(\mu_i\) with \(\int_C\mu_i f^j\,d^2z=\delta_i^j\). For small parameters \(y^i\) so that \(\|\sum_i y^i\mu_i\|_\infty<1\), the metric \(\rho|dz+\sum_i y^i\mu_i d\bar z|^2\) is positive and gives a deformed conformal structure. Different representatives modulo \(\bar\partial\)-exact fields give the same infinitesimal moduli tangent.',
 r'The superscript in (6) must be \(j\), and finite coordinates require smallness and a local slice; linear representatives need not give a single global coordinate system.',
 r'\citet[eqs.~(2.13)--(2.17)]{belavinknizhnik1986complex} gives the explicit duality and local construction.',
 ['belavinknizhnik1986complex'],literal='false as written',match='partial')

item(664,'P001249','definition','Elliptic moduli and the modular fundamental domain',
 r'A torus is \(\mathbb C/(\mathbb Z+\tau\mathbb Z)\); changes of cycles act by \(SL_2(\mathbb Z)\), generated by \(\tau\mapsto\tau+1\), \(\tau\mapsto-1/\tau\). The drawn domain is called a hyperbolic triangle of angles \(0,60,60\) degrees.',
 r'For pointed complex elliptic curves, \(\tau\in\mathbb H\), and the moduli orbifold is \([\mathbb H/SL_2(\mathbb Z)]\). A closed standard domain is \(\{\tau:|\Re\tau|\le1/2,\ |\tau|\ge1\}\), with identified boundary arcs. Its two finite corner angles are \(\pi/3\), and the cusp has angle zero. The right vertical boundary is \(\Re\tau=+1/2\). The effective action is by \(PSL_2(\mathbb Z)\), while the stack retains the central automorphism.',
 r'The word triangle refers to its hyperbolic geometry, not a Euclidean straight-edged triangle. Identification of a genus-one curve with its Jacobian requires a chosen origin.',
 r'This is classical elliptic-curve geometry, also used in \citet[\S6, genus-one discussion]{belavinknizhnik1986complex}. Earlier 1968-150.8 explains why a universal family does not exist over the coarse moduli space without extra structure.',
 ['belavinknizhnik1986complex'],literal='correct with missing hypotheses')

item(664,'P001249-P001250','construction','A torus Beltrami deformation and a wedge-sign error',
 r'With \(y=\Im\tau\), the notes take \(u(z)=z+\eta\bar z/y\), \(\tau\mapsto u(\tau)/u(1)\), then identify \(d\bar\eta\wedge d\eta/y\) with \(d\tau\wedge d\bar\tau/(4y)\).',
 r'For \(|\eta|<y\), the deformed period ratio is \(\tau_\eta=(\tau+\eta\bar\tau/y)/(1+\eta/y)\). At \(\eta=0\), \(d\tau=-2i\,d\eta\), hence \(d\bar\eta\wedge d\eta=-\tfrac14d\tau\wedge d\bar\tau\). The claimed identity has the wrong sign with its written wedge orders. These are tangent-coordinate identities at the base point, not globally constant differentials.',
 r'The computation is ours and is independently checked by a real Jacobian in \texttt{code/check\_mathematics.py}. The letter \(\eta\) replaces the notebook\textquotesingle s \(y^1\) to separate it from \(\Im\tau\).',
 r'The underlying Beltrami parametrization is the classical one used in \citet[eq.~(2.14)]{belavinknizhnik1986complex}; the printed wedge identity has no exact match because its sign is wrong.',
 ['belavinknizhnik1986complex'],literal='false as written',match='partial')

item(664,'P001250','method','Gaussian modes, zero modes and the power minus twelve',
 r'The 26 scalar fields contribute \((\det^{\prime}\Delta)^{-13}\); the denominator contributes \((\det^{\prime}\Delta)^{-1}\). The zero-mode ratio is called the universe volume divided by the torus area, yielding \((\det^{\prime}\Delta)^{-12}\).',
 r'On the orthogonal complement of constants, a normalized real Gaussian with quadratic operator \(\Delta>0\) contributes \((\det^{\prime}\Delta)^{-1/2}\). Twenty-six independent scalars give exponent \(-13\); the appropriate torus ghost determinant contributes exponent \(+1\). Scalar translation zero modes and conformal Killing vector zero modes must be factored separately. Their norms, the reference area and the moduli-coordinate volume must be kept in the same convention.',
 r'The elementary nonzero-mode exponents are exact. The symbolic infinite-dimensional Gaussian is defined spectrally, and the notebook\textquotesingle s isolated zero-mode factor is not meaningful without its normalization of area and field norms.',
 r'\citet[\S2, especially eq.~(2.19)]{belavinknizhnik1986complex} displays the missing Gram factors explicitly. This implements the already existing Polyakov construction.',
 ['polyakov1981quantum','belavinknizhnik1986complex'],match='partial')

item(664,'P001250-P001251','theorem','The torus determinant depends on the area convention',
 r'The answer is \((\det^{\prime}\Delta)^{-1/2}=y^{-1/2}|\eta(\tau)|^{-2}\), with the Dedekind product.',
 r'For \(C_\tau=\mathbb C/(\mathbb Z+\tau\mathbb Z)\), \(y=\Im\tau>0\), and the positive scalar Laplacian of the unit-area metric \(|dz|^2/y\), \(\det^{\prime}\Delta=C\,y|\eta(\tau)|^4\), where \(C\) depends only on the Laplacian convention. For the metric \(|dz|^2\), of area \(y\), the answer is instead \(C\,y^2|\eta(\tau)|^4\). Here \(\eta(\tau)=q^{1/24}\prod_{n\ge1}(1-q^n)\), \(q=e^{2\pi i\tau}\).',
 r'The formula is correct after unit-area normalization, or when the determinant is divided by area. The notebook\textquotesingle s reference to “the usual” Laplacian does not specify this. Scaling follows from \(\zeta_\Delta(0)=-1\) on a flat torus with its zero mode removed.',
 r'The classical determinant evaluation goes back to \citet{raysinger1973complex}; the exact flat-metric convention was read in \citet[\S5.0.1, eq.~(5.1)]{kokotov2007polyhedral}. Original 1973 metadata, not its full proof, was checked.',
 ['raysinger1973complex','kokotov2007polyhedral'],match='partial')

item(664,'P001250-P001251','construction','The modular invariant one-loop bosonic measure',
 r'The notebook combines the invariant area element with \((\det^{\prime}\Delta)^{-12}\).',
 r'With the preceding unit-area convention and per unit target volume, the resulting density is \(C\,d^2\tau\,y^{-14}|\eta(\tau)|^{-48}=C\,d^2\tau\,y^{-14}|\Delta(\tau)|^{-2}\), with \(\Delta=\eta^{24}\). Under \(\tau\mapsto(a\tau+b)/(c\tau+d)\), the weights of \(d^2\tau\), \(y^{-14}\), and \(|\eta|^{-48}\) are respectively \(-4,28,-24\), whose sum is zero. Orbifold stabilizers and overall constants remain separate conventions.',
 r'The exponent \(-14\), not \(-13\), includes the moduli measure. This is a density, not yet a convergent value of the vacuum amplitude.',
 r'The standard one-loop expression is reproduced by \citet[\S6]{belavinknizhnik1986complex}. It reappears correctly in the later Belavin intervention on P001256, despite the conflicting P001253 formula.',
 ['belavinknizhnik1986complex'],literal='correct with missing hypotheses')

item(664,'P001251','method','Metric variation inserts the stress tensor',
 r'The variation of \((\det^{\prime}\Delta)^{-1/2}\) is computed by varying the Gaussian. The stress tensor is written with repeated free indices: \(T_{ab}=\partial_a\psi\partial_b\psi-\tfrac12g_{ab}\partial^a\psi\partial^b\psi\).',
 r'For \(S[\psi,g]=\int\sqrt g\,g^{ab}\partial_a\psi\partial_b\psi\,d^2\xi\), variation in the inverse metric gives \(\delta S=\int\sqrt g\,T_{ab}\delta g^{ab}\,d^2\xi\), where \(T_{ab}=\partial_a\psi\partial_b\psi-\tfrac12g_{ab}g^{cd}\partial_c\psi\partial_d\psi\). The regulated logarithmic Gaussian variation is the negative expectation of the corresponding action variation, plus the measure and zero-mode terms of the chosen regularization.',
 r'The density factor and contracted indices are corrected. The notebook\textquotesingle s tentative formulas for \(\delta g^{++},\delta g^{--}\) have insufficient metric conventions to fix their numerical constants.',
 r'The stress-tensor variational method is pre-existing in \citet{polyakov1981quantum}; \citet[\S3]{belavinknizhnik1986complex} implements a compatible determinant regularization.',
 ['polyakov1981quantum','belavinknizhnik1986complex'],literal='false as written',match='partial')

item(664,'P001251','definition','Point splitting, normal ordering and the projective anomaly',
 r'The coincident product \(\partial\psi(z)\partial\psi(z)\) is replaced by a contour-defined normal-ordered product; \(T\) is called an almost holomorphic differential.',
 r'In a fixed local coordinate, subtract the universal double-pole singularity from the two-point function before taking the coincident limit. The contour prescription extracts its regular Laurent coefficient. For a chiral scalar with standard normalization, the resulting stress tensor has central charge one and transforms with a Schwarzian term. A difference of projective connections, or a stress tensor after subtracting a chosen reference projective connection, is a genuine quadratic differential.',
 r'An operator, its expectation and a tensor density are different objects, although the notebook uses the same \(T\) for them. The anomalous transformation cannot be omitted on a higher-genus surface.',
 r'The local conformal-field-theory framework is in \citet{belavinpolyakovzamolodchikov1984infinite}; occurrence 1976-417.18 already distinguishes Schwarzians from quadratic differentials.',
 ['belavinpolyakovzamolodchikov1984infinite'],match='partial')

item(664,'P001252','definition','Period normalization and theta characteristics',
 r'The Abel map \(z(Q)=\int_{Q_0}^Q\omega\) and periods \(\int_{a_i}\omega_j=\delta_i^j\), \(\int_{b_i}\omega_j=\tau_{ij}\) are followed by a corrected second theta series and parity \(4\delta\cdot\varepsilon\pmod2\).',
 r'For a symplectic homology marking, \(\tau=\tau^T\) and \(\Im\tau>0\). The Abel map is valued in \(\mathbb C^g/(\mathbb Z^g+\tau\mathbb Z^g)\). For half-characteristics \(\delta,\varepsilon\in\tfrac12\mathbb Z^g/\mathbb Z^g\), define \(\theta[\delta,\varepsilon](z|\tau)=\sum_{n\in\mathbb Z^g}\exp\{\pi i(n+\delta)^T\tau(n+\delta)+2\pi i(n+\delta)^T(z+\varepsilon)\}\). Its parity is \((-1)^{4\delta^T\varepsilon}\).',
 r'The second displayed series is the coherent one. The first crossed-over exponent is not independently a definition and must not be repaired by silently combining fragments.',
 r'Classical material in \citet{fay1973theta}; the full formulation was read in \citet[\S4.1]{matonevolpato2013determinantal}.',
 ['fay1973theta','matonevolpato2013determinantal'],literal='correct with missing hypotheses')

item(664,'P001252','construction','An odd characteristic gives a half-differential only when nonsingular',
 r'For an odd characteristic the differential \(\theta^*=\sum_k\theta_{,k}(0)\omega_k\) is said to admit a square root because all zeros have order two.',
 r'Choose a nonsingular odd characteristic \(\nu\), meaning \(\nabla\theta[\nu](0)\ne0\). The nonzero holomorphic differential \(\alpha_\nu=\sum_k\partial_k\theta[\nu](0)\omega_k\) has an even zero divisor and is the square of a section \(h_\nu\) of the corresponding theta-characteristic line bundle \(L_\nu\), \(L_\nu^{\otimes2}\simeq K_C\). Zero multiplicities need only be even, not all exactly two. This is a square root in a line bundle, not a globally single-valued scalar square root.',
 r'The nonsingularity condition and the bundle interpretation are essential. An odd theta characteristic with vanishing gradient gives the zero differential, so the later quotients are then undefined.',
 r'\citet[\S4.1, immediately before eq.~(4.1)]{matonevolpato2013determinantal} states the nonsingular hypothesis and the half-differential construction, referring to the pre-existing theory in \citet{fay1973theta}.',
 ['matonevolpato2013determinantal','fay1973theta'],literal='false as written',match='partial')

item(664,'P001252','claim','The incomplete higher-genus stress-tensor formula',
 r'Equation (28) combines \(\tfrac12[\theta^{*\prime\prime}/\theta^*-\tfrac32(\theta^{*\prime}/\theta^*)^2]\), a third theta derivative divided by \(\theta^{\prime}\), and \(-\tfrac\pi2\omega_i(\Im\tau)^{-1}_{ik}\omega_k\), then calls the sum a quadratic differential.',
 r'If \(\theta^*=a(z)\) denotes the coefficient of a one-form and \(F^{\prime}=a\), the bracket is the Schwarzian \(\{F,z\}=a^{\prime\prime}/a-\tfrac32(a^{\prime}/a)^2\). The other displayed terms, interpreted using \(a\) in the denominator, transform tensorially; they cannot cancel the Schwarzian inhomogeneity. Hence the literal sum is a projective-connection-type expression, not intrinsically a quadratic differential. Its exact normalization is not recoverable without the definition of \(\theta^{\prime}\), the scalar Green function and the normal-ordering convention.',
 r'We identify the mechanism but do not fabricate a corrected coefficient formula. The prime-form/Green-function construction is a precise route to one after these choices are fixed.',
 r'\citet{knizhnik1986analytic} subsequently developed analytic fields on Riemann surfaces; publisher metadata was checked, not a formula-by-formula match. The pre-existing theta framework is \citet{fay1973theta}.',
 ['knizhnik1986analytic','fay1973theta'],cls='F',literal='false as written',match='thematic only',verification='publisher metadata checked',confidence='medium',status=r'As of November 2026: the standard higher-genus stress tensor is established, but the exact handwritten expression cannot be verified in its unspecified conventions. This is an identification limit, not an open problem.')

correction('P001248','Equation (5), Gram pairing',r'\(\overline{f^i}f^i\)',r'\(\overline{f^i}f^j\)',r'The scan confirms both superscripts are i. The left-hand indices and the Gram-matrix transformation law require j in the second factor.')
correction('P001249','Products of one-forms',r'\ru{Всегда они так получаются}',r'For genus two, or for a nonhyperelliptic curve of genus at least three.',r'The scan confirms the universal wording. Max Noether\textquotesingle s theorem has the stated exception; the explicit hyperelliptic basis gives a cokernel of dimension g-2.')
correction('P001249','Equation (6), dual basis',r'\(\int\eta_i f^i=\delta_i^j\)',r'\(\int\eta_i f^j=\delta_i^j\)',r'The scan has i on f. The free index j on the right fixes the intended duality statement.')
correction('P001249','Fundamental-domain figure, right vertical axis label',r'\(-1/2\)',r'\(+1/2\)',r'The manuscript itself repeats -1/2. The right vertical boundary is the translate of the left by +1.')
correction('P001250','Wedge identity after equation (13)',r'\(d\bar\eta\wedge d\eta=\tfrac14d\tau\wedge d\bar\tau\)',r'\(d\bar\eta\wedge d\eta=-\tfrac14d\tau\wedge d\bar\tau\)',r'The displayed fractional-linear formula gives d tau=-2i d eta. The wedge orders in both languages agree with the scan. Independently checked using real coordinates.')
correction('P001251','Equation (20), determinant normalization',r'\(\det^{\prime}\Delta=y|\eta|^4\), up to an unstated constant',r'Specify the unit-area metric, or replace the right side by \(C y^2|\eta|^4\) for \(|dz|^2\).',r'The scan and translation agree. Area scaling of the spectral determinant distinguishes the two formulas.','ambiguity')
correction('P001251','Stress-tensor definition',r'\(g_{ab}\partial^a\psi\partial^b\psi\)',r'\(g_{ab}g^{cd}\partial_c\psi\partial_d\psi\)',r'The scan explicitly has the repeated a,b. The trace contraction needs dummy indices different from the free a,b.')
correction('P001251','Metric-variation identity',r'\(\delta(\sqrt g g^{ab}\partial_a\psi\partial_b\psi)=\delta g^{ab}T_{ab}\)',r'Insert \(\sqrt g\) on the right, or define T as a tensor density.',r'Direct variation of det g supplies the density factor; the source does not define a densitized tensor.')
correction('P001252','Odd characteristic and zero orders',r'Any odd characteristic; all zeros of order 2',r'A nonsingular odd characteristic; all zeros of even order.',r'Theta gradients may vanish at singular odd characteristics, and even multiplicity need not equal two.')
correction('P001252','Sentence following equation (28)',r'All of this is a quadratic differential',r'The Schwarzian term has an inhomogeneous coordinate transformation; specify a projective connection or a subtraction convention.',r'The source gives ordinary z-derivatives and says the omega symbols omit dz. The Schwarzian composition identity prevents the unqualified tensor claim.')
save()

talk(665,'','', 'P001253 (catalogue boundary)','The catalogue heading: Year 1986',
 r'This is the catalogue heading \ru{Год 1986}, not a separate mathematical talk. The next supplied leaf begins Beilinson\textquotesingle s dated talk on 17 February 1986. No independent mathematical item is assigned to the heading, and its page reference denotes the boundary only. The academic-year item prefix remains 1985.',kind='heading')

talk(666,'1986-02-17','A. A. Beilinson','P001253-P001257','Quillen determinants, anomaly cancellation and the Mumford form',
 r'Beilinson recasts the string determinant in the language of determinant lines and their Quillen metrics. A finite-dimensional comparison exposes a dual-line inconsistency in the written norm formula. The anomaly polynomial leads to the combination \(\lambda_2\lambda_1^{-13}\); Belavin intervenes with the holomorphic measure, low-genus theta formulas and divergences. The final uniqueness argument needs an overall normalization. P001258 and P001259 begin separately headed Kontsevich and Morozov talks (catalogue records 667 and 668), and are treated as adjacent evidence in a separate supplement, not assigned to Beilinson or counted as additional records in this chapter.')

item(666,'P001253','construction','Genus expansion and the erroneous one-loop q-density',
 r'The partition function is \(Z=\sum_{g\ge0}\int_{M_g}\mu_g\). The genus-one density is written \(|dq/q|^2\Delta(q)^{-2}\log|q|^{-13}\), attributed to Kronecker (1890) and Shapiro (1972).',
 r'The genus expansion is a formal perturbative series. For the critical uncompactified bosonic string per unit target volume, the consistent one-loop density is \(C|dq/q|^2|\Delta(q)|^{-2}(-\log|q|)^{-14}\), where \(q=e^{2\pi i\tau}\), \(\Delta(q)=q\prod_{n\ge1}(1-q^n)^{24}\), and constants absorb powers of \(2\pi\). The modular fundamental domain, boundary identifications and automorphism weights remain part of the integral.',
 r'The missing modulus of \(\Delta\) and exponent \(-13\) are not compatible with the later formula on P001256. Kronecker\textquotesingle s limit formula is relevant to the determinant calculation, but the specific dates and Shapiro attribution in this sentence were not independently verified and are not treated as an exact publication match.',
 r'The corrected measure is given in \citet[\S6]{belavinknizhnik1986complex} and \citet[\S1.6.4]{bost1987determinants}; it is an old one-loop result, not a new measure computed in this talk.',
 ['belavinknizhnik1986complex','bost1987determinants'],literal='false as written',match='partial')

item(666,'P001253','definition','Dolbeault cohomology and the determinant of cohomology',
 r'For a holomorphic line bundle \(L\) on \(X\), \(H^0=\ker\bar\partial\), \(H^1=\operatorname{coker}\bar\partial=\ker\bar\partial^+\), and \(d(X,L)=\det H^0/\det H^1\).',
 r'Let \(X\) be a compact connected Riemann surface, with smooth Hermitian metrics on \(X\) and a holomorphic line bundle \(L\). Elliptic Hodge theory identifies the finite-dimensional Dolbeault cohomology with \(\ker\bar\partial_L\) and \(\ker\bar\partial_L^*\). Define \(\lambda(L)=\det H^0(X,L)\otimes\det H^1(X,L)^{-1}\). The empty top exterior power is \(\mathbb C\). The metric on the oriented surface determines its complex structure; it does not alone give a holomorphic structure on an arbitrary smooth line bundle.',
 r'The identifications use harmonic representatives and a specified holomorphic structure on \(L\). We fix the symbol \(\lambda\) for the notebook\textquotesingle s convention, which is dual to Quillen\textquotesingle s original determinant line.',
 r'The construction predates the talk; \citet[\S\S1--2]{quillen1985determinants} uses the dual convention. \citet[\S2.2]{bost1987determinants} explicitly warns about the two conventions.',
 ['quillen1985determinants','bost1987determinants'])

item(666,'P001253','definition','Line bundles of fixed degree form a Picard torsor',
 r'Holomorphic line bundles are described by an integral Chern number and \(g\) continuous parameters, a point on the Jacobian.',
 r'For a fixed compact genus-\(g\) complex curve, isomorphism classes of degree-\(d\) holomorphic line bundles form \(\operatorname{Pic}^d(X)\), a complex torus torsor of dimension \(g\) under \(\operatorname{Jac}(X)=\operatorname{Pic}^0(X)\). An identification with the Jacobian requires a reference degree-\(d\) bundle; no canonical such identification exists for arbitrary \(d\).',
 r'The parameters are complex, and the torsor qualification is needed. Changing the curve itself would introduce further moduli.',
 r'Classical Picard theory precedes the talk. The family determinant/Picard setup is used in \citet[\S2]{quillen1985determinants}; earlier occurrence 1975-385.7 concerns the Picard group and its tangent space.',
 ['quillen1985determinants'],match='partial')

item(666,'P001254','definition','Zeta regularization removes zero eigenvalues before differentiating',
 r'For \(\Delta=\bar\partial^*\bar\partial\), \(\zeta_{\Delta^{\prime}}(s)=\sum_{\lambda\ne0}\lambda^{-s}\), \(\Re s>1\), and \(\det\Delta^{\prime}=e^{-\zeta^{\prime}_{\Delta^{\prime}}(0)}\).',
 r'For a nonnegative elliptic Laplacian of order two on a smooth closed real two-dimensional manifold, sum the positive eigenvalues with multiplicities. The series converges for \(\Re s>1\) and extends meromorphically to \(\mathbb C\), regularly at zero. Its zeta determinant is \(\det^{\prime}\Delta=\exp[-\zeta_\Delta^{\prime}(0)]>0\). The zero eigenspace is kept separately in the determinant line, not assigned an artificial determinant factor.',
 r'Compactness, self-adjointness, smooth coefficients, multiplicities and analytic continuation are made explicit. The prime on \(\Delta^{\prime}\) means restriction to the positive spectrum, whereas the prime on \(\zeta^{\prime}\) means differentiation.',
 r'\citet[\S3]{quillen1985determinants}; the heat-kernel justification is spelled out in \citet[\S1.5]{bost1987determinants}.',
 ['quillen1985determinants','bost1987determinants'],literal='correct')

item(666,'P001254','construction','The Quillen norm is inverted on the notebook determinant line',
 r'The Hodge norm on \(d=\det H^0/\det H^1\) is multiplied by \(\sqrt{\det^{\prime}\Delta}\) in equation (7).',
 r'With \(\lambda=\det H^0\otimes(\det H^1)^{-1}\), the Quillen norm is \(\|\cdot\|_{Q,\lambda}=\|\cdot\|_{L^2,\lambda}(\det^{\prime}\Delta)^{-1/2}\). Equivalently, on \(\lambda^{-1}\), which is Quillen\textquotesingle s determinant-line convention, \(\|\cdot\|_Q=\|\cdot\|_{L^2}(\det^{\prime}\Delta)^{1/2}\). Squared norms use the corresponding first powers. The corrected norm is smooth in smooth elliptic families, even across jumps of kernel dimension.',
 r'The source clearly writes multiplication and clearly defines \(d=\lambda\). Its formula is therefore a dual-convention error, not a transcription error. The scalar map \(T=a:\mathbb C\to\mathbb C\) gives an independent check: under the cohomology-to-complex isomorphism, \(1\) maps to \(a^{-1}e/f\) and has norm \(|a|^{-1}\).',
 r'\citet[\S\S1,3]{quillen1985determinants}, received 18 June 1984 and published in the first 1985 issue, is the precise pre-existing source. Compare \citet[Theorem~2.1]{bost1987determinants}.',
 ['quillen1985determinants','bost1987determinants'],literal='false as written',match='partial')

item(666,'P001254-P001255','construction','Finite-dimensional determinant comparison and operator variance',
 r'For \(T:E_1\to E_2\), the cohomological determinant is canonically \(\det E_1/\det E_2\). In the invertible one-dimensional case \(\det T\) is then placed in \(E_1/E_2\).',
 r'The determinant-of-complex isomorphism \(\det\ker T\otimes(\det\operatorname{coker}T)^{-1}\simeq\det E_1\otimes(\det E_2)^{-1}\) is canonical up to the standard consistent sign convention. Under it the induced norm is the cohomology norm divided by the product of the nonzero singular values of \(T\). In contrast, \(\det T\) itself belongs to \(\operatorname{Hom}(\det E_1,\det E_2)\), the dual line. For invertible \(T\), the canonical acyclic generator maps to \((\det T)^{-1}\).',
 r'The reciprocal explains both the misplaced determinant and the preceding Quillen-norm discrepancy. A complete singular-value argument and exact diagonal examples are included in the check appendix.',
 r'The finite-dimensional model is already used in \citet[\S1]{quillen1985determinants}. It motivates the analytic construction but does not erase the dependence of the infinite-dimensional metric on the operator.',
 ['quillen1985determinants'],literal='false as written',match='partial')

item(666,'P001255','claim','Operator independence holds only in the fixed finite-dimensional model',
 r'The correct metric is said not to change when \(\bar\partial\) changes. Defining a functorial infinite-dimensional determinant independent of \(\bar\partial\) is called an unattainable ideal.',
 r'With fixed finite-dimensional Hermitian spaces, the metric on \(\det E_1\otimes(\det E_2)^{-1}\) is independent of \(T\); the isomorphism from cohomology depends on \(T\). In a family of elliptic operators, the Quillen determinant is a line bundle with generally nonzero curvature, not a fixed one-dimensional space with a flat operator-independent norm. A functorial determinant of every bare infinite-dimensional vector space, under all linear isomorphisms, is not defined by the notes.',
 r'The finite-dimensional statement is valid; its unrestricted infinite-dimensional extrapolation is not. The aspirational sentence omits a category and regularization, so it is not promoted to a new problem.',
 r'\citet[\S4]{quillen1985determinants} explicitly computes nonzero curvature in operator space. \citet[\S\S2.1--2.5]{bost1987determinants} explains the family construction.',
 ['quillen1985determinants','bost1987determinants'],literal='correct with missing hypotheses',match='partial')

item(666,'P001255','definition','Metrics on powers of the canonical bundle',
 r'For \(L=\omega^j\), sections are \(f(z)(dz)^j\), and the metric \(\rho dzd\bar z\) gives \(|(dz)^j|^2=\rho^{-j}\), \(j\in\mathbb Z\).',
 r'For every integer \(j\), use the dual and tensor-power metric on \(K_X^j\) induced from a smooth positive metric on \(T_X\). In the convention \(\|dz\|^2=\rho^{-1}\), its local norm is exactly \(\|f(dz)^j\|^2=|f|^2\rho^{-j}\). Its Dolbeault determinant line depends on the complex curve, while its Hodge and Quillen metrics also use the chosen fiber metric.',
 r'The index labels tensor powers of \(K\), not real differential-form degree. In particular negative \(j\) is meaningful.',
 r'This pre-existing tensor construction is the setup of \citet[\S\S2.5--2.6]{bost1987determinants}.',
 ['bost1987determinants'],literal='correct')

item(666,'P001255','theorem','The anomaly polynomial and its normalization',
 r'Polyakov\textquotesingle s theorem is written \(\delta\log|\cdot|_j/\delta\rho=(6j^2-6j+1)R(\rho)\); the polynomial is called the second Bernoulli polynomial.',
 r'For the Quillen metrics of \(\lambda_j=\lambda(K_X^j)\) with all bundle metrics induced from the same surface metric, conformal variation has the universal coefficient \(c_j=6j^2-6j+1\). In an explicit relative formulation, for two surface metrics \(\rho_0,\rho_1\), the ratio of Quillen norms on each fixed \(\lambda_j\) is the \(c_j\)-th power of the corresponding ratio on \(\lambda_0\). With the usual convention \(B_2(t)=t^2-t+1/6\), one has \(c_j=6B_2(j)\).',
 r'The bare functional derivative omits whether \(\rho\), \(\log\rho\), norms or squared norms are varied, and suppresses area and numerical constants. The relative formulation fixes the invariant content without assigning a false absolute coefficient.',
 r'The conformal anomaly is pre-existing; see \citet[eq.~(2.21)]{belavinknizhnik1986complex} and the precise metric comparison in \citet[Proposition~2.3]{bost1987determinants}.',
 ['belavinknizhnik1986complex','bost1987determinants'],match='partial')

item(666,'P001255','theorem','Cancellation makes the tensor-product norm metric independent',
 r'For integers \(b_i,j_i\) with \(\sum_i b_i c_{j_i}=0\), the Quillen metric on \(\bigotimes_i d(X,\omega^{j_i})^{b_i}\) depends only on complex structure.',
 r'Fix a compact complex curve, use the compatible induced metrics and determinant convention in the previous item, and allow negative tensor powers as duals. The product of relative Quillen-norm changes is \(R_0^{\sum_i b_ic_{j_i}}=1\). Thus the tensor-product norm is independent of the auxiliary smooth surface metric. It may still vary when the complex structure varies.',
 r'The conclusion follows from the conformal anomaly and must not be confused with an automatic trivialization of the resulting holomorphic line over moduli.',
 r'\citet[\S2, eq.~(2.21)]{belavinknizhnik1986complex}; \citet[\S3.1]{bost1987determinants}. The linear cancellation argument is already implicit in the notes.',
 ['belavinknizhnik1986complex','bost1987determinants'],literal='correct')

item(666,'P001255','remark','Why thirteen and twenty-six occur',
 r'The important example is \((j_1,b_1)=(2,1)\), \((j_2,b_2)=(1,-13)\); the notes infer no conformal anomaly in dimension 26.',
 r'Since \(c_1=1\) and \(c_2=13\), the product \(\lambda_2\otimes\lambda_1^{-13}\) has vanishing anomaly. Each real free scalar contributes one-half of a scalar determinant power, so 26 scalar coordinates supply the exponent 13 that cancels the reparametrization ghosts. This concerns the flat-target critical bosonic model with the stated field content.',
 r'The dimension is not a general theorem about arbitrary two-dimensional quantum theories. The elementary arithmetic is independently checked in the supplied code.',
 r'\citet{polyakov1981quantum}; the geometric relation to the Todd coefficient is explained in \citet[\S2.6]{bost1987determinants}.',
 ['polyakov1981quantum','bost1987determinants'],literal='correct')

item(666,'P001256','construction','Determinant lines form a holomorphic bundle even across cohomology jumps',
 r'For a holomorphic family \(X_M\to M\), the spaces \(d(X_t,\omega^j)\) are fibers of a holomorphic line bundle \(d_j\).',
 r'Let \(\pi:X\to S\) be a proper holomorphic submersion with compact connected one-dimensional fibers and let \(K_{X/S}\) be its relative canonical bundle. The determinant of the perfect derived direct image \(\lambda_j=\det R\pi_*K_{X/S}^j\) is a holomorphic line bundle, with the stated fiber description and base-change compatibility. The individual cohomology dimensions may jump in general determinant constructions; local finite complexes, not exterior powers of nonexistent cohomology vector bundles, define the line across jumps.',
 r'Properness, smoothness and the relative canonical bundle are supplied. The moduli stack or a local/level cover is the correct base for a universal family; the coarse moduli space need not carry one.',
 r'Pre-existing determinant functor theory is summarized precisely in \citet[\S2.2]{bost1987determinants}; Quillen\textquotesingle s analytic construction is \citet{quillen1985determinants}.',
 ['bost1987determinants','quillen1985determinants'])

item(666,'P001256','theorem','Belavin--Knizhnik curvature cancellation',
 r'Belavin and Knizhnik\textquotesingle s theorem says the canonical metric on \(\bigotimes_i d_{j_i}^{b_i}\) has zero curvature when \(\sum_i b_ic_{j_i}=0\).',
 r'For the preceding smooth holomorphic family with compatible Hermitian metrics, the family-index curvature formula in the cohomological determinant convention is \(c_1(\lambda_j,h_Q)=\tfrac{6j^2-6j+1}{12}\,\pi_*[c_1(K_{X/S},h)^2]\). Consequently every indicated anomaly-free tensor product has zero Chern curvature. This is flatness of the Chern connection; global trivial holonomy is a further issue.',
 r'The normalization uses \(c_1(L,h)=-\tfrac{i}{2\pi}\partial\bar\partial\log h(s,s)\) in a holomorphic frame. The coefficient is independently reproduced by the degree-two expansion of \(e^{jx}(1-x/2+x^2/12)\).',
 r'The result was current in the seminar and published in \citet[\S3, eqs.~(3.3)--(3.5)]{belavinknizhnik1986complex}; the later family-index formulation is \citet[Theorem~2.2 and \S3.1]{bost1987determinants}. Class B reflects the named authors of the result, while Beilinson\textquotesingle s role in its geometric formulation is explicitly acknowledged in their paper.',
 ['belavinknizhnik1986complex','bost1987determinants'],cls='B',literal='correct with missing hypotheses')

item(666,'P001256','claim','Zero curvature alone cannot normalize a metric',
 r'Theorem (19) is said to determine the canonical metric uniquely.',
 r'If \(h\) is a Hermitian metric of zero curvature, so is \(Ch\) for every \(C>0\). Locally the ratio of any two flat metrics is \(e^{2\Re f}\) for a holomorphic function \(f\). Global constancy of this ratio requires a separate argument on the chosen base; even then a positive scalar remains. Flatness of a line bundle does not itself produce a nowhere-vanishing global holomorphic section.',
 r'The counterexample by constant rescaling is independent of every analytic convention. Later P001257 narrows the ambiguity but still suppresses the scalar.',
 r'\citet[Theorem~3.3]{bost1987determinants} gives the precise statement with a genus-dependent constant, consistent with \citet[\S\S4--5]{belavinknizhnik1986complex}.',
 ['bost1987determinants','belavinknizhnik1986complex'],literal='false as written',match='partial')

item(666,'P001256','construction','The Mumford form is a section, not a global scalar function',
 r'Belavin writes the scalar/ghost determinant ratio as the squared modulus of a holomorphic function on moduli, calling it almost unique.',
 r'For \(g\ge2\), the Mumford isomorphism \(\lambda_2\simeq\lambda_1^{13}\) on the stack of smooth curves supplies a nowhere-zero section \(\mu_g\) of \(\lambda_2\lambda_1^{-13}\), unique up to the chosen normalization. Via \(H^0(K^2)\simeq T^*\mathcal M_g\), it is a top differential valued in \(\lambda_1^{-13}\). In a homology marking with period matrix \(\Omega\), the bosonic measure is locally \(C_g|\mu_g|^2/(\det\Im\Omega)^{13}\), interpreted with the Hodge frame and its transformation law.',
 r'The local coefficient is holomorphic only in a holomorphic frame. Gram determinants and zero-mode factors are suppressed by the notebook\textquotesingle s schematic ratio. The Mumford isomorphism is stronger global information than curvature zero.',
 r'\citet[\S5, theorem after eq.~(5.3)]{belavinknizhnik1986complex} gives the global formulation and credits Beilinson--Drinfeld. Beilinson subsequently coauthored \citet{beilinsonmanin1986mumford} (September 1986); its publisher abstract confirms an explicit Mumford-form formula, but that paper\textquotesingle s full proof was not accessible. Class A records this direct subsequent publication by the speaker.',
 ['belavinknizhnik1986complex','beilinsonmanin1986mumford','bost1987determinants'],cls='A',literal='correct with missing hypotheses',match='partial')

item(666,'P001256','claim','The displayed local determinant Hessian suppresses zero modes',
 r'Equations (21)--(21\textquotesingle) write both complex-structure and metric variations of \(\log\det\Delta_j\) as \(c_j\) times universal curvature integrals, with \(f=\rho\eta\).',
 r'The invariant statement is the Quillen curvature and conformal-anomaly formula for determinant lines with their cohomology metrics. Raw \(\log\det^{\prime}\Delta_j\) has additional variations from the Gram determinants of harmonic sections and from the area/constant mode. Thus a bare determinant Hessian is not, in general, just \(c_j\) times the displayed local expression. The precise combination in Belavin--Knizhnik (2.21) includes the zero-mode normalizations.',
 r'The source does not state whether its determinant notation already contains those factors; we treat this as an ambiguity instead of fixing an arbitrary local regularization.',
 r'\citet[eqs.~(2.19)--(2.21), (3.3)]{belavinknizhnik1986complex} is the precise comparator; \citet[Theorem~2.2]{bost1987determinants} gives the coordinate-free version.',
 ['belavinknizhnik1986complex','bost1987determinants'],cls='B',literal='correct with missing hypotheses',match='partial',speaker='A. A. Belavin')

item(666,'P001256','claim','The bosonic moduli integral diverges at the cusp',
 r'Beilinson says the integral diverges and must be renormalized; Belavin writes the genus-one integral and repeats that it diverges.',
 r'For the uncompactified critical bosonic vacuum density, \(|\eta(x+iy)|^{-48}=e^{4\pi y}(1+O(e^{-2\pi y}))\) uniformly for \(|x|\le1/2\) as \(y\to\infty\). Therefore the positive cusp integral \(\int_Y^\infty y^{-14}e^{4\pi y}\,dy\) diverges. This is an infrared degeneration associated with the tachyon, even though the local conformal anomaly vanishes. The mere word renormalization does not specify a canonical finite value.',
 r'The elementary comparison proves the recorded divergence in the displayed genus-one case; it does not construct a subtraction scheme at all genera.',
 r'\citet[\S4]{belavinknizhnik1986complex} studies boundary asymptotics; \citet[\S\S2.3,6.4]{witten2012revisited} distinguishes tachyon and tadpole infrared problems from ultraviolet behavior.',
 ['belavinknizhnik1986complex','witten2012revisited'],literal='correct',speaker='A. A. Beilinson and A. A. Belavin')

item(666,'P001256','conjecture','The unqualified hope that everything converges for superstrings',
 r'\ru{Но есть гипотеза, что в суперструне всё сходится}.',
 r'The sentence supplies no string model, vacuum, external states, momenta, genus, integration cycle or distinction between a fixed-genus integral and the all-genus series. It therefore does not define one precise convergence conjecture. Tachyon-free supersymmetric vacua have substantially better behavior, but physical on-shell poles and possible infrared singularities are not excluded by the word superstring.',
 r'We do not silently replace this with a universal all-orders theorem or a new narrowly chosen open problem. Conditions eliminating massless tadpoles and handling degeneration contours are additional input.',
 r'\citet[\S\S6.4,7--8]{witten2012revisited}, first posted September 2012 and revised through November 2023, develops the integration-cycle and infrared analysis. This is a thematic successor, not a proof that every possible meaning of the notebook sentence converges.',
 ['witten2012revisited'],cls='F',literal='not determinable',match='thematic only',confidence='low',speaker='A. A. Belavin',status=r'As of November 2026: the recorded slogan has no definite quantifiers, and should not be indexed as an unresolved mathematical problem. The checked modern treatment explicitly retains physical infrared/on-shell qualifications.')

item(666,'P001256','construction','The genus-two measure uses ten even theta constants',
 r'The notes give \(Z_2=\int d^2\tau\,(\Im\tau)^{-3}(\Im\tau)^{-10}|F(\tau)|^{-2}\), \(F=\prod_m\theta_m^2\), naming Knizhnik, Morozov and Perelomov.',
 r'On the marked genus-two Siegel space, write \(d^6\Omega=\prod_{1\le i\le j\le2}d\Re\Omega_{ij}\,d\Im\Omega_{ij}\). Up to an overall constant, the bosonic density is \(d^6\Omega\,(\det\Im\Omega)^{-13}|\chi_{10}(\Omega)|^{-2}\), where \(\chi_{10}\) is a nonzero scalar multiple of \(\prod_{m\ \mathrm{even}}\theta_m(0|\Omega)^2\), over the ten even characteristics. Remove the decomposable locus to describe smooth genus-two curves and quotient by the symplectic action with orbifold factors.',
 r'The handwritten powers must be powers of a determinant, and its \(d^2\tau\) is shorthand for three complex variables. Including odd characteristics would make the product identically zero. The overall constant and the normalization of \(\chi_{10}\) are not fixed by the notes.',
 r'\citet[eqs.~(6.9),(6.14)--(6.17)]{belavinknizhnik1986complex} was read. The named low-genus work appeared as \citet{belavinetal1986loops}; the institutional author bibliography was checked. Belavin is an omitted coauthor in the notebook attribution.',
 ['belavinknizhnik1986complex','belavinetal1986loops'],cls='B',literal='correct with missing hypotheses',match='partial',speaker='A. A. Belavin')

item(666,'P001256','remark','A genus-three formula exists, but general moduli are not absent',
 r'\(Z_3\) is said also to exist; for general genus there is no good description of moduli space.',
 r'The recoverable assertion is that low-genus period-matrix formulas are particularly explicit. In genus three the product \(\chi_{18}\) of the 36 even theta constants enters a bosonic density; its square-root interpretation requires attention to the Torelli marking and hyperelliptic divisor. For arbitrary genus, moduli stacks, compactifications and deformation theory already exist; the difficulty is obtaining comparably simple global coordinates or theta expressions, not existence of moduli.',
 r'No exact genus-three formula was written in the notebook, so none is attributed to this occurrence. The phrase “no good description” is retained as a judgment about explicit calculational convenience.',
 r'\citet[eqs.~(6.18)--(6.20)]{belavinknizhnik1986complex} supplies the later formula; \citet[\S3.4]{bost1987determinants} discusses its geometric scope.',
 ['belavinknizhnik1986complex','bost1987determinants'],cls='B',literal='correct with missing hypotheses',match='partial',speaker='A. A. Belavin',confidence='medium')

item(666,'P001257','theorem','Global constancy on moduli and the remaining scalar ambiguity',
 r'For \(g>2\), every holomorphic function on moduli is declared constant; flat metrics differ by a holomorphic modulus square, so the metric and section are said to be unique.',
 r'On the full complex moduli space \(\mathcal M_g\), \(g\ge3\), global holomorphic functions are constant. More directly for the metric argument, a real pluriharmonic function is constant because any two moduli points can be joined by a complete curve inside moduli. Consequently two globally defined flat metrics on the same holomorphic line differ by a positive constant. A chosen nonzero holomorphic section is likewise unique only up to a nonzero scalar when the quotient is globally holomorphic. Local charts and Teichm\"uller space do have nonconstant holomorphic functions.',
 r'The complete-curve argument supplies the missing global hypothesis and avoids falsely assuming that every pluriharmonic function globally has a single-valued holomorphic conjugate. The scalar is still not determined by flatness.',
 r'\citet[proof of Theorem~3.3, pp.~141--142]{bost1987determinants} explicitly gives this argument for \(g\ge3\); \citet[Theorem~3.4]{favalepirolatorelli2023forms} proves the corresponding modern statement on the smooth locus for \(g\ge4\). The latter range is not incorrectly substituted for the full-moduli genus-three statement.',
 ['bost1987determinants','favalepirolatorelli2023forms'],literal='correct with missing hypotheses',match='partial')

correction('P001253','Equation (3), one-loop density',r'\(|dq/q|^2\Delta(q)^{-2}\log|q|^{-13}\)',r'\(C|dq/q|^2|\Delta(q)|^{-2}(-\log|q|)^{-14}\) in the conventions of P001256.',r'The scan confirms exponent -13 and no modulus on Delta. The later correct tau-density and q=e^{2pi i tau} determine the corrected exponent and absolute square.')
correction('P001253','Parenthesis after the definition of L',r'Holomorphic structure induced by the metric',r'The oriented surface metric induces a complex structure on X; a holomorphic structure on the arbitrary bundle L is additional data.',r'The same wording occurs in Russian and the scan. A base metric does not define a Dolbeault operator on an unspecified smooth line bundle.','ambiguity')
correction('P001254','Equation (7), Quillen metric',r'Hodge norm times \(\sqrt{\det^{\prime}\Delta}\) on \(\det H^0/\det H^1\)',r'Hodge norm divided by \(\sqrt{\det^{\prime}\Delta}\), or dualize the determinant line.',r'The scan confirms multiplication. Quillen uses the dual line. The independent finite-dimensional acyclic map T=a sends 1 to a^{-1}e/f and fixes the reciprocal.')
correction('P001255','Determinant of the one-dimensional map',r'\(\det T\in E_1/E_2\)',r'\(\det T\in E_2/E_1\); its inverse lies in \(E_1/E_2\).',r'The source fraction is clear. A map E1 to E2 belongs to E1* tensor E2.')
correction('P001255','Bernoulli-polynomial label',r'\(6j^2-6j+1\) is the second Bernoulli polynomial',r'\(6j^2-6j+1=6B_2(j)\) with \(B_2(j)=j^2-j+1/6\).',r'This is the standard normalization; the source suppresses the factor six.','ambiguity')
correction('P001256','Equation (18), exponent index',r'\(b_{j_i}\)',r'\(b_i\), in the notation of (14) and (19).',r'The scan has the nested index. The preceding cancellation sum and following theorem use coefficients indexed by the list position i.')
correction('P001256','Uniqueness following theorem (19)',r'Zero curvature uniquely determines the canonical metric',r'It can at most determine the metric up to a positive constant after a global constancy argument.',r'Constant rescaling preserves zero curvature. P001257 invokes global moduli but still leaves the normalization free.')
correction('P001256','Label below equation (20)',r'\(\Delta_j\) is the Laplacian on j-forms',r'The Laplacian on j-differentials, i.e. sections of \(K^j\).',r'The Russian reads j-differentials; negative j=-1 in the displayed formula excludes ordinary differential-form degree.','translation','en')
correction('P001256','Genus-two formula',r'Powers of \(\Im\tau\), \(d^2\tau\), and \(\prod_m\theta_m^2\) with no characteristic restriction',r'Powers of \(\det\Im\tau\), volume in three complex variables, and the product over ten even characteristics.',r'The scan omits these qualifications. The dimensional and modular-weight requirements and vanishing of odd theta constants determine them.','ambiguity')
correction('P001257','Last uniqueness conclusion',r'Unique metric and unique holomorphic section',r'Unique up to a positive metric scale and a nonzero section scalar, respectively.',r'The source claim of global constancy does not fix a nonzero constant. The precise comparison theorem contains a genus-dependent normalization.')
correction('P001258-P001259','Record ownership in the supplied catalogue page spans',r'Pages through P001259 assigned to record666',r'Record666 ends on P001257; separately headed records667 and668 start on P001258 and P001259.',r'Both scan headings name different speakers and dates. The archive all-links list has those adjacent entries. They are included in the adjacent-evidence supplement without changing the prescribed 26-record core.','provenance')
correction('P001258','Kontsevich date',r'24 February 1985 in the scan; 24 February 1987 in the archive',r'Preserve both attestations; 24 February 1986 is a plausible contextual inference, not an established reading.',r'The scan clearly ends in 85; the next leaf is dated24Feb86. Calendar check:24Feb85 Sunday,24Feb86 Monday,24Feb87 Tuesday. Monday regularity supports but does not prove the inferred year.','provenance')
correction('P001259','Morozov date',r'Catalogue24February1987',r'Manuscript24February1986, while retaining the catalogue discrepancy.',r'The scan clearly writes24.2.86; that day was Monday and follows Beilinson\textquotesingle s17Feb86 talk.','provenance')
save()



# Mark only calculations and proofs supplied here, not source-based identifications.
proved={'1985-663.1','1985-663.3','1985-663.5','1985-663.7','1985-663.13',
        '1985-664.4','1985-664.8','1985-664.12','1985-666.5','1985-666.6',
        '1985-666.10','1985-666.14','1985-666.17'}
computed={'1985-664.10','1985-664.11','1985-666.11','1985-666.13'}
for entry in items:
    if entry['id'] in proved:entry['reconstruction']=r'\ours\ '+entry['reconstruction']
    if entry['id'] in computed:entry['reconstruction']=r'\oursComputed\ '+entry['reconstruction']
save()
