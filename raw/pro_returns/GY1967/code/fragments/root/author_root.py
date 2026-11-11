"""Authored catalogue records 167--173; run to emit the structured fragment.
Statements were checked against the supplied Russian notes and scans.
This script serializes the editorial work; it does not infer mathematical content.
"""
import csv
import json
from pathlib import Path

HERE = Path(__file__).parent
talks, items, problems, corrections = [], [], [], []

def talk(record, date, speaker, pages, title, summary, kind='talk'):
 talks.append(dict(record=record,date=date,speaker=speaker,pages=pages,title=title,kind=kind,summary=summary))

def item(record, pages, kind, title, notes, statement, fate, refs=(), *,
         reconstruction='', cls='E', correctness='correct with missing hypotheses',
         match='exact', verification='read the result', development='annotated',
         problem='', worth='', confidence='high', status=None, speaker=None):
 n = 1 + sum(x['record']==record for x in items)
 x = dict(id=f'1968-{record}.{n}',record=record,pages=pages,kind=kind,title=title,
          notes=notes,statement=statement,reconstruction=reconstruction,**{'class':cls},
          fate=fate,present_status=status or 'As of November 2026: established in the stated scope; this occurrence does not pose an unresolved problem.',
          literal_correctness=correctness,publication_match=match,verification=verification,
          development=development,problem=problem,worth=worth,refs=list(refs),confidence=confidence)
 if speaker: x['speaker']=speaker
 items.append(x)

def correction(page, place, reads, should, evidence, applies='both', typ='faithful_error'):
 corrections.append(dict(page=page,place=place,transcription_reads=reads,should_read=should,evidence=evidence,applies_to=applies,type=typ))

def save():
 for name, data in [('talks',talks),('items',items),('problems',problems)]:
  (HERE/(name+'.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 with (HERE/'corrections.csv').open('w',encoding='utf-8',newline='') as f:
  fields=['page','place','transcription_reads','should_read','evidence','applies_to','type']
  w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(corrections)
 print(f'Root fragment: {len(talks)} records, {len(items)} items, {len(problems)} problems, {len(corrections)} corrections')

talk(167,'1969-02-10','I. M. Gelfand','P000271-P000274',
     '3-adic arithmetic for schoolchildren',
     r'The mathematical passage is on P000272, after Margulis and a list of prospective speakers. Gelfand introduces left-infinite ternary expansions, carries, the expansions of \(-1\) and \(1/2\), and the obstruction to division in base ten. The comparison with real decimal expansions is pedagogical, not a claim that the real numbers are mathematically defective. The surrounding catalogue pages contain other records.')
item(167,'P000272','construction','Left-infinite digits and the 3-adic topology',
     r'\ru{3-адические числа (для школьников)}; infinitely many digits extend to the left, and the rules and topology are introduced by analogy.',
     r'\(\mathbb Z_3=\varprojlim_k\mathbb Z/3^k\mathbb Z\). Each element has a unique expansion \(\sum_{j\geq0}a_j3^j\), \(a_j\in\{0,1,2\}\), convergent for \(|x|_3=3^{-v_3(x)}\). Addition and multiplication are compatible finite carry operations modulo \(3^k\); \(\mathbb Q_3=\mathbb Z_3[1/3]\). The digit construction first describes the ring of integers, not every element of the field without a finite right-hand tail.',
     r'Classical arithmetic, already known before the seminar; \citet[Chs.~3--4]{gouvea2020padic} is a modern exposition, not the first publication.',
     ['gouvea2020padic'],reconstruction='The inverse limit, valuation and distinction between the integer ring and field make the informal construction precise.',verification='publisher metadata checked')
item(167,'P000272','claim','The ternary expansions of minus one and one half',
     r'The sums display \(\ldots2222=-1\) and \(\ldots11112=1/2\); the latter is obtained by multiplying by two and carrying.',
     r'In \(\mathbb Z_3\), \(\sum_{j\geq0}2\cdot3^j=-1\) and \(2+\sum_{j\geq1}3^j=1/2\). Indeed the finite truncations are \(3^{k+1}-1\) and \((3^{k+1}+1)/2\); their errors tend to zero in the 3-adic norm. The displays are expansions in base three.',
     r'These are elementary instances of the geometric-series calculation in the 3-adic ring; the modern reference is \citet[Ch.~4]{gouvea2020padic}. The finite-truncation identities also verify the notebook directly.',
     ['gouvea2020padic'],correctness='correct',verification='publisher metadata checked',reconstruction='Finite-truncation verification is supplied here; no research novelty is claimed.')
item(167,'P000272','remark','Decimal identifications and the nonfield of 10-adic integers',
     r'The real expansion \(0.999\ldots=1\) is contrasted with a disconnected digit space. The last line says \ru{10-адические --- деления нет} and notes the absence of \(1/5\).',
     r'The real value map from digit sequences to \([0,1]\) is continuous and identifies the familiar terminating/nonterminating pairs; its image is connected although its domain is totally disconnected. In contrast, \(\mathbb Z_{10}=\varprojlim_k\mathbb Z/10^k\mathbb Z\simeq\mathbb Z_2\times\mathbb Z_5\) by the Chinese remainder theorem. Its units are precisely the elements invertible modulo ten; \(5\) is not a unit, so \(1/5\notin\mathbb Z_{10}\). Division by units does exist.',
     r'This is classical positional arithmetic. The prime-base setting is treated by \citet[Ch.~3]{gouvea2020padic}; the product description is the direct inverse-limit form of the Chinese remainder theorem.',
     ['gouvea2020padic'],reconstruction='The product-ring formulation and restriction of the phrase no division to nonunits are editorial precisifications.',verification='publisher metadata checked')
correction('P000272','Last line of the schoolchild explanation',r'\ru{10-адические --- деления нет} (no division).',r'\(\mathbb Z_{10}\) is not a field; division by units exists, but \(5\) is not invertible.',r'The scan faithfully has the abbreviated phrase. Reduction modulo five rules out \(5x=1\); reduction modulo ten characterizes units. This is a qualification of the mathematics, not a mistranscription.')

talk(168,'1969-03-31','P. M. Bleher','P000272-P000277',
     'Hörmander spectral asymptotics and their sharpness',
     r'The heading on P000273 reads 31/III; the surrounding year is 1969, so the date can be resolved despite the missing normalized date in the supplied list. P000273--P000275 explain \citet{hormander1968spectral}: the local Weyl law, the sphere obstruction to an improved unsmoothed remainder, the first-order root of an elliptic operator, a short-time oscillatory parametrix and a Tauberian passage back to the spectral function. Questions about averaged higher terms are recorded, although the cited paper itself already discusses Riesz means. Several numerical coefficients in the notebook need correction.')
item(168,'P000273','definition','The spectral function of a positive elliptic realization',
     r'\((Pu,u)\geq c(u,u)\), \(\widehat P=\int\lambda\,dE_\lambda\), and \(e(x,y,\lambda)\in C^\infty(\Omega\times\Omega)\) are introduced.',
     r'Let \(P\) be a scalar elliptic differential operator of order \(m>0\) with smooth coefficients on a smooth manifold \(\Omega\), formally self-adjoint and bounded below by \(c>0\) on \(C_c^\infty\) for a fixed smooth positive density. For a self-adjoint realization \(\widehat P\geq c\), let \(E_\lambda=1_{(-\infty,\lambda]}(\widehat P)\). Its Schwartz kernel is the spectral function \(e(x,y,\lambda)\), smooth in the spatial variables locally in the interior for each finite \(\lambda\). Smoothness here does not mean continuity in the spectral parameter.',
     r'The precise setup is already \citet[pp.~193--194]{hormander1968spectral}; received 7 May 1968, printed December 1968, before this exposition.',
     ['hormander1968spectral'],reconstruction='The density, self-adjoint realization, scalar ellipticity and interior restriction are restored from the identified source.')
item(168,'P000273','theorem','The local Weyl remainder',
     r'The diagonal expression is \(\lambda^{-n/m}e(x,x,\lambda)-(2\pi)^{-n}\int_{p^0(x,\xi)<1}d\xi=O(\lambda^{-1/m})\).',
     r'In the preceding setting, with real positive principal symbol \(p_m\), uniformly for \(x\) in each compact interior set, \[e(x,x,\lambda)=(2\pi)^{-n}\lambda^{n/m}\operatorname{vol}\{\xi:p_m(x,\xi)<1\}+O(\lambda^{(n-1)/m}).\] The cotangent measure is dual to the chosen base density.',
     r'Exact match: \citet[Theorem~1.1]{hormander1968spectral}. The 1968 publication precedes Bleher\textquotesingle s talk.',
     ['hormander1968spectral'],reconstruction='The formula is a local estimate; boundary terms and uniformity to a boundary are not asserted.')
item(168,'P000273','claim','Off-diagonal leading term',
     r'The underlined phrase is \ru{Вне диагонали 0}.',
     r'For fixed distinct interior points, the leading \(\lambda^{n/m}\) diagonal term disappears. In the local coordinate domain of the oscillatory formula, on compact subsets away from the diagonal, \(e(x,y,\lambda)=O(\lambda^{(n-1)/m})\); in particular \(\lambda^{-n/m}e(x,y,\lambda)\to0\). The unnormalized kernel is generally not zero.',
     r'The relevant off-diagonal parametrix and estimate are in \citet[Theorem~5.1 and (5.4), p.~215]{hormander1968spectral}.',
     ['hormander1968spectral'],correctness='false as written',reconstruction='Zero is read as zero leading normalized term. The notebook does not write this normalization in its short phrase.')
item(168,'P000273','construction','Spherical harmonics and the spectral jump',
     r'For the Laplacian on \(S^n\), the jump is written \((C_{n+k}^{k}-C_{n+k}^{k-2})/V_n\), with large multiplicities attributed to rotations.',
     r'For the nonnegative Laplacian on the unit \(S^n\), \(n\geq1\), the eigenvalue \(\lambda_k=k(k+n-1)\) has multiplicity \[d_{n,k}=\binom{n+k}{k}-\binom{n+k-2}{k-2},\] with the second binomial zero for \(k<2\). Rotational invariance and integration over the sphere give the pointwise projector diagonal \(d_{n,k}/\operatorname{vol}(S^n)\). The upper index of the second binomial in the notebook must change.',
     r'The example is analyzed in \citet[\S6]{hormander1968spectral}; the corrected formula also follows by subtracting the dimensions of homogeneous polynomials of degrees \(k\) and \(k-2\).',
     ['hormander1968spectral'],correctness='false as written',reconstruction='The eigenvalue and correct binomial coefficient are supplied; the transcriptions faithfully preserve the erroneous second index.')
item(168,'P000273','theorem','Why a universal smaller unsmoothed remainder is impossible',
     r'The jump has size \(\lambda^{(n-1)/2}\); the notes say one cannot write a term \(C\lambda^{(n-1)/2}\).',
     r'For the sphere, \(d_{n,k}\sim2k^{n-1}/(n-1)!\) as \(k\to\infty\). A continuous approximation has the same limiting value on both sides of each jump, so at least one one-sided error is at least half that jump. Consequently an unsmoothed expansion with remainder \(o(\lambda^{(n-1)/2})\) is impossible, even after adding a fixed continuous term of that order. An \(O(\lambda^{(n-1)/2})\) bound remains valid.',
     r'Avakumovi\v{c}\textquotesingle s sharpness example is explicitly credited and proved in \citet[\S6]{hormander1968spectral}.',
     ['hormander1968spectral'],reconstruction='The distinction between a big-O bound and a fixed second asymptotic coefficient is essential; the Russian abbreviated sentence does not deny the valid big-O estimate.')
item(168,'P000273-P000274','question','Higher spectral terms after averaging',
     r'The page asks for the next term of \(\lambda^{-1}\int_0^\lambda e(x,x,\nu)\,d\nu\), says this has not been done except for a square, and distinguishes obtaining subsequent terms from a formal asymptotic expansion.',
     r'For the positive elliptic \(P\) above, determine how many symbol-computable asymptotic terms are justified for the normalized Riesz means \[e^\alpha(x,x,\lambda)=\int_0^\lambda(1-\nu/\lambda)^\alpha\,d_\nu e(x,x,\nu),\quad\alpha>0.\] For \(\alpha=1\) integration by parts gives the notebook\textquotesingle s average. If the leading Weyl coefficient is \(a_0(x)\), its leading averaged coefficient is \(m a_0(x)/(m+n)\). A fixed smoothing order does not automatically yield an arbitrarily accurate expansion.',
     r'Already addressed in \citet[Theorem~4.5 and pp.~215--216]{hormander1968spectral}, with remainder order \(O(\lambda^{(n-1-\alpha)/m})\) after the appropriate finite expansion. The antecedent was circulated at the November 1966 Belfer conference and translated in 1968: \citet{hormander1968riesz}.',
     ['hormander1968spectral','hormander1968riesz'],correctness='false as written',match='partial',problem='GP-1968-40',
     reconstruction='The smoothing parameter and exact quantifier are editorial. The incorrect leading coefficient and the assertion of no existing work are not adopted.',
     status='As of November 2026: the general Riesz-mean framework was already available by 1968. Unsmoothed full expansions are obstructed by spectral jumps; no unresolved problem is inferred from this wording.')
item(168,'P000274','remark','The trace-formula reading pointer',
     r'The notes recommend Dikii in UMN, dated 1957, and an earlier Gelfand work, dated 1954, on traces.',
     r'This is a bibliographical pointer to regularized spectral traces, not a recorded trace identity. No boundary conditions, potential, summation prescription or operator pair are specified; a unique theorem cannot be reconstructed from the pointer alone.',
     r'The identifiable UMN review is \citet{dikii1958traces}, published in 1958, pp.~111--143. The Gelfand pointer is too abbreviated to identify one publication without a conjectural attribution.',
     ['dikii1958traces'],cls='F',correctness='not determinable',match='partial',verification='publisher metadata checked',confidence='medium',
     status='As of November 2026: the review is identified and its date corrected; no independent mathematical question is recoverable from the remaining pointer.')
item(168,'P000274','method','Reduction to a first-order pseudodifferential root',
     r'\(A=\widehat P^{1/m}\), \(A=a_1+a_0+a_{-1}+\cdots\), and \(a_1=p^{1/m}\).',
     r'On a closed manifold, for a positive invertible classical scalar elliptic \(P\) of order \(m\), spectral functional calculus defines \(A=P^{1/m}\), a classical pseudodifferential operator of order one with principal symbol \(p_m^{1/m}\). Its full symbol has a homogeneous asymptotic expansion away from the zero section. On a general open manifold the corresponding assertion is used microlocally in the interior.',
     r'Already used in \citet[p.~195]{hormander1968spectral}, citing Seeley\textquotesingle s complex-power construction. It is not a new method invented in Bleher\textquotesingle s talk.',
     ['hormander1968spectral'],reconstruction='Closedness and invertibility give a clean global version; a local statement suffices for the notes.')
item(168,'P000274','method','Half-wave evolution and propagation of singularities',
     r'\(G(t)=e^{itA}\), \((i\partial_t+A)G(t)=0\), \(G(0)=I\); the generalized Huygens principle is described as finite-speed propagation of singularities.',
     r'For self-adjoint \(A\), \(G(t)=e^{itA}\) is unitary and satisfies the displayed equation on its operator domain. When \(A\) is a real-principal-type first-order elliptic pseudodifferential operator, its short-time kernel is microlocally associated with the Hamiltonian flow, with sign determined by this evolution convention. Propagation of wavefront singularities is asserted, not compact support propagation for an arbitrary nonlocal operator.',
     r'The half-wave reduction and geometrical-optics construction are \citet[pp.~195--196 and \S3]{hormander1968spectral}.',
     ['hormander1968spectral'],reconstruction='The qualification concerns singularities, which is exactly the Russian noun; finite speed of the entire support would be stronger and generally false.')
item(168,'P000274','construction','A short-time phase and transport amplitude',
     r'The ansatz has phase \(\psi(x,y,\xi)-t a_1(y,\xi)\), \(\psi=(x-y,\xi)+O(|x-y|^2|\xi|)\), an amplitude expansion and a smoothing remainder.',
     r'Locally choose a homogeneous phase solving the appropriate eikonal equation and construct a classical amplitude by transport equations so that the oscillatory integral solves the half-wave equation modulo a smooth kernel for sufficiently small \(|t|\). In the local normal form used here, \(\psi\) satisfies \(a_1(x,d_x\psi)=a_1(y,\xi)\); signs are adjusted if the Fourier exponential is reversed. The condition \(\psi=(x-y)\cdot\xi+O(|x-y|^2|\xi|)\) alone would not determine a valid parametrix.',
     r'Exact construction: \citet[\S3, especially the phase and transport equations]{hormander1968spectral}.',
     ['hormander1968spectral'],reconstruction='The omitted eikonal and transport conditions supply the substantive hypotheses of the ansatz.')
item(168,'P000274-P000275','method','Fourier cutoff, smoothed spectral density and the Tauberian step',
     r'The smooth error \(E-Q\) is multiplied by \(\widehat\varrho(t)\); P000275 gives the convolution \(\int\varrho(\lambda-\mu)\,de(x,y,\mu)\) and defines \(R=\mathcal F^{-1}(q\widehat\varrho)\). A Marchenko Tauberian theorem is mentioned.',
     r'Choose \(\widehat\varrho\in C_c^\infty((-\varepsilon,\varepsilon))\). Fourier transformation of the localized smooth error is rapidly decreasing in the spectral variable. The remaining term is an oscillatory integral with amplitude \(R\). The diagonal spectral measure is positive; this positivity and a suitable cutoff permit a Tauberian estimate recovering the unsmoothed local counting bound. A displayed difference on P000275 is therefore a rapidly decreasing error, not an exact equality to zero.',
     r'The relevant estimates and Tauberian recovery are in \citet[\S4]{hormander1968spectral}; the notebook\textquotesingle s named Tauberian attribution is not needed to identify a separate theorem.',
     ['hormander1968spectral'],reconstruction='The order of the error, support of the cutoff and role of diagonal positivity are supplied explicitly.')
problems.append(dict(id='GP-1968-40',title='Higher spectral asymptotics with a specified smoothing order',
 statement=r'For a positive scalar elliptic operator with smooth coefficients, determine the asymptotic coefficients and remainder of its diagonal Riesz means of order \(\alpha\). The occurrence asks first about \(\alpha=1\), then about formal expansions; these are distinguished from a pointwise unsmoothed expansion.',
 occurrences=['1968-168.6'],status=r'As of November 2026: solved in the appropriate finite-order smoothed sense already by \citet[Theorem~4.5 and pp.~215--216]{hormander1968spectral}; the general unsmoothed full-expansion reading is false, as the sphere in 1968-168.5 shows. No earlier exact problem identifier is supplied in the previous index.',
 status_date='2026-11',refs=['hormander1968spectral','hormander1968riesz']))
correction('P000273','Sphere multiplicity numerator',r'\(C_{n+k}^{k}-C_{n+k}^{k-2}\).',r'\(\binom{n+k}{k}-\binom{n+k-2}{k-2}\).',r'The scan visibly repeats \(n+k\), confirming a faithful error. Harmonic homogeneous polynomials are the quotient of all degree-\(k\) polynomials by \(|x|^2\) times degree-\(k-2\) polynomials; compare \citet[\S6]{hormander1968spectral}.')
correction('P000273','Isolated leading Weyl coefficient for the sphere',r'\((2\pi)^{-n}\lambda^{n/2}/V_n\).',r'For standard Riemannian volume, the local coefficient is \[(2\pi)^{-n}\operatorname{vol}(B^n)\lambda^{n/2}.\] The global coefficient is this times \(\operatorname{vol}(S^n)\).',r'The scan has the displayed denominator. The symbol \(|\xi|^2\) gives a unit cotangent ball; \(V_n\), used immediately above as sphere volume, cannot supply its reciprocal. This is a mathematical emendation.')
correction('P000273','Leading coefficient of the normalized average',r'\(\lambda^{-1}\int_0^\lambda e(x,x,\nu)d\nu=a_0\lambda^{n/m}+\cdots\).',r'The leading coefficient is \(\frac{m}{m+n}a_0\lambda^{n/m}\).',r'The scan omits the factor. Integrating the leading power \(\nu^{n/m}\) gives the factor \((1+n/m)^{-1}\); direct symbolic integration independently checks it.')
correction('P000273','Off-diagonal shorthand',r'\ru{Вне диагонали 0}.',r'Zero leading normalized coefficient off the diagonal, rather than zero spectral kernel.',r'The scan supports the words. The local oscillatory formula in \citet[Theorem~5.1]{hormander1968spectral} gives the intended meaning; the literal unnormalized assertion is false.')
correction('P000274','Dikii bibliography',r'Dikii, UMN, 1957, on traces.',r'The identified review is Dikii, UMN 13(3), 1958, pp.~111--143.',r'The notebook visibly writes 1957. The Math-Net publisher record for \citet{dikii1958traces} gives 1958. The abbreviated Gelfand 1954 pointer is retained as unresolved rather than silently changed.',typ='provenance')
correction('P000273','Catalogue date for record 168','The supplied list gives 31-March-69 but labels the normalized date as absent.','1969-03-31.',r'The scan heading reads 31/III, between 10/II-1969 and 14/IV-69; the human-readable catalogue date agrees.',applies='both',typ='provenance')

talk(170,'1969-04-14','I. M. Gelfand','P000275-P000279',
     'Au-Yeung on a definite pair of Hermitian forms',
     r'This short intervention is first on P000276, before Davis, although its catalogue number is larger. The February 1969 Proceedings of the AMS reference identifies Au-Yeung precisely. The field and the meaning of simultaneous reduction need restoration: the complex Hermitian theorem concerns congruence, and it does not assert that both original forms are positive. The secondary handwritten linear-algebra book reference remains unidentified.')
item(170,'P000276','theorem','A pair without a common isotropic vector has a definite combination',
     r'If two quadratic forms are not simultaneously zero, rotate their pair of values so that one form is positive definite.',
     r'Let \(A,B\) be Hermitian \(n\times n\) complex matrices. If \(x^*Ax=x^*Bx=0\) implies \(x=0\), there exist real \(a,b\) with \(aA+bB>0\). For real symmetric matrices with the hypothesis tested only on real vectors, an additional dimension qualification is needed; the unrestricted two-dimensional version is false.',
     r'The named paper is \citet[pp.~545--548]{auyeung1969sphere}, published February 1969, before the talk. Its publisher contents and bibliographic identity were checked; the original article was not accessible. The exact complex assertion is independently readable in \citet[\S1, (1.1)]{guohighamtisseur2008arc}.',
     ['auyeung1969sphere','guohighamtisseur2008arc'],reconstruction=r'The complex field and exclusion of the zero vector are restored. A real counterexample is \(A=\operatorname{diag}(1,-1)\), \(B=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\): the forms have no common nonzero real zero, while every nonzero real combination is indefinite.',verification='read the result')
item(170,'P000276','method','The arc of normalized values and separation',
     r'The value pair \((x^*Ax,x^*Bx)\) is normalized; the resulting direction runs through no more than a semicircle.',
     r'For a complex Hermitian definite pair, \(W(A+iB)=\{x^*(A+iB)x:\|x\|=1\}\) is compact and convex and excludes zero. Strict separation from zero puts its directions in a closed arc of length strictly less than \(\pi\). The separating real functional gives a positive definite combination.',
     r'This is the geometric method associated with \citet{auyeung1969sphere}. The arc statement and its use in definite-pair algorithms are explicit in \citet[Lemma~2.1 and \S2]{guohighamtisseur2008arc}; that 2008 preprint is a later exposition and development, not the date of the theorem.',
     ['auyeung1969sphere','guohighamtisseur2008arc'],reconstruction='Compact numerical-range separation supplies the missing strictness; containment in an arbitrary closed semicircle alone would yield only semidefiniteness.')
item(170,'P000276','construction','Simultaneous diagonalization by congruence',
     r'The forms can be simultaneously reduced \ru{к сумме квадратов}.',
     r'Under the definite-pair hypothesis, there is an invertible complex \(S\) with \(S^*AS\) and \(S^*BS\) both real diagonal. Choose \(C=aA+bB>0\), use \(C^{-1/2}\) to make \(C\) the identity, then diagonalize the other Hermitian member by a unitary matrix. The diagonal coefficients of the original forms need not all be nonnegative.',
     r'The precise congruence convention is also spelled out by \citet[p.~81]{auyeung1970diagonalization}. The elementary reduction explains the conclusion of the February 1969 paper without inferring positivity of both forms.',
     ['auyeung1969sphere','auyeung1970diagonalization'],reconstruction='The displayed construction is an editorial verification of a standard consequence, not a claim that this proof was written in the notebook.',verification='read the result')
correction('P000276','Au-Yeung hypothesis and conclusion',r'Two quadratic forms not simultaneously zero; simultaneous reduction to a sum of squares.',r'Specify complex Hermitian forms, nonzero test vectors and simultaneous congruence to diagonal forms with real coefficients.',r'The scan writes \(x^*Ax\) and \(x^*Bx\) but omits the field and the nonzero condition. A two-dimensional real counterexample is given in item 1968-170.1. A definite combination does not make both original forms positive.')
correction('P000276','Source order of records 169 and 170','The catalogue lists Davis (169) before Gelfand (170).','Read record 170 before record 169 in the occurrence index.','The Gelfand heading and Au-Yeung paragraph precede the Davis heading on the same scan.',typ='provenance')

talk(169,'1969-04-14','Chandler Davis','P000275-P000277',
     'The shell of a Hilbert-space operator',
     r'P000276--P000277 give a compact account of \citet{davis1968shell}: an operator is replaced by a linear relation, its quadratic data are normalized to a subset of the three-dimensional ball, and norm, eigenvalues, M\"obius transformations and disk spectral sets become geometric features of that shell. The paper was published in 1968, before this lecture. P000278 already starts Buchstaber.')
item(169,'P000276','definition','Operators as linear relations',
     r'The graph is written \((y,x)\), \(y=Ax\); a more general relation is \(\alpha\subset H\oplus H\).',
     r'Let \(H\) be a complex Hilbert space. A linear relation is a linear subspace \(\alpha\subset H\oplus H\), written in output--input order \((y,x)\). A closed operator has closed graph \(\alpha=\{(Ax,x):x\in\operatorname{Dom}A\}\); a general closed relation may be multivalued and need not have dense domain.',
     r'This is the framework of \citet[\S\S1--2]{davis1968shell}, already published in 1968.',
     ['davis1968shell'],reconstruction='Linearity, and closedness where spectral conclusions require it, are added to the bare word set. An arbitrary subset is not the relevant notion of relation.')
item(169,'P000276','definition','Norm ratios, numerical range and point spectrum',
     r'Three numerical data are listed: norm ratios, \(w(A)\), and \(\sigma_p(A)\). The eigenvalue quantifier has no \(x\ne0\).',
     r'For a bounded operator \(A\), \(\|A\|^2=\sup_{x\ne0}\|Ax\|^2/\|x\|^2\), \(W(A)=\{\langle Ax,x\rangle/\|x\|^2:x\ne0\}\), and \(\sigma_p(A)=\{\lambda:\exists x\ne0,\ Ax=\lambda x\}\). The Hilbert inner product is taken linear in its first argument so that it agrees with the notebook\textquotesingle s \(x^*Ax\).',
     r'These classical invariants are the starting data in \citet[\S1]{davis1968shell}, not new definitions originating at this seminar.',
     ['davis1968shell'],correctness='correct with missing hypotheses',reconstruction='The nonzero eigenvector condition is essential; without it the displayed point spectrum would be all of the scalar field.')
item(169,'P000276','construction','The indicatrix cone',
     r'\(\{(\|Ax\|^2,x^*Ax,\|x\|^2):x\ne0\}\subset\mathbb R\times\mathbb C\times\mathbb R\) is called a cone.',
     r'For a nonzero linear relation \(\alpha\), its indicatrix is the set of triples \((\|y\|^2,\langle y,x\rangle,\|x\|^2)\) over nonzero \((y,x)\in\alpha\). Scaling the pair scales the triple by a positive real number. Every triple satisfies \(|\langle y,x\rangle|^2\leq\|y\|^2\|x\|^2\).',
     r'Exact construction in \citet[Definition~1.1 and the preceding normalization]{davis1968shell}.',
     ['davis1968shell'],correctness='correct',reconstruction='The relation version makes the operator formula compatible with the subsequent projective action.')
item(169,'P000277','construction','The shell in the closed unit ball',
     r'The convenient section is \((\xi,h)=(2x^*Ax,(\|Ax\|^2-\|x\|^2))/(\|Ax\|^2+\|x\|^2)\), with \(|\xi|^2+h^2\leq1\).',
     r'Normalize each nonzero pair \((y,x)\in\alpha\) by \(t=\|y\|^2+\|x\|^2\): \[s(\alpha)=\{(2\langle y,x\rangle/t,(\|y\|^2-\|x\|^2)/t)\}.\] Cauchy--Schwarz gives \(s(\alpha)\subset\{(\xi,h):|\xi|^2+h^2\leq1\}\). This set need not be closed; closure must be written explicitly when used.',
     r'This is \citet[Definition~1.1]{davis1968shell}, with equivalent stereographic coordinates.',
     ['davis1968shell'],correctness='correct',reconstruction='Set braces, quantification and the distinction between the shell and its closure repair the abbreviated notation.')
item(169,'P000277','theorem','Boundary points recover eigenvalues',
     r'An eigenvector is obtained when the shell point belongs to the sphere; the eigenvalue is related by stereographic projection.',
     r'For bounded \(A\), put \(\tau(\lambda)=(2\lambda/(1+|\lambda|^2),(|\lambda|^2-1)/(1+|\lambda|^2))\). Then \(s(A)\cap S^2=\tau(\sigma_p(A))\). Equality in Cauchy--Schwarz forces \(Ax=\lambda x\), and conversely. The north pole represents the infinite value for general multivalued relations, not an eigenvalue of a bounded operator.',
     r'Exact match with \citet[Theorem~2.2]{davis1968shell}; Theorem~2.3 separately treats the approximate point spectrum using closure.',
     ['davis1968shell'],reconstruction='The bounded-operator statement avoids conflating eigenvalues with approximate eigenvalues or the extra point at infinity.')
item(169,'P000277','claim','Height bounds encode an upper norm bound',
     r'If the shell does not go above \((a^2-1)/(a^2+1)\), then \(a\) is the norm.',
     r'For \(a\geq0\) and bounded \(A\), \[\|A\|\leq a\quad\Longleftrightarrow\quad h\leq\frac{a^2-1}{a^2+1}\text{ for every }(\xi,h)\in s(A).\] Equality \(\|A\|=a\) holds when \(a\) is the least such bound; the supremum need not be attained.',
     r'The shell formulation of the norm is in \citet[\S1 and Definition~7.1]{davis1968shell}. It also follows by solving the normalized ratio for \(\|Ax\|^2/\|x\|^2\).',
     ['davis1968shell'],correctness='false as written',reconstruction=r'The notebook\textquotesingle s asserted equality is replaced by the correct inequality and a separate minimality condition.')
item(169,'P000277','construction','Fractional linear transformations of relations',
     r'\(\mu(\lambda)=(a\lambda+b)/(c\lambda+d)\), \(ad-bc\ne0\), acts by \((y,x)\mapsto(ay+bx,cy+dx)\).',
     r'For complex \(a,b,c,d\) with \(ad-bc\ne0\), this invertible bounded block transformation sends a closed linear relation to a closed linear relation \(\mu(\alpha)\). If \(A\) is bounded and \(cA+dI\) is boundedly invertible, the transformed graph is the graph of \((aA+bI)(cA+dI)^{-1}\).',
     r'Exact relation calculus in \citet[\S5]{davis1968shell}.',
     ['davis1968shell'],correctness='correct with missing hypotheses',reconstruction='The inverse condition and identity operators are made explicit; the relation construction continues to exist when an operator formula does not.')
item(169,'P000277','theorem','Möbius equivariance of the shell',
     r'Theorem 1 states \(s(\mu(\alpha))=\varrho_\mu(s(\alpha))\).',
     r'Act on the positive Hermitian Gram matrix \(G=\left(\begin{smallmatrix}\|y\|^2&\langle y,x\rangle\\\langle x,y\rangle&\|x\|^2\end{smallmatrix}\right)\) by \(G\mapsto M G M^*\), \(M=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\), then divide by its trace. The resulting projective transformation \(\varrho_\mu\) of the closed ball satisfies the notebook\textquotesingle s identity and restricts on the boundary to stereographic conjugation of \(\mu\).',
     r'This is \citet[Theorem~5.1]{davis1968shell}.',
     ['davis1968shell'],reconstruction='The Gram-matrix construction defines the otherwise unnamed ball transformation; it is not an arbitrary analytic map of a three-dimensional ball.')
item(169,'P000277','definition','Spectral sets and the rational functional calculus',
     r'\(X\) is spectral when every rational \(f\) with \(f(X)\subset D\) satisfies \(\|f(A)\|\leq1\).',
     r'In the standard bounded-operator formulation, a closed set \(X\subset\mathbb C\) containing \(\sigma(A)\) is a spectral set if \(\|f(A)\|\leq\sup_X|f|\) for every rational function with poles off \(X\). The unit-disk formulation is equivalent by rescaling. For general relations and subsets of the Riemann sphere, use Davis\textquotesingle s Definition~7.2, including his convention for rational transforms.',
     r'\citet[Definitions~7.1--7.2]{davis1968shell} makes the quantifiers precise and explicitly traces the underlying spectral-set theory to earlier work.',
     ['davis1968shell'],reconstruction='The spectrum-containment and pole restrictions prevent an undefined rational calculus from being mistaken for a condition.')
item(169,'P000277','theorem','Disk spectral sets are detected by spherical caps',
     r'Theorem 2 says that, when \(\tau(X)\) is a spherical segment, \(X\) is spectral exactly when \(s(A)\subset\operatorname{conv}(\tau(X))\).',
     r'For a closed linear relation in Davis\textquotesingle s sense and a closed generalized disk \(X\) in the Riemann sphere (a finite disk, a half-plane with infinity, or the exterior of an open disk with infinity), \[X\text{ is a spectral set}\quad\Longleftrightarrow\quad s(\alpha)\subset\operatorname{conv}(\tau(X)).\] For bounded \(A\) and a finite disk \(X=\{z:|z-z_0|\leq r\}\), this is equivalently \(\|A-z_0I\|\leq r\). The spherical segment is a two-dimensional cap, not an arc.',
     r'Exact match: \citet[Theorem~7.2; preceding cases (i)--(iii)]{davis1968shell}.',
     ['davis1968shell'],reconstruction='The disk restriction is essential. The notebook does not claim this criterion for arbitrary closed spectral sets.')
correction('P000276','Definition of point spectrum',r'\(\exists x\;Ax=\lambda x\).',r'\(\exists x\ne0\;Ax=\lambda x\).','The scan has no nonzero restriction. Without it the zero vector makes every scalar an eigenvalue.')
correction('P000277','Height and norm','If the shell stays below the displayed height, then a is the norm.',r'Then \(\|A\|\leq a\); equality requires the least admissible bound.',r'The scan faithfully states equality. Substitution of \(A=0\) and \(a=1\) gives a counterexample to that literal implication.')
correction('P000277','Spherical segment in Theorem 2','A segment (spherical).','A spherical cap, namely the stereographic image of a generalized disk.',r'Russian \ru{сегмент (сферич.)} and the identified Theorem~7.2 of \citet{davis1968shell} determine the dimensional meaning; an arc is not intended.',applies='en',typ='translation')

talk(171,'1969-04-14','V. M. Buchstaber','P000277-P000281',
     'Finiteness of smooth homotopy tori and surgery',
     r'P000278--P000280 outline the reduction of the classification of homotopy tori to stable normal data, a finite Hurewicz fibre and surgery. The notebook conflates \(K_1\) with the Whitehead group and suppresses dimension and normal-data hypotheses. A closely matching report by Buchstaber and Mishchenko at the Moscow Mathematical Society on 22 April 1969 explicitly attributes the decisive algebraic methods to Wall and Shaneson; this is evidence of exposition of a current result, not an orphan theorem of Buchstaber. The concluding surgery step is an outline, not a proof supplied by the notes.')
item(171,'P000278','theorem','Finitely many smooth manifolds of torus homotopy type',
     r'There are finitely many smooth manifolds of homotopy type \(T^n\), up to diffeomorphism.',
     r'For each fixed \(n\geq5\), only finitely many diffeomorphism classes of closed connected smooth \(n\)-manifolds are homotopy equivalent to \(T^n=(S^1)^n\). This is a finiteness statement, not uniqueness in the smooth or PL category.',
     r'\citet[Theorem~A]{hsiangshaneson1969fake}, communicated 6 January and published March 1969, gives PL finiteness. The passage to smooth finiteness is an additional deduction: on a fixed finite PL complex the smoothing choices and differences are controlled by finitely many cochains with finite sphere-smoothing groups, and concordant smoothings are diffeomorphic \citep[Theorems~1.1, 3.1, 4.2, 5.1]{hirsch1963obstruction}. The finiteness input is supplied by Kervaire--Milnor and the low-dimensional Cerf theorem \citep{kervairemilnor1963spheres,cerf1968gamma4}. Thus E uses these prior ingredients, not the PL theorem alone. The exact smooth statement is reported in \citet[p.~224, meeting of 22 April]{buchstabermishchenko1969tori}; that later meeting is confirmation, not evidence of prior publication. Subsequent topological uniqueness is \citet[main theorem]{hsiangwall1969tori}, received 14 May 1969. These dates distinguish prior results, the seminar exposition and later topological strengthening.',
     ['hsiangshaneson1969fake','buchstabermishchenko1969tori','hsiangwall1969tori','hirsch1963obstruction','kervairemilnor1963spheres','cerf1968gamma4'],reconstruction='Closedness and the high-dimensional range are restored; the notebook is not evidence for a four-dimensional classification.',problem='GP-1968-42')
item(171,'P000278','theorem','Simply connected finiteness with fixed characteristic data',
     r'Novikov: homotopy type and Pontryagin classes determine a simply connected manifold up to finitely many possibilities.',
     r'Fix a closed simply connected smooth manifold \(M^n\), \(n\geq5\). Among closed smooth \(N^n\) with an orientation-preserving homotopy equivalence \(f:N\to M\) satisfying \(p_i(N)=f^*p_i(M)\) in rational cohomology, there are only finitely many diffeomorphism types. Neither arbitrary fundamental groups nor dimension four are covered by this assertion.',
     r'\citet[Introduction and classification theorem, pp.~366--367]{novikov1964homotopy}, received 22 March 1963 and published 1964, develops the tangential homotopy classification; its finiteness consequence with rational Pontryagin data is also stated in the author\textquotesingle s research summary \citep[Topology]{novikov2014bibliography}.',
     ['novikov1964homotopy','novikov2014bibliography'],reconstruction='The rational characteristic classes are compared under a specified homotopy equivalence. This does not say that the classes alone determine the homotopy type.')
item(171,'P000278','remark','Homotopy spheres as the simply connected model',
     r'Milnor\textquotesingle s sphere case is mentioned, with dimensions three and four marked unknown.',
     r'For \(n\geq5\), the oriented diffeomorphism classes of smooth homotopy \(n\)-spheres form a finite abelian group \(\Theta_n\) under connected sum, identified with the corresponding oriented h-cobordism classes. The notebook\textquotesingle s historical uncertainty in low dimensions is not extended into an assertion about their present status.',
     r'\citet[Theorems~1.1--1.2]{kervairemilnor1963spheres}, received 19 April 1962 and published in May 1963, is the precise antecedent. The earlier companion occurrence 1966-92.2 treats the seven-dimensional example; this is a related exposition, not a new unresolved sphere problem.',
     ['kervairemilnor1963spheres'],reconstruction='Only the high-dimensional theorem needed in this talk is asserted; h-cobordism and diffeomorphism are separated before using the dimension hypothesis.')
item(171,'P000278','definition','h-cobordism',
     r'Both \(M_i^n\subset W^{n+1}\) are deformation retracts and \(\partial W=M_1\cup M_2\).',
     r'A smooth h-cobordism \((W;M_1,M_2)\) is a compact smooth cobordism whose two boundary inclusions are homotopy equivalences. For oriented manifolds the boundary convention is \(\partial W=M_1\sqcup(-M_2)\); collars make the inclusions cofibrations, so the homotopy-equivalence formulation is compatible with deformation retractions.',
     r'This is the established framework in \citet[\S\S9,11]{milnor1966torsion}; the English survey appeared in 1966 and the checked Russian translation in 1967.',
     ['milnor1966torsion'],correctness='correct with missing hypotheses',reconstruction='Compactness, collars and orientation signs are made explicit.')
item(171,'P000278','theorem','The s-cobordism classification',
     r'Under Smale\textquotesingle s name, an h-cobordism is determined by one boundary and an invariant \(\alpha\in\operatorname{Wh}(\pi_1M_1)\).',
     r'If \(M^n\) is closed and connected, \(n\geq5\), smooth h-cobordisms on \(M\), modulo diffeomorphism relative to the incoming boundary, are classified by their Whitehead torsion in \(\operatorname{Wh}(\pi_1M)\). In particular, torsion zero is equivalent to a product cobordism relative to that boundary.',
     r'\citet[\S11, existence and uniqueness theorems]{milnor1966torsion} gives the classification. The non-simply-connected result is the s-cobordism theorem (Barden--Mazur--Stallings); attributing the full statement solely to Smale suppresses the essential extension.',
     ['milnor1966torsion'],reconstruction='Relative equivalence, dimension and the distinction from the simply connected h-cobordism theorem are restored.')
item(171,'P000278-P000279','definition','Stable general linear groups, K1 and Whitehead groups',
     r'The inductive general linear group is abelianized; \(\operatorname{Wh}\) is obtained by a further quotient. A noncommutative determinant is mentioned.',
     r'For a unital ring \(R\), let \(GL(R)=\varinjlim_m GL_m(R)\) under \(A\mapsto\operatorname{diag}(A,1)\), and let \(E(R)\) be the stable elementary subgroup. Then \(E(R)=[GL(R),GL(R)]\), \(K_1(R)=GL(R)/E(R)\), and \(\operatorname{Wh}(\pi)=K_1(\mathbb Z[\pi])/\langle[\pm g]:g\in\pi\rangle\). Dieudonn\'e\textquotesingle s determinant over a division ring is an analogy, not a literal determinant on an arbitrary group ring.',
     r'\citet[\S1, Whitehead lemma; \S6]{milnor1966torsion} states these constructions before the talk.',
     ['milnor1966torsion'],reconstruction='The ring-level and group-level Whitehead terminology is disambiguated, which is necessary for the next claim.')
item(171,'P000279','claim','The Whitehead group of a free abelian group vanishes',
     r'The scan explicitly writes \(K_1(\mathbb Z+\cdots+\mathbb Z)=0\), with a gloss referring to the group ring, and attributes it to Bass.',
     r'For \(\pi=\mathbb Z^n\), \(R=\mathbb Z[\pi]=\mathbb Z[t_1^{\pm1},\ldots,t_n^{\pm1}]\), one has \(K_1(R)\simeq R^\times\simeq\{\pm1\}\times\mathbb Z^n\). Consequently \(\operatorname{Wh}(\mathbb Z^n)=0\), but \(K_1(R)\) is not zero.',
     r'Exact corrected theorem: \citet[p.~63, corollaries]{basshellerswan1964whitehead}, received 15 June 1963 and published 1964. Quotienting the surviving trivial units is the missing step.',
     ['basshellerswan1964whitehead'],correctness='false as written',reconstruction='The zero group is the Whitehead quotient. The plus signs denote a direct sum of infinite cyclic groups, not a direct sum of coefficient rings.')
item(171,'P000279','claim','Invertible polynomial and Laurent-polynomial matrices',
     r'For polynomial matrices, invertibility is said to be equivalent to determinant \(\pm1\); elementary reduction after increasing size is discussed.',
     r'Over the commutative polynomial ring \(\mathbb Z[t_1,\ldots,t_n]\), a square matrix is invertible exactly when its determinant is \(\pm1\). Over the group ring \(\mathbb Z[\mathbb Z^n]\), the units instead are \(\pm t_1^{a_1}\cdots t_n^{a_n}\), \(a_i\in\mathbb Z\). Stable elementary reduction detects the zero class in \(K_1\), and does not mean every invertible matrix already has determinant one.',
     r'The unit distinction and stable \(K_1\) calculation are precisely the setting of \citet[pp.~61--63]{basshellerswan1964whitehead}. The determinant criterion follows from the adjugate identity.',
     ['basshellerswan1964whitehead'],reconstruction='The literal polynomial assertion is correct; applying it unchanged to the preceding Laurent group ring is not.')
item(171,'P000279','theorem','Stabilization at sufficiently large matrix size',
     r'Bass: it suffices to restrict to matrices of sufficiently high order.',
     r'For a commutative Noetherian ring \(R\) of finite Krull dimension, there exists a uniform \(m_0(R)\) such that every element of \(K_1(R)\) has a representative in \(GL_m(R)\) for every \(m\geq m_0(R)\). In particular this applies to \(\mathbb Z[t_1^{\pm1},\ldots,t_n^{\pm1}]\). This is a surjective stabilization statement; it does not by itself assert that every elementary equivalence is detected without further stabilization.',
     r'The precise pre-existing result is \citet[Theorem~11.1 and Proposition~11.2(b)]{bass1964stable}. Immediately after that proposition Bass separately formulates injective stabilization as a conjecture; the two assertions must not be retroactively conflated.',
     ['bass1964stable'],reconstruction='The ring hypotheses and uniform bound are restored; the weaker representability claim is all that the terse sentence needs. No unstated optimal bound or injectivity theorem is assigned to the speaker.')
item(171,'P000279','definition','Stable normal data under a homotopy equivalence',
     r'An embedding \(M^n\subset\mathbb R^N\) gives \(\nu_M\), independent of the embedding stably; equivalence includes \(f^*\nu_{M_2}=\nu_{M_1}\).',
     r'For a smooth embedding, \(TM\oplus\nu_M\cong\varepsilon^N\); thus the stable class \([\nu_M]-[\varepsilon^{N-n}]=-([TM]-[\varepsilon^n])\) is intrinsic. A tangential homotopy equivalence consists of a homotopy equivalence together with a stable identification of the pulled-back tangent, or equivalently normal, bundles.',
     r'These are the normal data used by \citet[Introduction and Ch.~I]{novikov1964homotopy}.',
     ['novikov1964homotopy'],correctness='correct with missing hypotheses',reconstruction='Equality means stable bundle isomorphism over a specified map; it is stronger than equality of rational Pontryagin classes.')
item(171,'P000279','claim','Pontryagin classes and parallelizability of homotopy tori',
     r'Adams\textquotesingle s J-functor and Novikov\textquotesingle s torus invariance are invoked; \(\nu_M=0\) is underlined.',
     r'For a smooth homotopy torus in the high-dimensional range, the rational Pontryagin classes vanish, and the classification of fake tori supplies stable triviality of the normal bundle. These are distinct statements: vanishing of rational characteristic classes alone does not prove integral stable triviality for a general manifold.',
     r'\citet[\S1]{novikov1966abelian} provides the relevant free-abelian and Pontryagin-class framework. The modern classification records parallelizability explicitly in \citet[p.~2212, Remark~1]{hambleton2006tori}. The notebook\textquotesingle s unnamed Adams reference is insufficient to identify a particular J-theorem with all its hypotheses.',
     ['novikov1966abelian','hambleton2006tori'],reconstruction='The conclusion is separated from the abbreviated argument. No proof of stable triviality from rational classes alone is accepted.',match='partial',confidence='medium')
item(171,'P000279','claim','Infinitely many manifolds with the homotopy type of S2 times S4',
     r'\ru{на \(S^2\times S^4\) бесконечно много гладких структур}.',
     r'There are infinitely many pairwise nondiffeomorphic closed smooth manifolds homotopy equivalent to \(S^2\times S^4\), with different rational Pontryagin data. This must not be read as infinitely many smoothings of one fixed topological \(S^2\times S^4\). In dimension six that fixed topological-manifold smoothing problem has only finitely many possibilities.',
     r'\citet[Introduction, consequences 1--2, pp.~208--209]{novikov1966abelian} explicitly distinguishes finiteness for a fixed simply connected topological manifold from infinitude within an appropriate homotopy type.',
     ['novikov1966abelian'],correctness='false as written',reconstruction='On is interpreted as of the homotopy type of. The corrected meaning fits the surrounding comparison of characteristic classes.')
item(171,'P000279-P000280','construction','Pontryagin--Thom collapse and the degree-one fibre',
     r'A tubular neighbourhood is collapsed to obtain \(S^N\to T_{\nu_M}\), whose Hurewicz image is \(+1\).',
     r'An oriented embedding and tubular neighbourhood give a collapse \(c_M:S^N\to\operatorname{Th}(\nu_M)\). The Thom isomorphism sends the image of \([S^N]\) to \([M]\), so the Hurewicz image is the chosen generator of \(\widetilde H_N(\operatorname{Th}(\nu_M);\mathbb Z)\cong\mathbb Z\). Homotopy-equivalent bases yield equivalent Thom spaces only when the relevant normal bundles have been identified stably over that equivalence.',
     r'This is the explicit method of \citet[pp.~366--367; Ch.~I, \S3]{novikov1964homotopy}.',
     ['novikov1964homotopy'],reconstruction='The normal-bundle identification in the preceding page is retained; homotopy type of the base by itself is insufficient.')
item(171,'P000280','claim','Stable torus splitting and finiteness of H inverse of one',
     r'\(T_\nu(T^n)=\Sigma^{N-n}T^n=S^N\vee\bigvee_{i<N}S^i\); \(H^{-1}(1)\) is called a finite group and Serre is cited.',
     r'For the trivial rank \(r=N-n\geq1\) bundle, \[\operatorname{Th}(\varepsilon^r_{T^n})\simeq\Sigma^r(T^n)_+\simeq\bigvee_{j=0}^n\bigvee^{\binom nj}S^{r+j}.\] Choose \(N>2n+1\) to lie in the stable range. The Hurewicz map \(\pi_N(\operatorname{Th}(\varepsilon^{N-n}_{T^n}))\to\mathbb Z\) is projection onto the top-sphere summand, with finite kernel because the other summands are positive stable stems. Its fibre over one is a finite torsor for that kernel, not a subgroup.',
     r'The finite-fibre mechanism is already used in \citet[p.~366]{novikov1964homotopy}; Novikov invokes Serre\textquotesingle s homotopy-finiteness theorem. The classes-of-groups framework and sphere applications are developed in \citet[Chs.~I--IV]{serre1953classes}.',
     ['novikov1964homotopy','serre1953classes'],correctness='false as written',reconstruction='A disjoint basepoint, wedge multiplicities, stable-range choice and the affine nature of the fibre are supplied. The statement is restricted to the torus case, not all possible Thom spaces.')
item(171,'P000280','method','From normal cobordism to h-cobordism by surgery',
     r'A homotopy between collapse maps produces a film; one must arrange retractions, classify films of finite index and use obstruction theory for modifications.',
     r'A transverse homotopy of collapse maps with fixed normal data produces a normal cobordism. It need not be an h-cobordism. In dimensions at least five, surgery seeks to make the boundary inclusions homotopy equivalences; middle-dimensional surgery obstructions and the action on the structure set must be analyzed. Once an h-cobordism is obtained for fundamental group \(\mathbb Z^n\), its Whitehead torsion vanishes and the s-cobordism theorem makes it a product.',
     r'The simply connected model is \citet[Ch.~I]{novikov1964homotopy}; the torus classification requires the non-simply-connected methods in \citet{hsiangshaneson1969fake}. The near-contemporary Buchstaber--Mishchenko abstract explicitly names Wall and Shaneson\textquotesingle s algebraic methods \citep[p.~224]{buchstabermishchenko1969tori}.',
     ['novikov1964homotopy','hsiangshaneson1969fake','buchstabermishchenko1969tori'],reconstruction='The missing surgery step is identified, not filled in as though the notebook contained a complete proof.',problem='GP-1968-42',match='partial')
correction('P000278','Attribution of torsion classification','Smale: an h-cobordism is classified by a boundary and an element of Wh.',r'The general fundamental-group statement is the s-cobordism theorem, relative to one boundary, in boundary dimension at least five.',r'The scan is faithful. \citet[\S11]{milnor1966torsion} distinguishes the general torsion classification from Smale\textquotesingle s simply connected theorem.',typ='provenance')
correction('P000279','Bass vanishing assertion',r'\(K_1(\mathbb Z+\cdots+\mathbb Z)=0\) for the group ring.',r'\(\operatorname{Wh}(\mathbb Z^n)=0\), while \(K_1(\mathbb Z[\mathbb Z^n])\cong\{\pm1\}\times\mathbb Z^n\).',r'The scan clearly has \(K_1\) and \(=0\). The corollaries on p.~63 of \citet{basshellerswan1964whitehead} identify the surviving units; this is a mathematical emendation.')
correction('P000279','Polynomial determinant in the group-ring context',r'Invertibility iff \(\det=\pm1\).',r'This is correct for ordinary integer polynomials; for Laurent polynomials the determinant may be any \(\pm t_1^{a_1}\cdots t_n^{a_n}\).','The scan says polynomials, so the isolated sentence is correct. The preceding group ring is Laurent; the correction records the necessary change when it is applied there.',typ='ambiguity')
correction('P000279','Meaning of infinitely many structures',r'Infinitely many smooth structures on \(S^2\times S^4\).',r'Infinitely many smooth manifolds of that homotopy type, distinguished by rational Pontryagin classes.',r'\citet[pp.~208--209]{novikov1966abelian} states both the fixed-topological-manifold finiteness and homotopy-type infinitude. The scan\textquotesingle s shorthand conflates them.')
correction('P000280','Common Thom space','Thom spaces are homotopy equivalent because their bases are homotopy equivalent.','Include the stable pullback identification of normal bundles written on the preceding page.','A homotopy equivalence of bases alone does not identify arbitrary vector bundles or their Thom spaces. The context supplies normal data, but the isolated implication is invalid.')
correction('P000280','Torus Thom space',r'\(T_\nu(T^n)=\Sigma^{N-n}T^n\).',r'\(\operatorname{Th}(\varepsilon^{N-n}_{T^n})=\Sigma^{N-n}(T^n)_+\).','The scan has no basepoint symbol. Without a disjoint basepoint the bottom sphere summand of the Thom space is lost.')
correction('P000280','Hurewicz fibre',r'\(H^{-1}(1)\), finite group for all manifolds.',r'In the stated stable torus setting, a finite fibre, naturally a torsor for \(\ker H\).','The scan clearly calls the fibre a group. It excludes the zero element and is not closed under addition; the general all-manifolds assertion needs additional hypotheses.')

talk(172,'1969-04-21','A. A. Kirillov','P000279-P000282',
     'A noncompact Borel--Weil--Bott theorem',
     r'The single mathematical page P000281 describes homogeneous line bundles on \(G/H\), harmonic \(L^2\) Dolbeault forms and discrete-series representations in a degree determined by compact and noncompact roots. The precise comparison is with the Griffiths--Schmid vanishing theorem and Schmid\textquotesingle s realization of sufficiently regular discrete series. The 1968 Schmid announcement concerns related homogeneous-cohomology work; it is not used as proof that every part of the 1969 notebook theorem had already been printed. The broader Langlands realization was settled later, and the second conjecture is named without a separate formula in the notes.')
item(172,'P000281','construction','An equal-rank homogeneous complex manifold',
     r'\(G\supset K\supset H\), \(\operatorname{rank}G=\operatorname{rank}K\); \(D=G/H\) is complex. The example is \(GL(2,\mathbb R)\), although \(G\) is called semisimple.',
     r'Let \(G\) be a connected real semisimple group with finite centre, \(K\) a maximal compact subgroup and \(H\subset K\) a compact Cartan subgroup of \(G\). Equivalently the complex ranks of \(G\) and \(K\) agree. A choice of positive roots for \((\mathfrak g_{\mathbb C},\mathfrak h_{\mathbb C})\) determines an invariant integrable complex structure on \(D=G/H\), realized as an open flag-domain orbit. A valid rank-one example is \(SL(2,\mathbb R)/SO(2)\).',
     r'The construction is established in \citet[\S\S1--2]{griffithsschmid1969locally}; that manuscript was received 3 April 1969, before the talk, assigned to Acta volume 123 (1969), and bears the print date 23 January 1970. The 1967 thesis and January 1968 announcement are distinct earlier stages \citep{schmid1968homogeneous}.',
     ['griffithsschmid1969locally','schmid1968homogeneous'],correctness='false as written',reconstruction=r'\(GL(2,\mathbb R)\) has a nontrivial central Lie algebra and is not semisimple. It is retained as a faithful notebook error, not silently read as \(SL_2\).')
item(172,'P000281','claim','The Weyl-group count concerns invariant structures',
     r'The number of complex structures equals the number of Weyl-group elements.',
     r'With a fixed compact Cartan and fixed identification of tangent root spaces, invariant integrable complex structures on \(G/H\) correspond to positive systems of the complex root system, hence there are \(|W|\) such marked structures. Passing to equivalence under diffeomorphisms or dropping invariance changes the counting problem.',
     r'The positive-root construction is explicit in \citet[\S1]{griffithsschmid1969locally}; the Weyl group acts simply transitively on positive systems.',
     ['griffithsschmid1969locally'],reconstruction='The word invariant and the marking convention are necessary; this is not a count of all complex structures on the underlying smooth manifold.')
item(172,'P000281','construction','Homogeneous line bundles from Cartan characters',
     r'\(\mathcal L_\lambda\) has fibre \(\mathbb C\); a one-dimensional representation of \(H\) determines it, with a Frobenius-reciprocity aside.',
     r'An integral character \(\chi_\lambda:H\to U(1)\) gives \(\mathcal L_\lambda=G\times_H\mathbb C_{\chi_\lambda}\to G/H\), with the holomorphic structure fixed by the chosen positive system. Sections are equivariant functions, with \(f(gh)=\chi_\lambda(h)^{-1}f(g)\) for this associated-bundle convention. Induction and Frobenius reciprocity explain the representation-theoretic interpretation; arbitrary unintegrated Lie-algebra weights do not necessarily define a bundle on the given group.',
     r'\citet[\S\S1,4]{griffithsschmid1969locally} treats the homogeneous bundle and its invariant Hermitian geometry.',
     ['griffithsschmid1969locally'],reconstruction='Integrality and the bundle convention are stated explicitly; signs of highest weights depend on this convention.')
item(172,'P000281','definition','Reduced L2 Dolbeault cohomology as harmonic forms',
     r'Compactly supported \((0,i)\)-forms, \(\bar\partial\), its adjoint and \(\Box\) are introduced; \(\ker\Box=\mathcal H^i(\mathcal L_\lambda)\) is called i-dimensional cohomology.',
     r'Choose invariant Hermitian metrics on \(G/H\) and \(\mathcal L_\lambda\). The complete homogeneous metric gives the closed \(L^2\) Dolbeault complex. In degree \(i\), reduced cohomology \(\ker\bar\partial_i/\overline{\operatorname{im}\bar\partial_{i-1}}\) is canonically the harmonic space \(\ker\Box_i\), where \(\Box=\bar\partial\bar\partial^*+\bar\partial^*\bar\partial\) has its natural self-adjoint realization. The superscript is cohomological degree, not vector-space dimension.',
     r'\citet[pp.~293--294, before Theorem~7.8]{griffithsschmid1969locally} defines the Hilbert space of harmonic forms and uses completeness. In the noncompact case a nonzero discrete-series realization is infinite-dimensional.',
     ['griffithsschmid1969locally'],reconstruction='The Hilbert completion is taken after the compactly supported test space; harmonic forms themselves are not required to have compact support. Reduced cohomology avoids silently assuming closed range.')
item(172,'P000281','theorem','The compact specialization is Borel--Weil--Bott',
     r'For compact \(G\), this is called the Borel--Weil theorem; Demazure is suggested as a reference.',
     r'For compact connected semisimple \(G\), a homogeneous holomorphic line bundle on its complete flag manifold has zero cohomology in every degree when the shifted weight \(\lambda+\rho\) is singular. For a regular shifted weight, exactly one cohomological degree can be nonzero, and it realizes the finite-dimensional irreducible representation determined by the shifted Weyl action. Dominant weights in the degree-zero convention give Borel--Weil.',
     r'The full higher-cohomology statement is the pre-existing Borel--Weil--Bott theorem; \citet[Theorem~6.1]{griffithsschmid1969locally} recalls it. The notebook\textquotesingle s unspecific Demazure pointer is not converted into an invented bibliographic entry.',
     ['griffithsschmid1969locally'],reconstruction='The compact higher-degree assertion is distinguished from the degree-zero Borel--Weil theorem; the sign convention is fixed by the bundle convention of the source.')
item(172,'P000281','theorem','Vanishing away from one degree for sufficiently regular weights',
     r'Theorem 1 requires \(|(\lambda,\alpha)|>b\) for every simple root, and says \(\mathcal H^i=0\) except at \(k(\lambda+\rho)\).',
     r'For the equal-rank flag domain with a fixed invariant metric, there is a constant \(b\) such that an integral weight satisfying \(|\langle\lambda,\alpha\rangle|>b\) for every root \(\alpha\) has harmonic \(L^2\) Dolbeault forms only in the degree \(q(\lambda+\rho)\). Enlarge \(b\) if necessary so that \(\lambda\) and \(\lambda+\rho\) lie in the same chamber. Conditions only on a fixed simple system with arbitrary signs do not ensure this distance from every wall.',
     r'The exact all-chamber vanishing result is \citet[Theorem~7.8]{griffithsschmid1969locally}; the manuscript was received 3 April 1969 but printed 23 January 1970. Receipt alone is not evidence of public circulation. The January 1968 announcement \citep[p.~57]{schmid1968homogeneous} proves a restricted antecedent for sufficiently high powers of a bundle in a fixed antidominant chamber, not this full formulation. B records the later exact publication by Griffiths and Schmid, distinct from the irreducibility theorem.',
     ['griffithsschmid1969locally','schmid1968homogeneous'],cls='B',correctness='correct with missing hypotheses',reconstruction='Every-root regularity replaces the insufficient literal simple-root condition. Opposite large simple-root pairings can cancel on a nonsimple positive root.')
item(172,'P000281','theorem','The remaining harmonic space realizes a discrete series',
     r'In the exceptional degree, Theorem 1 identifies \(\mathcal H^{k(\lambda+\rho)}(\mathcal L_\lambda)\) with \(\pi_{\lambda+\rho}\), as a partial answer to Langlands.',
     r'For sufficiently regular integral \(\lambda\) under the preceding hypotheses, the nonzero Hilbert representation of \(G\) on \(\mathcal H^{q(\lambda+\rho)}(\mathcal L_\lambda)\) is irreducible and is the discrete-series representation with Harish-Chandra parameter \(\lambda+\rho\), with the weight convention of the chosen holomorphic bundle.',
     r'\citet[Introduction, p.~255]{griffithsschmid1969locally} announces Schmid\textquotesingle s proof after completion of that manuscript; the full paper is \citet{schmid1971langlands}. \citet[\S3, Theorem~2]{schiffmann1971borel} states exactly the sufficiently regular result. The unrestricted harmonic realization is proved in \citet{schmid1976l2}, as explicitly confirmed in the author\textquotesingle s 1978 ICM address, published in 1980, p.~204 \citep{schmid1980representations}; the 1971 paper alone is not credited with the unrestricted theorem.',
     ['griffithsschmid1969locally','schmid1971langlands','schiffmann1971borel','schmid1976l2','schmid1980representations'],cls='B',reconstruction='The theorem is the precise first conjecture component recoverable from the notes. The full all-weights formulation in the problem index is identified from the cited literature, not quoted as notebook text.',problem='GP-1968-41',status='As of November 2026: this sufficiently regular realization is established; the general Langlands harmonic realization was proved by Schmid in 1976. No remaining open subproblem is inferred from this occurrence.',confidence='high')
item(172,'P000281','claim','The cohomological degree counts signed positive roots',
     r'Theorem 2 writes \(K(\mu)\) but uses \(\lambda\) on the right, counting compact roots with negative pairing and noncompact roots with positive pairing.',
     r'For a regular parameter \(\mu\), with positive roots partitioned as \(\Delta_c^+\sqcup\Delta_n^+\), \[q(\mu)=\#\{\alpha\in\Delta_c^+:\langle\mu,\alpha\rangle<0\}+\#\{\beta\in\Delta_n^+:\langle\mu,\beta\rangle>0\}.\] In the preceding realization use \(\mu=\lambda+\rho\). Counting both signs of every root would give a different, generally constant count.',
     r'The root-count convention already occurs in \citet[\S2, eq.~(2.1), p.~415]{griffiths1966locally}, followed by compact-quotient cohomology in \S3; it predates this talk. The precise later discrete-series convention is recorded in \citet[\S3, before Theorem~1]{schiffmann1971borel}; compare \citet[\S7]{griffithsschmid1969locally}.',
     ['griffiths1966locally','schiffmann1971borel','griffithsschmid1969locally'],correctness='false as written',reconstruction='The variable is made uniform and positive roots are specified. These changes are faithful-error emendations because the scan agrees with the transcription.')
item(172,'P000281','claim','The unspecified decay-at-infinity comparison',
     r'\ru{Если с убыванием на бесконечности --- будут те же когомологии}.',
     r'No exact comparison theorem is determined without a specified decay space, its topology, the closed extension of \(\bar\partial\), and the meaning of same cohomology. Harmonic \(L^2\), smooth Dolbeault, compactly supported and rapidly decreasing cohomology are different constructions and cannot simply be identified.',
     r'\citet[p.~293 and Introduction, p.~255]{griffithsschmid1969locally} explicitly treats comparison with ordinary cohomology as a separate issue; it does not validate every possible reading of this sentence. The notes leave the second Langlands conjecture similarly unnamed at formula level.',
     ['griffithsschmid1969locally'],cls='F',correctness='not determinable',match='thematic only',confidence='low',reconstruction='The possible function-space interpretations are alternatives, not silently supplied hypotheses.',status='As of November 2026: the exact assertion in this sentence remains unidentified from the surviving wording; this is an evidential limit, not a claim that a definite mathematical problem is open.')
problems.append(dict(id='GP-1968-41',title='The Langlands harmonic realization of the discrete series',
 statement=r'For a connected real semisimple group with finite centre and compact Cartan, determine the harmonic \(L^2\) Dolbeault cohomology of the homogeneous line bundle \(\mathcal L_\lambda\) on a fixed flag domain. The notes state the sufficiently regular case. The stronger literature formulation predicts vanishing for singular \(\lambda+\rho\), and otherwise a single nonzero degree \(q(\lambda+\rho)\) realizing the corresponding discrete series.',
 occurrences=['1968-172.7'],status=r'The notebook\textquotesingle s sufficiently regular theorem is established by Schmid\textquotesingle s work published in 1971; the 1976 paper proves the unrestricted \(L^2\) realization, as confirmed by the author\textquotesingle s ICM account, p.~204 \citep{schmid1980representations}. The all-weights formulation is an explicitly identified literature extension of this occurrence, not an additional conjecture transcribed from the notebook. The publisher metadata for both Annals papers was checked, and the exact early theorem was read in the Griffiths--Schmid paper and the 1971 Bourbaki exposition. The 1976 conclusion was checked against the author\textquotesingle s ICM account, not inferred merely from the title.',status_date='2026-11',refs=['griffithsschmid1969locally','schmid1971langlands','schmid1976l2','schiffmann1971borel','schmid1980representations']))
correction('P000281','Semisimple example',r'\(GL(2,\mathbb R)\), followed by real semisimple group.',r'A compatible example is \(SL(2,\mathbb R)\), with compact Cartan \(SO(2)\).',r'The scan clearly reads GL. Its scalar matrices give a nonzero centre of the Lie algebra, so the literal example is not semisimple.')
correction('P000281','Cohomological degree','i-dimensional L2 cohomology.','L2 cohomology in degree i.',r'Russian \ru{\(i\)-мерные} uses the older degree terminology here. The very next sentence distinguishes finite-dimensional compact cohomology from the noncompact case.',applies='en',typ='translation')
correction('P000281','Sufficient regularity',r'\(|(\lambda,\alpha)|>b\) for every simple root.',r'Require separation from every root hyperplane, or specify a chamber in which the simple-root conditions imply it.',r'\citet[Theorem~7.8]{griffithsschmid1969locally} uses all positive roots. In type \(A_2\), pairings \(M\) and \(-M\) with simple roots vanish on their sum.')
correction('P000281','Degree formula',r'\(K(\mu)\) with pairings against \(\lambda\); roots have no positivity restriction.',r'Use \(q(\mu)\) and pair with \(\mu\), counting only positive compact and positive noncompact roots.',r'The scan confirms the inconsistent variable and omitted positive-system qualifier. \citet[\S3]{schiffmann1971borel} gives the intended formula.')

talk(173,'1969-04-21','V. M. Buchstaber','P000280-P000284',
     'From finite h-cobordism classes to finite diffeomorphism classes',
     r'The actual continuation consists of three lines on P000282: finite h-cobordism classes of homotopy tori, the question of finitely many manifolds in each class, and Morse modifications. In the high-dimensional smooth setting the second step is stronger than finiteness: vanishing of \(\operatorname{Wh}(\mathbb Z^n)\) makes every h-cobordism a product. The catalogue range extends through P000284, but P000283 explicitly begins 15 September 1969 and P000284 includes 22 September; those later-year passages are inventoried as boundary material in the report, not attributed to Buchstaber on 21 April.')
item(173,'P000282','claim','Finitely many h-cobordism classes of homotopy tori',
     r'Manifolds of the homotopy type of a torus are divided into finitely many classes by h-cobordisms.',
     r'For each fixed \(n\geq5\), the closed connected smooth manifolds homotopy equivalent to \(T^n\) comprise finitely many smooth h-cobordism classes. The dimension, smooth category and unmarked equivalence relation are essential to this reading.',
     r'This follows from the PL classification of \citet[Theorem~A]{hsiangshaneson1969fake} together with the finite-smoothing deduction made explicit at occurrence 1968-171.1. It is not the PL theorem alone. The exact Moscow report is \citet[p.~224]{buchstabermishchenko1969tori}, from the following day, 22 April 1969.',
     ['hsiangshaneson1969fake','buchstabermishchenko1969tori'],reconstruction='The same high-dimensional, closed-manifold setting is carried over from the preceding lecture.',problem='GP-1968-42')
item(173,'P000282','problem','How many diffeomorphism types occur in one h-cobordism class?',
     r'\ru{Задача: показ., что в \(\forall\) классе конечн. число}.',
     r'Given a closed smooth homotopy \(n\)-torus, \(n\geq5\), prove that its smooth h-cobordism class contains only finitely many diffeomorphism types. In fact it contains exactly one: every h-cobordism has torsion in \(\operatorname{Wh}(\mathbb Z^n)=0\), and hence is a product by the s-cobordism theorem.',
     r'The two ingredients already predate the question: \citet[p.~63]{basshellerswan1964whitehead} and \citet[\S11]{milnor1966torsion}. Thus the question is a proof step in an exposition, not a remaining open problem.',
     ['basshellerswan1964whitehead','milnor1966torsion'],problem='GP-1968-42',reconstruction='Up to diffeomorphism is restored from record 171. The conclusion concerns unmarked boundary manifolds, not equality of all markings or parametrizations.',status='As of November 2026: resolved in the stated high-dimensional smooth setting, with exactly one diffeomorphism type per h-cobordism class.')
item(173,'P000282','method','Morse modifications of cobordisms',
     r'The simplest films are classified by Morse modifications.',
     r'A relative Morse function on a compact smooth cobordism gives a handle decomposition. Handle additions, slides and cancellation are the geometric operations used to simplify the relative chain complex and expose Whitehead torsion. The notebook does not give a new finite algorithm classifying arbitrary cobordisms.',
     r'This is the established method in \citet[\S\S9,11]{milnor1966torsion}.',
     ['milnor1966torsion'],reconstruction='The brief method label is expanded only to the standard handle-theoretic interpretation needed for the preceding problem.',match='partial')
problems.append(dict(id='GP-1968-42',title='Finiteness for smooth homotopy tori',
 statement=r'For fixed \(n\geq5\), are there finitely many diffeomorphism classes of closed connected smooth manifolds homotopy equivalent to \(T^n\)? The continuation isolates the subproblem of finiteness within one smooth h-cobordism class.',
 occurrences=['1968-171.1','1968-171.15','1968-173.1','1968-173.2'],
 status=r'Established. The 1969 fake-torus classification yields finitely many possibilities; the h-cobordism subproblem has the stronger answer one diffeomorphism type, by \(\operatorname{Wh}(\mathbb Z^n)=0\) and s-cobordism. Hsiang--Wall subsequently proved topological uniqueness in the high-dimensional range. None of these statements asserts smooth uniqueness or settles an unstated dimension-four problem.',status_date='2026-11',refs=['hsiangshaneson1969fake','buchstabermishchenko1969tori','hsiangwall1969tori','basshellerswan1964whitehead','milnor1966torsion']))
correction('P000282-P000284','End boundary of record 173','The supplied catalogue range for Buchstaber on 21 April 1969 is P000280--P000284.','The Buchstaber continuation ends on P000282. P000283--P000284 begin the next academic year.','P000283 has the explicit heading 15.9.69 and Vainberg; P000284 continues those remarks and introduces 22.IX with Fichera. The catalogue range overlaps later records; assigning these pages to record 173 would be a provenance error.',typ='provenance')

# All root records have now been serialized in actual source order.
if __name__ == '__main__':
 save()
