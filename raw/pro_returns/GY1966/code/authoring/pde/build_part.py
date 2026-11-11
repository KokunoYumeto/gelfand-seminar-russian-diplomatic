"""Research data for GY1966 records 105--114."""
import json,csv,re
from pathlib import Path
OUT=Path(__file__).parent
talks,items,problems,corrections=[],[],[],[]
def talk(record,date,speaker,pages,title,kind,summary):
    talks.append(dict(record=record,date=date,speaker=speaker,pages=pages,title=title,kind=kind,summary=summary))
def item(record,pages,kind,title,notes,statement,reconstruction,cls,fate,status,refs=(),literal="correct with missing hypotheses",match="exact",verification="read the result",development="annotated",problem="",worth="",confidence="high",speaker=None):
    n=1+sum(x["record"]==record for x in items)
    x=dict(id=f"1966-{record}.{n}",record=record,pages=pages,kind=kind,title=title,notes=notes,statement=statement,reconstruction=reconstruction,**{"class":cls},fate=fate,present_status="As of 9 November 2026: "+status,literal_correctness=literal,publication_match=match,verification=verification,development=development,problem=problem,worth=worth,refs=list(refs),confidence=confidence)
    if speaker:x["speaker"]=speaker
    items.append(x)
    return x["id"]
def problem(pid,title,statement,occurrences,status,refs):
    problems.append(dict(id=pid,title=title,statement=statement,occurrences=occurrences,status="As of 9 November 2026: "+status,status_date="2026-11",refs=refs))
def corr(page,place,reads,should,evidence,applies="both",kind="faithful_error"):
    # Table cells are emitted as LaTeX. Preserve explicit mathematics and make
    # literal source punctuation safe in every remaining prose segment.
    def safe_cell(value):
        segments=re.split(r'(\\\(.*?\\\)|\\\[.*?\\\])',value,flags=re.S)
        for index in range(0,len(segments),2):
            segments[index]=re.sub(r'(?<!\\)_',r'\\_',segments[index])
            segments[index]=re.sub(r'(?<!\\)\^',r'\\textasciicircum{}',segments[index])
        return ''.join(segments)
    corrections.append(dict(page=page,place=safe_cell(place),transcription_reads=safe_cell(reads),should_read=safe_cell(should),evidence=safe_cell(evidence),applies_to=applies,type=kind))
def save():
    for name,data in (("talks",talks),("items",items),("problems",problems)):
        (OUT/f"{name}.json").write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n")
    with (OUT/"corrections.csv").open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=["page","place","transcription_reads","should_read","evidence","applies_to","type"]);w.writeheader();w.writerows(corrections)

talk(105,"1966-10-03","Louis Nirenberg","P000160-P000164","Complex powers and an analytic index formula","talk",
 r"""The actual notes occupy P000161--P000162, after the preceding talk on P000160. Nirenberg reports Seeley's and H\"ormander's analytic approach to the index: positive-spectrum cancellation, complex powers, continuation of kernels and a local expression at exponent zero. Gelfand comments on analytic descriptions of topological quantities. The catalogue's wider interval also contains Minlos's next lecture. Both formula-critical pages were inspected against their scans and Seeley's contemporary preprint in its published Russian translation \citep[pp.~96--98]{seeley1968powers}.""")
item(105,"P000161","remark","Analytic expressions for topological index data",
 r"""The report is described as an analytic formula without topology; Gelfand replies that the Atiyah--Singer formula and Pontryagin classes also admit analytic expressions, for example through degrees of maps.""",
 r"""The Fredholm index of an elliptic operator on a closed manifold depends on the topological class of its principal symbol. Characteristic classes have differential-form representatives constructed from connections, allowing analytic integral formulae for topological invariants.""",
 r"""This is a conceptual comparison. No particular degree map or characteristic polynomial is supplied. The doubtful word preceding “terms disappear” is not used to assert independence of a particular coefficient in the local density.""",
 "E",r"""The index theorem predates this seminar; the analytic construction actually developed next is Seeley's \citep[pp.~96--98]{seeley1968powers}.""",
 r"""established background; no separate conjecture is specified.""",["seeley1968powers"],match="partial",speaker="I. M. Gelfand")
item(105,"P000161","theorem","Positive spectra of the two Laplacians",
 r"""For \(\lambda>0\), \(E_\lambda(L^*L)\) and \(E_\lambda(LL^*)\) have common dimension \(d_\lambda\); the identification explicitly excludes zero.""",
 r"""Let \(L:C^\infty(M;E)\to C^\infty(M;F)\) be elliptic of positive order on a closed smooth manifold with Hermitian bundles and a smooth positive density. For \(\lambda>0\), \(L:E_\lambda(L^*L)\to E_\lambda(LL^*)\) is an isomorphism with inverse \(\lambda^{-1}L^*\). Moreover \(\ker L^*L=\ker L\) and \(\ker LL^*=\ker L^*\).""",
 r"""The inverse and analytic setting are supplied. Direct composition proves the eigenspace assertion; \(\langle L^*Lu,u\rangle=\|Lu\|^2\) proves the kernel assertion.""",
 "E",r"""This elementary spectral argument is the input to the complex-power index calculation \citep[p.~96]{seeley1968powers}.""",
 r"""standard and correct under the stated domain hypotheses.""",["seeley1968powers"],literal="correct")
item(105,"P000161","construction","Spectral complex powers and traces",
 r"""For \(\operatorname{Re}s\ll0\), \((I+L^*L)^s\) has an eigenfunction kernel whose integrated diagonal gives \(\sum d_\lambda(1+\lambda)^s\).""",
 r"""If \(L\) has order \(r>0\), \(A=I+L^*L\) has order \(2r\). For \(\operatorname{Re}s<-n/(2r)\), \(A^s\) is trace class and \(\operatorname{Tr}A^s=\sum_j(1+\lambda_j)^s\), counting multiplicity. The kernel is distributionally \(\sum_j(1+\lambda_j)^s\Psi_j(x)\Psi_j(y)^*\); sufficiently negative real part gives continuity and the diagonal trace integral.""",
 r"""One may sum over distinct eigenvalues with multiplicities, or over a full eigenbasis without an additional multiplicity factor. The convergence threshold and bundle adjoint are supplied.""",
 "E",r"""Spectral calculus is the known starting point for the continuation in \citet[pp.~96--97]{seeley1968powers}.""",
 r"""standard with convergence qualifications.""",["seeley1968powers"])
item(105,"P000161","theorem","Regularized trace difference and index",
 r"""All positive-eigenvalue terms cancel in \(\operatorname{Tr}(I+L^*L)^s-\operatorname{Tr}(I+LL^*)^s\), leaving \(\dim\ker L-\dim\ker L^*\), independent of \(s\).""",
 r"""Initially for \(\operatorname{Re}s<-n/(2r)\), the difference of the two traces equals \(\operatorname{ind}L\). Their meromorphic continuations therefore have the same constant difference, in particular at a common regular point such as zero.""",
 r"""At zero the separately unregularized traces are not finite. The continuation identity follows from the identity theorem applied to the trace-class half-plane.""",
 "E",r"""The cancellation is elementary and underlies the local formula \citep[pp.~96--98]{seeley1968powers}.""",
 r"""established; regularization must remain explicit.""",["seeley1968powers"],literal="correct")
item(105,"P000162","construction","Contour powers with a spectral cut",
 r"""An angular gap about the negative ray is assumed for the principal symbol; powers use a resolvent contour and multiplication by integer powers. A parenthesis proposes reducing to order one by multiplication by an invertible operator.""",
 r"""Let \(A\) be an invertible classical elliptic operator of positive order \(m\) on a closed manifold, with a ray avoided by its principal-symbol spectra and operator spectrum. Fix a branch and oriented contour. Then \(A^s=(2\pi i)^{-1}\int_\Gamma\lambda^s(\lambda-A)^{-1}d\lambda\), initially for negative real part, extends by integer powers to a holomorphic family satisfying \(A^sA^t=A^{s+t}\). The parameter resolvent estimate applies along the contour.""",
 r"""The symbol condition concerns eigenvalues in the bundle case; invertibility and an operator spectral cut are added. Order reduction can simplify an index problem but does not preserve individual powers or kernels under arbitrary multiplication.""",
 "B",r"""Seeley's circulated preprint contains this construction; its Russian translation appeared in 1968 \citep[pp.~96--97]{seeley1968powers}. Nirenberg is reporting another author's work.""",
 r"""standard spectral-cut calculus.""",["seeley1968powers"])
item(105,"P000162","theorem","Holomorphy and diagonal meromorphic continuation",
 r"""The kernel is \(C^k\)-holomorphic when \(\operatorname{Re}(ms)<-n-k\), entire and smooth off the diagonal, and meromorphic on the diagonal with possible simple poles \((j-n)/m\); zero is regular.""",
 r"""Under the preceding hypotheses, \(A^s\) is classical of order \(ms\), with holomorphic distribution kernel. Its values are \(C^k\) in the stated half-plane and entire in \(C^\infty\) on compact subsets off the diagonal. The initially defined diagonal density has meromorphic continuation with at most simple poles at \((j-n)/m\), \(j\ge0\); the candidate pole at zero is removable, and others may cancel.""",
 r"""“Possible” poles are not necessarily actual poles. The continued diagonal is a density-valued endomorphism and is not restriction of an arbitrary distribution to the diagonal.""",
 "B",r"""These match the consecutive kernel assertions of \citet[p.~97]{seeley1968powers}.""",
 r"""established for classical elliptic operators with a spectral cut.""",["seeley1968powers"],literal="correct")
item(105,"P000162","claim","Exponent zero versus diagonal continuation",
 r"""The manuscript says \ru{при \(s=0\) это не единичный оператор}, with the explanation that the kernel is not a delta function.""",
 r"""As an operator \(A^0=I\), whose full distribution kernel is the identity delta distribution. The finite value at zero of the meromorphically continued diagonal \(K_s(x,x)\) results from restricting first in a left half-plane and then continuing. It is not the diagonal restriction of the full kernel of \(A^0\).""",
 r"""This corrects a conflation in the handwritten source, not a mistranscription. Acting on each eigenvector verifies \(A^0=I\) directly.""",
 "E",r"""The functional calculus and continued diagonal in \citet[pp.~96--97]{seeley1968powers} distinguish these operations.""",
 r"""the literal operator assertion is false; the intended regularized-diagonal distinction is valid.""",["seeley1968powers"],literal="false as written",match="partial")
item(105,"P000162","method","Local resolvent coefficient and index density",
 r"""The notes write \((2\pi)^nK_0(x,x)=m^{-1}\int_{|\xi|=1}\int_{-\infty}^0b_{-m-n}(x,\xi;\lambda)\,d\lambda\,dS\), then take the difference of such expressions for the index.""",
 r"""Continue the diagonal densities of \((I+L^*L)^s\) and \((I+LL^*)^s\) to zero. The integral of the difference of their fibre traces is \(\operatorname{ind}L\). Each local continued density is computable from the parameter-resolvent symbol term of degree \(-m-n\), with its resolvent-sign and contour conventions fixed consistently.""",
 r"""The coefficient formula is recorded in Seeley's convention. Replacing \((A-\lambda)^{-1}\) by \((\lambda-A)^{-1}\) changes the coefficient sign; the contour must change consistently. The invariant assertion is the integrated difference.""",
 "B",r"""The coefficient expression is \citet[p.~97, formula (II)]{seeley1968powers}; it is the close publication match.""",
 r"""established analytic index machinery.""",["seeley1968powers"])
save()

talk(106,"1966-10-03","R. A. Minlos","P000162-P000165","Infinite configurations and correlation axioms","talk",
 r"""The actual lecture is P000163--P000164. It constructs the measurable space of locally finite configurations, discusses limiting Gibbs measures and mixing, invokes ergodicity for mean density and introduces thermodynamic functions. Gelfand asks for intrinsic axioms on correlations. Minlos's expanded lectures trace their first delivery to Khumsan in September 1965 and their amplification to the autumn 1966 Gelfand seminar \citep[pp.~137--138]{minlos1968lectures}. That publication distinguishes results and hypotheses more carefully than this notebook.""")
item(106,"P000163","construction","Unlabelled finite configurations",
 r"""Collision-free labelled configurations map to \(N\)-point subsets \(C_{\Omega,N}\). Symmetry of \(H\) allows the Hamiltonian and Gibbs measure to descend; the discarded collision set has measure zero.""",
 r"""For bounded Borel \(\Omega\subset\mathbb R^\nu\), quotient the collision-free subset of \(\Omega^N\) by permutations. A symmetric measurable Hamiltonian with positive finite partition function defines a Gibbs probability, whose pushforward is a law on simple \(N\)-point configurations. Lebesgue reference measure gives all collision diagonals measure zero.""",
 r"""The \(1/N!\) factor belongs consistently to the quotient reference measure or to both normalized integrals. The null-set claim presupposes a non-atomic reference measure.""",
 "E",r"""The construction is explicit in \citet[\S1, pp.~60--62]{minlos1967limiting} and \citet[Lecture II]{minlos1968lectures}.""",
 r"""standard configuration-space probability.""",["minlos1967limiting","minlos1968lectures"],literal="correct")
item(106,"P000163","definition","Counting-cylinder sigma algebra",
 r"""\(C_\infty\) consists of finite or countable subsets without accumulation points; the sigma algebra is generated by \(n(d,U_i)=k_i\) for finite collections of disjoint sets.""",
 r"""Let \(\Gamma\) be the locally finite simple configurations in \(\mathbb R^\nu\), with the sigma algebra generated by \(N_U(\gamma)=|\gamma\cap U|\) for bounded Borel \(U\). Finite intersections of counting events generate it; disjoint observation sets suffice by a finite Boolean refinement.""",
 r"""Bounded Borel sets and ambient local finiteness specify the intended measurable space.""",
 "A",r"""This is the space used in Minlos's forthcoming construction \citep[\S1]{minlos1967limiting}; A marks the exact authorial publication, not a claim of novelty for counting cylinders.""",
 r"""the standard measurable configuration space.""",["minlos1967limiting"],literal="correct")
item(106,"P000163","theorem","Dilute limiting Gibbs distribution",
 r"""The notes ask for a limiting space with the finite-volume asymptotic properties and say existence is proved at low density.""",
 r"""A verified precise version is grand canonical: for stable pair interactions with integrable Mayer function, and sufficiently small activity at fixed \(\beta>0\), the low-activity expansion constructs a translation-invariant probability law on locally finite configurations with the limiting local distributions. A concrete subclass consists of hard-core finite-range potentials bounded below outside the core.""",
 r"""Stability is \(H_N\ge-BN\); Mayer integrability is \(\int|e^{-\beta\Phi(x)}-1|dx<\infty\). The ensemble and small parameter are supplied. This does not alone establish every canonical fixed-density limit or equivalence of ensembles.""",
 "A",r"""\citet[\S\S1--3]{minlos1967limiting}, received 20 December 1966, is the close construction. The canonical limiting-measure hypothesis is separately identified by \citet[Lecture II, pp.~150--152]{minlos1968lectures}.""",
 r"""proved in dilute regimes; unrestricted density, uniqueness and complete phase diagrams are different questions.""",["minlos1967limiting","minlos1968lectures"],match="partial")
item(106,"P000163","claim","Uniform mixing and its quantifiers",
 r"""Separated cylinder events satisfy \(\mu(A\cap B)-\mu(A)\mu(B)\to0\), with the gloss “uniformly over all pairs \(U\)”; the limiting measure is said to have this property.""",
 r"""The later lecture formulation fixes bounded \(U\) and \(A\in\mathcal F_U\), then asks for \(\sup_{V:\operatorname{dist}(U,V)\ge r}\sup_{B\in\mathcal F_V}|\mu(A\cap B)-\mu(A)\mu(B)|\to0\). Uniformity over unrestricted sizes of both windows is stronger. Pointwise correlation convergence does not by itself supply either uniformity or a quantitative variance bound.""",
 r"""The fixed-event quantifier is taken from the expanded lectures, not silently substituted into the diplomatic transcription. The 1967 existence paper explicitly defers the mixing/ergodicity discussion.""",
 "A",r"""\citet[Lecture II, formula (2.5), pp.~151--152]{minlos1968lectures} states the careful version and its general-regime hypothesis status; low-density cluster theory already appears in \citet{ruelle1964cluster}.""",
 r"""qualified dilute clustering is established, but the notebook's unrestricted gloss is unsupported.""",["minlos1968lectures","ruelle1964cluster"],match="partial",confidence="medium")
item(106,"P000164","theorem","Ergodic mean density",
 r"""Almost every configuration has a mean density, by Birkhoff's theorem and ergodicity.""",
 r"""For a translation-invariant ergodic point-process law with finite intensity \(\rho=\mathbb E N_{[0,1)^\nu}\), growing cubes satisfy \(N_{Q_R}/|Q_R|\to\rho\) almost surely. Without ergodicity the limit is an invariant conditional expectation and can be random.""",
 r"""Finite intensity and a specified averaging sequence are added. The assertion is a law of large numbers, not a rate or central limit theorem.""",
 "E",r"""This application of the spatial ergodic theorem is restated in \citet[Lecture II, p.~152]{minlos1968lectures}.""",
 r"""established; mixing is stronger than necessary.""",["minlos1968lectures"])
cid=item(106,"P000164","question","Characterizing correlation hierarchies",
 r"""Gelfand proposes starting with axioms on correlation functions and asks how to single them out.""",
 r"""Given a full hierarchy of symmetric locally finite factorial correlation measures with \(\rho_0=1\), characterize when it is realized by a probability law on locally finite configurations. The key positivity condition tests finite configuration polynomials \(KG(\gamma)=\sum_{\eta\subset\gamma,\ |\eta|<\infty}G(\eta)\): if \(KG\ge0\) pointwise, then the corresponding integral against the correlation measure must be nonnegative. Symmetry, this positivity and normalization characterize realizability in Lenard's correlation-measure framework; uniqueness is separate.""",
 r"""This is a precise reconstruction of the one-line proposal. Entrywise nonnegativity of the correlations is insufficient. Full-hierarchy realizability differs from a truncated pair-correlation problem.""",
 "B",r"""\citet[abstract and main characterization]{lenard1975characterization} gives necessary and sufficient conditions and explicitly permits nonunique realizations; \citet{lenard1973correlation} treats determinacy.""",
 r"""established at the level of an infinite family of positivity conditions.""",["lenard1975characterization","lenard1973correlation"],verification="publisher metadata checked",problem="GP-1966-20",speaker="I. M. Gelfand")
problem("GP-1966-20","Realizability of a full correlation hierarchy",
 r"""Characterize the symmetric locally finite factorial moment measures of probability laws on locally finite configurations, distinguishing existence from uniqueness.""",[cid],
 r"""Lenard's symmetry, positivity and normalization characterization supplies existence; determinacy requires additional conditions.""",["lenard1975characterization","lenard1973correlation"])
item(106,"P000164","theorem","Partition function and thermodynamic limit",
 r"""The notes define \(Z=N!^{-1}\int e^{-\beta H}da\), say \(E,P,S,F\) are expressed through \(\log Z\), and promise \(\lim N^{-1}\log Z\).""",
 r"""For stable tempered classical pair potentials, regular expanding vessels and fixed admissible density \(N/|\Omega|\to\rho>0\), the thermodynamic limit defines configurational free energy per particle through \(-(\beta N)^{-1}\log Z_{\Omega,N}\). Stability excludes collapse, decay controls long-range tails, and admissibility excludes impossible hard-core densities. Existence of this limit does not automatically imply convergence of every derivative.""",
 r"""The potential assumptions and regular vessel sequence are absent from this page. Full phase-space normalization adds a known momentum contribution. No all-shapes assertion is inferred.""",
 "E",r"""The expanded account is \citet[Lecture IV, \S\S1--4, pp.~164--176]{minlos1968lectures}; the thermodynamic-limit programme predates this talk.""",
 r"""established under stability and decay assumptions, compatible with phase-boundary nondifferentiability.""",["minlos1968lectures"],match="partial")
save()

talk(107,"1966-10-10","R. A. Minlos","P000163-P000166","Energy, wall pressure and entropy","talk",
 r"""The fourth lecture occupies the upper part of P000165. It records the energy derivative, a separate moving-wall pressure conjecture, and entropy per particle. The manuscript itself has an entropy sign error and an erroneous reciprocal-temperature factor. Arnold starts below the separator. The expanded treatment is \citet[Lecture IV]{minlos1968lectures}.""")
item(107,"P000165","theorem","Mean energy and temperature differentiation",
 r"""\(E=\langle H\rangle=-\partial_\beta\log Z\), with \(\langle H\rangle\approx Ne(v,\beta)\) for pair interactions; representativeness is said to have been proved.""",
 r"""For a \(\beta\)-independent Hamiltonian and fixed reference measure, finiteness of \(Z\) and of the first energy moment in a neighbourhood permits \(-\partial_\beta\log Z=\mathbb EH\). If convex functions \(f_N=N^{-1}\log Z_N\) converge on an open interval to \(f\), then \(f_N'(\beta)\to f'(\beta)\) at differentiability points of \(f\), and \(N^{-1}\mathbb EH_N\to-f'(\beta)\).""",
 r"""Numerator and denominator must use the same \(1/N!\) convention. Mean convergence is weaker than concentration; the latter requires fluctuation control.""",
 "E",r"""The identities and thermodynamic use are in \citet[Lecture IV, \S\S1--3]{minlos1968lectures}.""",
 r"""standard, with derivative limits qualified at phase transitions.""",["minlos1968lectures"],match="partial")
item(107,"P000165","question","Limiting wall pressure",
 r"""\(p(x)=\tau_1(x)\), \(P=S^{-1}\int p\,d\sigma\); a hypothesis says wall pressure tends to a constant. The notes correctly warn that fixed-window convergence of \(\tau_1\) does not imply this.""",
 r"""A definite theorem would require hard-wall or other boundary conditions, a family of growing vessels, a moving boundary observation point, normalization of pressure, and the exact uniformity sought. These are unspecified, so a unique modern proposition cannot be extracted.""",
 r"""For a classical hard wall the contact relation is \(\beta p_{\rm wall}=\rho_{\rm contact}\), with the appropriate mechanical stress. It is not a universal identity of pressure with a bulk correlation. Moving boundary points are outside the earlier fixed-window limit.""",
 "F",r"""The thermodynamic framework is present in \citet[Lecture IV]{minlos1968lectures}, but no publication establishing this unrestricted moving-wall assertion was verified.""",
 r"""insufficiently specified to label solved or open; the distinction of limiting procedures is valid.""",["minlos1968lectures"],literal="not determinable",match="thematic only",verification="unresolved lead",confidence="medium")
item(107,"P000165","claim","Pressure normalization",
 r"""The manuscript writes \(p=\partial_V\log Z\).""",
 r"""Physical pressure with \(k_B=1\) is \(p=\beta^{-1}(\partial_V\log Z)_{\beta,N}\), whenever a differentiable family of vessel deformations defines the derivative. The written equation instead holds for reduced pressure \(\beta p\).""",
 r"""The units are unspecified; the neighbouring contact-density formula suggests reduced pressure. This is a normalization ambiguity, not a certain transcription error.""",
 "E",r"""These conventions belong to the identities reviewed by \citet[Lecture IV]{minlos1968lectures}.""",
 r"""established after fixing units and the volume variation.""",["minlos1968lectures"],match="partial")
item(107,"P000165","claim","Entropy sign and temperature factor",
 r"""The scan has \(S=\int\pi\log\pi\) and \(S/N=N^{-1}\log Z-\beta^{-1}\partial_\beta(N^{-1}\log Z)\).""",
 r"""For \(\pi=Z^{-1}e^{-\beta H}\), Gibbs entropy is \(S=-\int\pi\log\pi=\log Z+\beta\mathbb EH=\log Z-\beta\partial_\beta\log Z\). Thus \(S/N=f_N-\beta f_N'\). An opposite entropy sign convention changes both terms consistently.""",
 r"""Substitution of \(\log\pi=-\beta H-\log Z\) verifies the correction without a thermodynamic-limit theorem. Both discrepancies are present in the handwriting.""",
 "E",r"""The corrected identity is standard in \citet[Lecture IV, \S1]{minlos1968lectures}; the two notebook formulae cannot share a consistent convention.""",
 r"""false as written; the correction is completely determined.""",["minlos1968lectures"],literal="false as written",match="partial")
item(107,"P000165","claim","Entropy per particle",
 r"""The limit of entropy per particle is asserted.""",
 r"""If \(f_N=N^{-1}\log Z_N\) converges on an open interval to differentiable \(f\), convex convergence gives \(S_N/N\to f(\beta)-\beta f'(\beta)\). At a nondifferentiability point this argument provides no unique limit without a state or one-sided prescription.""",
 r"""This sufficient formulation covers a regular single-phase regime without inferring differentiability merely from existence of free energy.""",
 "E",r"""The relevant expanded account is \citet[Lecture IV, \S\S1--3]{minlos1968lectures}.""",
 r"""standard with the phase qualification.""",["minlos1968lectures"],match="partial")
save()

talk(108,"1966-10-10","V. I. Arnold","P000164-P000168","Lagrangian planes and the Maslov class","talk",
 r"""Arnold begins in lower P000165 and continues through P000166. He identifies \(\Lambda(n)=U(n)/O(n)\), constructs determinant squared and pulls the circle class back by the tangent map of a Lagrangian manifold. The exact authorial match is \citet{arnold1967characteristic}, submitted 28 September 1966, before this talk, and published January 1967. It clarifies the geometric class behind earlier occurrence 1964-21.3.""")
item(108,"P000165","definition","Three compatible linear structures",
 r"""The Euclidean metric, multiplication by \(i\), and \([x,y]=(Ix,y)\) are introduced. The pairwise intersections of their preserving groups all equal \(U(n)\).""",
 r"""If \(g\) is positive definite and \(J^2=-I\), \(g(Jv,Jw)=g(v,w)\), then \(\omega(v,w)=g(Jv,w)\) is nondegenerate skew symmetric. Preserving any two of \(g,J,\omega\) preserves the third. Thus the pairwise intersections of \(O(2n)\), \(GL(n,\mathbb C)\), and \(Sp(2n,\mathbb R)\) equal \(U(n)\).""",
 r"""Compatibility of \(g\) and \(J\) is explicit; arbitrary metric and complex structures need not satisfy the assertion.""",
 "E",r"""This linear algebra is Lemma 1.1 of \citet[\S1.1]{arnold1967characteristic}.""",
 r"""standard.""",["arnold1967characteristic"],literal="correct")
item(108,"P000165-P000166","definition","Isotropic and Lagrangian spaces",
 r"""An \(n\)-plane with vanishing symplectic form is Lagrangian. Real and imaginary planes are examples; planes are said to have dimension at most \(n\), and every curve for \(n=1\) is Lagrangian.""",
 r"""An isotropic subspace \(W\subset V^{2n}\) satisfies \(\omega|_W=0\), hence \(\dim W\le n\). It is Lagrangian when \(\dim W=n\), equivalently \(W=W^\omega\). An immersed \(n\)-manifold is Lagrangian when all tangent spaces are. Every immersed curve in a symplectic surface satisfies this.""",
 r"""The inequality concerns isotropic spaces; “Lagrangian” means maximal dimension. A singular arbitrary curve need not be a submanifold.""",
 "E",r"""These are the definitions used in \citet[\S1.2]{arnold1967characteristic}.""",
 r"""standard with the terminology clarified.""",["arnold1967characteristic"])
item(108,"P000166","theorem","Generating functions for Lagrangian graphs",
 r"""The graph \(p=p(q)\) is Lagrangian if and only if \(p=\partial S/\partial q\).""",
 r"""For a smooth one-form \(\alpha=\sum p_i(q)dq_i\) on \(U\subset\mathbb R^n\), its cotangent graph is Lagrangian exactly when \(d\alpha=0\). Locally this is equivalent to \(\alpha=dS\). Globally it is equivalent to exactness, and holds in particular for simply connected \(U\).""",
 r"""The local qualification is missing. A closed angular one-form on an annulus has a Lagrangian graph but no globally single-valued primitive.""",
 "E",r"""This is the standard generating-function example in the framework of \citet[\S1]{arnold1967characteristic}.""",
 r"""correct locally; exactness is required globally.""",["arnold1967characteristic"],match="partial")
item(108,"P000166","theorem","Lagrangian Grassmannian as a homogeneous space",
 r"""\(U(n)\) acts transitively and \(O(n)\) stabilizes the real plane, so \(\Lambda(n)=U(n)/O(n)\).""",
 r"""A real orthonormal basis of any Lagrangian plane extends complex linearly to a unitary map. The stabilizer of the standard real plane is exactly \(O(n)\), yielding a smooth identification \(\Lambda(n)\cong U(n)/O(n)\).""",
 r"""A compatible metric presents the homogeneous space; Lagrangian subspaces themselves are defined by the symplectic form.""",
 "A",r"""This is Lemma 1.2 in \citet[\S1.2]{arnold1967characteristic}, already submitted when the lecture was given.""",
 r"""established; A records the matched authorial exposition rather than priority for elementary linear algebra.""",["arnold1967characteristic"],literal="correct")
item(108,"P000166","construction","Determinant-square fibration",
 r"""Determinant squared descends to \(\Lambda(n)\) because orthogonal determinants are \(\pm1\); a diagram relates \(SO,O,S^0\), \(SU,U,S^1\), and \(S\Lambda,\Lambda,S^1\).""",
 r"""The map \(d([U])=(\det U)^2\) from \(U(n)/O(n)\) to \(S^1\) is well defined. Its fibre over one is \(SU(n)/SO(n)\), since a determinant-minus-one representative can be adjusted by a real reflection. Quotient maps and squaring on \(S^1\) give the commutative diagram of fibrations.""",
 r"""The reflection argument identifies the handwritten \(S\Lambda\). The vertical maps are not all inclusions.""",
 "A",r"""This is the construction of \citet[\S1.3]{arnold1967characteristic}.""",
 r"""the standard universal Maslov construction.""",["arnold1967characteristic"],literal="correct")
item(108,"P000166","construction","Maslov cohomology class",
 r"""The tangent map \(M\to\Lambda(n)\to S^1\) assigns a loop the degree of its final circle map, yielding a class in \(H^1(M,\mathbb Z)\).""",
 r"""For a Lagrangian immersion \(i:M\to\mathbb R^{2n}\), use the ambient trivialization and tangent Gauss map \(\tau(x)=di_x(T_xM)\). Then \(\mu_M=(d\circ\tau)^*\eta\in H^1(M;\mathbb Z)\), for the chosen generator \(\eta\) on the circle. Evaluation on a loop is its winding number under \(d\circ\tau\).""",
 r"""The ambient trivialization is available in this phase space. A general symplectic ambient manifold requires the appropriate relative formulation. The doubtful “katsikl” means cocycle/class in this mathematical context.""",
 "A",r"""\citet[\S\S1--2]{arnold1967characteristic} develops the class already implicit in occurrence 1964-21.3; submission preceded the talk and publication followed it.""",
 r"""established, with an orientation-dependent sign convention.""",["arnold1967characteristic"],literal="correct")
item(108,"P000166","remark","Morse index and quantization",
 r"""The Maslov index occurs in asymptotic formulae; the Morse index is obtained by counting conjugate points of a geodesic. Another geometric definition by Maslov is mentioned.""",
 r"""For a nondegenerate fixed-endpoint geodesic segment, the index of the second variation equals the sum of interior conjugate-point multiplicities. The relative Maslov index of the path of Jacobi-data Lagrangian subspaces gives the same integer under consistent sign and endpoint conventions. In semiclassical quantization it measures caustic phase changes.""",
 r"""A relative path index is required; an arbitrary closed-loop winding number is not automatically a Morse index. The alternative definition is not actually recorded.""",
 "A",r"""These applications belong to \citet[\S\S2--3]{arnold1967characteristic}; the Morse index theorem itself is older.""",
 r"""established with multiplicities and endpoint conventions.""",["arnold1967characteristic"],match="partial")
save()

talk(109,"1966-10-17","I. M. Gelfand","P000166-P000168","Recovering a compact group from tensor intertwiners","talk",
 r"""The actual report is the upper-middle portion of P000167. Gelfand explains reconstruction from irreducible representation spaces and their tensor intertwiners. Multiplicities alone and arbitrary matrix solutions require corrections. The top of the same page separately says “Minlos, Lecture 5: Phase transitions”, with no mathematical content following that heading; no additional MCCME record or phase-transition theorem is invented. Nirenberg's heat-kernel report below belongs to record 110.""")
item(109,"P000167","construction","Tensor decomposition and intertwiner data",
 r"""For a finite or compact \(G\), irreducible finite-dimensional spaces \(A_i\) are given, together with \(A_i\otimes A_k\cong\sum A_j\) and component maps \(d_{ik}^j\).""",
 r"""For a compact topological group, finite-dimensional continuous unitary representations are completely reducible. Every tensor product \(V_i\otimes V_k\) decomposes as a finite direct sum of irreducibles with multiplicity spaces, and a choice of unitary decomposition gives intertwining maps. A general compact group can have infinitely many irreducible isomorphism classes, even though each individual tensor product is finite dimensional.""",
 r"""The notebook's finite list \(A_1,\ldots,A_n\) is appropriate to a finite group or a selected finite list, not to all irreducibles of an arbitrary compact group. The phrase “each 1500 times” illustrates a sufficiently large ambient direct sum rather than a universal multiplicity bound.""",
 "E",r"""This is classical compact-group representation theory, the concrete category recalled by \citet[summary]{doplicherroberts1989duality}.""",
 r"""standard; multiplicity spaces and actual intertwining maps are different levels of information.""",["doplicherroberts1989duality"],verification="publisher metadata checked")
item(109,"P000167","claim","Fusion multiplicities do not determine even a finite group",
 r"""The crossed-out and inserted line is transcribed as saying that properties of the tensor multiplicities recover a finite group, although not a compact group.""",
 r"""If only the fusion coefficients and dimensions of irreducibles are meant, the assertion is false. The dihedral group of order eight and the quaternion group each have four one-dimensional complex irreducibles forming \(C_2\times C_2\), and one two-dimensional irreducible \(W\), with \(\chi\otimes W=W\) and \(W\otimes W=\bigoplus_\chi\chi\). They are not isomorphic: their numbers of involutions differ.""",
 r"""This elementary countercheck is supplied here. It tests precisely the reading “multiplicities alone”; extra tensor coherence or intertwiner data could change the claim. The overwritten sentence remains a textual ambiguity.""",
 "E",r"""Classical Tannaka reconstruction uses more than a representation ring. The required categorical data are explicit in the comparison drawn by \citet[summary]{doplicherroberts1989duality}.""",
 r"""false on the multiplicity-only reading. No unsolved finite-group reconstruction problem is inferred.""",["doplicherroberts1989duality"],literal="false as written",match="partial",verification="publisher metadata checked")
item(109,"P000167","theorem","Tannaka reconstruction requires unit and reality conditions",
 r"""Replace all representation matrices \(T_i(g)\) by arbitrary linear maps \(C_i\) satisfying the displayed tensor intertwining equations; the notes claim every solution comes from a group element.""",
 r"""Let \(\mathcal R(G)\) be the rigid symmetric category of finite-dimensional continuous unitary representations of compact \(G\), and \(F\) its forgetful functor to Hilbert spaces. The group of unitary tensor-natural automorphisms of \(F\), with \(C_{\mathbf1}=1\), is naturally \(G\), with its compact topology. The naturality conditions include all intertwiners and dual compatibility.""",
 r"""Unqualified equations admit the zero family unless unit normalization is imposed. Merely complex linear tensor automorphisms need not be unitary; even for \(S^1\) the character family \(C_k=z^k\), \(z\in\mathbb C^\times\), exhibits the missing compact reality condition.""",
 "E",r"""The classical concrete duality predates the seminar. \citet[summary and references 18, 27]{doplicherroberts1989duality} explicitly contrasts it with their later abstract symmetric \(C^*\)-category reconstruction.""",
 r"""established with unitary tensor-natural data; the literal unrestricted matrix formulation is false.""",["doplicherroberts1989duality"],literal="false as written",match="partial",verification="publisher metadata checked")
item(109,"P000167","remark","An unspecified extension to SL(2,R)",
 r"""The report ends “There is a generalization to \(SL(2,\mathbb R)\)”.""",
 r"""No class of representations, topology, dual object, admissible tensor operations or reconstruction statement is given. Consequently the particular noncompact duality theorem intended cannot be identified from this sentence.""",
 r"""Finite-dimensional representations alone, all unitary representations, and operator-algebraic duality lead to materially different statements. A general later noncompact duality theorem cannot be treated as an exact match.""",
 "F",r"""The later literature cited in \citet[references 28--29]{doplicherroberts1989duality} supplies possible noncompact leads, not an identification of this report.""",
 r"""unresolved identification rather than a demonstrated open problem.""",["doplicherroberts1989duality"],literal="not determinable",match="thematic only",verification="unresolved lead",confidence="low")
save()

talk(110,"1966-10-17","Louis Nirenberg","P000166-P000168","Varadhan's short-time heat-kernel asymptotic","talk",
 r"""The lower portion of P000167 records Nirenberg reporting Varadhan's result: the leading exponential of the heat kernel measures squared geodesic distance. The handwritten general formula omits the factor four that is present in its own Euclidean example. A final allusion to elliptic eigenvalues contains no identifiable theorem. The close publication is \citet{varadhan1967fundamental}, published in May 1967.""")
item(110,"P000167","theorem","Short-time heat kernel and intrinsic distance",
 r"""For \(\partial_tu=\sum a^{ij}(x)u_{x_ix_j}\) with point-source initial data, the notes give \(u=\exp[-g(x,y)/t+o(t^{-1})]\) and identify \(g=d^2\) for the metric generated by \(a^{ij}\).""",
 r"""For a smooth symmetric uniformly positive definite coefficient matrix \(a(x)\), with standard boundedness assumptions ensuring the positive fundamental solution on \(\mathbb R^n\), put \(g_x(v,v)=v^\top a(x)^{-1}v\). Then \(\lim_{t\downarrow0}-4t\log p(t,x,y)=d_g(x,y)^2\). Equivalently \(p(t,x,y)=\exp[-d_g(x,y)^2/(4t)+o(t^{-1})]\) for fixed \(x,y\).""",
 r"""The inverse matrix defines the metric. Uniform ellipticity and a standard global coefficient setting are supplied as sufficient hypotheses. The normalization is for the displayed generator with no factor \(1/2\).""",
 "B",r"""\citet[pp.~431--455]{varadhan1967fundamental} is the exact subsequent paper by Varadhan, reported here by Nirenberg. Publisher metadata was checked; the normalization is independently fixed by the notebook's Gaussian.""",
 r"""established. The literal identification of \(g\) in the exponent is off by a factor four.""",["varadhan1967fundamental"],literal="false as written",verification="publisher metadata checked")
item(110,"P000167","theorem","Gaussian normalization and subleading powers of time",
 r"""The Euclidean example is \(Ct^{-n/2}\exp[-|x-y|^2/(4t)]\); the polynomial factor is said to enter the \(o(t^{-1})\) term.""",
 r"""For \(\partial_tu=\Delta u\), \(p(t,x,y)=(4\pi t)^{-n/2}\exp[-|x-y|^2/(4t)]\). Since \(t\log t\to0\), \(\log(t^{-n/2})=o(t^{-1})\), so this prefactor does not affect \(-4t\log p\).""",
 r"""The constant is supplied from mass-one normalization. Direct differentiation and Gaussian integration independently check the formula and its factor four.""",
 "E",r"""This classical example is the normalization check for the general result \citep{varadhan1967fundamental}.""",
 r"""standard and correct.""",["varadhan1967fundamental"],literal="correct",verification="publisher metadata checked")
item(110,"P000167","remark","Unspecified elliptic-eigenvalue analogy",
 r"""The last sentence says that elliptic eigenvalues of the Laplacian in a domain can be treated “in the same spirit”.""",
 r"""The sentence supplies no domain assumptions, asymptotic parameter, eigenvalue regime or proposed formula. It cannot uniquely identify Weyl asymptotics, a small-noise principal-eigenvalue estimate or another spectral result.""",
 r"""No precise theorem has been inserted from the speaker's presumed intentions.""",
 "F",r"""The heat-kernel paper \citep{varadhan1967fundamental} is relevant context only; it does not identify this unspecific extra sentence.""",
 r"""unidentified allusion, not a definite open problem.""",["varadhan1967fundamental"],literal="not determinable",match="thematic only",verification="unresolved lead",confidence="low")
save()

talk(111,"1966-10-24","M. I. Vishik","P000166-P000168","Pseudodifferential operators: two lecture headings","heading",
 r"""At the top of P000168, Vishik's first lecture has only “I. Kohn--Nirenberg definition” and “II. Boundedness theorem”. No hypotheses, formulas or proof survive. A separate unindexed heading attributes a Sturm--Liouville topic to a professor whose surname is uncertain (possibly Lorch); it has no mathematical statement either. The entries below distinguish contextual reconstructions from actual recorded assertions.""")
item(111,"P000168","definition","Kohn--Nirenberg definition: heading only",
 r"""The first outline entry names a Kohn--Nirenberg definition, without a formula or symbol class.""",
 r"""A contextual modern model is \(a(x,D)u(x)=(2\pi)^{-n}\int e^{ix\cdot\xi}a(x,\xi)\widehat u(\xi)\,d\xi\), initially for Schwartz \(u\), with \(a\) satisfying specified symbol estimates. The heading alone does not identify which symbol estimates were taught.""",
 r"""The formula is explanatory reconstruction, not a transcription of a missing lecture. In particular no \(S^m_{\rho,\delta}\) class is attributed to the speaker.""",
 "F",r"""\citet{ kohnnirenberg1965algebra} is the natural earlier source, but only its publisher metadata and the contextual match were verified.""",
 r"""the named framework is identifiable, while the precise definition used in this lecture is not.""",["kohnnirenberg1965algebra"],literal="not determinable",match="thematic only",verification="publisher metadata checked",confidence="medium")
item(111,"P000168","theorem","Boundedness theorem: heading only",
 r"""The second outline entry is merely “Theorem on boundedness”.""",
 r"""One standard theorem is \(a(x,D):H^s\to H^{s-m}\) for a properly supported symbol \(a\in S^m_{1,0}\), with the usual uniform derivative estimates and localization on a manifold. The heading does not specify whether this, an order-zero \(L^2\) theorem, or a different boundedness criterion was intended.""",
 r"""This example supplies context only and is not counted as a verified formulation of Vishik's theorem. Earlier occurrences 1965-81.8--9 discuss Sobolev order and angular regularity, but do not fill this gap.""",
 "F",r"""The relevant pre-lecture sources include \citet{kohnnirenberg1965algebra,hormander1965pseudo}; their existence does not determine the missing hypotheses.""",
 r"""no unique theorem can be assigned to the heading.""",["kohnnirenberg1965algebra","hormander1965pseudo"],literal="not determinable",match="thematic only",verification="publisher metadata checked",confidence="medium")
save()

talk(112,"1966-10-31","M. I. Vishik","P000166-P000170","Composition and formal symbols","talk",
 r"""Vishik's second lecture begins on P000168 and ends in the upper half of P000169. Unlike the preceding outline, it supplies the composition expansion, its Fourier/Taylor proof, formal asymptotic symbols, uniqueness modulo smoothing and realization of a formal symbol. These are expository parts of the calculus already published in 1965 by Kohn--Nirenberg and H\"ormander \citep{kohnnirenberg1965algebra,hormander1965pseudo}. Oleinik begins below and belongs to record 113.""")
item(112,"P000168","theorem","Composition expansion with a controlled remainder",
 r"""\(AB=C_0+\cdots+C_{s-1}+T_s\), with \(\sigma(C_k)=\sum_{|\alpha|=k}(\alpha!)^{-1}\partial_\xi^\alpha a\,D_x^\alpha b\); \(T_s\) has order \(\sigma+\lambda-s\).""",
 r"""For properly supported classical or \(S^{m}_{1,0}\) operators \(A,B\) of orders \(m_1,m_2\), the Kohn--Nirenberg product symbol satisfies \(a\# b-\sum_{|\alpha|<N}(\alpha!)^{-1}\partial_\xi^\alpha a\,D_x^\alpha b\in S^{m_1+m_2-N}_{1,0}\), with \(D_x=(1/i)\partial_x\). In particular the principal symbol is \(a_{m_1}b_{m_2}\).""",
 r"""The symbol class, support/localization conditions and Fourier convention are supplied. Symbol estimates are essential; a formal Taylor polynomial alone does not bound the remainder.""",
 "E",r"""This is the already published calculus of \citet{kohnnirenberg1965algebra,hormander1965pseudo}. The notebook's formula was checked directly against P000168; external verification here is bibliographic rather than a full rereading of those papers.""",
 r"""standard pseudodifferential composition.""",["kohnnirenberg1965algebra","hormander1965pseudo"],verification="publisher metadata checked")
item(112,"P000168-P000169","method","Fourier-space proof of the composition formula",
 r"""The localized Fourier kernels \(\widetilde h(\xi-\eta,\eta)\), \(\widetilde g(\eta-\tau,\tau)\) are composed; Taylor expansion of the second variable of \(\widetilde h\) at \(\eta=\tau\) gives derivatives and convolution products.""",
 r"""With compact spatial localization and the preceding symbol estimates, write the composition as an oscillatory double integral. Taylor-expand \(a(x,\xi+\eta)\) in \(\eta\); transfer each \(\eta^\alpha\) to \(D_x^\alpha b\) by Fourier inversion. The integral Taylor remainder and integration by parts yield the order \(m_1+m_2-N\) estimate.""",
 r"""The notebook gives the algebraic part of this proof but omits remainder estimates and convergence regularization. They are hypotheses and standard analytic steps required for the theorem, not additional recorded calculations.""",
 "E",r"""The method is part of the original symbol calculus \citep{kohnnirenberg1965algebra,hormander1965pseudo}.""",
 r"""established; the recorded proof is a sketch of the composition theorem.""",["kohnnirenberg1965algebra","hormander1965pseudo"],verification="publisher metadata checked",match="partial")
item(112,"P000169","definition","Formal asymptotic symbol",
 r"""For homogeneous \(A_k\) of orders \(\tau_k\searrow-\infty\), \(A\sim\sum A_k\) means the remainder after \(N\) terms has order below \(\tau_N\); the formal sum of \(a_k\) is called the symbol.""",
 r"""In the classical calculus a full formal symbol is a sequence \(a_{m-j}(x,\xi)\), homogeneous of degree \(m-j\) for \(|\xi|\ge1\), such that \(a-\sum_{j<N}\chi(\xi)a_{m-j}\in S^{m-N}_{1,0}\) for every \(N\), with a cutoff near zero. More generally one may specify a decreasing order sequence tending to \(-\infty\) with corresponding remainder bounds.""",
 r"""This distinguishes a formal homogeneous expansion from an exact total symbol. The notebook's weaker “order below \(\tau_N\)” does not itself specify the sharper conventional next-order bound.""",
 "E",r"""Asymptotic symbols were part of the 1965 calculus \citep{kohnnirenberg1965algebra,hormander1965pseudo}.""",
 r"""standard after a remainder convention is fixed.""",["kohnnirenberg1965algebra","hormander1965pseudo"],verification="publisher metadata checked")
item(112,"P000169","theorem","Zero formal symbol and smoothing operators",
 r"""“Symbol zero” means \(A\) has order \(-\infty\).""",
 r"""For a properly supported classical operator, vanishing of every homogeneous formal-symbol component is equivalent to membership in \(\Psi^{-\infty}\). Such an operator has a smooth kernel and maps compactly supported distributions to smooth functions; on a closed manifold it improves every Sobolev order.""",
 r"""A zero principal symbol merely lowers order; it is the entire formal expansion that must vanish.""",
 "E",r"""This is the smoothing ideal of the established calculus \citep{kohnnirenberg1965algebra,hormander1965pseudo}.""",
 r"""standard and correct with the meaning of “symbol” fixed.""",["kohnnirenberg1965algebra","hormander1965pseudo"],verification="publisher metadata checked",literal="correct")
item(112,"P000169","theorem","Uniqueness of the formal homogeneous expansion",
 r"""The theorem says an operator's symbol is uniquely determined.""",
 r"""For a fixed coordinate system and quantization, the homogeneous components of a classical symbol are uniquely determined by the operator modulo smoothing. Two distinct homogeneous leading terms cannot differ by a lower-order symbol. An exact total symbol depends on localization and quantization, and transforms nontrivially under coordinate changes.""",
 r"""The uniqueness is of the formal expansion in a fixed calculus, not of a coordinate-invariant scalar full symbol.""",
 "E",r"""This is the uniqueness convention in the calculus of \citet{kohnnirenberg1965algebra,hormander1965pseudo}.""",
 r"""standard after conventions are fixed.""",["kohnnirenberg1965algebra","hormander1965pseudo"],verification="publisher metadata checked")
item(112,"P000169","theorem","Realization of a formal symbol",
 r"""The notes assert that for every symbol there exists an operator.""",
 r"""Given smooth homogeneous components \(a_{m-j}\) satisfying the symbol bounds on each compact coordinate set, an asymptotic summation using cutoffs at successively larger frequencies constructs \(a\in S^m_{1,0}\) with that formal expansion. Quantization and localization give an operator, unique modulo smoothing for the prescribed expansion.""",
 r"""“Every symbol” means an admissible formal classical symbol, not an arbitrary collection without smoothness or local estimates. The cutoff construction is a Borel-type asymptotic summation.""",
 "E",r"""This realization theorem is already part of the 1965 calculus \citep{kohnnirenberg1965algebra,hormander1965pseudo}.""",
 r"""established.""",["kohnnirenberg1965algebra","hormander1965pseudo"],verification="publisher metadata checked")
item(112,"P000169","theorem","Filtered algebra of pseudodifferential operators",
 r"""Pseudodifferential operators form an algebra and their formal product is \(\sum_\alpha(\alpha!)^{-1}\partial_\xi^\alpha\sigma(A)D_x^\alpha\sigma(B)\).""",
 r"""Properly supported classical operators form a filtered algebra: \(\Psi^{m_1}\Psi^{m_2}\subset\Psi^{m_1+m_2}\), with the written asymptotic symbol product. The smoothing operators form a two-sided ideal, so this product descends to complete formal symbols modulo smoothing.""",
 r"""The conclusion is the algebraic organization of the preceding composition and realization theorems; it requires the same support and symbol-class hypotheses.""",
 "E",r"""This is the central already published result named in the title of \citet{kohnnirenberg1965algebra}.""",
 r"""standard calculus; no undeveloped research proposal is present.""",["kohnnirenberg1965algebra"],verification="publisher metadata checked")
save()

talk(113,"1966-10-31","O. A. Oleinik","P000168-P000172","The unsteady Prandtl boundary layer","talk",
 r"""Oleinik begins in lower P000169 and finishes P000170. She contrasts viscous and ideal-fluid boundary conditions, writes the Prandtl system and data, and announces uniqueness, short-time existence, existence near the inflow for all time, and stability. The monotonicity and compatibility assumptions needed for her theorems are absent from the notebook. The announcement had already appeared in 1966 \citep{oleinik1966system}; the detailed later treatment is \citet[Lecture II, Theorems 4--5]{oleinik1968boundary}.""")
item(113,"P000169","remark","Why vanishing viscosity is singular at a wall",
 r"""The incompressible planar Navier--Stokes equations are written. Setting viscosity to zero gives Euler, but the viscous terms cannot simply be discarded because no-slip and ideal-fluid boundary conditions differ.""",
 r"""At a stationary impermeable wall, viscous no-slip imposes both velocity components zero, whereas impermeable Euler flow imposes only the normal component zero. If the limiting outer tangential velocity is nonzero, convergence to that Euler field cannot be uniform up to the wall. A thin transition region is therefore required in the classical matched-asymptotic picture.""",
 r"""This observation does not prove a Navier--Stokes-to-Prandtl limit, a boundary-layer thickness theorem, or formation of a layer for all initial data.""",
 "E",r"""This is the classical Prandtl motivation reviewed by \citet[\S1]{oleinik1968boundary}.""",
 r"""the boundary-condition mismatch is established; a rigorous inviscid limit requires additional hypotheses.""",["oleinik1968boundary"],literal="correct")
item(113,"P000170","construction","The Prandtl system and outer pressure",
 r"""The tangential equation retains \(\nu u_{yy}\), continuity remains, and the pressure is a prescribed function \(p(t,x)\) constant in the normal direction. Although \(p_y=0\) is crossed out in the display, the prose explicitly retains its meaning.""",
 r"""In boundary-layer coordinates at a flat wall, the Prandtl model is \(u_t+uu_x+vu_y=\nu u_{yy}-\rho^{-1}p_x(t,x)\), \(u_x+v_y=0\). Matching to the outer tangential Euler velocity \(U(t,x)\) imposes \(U_t+UU_x=-\rho^{-1}p_x\). The formal scaling \(y=\sqrt{\nu}\,Y\), with the normal velocity scaled accordingly, explains the retained normal diffusion.""",
 r"""The outer Bernoulli equation and the distinction between physical and rescaled variables are supplied. The formal derivation is not a proved approximation theorem.""",
 "E",r"""The displayed model is the one studied in \citet[p.~751, equations (1)--(3)]{oleinik1966system} and \citet[\S1]{oleinik1968boundary}.""",
 r"""standard boundary-layer equations.""",["oleinik1966system","oleinik1968boundary"])
item(113,"P000170","problem","Correctly posed initial and inflow data",
 r"""The wall conditions are \(u=0\), \(v=v_0(x,t)\); the notebook writes inconsistent arguments in \(u|_{x=0}=u_0(x)\) and \(u|_{t=0}=u_0(x,t)\), and requires \(u\to U(t,x)\) as \(y\to\infty\).""",
 r"""On \(0<x<X\), \(y>0\), \(t>0\), prescribe \(u(t,x,0)=0\), \(v(t,x,0)=v_0(t,x)\), initial profile \(u(0,x,y)=u_0(x,y)\), inflow profile \(u(t,0,y)=u_1(t,y)\), and \(\lim_{y\to\infty}u(t,x,y)=U(t,x)\). These data must agree at their intersections, satisfy the wall compatibility equations, and match \(U\) at infinity.""",
 r"""Distinct \(u_0,u_1\) and their variables are reconstructed from the PDE and checked in Oleinik's paper. The notebook's variable mistakes are faithful errors, not proof of a different problem.""",
 "E",r"""The correctly indexed data are explicit in \citet[p.~751]{oleinik1966system}; the note was received 1 March 1966 and published before this October report.""",
 r"""the standard initial/inflow Prandtl problem under a specified solution class.""",["oleinik1966system"],literal="false as written")
item(113,"P000170","theorem","Local existence and uniqueness in the monotone class",
 r"""The solution is said to be unique if it exists, and to exist on \(0\le t\le T\) over the whole body; separation may occur later but not instantaneously.""",
 r"""A sufficient classical setting is \(U>c>0\), smooth compatible data with \(u_0,u_1>0\) for \(y>0\), \(\partial_yu_0,\partial_yu_1>0\), convergence to \(U\) at infinity, and two-sided tail bounds \(c_1(U-u_j)\le\partial_yu_j\le c_2(U-u_j)\), together with the bounded weighted derivatives and corner compatibility in Oleinik's Theorem 4. There is then a unique classical monotone solution for sufficiently short time on a finite streamwise interval.""",
 r"""The notebook omits this crucial monotone solution class. The complete derivative and compatibility package is specified by the cited theorem rather than an assertion about all smooth data. The Crocco transformation uses monotonicity to replace the normal coordinate by the velocity.""",
 "E",r"""\citet[pp.~751--754]{oleinik1966system} already announced this theory; \citet[Theorem 4, pp.~28--29]{oleinik1968boundary} supplies its detailed sufficient assumptions.""",
 r"""established in the monotone class; no arbitrary-data well-posedness statement is valid.""",["oleinik1966system","oleinik1968boundary"],match="partial")
item(113,"P000170","theorem","All-time existence on a short inflow interval",
 r"""Near the beginning of the flow around the body, the solution exists for all time. The inequality \(p_x\le0\) appears separately beneath this statement.""",
 r"""Under the uniform-in-time data bounds and compatibility assumptions of Oleinik's Theorem 5, one can choose a sufficiently small streamwise length \(X_1>0\) so that a monotone classical solution exists for all \(t\ge0\), \(0\le x\le X_1\). This differs from global existence on the entire body. A favourable pressure gradient is an additional recorded regime, not a license to omit all other assumptions.""",
 r"""The relation of the isolated inequality to the previous sentence is not grammatically explicit. The detailed cited short-inflow theorem is the verified comparison; no universal all-time theorem for every vessel is claimed.""",
 "E",r"""The result announced in the 1966 theory is proved in \citet[Theorem 5, pp.~29--32]{oleinik1968boundary}.""",
 r"""established with the stated short-inflow and uniform-data restrictions.""",["oleinik1966system","oleinik1968boundary"],match="partial")
item(113,"P000170","claim","The scope of stability of a boundary layer",
 r"""The final sentence says a solution is always stable if it exists and is a “nast.” boundary layer; the abbreviation is not safely expanded.""",
 r"""Oleinik-type monotone solutions have stability/continuous-dependence statements in the corresponding controlled class and norms. Existence of a smooth Prandtl solution alone does not imply Sobolev stability: linearization around suitable nonmonotone shear profiles with a nondegenerate critical point has high-frequency instability.""",
 r"""The note gives neither a norm nor the meaning of the qualifying abbreviation. Thus the exact historical stability theorem is not reconstructed. The later counter-scope is included to prevent reading “always” as an unrestricted theorem.""",
 "F",r"""The monotone framework is in \citet{oleinik1968boundary}; the nonmonotone obstruction is the result of \citet[abstract and main instability theorem]{gerardvaretdormy2010illposed}, first circulated in 2009 and published in 2010.""",
 r"""the literal sentence is underdetermined; general Sobolev stability is false, while qualified monotone theory is established.""",["oleinik1968boundary","gerardvaretdormy2010illposed"],literal="not determinable",match="partial",verification="publisher metadata checked",confidence="medium")
save()

talk(114,"1966-11-14","M. S. Agranovich","P000170-P000174","Pseudodifferential heading and nine geometry problems","other",
 r"""P000171 begins “Agranovich, Lecture 3 on pseudodifferential operators”, but no mathematical exposition of that lecture follows. Instead P000171--P000172 contain a numbered differential-geometry problem list, without an explicit speaker attribution for the list. It includes Helgason's spherical support question, entire Monge--Ampere and minimal-graph problems, metric reconstruction, symmetric-space eigenfunctions, infinite volume, two geodesic questions and contact structures. These are associated with this record by manuscript position, not individually attributed to Agranovich. P000173 begins Arnold's following record and is excluded.""")
item(114,"P000171","remark","Third pseudodifferential lecture: heading only",
 r"""The heading names Agranovich's third lecture on pseudodifferential operators; the next written heading is “Problems of differential geometry”.""",
 r"""There is no surviving mathematical statement of the pseudodifferential lecture on these pages.""",
 r"""Neither the title nor the catalogue overlap licenses importing the content of Agranovich's publications or the subsequent Arnold pages.""",
 "F",r"""No particular theorem or new result can be matched to the heading.""",
 r"""a documented lecture heading without reconstructible mathematical content.""",
 [],literal="not determinable",match="none found",verification="unresolved lead",development="none",confidence="high")
def geo(pages,kind,title,notes,statement,reconstruction,cls,fate,status,refs=(),**kwargs):
    return item(114,pages,kind,title,notes,statement,reconstruction,cls,fate,status,refs,
                speaker="Unattributed differential-geometry discussion",**kwargs)

hid=geo("P000171","problem","Helgason's support problem for geodesic spheres",
 r"""On a complete negatively curved manifold, \(f\in C^\infty_0\); if every sphere enclosing a given ball \(B\) has zero surface integral of \(f\), prove \(f=0\) outside \(B\). The name Helgason is written twice.""",
 r"""Let \(M\) be a complete simply connected smooth Riemannian manifold with negative sectional curvature, \(B\) a closed geodesic ball, and \(f\in C_c^\infty(M)\). If \(\int_{S(y,r)}f\,d\sigma=0\) for every geodesic sphere whose closed ball \(D(y,r)\) contains \(B\), must \(\operatorname{supp}f\subset B\)?""",
 r"""Simple connectivity is supplied from the exact published formulation, making geodesic spheres globally regular by the Hadamard setting. “Sphere containing \(B\)” means its enclosed ball contains \(B\), not that the hypersurface contains the ball as a subset. The transform is spherical integration, not the geodesic ray transform.""",
 "C",r"""This is exactly \citet[Problem 4.1]{quinto2008helgason}. That work proves the real-analytic metric case through its support theorems, including Theorem 5.1; it does not remove analyticity for an arbitrary smooth negatively curved metric.""",
 r"""the real-analytic case is verified; no resolution of the full smooth-metric statement was located in the targeted searches. The classification concerns this precise remaining regularity gap, not generic integral geometry.""",
 ["quinto2008helgason"],problem="GP-1966-21",
 worth=r"""Worth revisiting through smooth local support estimates, but the available evidence does not justify a bounded new theorem in this run.""",
 confidence="medium")
problem("GP-1966-21","Helgason spherical support problem on a smooth Hadamard manifold",
 r"""For complete simply connected negatively curved smooth \(M\), do zero integrals of \(f\in C_c^\infty(M)\) over all geodesic spheres enclosing a closed ball \(B\) imply \(\operatorname{supp}f\subset B\)?""",[hid],
 r"""verified for real-analytic metrics; a general smooth-metric resolution was not found. The precise source is Quinto's Problem 4.1, not a ray-transform support theorem.""",["quinto2008helgason"])
geo("P000171","theorem","Constant-curvature support theorem",
 r"""The notes say Helgason has done the preceding problem for constant curvature.""",
 r"""For real hyperbolic space, a compactly supported smooth function whose surface integrals vanish on all geodesic spheres enclosing a fixed geodesic ball is supported in that ball.""",
 r"""This is the already known special case of the preceding question. The broader real-analytic generalization is later and is kept distinct from what the note says was already proved.""",
 "E",r"""\citet[\S4, discussion after Problem 4.1]{quinto2008helgason} identifies Helgason's earlier constant-curvature proof and its reduction in the disk model.""",
 r"""established; it does not settle arbitrary variable smooth curvature.""",["quinto2008helgason"],literal="correct")
mid=geo("P000171","problem","Entire convex solutions of the constant Monge--Ampere equation",
 r"""Calabi's problem asks whether a convex function on \(\mathbb R^n\) satisfying \(\det D^2u=1\) must be a polynomial of degree two; the notes mention \(n=2\) and Calabi's \(n\le5\) result.""",
 r"""Every convex entire \(C^2\) solution of \(\det D^2u=1\) on \(\mathbb R^n\) is \(u(x)=\tfrac12x^\top Ax+b\cdot x+c\), where \(A\) is positive definite and \(\det A=1\). The modern theorem extends to convex viscosity solutions.""",
 r"""“Entire” and convexity are essential. The conclusion permits affine terms and arbitrary positive definite Hessian of determinant one; it does not say the Hessian is the identity.""",
 "B",r"""The all-dimensional result is the J\"orgens--Calabi--Pogorelov theorem. \citet[Introduction and Theorem 1.1, pp.~549--550]{caffarellili2003extension} gives the exact modern statement and records the sequence from J\"orgens's \(n=2\) result through Calabi to Pogorelov's all-dimensional resolution.""",
 r"""settled affirmatively in every dimension.""",["caffarellili2003extension"],problem="GP-1966-22",literal="correct")
problem("GP-1966-22","Entire convex Monge--Ampere rigidity",
 r"""Must every convex entire solution of \(\det D^2u=1\) be quadratic?""",[mid],
 r"""yes in all dimensions, by the J\"orgens--Calabi--Pogorelov theorem; convex viscosity solutions are included.""",["caffarellili2003extension"])
bid=geo("P000171","problem","The dimension-dependent Bernstein problem",
 r"""For a smooth entire solution of a displayed equation described as the minimal-surface equation, is \(u\) linear? The final parenthesis says “Done” with a reference to De Giorgi. The uncancelled formula visibly has an extra square on the second-derivative sum.""",
 r"""For \(u\in C^\infty(\mathbb R^n)\) satisfying \(\operatorname{div}(\nabla u/\sqrt{1+|\nabla u|^2})=0\), equivalently \((1+|\nabla u|^2)\Delta u-\sum_{i,j}u_i u_j u_{ij}=0\), must \(u\) be affine? The answer is yes for \(n\le7\) and no for every \(n\ge8\).""",
 r"""The notebook's raised square must be deleted to obtain the PDE identified by its prose. The graph lies in ambient \(\mathbb R^{n+1}\), so ambient and domain dimensions must not be confused. “Linear” is interpreted as affine.""",
 "B",r"""\citet[Introduction, Theorem B and \S~IV]{bombieridegiorgigiusti1969minimal} construct the high-dimensional counterexamples and explain the preceding positive results. The original appeared in 1969; the verified Russian translation is 1971, pp.~84--103.""",
 r"""settled with the sharp dimension split. The unqualified “Done” does not establish the all-dimensional affirmative assertion.""",["bombieridegiorgigiusti1969minimal"],literal="false as written",problem="GP-1966-23")
problem("GP-1966-23","Entire minimal-graph Bernstein problem",
 r"""For which \(n\) is every smooth entire minimal graph over \(\mathbb R^n\) an affine hyperplane?""",[bid],
 r"""exactly \(n\le7\); nonaffine entire minimal graphs exist for \(n\ge8\).""",["bombieridegiorgigiusti1969minimal"])
sid=geo("P000171-P000172","problem","Recovering the metric from a Sobolev pullback isometry",
 r"""The notes give the \(H^1\) inner product \(\int\varphi\psi+\int\langle d\varphi,d\psi\rangle\) and the Dirichlet energy. An \(H^1\) isometry inducing a diffeomorphism between \(M\) and \(M'\) should imply a Riemannian isometry.""",
 r"""Let \(F:M\to M'\) be a smooth diffeomorphism of closed smooth Riemannian manifolds. If the pullback \(u\mapsto u\circ F\) preserves the full \(H^1\) inner product for every smooth \(u,v\), then \(F^*g'=g\). An arbitrary abstract Hilbert-space isometry does not suffice.""",
 r"""“Inducing a diffeomorphism” is interpreted as composition pullback. Elementary verification \ours: testing the inner product against \(1\) shows \(F\) preserves volume. Subtracting the resulting \(L^2\) identity leaves equality of Dirichlet forms. In local coordinates their difference is \(\int q^{ij}\partial_i u\,\partial_jv=0\) for all compactly supported \(u,v\). Integration by parts gives \(\partial_j(q^{ij}\partial_i u)=0\); choose \(du=0\) and an arbitrary Hessian at a point to obtain \(q^{ij}=0\), hence equality of inverse metrics. A second check via equality of the principal symbols of the associated Laplacians gives the same conclusion.""",
 "B",r"""This precise pullback version follows by the displayed elementary argument. The later stronger reconstruction from an order isomorphism intertwining heat semigroups is \citet[Theorem 1.1]{arendt2017diffusion}, first circulated in 2011 and published in 2017; it is a partial, not exact historical match.""",
 r"""settled under the composition interpretation. No solution of an unspecified abstract Hilbert-space reconstruction problem is claimed.""",["arendt2017diffusion"],match="partial",problem="GP-1966-24",confidence="medium")
problem("GP-1966-24","Metric rigidity of a Sobolev composition isometry",
 r"""If a smooth diffeomorphism of closed Riemannian manifolds induces an isometry of their full \(H^1\) inner products by pullback, must it preserve their metrics?""",[sid],
 r"""yes, by volume and Dirichlet-form recovery; the composition condition is essential.""",["arendt2017diffusion"])
geo("P000172","remark","Laplace eigenvalues are invariants, not complete metric data",
 r"""The line following the Sobolev question says “Invariants: eigenvalues of the Laplace operator”.""",
 r"""A Riemannian isometry intertwines the Laplace--Beltrami operators and preserves their spectra with multiplicities. Conversely, equality of spectra alone does not imply isometry: an abstract unitary spectral identification need not preserve multiplication, order or the composition action of a map.""",
 r"""The source calls these invariants, not complete invariants. The converse warning prevents the preceding question from being read as an affirmative inverse-spectral theorem.""",
 "E",r"""\citet[Introduction]{arendt2017diffusion} recalls Milnor's 1964 isospectral nonisometric examples and explains the additional order structure used in reconstruction.""",
 r"""spectral invariance is established; isospectral nonisometric manifolds are known.""",["arendt2017diffusion"],literal="correct",match="partial")
geo("P000172","construction","Evaluation map from the first Laplace eigenspace",
 r"""For compact irreducible symmetric \(M\), \(V\) is the eigenspace of the smallest nonzero Laplace eigenvalue and \(\varphi:M\to V^*\) is written.""",
 r"""For a connected closed Riemannian manifold, the first positive Laplace eigenspace \(V\) is finite dimensional and smooth. Evaluation defines \(\varphi(x)(f)=f(x)\) in \(V^*\), after choosing the \(L^2\) inner product if one wants \(V^*\cong V\). The map is equivariant under isometries. If \(M\) is an irreducible compact symmetric space, its induced symmetric quadratic tensor is an invariant multiple of the metric.""",
 r"""Evaluation is the natural construction inferred from the displayed domain and codomain; it is not written in words. No assertion that the map is injective is recorded, and none is attributed to the source.""",
 "E",r"""This is the standard spectral construction; the link between functions, the Laplacian and the metric is reviewed in \citet[\S1]{arendt2017diffusion}. That reference is contextual rather than an exact source for this one-line symmetric-space item.""",
 r"""the construction is elementary; the problem or conclusion intended after it is missing.""",["arendt2017diffusion"],literal="correct with missing hypotheses",match="thematic only",confidence="medium")
geo("P000172","question","The unrecorded noncompact eigenfunction question",
 r"""After the evaluation map comes the doubtful line “If not compact”.""",
 r"""No specific noncompact manifold, spectral realization, eigenvalue, function space or desired conclusion is supplied. In general a complete noncompact manifold need not have a first positive \(L^2\) eigenvalue or a finite-dimensional space analogous to the compact \(V\).""",
 r"""The sentence is retained as an unresolved fragment; continuous-spectrum harmonic analysis is only one possible intended continuation.""",
 "F",r"""No exact question could be matched; the compact spectral reconstruction reference is not a solution of this fragment.""",
 r"""not identifiable as a definite mathematical problem.""",[],literal="not determinable",match="none found",verification="unresolved lead",confidence="low")
rid=geo("P000172","question","Infinite volume under positive Ricci curvature",
 r"""For complete noncompact \(M^3\) with positive Ricci tensor, does \(V\) tend to infinity? A two-dimensional result of Cohn--Vossen is mentioned.""",
 r"""Every complete connected noncompact Riemannian manifold with \(\operatorname{Ric}\ge0\) has infinite Riemannian volume. In particular \(\operatorname{Vol}(B(p,R))\to\infty\) as \(R\to\infty\) in the three-dimensional positive-Ricci case.""",
 r"""The letter \(V\) is read as volume, supported by the curvature context and the Cohn--Vossen reference. Completeness and noncompactness are retained; positive scalar curvature alone would be a different assertion.""",
 "B",r"""The stronger all-dimensional nonnegative-Ricci assertion is stated explicitly in \citet[p.~659, opening summary]{yau1976function}. That first page was opened and visually inspected; no unverified theorem number is assigned.""",
 r"""settled affirmatively, with weaker curvature than the question requests.""",["yau1976function"],problem="GP-1966-25",confidence="high")
problem("GP-1966-25","Infinite volume of a complete noncompact positive-Ricci three-manifold",
 r"""Does a complete connected noncompact Riemannian three-manifold with positive Ricci curvature have infinite volume?""",[rid],
 r"""yes; Yau's theorem covers nonnegative Ricci curvature in every dimension.""",["yau1976function"])
geo("P000172","question","An ambiguous infinite-geodesic question",
 r"""For compact \(M^n\), the notes ask for infinitely many \ru{пересек.} geodesics, followed by “actually distinct”; a preceding short word is crossed out.""",
 r"""No unique global proposition can be extracted: closedness is not legibly stated, and “intersecting” does not specify mutual intersections, intersections through a fixed point, endpoints or periodicity. If only distinct local geodesic germs through one point are meant and \(n\ge2\), infinitely many exist immediately by their tangent directions.""",
 r"""The scan was inspected. It does not justify replacing the written abbreviation by “closed” and thereby importing the famous infinitely-many-closed-geodesics conjecture. No problem-index entry is manufactured from that possible interpretation.""",
 "F",r"""Searches for closed-geodesic problems provide only thematic alternatives; none resolves the actual uncertain wording.""",
 r"""unidentified question because a defining qualifier is missing or doubtful.""",[],literal="not determinable",match="none found",verification="unresolved lead",confidence="low")
zid=geo("P000172","conjecture","Smooth type of a manifold with equally long closed geodesics",
 r"""The next numbered problem asks whether compact simply connected \(M\), all of whose geodesics are closed and have the same length, is diffeomorphic to a symmetric space “of the first type”. A rank-like expression is crossed out.""",
 r"""The standard intended topology question is: if every unit-speed prime geodesic of a closed simply connected Riemannian manifold has the same period, must the manifold be diffeomorphic to a compact rank-one symmetric space, namely a sphere, complex or quaternionic projective space, or the Cayley plane?""",
 r"""Rank one is a contextual identification, not a perfectly legible manuscript word. “Same length” means prime periods, since arbitrary iterates have different lengths. This topology problem is distinct from the Blaschke metric-rigidity conjecture and from the Berger conjecture about equality of periods.""",
 "C",r"""The cohomological restrictions below are established. \citet[definition on p.~1 and Main Theorem on p.~3]{lisong2026zoll} use the stronger Zoll hypothesis that every unit-speed prime geodesic is simple closed and all have the same period. Under that hypothesis and the additional entire-Grauert-tube assumption, they prove metric rigidity of the complex-projective cohomology type, up to scale. Simplicity is not explicit in the notebook, nor is an entire Grauert tube assumed; the result supplies no general diffeomorphism classification under its recorded hypotheses.""",
 r"""no full smooth classification was verified; the remaining issue is the diffeomorphism type beyond the known cohomology restrictions. The recent additional-hypothesis theorem is not counted as a solution of that issue.""",
 ["lisong2026zoll"],problem="GP-1966-26",match="partial",
 worth=r"""Worth pursuing through precise topological obstructions or restricted geometric classes, but no new bounded contribution is established here.""",
 confidence="medium")
problem("GP-1966-26","Diffeomorphism type of equal-period closed-geodesic manifolds",
 r"""Must a closed simply connected Riemannian manifold whose prime unit-speed geodesics all have the same period be diffeomorphic to a compact rank-one symmetric space?""",[zid],
 r"""cohomology is constrained to the rank-one symmetric models; the unrestricted smooth classification was not found resolved. The result of \citet[definition on p.~1 and Main Theorem on p.~3]{lisong2026zoll} assumes simple closed prime geodesics of a common period, as well as an entire Grauert tube, and proves metric rigidity only for the complex-projective cohomology type. Those additional hypotheses do not remove the gap for the notebook's question.""",["lisong2026zoll"])
geo("P000172","claim","Nonround metrics with all geodesics closed",
 r"""There is an analytic manifold diffeomorphic to a sphere but not isometric to it, in the preceding closed-geodesic context.""",
 r"""There exist nonround real-analytic metrics on \(S^2\) for which every prime geodesic is simple closed and has the same length. Consequently the conclusion sought in the preceding problem cannot be equality with the round metric merely from the closed-geodesic hypothesis.""",
 r"""“Not isometric” is interpreted relative to a standard round sphere after scale normalization. The source does not supply the metric, and no formula for a new example is invented.""",
 "E",r"""The historical nonround Zoll examples, beginning in 1903, are recalled by \citet[Introduction, p.~2]{lisong2026zoll}; they predate the seminar.""",
 r"""established and compatible with the proposed diffeomorphism conclusion.""",["lisong2026zoll"],literal="correct",match="partial")
geo("P000172","theorem","Bott--Samelson cohomology restriction",
 r"""The notes attribute to Bott the result that the preceding manifold has the same cohomological structure as the symmetric model.""",
 r"""For a closed simply connected manifold in the all-geodesics-closed setting, Bott--Samelson theory constrains its integral cohomology ring to that of a compact rank-one symmetric space. In particular it is a truncated polynomial ring of the corresponding sphere or projective-space type; this does not determine the smooth structure.""",
 r"""The coefficient ring and distinction from diffeomorphism classification are made explicit. The attribution is broadened to the standard Bott--Samelson formulation rather than attributing every refinement to one manuscript parenthesis.""",
 "E",r"""The modern formulation and reference to its classical proof are given by \citet[Introduction, pp.~1--2]{lisong2026zoll}; it is an already known partial answer, not the full smooth classification.""",
 r"""established topological restriction.""",["lisong2026zoll"],literal="correct with missing hypotheses",match="partial")
coid=geo("P000172","question","Contact structures on compact three-manifolds",
 r"""The last question is whether every compact \(M^3\) has a contact structure.""",
 r"""Every closed orientable smooth three-manifold admits a contact structure. The statement with no orientability assumption is false: a contact plane field locally given by \(\ker\alpha\) orients a three-manifold by \(\alpha\wedge d\alpha\), since replacement by \(f\alpha\) multiplies this volume form by \(f^2>0\). Thus a closed nonorientable example such as \(\mathbb{RP}^2\times S^1\) admits none, even if coorientation is not required.""",
 r"""The orientability correction is necessary for the literal question, not an optional modern strengthening. Compact is read as closed; boundaries require an additional convention. The local-form orientation check was independently verified by expanding \(f\alpha\wedge d(f\alpha)\).""",
 "B",r"""Martinet's affirmative orientable theorem appeared in 1971 \citep{martinet1971contact}; \citet[pp.~165--166]{eliashberg1992contact} explicitly states both the existence theorem and the orientation consequence.""",
 r"""settled: yes for closed orientable three-manifolds, no for nonorientable ones.""",["martinet1971contact","eliashberg1992contact"],literal="false as written",problem="GP-1966-27")
problem("GP-1966-27","Existence of contact structures in dimension three",
 r"""Which closed smooth three-manifolds admit a contact plane field?""",[coid],
 r"""exactly the orientable ones: necessity follows from the contact volume orientation and sufficiency from Martinet's theorem.""",["martinet1971contact","eliashberg1992contact"])
save()

# Keep separately stated mathematical assertions as separate occurrences.
old105=[x for x in items if x["record"]==105]
old105[5]["title"]="Holomorphic kernels in a left half-plane"
old105[5]["notes"]=r"""Assertion (i) says \(s\mapsto K_s\) is holomorphic into \(C^k\) when \(\operatorname{Re}(ms)<-n-k\)."""
old105[5]["statement"]=r"""Under the spectral-cut hypotheses of the preceding item, the distribution kernel of \(A^s\) is a holomorphic family; for \(\operatorname{Re}(ms)<-n-k\) its values are in \(C^k(M\times M)\), holomorphically in that topology."""
old105[5]["reconstruction"]=r"""The operator acts on a smooth bundle over a closed \(n\)-manifold. The stated threshold ensures enough negative order for the kernel derivatives to be continuous."""
old105[5]["fate"]=r"""This is the first kernel assertion of \citet[p.~97]{seeley1968powers}."""
item(105,"P000162","theorem","Entire continuation off the diagonal",
 r"""Assertion (ii) takes a compact set in \(M\times M\) disjoint from the diagonal and continues the restricted kernels holomorphically over the whole \(s\)-plane.""",
 r"""For every compact subset \(C\subset M\times M\setminus\operatorname{diag}M\), the kernel of \(A^s\) depends entirely on \(s\) as a smooth function on a neighbourhood of \(C\), with every \(C^\infty\) seminorm controlled locally in \(s\).""",
 r"""Smoothness in \(x,y\) is not real analyticity; the notebook itself warns that the coefficients are only infinitely differentiable.""",
 "B",r"""This is the off-diagonal kernel assertion of \citet[p.~97]{seeley1968powers}.""",
 r"""established in the classical elliptic calculus.""",["seeley1968powers"],literal="correct")
off=items.pop()
item(105,"P000162","theorem","Meromorphic continuation of the diagonal density",
 r"""Assertion (iii) gives possible simple poles at \((j-n)/m\), omitting zero because it is regular.""",
 r"""The initially defined diagonal \(K_s(x,x)\) has meromorphic continuation, with at most simple poles among \((j-n)/m\), \(j\in\mathbb N_0\). The candidate pole at zero is removable; other possible poles may cancel. This is a continued density-valued endomorphism.""",
 r"""Continuation is performed after taking the diagonal in a half-plane where it is defined. It is not a general distributional restriction operation.""",
 "B",r"""The candidate poles and regularity at zero are in \citet[p.~97]{seeley1968powers}.""",
 r"""established; the distinction from the full zero-power kernel is treated next.""",["seeley1968powers"],literal="correct")
diag=items.pop()
item(105,"P000162","theorem","Complex powers remain pseudodifferential",
 r"""The final paragraph says \(A^s\) is pseudodifferential, with a symbol obtained by inserting the symbol in the contour formula.""",
 r"""For an invertible classical elliptic operator of order \(m>0\) with a spectral cut, \(A^s\) is classical of complex order \(ms\). Its homogeneous symbol coefficients are obtained by contour integration of the parameter-resolvent symbol expansion.""",
 r"""The substitution is in the full symbolic calculus: lower-order derivative corrections are present. It is generally false that the exact symbol is just the pointwise scalar power \(a(x,\xi)^s\).""",
 "B",r"""This is the symbol construction of \citet[pp.~97--99]{seeley1968powers}.""",
 r"""established; its symbol calculation supplies the preceding local density formula.""",["seeley1968powers"])
pdo=items.pop()
new105=old105[:6]+[off,diag]+old105[6:]+[pdo]
items=[x for x in items if x["record"]!=105]+new105

item(113,"P000169","definition","Planar incompressible Navier--Stokes and Euler systems",
 r"""The notes display both momentum equations for \(u,v\), the pressure gradient, \(\nu\Delta u,\nu\Delta v\), and \(u_x+v_y=0\); \(\nu=0\) is called Euler's ideal-fluid system.""",
 r"""For constant density \(\rho>0\) and kinematic viscosity \(\nu>0\), a smooth planar velocity \(w=(u,v)\) obeys \(\partial_tw+(w\cdot\nabla)w=-\rho^{-1}\nabla p+\nu\Delta w\), \(\nabla\cdot w=0\). The formal zero-viscosity equations are the incompressible Euler system. This algebraic substitution alone is not a convergence theorem.""",
 r"""The vector notation condenses the two correctly written component equations. Boundary and initial conditions are a separate part of either problem.""",
 "E",r"""These are the classical governing equations used in \citet[\S1]{oleinik1968boundary}.""",
 r"""standard equations; the boundary-condition issue is the next item.""",["oleinik1968boundary"],literal="correct")
ns=items.pop()
old113=[x for x in items if x["record"]==113]
items=[x for x in items if x["record"]!=113]+[ns]+old113

geo("P000171","theorem","The known low-dimensional Monge--Ampere cases",
 r"""The Calabi question is followed by “proved for \(n=2\) and for \(n\le5\), Calabi”.""",
 r"""Before this 1966 list, quadratic rigidity for convex entire \(\det D^2u=1\) solutions was known in dimension two by J\"orgens and through dimension five by Calabi. These are special cases of the later all-dimensional theorem, but are separate historical results in the notes.""",
 r"""The notebook's punctuation is not read as attributing J\"orgens's two-dimensional theorem to Calabi.""",
 "E",r"""\citet[Introduction, p.~549]{caffarellili2003extension} identifies the two precedents; \citet[bibliography]{pogorelov1972improper} dates them to 1954 and 1958.""",
 r"""established before the seminar.""",["caffarellili2003extension","pogorelov1972improper"],literal="correct")
low=items.pop()
old114=[x for x in items if x["record"]==114]
items=[x for x in items if x["record"]!=114]+old114[:4]+[low]+old114[4:]

# Stable order and occurrence links after the insertions.
items.sort(key=lambda x:x["record"])
renumber={}
counts={}
for x in items:
    counts[x["record"]]=counts.get(x["record"],0)+1
    newid=f'1966-{x["record"]}.{counts[x["record"]]}'
    renumber[x["id"]]=newid
    x["id"]=newid
for p in problems:p["occurrences"]=[renumber.get(v,v) for v in p["occurrences"]]
for x in items:
    for k in ("notes","statement","reconstruction","fate","present_status"):
        x[k]=x[k].replace(r"\citet{ kohnnirenberg1965algebra}",r"\citet{kohnnirenberg1965algebra}")
    if x["title"]=="The scope of stability of a boundary layer":
        x["verification"]="read the result"
        x["fate"]=x["fate"].replace("abstract and main instability theorem","Theorem 1, author version pp.~4--5")
    if x["title"]=="Entire convex solutions of the constant Monge--Ampere equation":
        x["fate"]+=r""" The all-dimensional paper \citep{pogorelov1972improper} was received in June 1971 and published in 1972; its metadata, rather than its full proof, was checked."""
        x["refs"].append("pogorelov1972improper")
    if x["title"]=="Analytic expressions for topological index data":
        x["notes"]=r"""Nirenberg's report is analytic without explicit topology. The scan says the connection to topology and the disappearance of lower-order terms are unclear; the supplied transcription instead says “no connections” and “leading terms”. Gelfand replies that Atiyah--Singer and Pontryagin classes also have analytic expressions."""
        x["reconstruction"]=r"""The corrected readings are \ru{неясна связь} and \ru{младшие члены}. No particular degree map or characteristic polynomial is supplied. Independence of the index under lower-order perturbations must be distinguished from dependence of a chosen local density representative."""
    if x["title"]=="Fusion multiplicities do not determine even a finite group":
        x["reconstruction"]=x["reconstruction"].replace("This elementary countercheck",r"This elementary countercheck \ours\ ")
    if x["title"]=="Contact structures on compact three-manifolds":
        x["reconstruction"]+=r""" The local identity \(\alpha'=f\alpha\Rightarrow\alpha'\wedge d\alpha'=f^2\alpha\wedge d\alpha\) is checked here \ours."""

corr("P000161","opening analytic-index paragraph","никаких связей с топологией / no connections with topology","неясна связь с топологией / the connection with topology is unclear","Direct inspection shows the singular words неясна связь, not никаких связей.","both","transcription")
corr("P000161","opening analytic-index paragraph","главные члены / leading terms","младшие члены / lower-order terms","The scan clearly shows the initial м and the word младшие; this is also the mathematically relevant order-perturbation issue.","both","transcription")
corr("P000162","sentence following (iii)",r"At \(s=0\) this is not the identity operator",r"\(A^0=I\); the continued diagonal density at zero is not restriction of its delta kernel","The sentence is present in the scan. The correction separates two noncommuting operations; it is a mathematical emendation.")
corr("P000162","order-one reduction parenthesis","Take m=1 (multiply by an invertible operator)","An order reduction must specify what invariant it preserves; individual complex powers are not preserved by arbitrary multiplication","Faithfully written shorthand. Index preservation under suitable elliptic order reduction does not identify the original powers.","both","ambiguity")
corr("P000163","uniform mixing gloss","uniformly over all pairs U","Keep the diplomatic wording; the later precise formula fixes one local event before taking the remote-event supremum","Scan confirms the strong gloss. Minlos1968 formula(2.5), pp151–152, has more careful quantifiers.","both","ambiguity")
corr("P000165","mean-energy ratio","Numerator has no 1/N! while the preceding Z includes it","Use the same Gibbs reference-measure convention in numerator and denominator","The ratio is correct only with consistent normalization; an abbreviated da may conceal the quotient measure.","both","ambiguity")
corr("P000165","pressure derivative",r"p=∂_V log Z",r"Physical pressure is β^{-1}∂_V log Z; the written quantity may be reduced pressure βp","The manuscript gives no unit convention; adjacent p=τ1 supports reduced-pressure interpretation.","both","ambiguity")
corr("P000165","entropy definition",r"S=∫π logπ",r"S=−∫π logπ for Gibbs entropy","The plus sign is visibly in the source. Substitution of π=Z^{-1}e^{-βH} checks the sign independently.")
corr("P000165","entropy per-particle identity",r"S/N=(log Z)/N−β^{-1}∂_β((log Z)/N)",r"S/N=(log Z)/N−β∂_β((log Z)/N)","The source visibly has 1/β. It contradicts the standard Gibbs identity even after choosing an entropy sign convention.")
corr("P000166","generating-function example",r"graph p(q) Lagrangian iff p=∂S/∂q",r"Locally iff; globally iff p·dq is exact","The scan has no local qualifier. A closed angular form on an annulus supplies the elementary obstruction.")
corr("P000166","word after map to the circle","katsikl [?]","cocycle / cohomology class [contextual reading]","The subsequent H^1(M,Z) and degree formula determine the mathematical meaning; the Russian letter-level uncertainty remains.","en","translation")
corr("P000167","top heading","Minlos. Lecture5. Phase transitions","Record this as an additional heading only, separate from Gelfand's duality and Nirenberg's heat-kernel report","The scan supplies no phase-transition lecture body before the next speaker heading; the MCCME list has no separately allocated record here.","both","provenance")
corr("P000167","finite-group multiplicity claim","Tensor multiplicities recover a finite group","Multiplicity-only interpretation is false; actual intertwiner and tensor data are needed","The sentence is overwritten, so its reading is qualified. D8 and Q8 have the same complex fusion rules but are nonisomorphic.")
corr("P000167","arbitrary matrices in duality equations","Every family of arbitrary linear C_i satisfying the equations equals T_i(g)","Require unit-normalized unitary tensor-natural automorphisms and compatible duals","The zero family satisfies the bare homogeneous equations; for S1, C_k=z^k with nonunit |z| shows the missing reality condition.")
corr("P000167","heat-kernel exponent",r"u=exp[−g/t+o(1/t)], g=d²",r"g=d²/4 for the written generator ∑a^{ij}∂_{ij}","The same scanned page gives the Euclidean Gaussian exp[−|x−y|²/(4t)], which fixes the discrepancy.")
corr("P000168","Vishik Lecture1 and extra professor heading","Kohn–Nirenberg definition; boundedness theorem; Prof.Lodzhs. on Sturm–Liouville","Preserve as headings; do not reconstruct a complete theorem or assign the extra heading to Vishik","The source contains no symbol class or theorem statement; the professor's name is uncertain.","both","provenance")
corr("P000169","last abbreviation","отлип. / otlip.","отлич. / differ","Direct scan inspection shows отлич.; the sentence describes strong differences between viscous and inviscid velocity in a narrow region.","both","transcription")
corr("P000170","initial and inflow profiles",r"u|x=0=u0(x), u|t=0=u0(x,t)",r"u|x=0=u1(t,y), u|t=0=u0(x,y), with corner compatibility","The variables are inconsistent in the scan itself. Oleinik1966 p751 gives the correctly indexed initial/inflow problem.")
corr("P000170","crossed-out p_y=0 line","p_y=0 is crossed out in the display","Preserve cancellation but retain the following explicit statement p=p(t,x)","The prose immediately says pressure is constant along the normal; cancellation does not remove that model assumption.","both","ambiguity")
corr("P000170","unqualified existence and stability lines","Unique if it exists; always stable","These statements require the monotone solution class, compatibility, decay and specified stability norms","Oleinik1966 and Oleinik1968 Theorems4–5 supply omitted assumptions; the final abbreviation does not specify a norm.","both","faithful_error")
corr("P000171","minimal-surface equation",r"(1+Σu_i²)(Σu_jj²)−Σu_ij u_i u_j=0",r"(1+Σu_i²)Σu_jj−Σu_ij u_i u_j=0","The extra raised square is visible in the uncancelled manuscript line. Deleting it is required by the note's identification with minimal graphs.")
corr("P000171","Bernstein question parenthesis","Done (reference in De Giorgi)","Affirmative only in restricted dimensions; modern sharp answer is yes n≤7, no n≥8","The note supplies no dimension restriction. Bombieri–De Giorgi–Giusti1969 resolves the higher-dimensional negative cases.")
corr("P000171-P000172","attribution of geometry problems","Problems placed after Agranovich's PDO Lecture3 heading","Associate by manuscript position but keep the problem-list speaker unattributed","No speaker name introduces the geometry list and no PDO lecture text appears; page overlap is not evidence that every problem was Agranovich's.","both","provenance")
corr("P000172","problem7 geodesics","intersect. geodesics / пересек.","Retain uncertain intersecting-geodesic wording; do not silently emend to closed geodesics","The scan has пересек. after a cancelled word and no legible замкнутых in this problem; problem8 does explicitly write geodesics closed.","both","ambiguity")
corr("P000172","number following7","3.[?]","8 [sequential numbering, manuscript glyph ambiguous]","Its position between7 and9 identifies list position; the written glyph itself remains 3/8-like.","both","ambiguity")
corr("P000172","symmetric-space type in problem8","of the1st type; cancelled rank-like expression","Rank-one symmetric space [mathematical reconstruction, not a certain diplomatic reading]","The surrounding Bott cohomology and sphere examples support the CROSS identification, but the cancelled word cannot be recovered with certainty.","both","ambiguity")
corr("P000172","contact existence question","every compact M3","every closed orientable smooth M3; without orientability the answer is no","Contact local forms induce a consistent orientation in dimension3; Martinet proves sufficiency for orientable closed manifolds.")
save()

# Include reused keys verbatim; preserve audit annotations for new sources.
import re
cumulative=(OUT.parents[1]/"source_inputs/references_cumulative.bib").read_text()
bib=(OUT/"references_new.bib").read_text()
for key in ("kohnnirenberg1965algebra","hormander1965pseudo"):
    m=re.search(r"@\w+\{"+key+r",.*?\n\}",cumulative,re.S)
    assert m,key
    bib+="\n"+m.group(0)+"\n"
(OUT/"references.bib").write_text(bib)

# A concise machine-readable check accompanies the research handoff.
required=set("id record pages kind title notes statement reconstruction class fate present_status literal_correctness publication_match verification development problem worth refs confidence".split())
assert len(talks)==10 and {t["record"] for t in talks}==set(range(105,115))
assert len({x["id"] for x in items})==len(items)
bibkeys=set(re.findall(r"@\w+\{([^,]+),",bib))
for x in items:
    assert required<=x.keys(),x["id"]
    assert set(x["refs"])<=bibkeys,(x["id"],set(x["refs"])-bibkeys)
    assert x["class"] not in "CD" or x["worth"],x["id"]
for p in problems:
    assert set(p["occurrences"])<={x["id"] for x in items}
from collections import Counter
check=dict(records=len(talks),items=len(items),problems=len(problems),corrections=len(corrections),references=len(bibkeys),
           by_class=dict(Counter(x["class"] for x in items)),by_record=dict(Counter(x["record"] for x in items)),
           validation="required fields, unique sequential ids, reference keys, and problem occurrences checked")
(OUT/"validation.json").write_text(json.dumps(check,indent=2)+"\n")
print(json.dumps(check,indent=2))
