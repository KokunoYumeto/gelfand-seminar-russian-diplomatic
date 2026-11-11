"""Record 506: independently audited against Russian notes and all five scans."""
import json,csv
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PARTS=ROOT/'parts'
talks=[dict(record=506,date='1980-12-01',speaker='S. P. Novikov',pages='P000944-P000948',
 title='Magnetic translations, Pauli ground states, and Bloch bundles',kind='talk',
 summary=r'''The actual heading is on P000944; the earlier pages assigned to this record by the supplied catalog are the end of Beilinson's lectures. Novikov discusses a magnetic Schr\"odinger operator with periodic curvature and potential, the flux obstruction to ordinary Bloch theory, the explicit zero modes of the two-dimensional Pauli operator, and the topology and perturbation of their bundle over the reciprocal torus. The zero-mode results were already published in September 1980; the perturbation and topological discussion matches a paper received on 2 December 1980, the day after this seminar (\citealp[Secs.~II--IV]{dubrovinnovikov1980ground}; \citealp[Lemmas~1--2, Theorem~2]{novikov1981magnetic}).

The notebook's physical line bundle and its bundle of Bloch zero modes must be distinguished: the former has degree \(N\), whereas the latter has rank \(N\) and first Chern number \(1\) in Novikov's orientation. Gelfand's concluding suggestion of a complex or parabolic regularization in the irrational-flux case is a program, not a specified spectral theorem. The final reading assignment on \(G\)-structures, \(\mathcal D\)-structures and the Spencer resolution is recorded as an assignment, not converted into an additional conjecture.''')]

items=[]
def item(kind,title,pages,notes,statement,fate,refs,cls='E',reconstruction='',
         correctness='correct with missing hypotheses',match='exact',verification='read the result',
         confidence='high',speaker='',status='',development='annotated'):
    n=len(items)+1
    q=dict(id=f'1980-506.{n}',record=506,pages=pages,kind=kind,title=title,
           notes=notes,statement=statement,reconstruction=reconstruction,
           **{'class':cls},fate=fate,present_status=status or
           'As of November 2026, the precisely qualified statement above is established; the historical shorthand does not add a further open assertion.',
           literal_correctness=correctness,publication_match=match,verification=verification,
           development=development,problem='',worth='',refs=refs,confidence=confidence)
    if speaker:q['speaker']=speaker
    items.append(q)

item('definition','Periodic magnetic Schrödinger and Pauli operators','P000944',
 r'''Equations (1)--(7) give \(\widehat H=\frac12\sum_\alpha(i\partial_\alpha-eA_\alpha)^2+cV\), \(H_{\alpha\beta}=\partial_\beta A_\alpha-\partial_\alpha A_\beta\), and a spin term \(e\sigma_jH^j\). The curvature and electric potential are periodic; the vector potential need not be. The text first calls \(V\) the electric field but then explicitly distinguishes field from potential.''',
 r'''Let \(\Lambda\subset\mathbb R^2\) be a lattice, let \(B,V\) be smooth real \(\Lambda\)-periodic functions, and choose a smooth real potential \(A\) with \(\partial_xA_y-\partial_yA_x=B\). Put \(\Pi_j=-i\partial_j-eA_j\). The magnetic Schr\"odinger operator is the self-adjoint operator associated with the semibounded quadratic form \(\sum\|\Pi_jf\|^2+\int V|f|^2\). In a consistent Pauli normalization, \(P=\Pi_1^2+\Pi_2^2-e\sigma_3B\) splits into two scalar spin sectors. The notebook uses the opposite curvature sign and suppresses mass and spin-normalization conventions.''',
 r'''The model and its two spin sectors appear in \citet[Sec.~I, equations (1)--(8)]{dubrovinnovikov1980ground}, received 15 April 1980 and published before this talk.''',
 ['dubrovinnovikov1980ground'],reconstruction='The smoothness, real coefficients, form realization, dimension restriction for the displayed Pauli operator, and a single consistent normalization are supplied here. They are not a claim that the notebook fixes all physical units.')

item('remark','The aside on a constant electric field','P000944',
 r'''The parenthesis following (4) says that a constant electric field gives a potential of the form \(\vec E\cdot\vec x\), followed by \ru{не изучена даже 1-мерн. задача}.''',
 r'''A constant nonzero electric field requires an affine potential, which is not periodic on a full lattice. The phrase about an unstudied one-dimensional problem does not specify the periodic background, spectral property, or limiting regime, so no unique open problem can be extracted.''',
 r'''The observation about nonperiodicity is elementary. Searches of the Novikov bibliography and the cited 1980 papers identify no exact one-dimensional question corresponding to this aside; a general reference to Stark operators would be only thematic.''',
 ['dubrovinnovikov1980ground'],'F',correctness='not determinable',match='none found',verification='unresolved lead',confidence='low',
 status='As of November 2026, the intended historical question remains unidentified; this is not a claim that one-dimensional Stark spectral theory is undeveloped.')

item('construction','Integral magnetic flux as the degree of a physical line bundle','P000944',
 r'''Equations (8)--(10) impose \(e\Phi_{\alpha\beta}/(2\pi)\in\mathbb Z\) and identify these integers with \(\langle c_1(\xi),Z_{\alpha\beta}\rangle\). The operator on Euclidean space covers an operator in a bundle over a torus.''',
 r'''A smooth closed real two-form \(B\) on \(T^n=\mathbb R^n/\Lambda\) is the curvature, divided by \(-ie\), of a unitary connection on a complex line bundle precisely when \([eB/(2\pi)]\) is integral. On \(T^2\), its degree is \(N=e\int_{T^2}B/(2\pi)\). Pullback to \(\mathbb R^n\) trivializes the bundle; lattice transitions yield the magnetic boundary conditions. Changing the sign of the curvature convention changes the sign of this degree.''',
 r'''The integrality interpretation is already used in \citet[Sec.~I, equation (3)]{dubrovinnovikov1980ground}; the talk presents it as background.''',
 ['dubrovinnovikov1980ground'],reconstruction='Closedness, a unitary connection and the sign convention are explicit here. This is the bundle on physical space, not the reciprocal-torus eigenbundle in item 13.')

item('method','Reduction of rational flux to integral flux','P000944-P000945',
 r'''The last line of P000944 says \ru{Рац. свод. к нему укрупнением решётки}, after mentioning the irrational case. The next page imposes integral flux to obtain commuting translations.''',
 r'''If \(e\Phi/(2\pi)=p/q\) with coprime integers \(p,q\), replacing one period by \(q\) times that period gives cell flux \(p\). Replacing both periods by \(q\) gives flux \(pq\). A finite-index enlargement cannot make an irrational flux integral: multiplying an irrational number by a nonzero integer remains irrational.''',
 r'''The intended rational-to-integral reduction is explicit in \citet[Sec.~I and Sec.~IV]{dubrovinnovikov1980ground}. The immediately preceding pronoun in the notes is misleading.''',
 ['dubrovinnovikov1980ground'],correctness='false as written',reconstruction='The antecedent must be the integral case, not the irrational case. The arithmetic argument is an explanatory reconstruction, not a new result.')

item('remark','Flux quantization depends on the charge being modeled','P000945',
 r'''Two situations are contrasted: a prescribed crystal lattice in an external field and a superconducting lattice whose field is said to be automatically integral. The notebook assigns cell areas \(10^{-10}\,\mathrm{cm}^2\) to the former and \(10^{-16}\,\mathrm{cm}^2\) to the latter.''',
 r'''Flux quantization refers to the charge in the effective order parameter. If one superconducting flux quantum is \(2\pi/(2e_0)\), it is an integer quantum for charge \(2e_0\), but a half quantum for an electron of charge \(e_0\). Integrality therefore cannot be asserted independently of the chosen charge and model. The two numerical cell-area examples in the notes are reversed relative to the cited paper.''',
 r'''\citet[Sec.~I, Remark]{dubrovinnovikov1980ground} explicitly makes the charge distinction and gives the crystal area as about \(10^{-16}\,\mathrm{cm}^2\).''',
 ['dubrovinnovikov1980ground'],correctness='false as written',reconstruction='This is a correction of a faithfully transcribed physical example, not a correction inferred from handwriting alone.')

item('theorem','Magnetic translations form a projective lattice representation','P000945',
 r'''If \(A_\alpha(x+T_j)=A_\alpha(x)+\partial_\alpha f_j\), the notes set \(\widehat T_j^*\psi=\psi(x+T_j)e^{-ief_j(x)}\) and state \(\widehat T_j^*\widehat T_k^*=\widehat T_k^*\widehat T_j^*e^{-ie\Phi_{kj}}\), crediting Zak and Brown.''',
 r'''For a smooth real connection potential on \(\mathbb R^n\) with lattice-periodic curvature, the difference between a translate of \(A\) and \(A\) is exact. The corresponding gauge-corrected translations are unitary, commute with a magnetic Hamiltonian whose scalar potential is periodic, and commute with one another up to the exponential of the flux through the spanning parallelogram. They commute exactly on a pair of lattice generators when that normalized flux is integral.''',
 r'''Brown and Zak published magnetic-translation theory in 1964 (\citealp{brown1964bloch,zak1964magnetic}); the periodic-field formula is read in \citet[Sec.~I, equations (4)--(6)]{dubrovinnovikov1980ground}.''',
 ['brown1964bloch','zak1964magnetic','dubrovinnovikov1980ground'],correctness='correct with missing hypotheses',reconstruction='The phase depends on orientation and on whether active or passive translations are used. A missing hat on the last translation is merely typographical.')

item('claim','Irrational flux prevents finite-dimensional magnetic translation fibers','P000945; P000948',
 r'''The notes say irrational flux gives groups \ru{не типа 1}, as subgroups of the Heisenberg group; P000948 again writes the noncommuting two-translation relation and mentions factors and ergodicity.''',
 r'''For \(\theta\notin\mathbb Q\), the universal rotation algebra generated by unitaries \(U,V\) with \(UV=e^{2\pi i\theta}VU\) has no nonzero finite-dimensional unital representation: determinants in dimension \(d\) would require \(e^{2\pi id\theta}=1\). Its operator-algebraic representation theory replaces a finite-dimensional magnetic Bloch fiber. A particular representation or von Neumann completion must be specified before assigning a factor type.''',
 r'''The irrational-representation obstruction is already described in \citet[Sec.~I]{dubrovinnovikov1980ground}; later observable-algebra treatments are developed in \citet[Secs.~3.1, 3.5--3.6]{bellissard1994quantumhall}.''',
 ['dubrovinnovikov1980ground','bellissard1994quantumhall'],'E',reconstruction='The determinant proof and the precise rotation-algebra formulation are supplied here. The notebook does not assert a classification of all Heisenberg subgroups.',match='partial')

item('question','Describe the spectrum: a program without a specified invariant','P000945',
 r'''An underlined \ru{Задача: описать спектр} precedes the magnetic Bloch construction.''',
 r'''For the smooth periodic-field operators of item 1, the spectrum depends on the entire functions \(B,V\), on the flux and on the spin sector. The notes do not specify whether the desired description concerns explicit bands, spectral type, gap labels, a density of states, or continuity in the field. Thus no single complete yes-or-no problem is determined by this line.''',
 r'''The talk supplies the special Pauli zero-mode solution. Later noncommutative spectral geometry gives substantial invariant information (\citealp[Sec.~3.4, Theorem~1]{bellissard1994quantumhall}), but is not an exact solution to an unspecified request for the whole spectrum.''',
 ['dubrovinnovikov1980ground','bellissard1994quantumhall'],'F',correctness='not determinable',match='thematic only',confidence='medium',
 status='As of November 2026, this is retained as an identifiable research program with an unspecified target, not promoted to a newly discovered open conjecture.')

item('method','Magnetic Bloch decomposition for commuting lattice translations','P000945',
 r'''Equations (16)--(18) seek simultaneous eigenfunctions of \(\widehat H\) and the translations, with \(\widehat T_j^*\psi_p=e^{ip_jT_j}\psi_p\); \(L^2\) is a direct integral of torus problems and \(\varepsilon_j(p_1,p_2)\) are dispersion laws.''',
 r'''For integral flux and smooth periodic coefficients, the commuting magnetic lattice action decomposes the Hilbert space as a direct integral over its character torus. The fiber operator acts on sections of a line bundle over the physical torus twisted by a flat unitary character, and has compact resolvent. Its ordered eigenvalues, counted with multiplicity, give the fiberwise bands. Individual Bloch waves need not belong to \(L^2(\mathbb R^2)\).''',
 r'''This is the framework used before the seminar in \citet[Sec.~I, equation (7), and Sec.~III]{dubrovinnovikov1980ground}.''',
 ['dubrovinnovikov1980ground'],reconstruction='Integrality and generalized eigenfunctions are essential qualifications to the notebook\'s simultaneous-eigenfunction wording.')

item('theorem','Explicit Pauli zero modes in a periodic magnetic field','P000946',
 r'''For \(V=0\), spin \(1/2\) and \(N=e\Phi_{12}/(2\pi)\), equation (20) gives \(\Psi_A=e^{-e\varphi}\prod_{j=1}^N\sigma(z-a_j)e^{-az}\), with \(\Delta\varphi=H\) and a logarithmic sigma integral in (22). The margin cites Dubrovin--Novikov, JETP, September 1980.''',
 r'''Let a smooth real magnetic field on a two-torus have positive integral normalized flux \(N>0\), and take the Pauli operator with no electric potential. In the spin sector whose first-order factor is a Dolbeault operator, the zero modes are holomorphic sections of a degree-\(N\) line bundle, expressed on the universal cover as a gauge factor times an entire theta function with \(N\) zeros per cell. Sigma products provide such functions; their exponential factor must satisfy the magnetic boundary multipliers. For negative flux exchange the spin sector; at zero flux the statement requires a separate analysis.''',
 r'''This is \citet[Sec.~III, Theorem~(a)]{dubrovinnovikov1980ground}, not a post-seminar discovery. The JETP account appeared in September 1980 (\citealp[Sec.~2]{dubrovinnovikov1980electron}).''',
 ['dubrovinnovikov1980ground','dubrovinnovikov1980electron'],reconstruction='Positivity of N, the spin sector, and a consistent curvature normalization have been supplied. The sign of a can be changed by renaming that parameter; the curvature inconsistency between (2) and (27) cannot.')

item('construction','Divisors, sigma multipliers, and real quasimomenta','P000946',
 r'''Equations (21)--(24) relate \(p_1+ip_2\) to \(\sum a_j\); \(a=a(a_1,\ldots,a_N)\) is chosen to select real quasimomenta. The parameters are symmetric and defined modulo the lattice.''',
 r'''For an elliptic curve \(E=\mathbb C/\Lambda\), an effective degree-\(N\) divisor determines a degree-\(N\) line bundle. Fixing the Abel sum modulo \(\Lambda\) fixes its isomorphism class. The quasi-periodicity of the sigma product fixes its two multipliers; an exponential correction normalizes their absolute values to one after the gauge factor is included. The scalar multiplier and unordered zeros parametrize nonzero sections with the appropriate lattice identifications, not a globally free Cartesian coordinate system.''',
 r'''The exact multiplier equations are (14)--(16) of \citet[Sec.~III]{dubrovinnovikov1980ground}; alternative signs occur in \citet[equation (6)]{novikov1981magnetic}.''',
 ['dubrovinnovikov1980ground','novikov1981magnetic'],reconstruction='No correction is made solely because the two publications use different signs for the complex quasimomentum; orientation and exponential normalization must first be fixed.',match='partial')

item('theorem','The N-dimensional zero-mode fiber','P000946-P000947',
 r'''At fixed \(p\), the notes identify the fiber with \(\mathcal L(\mathcal D)\), state \(\dim\mathcal L(\mathcal D)=N\), and invoke Atiyah--Singer with zero cokernel. All functions in one fiber are obtained from one by meromorphic elliptic multipliers.''',
 r'''If \(L\) is a holomorphic line bundle of degree \(N>0\) on a smooth compact elliptic curve and \(F_p\) is any flat line bundle, then \(H^1(E,L\otimes F_p)=0\) and \(h^0(E,L\otimes F_p)=N\). Indeed Serre duality identifies \(H^1\) with the dual of sections of a negative-degree line bundle, hence zero; Riemann--Roch gives the dimension. A quotient of two nonzero sections is a meromorphic elliptic function with poles canceled by the zeros of the denominator section.''',
 r'''\citet[Sec.~III, Theorem~(b) and its proof]{dubrovinnovikov1980ground} applies this index calculation to the Pauli kernel.''',
 ['dubrovinnovikov1980ground'],reconstruction='The elementary curve-theoretic proof clarifies the zero-cokernel hypothesis; an index identity alone never proves the kernel dimension without it.')

item('claim','Rank and Chern number of the Bloch bundle','P000946-P000947',
 r'''Equation (25) states that the zero modes form an \(N\)-dimensional holomorphic vector bundle over the reciprocal torus with \(c_1=N\), identifying this with the number of magnetic-flux quanta.''',
 r'''The family \(\mathcal E_p=H^0(E,L\otimes F_p)\) has rank \(N\). Its first Chern number has absolute value \(1\), and equals \(1\) in Novikov's reciprocal-torus convention; it is not \(N\) for general positive \(N\). In the standard algebraic Poincar\'e-bundle orientation, the Fourier--Mukai transform of a degree-\(N\) line bundle has rank \(N\) and degree \(-1\); reversing the base orientation gives Novikov's sign.''',
 r'''\citet[Sec.~II, Lemma~1]{novikov1981magnetic} explicitly gives \(c_1=1\). This paper was received 2 December 1980 and published in 1981.''',
 ['novikov1981magnetic'],'A',correctness='false as written',reconstruction='The scan clearly reads \(c_1=N\); this is a faithful notebook error, not an OCR correction. The Fourier--Mukai terminology is a modern reconstruction; the cited source proves the topological normalization directly.',
 status='As of November 2026, the distinction is settled: physical line bundle degree N; reciprocal-torus zero-mode bundle rank N and Chern number of absolute value 1.')

item('theorem','The same fiber multiplicity at every constant-field Landau level','P000947',
 r'''The notes extend the \(N\)-dimensionality at fixed quasimomentum to all energy levels when the magnetic field is uniform. A question about the origin of the degeneracy is crossed out.''',
 r'''For a constant nonzero magnetic field with positive integral flux \(N\) per cell, each Landau eigenspace in a magnetic Bloch fiber in a fixed scalar spin sector has dimension \(N\). Creation operators identify the higher-level eigenbundles with the lowest-level bundle. This extension concerns constant field; an arbitrary periodic magnetic perturbation does not preserve all higher Landau levels. Combining both Pauli spin sectors can give an additional spin multiplicity at positive energies.''',
 r'''The constant-field comparison is made in \citet[Sec.~3]{dubrovinnovikov1980electron}; \citet[Sec.~II, Remark after Lemma~1]{novikov1981magnetic} also records the eigenbundle identification.''',
 ['dubrovinnovikov1980electron','novikov1981magnetic'],reconstruction='The crossed-out question is not counted as an independent unresolved problem.')

item('method','Compressing a weak electric perturbation to the zero-mode bundle','P000947',
 r'''For \(\widehat H=\widehat H_0+ev\), equation (30) restricts the Hermitian form \(\int_{K_{12}}\overline{\Psi_A}v\Psi_A\) to the unperturbed kernel at fixed \((p_1,p_2)\).''',
 r'''Let \(v\) be a smooth real periodic function and assume the zero-mode cluster of \(H_0(p)\) is isolated by a uniform gap. If \(P_0(p)\) is its orthogonal projection, the first-order coefficients of its eigenvalues under \(H_0+\varepsilon v\) are the eigenvalues of \(P_0(p)vP_0(p)\) on \(\ker H_0(p)\). This is an \(N\times N\) Hermitian endomorphism of the zero-mode bundle; it is not the exact full perturbed Hamiltonian.''',
 r'''The compression is already in \citet[Sec.~IV]{dubrovinnovikov1980ground}; its topological use is sharpened in \citet[Sec.~III]{novikov1981magnetic}.''',
 ['dubrovinnovikov1980ground','novikov1981magnetic'],'E',reconstruction='The small perturbation parameter and isolated-cluster qualification are made explicit.')

item('theorem','Codimension three and generic splitting into line bundles','P000947',
 r'''Theorem 2 states that a generic two-parameter family of complex Hermitian forms has no eigenvalue coincidences because the coincidence condition has codimension three; in three parameters coincidences are isolated. A corollary splits the Bloch bundle into lines.''',
 r'''In the real vector space of Hermitian \(N\times N\) matrices, the stratum with exactly one double eigenvalue and all other eigenvalues simple has codimension three. Globally, consider a smooth section of the bundle of Hermitian endomorphisms of the rank-\(N\) Bloch bundle, transverse to its fiberwise multiplicity strata. On a two-dimensional compact base it avoids all multiple eigenvalues and splits the bundle into smooth eigenlines. A transverse three-parameter family meets the simple-double stratum in isolated points. Applying this to scalar periodic potentials additionally requires transversality of the induced family of compressions. No global trivialization of the nontrivial Bloch bundle is assumed.''',
 r'''The potential-dependent transversality and resulting splitting are stated in \citet[Sec.~III, Lemma~2 and Theorem~2]{novikov1981magnetic}, received the day after the talk.''',
 ['novikov1981magnetic'],'A',reconstruction='The notebook\'s three equations concern coincidence at fixed quasimomentum. Allowing the two quasimomenta to vary gives codimension one in the space of potentials; the 1981 paper distinguishes these counts.',
 status='As of November 2026, the corrected genericity statement is established. The global Chern classes of the eigenlines need not vanish and sum to the total Bloch Chern class.')

item('remark','The aside about one-dimensional second-order operators','P000947',
 r'''An uncancelled parenthesis says that in the one-dimensional case general position never occurs, because the operator is second order.''',
 r'''For unrestricted smooth one-parameter Hermitian families, second-order coincidence is not forced: for example the constant diagonal family with distinct diagonal entries has simple spectrum. The notebook must therefore refer to a more restricted family of scalar differential operators, boundary conditions, or a different notion of general position; those data are not specified in this parenthesis.''',
 r'''The codimension statements in \citet[Sec.~III, Lemma~2]{novikov1981magnetic} concern the two-dimensional periodic-field construction. They do not identify the separate one-dimensional assertion or its intended quantifiers.''',
 ['novikov1981magnetic'],'F',correctness='not determinable',match='none found',verification='unresolved lead',confidence='low',
 reconstruction='The diagonal-matrix observation only shows why the preceding finite-dimensional genericity formulation cannot be transferred literally to this aside. It does not reconstruct a missing Sturm--Liouville theorem.',
 status='As of November 2026, the intended one-dimensional comparison remains unidentified; no open spectral problem is inferred from it.')

item('method','Complex or parabolic regularization in the irrational case','P000947-P000948',
 r'''Gelfand says \ru{Интересен иррац. случай!} and suggests entering the complex domain, \ru{внутри круга}, in a non-self-adjoint setting, or a parabolic regularization. The next page recalls the irrational magnetic-translation relation and von Neumann factors.''',
 r'''No regularized operator, analytic parameter, topology of convergence, or spectral invariant is specified. The strongest recoverable content is a proposal to investigate irrational-flux spectral theory through a non-self-adjoint or heat-type deformation. The relation \(UV=e^{2\pi i\theta}VU\) survives, but by itself does not define the proposed regularization.''',
 r'''Noncommutative observable algebras and trace/Chern invariants later gave rigorous tools (\citealp[Secs.~3--4]{bellissard1994quantumhall}). No exact implementation of this notebook prescription was identified in the checked Novikov and quantum-Hall sources.''',
 ['bellissard1994quantumhall'],'F',correctness='not determinable',match='thematic only',verification='unresolved lead',confidence='low',speaker='I. M. Gelfand',
 status='As of November 2026, the precise suggested regularization remains unidentifiable. No open existence theorem is manufactured from this incomplete method proposal.')

corrections=[
 dict(page='P000944',place='Last line, rational-flux reduction',transcription_reads=r'\ru{Рац. свод. к нему укрупнением решётки}; English: rational reduces to it, immediately after irrational.',should_read='Rational flux reduces to integral flux by passing to a larger lattice cell.',evidence=r'The scan faithfully contains the pronoun. Multiplication by a lattice index cannot turn a rational into an irrational number; the cited paper explicitly says integral (\citealp[Sec.~I]{dubrovinnovikov1980ground}).',applies_to='both',type='faithful_error'),
 dict(page='P000945',place='Cell-area estimates and superconducting integrality',transcription_reads=r'Crystal: \(10^{-10}\,\mathrm{cm}^2\); superconducting lattice: \(10^{-16}\,\mathrm{cm}^2\); flux automatically integral.',should_read=r'The examples are reversed: the source gives crystal area about \(10^{-16}\,\mathrm{cm}^2\) and superconducting area \(10^4\)--\(10^6\) times larger. Integrality is for the effective charge \(2e_0\); an electron sees a half quantum per such cell.',evidence=r'Both exponents are clear in the scan; \citet[Sec.~I, Remark]{dubrovinnovikov1980ground} supplies the contrary values and the charge qualification.',applies_to='both',type='faithful_error'),
 dict(page='P000946',place='Equation (25), Chern class of the reciprocal-torus bundle',transcription_reads=r'\(N\)-dimensional bundle, \(c_1=N\).',should_read=r'''Rank \(N\), \(c_1=1\) in Novikov's convention; absolute Chern number \(1\).''',evidence=r'Scan P000946 unequivocally has \(c_1=N\). \citet[Sec.~II, Lemma~1]{novikov1981magnetic}, received 2 December 1980, states \(c_1=1\). The physical line bundle and the reciprocal-torus eigenbundle were conflated.',applies_to='both',type='faithful_error'),
 dict(page='P000944; P000946; P000948',place='Curvature sign in (2), (27), and the irrational-case formula',transcription_reads=r'\(H_{12}=\partial_2A_1-\partial_1A_2\), but \(A_1=-\varphi_y,A_2=\varphi_x,\Delta\varphi=H\).',should_read=r'With the displayed gauge, \(\partial_2A_1-\partial_1A_2=-\Delta\varphi\). Either reverse the definition of \(H_{12}\) or write \(\Delta\varphi=-H_{12}\), adjusting the spin and flux signs consistently.',evidence='The scan confirms all signs. Direct differentiation detects the mismatch; it is not resolved by changing the exponential parameter a.',applies_to='both',type='faithful_error'),
 dict(page='P000944-P000948',place='Catalog range for record 506',transcription_reads='Supplied manifest: P000942-P000950.',should_read='The Novikov heading starts P000944, and the talk and concluding assignment end P000948.',evidence='P000942-P000943 continue Beilinson; P000949 starts MacPherson on 9 February 1981. The overlap is retained as provenance, not attributed to Novikov.',applies_to='both',type='provenance'),
]
for name,obj in [('root_talks',talks),('root_items',items),('root_problems',[])]:
    (PARTS/f'{name}.json').write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
with (PARTS/'root_corrections.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['page','place','transcription_reads','should_read','evidence','applies_to','type'])
    w.writeheader();w.writerows(corrections)
(PARTS/'root_areas.json').write_text(json.dumps({i['id']:'Mathematical physics and spectral theory' for i in items},indent=2)+'\n')
print(f'Wrote record 506: {len(items)} items, {len(corrections)} correction rows.')
