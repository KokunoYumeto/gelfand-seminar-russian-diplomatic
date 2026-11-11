"""Research data for GY1966 records 115--118; run from the project root."""
from pathlib import Path
import json, csv, re

D=Path(__file__).resolve().parent
items=[]
def item(record, pages, kind, title, notes, statement, reconstruction, cls, fate,
         status='Established, with the hypotheses stated here.', literal='correct with missing hypotheses',
         match='exact', verification='read the result', development='annotated',
         problem='', refs=None, confidence='high'):
    i=sum(x['record']==record for x in items)+1
    items.append(dict(id=f'1966-{record}.{i}',record=record,pages=pages,kind=kind,title=title,
      notes=notes,statement=statement,reconstruction=reconstruction,**{'class':cls},fate=fate,
      present_status='As of 9 November 2026: '+status,literal_correctness=literal,
      publication_match=match,verification=verification,development=development,problem=problem,
      worth='',refs=refs or [],confidence=confidence))

item(115,'P000173','definition','Smooth and topological left--right stability',
 r'The square with maps \(f,g\), source map \(h\), and target map \(k\) defines equivalence; homeomorphisms give topological stability, diffeomorphisms smooth stability. Local stability is phrased on neighborhoods and germs.',
 r'For smooth manifolds without boundary, two maps are left--right equivalent if \(k\circ f=g\circ h\) for diffeomorphisms \(h,k\). A map is smoothly stable if its orbit is a neighborhood of it in the Whitney \(C^\infty\) topology. For a germ, representatives may be restricted and the nearby singular point may move. Replacing coordinate changes by homeomorphisms defines topological equivalence and the corresponding stability notion.',
 r'The topology and the moving-point convention are supplied; stability of an origin-fixed germ under origin-fixed perturbations would be a different assertion. This repeats 1965-72.1.',
 'E',r'Classical framework, reproduced in \citet[\S1, Definition 1 and the definition of local stability]{arnold1968singularities}. The 1968 paper explicitly derives from 1966 lectures.',refs=['arnold1968singularities'])

item(115,'P000173','construction','A stable square and an unstable cube',
 r'The graphs \(y=x^2\) and \(y=x^3\) are labelled stable and unstable respectively.',
 r'As real smooth map germs \((\mathbb R,0)\to(\mathbb R,0)\), \(x^2\) is a fold and is stable with a moving critical point. The germ \(x^3\) is unstable: \(x^3+\varepsilon x\) has no critical point if \(\varepsilon>0\), while for \(\varepsilon<0\) its derivative has two simple zeros. These germs therefore cannot be related by source and target diffeomorphisms near the original critical point.',
 r'The two perturbations spell out the diagram; they do not constitute a newly posed problem.',
 'E',r'These elementary models are \citet[\S1, Examples 1--2]{arnold1968singularities}; the underlying fold is already Morse theory.',literal='correct',refs=['arnold1968singularities'])

item(115,'P000173-P000174','theorem','Maximal rank and the Morse local normal forms',
 r'The scan reads \ru{Ранг max}; maximal rank is stable. The Morse lemma supplies a nondegenerate quadratic form, followed by the regular form \(y=x_1\).',
 r'A maximal-rank germ is a submersion or an immersion and has the corresponding projection or inclusion normal form. For a scalar-valued smooth germ with \(df_0=0\) and nonsingular Hessian there are coordinates with \(f=f(0)+x_1^2+\cdots+x_k^2-x_{k+1}^2-\cdots-x_m^2\). Regular scalar germs have the form \(f=f(0)+x_1\). These are exactly the smoothly stable scalar germ types.',
 r'The additive constant, smooth category, and distinction between immersions and submersions complete the shorthand. Earlier occurrence: 1965-72.2.',
 'E',r'The standard Morse statement is recalled in \citet[\S1, Examples 3--4 and Theorem 1, p.~3]{arnold1968singularities}; it is exposition of an older theorem.',refs=['arnold1968singularities'])

item(115,'P000173-P000174','theorem','Global stability and density for functions on a compact manifold',
 r'For compact \(M\), stable maps \(M\to\mathbb R\) form an open dense set. Conditions M1 and M2 are nondegenerate critical points and distinct critical values.',
 r'Let \(M\) be a compact smooth manifold without boundary. A smooth function \(f:M\to\mathbb R\) is smoothly stable if and only if all critical points are nondegenerate and no two critical points have the same value. Such functions form an open dense subset of \(C^\infty(M,\mathbb R)\).',
 r'Boundarylessness and the Whitney topology are explicit here; the notebook gives compactness. Distinct critical values are a global condition, not part of the local Morse lemma.',
 'E',r'The compact global Morse criterion is recalled in \citet[\S1, Theorem 1, p.~3]{arnold1968singularities}.',refs=['arnold1968singularities'])

item(115,'P000174','theorem','Whitney regular, fold, and cusp local forms',
 r'The three displayed forms are \((x_1,x_2)\), \((x_1,x_2^2)\), and \((x_1,x_1x_2+x_2^3)\).',
 r'For generic smooth maps of surfaces without boundary, every point has one of the following local coordinate forms: a regular point \((u,v)\mapsto(u,v)\); a fold \((u,v)\mapsto(u,v^2)\); or a cusp \((u,v)\mapsto(u,uv+v^3)\). Each is a smoothly stable germ; these exhaust the stable surface-to-surface monogerms.',
 r'Genericity concerns derivatives as well as the map. The phrase nondegenerate critical point in the notebook is read in this map-theoretic sense, not as a nonsingular scalar Hessian. Earlier occurrence: 1965-72.3.',
 'E',r'Whitney published the plane classification in 1955; \citet[\S1, Theorem 2, pp.~3--4]{arnold1968singularities} reproduces the relevant forms. The original metadata are checked in \citet{whitney1955plane}.',refs=['arnold1968singularities','whitney1955plane'])

item(115,'P000174','theorem','Global stability of maps between surfaces',
 r'W1: critical points are nondegenerate; W2: fold images meet transversely; W3: cusp images are distinct. Stable mappings are said to be dense.',
 r'For a proper smooth map of surfaces, stability requires only regular, fold, and cusp monogerms and stable multigerms over each target point. Concretely the singular image has only ordinary transverse double crossings of fold arcs, each cusp image comes from one singular point, and no other singular branch passes through a cusp image; there are no triple fold intersections. For compact source, such maps form an open dense set.',
 r'The excluded triple intersections and cusp--fold coincidences are missing from W2--W3. The literal list alone is not sufficient. Compact source (or properness with the appropriate topology) supplies the global hypothesis.',
 'E',r'Whitney-type general position underlies the statement; see \citet[\S1, Theorem 2]{arnold1968singularities}. The precise multigerm formulation is part of \citet[\S1, especially the regular-intersection condition]{mather1969algebras}.',literal='correct with missing hypotheses',match='partial',refs=['arnold1968singularities','mather1969algebras'])

item(115,'P000174-P000175','construction','The critical parabola and cusp discriminant',
 r'The kernel directions are vertical. The cusp is where such a direction is tangent to the critical parabola. For \(x_1>0\) the vertical restriction is monotone; for \(x_1<0\) it has two turning points. The continuation says the merger has odd order.',
 r'For \(f(u,v)=(u,uv+v^3)\), \(\det Df=u+3v^2\), so the critical curve is \(u=-3v^2\), its image is \((-3v^2,-2v^3)\), and the kernel along it is generated by \(\partial_v\). Kernel tangency occurs only at the origin. The cubic \(v^3+uv=w\) has three distinct real roots inside the cusp, one outside, and coalescing roots on its discriminant.',
 r'Coefficients and the discriminant are computed directly from the written normal form. Odd order describes this cubic transition, not a sufficient criterion for stability of arbitrary odd-degree map germs. Earlier occurrence: 1965-72.4.',
 'E',r'The Whitney cusp geometry is shown in \citet[\S1, Example 5, p.~4]{arnold1968singularities}.',literal='correct',refs=['arnold1968singularities'])

item(115,'P000175','construction','Resolving the complex square into folds and three cusps',
 r'The real smooth map \(z\mapsto z^2\) is unstable; the proposed perturbation is \(F_\varepsilon(z)=z^2+\varepsilon\bar z\). The drawings show three cusp points.',
 r'For real \(\varepsilon>0\), viewed as a map \(\mathbb R^2\to\mathbb R^2\), the Jacobian of \(F_\varepsilon\) is \(4|z|^2-\varepsilon^2\). Its critical set is \(|z|=\varepsilon/2\); its critical-value curve is \(\varepsilon^2(e^{2it}/4+e^{-it}/2)\). The curve has ordinary cusps at \(e^{3it}=1\); the other critical points are folds. Regular points inside the three-cusped curve have four preimages and exterior regular points have two.',
 r'The real parameter normalization and critical-set calculation resolve the diagrams. They repeat the already indexed question GP-1965-03, occurrence 1965-72.5; they are not a fresh open problem.',
 'A',r'Published explicitly by \citet[\S1, Example 6, pp.~4--5]{arnold1968singularities}; the paper records its 1966 lecture origin, while the earlier notebook occurrence predates this repetition.',status='The stated real smooth perturbation and its fold--cusp picture are settled.',literal='correct',problem='GP-1965-03',refs=['arnold1968singularities'])

item(115,'P000175','remark','Large-circle winding and the trefoil caption',
 r'The caption says that large circles make two turns and adds \ru{трилистн. узел} (trefoil knot), next to several immersed planar curves.',
 r'For \(R>\varepsilon\), \(F_\varepsilon(Re^{it})\) is nonzero and has winding number two about zero: homotope the conjugate-linear term to zero without crossing zero. A knot type is not defined for this immersed planar image unless an embedding or lift to a three-dimensional space is specified; none is specified in the note.',
 r'The winding statement is unambiguous; the knot interpretation is not reconstructed from the drawing.',
 'F',r'\citet[\S1, Example 6, pp.~4--5]{arnold1968singularities} confirms the double winding, but does not identify a three-dimensional knot in this caption.',status='The winding is elementary; the intended trefoil assertion remains unidentified from this record.',literal='not determinable',match='partial',confidence='low',refs=['arnold1968singularities'])

item(115,'P000175','theorem','Failure of density of smoothly stable maps in dimension nine',
 r'Thom is credited with failure of density of stable germs for \(\mathbb R^9\to\mathbb R^9\), and in higher equidimensions; continuous differential invariants are mentioned.',
 r'For every \(n\geq9\), smooth stability is not dense among smooth maps of equidimensional \(n\)-manifolds in general. There exist local configurations persisting under small perturbations whose singular germs have smooth moduli. The mechanism starts with a transverse corank-three point and a nontrivial modulus of a triple of quadratic forms in three variables.',
 r'The precise mechanism is developed in the next lecture, P000184. This is a failure of density, not a claim that no stable germ exists in these dimensions. Earlier occurrence: 1965-72.10.',
 'B',r'\citet[\S3, Theorem 1]{arnold1968singularities} gives the quadratic-modulus argument. The complete density range was published by \citet[Introduction and \S\S3--5]{mather1971nice} in 1971 (Russian translation 1974).',refs=['arnold1968singularities','mather1971nice'])

item(115,'P000175','claim','The unspecified infinity of invariants from dimension twelve',
 r'A separate emphasized line says \ru{нач. с 12, инвар. беск.-много}: beginning with 12 there are infinitely many invariants.',
 r'The note does not specify whether this means infinitely many orbit types, arbitrarily many scalar moduli, or functional moduli, nor the class of germs to which the assertion applies. No exact theorem with these quantifiers can therefore be extracted.',
 r'These three meanings are not interchangeable. The well-defined dimension-nine result is indexed separately.',
 'F',r'The dimension-nine argument and Mather density classification were checked in \citet[\S3]{arnold1968singularities} and \citet{mather1971nice}; neither was used as an exact match for this undefined extra threshold.',status='Unresolved identification of the notebook wording; no new open problem is asserted.',literal='not determinable',match='thematic only',verification='unresolved lead',confidence='low',refs=['arnold1968singularities','mather1971nice'])

item(115,'P000175','claim','Thom topological discreteness outside infinite codimension',
 r'The space of germs is written \(A=\bigcup_{\gamma\in\Gamma}A_\gamma+A_\infty\), with countable \(\Gamma\), finite-codimension pieces of constant topological type and an infinite-codimension remainder. A constant map of a line is placed in the exceptional set.',
 r'The supported assertion is a finite-jet-controlled, countable topological classification of smooth map germs after an exceptional set of infinite jet codimension is removed. Here infinite codimension means containment, for each integer \(q\), in a jet-defined exceptional set of codimension at least \(q\). The asserted pieces are topological equivalence classes or constant-type subsets; no explicit list is provided.',
 r'The note does not define its partition rigorously. We preserve the announced theorem and do not infer that every germ is topologically finitely determined, or that the listed strata are smooth equivalence orbits. Earlier occurrence: 1965-72.11.',
 'B',r'\citet[\S1, Theorem 4, pp.~5--6]{arnold1968singularities} repeats this announcement and explicitly says its proof was unpublished. Thom--Mather stratification supplied the later framework; \citet[Introduction and \S11]{mather1970topological} proves the isotopy machinery, rather than furnishing an explicit enumeration of all these germ types.',status='The topological-stability framework is established; the exact stronger partition wording in this announcement is retained with indirect verification.',match='partial',verification='indirect',confidence='medium',refs=['arnold1968singularities','mather1970topological'])

item(115,'P000175-P000176','definition','Finite jets and their bundle',
 r'Two germs have the same \(k\)-jet when they have contact of order \(k\); the note writes \(f(x)-g(x)=o(x^k)\). Order zero remembers the image point, order one also the differential. \(J^k(M,N)\) is a bundle over \(M\); for \(N=\mathbb R^n\) it is a vector bundle.',
 r'For smooth germs with the same source and target base points, equality of all partial derivatives of orders at most \(k\) defines equality of \(k\)-jets; equivalently in coordinates, \(f(x)-g(x)=o(\|x\|^k)\). The jet bundle has projections to \(M\times N\) and to \(M\), and \(j^kf\) is a section over \(M\). For vector-valued maps it has a natural vector-bundle structure over \(M\). In arbitrary smooth coordinates its fibres are finite-dimensional spaces of Taylor coefficients, not a canonical global algebraic variety.',
 r'The norm in the remainder and the limitation of algebraic to coordinate fibres are explicit editorial qualifications.',
 'E',r'Jet spaces and the jet-section construction are set out in \citet[\S1]{boardman1967singularities}; the definitions predate the lecture.',refs=['boardman1967singularities'])

item(115,'P000176','claim','The truncation exponent in the jet algebra',
 r'The displayed formula is \(j_0^k(n,1)=\mathbb R[x_1,\ldots,x_n]/M^k\), with \(M=(x_1,\ldots,x_n)\); the scan has no \(+1\).',
 r'The algebra of scalar \(k\)-jets at the origin is \(\mathbb R[x_1,\ldots,x_n]/(x_1,\ldots,x_n)^{k+1}\). Its basis consists of monomials of total degree at most \(k\), and its dimension is \(\binom{n+k}{k}\).',
 r'The exponent is a mathematical emendation of a faithful transcription. The notebook itself says that first jets remember the differential; quotienting by \(M\) would erase it.',
 'E',r'The standard Taylor-jet definition in \citet[\S1]{boardman1967singularities} fixes the indexing. The discrepancy is not a new mathematical claim.',literal='false as written',match='partial',refs=['boardman1967singularities'])

item(115,'P000176','definition','Admissible finite-codimension conditions on germs',
 r'An admissible set is the inverse image of a finite-codimension subset of a finite jet space. A codimension-\(e\) variety is said to be given by \(e\) equations.',
 r'If \(S\subset J^k_{0,0}(\mathbb R^m,\mathbb R^n)\) is a smooth locally closed submanifold of codimension \(e\), the inverse image of \(S\) under the jet projection is a finite-jet condition of codimension \(e\). Locally, \(e\) equations specify this codimension only when their differentials are independent.',
 r'The regularity condition on the equations is essential; the bare number of equations is not a dimension theorem.',
 'E',r'This finite-jet interpretation of codimension accompanies \citet[\S1, pp.~5--6]{arnold1968singularities}.',refs=['arnold1968singularities'])

item(115,'P000176-P000177','theorem','Rank strata and their generic codimension',
 r'\(\Sigma^i(f)=\{x:\dim\ker df_x=i\}\). For generic maps the sets are manifolds, with codimension the product of source and target coranks, \((m-r)(n-r)\).',
 r'The matrices of rank exactly \(r\) in \(\operatorname{Hom}(\mathbb R^m,\mathbb R^n)\) form a smooth locally closed submanifold of codimension \((m-r)(n-r)\). If \(j^1f\) is transverse to this stratum, its inverse image is empty or a smooth submanifold of \(M\) of that codimension. The exact-rank stratum is locally closed; the rank-at-most locus is determinantal and can be singular.',
 r'Transversality and the distinction between an exact-rank stratum and its algebraic closure are made explicit. Earlier occurrence: 1965-72.6.',
 'E',r'Thom\textquotesingle s older generic-rank theorem appears in \citet[Part I]{thom1956singularites}; compare \citet[\S2 and Theorem 6.2]{boardman1967singularities}.',refs=['thom1956singularites','boardman1967singularities'])

item(115,'P000177','definition','Transversality of two maps',
 r'For \(f:A\to B\) and \(g:C\to B\), transversality is \(f_*T_aA+g_*T_cC=T_bB\) whenever \(f(a)=g(c)=b\). Intersecting lines in \(\mathbb R^3\) illustrate failure.',
 r'Smooth maps \(f:A\to B\), \(g:C\to B\) are transverse if the sum of their differential images is \(T_bB\) at every matched pair. Then their fibre product is a smooth submanifold of \(A\times C\) of dimension \(\dim A+\dim C-\dim B\), when nonempty.',
 r'The fibre-product formulation specifies the meaning for arbitrary maps; the note supplies the tangent-space definition.',
 'E',r'The classical tangent-space definition and its inverse-image consequence are recalled in \citet[\S2, footnote on p.~8]{arnold1968singularities}.',literal='correct',refs=['arnold1968singularities'])

item(115,'P000177','theorem','Transverse inverse images and perturbation',
 r'If \(f\) is transverse to an embedded submanifold \(C\subset B\), then \(f^{-1}C\) is a manifold of the same codimension. Every map can be perturbed to be transverse.',
 r'For a smooth embedded submanifold \(C\subset B\) and \(f\pitchfork C\), the preimage is empty or a smooth submanifold with \(\operatorname{codim}_A f^{-1}C=\operatorname{codim}_B C\). Thom transversality makes transverse maps residual and dense in the smooth topology; a corresponding jet-transversality theorem applies to submanifolds of \(J^k(A,B)\).',
 r'The statement involving \(\Sigma^i\) is about the jet extension \(j^1f\), not about \(f:M\to N\) being transverse to a subset of a different ambient space. Openness is not asserted for arbitrary nonclosed strata.',
 'E',r'Thom\textquotesingle s method is in \citet{thom1956singularites}; the jet-space application is used explicitly by \citet[Theorem 6.3]{boardman1967singularities}.',refs=['thom1956singularites','boardman1967singularities'])

item(115,'P000177-P000178','construction','Iterating the corank of restrictions',
 r'The restriction \(f|_{\Sigma^i(f)}\) is formed and its corank loci define \(\Sigma^{ij}(f)\); the example \(\Sigma^{110}\) is mentioned.',
 r'Provided the successive loci are smooth, define \(\Sigma^{i_1\cdots i_k}(f)\) by imposing kernel dimension \(i_k\) on the restriction of \(f\) to the previous locus. The successive kernels are nested and \(i_1\geq\cdots\geq i_k\). In the surface cusp, the critical curve has symbol beginning \((1)\), ordinary folds \((1,0)\), and the cusp \((1,1,0)\).',
 r'The construction is conditional on smoothness; Boardman\textquotesingle s jet definition avoids this restriction. Earlier occurrence: 1965-72.7.',
 'E',r'The naive iterative construction and its limitations are explicitly described by \citet[Introduction, p.~21]{boardman1967singularities}.',refs=['boardman1967singularities'])

item(115,'P000178','theorem','Boardman universal strata and simultaneous genericity',
 r'The notes credit Boardman (1965) with universal \(\Sigma^I\subset J^k(M,N)\), computed codimensions, and approximation by maps transverse to all these strata.',
 r'For a finite nonincreasing symbol \(I=(i_1,\ldots,i_k)\), the Boardman set is a smooth locally closed submanifold of the finite jet space when the symbol satisfies the dimension restrictions. Its codimension is the Boardman combinatorial number. Smooth maps whose jet extensions are transverse to all Boardman strata are dense; for them the intrinsic jet definition agrees with the iterative corank loci.',
 r'The notes\textquotesingle{} algebraic subvarieties is understood in local jet coordinates as locally closed sets given by polynomial equalities and inequalities, not as closed varieties. The explicit formula is treated in record 116. Earlier occurrence: 1965-72.8.',
 'B',r'The 1965 circulation date is the notebook\textquotesingle s testimony. The published theorem is \citet[Theorems 6.1--6.3, p.~46]{boardman1967singularities}, 1967.',refs=['boardman1967singularities'])

item(115,'P000178','claim','Boardman symbols are not complete smooth invariants',
 r'The last line says the symbols are not a complete set of invariants, first in \(\mathbb R^4\); rank drops cannot distinguish all cases.',
 r'There are smoothly inequivalent stable germs \((\mathbb R^4,0)\to(\mathbb R^4,0)\) with the same symbol \((2,0)\). Their intrinsic quadratic pencils have different real types. Therefore a Boardman symbol records successive degeneracy dimensions but not the full left--right equivalence class.',
 r'The next lecture supplies explicit real quadratic-pencil representatives. Earlier occurrence: 1965-72.10.',
 'B',r'The two real corank-two examples are given by \citet[\S2, Example 4; \S3]{arnold1968singularities}, while the systematic local-algebra classification is \citet{mather1969algebras}.',literal='correct',refs=['arnold1968singularities','mather1969algebras'])

def save():
    (D/'items.json').write_text(json.dumps(items,ensure_ascii=False,indent=2)+'\n')

save()

item(116,'P000179','construction','Nested corank loci and the limitation of the naive definition',
 r'The lecture restarts with \(\Sigma^i(f)=\{\dim\ker df=i\}\), then \(\Sigma^{ij}(f)=\Sigma^j(f|_{\Sigma^i(f)})\), labelled Thom\textquotesingle s naive definition. Nested kernels imply \(i_1\geq i_2\geq\cdots\).',
 r'If every successive corank locus is a smooth manifold, the restriction construction defines iterated corank strata. The tangent kernels at a point satisfy \(K_{j+1}\subset K_j\); their dimensions form a nonincreasing sequence. For arbitrary smooth maps some intermediate locus need not be smooth, so this is not a universal definition.',
 r'The note itself says to abandon the naive definition in favor of the jet construction; it is retained here as a separate occurrence of 1966-115.19.',
 'E',r'\citet[Introduction and Theorem 6.2]{boardman1967singularities} gives the conditional geometric interpretation and its relation to the intrinsic construction.',literal='correct',refs=['boardman1967singularities'])

item(116,'P000179','definition','Jacobian extension of an ideal and source-coordinate invariance',
 r'For an ideal \(B\subset A\), adjoin the \(k\)-rowed Jacobian minors of functions in \(B\) to obtain \(\Delta_k(B)\). A chain-rule display explains coordinate invariance.',
 r'Let \(A=C^\infty_{\mathbb R^m,0}\), and let \(B\) be a finitely generated ideal. Define \(\Delta_k(B)\) to be \(B\) plus the ideal generated by all \(k\times k\) minors of Jacobian matrices of finite lists of elements of \(B\). This depends only on \(B\), not on a generating list or smooth local coordinates. One may use a generating list, because derivatives of coefficients only contribute terms already in \(B\). Coordinate invariance follows from the chain rule and Cauchy--Binet.',
 r'The proof for all minors extends the notebook\textquotesingle s first-derivative calculation. The construction is stated for local germs, avoiding an undefined global ring of functions.',
 'B',r'\citet[\S2, Definition 2.1 and Lemmas 2.2--2.3]{boardman1967singularities} develops Jacobian extensions invariantly, publishing in 1967 work already circulating in 1965.',refs=['boardman1967singularities'])

item(116,'P000180','claim','Critical Jacobian extension: the first proper ideal',
 r'As \(k\) increases, the ideals decrease. The text calls \(k\) max when the ideal is not the whole \(B\), but the displayed condition is \(\Delta_{k-1}B=A\), \(\Delta_kB\subset A\); also \(\Delta_0B=A\).',
 r'For a proper local ideal \(B\), the critical minor size is the least \(k\geq1\) for which \(\Delta_k(B)\ne A\), equivalently \(\Delta_{k-1}(B)=A\) and \(\Delta_k(B)\subsetneq A\). With source dimension \(m\), write \(\Delta^i=\Delta_{m-i+1}\); the critical superscript then encodes the corank.',
 r'The words max and whole B conflict with both the monotonicity and the displayed transition. They are emended to min and whole A, without altering the diplomatic source.',
 'B',r'The intrinsic corank/critical-extension definition is established in \citet[\S2]{boardman1967singularities}.',literal='false as written',match='partial',refs=['boardman1967singularities'])

item(116,'P000180','construction','Successive extensions of the cubic ideal',
 r'The example begins with the ideal generated by \(x^3\), gives \(\Delta_1=(x^2)\), and has a crowded iterated expression ending in \((x)\).',
 r'In \(C^\infty_{\mathbb R,0}\), the successive first Jacobian extensions are \((x^3)\mapsto(x^2)\mapsto(x)\mapsto A\). Hence the cubic map germ has initial Boardman symbol \((1,1,0)\), although as a one-variable germ it is not a transverse, stable representative of that symbol.',
 r'The iteration sequence, rather than a literal interpretation of the overloaded superscript, is fixed by differentiation. The final zero is the critical corank when the current ideal is \((x)\).',
 'E',r'This is a direct example of the definition in \citet[\S2]{boardman1967singularities}. It illustrates algebraic symbol computation rather than a stability theorem.',literal='not determinable',match='partial',refs=['boardman1967singularities'])

item(116,'P000180','question','Target-coordinate independence of the Boardman ideal construction',
 r'For \(B=(f_1,\ldots,f_n)\), all iterated extensions \(\Delta^{i_j}\cdots\Delta^{i_1}B\) are to be critical. Source independence is stated; target independence is marked \ru{нужно пров.} (needs checking).',
 r'For a germ \(f:(\mathbb R^m,0)\to(\mathbb R^n,0)\), the ideal is intrinsically \(B=f^*\mathfrak m_n\,A\). If \(h\) is a target diffeomorphism germ fixing zero, then \(h^*\mathfrak m_n=\mathfrak m_n\), so \((h\circ f)^*\mathfrak m_n A=B\). Thus all subsequent Jacobian extensions and the Boardman symbol are unchanged. Membership for a symbol of length \(k\) depends only on the \(k\)-jet.',
 r'The maximal-ideal argument is the missing check. It resolves a pedagogical proof obligation, not an unanswered research problem.',
 'B',r'\citet[\S2, especially (2.17)--(2.18)]{boardman1967singularities} supplies the universal coordinate-independent construction.',status='Resolved by the intrinsic ideal definition; no separate open problem is introduced.',literal='correct',refs=['boardman1967singularities'])

item(116,'P000180-P000181','claim','Boardman codimension formula and two missing conventions',
 r'The coefficient is written \(m-n+i_1\). The count \(\mu(I)\) includes nonincreasing sequences satisfying \(0\leq j_s\leq i_s\), without excluding the all-zero sequence.',
 r'For source dimension \(m\), target dimension \(n\), and an admissible nonincreasing symbol \(I=(i_1,\ldots,i_k)\), put \(\mu(I)=\#\{j_1\geq\cdots\geq j_k\geq0: j_s\leq i_s,\ j_1>0\}\). Then \[c(I)=(n-m+i_1)\mu(I)-\sum_{r=1}^{k-1}(i_r-i_{r+1})\mu(i_{r+1},\ldots,i_k).\] For length one this gives \(i(n-m+i)\), and for \(I=(1,\ldots,1)\) of length \(k\) it gives \(k(n-m+1)\).',
 r'The dimension difference must be target minus source; the all-zero sequence must be excluded. Both repairs are forced already by the rank-stratum case. The supplied check script independently counts the sequences by enumeration and recursion; these finite computations are \oursComputed{} and do not replace Boardman\textquotesingle s theorem.',
 'B',r'The formula and both conventions are \citet[Definitions 6.4--6.5, pp.~46--47]{boardman1967singularities}. The scan confirms that these are mathematical emendations of the notebook, not transcription errors.',literal='false as written',match='partial',refs=['boardman1967singularities'])

item(116,'P000181','theorem','Generic agreement of intrinsic and geometric Boardman loci',
 r'Boardman\textquotesingle s three assertions are smooth strata, the codimension formula, and transversality for almost all maps, giving agreement with Thom\textquotesingle s naive definition.',
 r'If a smooth map has jet extension transverse to each relevant Boardman stratum, the inverse-image strata are smooth of the stated codimensions, and iterated corank loci agree pointwise with the intrinsic jet loci. Such maps are dense (indeed obtained by jet transversality). Almost all denotes genericity in function space, not a probability measure.',
 r'The note writes \(f\in\Sigma^I\); the precise statement is \(x\in\Sigma^I(f)\) if and only if \(j_x^kf\in\Sigma^I\).',
 'B',r'This is \citet[Theorems 6.1--6.3]{boardman1967singularities}, published 1967.',refs=['boardman1967singularities'])

item(116,'P000181','construction','First dimensions of transverse Boardman symbols',
 r'For equidimensional maps the table gives \(1_k\) in dimension \(k\), \((2)\) at four, \((2,1)\) at seven, \((3)\) at nine, and \((2,2)\), \((2,1,1)\) at ten. A later line mentions 16 and 4. The note asks to write the table precisely.',
 r'A Boardman stratum of codimension \(c\) can meet a transverse jet section only if the source dimension is at least \(c\). For equidimensional maps the displayed values are \(c(1_k)=k\), \(c(2)=4\), \(c(2,1)=7\), \(c(3)=9\), \(c(2,2)=c(2,1,1)=10\), and \(c(4)=16\). At \(n=9\), the fold, cusp, and corank-two loci have dimensions 8, 7, and 5 respectively.',
 r'First appearance means the codimension threshold for a generic map, not existence of such a germ in arbitrary small dimension without transversality. The isolated 4 at dimension 16 is interpreted as corank four, not four equivalence classes. Values were checked by two independent counts in the supplied script (\oursComputed).',
 'B',r'These values follow from \citet[(6.5), p.~47]{boardman1967singularities}; they are not an exhaustive classification by smooth type.',literal='correct with missing hypotheses',match='partial',refs=['boardman1967singularities'])

item(116,'P000182','theorem','Morin normal forms for corank-one singularities',
 r'The theorem name is written Moren/Morin. A good \(\Sigma^{1_k0}\) germ is given a generalized cusp normal form; the display specializes the number of ones to the ambient dimension.',
 r'Let \(1\leq k\leq n\). A transverse corank-one germ \((\mathbb R^n,0)\to(\mathbb R^n,0)\) of symbol \((\underbrace{1,\ldots,1}_{k},0)\) is smoothly equivalent to \[(u_1,\ldots,u_{n-1},t)\longmapsto\left(u_1,\ldots,u_{n-1},\ t^{k+1}+\sum_{j=1}^{k-1}u_jt^j\right).\] It is a stable Morin germ. The notebook\textquotesingle s formula is the case \(k=n\).',
 r'The transversality hypothesis cannot be replaced simply by algebraic membership of an arbitrary jet in the same Boardman locus; for example \(x^3\) alone is not a stable one-variable germ. Parameters and the index \(k\) are distinguished here.',
 'E',r'Morin\textquotesingle s result appeared in two 1965 Comptes rendus notes; \citet[\S2, Example 6, pp.~9--10]{arnold1968singularities} states the form and cites them. This item uses that checked exposition, not an uninspected original proof.',verification='indirect',refs=['arnold1968singularities'])

item(116,'P000182-P000183','construction','The intrinsic quadratic differential',
 r'The map \(f_{xx}:\ker df_x\to\operatorname{coker}df_x\) is defined by dividing the projected curve \(f(X(t\xi))\) by \(t^2\). The note says coordinate independence is easy and adds \ru{Посмотреть!}.',
 r'For a smooth map germ, put \(K=\ker df_x\), \(C=T_{f(x)}N/\operatorname{im}df_x\). The symmetric bilinear form \(H_f:K\times K\to C\) defined in coordinates by the class of \(D^2f_x(v,w)\) is intrinsic. The note\textquotesingle s diagonal limit is \(\tfrac12H_f(\xi,\xi)\). Under source-coordinate change the additional term lies in \(\operatorname{im}df_x\); under target-coordinate change the extra term contains \(df_x(v),df_x(w)\), which vanish.',
 r'The factor \(1/2\) follows from Taylor\textquotesingle s formula. The one-line coordinate-independence proof fills the explicit checking instruction; it is not attributed to the notebook.',
 'E',r'Intrinsic derivatives predate the lecture; \citet[\S7]{boardman1967singularities} develops them, and \citet[\S3, Definition 1 and Lemma 1]{arnold1968singularities} gives this exact quadratic construction.',literal='correct',refs=['boardman1967singularities','arnold1968singularities'])

item(116,'P000183','remark','Why a cubic differential is not defined by the same recipe',
 r'The parenthesis says that a cubic differential cannot be defined this way.',
 r'For a general germ, the raw third Taylor coefficient restricted to \(\ker df\) and projected to \(\operatorname{coker}df\) is not coordinate invariant. Already \(f(x)=x^2\) has zero cubic coefficient in coordinate \(x\), but under \(x=u+au^2\) it becomes \(u^2+2au^3+O(u^4)\). Higher intrinsic derivatives require additional kernel/quotient data or vanishing of the relevant lower derivatives.',
 r'The explicit one-variable check clarifies the intended limitation; it does not deny Boardman\textquotesingle s higher intrinsic derivatives.',
 'E',r'\citet[\S7]{boardman1967singularities} gives the corrected higher-derivative framework. The notebook\textquotesingle s warning is mathematically appropriate for the naive recipe.',literal='correct',refs=['boardman1967singularities'])

item(116,'P000183','construction','Binary quadratic pencils and seven linear orbit types',
 r'The dual of the cokernel maps to quadratic forms on the kernel. For kernel and cokernel of dimension two, binary quadratic forms occupy \(\mathbb R^3\), with degenerate cone \(b^2=ac\). Seven positions, including degeneracies, give seven orbits.',
 r'Let \(q:\mathbb R^2\to\mathbb R^2\) be homogeneous quadratic. Its dual pencil is a linear map \((\mathbb R^2)^*\to\operatorname{Sym}^2((\mathbb R^2)^*)\). Up to independent invertible source and target linear changes there are seven types: three rank-two pencils (plane cutting, tangent to, or exterior to the discriminant cone), three rank-one pencils (definite, indefinite, or rank-one form), and the zero pencil. Only the pencil is classified by this seven-orbit statement, not every smooth germ with that quadratic part.',
 r'Allowing the pencil image to have dimensions zero or one is essential to the count seven; a literal plane alone gives only three cases. The seven quadratic orbits must not be confused with seven smooth \(\Sigma^{20}\) germs.',
 'E',r'The elementary real linear classification appears in \citet[\S3, Example 2, pp.~13--14]{arnold1968singularities}.',literal='correct with missing hypotheses',refs=['arnold1968singularities'])

item(116,'P000184','construction','Two transverse corank-two germs in four dimensions',
 r'The maps are \(y_1=x_1x_2\), \(y_2=x_1^2\pm x_2^2+x_1x_3+x_2x_4\), \(y_3=x_3\), \(y_4=x_4\); the mixed terms are explicitly added for transversality.',
 r'These two germs \(F_\pm:(\mathbb R^4,0)\to(\mathbb R^4,0)\) have rank two at zero. Their normal Jacobian block is \(\left(\begin{smallmatrix}x_2&x_1\\2x_1+x_3&\pm2x_2+x_4\end{smallmatrix}\right)\), and its linearization is an isomorphism \(\mathbb R^4\to M_2(\mathbb R)\), so their first jet sections are transverse to the corank-two stratum. Their intrinsic pencils \((xy,x^2\pm y^2)\) are inequivalent over \(\mathbb R\).',
 r'Transversality was recomputed symbolically; the determinant is nonzero for either sign (\oursComputed). The signs encode a real invariant, even though the Boardman symbol is the same.',
 'A',r'\citet[\S2, Example 4 and \S3]{arnold1968singularities} publishes equivalent corank-two examples based on the 1966 lectures.',literal='correct',refs=['arnold1968singularities'])

item(116,'P000184','remark','Real signs, complexification, and variation along a corank-two curve',
 r'In \(\mathbb R^5\) the corank-two set can be a curve with varying singularities. The real plus and minus cases cease to differ over \(\mathbb C\), while a parabolic case remains.',
 r'For a transverse map between five-dimensional manifolds, the corank-two stratum has dimension one; its quadratic-pencil type can vary along it. Over \(\mathbb C\), replacing one source variable by its multiple by \(i\) identifies the two nonsingular real sign types of binary quadratic pencils, whereas a tangency degeneration is still distinguished by the discriminant.',
 r'The assertion is about quadratic-pencil types. No claim is made that every higher-order real or complex germ is determined by this second-order invariant.',
 'E',r'\citet[\S3, Examples 2--3]{arnold1968singularities} explains the real pencil geometry and degeneration types.',literal='correct with missing hypotheses',refs=['arnold1968singularities'])

item(116,'P000184','claim','The overstatement that every corank-two germ is stable',
 r'The line says \(\Sigma^{20}\): all singularities are stable and there is a differential classification; for \(\Sigma^{30}\) this is no longer so.',
 r'A Boardman symbol \((2,0)\) by itself does not imply smooth stability. Stable corank-two germs can be classified by their local algebras, subject to the source/target dimension and unfolding conditions. Nonstable germs with the same symbol exist. For example \((x,y)\mapsto(x^2+y^2,xy)\) has algebraic symbol \((2,0)\), but corank two cannot occur in a generic surface map, so it is unstable.',
 r'The strong literal sentence is corrected to a statement about stable or sufficiently generic germs. The following table supplies an algebraic classification but does not remove the stability hypothesis.',
 'B',r'\citet[Theorems A and B]{mather1969algebras} distinguishes algebraic classification from stable realizability; \citet[\S7]{mather1971nice} gives the stable corank-two list.',literal='false as written',match='partial',refs=['mather1969algebras','mather1971nice'])

item(116,'P000184','theorem','Dimension count forcing moduli of quadratic maps',
 r'For \(n\geq3\), the group \(GL(n)\times GL(n)\) has dimension \(2n^2\), the space of \(n\) quadratic forms has dimension \(n^2(n+1)/2\), and scalar transformations provide a one-dimensional stabilizer. Hence every orbit has positive codimension.',
 r'Let \(H_n=\operatorname{Hom}(\operatorname{Sym}^2\mathbb R^n,\mathbb R^n)\), with the action \((A,B)q=B\circ q\circ A^{-1}\). The one-dimensional subgroup \((tI,t^2I)\), \(t\ne0\), acts trivially. Thus every orbit has dimension at most \(2n^2-1\), and codimension at least \(n^2(n-3)/2+1\), which is positive for \(n\geq3\). For a transverse corank-three point of a map \(\mathbb R^9\to\mathbb R^9\), these quadratic moduli obstruct smooth stability.',
 r'The precise scalar action and the lower bound expand the proof already present in the notebook. Here \(n\) is the kernel/cokernel dimension, not the ambient dimension nine.',
 'B',r'This is the argument of \citet[\S3, Lemma 3 and Theorem 1]{arnold1968singularities}, attributed there to Thom; the later complete setting is \citet{mather1971nice}.',literal='correct',refs=['arnold1968singularities','mather1971nice'])

item(116,'P000184','claim','The announced dimension-dependent density classification',
 r'A dimension diagram labels the embedding region, Whitney, Morse, and cells 9,9 and 6,9; Mather is credited with announcing where moduli occur and classifying stable singularities.',
 r'For fixed source and target dimensions, there is a numerical criterion for density of proper smoothly stable maps among proper smooth maps. In Mather\textquotesingle s notation it is \(\dim M<\sigma(\dim M,\dim N)\), with an explicitly computed function \(\sigma\). The notebook diagram alone does not specify the ordering of the coordinates of every cell or the exact boundary inequalities.',
 r'The numerical criterion is identified through the later primary paper; no missing line in the diagram is reconstructed. The two ordered pairs are not silently interchanged.',
 'B',r'The announcement matured into \citet[Introduction and \S\S1--5]{mather1971nice}, published 1971; the opened Russian translation dates from 1974. Earlier occurrence: 1965-72.14.',literal='not determinable',match='partial',confidence='medium',refs=['mather1971nice'])

item(116,'P000185','definition','The local algebra of a map germ',
 r'The local ring is written as a quotient of \(E_x\) by the ideal generated by the pullback of the maximal ideal of \(E_y\); it is called the ring of functions on the coalesced inverse image.',
 r'For a smooth map germ \(f:(\mathbb R^m,0)\to(\mathbb R^n,0)\), let \(E_m\) and \(E_n\) be the real algebras of smooth germs and \(\mathfrak m_n\) the target maximal ideal. Define \(Q(f)=E_m/(f^*\mathfrak m_n)E_m\). Its isomorphism type as a real algebra is invariant under source and target diffeomorphisms. The ideal product is necessary: the pullback subalgebra alone is not the quotient ideal.',
 r'The notation \(f_*\) in the notebook denotes pullback of functions; modern notation \(f^*\) avoids conflict with differential pushforward.',
 'E',r'The quotient is the starting definition in \citet[Introduction, pp.~223--224]{mather1969algebras}; \citet[\S4]{arnold1968singularities} gives the same exposition.',literal='correct',refs=['mather1969algebras','arnold1968singularities'])

item(116,'P000185','construction','Dual numbers as two coalescing points',
 r'For \(f(x)=x^2\), multiplication by \(E\) adds all higher terms, leaving classes \(a+bx\). This is the ring of functions on an infinitesimal pair of points.',
 r'For \(f(x)=x^2\), Hadamard\textquotesingle s lemma gives \(Q(f)\simeq\mathbb R[x]/(x^2)\). The family \(\mathbb R[x]/(x^2-t)\) has dimension two for every \(t\); for \(t>0\) it is \(\mathbb R\oplus\mathbb R\), and at \(t=0\) it is the nonreduced dual-number algebra. This makes coalescence precise.',
 r'The parameter \(t\) and flat algebraic family formalize the diagram. The real fibre for \(t<0\) has no real points, showing why vector-space length must not be equated with the number of real preimages.',
 'E',r'The model and its limiting multiplication are worked out in \citet[\S4, Example 1 and Propositions 1--2]{arnold1968singularities}.',literal='correct',refs=['arnold1968singularities'])

item(116,'P000185-P000186','claim','Local algebra length and multiplicity',
 r'The note conjecturally identifies \(\dim Q\) with multiplicity for an analytic \(f:\mathbb C^n\to\mathbb C^m\), adding \ru{По-видимому, так} (apparently so); the preparation discussion calls it the correct definition.',
 r'For a holomorphic germ \(f:(\mathbb C^n,0)\to(\mathbb C^n,0)\) with isolated fibre \(f^{-1}(0)=\{0\}\) near zero, the finite length \(\dim_\mathbb C\mathcal O_n/(f_1,\ldots,f_n)\) is the local mapping multiplicity; a nearby regular value in a sufficiently small representative has that number of preimages counted with multiplicity. For unequal dimensions the length still makes sense if finite, but it is not automatically the number of inverse images of an arbitrary ambient regular value.',
 r'The equal-dimensional finite-map hypotheses are essential for the literal preimage-count interpretation. This resolves a tentative expository question rather than proposing a new conjecture.',
 'E',r'The analytic finite-module statement is part of \citet[Chapter III]{malgrange1966ideals}; its application to the local ring is explained in \citet[\S4, Theorem 2 and examples]{arnold1968singularities}. Malgrange\textquotesingle s lectures were delivered in 1964, with a July 1965 preface and 1966 publication.',refs=['malgrange1966ideals','arnold1968singularities'])

item(116,'P000185','theorem','Stable germs are classified by their local algebras',
 r'Mather\textquotesingle s theorem says stable singularities are equivalent if and only if their local rings coincide.',
 r'For stable smooth monogerms \(f,g:(\mathbb R^m,0)\to(\mathbb R^n,0)\) of the same source and target dimensions, an isomorphism of the appropriate local real algebras \(Q(f)\simeq Q(g)\) determines smooth left--right equivalence. In the finite-algebra case the ordinary local algebras suffice; in general one may use their formal completions or the finite truncations in Mather\textquotesingle s Theorem A. Equality of dimensions and stability cannot be dropped.',
 r'Coincide means algebra isomorphism, not literal equality of ideals or equality of vector-space dimensions. This is the map-germ classification theorem, not the later Mather--Yau theorem for hypersurface singularities.',
 'B',r'Announced by 1966 according to this notebook and \citet[\S4]{arnold1968singularities}; published as \citet[Theorem A, pp.~223--225]{mather1969algebras}, received June 1968, published 1969.',refs=['arnold1968singularities','mather1969algebras'])

item(116,'P000185-P000186','theorem','Infinitesimal stability and the source--target linearization',
 r'Every vertical field \(\varphi\) along \(f\) must be \(f_*\xi+f^*\eta\). The accompanying theorem asserts stability if and only if infinitesimal stability.',
 r'For a smooth monogerm, let \(\theta_m,\theta_n\) be the modules of source and target vector-field germs and \(\theta(f)\) the vector fields along \(f\). The linearization is \(t_f(\xi)=df\circ\xi\), \(\omega_f(\eta)=\eta\circ f\). Infinitesimal stability is the equality \(t_f\theta_m+\omega_f\theta_n=\theta(f)\); it is equivalent to smooth stability of the germ. For global maps a corresponding theorem requires properness (compact source suffices).',
 r'Vector fields in this extended tangent-space criterion need not vanish at the base point. Restricting to vanishing fields would test an origin-fixed equivalence problem. Earlier occurrence: 1965-72.12.',
 'B',r'Published in \citet{mather1969stability}; its metadata were checked. The germ linearization and stability convention were read directly in \citet[Introduction and \S1]{mather1969algebras}; \citet[\S5--\S7]{arnold1968singularities} explains the proof method.',refs=['mather1969stability','mather1969algebras','arnold1968singularities'])

item(116,'P000186','theorem','Smooth preparation as finite generation over the target',
 r'If \(Q\) has finite dimension \(r\) and representatives \(e_1,\ldots,e_r\), every smooth germ is written \(\varphi(x)=\sum_i\psi_i(y)e_i(x)\). The heading says Weierstrass preparation.',
 r'Let \(f:(\mathbb R^m,0)\to(\mathbb R^n,0)\) be smooth and \(Q(f)\) finite-dimensional. If the classes of \(e_1,\ldots,e_r\) span \(Q(f)\) as a real vector space, then every \(\varphi\in E_m\) has \(\varphi(x)=\sum_{i=1}^r\psi_i(f(x))e_i(x)\) with \(\psi_i\in E_n\). Equivalently \(E_m\) is a finitely generated \(E_n\)-module via \(f^*\). Neither uniqueness of the coefficients nor freeness is asserted.',
 r'For \(C^\infty\) germs this is the Malgrange preparation theorem and its finite-module form, not merely analytic Weierstrass preparation. Generators must mean linear spanning representatives in \(Q\), not merely generators of \(Q\) as an algebra.',
 'E',r'\citet[Chapter V]{malgrange1966ideals} publishes the smooth preparation theorem, from 1964 lectures; \citet[\S4, Theorem 1]{arnold1968singularities} gives exactly this finite-module formulation and records Mather\textquotesingle s 1966 simplification.',refs=['malgrange1966ideals','arnold1968singularities'])

item(116,'P000186','theorem','Five families of stable real corank-two local algebras',
 r'The list is \(I_{a,b}\), \(II_{a,b}\), \(III_{a,b}\), \(IV_a\), \(V_a\). The first ideal has a doubtful comma between \(x,y\). The notebook\textquotesingle s IV has \((x^a,xy^{a-1},x^2+y^2)\), and V has \((x^a,x^2+y^2)\). The left margin mixes dimension conditions and row numbers.',
 r'For stable real smooth germs of type \((2,0)\) with source dimension at most target dimension, Mather\textquotesingle s final list is, using \(R=\mathbb R[[x,y]]\): \[\begin{aligned}I_{a,b}&:R/(xy,x^a+y^b),&b\geq a\geq2;\\II_{a,b}&:R/(xy,x^a-y^b),&b\geq a\geq2\ \text{both even};\\III_{a,b}&:R/(xy,x^a,y^b),&b\geq a\geq2;\\IV_a&:R/(x^2+y^2,x^a),&a\geq3;\\V_a&:R/(x^2+y^2,x^a,x^{a-1}y),&a\geq3.\end{aligned}\] They are pairwise nonisomorphic. Stable realization for given dimensions is a further condition, not guaranteed merely by writing a family name; the three-generator cases require target dimension greater than source dimension.',
 r'The published labels IV and V are interchanged relative to the notebook. The first ideal must contain \(xy\), not separate \(x,y\); the three-generator elliptic family needs \(x^{a-1}y\), not \(xy^{a-1}\). At odd \(a\), the latter is redundant modulo \((x^a,x^2+y^2)\); the supplied exact algebra check detects the resulting length error (\oursComputed).',
 'B',r'\citet[\S7, pp.~150--151 of the Russian translation]{mather1971nice} proves the list and reports that Mather\textquotesingle s autumn 1965 letter to Morin contained an error, corrected by Morin; Arnold published the corrected account in 1968. That history makes the 1966 notebook especially valuable without licensing silent correction.',literal='false as written',match='partial',refs=['mather1971nice','arnold1968singularities','mather1969algebras'])

item(116,'P000186','claim','Finite-codimension algebra types and the exceptional remainder',
 r'The five families are followed by remainder: codimension infinity, the codimensions have been calculated, and a statement that \(\Sigma^{20}\) is subdivided into submanifolds.',
 r'In the source-dimension-at-most-target-dimension range, the stable finite local-algebra types of corank two are the five families just listed. The formal classification also has nonfinite residual cases; such exceptional germs are excluded from the finite stable classification. The primary paper computes orbit codimensions and stable-realizability conditions. The notebook gives no numerical codimension formula here, so none is attributed to this talk.',
 r'The finite-dimensional local-algebra condition, stability, and a universal finite-jet stratum are distinct. Remainder of infinite codimension is retained as the announced generic-classification qualification, not a proof that every other individual \((2,0)\) germ is absent.',
 'B',r'\citet[\S7]{mather1971nice} supplies the classification and numerical invariants; \citet[Theorem B]{mather1969algebras} states the realization test. The precise scope is narrower than an unqualified all singularities are stable.',literal='correct with missing hypotheses',match='partial',confidence='medium',refs=['mather1971nice','mather1969algebras'])

save()

# A later primary source establishes a precise generic finite classification,
# without silently identifying it with every quantifier of the 1966 announcement.
topological = next(x for x in items if x['id']=='1966-115.12')
topological['fate'] = r'\citet[\S1, Theorem 4, pp.~5--6]{arnold1968singularities} repeats the announcement and says its proof was unpublished. A precise later result is \citet[Introduction, p.~88]{mather1972stratifications}: for each source/target dimension pair there is a closed semialgebraic exceptional set in a finite jet space, of codimension greater than the source dimension, outside which only finitely many topological germ types occur. That paper gives a proof sketch; its Harvard preprint dates from 1971 and the opened translation appeared in 1972. The broader isotopy framework is in \citet[\S11]{mather1970topological}. These statements are a verified development, not an exact verification of the stronger countable partition outside infinite codimension.'
topological['present_status'] = 'As of 9 November 2026: the later generic finite-classification theorem is established; the exact infinite-codimension partition wording of this announcement was not independently verified in the opened sources.'
topological['refs'].append('mather1972stratifications')
algebra_classification=next(x for x in items if x['id']=='1966-116.21')
algebra_classification['fate']=r'Announced by 1966 according to this notebook and \citet[\S4]{arnold1968singularities}; the checked primary statement is \citet[Theorem A, pp.~223--225]{mather1969algebras}. The manuscript was received on 1 June 1968; the journal volume is dated 1969, while the scanned printing colophon says 1970. The bibliography follows the journal metadata and keeps that distinction explicit.'
for occurrence in ['1966-115.7','1966-115.8','1966-116.4','1966-116.11']:
    row=next(x for x in items if x['id']==occurrence)
    row['reconstruction']=r'\oursComputed{} '+row['reconstruction']
for occurrence in ['1966-115.9','1966-116.5','1966-116.15']:
    row=next(x for x in items if x['id']==occurrence)
    row['reconstruction']=r'\ours{} '+row['reconstruction']
save()

talks = [
    dict(record=115,date='1966-11-21',speaker='V. I. Arnold',pages='P000173-P000178',
         title='Singularities of smooth mappings I: stability, jets, and Boardman strata',kind='talk',
         summary=r'The first lecture moves from Morse and Whitney models through the perturbation \(z^2+\varepsilon\bar z\), smooth moduli, and Thom\textquotesingle s topological announcement to jets, transversality, and Boardman\textquotesingle s universal strata. It resumes the earlier 1965 record 72, including GP-1965-03. Arnold\textquotesingle s 1968 survey explicitly derives from his 1966 lectures and supplies unusually close publication matches. The MCCME catalogue associates P000172--P000180 with the record; the actual dated lecture starts on P000173 and ends on P000178.'),
    dict(record=116,date='1966-11-28',speaker='V. I. Arnold',pages='P000179-P000186',
         title='Singularities of smooth mappings II: intrinsic derivatives and local algebras',kind='talk',
         summary=r'The second lecture constructs Boardman ideals, states their codimension formula, and studies Morin germs and intrinsic quadratic pencils. It then explains the first smooth moduli, Mather\textquotesingle s local-algebra and infinitesimal-stability criteria, smooth preparation, and five real corank-two families. The scans reveal substantive mathematical slips in the codimension conventions and one mixed monomial; the corrected statements are separated from the notebook readings. The MCCME catalogue span P000178--P000188 overlaps both adjacent records; the dated lecture itself occupies P000179--P000186.'),
    dict(record=117,date='',speaker='',pages='P000186-P000188',title='Year 1967',kind='heading',
         summary=r'This is the MCCME catalogue\textquotesingle s year-heading record, not a separate mathematical lecture. Its broad page interval overlaps the end of Arnold\textquotesingle s lecture and the February plan. P000186 ends with a next-meeting notice for 13 February 1967. No distinct theorem, problem, or construction is assigned to the heading.'),
    dict(record=118,date='',speaker='',pages='P000187',title='Plan for 13 February 1967',kind='plan',
         summary=r'The catalogue labels the record 13-Feb-67 but supplies no machine-readable date; the label is preserved as a title. The plan lists Kirillov on Harish-Chandra (about ten lectures), Anosov on Maslov and semiclassics (two), Kazhdan on A.~Weil (six or seven), Dynin on the index (three), Anosov on first-order Pfaff equations (one), and Bernstein on the \(KG\)-functor (two). The next meeting is assigned to Kirillov and Anosov. The Russian surname \ru{Дынин} is Dynin, not the English translation\textquotesingle s Dynkin. These are topic announcements without mathematical assertions, so the plan has no occurrence-index items. The catalogue span P000186--P000188 is wider than the plan at the top of P000187.'),
]
(D/'talks.json').write_text(json.dumps(talks,ensure_ascii=False,indent=2)+'\n')

problems = [dict(
    id='GP-1965-03',title='The folds and cusps of the perturbed complex square',
    statement=r'For the real smooth map \(F_\varepsilon:\mathbb C\to\mathbb C\), \(F_\varepsilon(z)=z^2+\varepsilon\bar z\), \(\varepsilon>0\), determine the critical set, critical values, local singularity types, and the regular-fibre cardinalities.',
    occurrences=['1965-72.5','1966-115.8'],
    status=r'As of 9 November 2026: settled. The critical circle is \(|z|=\varepsilon/2\); its image is the three-cusped curve \(\varepsilon^2(e^{2it}/4+e^{-it}/2)\), with cusps where \(e^{3it}=1\) and folds elsewhere. There are four preimages in its interior and two in its exterior. The explicit treatment is \citet[\S1, Example 6, pp.~4--5]{arnold1968singularities}, published in 1968 from 1966 lectures. This repeats the earlier indexed question; it does not create a new problem.',
    status_date='2026-11-09',refs=['arnold1968singularities'])]
(D/'problems.json').write_text(json.dumps(problems,ensure_ascii=False,indent=2)+'\n')

corrections = [
 ('P000173','upper-page stability examples','Unclear Rangmax',r'\ru{Ранг} max (maximal rank)','Visual inspection of the handwritten Russian resolves the word; the next Morse formula is consistent.','both','ambiguity'),
 ('P000174','W1--W3 global surface stability list','Fold images transverse; cusp images distinct','Require only ordinary transverse double fold crossings; cusp images must meet no other critical image','The scan faithfully has the shorter list. Triple crossings and cusp--fold coincidences are not stable multigerms; additional conditions belong to the mathematical statement.','both','faithful_error'),
 ('P000175','trefoil caption','Trefoil knot','Retain caption, but no knot type asserted without a specified spatial lift',r'The scan shows planar curves and the abbreviation \ru{трилистн. узел}; it specifies no embedding into a three-dimensional space.','both','ambiguity'),
 ('P000175','threshold 12','Beginning with 12, infinitely many invariants','Retain wording; number/type of moduli is unspecified','The scan confirms the threshold but supplies no quantifiers distinguishing infinitely many types, scalar parameters, and functional invariants.','both','ambiguity'),
 ('P000176','scalar jet algebra',r'\(\mathbb R[x_1,\ldots,x_n]/M^k\)',r'\(\mathbb R[x_1,\ldots,x_n]/M^{k+1}\)',r'The scan has \(k\), without \(+1\). A first jet must retain linear terms; Boardman 1967 §1 uses the usual \(k\)-jet indexing.','both','faithful_error'),
 ('P000176','algebraic structure of jets',r'\(J^k(M,N)\) is an algebraic variety','Polynomial algebraic coordinates exist in each jet fibre; an arbitrary smooth global bundle need not be algebraic','Smooth changes of base coordinates are not assumed algebraic. This qualifies the notebook claim, not the transcription.','both','faithful_error'),
 ('P000176','codimension and equations',r'Codimension \(e\) means \(e\) equations',r'Locally \(e\) independent equations define a smooth codimension-\(e\) locus','The number of equations alone does not imply codimension or smoothness.','both','faithful_error'),
 ('P000177','transversality to a rank stratum',r'\(f\pitchfork\Sigma\)',r'\(j^1f\pitchfork\Sigma\)','The stratum is in the jet bundle rather than the target; the scan uses the abbreviated map symbol.','both','faithful_error'),
 ('P000178','Boardman universal loci','Algebraic subvarieties','Smooth locally closed Boardman strata in local polynomial jet coordinates','Exact-rank loci are not closed; Boardman 1967 Theorem 6.1 uses locally closed submanifolds.','both','faithful_error'),
 ('P000180','critical Jacobian extension',r'\(k=\max\) when the ideal is not the whole \(B\)',r'\(k=\min\) with \(\Delta_k(B)\ne A\)',r'The descending chain and the scan display \(\Delta_{k-1}B=A\), \(\Delta_kB\subsetneq A\). Both \(\max\) and \(B\) conflict with that display.','both','faithful_error'),
 ('P000180','cubic ideal example',r'Crowded superscript on the iteration ending in \((x)\)',r'Successive first extensions: \((x^3)\), \((x^2)\), \((x)\), \(A\)','The written exponents are ambiguous; differentiation fixes the mathematical sequence without claiming a definitive diplomatic superscript reading.','both','ambiguity'),
 ('P000180','Boardman codimension coefficient',r'\(m-n+i_1\)',r'\(n-m+i_1\)',r'The scan confirms \(m-n\) while source is \(M^m\) and target \(N^n\). Boardman 1967 Definition 6.5 has target minus source; the rank-stratum case independently forces the sign.','both','faithful_error'),
 ('P000181',r'definition of \(\mu\)',r'All nonincreasing sequences \(0\le j_s\le i_s\)',r'Exclude the all-zero sequence: \(j_1>0\)',r'The scan omits the exclusion. Boardman 1967 Definition 6.4 explicitly includes \(j_1>0\); otherwise even the length-one formula is wrong.','both','faithful_error'),
 ('P000181','dimension 16 in the informal table','16 and an isolated 4 / four types',r'Read tentatively as first occurrence of corank four, \(c(4)=16\)','The scan does not support a confident count of four smooth equivalence classes. The codimension computation supports corank four but remains an editorial reading.','both','ambiguity'),
 ('P000182','Morin normal form index',r'Ambient \(n\) and length \(k\) of \(1\)-string are intermingled',r'For \(1\le k\le n\) use \(t^{k+1}+\sum_{j=1}^{k-1}u_jt^j\); the written full formula is \(k=n\)','The scan and following examples distinguish a Boardman symbol from ambient dimension; Arnold 1968 §2 supplies the clarified form.','both','ambiguity'),
 ('P000182','composition with the diagonal',r'\(\Delta\circ\bar\psi=\psi\)',r'\(\bar\psi\circ\Delta=\psi\)',r'The written arrows give \(\Delta\) from the vector space to its symmetric square and \(\bar\psi\) onward. Standard composition order reverses the displayed expression.','both','faithful_error'),
 ('P000183','seven orbits / preceding corank-two language',r'Seven orbits of \(\Sigma^{(2,0)}\)','Seven linear orbits of binary quadratic pencils, not of all smooth germs','The seven-way picture classifies a plane, line, or zero image in the three-dimensional space of quadratic forms. Higher-order germs can share a pencil.','both','faithful_error'),
 ('P000184',r'all \(\Sigma^{(2,0)}\) singularities stable','All singularities stable','Stable or suitably generic corank-two germs admit the cited algebra classification; arbitrary symbol membership does not imply stability',r'The scan is unqualified. The germ \((x^2+y^2,xy):\mathbb R^2\to\mathbb R^2\) has symbol \((2,0)\) and is not stable, as checked by the codimension-four rank stratum.','both','faithful_error'),
 ('P000184','dimension diagram',r'Cells \((9,9)\) and \((6,9)\)','Retain diagram and do not infer a missing coordinate convention or inequality','Visual inspection does not fix every cell label and boundary; the later nice-dimensions theorem is cited separately.','both','ambiguity'),
 ('P000185','map on local functions',r'\(f_*\)',r'\(f^*\) (pullback of functions)',r'This is a notation clarification: composition with \(f\) goes from target functions to source functions. The scan faithfully uses the star below.','both','provenance'),
 ('P000185',r'dimension of \(Q\) equals multiplicity',r'Analytic maps \(\mathbb C^n\to\mathbb C^m\); dimension equals number of inverse images','For the direct nearby-value count require a finite holomorphic germ of equal source and target dimension','The note says apparently so and does not state these restrictions; real or unequal-dimensional examples require a different interpretation.','both','faithful_error'),
 ('P000186','preparation theorem heading','Weierstrass preparation for smooth germs','Malgrange smooth preparation / its finite-module consequence',r'The stated category is \(C^\infty\); analytic Weierstrass alone does not give that category. Malgrange 1966, chapter V, and Arnold 1968 §4 identify the result.','both','provenance'),
 ('P000186','first local-algebra family',r'\((x,y,x^a+y^b)\)',r'\((xy,x^a+y^b)\)',r'The scan has a mark between \(x\) and \(y\) that can resemble a comma; taking two separate generators would collapse the algebra to \(\mathbb R\). The checked final Mather table confirms \(xy\).','both','ambiguity'),
 ('P000186','elliptic three-generator family',r'\((x^a,xy^{a-1},x^2+y^2)\)',r'\((x^a,x^{a-1}y,x^2+y^2)\)',r'The scan confirms the mixed exponent on \(y\). Mather 1971 §7 gives \(x^{a-1}y\). At \(a=3\) the literal algebra has length 6, while the corrected family has length 5; two independent exact algorithms and a normal-form argument agree.','both','faithful_error'),
 ('P000186','names IV and V','IV has three generators; V has two','Record notebook labels, but use final Mather convention IV for two generators and V for three','The scan and the published final table differ in labels. This is a convention/provenance discrepancy rather than a false theorem by itself.','both','provenance'),
 ('P000186','left margin of algebra list',r'\(n\ge m1.;\ n>m3.;\ldots\)',r'Dimension conditions followed by row numbers \(1,3,\ldots\)',r'The visual layout separates row enumerators from the preceding inequalities. Do not read a spurious \(n\ge m+1\) into concatenated text.','both','ambiguity'),
 ('P000187','seminar plan, index lectures','Dynkin','Dynin',r'The Russian transcription and scan read \ru{Дынин}, with no \ru{к}; this refers to the index lecturer named in the plan.','en','translation'),
]
with (D/'corrections.csv').open('w',newline='') as f:
    w=csv.writer(f)
    w.writerow(['page','place','transcription_reads','should_read','evidence','applies_to','type'])
    w.writerows(corrections)

# No research development is warranted by a C/D item in these four records.
(D/'development.tex').write_text('% No C/D item in records 115--118 qualifies for a new research development.\n% Exact editorial computations are supplied separately and marked in the item annotations.\n')
