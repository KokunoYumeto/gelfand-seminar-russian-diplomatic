"""Complete root authoring: executes records92--100, then appends101--104."""
from pathlib import Path
exec((Path(__file__).resolve().parent/'make_root.py').read_text(), globals())

talk(101,'1966-09-26','D. A. Kazhdan','P000157-P000159',
     'Isolation of the trivial representation and lattice finiteness',
     r'Two finiteness conclusions for lattices are announced on P000158, followed by the representation-theoretic mechanism now called property \(T\). Kazhdan’s short paper, received two weeks after the seminar, is an unusually close match. A separate sentence about groups over \(\mathbb Q\) retains no conclusion and cannot be identified with a theorem.')
item(101,'P000158','theorem','Finite abelianization of the lattice',
     r'If the simple real or \(p\)-adic group \(G\) contains \(\mathrm{SL}(3,P)\), and \(\Gamma\) is discrete with finite-volume quotient, then \(\Gamma/[\Gamma,\Gamma]\) is finite.',
     r'Let \(K\) be a nondiscrete locally compact field. Every lattice in \(\mathrm{SL}_3(K)\) has finite abelianization. The same conclusion holds for a locally compact group \(G\) with property \(T\), including the simple algebraic groups covered by Kazhdan’s Theorem 6. In that extension the algebraic subgroup and compact-generation hypotheses of that theorem must be retained.',
     'A',r'\citet[Theorems 1, 3, 5--6]{kazhdan1967dual}; received 10 October 1966, published 1967.',
     r'established. Containing an arbitrary property-\(T\) subgroup, without the ambient hypotheses, does not transfer property \(T\) to every group.',
     ['kazhdan1967dual'],reconstruction=r'The explicit \(\mathrm{SL}_3(K)\) case is exact. The larger-group wording is restricted to the published theorem rather than extrapolated from the notebook’s abbreviation.')
item(101,'P000158','theorem','Finite generation of the lattice',
     r'\(\Gamma\) has finitely many generators, even extractable from any generating set.',
     r'A countable discrete group with property \(T\) is finitely generated; hence the lattices of the preceding item are finitely generated. Any generating set of a finitely generated group contains a finite generating subset, since finitely many fixed generators use only finitely many words in that set.',
     'A',r'\citet[Theorems 2--3]{kazhdan1967dual}, announced here in September 1966 and printed in 1967.',
     r'established. Finite presentation is a separate assertion and is not stated in these notes.',
     ['kazhdan1967dual'],literal='correct',reconstruction=r'The parenthetical strengthening is the elementary finite-word argument, not a stronger finiteness property.')
item(101,'P000158','method','Isolation of the trivial unitary representation',
     r'The proof uses \ru{изолированность единичного представления}, isolation of the trivial representation.',
     r'For a locally compact group, property \(T\) means that every unitary representation with almost invariant unit vectors has a nonzero invariant vector. Equivalently, the trivial representation is isolated in the appropriate unitary-dual topology. Kazhdan proves this for \(\mathrm{SL}_3(K)\) and transfers it to finite-covolume closed subgroups.',
     'A',r'\citet[\S1 and Theorems 3, 5]{kazhdan1967dual}. The terminology and mechanism occur in the original 1967 paper.',
     r'established; the notes record the central innovation, not merely its later name.',
     ['kazhdan1967dual'],reconstruction=r'Almost invariant vectors give an explicit modern formulation of the isolated-representation shorthand.',literal='correct')
item(101,'P000158','remark','A rational-group representation fragment',
     r'An algebraic group over \(\mathbb Q\) containing \(\mathrm{SL}(3,\mathbb Q)\) is followed only by \ru{что-то о представлениях}, something about representations.',
     r'No asserted property of representations, topology on \(G(\mathbb Q)\), or class of representations survives. Neither a local-field property-\(T\) theorem nor an automorphic theorem can be inferred from this sentence.',
     'F',r'The nearby results match \citet{kazhdan1967dual}; the rational-group fragment has no exact statement to match.',
     r'unidentified as a mathematical assertion, even though its subject is clear.',
     ['kazhdan1967dual'],literal='not determinable',match='thematic only',verification='unresolved lead',confidence='low')
save()

talk(102,'1966-09-26','Lee Lorch','P000157-P000160',
     'Higher monotonicity of zeros and wave integrals',
     r'The lecturer’s handwritten name on P000158 is uncertain; the MCCME entry and the joint work with Peter Szego identify Lee Lorch. The page treats Sturm comparison, higher finite differences of zeros, Bessel and Airy examples, and integrals between consecutive zeros. The strict inequality cannot follow from the weak derivative hypotheses exactly as written. Gelfand’s endpoint remark is mathematically suggestive but not completely recorded.')
item(102,'P000158','claim','Monotonicity of zero spacing and its alleged converse',
     r'Under the label Sturm (1836), increasing \(f\) in \(y^{\prime\prime}+fy=0\) makes consecutive zeros closer, “and conversely.”',
     r'For a continuous increasing coefficient on an oscillatory interval, Sturm comparison gives nonincreasing consecutive zero gaps, with strictness under an appropriate strict comparison. Decreasing gaps of one solution do not conversely force its coefficient to be increasing.',
     'E',r'The comparison-theory setting precedes the talk and is the starting point of \citet[Introduction]{lorchszego1963higher}.',
     r'the forward comparison is standard; the unrestricted converse is false.',
     ['lorchszego1963higher'],literal='false as written',reconstruction=r'\ours\ For \(x>1\), put \(y=x^{-1/2}e^{\epsilon\cos(2x^2)}\sin(x^2)\), \(\epsilon=1/100\). Its zeros \(\sqrt{k\pi}\) have strictly decreasing gaps. Direct differentiation gives \(f=x^2[4+16\epsilon+32\epsilon\cos(2x^2)-16\epsilon^2\sin^2(2x^2)]-3/(4x^2)\). This is smooth and positive on \((1,\infty)\), but \(f^{\prime}<0\) at all sufficiently large points with \(2x^2=\pi/2+2k\pi\). Thus even positive oscillatory coefficients do not satisfy the proposed converse. The identity is checked symbolically in the supplied code.',match='partial',development='annotated')
item(102,'P000158','theorem','Higher monotonicity needs a nondegeneracy condition',
     r'The assumptions are \((-1)^jf^{(j+1)}\geq0\), \(j=1,\ldots,N\), and \(f(\infty)>0\); the conclusion is \((-1)^n\Delta^{n+1}x_k>0\).',
     r'The written statement fails for \(f\equiv1\), whose zero gaps are constant. A checked sufficient theorem is formulated through independent real solutions \(y_1,y_2\) and \(p=y_1^2+y_2^2\): if \(p>0\), \(-p^{\prime}>0\), and \((-1)^jp^{(j)}\geq0\) for \(2\leq j\leq N\), with the derivatives continuous up to order \(N-1\) and the last derivative existing on the interval, then the alternating finite differences of zero gaps are strictly positive through the stated orders wherever the zeros exist.',
     'E',r'\citet[Theorem 2.1]{lorchszego1963higher} has the strict phase-amplitude conditions; \citet[Theorem, pp.~447--448]{muldoon1968extension} weakens the higher ones while retaining \(-p^{\prime}>0\).',
     r'the theorem family is established, but the exact recorded coefficient-only formulation is false. The later phase-amplitude theorem is a partial, explicitly different match.',
     ['lorchszego1963higher','muldoon1968extension'],literal='false as written',match='partial',reconstruction=r'\ours\ The constant-coefficient counterexample also survives adding the missing \(j=0\) weak inequality. Accordingly no silent change of an index repairs strictness.',development='annotated')
item(102,'P000158','remark','The Bessel and Airy examples',
     r'Bessel functions with \(\nu>1/2\), Airy functions, and others are listed as examples.',
     r'Writing \(u(x)=\sqrt{x}\,J_\nu(x)\) puts the Bessel equation in normal form \(u^{\prime\prime}+[1-(\nu^2-1/4)x^{-2}]u=0\). The oscillatory Airy equation is \(u^{\prime\prime}+xu=0\), for example \(u=\operatorname{Ai}(-x)\). Normal-form dependent variables and the oscillatory branch must be specified before importing zero or wave-integral assertions.',
     'E',r'These special-function applications belong to \citet[applications]{lorchszego1963higher}; the transformed equations identify the notebook’s examples.',
     r'established examples. A statement about wave areas of \(J_\nu\) itself is not identical to one about \(\sqrt{x}J_\nu\).',
     ['lorchszego1963higher'],reconstruction=r'The normalizing factor and the sign of the Airy argument are supplied.',match='partial')
item(102,'P000158','theorem','Higher monotonicity of wave integrals',
     r'For consecutive zeros, \(M_k=\int_{x_k}^{x_{k+1}}|y|^\lambda\,dx\), \(\lambda>-1\), has the same property; \(\lambda=0\) gives gaps and \(\lambda=1\) areas.',
     r'Under the phase-amplitude hypotheses in item 1966-102.2, \((-1)^n\Delta^nM_k>0\) for \(0\leq n\leq N\), whenever all required consecutive zeros lie in the interval. Nontrivial solutions have simple zeros, and \(\lambda>-1\) is the exact local integrability condition there.',
     'E',r'\citet[Theorem 2.1]{lorchszego1963higher}; the weakened hypotheses and unchanged conclusion are in \citet[Theorem]{muldoon1968extension}.',
     r'established with the stated hypotheses; the finite-difference order for gaps is one higher because \(M_k=x_{k+1}-x_k\) when \(\lambda=0\).',
     ['lorchszego1963higher','muldoon1968extension'],reconstruction=r'The range of differences is explicitly limited by the available zeros.')
item(102,'P000158','remark','The divergent endpoint and reciprocal derivatives',
     r'Gelfand’s \(\lambda=-1\) remark contains \(1/y^{\prime}(x_k)\) and an unresolved abbreviation; it is not a complete limiting formula.',
     r'The ordinary integral at \(\lambda=-1\) diverges at every simple endpoint zero. A precise nearby identity, not asserted to be the intended one, is \(\lim_{\lambda\downarrow-1}(\lambda+1)\int_a^b|y(x)|^\lambda dx=|y^{\prime}(a)|^{-1}+|y^{\prime}(b)|^{-1}\) for consecutive simple zeros of a \(C^1\) function with no zero inside.',
     'F',r'The integral theorem in \citet{lorchszego1963higher} assumes \(\lambda>-1\); no checked source identifies the exact endpoint remark.',
     r'the literal ordinary integral is divergent; the intended regularization or signed difference remains unidentified.',
     ['lorchszego1963higher'],literal='not determinable',match='none found',verification='unresolved lead',confidence='low',speaker='I. M. Gelfand',reconstruction=r'\ours\ Near \(a\), for \(0<\delta<|y^{\prime}(a)|\), \((|y^{\prime}(a)|-\delta)(x-a)\leq|y(x)|\leq(|y^{\prime}(a)|+\delta)(x-a)\). Integrating these bounds with \(-1<\lambda<0\), multiplying by \(\lambda+1\), taking the limit and then \(\delta\downarrow0\) gives the first reciprocal. Repeat at \(b\); on the remaining compact interval the scaled integral tends to zero. The sine example is independently checked with the beta-integral formula.',development='annotated')
corr('P000158','Lecturer and collaborator',r'Prof. Lodzhs. [?], with P. Szego',r'Identify the lecturer editorially as Lee Lorch and the collaborator as Peter Szego; preserve uncertainty in the diplomatic name.',r'The catalogue has Lee Lorch; the joint 1963 paper and Muldoon’s 1968 references identify Peter Szego. Neither supports substituting Gabor Szego.',typ='provenance')
corr('P000158','Sturm converse',r'Increasing coefficient gives closer zeros, and conversely.',r'Keep the words diplomatically; delete the unrestricted converse from a theorem statement.',r'The explicit positive-coefficient counterexample in item 1966-102.1 has decreasing zero gaps but a nonmonotone coefficient.')
corr('P000158','Strict higher differences',r'Weak derivative signs imply strict alternating differences.',r'Add an actual nondegeneracy hypothesis; do not repair the formula solely by changing the index range.',r'The scan clearly has weak signs in the hypothesis and strict signs in the conclusion. The constant coefficient 1 meets all written assumptions but gives constant gaps.')
corr('P000158','The endpoint lambda=-1',r'Formal endpoint integral associated with reciprocal derivatives.',r'Distinguish the divergent integral from a regularized endpoint limit; retain the unresolved abbreviation.',r'A simple zero makes the absolute-value integrand comparable to 1/|x-a|. The supplied limit has a sum of absolute reciprocal derivatives, not an unverified signed difference.',typ='ambiguity')
save()

talk(103,'1966-09-26','I. M. Gelfand','P000158-P000160',
     'A recapitulation of equivariant K-theory and completion',
     r'On P000159 Gelfand explicitly repeats Bernstein’s and Atiyah’s material: equivariant bundles, the Borel construction, the representation-ring action, and the approximate identification with ordinary K-theory. These are new notebook occurrences of the same constructions, not additional discovery claims.')
item(103,'P000159','definition','Equivariant K-theory as a contravariant ring functor',
     r'For compact \(G\), equivariant bundles and formal differences define \(K_G(X)\); the functor is contravariant and receives \(R(G)\) from \(X\to*\).',
     r'For a compact Lie group and compact \(G\)-space in the finite \(G\)-CW setting, complex equivariant vector bundles form the Grothendieck ring \(K_G^0(X)\). Pullback gives contravariance, and \(K_G^0(*)=R(G)\) acts by tensoring with representation bundles.',
     'E',r'The definitions precede this reprise; see \citet[Introduction]{atiyahsegal1969completion} and the earlier occurrences 1966-97.1 and 1966-98.4.',
     r'standard. Being an \(R(G)\)-algebra does not require the structural homomorphism to be injective.',
     ['atiyahsegal1969completion'],reconstruction=r'Finite \(G\)-CW hypotheses align the next completion statement with its checked classical scope.',verification='publisher metadata checked')
item(103,'P000159','construction','The Borel construction is not the ordinary orbit space',
     r'\(X_G=E\times_GX\) is called a generalization of the classifying space; for a point it is \(BG\). The accompanying phrase says the orbits are contracted to points.',
     r'For a contractible free \(G\)-space \(EG\), the diagonal quotient \(EG\times_GX\) is the homotopy quotient and is a bundle over \(BG\) with fibre \(X\). Only for free suitable actions is it homotopy equivalent to \(X/G\). For trivial actions it is \(BG\times X\).',
     'E',r'This is the construction used by \citet{atiyahsegal1969completion}; it repeats item 1966-98.5.',
     r'standard. The orbit phrase must refer to the diagonal action, not the loss of all isotropy information from \(X\).',
     ['atiyahsegal1969completion'],reconstruction=r'The distinction between homotopy and ordinary quotient is made explicit.',verification='publisher metadata checked')
item(103,'P000159','theorem','The approximate identification means I-adic completion',
     r'\(K_G(X)\) approximately coincides with \(K(X_G)\).',
     r'For a finite \(G\)-CW complex and compact Lie \(G\), the comparison identifies the augmentation-ideal completion of \(K_G^*(X)\) with \(K^*(EG\times_GX)\), interpreted through the skeletal inverse system. It is generally not an isomorphism from the uncompleted ring.',
     'B',r'\citet{atiyahsegal1969completion}, printed 1969, supplies the general completion theorem. Atiyah’s earlier special cases and Bernstein’s exposition account for the result circulating before this occurrence.',
     r'established in the stated finite setting; this is the same theorem family as item 1966-98.6.',
     ['atiyahsegal1969completion'],reconstruction=r'The ideal, completion, grading, and finiteness assumptions are supplied.',verification='publisher metadata checked')
corr('P000159','Ring over a subring',r'An R(G)-module, a ring over a subring.',r'An R(G)-algebra; the structure map need not be injective.',r'For a free action, representation bundles may become trivial or satisfy additional relations. A unital ring map alone does not identify its domain with a subring.')
save()

talk(104,'1966-09-26','I. N. Bernstein','P000158-P000162',
     'Families of elliptic operators and the index bundle',
     r'P000159--P000160 supply the analytic construction behind the K-theoretic direct image, then a finite-dimensional modification of a Fredholm family. The essential issue is that kernel dimensions jump. The index is a virtual bundle after stabilization, not generally the difference of two pre-existing kernel and cokernel bundles. This continues 1964-15.4.')
item(104,'P000159','construction','Twisting a vertical elliptic family',
     r'For a fibration \(Y\to X\) with compact manifold fibre \(M_x\), a family \(D_x\) acts between restrictions of two bundles; twisting by a bundle \(V\) on \(Y\) gives an elliptic family.',
     r'Let \(p:Y\to X\) be a smooth fibre bundle with closed fibres and compact base, and let \(D\) be a continuous family of vertical elliptic differential operators between complex vector bundles. A chosen connection defines a twist \(D\otimes V\) with symbol \(\sigma(D)\otimes1_V\); its analytic index defines an additive homomorphism \(p_!^D:K^0(Y)\to K^0(X)\).',
     'E',r'The family-index construction was discussed in Atiyah’s 1966 congress lecture, printed in 1968, and fully developed in \citet{atiyahsinger1971families}; see \citet{atiyah1968global}.',
     r'established. Independence of auxiliary choices is an index assertion, not the claim that twisting a differential operator is connection-free.',
     ['atiyah1968global','atiyahsinger1971families'],reconstruction=r'Closed fibres, compact base, operator continuity, and a connection are supplied. The symbol determines the index.',verification='publisher metadata checked')
item(104,'P000159','theorem','The direct image obeys the projection formula',
     r'The reverse map is required to be a map of \(K(X)\)-modules; the de Rham complex is mentioned as an example.',
     r'For the family index, \(p_!^D(p^*a\cdot b)=a\cdot p_!^D(b)\). A left inverse to \(p^*\) follows only if \(p_!^D(1)=1\). A de Rham family has fibrewise numerical index \(\chi(M)\), which need not equal one; the Dolbeault operator on the flag fibre used in the completion argument has index one.',
     'E',r'The family-index framework is in \citet{atiyahsinger1971families}; Atiyah discusses the flag-manifold direct image in \citet{atiyah1988commentary}.',
     r'established. An arbitrary elliptic family is not automatically a retraction of pullback.',
     ['atiyahsinger1971families','atiyah1988commentary'],reconstruction=r'The condition on the index of 1 is the missing algebraic step that connects this construction to the preceding completion argument.',verification='publisher metadata checked')
item(104,'P000159-P000160','claim','Kernels and cokernels need not form vector bundles',
     r'Finite-dimensional kernels and cokernels are subtracted to obtain an element of K-theory; after a projected deformation the kernel dimension is said to be locally constant.',
     r'A norm-continuous family of Fredholm operators has locally constant numerical index but need not have locally constant kernel or cokernel dimension. For \(A_t:\mathbb C\to\mathbb C\), \(A_tz=tz\), both dimensions jump at \(t=0\). Thus the virtual index requires stabilization or local patching.',
     'E',r'This distinction underlies the family construction of \citet{atiyahsinger1971families}; it also explains the Fredholm discussion in \citet{atiyah1968global}.',
     r'established. The abbreviated difference is valid only after the required index-bundle construction.',
     ['atiyahsinger1971families','atiyah1968global'],literal='false as written',reconstruction=r'\ours\ The one-dimensional family is a direct counterexample to the unstabilized bundle claim: its kernel is zero for \(t\ne0\) and \(\mathbb C\) at zero.',development='annotated',verification='publisher metadata checked')
item(104,'P000160','method','A rigorous finite-dimensional stabilization',
     r'A map \(X\to F(H,H)\) is modified through \(A_x(1-t)+tA_xP_V\), where the projection’s precise definition is abbreviated.',
     r'For a compact Hausdorff base \(X\), complex Hilbert spaces \(H_0,H_1\), and norm-continuous Fredholm family \(A_x:H_0\to H_1\), choose a finite-dimensional \(V\subset H_1\) with \(\operatorname{im}A_x+V=H_1\) for every \(x\). The augmented operators \(B_x:H_0\oplus V\to H_1\), \(B_x(u,v)=A_xu+v\), are surjective and their kernels form a finite-rank vector bundle. Define \(\operatorname{Ind}(A)=[\ker B]-[X\times V]\).',
     'E',r'This is the standard family-index construction, contemporary with the 1966 lecture and recorded in \citet{atiyahsinger1971families}. The specific projected formula in the notebook is not asserted to be an exact transcription of that argument.',
     r'established. The resulting class is independent of the auxiliary finite-dimensional subspace and homotopy invariant.',
     ['atiyahsinger1971families','atiyah1968global'],reconstruction=r'\ours\ For each \(x\), a complement to the range gives a surjective augmentation on a neighbourhood; a finite cover supplies a common \(V\). Locally a continuous right inverse exists by the Neumann-series argument, so the kernels form a bundle. Enlarging \(V\) to \(W\) yields \(0\to\ker B_V\to\ker B_W\to X\times(W/V)\to0\), preserving the virtual class. A common enlargement compares any two choices. Apply the same argument over compact \(X\times[0,1]\) for homotopy invariance.',match='partial',development='annotated',verification='publisher metadata checked')
corr('P000159-P000160','Kernel minus cokernel',r'Finite kernel and cokernel give two bundles over the parameter space.',r'Use a stabilized virtual index unless both dimensions are locally constant.',r'The scalar family \(A_t=t\) has jumping kernel and cokernel dimensions; the same problem occurs for general elliptic families.')
corr('P000160','Projection argument',r'The displayed homotopy already gives locally constant kernel dimension.',r'Retain the ambiguous projection notation; add a global finite-dimensional complement and a surjective augmentation for a complete argument.',r'The scan does not state the requisite complement condition. Compactness of the base supplies a finite common complement; the reconstruction proves the resulting kernel-bundle assertion.',typ='ambiguity')
# The primary family-index paper was subsequently opened and section2 read.
for entry in items:
    if entry['record']==104:
        entry['verification']='read the result'
        entry['fate']=entry['fate'].replace(r'\citet{atiyahsinger1971families}',r'\citet[\S2, Proposition 2.2 and Definition 2.3]{atiyahsinger1971families}')
save()
