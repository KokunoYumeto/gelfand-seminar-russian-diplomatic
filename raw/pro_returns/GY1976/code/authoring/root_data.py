"""Author the record-437 contribution; source and publication checks are logged separately.

Run from the project workspace. The final merge uses these UTF-8 segment files.
No claim of research novelty is made by this data-authoring script.
"""
from pathlib import Path
import csv
import json
import re

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'work'
OUT.mkdir(exist_ok=True)
items = []

def add(kind, title, pages, notes, statement, cls, fate, status, refs,
        reconstruction='', literal='correct', match='exact',
        verification='read the result', confidence='high', problem='', speaker=''):
    d = dict(id=f'1977-437.{len(items)+1}', record=437, pages=pages, kind=kind,
             title=title, notes=notes, statement=statement,
             reconstruction=reconstruction, **{'class':cls}, fate=fate,
             present_status='As of 10 November 2026: '+status,
             literal_correctness=literal, publication_match=match,
             verification=verification, development='annotated' if reconstruction else 'none',
             problem=problem, worth='', refs=refs, confidence=confidence,
             area='Algebraic geometry and homological algebra',
             manuscript_date='1978-02-13', chronological_scope='outside 1976-77')
    if speaker:
        d['speaker']=speaker
    items.append(d)
    (OUT/'root_items.json').write_text(json.dumps(items, ensure_ascii=False, indent=2)+'\n')

BGG='bernsteingelfandgelfand1978bundles'
BEI='beilinson1978coherent'
EFS='eisenbudfloystadschreyer2003exterior'
SER='serre1955coherent'
STP='stacks2026projective'
STC='stacks2026projconstruction'

talks=[dict(record=437, date='1978-02-13', speaker='S. I. Gelfand',
    pages='P000753-P000756',
    title='Exterior-algebra modules and algebraic bundles (manuscript: 13 February 1978)',
    kind='talk', manuscript_date='1978-02-13', chronological_scope='outside 1976-77',
    summary=r'''\textbf{Provenance correction.} The supplied catalogue date, 13 February 1977, is corrected in the structured \texttt{date} field to the manuscript date, 13 February 1978; the catalogue value is preserved here and in the provenance ledger. The scan of P000753 unambiguously reads \ru{13/II--78 г.}; P000757 begins a new lecture, \ru{27/II--78 г.}. Thus this is a 1977--78 talk accidentally included in the requested package, not evidence for a 1976--77 announcement. The occurrence prefix \texttt{1977-437} follows the format rule that YEAR is the first year of the actual academic year. The requested record is retained in this package as an explicitly identified chronological appendix. P000752 is an adjacent physics tail; P000757--P000758 belong to the next, separately dated, S.~I.~Gelfand lecture. They are accounted for in the source ledger and corrections, without assigning their new content to record~437.

The talk explains how finite graded modules over an exterior algebra produce complexes on projective space. A fibrewise exactness condition singles out vector bundles; graded free summands disappear, and every bundle is represented uniquely up to stable module isomorphism. Twisting is expressed through a cosyzygy and a grading shift, followed by an outline of the inverse construction from large-twist sections. I.~M.~Gelfand calls for coherent sheaves and derived categories, and Serre's projective module--sheaf correspondence closes the surviving lecture. The exact publication is \citet[Theorem~1 and its remarks]{bernsteingelfandgelfand1978bundles}: received 10 January 1978, before the manuscript's lecture date, published in the 1978 Russian volume; the English translation bears a 1979 copyright imprint. A submission date is not, by itself, a verified date of public circulation. Class A here denotes subsequent publication of the current work; it does not assert discovery after the lecture. The modern derived equivalence is given there by Theorem~2, but is not silently attributed to the surviving lecture as a fully stated theorem.''')]
(OUT/'root_talks.json').write_text(json.dumps(talks,ensure_ascii=False,indent=2)+'\n')

add('remark','Topoi and derived categories as organizing concepts','P000753',
 r'I.~M.~Gelfand identifies \ru{Топос} and \ru{Производная категория} as two primary concepts of category theory.',
 r'This is a pedagogical judgement, not a theorem that category theory has precisely two basic notions. A Grothendieck topos is a category equivalent to sheaves of sets on a site; for an abelian category \(\mathcal A\), its derived category inverts quasi-isomorphisms of complexes.',
 'E',r'The frameworks predate this lecture: \citet[Expos\'e~IV]{sga41972topos} and \citet[Chapter~I]{hartshorne1966residues}.',
 'Both frameworks remain established; the notebook supplies no testable exclusivity claim.',
 ['sga41972topos','hartshorne1966residues'],
 reconstruction='The definitions clarify the two names; the evaluative word primary remains the speaker\'s judgement.',
 literal='not determinable', match='thematic only', verification='publisher metadata checked',speaker='I. M. Gelfand')

add('problem','Describe algebraic vector bundles on projective space','P000753-P000755',
 r'\ru{Задача: описать все алгебраические расслоения над} \(\mathbb P^n\), for example over \(\mathbb C\). The subsequent theorem specifies the intended description by exterior-algebra modules.',
 r'For each integer \(n\geq0\), describe the isomorphism classes of finite-rank algebraic vector bundles on \(\mathbb P^n_{\mathbb C}\). In the sense actually developed in the notes, the answer sought is a bijection with stable isomorphism classes of proper finite-dimensional graded \(\Lambda(\mathbb C^{n+1})\)-modules.',
 'A',r'Answered in this representation-theoretic sense by \citet[Theorem~1]{'+BGG+'}.',
 'The correspondence is established. It is not a numerical enumeration of all moduli spaces, and does not imply a solution of every later vector-bundle classification question.',[BGG],
 reconstruction='The meaning of describe is fixed by the theorem that follows, rather than by an unrecorded demand for a finite list of invariants.',
 problem='GP-1977-01')

add('definition','Projective space is the scalar quotient of a punctured vector space','P000753',
 r'\(\Xi\) is called affine space and \(\xi\sim\alpha\xi\), \(\alpha\in\mathbb C^*\), \(\xi\ne0\); the quotient is \(\mathbb P^n\).',
 r'Let \(\Xi\) be a complex vector space of dimension \(n+1\). Then \(\mathbb P(\Xi)=(\Xi\setminus\{0\})/\mathbb C^*\) parametrizes its one-dimensional vector subspaces. The chosen origin and linear structure are essential; a bare affine space does not carry the displayed scalar action canonically.',
 'E',r'Classical projective geometry; compare \citet[\S27.8]{'+STC+'}.',
 'Standard, with the puncture and dimension made explicit.',[STC],
 reconstruction='Replace the informal affine-space wording by a vector space and retain the explicit exclusion of zero.', literal='correct with missing hypotheses')

add('definition','The negatively graded exterior algebra','P000753',
 r'\(\Lambda=\{\xi_0,\ldots,\xi_n\mid\xi_i\xi_j+\xi_j\xi_i=0\}\), \(\dim\Lambda=2^{n+1}\), and \(\Lambda=\bigoplus_{k=0}^{n+1}\Lambda_{-k}\).',
 r'Over \(\mathbb C\), put \(\Lambda=\bigwedge\Xi\) with \(\deg\xi=-1\) for \(\xi\in\Xi\). Then \(\Lambda_{-k}=\bigwedge^k\Xi\), \(\dim\Lambda_{-k}=\binom{n+1}{k}\), and the total dimension is \(2^{n+1}\). In characteristic two one must impose \(\xi_i^2=0\) explicitly; the notes use characteristic zero.',
 'E',r'The algebra is classical; these conventions are also fixed in \citet[\S2]{'+BGG+'}.',
 'An established definition. The sign of the grading must be retained in subsequent shifts.',[BGG],
 reconstruction='The binomial dimensions and characteristic qualification spell out the displayed presentation.')

add('definition','Finite graded representations of the exterior algebra','P000753',
 r'Objects are \(V=\bigoplus_jV_j\), \(\dim V<\infty\), with \(\Lambda_{-k}V_j\subset V_{j-k}\).',
 r'A finite-dimensional graded left \(\Lambda\)-module has a finite-support \(\mathbb Z\)-grading and degree-zero module morphisms. For a generator \(\xi\), multiplication gives \(V_j\to V_{j-1}\). Both the module and every free summand used later are graded.',
 'E',r'Standard graded-module language, used in \citet[\S2]{'+BGG+'}.',
 'The grading is essential; ungraded stable equivalence would be a different assertion.',[BGG])

add('construction','A complex for every nonzero exterior generator','P000753',
 r'\(L_\xi(V)=\{\cdots\to V_1\xrightarrow{\xi}V_0\xrightarrow{\xi}V_{-1}\to\cdots\}\), because \(\xi^2=0\).',
 r'For \(\xi\in\Xi\setminus\{0\}\), let \(d_j(v)=\xi v\) on \(V_j\). Then \(d_{j-1}d_j=0\), and \(H_j(L_\xi(V))=\ker(d_j)/\operatorname{im}(d_{j+1})\). This is a bounded chain complex of finite-dimensional vector spaces.',
 'A',r'The family is part of \citet[\S2]{'+BGG+'}.',
 'A standard component of the BGG construction; the displayed differential is literally correct.',[BGG])

add('definition','Proper modules: fibre homology concentrated in degree zero','P000753',
 r'\(V\) is \ru{правильный} if \(H_i(L_\xi(V))=0\) for every \(\xi\ne0\) and every \(i\ne0\).',
 r'A finite-dimensional graded \(\Lambda\)-module is proper when each nonzero \(\xi\in\Xi\) gives homology only in degree zero. No requirement that \(H_0\) be nonzero is imposed: free modules are included.',
 'A',r'This is the condition called faithful in the English translation of \citet[\S2]{'+BGG+'}.',
 'Established. Here faithful is a translation of the special definition, not injectivity of the action homomorphism.',[BGG],
 reconstruction='The terminology must not be confused with a faithful representation in ordinary ring theory.')

add('claim','The Euler characteristic fixes the fibre rank','P000754',
 r'For proper \(V\), \(\dim H_0(L_\xi(V))\) is constant and equals \(\sum_i(-1)^i\dim V_i\).',
 r'For a bounded finite-dimensional complex, \[\sum_i(-1)^i\dim H_i=\sum_i(-1)^i\dim V_i.\] Thus properness implies \(\dim H_0(L_\xi(V))=\sum_i(-1)^i\dim V_i\), independently of nonzero \(\xi\).',
 'E',r'An elementary Euler-characteristic identity, used in the construction of \citet[\S2]{'+BGG+'}.',
 'Correct. Constant fibre dimension is one part of the vector-bundle argument, not a substitute for its algebraicity.',[BGG],
 reconstruction='For an independent check, write each dimension as boundary rank plus homology dimension plus the preceding boundary rank; the alternating boundary terms cancel.')

add('construction','The homology spaces form an algebraic vector bundle','P000754-P000755',
 r'The assignment \(\xi\mapsto H_0(L_\xi(V))\) is the same for \(\xi\) and \(\alpha\xi\); later \(\Phi(V)=H^0(\mathcal L(V))\) is defined.',
 r'For a proper module over \(\Lambda(\Xi)\), the complex \(\mathcal L^j(V)=V_{-j}\otimes\mathcal O(j)\) on \(\mathbb P(\Xi)\), with differential \(\sum x_i\otimes\xi_i\), has zero cohomology sheaves outside degree zero, and \(\Phi(V)=\mathcal H^0(\mathcal L(V))\) is locally free. Its fibre at \([\xi]\) identifies with \(H_0(L_\xi(V))\).',
 'A',r'The precise assertion precedes Theorem~1 of \citet{'+BGG+'}.',
 'Established with sheaf cohomology understood as cohomology of this complex, not global cohomology of its terms.',[BGG],
 reconstruction='Algebraic dependence and local splitting are supplied by the displayed bundle complex: fibre exactness permits elimination of invertible minors at both ends until only a locally free degree-zero term remains.')

add('claim','Free exterior-algebra modules give the zero bundle','P000754',
 r'For \(V=\Lambda\), all \(H_i(L_\xi(V))\) vanish. Direct sums and grading shifts give \ru{трив. расслоение}, after the more precise phrase \ru{нулевое расслоение}.',
 r'Every finite graded free \(\Lambda\)-module \(P\) satisfies \(H_i(L_\xi(P))=0\) for all \(i\) and \(\xi\ne0\), hence \(\Phi(P)=0\), the rank-zero bundle. It does not yield every positive-rank trivial bundle.',
 'E',r'This is the acyclic exterior Koszul complex; see also \citet[\S2]{'+BGG+'}.',
 'Correct after disambiguating trivial as zero. The contraction identity is checked in the critical-verification appendix.',[BGG],
 reconstruction=r'Choose \(a\in\Xi^*\) with \(a(\xi)=1\). Interior multiplication \(\iota_a\) satisfies \(\iota_a(\xi\wedge-)+\xi\wedge\iota_a=1\), proving acyclicity in all dimensions. Direct sums and shifts preserve it.',literal='correct with missing hypotheses')

add('theorem','Every algebraic vector bundle has a proper-module model','P000754-P000755',
 r'Theorem~1, repeated as Theorem~\(1^{\prime}\)(1), says every bundle is \(\Phi(V)\) for a proper \(V\).',
 r'For every finite-rank algebraic vector bundle \(\mathcal E\) on \(\mathbb P^n_{\mathbb C}\), there is a finite-dimensional graded proper module \(V\) over \(\bigwedge\mathbb C^{n+1}\) with \(\Phi(V)\cong\mathcal E\).',
 'A',r'Exactly \citet[Theorem~1]{'+BGG+'}.',
 'Established; the public-talk evidence in this package is February 1978, not February 1977.',[BGG],problem='GP-1977-01')

add('theorem','Uniqueness is stable graded isomorphism','P000754-P000755',
 r'Theorem~\(1^{\prime}\)(2) states \(\Phi(V)\cong\Phi(V^{\prime})\) iff \(V\oplus P\cong V^{\prime}\oplus P^{\prime}\) for free \(P,P^{\prime}\).',
 r'For two finite-dimensional graded proper \(\Lambda\)-modules, their associated bundles are isomorphic exactly when there exist finite graded free modules \(P,P^{\prime}\) with a degree-zero \(\Lambda\)-module isomorphism \(V\oplus P\simeq V^{\prime}\oplus P^{\prime}\). The two added free modules need not coincide.',
 'A',r'Exactly the uniqueness clause of \citet[Theorem~1]{'+BGG+'}.',
 'Established. The stronger categorical form quotients morphisms factoring through graded free modules.',[BGG],
 reconstruction='The grading and the properness of both modules are carried over from the preceding definition.',problem='GP-1977-01')

add('remark','An independently obtained related theorem of Beilinson','P000754',
 r'The theorem is attributed to Bernstein, S.~Gelfand and I.~Gelfand, followed by \ru{независимо близкий рез. Бейлинсон}.',
 r'The supported historical assertion is a related independent construction, not identity of all formulations. Beilinson describes the derived category of coherent sheaves on \(\mathbb P^n\) through finite complexes formed from \(\mathcal O(-i)\) or \(\Omega^i(i)\), \(0\leq i\leq n\).',
 'A',r'Compare \citet[\S4, Theorem]{'+BEI+r'}; received 10 January 1978, published 1978.',
 'Both correspondences are established; their relationship has constructive formulations in '+r'\citet[Theorem~6.1]{'+EFS+'}.',[BEI,EFS],
 reconstruction='The derived-category formulation is taken from the checked publication; the notebook only reports a similar result. The student-year description is not independently verified.',match='partial')

add('definition','Twisting line bundles and homogeneous regular functions','P000754-P000755; adjacent check P000758',
 r'\(O(k)\) has sections described as homogeneous rational functions of degree \(k\); \(O(1)\) is called the bundle with a section, and then the Hopf bundle, with \(O(-1)\) offered as an alternative.',
 r'For \(n\geq1\), let \(\mathcal O(-1)\) be the tautological line bundle and \(\mathcal O(1)\) its dual. A section of \(\mathcal O(k)\) over a Zariski open \(U\subset\mathbb P(\Xi)\) is a homogeneous regular function of degree \(k\) on its preimage in \(\Xi\setminus\{0\}\). On \(x_i\ne0\), division by \(x_i^k\) gives a regular scalar function and proves local rank one. In particular \(H^0(\mathcal O(1))=\Xi^*\). The case \(n=0\) is a point, on which all twists are isomorphic.',
 'E',r'Classical twists; \citet[\S54]{'+SER+r'} and \citet[Lemma~30.8.1]{'+STP+'}.',
 'The convention is settled by the homogeneous-degree definition. Having a nonzero section does not uniquely characterize O(1).',[SER,STP],
 reconstruction='Rational sections must be regular on the specified open set. The separately dated P000758 provides corroborating anti-Hopf wording and asks the elementary rank-one question; it is not a second occurrence assigned to record 437.',literal='correct with missing hypotheses')

add('construction','The global linear complex on projective space','P000754-P000755',
 r'\(\mathcal L_j=V_{-j}\otimes O(j)\); on sections \((df)(\xi)=\xi f(\xi)\), giving \(\mathcal L(V)\).',
 r'For any finite graded \(\Lambda\)-module \(V\), define \(\mathcal L^j(V)=V_{-j}\otimes\mathcal O(j)\) and \(d=\sum_{i=0}^n x_i\otimes\xi_i\). The tensor \(\sum x_i\otimes\xi_i\) is independent of dual bases. Since the \(x_i\) commute and the \(\xi_i\) anticommute and square to zero, \(d^2=0\). The sheaf morphisms have the indicated twists, and the complex is bounded.',
 'A',r'This is the functor in \citet[\S3]{'+BGG+'}.',
 'Established. An arbitrary module gives a complex; properness is needed for a single vector bundle.',[BGG],
 reconstruction='Superscripts distinguish cohomological degree from the negative internal grading; the differential formula itself is the notebook formula.')

add('question','Twisting by O(1) is a shifted cosyzygy','P000755',
 r'What does \(\mathcal E\mapsto\mathcal E\otimes O(1)\) mean for modules? For \(0\to V\to P\to V^{\prime}\to0\), \(P\) free, set \(W_j=V^{\prime}_{j+1}\); then \(\Phi(W)=\Phi(V)\otimes O(1)\).',
 r'Let \(V\) be proper and \(0\to V\to P\to V^{\prime}\to0\) exact in finite graded \(\Lambda\)-modules, with \(P\) graded free. Then the grading shift \(W_j=V^{\prime}_{j+1}\) is proper and \(\Phi(W)\cong\Phi(V)(1)\). Such a free embedding exists because the finite-dimensional exterior algebra is Frobenius and its graded projectives are injective.',
 'A',r'Exactly \citet[remark~2 after Theorem~1]{'+BGG+'}.',
 'Established. Both the cosyzygy and internal grading shift are needed.',[BGG],
 reconstruction=r'The long exact fibre-homology sequence gives \(H_i(V^{\prime})\cong H_{i-1}(V)\). Hence \(W\) is proper. Globally \(\mathcal L^j(W)=\mathcal L^{j-1}(V^{\prime})(1)\); the exact sequence gives the asserted degree-zero cohomology. This also checks the sign of the shift.',problem='GP-1977-02')

add('theorem','Large positive twists are globally generated','P000755',
 r'For sufficiently large \(N\), Serre’s theorem gives enough sections of \(\mathcal E\otimes O(N)\) through every vector in every fibre, called \ru{обильное расслоение}.',
 r'If \(\mathcal E\) is coherent on \(\mathbb P^n_{\mathbb C}\), there is \(N_0\) such that for every \(N\geq N_0\) the evaluation map \(H^0(\mathcal E(N))\otimes\mathcal O\twoheadrightarrow\mathcal E(N)\) is surjective. The section space is finite-dimensional. The property used here is global generation, not the definition of an ample vector bundle.',
 'E',r'\citet[Chapter~III, \S65]{'+SER+r'}; modern hypotheses in \citet[Lemma~30.14.1]{'+STP+'}.',
 'Established; in an inverse BGG algorithm the twist must also be sufficiently regular for exactness.',[SER,STP],
 reconstruction='The evaluation formulation specifies the phrase many sections. Ampleness and generation are different properties.',literal='correct with missing hypotheses')

add('construction','The graded section module and coordinate multiplications','P000755',
 r'\(C_N=\Gamma(\mathbb P^n,\mathcal E(N))\), \(\dim\Gamma(O(1))=n+1\), and \(X_i:C_N\to C_{N+1}\) multiplies by the dual coordinate \(x_i\).',
 r'Put \(S=\operatorname{Sym}(\Xi^*)\) and \(C_{\geq N}=\bigoplus_{m\geq N}H^0(\mathcal E(m))\), for a vector bundle \(\mathcal E\) on \(\mathbb P(\Xi)\). Multiplication by \(x_i\in\Xi^*\) defines commuting maps between successive components; for a sufficiently large truncation this is a finite graded \(S\)-module.',
 'E',r'The classical construction is in \citet[Chapter~III]{'+SER+r'}. Finite generation is stated precisely in \citet[Lemma~30.14.1(5)]{'+STP+'}.',
 'Standard. The commutation relations imply the square-zero identity in the ensuing Koszul-dual complex.',[SER,STP],
 reconstruction='Finite generation refers to the graded module of all sufficiently large twists, not to a single vector space with a polynomial action.')

add('method','Recovering a module from two consecutive section spaces','P000756',
 r'The notes put \(V=C_N\otimes\Lambda\), \(V^{\prime}=C_{N+1}\otimes\Lambda\), \(\partial(c\otimes\lambda)=\sum_iX_i(c)\otimes\xi_i\lambda\), and \(W=\ker\partial\), followed by \(N\) inverse shifts using free covers.',
 'Let \\(\\mathcal E\\) be an algebraic vector bundle on \\(\\mathbb P(\\Xi)\\), \\(S=\\operatorname{Sym}(\\Xi^*)\\), and \\(M=\\bigoplus_{m\\geq0}H^0(\\mathcal E(m))\\). Choose an integer \\(N>\\max\\{0,\\operatorname{reg}M\\}\\). In cohomological degree \\(m\\), put \\(R(M)^m=\\operatorname{Hom}_{\\mathbb C}(\\Lambda,M_m)\\), with internal component \\[R(M)^m_t=\\operatorname{Hom}_{\\mathbb C}(\\Lambda_{m-t},M_m).\\] The differential is \\((d_Rf)(\\lambda)=\\sum_i x_i f(\\xi_i\\lambda)\\); it preserves internal degree. The tail with \\(m\\geq N\\) is exact in degrees strictly greater than \\(N\\). Adjoin a minimal graded free resolution of its initial kernel, retaining these cohomological indices, to obtain the everywhere exact Tate complex \\(T(\\mathcal E)\\). Then \\[V=\\ker\\bigl(T(\\mathcal E)^0\\longrightarrow T(\\mathcal E)^1\\bigr)\\] is a finite-dimensional graded proper module and \\(\\Phi(V)\\cong\\mathcal E\\).',
 'A','The notebook sketch belongs to the inverse BGG construction; compare \\citet[\\S~4]{bernsteingelfandgelfand1978bundles}. The explicit conventions above are \\citet[\\S~2, Corollary~2.4, Theorem~3.7 and the construction in \\S~4]{eisenbudfloystadschreyer2003exterior}.',
 'The construction is established, but the notebook omits the grading of the two free modules; its unqualified kernel cannot be certified as already proper.',[BGG,EFS],
 reconstruction="Both gradings, the regularity bound and the degree-zero kernel are supplied here; the notebook gives an abbreviated two-section-space construction. In the modern dual-module convention, \\((a\\cdot f)(\\lambda)=f(\\lambda a)\\), so \\(d_R\\) is a degree-zero \\(\\Lambda\\)-module map. By contrast the notebook's raw tensor formula has internal degree \\(-1\\) and anticommutes with the generators, although its kernel is still a graded submodule. For \\(n=0\\), \\(\\mathcal E=\\mathcal O\\), its raw kernel is \\(\\mathbb C\\xi_0\\) in degree \\(-1\\), hence is not proper. The dual free module \\(\\operatorname{Hom}_{\\mathbb C}(\\Lambda,\\mathbb C)\\) has degrees \\(0,\\ldots,n+1\\), and is noncanonically \\(\\Lambda(-(n+1))\\) under \\(Q(a)_j=Q_{a+j}\\); omitting that shift changes the answer.",
 literal='correct with missing hypotheses',match='partial',confidence='medium')

add('remark','Vector bundles must be enlarged to coherent sheaves','P000756',
 r'I.~M.~Gelfand says classification of bundles is not quite the right problem because they do not form an abelian category; one must allow fibre dimensions to vary and introduce sheaves.',
 r'For \(n\geq1\), finite-rank locally free sheaves on \(\mathbb P^n\) are not an abelian category with the inherited sheaf morphisms: multiplication by a nonzero linear form gives \(\mathcal O(-1)\to\mathcal O\) whose sheaf cokernel is the structure sheaf of a hyperplane and is not locally free. Coherent sheaves form an abelian category. For \(n=0\), vector bundles are finite-dimensional vector spaces and already form an abelian category.',
 'E',r'Coherent-sheaf formalism predates the lecture: \citet[Chapter~I, \S2]{'+SER+'}.',
 'Correct with the positive-dimensional qualification; variable fibre rank alone is not a definition of a coherent sheaf.',[SER],
 reconstruction='More intrinsically, that multiplication map is monic and epic within the category of locally free sheaves, since a map from its torsion cokernel to a locally free sheaf is zero, but is not an isomorphism on the hyperplane. An abelian category is balanced, so it cannot have such a map. The point case is exceptional.',literal='correct with missing hypotheses',speaker='I. M. Gelfand')

add('theorem','Serre correspondence is a quotient by finite-dimensional graded modules','P000756',
 r'The notes equate sheaves on \(\mathbb CP^n\) with finitely generated graded \(\mathbb C[x_0,\ldots,x_n]\)-modules up to finitely many homogeneous components.',
 r'For \(S=\mathbb C[x_0,\ldots,x_n]\) with standard grading, sheafification induces an equivalence \(\operatorname{grmod}(S)/\operatorname{fdim}(S)\simeq\operatorname{Coh}(\mathbb P^n_{\mathbb C})\). Here the numerator has finitely generated graded modules and degree-zero maps, and the denominator is its Serre subcategory of finite-dimensional modules. A quasi-inverse is the nonnegative graded section module followed by passage to the quotient.',
 'E',r'\citet[Chapter~III, \S\S57--65]{'+SER+r'}; \citet[Proposition~30.14.4]{'+STP+'}.',
 'Established. It concerns algebraic coherent sheaves; arbitrary sheaves are not covered.',[SER,STP],
 reconstruction='A quotient category replaces the informal phrase ignoring finitely many components; coherence is an essential omitted hypothesis.',literal='correct with missing hypotheses')

add('construction','Sheafification through degree-zero localization','P000756',
 r'On \(E_i=\{x_i\ne0\}\), \(\Gamma(E_i,L)=\{m/x_i^s:\deg m=s,\ m\in M\}\).',
 r'For a graded \(S\)-module \(M\), set \(\widetilde M(D_+(x_i))=(M_{x_i})_0\). Homogeneous fractions have \(\deg m=s\); equality is equality in the localization, so elements killed by powers of \(x_i\) vanish. The localization maps on overlaps glue these affine modules into a quasi-coherent sheaf, coherent if \(M\) is finitely generated.',
 'E',r'\citet[Lemma~27.8.4]{'+STC+'}.',
 'Established and literally correct when the braces mean localized fractions.',[STC],
 reconstruction='The equivalence relation on fractions and the gluing maps are implicit in the notebook.')

add('construction','Shifting the polynomial module yields O(N)','P000756',
 r'\(O(N)\) arises from \(M=\mathbb C[x_0,\ldots,x_n]\) with \(M_i=S_{i+N}\).',
 r'Define \(S(N)_i=S_{i+N}\). Then \(\widetilde{S(N)}\cong\mathcal O_{\mathbb P^n}(N)\). Locally a homogeneous numerator of degree \(s+N\), divided by \(x_i^s\), has homogeneous degree \(N\), exactly the earlier section convention.',
 'E',r'The standard twisting convention of \citet[\S54]{'+SER+'}.',
 'Correct; this independently fixes the sign of the polynomial-module shift.',[SER],
 reconstruction='The local fraction check compares the final formula with the earlier homogeneous-function definition.')

problems=[
 dict(id='GP-1977-01',title='Algebraic description of vector bundles on projective space',
 statement=r'For each \(n\geq0\), describe the finite-rank algebraic vector bundles on \(\mathbb P^n_{\mathbb C}\) up to isomorphism. The precise requested form in the notes is a classification by proper graded exterior-algebra modules up to adding graded free summands. This problem belongs to the manuscript lecture of 13 February 1978; its corrected GP-1977 identifier records the actual academic year, while this package retains the requested catalogue record.',
 occurrences=['1977-437.2','1977-437.11','1977-437.12'],
 status=r'Solved in the stated representation-theoretic sense by \citet[Theorem~1]{'+BGG+r'}, received 10 January 1978 and published in the 1978 volume. Theorem~2 gives the derived categorical equivalence. No earlier problem ID in the supplied index states this exact projective-bundle problem; affine freeness (the Quillen--Suslin theorem) has different hypotheses.',
 status_date='2026-11',refs=[BGG]),
 dict(id='GP-1977-02',title='Represent twisting by O(1) on the exterior-module side',
 statement=r'Given a proper graded exterior-algebra module \(V\), determine an operation whose associated bundle is \(\Phi(V)(1)\). The notes ask and answer this question within the same, miscatalogued 1978 lecture.',
 occurrences=['1977-437.16'],status=r'Solved: embed \(V\) into a finite graded free module, take the cokernel \(V^{\prime}\), and use \(W_j=V^{\prime}_{j+1}\). See \citet[remark~2 after Theorem~1]{'+BGG+r'}. The fibre long exact sequence independently checks the shift.',status_date='2026-11',refs=[BGG])]
(OUT/'root_problems.json').write_text(json.dumps(problems,ensure_ascii=False,indent=2)+'\n')

corrections=[]
def corr(page,place,reads,should,evidence,applies='both',kind='faithful_error'):
    corrections.append(dict(page=page,place=place,transcription_reads=reads,should_read=should,evidence=evidence,applies_to=applies,type=kind))
corr('P000753','Date and academic-year assignment',r'Catalogue record~437 and supplied talk list: 13 February 1977.',r'Manuscript: \ru{13/II--78 г.}, 13 February 1978; academic year 1977--78.',r'The date is plainly visible in the scan and is correctly transcribed in both TeX files. P000757 explicitly begins 27 February 1978. This corrects catalogue provenance, not either diplomatic date.',kind='provenance')
corr('P000752','Left boundary of the record-437 envelope','The supplied record range includes this physics page.','Do not attribute the sine-Gordon S-matrix and chiral-field tail to S. I. Gelfand\'s vector-bundle lecture.',r'The scan contains equations (46)--(51), soliton scattering and a chiral field, with no S.~I.~Gelfand heading. P000753 begins a new dated lecture and resets numbering to (1).',kind='provenance')
corr('P000757-P000758','Right boundary of the record-437 envelope','The supplied record range includes the next lecture.','Treat 27 February 1978 as a separate S. I. Gelfand lecture; its visible repetition and line-bundle exercise are adjacent evidence only.',r'The scan of P000757 has \ru{27/II--78 г.}; P000758 continues its constructions. The archive list places a 27-Feb-78 record immediately after the erroneous 13-Feb-77 entry.',kind='provenance')
corr('P000753','Projective quotient',r'\(\Xi\) is an affine space; \(\Xi/{\sim}=\mathbb P^n\).',r'Use a vector space \(\Xi\) of dimension \(n+1\) and \((\Xi\setminus\{0\})/\mathbb C^*\).',r'The scan explicitly adds \(\xi\ne0\), so the puncture is recoverable. Scalar multiplication and the following exterior algebra require the linear structure; the clarification does not overwrite the notebook.',kind='ambiguity')
corr('P000754','Free-module example','Free modules give trivial bundles.',r'Free modules give the zero bundle, of rank zero.',r'The scan first says \ru{нулевое расслоение} and then abbreviates \ru{трив.}. Its preceding formula has all homology groups zero. The contraction proof in the critical checks verifies the interpretation.',kind='ambiguity')
corr('P000754-P000755','Hopf convention and sections',r'\(O(1)\) is the one with a section; \(O(1)\) is the Hopf bundle (or \(O(-1)\)).',r'For the displayed homogeneous-degree convention, \(O(-1)\) is tautological and \(O(1)\) its dual; sections are regular on the specified open set.',r'The scan preserves this uncertainty. P000758 explicitly says anti-Hopf. Many positive twists have nonzero sections, so that property cannot identify degree one; the chart calculation resolves the sign.',kind='ambiguity')
corr('P000755','Serre theorem terminology',r'\ru{обильное расслоение}, translated as ample bundle, for having sections through every fibre vector.','The property asserted here is globally generated.',r'The explanatory clause in the scan is the surjectivity of the evaluation map. This is the actual hypothesis used by the construction; it is distinct from the definition of ampleness.',kind='faithful_error')
corr('P000756','Inverse construction, equations (18)--(20)','Two free modules and their kernel, without an explicit total grading.','Specify the grading shifts, the dual exterior module or its shifted identification, and a sufficiently regular section-module tail.',r'The scan leaves these data unstated. With the raw grading the case \(n=0\), \(X_0=1\), gives kernel \(\mathbb C\xi_0\) in degree \(-1\), which is not proper. This demonstrates a missing convention, not failure of the published BGG theorem.',kind='ambiguity')
corr('P000756','Serre citation date',r'Article in the collection \ru{Расслоенные пр-ва}; 1953.',r'The original FAC article is 1955; the Russian collection cited in the BGG paper is 1957.',r'The scan indeed writes 1953, so the transcription is faithful. \citet[title page]{'+SER+r'} gives 1955; \citet[reference~9]{'+BGG+r'} gives the Russian collection, Moscow 1957, pp.~372--453.')
corr('P000756','Scope of Serre correspondence','Sheaves on complex projective space.','Algebraic coherent sheaves, with a quotient of the finitely generated graded-module category by finite-dimensional modules.',r'The scan omits coherent. \citet[Chapter~III]{'+SER+r'} and \citet[Proposition~30.14.4]{'+STP+r'} give the exact scope; the omission cannot be extended to arbitrary sheaves.')
with (OUT/'root_corrections.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=['page','place','transcription_reads','should_read','evidence','applies_to','type']);w.writeheader();w.writerows(corrections)

def get_entry(key):
    s=(ROOT/'project/references_cumulative.bib').read_text()
    m=re.search(r'@\w+\s*\{\s*'+re.escape(key)+r'\s*,',s)
    if not m: raise KeyError(key)
    start=m.start(); p=s.index('{',start);depth=1;i=p+1
    while depth:
        if s[i]=='{' and (i==0 or s[i-1]!='\\'):depth+=1
        if s[i]=='}' and (i==0 or s[i-1]!='\\'):depth-=1
        i+=1
    return s[start:i]

reused=[SER,STP,STC,'sga41972topos','hartshorne1966residues']
bib='\n\n'.join(get_entry(k) for k in reused)
# Preserve keys, but the annote must describe this run rather than the previous chapter.
bib=re.sub(r'annote\s*=\s*\{[^{}]*\}', 'annote = {Reopened on 10 November 2026. See code/research/root_research_log.md for this run\'s locators and verification level.}',bib)
bib+=r'''

@article{bernsteingelfandgelfand1978bundles,
 author = {Bernstein, I. N. and Gel'fand, I. M. and Gel'fand, S. I.},
 title = {Algebraic bundles over {$P^n$} and problems of linear algebra},
 journal = {Functional Analysis and Its Applications},
 year = {1978}, volume = {12}, number = {3}, pages = {212--214},
 doi = {10.1007/BF01681435},
 url = {https://www.math.tau.ac.il/~bernstei/Publication_list/publication_texts/BGG-3.pdf},
 note = {verified},
 annote = {Author-hosted full English text and Math-Net faa2008 opened on 10 November 2026. Sections 2--7, Theorems 1--4 and remarks read. Russian original: 12(3), 66--67. Received 10 January 1978; English translation copyright imprint 1979. The lecture scan is dated 13 February 1978, despite the archive's 1977 catalogue date.}
}

@article{beilinson1978coherent,
 author = {Beilinson, A. A.},
 title = {Coherent sheaves on {$P^n$} and problems of linear algebra},
 journal = {Functional Analysis and Its Applications},
 year = {1978}, volume = {12}, number = {3}, pages = {214--216},
 doi = {10.1007/BF01681436}, url = {https://www.mathnet.ru/eng/faa2009},
 note = {verified},
 annote = {Math-Net metadata and the two-page Russian original opened and read, especially section 4 Theorem. Received 10 January 1978. Original pages 68--69. Checked 10 November 2026.}
}

@article{eisenbudfloystadschreyer2003exterior,
 author = {Eisenbud, David and Fl{\o}ystad, Gunnar and Schreyer, Frank-Olaf},
 title = {Sheaf cohomology and free resolutions over exterior algebras},
 journal = {Transactions of the American Mathematical Society},
 year = {2003}, volume = {355}, number = {11}, pages = {4397--4426},
 doi = {10.1090/S0002-9947-03-03291-4}, url = {https://arxiv.org/abs/math/0104203},
 note = {verified},
 annote = {arXiv metadata and v2 full text opened on 10 November 2026. First joint version 20 April 2001; v2 8 June 2001; journal 2003. Theorem locators refer to the checked v2, especially 2.6, 3.7, 4.1 and 6.1.}
}

@misc{mccme2026seminararchive,
 author = {{Moscow Center for Continuous Mathematical Education}},
 title = {Notes of the {I. M. Gelfand} seminar: chronological record list},
 year = {2026}, url = {https://old.mccme.ru/gelfand/notes/all-links.html},
 note = {verified},
 annote = {Archive list opened 10 November 2026. Individual record-437 and record-438 pages were inaccessible through the web reader; manuscript evidence is supplied by the user's attached scans. The list retains 13-Feb-77 between November 1977 and 27-Feb-78.}
}
'''
(OUT/'root_references.bib').write_text(bib+'\n')
meta=dict(records=[437],items=len(items),areas={i['id']:i['area'] for i in items},
 coverage=[dict(page='P000752',allocation='Adjacent physics tail, excluded from record 437',content='Sine-Gordon two-soliton action and phase; gamma=8pi/N interpolation; reflectionless potential analogy; chiral field and Lax pair; quantum solitons. No separate requested record begins here.'),
 dict(page='P000753-P000756',allocation='Record 437, manuscript 1978-02-13',content='All substantive constructions, theorem clauses, explicit question, inverse method, and interventions indexed in 23 items.'),
 dict(page='P000757-P000758',allocation='Adjacent next lecture, manuscript 1978-02-27',content='Repeated bundle classification, exterior algebra and grading; three definitions of O(j); elementary local rank-one exercise; repeated BGG differential and properness setup. Used for clarification only, not counted as new 1976 occurrences.')],
 development='No C/D problem in this segment. Elementary contractions and shift checks are critical verifications, not novel research.',
 earlier_related=['1970-204.1','1970-204.2','1970-204.3','1970-204.7','1973-302.4','1973-322.1','1975-395.1'],
 warning='All 23 occurrence IDs in this segment use the corrected academic-year prefix 1977; record437 remains in this requested package as a chronological appendix.')
(OUT/'root_meta.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'records':len(talks),'items':len(items),'problems':len(problems),'corrections':len(corrections),'references':len(reused)+4},indent=2))
