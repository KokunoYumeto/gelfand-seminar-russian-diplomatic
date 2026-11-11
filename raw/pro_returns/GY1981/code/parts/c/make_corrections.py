"""Corrections retain the distinction between transcription and source errors."""
import csv
from pathlib import Path

rows = []
def add(page,place,reads,should,evidence,applies='both',kind='ambiguity'):
    rows.append([page,place,reads,should,evidence,applies,kind])

add('P001001','Joint-work attribution','Schräder', 'Schrader in bibliographic identification; preserve the manuscript spelling diplomatically.',
    'Inspected scan; opened Cheeger--Müller--Schrader article and Springer chapter identify Robert Schrader.',kind='provenance')
add('P001001','Equation (2)',r'\(i\hbar\partial/\partial t=\widehat Hf\)',r'\(i\hbar\partial_t f=\widehat Hf\)',
    'The scan omits the function on the left. Differentiating the evolution in equation (3) gives the corrected identity.',kind='faithful_error')
add('P001001','Kernel interpretation','Transition probability', 'Transition amplitude; its probabilistic interpretation requires a state and a measurement convention.',
    'The displayed object is a matrix element of unitary Schrödinger evolution, not a nonnegative normalized density. The source wording was copied faithfully.',kind='faithful_error')
add('P001001','Equations (4)--(5)',r'\(e^{-iS[x]}\), \(S=\int(\dot x^2-V)\,dt\)',r'For the evolution written in (3), use formal phase \(e^{iS/\hbar}\) with \(S=\int(m\dot x^2/2-V)\,dt\), or state a consistent alternative convention.',
    'Both signs and omitted constants are visible in the scan. Legendre transformation of the stated Hamiltonian and the free-particle kernel independently determine the conventional action and phase.',kind='faithful_error')
add('P001002','Equation (6)',r'\(\hbar\partial_t f=+\widehat Hf\)',r'\(\hbar\partial_t f=-\widehat Hf\) for the semigroup in (7).',
    'Scan confirms absence of a minus sign. Differentiating the negative-exponent semigroup in the next line proves the inconsistency.',kind='faithful_error')
add('P001002','Equation (7), exponential weight',r'\(\exp(-\int_0^t x(\tau)d\tau)\)',r'\(\exp(-\hbar^{-1}\int_0^t V(x(\tau))d\tau)\), with Brownian generator \(\hbar\Delta/(2m)\).',
    'Russian text and inspected scan both show x(tau), not V(x(tau)). The corrected weight follows from the specified Schrödinger Hamiltonian and heat generator.',kind='faithful_error')
add('P001002','Equation (7), fixed endpoints','Wiener measure on paths with both endpoints fixed',
    'Use Brownian-bridge expectation multiplied by the free heat kernel, or an explicitly unnormalized bridge measure.',
    'The endpoint conditions and label Wiener measure are explicit. The source does not supply the conditioning or kernel normalization needed for equality.')
add('P001002','Equation (7), semigroup exponent',r'\(Hx\) after \(-t/\hbar\)',r'Read the operator as \(\widehat H\); keep the trailing x/index reading unresolved in the diplomatic text.',
    'The Russian transcription flags the additional x-like stroke and the scan does not decide whether it is an operator index. The mathematics alone cannot justify deleting it as a transcription error.')
add('P001002','Answer to Gelfand curvature-action question','Einstein and Pontryagin classes',
    'For the precise natural second-order tensor problem, use the dimension-dependent Lovelock family; top-degree characteristic numbers have zero interior variation.',
    'The manuscript answer is faithfully copied. Navarro--Navarro Theorem 2.6 supplies a bounded exact classification; dimensions at least five include nonzero Gauss--Bonnet tensors.',kind='faithful_error')
add('P001002','Equation (10)',r'\((\det g)^{5/2}\prod dg_{\mu\nu}\)',r'For the covariant matrix entries written, the pointwise invariant density has \((\det g)^{-5/2}\); a continuum product measure remains formal.',
    r'The positive exponent is visible in the scan and conflicts with the correctly negative general matrix exponent in (22). Congruence on symmetric matrices has Jacobian \(|\det A|^{n+1}\).',kind='faithful_error')
add('P001003','Regge scalar-curvature normalization (14)--(16)',r'\(\sum_h\delta_h\operatorname{vol}(h)=\int\operatorname{Scal}\,dV\)',
    'Specify the scalar-curvature convention; with scalar curvature twice Gaussian curvature on surfaces, the hinge sum needs a factor two.',
    'The source uses unnormalized angle defect. In dimension two the sum of angle defects is 2 pi times Euler characteristic, while the scalar integral is 4 pi times Euler characteristic.')
add('P001003','Refinement warning','Barycentric subdivision is unnecessary.',
    'Do not use this subdivision when it destroys the required angle bound; the following note says the angles become small.',
    'Russian says barycentrically subdividing is not to be done, and gives the geometric reason. Unnecessary weakens the practical warning.',applies='en',kind='translation')
add('P001003','Convergence theorem and angle condition','Mesh tends to zero; angles bounded away from zero.',
    'Use a uniformly fat admissible approximation family, with shape control on all simplex faces, not just mesh convergence or a selected angle.',
    'The source appends a nondegeneracy warning. Cheeger--Müller--Schrader Section 1 and Theorem 5.1 supply the full approximation hypotheses.')
add('P001003-P001005','Equations (17), (19), (26)--(29)',r'\(\operatorname{tr}(\Omega^k)\) as the general limiting curvature density',
    'Use the corresponding normalized Lipschitz--Killing density, including the required coframe factors in lower curvature degree.',
    'The original trace is visible and consistently copied. The full CMS article treats Lipschitz--Killing measures, not this raw trace family; degree alone rules out an unmodified trace as an n-form when 2k differs from n.',kind='faithful_error')
add('P001004','Top-degree Euler assertion',r'\(\int\operatorname{tr}(\Omega^{n/2})=\chi(M)\)',r'For even n, \(\int\operatorname{Pf}(\Omega/(2\pi))=\chi(M)\), with compatible orientation convention.',
    'Scan and both transcriptions agree on trace. For an oriented surface the orthogonal curvature matrix has trace zero, while the sphere has nonzero Euler characteristic. CMS introduction identifies the Euler density.',kind='faithful_error')
add('P001004','Solid-angle flag indices',r'Index in \([\sigma^i,\sigma^{ij}]\) or overwritten adjacent superscript',
    'Retain the diplomatic uncertainty; the intended geometric angle is for nested faces with their dimensions specified.',
    'The inspected stroke is not sufficiently clear to call a specific superscript a transcription error. The published flag definition supplies mathematical conventions but cannot rewrite the handwriting.')
add('P001004','Brin reference and date','Similar Brin work around 1946',
    'Retain the uncertain name/date; do not silently change the decade or assign a particular Brin.',
    'Scan inspected; searches of the exact surname with solid angles, polyhedral curvature and Euler formulas did not establish an exact bibliographic match.',kind='provenance')
add('P001004','Equation (23)',r'\(\operatorname{vol}(\sigma,\ell)^{-(n+1)}\prod d\ell_{ij}\)',
    r'\(C\operatorname{vol}(\sigma,\ell)^{-(n+1)}\prod\ell_{ij}\,d\ell_{ij}\), or use differentials of squared lengths.',
    'Length variables are explicitly defined on P001003 and the scan contains no product of lengths. Gram-coordinate Jacobian calculation, independent symbolic checks and the one-edge case confirm the missing factor.',kind='faithful_error')
add('P001004','Equation (24)',r'\(\deg g(x)^{5/2}\)',r'Intended determinant notation; for covariant entries the invariant exponent is negative, as in (22).',
    'The g-like final letter and positive exponent are copied faithfully. The nearby formula (10) and the matrix-density derivation determine the intended mathematical expression, not an alternative handwriting reading.',kind='faithful_error')
add('P001005','Final convergence argument','Eventually equal intersection Euler characteristics almost everywhere, therefore integrals converge.',
    'Include transversality and a valid integrable domination or equivalent uniform-integrability argument.',
    'The manuscript records a proof idea. Almost-everywhere convergence alone does not imply convergence of integrals; the full geometric convergence theorem supplies additional control.')
add('P001006','Contraction exactness','Globally (?) exact; possibly locally exact.',
    'A Hamiltonian Lie-algebra lift needs globally defined Hamiltonians. Preserve the disputed word as uncertain in the diplomatic reading.',
    'Scan inspected and Russian Unclear note retained. The local Poincaré lemma would only give infinitesimal symplecticity; the later global moment map needs a stronger condition.')
add('P001006','Moment-map group equivariance','Commutes with the A-action follows from the Lie-algebra homomorphism.',
    'Assume A connected, or impose equivariance for the remaining components separately.',
    'Infinitesimal equivariance integrates on the identity component. The source specifies no connectedness hypothesis.')
add('P001006','Speaker initials','V. L. Ginzburg in catalog; Ginzburg in manuscript.',
    'Retain catalog attribution with an explicit provenance qualifier, without assigning a full personal identity from the surname alone.',
    'The scan heading contains only the surname; no initials are visible.',kind='provenance')
add('P001007','Parallel-body polynomial',r'\(\sum_{i=0}^nV_k\varepsilon^k\)',r'Use one summation index consistently, e.g. \(\sum_{j=0}^nV_j\varepsilon^j\).',
    'The inspected scan genuinely mixes i and k; the transcription is faithful.',kind='faithful_error')
add('P001007','Curvature coefficient and principal curvatures',r'\(V_i=C_i\int\sigma_i(k)dS\), with n principal curvatures.',
    r'For the coefficient of \(\varepsilon^j\), j at least one, use \(j^{-1}\int\sigma_{j-1}(\kappa_1,\ldots,\kappa_{n-1})dS\); the constant coefficient is volume.',
    r'The source has no index shift. Integrating the outer normal Jacobian \(\prod_i(1+t\kappa_i)\) gives the corrected formula and the count of principal curvatures.',kind='faithful_error')
add('P001007','Projection and affine-plane dimensions','One coefficient index k labels both projected volume and plane-section integrals.',
    r'For the intrinsic volume \(V_j\), average j-dimensional projection volume or Euler characteristic of affine \((n-j)\)-plane sections.',
    'The manuscript mixes polynomial-power and intrinsic-volume conventions. McMullen pp. 491--492 and dimensional scaling distinguish them.')
add('P001008','Partition generating-function corollary',r'\(f_{\lambda,n}(t)+t^{m+n-1}f_{\lambda,m}(t)\)',
    r"\(f_{\lambda,n}(t)+t^{m+n-1}f_{\lambda',m}(t^{-1})\), where lambda-prime is the conjugate partition.",
    'Scan confirms neither conjugation nor inverse argument is written. Macdonald I.1 equation (1.7 prime), the preceding complementary-exponent identity, and exact finite checks independently fix both omissions.',kind='faithful_error')
add('P001008','Symplectic cone examples and contact quotient',r'Full \(\mathbb R^{2n}\) and full cotangent bundle, then smooth contact quotient.',
    'Remove the origin and the zero section for the stated examples, and require the scaling action to be free and proper.',
    'The omitted zero loci are fixed points, so homogeneity alone does not give the asserted smooth contact quotient.')
add('P001008','Weyl momentum convention',r'\(\xi_k\mapsto+i\partial_{x_k}\) with \(e^{i\xi\cdot(x-y)}\)',
    r'For the displayed phase, \(\xi_k\mapsto-i\partial_{x_k}\); changing phase changes this convention.',
    'Both signs are unambiguous in the scan. Differentiation of the Fourier kernel independently verifies the correction.',kind='faithful_error')
add('P001008','Input function in Weyl kernel',r'\((Pf)(x)\) on the left and \(u(y)\) on the right.',
    'Use the same input function on both sides.',
    'The scan confirms the mismatch already flagged by the Russian transcription.',kind='faithful_error')
add('P001008-P001009','Symbol sum and operator axioms','An infinite ordinary sum of homogeneous symbols; unqualified compactness statements.',
    'Read the symbol expansion asymptotically with derivative remainder estimates; specify a global classical calculus for negative-order compactness and the unit-order principal-symbol drop.',
    'The later asymptotic-summation axiom and the exact operator examples support this interpretation. Noncompact local calculi do not satisfy the compactness axiom without additional decay.')
add('P001010','MacPherson title and diagram','Holonomic D-modules approximately equivalent to perverse sheaves.',
    'For ordinary constructible perverse sheaves, specify regular holonomic modules and the de Rham degree convention.',
    'The scan omits regular. Kashiwara 1980 main theorem states the regular correspondence. The omitted hypothesis is mathematical, not a missing OCR word.')
add('P001010','Record type for MacPherson','A completed lecture inferred from the catalog speaker entry.',
    'Treat as proposed subjects: the manuscript explicitly says the title of a paper he would speak about, followed by another title.',
    'English words are part of the original scan, reproduced in the Russian diplomatic file. The record contains no completed proof narrative.',kind='provenance')
add('P001010','Fuchs subgroup fibration','G/H is used as a general model for the discrete-to-topological fiber.',
    'The displayed ordinary bundle model needs closed-subgroup or local-section hypotheses. For G-delta to G use the homotopy fiber, not the set quotient.',
    'The word usually is in the source. The comparison homomorphism is the identity on underlying sets, so the naive quotient is a point and cannot encode local homology.')
add('P001011','Superscript on diffeomorphism group in the cycle definition',r'\(\operatorname{Diff}^{k}_{\omega_0}M\)',r'\(\operatorname{Diff}^{c}_{\omega_0}M\) in the intended compact-support notation.',
    'Scan really shows k; surrounding definitions use c for compact support and k for cycle degree. This is a source-level notational slip, not a transcription correction.',kind='faithful_error')
add('P001011','Integral over K times a point',r'\(x\mapsto\int_{K\times x}\Omega\) as an (n-k)-form.',
    'Interpret as integration along the K fiber of the appropriate mixed-degree form, with compact support in the M direction.',
    'Literal restriction to a k-dimensional slice does not by itself describe the unintegrated M-form components. McDuff 1982 pp. 610--612 supplies the universal transverse-form framework.')
add('P001011','Sphere parity proof sketch','Integral over a horizontal leaf is zero.',
    'Retain uncertainty between a horizontal slice and a leaf in the diagram; the sketch alone does not prove the sphere parity theorem.',
    'Russian layer/fiber word and inspected diagram do not determine the intended cycle. Integrating a transverse volume form over an actual tangent leaf is trivially zero and would not explain parity.',applies='en')
add('P001012','Name preceding rational vanishing','Chern--Weyl', 'Chern--Weil in mathematical attribution; preserve the source spelling diplomatically.',
    'Scan and transcription agree on Weyl. Milnor Appendix and Lemma 8 proof explicitly use Chern--Weil characteristic forms.',kind='provenance')
add('P001012','Sah--Wagoner quotient',r'\(\bigsqcup\mathbb Q\) labelled uncountable sum.',
    'A direct sum of copies of Q, or equivalently an uncountable rational-vector-space quotient.',
    'The U-shaped source symbol is faithfully reproduced. A disjoint union is not an abelian group; Milnor Introduction p. 72 gives the precise vector-space quotient statement.',kind='faithful_error')
add('P001012','Integral cohomology corollary','A double-headed arrow between the two integral cohomology groups.',
    'The verified conclusion is the injection from H*(BG;Z) into H*(BG-delta;Z), for finitely many components.',
    'Both arrowheads are visible in the scan. Milnor Corollary 1 p. 76 and its proof determine the intended mathematical conclusion; this is not evidence that a hook was omitted by OCR.')
add('P001001-P001013','Record boundaries and order','Overlapping catalog windows treated as disjoint lecture ranges.',
    'Use actual dated and speaker headings: 546 ends on P001005, 547 occupies P001006, 549 precedes 548, Fuchs 551 intervenes within 553, and 555 ends on P001013.',
    'All thirteen source scans inspected; Kirillov 556 begins at P001014. Heading record 545 has no additional mathematical content.',kind='provenance')

path = Path(__file__).resolve().parent / 'corrections.csv'
with path.open('w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['page','place','transcription_reads','should_read','evidence','applies_to','type'])
    writer.writerows(rows)
print('Wrote', len(rows), 'correction and provenance rows')
