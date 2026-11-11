"""Authored critical-companion fragment, records 363--374.

This script checkpoints the JSON and correction files after each record.
All mathematical prose below is authored, not scraped or generated from titles.
"""
import csv, json, re
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'fragments'
talks=[]; items=[]; problems=[]; corrections=[]

def talk(record,date,speaker,pages,title,summary,kind='talk'):
    talks.append(dict(record=record,date=date,speaker=speaker,pages=pages,title=title,kind=kind,summary=summary))

def item(record,pages,kind,title,notes,statement,reconstruction,fate,
         cls='E',status='Established in the stated scope.',literal='correct with missing hypotheses',
         match='exact',verification='read the result',development='none',problem='',worth='',
         confidence='high',area='',speaker=None):
    n=1+sum(x['record']==record for x in items)
    d=dict(id=f'1975-{record}.{n}',record=record,pages=pages,kind=kind,title=title,
           notes=notes,statement=statement,reconstruction=reconstruction,**{'class':cls},fate=fate,
           present_status='As of 10 November 2026: '+status,literal_correctness=literal,
           publication_match=match,verification=verification,development=development,
           problem=problem,worth=worth,confidence=confidence,area=area)
    if speaker: d['speaker']=speaker
    cited=[]
    for s in (notes,statement,reconstruction,fate,d['present_status'],worth):
        for m in re.finditer(r'\\cite(?:t|p)?(?:\[[^\]]*\])?\{([^}]+)\}',s):
            for k in m.group(1).split(','):
                if k.strip() not in cited: cited.append(k.strip())
    d['refs']=cited
    items.append(d)
    return d['id']

def corr(page,place,reads,should,evidence,applies='both',type='faithful_error'):
    corrections.append(dict(page=page,place=place,transcription_reads=reads,should_read=should,
                            evidence=evidence,applies_to=applies,type=type))

def checkpoint():
    talks.sort(key=lambda x:x['record'])
    items.sort(key=lambda x:(x['record'],int(x['id'].split('.')[-1])))
    for filename,data in [('a_talks.json',talks),('a_items.json',items),('a_problems.json',problems)]:
        (OUT/filename).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    with (OUT/'a_corrections.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=['page','place','transcription_reads','should_read','evidence','applies_to','type'])
        w.writeheader();w.writerows(corrections)

# Record 363: the last question is retained as a suggestion, not upgraded to a problem.
talk(363,'1975-09-15','A. A. Kirillov','P000603-P000605','Deforming the Poisson bracket',
     r"""The introductory announcement of Polyakov's physics lectures is followed by Kirillov's report of Vey's deformation theorem. The page distinguishes local finite-order brackets from formal bidifferential deformations, and ends with the suggestive relation \(pq-qp=t\). The displayed planar formula suppresses necessary mixed derivatives; its omission is mathematical shorthand or error in the notebook, not an error introduced by translation.""")
item(363,'P000603','claim','Local Lie brackets and the locality hypothesis',
     r"""On a symplectic manifold \((M,\omega)\), there are ``essentially no other Lie algebra structures'' besides the Poisson bracket, with Kirillov and others named.""",
     r"""A meaningful precise version concerns local Lie brackets on sections of a real or complex line bundle over a smooth manifold. Such brackets are differential operators of order at most one in each entry and are described locally by Jacobi brackets, including Poisson and contact brackets. This does not classify arbitrary Lie algebra structures on the vector space \(C^\infty(M)\).""",
     r"""Locality, the line-bundle framework, and the qualification by Jacobi brackets are supplied to delimit the claim; the notes do not state a classification theorem with these hypotheses.""",
     r"""\citet[abstract]{kirillov1976local} is a close subsequent publication by the speaker (received 25 November 1975; published 1976). Only its publisher abstract and metadata were verified here, so an exact match to the notebook's shorthand is not asserted.""",
     cls='A',literal='not determinable',match='partial',verification='publisher metadata checked',confidence='medium',area='Poisson geometry')
item(363,'P000603','theorem','Formal deformation and the reported third-cohomology condition',
     r"""The theorem attributed to J. Vey asserts an inequivalent formal deformation \([u,v]_t=\sum_{k\geq0}t^k B_k(u,v)\), where \(B_0\) is Poisson and \(B_k\) has order \(2k+1\) in each argument. Global definition is said to follow from \(H^3(M,\mathbb R)=0\).""",
     r"""For a smooth symplectic manifold, seek skew bidifferential operators \(B_k\) such that the displayed series satisfies Jacobi coefficient by coefficient, with equivalence specified by invertible formal differential changes of functions. The cohomological condition in the notes is a sufficient condition reported for Vey's construction; it is not a necessary condition for existence of deformation quantization.""",
     r"""The coefficientwise interpretation and equivalence by formal differential operators make explicit what ``formal'' and ``inequivalent'' must mean. The notes's narrower phrase ``change of coordinates'' alone does not specify the customary equivalence relation.""",
     r"""\citet[pp.~421--454]{vey1975deformation} is the named 1975 publication; its exact obstruction argument was not obtained here. The report treats it as an existing theorem, but the publication month was not verified. The later Fedosov construction gives star products on arbitrary smooth symplectic manifolds; its mechanism is checked in \citet[Sections~1--2]{emmrichweinstein1993differential}.""",
     status='Formal symplectic deformation quantization is established without the displayed vanishing assumption; the exact Vey formulation in this shorthand remains only partially verified.',
     match='partial',verification='indirect',confidence='medium',area='Poisson geometry')
item(363,'P000603','construction','The planar Moyal bracket requires mixed derivatives',
     r"""The coefficient \(B_k\) is drawn as the difference of the two pure \((2k+1)\)-st derivative products, divided by \((2k+1)!\), followed by dots called lower terms; on the plane or torus the lower terms are said to vanish.""",
     r"""For a constant Poisson tensor \(P=\partial_p\otimes\partial_q-\partial_q\otimes\partial_p\), one consistent formal normalization is \[ [f,g]_t=\sum_{k\geq0}\frac{t^k}{(2k+1)!}\,\mu P^{2k+1}(f\otimes g). \] Here \(\mu\) multiplies the tensor factors. Already \(P^3\) contains the mixed terms \(-3f_{ppq}g_{qqp}+3f_{pqq}g_{qpp}\); these have the same differential order as the two displayed pure terms. The formula descends to a flat symplectic torus using periodic functions.""",
     r"""This is an explicit flat-model reconstruction. Writing \(t=h^2\), it is \((f\star_h g-g\star_h f)/(2h)\) for \(\star_h=\mu\exp(hP)\). Curvature corrections can vanish in a flat model; the binomial mixed derivatives cannot.""",
     r"""The flat Weyl/Moyal model is described in \citet[Section~2]{emmrichweinstein1993differential}. No assertion that the notebook's two pure terms alone define a Lie bracket is retained.""",
     literal='false as written',match='partial',development='annotated',area='Poisson geometry')
item(363,'P000603','remark','The final canonical-commutator suggestion',
     r"""The page ends with a question mark followed by \(pq-qp=t\).""",
     r"""This can be read as the formal Weyl-algebra relation for two generators over \(\mathbb C[[t]]\). It suggests an associative quantization whose commutator recovers a Poisson bracket after division by the parameter. The line does not specify whether existence, representations, global gluing, or comparison with the preceding deformation is being asked.""",
     r"""The Weyl-algebra interpretation is a possible identification, not a recovered definite research question. The use of the same letter \(t\) as in the previous expansion need not preserve the normalization.""",
     r"""The relation is compatible with the local Weyl construction in \citet[Section~2]{emmrichweinstein1993differential}, but that compatibility does not identify a unique problem or its fate.""",
     cls='F',status='No definite question can be recovered from this line.',literal='not determinable',match='thematic only',verification='unresolved lead',confidence='low',area='Poisson geometry')
corr('P000603','coefficient of the deformed bracket','Two pure derivative products; no lower terms on the plane or torus',
     'Retain the scan reading; a Moyal reconstruction must include all binomial mixed derivatives of the same order.',
     'Scan inspected. Expansion of the cube of the constant Poisson bidifferential operator supplies the missing mixed terms; the abbreviation for lower terms remains uncertain.')
checkpoint()

talk(365,'1975-09-22','I. M. Gelfand','P000609-P000611','Essentially normal operators and extension classes',
     r"""Gelfand reports the Brown--Douglas--Fillmore classification and its connection with odd \(K\)-homology, under a heading mentioning Atiyah. Essential normality and the equivalence relation defining \(\operatorname{Ext}\) are omitted in the shorthand. The intervening line ``Moser---Korteweg--de Vries'' contains no mathematical assertion and receives no separate item.""")
item(365,'P000610','question','Classification modulo compact operators',
     r"""For the Calkin algebra \(\mathfrak B=B(H)/K(H)\), when are \(B_1,B_2\) unitarily equivalent? The answer given is equality of essential spectra and of the indices on every component of their complement.""",
     r"""Let \(T_1,T_2\) be bounded essentially normal operators on a separable infinite-dimensional complex Hilbert space. They are unitarily equivalent modulo compacts, meaning \(UT_1U^*-T_2\) is compact for a unitary \(U\) on \(H\), precisely when \(\sigma_{\rm ess}(T_1)=\sigma_{\rm ess}(T_2)=X\) and \(\operatorname{ind}(T_1-\lambda)=\operatorname{ind}(T_2-\lambda)\) for every \(\lambda\notin X\). Essential normality means \([T_i,T_i^*]\) is compact. The index is constant on each complementary component.""",
     r"""Essential normality and the meaning of lifted unitary equivalence are indispensable additions. The theorem does not classify arbitrary nonnormal elements of the Calkin algebra by these data.""",
     r"""The cited 1973 chapter, \citet[pp.~58--128]{browndouglasfillmore1973unitary}, predates the seminar; its publisher metadata was opened, not its full proof. The claim is identified as the BDF theorem with the omitted hypothesis restored, rather than as a new Atiyah theorem.""",
     match='partial',verification='publisher metadata checked',problem='GP-1975-01',area='Operator algebras')
item(365,'P000610','theorem','Extensions as odd analytic K-homology',
     r"""The notes write \(\operatorname{Ext}(X)\cong K_1(X)\) and explain \(\operatorname{Ext}(X)\) as embeddings of \(C(X)\) in the Calkin algebra.""",
     r"""For compact metrizable \(X\), the stable unitary-equivalence classes of extensions \(0\to K(H)\to E\to C(X)\to0\), with split extensions treated as zero, form the BDF group \(\operatorname{Ext}(C(X))\). In modern notation it is naturally the odd analytic \(K\)-homology group \(KK^1(C(X),\mathbb C)\). This is a group of extension classes, not the unquotiented set of embeddings and not generally the group \(K_1(C(X))\).""",
     r"""Metrizability, stabilization, equivalence, and the distinction between homology of the space and \(K\)-theory of its function algebra are supplied. The notation \(K_1(X)\) is retained only when explicitly understood homologically.""",
     r"""The 1973 precursor is \citet{browndouglasfillmore1973unitary}; the full paper is \citet[pp.~265--324]{browndouglasfillmore1977extensions}. Both publisher records were checked. The modern \(KK\)-notation is a reconstruction, not claimed to occur in the seminar.""",
     match='partial',verification='publisher metadata checked',area='Operator algebras')
problems.append(dict(id='GP-1975-01',title='Unitary classification of essentially normal operators modulo compacts',
    statement=r"""For bounded essentially normal \(T_1,T_2\) on separable infinite-dimensional \(H\), determine whether essential spectrum and complementary Fredholm-index function classify unitary equivalence modulo compact operators. The essential-normality hypothesis is reconstructed from the BDF attribution.""",
    occurrences=['1975-365.1'],status=r"""As of 10 November 2026: answered affirmatively in the BDF setting before this talk; \citet[pp.~58--128]{browndouglasfillmore1973unitary}. The notebook's unrestricted formulation is not the theorem.""",status_date='2026-11',refs=['browndouglasfillmore1973unitary']))
corr('P000610','BDF classification','Arbitrary elements of the Calkin algebra','Supply essential normality of the lifts and specify unitary equivalence modulo compacts.','Scan contains no normality qualifier; this is a missing theorem hypothesis, not a translation error.')
corr('P000610','Ext(X)','Set of embeddings C(X) into the Calkin algebra','Stable unitary-equivalence classes of extensions, modulo the specified split-extension relation; K_1(X) denotes odd K-homology.','Scan and both transcriptions agree. The equivalence relation is absent from the notebook.')
checkpoint()

talk(366,'1975-09-22','B. Kostant','P000609-P000611','Euler products, root systems, and Kostant’s character formula',
     r"""The Euler product and its familiar powers introduce the Macdonald identities and Kostant's character-theoretic form. Manin anticipates his next discussion of several expressions for \(\tau(n)\), and Gelfand asks only the suggestive question \(\psi(x)^z\). The spectral-zeta fragment is too compressed to identify a unique formula.""")
item(366,'P000610','theorem','Euler’s product, partitions, and the pentagonal expansion',
     r"""For \(\psi(q)=\prod_{n\geq1}(1-q^n)\), the reciprocal generates partitions. The exponent in the displayed pentagonal expansion is \((n^2-3n)/2\).""",
     r"""For \(|q|<1\), or as formal power series, \[ \psi(q)^{-1}=\sum_{n\geq0}p(n)q^n,\quad p(0)=1,\qquad \psi(q)=\sum_{k\in\mathbb Z}(-1)^kq^{k(3k-1)/2}. \] Each coefficient is finite in the formal interpretation.""",
     r"""The correct pentagonal exponent and the bilateral index set are supplied. The notebook exponent would even give negative powers at small positive indices.""",
     r"""These classical formulas are recorded in \citet[Section~27.14(ii), equations~27.14.3--5]{nist2026dlmf}; no 1975 novelty is suggested.""",
     literal='false as written',development='annotated',area='Modular forms')
item(366,'P000610','theorem','Jacobi’s cubic Euler-product identity',
     r"""The cube is \(\psi(q)^3=\sum_{n\geq0}(-1)^n(2n+1)q^{n(n+1)/2}\), with Jacobi named.""",
     r"""The displayed identity holds for \(|q|<1\) and coefficientwise in \(\mathbb Z[[q]]\). It is the rank-one member of the eta-product/root-system family, after the appropriate leading power of \(q\) is separated.""",
     r"""Only the convergence/formal interpretation and the distinction between \(\eta\) and \(\psi\) are supplied.""",
     r"""\citet[Section~2, pp.~636--638]{dyson1972missed} explicitly identifies Jacobi's power \(3\) in the established sequence. This revisits the eta-power discussion in 1971-269.3.""",
     literal='correct',verification='indirect',area='Modular forms')
item(366,'P000610','definition','The discriminant and the exponent 24',
     r"""The notation is \(\eta(q)=q^{1/24}\psi(q)\), with \(\eta(q)^{24}=\sum\tau(n)q^n\); a similar formula for power \(10\) is mentioned.""",
     r"""For \(z\) in the upper half-plane and \(q=e^{2\pi iz}\), \(\eta(z)=q^{1/24}\prod_{n\geq1}(1-q^n)\) and \(\Delta(z)=\eta(z)^{24}=\sum_{n\geq1}\tau(n)q^n\). Thus \(\tau(1)=1\). Powers \(10\) and \(24\) have explicit lattice-sum identities, but the notes state no particular power-\(10\) summation.""",
     r"""The variable \(z\), branch convention \(q^{1/24}=e^{2\pi iz/24}\), and lower index \(1\) are explicit here. The phrase about power \(10\) is catalogued without inventing its omitted formula.""",
     r"""\citet[equations~(1)--(3), pp.~636--637]{dyson1972missed} gives the discriminant and explains Winquist's power \(10\). Earlier occurrences are 1971-269.1--3.""",literal='correct',area='Modular forms')
item(366,'P000610','theorem','Macdonald identities in Kostant’s character form',
     r"""The power is \(\dim K\), and the sum has terms \(\chi_\lambda(a)\dim V_\lambda\) with \(\chi_\lambda(a)\in\{0,\pm1\}\); the exponent is left unspecified.""",
     r"""For a compact connected simply connected simple Lie group \(K\), let \(\rho\) be half the sum of positive roots and use the Killing-form normalization to identify weights with the Cartan subalgebra. For Kostant's principal element \(a=\exp(2\pi i\,2\rho)\), \[ \prod_{n\geq1}(1-q^n)^{\dim K}=\sum_{\lambda\in P_+}\chi_\lambda(a)\dim V_\lambda\,q^{(\lambda+\rho,\lambda+\rho)-(\rho,\rho)},\qquad \chi_\lambda(a)\in\{0,1,-1\}. \] The inner product here is the one in the cited theorem; arbitrary root-length normalization changes the exponents.""",
     r"""Simplicity, simple connectedness, the principal element, and the Casimir exponent replace the omitted hypotheses and dots. ``Dimensions of compact groups'' alone is too broad a description of the precise theorem.""",
     r"""Macdonald's underlying identities appeared in 1972 \citep{macdonald1972affine}. \citet[Theorems~0.1 and~2.1]{kostant2003euler} restates the character formula and explicitly identifies its original 1976 Theorem~3.1. This supports class A for Kostant's particular formulation, not a new priority claim for the older product identities.""",
     cls='A',match='partial',area='Representation theory')
item(366,'P000610','remark','The spectral-zeta fragment',
     r"""After the character identity, the page records ``Kostant: \(\operatorname{Sp}(-\Delta+a)^{-s}\), etc.''""",
     r"""A spectral zeta function of a positive elliptic operator can be defined for sufficiently large \(\operatorname{Re}s\), and a group element can enter an equivariant trace. However, the notes do not specify the operator domain, the meaning of \(a\), whether it is added or acts by translation, or any asserted identity.""",
     r"""An equivariant heat/zeta-trace connection is a possible interpretation only. The group element \(a\) from the preceding line cannot simply be treated as a scalar spectral shift without additional information.""",
     r"""The heat-kernel connection in \citet[Introduction]{kostant2003euler} provides thematic context, but does not verify this literal expression.""",
     cls='F',status='The intended spectral formula is not identifiable with sufficient precision.',literal='not determinable',match='thematic only',verification='unresolved lead',confidence='low',area='Spectral theory')
item(366,'P000610','question','Gelfand’s complex-exponent suggestion',
     r"""Gelfand writes \(\psi(q)^z\), followed by a question mark, with \(z\in\mathbb C\).""",
     r"""There is a canonical analytic definition on \(|q|<1\):
     \[\psi(q)^z=\exp\!\left(z\sum_{n\geq1}\log(1-q^n)\right),\]
     using the branch equal to \(1\) at \(q=0\). Its formal coefficients are polynomials in \(z\). This observation does not determine whether Gelfand wanted analytic continuation, coefficient formulas, representation-theoretic interpolation, or another property.""",
     r"""The elementary definition is supplied only to show that existence of a complex power is not itself a uniquely recoverable open problem. It is not equated with the earlier definite question about exponent \(26\), GP-1971-41.""",
     r"""\citet[Introduction]{kostant2003euler} studies coefficients of general powers, but the notebook specifies no assertion that can be matched to one of its theorems.""",
     cls='F',status='The intended question remains underdetermined; no new problem-index entry is manufactured.',literal='not determinable',match='thematic only',verification='unresolved lead',confidence='low',speaker='I. M. Gelfand',area='Modular forms')
corr('P000610','Euler exponent','(n^2-3n)/2','n(3n-1)/2, summed over all integers n','Scan confirms the erroneous exponent. The pentagonal-number identity fixes the intended expression.')
checkpoint()

talk(367,'1975-09-22','A. M. Polyakov','P000609-P000614','From lepton symmetries to electroweak gauge fields',
     r"""After reading recommendations, Polyakov extends the QED construction to chiral lepton doublets and local \(SU(2)\) symmetry. Charged currents, muon decay, neutral-field mixing, and the then four-flavour, three-colour quark count appear. The Higgs sector and hypercharge assignment are not supplied in these pages; a complete electroweak reconstruction must mark those additions.""")
item(367,'P000611','claim','The enlarged symmetry of massless lepton kinetic terms',
     r"""The kinetic terms for \(e_L,\nu_L,e_R\) have \(SU_L(2)\times U_R(1)\times U_L(1)\) symmetry; another lepton family is indicated. A preceding line still includes the electron mass term.""",
     r"""For a massless left Weyl doublet \(L=(\nu_L,e_L)^T\) and a right Weyl singlet \(e_R\), the free kinetic Lagrangian is invariant under \(U(2)_L\times U(1)_R\). At the Lie-algebra level this is \(\mathfrak{su}(2)_L\oplus\mathfrak u(1)_L\oplus\mathfrak u(1)_R\); the product-group notation suppresses a finite central quotient. A nonzero bare Dirac mass selecting the electron component breaks the independent left-doublet symmetry.""",
     r"""The massless restriction and global central quotient are supplied. The doublet order is changed explicitly to the usual convention for later charge assignments.""",
     r"""\citet[p.~1264, equations~(1)--(4)]{weinberg1967leptons} starts from these kinetic symmetries and selects the gauged combination. It was published 20 November 1967.""",match='partial',area='Quantum field theory')
item(367,'P000611','construction','Local SU(2) covariance and the three gauge fields',
     r"""The doublet transforms by \(U(x)=\exp(i\boldsymbol\tau\cdot\boldsymbol\alpha(x)/2)\), while the infinitesimal line has the opposite sign. A three-component connection is introduced, yielding three massless particles at this stage.""",
     r"""Set \(D_\mu=\partial_\mu+igW_\mu\), \(W_\mu=W_\mu^a\tau_a/2\). Requiring \(D'_\mu(UL)=UD_\mu L\) gives \(W'_\mu=UW_\mu U^{-1}+(i/g)(\partial_\mu U)U^{-1}\). The curvature is \(F_{\mu\nu}=\partial_\mu W_\nu-\partial_\nu W_\mu+ig[W_\mu,W_\nu]\). The gauge-invariant Yang--Mills kinetic term describes three massless gauge fields before symmetry breaking.""",
     r"""The coupling, complete connection transformation, and curvature are supplied. The infinitesimal sign is made consistent with the finite exponential; no mass-generation mechanism is inferred from this line.""",
     r"""The nonabelian construction is present in the electroweak Lagrangian of \citet[equation~(4)]{weinberg1967leptons}. The notebook is expository.""",literal='false as written',match='partial',area='Quantum field theory')
item(367,'P000612','construction','Charged weak currents and muon decay',
     r"""The off-diagonal fields \(A^1\pm iA^2\) change electron-type leptons into their neutrinos; a diagram represents muon decay.""",
     r"""With canonically normalized \(W^\pm=(W^1\mp iW^2)/\sqrt2\), the charged-current term is proportional to \(g\bar\nu_{eL}\gamma^\mu e_LW^+_\mu/\sqrt2\), plus its adjoint and the muon-family analogue. Exchange of \(W^-\) gives \(\mu^-\to e^-+\bar\nu_e+\nu_\mu\). At energies much below \(m_W\), the propagator reduces to the local four-fermion interaction with \(G_F/\sqrt2=g^2/(8m_W^2)\).""",
     r"""The \(\sqrt2\) normalization, conjugate neutrino, chirality, and low-energy hypothesis are supplied. The low-energy coefficient is a reconstruction, not an extra formula recovered from the sketch.""",
     r"""\citet[equations~(8), (13), and~(16)]{weinberg1967leptons} gives the charged fields and their weak-coupling normalization, predating the lecture.""",match='partial',area='Quantum field theory')
item(367,'P000612','claim','Neutral mixing requires a hypercharge assignment',
     r"""A right-handed \(U(1)\) field \(B\) and \(A_\gamma=A^3\cos\theta+B\sin\theta\) are written, without a complete left-handed \(B\)-coupling or symmetry-breaking sector.""",
     r"""In the standard completion, \(SU(2)_L\times U(1)_Y\) has \(Y_L=-1/2\), \(Y_{e_R}=-1\), \(Q=T_3+Y\), and a scalar doublet of \(Y=1/2\) with a neutral nonzero vacuum value. Then \(A_\gamma=W^3\sin\theta_W+B\cos\theta_W\), \(\tan\theta_W=g'/g\), and \(e=g\sin\theta_W=g'\cos\theta_W\). The orthogonal neutral field is massive. A \(U(1)\) acting only on \(e_R\) cannot by itself reproduce these charges.""",
     r"""Hypercharges, the scalar doublet, and its vacuum are explicitly added. The reversed sine and cosine in the notebook can be an angle convention; it is not alone an error.""",
     r"""\citet[equations~(4), (7), and~(10)--(15)]{weinberg1967leptons} verifies this completion. It is only a partial match to the incomplete notebook account.""",match='partial',area='Quantum field theory')
item(367,'P000612','remark','Four flavours and three colours in the quark count',
     r"""The last line counts twelve quarks as four flavours times three colours.""",
     r"""In the four-flavour model under discussion, the internal one-particle labels are \(\{u,d,s,c\}\times\{1,2,3\}\), giving twelve flavour--colour labels. This does not mean twelve flavours, and it does not count spin or antiquark labels.""",
     r"""The interpretation of the multiplication is made explicit; the notebook is not recast as a claim that four flavours exhaust all future observations.""",
     r"""This is bookkeeping within the lecture's historical model, with no independent theorem or definite research question to trace.""",literal='correct',match='none found',verification='indirect',area='Quantum field theory')
corr('P000611','infinitesimal SU(2) transformation','exp(+i tau alpha/2) followed by 1-i tau alpha/2','Use the same sign in the finite transformation and its first-order expansion.','Both signs are visible in the scan; this is an internal convention mismatch.')
checkpoint()

talk(368,'1975-09-29','I. M. Gelfand','P000612-P000614','The Lie algebra of differential polynomials',
     r"""Gelfand introduces the bracket on differential polynomials underlying evolutionary equations and the KdV hierarchy. Povzner identifies its action by derivations. On the same page Manin's opening definition of \(\tau\) precedes the Gelfand passage and his numbered formulas follow it; the catalogue's two Manin records are therefore kept distinct.""")
item(368,'P000613','definition','Differential polynomials and total differentiation',
     r"""The algebra consists of polynomials in \(u,u',u'',\ldots\), and differentiation is \(D=\sum u^{(k+1)}\partial/\partial u^{(k)}\).""",
     r"""Let \(\mathcal A=\mathbb R[u_0,u_1,\ldots]\), each element depending on finitely many variables, and \(D=\sum_{j\geq0}u_{j+1}\partial_{u_j}\). Evaluation at a smooth function, \(u_j=\partial_x^j u(x)\), intertwines \(D\) with \(\partial_x\). Each formal sum acts finitely on every element of \(\mathcal A\).""",
     r"""Finite dependence and the evaluation interpretation are explicit additions. The variables are algebraically independent before evaluation.""",
     r"""The framework is developed in \citet[Sections~8--10]{gelfanddikii1976fractional}, received 22 June 1976 and published in 1976. The source's differential-polynomial construction was read.""",cls='A',literal='correct',area='Integrable systems')
item(368,'P000613','construction','The evolutionary Lie bracket',
     r"""For two differential polynomials the notes write
     \[[P,Q]=\sum_{k\geq0}\left(D^kP\,\frac{\partial Q}{\partial u_k}-D^kQ\,\frac{\partial P}{\partial u_k}\right).\]""",
     r"""For \(P\in\mathcal A\), define the evolutionary derivation \(\mathcal D_P=\sum_{k\geq0}D^k(P)\partial_{u_k}\). Then \([P,Q]=\mathcal D_P(Q)-\mathcal D_Q(P)\) is a Lie bracket, and \([\mathcal D_P,\mathcal D_Q]=\mathcal D_{[P,Q]}\). The injection \(P\mapsto\mathcal D_P\) follows from \(\mathcal D_P(u_0)=P\); Jacobi follows from the derivation commutator.""",
     r"""\ours\ The short derivation argument makes the Jacobi claim precise and fixes the sign convention, without introducing a Poisson bracket on the original jet variables.""",
     r"""\citet[Section~10, equation~(24)]{gelfanddikii1976fractional} gives the same evolutionary bracket in the subsequent joint paper.""",cls='A',literal='correct',area='Integrable systems')
item(368,'P000613','remark','Povzner’s identification with compatible evolution equations',
     r"""Povzner associates \(a\) with \(u_t=a\), explains its derivation on all derivatives of \(u\), and identifies the bracket of these derivations.""",
     r"""For autonomous differential-polynomial flows \(u_t=P[u]\) and \(u_s=Q[u]\), compatibility of the formal prolonged vector fields is \([P,Q]=0\). Indeed \(\partial_tQ[u]-\partial_sP[u]=\mathcal D_PQ-\mathcal D_QP\). This is a formal jet-space statement; it alone does not establish existence, uniqueness, or commuting solution maps for a chosen PDE function space.""",
     r"""The distinction between algebraic compatibility and analytic well-posedness is supplied. The observation belongs to Povzner's intervention, not to a separately catalogued talk.""",
     r"""The derivation interpretation is incorporated in \citet[Section~10]{gelfanddikii1976fractional}.""",cls='A',literal='correct',speaker='A. Ya. Povzner',area='Integrable systems')
checkpoint()

talk(369,'1975-09-29','Yu. I. Manin','P000612-P000614','Opening definition of Ramanujan’s tau function',
     r"""This catalogue record is represented by the short Manin heading and product definition at the top of P000613. Gelfand's differential-polynomial discussion follows immediately; Manin resumes below it in record 370. The mathematical content is therefore one definition, despite the archive's broad overlapping page range.""")
item(369,'P000613','definition','Tau as the coefficients of the discriminant',
     r"""Manin opens with \(x\prod_{n\geq1}(1-x^n)^{24}=\sum_{n\geq1}\tau(n)x^n\).""",
     r"""The identity defines integers \(\tau(n)\), \(n\geq1\), as the coefficients of \(\Delta(q)=q\prod_{m\geq1}(1-q^m)^{24}\), with \(\tau(1)=1\). It is valid formally and analytically for \(|q|<1\).""",
     r"""Only the formal/analytic interpretation is supplied. This occurrence repeats 1975-366.3 and 1971-269.1, rather than introducing a second tau function.""",
     r"""\citet[equation~(1), p.~636]{dyson1972missed} gives the same definition before the seminar.""",literal='correct',area='Modular forms')
checkpoint()

talk(364,'1975-09-15','A. M. Polyakov','P000603-P000611','Spinors, gauge invariance, and perturbative quantum electrodynamics',
     r"""This extended introductory lecture moves from the particle table to Weyl and Dirac fields, local phase covariance, electromagnetic connections, propagators, Feynman parameters, and charge screening. Gelfand's Gaussian-integral analogy interrupts the discussion. The notebook combines exact finite-dimensional identities with formal functional integrals and schematic diagrams; the companion preserves that distinction.""")
item(364,'P000604','remark','The 1975 particle table and interaction-strength heuristic',
     r"""The table lists photons; electrons, muons and two massless neutrinos; protons, neutrons and pions. Approximate masses are \(0.5,105,940,140\), and gravitational, weak, electromagnetic and strong strengths are ranked by \(10^{-38},10^{-5},10^{-2},1\).""",
     r"""The masses are approximate values in \(\mathrm{MeV}/c^2\). The table is a historical teaching selection, not an exhaustive particle classification. A dimensionless interaction strength must specify the process and energy scale; \(E_{\rm int}/m\) is not a universal constant for each interaction. Statements ordering the number of violated conservation laws by strength have no general theorem behind them. Massless neutrinos are an approximation of the then minimal model.""",
     r"""Units, scale dependence, and the distinction between a model assumption and a measured mass are supplied. No numerical modernization of this historical table is attempted.""",
     r"""The later oscillation evidence in \citet[abstract]{fukuda1998oscillation} rules out treating all neutrinos as exactly massless. The strength ranking is retained as an introductory heuristic, not a theorem awaiting development.""",
     status='The particle table is historical; the neutrino masslessness and universal strength assertions are not valid literal modern statements.',
     literal='false as written',match='partial',verification='publisher metadata checked',area='Quantum field theory')
item(364,'P000604-P000605','construction','Spin one-half, Weyl spinors, and Lorentz boosts',
     r"""Rotations act by \(\exp(i\boldsymbol\sigma\cdot\boldsymbol\Theta/2)\); the two boost laws are \(e_L\mapsto e^{\boldsymbol\sigma\cdot\boldsymbol\psi/2}e_L\) and \(e_R\mapsto e^{-\boldsymbol\sigma\cdot\boldsymbol\psi/2}e_R\), with \(v=\tanh|\boldsymbol\psi|\).""",
     r"""The Pauli matrices generate the two-dimensional representation of \(SU(2)\). The two inequivalent Weyl representations of \(SL_2(\mathbb C)=\operatorname{Spin}^+(1,3)\) restrict to this rotation representation and have opposite boost generators. The signs depend on active/passive and left/right conventions; rapidity has \(|\mathbf v|=c\tanh|\boldsymbol\psi|\). They are representations of the spin cover, not single-valued spinor representations of \(SO^+(1,3)\).""",
     r"""The covering group and units are supplied; the notebook boost convention is retained.""",
     r"""\citet[Section~4.1]{tong2006qft} supplies the standard spinor construction. This is exposition of pre-existing representation theory.""",area='Quantum field theory')
item(364,'P000605','remark','Gelfand’s covering-group explanation',
     r"""Gelfand draws \(SO(3)\longrightarrow SU(2)\) and explains the spinor rotation action and its extension to Lorentz transformations.""",
     r"""The canonical surjective covering map is \(SU(2)\to SO(3)\), with kernel \(\{\pm I\}\). A rotation lifts to two elements, so an arrow in the opposite direction cannot be a globally defined inverse homomorphism. Likewise \(SL_2(\mathbb C)\to SO^+(1,3)\) is a double cover.""",
     r"""The arrow is interpreted as a covering-group explanation because of its surrounding text, not silently reversed in the diplomatic transcription.""",
     r"""The covering description is standard; see \citet[Section~4.1]{tong2006qft}.""",literal='false as written',development='annotated',speaker='I. M. Gelfand',area='Representation theory')
item(364,'P000605-P000606','construction','Parity, the Weyl equations, and the Dirac mass',
     r"""Parity interchanges \(e_L,e_R\); the massless equations imply \(E^2=\mathbf p^2\). A bilinear \(m(e_L^\dagger e_R+e_R^\dagger e_L)\) is added and rewritten as \(\bar e(i\gamma^\mu\partial_\mu-m)e\).""",
     r"""With \(\eta=\operatorname{diag}(1,-1,-1,-1)\) and \(\{\gamma^\mu,\gamma^\nu\}=2\eta^{\mu\nu}\), the Dirac equation implies \((\Box+m^2)e=0\). Plane waves have \(E=\pm\sqrt{\mathbf p^2+m^2}\); the displayed positive root is the positive-energy branch. A parity-invariant charged Dirac field combines the two Weyl modules. Up to normalization, phase choices, and the stated parity and charge symmetries, its real scalar mass couples opposite chiralities.""",
     r"""The factors of \(i\), relative signs, both energy branches, and the symmetries needed for the claimed uniqueness of the mass term are supplied. Unqualified uniqueness would ignore pseudoscalar and, for neutral fields with different symmetries, Majorana masses.""",
     r"""\citet[Sections~4.2--4.4]{tong2006qft} treats the free Dirac construction.""",match='partial',area='Quantum field theory')
item(364,'P000606-P000607','construction','Local phase covariance introduces a connection',
     r"""The global phase \(e\mapsto e^{i\beta}e\) is made position dependent; the connection transforms as \(A_\mu\mapsto A_\mu-\partial_\mu\beta\), and \(\nabla_\mu=\partial_\mu+iA_\mu\). The first displayed coupling omits a gamma contraction.""",
     r"""For \(D_\mu=\partial_\mu+iA_\mu\), \(D^{\prime}_\mu(e^{i\beta}e)=e^{i\beta}D_\mu e\). Consequently \(\bar e(i\gamma^\mu D_\mu-m)e\) is invariant under the local \(U(1)\) transformation. Its interaction is \(-\bar e\gamma^\mu A_\mu e\); a separate charge can instead be absorbed into \(A\).""",
     r"""The contraction and placement of parentheses are repaired mathematically; the malformed displayed coupling is present in the scan.""",
     r"""\citet[Section~6.3.1]{tong2006qft} gives this standard gauge-covariant construction.""",literal='false as written',development='annotated',area='Quantum field theory')
item(364,'P000607','construction','Curvature and the Maxwell kinetic term',
     r"""To give equations for the connection, the notes add \((4e^2)^{-1}F_{\mu\nu}^2\), with \(F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu\).""",
     r"""With the preceding Lorentz signature and \(D=\partial+iA\), a standard real Minkowski Lagrangian is \[ \mathcal L=\bar e(i\gamma^\mu D_\mu-m)e-\frac{1}{4e^2}F_{\mu\nu}F^{\mu\nu}. \] Variation in \(A\) gives Maxwell's equations with the Dirac current. A positive quadratic sign instead belongs to the usual Euclidean action after Wick rotation.""",
     r"""Raising the tensor indices, selecting Lorentz signature consistently, and distinguishing the Euclidean sign are necessary additions; no Wick rotation appears at this point in the notes.""",
     r"""\citet[Section~6.1]{tong2006qft} verifies the conventional Maxwell and QED action.""",literal='false as written',match='partial',area='Quantum field theory')
item(364,'P000607','method','The scattering functional integral is formal',
     r"""A transition amplitude is written \(\int_{\Phi_{\rm in}}^{\Phi_{\rm out}}D\varphi\,e^{iS[\varphi]}\); \(D\varphi\) is called a natural Lebesgue measure. Free theory is Gaussian and interaction gives perturbation theory.""",
     r"""A finite-mode or lattice regulator produces finite-dimensional oscillatory bosonic integrals and Berezin integrals for fermions, with boundary and gauge-fixing choices. Their normalized perturbative expansion defines formal Green functions and, after suitable limiting and scattering prescriptions, perturbative amplitudes. There is no nonzero locally finite translation-invariant Lebesgue measure on an infinite-dimensional topological vector space of fields.""",
     r"""The regulated/formal interpretation is supplied. It is neither a construction of an unregularized four-dimensional QED measure nor a theorem that pointwise field limits as \(t\to\pm\infty\) exist.""",
     r"""\citet[Sections~3.1--3.3, 6.1]{tong2006qft} checks the perturbative scattering framework; it does not verify the notebook's literal measure claim.""",
     status='The perturbative interpretation is established; the written infinite-dimensional Lebesgue integral is not a literal measure-theoretic definition.',literal='false as written',match='partial',area='Quantum field theory')
item(364,'P000607','method','Gelfand’s Gaussian-moment analogy and divergent cubic integral',
     r"""Gelfand compares the theory with \(\int e^{i(x^2+\varepsilon x^3)}dx\) and \(\int e^{-\sum a_{ij}x_ix_j+\varepsilon\sum x_i^3}dx\). The last expansion instead displays \(e^{ix^2(1+\varepsilon x^3)}\).""",
     r"""For a positive definite real quadratic form \(Q\), every coefficient \(\int P(x)^k e^{-Q(x)}dx/k!\) exists for a polynomial \(P\); these coefficients define a formal perturbation series. If \(P=x^3\) and real \(\varepsilon\ne0\), the displayed real-line integral diverges on one tail. Oscillatory analogues require a contour or distributional prescription. The final written phase is quintic, not cubic.""",
     r"""The rigorous content retained is the coefficientwise Gaussian-moment calculation, not convergence of the formal series or the cubic exponential integral.""",
     r"""The Wick-contraction method is standard; \citet[Section~3.3]{tong2006qft} gives the corresponding perturbative mechanism. The convergence objection follows directly from the odd leading term in the notebook's real exponent.""",literal='false as written',match='partial',development='annotated',speaker='I. M. Gelfand',area='Quantum field theory')
item(364,'P000607','claim','A logarithmically divergent model loop integral',
     r"""The sample integral is \(\int_{\mathbb R^4}d^4x/((|x|^2+m_1)(|x|^2+m_2))\), without a regulator.""",
     r"""For \(m_1,m_2>0\), the integrand is locally integrable, but its radial integral at infinity behaves like \(\int^\infty r^{-1}dr\); hence the unregularized integral diverges logarithmically. A cutoff makes it a legitimate starting point for parameterization and subtraction.""",
     r"""Positivity and the ultraviolet cutoff are supplied. The radial comparison is an elementary check of this specific notebook example, not a claim about all loop integrals.""",
     r"""The general perturbative setting is reviewed in \citet[Section~3.2]{tong2006qft}; the explicit divergence is determined directly from the written integrand.""",literal='correct with missing hypotheses',match='thematic only',development='annotated',area='Quantum field theory')
item(364,'P000607-P000608','method','Feynman parameters and the missing beta normalization',
     r"""The identity \(1/(ab)=\int_0^1(sa+(1-s)b)^{-2}ds\) is extended to arbitrary exponents and to a simplex without gamma factors.""",
     r"""For \(a_i>0\), \(\operatorname{Re}\lambda_i>0\), and \(\Lambda=\sum_i\lambda_i\), \[ \prod_i a_i^{-\lambda_i}=\frac{\Gamma(\Lambda)}{\prod_i\Gamma(\lambda_i)}\int_{s_i\geq0}\frac{\delta(1-\sum_i s_i)\prod_i s_i^{\lambda_i-1}\,ds_i}{(\sum_i s_i a_i)^\Lambda}. \] The two-denominator formula is its special case. Continuation to Lorentzian denominators additionally requires consistent branches and the pole prescription.""",
     r"""The gamma ratio and domain are restored. At \(a=b=1\), \(\lambda=\mu=2\), the notebook's right-hand side is \(1/6\), while the left-hand side is \(1\); the missing factor is \(6\).""",
     r"""\citet[Section~5.12, equations~5.12.1 and~5.12.4]{nist2026beta} verifies the beta-integral normalization. The simplex identity follows by introducing positive Schwinger parameters and separating their sum.""",literal='false as written',development='annotated',area='Special functions')
item(364,'P000608','construction','Dirac Green function and the Feynman pole prescription',
     r"""Although the prose says ``according to Maxwell'', the equation is \((i\gamma^\mu\partial_\mu-m)K=\delta\), and the Fourier inverse is \((\gamma^\mu p_\mu+m)/(p^2-m^2+i0)\).""",
     r"""For the convention \(K_F(x)=\int d^4p\,(2\pi)^{-4}e^{-ipx}(\gamma^\mu p_\mu+m)/(p^2-m^2+i0)\), \((i\gamma^\mu\partial_\mu-m)K_F=\delta\) distributionally. The usual time-ordered two-point function is \(iK_F\) in this convention. The two displaced poles encode positive-frequency propagation forward and negative-frequency propagation backward in time.""",
     r"""The Fourier sign, normalization, matrix identity on the delta function, and distinction between Green function and two-point function are supplied. ``Maxwell'' here must not be used to identify the displayed electron kernel as a photon propagator.""",
     r"""\citet[Section~5.5]{tong2006qft} gives the free Dirac propagator.""",literal='correct with missing hypotheses',match='partial',area='Quantum field theory')
item(364,'P000608','method','Single-photon exchange and the diagram expansion',
     r"""The diagram joins two electron lines by a photon. Each emission or absorption carries \(e\), but the displayed integral is a product of four electron kernels and one photon kernel without explicit vertices or \(e^2\). More diagrams contain loops and pair creation.""",
     r"""After a fixed gauge and propagator convention, the order-\(e^2\) electron-exchange kernel contains \[ e^2\!\int\! [S_F(x_3-z_1)\gamma^\mu S_F(z_1-x_1)]\otimes[S_F(x_4-z_2)\gamma^\nu S_F(z_2-x_2)]D_{\mu\nu}(z_1-z_2)\,d^4z_1d^4z_2, \] up to the conventional factors of \(i\), external-state contractions, and exchange antisymmetrization for identical fermions. Higher terms are organized by Wick contractions with loop signs and symmetry factors.""",
     r"""The displayed formula is reconstructed as a schematic kernel, not asserted to be a fully normalized scattering amplitude. Unclear connections in the hand-drawn third and fourth diagrams are not assigned a unique graph.""",
     r"""\citet[Section~6.5]{tong2006qft} supplies the QED vertex and diagram rules.""",match='partial',area='Quantum field theory')
item(364,'P000608','remark','Antiparticles do not make the Feynman inverse the only Green function',
     r"""The final lines link negative-energy levels, backward time propagation, antiparticles, and an alleged unique consistent way to bypass the poles; the terminal Russian words remain doubtful.""",
     r"""The time-ordered vacuum propagator has the Feynman \(i0\) prescription. Retarded and advanced Green functions are also well-defined distributional inverses with different boundary conditions. Antiparticles arise in the quantized complex Dirac field; uniqueness is meaningful only after the state, ordering, and boundary conditions have been specified.""",
     r"""This separates the unambiguous pole discussion from the unreadable terminal assertion. No claim that the seminar denied antiparticles is extracted from the doubtful English phrase.""",
     r"""\citet[Sections~5.2--5.5]{tong2006qft} gives the particle/antiparticle interpretation and the time-ordered propagator.""",literal='not determinable',match='partial',confidence='medium',area='Quantum field theory')
item(364,'P000609','claim','Charge screening and the opposite nonabelian sign',
     r"""The leading exchange is of order \(e^2\), the polarization correction of order \(e^4\); the notes write \(e_{\rm phys}^2<e^2\) and the reverse inequality for the strong interaction.""",
     r"""For a cutoff description of QED, vacuum polarization screens electric charge at long distances. In a mass-independent perturbative convention with one unit-charge Dirac fermion, \(\beta(e)=e^3/(12\pi^2)+O(e^5)\). For \(SU(N_c)\) with \(N_f\) fundamental Dirac flavours, \(\beta(g)=-g^3(11N_c-2N_f)/(48\pi^2)+O(g^5)\), so the coupling decreases toward high energy when \(N_f<11N_c/2\).""",
     r"""The comparison is reconstructed as the sign of scale dependence, rather than a scheme-independent inequality between undefined bare and physical numbers. The negative beta function by itself does not prove confinement.""",
     r"""\citet[p.~1344, equations~(8)--(9)]{grosswilczek1973ultraviolet} gives the nonabelian and fermion contributions in June 1973, before this lecture; the comparison with the Abelian sign is made on the same page.""",match='partial',verification='indirect',area='Quantum field theory')
corr('P000605','covering-group arrow','SO(3) points to SU(2)','The canonical double-cover homomorphism points from SU(2) to SO(3).','The diplomatic transcription explicitly records the arrow direction; the scan confirms it. The error concerns interpretation, not copying.')
corr('P000606','local gauge coupling','The A term has no gamma contraction and mismatched parentheses',r'Use \(\bar e(i\gamma^\mu(\partial_\mu+iA_\mu)-m)e\).','The missing contraction is visible in the scan; covariance and scalar-index contraction determine the mathematical repair.')
corr('P000607','Maxwell term','Plus F squared in the Lorentz-signature Lagrangian','Use minus F_mu_nu F^mu_nu/(4e^2) for the stated Minkowski conventions; a Euclidean plus requires an explicit change of convention.','Compare the metric on P000606 and the action e^{iS} on P000607; this is a convention-sensitive emendation.')
corr('P000607','Gaussian perturbation analogy','Natural Lebesgue measure on field space; convergent-looking real cubic perturbation','Treat the functional integral and cubic perturbation series formally or after a specified regulator/contour.','Infinite-dimensional field space has no locally finite translation-invariant Lebesgue measure; a real cubic term defeats decay on one tail.')
corr('P000607','last model exponent','ix^2(1+epsilon x^3)','Retain the quintic phase as written; do not silently turn it into the preceding cubic phase.','Scan and both transcriptions agree; the discrepancy is internal to the notebook.',type='ambiguity')
corr('P000608','generalized Feynman parameters','No prefactor in either parameter integral',r'Insert \(\Gamma(\sum_i\lambda_i)/\prod_i\Gamma(\lambda_i)\).','Scan inspected; beta-integral normalization and the a=b=1, lambda=mu=2 check give 6 rather than 1.')
corr('P000608','description of K','According to Maxwell','The displayed K solves the Dirac equation; retain Maxwell as a notebook misidentification unless it was intended to anticipate D.','The operator i gamma d-m and its matrix numerator identify the Dirac kernel.')
checkpoint()

talk(370,'1975-09-29','Yu. I. Manin','P000612-P000617','Eight descriptions of Ramanujan’s tau function',
     r"""Manin resumes with a list announced as six expressions but numbered through eight: the product, Dyson's root-lattice sum, divisor convolutions, lattice theta series, a period formula, partition asymptotics, Hecke multiplicativity, and a Galois representation. The subsequent explanation invokes eta transformations, the ring of modular forms, Rademacher contours, and Kostant's identity. Several formulas are faithfully transcribed mathematical errors; their corrected forms and the exact scope of independent finite checks are separated from the notebook.""")
item(370,'P000613','remark','The unexplained nonalgorithmic qualification',
     r"""The heading calls the expressions ``not obtained by a finite algorithm'', while the list itself begins with a finite coefficient-extraction procedure.""",
     r"""For any given positive integer \(n\), \(\tau(n)\) is computable by truncating \(q\prod_{m=1}^{n-1}(1-q^m)^{24}\) modulo \(q^{n+1}\). Therefore a literal assertion that no finite algorithm computes \(\tau(n)\) is false. The phrase may instead concern deriving one description from another or the conceptual diversity of the formulas; no complexity model or quantified claim is stated.""",
     r"""The finite coefficient algorithm is an elementary consequence of the supplied definition. The possible alternative reading is explicitly conjectural and is not indexed as a research problem.""",
     r"""No exact noncomputability or complexity assertion was identified. The surrounding explicit coefficient formulas in \citet[Section~1.3]{manin1973periods} reinforce the need to retain this textual uncertainty.""",
     cls='F',status='The qualification is not a recoverable mathematical conjecture.',literal='not determinable',match='none found',verification='unresolved lead',confidence='low',area='Modular forms')
item(370,'P000613','construction','The combinatorial expansion needs multiplicities',
     r"""The first expression sums \((-1)^k\) over ordered-by-size partitions of \(n-1\), with at most 24 consecutive equality signs. No colours or binomial coefficients are shown.""",
     r"""The literal product expansion is \[ \tau(n)=\sum_{\substack{0\leq r_j\leq24\ (j\geq1)\\\sum j r_j=n-1}}(-1)^{\sum r_j}\prod_j\binom{24}{r_j}. \] Only \(j\leq n-1\) contribute. Equivalently, each selected part size comes with a subset of 24 labelled copies; it can occur at most 24 times, hence at most 23 equality signs within a run.""",
     r"""The binomial multiplicities are mandatory. At \(n=2\), an unweighted partition count gives \(-1\), while the product gives \(-24\). This counterexample is independent of the ambiguity between copies and equality signs.""",
     r"""The reconstruction follows directly by the binomial theorem from the discriminant product in \citet[equation~(1)]{dyson1972missed}. The accompanying exact-arithmetic code independently computes the coefficients through \(n=50\).""",
     literal='false as written',match='partial',development='annotated',area='Modular forms')
item(370,'P000613','theorem','Dyson’s five-variable formula',
     r"""The second expression is \(\tau(n)=(1!2!3!4!)^{-1}\sum\prod_{i<j}(u_i-u_j)\), subject to \(\sum u_i=0\), \(\sum u_i^2=10n\), and \(u_i\equiv i\pmod5\).""",
     r"""For every positive integer \(n\), sum over all labelled integer 5-tuples satisfying those three conditions. Then the displayed Vandermonde sum equals \(\tau(n)\); its finiteness follows from the sum-of-squares condition. The congruences are attached to the labels, so no extra quotient by permutations is taken.""",
     r"""The labelled summation convention and positivity of \(n\) are made explicit; no further mathematical repair is required.""",
     r"""\citet[equation~(2), pp.~636--637]{dyson1972missed} prints exactly this formula. His Gibbs lecture was delivered 17 January 1972 and the paper appeared in September 1972; this repeats 1971-269.2.""",literal='correct',area='Modular forms')
item(370,'P000613','theorem','Ramanujan’s divisor-convolution identity',
     r"""The third formula is \(\tau(n)=\frac{65}{756}\sigma_{11}(n)+\frac{691}{756}\sigma_5(n)-\frac{691}{3}\sum_{m=1}^{n-1}\sigma_5(m)\sigma_5(n-m)\).""",
     r"""For \(\sigma_k(n)=\sum_{d\mid n}d^k\) and \(n\geq1\), this identity is correct. It follows by comparing coefficients in \(E_6^2=E_{12}-(762048/691)\Delta\), using \(E_6=1-504\sum\sigma_5(n)q^n\) and \(E_{12}=1+(65520/691)\sum\sigma_{11}(n)q^n\).""",
     r"""The modular-form identity explains the otherwise opaque constants. The coefficient comparison is a reconstruction, not a second formula written in the notes.""",
     r"""The modular-form basis theorem is checked in \citet[Proposition~4.16]{milne2017modular}; the weight-12 normalization is checked independently in \citet[Section~3]{brouwerleech}. Direct Euler-product coefficients and a separate divisor recurrence agree with the notebook convolution for \(1\leq n\leq50\).""",
     literal='correct',development='annotated',area='Modular forms')
item(370,'P000613','theorem','The congruence modulo 691',
     r"""The convolution formula is followed by \(\tau(n)\equiv\sigma_{11}(n)\pmod{691}\), attributed to Ramanujan.""",
     r"""For every positive integer \(n\), \(\tau(n)-\sigma_{11}(n)\) is divisible by \(691\). Indeed multiply the preceding identity by \(756\), reduce modulo \(691\), and use \(756\equiv65\pmod{691}\) with \(65\) invertible modulo \(691\).""",
     r"""The elementary modular reduction is supplied; it does not require the later Galois-representation construction.""",
     r"""\citet[Section~1.3, p.~374]{manin1973periods} explicitly recovers this already classical congruence from his coefficient theorem. It also occurs in 1973-305.9.""",literal='correct',area='Modular forms')
item(370,'P000614','claim','The assertion that there are only two rank-24 forms',
     r"""Integral quadratic forms of determinant one in 24 variables are said to number ``2 in all''; neither evenness nor positive definiteness is written.""",
     r"""Even after imposing positive definiteness and even unimodularity on the associated lattice, there are more than two classes. For example \(E_8^{\oplus3}\), \(D_{24}^+\), and the Leech lattice are distinguished by their numbers of norm-two vectors: \(720\), \(1104\), and \(0\). Here \(D_{24}=\{x\in\mathbb Z^{24}:\sum x_i\text{ is even}\}\) and \(D_{24}^+=D_{24}\cup((1/2,\ldots,1/2)+D_{24})\); the index-two extension is even and unimodular, and its new coset has minimal squared norm \(6\).""",
     r"""This explicit three-lattice counterexample suffices; a full classification is not needed for the correction. The nearby number two may refer to the dimension of the weight-12 modular-form space, but that is an interpretation, not a legible correction of the scan.""",
     r"""\citet[Theorems~1.1--1.3 and Section~3]{brouwerleech} checks the Leech and theta-series facts and distinguishes the two rank-16 lattices from the two-dimensional weight-12 space. The \(D_{24}^+\) count above is the elementary root count \(2\cdot24\cdot23\).""",
     literal='false as written',match='partial',development='annotated',area='Quadratic forms')
item(370,'P000614','theorem','Recovering tau from a rank-24 lattice theta series',
     r"""The fourth formula expresses \(\tau(n)\) as a linear combination of the number of representations \(Q_{24}=n\) and \(\sigma_{11}(n)\), with constants obtained from small coefficients.""",
     r"""Let \(L\) be an even positive definite unimodular lattice of rank 24, set \(Q(v)=(v,v)/2\), and \(r_L(n)=\#\{v\in L:Q(v)=n\}\). Then \[ r_L(n)=\frac{65520}{691}\sigma_{11}(n)+c_L\tau(n),\qquad c_L=r_L(1)-\frac{65520}{691}. \] Thus \(\tau(n)\) is recovered by division by \(c_L\ne0\); nonvanishing follows because \(r_L(1)\) is an integer. This uses \(\Theta_L\in M_{12}(SL_2(\mathbb Z))=\mathbb C E_{12}\oplus\mathbb C\Delta\).""",
     r"""The lattice hypotheses and half-norm convention are necessary. Determinant one alone is insufficient for this weight and full modular group. The constant coefficient and the coefficient of \(q\) already determine the two constants.""",
     r"""\citet[Theorem~1.2 and Section~3]{brouwerleech} verifies the theta-series argument and the explicit Leech instance. This is established modular-form theory, not a new classification of forms.""",match='partial',area='Quadratic forms')
item(370,'P000614','theorem','Manin’s finite coefficient formula and its boundary weights',
     r"""The fifth expression sums over \(n=\Delta\Delta'+\delta\delta'\), but its polynomial is printed as \((\Delta^8\delta^2-\Delta^2\delta^8)+(691/6)(\Delta^6\delta^4-\Delta^4\delta^6)\), subtracted from \(\sigma_{11}(n)\).""",
     r"""The corrected factorized form is \[ \tau(n)=\sigma_{11}(n)-\frac{691}{18}\sum{}'\Delta^2\delta^2(\Delta^2-\delta^2)^3. \] Sum over integers \(\Delta>\delta>0\) satisfying either \(\Delta'>\delta'>0\), \(n=\Delta\Delta'+\delta\delta'\), or \(\delta'=0\), \(\Delta\mid n\), \(\Delta'=n/\Delta\), and \(0<\delta/\Delta\leq1/2\). In the latter case the boundary \(\delta/\Delta=1/2\) has weight \(1/2\). Expanding the polynomial gives coefficient \(691/18\) on the first difference and \(-691/6\) on the second.""",
     r"""Both coefficients and the boundary weight are restored. At \(n=2\), the corrected sum gives \(-24\); even granting the missing half weight, the notebook polynomial gives \(-841\). The factorized formula was independently checked for \(n\leq50\) against two exact coefficient algorithms; this finite check is not offered as a proof for all \(n\).""",
     r"""\citet[Section~1.3, pp.~373--374; proof in Section~5]{manin1973periods} is the direct earlier publication. The summation region and half-weight rule were read; the poor formula OCR was cross-checked by the factorization and exact computation. Russian publication was 1973, whereas the opened English translation carries copyright 1975; neither is inferred merely from receipt dates.""",
     literal='false as written',match='partial',verification='indirect',development='annotated',area='Modular forms')
item(370,'P000614','method','Recursive computation using partition numbers',
     r"""The sixth expression uses \(P(q)=\sum p(n)q^n=\prod(1-q^n)^{-1}\), but writes the inner sum from \(n=1\) in \(\Delta=qP^{-24}\). It proposes recovering \(\tau\) recursively from \(p\).""",
     r"""The invertible formal series is \(P(q)=\sum_{n\geq0}p(n)q^n\), with \(p(0)=1\). Thus \(\Delta(q)=qP(q)^{-24}\) and ordinary series inversion gives a finite recursion for each coefficient. An independent recurrence from logarithmic differentiation is \((n-1)\tau(n)=-24\sum_{m=1}^{n-1}\sigma_1(m)\tau(n-m)\), \(n\geq2\).""",
     r"""The lower index is repaired. The divisor recurrence is explicitly an additional elementary verification device, not asserted to be the recursion Manin wrote.""",
     r"""\citet[equations~27.14.3 and~27.14.7]{nist2026dlmf} verifies the partition normalization. The product and derivative recurrences independently agree through \(n=50\) in the supplied computation.""",
     literal='false as written',match='partial',development='annotated',area='Partitions')
item(370,'P000614','theorem','The convergent Rademacher series and its phases',
     r"""A Hardy--Ramanujan--Rademacher series is written with a phase depending on \(1/k\) rather than \(h/k\), an asserted \(\omega_{h,k}^{24}=1\), and a derivative of a normalized hyperbolic sine. The exponential-only predecessor is contrasted with it.""",
     r"""For \(n\geq1\), put \(t=n-1/24\), \(C=\pi\sqrt{2/3}\), and \[ A_k(n)=\sum_{\substack{h\bmod k\\(h,k)=1}}e^{\pi i s(h,k)-2\pi inh/k},\quad s(h,k)=\sum_{r=1}^{k-1}\frac r k\left(\frac{hr}{k}-\left\lfloor\frac{hr}{k}\right\rfloor-\frac12\right). \] Then \[ p(n)=\frac1{\pi\sqrt2}\sum_{k\geq1}\sqrt{k}\,A_k(n)\left.\frac{d}{dt}\frac{\sinh(C\sqrt t/k)}{\sqrt t}\right|_{t=n-1/24}. \] The series converges. The factor \(e^{\pi i s(h,k)}\) does not in general have order dividing 24.""",
     r"""This complete conventional normalization replaces the malformed formula. For instance \(s(1,5)=1/5\), so \((e^{\pi i/5})^{24}\ne1\). The Hardy--Ramanujan truncation is an asymptotic method, not the same convergent series with \(\sinh\) simply replaced by \(e^x\).""",
     r"""\citet[Section~27.14(iii), equations~27.14.8--11]{nist2026dlmf} gives the convergent series, phases, and historical distinction between the 1918 asymptotic and Rademacher's 1938 treatment.""",
     literal='false as written',match='partial',development='annotated',area='Partitions')
item(370,'P000614','theorem','Hecke multiplicativity of tau',
     r"""The seventh entry underlines \(\tau(mn)=\tau(m)\tau(n)\) when \((m,n)=1\), noting that this is not apparent from the earlier formulas.""",
     r"""The normalized cusp form \(\Delta\), spanning the one-dimensional space \(S_{12}(SL_2(\mathbb Z))\), is a simultaneous Hecke eigenform. With the conventional normalized Hecke operators, \(T_n\Delta=\tau(n)\Delta\), and \(T_mT_n=T_{mn}\) for coprime \(m,n\), giving the displayed multiplicativity.""",
     r"""The Hecke interpretation and normalization are supplied as the explanation. No assertion of multiplicativity for noncoprime arguments is made.""",
     r"""\citet[Proposition~5.18 and Corollary~5.20]{milne2017modular} verifies the standard argument. Earlier relevant occurrences are 1973-304.8--9.""",literal='correct',area='Modular forms')
item(370,'P000614','claim','Prime-power coefficients are complete symmetric sums',
     r"""After \(\tau(p)=\theta_p+\bar\theta_p\) and \(\theta_p\bar\theta_p=p^{11}\), the notes underline \(\tau(p^a)=\theta_p^a+\bar\theta_p^a\).""",
     r"""If \(\alpha_p,\beta_p\) are the roots of \(T^2-\tau(p)T+p^{11}\), then \[ \sum_{a\geq0}\tau(p^a)T^a=\frac1{(1-\alpha_pT)(1-\beta_pT)},\qquad \tau(p^a)=\sum_{j=0}^a\alpha_p^{a-j}\beta_p^j. \] Equivalently \(\tau(p^{a+1})=\tau(p)\tau(p^a)-p^{11}\tau(p^{a-1})\). A sum of just the two powers describes a trace of a Frobenius power, not this Hecke coefficient.""",
     r"""The distinction is decisive already at \(p=2,a=2\): the notebook expression is \(-3520\), while \(\tau(4)=-1472\). The complete sum, or its quotient \((\alpha^{a+1}-\beta^{a+1})/(\alpha-\beta)\) when distinct, repairs the formula.""",
     r"""\citet[Corollary~5.20]{milne2017modular} verifies the recurrence. The small counterexample is checked independently by direct product multiplication and the divisor recurrence.""",
     literal='false as written',match='partial',development='annotated',area='Modular forms')
item(370,'P000614','theorem','The two-dimensional l-adic representation',
     r"""The eighth entry says that \(\tau\) is the trace of a representation and names Serre, Deligne, Grothendieck, Weil, Kuga, and Sato. The target is drawn as \(\mathbb Q_\ell^2\).""",
     r"""For every prime \(\ell\), the eigenform \(\Delta\) has a continuous two-dimensional \(\ell\)-adic representation \(\rho_\ell:G_{\mathbb Q}\to GL_2(\mathbb Q_\ell)\), unramified outside \(\ell\), with \(\det(1-\rho_\ell(\operatorname{Frob}_p)T)=1-\tau(p)T+p^{11}T^2\) for \(p\ne\ell\), choosing Frobenius and dual conventions to give determinant \(p^{11}\). In particular \(\tau(p)\) is a trace at primes; the preceding item explains why \(\tau(p^a)\) is not usually the trace of the \(a\)-th power.""",
     r"""The group-valued target, continuity, ramification restriction, and convention are supplied. A vector space is the representation space, not the target group of the homomorphism.""",
     r"""\citet[Sections~3--4, especially Theorem~4.9]{deligne1971modulaires} constructs the cohomological representation. The Bourbaki talk was given in February 1969; the collected publication is 1971, so this is established before the seminar.""",
     literal='false as written',match='partial',area='Arithmetic geometry')
item(370,'P000614','theorem','Deligne’s bound does not make the roots purely imaginary',
     r"""The text calls \(\theta_p\) ``purely imaginary (nonreal)'', and attributes the result to Deligne's proof of the Weil conjectures.""",
     r"""The roots of \(T^2-\tau(p)T+p^{11}\) have complex absolute value \(p^{11/2}\), and \(|\tau(p)|\leq2p^{11/2}\). Since \(\tau(p)\) is an integer and \(2p^{11/2}\) is irrational, equality cannot occur; the roots are a nonreal conjugate pair. They need not be purely imaginary: at \(p=2\), their real part is \(\tau(2)/2=-12\).""",
     r"""The distinction between \ru{чисто мнимые} and \ru{невещественные} is mathematical, not an English mistranslation. The strictness and small-prime counterexample are elementary consequences of the established bound.""",
     r"""\citet[Theorem~5.6]{deligne1971modulaires} gives the implication Weil \(\Rightarrow\) Ramanujan; \citet[Theorem~1.6]{deligne1974weil} proves the needed weight statement. The latter was publicly published in 1974, not merely received then; it precedes this talk.""",
     literal='false as written',match='partial',development='annotated',area='Arithmetic geometry')
item(370,'P000615','theorem','Eta transformations and the invariant sixth differential',
     r"""Eta is rewritten in the upper-half-plane variable, with an extraneous \(n\) in the leading exponential. Translation and inversion laws are given, and \(\eta^{24}(z)(dz)^6\) is called invariant.""",
     r"""For \(\operatorname{Im}z>0\), \(\eta(z)=e^{2\pi iz/24}\prod_{n\geq1}(1-e^{2\pi inz})\), \(\eta(z+1)=e^{\pi i/12}\eta(z)\), and \(\eta(-1/z)=\sqrt{-iz}\,\eta(z)\), with the holomorphic square root positive at \(z=i\). Therefore \(\Delta(\gamma z)=(cz+d)^{12}\Delta(z)\) for \(\gamma\in SL_2(\mathbb Z)\), and \(\Delta(z)(dz)^6\) is invariant under pullback.""",
     r"""The leading exponent, square-root branch, and group are specified. The multiplier of eta has finite order in the transformation law; this does not justify the different \(\omega_{h,k}^{24}=1\) assertion in the partition formula.""",
     r"""\citet[equations~27.14.12--14]{nist2026dlmf} verifies the eta definition and multiplier formula. This is classical exposition.""",literal='false as written',match='partial',area='Modular forms')
item(370,'P000615','theorem','The graded ring generated by E4 and E6',
     r"""The notes assert that the ring of modular forms is \(\mathbb C[E_4,E_6]\) and identify the nonconstant coefficients with \(\sigma_3(n)\) and \(\sigma_5(n)\), without their normalization factors.""",
     r"""For holomorphic scalar modular forms on \(SL_2(\mathbb Z)\), holomorphic also at the cusp, \[ M_* = \bigoplus_{k\geq0}M_k(SL_2(\mathbb Z))=\mathbb C[E_4,E_6], \] where \(E_4=1+240\sum_{n\geq1}\sigma_3(n)q^n\), \(E_6=1-504\sum_{n\geq1}\sigma_5(n)q^n\), and \(\Delta=(E_4^3-E_6^2)/1728\). Homogeneous polynomial identities therefore yield coefficient convolutions such as 1975-370.4.""",
     r"""The group, cusp condition, grading, constant coefficients, and scaling factors are essential. The theorem is not a statement about all levels, meromorphic forms, or arbitrary multiplier systems.""",
     r"""\citet[Proposition~4.16 and p.~78]{milne2017modular} proves the structure and supplies the two normalized generators, using half the conventional weight in its subscripts. Earlier occurrences are 1973-304.6--7.""",literal='correct with missing hypotheses',match='partial',area='Modular forms')
item(370,'P000615','method','Rademacher contours and cusp singularities',
     r"""The explanation of formula six draws circles tangent at rational points and successive integration contours; it calls the boundary singularities poles of infinite order.""",
     r"""Coefficient extraction for \(P(q)=\prod(1-q^n)^{-1}\), followed by \(q=e^{2\pi iz}\), deforms a contour through arcs associated with rational cusps (Ford circles in the standard construction). Modular transformations give local expansions contributing the sums \(A_k(n)\). The analytic boundary singularities at roots of unity are not meromorphic poles of a finite order; ``pole of infinite order'' is informal terminology.""",
     r"""The identification of the circles as Ford circles and the modular coefficient-extraction mechanism are reconstructed from the labelled Rademacher diagram. No error estimate for a particular drawn truncation is inferred.""",
     r"""The resulting convergent coefficient formula is checked in \citet[equations~27.14.9--11]{nist2026dlmf}; this verifies the endpoint, while the exact hand-drawn contour parametrization remains schematic.""",match='partial',verification='indirect',area='Partitions')
item(370,'P000615','theorem','Kostant’s identity revisited with a missing power',
     r"""The final formula again sums \(\chi_\lambda(a)\dim V_\lambda q^{c(\lambda)}\), now with \(c(\lambda)=(\lambda+\rho,\lambda+\rho)-(\rho,\rho)\), but the left side is only \(\psi(q)\).""",
     r"""With the compact simple simply connected group and Killing normalization of 1975-366.4, the left side is \(\psi(q)^{\dim K}\), and the displayed Casimir exponent is correct in that normalization. The root-system character values are again \(0,\pm1\).""",
     r"""The omitted dimension power is restored by direct comparison with P000610 and with the verified theorem; the new occurrence is kept because the exponent is supplied here for the first time in these notes.""",
     r"""\citet[Theorem~0.1]{kostant2003euler} verifies the formula. It had already been reported at this seminar on 22 September; classification E describes this repeated exposition, while 1975-366.4 records the subsequent 1976 publication.""",
     literal='false as written',match='partial',area='Representation theory')
corr('P000613','first tau sum','Unweighted signed partitions with at most 24 equality signs',r'Use multiplicities \(0\leq r_j\leq24\) and weights \(\prod_j\binom{24}{r_j}\), or equivalently 24 labelled copies of each part.','Scan inspected. At n=2 the written unweighted sum is -1 whereas tau(2)=-24; a run of 24 copies has 23 equality signs.')
corr('P000614','quadratic-form count','Two forms in dimension 24','Retain the reading; the count is false even for positive definite even unimodular lattices. The two-dimensional modular-form space is a possible intended referent.','Scan explicitly reads two in all. E8 cubed, D24 plus, and Leech provide three inequivalent examples.',type='faithful_error')
corr('P000614','Manin coefficient polynomial','First coefficient 1 and second coefficient +691/6',r'Use \((691/18)(\Delta^8\delta^2-\Delta^2\delta^8)-(691/6)(\Delta^6\delta^4-\Delta^4\delta^6)\).','The notebook scan confirms the printed reading. Manin1973 Section1.3 supplies the coefficient theorem; exact evaluation through n=50 supports the corrected factorized form and rejects the notebook already at n=2.')
corr('P000614','prime on Manin summation','No explanation of boundary weight',r'At \(\delta/\Delta=1/2\), with \(\delta^{\prime}=0\), assign weight \(1/2\).','Manin1973 p374 explicitly states this rule. It is omitted in the seminar explanation; without it n=2 already fails.')
corr('P000614','partition-series inversion','Sum from n=1 before raising to -24','Sum from n=0 and set p(0)=1.','The constant term is required for formal series inversion; the lower limit 1 is visible in the scan.')
corr('P000614','Rademacher formula','Phase exp(-2 pi i n/k) and omega_hk^24=1','Use exp(-2 pi i n h/k), Dedekind-sum phase exp(pi i s(h,k)), and the normalized Rademacher formula in the item.','Scan matches transcription. DLMF27.14.9--11 supplies the complete normalization; s(1,5)=1/5 disproves the asserted phase order.')
corr('P000614','prime-power tau','tau(p^a)=theta_p^a+conjugate(theta_p)^a','Use the complete symmetric sum of degree a or the Hecke recurrence.','Scan double-underlines the erroneous formula. p=2,a=2 gives -3520 instead of -1472.')
corr('P000614','Galois representation target','Representation into Q_l^2','The space is Q_l^2 and the homomorphism target is GL_2(Q_l).','This is a target/type correction required for the trace assertion, not a claim about the precise handwritten arrow.')
corr('P000614','Deligne root assertion','Purely imaginary (nonreal)','Nonreal conjugate roots of modulus p^(11/2); generally not purely imaginary.','Russian scan says both expressions. tau(2)=-24 forces real part -12, so the parenthetical is not synonymous with the preceding words.')
corr('P000615','eta prefactor','exp(2 pi i n z/24)','exp(2 pi i z/24)','The extra n is visible outside the product in the scan. DLMF27.14.12 gives the standard prefactor.')
corr('P000615','Eisenstein coefficients','Coefficients sigma_3(n), sigma_5(n)','For normalized E4 and E6 use 240 sigma_3(n), -504 sigma_5(n), respectively, and constant term 1.','The scan suppresses normalization; the ring statement requires a consistent choice of generators.')
corr('P000615','final Kostant formula','psi(q) equals the character sum','psi(q) raised to dim K equals the character sum.','Compare the same notebook formula on P000610 and Kostant2003 Theorem0.1; the exponent is omitted in this repetition.')
checkpoint()

talk(371,'1975-10-06','J. Leray','P000615-P000618','Quadratic Fourier operators and the metaplectic group',
     r"""Leray explains the algebraic background of Maslov's method, beginning with the Schwartz space, its distribution dual, and linear position--momentum operators. Quadratic generating functions produce unitary integral operators. The notes then pass from their arbitrary scalar phases to the metaplectic double cover and its Maslov signs; this passage needs a phase convention beyond unitarity alone. The subject continues the metaplectic discussion in 1973-312.1--2 and 1973-315.1--4.""")
item(371,'P000616','construction','Heisenberg operators and their symplectic normalizer',
     r"""The operators \(a(x,\nu^{-1}\partial_x)\), linear in position and momentum, are normalized by automorphisms of \(S'(\mathbb R^\ell)\). The quotient by nonzero scalar operators is identified with \(\operatorname{Sp}(\ell)\).""",
     r"""Let \(Q_jf=x_jf\), \(P_jf=-i\hbar\partial_jf\), with \(\hbar>0\), on \(\mathcal S(\mathbb R^\ell)\subset L^2(\mathbb R^\ell)\subset\mathcal S'(\mathbb R^\ell)\). Their commutators encode the real symplectic form on \(\mathbb R^{2\ell}\). An invertible continuous complex-linear implementer preserving the common Schwartz domain and the real linear span of the \(Q_j,P_j\) induces a real symplectic transformation. In the irreducible Schrödinger representation, implementers of a fixed transformation differ by a scalar; allowing all nonzero scalar multiples gives kernel \(\mathbb C^\times\), while unitary implementers have kernel \(U(1)\).""",
     r"""The real structure, continuity, irreducible Schrödinger representation, and common invariant Schwartz domain are supplied. These conditions delimit the phrase \emph{automorphisms of distributions}; arbitrary algebraic automorphisms of \(S'\) are not being classified.""",
     r"""The metaplectic implementers and their action on Schwartz functions and distributions are verified in \citet[Section~1]{degosson1990maslov}. That article explicitly reviews the earlier Weil--Leray framework; this is an expository occurrence, not a new 1975 normalizer theorem.""",
     match='partial',area='Symplectic geometry')
item(371,'P000617','construction','Quadratic generating functions and unitary Fourier kernels',
     r"""For a real quadratic \(A(x,x')\), the notes write a kernel proportional to \(\Delta(A)e^{\nu A(x,x')}\), with \(\Delta(A)=\sqrt{\det A''}\), and the canonical relation \(p=A_x,\ p'=-A_{x'}\).""",
     r"""Assume \(A(x,y)\) is a real homogeneous quadratic form and its mixed Hessian \(B=\partial_x\partial_y A\) is invertible. The equations \(p=\partial_xA,\ p'=-\partial_yA\) define a linear symplectic map. For any phase \(\zeta\in U(1)\),
     \[ (T_Af)(x)=\zeta(2\pi\hbar)^{-\ell/2}|\det B|^{1/2}\int_{\mathbb R^\ell}e^{iA(x,y)/\hbar}f(y)\,dy \]
     defines a unitary operator on \(L^2\), initially on Schwartz functions and then by extension. It factors into quadratic phase multipliers, an invertible linear substitution with its Jacobian factor, and a Fourier transform.""",
     r"""Here \(\nu=i/\hbar\); the determinant means the mixed Hessian, and its absolute value supplies the modulus. The complex square-root phase in the notebook must be chosen consistently. Symplectic maps for which this mixed-coordinate generating function fails require other charts or products of such operators.""",
     r"""The explicit kernels and elementary factorization appear in \citet[Section~1, equations~(1.1)--(1.5)]{degosson1990maslov}. The formula verifies the local chart construction, with its missing determinant and phase qualifications.""",
     area='Symplectic geometry')
item(371,'P000617','claim','Unitarity alone does not select the metaplectic double cover',
     r"""The line \ru{Унитарность} \(\Rightarrow\) \ru{метапл. группа} is followed by \(|c|=1\), then by the instruction to take \(c=\pm1\).""",
     r"""All unitary canonical implementers form a central \(U(1)\)-extension of \(\operatorname{Sp}(2\ell,\mathbb R)\). The metaplectic group is a distinguished subgroup defined by coherent phase choices and fits into
     \[1\longrightarrow\{\pm I\}\longrightarrow\operatorname{Mp}(2\ell,\mathbb R)\longrightarrow\operatorname{Sp}(2\ell,\mathbb R)\longrightarrow1.\]
     Multiplying a unitary implementer by an arbitrary phase preserves unitarity and its underlying symplectic map. Thus the displayed implication requires the additional normalization.""",
     r"""The modern notation \(\operatorname{Sp}(2\ell,\mathbb R)\) denotes the group written \(\operatorname{Sp}(\ell)\) in the notes. The double cover is the corrected conclusion after phase normalization, not a consequence of \(|c|=1\) alone.""",
     r"""\citet[Section~1, Theorem~1]{degosson1990maslov} states the double-cover construction, using discrete phase indices in the generators. Earlier seminar occurrences are 1973-312.1--2.""",
     literal='false as written',match='partial',development='annotated',area='Symplectic geometry')
item(371,'P000617','claim','Composition phases and the Maslov sign',
     r"""The notebook writes \(S_AS_{A'}=S_{A''}\) and, when \(s_As_{A'}s_{A''}=e\), the doubly underlined identity \(S_AS_{A'}S_{A''}=\pm E\), with its sign linked to the Maslov index.""",
     r"""For lifts \(\widehat s_1,\widehat s_2,\widehat s_3\in\operatorname{Mp}(2\ell,\mathbb R)\) with \(s_1s_2s_3=I\), their product lies in the kernel and is \(\pm I\). In a nondegenerate quadratic-kernel chart, Gaussian integration contributes the signature phase \(e^{i\pi\operatorname{sgn}(H)/4}\), where \(H\) is the Hessian in the integrated intermediate variables. The discrete phase indices must incorporate this contribution. For arbitrary unitary lifts, the corresponding product can instead be any scalar in \(U(1)\).""",
     r"""The triple-product assertion is separated from a globally defined multiplication law for generating functions: compositions may leave a given chart, and an unqualified assignment \(A\mapsto S_A\) does not provide a global section of the cover.""",
     r"""\citet[Section~1, Theorem~2]{degosson1990maslov} gives the quadratic composition rule with its signature correction. The notes correctly point toward the Maslov obstruction but suppress the phase bookkeeping.""",
     match='partial',area='Symplectic geometry')
corr('P000617','quadratic determinant','Square root of det A double prime','Use the mixed Hessian, its absolute determinant for the modulus, and a separate coherent phase.','Scan inspected. The two Hessian strokes are ambiguous; the mixed-Hessian interpretation is required by the displayed generating relation.',type='ambiguity')
corr('P000617','unitarity implication','Unitarity implies metaplectic group; absolute value c equals 1','Unitarity gives a U(1) extension; a further phase normalization selects the double cover.','Scan confirms the implication and the following separate choice c=plus or minus1. The distinction is mathematical, not a translation error.')
checkpoint()

talk(372,'1975-10-13','E. S. Fradkin','P000616-P000622','Integrable particle systems and constrained quantization',
     r"""After Fradkin's reading list, Perelomov gives a substantial intervening report on Toda and Calogero--Moser systems. Its table distinguishes finding conserved quantities, proving their involution, reconstructing the dynamics, and performing quadratures; elliptic involution and exceptional root systems are explicitly questioned. Gelfand asks about a larger group-theoretic construction. Fradkin then returns to Bose and Fermi canonical variables, constrained Hamiltonian systems, and a formal functional integral. The individual attributions below follow the page headings rather than assigning Perelomov's report to Fradkin.""")
item(372,'P000618','theorem','Liouville integrability and quadratures',
     r"""Perelomov defines complete integrability by \(n\) first integrals in involution for \(H=\frac12\sum p_k^2+U(q)\); Gelfand recalls Liouville's theorem that the system can then be solved by quadratures.""",
     r"""On a smooth \(2n\)-dimensional symplectic manifold, suppose \(F_1=H,F_2,\ldots,F_n\) Poisson commute and \(dF_1,\ldots,dF_n\) are independent on the regular region under consideration. The local integration procedure reduces the motion to quadratures. A compact connected regular common level is an \(n\)-torus, with action--angle coordinates in a neighborhood and linear motion on each torus. Without compactness this global torus conclusion does not follow.""",
     r"""Functional independence, regularity and the separate compactness hypothesis are supplied; merely listing \(n\) possibly dependent conserved functions is insufficient.""",
     r"""The classical theorem is stated with completeness and regularity conditions in \citet[Section~4.4, Theorem~4.11]{cannas2007introduction}. This is background for the four distinct tasks subsequently listed by Gelfand.""",
     area='Integrable systems',speaker='A. M. Perelomov; I. M. Gelfand')
item(372,'P000618','remark','The pendulum quadrature is not a second independent integral',
     r"""For \(H=\frac12p^2+\sin q\), the next line reads \ru{2-й инт. --- эллиптич. ф-я}, rendered as a second integral and an elliptic function.""",
     r"""On an energy level \(H=E\), \(\dot q=p\) gives
     \[t-t_0=\pm\int_{q_0}^{q}\frac{ds}{\sqrt{2(E-\sin s)}}.\]
     Away from turning points this is a local quadrature; its inversion is expressed through elliptic functions for generic energy. The critical energies \(E=\pm1\) require separate limiting or equilibrium solutions. There cannot be a second functionally independent first integral on a regular two-dimensional phase region.""",
     r"""The abbreviation is interpreted as the second integration step, not an additional independent conserved quantity. The quadrature follows directly from the stated Hamiltonian.""",
     r"""This is the classical one-degree-of-freedom example; \citet[Section~4.5]{cannas2007introduction} treats the equivalent shifted pendulum Hamiltonian and its critical levels.""",
     literal='not determinable',match='partial',area='Integrable systems',speaker='A. M. Perelomov')
item(372,'P000618-P000619','construction','The periodic Toda Hamiltonian',
     r"""The first Toda potential is written as a difference of exponentials, with a summation index \(k\) but exponents using \(n\). P000619 instead gives \(U=g^2\sum_{k=1}^n e^{-(q_{k+1}-q_k)}\); P000618 states \(q_{k+n}=q_k\).""",
     r"""For \(n\geq3\), take the phase space \(T^*\mathbb R^n\), canonical brackets, and the periodic convention \(q_{n+1}=q_1\). The corrected Hamiltonian is
     \[H=\tfrac12\sum_{k=1}^np_k^2+g^2\sum_{k=1}^ne^{q_k-q_{k+1}}.\]
     The difference of neighboring exponentials belongs in the force equation \(\dot p_k=g^2(e^{q_{k-1}-q_k}-e^{q_k-q_{k+1}})\). Summing such differences as the potential would telescope to zero after correcting the index.""",
     r"""The potential is restored from the explicit repetition on P000619. The open chain has a different boundary convention and is not silently substituted for the periodic system.""",
     r"""\citet[abstract]{henon1974integrals}, published 15 February 1974, explicitly reports \(n\) integrals for periodic Toda and covers fixed ends separately. Only that publisher statement and metadata were checked here.""",
     literal='false as written',match='partial',verification='publisher metadata checked',development='annotated',area='Integrable systems',speaker='A. M. Perelomov')
item(372,'P000618','question','Involution of the Toda integrals',
     r"""The chronology names Hénon, Flaschka, Manakov, and Kac--van Moerbeke, adding that integrals existed but involution had not been proved.""",
     r"""For the periodic Toda Hamiltonian of 1975-372.3, the issue is to exhibit \(n\) generically independent conserved functions \(I_1,\ldots,I_n\) with \(\{I_j,I_k\}=0\), not merely to produce an isospectral matrix evolution. Independence is understood on an open dense regular set; the center-of-mass motion remains a free degree of freedom.""",
     r"""The precise family and boundary condition are fixed by the adjacent potential. The notebook's historical assertion about which proof was available in October 1975 has not been independently established.""",
     r"""A subsequent paper is specifically devoted to this claim: \citet[pp.~1668--1669]{kawasaki1976involution}, received 8 January and published 1 May 1976. Its publisher record was checked, but the proof was not accessed, so neither an earliest-proof priority nor an exact match to every named 1975 family is asserted.""",
     cls='B',status='Toda involution is established; the precise chronology claimed by this note remains only partially verified.',literal='not determinable',match='partial',verification='publisher metadata checked',confidence='medium',problem='GP-1975-05',area='Integrable systems',speaker='A. M. Perelomov')
item(372,'P000618','construction','Five pair-potential families and their phase spaces',
     r"""The table lists \(q^{-2}\), \(a^2\sinh^{-2}(aq)\), \(a^2\sin^{-2}(aq)\), \(a^2\wp(aq)\), and \(q^{-2}+a^2q^2\), first for \(U=g^2\sum_{i<j}V(q_i-q_j)\). The hyperbolic and trigonometric cases are called limits of the elliptic case.""",
     r"""For \(n\) particles on the line, use canonical coordinates \((q_i,p_i)\) on the cotangent bundle of a collision-free configuration chamber; exclude all poles of \(V\). The trigonometric model may instead be interpreted on a circle, with collisions modulo its period excluded. In the elliptic model choose periods and a real slice on which the potential is real. The fifth pair potential leaves the center of mass free:
     \(\sum_{i<j}(q_i-q_j)^2=n\sum_i(q_i-Q_{\rm cm})^2\).
     Thus its relative motion has harmonic confinement, while a one-body trap \(\frac12\omega^2\sum q_i^2\) also confines the center of mass. Elliptic degenerations give the first three potentials up to scale and additive constants.""",
     r"""The domains, reality conditions and separation of center-of-mass motion are supplied. No integrability claim is inferred for arbitrary singular continuations or boundary identifications.""",
     r"""The five types and their allowed chambers are explicitly listed in \citet[Section~2, equations~(2.1)--(2.6)]{olshanetskyperelomov1978radial}; their classical antecedents are summarized in \citet[Section~2]{sasaki2006explicit}. The named \(A\)-type models were already being reported as known here.""",
     match='partial',area='Integrable systems',speaker='A. M. Perelomov')
item(372,'P000618-P000619','construction','Classical and nonreduced root-system potentials',
     r"""The second family adds \(V(q_i+q_j)\), \(V(q_i)\), and \(V(2q_i)\). P000619 rewrites this as \(\sum_{\alpha>0}g_\alpha^2V((\alpha,q))\), with equal couplings for equal root lengths, and identifies types \(A,B,C,BC,D\).""",
     r"""Let \(R\) be a finite crystallographic root system, or the standard nonreduced \(BC_r\), in a Euclidean space \(\mathfrak a\). On \(T^*\mathfrak a_{\rm reg}\), away from the potential's root hyperplanes or affine pole walls, set
     \[H=\tfrac12(p,p)+\sum_{\alpha\in R_+}c_\alpha V((\alpha,q)),\]
     with couplings constant on Weyl orbits. The roots \(e_i-e_j\) yield \(A_{n-1}\) for \(n\) particles after separating the center of mass; \(e_i\pm e_j,e_i,2e_i\) yield the \(BC\) family. In the displayed \(B\) formula the plus and minus pair terms must have compatible Weyl-invariant coefficients; an arbitrary independent \(\varepsilon\) is not covered by this statement.""",
     r"""The shift from \(A_n\) to \(A_{n-1}\) records the usual rank convention. Weyl-orbit coupling and regular-domain hypotheses are made explicit. This item is the construction, distinct from the exceptional-case integrability question.""",
     r"""The speaker's joint work gives this root-system framework in \citet[Section~2]{olshanetskyperelomov1978radial}; that 1978 paper itself cites the classical 1976 construction. The match is to the stated family, not to every arbitrary coefficient suggested by the shorthand.""",
     cls='A',match='partial',area='Integrable systems',speaker='A. M. Perelomov')
item(372,'P000618','question','Commuting complete integrals in the elliptic case',
     r"""In row 4, conserved quantities for the elliptic potential are credited to Calogero and Olshanetsky--Perelomov, while the involution column contains two question marks, corresponding to families A and B.""",
     r"""For the unreduced \(n\)-particle elliptic Calogero--Moser system on \(T^*Q_{\rm reg}\), where \(Q_{\rm reg}\subset\mathbb R^n\) (or \(\mathbb C^n\)) excludes every pair difference at a potential pole, do there exist \(n\) generically independent meromorphic integrals in involution, including the free center-of-mass momentum? After removing the center-of-mass canonical pair, the relative \(A_{n-1}\) problem instead needs \(n-1\) integrals. The analogous root-system question requires orbit-constant couplings. The assertion concerns generic regular points, not a uniform action--angle chart through collisions or singular fibers.""",
     r"""The two table columns are retained, but the completely verified answer below is restricted to reduced crystallographic root systems, including \(A,B,C,D\). No blanket identification with every nonreduced \(BC\) or arbitrary-\(\varepsilon\) variant is made.""",
     r"""\citet[pp.~3--5 and Table~I]{khastgirsasaki2001liouville} proves involution and independence for the root-system Calogero--Moser models, including the elliptic potentials in its scope. The preprint circulated 30 May 2000 and appeared in print in 2001; it supplies a verified later answer, not a claim to the first solution.""",
     cls='B',status='Affirmative for the reduced crystallographic elliptic models specified here; the shorthand B-family is broader than the exact formulation checked.',
     match='partial',problem='GP-1975-02',area='Integrable systems',speaker='A. M. Perelomov')
item(372,'P000618','method','Four separate tasks in solving an integrable model',
     r"""Gelfand lists: find the integrals, prove involution, solve the inverse problem, and express the solution by quadratures.""",
     r"""Conservation, \(\{I_j,H\}=0\), does not imply mutual involution or functional independence. Liouville integration requires a complete independent commuting family on a regular region. An inverse problem additionally requires specification of spectral data and its equivalences; quadrature or explicit inversion is a further constructive step. Consequently the table's question marks concern different mathematical assertions.""",
     r"""The fourth phrase is interpreted as integrating the dynamics, rather than evaluating an already known constant of motion. No single unsolved theorem is extracted from this methodological list.""",
     r"""The distinction is consistent with the hypotheses of \citet[Theorem~4.11]{cannas2007introduction}; concrete inverse data are addressed separately in 1975-372.11.""",
     literal='correct',match='partial',area='Integrable systems',speaker='I. M. Gelfand')
item(372,'P000619','construction','Lax matrices and trace invariants',
     r"""For types 1--4, \(I_k=\operatorname{Sp}(L^k)\), with \(L=P+iX\), \(P_{ij}=p_i\delta_{ij}\), and \(X_{ij}=(1-\delta_{ij})x(q_i-q_j)\). The table gives \(x=q^{-1},a\coth(aq),a\cot(aq),a\,\operatorname{cn}(aq)/\operatorname{sn}(aq)\).""",
     r"""An exact rational reconstruction is
     \[L_{ij}=p_i\delta_{ij}+\frac{ig(1-\delta_{ij})}{q_i-q_j},\qquad
     M_{ij}=-\frac{ig}{(q_i-q_j)^2}\ (i\ne j),\quad M_{ii}=ig\sum_{j\ne i}(q_i-q_j)^{-2}.\]
     For \(H=\frac12\sum p_i^2+g^2\sum_{i<j}(q_i-q_j)^{-2}\), Hamilton's equations give \(\dot L=[L,M]\), hence every \(\operatorname{tr}L^k\) is conserved and \(H=\frac12\operatorname{tr}L^2\). This argument alone does not prove involution. The nonrational kernels require compatible diagonal terms, coupling and elliptic-period conventions; the table alone does not specify these.""",
     r"""The missing coupling and companion matrix are supplied only for the rational case. No assertion that the displayed scalar \(n\times n\) matrix directly represents every \(B,C,D\) model is retained.""",
     r"""The rational matrix is verified in \citet[Section~5, equations~(5.2)--(5.10)]{sasaki2006explicit}; the notebook's broader table is therefore a partial match.""",
     match='partial',area='Integrable systems',speaker='A. M. Perelomov')
item(372,'P000619','construction','The quadratic matrix invariant for harmonic confinement',
     r"""For type 5 the notes use \(N=L^2+\omega^2Q^2\), \(Q=\operatorname{diag}(q_i)\), and \(I_k=\operatorname{Sp}(N^k)\).""",
     r"""For the rational Calogero Hamiltonian with a one-body harmonic trap, the rational matrices satisfy
     \(\dot L=[L,M]-\omega^2Q\), \(\dot Q=[Q,M]+L\).
     Therefore \(N=L^2+\omega^2Q^2\) satisfies \(\dot N=[N,M]\), and \(\operatorname{tr}N^k\) is conserved. For the pairwise quadratic potential on P000618 this applies to the relative variables after separating the free center of mass and matching the frequency; with the table's coefficients, \(\omega^2=2ng^2a^2\). Conservation of these traces is the assertion verified here, not a separate proof that this particular list is independent and in involution.""",
     r"""The phase space is a collision-free chamber, with either the stated one-body trap or the explicitly reduced center-of-mass system. The matrix identity follows by the product rule from the two displayed evolution equations.""",
     r"""The required equations are read in \citet[Section~3, equations~(3.1)--(3.3)]{sasaki2006explicit}. Their elementary consequence validates the notebook formula once its phase-space convention is supplied.""",
     match='partial',area='Integrable systems',speaker='A. M. Perelomov')
item(372,'P000618-P000619','question','Inverse spectral data require more than the traces',
     r"""Every inverse-problem column for types 1--5 carries a question mark. The text says to find matrix entries from traces of powers and says the inverse problem is solved only for Toda, with Stieltjes named.""",
     r"""The traces determine the characteristic polynomial of a finite matrix, not its entries or the full phase point. Even in the rational family, \(q_i\mapsto q_i+c\) leaves \(L\) unchanged. A well-posed reconstruction must add position or eigenvector data and specify permutation, conjugation and center-of-mass conventions. For the rational model, full initial matrices \(Q_0,L_0\) determine the particle positions as the eigenvalues of \(Q_0+tL_0\); for a harmonic trap replace this by \(Q_0\cos\omega t+\omega^{-1}L_0\sin\omega t\), on regular intervals.""",
     r"""The literal trace-only reconstruction is underdetermined. The explicit initial-value formulas are a bounded corrected formulation, not a solution of recovering every matrix from its spectrum. Stieltjes data for a finite Jacobi matrix include spectral weights; the notebook gives no boundary specification making that name an exact periodic-Toda inverse theorem.""",
     r"""\citet[Sections~2--4, especially (2.17)--(2.18) and (3.7)--(3.8)]{sasaki2006explicit} verifies the augmented-data solution. Its historical discussion attributes the \(A\)-type matrix method to Olshanetsky--Perelomov's 1976 papers. Thus the precise initial-value problem was developed, while the trace-only wording remains false.""",
     cls='A',status='Explicit reconstruction is available with adequate initial or spectral data; traces alone cannot determine a phase point.',literal='false as written',match='partial',verification='indirect',problem='GP-1975-04',development='annotated',area='Inverse problems',speaker='A. M. Perelomov')
item(372,'P000619','claim','Higher commuting particle flows',
     r"""Manakov's work is described as a finite-dimensional analogue of the higher KdV hierarchy, with the first two cases treated.""",
     r"""Once a mutually commuting complete collection of spectral Hamiltonians has been established, their Hamiltonian vector fields commute. For the rational \(A\)-type model, \(H_k=\operatorname{tr}(L^{k+1})/(k+1)\) gives higher flows with \(\partial_{t_k}L=[L,M_k]\). Their existence and commutativity require the Poisson statement; isospectrality alone is insufficient.""",
     r"""The report does not identify the dissertation or the exact two cases. Only the rational \(A\)-type hierarchy is reconstructed explicitly; the historical priority claim remains unverified.""",
     r"""The concrete hierarchy and integration formulas are read in \citet[Section~5]{sasaki2006explicit}. This is a partial mathematical identification of the notebook's analogy, without replacing its uncertain Manakov reference by an invented bibliographic match.""",
     match='partial',confidence='medium',area='Integrable systems',speaker='A. M. Perelomov')
item(372,'P000619','claim','Quantum Hamiltonians as conjugated radial Laplacians',
     r"""After \(p=-i\partial_q\), the quantum Hamiltonian is identified with the radial part of a Laplace operator on a symmetric space, particularly for the trigonometric system.""",
     r"""For a Riemannian symmetric space, restriction of the Laplace--Beltrami operator to invariant functions gives a radial differential operator with first-derivative terms. Conjugation by the square root of the radial density removes them and produces a Schrödinger operator of Calogero--Sutherland type, up to an additive constant and scale. The couplings are determined by the restricted-root multiplicities. The compact, noncompact and flat cases lead respectively to trigonometric, hyperbolic and rational interactions. Arbitrary continuous couplings need not come from an actual symmetric space.""",
     r"""Conjugation, the energy shift, root multiplicities and radial domains are missing from the equality in the notes. The statement is a relation of differential expressions; self-adjoint domains and boundary conditions are additional analytic data.""",
     r"""\citet[Section~3, Lemma~1, Proposition~1 and Theorems~1--2]{olshanetskyperelomov1978radial} supplies the precise group-coupling formulation. Received 16 June 1977 and published in 1978, it is a subsequent publication by the intervening speaker.""",
     cls='A',match='partial',area='Representation theory',speaker='A. M. Perelomov')
item(372,'P000619','question','Gelfand’s larger group-integrability programme',
     r"""Gelfand asks whether everything can be reduced to group integrability in a larger space.""",
     r"""The line suggests realizing the particle system by reduction of a simpler group or matrix motion. It does not specify the larger phase space, group, moment-map value, equivalence relation, allowed potentials, or meaning of solving the group motion. It therefore does not determine a universal theorem or a yes/no problem with fixed hypotheses.""",
     r"""Hamiltonian reduction is an interpretation of the suggestion, not wording recovered from the note.""",
     r"""A concrete rational \(A\)-type realization is described in \citet[Section~7, equations~(7.1)--(7.4)]{sasaki2006explicit}. This confirms the theme but does not settle the unspecified word \emph{everything}.""",
     cls='F',status='The general programme is not a determinate problem in this record.',literal='not determinable',match='thematic only',verification='indirect',confidence='medium',area='Integrable systems',speaker='I. M. Gelfand')
item(372,'P000619','question','Complete integrability for exceptional root systems',
     r"""The root-system construction ends: it is still unclear whether the systems for exceptional groups are completely integrable.""",
     r"""For \(R=G_2,F_4,E_6,E_7,E_8\) of rank \(r\), take the canonical phase space away from all poles of
     \[H=\tfrac12(p,p)+\sum_{\alpha\in R_+}c_\alpha V((\alpha,q)),\]
     with positive real couplings constant on Weyl orbits, and \(V\) rational, hyperbolic, trigonometric or untwisted elliptic, with a compatible real slice. The question is existence of \(r\) generically independent integrals in involution. Harmonic confinement is a separate variant and is not included in the verified elliptic theorem below.""",
     r"""The statement fixes the root systems, couplings and regular domain, and distinguishes Liouville integrability from global nonsingular coordinates or an explicit solution formula.""",
     r"""\citet[pp.~3--5 and Table~I]{khastgirsasaki2001liouville} verifies Liouville integrability in this scope, with first public preprint 30 May 2000. Earlier group-coupling cases are covered in \citet[Theorem~1 and Corollary~1]{olshanetskyperelomov1978radial}. These are affirmative developments, not evidence of a remaining exceptional-root obstruction.""",
     cls='B',status='Affirmative in the stated exceptional-root scope; no open remainder is inferred from the 1975 uncertainty.',
     problem='GP-1975-03',area='Integrable systems',speaker='A. M. Perelomov')
item(372,'P000619','claim','The quantum sine-Gordon and massive Thirring correspondence',
     r"""A short line names Coleman and Schroer for a connection between the Thirring model and sine-Gordon.""",
     r"""The identifiable claim concerns bosonization in \(1+1\) spacetime dimensions: a suitably renormalized sine-Gordon scalar theory corresponds to the zero-charge sector of the massive Thirring fermion theory, with coupling parameters related. At \(\beta^2=4\pi\), Coleman's formulation gives the free massive fermion case. This is a quantum correspondence with a sector and renormalization prescription, not equality of the two classical equations.""",
     r"""Only Coleman's identifiable result is delimited here. The single surname Schroer does not identify a second paper or an independent theorem, and no exact coupling formula absent from the opened abstract is supplied.""",
     r"""\citet[abstract]{coleman1975equivalence} states this correspondence and its free-fermion specialization; the paper was publicly published 15 April 1975. The full proof was not accessed.""",
     match='partial',verification='publisher metadata checked',area='Quantum field theory',speaker='A. M. Perelomov')
item(372,'P000619-P000620','construction','Classical Grassmann coordinates and the graded Poisson bracket',
     r"""Fradkin allows Bose and Fermi canonical variables, writes \(pq+qp=1\) after Grassmann variables, and then introduces a Poisson bracket using right and left derivatives and the parities \(n_A,n_B\).""",
     r"""Classical odd coordinates in a supercommutative algebra satisfy \(\theta_a\theta_b=-\theta_b\theta_a\), so their algebra product does not obey \(pq+qp=1\). That relation belongs to quantized creation and annihilation operators, or to an odd multiplication operator paired with differentiation. An even graded Poisson bracket instead satisfies
     \[\{A,B\}=-(-1)^{|A||B|}\{B,A\},\qquad
       \{A,BC\}=\{A,B\}C+(-1)^{|A||B|}B\{A,C\}.\]
     Canonical even pairs obey \(\{q_i,p_j\}=\delta_{ij}\), while an odd canonical pair has a symmetric bracket \(\{\theta_a,\pi_b\}=\{\pi_b,\theta_a\}=\delta_{ab}\), after choosing left/right derivative conventions.""",
     r"""The algebra product, the classical graded bracket and the quantum anticommutator are separated. This removes the contradiction while preserving the intended mixed canonical formalism.""",
     r"""The basic distinction is algebraic and predates the talk; Berezin is explicitly named in the record. The later general constrained formalism in \citet[abstract, publication lead]{fradkinfradkina1978quantization} matches the theme, but its inaccessible full text is not used to certify the notebook's derivative signs.""",
     literal='false as written',match='partial',verification='indirect',development='annotated',area='Constrained quantization')
item(372,'P000619','claim','Gauge constraints and the two photon polarizations',
     r"""Electromagnetism and Yang--Mills theory are examples of constrained systems; light has two states rather than three because gauge invariance removes an extra state.""",
     r"""For free Maxwell theory in \(3+1\)-dimensional Minkowski space, a nonzero null momentum has a transverse polarization space modulo gauge shifts \(\epsilon_\mu\mapsto\epsilon_\mu+\lambda k_\mu\). This quotient is two-dimensional, corresponding to two physical helicities. In Hamiltonian language the primary and Gauss constraints, together with gauge equivalence, remove the unphysical canonical variables. The assertion does not count polarizations of a massive vector field, which has a different constraint structure.""",
     r"""The spacetime dimension, massless free field and gauge quotient are supplied to make the numerical assertion definite.""",
     r"""The constraint and polarization analysis is checked in \citet[Sections~6.1--6.2]{tong2006qft}; this is established Maxwell theory, used as an example rather than a new 1975 result.""",
     area='Quantum field theory')
item(372,'P000620','method','The singular Legendre map and the constraint algorithm',
     r"""The momentum is defined by a right derivative of \(L\); failure to solve for \(\dot q\), expressed by a vanishing Hessian determinant, leads to additional constraints and the Dirac procedure.""",
     r"""For an ordinary finite-dimensional Lagrangian \(L(q,\dot q)\), an invertible velocity Hessian gives a local Legendre transformation by the inverse function theorem. A constant-rank singular Legendre map has a locally constrained image. Preservation of primary constraints under Hamiltonian evolution can impose secondary constraints, fix multipliers, or reveal gauge freedom. In a Bose--Fermi system the relevant invertibility is that of a graded linear map; an ordinary determinant is inadequate for a general mixed Hessian.""",
     r"""Constant-rank and local regularity assumptions are supplied. Singular rank-changing Lagrangians are not covered by a statement that all constraints automatically form a finite-dimensional Lie algebra with constant structure coefficients.""",
     r"""The regular Legendre step is recalled in \citet[Appendix~C.4]{cannas2007introduction}. The mixed constrained extension is the subject of the later Fradkin--Fradkina publication lead, whose exact formula has not been read \citep{fradkinfradkina1978quantization}.""",
     match='partial',verification='indirect',area='Constrained quantization')
item(372,'P000620','definition','First- and second-class constraints require a rank condition',
     r"""Second-class constraints are described by brackets \(\{\varphi_k,\psi_j\}\ne0\) after imposing the other constraints, with central constraints discarded.""",
     r"""On a regular constraint surface, a first-class function has bracket zero on that surface with every constraint. A selected family \(\chi_a\) is second class when its bracket matrix \(C_{ab}=\{\chi_a,\chi_b\}\) is invertible on the surface (in the graded sense when needed). A nonzero matrix entry alone is insufficient. For purely even second-class constraints,
     \[\{F,G\}_D=\{F,G\}-\{F,\chi_a\}(C^{-1})^{ab}\{\chi_b,G\}\]
     is the Dirac bracket, under the usual regularity assumptions. First-class constraints may close with phase-space-dependent structure functions rather than constants.""",
     r"""The invertibility condition replaces the notebook's entrywise nonvanishing shorthand. The displayed bracket is explicitly restricted to the ungraded case so that no missing super-sign convention is hidden.""",
     r"""This is the Dirac distinction named in the note. The relation with general Bose--Fermi quantization is only indirectly identified through \citet[abstract, publication lead]{fradkinfradkina1978quantization}; the original Dirac book edition is not specified here.""",
     literal='false as written',match='partial',verification='indirect',development='annotated',area='Constrained quantization')
item(372,'P000620','construction','Sources and the formal generating functional',
     r"""The displayed \(Z\) integrates fields and canonical momenta against constraint delta functions and an exponential of the Hamiltonian action plus sources. It is called the generating function of all Green functions and an analogue of a Fourier transform.""",
     r"""Formally, with fixed boundary or vacuum prescription and consistent factors of \(i\), one writes \(Z[J]=C^{-1}\int D\mu\,e^{iS+i\langle J,\Phi\rangle}\). Functional derivatives with respect to even and odd sources generate the corresponding ordered correlation functions. The measure \(D\mu\), constraint reduction or gauge fixing, regularization, and source parity must be specified. This symbolic integral is not a countably additive Lebesgue measure on an infinite-dimensional field space, and the line alone does not define all quantum theories.""",
     r"""Only the formal generating-functional mechanism is reconstructed. The notebook's crossed-out measure and uncertain grouping are not silently converted into a rigorous path-integral theorem.""",
     r"""Formal source differentiation gives the generating mechanism; the Wick expansion read in \citet[Section~3.3]{tong2006qft} checks the corresponding perturbative correlation-function structure, not existence of the displayed measure. A more specific subsequent constrained construction is suggested by \citet[abstract, publication lead]{fradkinfradkina1978quantization}, but an exact formula-by-formula identification has not been verified.""",
     cls='E',literal='not determinable',match='partial',verification='indirect',confidence='medium',area='Constrained quantization')
item(372,'P000620','claim','The constraint determinant and the ambiguous term A',
     r"""The term \(A\) contains trace logarithms of even and odd constraint brackets and a Schur-complement expression. It appears after the exponent's integral, while another exponential and \(\delta(0)/2\) occur inside the definition of \(A\).""",
     r"""A finite-dimensional model for regular second-class reduction inserts the constraint delta function and the square root of the determinant of the bracket matrix; with even and odd constraints the corresponding object is a square root of a Berezinian, with conventions fixed. For a block matrix \(C=\left(\begin{smallmatrix}A&B\\ C_1&D\end{smallmatrix}\right)\) with invertible odd block \(D\),
     \[\operatorname{Ber}C=\frac{\det(A-BD^{-1}C_1)}{\det D}.\]
     This explains the visible Schur complement and difference of trace logarithms. It does not determine the notebook's misplaced exponential, numerical coefficient, sign, or distributional factor. First-class systems also require gauge fixing or its equivalent.""",
     r"""The Berezinian is an explicit algebraic reconstruction of the visible pattern; the complete \(A\) formula remains unresolved. No universal determinant formula for arbitrary quantum field theories is claimed.""",
     r"""The abstract of the 1978 Fradkin--Fradkina lead concerns precisely mixed first- and second-class constraints, but its full text was inaccessible \citep{fradkinfradkina1978quantization}. The exact displayed expression therefore remains a partial, indirect identification rather than a verified publication match.""",
     cls='F',status='The regular determinant/Berezinian mechanism is standard; the exact notebook term A has not been recovered.',
     literal='not determinable',match='thematic only',verification='indirect',confidence='medium',area='Constrained quantization')
item(372,'P000620','claim','The asserted cancellation of delta at zero',
     r"""The final line says that \(\delta(0)\) later cancels in the \(S\)-matrix.""",
     r"""No theory, regularization, observable definition, order in perturbation theory, or cancellation mechanism is specified. Consequently the line does not state a determinate cancellation theorem. In particular, a formal trace logarithm at coincident points cannot be assigned a numerical value merely by writing \(\delta(0)\).""",
     r"""The uncertainty concerns the missing model and prescriptions, beyond a possible transcription ambiguity in the preceding \(A\).""",
     r"""The related general constrained-quantization publication lead does not verify this specific cancellation \citep{fradkinfradkina1978quantization}. No exact source match was obtained for the isolated claim.""",
     cls='F',status='No definite universal cancellation statement can be extracted.',literal='not determinable',match='none found',verification='unresolved lead',confidence='low',area='Constrained quantization')
problems.extend([
 dict(id='GP-1975-02',title='Involution for elliptic Calogero--Moser systems',statement=r"""For reduced crystallographic root systems with Weyl-orbit couplings, construct a generically independent complete set of commuting integrals for the elliptic Hamiltonian on its regular canonical phase space; retain the free center of mass in the particle \(A\)-model.""",occurrences=['1975-372.7'],status=r"""As of 10 November 2026: affirmative in this scope; \citet[pp.~3--5]{khastgirsasaki2001liouville} is a directly checked proof, first publicly circulated 30 May 2000. This does not certify every arbitrary-\(\varepsilon\) or nonreduced variant in the shorthand table.""",status_date='2026-11',refs=['khastgirsasaki2001liouville']),
 dict(id='GP-1975-03',title='Integrability of exceptional-root Calogero--Moser systems',statement=r"""For \(G_2,F_4,E_6,E_7,E_8\), determine Liouville integrability of the rational, hyperbolic, trigonometric and untwisted elliptic root potentials with couplings constant on Weyl orbits, away from poles.""",occurrences=['1975-372.15'],status=r"""As of 10 November 2026: affirmative in the stated scope. The group-coupling cases occur in \citet[Theorem~1 and Corollary~1]{olshanetskyperelomov1978radial}; \citet[pp.~3--5]{khastgirsasaki2001liouville} supplies the checked general involution argument. Harmonic confinement is not included in that elliptic theorem.""",status_date='2026-11',refs=['olshanetskyperelomov1978radial','khastgirsasaki2001liouville']),
 dict(id='GP-1975-04',title='Adequate inverse data for Calogero--Moser particle systems',statement=r"""Identify data sufficient to recover a regular particle trajectory, with center-of-mass and permutation conventions fixed. The trace-only wording in the notebook is underdetermined; a concrete corrected rational problem uses the full initial matrices \(Q_0,L_0\).""",occurrences=['1975-372.11'],status=r"""As of 10 November 2026: the rational initial-value reconstruction is explicit by diagonalizing \(Q_0+tL_0\), or its harmonic counterpart. These formulas are read in \citet[Sections~2--3]{sasaki2006explicit}. Traces alone still do not determine matrix entries or a phase point.""",status_date='2026-11',refs=['sasaki2006explicit']),
 dict(id='GP-1975-05',title='Involution of the periodic Toda integrals',statement=r"""For the periodic \(n\)-particle Toda Hamiltonian, exhibit \(n\) generically independent conserved functions that commute for the canonical Poisson bracket, keeping the free center-of-mass degree of freedom.""",occurrences=['1975-372.4'],status=r"""As of 10 November 2026: established. \citet[pp.~1668--1669]{kawasaki1976involution}, published 1 May 1976, is a verified publisher record devoted to the claim. Its proof and the earliest-priority chronology were not independently read in this check.""",status_date='2026-11',refs=['kawasaki1976involution'])
])
corr('P000618','first Toda potential','Difference of exponentials with n in the exponents under a sum over k','Use the single exponential sum displayed on P000619; the difference belongs to a force equation.','Both scans inspected. Changing n to k alone would produce a telescoping sum, not the Toda potential.')
corr('P000618','pendulum abbreviation','Second integral is an elliptic function','Interpret as the next integration or inversion step; there is only one independent first integral for one degree of freedom.','The abbreviated Russian permits this reading; the energy equation gives the explicit quadrature.',type='ambiguity')
corr('P000619','root-system rank','n particles associated with A_n','n particles have relative root system A_(n-1), with a separate center-of-mass coordinate.','The listed roots e_i-e_j span the sum-zero hyperplane in R^n; the notebook does not fix its rank convention.',type='ambiguity')
corr('P000619','classical Fermi variables','pq+qp=1 for Grassmann variables','Classical odd coordinates anticommute to zero; 1 is the canonical quantum anticommutator or multiplication/differentiation pairing.','Scan confirms the 1. The subsequent graded Poisson construction requires separating these meanings.')
corr('P000620','second-class condition','Nonzero pairwise brackets','Invertibility of the complete constraint-bracket matrix on the regular constraint surface.','The scan states nonzero brackets; entrywise nonvanishing does not imply invertibility.')
corr('P000620','A and exponential grouping','A added after the action integral and itself beginning with an exponential','Retain the unresolved grouping; the Schur-complement pattern suggests a determinant or Berezinian measure factor.','Scan inspected; multiple braces and the inserted second trace are visibly ambiguous. No complete emendation was verified.',type='ambiguity')
checkpoint()

talk(373,'1975-10-20','I. M. Gelfand','P000620-P000622','Fractional differential operators and stationary KdV',
     r"""Gelfand introduces Krichever's report by recalling the differential parts of fractional Schrödinger powers and the stationary one-gap equation. His final suggestion of an unworked-out noncommutative theory remains a programme rather than a precise conjecture. This brief intervention continues the higher-KdV discussion of 1973 and the finite-gap work of 1974.""")
item(373,'P000621','construction','Differential parts of fractional powers and the KdV hierarchy',
     r"""For \(L=-D^2+u\), \(A=D^3+\cdots\) is described as \(L^{3/2}\) with nondifferential terms cut off. The same operation on \(L^{5/2},L^{7/2},\ldots\) leaves a commutator that is multiplication by a function.""",
     r"""Use the formal pseudodifferential algebra and choose \(R=(-L)^{1/2}=D+O(D^{-1})\). Then \(B_{2j+1}=(R^{2j+1})_+\), the part with nonnegative powers of \(D\), satisfies \([B_{2j+1},L]\) of differential order at most zero. For \(j=1\),
     \[B_3=D^3-\tfrac32uD-\tfrac34u',\qquad [L,B_3]=\tfrac32uu'-\tfrac14u'''.\]
     Thus the corresponding Lax equation gives KdV after a constant time rescaling. The formal higher flows commute; analytic existence for particular function spaces is a separate issue.""",
     r"""The branch and sign are essential: \(L=-D^2+u\) has no formal square root with leading term \(D\). The construction is algebraic, not the spectral fractional power of an unbounded self-adjoint operator.""",
     r"""The hierarchy was already discussed in 1973-326.1 and 1973-327.1, so the present statement is expository. A systematic later fractional-operator treatment is read in \citet[Sections~8--12]{gelfanddikii1976fractional}, received 22 June 1976 and published that year.""",
     cls='E',match='partial',problem='GP-1973-53',area='Integrable systems')
item(373,'P000621','claim','The stationary third-order equation and one-gap potentials',
     r"""A one-zone potential is identified by \(K(u)=0\), so that the second- and third-order operators commute; this is called a hypothesis in the notes.""",
     r"""For a real smooth periodic potential, the existence of a normalized third-order commuting operator gives a stationary KdV equation
     \[u'''-6uu'+cu'=0\]
     for a constant \(c\). For example \(A=-4D^3+6uD+3u'-cD\) obeys \([A,-D^2+u]=6uu'-u'''-cu'\). Such periodic stationary solutions have at most one finite open spectral gap; the nonconstant nonsingular elliptic case has one, and constant or degenerate cases must be distinguished. A general one-gap potential need not obey the unshifted equation with \(c=0\).""",
     r"""Real smooth periodicity, the lower-flow constant, and the meaning of one finite open gap are supplied. The algebraic commutator calculation by itself does not establish a band-spectrum statement for arbitrary complex or nonperiodic coefficients.""",
     r"""\citet[Section~2, Theorem~2.1 and the \(n=1\) example on p.~63]{novikov1974periodic} verifies the stationary-to-finite-gap implication before this talk. The converse characterization belongs to the earlier problem GP-1974-10, represented here by its one-gap occurrence; see also 1974-340.7 and 1974-343.2.""",
     match='partial',problem='GP-1974-10',area='Spectral theory')
item(373,'P000621','conjecture','An unspecified noncommutative theory',
     r"""Gelfand calls the construction a piece of an \ru{несделанной некоммут. теории}; Krichever replies that he in fact started from this.""",
     r"""No algebra, objects, equivalences or proposed theorem are specified. The phrase might refer to noncommuting coefficient rings, the ambient differential-operator algebra, or a broader structural explanation of integrability; these are different mathematical programmes.""",
     r"""None of these alternatives is selected as the uniquely intended problem. The following theory of commutative scalar differential-operator rings cannot be treated as the solution of every possible noncommutative extension.""",
     r"""The adjacent report is identified precisely in 1975-374.1--10. The historical thematic connection is also visible in \citet[introduction and Section~2]{krichever1977methods}, but this does not recover a definite conjecture.""",
     cls='F',status='No determinate conjecture can be extracted from this phrase.',literal='not determinable',match='thematic only',verification='indirect',confidence='low',area='Integrable systems')
problems.extend([
 dict(id='GP-1973-53',title='Recursive construction of KdV Lax operators',statement=r"""Construct odd differential operators from formal fractional powers of the Schrödinger operator so that their commutators with it have order zero, and organize the resulting compatible higher KdV flows.""",occurrences=['1973-326.1','1973-327.1','1975-373.1'],status=r"""As of 10 November 2026: established in the formal differential-algebra setting; \citet[Sections~8--12]{gelfanddikii1976fractional} provides the systematic formulation. Formal fractional powers are distinguished from spectral functional calculus.""",status_date='2026-11',refs=['gelfanddikii1976fractional']),
 dict(id='GP-1974-10',title='Finite-gap spectra and stationary KdV characterization',statement=r"""Relate real smooth periodic Schrödinger potentials with finitely many open gaps to stationary equations in the KdV hierarchy; the present occurrence is the third-order, at-most-one-gap case.""",occurrences=['1974-340.7','1974-343.2','1975-373.2'],status=r"""As of 10 November 2026: the periodic stationary-to-finite-gap implication is read in \citet[Section~2, Theorem~2.1]{novikov1974periodic}. The one-gap specialization requires the lower-flow constant and allowance for degenerations; the older general problem's full occurrence list belongs to the cumulative index.""",status_date='2026-11',refs=['novikov1974periodic'])
])
corr('P000621','fractional-power normalization','L=-D squared+u and A equals L to the three-halves with leading D cubed','Use the formal square root of -L with leading D, or supply the equivalent complex phase for a root of L.','Scan confirms both signs. This is a formal branch and normalization issue, not spectral functional calculus.',type='ambiguity')
checkpoint()

talk(374,'1975-10-20','I. M. Krichever','P000620-P000625','Algebraic curves and commuting ordinary differential operators',
     r"""Krichever passes from coefficient equations for commuting scalar operators to their algebraic spectral curve, then reverses the construction using a normalized Baker--Akhiezer function. The report includes the polynomial-relation theorem attributed to Shabat, pole-order gaps, a genus criterion, a centralizer intervention, and a theta formula. Several distinctions matter: algebraic dependence was known earlier; rank-one spectral data are required for the scalar eigenfunction construction; a pole divisor is a bound rather than an exact divisor at every \(x\); and the claimed algebraic independence and final theta normalization contain errors. The notebook's date is retained even though Krichever's 1977 retrospective mentions related seminar talks in November--December 1975.""")
item(374,'P000621','method','Coefficient recursion for a commuting operator',
     r"""Expanding \([L_n,L_m]=0\) gives coefficient equations. The first \(m-1\) equations express the \(v_i\) as differential polynomials in the \(u_i\), with integration constants; the first relation is \(v_{m-2}=(m/n)u_{n-2}+h_2\).""",
     r"""Work locally with scalar differential operators over a characteristic-zero differential field, with constant nonzero leading coefficients. After scaling, let
     \(L_n=D^n+\sum_{j=0}^{n-2}u_jD^j\), while \(L_m=D^m+cD^{m-1}+\sum_{j=0}^{m-2}v_jD^j\), with \(n,m\geq2\) and \(c\) constant. Equating the coefficient of \(D^{n+m-3}\) gives
     \(nv'_{m-2}-mu'_{n-2}=0\), hence the displayed relation. Recursive comparison determines the lower \(v_j\) as differential polynomials with constants; the remaining \(n-1\) equations constrain the \(u_j\). For \(n=2\) and odd \(m\), these are stationary higher-KdV equations.""",
     r"""The monic normalization and vanishing \(D^{n-1}\) coefficient are supplied. One common scalar gauge can remove that coefficient of \(L_n\); it need not simultaneously remove the constant \(D^{m-1}\) coefficient of an arbitrary commuting partner.""",
     r"""This elimination is part of the systematic formal-operator framework in \citet[Sections~8--12]{gelfanddikii1976fractional}; Krichever's normalization is explicit in \citet[Section~2.1]{krichever1977methods}. The subsequent algebraic-geometric solution is more than this coefficient count.""",
     cls='A',match='partial',area='Differential operators')
item(374,'P000621-P000622','theorem','Polynomial dependence of commuting scalar differential operators',
     r"""The theorem attributed to A. B. Shabat says \([L_n,L_m]=0\Rightarrow P(L_n,L_m)=0\). Its proof uses \(L_m\) on the solution space of \(L_ny=Ey\), but calls a polynomial of degree \(n+1\) the characteristic polynomial. Bernstein mentions an earlier polynomial-coefficient result without a title.""",
     r"""For commuting scalar ordinary differential operators of positive orders \(n,m\), with complex analytic germs as coefficients and nonvanishing leading coefficients, there is a nonzero \(P(E,w)\in\mathbb C[E,w]\) such that \(P(L_n,L_m)=0\). The solution space of \(L_ny=Ey\) has dimension \(n\). In its initial-jet basis, the induced matrix \(M(E)\) of \(L_m\) has entries polynomial in \(E\), by repeated substitution of the differential equation. Thus \(P(E,w)=\det(wI-M(E))\) has degree \(n\) in \(w\), and Cayley--Hamilton gives the operator identity. Coprimality of \(n,m\) is unnecessary.""",
     r"""\ours\ The condensed initial-jet argument reconstructs the proof read in Krichever's Theorem~2.1; the notebook's exponential asymptotic sketch is not needed. The degree \(n+1\) is corrected to \(n\). The untitled 1967 reference mentioned by Bernstein was not independently identified.""",
     r"""\citet[Theorem~1]{amitsur1958commutative} already yields algebraic dependence. The notebook proof is reproduced as \citet[Theorem~2.1]{krichever1977methods}; the Shabat attribution does not establish general priority.""",
     literal='false as written',match='partial',development='annotated',area='Differential operators')
item(374,'P000622','construction','The spectral curve and a normalized common eigenfunction',
     r"""The eigenvalues satisfy \(P(E,w)=0\), and a common eigenfunction normalized by \(\psi(x_0,P)=1\) is viewed as a function on the resulting algebraic curve.""",
     r"""Take an irreducible component of the joint spectral curve and, when necessary, its normalization. If the generic simultaneous eigenspace is one-dimensional, the eigenline can locally be normalized by evaluation at \(x_0\), away from points where that evaluation vanishes. This gives a common eigenfunction meromorphic in the spectral point off the distinguished point at infinity, with a fixed divisor bounding its finite poles. A commuting pair of coprime positive orders is a sufficient rank-one situation. Higher generic rank requires vector-bundle data and does not yield one scalar normalized eigenfunction carrying the full information.""",
     r"""Generic rank, normalization of a possibly singular affine curve, and the excluded normalization zeros are supplied. The scalar construction is not asserted for every commuting pair merely because a polynomial relation exists.""",
     r"""The rank-one and coprime-order argument is read in \citet[Section~2.2]{krichever1977methods}. It was developed in the speaker's 1976--1977 publications following these seminar reports.""",
     cls='A',match='partial',area='Algebraic geometry')
item(374,'P000622','theorem','Existence and uniqueness of the one-point Baker--Akhiezer function',
     r"""On a nonsingular algebraic curve \(X\) with marked \(P_0\), the notes prescribe an \(x\)-independent nonspecial divisor \(D\) of degree \(g\) and the expansion \(e^{k(x-x_0)}(1+\sum\xi_i(x)k^{-i})\). The local coordinate \(1/k\) is mistakenly said to be near \(x_0\).""",
     r"""Let \(X\) be a smooth compact complex curve of genus \(g\), \(P_\infty\in X\), \(z=k^{-1}\) a local coordinate there, and \(D\) a nonspecial effective divisor of degree \(g\), disjoint from \(P_\infty\). For \(x\) near \(x_0\), except possible exceptional parameter values, there is a unique function \(\psi(x,P)\), meromorphic on \(X\setminus\{P_\infty\}\) with poles bounded by \(D\), such that
     \[e^{-k(x-x_0)}\psi(x,P)=1+\sum_{j\geq1}\xi_j(x)k^{-j}\]
     is holomorphic at \(P_\infty\). At \(x=x_0\), nonspeciality and normalization give \(\psi=1\). For more general \(x\), the dependence may be meromorphic and the construction is used away from its parameter poles.""",
     r"""Compactness, disjointness and exceptional \(x\)-values are made explicit. The divisor bounds the poles: it cannot be the exact polar divisor for every \(x\), since \(\psi(x_0,\cdot)=1\).""",
     r"""The lemma is read in \citet[pp.~291--292]{krichever1976zakharov}. Receipt on 8 October 1975 and presentation on 24 October do not independently prove public availability before the notebook's 20 October report.""",
     cls='A',match='partial',area='Algebraic geometry')
item(374,'P000623','theorem','The function ring acts by commuting differential operators',
     r"""Every \(E\in\Lambda(X,P_0)\), meromorphic only at \(P_0\), is assigned a unique \(L_E\) with \(L_E\psi=E\psi\). Matching principal parts determines its coefficients, and \(E\mapsto L_E\) is a ring homomorphism.""",
     r"""For the smooth Baker--Akhiezer data of 1975-374.4, let \(A(X,P_\infty)\) be the ring of meromorphic functions with poles only at \(P_\infty\). For pole order \(n\geq2\), if
     \(E=c_nk^n+c_{n-1}k^{n-1}+c_{n-2}k^{n-2}+\cdots\), there is a unique scalar differential operator
     \(L_E=c_nD^n+c_{n-1}D^{n-1}+\sum_{j=0}^{n-2}u_j(x)D^j\)
     satisfying \(L_E\psi=E\psi\), with coefficients meromorphic in the allowed \(x\)-domain. For example,
     \(u_{n-2}=c_{n-2}-nc_n\xi'_1\).
     Constants act by \(L_E=c_0\); for pole order one the formula is \(L_E=c_1D+c_0\).
     The map is injective and obeys \(L_{E+F}=L_E+L_F\), \(L_{EF}=L_EL_F\); hence its image is commutative and order equals pole order for nonconstant \(E\).""",
     r"""After matching principal parts, the remainder has zero normalized leading term and the same allowed poles; Baker--Akhiezer uniqueness makes it vanish. The index bounds printed for \(u_i=Q(c_j,\xi_s^{(r)})\) cannot hold literally: already \(u_0\) for \(n=2\) depends on \(\xi'_1\).""",
     r"""The construction is read in \citet[pp.~291--292]{krichever1976zakharov}; the coefficient example and ring statement are explicit in \citet[Sections~1--2]{krichever1977methods}.""",
     cls='A',literal='false as written',match='partial',development='annotated',area='Differential operators')
item(374,'P000623','claim','Pole-order gaps and the genus sum',
     r"""Let \(n\) be the least positive pole order and \(s+\mu_sn\) an available order in residue class \(s\); then \(\sum_{s=1}^{n-1}\mu_s=g\).""",
     r"""For a smooth genus-\(g\) curve and marked point, let \(H\subset\mathbb Z_{\geq0}\) be its Weierstrass semigroup of allowable pole orders. If \(n\) is its least positive element and \(w_s=s+\mu_sn\) is the \emph{least} element of \(H\) congruent to \(s\pmod n\), then the gaps in this residue class are \(s,s+n,\ldots,s+(\mu_s-1)n\). The gap theorem gives exactly \(g\) gaps, so \(\sum_s\mu_s=g\). Merely choosing an arbitrary available order in each residue class would not give this equality.""",
     r"""\ours\ The residue-class count is supplied explicitly. Minimality in each residue class is essential and is restored. The same semigroup records orders of the operators from 1975-374.5.""",
     r"""This is the classical Riemann--Roch gap count applied to the function ring used in \citet[Section~2.2]{krichever1977methods}; the elementary residue-class count above explains the exact notebook formula.""",
     match='partial',area='Algebraic geometry')
item(374,'P000623','claim','The claimed algebraic independence is impossible',
     r"""At a point in general position the notes assert \(g\) algebraically independent commuting operators.""",
     r"""The function field of a curve has transcendence degree one. Therefore any two elements of the associated scalar differential-operator ring are algebraically dependent, and for \(g>1\) the asserted \(g\)-fold algebraic independence is impossible. At an ordinary point the gaps are \(1,\ldots,g\); one can instead choose algebra generators with pole orders \(g+1,\ldots,2g+1\), subject to algebraic relations. An alternative module description uses one pole-order-\(g+1\) function and a basis over its polynomial ring.""",
     r"""Algebra generators, module generators and algebraically independent elements are different notions. The notebook does not identify which of the first two was intended, so its numeral is not silently emended.""",
     r"""The contradiction already follows from \citet[Theorem~1]{amitsur1958commutative} and the polynomial dependence of 1975-374.2. The curve-ring construction supplies the corrected interpretation.""",
     literal='false as written',match='partial',development='annotated',area='Algebraic geometry')
item(374,'P000623-P000624','claim','A genus criterion requires more than a list of operator orders',
     r"""An operator is called algebraic of genus \(g\) if it arises from the curve construction. An equivalence is then asserted with the existence of commuting operators of orders \(s+\mu_sn\), where \(\sum\mu_s=g\); the proof of sufficiency is only a short sketch.""",
     r"""In the smooth rank-one construction, the least pole orders in each residue class provide the stated commuting partners and recover the genus by the gap count. In the reverse direction, a commutative ring of scalar operators gives a spectral curve and eigenfunction data. To identify it with the preceding smooth-curve construction one must control rank, the full ring rather than an arbitrary subalgebra, the compactification and possible singularities, and the divisor and normalization at infinity. A list of available orders is not itself this spectral data, and arbitrary nonminimal \(\mu_s\) do not determine genus.""",
     r"""This is a partial reconstruction of the claimed criterion. No exact if-and-only-if theorem with only the notebook's numerical hypotheses is asserted; in particular arithmetic and geometric genus cannot be silently interchanged in a singular case.""",
     r"""The relevant classification appears in \citet[Section~2.2, Theorem~2.2]{krichever1977methods}. It verifies the spectral-data framework, not the exact abbreviated numerical criterion here.""",
     cls='A',status='The rank-one spectral classification is established; the notebook’s bare genus criterion remains only partially reconstructed.',
     literal='not determinable',match='partial',verification='indirect',confidence='medium',area='Differential operators')
item(374,'P000624','theorem','Commutativity of the centralizer',
     r"""The report remarks that operators commuting with a pair commute with each other. A participant recorded as Limanov adds the polynomial-coefficient version: two operators commuting with a third commute mutually.""",
     r"""For scalar ordinary differential operators over a characteristic-zero differential field with algebraically closed constant field, the centralizer of a positive-order operator is commutative. Thus two operators commuting with such an operator commute with one another; a pair is unnecessary. The qualifier matters: if the third operator is merely a scalar constant, every operator commutes with it, and the conclusion is false. For example \(D\) and multiplication by \(x\) both commute with \(I\), but \([D,x]=1\).""",
     r"""The hypothesis of a positive-order operator is supplied, covering the adjacent \(L_n\) setting. The tentatively read surname is retained without identifying a particular person or a new polynomial-coefficient paper.""",
     r"""\citet[Theorem~1]{amitsur1958commutative} proves this stronger centralizer statement in 1958. The seminar intervention is expository in that setting.""",
     match='exact',area='Differential operators',speaker='I. M. Krichever; participant recorded as Limanov')
item(374,'P000624','construction','The normalized theta formula and its missing factors',
     r"""The final formula has an exponential \(\exp\int_{P_0}^{P}\omega\) without \(x\), a theta quotient shifted by \(Ux\), and a theta series whose factors of \(2\pi i\) are inconsistent with the normalized periods.""",
     r"""Choose holomorphic differentials with \(a\)-periods \(\delta_{ij}\), period matrix \(B\), and Abel map \(\mathcal A(P_\infty)=0\). Set
     \[\theta(z\mid B)=\sum_{m\in\mathbb Z^g}\exp(\pi i\,m^TBm+2\pi i\,m^Tz),\qquad \operatorname{Im}B>0.\]
     Let \(d\Omega\) have zero \(a\)-periods, only a double pole at \(P_\infty\), and principal part \(dk=-dz/z^2\); normalize its regularized integral by \(\Omega(P)=k+O(k^{-1})\). Put \(U_j=(2\pi i)^{-1}\int_{b_j}d\Omega\), and choose \(Z\) so that \(\theta(\mathcal A(P)+Z)\) has zero divisor \(D\). With \(t=x-x_0\), on the set where the denominator is nonzero,
     \[\psi(x,P)=e^{t\Omega(P)}
       \frac{\theta(\mathcal A(P)+tU+Z)\,\theta(Z)}
       {\theta(\mathcal A(P)+Z)\,\theta(tU+Z)}.\]
     This has the required normalized exponential expansion and \(\psi(x_0,P)=1\).""",
     r"""The parameter factor in the exponential, the normalization factor depending only on \(x\), the regularization at the pole, the sign of the second-kind principal part, and the consistent theta convention are all supplied explicitly. They cannot be recovered by treating an integral starting at its double pole as an ordinary convergent integral.""",
     r"""The theta construction and normalization at the marked point are read in \citet[Section~1, pp.~189--190]{krichever1977methods}; the notebook has omitted essential factors.""",
     cls='A',literal='false as written',match='partial',development='annotated',area='Algebraic geometry')
corr('P000621','leading coefficients of L_m','u_m and u_(m-1) are constant','v_m and v_(m-1) are constant.','Scan and both transcriptions use u after defining the second operator with coefficients v; this is a notebook variable slip.')
corr('P000622','characteristic polynomial degree','L_m to the n+1 plus r_n L_m to the n','An n-dimensional solution space has characteristic polynomial of degree n.','Scan confirms n+1. Krichever1977 Theorem2.1 uses the n by n initial-jet matrix.')
corr('P000622','local-coordinate point','1/k is a local parameter near x_0','1/k is a local parameter near P_0 (the marked point of the curve).','The scan says x_0 at right but P_0 under the expansion; x_0 is the independent-variable basepoint.')
corr('P000623','coefficient dependence bounds','u_i depends on xi_s with 0<=s<=i-1','The displayed bounds are incorrect; for n=2, u_0=c_0-2c_2 xi_1 prime.','Scan confirms these indices. Direct matching of the normalized exponential expansion, also Krichever1977 Section1, yields the counterexample.')
corr('P000623','gap numbers','Some pole order s+mu_s n in each residue class','The least available pole order in each residue class.','Without minimality the sum of mu_s is not the genus; the scan omits the qualifier.')
corr('P000623','generic-point operator count','g algebraically independent commuting operators','Retain the error; a curve ring has transcendence degree one. Algebra or module generators would be different assertions.','The scan clearly says algebraically independent. The earlier polynomial-relation theorem already contradicts the wording for g>1.')
corr('P000624','common centralizer','Two operators commuting with a third commute mutually','Require a suitable non-scalar operator; the positive-order scalar-ODE hypothesis suffices.','The scan has no qualifier; taking the third operator to be the identity gives an immediate counterexample.')
corr('P000624','Baker--Akhiezer exponential','Exponential of the integral without x','Use exp((x-x_0) Omega(P)) with a regularized second-kind integral and normalization factor.','Scan confirms the missing x. The P000622 required local asymptotic cannot hold otherwise.')
corr('P000624','theta-series normalization','2 pi i multiplying the quadratic term with an unscaled linear term','For a-periods1 use pi i m transpose B m +2 pi i m transpose z.','Scan inspected; the crossing after2 pi i leaves a damaged coefficient, and the final linear term lacks its needed factor.',type='ambiguity')
corr('P000621-P000624','retrospective dating','Notebook date20October1975','Retain20October; record the discrepancy with the1977 survey’s retrospective November--December1975 account.','The notebook date is explicit and applies to both headings. Krichever1977 introduction p186 gives the later recollection.',type='provenance')
checkpoint()
