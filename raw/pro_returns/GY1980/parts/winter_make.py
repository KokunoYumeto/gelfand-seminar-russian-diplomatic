import json, csv
from pathlib import Path

OUT=Path(__file__).parent
talks=[]; items=[]; problems=[]; corrections=[]; areas={}

def talk(record,date,speaker,pages,title,summary,kind='talk'):
    talks.append(dict(record=record,date=date,speaker=speaker,pages=pages,title=title,kind=kind,summary=summary))

def item(record,pages,kind,title,notes,statement,reconstruction,fate,refs,area,
         cls='E',correct='correct with missing hypotheses',match='exact',verification='read the result',
         status=None,development='annotated',problem='',confidence='high',speaker=None,worth=''):
    n=1+sum(x['record']==record for x in items)
    ident=f'1980-{record}.{n}'
    x=dict(id=ident,record=record,pages=pages,kind=kind,title=title,notes=notes,statement=statement,
           reconstruction=reconstruction,**{'class':cls},fate=fate,
           present_status=status or r'As of November 2026, the statement with the displayed hypotheses is established; the notebook occurrence is expository.',
           literal_correctness=correct,publication_match=match,verification=verification,
           development=development,problem=problem,worth=worth,refs=refs,confidence=confidence)
    if speaker: x['speaker']=speaker
    items.append(x); areas[ident]=area
    return ident

def problem(ident,title,statement,occurrences,status,refs):
    problems.append(dict(id=ident,title=title,statement=statement,occurrences=occurrences,status=status,status_date='2026-11',refs=refs))

def corr(page,place,reads,should,evidence,typ='faithful_error',applies='both'):
    corrections.append(dict(page=page,place=place,transcription_reads=reads,should_read=should,evidence=evidence,applies_to=applies,type=typ))

def save():
    def clean(v):
        if isinstance(v,str): return v.replace("\\'", "'")
        if isinstance(v,list): return [clean(z) for z in v]
        if isinstance(v,dict): return {k:clean(z) for k,z in v.items()}
        return v
    for name,data in [('talks',talks),('items',items),('problems',problems),('areas',areas)]:
        (OUT/f'winter_{name}.json').write_text(json.dumps(clean(data),ensure_ascii=False,indent=2)+'\n')
    with (OUT/'winter_corrections.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=['page','place','transcription_reads','should_read','evidence','applies_to','type']); w.writeheader(); w.writerows(corrections)

DM='gourevitch2025dmodules'

talk(500,'1980-11-17','A. A. Beilinson','P000937-P000939','Inverse and direct images of D-modules',
     r'The manuscript heading on the lower part of P000937 begins this talk, following I. M. Gelfand\'s exercises. Beilinson constructs ordinary inverse images of left modules and transfer bimodules for direct images of right modules, tests them on point inclusions and delta modules, and introduces derived integration and its de Rham interpretation. The actual continuation reaches P000939, beyond the catalogue range. P000936 belongs to the preceding meeting.')
talk(501,'1980-11-17','I. M. Gelfand','P000937','Elementary analysis exercises and rapidly oscillating integrals',
     r'Four numbered exercises precede Beilinson\'s heading: Thomae\'s function and its powers, a double-limit representation of the Dirichlet function, the obstruction to a single limit of continuous functions, and Fourier integrals with quadratic, quartic, and sextic decay. These are definite questions with classical solutions, not evidence of newly announced unresolved conjectures.')
talk(502,'1980-11-17','S. I. Gelfand','P000940 (upper part)','Two exercises on derived categories',
     r'The upper portion of P000940, before the explicit 24 November heading, gives an exercise separating isomorphic cohomology from a chain map and an incompletely specified dual-sphere equivalence. The latter does not determine a kernel, an equivariance convention, or a precise category; its resemblance to a Radon transform is insufficient for an exact identification.')
talk(503,'1980-11-24','A. A. Beilinson','P000940-P000943','Derived direct images and holonomic modules',
     r'The talk starts below the Fuchs and Lomonosov interventions on P000940 and continues through P000943. It treats composition of derived direct images, Spencer and relative de Rham complexes, Gauss--Manin connections, closed embeddings, point-fibre criteria for holonomicity, finite length, and simple modules as minimal extensions of irreducible connections. Several assertions need the distinction between a closed embedding and an arbitrary locally closed embedding.')
talk(504,'1980-11-24','D. B. Fuchs','P000940 (middle)','Whitehead products and the Jacobi identity',
     r'A short intervention gives the boundary-of-a-product construction of the Whitehead product and its graded Jacobi identity. The target homotopy degree is one too high in the manuscript itself; this is a faithful mathematical error, not an English translation error.')
talk(505,'1980-11-24','V. I. Lomonosov','P000940 (middle)','A compressed perturbation statement for commuting operators',
     r'The manuscript records a trace-class difference for two operators, a compact difference for another pair, two commutation assertions, and a claimed unitary equivalence of absolutely continuous restrictions. The primes and the operators used in the spectral subspaces do not yield a valid identifiable theorem as written. A standard scattering-theoretic repair can be proved, but is explicitly separated from any attribution to Lomonosov.')
talk(507,'','-','Catalogue range P000948-P000950','YEAR 1981',
     r'This catalogue record is a calendar-year divider before the 9 February MacPherson talk. No independent mathematical assertion belongs to it, so it has no occurrence-index items. The actual P000949 scan begins with the date and MacPherson heading; the catalogue divider is not represented as a separate manuscript theorem or talk. Adjacent Novikov and MacPherson material is assigned to their own manuscript headings.',kind='heading')
talk(508,'1981-02-09','Robert D. MacPherson','P000949-P000953','Grassmannian simplices, the dilogarithm, and convexity',
     r'The talk, described as joint work with I. M. Gelfand, develops positive diagonal-torus orbit closures in real Grassmannians, hypersimplex combinatorics, cross-ratios, Pontryagin-form integration, and a five-term dilogarithm identity. It then reports Atiyah\'s extensions to Kähler and symplectic geometry. The unrestricted harmonic-form assertion, the use of an orbit in place of an orbit closure, and the final Hamiltonian-orbit diagram each need distinct qualifications. The construction continues the 1979 occurrences 1979-486.12--15 and 1979-487.1--2.')
talk(509,'1981-02-16','A. G. Khovanskii','P000954-P000959','Newton polygons, genus, mixed volumes, and toric compactification',
     r'Khovanskii explains how Newton polygons determine the genus and punctures of a nondegenerate curve, derives root counts through boundary valuations, introduces mixed area, and connects Pick\'s formula and Minkowski\'s inequality with toric intersection theory. The notes cite his 1977 and 1978 papers and Danilov\'s 1978 survey. P000960 starts the 23 February meeting, so it is not part of this lecture despite the catalogue endpoint.')
talk(512,'1981-02-23','A. G. Khovanskii','P000961 (lower part)-P000962 (upper part)','Continuation: monomial charts and fans',
     r'This recovered catalogue record continues Khovanskii after the Cherednik and Gelfand interventions of 23 February. The live catalogue\'s decade typo had excluded it from the supplied academic-year list. Character--cocharacter pairings, cones of one-parameter subgroups, a modification chart, the completeness criterion, and the fan of the projective plane precede the separate Kazarnovskii heading. The actual manuscript date is 1981, not 1991.')
talk(513,'1981-02-23','B. Ya. Kazarnovskii','P000962 (lower part)-P000963; follow-up P000964','Zeros of exponential sums and mixed pseudovolume',
     r'Kazarnovskii extends Newton-polytope root counting to exponential sums with complex spectra, explains mixed pseudovolume through faces and complex tangent geometry, and mentions its support-function formulation. A separately dated 2 March question by I. M. Gelfand asks for the connection with the growth indicatrix; that follow-up is included with its own speaker and date, while the neighbouring Gaussian-tail exercise is assigned to record 514.')

# Beilinson, 17 November.
item(500,'P000937-P000938','construction','Pullback of a left D-module',
     r'For \(f:X\to Y\), the notes put \(f^*M=\mathcal O_X\otimes_{f^{-1}\mathcal O_Y}f^{-1}M\) and differentiate both factors through \(df\).',
     r'Let \(X,Y\) be smooth varieties over a characteristic-zero field and \(M\) a left \(\mathcal D_Y\)-module quasicoherent over \(\mathcal O_Y\). If \(df(v)=\sum_i a_i\otimes w_i\), the pullback left action is \(v(b\otimes m)=v(b)\otimes m+\sum_i ba_i\otimes w_i m\). The resulting module is independent of the local expression for \(df(v)\).',
     r'Smoothness, characteristic zero, and the inverse-image sheaves are written explicitly. This is the ordinary tensor pullback; it need not preserve coherent \(\mathcal D\)-modules.',
     r'This is the standard inverse-image construction of algebraic \(\mathcal D\)-module theory. The exact bimodule and action are read in \citet[\S7 and \S13]{gourevitch2025dmodules}; the contemporary framework is already represented by \citet[\S1]{bernstein1971modules}. The 2025 course is used as a precise later exposition, not a priority date.',
     [DM,'bernstein1971modules'],'D-modules')
item(500,'P000938','theorem','Pullback of connections and of the structure sheaf',
     r'The pullback agrees with the usual pullback of a bundle with flat connection, and \(f^*\mathcal O_Y=\mathcal O_X\).',
     r'For a finite-rank algebraic vector bundle \((E,\nabla)\) with integrable connection on smooth \(Y\), the displayed module action gives the integrable pullback connection on \(f^*E\); the trivial connection on \(\mathcal O_Y\) pulls back to the trivial connection on \(\mathcal O_X\).',
     '',r'The compatibility is part of the classical connection--\(\mathcal D\)-module correspondence; compare \citet[Lemma 9.11 and inverse-image construction]{gourevitch2025dmodules}.',
     [DM],'D-modules',correct='correct')
item(500,'P000938','claim','Ordinary pullback can destroy D-module coherence',
     r'For a point inclusion \(i:x\hookrightarrow Y\), the fibre of the free module \(\mathcal D_Y\) is the infinite-dimensional space of constant-coefficient differential operators.',
     r'If \(\dim Y=d>0\), then \(i^*\mathcal D_Y\simeq k[\partial_1,\ldots,\partial_d]\) as a module over \(\mathcal D_{\{x\}}=k\). Thus a coherent \(\mathcal D_Y\)-module can have an ordinary inverse image that is not coherent over \(k\).',
     r'The polynomial description uses local smooth coordinates and the positive-dimensional assumption.',
     r'The example follows directly from the Weyl-algebra normal form; see \citet[\S1.2 and inverse images]{gourevitch2025dmodules}. It is a classical warning about inverse images, not a later counterexample to holonomic stability.',
     [DM],'D-modules')
item(500,'P000938','claim','The ordinary fibre of a delta module vanishes',
     r'The notes assert \(i^*\delta_x=0\), justifying it with the written identity \(\delta(y)=y\delta^{\prime}(y)\).',
     r'For the left delta module at the origin of \(\mathbb A^d\), \(\delta_0\simeq k[\partial_1,\ldots,\partial_d]\), one has \(x_i\partial^\alpha\delta_0=-\alpha_i\partial^{\alpha-e_i}\delta_0\). Consequently each coordinate acts surjectively and \(k\otimes_{\mathcal O_{\mathbb A^d}}\delta_0=0\). The derived fibre is nonzero; in the unshifted tensor convention its only cohomology is \(k\) in degree \(-d\).',
     r'The sign is repaired: \(y\delta^{\prime}=-\delta\). Derived and ordinary pullbacks are distinguished; the Koszul-complex calculation supplies the derived degree.',
     r'The delta-module and closed-embedding calculations are classical; see \citet[Example 9.5 and Theorem 9.1]{gourevitch2025dmodules}. The sign follows from differentiating \(y\delta=0\).',
     [DM],'D-modules',correct='false as written')
item(500,'P000938','construction','The transfer bimodule and ordinary right direct image',
     r'The notebook defines \(\mathcal D_{X\to Y}=f^*\mathcal D_Y\) and \(f_*M=f_\bullet(M\otimes_{\mathcal D_X}\mathcal D_{X\to Y})\) for right modules.',
     r'For a morphism of smooth varieties, \(\mathcal D_{X\to Y}=\mathcal O_X\otimes_{f^{-1}\mathcal O_Y}f^{-1}\mathcal D_Y\) is a \((\mathcal D_X,f^{-1}\mathcal D_Y)\)-bimodule. Its underived direct image sends a right module \(M\) to \(f_\bullet(M\otimes_{\mathcal D_X}\mathcal D_{X\to Y})\).',
     r'The subscript \(\bullet\) is reserved for ordinary sheaf direct image, avoiding confusion with the differential-module direct image.',
     r'This transfer-module construction is classical and appears with the derived version in \citet[\S13]{gourevitch2025dmodules}.',
     [DM],'D-modules',correct='correct')
item(500,'P000938-P000939','construction','Closed-embedding direct images and normal delta derivatives',
     r'Pushing a scalar at a point gives a delta module; a closed embedding of a subvariety adds delta functions and derivatives in transverse directions.',
     r'If \(i:X\hookrightarrow Y\) is a closed embedding of smooth varieties, the right direct image is exact and locally adjoins freely the normal derivatives to a right \(\mathcal D_X\)-module. At a coordinate origin it sends \(k\) to \(\mathcal D_Y/\sum_j y_j\mathcal D_Y\) as a right module.',
     r'The closed and smooth hypotheses are essential. The quotient is a right-module quotient by the right ideal generated by multiplication by the coordinates, not its left-module analogue.',
     r'The exact identification is the closed-embedding calculation underlying Kashiwara\'s equivalence; \citet[Theorem 9.1, Example 9.5]{gourevitch2025dmodules} gives the read modern formulation.',
     [DM],'D-modules')
item(500,'P000939','construction','Canonical right module and conversion from left modules',
     r'Top-degree forms, and top-degree forms valued in a flat bundle, are presented as natural right modules.',
     r'For smooth \(X\), \(\omega_X=\Omega_X^{\dim X}\) has the right action \(\eta\cdot v=-\mathcal L_v\eta\). Tensoring a left module \(E\) with \(\omega_X\) gives a right module, with \((\eta\otimes e)\cdot v=(\eta\cdot v)\otimes e-\eta\otimes ve\). This is an equivalence between left and right \(\mathcal D_X\)-modules.',
     r'The signs and the full equivalence are supplied to make the note about volume forms precise.',
     r'The standard left/right conversion is read in \citet[Exercise 7.16]{gourevitch2025dmodules}; it belongs to the established theory used in the talk.',
     [DM],'D-modules')
item(500,'P000939','construction','Derived pullback and derived integration',
     r'The notes replace pullback by \(Lf^*\) and define \(\int M=Rf_\bullet(M\otimes^L_{\mathcal D_X}\mathcal D_{X\to Y})\), with its cohomology objects \(\int^iM\).',
     r'For bounded complexes of quasicoherent right \(\mathcal D_X\)-modules, define \(f_+M=Rf_\bullet(M\otimes^L_{\mathcal D_X}\mathcal D_{X\to Y})\). For left modules, the unshifted inverse image is \(\mathcal D_{X\to Y}\otimes^L_{f^{-1}\mathcal D_Y}f^{-1}N\). These derived functors retain the higher Tor and sheaf-cohomology terms lost by ordinary operations.',
     r'A bounded setting and the distinction from dimension-shifted extraordinary inverse image are stated explicitly.',
     r'These are established derived operations; see \citet[\S13]{gourevitch2025dmodules} and the derived-functor formalism in \citet[\S10.5]{weibel1994homological}.',
     [DM,'weibel1994homological'],'D-modules',correct='correct')
item(500,'P000939','theorem','Integration of the canonical module computes shifted de Rham cohomology',
     r'For smooth complex \(X\), the final formula is \(\int^i\omega_X=H^{\dim X+i}(X,\mathbb C)\).',
     r'If \(X\) is a smooth complex algebraic variety of dimension \(d\), and \(p:X\to\mathrm{pt}\), then \(p_+\omega_X\simeq R\Gamma(X,\Omega_X^\bullet)[d]\). Hence \(H^i(p_+\omega_X)\simeq H^{i+d}(X^{\mathrm{an}},\mathbb C)\) by algebraic de Rham comparison. This is ordinary cohomology, not cohomology with compact support.',
     r'The algebraic/analytic comparison and the cohomological shift convention are made explicit. Properness is unnecessary for this ordinary algebraic de Rham comparison.',
     r'The de Rham description of direct image is classical; see \citet[\S13, de Rham direct image]{gourevitch2025dmodules}. The notebook states an already established comparison, rather than a new 1980 theorem.',
     [DM],'D-modules',correct='correct')

# I. M. Gelfand's exercises.
th=item(501,'P000937','problem','Continuity and differentiability of Thomae’s function',
     r'Exercise 1 asks for the continuity and differentiability of \(f(p/q)=1/q\) for reduced fractions and \(f(x)=0\) for irrational \(x\).',
     r'On \(\mathbb R\), with \(q>0\) and \(\gcd(p,q)=1\), this function is continuous exactly at the irrational points and differentiable nowhere. At an irrational point, any derivative would be zero along irrational increments, whereas the convergents \(p_k/q_k\) satisfy \(|x-p_k/q_k|<q_k^{-2}\), so the absolute difference quotients exceed \(q_k\).',
     r'The domain, reduced denominators, and the short differentiability proof are explicit completion of the exercise.',
     r'This is the classical Thomae example. \citet[pp.353--354]{varona2009differentiability} reproduces the exact function and proof; the 2009 article is a later exposition and extension, not the origin of this elementary result.',
     ['varona2009differentiability'],'Real analysis',correct='correct',problem='GP-1980-20')
th2=item(501,'P000937','problem','Differentiability of powers of Thomae’s function',
     r'The same exercise asks what changes when \(1/q\) is replaced by \(1/q^\alpha\).',
     r'For real \(\alpha\), let \(f_\alpha(p/q)=q^{-\alpha}\), \(f_\alpha(x)=0\) at irrationals. If \(\alpha\le0\), it is nowhere continuous; if \(\alpha>0\), continuity holds exactly at irrationals. It is nowhere differentiable for \(\alpha\le2\). For \(\alpha>2\) and irrational \(x=[a_0;a_1,\ldots]\) with convergent denominators \(q_k\), differentiability is equivalent to \(q_{k+1}/q_k^{\alpha-1}\to0\), and then \(f_\alpha^{\prime}(x)=0\). Equivalently, \(q^\alpha|x-p/q|\to\infty\) along all reduced rationals tending to \(x\).',
     r'The exact continued-fraction criterion is our explicit reformulation of the difference quotient. Necessity uses \((q_k(q_k+q_{k+1}))^{-1}<|x-p_k/q_k|<(q_kq_{k+1})^{-1}\); sufficiency also uses that a nonconvergent approximation has error at least \(1/(2q^2)\). Statements using only the irrationality exponent require care at equality.',
     r'The family had already been studied by Nymann in 1969, as documented in \citet[introduction, \S\S1--3, reference 7]{varona2009differentiability}; that article gives further exact differentiability and measure statements. Thus the exercise is not classified as an unresolved 1980 conjecture. No assertion that the present denominator formulation first appeared in 1969 is made.',
     ['varona2009differentiability'],'Real analysis and Diophantine approximation',correct='correct',problem='GP-1980-20')
di=item(501,'P000937','construction','A double continuous limit for the Dirichlet function',
     r'Exercise 2 gives \(\lim_{n\to\infty}\lim_{m\to\infty}\cos^{2m}(2\pi n!x)\).',
     r'For every real \(x\), this iterated limit equals \(\mathbf1_{\mathbb Q}(x)\). For fixed \(n\), the inner limit is one exactly when \(2n!x\in\mathbb Z\), and zero otherwise. Every rational satisfies the condition for all sufficiently large \(n\), whereas an irrational never does.',
     r'The order of limits is essential and is retained. This elementary calculation proves the formula without interchanging limits.',
     r'This is the classical distinction between first and second Baire class. The underlying classification was established before 1900; \citet[p.173]{baire1900nouvelle} states the continuous-limit criterion. The displayed factorial formula is checked directly here, not attributed to that article.',
     ['baire1900nouvelle'],'Real analysis',correct='correct')
di2=item(501,'P000937','problem','Can the Dirichlet function be a pointwise limit of continuous functions?',
     r'Exercise 3 asks whether a single sequence of continuous functions can tend pointwise to the Dirichlet function.',
     r'No sequence \(g_j\in C(\mathbb R)\) converges at every real point to \(\mathbf1_{\mathbb Q}\). A real-valued Baire-class-one function has a dense \(G_\delta\) set of continuity points on every nonempty closed interval, while \(\mathbf1_{\mathbb Q}\) is nowhere continuous.',
     r'Pointwise convergence at every point is the required meaning; convergence almost everywhere would give a different, trivial answer.',
     r'The negative answer is an immediate classical consequence of Baire\'s criterion; see \citet[p.173, opening theorem and reference to the 1899 thesis]{baire1900nouvelle}.',
     ['baire1900nouvelle'],'Real analysis',correct='correct',problem='GP-1980-21')
oi=item(501,'P000937','problem','Fourier integrals with quadratic, quartic, and sextic decay',
     r'Exercise 4 asks for approximate values of \(\int_{-\infty}^{\infty}e^{-x^2}\cos(1000x)\,dx\), and the analogues with \(x^4\) and \(x^6\).',
     r'Write \(I_p(\lambda)=\int_{\mathbb R}e^{-x^p}\cos(\lambda x)\,dx\). Then \(I_2(1000)=\sqrt\pi e^{-250000}\). For \(p=4,6\), put \(r=(\lambda/p)^{1/(p-1)}\), \(\theta=\pi/(2(p-1))\), \(A=(p-1)r^p\). As \(\lambda\to+\infty\), the two dominant conjugate saddle contributions give \[I_p(\lambda)=2\sqrt{\frac{2\pi}{p(p-1)}}r^{-(p-2)/2}e^{-A\sin\theta}\left\{\cos\!\left(A\cos\theta-\frac{p-2}{2}\theta\right)+O(A^{-1})\right\}.\] The remainder is absolute relative to the displayed envelope, not relative to the cosine, which can vanish.',
     r'The parameter \(\lambda\), saddle computation, and error convention are supplied; the notebook asks only for approximations. Saddles solve \(pz^{p-1}=i\lambda\). The quartic and sextic formulas are explicit applications of the classical method, not a claimed new asymptotic theorem.',
     r'Gaussian Fourier transformation and steepest descent predate the seminar. The simple-saddle expansion and branch convention are checked in \citet[\S2.4(iv), equations 2.4.15--16]{nist2026dlmf}; its cited pre-1980 sources include Olver and Bleistein--Handelsman. The displayed specialization is our calculation.',
     ['nist2026dlmf'],'Asymptotic analysis',correct='correct',problem='GP-1980-22',confidence='medium')

# S. I. Gelfand.
ch=item(502,'P000940','problem','Isomorphic cohomology need not lift to a chain map',
     r'Exercise 1 says that an isomorphism of the cohomology of two complexes need not extend to a chain map inducing it.',
     r'In complexes of abelian groups, let \(A=(\mathbb Z/2)[0]\), and let \(B\) be \(\mathbb Z\xrightarrow{2}\mathbb Z\) in degrees \(-1,0\). Both have only \(H^0\simeq\mathbb Z/2\). Every chain map \(A\to B\) is zero because \(\operatorname{Hom}(\mathbb Z/2,\mathbb Z)=0\); hence none induces the prescribed identity on \(H^0\). They are nevertheless isomorphic in the derived category through the quasi-isomorphism \(B\to A\).',
     r'The explicit example and the direction of the attempted map are supplied. Over a field, complexes split and this particular obstruction disappears; the ambient abelian category cannot be omitted.',
     r'This is established homological algebra, explained by localization at quasi-isomorphisms; see \citet[\S\S10.1--10.3]{weibel1994homological}. It continues earlier seminar discussions of the derived-category universal property, especially 1971-266.3.',
     ['weibel1994homological'],'Homological algebra',correct='correct',problem='GP-1980-23')
item(502,'P000940','claim','An unspecified derived equivalence between a sphere and its dual',
     r'The notes write sheaf categories \(C,C_1\) on \(S^n,S^{*n}\), an \(O(n)\)-action, \(C_1\not\simeq C\) because the action differs, and \(D(S)\sim D(S^*)\).',
     r'An exact equivalence cannot be specified from the record: the definition of the dual sphere, the action on each category, the coefficients and boundedness or constructibility restrictions, and the transforming kernel are absent. With the standard Euclidean duality and orthogonal action, the spheres are already equivariantly isomorphic, so their ordinary sheaf categories are equivalent; that literal reading does not produce the claimed distinction.',
     r'No Radon-transform equivalence is substituted for the missing assertion. Such a reconstruction would require extra geometry not fixed by the manuscript.',
     r'Searches for S. I. Gelfand, dual spheres, equivariant sheaves, and derived/Radon transformations did not establish an exact publication match. \citet[Chapter 10]{weibel1994homological} supplies only the general derived-category language, not this claimed equivalence.',
     ['weibel1994homological'],'Sheaf theory',cls='F',correct='not determinable',match='none found',verification='unresolved lead',confidence='low',status=r'As of November 2026, the exact assertion and its fate remain unidentifiable from the surviving formulation; this is a source ambiguity, not a well-posed open problem.')

save()

# Beilinson, 24 November.
item(503,'P000940-P000941','method','Pulling solutions back and integrating solutions along fibres',
     r'The transfer-module formulas are repeated with the explanation that pullback carries solutions to solutions and direct image supplies equations for integrals, including improper integrals.',
     r'For a morphism of smooth characteristic-zero varieties, inverse-image modules encode the chain rule and derived direct-image modules encode relative de Rham classes. In an analytic realization, an integral of a differential form solving a \(\mathcal D_X\)-system gives a solution of the appropriate direct-image system when differentiation under the integral and integration by parts are valid, for example along a proper smoothly varying closed cycle or with controlled compact support.',
     r'The analytic convergence, boundary, and differentiation conditions are supplied; the bare module formula does not justify arbitrary improper integration.',
     r'This is the established direct-image interpretation of differential equations and periods; see \citet[\S13, especially the de Rham and Gauss--Manin discussion]{gourevitch2025dmodules}. It repeats the construction of 1980-500.5 and develops its analytic meaning.',
     [DM],'D-modules and period integrals')
item(503,'P000941','theorem','Derived direct images compose',
     r'The underived operation is said not to satisfy composition; equation (7) states \(Rg_*Rf_*=R(g\circ f)_*\).',
     r'For morphisms \(X\xrightarrow fY\xrightarrow gZ\) of smooth varieties in characteristic zero, the derived right-module direct images satisfy a natural isomorphism \(g_+f_+\simeq(gf)_+\) on the bounded quasicoherent derived categories where these operations are defined. The ordinary tensor-and-sheaf-direct-image construction can lose higher cohomology and does not in general have this property.',
     r'The notation \(f_+\) distinguishes this operation from the ordinary derived direct image of sheaves. The assertion concerns natural derived isomorphisms, not equality of chosen complexes.',
     r'The exact composition theorem is read in \citet[Theorem 13.22]{gourevitch2025dmodules}. Its mechanism is associativity of derived tensor products and the derived projection formula, established before this expository lecture.',
     [DM],'D-modules',correct='correct')
item(503,'P000941','construction','Projection of a plane and the degree minus one direct image',
     r'For the projection of a plane to a line, the direct image of volume forms has zero degree-zero component and volume forms on the line in degree \(-1\).',
     r'For the algebraic projection \(f:\mathbb A^2\to\mathbb A^1\) over a characteristic-zero field, \(f_+\omega_{\mathbb A^2}\simeq\omega_{\mathbb A^1}[1]\). Its only cohomology is \(H^{-1}=\omega_{\mathbb A^1}\). Relative de Rham cohomology of the affine-line fibre is concentrated in unshifted degree zero.',
     r'The notes\' word “component” is read as a cohomology object, not a canonical zero/nonzero pattern for every representative complex. The affine algebraic setting fixes the cohomology convention.',
     r'This elementary instance of the relative de Rham description is verified from \citet[\S13]{gourevitch2025dmodules}.',
     [DM],'D-modules')
item(503,'P000941','construction','The right-module Spencer complex and de Rham shift',
     r'The complex \(\cdots\to M\otimes\Lambda^2T_X\to M\otimes T_X\to M\) computes direct image to a point. For volume forms, it is called the de Rham complex shifted to the left by a symbol transcribed as \(M\).',
     r'For a right module \(M\) on smooth \(d\)-dimensional \(X\), the Spencer differential uses the right vector-field action and Lie brackets on \(M\otimes_{\mathcal O_X}\Lambda^jT_X\), placed in degree \(-j\). This complex computes \(M\otimes^L_{\mathcal D_X}\mathcal O_X\); applying \(R\Gamma\) computes \(p_+M\). For \(M=\omega_X\), contraction identifies it with \(\Omega_X^\bullet[d]\).',
     r'The shift is \(d=\dim X\), as confirmed by the following displayed formula \(R^ip_*\omega_X=H^{d+i}(X)\); the ambiguous handwritten symbol cannot serve as a shift index.',
     r'The Spencer resolution and de Rham interpretation are standard; see \citet[\S13]{gourevitch2025dmodules}. This makes explicit the calculation already announced in 1980-500.9.',
     [DM],'D-modules',correct='correct with missing hypotheses')
item(503,'P000941-P000942','construction','Relative de Rham cohomology and the Gauss–Manin action',
     r'For a smooth morphism, the relative tangent complex is pushed forward and receives a \(\mathcal D_Y\)-action called the Gauss--Manin connection.',
     r'If \(f:X\to Y\) is smooth between smooth varieties, the relative Spencer complex computes direct image after the canonical left/right conversion and the appropriate relative-dimension shift. For a smooth proper morphism and a finite-rank integrable connection on \(X\), its relative de Rham cohomology sheaves are locally free and carry integrable Gauss--Manin connections, compatible with the \(\mathcal D_Y\)-module direct image.',
     r'The canonical-bundle conversion is necessary for a right-module formula: locally \(\omega_X\simeq\omega_{X/Y}\otimes f^*\omega_Y\). Properness is added only for the stated finite-rank bundle conclusion; without it the direct image is still a derived \(\mathcal D\)-module and need not be a vector bundle.',
     r'The exact smooth-proper connection statement and its qualifications are read in \citet[\S13, Gauss--Manin discussion]{gourevitch2025dmodules}.',
     [DM],'D-modules and variations of cohomology')
item(503,'P000942','theorem','Closed-embedding exactness and Kashiwara equivalence',
     r'For an “embedding”, both direct-image steps are said to be exact; volume forms become delta forms in normal directions.',
     r'For a closed embedding \(i:X\hookrightarrow Y\) of smooth varieties, the transfer bimodule is flat for the required left \(\mathcal D_X\)-action, and \(i_+\) is exact on modules. It identifies \(\mathcal D_X\)-modules with \(\mathcal D_Y\)-modules supported on \(X\), with an inverse given by the appropriate degree of extraordinary restriction.',
     r'“Closed” must be supplied; an arbitrary open or locally closed embedding does not make ordinary sheaf direct image exact in the same fashion.',
     r'This is Kashiwara\'s equivalence, read in \citet[Theorem 9.1]{gourevitch2025dmodules} and independently in \citet[\S8]{bernstein1982dmodules}. The later lecture notes are verification sources for an already established theorem.',
     [DM,'bernstein1982dmodules'],'D-modules')
item(503,'P000942','definition','Holonomicity tested by all derived point fibres',
     r'A finitely generated module is called holonomic if the cohomology of \(Li_x^*M\) is finite-dimensional for every point. The free module is explicitly excluded.',
     r'For a coherent \(\mathcal D_X\)-module on a smooth complex algebraic variety, holonomicity is equivalent to finite-dimensional cohomology of its derived inverse image at every closed point. Equivalently, its nonempty characteristic variety has dimension \(\dim X\). A nonzero locally free \(\mathcal D_X\)-module is not holonomic if \(\dim X>0\). Dimension shifts between \(i^*\) and \(i^!\) do not affect this finiteness test.',
     r'Coherence, the complex algebraic category, and derived rather than ordinary fibres are essential. For example, the ordinary fibre of a delta module vanishes, while its derived fibre does not.',
     r'The exact converse as well as the forward implication are read in \citet[Proposition 16.6]{gourevitch2025dmodules}. The foundational dimension framework is in \citet[\S\S1--3]{bernstein1971modules}.',
     [DM,'bernstein1971modules'],'D-modules')
item(503,'P000942','claim','Generic connections and gluing holonomic modules along strata',
     r'The examples say that a holonomic module is a flat bundle away from exceptional points or curves, and ask whether all such modules are glued from transverse delta modules.',
     r'A holonomic module has a finite algebraic stratification of its support such that the appropriate restrictions to smooth strata are finite-rank integrable connections. Its simple constituents are minimal extensions of irreducible connections on dense smooth locally closed strata; general holonomic modules are finite successive extensions of these. This does not assert a direct-sum decomposition, regular singularities, or a classification by arbitrary gluing matrices.',
     r'The circled question is resolved in the precise finite-extension sense supplied by the following finite-length and simple-object statements. “Away from curves” on a surface is not an assertion that every module has full support.',
     r'The reconstruction follows the structure results read in \citet[\S\S16--17, especially Lemma 16.18 and Theorem 17.2]{gourevitch2025dmodules}; the next notebook page itself supplies these two ingredients.',
     [DM],'D-modules',match='partial')
item(503,'P000943','theorem','Finite length of holonomic modules',
     r'Theorem (15)(1) states finite length and equality of the lengths of filtrations with irreducible factors.',
     r'The category of holonomic \(\mathcal D_X\)-modules on a smooth characteristic-zero algebraic variety is both noetherian and artinian. Every object admits a finite composition series; the multiset of simple factors, with multiplicities, is independent of the series.',
     r'The Jordan--Hölder conclusion is stated in its stronger usual form, including multiplicities rather than only length.',
     r'Finite length is classical holonomic-module theory. The exact statement and its proof using duality are read in \citet[Lemma 16.18]{gourevitch2025dmodules}; compare the early finiteness framework in \citet[\S3]{bernstein1971modules}.',
     [DM,'bernstein1971modules'],'D-modules',correct='correct')
item(503,'P000943','theorem','Simple holonomic modules as minimal extensions',
     r'The notes classify irreducibles by an irreducible variety and irreducible flat bundle, identify pairs after shrinking, and claim a unique irreducible submodule of \(i_*\mathcal L_Y\).',
     r'Simple holonomic modules on smooth \(X\) correspond to pairs consisting of an irreducible closed support \(Z\subset X\) and an irreducible integrable connection on a nonempty smooth open subset \(U\subset Z\), modulo isomorphism after further shrinking. The corresponding module is the intermediate extension to \(X\); equivalently, it is the unique simple submodule of \(H^0j_+\mathcal L\) for the locally closed embedding \(j:U\hookrightarrow X\).',
     r'The connection lives on a smooth dense open subset, not necessarily all of a singular support. Equivalence is generated by restriction to a common dense open, rather than the asymmetric single inclusion written in the notes.',
     r'The exact minimal-extension classification is read in \citet[Theorem 17.2]{gourevitch2025dmodules}. It is standard holonomic theory and does not require regular singularities unless one also invokes a constructible-sheaf Riemann--Hilbert equivalence.',
     [DM],'D-modules')
item(503,'P000943','claim','Smoothness alone does not make a direct image simple',
     r'The final line says that if \(Y\) is smooth, the direct image is already irreducible.',
     r'This is valid for a closed embedding of smooth varieties and a simple source module, by Kashiwara equivalence. It is false for a general locally closed embedding: for \(j:\mathbb G_m\hookrightarrow\mathbb A^1\), the simple connection \(\mathcal O_{\mathbb G_m}\) has \(j_+\mathcal O_{\mathbb G_m}=\mathcal O_{\mathbb A^1}(*0)\), which contains the proper nonzero submodule \(\mathcal O_{\mathbb A^1}\). Its quotient is supported at the origin.',
     r'The counterexample distinguishes smooth source from closed support and explains why intermediate extension is needed.',
     r'The exact closed-embedding and intermediate-extension theorems are read in \citet[Theorems 9.1 and 17.2]{gourevitch2025dmodules}; the localization counterexample is a direct calculation in the first Weyl algebra.',
     [DM],'D-modules',correct='false as written')

# Short interventions.
item(504,'P000940','construction','Whitehead product from the boundary of a product of cubes',
     r'The notes write \(\pi_n(X)\times\pi_m(X)\to\pi_{n+m}(X)\) and decompose \(\partial(I^n\times I^m)\).',
     r'For a pointed space and \(n,m\ge2\), the Whitehead product is \([\ ,\ ]:\pi_n(X)\times\pi_m(X)\to\pi_{n+m-1}(X)\). Representatives on \(I^n/\partial I^n\) and \(I^m/\partial I^m\) define the map on the two pieces of the boundary of \(I^n\times I^m\), agreeing at the basepoint on their intersection.',
     r'The target is corrected by one degree; the boundary has dimension \(n+m-1\). Low-dimensional nonabelian variants are not needed for the next graded statement.',
     r'This is Whitehead\'s classical construction; the attaching-map formulation is read in \citet[\S4.2, p.381]{hatcher2002algebraic}.',
     ['hatcher2002algebraic'],'Algebraic topology',correct='false as written')
item(504,'P000940','theorem','Shifted graded Jacobi identity for Whitehead products',
     r'The note compares the product to a Lie bracket and says that the Jacobi identity holds, with a “super” sign convention.',
     r'After the usual sign adjustment identifying Whitehead products with Samelson products in \(\Omega X\), the graded group \(L_d=\pi_{d+1}(X)\), \(d\ge1\), satisfies \([a,b]=-(-1)^{|a||b|}[b,a]\) and \((-1)^{|a||c|}[a,[b,c]]+(-1)^{|b||a|}[b,[c,a]]+(-1)^{|c||b|}[c,[a,b]]=0\). Over \(\mathbb Z\), torsion can prevent the alternating axiom \([a,a]=0\) in even degree; after tensoring with \(\mathbb Q\), this is a graded Lie algebra in the usual sense.',
     r'The degree shift and the integral torsion caveat are supplied. The notebook\'s analogy should not be read as an unrestricted ordinary Lie algebra on unshifted homotopy groups.',
     r'The identity predates the talk by decades. \citet[p.180, publisher extract]{hilton1961jacobi} explicitly describes the already-known identity; the 1961 print date is distinct from the 2008 digital posting. Only the extract, not the full three-page proof, was read.',
     ['hilton1961jacobi'],'Algebraic topology',verification='publisher metadata checked')
item(505,'P000940','claim','An ambiguous four-operator perturbation assertion',
     r'The manuscript has \(A-A^{\prime}\) nuclear, \([B,A]=[B,A^{\prime}]=0\), \(B-B^{\prime}\) completely continuous, and concludes \(B|_{\mathcal H_{ac}(B)}\simeq B^{\prime}|_{\mathcal H_{ac}(B^{\prime})}\). It then proposes treating commuting families directly.',
     r'The exact intended theorem is undetermined. A valid nearby statement is: for bounded self-adjoint \(A,A^{\prime},B,B^{\prime}\), if \(A-A^{\prime}\) is trace class, \([A,B]=[A^{\prime},B^{\prime}]=0\), and \(B-B^{\prime}\) is compact, the complete wave operators \(W_\pm(A^{\prime},A)\) intertwine \(B|_{\mathcal H_{ac}(A)}\) and \(B^{\prime}|_{\mathcal H_{ac}(A^{\prime})}\). They are unitary between those two spectral subspaces.',
     r'This repair changes both the second commutator and the operators defining the absolutely continuous subspaces; it is ours, not a corrected reading. Indeed \(e^{-itA}u\rightharpoonup0\) on \(\mathcal H_{ac}(A)\), so \((B^{\prime}-B)e^{-itA}u\to0\) in norm. Passing to the wave-operator limit proves the extra intertwining. The literal conditions, with \(A=A^{\prime}=0\), would impose no control beyond compact perturbation on \(B,B^{\prime}\), which is insufficient to preserve absolutely continuous spectrum.',
     r'\citet[Theorem 1, pp.260--261]{kato1957trace} proves the required complete wave operators, already in 1957. The compact-perturbation counterexample follows from the classical Weyl--von Neumann theorem, whose exact statement is read in \citet[Theorem 1.1]{andomatsuzawa2014weyl}. Lomonosov\'s \citet[pp.54--55]{lomonosov1980intertwiner} is a bibliographically verified contemporary lead, received 11 December 1978; its full text was not retrieved and it is not claimed as a match. The commuting-family remark has no recoverable additional hypotheses.',
     ['kato1957trace','lomonosov1980intertwiner','andomatsuzawa2014weyl'],'Operator theory',cls='F',correct='false as written',match='thematic only',verification='unresolved lead',confidence='low',status=r'As of November 2026, the repaired statement is a standard consequence of trace-class scattering theory, but the exact Lomonosov assertion and its publication fate remain unresolved at the source-identification level. No open mathematical problem is inferred.')

corr('P000938','delta-module pullback example',r'\(\delta(y)=y\delta^{\prime}(y)\)',r'\(\delta(y)=-y\delta^{\prime}(y)\)',r'The scan has no minus sign. Differentiating y delta=0 gives delta+y delta-prime=0. Faithful mathematical emendation.')
corr('P000940','Fuchs Whitehead-product target',r'\(\pi_{n+m}(X)\)',r'\(\pi_{n+m-1}(X)\)',r'The actual scan has n+m. The boundary of I^n times I^m has dimension n+m-1; Hatcher section4.2 p381.')
corr('P000940','Lomonosov second commutator and spectral subspaces',r'\([B,A^{\prime}]=0\); \(\mathcal H_{ac}(B),\mathcal H_{ac}(B^{\prime})\)',r'Leave the literal text; annotate the possible repair \([B^{\prime},A^{\prime}]=0\), \(\mathcal H_{ac}(A),\mathcal H_{ac}(A^{\prime})\).',r'Scan explicitly shows B without a prime before A-prime and B in the spectral-subspace labels. No textual authority for silently replacing them; item1980-505.1 distinguishes the reconstruction.','ambiguity')
corr('P000941','de Rham shift after equation10',r'shifted to the left by \(\mathcal M\)',r'shifted to the left by \(\dim X\), as a mathematical reconstruction',r'The symbol resembles the module M in the scan; the next displayed equation fixes the intended dimensional shift.','ambiguity')
corr('P000942','exactness for an embedding',r'\(f\) an embedding',r'\(f\) a closed embedding of smooth varieties',r'Both exactness claims are the closed-embedding theorem. They do not hold for arbitrary open embeddings in the same form.')
corr('P000943','final irreducibility line',r'\(Y\) smooth implies already irreducible',r'For a closed embedding, a simple module stays simple; otherwise use intermediate extension.',r'The scan contains no closedness condition. The open immersion G_m into A^1 gives O(*0), with the proper submodule O.')
save()

GM='gelfandmacpherson1982geometry'; AT='atiyah1982convexity'
gmdate=r'The work was published by Gelfand and MacPherson in June 1982; this 9 February 1981 seminar is a verified earlier oral occurrence. No earlier public preprint date was independently established.'
item(508,'P000949','definition','Grassmannian dimension notation and coordinate inclusions',
     r'The talk uses \(G_n^m\) for \(n\)-planes in \(\mathbb R^{n+m}\) and arranges coordinate inclusions in a two-dimensional array.',
     r'Write \(G_n^m=\operatorname{Gr}_n(\mathbb R^{n+m})\), of dimension \(nm\). The horizontal inclusion adds an unused coordinate; the vertical inclusion sends \(V\) to \(V\oplus\mathbb R e_{n+m+1}\). Equivalently \(G_n^m\) parametrizes projective \((n-1)\)-planes in \(\mathbb{RP}^{n+m-1}\).',
     r'The third entry in the second row must be \(G_2^3\), not the handwritten \(G_1^3\). These coordinate choices specify which smaller Grassmannians contain faces.',
     r'The underlying coordinate Grassmannian geometry is classical; compare the explicit Grassmannian setting in \citet[pp.13--14]{atiyah1982convexity}. The table is checked directly from its dimensions.',
     [AT],'Grassmannian geometry',correct='false as written')
item(508,'P000949','remark','The inadequately specified geodesic-simplex construction',
     r'The opening asks for polyhedra whose faces lie in smaller Grassmannians; it says that filling a triangle with geodesic segments fails when the rank is at least two.',
     r'The record does not specify a metric, a canonical filling rule, or an exact compatibility condition that is alleged to fail. Thus it records motivation for using torus orbit closures, rather than a quantified nonexistence theorem for geodesic simplices.',
     r'No universal claim that higher-rank Grassmannians lack totally geodesic simplices is inferred. Totally geodesic subspaces and small geodesic triangles certainly exist.',
     r'The subsequent construction has a precise publication match in \citet{gelfandmacpherson1982geometry}, but no exact theorem corresponding to this preliminary objection was identified. The previous problem GP-1979-04 concerns a Grassmannian counterpart of a projective-space linear model; title-level resemblance does not establish that its exact question recurs here.',
     [GM],'Grassmannian geometry',cls='F',correct='not determinable',match='thematic only',verification='indirect',confidence='low',status=r'As of November 2026, this motivating remark does not determine an independently assessable mathematical problem.')
item(508,'P000949','definition','The hypersimplex',
     r'\(\Delta_n^m\) is defined by \(0\le x_i\le1\) and \(\sum x_i=n\).',
     r'For positive integers \(n,m\), put \(N=n+m\) and \(\Delta(n,N)=\{x\in[0,1]^N:\sum_i x_i=n\}\). This \((N-1)\)-dimensional polytope is the convex hull of the characteristic vectors of all \(n\)-element subsets of \(\{1,\ldots,N\}\).',
     r'The vertex description and dimension are explicit consequences of the inequalities; \(\Delta_n^m=\Delta(n,n+m)\).',
     r'The combinatorial object is classical and already occurs in 1979-486.2. Its Grassmannian realization is part of \citet{gelfandmacpherson1982geometry}; see also the read orbit-polytope theorem \citet[Theorem 2′, p.13]{atiyah1982convexity}.',
     [GM,AT],'Convex and Grassmannian geometry',correct='correct')
item(508,'P000949','construction','Positive torus orbit closures and the genericity condition',
     r'A projective frame determines the identity component \(H^0\) of its stabilizer. A Grassmannian simplex is the closure of a generic orbit; generic means transverse to every coordinate subspace, not merely maximal orbit dimension.',
     r'In \(\operatorname{Gr}_n(\mathbb R^N)\), let \(H=(\mathbb R_{>0})^N/\mathbb R_{>0}\) act diagonally. If every Plücker coordinate \(p_I(V)\) is nonzero, define the Grassmannian simplex to be \(\overline{H\cdot V}\). The open orbit has dimension \(N-1\). Nonvanishing of all Plücker coordinates is stronger than maximal orbit dimension and is equivalent to the stated coordinate general-position condition.',
     r'The central scalar quotient, all-minor condition, and orbit closure are explicit. Non-generic supports generally yield smaller matroid polytopes, not the full hypersimplex.',
     r'This is the announced Gelfand--MacPherson construction, explicitly identified by \citet[p.13]{atiyah1982convexity}. '+gmdate,
     [GM,AT],'Grassmannian geometry',cls='A',correct='correct',status=r'As of November 2026, this construction is established. The distinction between full Plücker support and maximal orbit dimension remains essential.')
item(508,'P000950; P000952-P000953','theorem','The orbit closure is a hypersimplex with its face stratification',
     r'P000950 calls the two objects diffeomorphic; P000952 identifies face interiors with positive-torus orbits, and P000953 corrects the global conclusion to homeomorphism with smoothness on individual orbits.',
     r'For the generic \(V\) above, the Grassmannian moment map restricts to a homeomorphism \(\overline{H\cdot V}\to\Delta(n,N)\). One convenient expression is \(\mu(V)=\sum_I |p_I(V)|^2\mathbf1_I/\sum_I|p_I(V)|^2\). Each positive orbit maps diffeomorphically to a relative face interior. A global diffeomorphism of embedded orbit closures is not asserted; boundary strata can be singular.',
     r'The corrected conclusion follows the notebook\'s own later qualification. The formula fixes the normalization and makes the polytope correspondence concrete.',
     r'\citet[Theorems 2 and 2′, pp.3 and 13]{atiyah1982convexity} proves the exact orbit-closure statement and explicitly identifies the real-Grassmannian case with Gelfand--MacPherson. '+gmdate,
     [GM,AT],'Grassmannian and symplectic geometry',cls='A',correct='false as written',status=r'As of November 2026, the homeomorphism and orbit-by-face smoothness are established; the initial unrestricted diffeomorphism wording requires the recorded correction.')
item(508,'P000950','construction','The projective triangle and its dual Grassmannian triangle',
     r'The examples \(G_1^2\) and \(G_2^1\) give four triangular chambers in the projective plane and a dual triangle of lines, with sides in \(G_1^1\).',
     r'The complement of the three coordinate lines in \(\mathbb{RP}^2\) has four sign chambers, each a positive diagonal orbit; its closure is a triangle. Dually, two-planes in \(\mathbb R^3\) are kernels of nonzero covectors, and each covector-sign chamber similarly gives a triangle. Its edges consist of planes containing a fixed coordinate axis, and its vertices are coordinate two-planes.',
     r'The dual description depends on the selected sign chamber. The informal phrase about lines avoiding a hatched region is interpreted through these explicit coordinate conditions.',
     r'These elementary models are exact special cases of the orbit-closure construction; \citet[Theorem 2′]{atiyah1982convexity}. They are already implicit in the earlier configuration descriptions 1979-487.1--2.',
     [AT,GM],'Projective geometry',cls='A',status=r'As of November 2026, the coordinate and dual models are established; the drawings specify a chosen chamber, not the whole dual projective plane.')
item(508,'P000951','construction','The octahedron and the cross-ratio in Gr(2,4)',
     r'\(G_2^2\) is four-dimensional, its positive orbit is three-dimensional, and the cross-ratio of four planes through a projective line is constant along the orbit. The six vertices are labelled by pairs.',
     r'For a generic projective line \(\ell\subset\mathbb{RP}^3\), the planes spanned by \(\ell\) and the four coordinate points determine four distinct points in the projective line of planes through \(\ell\). Their cross-ratio is invariant under diagonal transformations. The positive-orbit closure is \(\Delta(2,4)\), an octahedron with six pair-labelled vertices and eight triangular facets, four of each coordinate-facet type.',
     r'Cross-ratio conventions and sign chambers must be fixed to identify a particular connected orbit in a level set; the notes state only containment in a level set.',
     r'This is the same four-ray/cross-ratio geometry discussed in 1979-486.12--13. The hypersimplex identification follows the exact theorem read in \citet[Theorem 2′]{atiyah1982convexity}; its use in the dilogarithm construction was published in \citet{gelfandmacpherson1982geometry}.',
     [GM,AT],'Grassmannian and projective geometry',cls='A',correct='correct',status=r'As of November 2026, the octahedral model and cross-ratio invariant are established.')
item(508,'P000951','claim','Dilogarithmic volume between two Grassmannian simplices',
     r'The recorded volume between \(K=c_1\) and \(K=c_2\), with \(0<c_1<c_2<1\), is \(\Phi(c_1)-\Phi(c_2)\), where \(\Phi(x)=\operatorname{Li}_2(x)-\operatorname{Li}_2(1-x)\).',
     r'The formula can describe an oriented, normalized characteristic-form integral, but it cannot literally be an unsigned positive volume with the stated order: \(\Phi^{\prime}(x)=-\log(1-x)/x-\log x/(1-x)>0\). The natural increasing primitive satisfies \(\Phi=2L-\pi^2/6\), where \(L(x)=\operatorname{Li}_2(x)+\tfrac12\log x\log(1-x)\) is the Rogers dilogarithm. An unsigned volume requires the opposite difference after fixing the form normalization.',
     r'The sign test is direct. The exact normalization of the invariant four-form, orientation of the slab, and choice of cross-ratio are not recoverable from this line alone, so no numerical constant is silently supplied.',
     r'The geometric dilogarithm construction is the subject of \citet{gelfandmacpherson1982geometry}; publisher metadata is verified, but its full text was not retrieved. The precise Rogers identity and normalization are read in \citet[Chapter II, \S1.A]{zagier2007dilogarithm}. '+gmdate,
     [GM,'zagier2007dilogarithm'],'Characteristic classes and special functions',cls='A',correct='false as written',match='partial',verification='indirect',confidence='medium',status=r'As of November 2026, the characteristic-form/dilogarithm construction is established, but the notebook\'s unsigned-volume wording has a sign defect and omits normalization.')
item(508,'P000952','construction','The two families of hypersimplex boundary faces',
     r'Equation (12) starts an alternating boundary sum over \(x_i=0\) faces and then breaks off in the second family; its second lower limit is written \(-1\).',
     r'For \(1<n<N-1\), the facets of \(\Delta(n,N)\) are \(x_i=0\), isomorphic to \(\Delta(n,N-1)\), and \(x_i=1\), isomorphic to \(\Delta(n-1,N-1)\). Giving the ambient affine hyperplane and each facet compatible orientations yields its ordinary signed cellular boundary. At \(n=1\) or \(n=N-1\), the degenerate family must be omitted as a family of facets.',
     r'The missing \(x_i=1\) condition and index range \(i=1,\ldots,N\) are reconstructed from the defining inequalities. The incomplete manuscript does not determine a fully checked orientation-sign formula.',
     r'The face geometry is elementary and underlies \citet{gelfandmacpherson1982geometry}; the face/orbit compatibility is independently read in \citet[Theorem 2]{atiyah1982convexity}. No unverified completion of the alternating signs is represented as a transcription.',
     [GM,AT],'Convex geometry',correct='not determinable',match='partial',confidence='medium')
item(508,'P000952','theorem','Vanishing of harmonic forms on real Grassmannian simplices',
     r'Equation (13) claims that every harmonic form on \(G_n^m\), for a coordinate-compatible metric, vanishes on every Grassmannian simplex.',
     r'For the unoriented real Grassmannian \(G_n^m\) with \(nm\) even and its orthogonally invariant metric, every harmonic differential form of positive degree restricts to zero on each positive diagonal orbit. The same assertion holds for the corresponding invariant positive-degree forms. Constants are excluded; the unrestricted assertion fails in general for \(nm\) odd and for oriented Grassmannians.',
     r'Positive degree, the unoriented space, and the parity hypothesis are supplied from the primary theorem. Restriction is understood on the smooth orbit strata, avoiding a fictitious smooth structure at singular boundary points.',
     r'\citet[pp.13--14, discussion before and after Theorem 4]{atiyah1982convexity} states this Gelfand--MacPherson result, gives a new proof, and explicitly records the odd-dimensional and oriented failures. '+gmdate,
     [GM,AT],'Grassmannian geometry and harmonic forms',cls='A',correct='false as written',status=r'As of November 2026, the qualified vanishing theorem is established; the literal all-degrees, all-Grassmannians formulation is false.')
item(508,'P000952','theorem','Five configurations and the differential five-term identity',
     r'Five points on \(\mathbb P^1\), modulo projectivities, form a two-dimensional space. Omitting each point gives a cross-ratio \(k_i\), and equation (14) alternates the differentials \(d\Phi(k_i)\).',
     r'The moduli space of five ordered distinct points on \(\mathbb P^1\) modulo \(\operatorname{PGL}_2\) has dimension two. On a real chamber with consistent cross-ratio conventions, the five-term relation is equivalent to the Rogers identity, for \(0<x,y<1\): \[L(x)+L(y)=L(xy)+L\!\left(\frac{x(1-y)}{1-xy}\right)+L\!\left(\frac{y(1-x)}{1-xy}\right).\] Since \(\Phi=2L-\pi^2/6\), differentiating gives a five-term zero relation; its displayed signs depend on the ordered cross-ratios.',
     r'A concrete branch-free chamber and the exact five arguments replace the notebook\'s unspecified cross-ratio convention. The constant in the corresponding undifferentiated \(\Phi\)-relation is \(\pi^2/6\).',
     r'The analytic identity is classical, not new in 1981; its exact Rogers form is read in \citet[Chapter II, \S1.A]{zagier2007dilogarithm}. The geometric derivation is the Gelfand--MacPherson contribution discussed separately below.',
     ['zagier2007dilogarithm'],'Special functions and moduli',correct='correct with missing hypotheses')
item(508,'P000952-P000953','method','Pontryagin-form fibre integration and Stokes’ formula',
     r'The notes use the first Pontryagin form on \(G_3^2\), say its harmonic degree-four space is one-dimensional, and apply fibre integration with boundary terms over the space of five-point configurations.',
     r'The invariant degree-four cohomology of \(\operatorname{Gr}_3(\mathbb R^5)\) is one-dimensional, generated by the first Pontryagin class of the tautological bundle (equivalently the negative of the quotient bundle class). On the suitable oriented family of compactified positive orbits, fibre integration of its closed invariant representative satisfies the Stokes formula with oriented facet terms. The vanishing theorem and the two facet families turn those terms into the differential five-term identity.',
     r'The tautological rank-three and complementary rank-two bundles have opposite first Pontryagin classes because their sum is trivial. “Exactly one form” means a one-dimensional vector space. Boundary orientations and the family compactification must be fixed; the abbreviated diagram does not supply them.',
     r'This is a recurrence of the characteristic-form construction in 1979-486.14--15 and 1979-487.2, published in \citet{gelfandmacpherson1982geometry}. The exact vanishing input is independently read in \citet[Theorem 4 and its Grassmannian application]{atiyah1982convexity}. Full verification of every 1982 normalization was unavailable.',
     [GM,AT],'Characteristic classes and special functions',cls='A',match='partial',verification='indirect',confidence='medium',status=r'As of November 2026, the geometric mechanism is established; this occurrence does not fix a unique sign and normalization for the primitive.')
item(508,'P000953','theorem','Positive orbits in compact Kähler manifolds and their polytope closures',
     r'The generalization says that algebraic torus actions with a fixed point have positive-real orbits homeomorphic to polyhedra, with only stratumwise differentiability.',
     r'Let a compact torus \(T\) act by Kähler automorphisms on a compact connected Kähler manifold \(M\), with a fixed point. Let \(T^{\mathbb C}=T\cdot H\), where \(\operatorname{Lie}H=J\operatorname{Lie}T\), and choose a moment map. For each \(y\), the moment map restricts to a homeomorphism \(\overline{H\cdot y}\to P_y\), a convex polytope; \(H\cdot y\) maps to its relative interior, and lower orbits to face interiors.',
     r'Compactness, a Kähler-preserving action, and an orbit closure are supplied. A positive orbit itself is generally noncompact and cannot be homeomorphic to a compact polytope.',
     r'This is the exact general theorem of \citet[Theorems 2 and 2′]{atiyah1982convexity}, published in 1982 after receipt on 27 March 1981. The notebook\'s 9 February report is earlier evidence of oral circulation; receipt is not treated as a public preprint date.',
     [AT],'Symplectic and Kähler geometry',cls='B',correct='false as written',status=r'As of November 2026, the orbit-closure theorem is established with the compact Kähler and Hamiltonian hypotheses.')
item(508,'P000953','theorem','Kähler harmonic-form vanishing on the positive torus part',
     r'A torus-invariant harmonic form, with respect to a Kähler metric, is said to vanish on every positive-real orbit.',
     r'For compact connected Kähler \(M\), a torus \(T\) preserving its Kähler structure and having a fixed point, every harmonic form of degree \(\ell>0\) restricts to zero on the orbits of the positive subgroup \(H\subset T^{\mathbb C}\). A torus orbit is null-homotopic through the fixed point; its invariant exact pullback vanishes, and Hodge-type decomposition transfers this conclusion from \(T\)-directions to \(J T\)-directions.',
     r'The degree-zero exception and the compact connected hypotheses are explicit. A \(T\)-invariant Kähler metric ensures the form-invariance used in the proof.',
     r'The statement and proof are read in \citet[Theorem 4, pp.13--14]{atiyah1982convexity}. The paper appeared in 1982; its recorded receipt was 27 March 1981, after this seminar report.',
     [AT],'Kähler geometry',cls='B',status=r'As of November 2026, the positive-degree theorem is established; nonzero harmonic constants are the immediate exception to the literal wording.')
item(508,'P000953','theorem','Convexity for commuting Hamiltonians and the orbit-image conflation',
     r'Theorem (15), attributed to Atiyah, assumes Poisson commutation and a common critical point, then depicts an orbit of the Hamiltonian fields mapping to a convex polyhedron.',
     r'Let \(M\) be compact connected symplectic and \(f_1,\ldots,f_r\) commuting Hamiltonians whose flows generate a compact torus action (Atiyah allows almost-periodic fields). The map \(f:M\to\mathbb R^r\) has connected nonempty fibres and convex-polytope image, the convex hull of its common critical values. Its restriction to an orbit of the Hamiltonian fields is constant, since \(H_{f_i}(f_j)=\{f_i,f_j\}=0\). Nontrivial orbit polytopes instead concern the positive complexified action in the Kähler version.',
     r'The missing compactness and almost-periodicity hypotheses and the correct domain of the moment-image assertion are supplied. Mere commutation plus a common critical point is insufficient: on a symplectic two-torus, \((\cos x,\cos^2x)\) has these properties and a nonconvex parabolic image.',
     r'The full theorem is read in \citet[Theorem 1 and following remarks, pp.2--3]{atiyah1982convexity}; the orbit theorem is its distinct Theorem 2′. Publication was 1982, receipt 27 March 1981. The counterexample and constant-orbit observation are direct checks here.',
     [AT],'Symplectic geometry',cls='B',correct='false as written',status=r'As of November 2026, moment-map convexity is established. The notebook conflates the whole-manifold moment image, positive complexified orbits, and Hamiltonian orbits; the latter have point images.')
item(508,'P000953','question','The unspecified relation with integration by quadratures',
     r'The final line asks for the relation with integration by quadratures.',
     r'No precise implication, class of differential equations, or meaning of global quadratures is specified. The nearby theorem concerns global moment-map geometry; a regular Liouville integrable system would additionally require an appropriate number of independent commuting first integrals. These are related frameworks but are not interchangeable assertions.',
     r'No new conjecture equating convexity and integrability is inferred. The final sentence is retained as a research-direction question, not assigned a fabricated definite problem.',
     r'\citet[Theorem 1 and introduction]{atiyah1982convexity} provides the exact geometric result being discussed, but does not identify this unspecified requested relation as a separate theorem. Searches found no exact formulation attributable to this sentence.',
     [AT],'Hamiltonian dynamics',cls='F',correct='not determinable',match='thematic only',verification='unresolved lead',confidence='low',status=r'As of November 2026, no independently assessable open question can be recovered from the one-line formulation.')

corr('P000949','Grassmannian inclusion table, second row third entry',r'\(G_1^3\)',r'\(G_2^3\)',r'The scan and both transcriptions agree on G_1^3. The second row parametrizes two-planes, so this is a faithful index error.')
corr('P000950','Theorem5 global regularity',r'diffeomorphic',r'homeomorphic, with a diffeomorphism on each orbit/face interior',r'P000953 explicitly qualifies the global statement and mentions possible infinite curvature at vertices; Atiyah1982 Theorem2-prime.')
corr('P000951','volume formula for 0<c1<c2<1',r'\(\Phi(c_1)-\Phi(c_2)\)',r'For unsigned positive volume use the opposite difference, or specify an oriented integral and its normalization.',r'The scan confirms this order. Phi-prime is strictly positive on (0,1), so the recorded difference is negative.')
corr('P000952','incomplete hypersimplex boundary formula',r'second sum starts at -1 and stops after the hypersimplex label',r'Reconstruct the second family as x_i=1, i=1,...,n+m; do not silently supply orientation signs.',r'Actual formula is incomplete. The inequalities give the two facet families; no full signed formula survives.','ambiguity')
corr('P000952','harmonic-form vanishing theorem13',r'every harmonic form on G_n^m',r'positive-degree harmonic forms on the unoriented real Grassmannian, with nm even and the invariant metric',r'Atiyah1982 pp13-14 explicitly states the parity hypothesis and failures for odd nm and oriented Grassmannians. Constants also refute the all-degrees reading.')
corr('P000952','one harmonic four-form; tautological two- or three-bundle',r'exactly one form; either bundle without a sign distinction',r'a one-dimensional space; p1 of the complementary bundles differs by a sign',r'Forms can be rescaled; Whitney product for the trivial rank-five sum gives p1(E)+p1(Q)=0.')
corr('P000953','torus-orbit polytope assertion',r'every positive-real orbit is homeomorphic to a polyhedron',r'every positive-real orbit closure is homeomorphic to its moment polytope; the orbit maps to the relative interior',r'The missing closure is substantive; Atiyah1982 Theorem2-prime concerns the closure.')
corr('P000953','Atiyah theorem15 hypotheses and orbit diagram',r'commuting Hamiltonians plus a common critical point; Hamiltonian orbit maps to a polyhedron',r'compact connected symplectic M with almost-periodic Hamiltonian flows; f(M) is convex. Positive complexified orbits belong to the Kähler theorem.',r'Actual scan labels H_fi. Commuting Hamiltonians are constant along their Hamiltonian orbits; (cos x,cos²x) on a symplectic torus gives a nonconvex image under the written hypotheses.')
save()

# Khovanskii, 16 February. The continuation after 23 February has its own record.
KH='khovanskii1978genus'; KT='khovanskii1977toroidal'; DA='danilov1978toric'; KC='khovanskii2025chern'
item(509,'P000955','theorem','Genus of a hyperelliptic curve',
     r'The motivating example is \(y^2=P_n(x)\), with \(P_n\) squarefree, and genus \(\lfloor(n-1)/2\rfloor\); degrees three and four give one handle and degrees five and six give two.',
     r'Over \(\mathbb C\), let \(P\) be a squarefree polynomial of degree \(n\geq1\). The smooth projective model of \(y^2=P(x)\) has genus \(\lfloor(n-1)/2\rfloor\). Indeed, its degree-two map to \(\mathbb P^1\) has \(n\) finite simple branch points and one further branch point at infinity exactly when \(n\) is odd; Riemann--Hurwitz gives the formula.',
     r'The genus belongs to the smooth compact model. The branch count supplies an elementary proof and includes the point at infinity.',
     r'This is a classical hyperelliptic genus calculation. It also follows from the Newton-polygon genus theorem read in \citet[\S2]{khovanskii1978genus}; that publication predates this explanatory talk.',
     [KH],'Algebraic curves',correct='correct')
item(509,'P000955','theorem','Degree genus formula and why the hyperelliptic plane model is special',
     r'The notes give \((n-1)(n-2)/2\) for a general degree-\(n\) equation, then say that the hyperelliptic equation is “not an equation of degree \(n\)”. ',
     r'A nonsingular plane projective curve of degree \(d\) has genus \((d-1)(d-2)/2\). For \(n\geq2\), \(y^2-P_n(x)\) does have total degree \(n\); its projective closure is a special degree-\(n\) model, generally singular at infinity, so the nonsingular plane-curve formula cannot simply be applied to that model.',
     r'The intended distinction is generic versus special support, not total degree. Passing to normalization explains the discrepancy in genera.',
     r'This is the classical plane genus formula. Its realization as the count of interior lattice points of the degree-\(d\) triangle is covered by \citet[\S2]{khovanskii1978genus} and the speaker\'s later explicit comparison in \citet[slides 6--8]{khovanskii2025chern}.',
     [KH,KC],'Algebraic curves',correct='false as written')
item(509,'P000955-P000956','definition','Newton polygons and Laurent-monomial translation',
     r'The Newton polygon is the convex hull of exponent pairs with nonzero coefficients. Multiplication by \(x^ay^b\) translates it; the curve is considered away from the coordinate cross.',
     r'For a nonzero Laurent polynomial \(P=\sum_{m\in A}c_mx^m\) on \(T=(\mathbb C^*)^n\), define \(\Delta(P)=\operatorname{conv}\{m:c_m\ne0\}\subset\mathbb R^n\). Since a Laurent monomial is a unit on \(T\), multiplying by it leaves the torus zero scheme unchanged and translates \(\Delta(P)\) by the exponent vector.',
     r'The torus restriction is essential: multiplication by a polynomial monomial can add coordinate-axis components in affine space.',
     r'The definition and its character-lattice interpretation are read in \citet[\S\S1--2]{khovanskii1977toroidal}, published in 1977. These are already established tools in the 1981 lecture.',
     [KT],'Toric geometry',correct='correct')
item(509,'P000955','theorem','The Newton-polygon genus theorem',
     r'The answer to the first motivating question is the number of interior lattice points of the Newton polygon, for coefficients in general position; the notebook attributes the earlier result to Baker and its rediscovery to Khovanskii.',
     r'Let \(P\in\mathbb C[x^{\pm1},y^{\pm1}]\) have a two-dimensional Newton polygon \(\Delta\), and assume its torus curve is irreducible and Newton nondegenerate: for every face \(F\), including \(\Delta\), the equations \(P_F=x\partial_xP_F=y\partial_yP_F=0\) have no common solution in \((\mathbb C^*)^2\). The genus of its smooth projective model is \(\#(\operatorname{int}\Delta\cap\mathbb Z^2)\). Generic coefficients with prescribed full Newton polygon satisfy these hypotheses.',
     r'Face nondegeneracy and the smooth projective model make “general position” precise. The historical teacher--student anecdote is not needed for the theorem and was not independently verified.',
     r'The exact hypersurface genus result is read in \citet[\S2]{khovanskii1978genus}; its companion paper \citet[\S2]{khovanskii1977toroidal} defines nondegeneracy and the good toric compactification. Thus the talk is exposition of published 1977--1978 work, not a new unresolved genus question.',
     [KH,KT],'Algebraic curves and Newton polytopes',problem='GP-1980-24')
item(509,'P000955-P000956','construction','Boundary valuations and unimodular monomial changes',
     r'At an omitted point, the orders of \(x,y\) give an integral vector. A monomial substitution with determinant one changes this vector by the corresponding integral matrix; primitive vectors can be made coordinate vectors.',
     r'On the smooth compactification of an irreducible torus curve, each boundary point \(p\) has \(v_p=(\operatorname{ord}_p x,\operatorname{ord}_p y)\in\mathbb Z^2\setminus\{0\}\). Under \(x=u^{a_{11}}v^{a_{12}},\ y=u^{a_{21}}v^{a_{22}}\), the order column is multiplied by \(A\). For \(A\in\operatorname{GL}_2(\mathbb Z)\), the map is an isomorphism of tori. Any primitive lattice vector is carried to a coordinate vector by such a matrix. In the nondegenerate compactification the boundary order vectors are primitive inward edge normals.',
     r'The determinant may be either \(1\) or \(-1\); the written determinant-one subcase is sufficient. Primitivity of boundary vectors uses transverse intersection with the toric boundary and cannot be assumed for arbitrary singular curves.',
     r'The lattice duality and admissible smooth toric charts are read in \citet[\S1]{khovanskii1977toroidal}; its \S2 gives the transverse compactification for nondegenerate systems.',
     [KT],'Toric geometry and valuations')
item(509,'P000956-P000957','theorem','Edge lengths count punctures',
     r'After translating an edge to a coordinate axis, its polynomial has as many nonzero roots as the length of the edge, with distinct roots in general position. A later sentence instead says “number of lattice points on the segment”; the total puncture count is the number of boundary lattice points.',
     r'Under the nondegeneracy hypotheses of 1980-509.4, the compactified curve meets the toric divisor associated to an edge \(E\) in exactly its lattice length \(\ell(E)=\#(E\cap\mathbb Z^2)-1\) distinct transverse points. Consequently the number of punctures of the curve in \((\mathbb C^*)^2\) is \(\sum_E\ell(E)=\#(\partial\Delta\cap\mathbb Z^2)\). Vertex initial polynomials are monomials and contribute no roots.',
     r'The local edge count and the global boundary-point count differ by one per closed edge because vertices are counted twice in the latter edgewise listing. Simple roots supply the transverse local parameter.',
     r'This is the elementary boundary calculation in the nondegenerate toric compactification of \citet[\S\S1--2]{khovanskii1977toroidal}; the speaker states the exact curve count again in \citet[slide 6]{khovanskii2025chern}.',
     [KT,KC],'Algebraic curves and lattice geometry',correct='false as written')
item(509,'P000957','method','Divisor degree and the signed boundary root count',
     r'The notes restrict \(Q\) to \(P=0\), say its divisor is zero, substitute \(x\sim t^n,y\sim t^m\), and sum minimum scalar products over punctures to count the torus roots.',
     r'Let \(C\) be the smooth projective model of \(P=0\) and let \(Q|_C\) be a nonzero meromorphic function. Then \(\deg\operatorname{div}(Q|_C)=0\), not generally \(\operatorname{div}(Q|_C)=0\). If the initial terms of \(Q\) do not cancel at a boundary point \(p\), its order is \(\min_{a\in\Delta(Q)}\langle a,v_p\rangle\). As \(Q\) has no poles in the torus, the number of its torus zeros, with multiplicity, is \[-\sum_{p\in C\setminus T}\operatorname{ord}_p(Q)=-\sum_{p\in C\setminus T}\min_{a\in\Delta(Q)}\langle a,v_p\rangle.\]',
     r'The missing minus sign and the difference between a divisor and its degree are explicit corrections. Local expansions have nonvanishing unit factors and the right-hand side of equation (11) requires the full sum; the minimum formula needs noncancellation of its leading coefficient.',
     r'The valuation and intersection mechanism is already present in \citet[\S\S1--2]{khovanskii1977toroidal} and the root-count application in \citet[\S1]{khovanskii1978genus}. The sign is checked directly from the degree-zero identity.',
     [KT,KH],'Algebraic curves and intersection theory',correct='false as written')
item(509,'P000957-P000958','definition','Mixed area and the two incompatible normalizations',
     r'The planar coefficient \(S(K,L)\) is defined by \(\operatorname{Area}(aK+bL)=a^2\operatorname{Area}(K)+b^2\operatorname{Area}(L)+abS(K,L)\). The following general definition instead sets \(V(K,\ldots,K)=\operatorname{Vol}(K)\).',
     r'The standard mixed volume is the symmetric Minkowski-multilinear functional with \(V(K,\ldots,K)=\operatorname{Vol}_n(K)\); equivalently, the coefficient of \(t_1\cdots t_n\) in \(\operatorname{Vol}(\sum t_iK_i)\) is \(n!V(K_1,\ldots,K_n)\). Thus \(S(K,L)=2V(K,L)=\operatorname{Area}(K+L)-\operatorname{Area}(K)-\operatorname{Area}(L)\), and \(S(K,K)=2\operatorname{Area}(K)\).',
     r'Symmetry and multilinearity in every slot are included in the characterization. The notebook shifts from the coefficient normalization \(S\) to the diagonal-volume normalization \(V\), so they cannot be substituted into root counts without the factorial.',
     r'The exact polarization normalization is read in \citet[\S1, mixed-volume definition]{khovanskii1978genus} and \citet[slide 12]{khovanskii2025chern}. This is classical mixed-volume theory; the later lecture is an explicit normalization check.',
     [KH,KC],'Convex geometry',correct='correct with missing hypotheses')
item(509,'P000957-P000958','theorem','Bernshtein’s torus root count, with multiplicities and nondegeneracy',
     r'The second motivating question is answered by mixed area, and theorem (14), attributed to D. Bernshtein, states the generic system root count as the mixed volume of its Newton polytopes.',
     r'For finite supports \(A_i\subset\mathbb Z^n\), put \(\Delta_i=\operatorname{conv}(A_i)\). A generic system of Laurent polynomials \(f_i\) with these Newton polytopes has \(n!V(\Delta_1,\ldots,\Delta_n)\) isolated roots in \((\mathbb C^*)^n\), counted with multiplicity. A sufficient precise hypothesis for equality is that for every nonzero weight \(w\in\mathbb R^n\), the simultaneous initial system \(f_{1,w}=\cdots=f_{n,w}=0\) has no torus root and that the original system is zero-dimensional. In two variables the count is \(S(\Delta(P),\Delta(Q))\).',
     r'The torus, multiplicities, finite intersection, and nonzero-weight conditions are explicit. With the normalization immediately preceding theorem (14), its right-hand side lacks \(n!\), or lacks \(2\) in the stated planar case.',
     r'\citet{bernshtein1975roots} was published in 1975 (received 7 April 1975; receipt is not a public-circulation date). The exact normalized theorem is read in \citet[\S1, number-of-solutions consequence]{khovanskii1978genus}. It is therefore known before this talk. Earlier 1974 Newton-polyhedron occurrences concern local singularity invariants and are not automatically the same problem.',
     ['bernshtein1975roots',KH],'Sparse polynomial systems',correct='false as written',problem='GP-1980-25')
item(509,'P000957','theorem','Equal polygons and the Bézout specialization',
     r'When both polygons coincide, a support-distance sum equals twice their area; for the degree triangle this gives \(n^2\), identified with Bézout.',
     r'Two generic torus polynomials with the same Newton polygon \(\Delta\) have \(2\operatorname{Area}(\Delta)\) common roots. For generic polynomials of total degrees \(d,e\), the polygons are \(d\Sigma,e\Sigma\), where \(\Sigma=\operatorname{conv}(0,e_1,e_2)\); hence the mixed-area root count is \(de\). Genericity ensures that the projective Bézout intersections do not escape to coordinate divisors.',
     r'The displayed \(n^2\) is the equal-degree subcase. The support-distance formula is invariant under translation because the length-weighted outward normals sum to zero.',
     r'This is the classical Bézout count recovered from the already published Bernshtein theorem; see \citet[\S1]{khovanskii1978genus}.',
     [KH,'bernshtein1975roots'],'Algebraic geometry and convex geometry',correct='correct')
item(509,'P000958','theorem','Euler characteristic of a nondegenerate torus hypersurface',
     r'The word “curve” is crossed out in favor of “hypersurface”, while equation (15) retains the constant negative sign \(-n!\operatorname{Vol}(\Delta)\).',
     r'Let \(f\) have full-dimensional Newton polytope \(\Delta\subset\mathbb R^n\), and assume every face truncation, including the full polynomial, defines a smooth hypersurface in \((\mathbb C^*)^n\) when nonempty. Then \[\chi\{f=0\text{ in }(\mathbb C^*)^n\}=(-1)^{n-1}n!\operatorname{Vol}_n(\Delta).\] For complex algebraic varieties the ordinary and compactly supported Euler characteristics agree, although their cohomology groups do not generally agree.',
     r'The parity-dependent sign and the nondegeneracy assumption are supplied. The negative sign is correct for plane torus curves, but already fails for one-variable polynomials, whose zero set has positive cardinality.',
     r'The exact result is read in \citet[\S3, Theorem 2 and hypersurface example]{khovanskii1978genus}. It was published three years before the seminar occurrence.',
     [KH],'Newton polytopes and topology',correct='false as written')
item(509,'P000958','theorem','Pick’s formula from genus, punctures, and Euler characteristic',
     r'Combining \(\chi=2-2B-\Gamma=-2S\), with \(B\) interior and \(\Gamma\) boundary lattice points, gives \(B+\Gamma/2=S+1\).',
     r'For a two-dimensional convex lattice polygon \(\Delta\), write \(I=\#(\operatorname{int}\Delta\cap\mathbb Z^2)\) and \(B=\#(\partial\Delta\cap\mathbb Z^2)\). Then \(\operatorname{Area}(\Delta)=I+B/2-1\). Choosing a generic nondegenerate torus curve gives genus \(I\), exactly \(B\) punctures, and Euler characteristic \(-2\operatorname{Area}(\Delta)\), which proves the identity.',
     r'Notation distinguishes the notebook\'s area \(S\) from its mixed-area coefficient. A generic curve exists for any such polygon; the formula is for the polygon itself.',
     r'Pick\'s identity is classical. The same algebraic derivation is explicitly presented by the speaker in \citet[slides 6--7]{khovanskii2025chern}, and its ingredients were already published in \citet{khovanskii1978genus}.',
     [KH,KC],'Lattice geometry',correct='correct')
item(509,'P000958','theorem','Mixed area with a disk and the isoperimetric inequality',
     r'The mixed area of a polygon and the unit disk is its perimeter. The following inequality is written in the diagonal-volume normalization, \(V(K,L)^2\geq\operatorname{Area}(K)\operatorname{Area}(L)\), and equality for a disk is mentioned.',
     r'For compact convex planar bodies \(K,L\) with nonempty interior, \(V(K,L)^2\geq\operatorname{Area}(K)\operatorname{Area}(L)\). If \(B\) is the unit disk, \(2V(K,B)=\operatorname{Perimeter}(K)\), because \(\operatorname{Area}(K+tB)=\operatorname{Area}(K)+t\operatorname{Perimeter}(K)+\pi t^2\). Hence \(\operatorname{Perimeter}(K)^2\geq4\pi\operatorname{Area}(K)\), with equality for disks.',
     r'The notebook\'s perimeter statement uses its coefficient normalization \(S=2V\). This accounts for the factor of four in the isoperimetric inequality; convexity and full planar dimension are explicit.',
     r'These are established Minkowski and isoperimetric inequalities, not questions left open in 1981. The precise normalization and disk consequence are read in \citet[slide 12]{khovanskii2025chern}; the general Alexandrov--Fenchel statement is read in \citet[Theorem 2.1]{kavehkhovanskii2012equations}.',
     [KC,'kavehkhovanskii2012equations'],'Convex geometry',correct='correct with missing hypotheses')
item(509,'P000958-P000959','theorem','The surface intersection inequality requires positivity',
     r'For any two curves on any algebraic surface the notes claim \((\Gamma_1\cdot\Gamma_2)^2\geq\Gamma_1^2\Gamma_2^2\), citing the Hodge structure and relating it to mixed area.',
     r'On a smooth projective complex surface, nef real divisor classes \(D,E\) satisfy \((D\cdot E)^2\geq D^2E^2\), by the Hodge index theorem and approximation by ample classes. The assertion for arbitrary curves is false: the two disjoint exceptional curves on the blow-up of \(\mathbb P^2\) at two distinct points have squares \(-1\) and mutual intersection zero. For globally generated toric divisors associated to polygons, \(D_K\cdot D_L=2V(K,L)\), which gives the mixed-area inequality.',
     r'Smoothness, projectivity, and positivity are substantive hypotheses. The exceptional-curve example is a direct diagnostic counterexample, not a historical attribution. The last toric identity requires a common smooth projective refinement of the polygons\' normal fans.',
     r'The surface Hodge inequality is classical. The exact positive-form version and its proof are read in \citet[Corollary 7.11]{kavehkhovanskii2010mixed}; the same paper explains the toric intersection/mixed-volume correspondence in \S2. The later work broadens the intersection theory but does not make the unrestricted notebook assertion true.',
     ['kavehkhovanskii2010mixed',DA],'Intersection theory and convex geometry',correct='false as written')
item(509,'P000959','construction','Toric compactification from compatible monomial charts',
     r'The end of the talk begins a compactification by monomial changes of coordinates and cones, explaining how a curve or divisor becomes visible at the boundary.',
     r'A finite fan \(\Sigma\) of strongly convex rational polyhedral cones in the cocharacter lattice defines a normal toric variety by gluing \(U_\sigma=\operatorname{Spec}\mathbb C[\sigma^\vee\cap M]\) along their face charts. When every cone is generated by part of a lattice basis, the variety is smooth. A complete fan gives a compact complex toric variety. Refining the normal fan of the Newton polytopes supplies a compactification in which nondegenerate complete intersections meet torus strata transversely.',
     r'Compatibility means that every cone intersection is a common face and all faces are included; mere disjointness of maximal-cone interiors does not suffice. The later 23 February occurrence supplies the fuller chart and completeness discussion.',
     r'The exact construction and admissibility/completeness theorems are read in \citet[\S1]{khovanskii1977toroidal}, and the systematic fan construction in \citet[\S5]{danilov1978toric}. Both sources were explicitly available before this lecture.',
     [KT,DA],'Toric geometry')

corr('P000954','reference to Toroidal Embeddings I, Lecture Notes339','1972','1973','Danilov1978 bibliography[26] explicitly lists Lecture Notes in Mathematics339(1973); this corrects the seminar bibliographic year.')
corr('P000955','comparison after plane genus formula','y²=P_n(x) is not an equation of degree n','For n≥2 it has total degree n, but is a special plane model, generally singular at infinity.','Actual scan confirms the literal wording; its total-degree assertion is false. The intended Newton-support distinction remains valid.')
corr('P000956','final edge count','number of integer points on this segment','lattice length = number of lattice points minus one','The same scan earlier states length correctly. A binomial edge of primitive length1 already has one root and two endpoints.')
corr('P000957','divisor of Q restricted to the compact curve','its divisor is zero','its divisor has degree zero','The scan uses the word divisor without degree; principal divisors need not vanish as divisors.')
corr('P000957','equation11 local expansion','sum c_ab x^a y^b = c_ab t^(an+bm)','Use a full sum on the right and nonvanishing unit factors from x=t^n u(t), y=t^m v(t).','Both transcriptions preserve the missing summation and schematic expansion; exact order uses noncancellation.','faithful_error')
corr('P000957','equation13 boundary sum equals root count','sum of minimum boundary orders','negative sum of boundary orders','Principal-divisor degree zero and absence of torus poles give N=-sum ord_boundary(Q); the scan confirms no minus sign.')
corr('P000958','mixed-volume definition followed by theorem14','V(Delta,...,Delta)=Vol(Delta), then number of roots=V','number of roots=n! V; in the planar formulation2V=S','The scan moves between coefficient normalization S and diagonal normalization V. Khovanskii1978 section1 gives the factorial explicitly.')
corr('P000958','theorem15 after curve is changed to hypersurface','Euler characteristic = -n! Vol(Delta)','Euler characteristic = (-1)^(n-1) n! Vol(Delta), under Newton nondegeneracy','Actual scan preserves the minus sign after generalizing the word; Khovanskii1978 section3 Theorem2 supplies the dimension-dependent sign.')
corr('P000958','surface intersection inequality19','any two curves on any algebraic surface','nef divisor classes on a smooth projective surface suffice; arbitrary curves need not satisfy the inequality','Two disjoint (-1)-exceptional curves give 0≥1 in the literal assertion. Hodge index supplies the positive-cone statement.')
save()

item(512,'P000961-P000962','construction','Unimodular torus charts and character--cocharacter duality',
     r'The continuation writes \(x_i=\prod_j u_j^{a_{ij}}\), one-parameter groups \(x_i=t^{\lambda_i}\), and the value \(t^{\langle m,\lambda\rangle}\) of a monomial on such a group.',
     r'For \(T=(\mathbb C^*)^n\), the character lattice \(M=\operatorname{Hom}(T,\mathbb C^*)\) and cocharacter lattice \(N=\operatorname{Hom}(\mathbb C^*,T)\) are dual. In chosen bases, \(\chi^m(t^\lambda)=t^{\langle m,\lambda\rangle}\). The monomial change \(x_i=\prod_j u_j^{a_{ij}}\) is an isomorphism of tori precisely when \(A\in\operatorname{GL}_n(\mathbb Z)\). An \(\mathbb A^n\) chart in a smooth toric compactification corresponds to a maximal cone generated by its cocharacter-basis columns.',
     r'Unimodularity distinguishes a chart isomorphism from a finite monomial covering. The statement concerns a chosen torus with its action, not arbitrary analytic compactifications.',
     r'The exact pairing, monomial coordinate change, and associated cones are read in \citet[\S1]{khovanskii1977toroidal}, published in 1977, and \citet[\S5]{danilov1978toric}.',
     [KT,DA],'Toric geometry',correct='correct with missing hypotheses')
item(512,'P000962','theorem','The fan compatibility condition',
     r'Cones are generated by the columns of the chart matrix. Overlapping interiors force equality; a second statement applies the same requirement to faces.',
     r'A finite collection of strongly convex rational cones defines a separated toric gluing when it is closed under faces and the intersection of every two cones is a face of each. Equivalently, relative interiors of all its cones are disjoint unless the cones coincide. Smoothness requires every cone to be generated by part of a lattice basis.',
     r'The second, facewise sentence is essential: disjoint interiors of maximal cones alone are insufficient. Including all faces makes the notebook\'s criterion the standard fan condition.',
     r'This is the admissibility theorem in \citet[\S1]{khovanskii1977toroidal}; compare the systematic fan gluing in \citet[\S5]{danilov1978toric}. It is established before the lecture.',
     [KT,DA],'Toric geometry',correct='correct with missing hypotheses')
item(512,'P000962','construction','The sigma-process example is one blow-up chart',
     r'The substitution \(x_1=u_1u_2^{-1},\ x_2=u_2\), or \(u_1=x_1x_2,\ u_2=x_2\), is called a sigma-process.',
     r'The map \((x_1,x_2)\mapsto(u_1,u_2)=(x_1x_2,x_2)\) is one affine chart of the blow-up of the origin in the \(u\)-plane; the other standard chart is needed for the complete blow-up. Torically, the modification subdivides the positive-quadrant cone by the ray \(e_1+e_2\). On the dense torus the displayed inverse is the stated unimodular monomial transformation.',
     r'The direction of the morphism and the need for the second chart are explicit; the inverse formula is not regular along \(u_2=0\) in the original plane.',
     r'The standard toric modification construction is read in \citet[\S5 and the discussion of subdivisions]{danilov1978toric}; its unimodular chart interpretation is also in \citet[\S1]{khovanskii1977toroidal}.',
     [DA,KT],'Birational and toric geometry',correct='correct with missing hypotheses')
item(512,'P000962','theorem','Completeness, the projective-plane fan, and toric classification',
     r'The compactness criterion is that the cones cover the whole vector space. A three-ray drawing gives the projective plane, and the compactification is said to be determined up to an integral automorphism.',
     r'The complex toric variety \(X_\Sigma\) is complete (equivalently compact analytically) exactly when \(|\Sigma|=N_\mathbb R\). The fan with rays \((1,0),(0,1),(-1,-1)\) and the three intervening two-dimensional cones gives \(\mathbb P^2\). Smooth complete toric varieties with their dense torus action are classified by smooth complete fans; allowing an automorphism of the torus identifies fans under \(\operatorname{GL}(N)\). Completeness alone does not assert projectivity.',
     r'The classification is equivariant and concerns valid fans. The projective-plane ray generators are reconstructed from the standard three-chart model shown schematically.',
     r'The completeness equivalence is read in \citet[\S1, compactness theorem]{khovanskii1977toroidal}; \citet[\S5]{danilov1978toric} supplies the fan classification. Both precede 1981.',
     [KT,DA],'Toric geometry',correct='correct with missing hypotheses')
corr('P000961-P000962','speaker and date provenance','catalogue continuation included within record509 or omitted because dated1991','record512, A.G.Khovanskii, 23February1981, P961 lower through P962 upper','The actual Khovanskii heading is onP961 below the integrable-system discussion and above Kazarnovskii onP962; the meeting date onP960 is23/II/81.','provenance')
corr('P000962','sigma-process chart','the displayed rational inverse is the sigma-process','Specify the blow-up morphism direction and include the second chart for the full blow-up.','The two displayed equations describe one standard affine blow-up chart; the inverse rational map fails at u2=0.','ambiguity')
save()

KZ='kazarnovskii1981zeros'; KZ24='kazarnovskii2024distribution'
kzdate=r'The paper appeared in 1981 and records receipt on 6 November 1980; receipt is not treated as evidence of public circulation. The seminar report on 23 February 1981 is the verified oral occurrence.'
item(513,'P000962','definition','Exponential sums and complex Newton polytopes',
     r'The proposed extension replaces Laurent polynomials by finite sums \(f(z)=\sum_{\lambda\in\Lambda}c_\lambda e^{\langle z,\lambda\rangle}\), with \(\Lambda\subset\mathbb C^n\), and calls \(\operatorname{conv}(\Lambda)\) the Newton polyhedron.',
     r'For a finite spectrum \(\Lambda\subset(\mathbb C^n)^*\), with nonzero coefficients on its support, the expression defines an entire exponential sum. Its complex Newton polytope is the real convex hull \(\Gamma\subset\mathbb R^{2n}\) of that spectrum. The pairing in the exponential is complex bilinear; the associated real support function is \(h_\Gamma(z)=\max_{\lambda\in\Gamma}\operatorname{Re}\langle z,\lambda\rangle\). Integer real spectra recover Laurent polynomials after \(x_j=e^{z_j}\).',
     r'The real convex hull and the complex-bilinear pairing are distinguished. The logarithmic substitution is a covering map, so it changes finite torus counts into densities of infinitely many lifted roots.',
     r'The definition is read at the opening of \citet[p.347]{kazarnovskii1981zeros}. '+kzdate,
     [KZ],'Complex analysis and Newton polytopes',cls='A',correct='correct',status=r'As of November 2026, the complex-spectrum formulation is established; it is the precise setting of the announced extension.')
item(513,'P000962','theorem','Asymptotic zero count for regular exponential systems',
     r'For \(F=(f_1,\ldots,f_n)\), the notebook states \(N_F(R)=cV(\Gamma_1,\ldots,\Gamma_n)R^n+O(R^{n-1})\), without recording the regularity condition or exact constant.',
     r'Put \(\Gamma=\sum_i\Gamma_i\). For each face \(\Delta\) of \(\Gamma\), write \(\Delta=\sum_i\Delta_i\) and form the face sums \(f_i^\Delta\). Assume there is \(\varepsilon>0\) such that for every face whose complex affine span has dimension less than \(n\), and every \(z\in\mathbb C^n\), \[\sum_i\frac{|f_i^\Delta(z)|}{\max_{\lambda\in\Lambda_i\cap\Delta_i}|e^{\langle z,\lambda\rangle}|}\geq\varepsilon.\] This is Kazarnovskii\'s regularity condition. Counting isolated common roots with multiplicity in the radius-\(R\) Euclidean ball, \[N_F(R)=\frac{\kappa_n n!}{(2\pi)^n}P_n(\Gamma_1,\ldots,\Gamma_n)R^n+O(R^{n-1}),\] where \(\kappa_n\) is the volume of the real unit \(n\)-ball and \(P_n\) agrees with ordinary mixed volume for bodies in \(\mathbb R^n\).',
     r'The condition and normalization are imported from the publication. A system with common positive-dimensional zero components cannot be counted by the literal bare formula. For \(e^z-1\), \(P_1([0,1])=1\) gives \(N(R)=R/\pi+O(1)\), checking the constant. The actual notebook scan clearly has uppercase \(O\); the retrieved 1981 OCR renders that glyph ambiguously.',
     r'This matches \citet[Definition 3 and Theorem 1, pp.348--349]{kazarnovskii1981zeros}, specialized to \(r=n\). '+kzdate,
     [KZ],'Zeros of exponential systems',cls='A',problem='GP-1980-26',status=r'As of November 2026, the stated regular-system asymptotic is established. No claim is made for an arbitrary fixed system with the same spectra.')
item(513,'P000963','definition','The face formula for pseudovolume',
     r'The diagonal functional is a sum over real \(n\)-faces of volume times external angle times the area distortion of \(E^\perp\to iE\).',
     r'For a convex polytope \(\Gamma\subset\mathbb C^n\), \[P_n(\Gamma)=\sum_{\dim_{\mathbb R} F=n}\operatorname{Vol}_n(F)\,\Omega(F)\,g(E_F),\qquad g(E)=\left|\det\bigl(\operatorname{pr}_{iE}|_{E^\perp}\bigr)\right|.\] Here \(E_F\) is the direction space of the face, and \(\Omega(F)\) is the solid angle of its exterior normal cone, normalized as a fraction of the unit ball in \(E_F^\perp\). In particular \(g(\mathbb R^n)=1\), while \(g(E)=0\) when \(E\) contains a complex line. The formula is unitarily invariant; for \(n>1\) it is not generally monotone under inclusion.',
     r'All face dimensions are real; the determinant is an absolute Euclidean Jacobian between equal-dimensional real spaces. For a lower-dimensional body its whole body can be a face and its normal cone can be a full orthogonal space.',
     r'The exact face construction, complex-angle factor, and nonmonotonicity warning are read in \citet[\S1, Definition 1]{kazarnovskii1981zeros}. The notebook\'s projection is the transpose version of the same equal-dimensional projection determinant. '+kzdate,
     [KZ],'Hermitian convex geometry',cls='A',correct='correct with missing hypotheses',status=r'As of November 2026, the face formula and its Hermitian dependence are established; ordinary real volume is only a special case.')
item(513,'P000962-P000963','theorem','Polarization and the real-spectrum specialization',
     r'The multilinear \(V(\Gamma_1,\ldots,\Gamma_n)\) is described through the single-polytope functional; it is ordinary mixed volume when all spectra are real. In one variable a perimeter appears.',
     r'There is a symmetric Minkowski-multilinear polarization \(P_n(\Gamma_1,\ldots,\Gamma_n)\) whose diagonal is the preceding face functional. For bodies in the same real form \(\mathbb R^n\subset\mathbb C^n\), it is ordinary mixed volume in the normalization \(V(K,\ldots,K)=\operatorname{Vol}_n(K)\). For \(n=1\), \(P_1\) is half the planar perimeter, with a line segment assigned perimeter twice its length. Thus the one-variable leading zero count is \(\operatorname{Perimeter}(\Gamma)R/(2\pi)\).',
     r'The polarization and semiperimeter normalization explain the unspecified constant in the notes. The statement is not ordinary \(2n\)-dimensional mixed volume of complex polytopes.',
     r'The exact polarization is \citet[Propositions 1--2 and opening comparison, pp.347--348]{kazarnovskii1981zeros}. '+kzdate,
     [KZ],'Convex geometry and complex analysis',cls='A',correct='correct with missing hypotheses',status=r'As of November 2026, the mixed pseudovolume and real-spectrum reduction are established.')
item(513,'P000963','construction','Smooth-boundary and Levi-form descriptions of pseudovolume',
     r'The notes extend the polytope functional to bodies with smooth boundary, introduce the complex tangent hyperplane, symmetrize the second fundamental form, and write an integral of the product of Levi eigenvalues, labelled \(S(\Delta)\).',
     r'For a bounded domain \(K\subset\mathbb C^n\) with smooth boundary, let \(\nu\) be its outward unit normal and \(\alpha(v)=\langle v,i\nu\rangle\) on \(\partial K\). The normalized extension is \[P_n(K)=\frac1{\kappa_n n!}\int_{\partial K}\alpha\wedge(d\alpha)^{n-1}.\] For convex bodies it agrees with the polytope functional by approximation. On the complex tangent space \(H=T\partial K\cap iT\partial K\), the Hermitian part of the second fundamental form is the Levi form; the integral can equivalently be expressed through its determinant with the convention-dependent numerical factor.',
     r'The notebook\'s final label conflates the dimensionless face-angle factor \(S(\Delta)\) with the integrated body functional. Its division by two in defining the Hermitian part changes the Levi eigenvalue normalization, so no unverified factor is attached to its eigenvalue-product formula. The contact-form expression fixes a consistent normalization independently.',
     r'All three constructions are read in \citet[\S1(a)--(c), p.348]{kazarnovskii1981zeros}; the paper explicitly allows nonconvex smooth domains for the first two boundary expressions. '+kzdate,
     [KZ],'Complex differential geometry and convex geometry',cls='A',correct='false as written',confidence='medium',status=r'As of November 2026, the normalized boundary construction is established; the notebook\'s notation and unsupplied eigenvalue factor require qualification.')
item(513,'P000963-P000964','question','Support functions and the growth-indicatrix question of 2 March',
     r'P000963 ends by mentioning a support-function formulation. On 2 March 1981, I. M. Gelfand asks on P000964 to relate Kazarnovskii\'s result to the growth indicatrix.',
     r'With \(d^c=i(\bar\partial-\partial)\) and \(h_j=h_{\Gamma_j}\), the precise bridge is \[P_n(\Gamma_1,\ldots,\Gamma_n)=\frac1{\kappa_n n!}\int_{B_1}dd^ch_1\wedge\cdots\wedge dd^ch_n.\] These positive currents are well defined for the continuous convex support functions, by smooth approximation. For a finite exponential sum, \(\log|f(tz)|/t\leq h_\Gamma(z)+O(1/t)\); if one spectral exponent uniquely maximizes the real pairing at a direction, the limit equals the support function at that direction. Exceptional directions require the usual upper regularization of the indicator. Poincaré--Lelong converts logarithmic growth to zero currents. Passing to a product of zero currents or to a fixed-system remainder still requires appropriate regularity; individual pointwise bounds alone do not justify that passage.',
     r'The statement answers the requested structural relation without turning it into an unrestricted convergence conjecture. The date and intervening speaker are explicit. The support-function integral already occurs in the 1981 publication, so the connection is not credited solely to much later work.',
     r'\citet[\S1(c), p.348]{kazarnovskii1981zeros} gives the exact support-function expression. \citet[Definition 5 and Theorems 1--2]{kazarnovskii2024distribution} later treats averaged zero currents for finite-dimensional spaces whose normalized evaluation norms converge locally uniformly to the support function; that is a precise extension with averaging, published 11 July 2024 after submissions in 2023 and 2024. Its displayed HTML normalizations are not imported here. The factor above uses the 1981 real-volume normalization and is checked on an interval.',
     [KZ,KZ24],'Complex analysis and growth indicators',cls='A',match='exact',speaker='I. M. Gelfand (follow-up, 1981-03-02)',problem='GP-1980-27',status=r'As of November 2026, the finite-spectrum support-function connection is established, and later averaged generalizations have precise regularity assumptions. The notebook sentence supplies no broader independently stated open conjecture.')
corr('P000962','exponential-system zero-count theorem','N_F(R)=c V R^n+O(R^(n-1)), without conditions','Add Kazarnovskii regularity, multiplicities, and c=kappa_n n!/(2pi)^n in the real-volume normalization.','Kazarnovskii1981 Definition3 and Theorem1; e^z-1 gives the independent calibration R/pi+O(1).')
corr('P000963','last Levi-eigenvalue integral labelled S(Delta)','S(Delta)=integral product kappa_i dS','This is a body pseudovolume formula up to an explicit convention-dependent factor, not the dimensionless face projection factor S(Delta).','The scan uses S(Delta) both for projection distortion and for a dimensional boundary integral; the published formulas distinguish these quantities.')
corr('P000964','question relating Kazarnovskii to growth indicatrix','placed adjacent to the next meeting without attribution to its actual date','I.M.Gelfand, 2March1981; a follow-up to record513 rather than part of the23February speech','The EN/RU page begins2March and labels Gelfand. This is kept under513 only as an explicitly dated cross-record follow-up.','provenance')
save()

problem('GP-1980-20','Continuity and differentiability of Thomae functions',
        r'For \(T_\alpha(p/q)=q^{-\alpha}\) in lowest terms and \(T_\alpha(x)=0\) for irrational \(x\), determine continuity and differentiability, including \(\alpha=1\).',
        ['1980-501.1','1980-501.2'],
        r'As of November 2026, this is a solved classical exercise. For \(\alpha>0\), continuity holds exactly at irrational points; for \(\alpha\leq0\) there are no continuity points. For \(0<\alpha\leq2\) there are no differentiability points. For \(\alpha>2\), at an irrational point with convergent denominators \(q_k\), differentiability is equivalent to \(q_{k+1}/q_k^{\alpha-1}\to0\), and the derivative is zero. The criterion is supplied by the elementary convergent estimate in the companion; \citet{varona2009differentiability} documents the classical general-power problem and its earlier literature.',
        ['varona2009differentiability'])
problem('GP-1980-21','A single continuous-function limit for the Dirichlet function',
        r'Can the indicator of the rational numbers on \(\mathbb R\), already expressed by an iterated pointwise limit in the notes, be the pointwise limit of one sequence of continuous real-valued functions?',
        ['1980-501.4'],
        r'As of November 2026, the answer is no: Baire-one real functions on \(\mathbb R\) have a dense set of continuity points, whereas this indicator is nowhere continuous. This is an application of the classical Baire criterion, read in \citet[p.173]{baire1900nouvelle}.',
        ['baire1900nouvelle'])
problem('GP-1980-22','Large-frequency asymptotics of Gaussian, quartic, and sextic Fourier integrals',
        r'Determine the asymptotics as \(\lambda\to+\infty\) of \(\int_{\mathbb R}e^{-x^p}\cos(\lambda x)\,dx\) for \(p=2,4,6\).',
        ['1980-501.5'],
        r'As of November 2026, this is a solved steepest-descent exercise. The Gaussian is \(\sqrt\pi e^{-\lambda^2/4}\); the higher powers have exponentially damped oscillatory leading terms from a conjugate pair of dominant saddles, explicitly reconstructed in the occurrence. The method and branch convention are checked against \citet[\S2.4(iv)]{nist2026dlmf}. No new asymptotic theorem is claimed.',
        ['nist2026dlmf'])
problem('GP-1980-23','Isomorphic cohomology without a direct chain map',
        r'Find complexes with isomorphic cohomology for which a prescribed cohomology isomorphism cannot be induced by a chain map in the stated direction.',
        ['1980-502.1'],
        r'As of November 2026, this is a solved exercise: \(A=(\mathbb Z/2)[0]\) and \(B=[\mathbb Z\xrightarrow{2}\mathbb Z]\) in degrees \(-1,0\) have the same cohomology, but every map \(A\to B\) is zero. Their derived-category isomorphism is represented by the reverse quasi-isomorphism, inverted by localization. Earlier occurrence 1971-266.3 concerns the general derived-category universal property, not the exact counterexample question, so its problem identifier is not reused.',
        ['weibel1994homological'])
problem('GP-1980-24','Genus from a Newton polygon',
        r'Determine the genus of the smooth projective model of a generic irreducible plane Laurent curve with prescribed two-dimensional Newton polygon.',
        ['1980-509.4'],
        r'As of November 2026, the problem is solved under Newton nondegeneracy: the genus is the number of interior lattice points. Khovanskii\'s 1978 publication predates this exposition; the question is a motivating problem, not an open 1981 conjecture.',
        [KH,KT])
problem('GP-1980-25','Root counts from prescribed Newton polytopes',
        r'For a generic square system of Laurent polynomials with prescribed Newton polytopes, determine the number of roots in the algebraic torus, with multiplicity.',
        ['1980-509.9'],
        r'As of November 2026, Bernshtein\'s 1975 theorem gives \(n!\) times ordinary mixed volume, with equality under the appropriate initial-system nondegeneracy. The notebook presents a problem already solved before this lecture. Earlier local Newton-polyhedron questions are related but not exact recurrences.',
        ['bernshtein1975roots',KH])
problem('GP-1980-26','Newton-type asymptotic root count for complex exponential sums',
        r'Extend the Laurent-polynomial root count to the density of roots of a regular square system of finite exponential sums with complex spectra.',
        ['1980-513.2'],
        r'As of November 2026, this formulation is solved by Kazarnovskii\'s 1981 regular-system theorem, with leading coefficient \(\kappa_n n!P_n/(2\pi)^n\) and remainder \(O(R^{n-1})\). The theorem requires its face-system regularity; arbitrary fixed systems are outside the assertion.',
        [KZ])
problem('GP-1980-27','Relating exponential zero density to the growth indicatrix',
        r'Explain how the exponential-sum zero-density theorem is expressed through the support functions of the spectral convex bodies, as asked by I. M. Gelfand on 2 March 1981.',
        ['1980-513.6'],
        r'As of November 2026, the finite-spectrum connection is established through the mixed Monge--Ampère integral already in Kazarnovskii1981 \S1(c). Kazarnovskii2024 extends this framework to averaged zero currents of regular finite-dimensional spaces of entire functions of exponential growth. The later result is not a universal fixed-system convergence theorem, and the notebook does not specify such a conjecture.',
        [KZ,KZ24])

# Keep grouping by each talk, ordered by the first new manuscript material.
source_order={501:0,500:1,502:2,504:3,505:4,503:5,507:6,508:7,509:8,512:9,513:10}
talks.sort(key=lambda x:source_order[x['record']])
items.sort(key=lambda x:(source_order[x['record']],int(x['id'].split('.')[-1])))
save()
