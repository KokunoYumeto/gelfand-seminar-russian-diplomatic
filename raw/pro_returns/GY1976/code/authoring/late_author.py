#!/usr/bin/env python3
"""Author the late records; all prose and mathematics are editorial input."""
from pathlib import Path
import csv
import json
from collections import Counter
ROOT=Path(__file__).resolve().parents[1]
WORK=ROOT/'work'
talks,items,problems,corrections=[],[],[],[]
def talk(record,date,speaker,pages,title,summary,kind='talk',**extra):
    talks.append(dict(record=record,date=date,speaker=speaker,pages=pages,title=title,kind=kind,summary=summary,**extra))
def item(record,pages,kind,title,notes,statement,reconstruction='',cls='E',fate='',status='',literal='correct with missing hypotheses',match='exact',verification='read the result',development='none',problem='',worth='',refs=(),confidence='high',**extra):
    number=sum(x['record']==record for x in items)+1
    items.append(dict(id=f'1976-{record}.{number}',record=record,pages=pages,kind=kind,title=title,notes=notes,statement=statement,reconstruction=reconstruction,**{'class':cls},fate=fate,present_status='As of November 2026: '+status,literal_correctness=literal,publication_match=match,verification=verification,development=development,problem=problem,worth=worth,refs=list(refs),confidence=confidence,**extra))
    return items[-1]['id']
CORRECTION_LATEX_OVERRIDES = {('P000686', 'graph notation'): {'transcription_reads': '\\(\\varphi(t)=\\operatorname{graph}\\varphi(t)\\)',
                                 'should_read': '\\(\\varphi(t)=\\operatorname{graph}\\Phi(t)\\)'},
 ('P000686', 'symmetric-form equivalence'): {'transcription_reads': '\\(\\sigma=0\\text{ on }\\Gamma\\)',
                                             'should_read': '\\(\\sigma=0\\text{ on '
                                                            '}\\operatorname{graph}\\Gamma\\)'},
 ('P000688-P000689', 'individual trace terms'): {'transcription_reads': '\\(\\int_X\\varphi(x\\gamma '
                                                                        'x^{-1})\\,dx\\)'},
 ('P000688', 'half-sum of roots'): {'transcription_reads': '\\(\\rho=\\frac12\\sum\\text{positive roots}\\)',
                                    'should_read': '\\(\\rho=\\frac12\\sum_{\\alpha>0}m_\\alpha\\alpha\\)'},
 ('P000689', 'final remainder'): {'transcription_reads': '\\(O(R^{n-r-1})\\)',
                                  'should_read': 'Retain the uncertain symbol; the matched general theorem '
                                                 'has \\(O(R^{n-1})\\).'},
 ('P000690', 'Zakharov--Shabat equation'): {'transcription_reads': '\\(L_t+P_y=[P,L]\\)',
                                            'should_read': '\\(L_t-P_y=[P,L]\\)'},
 ('P000691', 'node parameters in real case'): {'transcription_reads': '\\(\\alpha_i,\\beta_i\\in k\\); '
                                                                      '\\(\\alpha_i=\\overline{\\beta_i}\\) '
                                                                      'for \\(k=\\mathbb R\\)',
                                               'should_read': 'Use complexified parameters for real descent '
                                                              'and require all \\(2N\\) points distinct.',
                                               'evidence': 'Real distinct conjugate pairs cannot both lie in '
                                                           '\\(\\mathbb R\\); Manin III.5.1 explicitly '
                                                           'chooses complex node parameters.'},
 ('P000692', 'filtration shift'): {'transcription_reads': '\\(M_i=M_{(i-rN)}\\)',
                                   'should_read': '\\(M_i=M_{(i+rN)}\\quad(M_0=0,\\ \\mathbf1\\in M_1)\\)',
                                   'evidence': 'Actual PNG has minus. The preceding vanishing lemma forces a '
                                               'positive shift; Manin III.5.5 uses \\(+rN+1\\) with '
                                               'generator in \\(M_0\\).'},
 ('P000692', 'generator coefficient equation'): {'transcription_reads': '\\(\\sum_j(\\alpha_i^jE_r-\\beta_i^jg_i)m_i\\)',
                                                 'should_read': '\\(\\sum_j(\\alpha_i^jE_r-\\beta_i^jg_i)m_j\\)',
                                                 'evidence': 'Actual PNG and Russian have \\(m_i\\); '
                                                             'substitution of the displayed polynomial '
                                                             'forces \\(m_j\\).'},
 ('P000692', 'endomorphism ring'): {'transcription_reads': '\\(M_r(\\mathcal '
                                                           'B[\\lambda])=\\operatorname{End}_{\\mathcal '
                                                           'B}(N)\\)',
                                    'should_read': '\\(M_r(\\mathcal '
                                                   'B[\\lambda])=\\operatorname{End}_{\\mathcal '
                                                   'B[\\lambda]}(N)\\)'},
 ('P000692', 'flatness equation'): {'transcription_reads': '\\(\\partial_xd_t-\\partial_td_x=[d_x,d_t]\\)',
                                    'should_read': '\\(\\partial_xd_t-\\partial_td_x=-[d_x,d_t]\\)',
                                    'evidence': 'Scan has no minus; expansion of '
                                                '\\([\\partial_x+d_x,\\partial_t+d_t]\\) fixes the sign.'},
 ('P000693', 'left time exponential'): {'transcription_reads': '\\[\\begin{aligned}g_i(x)&=e^{-xd_x(\\alpha_i)+td_t(\\alpha_i)}g_i(0,0)\\\\&\\qquad{}\\times '
                                                               'e^{xd_x(\\beta_i)+td_t(\\beta_i)}.\\end{aligned}\\]',
                                        'should_read': '\\[\\begin{aligned}g_i(x,t)&=e^{-xd_x(\\alpha_i)-td_t(\\alpha_i)}g_i(0,0)\\\\&\\qquad{}\\times '
                                                       'e^{xd_x(\\beta_i)+td_t(\\beta_i)}.\\end{aligned}\\]'},
 ('P000695', 'determinantal coorientation'): {'transcription_reads': '\\(Z\\subset\\operatorname{Hom}(\\mathbb '
                                                                     'R^m,\\mathbb R^n)\\) has canonical '
                                                                     'coorientation',
                                              'evidence': 'Arbitrary real determinantal strata need not be '
                                                          'coorientable; here the normal space is '
                                                          '\\(\\operatorname{Hom}(\\ker '
                                                          'A,\\operatorname{coker}A)\\), with both factors '
                                                          'of dimension two.'},
 ('P000700', 'hook length'): {'evidence': 'The displayed hook formula requires '
                                          '\\(h=\\text{arm}+\\text{leg}+1\\); otherwise a removable cell '
                                          'would have length zero.'},
 ('P000700', 'branching sentence'): {'transcription_reads': 'Every irreducible of \\(S_{n-1}\\) occurs '
                                                            'once.'},
 ('P000700', 'regular representation'): {'transcription_reads': 'Functions on \\(S^n\\)',
                                         'should_read': 'Functions on \\(S_n\\)',
                                         'evidence': 'Context is the finite symmetric group and its regular '
                                                     'representation of dimension \\(n!\\).'},
 ('P000701', 'rotated coordinates'): {'transcription_reads': '\\(X=(x+y)/2;\\quad Y=(x-y)/2\\)',
                                      'should_read': '\\(X=(x-y)/2;\\quad Y=(x+y)/2\\), for the stated graph '
                                                     'normalization.'},
 ('P000701', 'limit-shape formula'): {'should_read': 'Add \\(\\Omega(X)=|X|\\) for \\(|X|>1\\).',
                                      'evidence': 'The real square root is defined only on \\([-1,1]\\); the '
                                                  '1977 paper gives both branches.'},
 ('P000701', 'subsequence definition'): {'transcription_reads': '\\(i_1<\\cdots<i_n\\) inside a maximum over '
                                                                '\\(r\\)',
                                         'should_read': '\\(i_1<\\cdots<i_r\\)',
                                         'evidence': 'The scan confirms \\(n\\); \\(r\\) is the length being '
                                                     'maximized.'},
 ('P000702', 'packet dimension in GL(n)'): {'transcription_reads': '\\((n^2-1)(g-1)\\)',
                                            'should_read': '\\(n^2(g-1)+1\\); the displayed value is for a '
                                                           'fixed determinant connection.',
                                            'evidence': 'Connections on a stable degree-zero bundle form a '
                                                        'torsor for \\(H^0(X,\\operatorname{End}(E)\\otimes '
                                                        'K_X)\\); Riemann--Roch. Rank one gives \\(g\\), not '
                                                        'zero.'},
 ('P000703', 'section notation'): {'transcription_reads': '\\(f_i\\) on \\(U_j\\)',
                                   'should_read': '\\(f_i\\) on \\(U_i\\)',
                                   'evidence': 'The cocycle equation and local restriction \\(df_i/f_i\\) on '
                                               '\\(U_i\\) fix the index; the handwritten subscript is '
                                               'ambiguous.'},
 ('P000704', 'bottom monodromy diagram'): {'should_read': '\\(f(g(u))=\\rho(g)(f(u))\\)'}}
def correction(page,place,reads,should,evidence,applies='both',typ='faithful_error'):
    entry=dict(page=page,place=place,transcription_reads=reads,should_read=should,evidence=evidence,applies_to=applies,type=typ)
    entry.update(CORRECTION_LATEX_OVERRIDES.get((page,place),{}))
    corrections.append(entry)
def problem(pid,title,statement,occurrences,status,refs):
    problems.append(dict(id=pid,title=title,statement=statement,occurrences=occurrences,status=status,status_date='2026-11',refs=refs))
def checkpoint():
    for name,data in [('talks',talks),('items',items),('problems',problems)]:
        (WORK/f'late_{name}.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    with (WORK/'late_corrections.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=['page','place','transcription_reads','should_read','evidence','applies_to','type'])
        w.writeheader();w.writerows(corrections)
MORSE=['duistermaat1974morse']
DKV=['duistermaatkolkvaradarajan1979spectra']
MANIN=['manin1978algebraic']
TYURIN=['tyurin1978periods']

talk(411,'1977-02-21','J. J. Duistermaat','P000685-P000689','Morse indices, Lagrangian intersections, and the spherical trace formula',
 r'''The first part explains the finite Morse index of a regular variational problem with general endpoint constraints through a path of Lagrangian subspaces. The general-boundary theory was publicly presented in May 1974. The second part passes from spherical convolution to a distributional Selberg formula and joint spectral asymptotics; its identifiable continuation is the 1979 paper with Kolk and Varadarajan. The notebook suppresses transversality and normalization conventions, indexes orbital terms by elements rather than conjugacy classes, and ends with a remainder exponent not supported by the matched theorem. These are assessed separately.''')

item(411,'P000685','definition','Variational problem with a submanifold of endpoint pairs',
 r'''The action is \(I(\gamma)=\int_0^T f(\gamma,\dot\gamma)\,dt\), with \((\gamma(0),\gamma(T))\in R\subset\mathbb R^n\times\mathbb R^n\). Fixed endpoints and the diagonal \(R\) are examples.''',
 r'''Let \(R\) be smooth and \(f\) be \(C^2\) near a smooth critical path. Allowed variations satisfy \((v(0),v(T))\in T_{(\gamma(0),\gamma(T))}R\). Stationarity consists of the Euler--Lagrange equation and \((-p(0),p(T))\in N^*R\), where \(p=f_{\dot\gamma}\).''',
 r'''The momentum condition and regularity assumptions are additions. An arbitrary smooth Lagrangian need not define a \(C^2\) action on all of \(H^1\); the Hessian along the smooth path is used here.''',
 fate=r'''The setup appears in \citet[\S1]{duistermaat1974morse}.''',status='this is standard regular variational calculus.',refs=MORSE)

item(411,'P000685','theorem','Positive Legendre condition gives a finite Morse index',
 r'''Positivity of \(f_{\dot\gamma\dot\gamma}\) is said to make the number of negative squares finite.''',
 r'''On a compact time interval, suppose \(A(t)=f_{\dot\gamma\dot\gamma}(\gamma(t),\dot\gamma(t))\) is continuous and positive definite. The second variation on the closed \(H^1\) space of admissible endpoint variations, including the boundary term from \(R\), has finite negative index.''',
 r'''Compactness makes the Legendre bound uniform. Lower-order terms and endpoint traces are compact relative to the positive derivative form after adding an \(L^2\) term.''',
 fate=r'''See \citet[\S1]{duistermaat1974morse}.''',status='the assertion is valid under these hypotheses.',refs=MORSE)

item(411,'P000686','construction','Legendre transform and the symplectic variational flow',
 r'''Euler--Lagrange equations become Hamilton equations; \(\Phi(t)\) is the derivative of the flow along the extremal.''',
 r'''An invertible velocity Hessian gives the local Legendre transform \(p=f_v(q,v)\), \(H(q,p)=p\cdot v-f(q,v)\). In a symplectic trivialization along the extremal, the linearized flow satisfies \(\Phi(0)=1\) and \(\Phi(t)^*\sigma=\sigma\).''',
 r'''Only local invertibility is needed.''',fate=r'''See \citet[\S1]{duistermaat1974morse}.''',status='the Hamiltonian reduction is established.',refs=MORSE)

item(411,'P000686','construction','Graphs of symplectic maps as Lagrangian planes',
 r'''The page writes \(\varphi(t)=\operatorname{graph}\varphi(t)\) and says that \(\sigma\oplus(-\sigma)\) vanishes on the graph.''',
 r'''For symplectic \(V\) of dimension \(2n\), \(\Lambda(t)=\{(v,\Phi(t)v):v\in V\}\) is Lagrangian in \((V\oplus V,\sigma\oplus(-\sigma))\) exactly when \(\Phi(t)\) is symplectic.''',
 r'''Upper-case \(\Phi\) is the map and \(\Lambda\) the subspace.''',fate=r'''See \citet[\S\S1--3]{duistermaat1974morse}.''',status='the equivalence is elementary and exact.',literal='correct',refs=MORSE)

item(411,'P000686','construction','Symmetric-form chart on the Lagrangian Grassmannian',
 r'''For \(\alpha\cap\beta=0\) and \(\gamma\cap\beta=0\), write \(\gamma=\operatorname{graph}\Gamma\), \(\Gamma:\alpha\to\beta\), and \(Q(u,v)=\sigma(\Gamma u,v)\).''',
 r'''Relative to \(V=\alpha\oplus\beta\), every plane transverse to \(\beta\) is such a graph. It is Lagrangian exactly when \(Q\) is symmetric, and \(\gamma\cap\alpha=\ker Q\) under the graph identification.''',
 r'''The phrase that \(\sigma\) vanishes on \(\Gamma\) means on its graph.''',fate=r'''See \citet[\S2]{duistermaat1974morse}.''',status='the coordinate description is standard.',refs=MORSE)

item(411,'P000686-P000687','construction','Maslov crossings and independence of the auxiliary complement',
 r'''At a simple crossing \(\gamma(t)\cap\alpha\ne0\), take the jump of the quadratic-form index; it does not depend on the transverse \(\beta\).''',
 r'''For a Lagrangian path with endpoints transverse to \(\alpha\), signed regular crossings of \(\Sigma_\alpha=\{\Lambda:\Lambda\cap\alpha\ne0\}\) define an integer. Symmetric-form charts give compatible local counts; homotopies with fixed transverse endpoints preserve the integer.''',
 r'''Perturbation defines nonregular crossings. A symplectic sign convention fixes the sign.''',fate=r'''See \citet[\S2]{duistermaat1974morse}.''',status='the Maslov index is established; endpoint conventions remain essential.',refs=MORSE)

item(411,'P000687','claim','Topology of the Lagrangian Grassmannian and the singular Maslov cycle',
 r'''The notes call \(\Sigma_\alpha\) an embedded two-sided hypersurface and infer \(\pi_1(\operatorname{Lag})=\mathbb Z\); its complement is identified with quadratic forms.''',
 r'''For \(N\geq1\), \(\operatorname{Lag}(\mathbb R^{2N})=U(N)/O(N)\) has fundamental group \(\mathbb Z\). Transverse planes form a contractible symmetric-matrix chart. The one-dimensional-intersection stratum is a cooriented smooth hypersurface; higher-intersection strata are singular when \(N\geq2\).''',
 r'''The whole cycle is not smooth. The complement description alone is not a proof of the fundamental group.''',fate=r'''Compare \citet[\S2]{duistermaat1974morse}.''',status='the topological conclusion is correct, but the literal smoothness assertion is not.',literal='false as written',match='partial',development='annotated',refs=MORSE)

item(411,'P000687','definition','Endpoint correction for an open Lagrangian path',
 r'''The proposed index is \([\gamma:\alpha]+\operatorname{ind}Q\{\gamma(T),\alpha,\gamma(0)\}\); in dimension one it is described by completing an arc on a circle.''',
 r'''An open-path Maslov index needs an endpoint normalization. For triples admitting the graph chart, a triple quadratic form measures the change of reference plane. The Hörmander identity supplies a reference-independent correction. Degenerate endpoints require a specified extension.''',
 r'''The notes define neither all nontransverse triple forms nor an unambiguous orientation of the circle completion.''',fate=r'''Compare \citet[\S2, formula (2.4)]{duistermaat1974morse}.''',status='the construction is known, but some notebook conventions are undetermined.',literal='not determinable',match='partial',development='annotated',refs=MORSE)

item(411,'P000687','construction','The conormal Lagrangian for a boundary condition',
 r'''The notes define \(R^\perp\) with reversal of the second momentum, write \(\rho=T(R^\perp)\), and call it a fibre of the normal bundle.''',
 r'''Under \((x,y;\xi,\eta)\mapsto(x,\xi;y,-\eta)\), \(N^*R\) is Lagrangian in the doubled phase space. Its tangent at the endpoint covector is the required Lagrangian \(2n\)-plane \(\rho\).''',
 r'''This is a tangent to the total conormal bundle; a fibre has dimension \(2n-\dim R\).''',fate=r'''See \citet[\S1]{duistermaat1974morse}.''',status='the geometry is correct after the tangent/fibre distinction.',literal='false as written',match='partial',development='annotated',refs=MORSE)

item(411,'P000686-P000687','theorem','General-boundary Morse--Maslov index formula',
 r'''The equality is \(\operatorname{ind}_R\gamma=\operatorname{ind}(\varphi)+i(I,\rho,\varphi(T))+\dim\pi(\rho\cap I)-2n\), with \(i=(\operatorname{ind}+\operatorname{null})Q\).''',
 r'''Under regularity and the positive Legendre condition, the Morse index is computable from flow graphs, the boundary conormal Lagrangian, and endpoint forms. The fixed-endpoint specialization is \(\operatorname{ind}\gamma=\sum_{0<t<T}\dim\{J:J\text{ is Jacobi},\,J(0)=J(t)=0\}\), with endpoint nullity separate.''',
 r'''The general equality is retained as an announcement. Its absolute constant and triple-index convention cannot be recovered from the transverse-chart definition: \(\varphi(0)=I\), and \(\rho\cap I\) may be nonzero. The precise fixed-endpoint specialization is an editorial reconstruction.''',
 fate=r'''See \citet[\S3, formulas (3.1)--(3.4)]{duistermaat1974morse}.''',status='the general theorem is established; the exact notebook normalization is partially matched.',literal='not determinable',match='partial',development='annotated',refs=MORSE)
checkpoint()

item(411,'P000687-P000688','construction','Spherical convolution and kernels on a compact quotient',
 r'''For \(X=K\backslash G/\Gamma\), the kernel is \(K_\varphi(x,y)=\sum_{\gamma\in\Gamma}\varphi(x\gamma y^{-1})\), with bi-\(K\)-invariant \(\varphi\).''',
 r'''Let \(G\) be connected semisimple with finite centre, \(K\) maximal compact, and \(\Gamma\) torsion-free cocompact. For \(\varphi\in C_c^\infty(K\backslash G/K)\), the locally finite kernel is smooth on \(X\times X\), hence trace class. Invariant differential operators arise from suitable distributions supported at the identity coset.''',
 r'''Torsion-freeness makes \(X\) a manifold. In the bi-\(K\)-invariant realization on \(G\), identity-coset support means support on \(K\).''',
 fate=r'''The setup is reviewed in \citet[\S\S2--3]{duistermaatkolkvaradarajan1979spectra}.''',status='the compact-quotient construction is established.',refs=DKV)

item(411,'P000688','theorem','Commuting spherical operators and a common eigenbasis',
 r'''The spherical convolution algebra is commutative with involution; its compact operators have common orthonormal eigenvectors \(e_j\).''',
 r'''For the Riemannian symmetric pair \((G,K)\), bi-\(K\)-invariant convolution is commutative. On compact \(X\), spherical smoothing operators and an invariant elliptic Laplacian have a complete orthonormal simultaneous eigenbasis. Eigenvalue functionals are multiplicative characters.''',
 r'''An elliptic operator or approximate identity supplies completeness; compactness alone would leave a possible common kernel.''',
 fate=r'''See \citet[\S3]{duistermaatkolkvaradarjan1979spectra}.'''.replace('varadarjan','varadarajan'),status='the joint decomposition is standard.',refs=DKV)

item(411,'P000688-P000689','theorem','Trace formula and the grouping into conjugacy classes',
 r'''The notes equate \(\sum_j\lambda_j(\varphi)\), the diagonal integral, and a sum of individual \(\int_X\varphi(x\gamma x^{-1})\,dx\).''',
 r'''The trace is the diagonal integral. Its geometric expansion is a sum over \(\Gamma\)-conjugacy classes with centralizer-volume factors and orbital integrals. An individual \(\varphi(x\gamma x^{-1})\) generally does not descend to \(X\); an ungrouped sum can be integrated over a specified fundamental domain.''',
 r'''Class regrouping repairs the quotient-invariance gap. One can instead integrate over a specified fundamental domain, but the notes do not say so.''',
 fate=r'''The normalized side is in \citet[Theorem 5.1]{duistermaatkolkvaradarajan1979spectra}.''',status='the trace identity is established with this interpretation.',literal='false as written',match='partial',development='annotated',refs=DKV)

item(411,'P000688','construction','Abel transform and the Euclidean spherical transform',
 r'''The map is \(f(a)=e^{\langle\rho,a\rangle}\int_N\varphi(an)\,dn\); the margin calls \(A\) a vector space.''',
 r'''Use \(G=KAN\), write \(a=\exp H\), and put \(\rho=\tfrac12\sum_{\alpha>0}m_\alpha\alpha\). With compatible Haar measures, \(\mathcal A\varphi(H)=e^{\rho(H)}\int_N\varphi(\exp H\,n)\,dn\) identifies spherical convolution with convolution on \(C_c^\infty(\mathfrak a)^W\).''',
 r'''Restricted-root multiplicities and exponential coordinates are additions.''',
 fate=r'''See \citet[\S\S2--3]{duistermaatkolkvaradarajan1979spectra}.''',status='this is classical, with measure-dependent normalization.',refs=DKV)

item(411,'P000688-P000689','definition','Joint spectral parameters and multiplicities',
 r'''Multiplicativity gives \(\lambda_j(\varphi)=\widetilde f(\mu_j)\), with \(\mu_j\in A_\mathbb C^*\); these form the spectrum.''',
 r'''A spherical eigencharacter is evaluation at a parameter in \(\mathfrak a_\mathbb C^*/W\). Joint eigenspaces are counted with dimension. Representatives before the Weyl quotient are noncanonical, and nonprincipal parameters need not lie on the real spectral axis.''',
 r'''Multiplicities and the Weyl quotient are needed for the counting formula.''',
 fate=r'''See \citet[\S3]{duistermaatkolkvaradarajan1979spectra}.''',status='the parametrization is established.',refs=DKV)

item(411,'P000689','theorem','Poisson form of the spherical trace identity',
 r'''The trace becomes \(\sum_j\widetilde f(\mu_j)=\sum_\gamma\langle T_\gamma,f\rangle\), for a locally finite family.''',
 r'''For compact \(X\), the joint spectral distribution is a sum of \(W\)-invariant distributions indexed by conjugacy classes, with centralizer-volume weights. Nonidentity terms avoid a common neighbourhood of zero. The identity term is quotient volume times the Fourier transform of spherical Plancherel measure, with fixed Haar normalization.''',
 r'''Weights and normalization are supplied from the paper.''',cls='A',
 fate=r'''See \citet[Theorem 5.1]{duistermaatkolkvaradarajan1979spectra}, received July 1978 and published 1979.''',status='the distributional formula is proved.',refs=DKV)

item(411,'P000689','claim','Closed-geodesic length and support of the geometric distribution',
 r'''The boxed assertion reads \(\ell(\gamma)=\operatorname{dist}(\operatorname{supp}T_\gamma,0)\).''',
 r'''For nontrivial \(c\), the matched theorem places \(\operatorname{supp}T_c\) in a Weyl union of affine subspaces at distance equal to the minimal translation length \(\ell(c)\). For real regular Iwasawa classes, including rank one, \(T_c\) is a nonzero sum of Dirac masses on that Weyl orbit, giving equality of distances.''',
 r'''A general support inclusion gives a lower bound, not itself equality. Equality is verified here in the explicit regular case.''',cls='A',
 fate=r'''See \citet[Theorems 5.1--5.2 and Proposition 5.15]{duistermaatkolkvaradarajan1979spectra}.''',status='the regular case is established; the universal equality is partially verified.',literal='not determinable',match='partial',development='annotated',refs=DKV)

item(411,'P000689','claim','Joint Weyl law and the unsupported remainder exponent',
 r'''The last line gives a ball count with main term \(\operatorname{vol}(X)\int_{\operatorname{ball}(R)}\beta\) and \(O(R^{n-r-1})\); the middle exponent letter is uncertain.''',
 r'''For bounded open principal spectral \(\Omega\) with smooth boundary, the matched result is \(\sum_{\lambda\in R\Omega}m(\lambda)=c_G\operatorname{vol}(X)\int_{R\Omega}\beta+O(R^{n-1})\), \(n=\dim X\). Complementary parameters are separately controlled; rank one gives \(O(R^{n-1}/\log R)\).''',
 r'''These are verified conclusions, not a claim that the extra exponent symbol is absent from the scan.''',cls='A',
 fate=r'''See \citet[Theorems 8.8--8.9 and 9.1]{duistermaatkolkvaradarajan1979spectra}.''',status='the classical bounds are established; the stronger exponent was not verified.',literal='not determinable',match='partial',development='annotated',refs=DKV)

correction('P000686','graph notation',r'\varphi(t)=\operatorname{graph}\varphi(t)',r'\varphi(t)=\operatorname{graph}\Phi(t)',
 'The scan defines capital Phi as the flow derivative; map and graph need distinct symbols.',typ='ambiguity')
correction('P000686','symmetric-form equivalence',r'\sigma=0\text{ on }\Gamma',r'\sigma=0\text{ on }\operatorname{graph}\Gamma',
 'A two-form restricts to the graph, not to the linear map.')
correction('P000687','Maslov cycle','Sigma is embedded and two-sided',
 'The one-dimensional-intersection stratum is a smooth cooriented hypersurface.',
 'Higher-intersection strata are singular; faithful mathematical shorthand.')
correction('P000687','rho','tangent to R-perp; fibre of the normal bundle',
 'Tangent to the total conormal bundle at the endpoint covector.',
 'The scan writes T(R-perp); the fibre generally has another dimension.')
correction('P000688-P000689','individual trace terms',r'\int_X\varphi(x\gamma x^{-1})\,dx',
 'Regroup by conjugacy classes or specify a fundamental domain.',
 'An individual term is not Gamma-invariant; DKV1979 section5 gives the grouped formula.')
correction('P000688','half-sum of roots',r'\rho=\frac12\sum\text{positive roots}',r'\rho=\frac12\sum_{\alpha>0}m_\alpha\alpha',
 'Restricted-root multiplicities are needed in general.')
correction('P000689','final remainder',r'O(R^{n-r-1})',
 'Retain the uncertain symbol; the matched general theorem has O(R^{n-1}).',
 'PNG inspected; DKV1979 Theorem8.8 verifies the weaker estimate.',typ='ambiguity')
checkpoint()

talk(412,'1977-02-28','Yu. I. Manin','P000690-P000693',
 'Filtered bimodules, nodal spectral curves, and soliton equations',
 r'''This continuation recapitulates the bimodule reconstruction of commuting operators, Lax evolutions, and zero-curvature equations, then constructs the modules explicitly on an affine line with pairs of points identified. The block interpolation matrix, filtration, connection matrices, and operator orders closely match Chapter III, sections 2 and 5, of Manin's 1978 Russian exposition (English translation 1979). Several signs and indices in the notebook are demonstrably inconsistent with that construction. The final question about the behaviour of an \(N\)-soliton solution specifies neither an equation nor a limiting regime; it is retained without manufacturing a new open problem.''')

item(412,'P000690','definition','Matrix differential-operator algebra and three compatibility equations',
 r'''The coefficients are \(\mathcal B=M_\ell(\mathcal B_0)\), where \(\mathcal B_0\) consists of meromorphic germs in \(x\), \(x,t\), or \(x,t,y\). The targets are \([L,P]=0\), \(L_t=[P,L]\), and a displayed Zakharov--Shabat equation.''',
 r'''Form the Ore algebra \(\mathcal B[\partial_x]\) with \(\partial_x b=b\partial_x+\partial_x(b)\). The stationary equation is commutation; the Lax equation is compatibility of \(L\psi=\lambda\psi\) and \(\psi_t=P\psi\). Two evolution equations \(\psi_y=L\psi\), \(\psi_t=P\psi\) have compatibility \(L_t-P_y=[P,L]\).''',
 r'''Commutators mean \([A,B]=AB-BA\). The sign correction is justified again in the dedicated zero-curvature item.''',
 fate=r'''The framework is summarized in \citet[Ch.~III, \S2]{manin1978algebraic}.''',
 status='these operator equations are standard.',refs=MANIN)

item(412,'P000690','construction','Filtered bimodule data and the omitted generation axioms',
 r'''The notes specify a \((\mathcal B,\mathcal O)\)-bimodule \(M\), a filtration, a distinguished \(\mathbf1\), and \(\nabla(bm)=b_xm+b\nabla m\), referring backwards for further axioms.''',
 r'''A sufficient precise version is an exhaustive filtration \(M_0=0\subset M_1\subset\cdots\), \(M_1=\mathcal B\mathbf1\), with each quotient free of rank one, and \(\nabla M_i\subset M_{i+1}\) inducing isomorphisms on consecutive quotients. The right action of the commutative algebra \(\mathcal O\) commutes with \(\nabla\) and the left \(\mathcal B\)-action, and is faithful.''',
 r'''These are the generation and commutation hypotheses needed below, supplied from the referenced earlier axioms and the matched exposition. The notebook alone does not repeat them.''',cls='A',
 fate=r'''See \citet[Ch.~III, \S2.2]{manin1978algebraic}, Russian original 1978, English 1979.''',
 status='the reconstruction data are established.',refs=MANIN)

item(412,'P000690','theorem','A free cyclic differential module produces commuting operators',
 r'''The lemma makes \(M\) a free rank-one \(\mathcal B[\partial_x]\)-module, with \(\partial_x\) acting as \(\nabla\); \(\mathbf1\varphi=L_\varphi\mathbf1\).''',
 r'''Under the preceding filtration axioms, \(\mathbf1,\nabla\mathbf1,\ldots,\nabla^{i-1}\mathbf1\) are a \(\mathcal B\)-basis of \(M_i\). Thus evaluation at \(\mathbf1\) identifies \(\mathcal B[\partial_x]\) with \(M\). Each right multiplication by \(\varphi\in\mathcal O\) determines \(L_\varphi\), and \(\varphi\mapsto L_\varphi\) is an injective algebra map; its image is commutative.''',
 r'''Faithfulness gives injectivity. This does not say that arbitrary operators commuting with one chosen \(L\) automatically form this algebra.''',cls='A',
 fate=r'''The precise reconstruction is \citet[Ch.~III, Theorem 2.4]{manin1978algebraic}.''',
 status='the cyclic-module theorem is proved.',refs=MANIN)

item(412,'P000690','theorem','A commuting time connection yields a Lax equation',
 r'''The notes add \(\nabla_t\), require \([\nabla_x,\nabla_t]=0\), and obtain \(L_t=[P,L]\).''',
 r'''Let \(\nabla_t\) extend \(\partial_t\), commute with \(\nabla_x\), and commute with the right \(\mathcal O\)-action. Define \(P\) by \(\nabla_t\mathbf1=P\mathbf1\). Then \(\partial_tL_\varphi=[P,L_\varphi]\).''',
 r'''Compatibility with the spectral-ring action is needed in addition to the displayed commutator.''',cls='A',
 fate=r'''See \citet[Ch.~III, Theorem 2.5]{manin1978algebraic}.''',
 status='the stated construction is established.',refs=MANIN)

item(412,'P000690-P000691','claim','Zero curvature and the sign in the Zakharov--Shabat equation',
 r'''The page has \(L_t+P_y=[P,L]\), while \(\nabla_t\mathbf1=P\mathbf1\), \(\nabla_y\mathbf1=L\mathbf1\), and the three connections commute.''',
 r'''With the displayed connection convention and \([A,B]=AB-BA\), the resulting identity is \(L_t-P_y=[P,L]\). Indeed \([\nabla_t-P,\nabla_y-L]\mathbf1=(-L_t+P_y+[P,L])\mathbf1=0\); cyclic freeness makes the operator vanish.''',
 r'''This is a mathematical emendation, not a claim that the scan has a minus. Independent visual inspection of the published English Theorem~2.6, p.~83, confirms a printed plus rather than an OCR artifact. Its connection conventions likewise require a difference; the notebook and publication both need a mathematical sign correction.''',cls='A',
 fate=r'''Compare \citet[Ch.~III, Theorem 2.6 and its proof]{manin1978algebraic}.''',
 status='zero curvature is established with the corrected sign.',
 literal='false as written',match='partial',development='annotated',refs=MANIN)

item(412,'P000691','construction','An affine nodal spectral curve by pairwise identification',
 r'''The ring is \(\mathcal O=\{f\in k[\lambda]:f(\alpha_i)=f(\beta_i),\,1\leq i\leq N\}\).''',
 r'''For \(2N\) pairwise distinct complex numbers \(\alpha_i,\beta_i\), this subring is the coordinate ring of the affine line with the \(N\) pairs identified as ordinary nodes. Its normalization is \(\mathbb A^1\). For a real model the node set and identifications must be invariant under conjugation.''',
 r'''Pairwise distinctness of all \(2N\) points is stronger than the notebook's explicitly written \(\alpha_i\ne\alpha_j\), and excludes unintended multiple identifications.''',cls='A',
 fate=r'''The exact construction is \citet[Ch.~III, \S5.1]{manin1978algebraic}.''',
 status='this spectral-curve construction is established.',refs=MANIN)

item(412,'P000691','construction','Gluing a trivial module over the normalization',
 r'''Inside \(N=\mathcal B[\lambda]^r\), the module is defined by \(m(\alpha_i)=g_i m(\beta_i)\); the left \(\mathcal B\)-action is componentwise right multiplication by \(b^t\).''',
 r'''Write the ambient module as \(\mathcal N=\mathcal B[\lambda]^r\) to distinguish it from the number of nodes. The left action \(b\cdot(m_j)=(m_jb^t)\) commutes with left block matrices \(g_i\in GL_r(\mathcal B_\mathbb C)\). The gluing equations define a left \(\mathcal B\), right \(\mathcal O\) sub-bimodule, the algebraic analogue of sections of a bundle with prescribed nodal gluing.''',
 r'''The transpose is essential for associativity of this left action; it is not a transcription error.''',cls='A',
 fate=r'''See \citet[Ch.~III, \S\S5.1--5.2]{manin1978algebraic}.''',
 status='the module model is established.',literal='correct',refs=MANIN)

item(412,'P000691','claim','Reality conditions at conjugate nodes',
 r'''For real \(k\), the notes put \(\alpha_i=\overline{\beta_i}\) and \(\overline{g_i}=g_i^{-1}\).''',
 r'''Work first over the complexification of the real coefficient algebra. At conjugate paired nodes, conjugating \(m(\alpha_i)=g_i m(\beta_i)\) gives the same condition precisely when \(\overline{g_i}g_i=1\). Taking the fixed real subspace then descends the module.''',
 r'''The points cannot all be required to lie in \(\mathbb R\) as well as to be distinct conjugate pairs. The scalar field in the initial point list must be complexified.''',cls='A',
 fate=r'''These conditions appear in \citet[Ch.~III, \S5.1]{manin1978algebraic}.''',
 status='the real descent condition is valid with complexified node parameters.',refs=MANIN)

item(412,'P000691','definition','The staircase filtration on polynomial columns',
 r'''In \(N_{ar+k}\), the first \(k\) components have degree at most \(a\), the remaining components degree at most \(a-1\), \(0\leq k<r\).''',
 r'''For \(a\geq0\), define \(\mathcal N_{ar+k}\) by those bounds, interpreting degree at most \(-1\) as zero. Then \(\mathcal N_0=0\), the filtration is exhaustive, and each successive quotient is a free left \(\mathcal B\)-module of rank one.''',
 r'''The boundary convention \(a=0\) is explicit; it matters for the later shift.''',cls='A',
 fate=r'''See \citet[Ch.~III, \S5.3]{manin1978algebraic}.''',
 status='the filtration is established.',literal='correct',refs=MANIN)

item(412,'P000691-P000692','theorem','The block interpolation matrix and nondegeneracy',
 r'''The block matrix has entries \(\alpha_i^j I_r-\beta_i^jg_i\), \(i=1,\ldots,N\), \(j=0,\ldots,N-1\); the notebook requires nonzero determinant.''',
 r'''Assume \(G=(\alpha_i^jI_r-\beta_i^jg_i)_{i,j}\) is invertible in \(M_{rN}(\mathcal B)\). If \(M_{(i)}=M\cap\mathcal N_i\), then \(M_{(rN)}=0\), and \(M_{(i)}/M_{(i-1)}\to\mathcal N_i/\mathcal N_{i-1}\) is an isomorphism for \(i>rN\).''',
 r'''Over a matrix coefficient algebra the clean condition is invertibility. A scalar determinant is taken only after expanding into matrices over the commutative coefficient ring and restricting to a locus where it is a unit.''',cls='A',
 fate=r'''See \citet[Ch.~III, \S5.4 and Lemma 5.5]{manin1978algebraic}.''',
 status='the interpolation lemma is proved.',refs=MANIN)

item(412,'P000692','claim','The sign and indexing of the filtration shift',
 r'''After \(M_{(rN)}=0\), the definition reads \(M_i=M_{(i-rN)}\), but the generator is then placed in \(M_1\).''',
 r'''With the notebook's one-based convention \(M_0=0\), \(M_1\) generated by \(\mathbf1\), the correct shift is \(M_i=M_{(i+rN)}\). With the paper's generator in \(M_0\), it is \(M_i=M_{(i+rN+1)}\).''',
 r'''The negative shift leaves the supposed first generator space zero and is incompatible with the preceding vanishing lemma. The one-unit difference between conventions must not be mistaken for another error.''',cls='A',
 fate=r'''Compare \citet[Ch.~III, Lemma 5.5]{manin1978algebraic}.''',
 status='the corrected positive shift is definite.',
 literal='false as written',match='partial',development='annotated',refs=MANIN)

item(412,'P000692','construction','Normalized cyclic vector from finite linear equations',
 r'''The normalized vector is \(\mathbf1=\sum_{j=0}^{N-1}m_j\lambda^j+\lambda^Ne_1\), with a displayed system using \(m_i\) inside the sum over \(j\).''',
 r'''Its coefficients uniquely solve \(\sum_{j=0}^{N-1}(\alpha_i^jI_r-\beta_i^jg_i)m_j=-(\alpha_i^NI_r-\beta_i^Ng_i)e_1\), \(1\leq i\leq N\), under invertibility of \(G\).''',
 r'''The summation coefficient must be \(m_j\), not the row-indexed \(m_i\).''',cls='A',
 fate=r'''The normalized vector is \citet[Ch.~III, \S5.6, equation (5)]{manin1978algebraic}.''',
 status='the finite linear construction is established.',
 literal='false as written',match='partial',development='annotated',refs=MANIN)

item(412,'P000692','theorem','Connection preserving the nodal gluing equations',
 r'''For \(\nabla_x=\partial_x+d_x(\lambda)\), the notes give \(\partial_xg_i=g_id_x(\beta_i)-d_x(\alpha_i)g_i\).''',
 r'''Let \(d_x\in M_r(\mathcal B[\lambda])\), acting on columns on the left. The displayed differential equations imply \(\nabla_xM\subset M\); differentiating the gluing relation proves this directly. Such matrices are \(\mathcal B[\lambda]\)-linear endomorphisms of the ambient module under the transpose action.''',
 r'''The notebook's equality with all \(\mathcal B\)-linear endomorphisms is too broad: commuting with multiplication by \(\lambda\) is additionally required.''',cls='A',
 fate=r'''This is \citet[Ch.~III, Lemma 5.8]{manin1978algebraic}.''',
 status='the preservation criterion is established.',refs=MANIN)

item(412,'P000692','construction','Explicit evolution of the gluing matrices',
 r'''For constant \(d_x(\lambda)\), \(g_i(x)=e^{-xd_x(\alpha_i)}g_i(0)e^{xd_x(\beta_i)}\).''',
 r'''If \(d_x\) is independent of \(x\), the displayed formula solves the gluing-preservation equation for every invertible initial \(g_i(0)\). Matrix exponentials are required even when \(r=1\) if the coefficient algebra has matrix size \(\ell>1\).''',
 r'''The marginal assertion that \(r=1\) gives ordinary scalar exponentials additionally requires \(\ell=1\), or scalar commuting coefficients.''',cls='A',
 fate=r'''See \citet[Ch.~III, \S5.9]{manin1978algebraic}.''',
 status='the explicit evolution is established.',refs=MANIN)

item(412,'P000692-P000693','claim','Flatness of the parameter connections and two-time exponential signs',
 r'''The notes write \(\partial_xd_t-\partial_td_x=[d_x,d_t]\), and later put \(+td_t(\alpha_i)\) in the left exponential as well as \(+td_t(\beta_i)\) on the right.''',
 r'''For \(\nabla_x=\partial_x+d_x\), \(\nabla_t=\partial_t+d_t\), flatness is \(\partial_xd_t-\partial_td_x+[d_x,d_t]=0\). For constant commuting matrices the compatible solution is \[g_i(x,t)=e^{-xd_x(\alpha_i)-td_t(\alpha_i)}g_i(0,0)e^{xd_x(\beta_i)+td_t(\beta_i)}.\]''',
 r'''Both signs follow by differentiation. Choosing \(d_t,d_y\) as scalar polynomials in \(d_x\) ensures commutation; arbitrary constants need not commute.''',cls='A',
 fate=r'''Compare \citet[Ch.~III, \S5.12, equations (9)--(10)]{manin1978algebraic}.''',
 status='the equations hold with these corrected signs.',
 literal='false as written',match='partial',development='annotated',refs=MANIN)

item(412,'P000693','theorem','Graded cyclicity and the order of a spectral operator',
 r'''The lemma \(\operatorname{ord}L_\varphi=r\deg\varphi\) ends with an unfinished condition. A matrix pattern and the example \(\begin{pmatrix}0&\lambda\\b&0\end{pmatrix}\) follow.''',
 r'''Assume \(\nabla_x\) increases filtration by one and is invertible on successive graded pieces. Multiplication by a polynomial \(\varphi\in\mathcal O\) of degree \(d\) raises the staircase filtration by exactly \(rd\), giving \(\operatorname{ord}L_\varphi=rd\). For \(r=2\), the displayed matrix has the required graded property when \(b\) is invertible.''',
 r'''The unfinished hypothesis is supplied from the adjacent graded-isomorphism condition, not guessed solely from the desired order. For general \(r\), a cyclic lower subdiagonal with invertible entries and an invertible \(\lambda\)-coefficient in the upper-right corner suffices.''',cls='A',
 fate=r'''See \citet[Ch.~III, Lemma 5.10 and \S\S5.11--5.13]{manin1978algebraic}.''',
 status='the conditional order formula is proved.',refs=MANIN)

item(412,'P000693','construction','A quadratic function on the nodal curve and an operator of order twice the rank',
 r'''If \(\alpha_i+\beta_i\) is independent of \(i\), there is \(\psi\in\mathcal O\) of degree two, hence an operator of order \(2r\).''',
 r'''If every pair is distinct and \(\alpha_i+\beta_i=s\), then \(\psi(\lambda)=\lambda^2-s\lambda\) has equal values at paired points. Under the graded-cyclicity hypotheses, \(L_\psi\) has order \(2r\), including order four for \(r=2\). Conversely, a genuine quadratic polynomial constant on all pairs forces their sums to agree.''',
 r'''The explicit polynomial and converse follow by factoring \(\psi(\alpha)-\psi(\beta)\).''',cls='A',
 fate=r'''The degree/order application appears in \citet[Ch.~III, \S5.13 and \S6]{manin1978algebraic}.''',
 status='the construction is established.',literal='correct',refs=MANIN)


item(412,'P000691-P000693','construction','The rank-one nodal construction includes KdV multisolitons',
 r'''The notes identify the rank-one case with \(N\)-soliton solutions of KdV and its hierarchy.''',
 r'''Take scalar coefficients \(\ell=1\), spectral rank \(r=1\), paired spectral points with a common sum, and the nodal gluing data of the preceding construction. On any parameter domain where the interpolation determinant is nonzero, the quadratic spectral function gives a second-order scalar differential operator. Choosing the compatible cubic time flow yields the KdV Lax equation after the usual normalization; its nodal specialization includes the classical multisoliton family.''',
 r'''This does not assert that every arbitrary gluing matrix yields a globally smooth real soliton. The real multisoliton subclass needs real spectral choices and a nonvanishing real denominator; the notebook states neither global regularity nor those restrictions.''',
 cls='E',fate=r'''The identification is explicit in \citet[Ch.~III, \S5.13]{manin1978algebraic}. The rank-one multisoliton family is treated there as known, whereas the uniform higher-rank module construction is the newer part.''',
 status='the stated local construction includes the established rank-one soliton family.',
 match='exact',refs=MANIN)

item(412,'P000693','question','The unqualified question about N-soliton behaviour',
 r'''The talk ends with \ru{Вопрос: поведение \(N\)-солит. решения?}.''',
 r'''No equation, spectral rank, reality or nonsingularity conditions, time direction, or requested observable is specified in the final question.''',
 r'''It cannot be equated with the earlier two-soliton phase-shift problem GP-1973-54 or promoted to a new higher-rank scattering conjecture merely because of the preceding examples.''',
 cls='F',fate=r'''The surrounding soliton construction is matched by \citet[Ch.~III, \S5.13 and \S6]{manin1978algebraic}, but no definite final question was identified.''',
 status='the final question is too underspecified to support an open-problem claim.',
 literal='not determinable',match='thematic only',development='annotated',refs=MANIN,confidence='medium')

correction('P000690','Zakharov--Shabat equation',r'L_t+P_y=[P,L]',r'L_t-P_y=[P,L]',
 'The scan has plus. With the displayed commuting connections and commutator AB-BA, expansion gives the corrected sign.')
correction('P000691','node parameters in real case','alpha_i,beta_i in k; alpha_i=conjugate(beta_i) for k=R',
 'Use complexified parameters for real descent and require all 2N points distinct.',
 'Real distinct conjugate pairs cannot both lie in R; Manin III5.1 explicitly chooses complex node parameters.')
correction('P000692','filtration shift',r'M_i=M_{(i-rN)}',r'M_i=M_{(i+rN)}\quad(M_0=0,\ \mathbf1\in M_1)',
 'Actual PNG has minus. The preceding vanishing lemma forces a positive shift; Manin III5.5 uses +rN+1 with generator in M0.')
correction('P000692','generator coefficient equation',r'\sum_j(\alpha_i^jE_r-\beta_i^jg_i)m_i',
 r'\sum_j(\alpha_i^jE_r-\beta_i^jg_i)m_j',
 'Actual PNG and Russian have m_i; substitution of the displayed polynomial forces m_j.')
correction('P000692','endomorphism ring',r'M_r(\mathcal B[\lambda])=\operatorname{End}_{\mathcal B}(N)',
 r'M_r(\mathcal B[\lambda])=\operatorname{End}_{\mathcal B[\lambda]}(N)',
 'Polynomial matrices also commute with multiplication by lambda; arbitrary B-linear maps need not.')
correction('P000692','flatness equation',r'\partial_xd_t-\partial_td_x=[d_x,d_t]',
 r'\partial_xd_t-\partial_td_x=-[d_x,d_t]',
 'Scan has no minus; expansion of [partial_x+d_x,partial_t+d_t] fixes the sign.')
correction('P000693','left time exponential',r'g_i(x)=e^{-xd_x(\alpha_i)+td_t(\alpha_i)}g_i(0,0)e^{xd_x(\beta_i)+td_t(\beta_i)}',
 r'g_i(x,t)=e^{-xd_x(\alpha_i)-td_t(\alpha_i)}g_i(0,0)e^{xd_x(\beta_i)+td_t(\beta_i)}',
 'PNG shows both plus time signs; Manin III5.12 equation10 and direct differentiation require the left minus.')
checkpoint()

GGL=['gabrielovgelfandlosik1975computation','gabrielovgelfandlosik1975calculus']
MAC=['macpherson1978combinatorial']
talk(413,'1977-03-14','A. M. Gabrielov','P000694-P000696',
 'Pontryagin cycles, changes of sections, and hypersimplicial chains',
 r'''Gelfand motivates a combinatorial theory by local Euler-characteristic formulas and the difficulty of noncommuting rotations. Gabrielov then describes the first Pontryagin class by a corank-two degeneracy locus, reduces the chain calculations to pairs of sections of a real plane bundle, and organizes their cobordisms by hypersimplices. The notes identify MacPherson's February 1977 Bourbaki exposition, which was published in the 1978 proceedings. The core constructions were already in the two Gabrielov--Gelfand--Losik papers of 1975. The final diagrams sketch low-dimensional chain assignments rather than a new, fully specified open problem.''')

item(413,'P000694','remark','The programme of an elementary geometry of polyhedra',
 r'''Gelfand says that an elementary geometry of higher-dimensional polyhedra remains to be made; he contrasts commutative planar rotations with noncommutative \(SO(3)\).''',
 r'''The contrast concerns the search for local combinatorial characteristic-class formulas. Noncommutativity of \(SO(3)\) is a definite fact, but the assertion that three-dimensional polyhedra have no substantive theory specifies no mathematical obstruction or question.''',
 r'''No universal nonexistence statement or orphan problem is extracted from this programme. The claim that named mathematicians learned from the GGL work is recorded as Gelfand's recollection, not independently established intellectual genealogy.''',cls='F',
 fate=r'''The contemporary programme is described in \citet[introduction, p.~105]{macpherson1978combinatorial}; it is not an exact theorem matching the rhetoric.''',
 status='the programme is identifiable, but no definite open proposition is stated.',
 literal='not determinable',match='thematic only',refs=MAC,confidence='medium',speaker='I. M. Gelfand')

item(413,'P000694','claim','The two-faces condition does not characterize a manifold',
 r'''Every \((n-1)\)-simplex is said to bound exactly two \(n\)-simplices.''',
 r'''For a finite pure simplicial complex, this is the codimension-one incidence condition of a pseudomanifold without boundary. To obtain a PL manifold one must also impose the appropriate sphere links at every simplex; incidence alone is insufficient.''',
 r'''The notebook's use of this condition as a description of the intended polyhedral manifold needs the link condition. MacPherson additionally formulates his flattenability hypotheses.''',
 fate=r'''Compare \citet[introduction, pp.~105--106]{macpherson1978combinatorial}.''',
 status='the distinction between pseudomanifolds and PL manifolds is standard.',
 literal='correct with missing hypotheses',development='annotated',refs=MAC,speaker='I. M. Gelfand')

item(413,'P000694','question','Assigning local vertex weights for the Euler characteristic',
 r'''Gelfand asks how numbers at vertices can sum to the Euler characteristic and invokes angular defects.''',
 r'''For a finite simplicial complex \(K\), the vertex weights
 \[w(v)=\sum_{\sigma\ni v}\frac{(-1)^{\dim\sigma}}{\dim\sigma+1}\]
 satisfy \(\sum_vw(v)=\chi(K)\). For a closed piecewise Euclidean triangulated surface, the angle defects
 \[\kappa(v)=2\pi-\sum_{\sigma\ni v}\theta_{\sigma,v}\]
 satisfy \(\sum_v\kappa(v)=2\pi\chi(K)\).''',
 r'''These are precise reconstructions of the local-counting question. The notebook's external-angle sentence does not identify which angles it sums and should not be read as the displayed \(2\pi\) formula without explanation.''',
 fate=r'''The classical Euler formula is recalled in \citet[introduction, p.~105]{macpherson1978combinatorial}.''',
 status='the definite local Euler-characteristic question has elementary established answers.',
 literal='not determinable',match='partial',development='annotated',refs=MAC,speaker='I. M. Gelfand')

item(413,'P000694','claim','Two degree-four characteristic numbers',
 r'''Gelfand says that four-dimensional polyhedra have two invariants, the Euler characteristic and one more.''',
 r'''For a closed oriented smooth four-manifold, the characteristic numbers in view are \(\langle e(TX),[X]\rangle=\chi(X)\) and \(\langle p_1(TX),[X]\rangle=3\,\operatorname{sign}(X)\). These do not classify four-manifolds and are not their only topological invariants.''',
 r'''The statement is interpreted within the local characteristic-class programme, not as a classification claim.''',
 fate=r'''The Euler/Pontryagin context is explicit in \citet[introduction, p.~105]{macpherson1978combinatorial}.''',
 status='the characteristic-number interpretation is established.',
 match='partial',development='annotated',refs=MAC,speaker='I. M. Gelfand')

item(413,'P000694-P000695','construction','The first Pontryagin cycle as a corank-two degeneracy locus',
 r'''Four generic vector fields on a four-manifold give \(Z=\{x:\operatorname{rk}(e_1,e_2,e_3,e_4)\leq2\}\), a codimension-four signed set.''',
 r'''Let \(E\) be a real rank-four bundle on a smooth closed oriented four-manifold. A generic bundle map \(\mathbb R^4\to E\) meets the rank-two stratum transversely and avoids lower ranks. The resulting zero-cycle, with the standard determinantal coorientation, represents the Poincaré dual of \(p_1(E)\). Apply this to \(E=TX\).''',
 r'''Genericity means transversality to rank strata; the rank-at-most-one locus has codimension nine and is avoided. The sign convention is normalized by \(p_1\) of an oriented plane bundle being its Euler class squared.''',
 fate=r'''The degeneracy-cycle framework underlies \citet[\S1]{gabrielovgelfandlosik1975computation}.''',
 status='the construction is classical and was expository here.',refs=GGL)

item(413,'P000695','construction','Canonical coorientation and independence of the signed count',
 r'''The rank degeneracy set in \(\operatorname{Hom}(\mathbb R^m,\mathbb R^n)\) is said to carry a canonical coorientation; the signed count does not depend on the chosen fields.''',
 r'''For a square map of corank two, the normal space to the rank stratum is \(\operatorname{Hom}(\ker A,\operatorname{coker}A)\), with both factors two-dimensional. Its determinant transforms by even powers, so a fixed universal orientation convention is independent of bases. A generic homotopy of sections gives a compact oriented cobordism of the zero-cycles.''',
 r'''The assertion is restricted to the corank-two square situation actually used; arbitrary determinantal strata need not have a canonical coorientation.''',
 fate=r'''See the section-change framework of \citet[\S1]{gabrielovgelfandlosik1975computation}.''',
 status='the signed homology class is independent of the generic fields.',refs=GGL)

item(413,'P000695','construction','Two sections of a plane bundle represent the square of the Euler class',
 r'''For a two-dimensional real bundle \(E\), \(Z=\{e_1=e_2=0\}\) is identified with its first Pontryagin cycle.''',
 r'''For an oriented real rank-two bundle over a closed oriented four-manifold, a transverse section \((e_1,e_2)\) of \(E\oplus E\) has zero-cycle dual to \(e(E\oplus E)=e(E)^2=p_1(E)\).''',
 r'''Orientation is supplied so that the ordinary integral Euler class notation is unambiguous. The canonical orientation of \(E\oplus E\) also admits a formulation without orienting \(E\), but that extension is not needed here.''',
 fate=r'''This is the plane-bundle model used in \citet[\S1]{gabrielovgelfandlosik1975computation}.''',
 status='the model is established.',refs=GGL)

item(413,'P000695','construction','A one-chain relating cycles after replacing one section',
 r'''The first identity is \(Z(e_2,e_3)-Z(e_1,e_3)=\partial Z^1(e_1,e_2;e_3)\), with \(e_3=0\), \(e_1=\lambda e_2\), \(\lambda>0\).''',
 r'''For generic sections of a real plane bundle, use the compactified parameter \(\lambda\in[0,\infty]\). The incidence locus \(e_3=0,\ e_1=\lambda e_2\), projected as an oriented chain to the base, has boundary the difference of the two zero-cycles, with sign fixed by the parameter orientation.''',
 r'''The chain is the closure or pushforward of the parameterized locus; the open set with \(\lambda>0\) alone has no included boundary points. Transversality and compactification are explicit additions.''',
 fate=r'''The section-change calculus is developed in \citet{gabrielovgelfandlosik1975calculus}.''',
 status='the cobordism identity is established after orientation conventions.',refs=GGL)

item(413,'P000695','construction','A two-chain filling the cyclic sum of section changes',
 r'''Adding three displayed one-chain boundaries gives a closed curve; it is said to bound the locus \(e_1=\lambda e_2=\mu e_3\), \(\lambda,\mu>0\).''',
 r'''For generic triples, compactify the positive proportionality parameters and take the corresponding oriented incidence chain. Its codimension-two projection has boundary equal to the cyclic sum of the three codimension-three section-change chains, with compatible signs.''',
 r'''The parameter compactification and signs are necessary for a chain identity; the notebook gives the geometric idea rather than a complete orientation convention.''',
 fate=r'''This is part of the published hypersimplicial chain calculus \citep{gabrielovgelfandlosik1975calculus}.''',
 status='the geometric chain relation is established.',match='partial',refs=GGL)

item(413,'P000695','definition','Hypersimplices and their two kinds of triangular faces',
 r'''A hypersimplex is the convex hull of centres of faces of a simplex. Vertices carry index sets; the octahedron has triangular faces of two types.''',
 r'''The standard hypersimplex is \(\Delta(k,m)=\{x\in[0,1]^m:\sum_i x_i=k\}\), the convex hull of indicator vectors of \(k\)-subsets. Scaling by \(1/k\) identifies these with barycentres of \((k-1)\)-faces. Its faces are obtained by fixing coordinates to zero or one; \(\Delta(2,4)\) is an octahedron whose triangular faces arise in the two ways.''',
 r'''The notebook's appended fixed indices correspond to coordinates fixed to one.''',
 fate=r'''See \citet[\S1, pp.~107--109]{macpherson1978combinatorial}.''',
 status='the combinatorial definition is standard.',literal='correct',refs=MAC)

chain_id=item(413,'P000695-P000696','problem','Boundary-compatible chains assigned to hypersimplices',
 r'''The task is to construct a chain for each hypersimplex with the required properties; vertices represent double-zero loci and edges represent the one-section changes.''',
 r'''Construct rational chains \(C(H)\) in spaces of vector configurations, extending the specified vertex and edge assignments, so that \(\partial C(H)=C(\partial H)\), with the appropriate codimension and compatibility under restriction to faces. In the first-Pontryagin construction these chains must descend through the configuration and hypersimplicial complexes.''',
 r'''The boundary equation is the strongest definite compatibility indicated by the preceding examples. The full list of admissibility and locality properties is supplied by the published construction, not repeated by the notebook.''',
 fate=r'''The chain systems already exist in \citet[\S18, Proposition 14; \S\S27--28]{gabrielovgelfandlosik1975calculus}; compare \citet[\S3]{macpherson1978combinatorial}.''',
 status='the first-Pontryagin chain problem was solved before this talk; no new unsolved variant is specified.',
 match='partial',problem='GP-1976-20',refs=GGL+MAC)

item(413,'P000696','remark','The two triangular chain assignments and the handwritten one-half',
 r'''One triangle with labels \(14,24,34\) points to \(\tfrac12(e_4=0)\); the other, labelled \(12,13,23\), points to positive proportionality of \(e_1,e_2,e_3\).''',
 r'''These drawings distinguish the two triangular face types. The second has the incidence interpretation in the preceding two-chain item. The first shows a rational coefficient \(1/2\), but the notes do not specify the oriented region, multiplicity function, or chain category needed to interpret \(\tfrac12\{e_4=0\}\) as a complete boundary-compatible chain.''',
 r'''The PNG confirms the coefficient. It is not corrected to an integer and is not promoted to a fully defined chain formula.''',cls='F',
 fate=r'''The surrounding rational chain construction is identifiable in \citet[\S3]{macpherson1978combinatorial}, but the isolated drawn assignment is only partially specified.''',
 status='the diagram belongs to a known construction; its literal chain convention remains undetermined.',
 literal='not determinable',match='partial',development='annotated',refs=MAC,confidence='medium')

problem('GP-1976-20','Boundary-compatible hypersimplicial chains for the first Pontryagin class',
 r'''Extend the double-zero and one-section-change loci to rational configuration-space chains assigned to hypersimplices, compatible with faces and satisfying \(\partial C(H)=C(\partial H)\), in the first-Pontryagin construction.''',
 [chain_id],r'''As of November 2026: solved before the 1977 exposition by the 1975 GGL construction. The notebook does not specify a separate stronger variant. Compare \citet[\S18 and \S\S27--28]{gabrielovgelfandlosik1975calculus}.''',GGL+MAC)
correction('P000694','polyhedral manifold criterion','each codimension-one simplex belongs to exactly two top simplices',
 'This is an incidence condition; manifold links or flattenability must also be required.',
 'Russian and scan agree. MacPherson1977/78 pp105–106 supplies the missing geometric hypotheses.')
correction('P000694','angle-defect motivation','sum of external angles is not pi',
 'Preserve the ambiguous angle description; for a closed Euclidean triangulated surface the standard defect is 2pi minus the incident face-angle sum.',
 'The scan does not identify the external angles or justify a numerical replacement.',typ='ambiguity')
correction('P000695','determinantal coorientation','Z in Hom(R^m,R^n) has canonical coorientation',
 'Restrict this assertion to the square corank-two stratum used in the argument.',
 'Arbitrary real determinantal strata need not be coorientable; here normal=Hom(ker,coker) with both dimensions2.')
checkpoint()

RADON=['gelfand1967planes']
COMPLEX=['gelfandgraev1968complexes']
talk(414,'1977-03-21','M. I. Graev','P000697-P000698',
 'Range equations, differential-form inversion, and complexes of lines',
 r'''Graev develops the complex line transform in three-space, its range equations, and inversion by integrating a closed \((1,1)\)-form over a cycle of directions. This matches the explicitly cited 1967 Gelfand--Graev--Shapiro paper. The classification of admissible complexes matches the 1968 Gelfand--Graev paper, including its algebraic and genericity conditions. The final discussion of linear complexes is a separate projective-geometric construction: nondegenerate and special complexes must be distinguished, and it is not automatically an example of the preceding admissibility theorem.''')

item(414,'P000697','definition','The affine complex line transform',
 r'''A line is \(x_1=\alpha_1x_3+\beta_1,\ x_2=\alpha_2x_3+\beta_2\), and \(\varphi(\alpha,\beta)\) is the integral of \(f\) against \(dx_3\,d\bar x_3\).''',
 r'''For \(f\in\mathcal S(\mathbb C^3)\), define \(\varphi(\alpha,\beta)=\int_{\mathbb C}f(\alpha_1t+\beta_1,\alpha_2t+\beta_2,t)\,dA(t)\). This chart excludes directions parallel to \(x_3=0\); changing the line parameter transforms the density by the corresponding squared Jacobian.''',
 r'''The area-measure convention and chart limitation are explicit additions. A global scalar realization uses the compensating density factor of the cited paper.''',
 fate=r'''See \citet[\S1, equations (1)--(4)]{gelfand1967planes}.''',
 status='the line transform is classical.',refs=RADON)

radon_id=item(414,'P000697','question','Reconstruction from all line integrals and reduction to a plane',
 r'''The notes ask how to recover \(f\) from \(\varphi\), call the data redundant, and restrict to lines in a plane.''',
 r'''For a fixed complex two-plane through \(x\), the supplied line integrals over its lines are the complex Radon transform of \(f\) restricted to that plane. Its inversion recovers \(f(x)\); taking all such planes gives uniqueness of the full line transform on Schwartz functions.''',
 r'''The restriction is to lines contained in the chosen plane, not a projection of \(f\) onto that plane.''',
 fate=r'''The precise cycle inversion is \citet[\S8, Theorem 2]{gelfand1967planes}.''',
 status='the reconstruction problem is solved.',problem='GP-1976-21',refs=RADON)

item(414,'P000697','claim','John equation and the missing global range hypotheses',
 r'''In the real case \(\varphi_{\alpha_1\beta_2}=\varphi_{\alpha_2\beta_1}\), and the equation is said to be sufficient.''',
 r'''For the real line transform in \(\mathbb R^3\), differentiation under the integral gives this equation. It characterizes the range within the global smooth line-data class whose density-normalized derivatives decay faster than every inverse power of the line's distance from zero, uniformly in compact direction charts, with the correct coordinate covariance.''',
 r'''A local smooth solution in one affine chart, with no decay or global extension, is not covered by sufficiency. The condition \(k<n-1\) in the paper holds for \(k=1,n=3\).''',
 fate=r'''See \citet[\S7, Theorem 1 and its real-case footnote]{gelfand1967planes}.''',
 status='the range theorem is established in its stated global class.',refs=RADON)

item(414,'P000697','method','A wavefront-set heuristic from singular plane integrals',
 r'''The page suggests that \((x_0,\xi_0)\in WF(u)\) when integration over parallel planes in direction \(\xi_0\) has a singularity.''',
 r'''For a localized distribution, Radon data can detect conormal singularities through the incidence canonical relation. An unlocalized integral over a whole plane does not identify which point caused a singularity, and cancellations can erase contributions. Thus a pointwise criterion requires localization near \(x_0\), a convention making \(\xi_0\) a normal covector, and a precise microlocal implication.''',
 r'''These are necessary qualifications, not a theorem present in the notebook. No unique equivalence is reconstructed from the single sentence.''',cls='F',
 fate=r'''The related characteristic geometry is explained in \citet[\S\S2--3]{guillemin1985line}; the notebook's particular wavefront criterion is not matched.''',
 status='the heuristic is recognizable, but its literal pointwise assertion is insufficiently specified.',
 literal='not determinable',match='thematic only',development='annotated',refs=['guillemin1985line'],confidence='medium')

item(414,'P000697','construction','Differential forms on the space of lines through a point',
 r'''In the complex case \(\mathcal H\varphi=\sum_{i,j}\varphi_{\beta_i\bar\beta_j}\,d\alpha_i\wedge d\bar\alpha_j\); in the real case \(\mathcal H\varphi=\sum_i\varphi_{\beta_i}\,d\alpha_i\). Substitute \(\beta_i=x_i-\alpha_i x_3\).''',
 r'''The substitution pulls the relevant differentiated data back to the pencil of lines through \(x\). In the indicated chart it gives a complex \((1,1)\)-form, or a real one-form. With the line-density transformation law these expressions patch to forms on the projective space of directions.''',
 r'''Global patching and measure normalization are implicit in the handwritten chart formula.''',
 fate=r'''See \citet[\S\S4--6]{gelfand1967planes}; differential-form generalization in \citet[\S1]{gelfand1969forms}.''',
 status='the differential-form construction is established.',refs=RADON+['gelfand1969forms'])

range_id=item(414,'P000697','theorem','The closed-form characterization of the complex line-transform range',
 r'''The theorem is \(\varphi=Rf\Longleftrightarrow d(\mathcal H_x\varphi)=0\) for every \(x\).''',
 r'''Let \(\varphi\) be globally smooth normalized line data in the rapidly decreasing class: all derivatives in local vector-bundle trivializations of the affine Grassmannian decay rapidly in the transverse displacement, uniformly over directions. Then \(\varphi=Rf\) for some \(f\in\mathcal S(\mathbb C^3)\) exactly when the associated \((1,1)\)-form is closed on the pencil through every \(x\).''',
 r'''The global class is essential and is not contained in the notebook's displayed equivalence.''',
 fate=r'''This is \citet[\S7, Theorem 1]{gelfand1967planes}, published ten years before the seminar.''',
 status='the characterization is proved.',problem='GP-1976-21',refs=RADON)

item(414,'P000697','theorem','Cycle inversion and the real dimension of the integrating cycle',
 r'''The inversion formula is \(\int_\gamma\mathcal H_x\varphi=c_\gamma f(x)\); the cycle is called one-dimensional.''',
 r'''For data in the range and a closed real two-cycle \(\gamma\) in the complex projective direction space \(\mathbb{CP}^2\), the formula holds with a constant depending only on its homology class and density normalization. A projective line is a cycle with nonzero coefficient and gives reconstruction.''',
 r'''A \((1,1)\)-form has real degree two. The notebook's dimension is interpretable as complex dimension one, not real dimension one. A nontrivial cycle also cannot be contained entirely in the contractible affine direction chart.''',
 fate=r'''See \citet[\S8, Theorem 2, pp.~29--30 of the Russian original]{gelfand1967planes}.''',
 status='cycle inversion is established with the corrected dimension convention.',
 literal='correct with missing hypotheses',development='annotated',refs=RADON)

item(414,'P000697','claim','Why the analogous real local period gives zero',
 r'''For the real case the notes say \(C_\gamma=0\), and inversion is nonlocal.''',
 r'''For real Schwartz line data in the range, the closed real one-form on the pencil has zero periods: \(H^1_{\mathrm{dR}}(\mathbb{RP}^2)=0\). This particular local differential-form period cannot reconstruct \(f(x)\); a real inversion uses a different, nonlocal operator.''',
 r'''The conclusion is about this period formula, not a claim that the real line transform lacks an inverse.''',
 fate=r'''The distinction follows from the real range form and complex inversion theorem in \citet[\S\S7--8]{gelfand1967planes}.''',
 status='the obstruction to this particular local period is established.',
 match='partial',development='annotated',refs=RADON)

complex_id=item(414,'P000697','question','Restricted data and the definition of an admissible complex',
 r'''For a three-dimensional family \(K\) of lines, the notes ask when knowing \(\mathcal H\varphi\) on \(K\) permits recovery of \(\varphi\).''',
 r'''In the matched 1968 formulation, \(K\) is a closed irreducible algebraic three-dimensional family of complex lines covering a dense open subset of \(\mathbb C^3\). Admissibility means the inversion form on \(K\cap G_x\) can be computed by a differential operator from restricted scalar data \(\varphi|_K\), independently of an extension off \(K\). Reconstruction additionally requires a cycle with nonzero inversion coefficient.''',
 r'''The notebook's question supplies differentiated data, whereas the published definition asks whether those derivatives descend from scalar restricted data. These distinct inverse problems must not be identified without this correction.''',
 fate=r'''See \citet[\S2, Definitions 1--2 and formula (7)]{gelfandgraev1968complexes}.''',
 status='the classical admissibility problem is formulated and solved in that setting.',
 match='partial',problem='GP-1976-22',development='annotated',refs=COMPLEX)

item(414,'P000697','theorem','Admissible line complexes come from a curve or a surface',
 r'''The asserted alternatives are all lines meeting a curve or all lines tangent to a surface.''',
 r'''For the algebraic admissibility notion just stated, a complex of lines in \(\mathbb C^3\), near a generic regular line and its regular critical point, is either the family meeting a local curve or the family tangent to a local surface. The general-dimensional theorem imposes distinct critical points and general-position tangent hyperplanes; the paper states the three-dimensional dichotomy as its corollary.''',
 r'''This is not a classification of arbitrary smooth three-parameter families with any conceivable injectivity property. Singular global branches and the data model require the paper's hypotheses.''',
 fate=r'''See \citet[\S5, Theorem 6 and corollary, pp.~49--51]{gelfandgraev1968complexes}; compare \citet[\S3]{guillemin1985line}.''',
 status='the identified classification predates the talk.',
 match='exact',refs=COMPLEX+['guillemin1985line'],problem='GP-1976-22')

item(414,'P000698','definition','Plücker coordinates and the equation of a linear complex',
 r'''For a plane spanned by \(x,y\in k^4\), \(p_{ij}=x_i y_j-x_j y_i\); a linear complex satisfies \(\sum c_{ij}p_{ij}=0\).''',
 r'''A projective line in \(\mathbb P^3_k\), \(k=\mathbb R\) or \(\mathbb C\), is a two-plane in \(k^4\). Its decomposable bivector \(x\wedge y\) gives a point of the Klein quadric in \(\mathbb P(\Lambda^2k^4)\). A linear complex is its hyperplane section, equivalently the two-planes isotropic for an alternating form \(\omega\).''',
 r'''The plane in the notebook is the vector two-plane representing a projective line.''',
 fate=r'''The Grassmannian framework is recalled in \citet[\S\S1--2]{guillemin1985line}; this is classical projective geometry.''',
 status='the construction is established.',literal='correct',refs=['guillemin1985line'])

item(414,'P000697-P000698','construction','Symplectic polarity attached to a nondegenerate linear complex',
 r'''Each point is associated with a plane containing the complex's lines through it; each line is associated with another line meeting those lines.''',
 r'''If \(\omega\) is nondegenerate, the plane of complex lines through \(p=[v]\) is \(\mathbb P(v^\perp)\). A line \(\mathbb P(L)\) has polar line \(\mathbb P(L^\perp)\). Every isotropic line meeting \(\mathbb P(L)\) also meets \(\mathbb P(L^\perp)\).''',
 r'''Nondegeneracy is needed for a polarity. If \(v\in\ker\omega\), all lines through \(p\) satisfy the complex equation, and no single projective plane contains them.''',
 fate=r'''This is the alternating-form realization of the classical line geometry underlying \citet[\S2]{guillemin1985line}.''',
 status='the stated polarity is valid in the nondegenerate case.',
 match='partial',development='annotated',refs=['guillemin1985line'])

item(414,'P000698','claim','The standard linear complex and its isomorphism class',
 r'''The example is \(x_1=\alpha x_3+\beta,\ x_2=\gamma x_3+\alpha\); the notes say any other complex is isomorphic to it.''',
 r'''In homogeneous coordinates this is the affine chart of \(p_{14}+p_{23}=0\), a rank-four alternating form. All nondegenerate alternating forms on \(k^4\) are linearly equivalent. Rank-two forms give a different projective orbit: their complexes consist of lines meeting the projectivized kernel.''',
 r'''The universal assertion must be restricted to nondegenerate linear complexes. It does not classify all nonlinear complexes and does not prove admissibility for restricted scalar line data.''',
 fate=r'''The linear-algebra normal form supplies the correction; compare the admissibility distinction in \citet[\S2]{gelfandgraev1968complexes}.''',
 status='the nondegenerate normal form is established; the unqualified assertion is false.',
 literal='false as written',match='partial',development='annotated',refs=COMPLEX)

item(414,'P000698','remark','An unspecified Legendre transformation',
 r'''The single line says \ru{Преобр. Лежандра есть}.''',
 r'''No source space, target space, generating function, or transformation formula is given. Contact or projective duality associated with the line complex is a possible interpretation, but is not uniquely determined.''',
 r'''No specific Legendre transform is inserted into the notebook.''',cls='F',
 fate='The phrase was compared with the cited integral-geometry papers and the line-complex literature; no exact transformation was identified.',
 status='the intended transformation remains unidentifiable from this record.',
 literal='not determinable',match='none found',verification='unresolved lead',refs=[],confidence='low')

problem('GP-1976-21','Range and inversion of the line transform in three-space',
 r'''Characterize globally smooth rapidly decreasing line data that are integrals of a Schwartz function on \(\mathbb C^3\) or \(\mathbb R^3\), and reconstruct that function.''',
 [radon_id,range_id],r'''As of November 2026: solved before the talk by \citet[\S\S7--8, Theorems 1--2]{gelfand1967planes}. The notebook omits the global data class and real/complex cycle distinction.''',RADON)
problem('GP-1976-22','Admissible algebraic complexes of lines',
 r'''For a closed irreducible algebraic three-dimensional line complex covering a dense open subset of \(\mathbb C^3\), determine when the differential inversion form descends from the scalar line data restricted to the complex, and classify such complexes near generic regular lines.''',
 [complex_id,'1976-414.10'],r'''As of November 2026: the specified admissibility and generic classification were established in \citet[\S\S2--5]{gelfandgraev1968complexes}. The notebook's wording about already differentiated data is a partial match.''',COMPLEX)
correction('P000697','range theorem','closedness is necessary and sufficient without a function class',
 'Add the global smooth, rapidly decreasing, density-covariant data class.',
 r'GGS (1967), Theorem 1, states class \(\Phi\) as an independent hypothesis.')
correction('P000697','inversion cycle dimension','one-dimensional cycle',
 'A real two-cycle, for example a complex one-dimensional projective line.',
 r'The PNG clearly says one-dimensional; the integrand is a \((1,1)\)-form. GGS (1967), Theorem 2, explicitly says real dimension \(2k\).',typ='ambiguity')
correction('P000697','admissibility question','recover phi from Hphi on K',
 'Distinguish this from recovering the inversion form from scalar data phi restricted to K.',
 'Gelfand--Graev (1968), section 2, Definition 2, specifies descent of the differential inversion operator.',typ='ambiguity')
correction('P000698','all linear complexes isomorphic','any other is isomorphic to it',
 'Any other nondegenerate linear complex is projectively isomorphic to it.',
 'The rank of the associated alternating form distinguishes ranks four and two; rank two gives a special complex.')
checkpoint()

talk(416,'1977-03-28','I. M. Gelfand','P000699',
 'Poncelet closure and Figiel’s short proof of Dvoretzky’s theorem',
 r'''The short intervention above Vershik's heading states the Poncelet porism for two conics, asks for the closing condition, and points to Griffiths's 1976 paper. It then identifies Figiel's 1976 Compositio proof of Dvoretzky's theorem. This material precedes record 415 on the manuscript page despite the catalogue record-number order.''')

poncelet_id=item(416,'P000699','problem','When does the Poncelet polygon close?',
 r'''A polygon is inscribed in one conic and tangent to another; Gelfand asks when such a polygon closes, citing Griffiths.''',
 r'''For two nonsingular complex plane conics whose incidence curve of a point on the outer conic and a tangent to the inner conic is smooth, that curve is genus one. The successive-tangent operation is translation by a fixed \(\delta\) on it. A polygon closes after \(m\) steps exactly when \(m\delta=0\); exact period \(m\) requires \(\delta\) to have exact order \(m\). Nested real ovals select the real branch and direction of iteration.''',
 r'''Smoothness of the incidence curve excludes degenerate conic pairs. The elliptic-curve translation is the precise reconstruction behind the notes' mention of Jacobi's elliptic integrals.''',
 fate=r'''See \citet[\S I(d), pp.~345--348]{griffiths1976abel}, published before the talk.''',
 status='the closure criterion is classical and solved.',problem='GP-1976-23',refs=['griffiths1976abel'])

item(416,'P000699','theorem','Poncelet’s porism',
 r'''If the construction closes from one point, it closes from every other point in the same number of steps.''',
 r'''For the nondegenerate conic pair and consistent tangent iteration above, the existence of a closed \(m\)-step orbit means the elliptic translation is \(m\)-torsion. Therefore its \(m\)th iterate is the identity for every admissible starting point. Exceptional points of the algebraic construction are understood by extension.''',
 r'''The same branch and a nondegenerate conic pair are required; changing tangent directions arbitrarily is not this map.''',
 fate=r'''The porism is stated in \citet[\S I(d), formula (1.37) and discussion]{griffiths1976abel}.''',
 status='the theorem is classical.',refs=['griffiths1976abel'],problem='GP-1976-23')

item(416,'P000699','claim','Invariant measure and circle-rotation coordinates',
 r'''The notebook writes that the Poncelet theorem implies an invariant measure and an isomorphism with a circle rotation.''',
 r'''For nested smooth real conics with a regular real Poncelet map, the elliptic-curve parameter gives an invariant positive measure on the relevant circle component. Integrating and normalizing this measure gives a coordinate conjugating the map to a rigid rotation. Rational rotation number is the closure criterion.''',
 r'''The construction uses the elliptic geometry and a full-support nonatomic invariant density. The mere logical statement of a porism does not supply such a density or the conjugacy.''',
 fate=r'''The elliptic-parameter construction is in \citet[\S I(d)]{griffiths1976abel}.''',
 status='the geometric rotation description is established, with the stated regularity.',
 match='partial',development='annotated',refs=['griffiths1976abel'])

item(416,'P000699','remark','Figiel’s short proof of Dvoretzky’s theorem',
 r'''Gelfand points to the latest Compositio issue and attributes the simplest proof of Dvoretzky's theorem to Figiel.''',
 r'''For every integer \(k\geq2\) and \(\varepsilon>0\), there is \(N(k,\varepsilon)\) such that every real or complex normed space of dimension at least \(N(k,\varepsilon)\) has a \(k\)-dimensional subspace with Banach--Mazur distance at most \(1+\varepsilon\) from the corresponding Euclidean space.''',
 r'''This is a bibliographically identifiable pointer; the notebook contains no details of the proof and makes no quantitative claim about \(N\).''',
 fate=r'''The exact source is \citet[theorem, p.~297]{figiel1976short}, Compositio 33(3), 1976.''',
 status='the theorem and the cited proof predate the talk.',literal='correct',refs=['figiel1976short'])

problem('GP-1976-23','Poncelet closure for two conics',
 r'''For two nonsingular conics with smooth incidence elliptic curve, determine whether the consistent tangent iteration has a closed polygon, and characterize its period.''',
 [poncelet_id,'1976-416.2'],r'''As of November 2026: classical; the translation point on the incidence elliptic curve is torsion precisely in the closing case. The exact source cited in the notes is \citet[\S I(d)]{griffiths1976abel}.''',['griffiths1976abel'])
checkpoint()

# Record 415 occurs after record 416 on the manuscript page.
VK=['vershikkerov1977asymptotics']
VO=['vershikokounkov2005approach']
CLT=['ivanovolshanski2002kerov']
talk(415,'1977-03-28','A. M. Vershik','P000699-P000701',
 'Probability, the Young graph, and Plancherel asymptotics',
 r'''The manuscript starts Vershik's talk below Gelfand's intervention on the page headed 28 March 1977, without another date. The catalogue's 4 April date is therefore corrected here, with the catalogue value preserved in the provenance. The exposition moves from Young's finite representation theory and branching paths to Plancherel growth, the limit shape, Ulam's longest increasing subsequence problem, and a proposed fluctuation theorem. The exact limit-shape and first-row results are in the 1977 Vershik--Kerov announcement, received in December 1976. The fluctuation line is not an exact statement of the later Kerov theorem: both the displayed fourth-root scaling and the white-noise description require correction.''',
 catalogue_date='1977-04-04',manuscript_date='1977-03-28')

item(415,'P000699','definition','Symmetric groups, partitions, and Young diagrams',
 r'''The notes define \(S_n\), finitary \(S_\infty\), and a descending array of left-aligned rows called a Young tableau.''',
 r'''\(S_\infty=\bigcup_nS_n\) under the inclusions fixing the last letter. A partition \(\lambda_1\geq\lambda_2\geq\cdots\geq0\), \(\sum\lambda_i=n\), specifies a Young diagram. A standard tableau additionally labels its cells \(1,\ldots,n\), increasingly in rows and columns.''',
 r'''The distinction between an unfilled diagram and a labelled tableau is editorial terminology; the notebook uses the Russian word for tableau for both.''',
 fate=r'''This is the classical framework recalled in \citet[\S\S1,5]{vershikokounkov2005approach}; the asymptotic setting is explicit in \citet[p.~1024]{vershikkerov1977asymptotics}.''',
 status='these definitions are standard.',literal='correct',refs=VO+VK)

item(415,'P000699-P000700','construction','The common constituent of row and column induced representations',
 r'''For the row subgroup \(G_1\) and column subgroup \(G_2\), the notes induce the trivial and alternating representations and select their one common irreducible constituent.''',
 r'''Over \(\mathbb C\), let \(R_\lambda\) and \(C_\lambda\) permute the labelled cells within each row and column. The representations \(\operatorname{Ind}_{R_\lambda}^{S_n}{\bf1}\) and \(\operatorname{Ind}_{C_\lambda}^{S_n}\operatorname{sgn}\) have just one common irreducible constituent, \(V^\lambda\), with multiplicity one in both. The resulting \(V^\lambda\) exhaust the irreducible representations.''',
 r'''The field and multiplicity are made explicit. A different labelling gives conjugate subgroups and the same representation class.''',
 fate=r'''The traditional Young construction is recalled in \citet[Introduction]{vershikokounkov2005approach}; the paper's new inductive proof is later, but the theorem itself is classical.''',
 status='this is established characteristic-zero representation theory.',refs=VO)

item(415,'P000700','theorem','Hook-length formula for the degree of an irreducible',
 r'''The page gives \(n!/\prod h\) and dates the hook formula to 1955; its hook description mentions the cells to the right and below.''',
 r'''For \(\lambda\vdash n\), \(d_\lambda=\dim V^\lambda=n!/\prod_{(i,j)\in\lambda}h_{ij}\), where \(h_{ij}=\lambda_i-j+\lambda'_j-i+1\). The corner cell itself is included.''',
 r'''The \(+1\) is essential. Interpreting the notebook's verbal description as excluding the corner would give zero hook lengths at removable cells.''',
 fate=r'''The original publication is \citet{framerobinsonthrall1954hook}, dated 1954 in the opened publisher record; the formula also appears in \citet[p.~1024]{vershikkerov1977asymptotics}. The original full article was not accessible in this run.''',
 status='the formula is classical; the notebook date is one year late.',
 match='exact',refs=['framerobinsonthrall1954hook']+VK,development='annotated')

item(415,'P000700','theorem','Multiplicity-free branching by removing a cell',
 r'''One sentence says that every irreducible of \(S_{n-1}\) occurs once, but the following line restricts to diagrams preceding \(\lambda\) in the Young graph.''',
 r'''\(\operatorname{Res}^{S_n}_{S_{n-1}}V^\lambda\cong\bigoplus_{\mu\nearrow\lambda}V^\mu\), where \(\mu\nearrow\lambda\) means that \(\lambda/\mu\) consists of one removable cell. No other irreducible occurs.''',
 r'''The unrestricted wording is corrected using the immediately following notebook qualification.''',
 fate=r'''The classical branching theorem is proved in \citet[Theorems~2.9 and 5.8]{vershikokounkov2005approach}.''',
 status='the predecessor restriction is indispensable.',literal='false as written',development='annotated',refs=VO)

item(415,'P000700','construction','Paths, standard tableaux, and a Gelfand--Tsetlin basis',
 r'''Paths from the empty diagram to \(\lambda\) index basis vectors and count the degree of the representation.''',
 r'''Successive multiplicity-free restrictions along \(S_1\subset\cdots\subset S_n\) decompose \(V^\lambda\) into one-dimensional joint eigenspaces for the centers of the subgroup algebras. Paths to \(\lambda\) index these lines, hence \(d_\lambda=f^\lambda\), the number of standard tableaux. Choosing a nonzero vector in each line gives a basis, unique only up to independent rescalings.''',
 r'''A canonical basis of lines does not choose phases or scales of vectors.''',
 fate=r'''See \citet[\S1 and Theorem~5.8]{vershikokounkov2005approach}.''',
 status='the classical branching-path interpretation is exact.',refs=VO)

skew_id=item(415,'P000700','question','Counting paths between two fixed Young diagrams',
 r'''After calling combinatorial counting unsolved, the notes ask for the number of paths from a diagram of size \(n\) to a specified diagram of size \(m<n\).''',
 r'''For \(\mu\vdash m\), \(\lambda\vdash n\), \(\mu\subseteq\lambda\), the multiplicity of \(V^\mu\) in \(\operatorname{Res}^{S_n}_{S_m}V^\lambda\) is \(f^{\lambda/\mu}\). Equivalently, it counts standard tableaux of the skew shape. For \(r\geq\ell(\lambda)\), padding both partitions with zeros,
 \[
 f^{\lambda/\mu}=(n-m)!\det\left[\frac1{(\lambda_i-\mu_j-i+j)!}\right]_{i,j=1}^r,
 \]
 with \(1/k!=0\) for \(k<0\).''',
 r'''The determinant and the precise skew-tableau formulation are supplied here. The notebook does not specify a stronger demand such as a positive product formula or uniform asymptotics; such demands are not manufactured as open problems.''',
 fate=r'''Iterated branching gives the multiplicity interpretation. The classical Aitken determinant follows from Jacobi--Trudi, as explicitly derived in \citet[\S1, equations~(1.1)--(1.2)]{stanley2011skew}; the latter is a checked later exposition, not a claim that the formula originated in 2011.''',
 status='the literal finite counting problem has an exact determinant; no precise unsolved strengthening is recorded.',
 literal='correct',problem='GP-1976-24',refs=VO+['stanley2011skew'])

item(415,'P000700','claim','The assertion that total path counting is unsolved',
 r'''The notebook says \ru{Комбинаторная задача подсчета не решена} and mentions only Frobenius's formula, despite having just written the hook formula.''',
 r'''For paths from the empty diagram, the hook formula already counts them. For two fixed endpoints, the skew determinant in the preceding item gives an exact count. Without an additional restriction on the permitted formula or asymptotic regime, the stated unsolved assertion is false.''',
 r'''The two possible literal readings are distinguished; neither supports an identified open problem.''',
 fate=r'''Compare \citet{framerobinsonthrall1954hook} and \citet[equation~(1.2)]{stanley2011skew}.''',
 status='the claim cannot be retained as evidence of an open counting problem.',
 literal='false as written',match='partial',refs=['framerobinsonthrall1954hook','stanley2011skew'],development='annotated')

item(415,'P000700','theorem','First-row length detected by invariant vectors',
 r'''The first row is characterized by restriction to symmetric subgroups and the appearance of an invariant vector.''',
 r'''For the standard inclusion \(S_m\subset S_n\), \((V^\lambda)^{S_m}\ne0\) if and only if \(m\leq\lambda_1\). Thus \(\lambda_1=\max\{m:(V^\lambda)^{S_m}\ne0\}\).''',
 r'''This follows by iterating the branching theorem: the one-row partition \((m)\) must be a subdiagram of \(\lambda\).''',
 fate=r'''This is an elementary consequence of the classical branching rule, verified in \citet[Theorem~5.8]{vershikokounkov2005approach}.''',
 status='the representation-theoretic characterization is exact.',literal='correct',refs=VO)

item(415,'P000700','definition','Finite Plancherel measure',
 r'''The regular representation is described by functions on a symbol resembling \(S^n\); weights are \((\dim\lambda)^2/n!\).''',
 r'''\(\mathbb C[S_n]\cong\bigoplus_{\lambda\vdash n}V^\lambda\otimes(V^\lambda)^*\); therefore \(\sum_\lambda d_\lambda^2=n!\), and \(\mathrm{Pl}_n(\lambda)=d_\lambda^2/n!\) is a probability measure on partitions of \(n\).''',
 r'''The group is \(S_n\), not a sphere or a Cartesian power.''',
 fate=r'''See \citet[p.~1024]{vershikkerov1977asymptotics}.''',
 status='this is the classical finite-group Plancherel measure.',refs=VK)

item(415,'P000700','construction','The coherent Plancherel measure on infinite Young paths',
 r'''The notes pass to infinite paths and conditional probabilities for adding a cell.''',
 r'''Give a specified length-\(n\) path ending at \(\lambda\) mass \(d_\lambda/n!\). The resulting coherent probability measure has level marginal \(d_\lambda^2/n!\). Its growth transition is
 \[
 p(\lambda,\nu)=\frac{d_\nu}{(n+1)d_\lambda}\quad(\lambda\nearrow\nu,\ |\lambda|=n).
 \]
 The dimension identity for induction makes the transition probabilities sum to one.''',
 r'''These precise cylinder and transition probabilities expand the notebook shorthand.''',
 cls='A',fate=r'''The infinite path measure is described in \citet[p.~1025, before Theorem~2]{vershikkerov1977asymptotics}. The paper was received 14 December 1976 and presented 17 December 1976, then printed in 1977; those editorial dates do not establish an earlier public preprint.''',
 status='the coherent growth process is established.',refs=VK)

item(415,'P000700','question','Gelfand asks for an infinite-dimensional Plancherel formulation',
 r'''Gelfand asks for a continuous, infinite-dimensional analogue of Plancherel's formula.''',
 r'''For finitary \(S_\infty\), a precise interpretation in the subsequent discussion is the spectral measure of the Young-path commutative subalgebra in the regular representation. The notebook does not specify a unique general Plancherel theorem for arbitrary infinite-dimensional groups.''',
 r'''A type-I direct integral over irreducible representations is not silently substituted for this question: the regular von Neumann algebra of \(S_\infty\) is a type \(\mathrm{II}_1\) factor.''',
 cls='F',fate=r'''The specific path-space realization and the type \(\mathrm{II}_1\) factor are explicit in \citet[p.~1025]{vershikkerov1977asymptotics}; this supplies only a partial match to the unqualified request.''',
 status='the specific construction is known; the broader requested object is not uniquely determined.',
 literal='not determinable',match='partial',refs=VK,confidence='medium',speaker='I. M. Gelfand')

item(415,'P000701','theorem','Plancherel limit shape in half-rotated coordinates',
 r'''The page displays uniform convergence in probability to \(\frac2\pi(X\arcsin X+\sqrt{1-X^2})\), but interchanges the sum and difference in the coordinate definition and omits the exterior formula.''',
 r'''For nonnegative row-column coordinates \(x,y\), set \(X=(x-y)/2\), \(Y=(x+y)/2\), and let \(\widetilde\lambda(X)\) be the upper boundary of the rotated diagram. Under \(\mathrm{Pl}_n\),
 \[
 \sup_X\left|n^{-1/2}\widetilde\lambda(\sqrt n X)-\Omega(X)\right|
 \longrightarrow0
 \quad\hbox{in probability},
 \]
 where \(\Omega(X)=\frac2\pi(X\arcsin X+\sqrt{1-X^2})\) for \(|X|\leq1\), and \(\Omega(X)=|X|\) otherwise.''',
 r'''The corrected coordinates and the exterior branch are checked against the 1977 paper. Their normalization has half the coordinates used in many later accounts.''',
 cls='A',fate=r'''This is \citet[Theorem~1, pp.~1024--1025]{vershikkerov1977asymptotics}, received December 1976 and published in 1977.''',
 status='the limit-shape theorem is established with these conventions.',
 literal='false as written',development='annotated',refs=VK)

item(415,'P000701','theorem','Almost-sure convergence along coherent paths',
 r'''The notes separately assert convergence almost everywhere for infinite diagrams, interpreted as paths.''',
 r'''For almost every infinite path under the coherent Plancherel measure, the uniformly rescaled boundary at level \(n\) converges uniformly to \(\Omega\). The assertion uses that coupling of the marginals, not an unspecified coupling of independent samples.''',
 r'''The ambient probability space is made explicit.''',
 cls='A',fate=r'''This is \citet[Theorem~2, p.~1025]{vershikkerov1977asymptotics}.''',
 status='almost-sure pathwise convergence is established.',refs=VK)

ulam_first=item(415,'P000701','theorem','Asymptotic first-row length',
 r'''The displayed corollary has \(\lambda_1/(2\sqrt n)\) near one and is called a solution of Ulam's problem.''',
 r'''For every \(\varepsilon>0\),
 \(\mathrm{Pl}_n\{|\lambda_1/(2\sqrt n)-1|<\varepsilon\}\to1\). The same first-order statement holds for the first column by transposition.''',
 r'''The missing terminal probability limit is supplied. Uniform boundary convergence alone does not control arbitrarily thin outer rows; the original proof also invokes a bound on expected first-row length.''',
 cls='A',fate=r'''See \citet[Corollary~1 and its proof, p.~1026]{vershikkerov1977asymptotics}.''',
 status='the first-order law is proved; it is not itself a fluctuation theorem.',
 problem='GP-1976-25',refs=VK)

item(415,'P000701','claim','The proposed white-noise central limit theorem',
 r'''The notes say \ru{Уклонения дают белый шум} and display fourth roots in both the argument and prefactor of an uncentered boundary functional; the test-function class and limiting distribution are unspecified.''',
 r'''A verified later formulation uses full rotated coordinates \(x=2X\), profile \(\bar\lambda_n(x)=2n^{-1/2}\widetilde\lambda(\sqrt n x/2)\), and \(\Omega_{\rm full}(x)=2\Omega(x/2)\). Put \(\Delta_n(x)=\frac{\sqrt n}{2}(\bar\lambda_n(x)-\Omega_{\rm full}(x))\). For any finite collection of polynomials \(p\), their integrals against \(\Delta_n\) converge jointly to those against the generalized Gaussian field
 \[
 \Delta(2\cos\theta)=\frac1\pi\sum_{k\geq2}\frac{\xi_k}{\sqrt k}\sin(k\theta),\qquad 0<\theta<\pi,
 \]
 with independent standard Gaussian \(\xi_k\). This field is not spatial white noise.''',
 r'''This is a later mathematically precise substitute, not a transcription repair or a claim that the 1977 speaker proved Kerov's theorem. The mode weights \(k^{-1/2}\), the vanishing area fluctuation, and polynomial-test topology are part of the correction.''',
 cls='B',fate=r'''Kerov announced the central limit theorem in 1993. \citet[Introduction, Theorem~7.1, and \S9]{ivanovolshanski2002kerov} give a full account, published in the 2002 volume and posted to arXiv in 2003; their introduction distinguishes the 1993 announcement and 1999 unpublished notes.''',
 status='the later generalized-Gaussian theorem is proved; the notebook fourth-root formula is not a correct statement of it.',
 literal='false as written',match='partial',refs=CLT,development='annotated')

item(415,'P000701','remark','An unidentified stationarity assertion',
 r'''The words \ru{марковость и стационарность проверяются} immediately follow the fluctuation formula, without naming the process or action.''',
 r'''Plancherel growth is Markov with the transition probabilities above, but the unrescaled shape process is not stationary: the number of cells is deterministically \(n\). A stationary process of rescaled fluctuations would require an additional time parametrization and an identified law, neither of which is given.''',
 r'''The known Markov construction does not identify what stationarity meant in this position on the page.''',
 cls='F',fate=r'''The path construction is checked in \citet[p.~1025]{vershikkerov1977asymptotics}; the fluctuation source \citet[\S7]{ivanovolshanski2002kerov} does not identify this notebook sentence.''',
 status='the Markov part has a precise interpretation, while the stationarity claim remains unidentified.',
 literal='not determinable',match='partial',refs=VK+CLT,confidence='medium')

item(415,'P000701','method','Row insertion connects permutations and Plancherel diagrams',
 r'''A bumping map into diagrams is credited to Knuth (1970) and a 1961 author written as Shenstead.''',
 r'''Schensted insertion associates to a permutation of \(n\) a pair of standard tableaux of the same shape \(\lambda\). This correspondence is bijective, so a uniform permutation has insertion shape distributed by \(d_\lambda^2/n!\). Its longest increasing subsequence has length \(\lambda_1\).''',
 r'''The 1961 author is C. Schensted. Knuth's 1970 paper extends the correspondence; the distinction between a pair of tableaux and just a diagram is restored.''',
 fate=r'''See \citet[Theorems~1--3]{schensted1961longest} and \citet[\S\S2--3]{knuth1970permutations}.''',
 status='the classical insertion mechanism exactly transfers the Plancherel law to increasing subsequences.',
 literal='correct with missing hypotheses',refs=['schensted1961longest','knuth1970permutations'])

ulam_sample=item(415,'P000701','question',"Ulam's problem for a random real sequence",
 r'''For uniform \(x_i\in[0,1]\), the notes ask for the greatest increasing-subsequence length and state \(2\sqrt n\). The displayed maximum is over \(r\), but the subsequence indices end at \(n\).''',
 r'''Let \(X_1,\ldots,X_n\) be independent uniform random variables on \([0,1]\), and let \(L_n=\max\{r:\exists i_1<\cdots<i_r,\ X_{i_1}<\cdots<X_{i_r}\}\). Then \(L_n/(2\sqrt n)\to1\) in probability. The same holds for any independent identically distributed continuous law, since its ranks form a uniform permutation.''',
 r'''Independence, continuity, and the terminal index \(r\) are supplied. With continuous laws, strict and weak inequalities agree almost surely.''',
 cls='A',fate=r'''The uniform version is \citet[Corollary~2, p.~1027]{vershikkerov1977asymptotics}; the rank reduction uses \citet[Theorems~1 and 3]{schensted1961longest}.''',
 status='the first-order Ulam problem is solved.',
 literal='correct with missing hypotheses',problem='GP-1976-25',refs=VK+['schensted1961longest'])

problem('GP-1976-24','Counting Young-graph paths between prescribed endpoints',
 r'''Given \(\mu\subseteq\lambda\), count saturated Young-graph paths from \(\mu\) to \(\lambda\), equivalently compute the multiplicity of \(V^\mu\) in \(V^\lambda|_{S_{|\mu|}}\).''',
 [skew_id],r'''As of November 2026: the count is the skew-tableau number \(f^{\lambda/\mu}\), given exactly by the classical Jacobi--Trudi/Aitken determinant. The notebook states no further asymptotic or positivity demand. The checked later derivation is \citet[equation~(1.2)]{stanley2011skew}.''',VO+['stanley2011skew'])
problem('GP-1976-25','Ulam asymptotics and the Plancherel first row',
 r'''For a uniform permutation, or the ranks of an independent continuous sample, determine the leading asymptotic longest increasing-subsequence length.''',
 [ulam_first,ulam_sample],r'''As of November 2026: \(L_n/(2\sqrt n)\to1\) in probability. This is the 1977 first-order result of \citet[Corollaries~1--2]{vershikkerov1977asymptotics}; the separate fluctuation discussion is not folded into this solved question.''',VK+['schensted1961longest'])
correction('P000699','record415 date','Catalogue 4 April 1977','28 March 1977; retain catalogue date separately',
 'The PNG has a single clear 28/III-77 heading, Gelfand intervention, then Vershik heading on the same page with no new date.','both','provenance')
correction('P000700','hook formula attribution','1955','1954',
 'The Frame, Robinson and Thrall publisher record dates Canadian Journal of Mathematics, volume 6, to 1954.','both','faithful_error')
correction('P000700','hook length','cells to the right and below','include the distinguished cell itself',
 'The displayed hook formula requires h=arm+leg+1; otherwise a removable cell would have length0.','both','ambiguity')
correction('P000700','branching sentence','every irreducible of S(n-1) occurs once','only the immediate predecessor diagrams occur once',
 'The next notebook line specifies predecessor diagrams; Young branching theorem.','both','faithful_error')
correction('P000700','regular representation','functions on S^n','functions on S_n',
 'Context is the finite symmetric group and its n! dimensional regular representation.','both','transcription')
correction('P000701','rotated coordinates','X=(x+y)/2; Y=(x-y)/2','X=(x-y)/2; Y=(x+y)/2 for the stated graph normalization',
 'PNG confirms the transcribed sum/difference; Vershik--Kerov1977p1024 has the corrected order.','both','faithful_error')
correction('P000701','limit-shape formula','interior arcsine formula alone','add Omega(X)=|X| for |X|>1',
 'The real square root is defined only on[-1,1]; the1977paper gives both branches.','both','faithful_error')
correction('P000701','fluctuation claim','white noise; fourth-root scaled uncentered functional','not an identified valid CLT; use a separately labelled later Kerov Gaussian-field theorem',
 'Both radical indices 4 are visible on the PNG. Ivanov--Olshanski, Theorem 7.1, uses centered profile fluctuations and a generalized Gaussian field with nonwhite covariance.','both','faithful_error')
correction('P000701','subsequence definition','i_1<...<i_n inside max over r','i_1<...<i_r',
 'The scan confirms n; r is the length being maximized.','both','faithful_error')
correction('P000701','1961 author','Shenstead','Schensted',
 'The cited 1961 Canadian Journal paper is C. Schensted, Longest Increasing and Decreasing Subsequences.','both','faithful_error')
checkpoint()

talk(417,'1977-04-04','A. Tyurin','P000702-P000704',
 'Packets of flat representations and exponential and Schwarzian periods',
 r'''The scan identifies only A. Tyurin; the catalogue gives A. S., whereas the exactly matching 1977 paper and 1978 survey are by A. N. Tyurin. This identification is made from the publications, not from an expanded manuscript initial. The talk compares flat representations having isomorphic underlying holomorphic bundles, explicitly solves the rank-one packet problem by logarithmic differentials, and turns to Schwarzian derivatives and projective monodromy. The GL(n) packet dimension in the notes is the fixed-determinant dimension, and the universal assertion about any two irreducible representations is false, already for unitary characters. Both require mathematical annotations rather than silent transcription repairs.''',
 catalogue_speaker='A. S. Tyurin',identified_speaker='A. N. Tyurin')

item(417,'P000702','definition','The marked surface group',
 r'''The group \(FG_g\) has generators \(a_1,\ldots,a_g,b_1,\ldots,b_g\) and relation \(\prod_i[a_i,b_i]=1\).''',
 r'''For a compact connected oriented surface \(\Sigma_g\), this is a presentation of \(\pi_1(\Sigma_g)\). A marked Riemann surface specifies an identification of its fundamental group with this fixed group; the orientation determines the integral intersection form on its abelianization.''',
 r'''Marking matters because the same abstract representations are compared while the complex structure varies.''',
 fate=r'''See \citet[Ch.~II, \S2, equation~(2.2.6) and Definition~2.2.6]{tyurin1978periods}. The survey was received 19 April 1977 and published in the 1978 volume; its introduction dates the underlying lectures to 1973.''',
 status='the group and marking are standard.',literal='correct',refs=TYURIN)

item(417,'P000702','claim','Dimension of the general linear character variety',
 r'''The notes subtract the relation and conjugacy dimensions to obtain \(2(g-1)n^2+2\), calling the quotient an algebraic variety with singularities.''',
 r'''For \(g\geq2\), the irreducible locus of
 \(\operatorname{Hom}(\pi_1(\Sigma_g),GL_n(\mathbb C))/\!/GL_n(\mathbb C)\)
 is smooth of complex dimension \(2(g-1)n^2+2\). A point of the affine quotient represents a semisimple conjugacy class; singular and reducible strata are not covered by the displayed tangent-dimension count.''',
 r'''At an irreducible representation, \(H^0(\Sigma_g,\operatorname{ad}\rho)\) and \(H^2\) each have dimension one. Euler characteristic gives \(\dim H^1=2+(2g-2)n^2\). This cohomological calculation checks the notebook's generic parameter count.''',
 fate=r'''The flat-bundle and representation interpretation is \citet[Ch.~II, \S2]{tyurin1978periods}; the explicit tangent-space argument is an editorial reconstruction of the familiar generic count.''',
 status='the generic dimension is correct; the unrestricted singular quotient needs the stated qualification.',
 match='partial',refs=TYURIN,development='annotated')

item(417,'P000702','construction','The flat bundle associated to a representation',
 r'''The notes form \(E_\rho=U(X)\times V^n/\pi_1(X)\) and declare two representations analytically equivalent when their underlying bundles are isomorphic.''',
 r'''For a representation \(\rho:\pi_1(X)\to GL_n(\mathbb C)\), quotient the trivial bundle on the universal cover by the compatible deck and linear action. Constant transition functions give a flat connection and a holomorphic bundle \(E_\rho\). Forgetting the flat connection sends the conjugacy class of \(\rho\) to the holomorphic isomorphism class of \(E_\rho\).''',
 r'''The deck-action convention must be used consistently; changing it changes \(\rho\) to the corresponding inverse convention, not the underlying correspondence.''',
 fate=r'''This is \citet[Ch.~II, \S2, equations~(2.2.3)--(2.2.5) and Definition~2.2.7]{tyurin1978periods}.''',
 status='the construction and equivalence relation are standard.',literal='correct',refs=TYURIN)

item(417,'P000702','definition','A packet is a fiber of forgetting the flat structure',
 r'''For fixed \(X,E\), a packet \(H(X,E)\) is a subset of the representation space.''',
 r'''\(H(X,E)\) consists of conjugacy classes of representations whose associated holomorphic bundle is isomorphic to \(E\). Equivalently, it is the set of holomorphic connections on \(E\), modulo the action of \(\operatorname{Aut}_{\rm hol}(E)\). On a complex curve a holomorphic connection is flat because its holomorphic curvature is a two-form.''',
 r'''The quotient by bundle automorphisms is necessary before calling this a space of representation classes.''',
 fate=r'''See \citet[Ch.~II, Definition~2.2.8 and Exercises~1--5 to \S2, pp.~199, 204]{tyurin1978periods}. The survey explicitly refers the connection theory back to Atiyah's earlier work.''',
 status='the packet interpretation is established.',refs=TYURIN)

item(417,'P000702','claim','The packet dimension mixes GL(n) and fixed determinant',
 r'''An arrow labels \(H(X,E)\) as an affine space of dimension \((n^2-1)(g-1)\), although the ambient representations are in \(GL_n\).''',
 r'''If \(E\) is a stable degree-zero rank-\(n\) bundle on a compact curve of genus \(g\geq2\), its holomorphic connections form an affine torsor for \(H^0(X,\operatorname{End}E\otimes K_X)\), of dimension \(n^2(g-1)+1\). Scalar automorphisms act trivially. If one also fixes the connection on \(\det E\), the modeling space is \(H^0(X,\operatorname{End}_0E\otimes K_X)\), of dimension \((n^2-1)(g-1)\).''',
 r'''The dimensions follow from Riemann--Roch and \(h^0(\operatorname{End}E)=1\). In rank one the GL(1) packet has dimension \(g\), whereas the notebook formula gives zero; this directly exposes the missing determinant constraint.''',
 fate=r'''The affine difference of connections and the dimension exercise are \citet[Ch.~II, \S2, Exercises~1 and 8, p.~204]{tyurin1978periods}. The corrected Riemann--Roch calculation is supplied here.''',
 status='the displayed formula is valid only for the fixed-determinant connection problem.',
 literal='false as written',match='partial',refs=TYURIN,development='annotated')

item(417,'P000702','question','An ambiguous question about related bundles and representations',
 r'''A short line asks \ru{Расслоения связ. \(\Rightarrow\) что можно сказать о предст.?}; the word abbreviated as \ru{связ.} is uncertain.''',
 r'''No specific relation between the two bundles is given. If holomorphic isomorphism is intended, the question asks about membership in a common packet; if deformation or another relation is intended, the notebook does not supply a precise condition or requested conclusion.''',
 r'''The surrounding definition suggests packet equivalence, but that suggestion is not substituted for the uncertain word.''',
 cls='F',fate=r'''The packet framework of \citet[Definitions~2.2.7--2.2.8]{tyurin1978periods} is relevant, but does not identify this isolated question's exact quantifiers.''',
 status='the local wording remains insufficient for a separate problem.',
 literal='not determinable',match='thematic only',refs=TYURIN,confidence='low')

item(417,'P000702','claim','Any two irreducibles need not become analytically equivalent',
 r'''The manuscript states \ru{Любые два неприв. предст. эквивал. относит. нек-рой рим. пов.} and explains that they enter one packet.''',
 r'''The literal assertion is false. Fix \(g\geq2\), \(0<\theta<2\pi\), and rank-one unitary characters \(\chi_0=1\), \(\chi_1(a_1)=e^{i\theta}\), with \(\chi_1=1\) on the remaining generators. Both are irreducible and satisfy the surface relation, but for every complex structure on \(\Sigma_g\) their underlying holomorphic line bundles are nonisomorphic.''',
 r'''Proof: an isomorphism would give a nowhere-zero holomorphic section of the unitary flat line bundle with character \(\chi_1\chi_0^{-1}\). In unitary parallel local frames, its log norm is harmonic; compactness makes it constant. Each local holomorphic coefficient then has constant modulus, hence is constant. The section is parallel, forcing the character to be trivial, a contradiction. An independent universal-cover derivation reaches the same conclusion. This is a correction of a false literal assertion, not a new open problem.''',
 fate=r'''\citet[Ch.~II, \S2, Exercise~10, p.~204]{tyurin1978periods} states that a packet cannot contain two distinct unitary representation classes. The 1973-lecture provenance establishes that the surrounding theory was not new in the 1978 printing; no claim is made that this exact notebook sentence is reproduced in the publication.''',
 status='the universal assertion is disproved by the checked rank-one example.',
 literal='false as written',match='partial',refs=TYURIN,development='annotated')

item(417,'P000702','claim','The affine fibration exists only over an appropriate bundle locus',
 r'''The notes draw \(R_C\to S_n(X)\), label it an affine bundle, and call \(S_n(X)\) the moduli of bundles.''',
 r'''Let \(X\) be a smooth projective complex curve of genus \(g\geq2\). Over the moduli of stable degree-zero bundles, forgetting a holomorphic connection gives a torsor modeled on the cotangent bundle, with fiber dimension \(n^2(g-1)+1\); fixing determinant and its connection gives the trace-free version. The whole character variety does not map to stable-bundle moduli in this way: an irreducible flat bundle can have unstable underlying holomorphic bundle.''',
 r'''This is a restricted de Rham moduli statement. In a presentation using the Betti character variety, Riemann--Hilbert is analytic, so the notebook does not establish an algebraic affine bundle on the full Betti quotient.''',
 fate=r'''The difference-of-connections model is \citet[Ch.~II, \S2, Exercises~1--5]{tyurin1978periods}; the moduli-locus and torsor formulation make the suppressed hypotheses explicit.''',
 status='the restricted torsor picture is standard; the global unrestricted diagram is too strong.',
 literal='false as written',match='partial',refs=TYURIN,development='annotated')

line_packet=item(417,'P000703','problem','Describe the packet of a fixed line bundle',
 r'''The typical problem is to describe \(H(X,L)\subset\mathbb C^{*\,2g}\) for a fixed one-dimensional holomorphic bundle.''',
 r'''For a compact connected Riemann surface \(X\), the packet is empty unless \(\deg L=0\). If \(\deg L=0\), choose one flat connection \(\nabla_0\); all others are \(\nabla_0+\eta\), \(\eta\in H^0(X,K_X)\). With a fixed sign convention for periods, the character set is a coset
 \[
 H(X,L)=\chi_0\left\{\gamma\longmapsto
       \exp\!\int_\gamma\eta:\eta\in H^0(X,K_X)\right\}.
 \]''',
 r'''Degree zero, the additive connection parameter, and the period convention are supplied. The next notebook calculations give an explicit divisor version of this description.''',
 fate=r'''The precise packet question is answered by \citet[Ch.~II, \S2, Exercises~1--5 and 12; \S3]{tyurin1978periods}; the logarithmic construction is also the introduction to \citet{tyurin1977periods}.''',
 status='the rank-one packet is explicitly described; there is no residual open inverse problem here.',
 problem='GP-1976-26',refs=TYURIN+['tyurin1977periods'])

item(417,'P000703','theorem','Constant transition functions and degree zero',
 r'''The line bundle is represented by a cocycle in \(\mathcal O_X^*\), and comes from a character if a representative has constant transition functions.''',
 r'''The forgetful map \(H^1(X,\mathbb C^*)\to H^1(X,\mathcal O_X^*)\) has image \(\operatorname{Pic}^0(X)\). Thus a holomorphic line bundle on a compact Riemann surface admits a flat structure exactly when its degree is zero; many flat structures can have the same holomorphic image.''',
 r'''This is a statement about existence of a constant cocycle representative, not that an arbitrarily chosen holomorphic transition cocycle is already constant.''',
 fate=r'''See \citet[Ch.~II, \S2, Definitions~2.2.1--2.2.2 and Exercise~5]{tyurin1978periods}.''',
 status='the line-bundle criterion is established.',refs=TYURIN)

item(417,'P000703','construction','A meromorphic section gives an integral-residue differential',
 r'''When transition functions are constant, the local \(df_i/f_i\) glue to one meromorphic differential. Its poles are simple and its residues are integers.''',
 r'''For a nonzero meromorphic section of a flat line bundle, \(\omega=df_i/f_i\) is global. At a zero or pole of local order \(m\in\mathbb Z\), it has residue \(m\). Hence \(\sum_x\operatorname{Res}_x\omega=0\), and its residue divisor is the divisor of that section, of degree zero.''',
 r'''The residue sum and degree condition use compactness. The notation \([\omega]\) here records the residue divisor, not the full differential.''',
 fate=r'''This construction is explicitly given in \citet[Introduction, pp.~1359--1360]{tyurin1977periods} and \citet[Ch.~II, \S3]{tyurin1978periods}.''',
 status='the logarithmic differential construction is classical and exact.',literal='correct',refs=['tyurin1977periods']+TYURIN)

item(417,'P000703','construction','Changing a section changes the residue divisor by a principal divisor',
 r'''The notes say that two representatives give equivalent divisors.''',
 r'''Two nonzero meromorphic sections of the same holomorphic line bundle differ by a nonzero meromorphic function \(h\). Their divisors differ by \(\operatorname{div}(h)\); for the same flat connection the associated differentials differ by \(dh/h\). Exponentiated periods of \(dh/h\) equal one.''',
 r'''Holding the flat connection fixed is essential for the displayed differential comparison.''',
 fate=r'''This is the divisor and exponential-integral correspondence in \citet[Introduction]{tyurin1977periods}.''',
 status='the gauge and divisor equivalence is established.',refs=['tyurin1977periods'])

item(417,'P000703','construction','Constructing every character in a packet from a divisor',
 r'''Fix a divisor, construct a differential with its principal parts, and solve \(df/f=\omega+\omega_0\) on the universal cover, with \(\omega_0\) holomorphic.''',
 r'''Let \(D=\sum m_pp\) be a degree-zero divisor representing \(L\). There exists a meromorphic one-form with only simple poles of residues \(m_p\); all such forms differ by \(H^0(X,K_X)\). Their exponential integrals are meromorphic on \(U(X)\), because integer residues make the local exponent single-valued at each pole. Their deck multipliers give exactly \(H(X,L)\), in a compatible divisor/character convention.''',
 r'''The residue theorem's degree-zero condition is the missing existence hypothesis. Local meromorphic integrability of this first-order equation really does follow from the integer residues.''',
 fate=r'''See \citet[Introduction, pp.~1359--1360]{tyurin1977periods} and \citet[Ch.~II, \S3]{tyurin1978periods}.''',
 status='this solves the stated rank-one packet problem.',
 problem='GP-1976-26',refs=['tyurin1977periods']+TYURIN)

item(417,'P000703','construction','The trivial packet is the exponential of holomorphic periods',
 r'''The zero fiber is described as exponentials of primitives of holomorphic differentials.''',
 r'''The homomorphism \(H^0(X,K_X)\to\operatorname{Hom}(\pi_1(X),\mathbb C^*)\), \(\eta\mapsto(\gamma\mapsto e^{\int_\gamma\eta})\), has trivial kernel and image the packet of \(\mathcal O_X\). Indeed, a kernel element gives a single-valued nowhere-zero holomorphic function \(e^{\int\eta}\) on compact \(X\), hence a constant, so \(\eta=0\). Every other nonempty line packet is a coset.''',
 r'''The injectivity proof identifies the affine dimension \(g\) and provides a second check on the erroneous GL(1) dimension in P000702.''',
 fate=r'''Compare \citet[Ch.~II, \S2, Exercise~12(a), pp.~204--205]{tyurin1978periods}.''',
 status='the trivial packet and its translates are explicitly understood.',literal='correct',refs=TYURIN)

item(417,'P000703','theorem','A marked character packet determines the curve through Torelli',
 r'''The notes claim that the surface can be recovered uniquely from a packet, by a theorem written as Terelli.''',
 r'''Regard a nonempty packet as its embedded analytic subset in the character torus of the fixed oriented marked surface. Translating it to the identity gives the trivial packet; its tangent space identifies \(H^{1,0}(X)\subset H^1(\Sigma_g,\mathbb C)\). Together with the integral lattice and intersection pairing this gives the principally polarized Jacobian, which determines \(X\) up to isomorphism by Torelli.''',
 r'''The embedding, integral marking, and polarization are indispensable. An abstract affine space of dimension \(g\), or an unpolarized torus without the retained data, is not the claimed invariant.''',
 fate=r'''This is the content of \citet[Ch.~II, \S2, Exercises~12--13, pp.~204--205]{tyurin1978periods}.''',
 status='the Torelli conclusion is valid with the retained marking and polarization.',
 refs=TYURIN,problem='GP-1976-26')

item(417,'P000703','construction','Unitary characters select a unique point of each line packet',
 r'''A small diagram marks unitary characters beside the Jacobian family; its circular central symbol is uncertain.''',
 r'''The map \(\operatorname{Hom}(\pi_1(X),U(1))\to\operatorname{Pic}^0(X)\) is a bijection of real tori. Thus each degree-zero line packet contains exactly one unitary character. This is a real analytic selection, not a holomorphic section of the complex character torus.''',
 r'''The precise assertion reconstructs the diagram using rank-one unitary flat-bundle theory; the uncertain central glyph is not identified as a theta divisor.''',
 fate=r'''Uniqueness is \citet[Ch.~II, \S2, Exercise~10]{tyurin1978periods}; the adjacent Jacobian construction in Exercise~12 supplies the line-bundle setting.''',
 status='the unitary character parametrization is standard.',match='partial',refs=TYURIN)

item(417,'P000703','definition','Schwarzian derivative and its chain rule',
 r'''The notes define \(S(f)=(f''/f')'-\frac12(f''/f')^2\) and give its composition rule, with zero Schwarzian for fractional-linear coordinate changes.''',
 r'''For a locally univalent holomorphic map,
 \[
 S_z(f)=\frac{f^{(3)}}{f'}-\frac32\left(\frac{f''}{f'}\right)^2,\qquad
 S_t(f\circ g)=(S_z(f)\circ g)(g')^2+S_t(g).
 \]
 A Möbius map has zero Schwarzian; postcomposition by one leaves \(S_z(f)\) unchanged.''',
 r'''Local univalence is needed away from the meromorphic singularities considered next.''',
 fate=r'''See \citet[\S1, properties~1--2]{tyurin1977periods} and \citet[Ch.~I, \S2]{tyurin1978periods}.''',
 status='the classical chain rule is exact.',literal='correct',refs=['tyurin1977periods']+TYURIN)

item(417,'P000703','claim','Schwarzians require a projective atlas to become quadratic differentials',
 r'''After the chain rule, the notes say that general quadratic differentials result.''',
 r'''Local Schwarzians transform as a projective connection under arbitrary holomorphic coordinate changes. After choosing a projective atlas, whose transition functions are Möbius, the extra Schwarzian term vanishes and the resulting expressions can be compared as quadratic differentials. The difference of two projective connections is intrinsically a quadratic differential.''',
 r'''Choosing the projective structure is essential; the notebook suppresses that choice.''',
 fate=r'''The projective-atlas assumption is explicit in \citet[Introduction and Definition~1.2]{tyurin1977periods}.''',
 status='the claim is correct with the projective-coordinate hypothesis.',
 match='exact',refs=['tyurin1977periods'],development='annotated')

item(417,'P000703-P000704','claim','Double poles and the leading coefficient called a residue',
 r'''The margin allows poles of order at most two and calls the coefficient of \((dz/z)^2\) a residue.''',
 r'''If a meromorphic map has local degree \(m\geq1\), its Schwarzian is
 \[
 S_z(f)=\frac{1-m^2}{2z^2}+O(z^{-1}).
 \]
 For a quadratic differential with a double pole, the coefficient \(a\) of \(a(dz/z)^2\) is invariant under a local holomorphic change of parameter. This is not the residue of a one-form.''',
 r'''This is a necessary local property of a meromorphic Schwarzian, not a sufficient criterion for an arbitrary quadratic differential to have a meromorphic Schwarzian primitive. Resonant logarithmic terms require additional conditions.''',
 fate=r'''The terminology and necessary coefficient are in \citet[\S1, property~4 and equations~(1.3)--(1.4)]{tyurin1977periods}. The stronger sufficiency claim in its following property~5 is not used here; it does not match anything explicitly asserted in the notebook.''',
 status='the leading coefficient statement is exact; no converse is inferred.',
 refs=['tyurin1977periods'],development='annotated')

item(417,'P000704','construction','Schwarzian integration and projective monodromy',
 r'''The scan, in a diagram omitted from the plain transcription, reads \(f(g(u))=\rho(g)(f(u))\) and says that this reconstructs \(\rho\).''',
 r'''On a Riemann surface with a fixed projective atlas, a holomorphic quadratic differential locally gives \(S(f)=q\), equivalently \(f=y_1/y_2\) for independent solutions of \(y''+\tfrac12q\,y=0\). Analytic continuation on the universal cover produces a locally univalent developing map and a conjugacy class \(\rho:\pi_1(X)\to PGL_2(\mathbb C)\) satisfying the displayed equivariance. For meromorphic data, continuation first gives monodromy of the punctured surface; it descends across poles only under the requisite local meromorphic integrability conditions.''',
 r'''The second-order equation and the distinction between the closed and punctured surface make the notebook's abbreviated reconstruction precise. The stronger uniqueness theorem of the 1977 paper is not imported as an occurrence absent from these pages.''',
 fate=r'''See \citet[\S1, Definitions~1.1--1.3 and equation~(1.6)]{tyurin1977periods} and \citet[Ch.~II, equation~(2.2.7)]{tyurin1978periods}.''',
 status='the projective monodromy construction is established with the indicated local hypotheses.',
 refs=['tyurin1977periods']+TYURIN)

problem('GP-1976-26','Description and Torelli information of rank-one representation packets',
 r'''For a fixed marked compact Riemann surface \(X\) and degree-zero line bundle \(L\), describe all characters with underlying holomorphic bundle \(L\), and determine the information about \(X\) retained by that embedded packet.''',
 [x['id'] for x in items if x['record']==417 and x['problem']=='GP-1976-26'],
 r'''As of November 2026: the packet is a coset of the exponential of holomorphic periods; its embedded tangent space, integral marking, and intersection pairing recover the principally polarized Jacobian and hence the curve. These are the classical constructions and exercises in \citet[Ch.~II, \S\S2--3]{tyurin1978periods}.''',TYURIN+['tyurin1977periods'])
correction('P000702','speaker initials','Catalogue A.S.Tyurin','Scan A.Tyurin; publication identification A.N.Tyurin',
 'The scan abbreviates the first name only. Both exactly matching primary papers are signed A.N.Tyurin; the supplied catalogue initials conflict.','both','provenance')
correction('P000702','packet dimension in GL(n)',r'(n^2-1)(g-1)',r'n^2(g-1)+1; the displayed value is for a fixed determinant connection',
 'Connections on a stable degree-zero bundle form a torsor for H0(End(E)K); Riemann--Roch. Rank1 gives g, not0.','both','faithful_error')
correction('P000702','any two irreducible representations','any two are in one packet for some Riemann surface','false: distinct unitary characters cannot be in one packet for any complex structure',
 'Unitary flat Hom line has no nowhere-zero holomorphic section unless its character is trivial; Tyurin (1978), Chapter II, section 2, Exercise 10. Full proof independently checked.','both','faithful_error')
correction('P000702','affine bundle diagram','whole character variety to moduli of bundles is an affine bundle','restrict to stable degree-zero underlying bundles, and specify determinant conventions',
 'Packet automorphisms and unstable underlying bundles prevent the unrestricted claim.','both','faithful_error')
correction('P000703','section notation',r'f_i on U_j',r'f_i on U_i',
 'The cocycle equation and local restriction df_i/f_i on U_i fix the index; handwritten subscript is ambiguous.','both','ambiguity')
correction('P000703','construct a differential with specified divisor','arbitrary divisor','degree-zero divisor for a compact surface',
 'Sum of residues of a meromorphic differential on a compact Riemann surface is zero.','both','faithful_error')
correction('P000703','Torelli name','Terelli','Torelli',
 'The notebook claim and matching Tyurin (1978), Chapter II, section 2, Exercise 13, explicitly invoke the Torelli theorem.','both','faithful_error')
correction('P000703','Schwarzian gluing','general quadratic differentials','fix a projective atlas; otherwise a projective connection',
 'The written chain rule includes the extra Schwarzian term; Tyurin (1977), Introduction, assumes Möbius coordinate changes.','both','faithful_error')
correction('P000704','bottom monodromy diagram','diagram only; equation absent from plain text',r'f(g(u))=\rho(g)(f(u))',
 'The actual PNG contains this equation and a phrase saying that rho is thereby recovered. It belongs to the Tyurin continuation.','both','transcription')
checkpoint()

talk(418,'','','P000705-P000706','Catalogue heading for 1977–78 and adjacent next-year context',
 r'''This catalogue record marks the 1977--78 academic-year boundary; it is retained as a heading, with no fabricated 1976--77 mathematical occurrences. On P000705 the source starts the seminar's thirty-fourth year and proposes noncommutative algebraic geometry in connection with Bernstein, I.~M.~Gelfand and S.~I.~Gelfand. A distinct heading then names V.~Drinfeld and Atiyah's work on Yang--Mills equations. P000705--P000706 contain the beginning of that adjacent talk: self-dual curvature on \(S^4\), conformal invariance of the Hodge star on two-forms, a heuristic quantization/determinant discussion, the twistor map \(\mathbb{CP}^3\to\mathbb{HP}^1=S^4\) with fibers \(\mathbb{CP}^1\), and a correspondence with bundles trivial on twistor fibers, followed by the quaternionic real structure. These adjacent contents are inventoried for coverage and must be catalogued with the next academic year. The visible date is transcribed as 5/IV-77, in tension with the boundary; the exact month is left unresolved rather than silently changed to September.''',
 kind='heading',scope='next-year boundary and adjacent context; no 1976 items',manuscript_date_text='5/IV-77 (month unresolved)',academic_year='1977-78')
correction('P000705-P000706','year and talk boundary','included pages after 1976--77 Tyurin record','next-academic-year heading with a separately named adjacent Drinfeld talk',
 'Catalogue record 418 is the 1977--78 heading; P000705 explicitly marks the thirty-fourth seminar year and names V. Drinfeld in a new heading.','both','provenance')
correction('P000705','visible meeting date','5/IV-77','preserve the visible reading; exact month unresolved',
 'The transcribed IV is compatible with visible strokes but conflicts with the new-year boundary; replacing it by IX would be an inference, not a secure scan reading.','both','ambiguity')
checkpoint()


# Exact recurrence of the scalar filtered-module mechanism; share the audited definition.
for it in items:
    if it['id']=='1976-412.3':
        it['problem']='GP-1975-26'
        it['reconstruction']+=r''' The scalar specialization \(\ell=1\) is the filtered-module reconstruction mechanism in GP-1975-26; the occurrence does not replace its pointed-curve and local-data hypotheses by a bare curve and bundle. Matrix coefficients and the later explicit nodal examples are additional scope, not a changed definition of that earlier problem.'''
shared=next(p for p in json.loads((WORK/'middle_problems.json').read_text()) if p['id']=='GP-1975-26')
shared['occurrences']=list(dict.fromkeys(shared['occurrences']+['1976-412.3']))
shared['refs']=list(dict.fromkeys(shared['refs']+MANIN))
problems.append(shared)
checkpoint()
print(json.dumps({'talks':len(talks),'items':len(items),'problems':len(problems),'classes':dict(Counter(x['class'] for x in items)),'by_record':dict(Counter(str(x['record']) for x in items)),'corrections':len(corrections)},indent=2))
