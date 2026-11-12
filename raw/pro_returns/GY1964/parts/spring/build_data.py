import json, re, csv
from pathlib import Path

BASE = Path(__file__).resolve().parent
items, talks, problems, corrections = [], [], [], []

def save():
    for name, data in [('items',items),('talks',talks),('problems',problems)]:
        (BASE/(name+'.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    with (BASE/'corrections.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=['page','place','transcription_reads','should_read','evidence','applies_to','type'])
        w.writeheader(); w.writerows(corrections)

def talk(record,date,speaker,pages,title,summary,kind='talk'):
    talks.append(dict(record=record,date=date,speaker=speaker,pages=pages,title=title,kind=kind,summary=summary))

def item(record,pages,kind,title,notes,statement,fate,refs=(),**kw):
    n=1+sum(i['record']==record for i in items)
    d=dict(id=f'1964-{record}.{n}',record=record,pages=pages,kind=kind,title=title,notes=notes,statement=statement,
           reconstruction='',**{'class':'E'},fate=fate,present_status='As of November 2026: established with the hypotheses in the modern statement.',
           literal_correctness='correct with missing hypotheses',publication_match='exact',verification='read the result',
           development='annotated',problem='',worth='',refs=list(refs),confidence='high')
    d.update(kw); items.append(d)

def correction(page,place,reads,correct,evidence,typ='faithful_error',applies='both'):
    corrections.append(dict(page=page,place=place,transcription_reads=reads,should_read=correct,evidence=evidence,applies_to=applies,type=typ))

def problem(id,title,statement,occurrences,status,refs):
    problems.append(dict(id=id,title=title,statement=statement,occurrences=occurrences,status=status,status_date='2026-11',refs=refs))

# The record catalog gives overlapping page envelopes; item pages locate the actual statements.
talk(36,'1965-03-08','Ya. G. Sinai','P000062-P000066','Moduli of ergodic eigenfunctions',
     r'The dated Sinai fragment on P000063 states that a Koopman eigenfunction of an ergodic system has constant modulus. The surrounding pages continue earlier dynamical-system material and begin other speakers; the catalog envelope is retained without attributing all its contents to this fragment.')
item(36,'P000063','theorem','Ergodic eigenfunctions have constant modulus',
     r'The notes give \(U_t f_\lambda=e^{i\lambda t}f_\lambda\) and \ru{пост. по mod (у эргод. системы)}.',
     r'Let \((X,\mu)\) be a probability space and \((T_t)\) an ergodic measure-preserving measurable flow. If \(0\ne f\in L^2(\mu)\) and \(f\circ T_t=e^{it\lambda}f\) for every \(t\), as equalities in \(L^2\), then \(|f|=c>0\) almost everywhere. More generally the same statement holds for an ergodic action and a unitary character.',
     r'This is an immediate consequence of ergodicity: \(|f|\) is invariant. It is used explicitly, in the normalization \(|f|=1\), by \citet[p.~775]{stepin1966spectra}. That 1966 use is corroboration, not a claim that the elementary observation originated then.',
     ['stepin1966spectra'],literal_correctness='correct',reconstruction=r'The probability-space convention and almost-everywhere qualification make the shorthand precise.')
save()

talk(37,'1965-03-29','V. N. Latyshev','P000064-P000067','Enveloping algebras, Lie ideals and bounded nilpotence',
     r'The speaker, named only Viktor Nikolaevich in the handwriting, discusses primitive universal enveloping algebras, the passage from associative to Lie ideals, and a Burnside-type nilpotence assertion attributed to Kostrikin. The catalog identification as Latyshev is retained. Two assertions require correction or cannot be identified with a theorem under the recorded hypotheses.')
item(37,'P000065','problem','When is a universal enveloping algebra primitive?',
     r'The notes ask when \(U(L)\) is primitive and explain this as admitting a faithful irreducible module; Harish-Chandra and Jacobson are named.',
     r'For a specified Lie algebra \(\mathfrak g\) over a field \(k\), determine whether the associative algebra \(U(\mathfrak g)\) has a faithful simple left module. A useful later formulation, for finite-dimensional complex \(\mathfrak g\), is the primitiveness of the zero ideal, equivalently rationality of that prime ideal in the Dixmier--Moeglin equivalence.',
     r'The question became part of the systematic theory of primitive ideals. \citet[abstract and pp.~488--500]{ooms1974primitive} gives necessary conditions and a converse for solvable algebras over an algebraically closed field of characteristic zero. This exact scope is narrower than arbitrary Lie algebras or fields. The original article was not accessible in full during this run; its advertised theorem is not used beyond that scope.',
     ['ooms1974primitive'],**{'class':'B'},publication_match='partial',verification='indirect',confidence='medium',
     reconstruction=r'Finite dimension, characteristic zero and the base field are not recorded; the complex finite-dimensional case is a reconstruction. No claim is made that all \(U(\mathfrak g)\) are primitive.',
     present_status=r'As of November 2026: a developed primitive-ideal theory, rather than the fixed-rank Weyl endomorphism conjecture. This entry does not assert a field-independent criterion.',problem='GP-1964-S01')
item(37,'P000065','example' if False else 'construction','Two two-dimensional examples of primitive envelopes',
     r'The nonabelian relation is \([e_1,e_2]=e_1\); its envelope is called primitive. The abelian two-generator envelope is said not to be primitive because a commutative primitive ring is a field.',
     r'Over \(\mathbb C\), the two-dimensional nonabelian Lie algebra \([x,h]=x\) has primitive enveloping algebra. In contrast \(U(\mathbb C^2)=\mathbb C[x,h]\) is not primitive: every simple module of a commutative ring is a residue field, and faithfulness forces the ring itself to be a field.',
     r'The elementary examples agree with the later solvable-Lie-algebra criteria described by \citet[pp.~488--500]{ooms1974primitive}. The nonabelian conclusion is sensitive to the field; the modern statement deliberately uses \(\mathbb C\).',
     ['ooms1974primitive'],verification='indirect',confidence='medium')
item(37,'P000065','claim','Associative simplicity does not eliminate Lie ideals',
     r'Under the name Baxter the manuscript says \ru{Если A --- простая, то Ли-ид. тоже нет}, and repeats that absence of ordinary ideals implies absence of Lie ideals.',
     r'The literal assertion is false. In the simple associative algebra \(M_2(\mathbb C)\), the center \(\mathbb C I\) is a proper nonzero Lie ideal; so is \(\mathfrak{sl}_2(\mathbb C)\). Correct simplicity theorems concern specified commutator Lie algebras, quotients by their centers, or skew elements of an algebra with involution, with characteristic and small-dimension exceptions.',
     r'Baxter\textquotesingle s paper \citet[title and theorem scope]{baxter1956lie} concerns a special class of associative rings; its topic cannot validate the unrestricted sentence. The direct matrix counterexamples already settle the literal reading. No new open problem is inferred from the error.',
     ['baxter1956lie'],literal_correctness='false as written',publication_match='thematic only',verification='publisher metadata checked',confidence='high',
     reconstruction=r'The corrected theorem is intentionally not guessed: the notebook omits the quotient or involution that would determine which result was intended.',
     present_status=r'As of November 2026: false literally; the intended Baxter theorem remains incompletely identified.',**{'class':'F'})
item(37,'P000066','claim','Uniform nilpotence on a generating Lie algebra',
     r'The Burnside/Kostrikin paragraph has finite generators \(X\), their Lie algebra \([X]\), and a corrected quantifier \(\exists n\) followed by \(e^n=0\). It concludes that the associative algebra is \ru{нильпот.}, glossed as every element being nilpotent.',
     r'The strongest recoverable question is: if a finitely generated associative algebra \(A\) over an unspecified field is generated by a finite set \(X\), and every element of the Lie subalgebra generated by \(X\) has a common associative nilpotence bound, what follows about \(A\)? Being nil (each element nilpotent) and being nilpotent (\(A^m=0\) for one \(m\)) are different conclusions.',
     r'Searches on Latyshev, Kostrikin, the restricted Burnside problem, Lie-generated associative algebras and bounded nilpotence did not identify a theorem with precisely these assumptions and conclusion. A citation to a restricted-Burnside theorem alone would not supply the omitted characteristic and identity hypotheses.',
     [],**{'class':'F'},literal_correctness='not determinable',publication_match='none found',verification='unresolved lead',confidence='low',
     reconstruction=r'The membership sign \(e\in[X]\) and universal quantification over \(e\) are interpretive expansions. The field, associativity and distinction between nil and nilpotent are not supplied by the notes.',
     present_status=r'As of November 2026: insufficiently specified for a reliable fate assignment; not classified as an undeveloped conjecture.')
save()

talk(38,'1965-03-29','I. M. Gelfand','P000065-P000067','Weyl algebras with different numbers of canonical pairs',
     r'A short intervention attributes to Dixmier the question whether the differential-operator algebras in one and in two variables are isomorphic. This is a comparison of different ranks. Gelfand and Kirillov answered such isomorphism questions in 1966 by an invariant of growth.')
item(38,'P000066','question','Weyl algebras of different ranks',
     r'The two rings are written \(P(x,d/dx)\) and \(P(x,d/dx,y,d/dy)\), followed by \ru{Изоморфны ли эти кольца?}.',
     r'Over a field \(k\) of characteristic zero, let \(A_n(k)=k\langle x_1,\ldots,x_n,\partial_1,\ldots,\partial_n\rangle/([x_i,x_j],[\partial_i,\partial_j],[\partial_i,x_j]-\delta_{ij})\). Are \(A_1(k)\) and \(A_2(k)\) isomorphic as \(k\)-algebras? They are not: more generally \(A_m(k)\cong A_n(k)\) implies \(m=n\).',
     r'\citet[\S4, Lemma~5 and Theorem~2, pp.~11--14]{gelfandkirillov1966corps} distinguish the algebras \(R_{n,k}\), including Weyl algebras, by growth. The paper was received 19 January 1966 and published that year. In modern terms \(\operatorname{GKdim}A_n=2n\). This is unrelated in quantifiers to asking whether every endomorphism of one fixed \(A_n\) is an automorphism.',
     ['gelfandkirillov1966corps'],**{'class':'A'},literal_correctness='correct',problem='GP-1964-04',
     reconstruction=r'The base field and preservation of it are made explicit. The scan decisively shows one canonical pair versus two.',
     present_status=r'As of November 2026: solved negatively for isomorphism of distinct ranks; the same-year first index must not label this an open fixed-rank endomorphism conjecture.')
problem('GP-1964-04','Isomorphism of Weyl algebras of different ranks',
        r'For characteristic-zero \(k\), can \(A_m(k)\cong A_n(k)\) as \(k\)-algebras with \(m\ne n\)? The notebook asks \(m=1,n=2\).',
        ['1964-38.1'],r'Solved: no. Growth dimension \(2n\) distinguishes the rank; Gelfand--Kirillov, received January 1966, published 1966. Status checked November 2026.',['gelfandkirillov1966corps'])
save()

talk(39,'1965-03-29','S. I. Gelfand','P000065-P000070','Dyson circular ensembles and the logarithmic gas',
     r'The talk explains the circular orthogonal and unitary ensembles, their eigenangle densities and a Coulomb-gas interpretation of an empty arc. It then moves from an exact finite-dimensional integral to a continuum free-energy ansatz. The manuscript fails to keep that approximation separate from an exact gap formula.')
item(39,'P000066','construction','The circular orthogonal ensemble as U(N)/O(N)',
     r'Symmetric unitary matrices satisfy \(U^T=U\), \(UU^*=I\), with action \(U\mapsto VUV^T\); the stabilizer at the identity is orthogonal. The eigenangle density has Vandermonde power one.',
     r'The pushforward of Haar measure under \(V\mapsto VV^T\) on \(U(N)\) is the invariant probability measure on \(U(N)/O(N)\). Its unordered eigenangles have joint density \(Z_{N,1}^{-1}\prod_{i<j}|e^{i\theta_i}-e^{i\theta_j}|\) relative to Lebesgue measure on \([0,2\pi)^N\), with the ordering convention absorbed in \(Z_{N,1}\).',
     r'This is Dyson\textquotesingle s circular orthogonal ensemble, published in 1962 after receipt in September 1961; see \citet[the circular ensembles and eigenvalue measures]{dyson1962statisticalI}.',
     ['dyson1962statisticalI'],literal_correctness='correct')
item(39,'P000066','construction','Haar unitary eigenangles and quadratic repulsion',
     r'For all unitary matrices the notes display Vandermonde power two and discuss integration over conjugacy classes. In the action formula the final \(V^*\) is crossed or omitted.',
     r'For Haar-distributed \(U\in U(N)\), the eigenangle density is \(Z_{N,2}^{-1}\prod_{i<j}|e^{i\theta_i}-e^{i\theta_j}|^2\). Haar invariance is under left and right multiplication; conjugation \(U\mapsto VUV^*\) is the action relevant to eigenvalue class integration.',
     r'The circular unitary ensemble and its eigenangle law are already in \citet[unitary ensemble]{dyson1962statisticalI}. Coinciding angles have vanishing density, the precise content of the recorded repulsion remark.',
     ['dyson1962statisticalI'],reconstruction=r'Left invariance and conjugacy invariance are separated instead of treating the incomplete action as a new ensemble.')
item(39,'P000066-P000068','construction','Circular beta gap integrals and logarithmic interaction',
     r'The forbidden arc is \((-\alpha,\alpha)\); the normalized probability is eventually written \(R_\beta=\Psi_\beta(\alpha)/\Psi_\beta(0)\). The first energy sign conflicts with the later Boltzmann factor.',
     r'For \(N\ge1,\beta>0,0\le\alpha<\pi\), define \(\Psi_{N,\beta}(\alpha)=\int_{[\alpha,2\pi-\alpha]^N}\prod_{i<j}|e^{i\theta_i}-e^{i\theta_j}|^\beta\,d\theta\). Then \(R_{N,\beta}(\alpha)=\Psi_{N,\beta}(\alpha)/\Psi_{N,\beta}(0)\) is the no-eigenangle probability. With energy \(W=-\sum_{i<j}\log|e^{i\theta_i}-e^{i\theta_j}|\), the density is proportional to \(e^{-\beta W}\).',
     r'Dyson\textquotesingle s log-gas construction is exact at the finite integral level; see \citet[statistical-mechanical interpretation]{dyson1962statisticalI}. The source\textquotesingle s missing product and normalization are repaired by its own next page.',
     ['dyson1962statisticalI'],literal_correctness='false as written',reconstruction=r'The sign convention, product over pairs and normalization are supplied explicitly; \(\beta>0\) is a sufficient integrability range, not the maximal possible range.')
item(39,'P000067-P000068','method','Continuum density and local free-energy approximation',
     r'The notes replace the point density by \(\sigma\), impose \(\int\sigma=N\), and write \(F=V+F_1\) with a logarithmic double integral and a local term \(\int\sigma f_\beta(\sigma)\). They label the construction a physical assumption.',
     r'The empirical measure is \(\sum_{j=1}^N\delta_{\theta_j}\), not an ordinary density. A continuum ansatz replaces it by \(\sigma(\theta)\,d\theta\), minimizes a logarithmic-energy functional under the mass and support constraints, and adds a local entropy correction. This does not give an exact finite-\(N\) theorem. If \(F=-\beta^{-1}\log\Psi\), then \(R=e^{-\beta(F_\alpha-F_0)}\).',
     r'The method is the 1962 Dyson asymptotic program, not an independently established exact identity. Later determinant asymptotics such as \citet[Introduction and the large-gap formulas]{ehrhardt2007dyson} separate leading energy, logarithmic terms and constants.',
     ['dyson1962statisticalI','ehrhardt2007dyson'],publication_match='partial',reconstruction=r'The distinction between an empirical measure and a density, and between an ansatz and a theorem, is editorial. The source also permits its positive-sign exponential to define an opposite convention for \(F\); it cannot simultaneously be the usual minimized free energy without a sign change.',literal_correctness='correct with missing hypotheses')
item(39,'P000067','claim','The cosine-power expression is not an exact CUE gap probability',
     r'The manuscript writes \(R_2(\alpha)=\exp(N^2\log\cos(\alpha/2))\) as an equality.',
     r'The equality \(R_{N,2}(\alpha)=\cos(\alpha/2)^{N^2}\) is false for the stated circular unitary ensemble. For \(N=1\), the eigenangle is uniform and \(R_{1,2}(\alpha)=1-\alpha/\pi\), which is not \(\cos(\alpha/2)\). The cosine-power captures a leading energy contribution in an appropriate large-\(N\) regime, not the complete finite probability.',
     r'The later asymptotic theory includes essential subleading powers and constants. \citet[Introduction]{ehrhardt2007dyson} verifies the distinction in the sine-kernel limit; it is not a proof of the notebook\textquotesingle s finite equality. The same expression returns in item 1964-42.1.',
     ['ehrhardt2007dyson'],literal_correctness='false as written',publication_match='partial',reconstruction=r'The one-eigenvalue check is an editorial diagnosis. No unrecorded special ensemble is inserted to save the equality.',present_status=r'As of November 2026: the finite identity is disproved by \(N=1\); precise large-gap asymptotics are established.',**{'class':'B'})
save()

talk(40,'1965-04-05','I. N. Bernstein','P000068-P000073','Grothendieck topologies and arithmetic cohomology',
     r'Beginning with finite-field solutions as Frobenius fixed points, Bernstein introduces slice categories, products, coverings and sheaf descent. The title mentions monoidal transformations, but no actual blow-up construction is developed in this fragment. The category of sheaves over a field anticipates Galois cohomology.')
item(40,'P000069','method','Frobenius fixed points and the cohomological counting program',
     r'Reduction modulo \(p\) is denoted \(Z_p\). Over its algebraic closure, \(x\mapsto x^p\) fixes exactly the base field; a Lefschetz alternating trace is proposed to count rational points.',
     r'For a finite-type scheme \(X/\mathbb F_q\), \(X(\mathbb F_q)\) is the fixed-point set of the geometric Frobenius action on geometric points. The precise cohomological formula is \(\#X(\mathbb F_q)=\sum_i(-1)^i\operatorname{Tr}(\operatorname{Frob}_q\mid H^i_c(X_{\overline{\mathbb F}_q},\mathbb Q_\ell))\), with \(\ell\ne\operatorname{char}\mathbb F_q\) and compatible Frobenius convention.',
     r'The notebook describes the Weil--Grothendieck program rather than a usable topological Lefschetz theorem in the Zariski topology. The étale-site framework was circulating in the 1963--64 SGA seminar; the published source is \citet[Exposés I--IV, site and topos foundations]{sga4I1972}. The full trace formula requires additional étale-cohomological finiteness and trace theorems.',
     ['sga4I1972'],**{'class':'B'},publication_match='partial',verification='publisher metadata checked',reconstruction=r'Finite type, compact supports, \(\ell\)-adic coefficients and the Frobenius convention are later precise reconstruction, not statements supplied in the notes.',present_status=r'As of November 2026: the arithmetic trace formula is established; the recorded ordinary-topological analogy alone is insufficient.')
item(40,'P000069-P000070','definition','Slice categories and relative products',
     r'The objects over \(X\) are arrows \(U\to X\); a morphism is a commuting triangle. The universal property of products is explained, with open-set intersection and pairs having the same image as examples.',
     r'For a category \(\mathcal C\), the slice \(\mathcal C/X\) has objects \(U\to X\). If \(U\times_X V\) exists, it is the product of \(U\to X\) and \(V\to X\) in this slice. Its universal property gives uniqueness up to a unique isomorphism. For the poset of opens of a space, this is intersection.',
     r'This is the categorical language used in SGA~4; see \citet[Exposé I]{sga4I1972} and the explicit modern site conventions of \citet[Tag 00VH]{stacks2026sites}. Publication in 1972 must not be mistaken for first circulation: the seminar dates to 1963--64.',
     ['sga4I1972','stacks2026sites'],literal_correctness='correct')
item(40,'P000070-P000071','definition','Covering families and Grothendieck topologies',
     r'The axioms require identity coverings, composition of covering families and preservation under pullback. Existence of every pairwise product in the slice is recorded separately.',
     r'A pretopology on a category with the requisite fiber products is a collection of covering families containing isomorphisms and stable under base change and composition. It generates a Grothendieck topology of covering sieves. A general Grothendieck topology does not require all fiber products in the underlying category; the notes use a convenient stronger presentation.',
     r'This is established pre-lecture Grothendieck-site theory, circulated in SGA~4 (1963--64) and published in \citet[Exposé II]{sga4I1972}. \citet[Tag 00VH and covering axioms]{stacks2026sites} supplies a checked current formulation.',
     ['sga4I1972','stacks2026sites'],reconstruction=r'The distinction between a pretopology of families and a topology of sieves is modern clarification.')
item(40,'P000071','definition','Sheaf descent and the point represented by a field',
     r'A presheaf is a contravariant abelian-group-valued functor. Compatible sections over a covering glue uniquely. The notes add that a point can mean a field and then give Galois cohomology.',
     r'A sheaf \(F\) on a site with fiber products satisfies the equalizer condition \(F(U)\to\prod_iF(U_i)\rightrightarrows\prod_{i,j}F(U_i\times_U U_j)\). On the small étale site of \(\operatorname{Spec}k\), abelian sheaves correspond to discrete continuous modules for \(G_k=\operatorname{Gal}(k^{\mathrm{sep}}/k)\); sheaf cohomology identifies with continuous Galois cohomology.',
     r'See \citet[Exposé II]{sga4I1972} for the foundations and \citet[Tags 00VL and 03QR]{stacks2026sites} for descent and the field case. The Zariski site of a one-point space would not produce this Galois information.',
     ['sga4I1972','stacks2026sites'],reconstruction=r'The small étale topology and continuity of the Galois action are missing but decisive hypotheses.')
save()

talk(41,'1965-04-12','I. M. Gelfand','P000071-P000073','A curriculum and a symmetric-space research direction',
     r'This is chiefly a planning intervention: subjects needed by seminar participants are listed, alongside a suggestion to extend Dyson\textquotesingle s calculations to symmetric spaces. The item index preserves both the organizational list and the mathematical direction.',kind='plan')
item(41,'P000072','remark','Subjects proposed for study',
     r'The list includes Lie groups and representations, sheaves and homological algebra, bundles, algebraic geometry, quantum mechanics, several-variable Cauchy theory and nuclear spaces with measures.',
     r'This is a curriculum proposal, not a theorem or a mathematically quantified research problem.',
     r'No publication fate can be assigned to a list of study topics. Its value is evidence of the seminar\textquotesingle s program and links to records 39, 40, 48 and 49.',
     [],**{'class':'F'},literal_correctness='not determinable',publication_match='none found',verification='indirect',development='none',confidence='high',present_status=r'As of November 2026: historical planning evidence; no open mathematical status is applicable.')
item(41,'P000072','problem','Dyson-type calculations on symmetric spaces',
     r'Gelfand proposes investigating Dyson\textquotesingle s results for general symmetric spaces.',
     r'One precise direction is to push invariant measure on a specified compact symmetric space to a maximal flat and compute the Jacobian in restricted-root coordinates, then study eigenvalue or radial gap observables. A space, normalization, root multiplicities and observable must be specified before an exact theorem can be stated.',
     r'Dyson\textquotesingle s \(U(N)/O(N)\) example is already a compact symmetric space \citep{dyson1962statisticalI}. Later random-matrix symmetry classifications systematically use symmetric spaces \citep[the symmetry-class correspondence]{altlandzirnbauer1997}. This matches the direction, not a single universal gap formula.',
     ['dyson1962statisticalI','altlandzirnbauer1997'],**{'class':'B'},publication_match='partial',verification='read the result',confidence='medium',reconstruction=r'The restricted-root formulation and choice of radial observables are an explanatory modern realization, not an assertion that the notebook posed a complete classification problem.',present_status=r'As of November 2026: extensively developed as a framework; the short suggestion is too broad to carry an unresolved problem label.')
save()

talk(42,'1965-04-12','S. I. Gelfand','P000071-P000073','Circular gap probabilities and an even sine-kernel determinant',
     r'The discussion revisits the cosine-power claim, relates a nearest-neighbor law to derivatives of an empty-interval probability and displays a cosine determinant with a large-gap prediction. Its written exponent and its scaling parameter require explicit critical annotation.')
item(42,'P000072','claim','Repeated cosine-power claim and an unnamed replacement model',
     r'The speaker says the cosine-power result has not been proved for the original model but another similar model gives it exactly. That replacement model is not specified.',
     r'For the original finite circular unitary ensemble, the asserted exact identity is false as in item 1964-39.5. No exact alternative statement can be recovered without the replacement ensemble and its probability measure.',
     r'Dyson\textquotesingle s asymptotic program and subsequent sine-kernel work explain the leading exponential, but do not identify the unrecorded substitute ensemble \citep[Introduction]{ehrhardt2007dyson}. The two claims must be separated: a false literal finite-CUE equality and an unidentifiable possible exact identity for another model.',
     ['ehrhardt2007dyson'],**{'class':'F'},literal_correctness='not determinable',publication_match='thematic only',confidence='low',present_status=r'As of November 2026: the original equality is false; the unnamed model remains unidentified. This is not evidence of an open exact-CUE problem.')
item(42,'P000072','method','Nearest-neighbor spacing from the empty-interval probability',
     r'A translation-invariant two-endpoint expression is written as \(S(\theta_2-\theta_1)\), and the spacing density is related to a second derivative of the empty-interval probability.',
     r'For a stationary simple point process on \(\mathbb R\) of intensity \(\rho>0\), let \(E(s)=\Pr\{N(0,s)=0\}\). Under the usual differentiability assumptions, the density \(p(s)\) of the forward nearest-neighbor distance under the Palm law is \(p(s)=E^{\prime\prime}(s)/\rho\). At unit intensity this is \(p=E^{\prime\prime}\). If the gap is parameterized by a half-width, chain-rule factors must also be included.',
     r'This is the standard gap-to-spacing mechanism in Dyson\textquotesingle s statistical theory \citep[spacing distributions]{dyson1962statisticalIII}. The notebook omits the density normalization; a two-point correlation function is not in general a nearest-neighbor density.',
     ['dyson1962statisticalIII'],verification='publisher metadata checked',reconstruction=r'The Palm nearest-neighbor law, intensity and differentiability hypotheses identify precisely which spacing distribution is meant.')
item(42,'P000073','claim','Even sine-kernel determinant and the large-gap exponent',
     r'The finite matrix is \(\delta_{pq}-\pi^{-1}\int_{-\alpha}^{\alpha}\cos(p\theta)\cos(q\theta)\,d\theta\), with half-integer \(p,q\). The scan shows an asymptotic factor \(t^{17/8}e^{-t^2/4-t/2}\) and \(t=\alpha n\).',
     r'For \(K_+(x,y)=\sin(x-y)/(\pi(x-y))+\sin(x+y)/(\pi(x+y))\) on \(L^2(0,s)\), the established asymptotic is \(\log\det(I-K_+)=-s^2/4-s/2-(1/8)\log s+c_++o(1)\) as \(s\to\infty\). Thus the power in this standard normalization is \(-1/8\), not \(17/8\).',
     r'\citet[Introduction, formulas for \(K_\pm\)]{ehrhardt2007dyson} proves the large-gap constant as well as these terms (preprint April 2006; publication 2007). The notebook\textquotesingle s finite cosine matrix is a precursor of this even kernel, but its additional notation \(2m=n\) would naturally scale with \(m\alpha\), not automatically with \(n\alpha\).',
     ['ehrhardt2007dyson'],**{'class':'B'},literal_correctness='false as written',publication_match='partial',reconstruction=r'The continuum kernel is identified separately from the finite matrix. The power is a faithful manuscript error, while the exact \(m,n,t\) normalization remains an ambiguity; no silent rescaling is made.',present_status=r'As of November 2026: the standard even-kernel asymptotic is established; the manuscript power and unexplained scaling cannot be used literally.')
save()

talk(43,'1965-04-12','A. M. Stepin','P000071-P000074','A torsion-group action with continuous spectrum',
     r'Stepin answers the preceding dynamical-system discussion with an action of the dyadic torsion group. Finite-order transformations can jointly have a continuous spectral component. His 1966 paper supplies an exact continuation and stronger spectral analysis.')
item(43,'P000072','construction','Continuous spectral component for a dyadic torsion-group action',
     r'The group is the dyadic rationals modulo one; the generators satisfy \(T_{1/2^{k+1}}^2=T_{1/2^k}\). The notes describe rearrangements of interval pieces and claim a continuous spectral component.',
     r'There is an ergodic probability-preserving action of the discrete Prüfer group \(\mathbb Z[1/2]/\mathbb Z\) whose Koopman representation has a nonzero continuous spectral component, although each individual group element has finite order. Continuous means non-atomic spectral measure on the compact dual group, not continuous time and not necessarily Lebesgue measure.',
     r'\citet[\S2, pp.~774--776]{stepin1966spectra} constructs precisely this group action on a circle times a two-point space. Its even subspace has discrete spectrum; its odd subspace has simple singular continuous spectrum. The paper was presented 23 November 1965 and published in 1966.',
     ['stepin1966spectra'],**{'class':'A'},literal_correctness='correct',reconstruction=r'The discrete topology on the group, joint spectral measure and distinction between continuous and absolutely continuous spectrum are made explicit.',present_status=r'As of November 2026: the announced construction and its singular-continuous refinement are established.')
save()

talk(44,'1965-04-12','A. A. Kirillov','P000072-P000074','Recovering convex bodies from central sections and shadows',
     r'Kirillov explains how central section areas of a symmetric body reduce to integration of an even function over great spheres. He then asks the analogous question for projection areas. The symmetry assumption is essential for both uniqueness statements.')
item(44,'P000074','theorem','Central section volumes determine an origin-symmetric body',
     r'The body is explicitly centrally symmetric. In three dimensions the notes replace it by \(\rho^2/2\) on \(S^2\) and invoke spherical harmonics to invert integration over great circles.',
     r'If \(K,L\subset\mathbb R^n\), \(n\ge2\), are origin-symmetric star bodies with positive continuous radial functions and \(\operatorname{vol}_{n-1}(K\cap u^\perp)=\operatorname{vol}_{n-1}(L\cap u^\perp)\) for all \(u\in S^{n-1}\), then \(K=L\). The section function is the spherical Radon transform of \(\rho_K^{n-1}/(n-1)\); the transform is injective on even functions. In \(n=3\), its spherical-harmonic multiplier at degree \(2j\) is \(2\pi P_{2j}(0)\ne0\), while odd degrees are killed.',
     r'The great-circle transform is classical Funk theory, originating before the seminar \citep{funk1913flachen}. The modern geometric formulation is documented by \citet[section functions and geometric tomography]{gardner2026tomography}. The original Funk publication metadata was checked; the general-dimensional formulation is a modern reconstruction.',
     ['funk1913flachen','gardner2026tomography'],publication_match='partial',verification='publisher metadata checked',reconstruction=r'Origin symmetry, continuous star bodies and the \((n-1)\)-dimensional measure generalize the explicit three-dimensional argument. Convexity is sufficient but not needed.')
item(44,'P000074','question','Do all projection areas determine a convex body?',
     r'The final question asks whether the areas of all shadows determine the convex body, followed only by \ru{Сводится}.',
     r'The brightness function \(b_K(u)=\operatorname{vol}_{n-1}(K\mid u^\perp)\) determines an origin-symmetric convex body \(K\subset\mathbb R^n\) uniquely among such bodies. Without a fixed center, translation is invisible; without central symmetry, uniqueness fails, already because \(K\) and \(-K\) have the same brightness.',
     r'Aleksandrov\textquotesingle s projection theorem dates to 1937; the precise symmetric uniqueness statement and date are given by \citet[Reconstruction from brightness functions; reference to Theorem~3.3.1]{gardner2026tomography}. This is an old theorem under the symmetry convention of the preceding paragraph, not an unresolved projection problem.',
     ['gardner2026tomography'],publication_match='exact',reconstruction=r'The inherited central-symmetry assumption is made explicit; if the last line is read independently for arbitrary convex bodies, its affirmative answer is false.',present_status=r'As of November 2026: affirmative with origin symmetry, negative as an unrestricted uniqueness claim.')
save()

talk(45,'1965-04-12','D. A. Kazhdan','P000072-P000074','Dvoretzky sections and an incompletely recorded Gromov method',
     r'Kazhdan reports a result of Gromov in the setting of Dvoretzky\textquotesingle s theorem. Sphere bundles over Grassmannians and disappearance of low spherical harmonics are proposed as a method. The exact additional hypothesis and representation-theoretic quantifiers are not preserved well enough to equate this with Gromov\textquotesingle s later Banach-conjecture paper.')
item(45,'P000073','theorem','Dvoretzky almost-Euclidean sections',
     r'For every \(\varepsilon,k\), a sufficiently high-dimensional centrally symmetric convex body has a \(k\)-dimensional section that is nearly a ball.',
     r'For every \(k\ge1\) and \(\varepsilon>0\), there is \(N(k,\varepsilon)\) such that every real normed space of dimension at least \(N\) has a \(k\)-dimensional subspace \(E\), a Euclidean norm \(|\cdot|\) on \(E\), and \(a>0\) with \(a|x|\le\|x\|\le(1+\varepsilon)a|x|\) for all \(x\in E\). The corresponding ellipsoid comparison is affine, not a demand for a round section in an arbitrarily fixed ambient metric.',
     r'Dvoretzky\textquotesingle s result appeared in the proceedings of the 1960 Jerusalem symposium, published in 1961. \citet[p.~297, stated theorem]{figiel1976dvoretzky} gives a later short proof and identifies that original publication.',
     ['dvoretzky1961convex','figiel1976dvoretzky'],literal_correctness='correct with missing hypotheses',reconstruction=r'The norm comparison fixes the quantitative meaning of nearly a ball and allows a suitable Euclidean structure.')
item(45,'P000073','method','A sphere-bundle and low-harmonic vanishing proposal',
     r'The fiber consists of a unit vector in a \(k\)-plane. The notes claim that, for large \(n\), some fiber kills the first \(\ell\) nonconstant spherical components, then state a broader unitary-representation version. A condition on outer-to-inner radii is left unfinished; weaker and stronger appear in adjacent comments.',
     r'The incidence space \(M_{n,k}=\{(E,v):E\in G_k(\mathbb R^n),v\in E,|v|=1\}\) has fiber \(S^{k-1}\). A precise possible question concerns simultaneous vanishing of specified nonconstant harmonic projections of the restriction of a norm to one fiber. The notebook does not specify the representation, parity, regularity, dimension bounds or extra convex-body condition needed to turn its universal sentence into a theorem.',
     r'\citet[Theorem~1]{gromov1967banach}, received September 1966 and published 1967, proves results on normed spaces whose subspaces are mutually isometric. Its theorem is not the exact harmonic-vanishing assertion recorded here. Searches of the paper and the Dvoretzky/Grassmannian literature did not establish an exact match.',
     ['gromov1967banach'],**{'class':'F'},literal_correctness='not determinable',publication_match='thematic only',confidence='low',
     reconstruction=r'The corrected fiber dimension is certain. A conjectural completion of the harmonic assertion would be editorial invention and is not supplied.',present_status=r'As of November 2026: the program is recognizable, but this particular theorem announcement remains unidentified; no claim of an orphan open problem is made.')
save()

talk(46,'1965-04-12','R. A. Minlos','P000072-P000075','Gaussian Hermitian matrices, Brownian motion and angles',
     r'The actual Minlos fragment is very short: Gaussian entries in a Hermitian matrix, Brownian motion, and a question about angles between subspaces. The modern interpretations are supplied explicitly as reconstructions, without attributing detailed stochastic equations to the handwriting.')
item(46,'P000073','method','Hermitian matrix Brownian motion and eigenvalue diffusion',
     r'The notes say only that the Hermitian matrix entries are Gaussian random variables and then \ru{Брауновское дв-ние}.',
     r'A standard realization takes independent real Brownian diagonal entries of variance \(dt\) and independent complex off-diagonal entries with real and imaginary variances \(dt/2\), reflected by Hermitian symmetry. Starting with distinct eigenvalues, its eigenvalues satisfy \(d\lambda_i=dB_i+\sum_{j\ne i}(\lambda_i-\lambda_j)^{-1}dt\) up to, and in fact without, collision. Other entry normalizations rescale time.',
     r'Dyson\textquotesingle s Brownian-motion model was published in 1962 \citep{dyson1962brownian}. The title and metadata match this interpretation, but the short fragment itself does not distinguish free matrix Brownian motion from a Gaussian stationary Ornstein--Uhlenbeck variant.',
     ['dyson1962brownian'],publication_match='partial',verification='indirect',confidence='medium',reconstruction=r'The independent increments, variances and stochastic equation are the modern reconstruction. A single Gaussian matrix does not determine a time process.')
item(46,'P000073','question','Angles between two k-dimensional subspaces',
     r'The question is simply what an angle between two \(k\)-dimensional subspaces in \(n\) dimensions means.',
     r'For subspaces \(E,F\) of a Euclidean or complex Hermitian space, with orthonormal column matrices \(Q_E,Q_F\), the singular values of \(Q_E^*Q_F\) are \(\cos\theta_1,\ldots,\cos\theta_r\), where \(r=\min(\dim E,\dim F)\) and \(0\le\theta_1\le\cdots\le\theta_r\le\pi/2\). These principal angles, including forced zeros from intersections, describe the relative position up to ambient isometry.',
     r'The theory goes back to \citet[\S\S IV--V; introduction, pp.~104--105]{jordan1875geometrie}, presented in May 1875. The singular-value expression is modern notation for this established collection of invariants.',
     ['jordan1875geometrie'],literal_correctness='correct',reconstruction=r'The notes ask for an angle; the answer is generally a list of principal angles. The complex version and matrix expression are added for precision.')
save()

talk(47,'1965-04-19','L. D. Faddeev','P000073-P000077','Characteristic determinants, Jost functions and regularized traces',
     r'Faddeev moves from a finite-interval Sturm--Liouville characteristic function to half-line and whole-line Jost determinants, then to contour trace identities. The notes mix exact identities with formal diagonal-kernel reasoning. A final Gelfand question asks when traces of commutators vanish.')
item(47,'P000074','construction','Finite-interval characteristic function and resolvent trace',
     r'For \(L=-d^2/dx^2+q\) on \([0,\pi]\) with Neumann ends, \(\psi(0,\lambda)=1\), \(\psi_x(0,\lambda)=0\), and \(w(\lambda)=\psi_x(\pi,\lambda)\). The finite-matrix identity \(d\log w/d\lambda=-\operatorname{Tr}(L-\lambda)^{-1}\) is proposed.',
     r'For real \(q\in L^1(0,\pi)\) and the self-adjoint Neumann realization, \(w\) is entire, with zeros exactly the simple eigenvalues. Outside the spectrum, \(w^{\prime}(\lambda)/w(\lambda)=-\operatorname{Tr}(L-\lambda)^{-1}\). The derivative on \(w\) is with respect to \(\lambda\); the derivative on \(\psi\) is spatial. Multiplying \(w\) by a nonzero constant leaves the identity unchanged.',
     r'This is classical one-dimensional spectral theory. The determinant-to-solution method belongs to the pre-seminar scattering and inverse-spectral framework of \citet[\S\S1--2]{faddeev1959inverse}; the finite-interval formula itself follows from the Green kernel and Lagrange identity. It is not a newly announced 1965 result.',
     ['faddeev1959inverse'],publication_match='partial',reconstruction=r'Integrability, real potential, operator domain and the two different derivatives are made explicit.')
item(47,'P000074-P000075','construction','Half-line Jost function as a relative determinant',
     r'On the half-line, with \(y(0)=0\) and rapidly decaying \(q\), the resolvent has no ordinary trace. A free part is subtracted; the outgoing solution satisfies \(f(x,k)\sim e^{ikx}\), and \(W(\lambda)=f(0,\sqrt\lambda)\).',
     r'For real \(q\) with \(\int_0^\infty(1+x)|q(x)|\,dx<\infty\), take the Dirichlet Schrödinger operator \(H\), free operator \(H_0\), and \(k^2=z\) with \(\operatorname{Im}k>0\). The normalized perturbation determinant is the Jost value \(D(z)=f(0,k)\); off both spectra, \(-d\log D/dz=\operatorname{Tr}((H-z)^{-1}-(H_0-z)^{-1})\). The difference, not the individual resolvent, is trace class.',
     r'The Jost solutions are treated by \citet[\S1 and \S6]{faddeev1959inverse}; an explicit Fredholm-determinant equality under even weaker \(L^1\) conditions is \citet[Theorem~1.1]{gesztesy2007jost}. The latter is a checked modern formulation, not the first appearance of the method.',
     ['faddeev1959inverse','gesztesy2007jost'],reconstruction=r'The relative normalization \(D=1\) for \(q=0\) and a sufficient short-range hypothesis are supplied. The scribbled diagonal asymptotic alone does not justify trace class.')
item(47,'P000075','remark','Resolvent sheets and free Green kernels',
     r'The notes discuss square-root branching in one dimension and logarithmic branching in two, and say one must leave the Hilbert-space setting to see a multivalued resolvent.',
     r'The bounded-operator resolvent \((H-z)^{-1}\) is single-valued and analytic on its resolvent set. For the free one-dimensional operator, its outgoing kernel is \(i e^{ik|x-y|}/(2k)\), \(k^2=z,\operatorname{Im}k>0\), so the kernel has a continuation in the square-root parameter. In two dimensions the outgoing Hankel kernel has logarithmic branching. Continuation across continuous spectrum requires specified weighted spaces or compactly supported test functions.',
     r'This interpretation agrees with the analytic scattering framework in \citet[\S\S1--2]{faddeev1959inverse}. It corrects a possible literal reading that an abstract Hilbert-space resolvent is multivalued on its ordinary domain.',
     ['faddeev1959inverse'],publication_match='partial',reconstruction=r'The distinction between the physical resolvent and continued kernels is essential; no general meromorphic continuation is asserted for every decaying potential.')
item(47,'P000075','construction','Whole-line Jost Wronskian',
     r'Two solutions behave like \(e^{ikx}\) at plus infinity and \(e^{-ikx}\) at minus infinity. Their Wronskian \(f_1^{\prime} f_2-f_1 f_2^{\prime}\) is called the determinant.',
     r'For real short-range \(q\) on \(\mathbb R\), let \(f_\pm(x,k)\sim e^{\pm ikx}\) at \(\pm\infty\), with \(\operatorname{Im}k>0\). The Wronskian \(W(k)=f_+^{\prime} f_- - f_+f_-^{\prime}\) is independent of \(x\); its zeros in the upper half-plane give bound states, with the usual threshold caveat at \(k=0\). The free Wronskian is \(2ik\), so a relative determinant uses \(W(k)/(2ik)\).',
     r'The construction belongs to the pre-1965 inverse-scattering theory; \citet[whole-line extensions in the introduction and supplementary remarks]{faddeev1959inverse} distinguishes these extensions from the main half-line problem. The unnormalized Wronskian is a characteristic function, not automatically a normalized Fredholm determinant.',
     ['faddeev1959inverse'],publication_match='partial',reconstruction=r'The short-range assumption may be taken as \(\int_{\mathbb R}(1+|x|)|q|<\infty\). The normalization and threshold exception are editorial additions.')
item(47,'P000075-P000076','method','Argument principle and analytically regularized spectral sums',
     r'The notes integrate \(h(\lambda)W^{\prime}(\lambda)/W(\lambda)\), deform the contour, and use \(h=\lambda^s\). The real-axis expression is followed by the annotation that the integral is a jump.',
     r'If \(W\) is meromorphic and nonzero on a closed contour and \(h\) is analytic inside it, \((2\pi i)^{-1}\oint hW^{\prime}/W\) equals the zero sum minus the pole sum, with multiplicities. A deformation onto a cut must retain both boundary values, its orientation and the factor \((2\pi i)^{-1}\). For spectral zeta or trace identities, convergence, subtraction of asymptotic terms and continuation must be proved separately.',
     r'The singular Sturm--Liouville trace formulas of \citet[pp.~13--16]{buslaevfaddeev1960traces} are a pre-seminar publication on this line. The notebook\textquotesingle s bare real-axis equality is shorthand for a contour-jump expression, not a universal ordinary improper integral identity.',
     ['buslaevfaddeev1960traces'],verification='publisher metadata checked',publication_match='partial',reconstruction=r'The argument-principle statement is exact; its application to an unspecified spectral determinant and branch of \(\lambda^s\) remains conditional.')
item(47,'P000076','claim','An unidentified boundary term in a Neumann regularized trace',
     r'The scan reads \(\sum_n(\lambda_n-n^2-c_0)=\tfrac14(y^{\prime}(0)-y^{\prime}(\pi))\). No function \(y\) on that right side is defined.',
     r'A standard comparison, for a sufficiently smooth real potential and Neumann eigenvalues numbered \(\lambda_0,\lambda_1,\ldots\), is \(\sum_{n=0}^\infty(\lambda_n-n^2-\bar q)=(q(0)+q(\pi))/4-\bar q/2\), where \(\bar q=\pi^{-1}\int_0^\pi q\). This is a different, specified statement; it cannot identify the written \(y^{\prime}\)-difference without an additional definition.',
     r'The Gelfand--Levitan trace identity dates to 1953, followed by Gelfand\textquotesingle s 1956 treatment \citep{gelfand1956identities}. The recorded boundary expression is therefore classified as an unidentified or corrupted instance of established trace theory, not a new spectral formula.',
     ['gelfand1956identities'],**{'class':'F'},literal_correctness='not determinable',publication_match='thematic only',verification='publisher metadata checked',confidence='low',reconstruction=r'The comparison formula is supplied to expose the ambiguity; it is not silently substituted into the transcription.',present_status=r'As of November 2026: the regularized-trace theory is established, but this exact boundary expression cannot be recovered from the notes.')
item(47,'P000076','method','Formal diagonal kernels and boundary contributions',
     r'The distributional kernel \(-\delta^{\prime\prime}(x-y)+q(x)\delta(x-y)\) is restricted formally to the diagonal. The notes write \(\delta(0)=0\), then discuss a boundary coefficient \(1/4\).',
     r'The distribution \(\delta(x-y)\) has no pointwise diagonal value \(\delta(0)\), and multiplication by a nonzero potential is not trace class on \(L^2\). A valid regularized trace must first specify a spectral, heat-kernel or resolvent subtraction and account for its endpoint terms. The displayed manipulations are heuristic motivation, not legitimate distributional equalities.',
     r'The endpoint effects belong to established regularized-trace formulas \citep{gelfand1956identities,buslaevfaddeev1960traces}. Their rigorous existence does not validate the intermediate assertion \(\delta(0)=0\).',
     ['gelfand1956identities','buslaevfaddeev1960traces'],literal_correctness='false as written',publication_match='partial',verification='publisher metadata checked',reconstruction=r'The source\textquotesingle s distinction between periodic and endpoint problems is retained as motivation, while the regularization is not invented.')
item(47,'P000076','problem','When does a commutator have trace zero?',
     r'Gelfand writes \(\operatorname{Sp}(AB-BA)=0\) and labels it a problem, without operator-ideal assumptions.',
     r'For bounded operators on a Hilbert space, \(\operatorname{Tr}(AB)=\operatorname{Tr}(BA)\) when both products are trace class (in particular if one factor is trace class). Merely requiring \([A,B]\) to be trace class is insufficient: for the unilateral shift \(S\) on \(\ell^2(\mathbb N_0)\), \([S^*,S]=P_{e_0}\) has trace one.',
     r'The question depends completely on the trace domain. Nonzero traces of trace-class commutators became a substantial theory; \citet[Introduction]{heltonhowe1975traces} develops trace formulas for almost commuting operators and relates them to symbols and index theory. This is a later development, not evidence for the unrestricted zero-trace assertion.',
     ['heltonhowe1975traces'],**{'class':'B'},literal_correctness='correct with missing hypotheses',publication_match='partial',problem='GP-1964-S02',reconstruction=r'The two distinct hypotheses are separated. The rank-one shift example is an explicit diagnosis of the unrestricted formulation.',present_status=r'As of November 2026: vanishing is established in the standard trace-cyclicity domain and false under the weaker trace-class-commutator assumption.')
problem('GP-1964-S02','Trace of a commutator',r'Under what hypotheses on bounded \(A,B\) and the trace is \(\operatorname{Tr}[A,B]=0\)?',
        ['1964-47.8'],r'As of November 2026: both products trace class suffice; trace class of the commutator alone does not, as \([S^*,S]\) shows. Later trace formulas treat the nonvanishing case.',['heltonhowe1975traces'])
save()

talk(48,'1965-04-19','S. G. Gindikin','P000075-P000080','Cauchy--Weil formulas and holomorphic Radon transforms',
     r'Gindikin begins with the product Cauchy formula and analytic polyhedra, introduces Hefer decompositions and skeleton integrals, then proposes a continuous family of defining functions. The final linear case connects directly to his 1965 holomorphic Radon-transform note, announced to the Moscow Mathematical Society in February.')
item(48,'P000076-P000077','construction','Product Cauchy formula and analytic polyhedra',
     r'A bicylinder \(D_z\times D_w\) has the iterated Cauchy formula. Weil domains are cut out by holomorphic \(\chi_i(z,w)\in D_i\).',
     r'If \(D_1,D_2\subset\mathbb C\) have piecewise smooth positively oriented boundaries and \(f\) is holomorphic near \(\overline{D_1\times D_2}\), then \(f(z,w)=(2\pi i)^{-2}\int_{\partial D_1\times\partial D_2}f(\zeta,\eta)\,d\zeta\wedge d\eta/((\zeta-z)(\eta-w))\). More general analytic polyhedra are relatively compact sets defined by finitely many holomorphic inequalities. Two defining functions are genuine global coordinates only with an injective biholomorphic change of variables; otherwise multiplicities matter.',
     r'The product formula is classical, and the polyhedral extension is explained in the pre-seminar work \citet[\S17 and Corollary~18.2]{norguet1961formes}. The notes are expository at this stage.',
     ['norguet1961formes'],reconstruction=r'Boundary regularity, holomorphy near closure and the coordinate-map caveat are supplied.')
item(48,'P000077','theorem','Hefer holomorphic difference decomposition',
     r'The displayed lemma expresses \(f(z,w)-f(\zeta,\eta)\) as \((z-\zeta)P+(w-\eta)Q\), with holomorphic coefficients.',
     r'If \(D\subset\mathbb C^n\) is a domain of holomorphy and \(f\in\mathcal O(D)\), there exist \(H_j\in\mathcal O(D\times D)\) such that \(f(z)-f(\zeta)=\sum_j(z_j-\zeta_j)H_j(z,\zeta)\). On a convex domain one may take \(H_j=\int_0^1\partial_j f(\zeta+t(z-\zeta))\,dt\); the global Stein-domain statement uses holomorphic division along the diagonal.',
     r'\citet{hefer1950zerlegung} published the decomposition in 1950. The use and existence of these coefficients for domains of holomorphy are also stated in the opened \citet[p.~78, following Corollary~18.2]{norguet1961formes}.',
     ['hefer1950zerlegung','norguet1961formes'],reconstruction=r'The domain-of-holomorphy hypothesis is essential to the global assertion. The convex-domain integral is a transparent special-case realization.')
item(48,'P000077-P000078','theorem','Cauchy--Weil representation on the distinguished boundary',
     r'The notes sum over pairs of boundary faces, with a determinant of Hefer coefficients divided by two defining-function differences. The indices in the written kernel are incomplete.',
     r'For a relatively compact analytic polyhedron \(P=\{|\chi_j|<1\}\subset D\subset\mathbb C^2\), with regular transverse boundary faces and \(D\) a domain of holomorphy, choose \(\chi_i(\zeta)-\chi_i(z)=\sum_{a=1}^2(\zeta_a-z_a)H_{ia}(\zeta,z)\). With the standard induced orientations on \(\Gamma_{ij}=\{|\chi_i|=|\chi_j|=1\}\cap\overline P\), a function holomorphic near \(\overline P\) has the Cauchy--Weil representation \((2\pi i)^{-2}\sum_{i<j}\int_{\Gamma_{ij}} f(\zeta)\det(H_{ia},H_{ja})\,d\zeta_1\wedge d\zeta_2/((\chi_i(\zeta)-\chi_i(z))(\chi_j(\zeta)-\chi_j(z)))\).',
     r'The exact architecture of this kernel is already in \citet[\S17; Corollary~18.2]{norguet1961formes}, following Weil and Hefer. The construction is known before the 1965 seminar.',
     ['norguet1961formes','hefer1950zerlegung'],reconstruction=r'The determinant notation means the determinant of the two rows \((H_{i1},H_{i2})\), \((H_{j1},H_{j2})\); regularity and orientation are supplied. This is not a literal reproduction of the notebook\textquotesingle s mixed indices.')
item(48,'P000078','method','Polyhedral approximation and decomposition by face integrals',
     r'The notes say that domains of holomorphy can be approximated by Weil domains and that the formula decomposes a holomorphic function into terms extending to larger regions.',
     r'In a Stein domain, holomorphically convex compact sets admit relatively compact analytic-polyhedron neighborhoods. In a Cauchy--Weil representation, each face integral is holomorphic in any parameter region on which its coefficient functions are holomorphic and its denominator stays nonzero uniformly on the integration cycle. This gives controlled local extension/decomposition; it does not imply that every holomorphic function extends beyond its domain of holomorphy.',
     r'The polyhedral and ideal-theoretic foundations precede the seminar \citep{cartan1950ideaux}; \citet[Corollary~18.2]{norguet1961formes} provides the representation used here. The separate extensions of summands must not be confused with extension of their total across every boundary point.',
     ['cartan1950ideaux','norguet1961formes'],publication_match='partial',reconstruction=r'The relevant compact-set and nonvanishing conditions are the precise reconstruction of the broad approximation sentence.')
item(48,'P000078','method','A continuous family of Weil defining functions',
     r'The finite \(\chi_i\) are replaced by \(\chi(\alpha,z,w)\); a kernel containing \(P_1\partial_\alpha P_2-P_2\partial_\alpha P_1\) is sketched.',
     r'The fragment proposes a continuous-parameter analogue of the Cauchy--Weil sum. It does not fix the parameter cycle, differentiability in \(\alpha\), the integration manifold, denominator order or orientations needed for an integral representation theorem.',
     r'Integral formulas with continuously varying complex hyperplanes are part of Gindikin\textquotesingle s work, including \citet[formula~(2)]{gindikin1965radon}. That paper identifies the next, linear example; it does not justify every symbol in this more general unfinished kernel. Searches did not recover an exact formula with all the manuscript\textquotesingle s conventions.',
     ['gindikin1965radon'],**{'class':'F'},literal_correctness='not determinable',publication_match='thematic only',confidence='low',reconstruction=r'No missing denominator power or integration cycle is guessed.',present_status=r'As of November 2026: a recognizable method with an incomplete exact statement; no independent open problem is inferred.')
item(48,'P000078','construction','Linear defining functions and the holomorphic Radon transform',
     r'For linear \(\chi\), the notes connect the formulas with Radon transforms, particularly in a tube over a convex domain.',
     r'Let \(T_\Omega=\mathbb R^n+i\Omega\), where \(\Omega\) is open convex and contains no affine line. Under the smooth strictly convex assumptions of the initial construction, take a holomorphic \(f\) with sufficient rapid decay in the real directions on each horizontal slice. Its integrals over real \((n-1)\)-planes in suitable complex hyperplanes form a holomorphic Radon transform, with inversion by the specified oriented boundary integral in Gindikin\textquotesingle s formula~(2). The result requires these geometric and decay conditions.',
     r'This is an exact match to \citet[pp.~237--239, formula~(2)]{gindikin1965radon}. The printed footnote records an announcement to the Moscow Mathematical Society on 23 February 1965, before this April seminar; the publication appeared in 1965. The article also discusses how its initial boundary regularity can be relaxed.',
     ['gindikin1965radon'],**{'class':'A'},reconstruction=r'The precise tube, rapid-decay hypothesis and initial boundary assumptions come from the paper, not from the shorthand notes.',present_status=r'As of November 2026: established published work, with pre-seminar circulation distinguished from publication.')
save()

talk(49,'1965-04-26','I. N. Bernstein','P000078-P000085','Čech complexes and derived sheaf cohomology',
     r'Bernstein reviews descent, constructs a Čech complex and maps under refinement, and explains why global sections need derived functors. The example of functions vanishing at two points of the projective line is useful and precise. The attribution of a failure of exactness to taking a direct limit is mathematically wrong and is corrected separately from the underlying cohomological construction.')
item(49,'P000079-P000080','definition','Review of sites, fiber products and sheaf descent',
     r'The opening diagrams repeat products over an object, pullback of a cover, and compatibility of sections on double overlaps.',
     r'For a site presented by covering families and the required fiber products, a sheaf of abelian groups is a contravariant functor satisfying the equalizer condition for every covering. Products in the slice represent overlaps; the universal property fixes all restriction maps used in the Čech complex.',
     r'This continues record~40 and follows the pre-seminar site formalism of SGA~4; see \citet[Exposé II]{sga4I1972} and \citet[Tags 00VH, 00VL]{stacks2026sites}.',
     ['sga4I1972','stacks2026sites'],literal_correctness='correct')
item(49,'P000080-P000081','construction','Čech cochains and the alternating differential',
     r'The terms are products of sections on multiple intersections, with alternating restriction maps; the notes show the first degrees and \(d^2=0\).',
     r'For a cover \(\mathcal U=(U_i\to X)\), set \(\check C^q(\mathcal U,F)=\prod_{i_0,\ldots,i_q}F(U_{i_0}\times_X\cdots\times_XU_{i_q})\). The differential is the alternating sum of pullbacks along omission maps. Simplicial identities imply \(d^2=0\), and \(\check H^0(\mathcal U,F)=F(X)\) for a sheaf.',
     r'This is classical Čech theory in the language of sites. The explicit construction and extension to complexes are given in \citet[Tags 01FP and 01GZ]{stacks2026cohomology}; the site version was part of the 1963--64 SGA program \citep{sga4I1972}.',
     ['stacks2026cohomology','sga4I1972'],literal_correctness='correct')
item(49,'P000081','construction','Refinement maps and direct-limit Čech cohomology',
     r'A refinement is assigned a map of cochain complexes; cohomology over all covers is then considered.',
     r'A chosen refinement map induces a cochain map in the opposite direction on Čech complexes. Two choices subordinate to the same refinement induce chain-homotopic maps, hence the same cohomology map. For ordinary open covers, direct-limit Čech cohomology is \(\check H^q(X,F)=\varinjlim_\mathcal U\check H^q(\mathcal U,F)\). On a site, one must use a specified refinement category and smallness convention.',
     r'The refinement construction is explicitly checked in \citet[Tag 01FP, Refinements]{stacks2026cohomology}. Passing to hypercovers gives derived sheaf cohomology on sites \citep[Tag 01GZ, Theorem~25.10.1]{stacks2026cohomology}.',
     ['stacks2026cohomology'],reconstruction=r'Independence of the chosen refinement and the size convention are supplied; the notes do not prove them.')
item(49,'P000081-P000082','claim','The direct-limit explanation of Čech exactness is false',
     r'The source suggests that a long exact sequence exists for each cover but can fail after the passage over refinements.',
     r'Filtered colimits of abelian groups are exact, so a compatible filtered system of long exact sequences remains exact. The actual issue is earlier: an epimorphism of sheaves need not be surjective on sections of an overlap, so a short exact sequence of sheaves need not give a short exact sequence of fixed-cover Čech complexes. In higher degree, ordinary Čech cohomology on an arbitrary site need not equal derived sheaf cohomology.',
     r'The derived-functor remedy was available before this talk in \citet{grothendieck1957tohoku}. The precise hypercover comparison is \citet[Tag 01GZ, Theorem~25.10.1]{stacks2026cohomology}. Neither result supports blaming a filtered direct limit for loss of exactness.',
     ['grothendieck1957tohoku','stacks2026cohomology'],literal_correctness='false as written',publication_match='partial',reconstruction=r'This separates the faithful source error from the correct motivation for derived functors.',present_status=r'As of November 2026: the exactness issue is settled under the stated category conventions; the manuscript explanation is false.')
item(49,'P000082','definition','Abelian sheaves, presheaves and exactness',
     r'The notes contrast a category of sheaves with one of presheaves and discuss failure of exactness for an inclusion or section functor. A subscript resembling \(p\) is not securely identified as a stalk.',
     r'Abelian presheaves form an abelian category with kernels and cokernels computed objectwise. Abelian sheaves also form an abelian category; their kernels are computed as presheaf kernels, while cokernels are obtained by sheafifying presheaf cokernels. The inclusion into presheaves is left exact and generally not right exact. On a topological space, exactness of sheaves is tested on stalks.',
     r'This is part of Grothendieck\textquotesingle s abelian-category foundation \citep{grothendieck1957tohoku}; site formulations appear in SGA~4 \citep[Exposé II]{sga4I1972}. The notebook must not be read as denying stalkwise exactness.',
     ['grothendieck1957tohoku','sga4I1972'],verification='publisher metadata checked',reconstruction=r'The ambiguous subscript is left unresolved; the three functors---inclusion, sections and stalk---are distinguished.')
item(49,'P000082','construction','The ideal sheaf of two points on the projective line',
     r'The example takes two points of \(\mathbb P^1\), functions vanishing there, and an exact sequence whose global sections are not right exact.',
     r'For distinct \(p,q\in\mathbb P^1_\mathbb C\), let \(J=\mathcal I_{\{p,q\}}\cong\mathcal O(-2)\). The exact sequence \(0\to J\to\mathcal O\to\mathbb C_p\oplus\mathbb C_q\to0\) gives \(H^0(J)=0\), \(H^0(\mathcal O)=\mathbb C\), and the diagonal map \(\mathbb C\to\mathbb C^2\), which is not onto. Its cokernel is \(H^1(J)\cong\mathbb C\), since \(H^1(\mathcal O)=0\).',
     r'The example concretely illustrates the derived-functor theory already established in \citet{grothendieck1957tohoku}. The line-bundle notation identifies the exact obstruction; it is not an open extension problem.',
     ['grothendieck1957tohoku'],verification='publisher metadata checked',literal_correctness='correct with missing hypotheses',reconstruction=r'The points are assumed distinct and the ground field complex, matching the holomorphic formulation. The cohomology calculation completes the source\textquotesingle s example.')
item(49,'P000082-P000083','construction','An incomplete differential-form exact sequence',
     r'A sequence beginning \(0\to C\to\Omega^0\to\Omega\to0\) is sketched without a secure definition of the final sheaf or differential.',
     r'On a smooth manifold, \(0\to\underline{\mathbb C}\to\mathcal A^0\xrightarrow{d}\mathcal Z^1\to0\) is locally exact, where \(\mathcal Z^1\) is the sheaf of closed smooth one-forms. The complete de Rham resolution instead continues through \(\mathcal A^1,\mathcal A^2,\ldots\). Replacing \(\mathcal Z^1\) by all one-forms and ending with zero is false in dimension greater than one.',
     r'The Poincaré-lemma/de Rham interpretation is standard pre-seminar material, but the notebook does not decide whether \(\Omega\) means closed forms, an image sheaf or something else. The exact sequence is therefore not identified beyond this possible reconstruction.',
     [],**{'class':'F'},literal_correctness='not determinable',publication_match='none found',verification='indirect',confidence='low',reconstruction=r'The smooth de Rham example is a possible precise repair, explicitly not a decipherment of the unspecified final symbol.',present_status=r'As of November 2026: the proposed reconstruction is classical; the literal abbreviated sequence remains underdetermined.')
item(49,'P000083','method','Derived functors of sections and cohomology presheaves',
     r'The final paragraph proposes right-derived functors of a left-exact functor from sheaves to presheaves, using injective resolutions to recover the long exact sequence.',
     r'For abelian sheaves on a site, choose an injective resolution \(F\to I^\bullet\). Then \(H^q(U,F)=H^q(I^\bullet(U))\), and \(U\mapsto H^q(U,F)\) is a cohomology presheaf. Global cohomology is the right-derived functor of \(\Gamma(X,-)\). A short exact sequence of sheaves yields the usual long exact cohomology sequence. The inclusion of sheaves into presheaves is a different left-exact functor, whose derived values encode these local section cohomologies.',
     r'Grothendieck\textquotesingle s 1957 paper established this derived-functor organization before the talk \citep{grothendieck1957tohoku}. \citet[Tags 01FP and 01GZ]{stacks2026cohomology} makes clear how Čech and hypercover constructions compare with it.',
     ['grothendieck1957tohoku','stacks2026cohomology'],reconstruction=r'Enough injectives, the precise functor and the distinction between a cohomology presheaf and a cohomology sheaf are stated explicitly.')
save()

talk(50,'1965-05-10','Paul R. Halmos; I. M. Gelfand; unidentified participant','P000083-P000090','Invariant subspaces, polynomial compactness, unicellular operators and Bishop operators',
     r'Halmos surveys invariant-subspace results and gives the elementary proof of the polynomially compact case. The ensuing questions concern invariant-subspace lattices, weighted shifts, a measure version of Volterra integration and Bishop operators. A final intervention sketches the Sz.-Nagy--Foiaş analytic model. The catalog envelope is preserved, but P000090 begins Kohn on 20 September 1965 and is outside this academic year and record.')
item(50,'P000084; P000088','problem','The invariant-subspace problem on complex Hilbert space',
     r'The notes explicitly require a closed invariant subspace different from zero and the whole complex Hilbert space. On P000088 this is reformulated as whether the lattice can consist only of \(\{0,H\}\).',
     r'For every bounded linear operator \(T\) on a separable infinite-dimensional complex Hilbert space \(H\), must there be a closed subspace \(M\) with \(0\ne M\ne H\) and \(TM\subseteq M\)? Equivalently, can every nonzero vector be cyclic for one such \(T\)?',
     r'The 1964 de Branges--Rovnyak announcement was retracted in 1965 \citep{debrangesrovnyak1964existence,debrangesrovnyak1965correction}; the author bibliography explicitly identifies the retraction. Later primary accounts still distinguish the Hilbert problem from Banach-space counterexamples \citep[Introduction]{chamizo2020bishop,behani2023bishop}. Targeted searches through 12 November 2026 found recent claimed solutions and new partial results, but no generally accepted solution was verified. Claims are not promoted to established theorems on the strength of a preprint abstract.',
     ['debrangesrovnyak1964existence','debrangesrovnyak1965correction','chamizo2020bishop','behani2023bishop','szczepanski2026chain'],**{'class':'C'},literal_correctness='correct',publication_match='exact',problem='GP-1964-02',confidence='high',
     present_status=r'As of 12 November 2026: no generally accepted solution was verified in the literature checked. This qualified status concerns bounded operators on complex infinite-dimensional Hilbert space, not arbitrary Banach spaces or special classes.',
     worth=r'Yes, as the central recognized problem, but an unrestricted attack is far beyond a bounded chapter development. The tractable work here is confined to the precisely specified Bishop family and finite-orbit certificates.')
item(50,'P000084','theorem','Normal and self-adjoint operators have invariant subspaces',
     r'The normal and Hermitian cases are described as known.',
     r'Every normal bounded operator on a complex Hilbert space of dimension greater than one has a nonzero proper closed invariant subspace. A nontrivial spectral projection gives a reducing subspace; when the operator is scalar, any one-dimensional subspace suffices. Self-adjoint operators are included.',
     r'This is classical spectral theory, already treated as established background in the contemporary polynomially compact discussion \citep[p.~433]{halmos1966polynomial}. It does not require compactness or an eigenvalue in the nonscalar continuous-spectrum case.',
     ['halmos1966polynomial'],publication_match='partial',literal_correctness='correct with missing hypotheses',reconstruction=r'The dimension restriction and the scalar exceptional argument prevent the shorthand from being applied to a one-dimensional space.')
item(50,'P000084','theorem','Compact operators and the Aronszajn--Smith theorem',
     r'Completely continuous operators are attributed to von Neumann, followed by Aronszajn and Smith.',
     r'Every compact bounded linear operator on an infinite-dimensional complex Banach space has a nonzero proper closed invariant subspace. In particular this holds on complex Hilbert space; for finite dimension greater than one, ordinary eigenvector theory supplies the result.',
     r'\citet{aronszajnsmith1954} published the Banach-space theorem in 1954. The later primary account \citet[Introduction]{chamizo2020bishop} explicitly records the earlier unpublished von Neumann Hilbert-space result. The accessible Aronszajn--Smith record verified publication metadata; the complete original proof was not read.',
     ['aronszajnsmith1954','chamizo2020bishop'],verification='publisher metadata checked',literal_correctness='correct with missing hypotheses')
item(50,'P000084','definition','Subnormality and the unilateral shift',
     r'Subnormal means having a normal extension on a larger Hilbert space. The unilateral shift becomes normal after negative-index basis vectors are added; finite-dimensional subnormal operators are normal.',
     r'An operator \(T\in B(H)\) is subnormal if \(H\) is an invariant subspace of a Hilbert space \(K\) for a normal \(N\in B(K)\), and \(T=N|_H\). The unilateral shift on \(\ell^2(\mathbb N_0)\) is the restriction of the bilateral unitary shift on \(\ell^2(\mathbb Z)\). Finite-dimensional subnormal operators are normal. Taking adjoints need not preserve subnormality.',
     r'This is the established Halmos--Bram theory. The definition and intrinsic positivity criteria are recalled and extended by \citet[p.~99]{lambert1984subnormal}; Bram\textquotesingle s original 1955 paper is identified in its bibliography \citep{bram1955subnormal}.',
     ['lambert1984subnormal','bram1955subnormal'],publication_match='partial',reconstruction=r'Invariance of the embedded space is essential: a compression of a normal operator to an arbitrary subspace would not be the stated notion.')
item(50,'P000084','problem','Invariant subspaces for subnormal operators',
     r'After defining subnormality, the notes say that its invariant-subspace question is still unsolved.',
     r'Does every subnormal bounded operator on a complex Hilbert space of dimension greater than one possess a nonzero proper closed invariant subspace? The answer is affirmative.',
     r'\citet[abstract and pp.~310--333]{brown1978subnormal} proved the affirmative result, published in September 1978 after receipt on 21 July 1978. The publisher abstract was opened and explicitly states this result; the full subscription article was not read. The 1965 unsolved label is historically appropriate but cannot be retained as a current status.',
     ['brown1978subnormal'],**{'class':'B'},verification='publisher metadata checked',literal_correctness='correct',present_status=r'As of November 2026: solved affirmatively by Brown in 1978; this special-class problem is distinct from item 1964-50.1.')
item(50,'P000084','claim','Hyponormality is necessary but not sufficient for subnormality',
     r'The overwritten qualification after \(T^*T-TT^*\ge0\) reads necessary and sufficient; the scan leaves the horizontal sign slightly ambiguous.',
     r'Subnormality implies hyponormality \(T^*T-TT^*\ge0\), but the converse is false. The bounded unilateral shift with weights \(1,1,2,2,\ldots\) is hyponormal since the weights are nondecreasing. If it were subnormal, its moment measure would have moments \(\gamma_0=\gamma_1=\gamma_2=1\), forcing concentration at \(1\), contrary to \(\gamma_3=4\).',
     r'The full Bram--Halmos positivity conditions involve all finite arrays of vectors and powers, not just the first commutator; see \citet[Introduction and criterion]{lambert1984subnormal}. The recorded biconditional is a faithful mathematical error. The explicit shift supplies a short diagnostic counterexample, independently of the uncertain overwritten punctuation.',
     ['lambert1984subnormal','bram1955subnormal'],literal_correctness='false as written',publication_match='partial',reconstruction=r'The minus sign is the mathematically coherent reading. The weighted-shift counterexample and moment argument are editorial verification; they are not attributed to the speaker.',present_status=r'As of November 2026: the single positivity condition is insufficient; complete intrinsic subnormality criteria are established.')
item(50,'P000084-P000087','theorem','Polynomially compact operators have invariant subspaces',
     r'The case \(T^2\) compact is attributed to Robinson and Bernstein using predicate calculus. Halmos then proves the general case \(p(T)\) compact for a nonzero polynomial.',
     r'If \(H\) is an infinite-dimensional complex Hilbert space, \(T\in B(H)\), and \(p\in\mathbb C[z]\setminus\{0\}\) has \(p(T)\) compact, then \(T\) has a nonzero proper closed invariant subspace. The case \(p(T)=0\) is included.',
     r'\citet[Theorem~1.1]{bernsteinrobinson1966} published the nonstandard-analysis proof in 1966; their paper was received 5 July 1964 and revised 10 December 1964. \citet[pp.~433--437]{halmos1966polynomial} gave the elementary proof, received 10 October 1964. Thus both arguments circulated before this May 1965 lecture although publication followed it. The coauthor is Allen R. Bernstein, not seminar participant I. N. Bernstein.',
     ['bernsteinrobinson1966','halmos1966polynomial'],**{'class':'A'},literal_correctness='correct with missing hypotheses',reconstruction=r'Infinite dimension and a nonzero polynomial are explicit. In finite dimension greater than one the conclusion is elementary; in dimension one it fails.',present_status=r'As of November 2026: established; the notebook is an early oral record of the subsequently published elementary proof.')
item(50,'P000084-P000085','method','Cyclic Hessenberg matrices and small subdiagonal products',
     r'Gram--Schmidt on \(e,Te,T^2e,\ldots\) gives a matrix with one nonzero subdiagonal. Products along its lowest diagonal tend to zero by compactness of \(p(T)\).',
     r'If one nonzero cyclic vector has linearly independent iterates, Gram--Schmidt gives \(a_{mn}=\langle Te_n,e_m\rangle=0\) for \(m>n+1\). For \(k\ge1\), \((T^k)_{n+k,n}=\prod_{j=1}^k a_{n+j,n+j-1}\). If \(p\) has degree \(k\), nonzero leading coefficient, and \(p(T)\) is compact, these products tend to zero, so some increasing subsequence of subdiagonal entries tends to zero.',
     r'This is the reduction on \citet[pp.~433--434]{halmos1966polynomial}. A noncyclic orbit closure or a finite dependence already yields an invariant subspace. P000085 reverses the matrix indices in one definition; maintaining the convention from P000084 repairs the argument.',
     ['halmos1966polynomial'],**{'class':'A'},literal_correctness='false as written',reconstruction=r'The leading coefficient, consistent row-column convention and exceptional finite-dimensional orbit are made explicit.')
item(50,'P000085-P000086','method','Almost invariant finite compressions and polynomials',
     r'The small subdiagonal entry is used to compress \(T\) to initial finite-dimensional spans. Bounded vector sequences are compared modulo norm convergence to zero, with a special warning about constant terms.',
     r'Let \(P_n\) be finite-rank orthogonal projections with \(P_n\to I\) strongly and \(\|(I-P_n)TP_n\|\to0\). For every polynomial \(p\) and bounded \(x_n\) with \(\|(I-P_n)x_n\|\to0\), one has \(\|p(T)x_n-p(P_nTP_n)x_n\|\to0\). On \(P_nH\), the compression admits a complete invariant flag.',
     r'The approximation lemma is in \citet[p.~435]{halmos1966polynomial}. The source\textquotesingle s two differently placed \(P_n\) factors explain its warning at exponent zero; dropping them silently would create a false formula for arbitrary bounded sequences.',
     ['halmos1966polynomial'],**{'class':'A'},literal_correctness='correct with missing hypotheses',reconstruction=r'The norm of the escaping corner, boundedness of the vector sequence, and asymptotic membership in \(P_nH\) are the exact sufficient hypotheses.')
item(50,'P000086-P000087','method','Adjacent flags and weak limits in the compactness argument',
     r'Two adjacent projections from each finite-dimensional invariant flag are chosen at a norm threshold. Their weak limits define spaces on which they converge strongly to the identity; compactness provides a nonzero limiting vector.',
     r'For adjacent projections \(Q_n^-\le Q_n^+\), with rank-one difference and asymptotically invariant ranges, choose weak-operator limits \(Q^\pm\). The subspaces \(M^\pm=\ker(I-Q^\pm)=\{x:Q_n^\pm x\to x\}\) are closed and invariant. The compact polynomial and a correct threshold selection give \(M^-\ne H\), \(M^+\ne0\); rank-one adjacency excludes \(M^-=0\) and \(M^+=H\) simultaneously.',
     r'This is the closing argument of \citet[pp.~435--437]{halmos1966polynomial}. Weak limits of projections need not be projections. The notebook\textquotesingle s missing terminal vector and conflicting threshold directions are not reproduced as a proof; the published selection supplies their precise repair.',
     ['halmos1966polynomial'],**{'class':'A'},literal_correctness='false as written',reconstruction=r'The weak limits are positive contractions. The mathematical mechanism is reconstructed from the exact publication; no unrecorded monotonicity of the displayed norms is assumed.')
item(50,'P000088','theorem','An entire function giving a compact operator reduces to a polynomial',
     r'The notes state that if \(p\) is entire and \(p(T)\) compact, the polynomial result immediately gives an invariant subspace.',
     r'Let \(f\) be a nonzero entire function and \(T\in B(H)\) on an infinite-dimensional complex Hilbert space. If \(f(T)\) is compact, factor the finitely many zeros in a compact neighborhood of \(\sigma(T)\): \(f=p g\), where \(p\) is polynomial and \(g(T)\) is invertible. Then \(p(T)=g(T)^{-1}f(T)\) is compact, so the polynomial theorem applies.',
     r'This functional-calculus consequence uses the theorem of \citet{bernsteinrobinson1966,halmos1966polynomial}. The zero entire function must be excluded: allowing it would make the assumption hold for every bounded operator and simply restate the unsolved general problem.',
     ['bernsteinrobinson1966','halmos1966polynomial'],**{'class':'A'},publication_match='partial',literal_correctness='correct with missing hypotheses',reconstruction=r'The finite-zero factorization takes place near the compact spectrum, not over all of \(\mathbb C\). The analytic functional calculus supplies invertibility of the zero-free factor.')
item(50,'P000088','claim','The de Branges--Rovnyak compact-defect assertion',
     r'After noting the error in their general announcement, the manuscript claims a consequence under \(\|T\|<1\) or \(\|T\|\le1\) and compact \(I-T^*T\). The scan does not securely distinguish the two norm signs.',
     r'If \(\|T\|<1\), then \(I-T^*T\ge(1-\|T\|^2)I\); on infinite-dimensional \(H\), this operator cannot be compact. The strict reading is vacuous. The weak reading is a materially different assertion about a contraction with compact defect and requires a separate theorem; it is not certified by the retracted general proof.',
     r'Rovnyak\textquotesingle s author bibliography identifies the 1964 announcement and its 1965 retraction \citep{debrangesrovnyak1964existence,debrangesrovnyak1965correction}. It does not verify the exact compact-defect corollary. The general retraction and the unresolved norm sign are kept separate.',
     ['debrangesrovnyak1964existence','debrangesrovnyak1965correction'],**{'class':'F'},literal_correctness='not determinable',publication_match='thematic only',verification='publisher metadata checked',confidence='low',reconstruction=r'The coercivity argument diagnoses the strict reading without choosing an uncertain glyph. No current open problem is manufactured from the weak reading.',present_status=r'As of November 2026: the strict hypothesis is impossible in the intended infinite-dimensional setting; an exact source for the non-strict compact-defect assertion was not verified.')
item(50,'P000088','remark','A small imaginary part and unspecified invariant-subspace criteria',
     r'Sakhnovich, Livshits and Brodskii are named for \(A+iB\), with \(A\) self-adjoint and \(B\) small in some sense, for example nuclear.',
     r'The fragment indicates invariant-subspace criteria for operators with a small imaginary part, but does not state whether \(B\) is self-adjoint, positive, trace class, finite rank, or subject to spectral or dissipativity hypotheses. Those choices lead to different theorems.',
     r'The authors and topic identify a substantial pre-existing theory of non-self-adjoint operators, but a theorem with the recorded incomplete hypotheses was not established from an opened primary source. The names alone do not justify treating every trace-class imaginary perturbation as covered by a specific theorem.',
     [],**{'class':'F'},literal_correctness='not determinable',publication_match='none found',verification='unresolved lead',confidence='low',present_status=r'As of November 2026: insufficiently specified for an individual theorem-level fate; retained as a historical reference to a research direction.')
item(50,'P000088','theorem','Contractions with neither forward nor adjoint powers strongly stable',
     r'Both arrows in \(T^n\not\to0\), \((T^*)^n\not\to0\) are crossed; the norm condition is \(\|T\|\le1\). The result is attributed to Nagy and Foias.',
     r'If \(T\) is a contraction on a complex Hilbert space with \(\dim H>1\), and neither \(T^n\) nor \((T^*)^n\) converges strongly to zero, then \(T\) has a nonzero proper closed invariant subspace.',
     r'This is exactly \citet[\S6, Theorem~3 and Remark~(ii), p.~314]{sznagyfoias1964ix}; footnote~29 handles the unitary case and dimension restriction. The paper was received 1 May 1964 and published in 1964. Its 1965 correction explicitly says that the error in Proposition~5.4 does not affect this theorem or its proof \citep[p.~193]{sznagyfoias1965corrections}.',
     ['sznagyfoias1964ix','sznagyfoias1965corrections'],literal_correctness='correct with missing hypotheses',reconstruction=r'Strong nonconvergence means failure for at least one vector for each sequence; it does not require every vector to have a nonzero limiting norm.')
item(50,'P000088','construction','Donoghue lattice of finite initial spans',
     r'The lattice \(\{0,1,2,\ldots,\infty\}\) is attributed to Donoghue (1957). The upper-diagonal weights begin \(1/2,1/4\), followed by an uncertain \(1/8\) or \(1/6\).',
     r'On \(\ell^2(\mathbb N_0)\), the backward weighted shift \(Be_0=0\), \(Be_n=2^{-n}e_{n-1}\) for \(n\ge1\) is compact and quasinilpotent, and its closed invariant subspaces are exactly \(0\), \(\operatorname{span}\{e_0,\ldots,e_{m-1}\}\) for \(m\ge1\), and the whole space.',
     r'\citet[Examples~1--2, pp.~1031--1033]{donoghue1957lattice} proves the forward-shift tail lattice and its adjoint version. A scalar multiple yields the notebook\textquotesingle s normalization. The 1957 date is correct; the paper was received 25 June 1956.',
     ['donoghue1957lattice'],literal_correctness='correct with missing hypotheses',reconstruction=r'The geometric weight sequence is a literature-supported interpretation, not a confident decipherment of its overwritten third entry. The endpoints are the zero and whole subspaces.')
item(50,'P000088','problem','Weight conditions for the Donoghue invariant-subspace lattice',
     r'The exact conditions on the superdiagonal numbers that give precisely the Donoghue chain are said to be unknown.',
     r'For a bounded sequence of nonzero weights \((w_n)_{n\ge1}\), determine criteria expressed in the weights for the backward shift \(Be_n=w_ne_{n-1}\), \(Be_0=0\), to have only finite initial spans and the whole space as closed invariant subspaces. Equivalently its forward-shift adjoint must be unicellular, with only coordinate tails.',
     r'\citet[\S1 and Lemmas~2.1--2.2]{harrison1971unicellularity} states this weight-criterion problem and develops sufficient conditions. \citet[abstract]{yakubovich1985weighted} proves unicellularity when the positive moduli decrease monotonically to zero, on \(\ell^p\), \(1\le p<\infty\); the Hilbert adjoint gives the backward version. These are major extensions, but do not settle a weight-only necessary-and-sufficient characterization for arbitrary nonmonotone bounded weights.',
     ['donoghue1957lattice','harrison1971unicellularity','yakubovich1985weighted'],**{'class':'C'},publication_match='partial',literal_correctness='correct',problem='GP-1964-S03',confidence='medium',
     present_status=r'As of November 2026: many sufficient classes are established; a general explicit weight-only characterization was not verified in the checked literature. This is a qualified unresolved classification, not a claim that monotone weights remain untreated.',
     worth=r'Yes, for a restricted computable weight family or a new sharp sufficient criterion. The unrestricted classification needs more than repackaging cyclicity as an equivalent condition; no general solution or novelty claim is made here.')
item(50,'P000088','question','An invariant-subspace chain indexed by all integers',
     r'The question whether there is an operator with the structure of all integers is followed by unknown.',
     r'A precise repaired question asks for a bounded operator on a separable Hilbert space whose invariant-subspace lattice is \(\{0,H\}\cup\{M_n:n\in\mathbb Z\}\), with strict inclusions \(M_n\subset M_{n+1}\), intersection zero and dense union. The literal ordered set \(\mathbb Z\) alone cannot be a full invariant-subspace lattice because it lacks the required least and greatest elements.',
     r'The question belongs to the theory of unicellular operators and bilateral weighted shifts. The checked Donoghue and Harrison papers treat unilateral chains and do not themselves establish this exact bilateral construction \citep{donoghue1957lattice,harrison1971unicellularity}. An exact primary construction or obstruction was not yet verified; this limitation is not evidence that the repaired question remains open.',
     ['donoghue1957lattice','harrison1971unicellularity'],**{'class':'F'},literal_correctness='correct with missing hypotheses',publication_match='thematic only',verification='unresolved lead',confidence='low',present_status=r'As of November 2026: the intended completed order type is clear, but the exact later fate was not verified. No C/D open-problem designation is assigned on a failed literature match.')
item(50,'P000088','construction','Volterra integration and a continuous chain',
     r'The interval \([0,1]\) is represented by \((Vf)(x)=\int_0^x f(y)\,dy\), with the result dated to the 1950s.',
     r'On \(L^2(0,1)\), the nonzero proper closed invariant subspaces of the Volterra operator are precisely \(M_a=\{f:f=0\ \text{a.e. on }(0,a)\}\), \(0<a<1\). With \(M_0=H\), \(M_1=0\), these form a continuous totally ordered lattice, reverse-ordered by \(a\), hence order-isomorphic to \([0,1]\).',
     r'\citet[Example~3, pp.~1033--1034]{donoghue1957lattice} gives the theorem and proof, including \(L^p\), \(1\le p<\infty\), and an appropriate continuous-function version. The existence assertion was established well before the seminar.',
     ['donoghue1957lattice'],literal_correctness='correct',reconstruction=r'The direction of inclusion and the endpoint subspaces are supplied; the Hilbert case is \(p=2\).')
item(50,'P000088','conjecture','A measure-Volterra lattice is not determined by the support as written',
     r'A measure on the whole real line is drawn, \((Af)(x)=\int_0^x f(y)\,d\mu(y)\), and the lattice is conjectured to be isomorphic to \(\operatorname{supp}\mu\). The normalization resembles total mass one but is not secure.',
     r'The literal conjecture is false even for an atomless probability measure: take \(d\mu=\tfrac12\mathbf1_{[-1,1]}dx\), interpreting the integral from zero in the oriented sense for negative \(x\). The subspaces supported on \([-1,0]\) and \([0,1]\) are closed, nonzero, proper and invariant, since every integration interval stays on its side of zero. They are incomparable, whereas \(\operatorname{supp}\mu=[-1,1]\) is linearly ordered.',
     r'A repaired one-sided statement is classical: a positive continuous probability density on \([a,b]\), with lower integration limit \(a\), is transformed by its cumulative distribution into ordinary Volterra integration. The latter lattice is given by \citet[Example~3]{donoghue1957lattice}. This does not validate the two-sided source formula, and no general unresolved measure classification is inferred from that false conjecture.',
     ['donoghue1957lattice'],literal_correctness='false as written',publication_match='partial',reconstruction=r'The counterexample has no atoms, so endpoint conventions cannot explain away the failure. Its total mass is one. The boundedness of this particular integral operator follows directly from Cauchy--Schwarz.',present_status=r'As of November 2026: false under the literal two-sided formulation; the indicated regular one-sided repair is established.',development='annotated')
item(50,'P000089','conjecture','Bishop operators as possible invariant-subspace counterexamples',
     r'The weighted composition operator is specialized to \(Tf(x)=x f(x+\alpha\bmod1)\), irrational \(\alpha\). It is proposed as having no invariant subspace, equivalently every vector cyclic.',
     r'For irrational \(\alpha\in(0,1)\), let \(T_\alpha f(x)=x f(\{x+\alpha\})\) on complex \(L^2(0,1)\). Does every such operator have a nonzero proper closed invariant subspace? The source\textquotesingle s contrary suggestion is false for many parameters, but the universal affirmative question is a distinct remaining problem. The equivalence with cyclicity requires every nonzero vector, not the zero vector.',
     r'Davie\textquotesingle s 1974 theorem covers non-Liouville parameters; \citet[Theorem~3.7]{chamizo2020bishop} extends this to convergent denominators satisfying \(\log q_{j+1}=O(q_j/(\log q_j)^3)\), and hence includes some Liouville numbers. The same paper proves biquasitriangularity and norm approximation by nilpotent operators, neither of which alone produces an invariant subspace. \citet[Introduction]{behani2023bishop} explicitly retains the all-irrational question.',
     ['chamizo2020bishop','behani2023bishop'],**{'class':'C'},literal_correctness='correct with missing hypotheses',publication_match='partial',problem='GP-1964-05',development='annotated',
     present_status=r'As of November 2026: the checked established results cover the stated arithmetic class, not every irrational parameter. No established all-parameter resolution was verified; the original no-subspace suggestion is already disproved for non-Liouville parameters.',
     worth=r'Yes. Exact finite-rotation products and quantitative rational approximation give concrete test cases. An invariant-subspace proof for the exceptional arithmetic regime still requires an argument beyond the finite-orbit continuity developed here.')
item(50,'P000089','problem','Cyclic vectors for irrational Bishop operators',
     r'After conjecturing that every vector is cyclic, the speaker says that not even one cyclic vector is known.',
     r'For each irrational \(\alpha\in(0,1)\), does there exist \(f\in L^2(0,1)\) with \(\overline{\operatorname{span}}\{T_\alpha^n f:n\ge0\}=L^2(0,1)\)? A stronger concrete question asks when the constant function \(1\) is cyclic. Existence of one cyclic vector is far weaker than every nonzero vector being cyclic.',
     r'\citet[Theorems~4.4--4.5, 4.9 and 4.16]{behani2023bishop} establishes rational cyclicity, a co-meager set of cyclic irrational parameters, and sufficient continued-fraction conditions. The preprint circulated in July 2022 and the paper appeared in 2023. Its Question~5.4 asks for an explicit approximation threshold. The chapter gives a bounded rational-fibre certificate and continuity estimate, not an all-irrational proof. A 2026 preprint lead was inaccessible and is not used as an established result.',
     ['behani2023bishop','ma2026rational'],**{'class':'C'},literal_correctness='correct',publication_match='partial',problem='GP-1964-06',development='developed in this chapter',
     present_status=r'As of November 2026: cyclicity is established for a co-meager parameter set and explicit sufficient classes in the checked work; universal irrational cyclicity was not verified. The historical absence of any known vector is obsolete.',
     worth=r'Yes. Rational cyclicity, exact finite products and strong continuity reduce selected questions to finite polynomial approximations with controlled error. The chapter develops such certificates and states their remaining arithmetic and conditioning obstacles explicitly.')
item(50,'P000089','claim','The unspecified Ornstein cyclicity example',
     r'An operator on \(L^2(0,1)\) is attributed to Ornstein, with every vector in \(L^{2+\varepsilon}\) cyclic. A nonsingular transformation without invariant measure is mentioned, but no operator is written.',
     r'At minimum the cyclicity assertion must concern nonzero vectors and specify whether \(\varepsilon>0\) is fixed or varies. The operator, weight, transformation, and intended class of invariant measures are absent. A nonsingular transformation alone does not specify a bounded weighted-composition operator with the asserted cyclicity.',
     r'Targeted searches on Ornstein, cyclic vectors, \(L^{2+\varepsilon}\), nonsingular transformations and invariant measures did not produce an opened primary theorem with these exact hypotheses. This anecdote is not identified with unrelated Ornstein results in ergodic theory, and no claimed counterexample to the Hilbert invariant-subspace problem is extracted from it.',
     [],**{'class':'F'},literal_correctness='not determinable',publication_match='none found',verification='unresolved lead',confidence='low',present_status=r'As of November 2026: insufficiently specified and not securely identified; retained with explicit search limits.')
item(50,'P000089','question','Why invariant subspaces, and what could replace them?',
     r'Gelfand asks why invariant subspaces are needed and what could replace them.',
     r'This is a methodological question about structural invariants and operator models, not a quantified mathematical conjecture. Spectral measures, characteristic functions, similarity invariants and invariant-subspace lattices answer different versions of it.',
     r'The next intervention gives one concrete contemporary response through analytic characteristic functions. No solved/open status is meaningful for the unrestricted methodological question itself.',
     [],**{'class':'F'},literal_correctness='not determinable',publication_match='none found',verification='indirect',development='none',confidence='high',present_status=r'As of November 2026: historical methodological discussion, not an independently unresolved theorem.')
item(50,'P000089','construction','Analytic characteristic functions and the contraction model',
     r'An English-speaking visitor with an uncertain F-name describes an analytic contraction from \(E\) to \(E_*\), Hardy boundary functions and analogues of Jordan blocks. The final finite-dimensional affine-map sentence does not specify the equivalence relation.',
     r'For a completely nonunitary contraction \(T\), its characteristic function \(\Theta_T(z):\mathcal D_T\to\mathcal D_{T^*}\) is analytic and contractive for \(|z|<1\). It determines \(T\) up to unitary equivalence, modulo constant unitary identifications of the defect spaces. The standard model uses \([H^2(\mathcal D_{T^*})\oplus\overline{\Delta L^2(\mathcal D_T)}]\ominus\{\Theta_T f\oplus\Delta f:f\in H^2(\mathcal D_T)\}\), with \(\Delta=(I-\Theta_T^*\Theta_T)^{1/2}\).',
     r'\citet[Theorem~1, p.~50; Theorem~3, p.~58]{sznagyfoias1964viii} gives the model and complete unitary invariant; it was received April 1963, revised December 1963 and published in 1964. \citet[Theorem~1 and formulas (3.16)--(3.17), pp.~294--295]{sznagyfoias1964ix} gives the factorization/invariant-subspace correspondence. This is an exact mathematical match, but not independent proof of the visitor\textquotesingle s identity.',
     ['sznagyfoias1964viii','sznagyfoias1964ix'],literal_correctness='correct with missing hypotheses',reconstruction=r'The missing upper Fourier-integral limit is \(2\pi\); the positive exponent \(e^{int}\), \(n\ge1\), correctly kills negative Fourier coefficients. Complete nonunitarity and the defect-space constraints are essential. The separate finite-dimensional affine-map/Jordan analogy remains underdetermined.',speaker='Unidentified participant (possibly C. Foiaş)',confidence='medium')
save()

problem('GP-1964-02','Invariant subspaces of bounded operators on complex Hilbert space',
        r'Does every bounded operator on a separable infinite-dimensional complex Hilbert space have a nonzero proper closed invariant subspace?',
        ['1964-50.1'],r'No generally accepted general solution was verified in sources checked through 12 November 2026. The 1964 de Branges--Rovnyak announcement was retracted in 1965; recent claimed proofs are not treated as established. Parent merge adds the occurrence in record 17.',
        ['debrangesrovnyak1964existence','debrangesrovnyak1965correction','chamizo2020bishop','behani2023bishop','szczepanski2026chain'])
problem('GP-1964-S03','Weight criteria for a unicellular backward shift',
        r'Characterize bounded nonzero weight sequences for which the backward shift on \(\ell^2\) has exactly the finite initial-span invariant subspaces and the whole space.',
        ['1964-50.16'],r'Many sufficient criteria are established, including monotone moduli decreasing to zero. A complete explicit criterion for arbitrary nonmonotone weights was not verified; this qualified residual classification is not the monotone case.',
        ['donoghue1957lattice','harrison1971unicellularity','yakubovich1985weighted'])
problem('GP-1964-05','Invariant subspaces of every irrational Bishop operator',
        r'For every irrational \(\alpha\), must \(T_\alpha f(x)=x f(\{x+\alpha\})\) on \(L^2(0,1)\) have a nonzero proper closed invariant subspace?',
        ['1964-50.20'],r'Affirmative for non-Liouville parameters and a larger arithmetic class, including the continued-fraction condition in Chamizo et al., Theorem 3.7. No established all-parameter resolution was verified through November 2026.',
        ['chamizo2020bishop','behani2023bishop'])
problem('GP-1964-06','Cyclicity of irrational Bishop operators',
        r'Does every irrational Bishop operator admit a cyclic vector, and for which parameters is the constant function cyclic?',
        ['1964-50.21'],r'Béhani proves a co-meager cyclic parameter set and sufficient approximation conditions. The chapter develops a bounded rational-orbit certificate and continuity estimates. It does not prove universal irrational cyclicity; an inaccessible 2026 lead is not relied on.',
        ['behani2023bishop','ma2026rational'])
save()

# Final primary-source audit. This is kept in the reproducible builder rather
# than being an unrecorded edit to the generated JSON.
by_id={i['id']:i for i in items}
by_id['1964-37.1'].update(
    statement=r'For a specified Lie algebra \(\mathfrak g\) over a field \(k\), determine whether \(U(\mathfrak g)\) has a faithful simple left module. For finite-dimensional complex \(\mathfrak g\), the Dixmier--Moeglin equivalence gives a precise criterion: the zero ideal is primitive if and only if the center of the quotient division ring of \(U(\mathfrak g)\) is \(\mathbb C\). The restriction on the field and dimension is essential to the stated scope.',
    fate=r'\citet[p.~2020]{bell2017poisson} explicitly records the primitive--rational--locally-closed equivalence for enveloping algebras of finite-dimensional complex Lie algebras, crediting Dixmier (1977) and Moeglin (1980). Applied to the zero prime ideal, it yields the criterion stated here. This later primary account was read; the original proofs were not. \citet{ooms1974primitive} is a separate, inaccessible lead on solvable Lie algebras and is not needed to certify the criterion.',
    refs=['bell2017poisson','ooms1974primitive'],verification='read the result',confidence='high',
    present_status=r'As of November 2026: the finite-dimensional complex problem belongs to an established primitive-ideal theory and admits the stated criterion. The notebook omits the field and dimension, so an unrestricted field-independent classification is not asserted.')
by_id['1964-37.2'].update(
    fate=r'The nonabelian case can be checked directly on \(\mathbb C[t]\): let \(h\) multiply by \(t\) and \(x f(t)=f(t+1)\), so \([x,h]=x\). A submodule is an ideal stable under translation, hence is zero or the whole ring; distinct finite translations are linearly independent over \(\mathbb C[t]\), giving faithfulness. This elementary verification agrees with the later primitive-ideal framework \citep[p.~2020]{bell2017poisson}.',
    refs=['bell2017poisson'],verification='read the result',confidence='high',
    reconstruction=r'The faithful simple module is an editorial verification, not a reconstruction of an omitted notebook proof. The base field is fixed to \(\mathbb C\).')
by_id['1964-37.3']['verification']='indirect'
by_id['1964-42.2']['verification']='indirect'
by_id['1964-47.2'].update(
    fate=r'\citet[Theorem~1, p.~13]{buslaevfaddeev1960traces} gives the relative-resolvent/logarithmic-Jost-derivative identity before the seminar; the note was received 17 December 1959 and published in 1960. Jost solutions are developed in \citet[\S1 and \S6]{faddeev1959inverse}. The precise Fredholm-determinant equality under weaker \(L^1\) conditions is also verified in \citet[Theorem~1.1]{gesztesy2007jost}.',
    refs=['buslaevfaddeev1960traces','faddeev1959inverse','gesztesy2007jost'])
by_id['1964-47.5'].update(
    fate=r'\citet[\S2, pp.~14--15]{buslaevfaddeev1960traces} carries out contour deformation, asymptotic subtraction and Mellin continuation in the singular Sturm--Liouville setting. Its finite-interval discussion on p.~16 uses Dirichlet ends, so it is not silently identified with the notebook\textquotesingle s Neumann expression. This is pre-seminar trace theory, not a universal ordinary-integral identity.',
    verification='read the result')
by_id['1964-50.1'].update(
    fate=r'The 1964 de Branges--Rovnyak announcement was retracted in 1965, as explicitly identified by Rovnyak\textquotesingle s author bibliography \citep{debrangesrovnyak1964existence,debrangesrovnyak1965correction}. The primary preprint \citet[abstract and Introduction, pp.~1--2]{marcoux2026generators}, dated 21 August 2026, still calls the precisely scoped Hilbert problem unsolved. Targeted searches through 12 November found claimed solutions and partial results; no generally accepted general solution was verified. A claim in a preprint is not treated as an established theorem.',
    refs=['debrangesrovnyak1964existence','debrangesrovnyak1965correction','chamizo2020bishop','behani2023bishop','szczepanski2026chain','marcoux2026generators'])
by_id['1964-50.13'].update(**{
    'title':'Trace-class imaginary parts and triangular models',
    'class':'E','literal_correctness':'correct with missing hypotheses',
    'publication_match':'partial','verification':'read the result','confidence':'high',
    'statement':r'One precise realization is the following. Let \(T=A+iB\) be bounded on a separable complex Hilbert space, with \(A=A^*\), \(B=B^*\), and \(B\) trace class. The restriction of \(T\) to the orthogonal complement of its maximal reducing self-adjoint part is unitarily equivalent to the corresponding non-self-adjoint part of a Liv\v{s}ic triangular model. The additional reducing component is self-adjoint. Here nuclear means trace class; small operator norm is not a substitute for this hypothesis.',
    'reconstruction':r'The bounded separable Hilbert-space setting and the canonical self-adjoint real and imaginary parts are supplied explicitly. The nuclear example in the source identifies this established theorem, but its unspecified additional classes are not reconstructed. The stronger Hilbert--Schmidt criterion is reported by a later survey; its attribution was not independently confirmed in the cited 1959 original.',
    'fate':r'\citet[Introduction, p.~145; \S11, Theorem~4, pp.~180--181]{livsic1954spectral} gives the triangular-model theorem for trace-class imaginary part. Its introduction dates the preliminary announcements to two 1952 notes. \citet[Introduction and theorem, pp.~180--181]{sakhnovich1959triangular} recalls this nuclear case and constructs a triangular representation under an explicit invariant-subspace interpolation condition. The latter paper was received 6 December 1957 and published in 1959. The broader survey discussion \citep[\S7, pp.~57--59]{dymkatsnelson2007schur} is kept distinct from the original results actually read.',
    'present_status':r'As of November 2026: the nuclear example is an established pre-seminar result. The match is partial because the notebook does not identify its further small-imaginary-part classes or a particular theorem of each named author.',
    'refs':['livsic1954spectral','sakhnovich1959triangular','dymkatsnelson2007schur']})
by_id['1964-50.16'].update(**{
    'class':'B','worth':'',
    'fate':r'\citet[Theorem~1 and subsequent counterexamples]{nikolskii1967weighted} gives weight conditions and examples delimiting them. \citet[\S1; Lemmas~2.1--2.2]{harrison1971unicellularity} develops further criteria. The opened abstract of \citet{yakubovich1985weighted} proves that positive moduli monotonically decreasing to zero suffice on \(\ell^p\), \(1\le p<\infty\); Hilbert adjoints give the backward form. \citet[p.~232]{latapokhriyalsingh2023powers} also credits Nikol\textquotesingle skii\textquotesingle s 1967 and 1968 work with additional necessary and sufficient conditions. The 1968 original was verified only at metadata level \citep{nikolskii1968basicity}; its exact scope is not guessed.',
    'present_status':r'As of November 2026: developed and answered in substantial verified weight classes. The generality of a complete explicit characterization for arbitrary bounded nonmonotone weights was not ascertained in this audit. That verification gap is not classified as an established open problem.',
    'refs':['donoghue1957lattice','nikolskii1967weighted','nikolskii1968basicity','harrison1971unicellularity','yakubovich1985weighted','latapokhriyalsingh2023powers'],
    'reconstruction':r'Nonzero bounded weights and the Hilbert adjoint equivalence supply a precise classification question. The broad request for conditions is not silently replaced by an unverified demand for a novel universal closed-form criterion.'})
by_id['1964-50.17'].update(**{
    'class':'B','problem':'GP-1964-S04','publication_match':'exact','verification':'read the result','confidence':'high',
    'statement':r'There is a bounded operator on \(\ell^2(\mathbb Z)\) with full invariant-subspace lattice \(\{0,H\}\cup\{M_m:m\in\mathbb Z\}\), where \(M_m=\overline{\operatorname{span}}\{e_j:j\ge -m\}\). In particular take \(Se_j=\exp(-2|2j+1|)e_{j+1}\). The \(M_m\) increase strictly, have intersection zero and dense union. The literal ordered set \(\mathbb Z\) needs the endpoints \(0,H\).',
    'fate':r'\citet[Theorem~2, pp.~134--135; definitions p.~133]{domar1981translation} supplies an exact construction through weighted translation. Set \(w_n=\exp(-2n|n|)\). Then \(\log w\) is convex for \(n\le0\), concave for \(n\ge0\), \(\sum_{n\ne0}w_n^{1/n}=2\sum_{n\ge1}e^{-2n}<\infty\), and its quadratic limits are \(2>\log3\) at minus infinity and \(-2<-\log3\) at plus infinity. The unitary map \(c\mapsto(w_nc_n)\) turns right translation into the displayed shift. Domar proves that all invariant subspaces are the standard tails. Received 9 June 1980; published 1981.',
    'present_status':r'As of November 2026: the completed integer-chain existence question is solved affirmatively by the established bilateral weighted-shift construction. The literal omission of least and greatest lattice elements is only a shorthand defect.',
    'refs':['domar1981translation'],
    'reconstruction':r'The endpoints and reversal of indexing are editorial. The concrete choice of Domar\textquotesingle s weights and the unitary conversion were checked independently in this audit; no novelty is claimed.'})

problem('GP-1964-S01','Primitivity of universal enveloping algebras',
        r'For a Lie algebra \(\mathfrak g\), when does \(U(\mathfrak g)\) have a faithful irreducible module? For the finite-dimensional complex reconstruction, this asks whether its zero prime ideal is primitive.',
        ['1964-37.1'],r'As of November 2026: established primitive-ideal theory gives the Dixmier--Moeglin criterion in the finite-dimensional complex case. The source omits field and dimension, so the audit does not assert an unrestricted field-independent answer.',
        ['bell2017poisson','ooms1974primitive'])
problem('GP-1964-S04','An invariant-subspace lattice with a bilateral integer chain',
        r'Does a bounded Hilbert-space operator have full invariant-subspace lattice \(\{0,H\}\cup\{M_m:m\in\mathbb Z\}\), with strict successive inclusion, intersection zero and dense union?',
        ['1964-50.17'],r'As of November 2026: yes. Domar\textquotesingle s Theorem~2 (1981) gives an exact example; \(Se_j=\exp(-2|2j+1|)e_{j+1}\) on \(\ell^2(\mathbb Z)\) has precisely the coordinate-tail nest and the two endpoints.',
        ['domar1981translation'])
for p in problems:
    if p['id']=='GP-1964-S03':
        p['status']=r'As of November 2026: developed and partly answered in verified weight classes, including monotone moduli tending to zero. The scope of a universal explicit arbitrary-weight criterion was not ascertained in this audit; it is not declared solved or open by default.'
        p['refs']=by_id['1964-50.16']['refs']
    if p['id']=='GP-1964-02':
        p['refs'].append('marcoux2026generators')
        p['status']=r'No generally accepted general solution was verified through 12 November 2026. A primary expert preprint of 21 August 2026 still explicitly calls this precise Hilbert-space problem unsolved. The 1964 announcement was retracted in 1965; unaccepted claimed proofs do not change the audited status.'

by_id['1964-42.3']['fate']=r'\citet[Introduction, formulas for \(K_\pm\)]{ehrhardt2007dyson} proves the large-gap constant as well as the displayed terms (preprint April 2006; publication 2007). The finite cosine matrix is a precursor of this even kernel. The manuscript relation between \(2m\) and \(n\) is itself uncertain (equality or inequality); the natural continuum scaling of the matrix uses \(m\alpha\). The source\textquotesingle s \(t=\alpha n\) is therefore not silently identified with the standard \(s\).'

# Corrections distinguish decipherment, explicit ambiguity, mathematical error,
# and provenance. The Russian diplomatic text is not silently modernized.
correction('P000065','Baxter paragraph, final two lines',
           r'If A is simple, there are no Lie ideals either.',
           r'False literally: for A=M_2(C), CI and sl_2(C) are proper nonzero Lie ideals. The intended quotient/involution theorem is not specified.',
           'Russian and English agree; scan confirms the two unrestricted sentences. Direct matrix examples refute the literal assertion. Item 1964-37.3.')
correction('P000066','Kostrikin/Burnside paragraph',
           r'Uniform e^n=0; the associative algebra is nilpotent, glossed as every element nilpotent.',
           r'Distinguish nil from nilpotent; retain uncertainty about the field, the quantified Lie subalgebra, and the intended conclusion.',
           'Russian abbreviation and explanatory clause do not give the same condition. The scan supports the uniform-n correction but does not supply characteristic or a theorem statement. Item 1964-37.4.',typ='ambiguity')
correction('P000066','Dixmier question, two differential-operator rings',
           r'P(x,d/dx) and P(x,d/dx,y,d/dy); are they isomorphic?',
           r'Interpret as A_1 versus A_2, not the fixed-rank Dixmier endomorphism conjecture.',
           'Scan shows one canonical pair and then two; Gelfand--Kirillov 1966 Section 4 distinguishes ranks by growth. The error is an index/provenance risk, not a false transcription.',typ='provenance')
correction('P000066-P000068','Log-gas energy and Boltzmann factor',
           r'Positive sum of pair logarithms called W, together with exp(-beta W).',
           r'With exp(-beta W), set W=-sum_{i<j}log|exp(i theta_i)-exp(i theta_j)|.',
           'The eigenangle density requires a positive power of the Vandermonde; the later integral uses exp(+beta sum log). Item 1964-39.3.')
correction('P000067','Claimed exact beta=2 gap expression',
           r'R_2(alpha)=exp(N^2 log cos(alpha/2)).',
           r'Not an exact finite-CUE probability; N=1 gives 1-alpha/pi. Treat only an appropriately qualified leading-energy approximation.',
           'Scan and both transcriptions give equality. Elementary N=1 check and the distinction from later determinant asymptotics. Items 1964-39.5 and 42.1.')
correction('P000068','First free-energy relation',
           r'R_beta(alpha)=exp(+beta(F(alpha)-F(0))) while F is minimized.',
           r'For F=-beta^{-1}log Psi, use exp(-beta(F(alpha)-F(0))); otherwise explicitly define the opposite sign convention for F.',
           'Scan confirms positive exponent. The normalization Psi(alpha)/Psi(0) and usual minimized-free-energy convention fix the sign. Item 1964-39.4.')
correction('P000068','Middle W formula',
           r'W=sum log|exp(i theta_i-i theta_j)|.',
           r'The interaction depends on |exp(i theta_i)-exp(i theta_j)|, with its energy sign separately specified.',
           'Scan shows a single exponential containing the phase difference; its modulus is identically one. The next multiple integral restores the difference of exponentials. Item 1964-39.3.')
correction('P000069','Notation Z_p in finite-field counting discussion',
           r'Z_p and its algebraic closure.',
           r'Here Z_p means the finite field F_p, not the p-adic integers.',
           'Russian finite-equation and Frobenius context identifies the notation. Clarification of historical notation, not replacement of a wrong glyph. Item 1964-40.1.',typ='ambiguity')
correction('P000073','Even-kernel asymptotic',
           r'R_1(t)~A t^(17/8) exp(-t^2/4-t/2).',
           r'For the identified standard even sine kernel, the power is -1/8; retain the manuscript 17/8 in the notes field.',
           'Scan and Russian EvidenceBlock both confirm 17/8; Ehrhardt Introduction gives -(1/8)log(s). The parameter normalization remains separately uncertain. Item 1964-42.3.')
correction('P000073','Relation between m,n and gap parameter',
           r'2m >= n or 2m=n; t=alpha n.',
           r'Keep the relation ambiguous; the finite cosine matrix naturally scales with m alpha and cannot automatically be identified with the standard s.',
           'The handwritten relation is thick and not securely an equality; t=alpha n is underlined twice. No invented rescaling. Item 1964-42.3.',typ='ambiguity')
correction('P000073','Sphere bundle over the Grassmannian',
           r'M_{n,k} -> G_{n,k} with fibre written S_k.',
           r'The unit sphere in a k-dimensional real plane is S^{k-1}; retain S_k only as historical notation.',
           'The definition says a k-plane and one point of its unit sphere; the subscript is not a claim of dimension k. Item 1964-45.2.',typ='ambiguity')
correction('P000074-P000075','Half-line characteristic function and resolvent',
           r'Whole function/trace terminology carried over from the finite interval.',
           r'For the half-line use the Jost function on the specified sqrt(z) sheet and a relative resolvent trace, not the ordinary trace of the individual resolvent.',
           'Russian text distinguishes subtraction of the free term; Buslaev--Faddeev 1960 Theorem 1 gives the exact relative identity. Items 1964-47.1--47.3.',typ='ambiguity')
correction('P000076','Real-axis trace integral',
           r'Integral of |lambda|^s Wprime/W equals sum of eigenvalue powers.',
           r'Read the manuscript parenthesis “integral is a jump”: retain both boundary values, contour orientation, normalization and regularizing subtractions.',
           'The handwritten parenthesis and Russian text explicitly say jump. Buslaev--Faddeev Section 2 implements the contour/Mellin argument. Item 1964-47.5.',typ='ambiguity')
correction('P000076','Neumann trace boundary expression',
           r'(1/4)(yprime(0)-yprime(pi)).',
           r'Retain yprime and mark it unidentified; do not silently replace it by q(0)+q(pi).',
           'Scan confirms y with prime in both terms. No definition of this y is supplied. Item 1964-47.6.',typ='ambiguity')
correction('P000076','Formal diagonal of the delta kernel',
           r'delta(0)=0.',
           r'delta(0) is not a defined pointwise value; state an explicit spectral/resolvent regularization before taking a trace.',
           'Scan confirms the equality. Distribution theory does not permit this diagonal substitution. Item 1964-47.7.')
correction('P000076','Gelfand commutator trace question',
           r'Tr(AB-BA)=0 without assumptions.',
           r'Both AB and BA trace class suffice; trace class of the commutator alone does not. [S*,S] has rank one and trace one.',
           'The source labels this a problem rather than a fully quantified theorem; the distinction is necessary for a precise reconstruction. Item 1964-47.8.',typ='ambiguity')
correction('P000078','Continuous-parameter Weil kernel',
           r'Kernel involving P_1 P_2prime-P_2 P_1prime over a single displayed defining-function difference.',
           r'Retain as an unfinished formula; no denominator order, parameter cycle or orientation is supplied editorially.',
           'Scan shows the incomplete formula and the subsequent linear/Radon specialization. The latter has a precise 1965 publication, but it does not identify the whole general kernel. Item 1964-48.5.',typ='ambiguity')
correction('P000081','Exactness after refinements',
           r'Long exact sequences exist for each cover but may lose exactness upon passage to the limit.',
           r'Filtered colimits of abelian groups preserve exactness. The fixed-cover section complexes may already fail to form a short exact sequence.',
           'Scan confirms the claim about passage to a limit. The sheaf epimorphism/local-lifting distinction gives the actual obstruction. Item 1964-49.4.')
correction('P000082','Subscript p in exactness discussion',
           r'F_pprime -> F_p -> F_pdoubleprime is not necessarily onto.',
           r'Do not interpret p automatically as a stalk. The line labels presheaves; stalks of an exact sequence of sheaves are exact.',
           'Scan has “предпучки” under the first object and distinguishes the inclusion functor below. The handwriting alone does not define p. Item 1964-49.5.',typ='ambiguity')
correction('P000082-P000083','Truncated differential-form sequence',
           r'0 -> C -> Omega^0 -> Omega -> 0.',
           r'Identify the final sheaf and differential before claiming exactness; one classical repair uses closed one-forms, not all one-forms in higher dimension.',
           'Russian and English leave the final Omega unspecified; scan confirms the truncated sequence. Item 1964-49.7.',typ='ambiguity')
correction('P000084','Subnormality condition',
           r'T*T-TT* >= 0 is necessary and sufficient.',
           r'Necessary only; subnormality requires the full positivity conditions. Weights 1,1,2,2,... give a hyponormal non-subnormal unilateral shift.',
           'Scan shows the rewritten necessary-and-sufficient phrase. The moment counterexample is checked in item 1964-50.6; uncertainty of the horizontal glyph does not save the biconditional.')
correction('P000084-P000085','Matrix coefficients in the polynomial proof',
           r'P84 a_mn=(Ae_n,e_m), but P85 defines a_mn^(p)=(p(A)e_m,e_n).',
           r'Use a_mn^(p)=(p(A)e_n,e_m) consistently with the lower-Hessenberg convention.',
           'Scans of both pages and Halmos 1966 pp.433--434 agree on the convention required by the displayed subdiagonal product. Item 1964-50.8.')
correction('P000086','Positive norm limit',
           r'lim ||p(P_n A P_n)||=d>0 after convergence applied to e.',
           r'The inference supplies lim ||p(P_n A P_n)e||=||p(A)e||>0; it does not supply operator-norm convergence.',
           'Scan visibly omits e in this one line while surrounding formulas contain it; the published Halmos proof uses the vector norm. Item 1964-50.10.')
correction('P000086-P000087','Adjacent-flag threshold and cancelled monotonicity',
           r'Conflicting half-d threshold directions; assertion of monotonic decrease is cancelled.',
           r'Keep the cancellation; select the first adjacent crossing using the endpoint values, as in the published proof, without assuming monotonicity of these norms.',
           'Both scans reviewed. The terminal norm is zero and initial norm exceeds 3d/4, but monotonicity is neither needed nor established. Halmos 1966 pp.435--437. Item 1964-50.10.')
correction('P000088','Compact-defect norm assumption',
           r'||T||<1 or ||T||<=1; I-T*T compact.',
           r'Keep the sign uncertain. Strict inequality is impossible with compact defect in infinite dimension; non-strict inequality is a separate theorem request.',
           'The scan does not securely distinguish the signs. Coercivity I-T*T >= (1-||T||^2)I diagnoses the strict reading. Item 1964-50.12.',typ='ambiguity')
correction('P000088','Sz.-Nagy--Foias powers',
           r'Both T^n -> 0 and (T*)^n -> 0 have crossed arrows.',
           r'Retain failure of strong convergence to zero for both power sequences, with ||T||<=1 and dim H>1.',
           'Scan confirms crossed arrows; exact primary theorem is Sz.-Nagy--Foias IX, Section 6, Theorem 3 and Remark (ii), p.314, unaffected by the 1965 correction. Item 1964-50.14.',typ='ambiguity')
correction('P000088','Donoghue superdiagonal weights',
           r'1/2,1/4,then 1/8 or 1/6.',
           r'Retain the third-entry uncertainty; the geometric 2^{-n} choice is a literature-supported reconstruction, not a certain decipherment.',
           'Scan and diplomatic uncertainty compared with Donoghue Examples 1--2. Item 1964-50.15.',typ='ambiguity')
correction('P000088','Integer-chain lattice',
           r'The structure of all integers.',
           r'Adjoin the obligatory lattice endpoints 0 and H; the completed integer-chain question has an affirmative Domar construction.',
           'Every full invariant-subspace lattice contains least and greatest elements. Domar 1981 Theorem 2 supplies the exact completed order type. Item 1964-50.17.',typ='ambiguity')
correction('P000088','Measure-Volterra conjecture',
           r'A f(x)=integral_0^x f(y) dmu(y) on the real line; lattice isomorphic to supp(mu).',
           r'False for mu=(1/2)1_{[-1,1]}dx with oriented integration: negative-side and positive-side support spaces are incomparable invariant subspaces.',
           'Scan gives the real line and lower limit zero. The atomless probability counterexample avoids endpoint-convention ambiguity. The one-sided classical repair is stated separately. Item 1964-50.19.')
correction('P000089','Every vector cyclic, including the Ornstein remark',
           r'Every vector is cyclic.',
           r'Every nonzero vector is the meaningful formulation; the zero vector cannot be cyclic in a nonzero space.',
           'Scan and both transcriptions omit nonzero. The Bishop universal claim is also disproved for known arithmetic parameter classes. Items 1964-50.20--50.22.')
correction('P000089','Hardy Fourier condition',
           r'Integral_0 u(t) exp(int) dt=0, n=1,2,..., with no upper limit.',
           r'Use upper limit 2pi in the stated circle normalization. Keep the positive exponent: it correctly eliminates negative Fourier coefficients.',
           'Scan shows lower zero only and the circle 2pi immediately above. Item 1964-50.24.',typ='ambiguity')
correction('P000089','Final intervention speaker',
           r'An English-speaking professor with a doubtful F-name, Hungarian from Romania.',
           r'Possible C. Foias identification remains qualified; exact theorem identification does not establish speaker identity.',
           'Scan surname is overwritten; analytic-contraction content matches Sz.-Nagy--Foias 1964 but is not independent biographical evidence. Item 1964-50.24.',typ='provenance')
correction('P000090','Academic-year boundary at page heading',
           r'Page included in the supplied 1964--65 translation envelope.',
           r'Opening 20/IX, Kohn, belongs to 20 September 1965 and the next academic year; do not attribute it to record 50.',
           'Scan and Russian heading explicitly show 20/IX and Kohn. Catalog page envelopes overlap; provenance is preserved in the record-50 summary.',typ='provenance')
save()
print(f'Spring checkpoint: {len(talks)} talks, {len(items)} items, {len(problems)} problems, {len(corrections)} corrections.')
