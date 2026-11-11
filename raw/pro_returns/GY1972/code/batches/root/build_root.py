"""Author the root-owned GY1972 records; run from any working directory.

All mathematical prose is editorial, with evidence and reconstruction separated.
This script is included for reproducibility; it makes no network requests.
"""
import csv
import json
from pathlib import Path

OUT = Path(__file__).resolve().parent
TALKS, ITEMS, PROBLEMS, CORRECTIONS = [], [], [], []


def talk(record, date, speaker, pages, title, summary):
    TALKS.append(dict(record=record, date=date, speaker=speaker, pages=pages,
                      title=title, kind='talk', summary=summary))


def item(record, pages, kind, title, notes, statement, fate, refs,
         cls='E', reconstruction='', literal='correct with missing hypotheses',
         match='exact', verification='read the result', confidence='high',
         development='none', problem='', worth='', status='', speaker=None):
    n = sum(x['record'] == record for x in ITEMS) + 1
    obj = dict(id=f'1972-{record}.{n}', record=record, pages=pages, kind=kind,
               title=title, notes=notes, statement=statement,
               reconstruction=reconstruction, **{'class': cls}, fate=fate,
               present_status='As of 9 November 2026: ' + status,
               literal_correctness=literal, publication_match=match,
               verification=verification, development=development, problem=problem,
               worth=worth, refs=refs, confidence=confidence)
    if speaker:
        obj['speaker'] = speaker
    ITEMS.append(obj)
    return obj['id']


def correction(page, place, reads, should, evidence, applies='both', typ='faithful_error'):
    CORRECTIONS.append(dict(page=page, place=place, transcription_reads=reads,
                           should_read=should, evidence=evidence, applies_to=applies, type=typ))


def save():
    OUT.mkdir(parents=True, exist_ok=True)
    for name, data in [('talks', TALKS), ('items', ITEMS), ('problems', PROBLEMS)]:
        (OUT / f'{name}.json').write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n')
    with (OUT/'corrections.csv').open('w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['page','place','transcription_reads','should_read',
                                         'evidence','applies_to','type'])
        w.writeheader(); w.writerows(CORRECTIONS)


# Record 290: the manuscript's theorem and proof, followed by its corollary.
talk(290, '1973-03-05', 'V. I. Lomonosov', 'P000482-P000483',
     'A compact operator, a fixed point, and a common invariant subspace',
     r'''The notebook gives a proof for a commuting family containing a nonzero compact operator: a finite cover of a compact image produces a convex-combination map, Schauder gives a fixed point, and compact spectral theory gives the contradiction to transitivity. It then states a locally convex extension and a corollary for multiplication operators on commutative Banach algebras. The page itself replaces a crossed-out attribution to Berezin by Lomonosov. The published note was received on 5 February 1973, before this seminar, and appeared later in 1973; its theorem is stronger than the commuting-family formulation recorded here \citep[pp.~55--56]{lomonosov1973invariant}. Henkin's announcement follows on the lower part of P000483, before Berezin on P000484.''')
item(290,'P000482','theorem','Common invariant subspace for a commuting compact-containing family',
     r'''\ru{сем-во попарно комм.} operators on a Banach space contains a completely continuous \(A\ne0\); the family has a common nontrivial invariant subspace. The notes call this a generalization of Aronszajn--Smith.''',
     r'''Let \(X\) be an infinite-dimensional complex Banach space and \(\mathcal R\subset\mathcal B(X)\) a pairwise commuting family containing a nonzero compact operator. There is a closed linear subspace \(M\), \(0\ne M\ne X\), invariant under every member of \(\mathcal R\). The published theorem gives a subspace invariant under the entire commutant of any nonzero compact operator; pairwise commutativity of that commutant is unnecessary.''',
     r'''The exact proof and a stronger theorem occur in \citet[theorem, p.~55]{lomonosov1973invariant}; received 5 February, published 1973. This develops the compact-operator theme indexed earlier as 1964-50.3.''',
     ['lomonosov1973invariant'], cls='A',
     reconstruction='Complex scalars, infinite dimension, boundedness and closedness are made explicit; the stronger published theorem is not attributed to the notebook.',
     status='Established. Neither the unrestricted Banach-space invariant-subspace problem nor the Hilbert-space problem is a question posed by this entry.')
item(290,'P000482','claim','Extension of the argument to locally convex spaces',
     r'''\ru{Док-во проходит в случае ЛВП, короткое и простое.} No completeness or compactness convention is specified.''',
     r'''A sufficient precise version replaces \(X\) by an infinite-dimensional complete Hausdorff complex locally convex space and uses a continuous linear compact operator \(K\ne0\), where compact means that some zero-neighbourhood has relatively compact image. A commuting family containing \(K\) has a common nonzero proper closed invariant subspace. One must use the locally convex fixed-point theorem and this neighbourhood notion of compactness, rather than merely mapping bounded sets to relatively compact sets.''',
     r'''The extension to real or complex locally convex spaces is explicitly stated in \citet[p.~56, paragraph after the proof]{lomonosov1973invariant}. The publication also leaves the precise topological conventions implicit.''',
     ['lomonosov1973invariant'], cls='A', confidence='medium', match='partial',
     reconstruction='The complete Hausdorff formulation and the neighbourhood definition are a sufficient editorial formulation; no claim is made for every possible meaning of compact on an arbitrary locally convex space.',
     status='The compact-operator fixed-point argument has this precise sufficient extension. The unqualified notebook sentence requires these conventions.')
item(290,'P000482','method','A compact image separated from zero and the transitivity alternative',
     r'''Choose a closed unit ball \(S\) about \(x_0\) with \(\inf_{x\in S}\|Ax\|>1/2\), then use \(\overline{AS}\). The displayed recipe reads \(x_0=\|A\|x'_0\), \(\|x'_0\|=1\), \(Ax'_0\ne0\). Orbit closures \(\overline{\mathcal R y}\) are invariant.''',
     r'''For nonzero bounded \(A\), take a unit vector \(u\) with \(Au\ne0\) and \(t>(\|A\|+1/2)/\|Au\|\). Then the closed unit ball about \(tu\) satisfies \(\|Ax\|\ge t\|Au\|-\|A\|>1/2\). Compactness makes \(K=\overline{AS}\) compact and disjoint from zero. For a unital operator algebra, if every nonzero orbit is dense, then each \(y\in K\) can be carried into the open unit ball about \(x_0\).''',
     r'''This is the opening reduction of \citet[p.~55]{lomonosov1973invariant}; the publication asserts existence of the ball without the notebook's incorrect scaling recipe.''',
     ['lomonosov1973invariant'], cls='A', literal='false as written', development='annotated',
     reconstruction=r'\ours\ The explicit valid choice of t repairs the notebook formula. Reversing the triangle inequality independently verifies the separation. It is an elementary editorial check, not a new invariant-subspace theorem.',
     status='The reduction is valid after correcting the scale. For a small-norm nonzero A, the printed recipe places zero in S and cannot work.')
item(290,'P000482-P000483','method','Finite covering, convex weights, and the Schauder fixed point',
     r'''Finitely many \(T_i\) cover \(\overline{AS}\) by \(\|T_i y-x_0\|<1\). With the drawn cutoff \(f(t)=\max(1-t,0)\), form \(\Phi(y)=\sum_i\alpha_i(y)T_i y\), and apply Schauder to \(\Phi A:S\to S\).''',
     r'''Set \(\alpha_i(y)=f(\|T_i y-x_0\|)/\sum_j f(\|T_j y-x_0\|)\). The denominator is positive on \(K\); the weights are continuous, nonnegative and sum to one. Only vectors in the open ball have positive weights, so \(\Phi(K)\subset S\). The map \(\Phi A\) is continuous with relatively compact range, hence has a fixed point \(x\in S\), and \(x\ne0\) because \(0\notin S\).''',
     r'''The construction is reproduced in \citet[pp.~55--56, displayed fixed-point equation]{lomonosov1973invariant}. Its chronology is the same as item 1972-290.1.''',
     ['lomonosov1973invariant'], cls='A', literal='correct',
     reconstruction='The value f(0)=1 and the positivity of the denominator are supplied explicitly from the graph; the missing parenthesis in one weight is restored.',
     status='Established proof mechanism. The dependence of the weights on y is frozen at y=Ax only after obtaining the fixed point.')
item(290,'P000483','claim','The spectral contradiction does not promise a finite-dimensional invariant subspace',
     r'''The compact operator \(T=\sum_i\alpha_iT_iA\) has eigenvalue 1; the notes infer an invariant subspace and immediately caution that a finite-dimensional one need not exist in general.''',
     r'''Under the temporary assumption of transitivity and for the commuting algebra in the notebook, \(E=\ker(I-T)\) is nonzero and finite-dimensional, and commutation makes E invariant for that algebra. Since X is infinite-dimensional, E is proper, contradicting transitivity. The finite-dimensional E belongs to the contradiction argument. The final theorem only asserts some nonzero proper closed invariant subspace. An injective quasinilpotent compact operator, such as the Volterra operator on \(L^2[0,1]\), cannot have a nonzero finite-dimensional invariant subspace over \(\mathbb C\).''',
     r'''Compare the contradiction at the end of \citet[p.~56]{lomonosov1973invariant}; the published noncommutative-commutant proof instead uses E to obtain an eigenvector of A.''',
     ['lomonosov1973invariant'], cls='A', literal='correct', development='annotated',
     reconstruction=r'\ours\ The Volterra example is an explanatory check, not a claim that the speaker gave it: injectivity excludes eigenvalue zero, and quasinilpotence excludes every other eigenvalue; a nonzero finite-dimensional complex invariant subspace would supply an eigenvector. The distinction between the commuting notebook proof and the stronger published proof is explicit.',
     status='The qualification is essential. Compactness of A does not imply a finite-dimensional common invariant subspace.')
item(290,'P000483','theorem','A nontrivial closed ideal from compact multiplication',
     r'''A commutative Banach algebra containing an element multiplication by which is completely continuous has a nontrivial ideal.''',
     r'''Let B be an infinite-dimensional commutative complex Banach algebra. If some left multiplication \(L_a:b\mapsto ab\) is nonzero and compact, then the commuting family \(\{L_b:b\in B\}\) has a nonzero proper closed invariant subspace I. Commutativity makes I a closed two-sided ideal. The zero multiplier must be excluded from this direct application, and dimension one is an immediate exception to the unqualified statement.''',
     r'''This is the direct multiplication-representation consequence of \citet[p.~55, theorem]{lomonosov1973invariant}. The separate algebraic corollary is recorded in the seminar rather than stated in that two-page article.''',
     ['lomonosov1973invariant'], cls='A', match='partial',
     reconstruction='Infinite dimension and a nonzero multiplier are sufficient hypotheses for the stated argument, not a claim that the notebook gave them.',
     status='Established under the stated hypotheses; the original unqualified formulation omits necessary exclusions.')
correction('P000482','Scaling the centre of the ball',r"\(x_0=\|A\|x'_0\).",
           r'Choose \(x_0=tu\) with \(t\|Au\|>\|A\|+1/2\).',
           r'The scan visibly has the norm multiplier. Its value does not ensure that AS avoids zero; the stated inequality follows by the reverse triangle inequality. This is an emendation, not a transcription replacement.')
correction('P000483','Numerator of the fixed-point weights',r'\(f(\|T_jy-x_0\|\)',
           r'\(f(\|T_jy-x_0\|)\).',
           'Scan inspected: the closing parenthesis is absent, while the parallel denominator determines its restoration.')
correction('P000483-P000484','Order of the three 5 March records','Catalogue order: 290, 291, 292.',
           'Manuscript order: 290 (Lomonosov), 292 (Henkin), 291 (Berezin).',
           'P000483 places the Henkin announcement immediately after the invariant-subspace proof; P000484 begins Berezin. Catalogue windows are not exact talk spans.',typ='provenance')
save()


# Record 292 occurs before 291 in the manuscript.
talk(292, '1973-03-05', 'G. M. Henkin', 'P000483',
     'Leray kernels, extension estimates, and convex embeddings',
     r'''A short announcement connects boundary integral formulas, compact localization errors, realization of strictly pseudoconvex domains inside convex domains, bounded holomorphic extension, and the maximal ideal space of the continuous holomorphic algebra. The extension theorem had already appeared in 1972. The convex embedding assertion anticipates the Henkin--Chirka and Fornæss publications; it is substantially stronger than the words ``follows from Oka'' suggest.''')
item(292,'P000483','construction','The Leray integral representation on a convex domain',
     r'''The displayed boundary integral has denominator \(\langle\partial\rho(\zeta),\zeta-z\rangle^n\) and coefficient \((n-1)!/(2\pi i)^n\). It is described for bounded holomorphic functions.''',
     r'''A sufficient classical setting is a bounded smoothly strictly convex domain \(D=\{\rho<0\}\subset\mathbb C^n\), with \(d\rho\ne0\) on the boundary and \(f\in\mathcal O(D)\cap C(\overline D)\). With the boundary orientation and the standard alternating form \(\omega'(w)=\sum_j(-1)^{j-1}w_j\,dw_1\wedge\cdots\widehat{dw_j}\cdots\wedge dw_n\), the notebook formula reproduces f inside D. An arbitrary bounded holomorphic f needs a boundary-limit or limiting-domain interpretation.''',
     r'''This is established integral-representation machinery predating the announcement; compare \citet[\S1, Theorem 1.1 and Lemma 2.1]{henkin1969integral}. Strict pseudoconvexity requires a suitably constructed supporting kernel, rather than the unmodified convex-domain denominator.''',
     ['henkin1969integral'], reconstruction='Smooth strict convexity and continuous boundary values are sufficient hypotheses supplied for an unambiguous classical integral.',
     status='Established; no new existence problem is posed by this formula.')
item(292,'P000483','claim','A compact localization error with a half-Hölder gain',
     r'''The operator \(f\mapsto f g-f_g\) is said to be completely continuous and to satisfy a Hölder condition of exponent \(1/2\), but the displayed definition of \(f_g\) does not show its dependence on f.''',
     r'''A precise sufficient interpretation uses a smooth bounded strictly pseudoconvex domain, \(f\in A(D)=\mathcal O(D)\cap C(\overline D)\), and a fixed smooth cutoff g. Apply a bounded \(\overline\partial\)-solution operator T with a half-Hölder estimate to \(f\overline\partial g\), and put \(f_g=fg-T(f\overline\partial g)\). Then \(f_g\) is holomorphic and \(f\mapsto fg-f_g\) maps the unit ball of A(D) into a bounded subset of \(C^{0,1/2}(\overline D)\), hence is compact into \(C(\overline D)\).''',
     r'''The localization and uniform-estimate method is already present in \citet[Theorem 1.2]{henkin1969integral} and \citet[\S1]{henkin1970integral}. The precise abbreviated operator in the notebook is only partially matched.''',
     ['henkin1969integral','henkin1970integral'], match='partial', confidence='medium',
     reconstruction=r'The definition through a solution operator is editorial. The notes do not specify the cutoff regularity, source norm, or whether \(f_g\) denotes a projection of \(fg\).',
     status='The reconstructed compactness statement is established; identifying the exact boundary operator from the abbreviation alone is not possible.')
item(292,'P000483','theorem','A strictly pseudoconvex domain as a convex-domain section',
     r'''A domain with strictly plurisubharmonic defining function is a closed submanifold of a strictly convex domain and meets its boundary transversely; the parenthesis reads \ru{следует из теор. Ока}.''',
     r'''Let \(D\Subset\mathbb C^n\) have smooth strictly pseudoconvex boundary. There are a Stein neighbourhood U of \(\overline D\), chosen with \(\overline D\) holomorphically convex in U, a proper holomorphic embedding \(F:U\to\mathbb C^N\), and a bounded smoothly strongly convex domain \(\Omega\) such that \(F(D)=F(U)\cap\Omega\) is a closed complex submanifold of \(\Omega\), and \(F(U)\) meets \(\partial\Omega\) transversely. The target dimension may exceed n.''',
     r'''The precise result appears in \citet[Proposition 14, Russian p.~111]{henkinchirka1975boundary} (1975; English 1976, p.~668); the modern formulation is \citet[Theorem 1]{forstneric2026embedding}. Fornæss obtained the independent 1976 realization. Class A records Henkin's coauthorship of the subsequent account.''',
     ['henkinchirka1975boundary','forstneric2026embedding'], cls='A',
     reconstruction='Embedding, enlarged ambient dimension, analytic submanifold, regular boundary, and transversality are made explicit. The notebook does not contain an Oka-theoretic proof.',
     status='Established convex embedding theorem; a generic closed subset of a convex domain would not suffice.')
item(292,'P000483','theorem','Bounded extension from a transverse analytic submanifold',
     r'''In point 2, \ru{выпис. продолж. с подмн-зия с оценками!} in the class of bounded functions.''',
     r'''Let D be a bounded smooth strictly pseudoconvex domain and let M be the intersection of D with a closed complex submanifold defined in a neighbourhood of \(\overline D\), transverse to \(\partial D\). There is a bounded linear right inverse \(E:H^\infty(M)\to H^\infty(D)\) of restriction, with \(\|Ef\|_\infty\le C\|f\|_\infty\). It can be chosen to take \(A(M)\) into \(A(D)\).''',
     r'''This is the main theorem of \citet[pp.~536--537]{henkin1972continuation}, received 8 December 1971 and published in the 1972 volume. Thus the imperative in the notebook records an announced construction or exposition, not an unaddressed 1973 open problem.''',
     ['henkin1972continuation'], status='Established under the smoothness and transversality hypotheses; these must remain attached to the estimate.')
item(292,'P000483','claim','The converse geometric implication',
     r'''The converse is said to hold: such a submanifold is a bounded domain of holomorphy.''',
     r'''A closed complex submanifold of a Stein convex domain is Stein. If it extends smoothly across the ambient strongly convex boundary and is transverse to it, the restricted defining function is strictly plurisubharmonic and defines a strongly pseudoconvex domain in the submanifold. Calling it a domain in \(\mathbb C^n\) additionally presupposes the given parametrization or embedding of D.''',
     r'''This is the classical Stein/submanifold direction used in the setting of \citet{henkin1972continuation}; it does not require the later difficult convex embedding theorem in the other direction.''',
     ['henkin1972continuation'], match='partial',
     reconstruction='The word analytic and the intrinsic meaning of domain of holomorphy are indispensable; an arbitrary smooth or closed subset is insufficient.',
     status='Established geometric implication, distinct from the forward embedding theorem.')
item(292,'P000483','theorem','The maximal ideal space of A(D)',
     r'''For functions analytic inside and continuous on the closure, the maximal ideal space equals the closure of the domain.''',
     r'''For a bounded smoothly strictly pseudoconvex domain \(D\subset\mathbb C^n\), every nonzero multiplicative continuous functional on the unital uniform algebra \(A(D)\) is evaluation at one point of \(\overline D\); the resulting identification of maximal ideal space with \(\overline D\) is a homeomorphism.''',
     r'''Already explicitly recorded in the introduction to \citet[p.~219]{ovrelid1971generators}, using uniform approximation by functions holomorphic near the closure. It is not the unrestricted corona problem for \(H^\infty(D)\).''',
     ['ovrelid1971generators'], status='Established for the continuous holomorphic algebra under the stated domain hypotheses.')
correction('P000483','Henkin point 2: submanifold','English: closed subset.',
           'Read closed analytic submanifold; preserve the manuscript abbreviation.',
           r'The Russian has \ru{подмн-зие}, repeated in the extension clause, and the transverse analytic-submanifold theorem identifies the intended category.',applies='en',typ='translation')
correction('P000483','Henkin localization operator',r'\(f\mapsto f g-f_g\) with \(f_g\) defined from g alone.',
           r'The dependence of \(f_g\) on f must be specified; retain as incomplete notation.',
           'Both transcriptions and the scan omit the needed dependence. An integral of g alone gives an affine, not the asserted linear, operator.',typ='ambiguity')
save()

talk(291,'1973-03-05','F. A. Berezin','P000484-P000487',
     'Quantization, coherent-state symbols, and Kähler geometry',
     r'''The talk passes from a correspondence-principle definition of quantization to the Fock model, covariant and contravariant symbols, trace inequalities, and constructions from Bergman kernels. The compact symmetric and disk examples close the record. The symbol calculus is already in the 1972 paper; the quantization programme was announced in Doklady in 1973 (received 14 December 1972), expanded in 1974, and applied to complex symmetric spaces in 1975. The notebook contains several consequential sign, conjugation, and measure-normalization errors. Its formal and convergent analytic meanings must be separated.''')
item(291,'P000484','definition','The symplectic Poisson bracket',
     r'''For a symplectic manifold M with matrix \(\omega_{ik}\) and inverse \(\omega^{ik}\), \([f,g]=\sum\omega^{ik}\partial_i f\partial_k g\).''',
     r'''On a smooth manifold equipped with a closed nondegenerate two-form \(\omega\), its inverse bivector defines \(\{f,g\}=\omega^{-1}(df,dg)\), with the sign fixed by that inverse convention. Closedness is the condition making the Jacobi identity hold. The notebook's complex-coordinate form suppresses the factor i needed for a real Kähler form.''',
     r'''Classical symplectic geometry, restated as the starting data in \citet[\S1]{berezin1974quantization}.''',
     ['berezin1974quantization'],status='Established definition; a nondegenerate but nonclosed two-form is not sufficient.')
item(291,'P000484','definition','Associative quantization and the correspondence principle',
     r'''A family of associative rings \(A_h\) of functions has \(f*_0g=fg\) and \(\partial_h(f*_hg-g*_hf)|_{h=0}=\{f,g\}\).''',
     r'''A formal interpretation specifies an associative \(\mathbb C[[h]]\)-bilinear product \(f*g=fg+hC_1(f,g)+\cdots\) on a chosen function algebra, with \(C_1(f,g)-C_1(g,f)=\{f,g\}\). An analytic interpretation instead specifies admissible real h, symbol domains and a topology for the limit. Factors of i can be absorbed into h; a real Hermitian convention usually has \(ih\{f,g\}\). These are different existence problems.''',
     r'''The quantization definition and examples were announced in \citet{berezin1973bounded} and developed in \citet[\S1]{berezin1974quantization}.''',
     ['berezin1973bounded','berezin1974quantization'],cls='A',
     reconstruction='Formal series are supplied as one exact interpretation, not substituted silently for Berezin’s analytic family.',
     status='Established framework. The displayed first-order condition alone neither ensures associativity at higher orders nor selects a unique quantization.')
item(291,'P000484','definition','The optional constant unit',
     r'''Requirement 3: every \(A_h\) has a unit corresponding to \(f_0\equiv1\).''',
     r'''The constant symbol 1 is required to satisfy \(1*_h f=f*_h1=f\) on the specified symbol algebra for every admissible h. Having some nonconstant unit is weaker than this normalization.''',
     r'''Explicit quantization axiom in \citet[\S1]{berezin1974quantization}; the later question on P000486 concerns precisely this extra requirement.''',
     ['berezin1974quantization'],cls='A',literal='correct',status='Well-defined normalization; see problem GP-1972-401 below.')
item(291,'P000484','definition','Trace and symplectic volume',
     r'''Requirement 4: a trace on a distinguished set, with \(\operatorname{Sp}(f*g)=\operatorname{Sp}(g*f)\) and \(\operatorname{Sp}f=c\int f\,d\mu\).''',
     r'''For \(\dim_{\mathbb R}M=2n\), the natural volume is \(\omega^n/n!\). A trace is a linear functional on a specified ideal of integrable or trace-class symbols, cyclic whenever both products lie in its domain. The scalar c may depend on h. It is not asserted that every bounded operator or arbitrary symbol has finite trace.''',
     r'''The trace axiom is formulated in \citet[\S1]{berezin1974quantization}; the actual operator-symbol trace identities already appear in \citet[\S1, formulas (1.13)--(1.16)]{berezin1972symbols}.''',
     ['berezin1974quantization','berezin1972symbols'],cls='A',status='Established in the models with the indicated trace ideal; convergence is part of the assertion.')
item(291,'P000484','remark','Naturality relative to a chosen category',
     r'''Quantization should be functorial for canonical diffeomorphisms, with the qualification ``some fixed category''. Two Kähler classes are named.''',
     r'''For a specified group G of symplectic symmetries, one may require pullback to act by algebra automorphisms of each \(A_h\), compatibly with composition. This covariance requirement is precise once G, the symbol spaces, and equivalence of quantizations are fixed. The notebook does not claim a functor on all symplectic manifolds and all canonical transformations.''',
     r'''This relative naturality is built into \citet[\S1 and \S3]{berezin1974quantization}. Earlier prequantization items 1969-178.3--4 and 1971-229.4 concern different constructions.''',
     ['berezin1974quantization'],cls='A',match='partial',status='A meaningful specified-category axiom; unrestricted functorial quantization is not established by this entry.')
item(291,'P000484','construction','The Gaussian Fock product and its domain',
     r'''An integral of \(f_1(z,\bar v)f_2(v,\bar z)e^{-|z-v|^2/h}\) defines the product on entire real-analytic functions.''',
     r'''For h>0 use \(d\nu_h(v)=(\pi h)^{-n}d^{2n}v\). On polynomial symbols the formula \((f*g)(z,\bar z)=\int f(z,\bar v)g(v,\bar z)e^{-|z-v|^2/h}d\nu_h(v)\) converges and is associative; it equals \(\sum_\alpha h^{|\alpha|}(\partial_{\bar z}^\alpha f)(\partial_z^\alpha g)/\alpha!\). Larger analytic classes require growth estimates. Entire real analyticity alone does not ensure integrability against a Gaussian.''',
     r'''The Fock symbol calculus predates the seminar and is treated in \citet{berezin1972symbols}; see also \citet[\S4]{berezin1974quantization}.''',
     ['berezin1972symbols','berezin1974quantization'],literal='false as written',
     reconstruction='Polynomial symbols give a sufficient closed algebra. The measure convention removes suppressed powers of pi; unrestricted entire functions are not admitted.',
     status='Established on specified symbol classes, with the displayed bidifferential formula also meaningful formally.')
item(291,'P000484','construction','The Fock representation must be complex linear',
     r'''The representation formula writes \(f(z,v)\overline{\varphi(v)}\), while its next anti-Wick formula has \(\varphi(v)\).''',
     r'''On \(\mathcal F_h=\{\varphi\in\mathcal O(\mathbb C^n):\int|\varphi|^2e^{-|z|^2/h}d\nu_h<\infty\}\), the covariant-symbol kernel acts as \((A_f\varphi)(z)=\int f(z,\bar v)\varphi(v)e^{z\bar v/h-|v|^2/h}d\nu_h(v)\). Domain conditions are needed for unbounded polynomial operators. Conjugating \(\varphi\) would instead make the map antilinear.''',
     r'''The corrected kernel is the reproducing-kernel realization in \citet{berezin1972symbols,berezin1974quantization}. The scan confirms that the misplaced bar is in the manuscript.''',
     ['berezin1972symbols','berezin1974quantization'],literal='false as written',development='annotated',
     reconstruction='The bar is moved from the input vector to the second kernel variable as a mathematical emendation.',
     status='The corrected formula is standard; the literal displayed map is not the claimed linear representation.')
item(291,'P000484','construction','Creation, annihilation, and the two orderings',
     r'''The notes give \(a=\partial_z\), \(a^*=z\), normal and antinormal orderings, and symbolic monomials with opposite placements of bars.''',
     r'''On the polynomial core of \(\mathcal F_h\), put \(a=h\partial_z\) and \(a^*=z\); these are Hilbert adjoints after closure and \([a_j,a_k^*]=h\delta_{jk}\). The normally ordered \((a^*)^m a^n\) has covariant symbol \(z^m\bar z^n\). A contravariant monomial is quantized in the opposite order \(a^n(a^*)^m\). The derivative without h is the h=1 convention.''',
     r'''These are the Wick/anti-Wick realizations developed before the talk in \citet{berezin1972symbols}.''',
     ['berezin1972symbols'],literal='false as written',
     reconstruction='The stated h-dependent Gaussian determines the adjoint normalization; the notation a* cannot simultaneously mean its Hilbert adjoint with the unscaled derivative.',
     status='Established after fixing h and the symbol orientation.')
item(291,'P000485','definition','Coherent states and covariant symbols',
     r'''\(e_{\bar v}(z)=e^{z\bar v/h}\); the quotient of matrix coefficients equals \(\operatorname{Sp}(AP_v)\).''',
     r'''Write \(e_v(z)=e^{z\bar v/h}\), \(k_v=e_v/\|e_v\|\), and \(P_v=|k_v\rangle\langle k_v|\). For a bounded operator A its covariant symbol is \(\sigma(A)(v)=\langle Ak_v,k_v\rangle=\operatorname{Tr}(AP_v)\). The same vector must occur in both slots and the denominator; the notebook alternates v and \(\bar v\) in the labels.''',
     r'''This is the definition in \citet[\S1, formula (1.2)]{berezin1972symbols}.''',
     ['berezin1972symbols'],status='Established. Off-diagonal polarization of the symbol is an additional analytic step.')
item(291,'P000485','theorem','Boundedness duality for symbols',
     r'''Bounded A implies bounded Wick symbol; bounded anti-Wick symbol implies bounded A.''',
     r'''For normalized coherent states, \(\|\sigma(A)\|_\infty\le\|A\|\). For a normalized resolution \(\int P_vd\nu_h(v)=I\), the weak integral \(T_a=\int a(v)P_vd\nu_h(v)\) satisfies \(\|T_a\|\le\|a\|_\infty\). The two arrows concern different symbol maps and are not inverse norm equivalences.''',
     r'''These estimates are in \citet[\S1, formula (1.14) and the compression construction]{berezin1972symbols}.''',
     ['berezin1972symbols'],literal='correct',status='Established; a bounded covariant symbol alone is not the stated boundedness criterion.')
item(291,'P000485','theorem','Compactness and decay in the Fock model',
     r'''Compact A implies f tends to zero; a contravariant symbol tending to zero gives a compact operator.''',
     r'''In the Fock model, normalized \(k_v\) tends weakly to zero as \(|v|\to\infty\), so compact A has \(\sigma(A)(v)\to0\). If \(a\in C_0(\mathbb C^n)\), then \(T_a\) is compact: approximate a uniformly by compactly supported symbols, whose coherent-projector integrals are trace class. The assertion needs this geometry and cannot be carried unchanged to an arbitrary frame.''',
     r'''This is the symbol-calculus compactness mechanism associated with \citet{berezin1972symbols}; the stated sufficient Fock hypotheses explain the shorthand.''',
     ['berezin1972symbols'],match='partial',development='annotated',
     reconstruction=r'\ours\ The two-sentence compactness verification is editorial; no equivalence with arbitrary vanishing covariant symbols is asserted.',
     status='Established in this setting; ``all theorems hold'' later on the page requires additional assumptions for this one.')
item(291,'P000485','theorem','Trace class and the two trace integrals',
     r'''``Nuclearity (analog.)'' followed by equal integrals of Wick and anti-Wick symbols.''',
     r'''If A is trace class, its covariant symbol is integrable against the normalized frame measure and \(\operatorname{Tr}A=\int\sigma(A)d\nu_h\). If \(a\in L^1(d\nu_h)\), then \(T_a\) is trace class, \(\|T_a\|_1\le\|a\|_1\), and \(\operatorname{Tr}T_a=\int a\,d\nu_h\). These sufficient statements do not say that integrability of an arbitrary covariant symbol implies trace class.''',
     r'''Read in \citet[\S1, formulas (1.13)--(1.16)]{berezin1972symbols}.''',
     ['berezin1972symbols'],status='Established with trace-class and integrability assumptions made explicit.')
item(291,'P000485','construction','Gaussian conversion and the Weyl midpoint',
     r'''The Wick symbol is the Gaussian convolution of the anti-Wick symbol; h/2 gives the Weyl symbol.''',
     r'''For a Schwartz contravariant symbol a in the flat model, \(\sigma(T_a)=B_ha\), where \(B_ha(z)=\int a(v)e^{-|z-v|^2/h}d\nu_h(v)=e^{(h/4)\Delta_{\mathbb R^{2n}}}a(z)\). In the consistent Weyl convention the Weyl symbol of the same operator is \(e^{(h/8)\Delta}a\). These constants depend on the chosen real coordinates and h convention.''',
     r'''The conversion formula is explicit in \citet[\S1, formula (1.12)]{berezin1972symbols}; the flat quantizations are compared in \citet[\S4 and \S7]{berezin1974quantization}.''',
     ['berezin1972symbols','berezin1974quantization'],status='Established Gaussian/heat relation; inverse heat evolution is not bounded on arbitrary function spaces.')
item(291,'P000485','remark','Gelfand’s Poincaré attribution',
     r'''The parenthetical says that these are Poincaré's symbols, without a title, formula, or date.''',
     'No uniquely identifiable mathematical attribution follows. It could concern symmetric ordering or an earlier symbolic calculus, but the notebook supplies no discriminating reference.',
     'Searches of the Berezin 1972 and 1974 papers and their bibliographies did not identify the precise Poincaré source intended. The established Weyl conversion in the previous item does not verify this historical attribution.',
     ['berezin1972symbols','berezin1974quantization'],cls='F',literal='not determinable',match='none found',verification='unresolved lead',confidence='low',
     status='Attribution unresolved; no research problem or priority conclusion is inferred.',speaker='I. M. Gelfand')
item(291,'P000485','construction','Continuous Parseval frames and the missing norm weight',
     r'''An overcomplete system satisfies \(\|f\|^2=\int|\langle f,e_\alpha\rangle|^2d\alpha\), but the contravariant reconstruction is written \(A=\int\mathring A(\alpha)P_\alpha d\alpha\) with orthogonal projectors.''',
     r'''For a measurable continuous Parseval frame, \(I=\int|e_\alpha\rangle\langle e_\alpha|d\alpha\) weakly. If \(P_\alpha\) is the orthogonal rank-one projector, the appropriate measure is \(d\nu=\|e_\alpha\|^2d\alpha\), omitting zero vectors. Then \(A=\int a(\alpha)P_\alpha d\nu\). In general a contravariant symbol need not exist for every A and need not be unique.''',
     r'''The norm factor is explicitly present in \citet[\S1, formulas (1.1)--(1.3)]{berezin1972symbols}.''',
     ['berezin1972symbols'],literal='false as written',status='Established frame construction; normalization cannot be dropped when the vectors are not unit vectors.')
item(291,'P000485-P000486','construction','Compression and the Fourier example',
     r'''Embed H into \(L^2(M)\), multiply by the contravariant symbol, and compress by the orthogonal projection. The next page names \(e^{i(p,x)}\) on bounded domains.''',
     r'''For the frame analysis isometry \(V:H\to L^2(M,d\alpha)\), \(T_a=V^*M_aV\); on VH this is \(PM_aP\). For a bounded measurable \(\Omega\subset\mathbb R^n\), the restricted exponentials \((2\pi)^{-n/2}e^{ip\cdot x}\) form a continuous Parseval frame in \(L^2(\Omega)\) by Plancherel. Their normalization determines the projector measure.''',
     r'''This is the multiplication-compression realization in \citet[\S1, formula (1.5)]{berezin1972symbols}; the Fourier example is a standard instance.''',
     ['berezin1972symbols'],literal='correct',status='Established; writing PMP as an operator on the full ambient space adds a zero block.')
item(291,'P000486','theorem','The convex trace inequalities',
     r'''For a convex function \(\varphi\), \(\int\varphi(A)\le\operatorname{Sp}\varphi(\hat A)\le\int\varphi(\mathring A)\). The lower bound is called Jensen's inequality; the upper one is written as a compression inequality.''',
     r'''For a normalized projector resolution, a self-adjoint A admitting a real contravariant symbol a, and a convex scalar function \(\varphi\), one has \(\int\varphi(\sigma(A))d\nu\le\operatorname{Tr}\varphi(A)\le\int\varphi(a)d\nu\) whenever the terms are finite (or in a consistent extended nonnegative sense). The compression trace is taken on PH; in infinite dimension one cannot include an infinite zero block with \(\varphi(0)\ne0\). Scalar convexity suffices for this trace inequality, not for an operator inequality.''',
     r'''This is \citet[\S2, Theorem 2]{berezin1972symbols}, published before the seminar.''',
     ['berezin1972symbols'],status='Established Berezin trace inequalities with the trace domain and frame measure specified.')
item(291,'P000486','construction','The Bergman cross-ratio and weighted holomorphic space',
     r'''The kernel \(G_h\) has diagonal Bergman factors in the numerator, and the Hilbert-space weight is \(K(z,\bar z)^{+1/h}\).''',
     r'''In a homogeneous bounded domain with admissible h and a consistent analytic power of K, use the weighted space with measure \(K(z,\bar z)^{-1/h}d\mu(z)\), where \(d\mu\) is invariant volume. The normalized overlap in the product is \([K(z,\bar v)K(v,\bar z)/(K(z,\bar z)K(v,\bar v))]^{1/h}\), with a normalization factor and the invariant integration measure. Cauchy--Schwarz bounds the base of this ratio by 1; its reciprocal has the wrong concentration behaviour.''',
     r'''The corrected ratios and negative weight are in \citet[\S2, especially (2.23), and \S5]{berezin1974quantization}; the short precursor is \citet{berezin1973bounded}.''',
     ['berezin1973bounded','berezin1974quantization'],cls='A',literal='false as written',development='annotated',
     reconstruction='Both sign changes are mathematical emendations: the scan confirms the positive weight and reciprocal ratio. The unspecified volume density is also supplied.',
     status='Established homogeneous construction. The formulas do not define a quantization on all real-analytic functions of every domain.')
unit_id=item(291,'P000486','question','A constant unit outside the homogeneous case',
     r'''A marginal question asks whether there exists a quantization also satisfying condition 3; an arbitrary scalar \(c_1(h)\) is written in \(c(h)=h^{-n}c_1(h)\).''',
     r'''The supported analytic question is whether the proposed Bergman-kernel integral construction can be given nontrivial symbol algebras and a constant unit on a specified nonhomogeneous domain. The domain class, admissible h, convergence bounds and allowed changes of kernel are not fixed. A separately precise formal variant asks for a unital associative deformation product on a Kähler manifold.''',
     r'''\citet[\S2.8, p.~1133]{berezin1974quantization} explicitly retains an analytic obstruction even to nonzero algebras without his hypothesis A. \citet[\S4, Proposition 4.3]{reshetikhintakhtajan2000deformation} construct a normalized unital formal product on arbitrary Kähler manifolds. That result does not establish convergence of the notebook integral or scalar normalization on every nonhomogeneous domain.''',
     ['berezin1974quantization','reshetikhintakhtajan2000deformation'],cls='F',literal='not determinable',match='partial',confidence='medium',
     reconstruction='The formal theorem is contextual comparison only. The missing analytic category prevents identification of one precisely formulated question of which that theorem would be a partial solution.',
     status='The formal unital theorem is established, but the intended convergent analytic problem is not identifiable with precise quantifiers. This occurrence is not registered as an open problem.')
item(291,'P000486','theorem','Homogeneity fixes the normalization',
     r'''For a homogeneous domain condition 3 holds and fixes \(c_1(h)\); \(e_v(z)=K(z,\bar v)^{1/h}\) gives the coherent system.''',
     r'''For a bounded homogeneous domain and the admissible positive parameters in Berezin's construction, the weighted reproducing kernel is a constant multiple of \(K^{1/h}\). Transitivity makes the diagonal normalization spatially constant. Choosing the reciprocal constant gives the reproducing identity and hence constant symbol 1 as the unit.''',
     r'''This is the homogeneous-domain construction of \citet[\S5]{berezin1974quantization}, announced in \citet{berezin1973bounded}.''',
     ['berezin1973bounded','berezin1974quantization'],cls='A',status='Established for admissible parameters; arbitrary positive h is not part of the statement.')
item(291,'P000486','claim','The shorthand uniqueness assertion on symmetric domains',
     r'''If the domain is symmetric and its motions act by ring automorphisms, \ru{то только это} (only this).''',
     r'''No fully quantified uniqueness theorem can be recovered from these words: the class of algebras, equivalence, irreducibility and admissible parameters are missing. The later paper formulates exhaustion of irreducible effective w*-quantizations on classical complex symmetric spaces as a conjecture, with the sphere case then proved.''',
     r'''Compare \citet[Introduction, pp.~341--342]{berezin1975symmetric} and the restricted uniqueness discussion in \citet[\S7]{berezin1974quantization}. They prevent treating the notebook's blanket phrase as an established theorem. No exact current problem is extracted from unspecified hypotheses.''',
     ['berezin1975symmetric','berezin1974quantization'],cls='F',literal='not determinable',match='partial',confidence='medium',
     status='The precise intended uniqueness assertion is not identifiable; covariance alone is not enough to assert it.')
zero_id=item(291,'P000486','question','Can the Bergman kernel vanish?',
     r'''One parenthesis says \(K(z,\bar v)\ne0\); later the general case is called unknown.''',
     r'''For a bounded domain G the off-diagonal Bergman kernel can vanish. Every planar annulus \(r<|z|<1\), \(0<r<1\), has zeros. In contrast the disk and bounded homogeneous complete circular domains have zero-free kernels. Positivity of \(K(z,\bar z)\) on the diagonal is a different assertion.''',
     r'''The annulus counterexamples are already from 1969 (Rosenthal and Skwarczyński); the precise statements and original references are checked in \citet[\S4, pp.~258--259]{boas2000luqikeng}. The original 1969 full texts were not accessible in this run, so the chronology rests on this author survey.''',
     ['boas2000luqikeng'],cls='E',literal='false as written',match='exact',verification='indirect',problem='GP-1972-402',
     reconstruction='The negative unrestricted answer is separated from valid zero-freeness in the model homogeneous domains.',
     status='The unrestricted question had a negative answer before this seminar. No broader classification problem is silently substituted.')
PROBLEMS.append(dict(id='GP-1972-402',title='Off-diagonal zeros of the Bergman kernel',statement=ITEMS[-1]['statement'],occurrences=[zero_id],status=ITEMS[-1]['present_status'],status_date='2026-11',refs=ITEMS[-1]['refs']))
item(291,'P000486','claim','Global polarization of covariant symbols',
     r'''Covariant symbols have analytic continuations to all of \(G\times\bar G\).''',
     r'''For a reproducing-kernel Hilbert space with nowhere-zero kernel \(K_h(z,\bar v)\), the covariant symbol of a bounded operator polarizes as its operator kernel divided by \(K_h\); it is holomorphic in z and antiholomorphic in v on the product. If the denominator has zeros, the quotient may have poles and the blanket global extension no longer follows.''',
     r'''This is the symbol realization under the kernel hypotheses in \citet[\S2]{berezin1974quantization}.''',
     ['berezin1974quantization'],cls='A',status='Established in the zero-free homogeneous setting; related to the preceding kernel-zero question.')
item(291,'P000486-P000487','construction','Compact Hermitian symmetric quantization',
     r'''A Kähler potential is exponentiated; at \(h=1/n\) a single-valued kernel exists and the Hilbert space is finite-dimensional with computable dimension.''',
     r'''For an integral positive Kähler class on a compact classical Hermitian symmetric manifold, choose its positive holomorphic line bundle L. At integral tensor powers \(L^n\), the quantum space is \(H^0(M,L^n)\), finite-dimensional; local kernels glue as sections with transition factors, not generally as scalar functions on all of \(M\times\bar M\). The potential is local and \(g_{i\bar j}=\partial_i\partial_{\bar j}\Phi\), not the inverse matrix. The relation h=1/n uses a fixed integral normalization.''',
     r'''The compact classical symmetric cases and their parameter/dimension formulas are developed in \citet[compact-space part]{berezin1975symmetric}. The notebook announcement precedes that publication; it does not supply a global scalar potential.''',
     ['berezin1975symmetric'],cls='A',literal='false as written',
     reconstruction='The line-bundle formulation supplies the indispensable global gluing and integrality conditions.',
     status='Established for the specified integral compact symmetric models. Arbitrary Kähler scaling does not automatically permit h=1/n.')
item(291,'P000487','construction','The disk and its projective symmetry representation',
     r'''For the Lobachevsky plane the notebook writes \(K^{1/h}=(1-z\bar z)^{+2/h}\), followed by a projective representation of its automorphism group.''',
     r'''On the unit disk the Bergman kernel is proportional to \((1-z\bar v)^{-2}\). With \(\beta=2/h>1\), the weighted holomorphic norm has density proportional to \((1-|z|^2)^{\beta-2}d^2z\) and reproducing kernel \((1-z\bar v)^{-\beta}\). The automorphism group acts projectively by weighted composition; a genuine representation can be taken on a suitable covering group. The positive exponent belongs to the reciprocal weight, not the reproducing kernel.''',
     r'''The disk specializes the homogeneous-domain construction in \citet[\S5, Theorems 5.1--5.2]{berezin1974quantization}; parameters and symmetry are developed further in \citet{berezin1975symmetric}.''',
     ['berezin1974quantization','berezin1975symmetric'],cls='A',literal='false as written',status='Established. The displayed sign must be corrected and the Hilbert-space parameter range specified.')
for page,place,reads,should,evidence in [
 ('P000484','Fock representation',r'\(f(z,v)\overline{\varphi(v)}\)',r'\(f(z,\bar v)\varphi(v)\)', 'The scan places the bar over the input vector. The literal operation is antilinear; the reproducing-kernel formula fixes the correction.'),
 ('P000484','Annihilation and adjoint',r'\(a=\partial_z,\ a^*=z\) for Gaussian parameter h.',r'\(a=h\partial_z,\ a^*=z\), or restrict this line to h=1.', r'Monomial Gaussian norms are proportional to \(h^m m!\), which determine the adjoint. The displayed h was not specialized in the notes.'),
 ('P000484','Normal-symbol monomials',r'\((a^*)^m a^n\leftrightarrow\bar z^m z^n\).',r'\((a^*)^m a^n\leftrightarrow z^m\bar z^n\) in the stated Fock convention.', 'The representation sends the creation operator to multiplication by z; direct coherent-state evaluation interchanges the displayed bars.'),
 ('P000485','General contravariant integral',r'\(A=\int aP_\alpha d\alpha\) after an unnormalized Parseval identity.',r'\(A=\int aP_\alpha\|e_\alpha\|^2d\alpha\), or absorb the weight in the measure.', 'Rank-one orthogonal projectors differ from outer products by the squared norm; the 1972 paper includes it.'),
 ('P000486','Bergman overlap ratio','Diagonal kernel factors in numerator.', 'Off-diagonal factors in numerator, diagonal factors in denominator.', 'The scan confirms the reciprocal ratio; Cauchy--Schwarz and the Gaussian limit determine the mathematical correction.'),
 ('P000486','Holomorphic Hilbert-space weight',r'\(K^{+1/h}\).',r'\(K^{-1/h}\) against invariant volume.', 'No minus is visible in the scan. The positive sign makes the model boundary weight grow in the wrong direction.'),
 ('P000487','Kähler potential matrix',r'\(\omega^{ij}=\partial_i\partial_{\bar j}\Phi\).',r'\(g_{i\bar j}=\partial_i\partial_{\bar j}\Phi\); inverse coefficients belong to the Poisson tensor.', 'The scan uses upper indices; the earlier page defines upper indices as the inverse. These two conventions conflict.'),
 ('P000487','Disk kernel exponent',r'\((1-z\bar z)^{+2/h}\).',r'Kernel: \((1-z\bar z)^{-2/h}\); reciprocal weight has the positive exponent.', 'The plus is explicit in the scan. Comparison with the reproducing kernel and the corrected weight resolves its role.')]:
    correction(page,place,reads,should,evidence)
save()

talk(296,'1973-03-26','I. M. Gelfand','P000495',
     'Atiyah--Patodi--Singer spectral asymmetry',
     r'''Gelfand announces the eta series, its regular value at zero, and the shifted-circle example, then suggests more general character-weighted spectral series. The 1973 APS announcement was received eleven days before this seminar. The later proofs require a chronology distinction: APS established the geometric cases and odd-dimensional general theorem, while Gilkey completed general even-dimensional regularity in 1981.''')
item(296,'P000495','theorem','Regularity of an elliptic zeta function at zero',
     r'''For a self-adjoint elliptic A, \(\zeta_A(s)=\operatorname{Tr}A^{-s}=\sum\lambda_i^{-s}\) has no pole at zero (Seeley).''',
     r'''A sufficient unambiguous setting is a positive invertible classical elliptic pseudodifferential operator A of order m>0 on a vector bundle over a closed smooth d-manifold. The spectral sum converges for \(\operatorname{Re}s>d/m\), extends meromorphically, and is regular at zero. For nonnegative A omit the zero eigenvalues; for general nonpositive A a complex-power spectral-cut convention is needed.''',
     r'''Known before the seminar: \citet{seeley1968powers}; the exact zeta statement and the null-space modification are recalled in \citet[\S2, pp.~73--74]{atiyahpatodisinger1976spectral3}.''',
     ['seeley1968powers','atiyahpatodisinger1976spectral3'],status='Established. Self-adjointness alone does not define the written complex powers without handling negative and zero eigenvalues.')
item(296,'P000495','definition','The eta function of a self-adjoint elliptic operator',
     r'''\(\eta_A(s)=\sum_{\lambda\ne0}\operatorname{sign}(\lambda)|\lambda|^{-s}\), emphasized for a first-order operator.''',
     r'''For a self-adjoint classical elliptic operator A of positive order m on a Hermitian bundle over a closed smooth d-manifold, take eigenvalues with multiplicity and omit the kernel. The series converges absolutely for \(\operatorname{Re}s>d/m\) and has meromorphic continuation. In that half-plane it equals \(\operatorname{Tr}(A|A|^{-s-1})\).''',
     r'''The new invariant was announced in \citet{atiyahpatodisinger1973spectral}; its geometric role is developed in \citet[Introduction and \S4]{atiyahpatodisinger1975spectral1}. Class B records development by the reported authors, not by the seminar speaker.''',
     ['atiyahpatodisinger1973spectral','atiyahpatodisinger1975spectral1'],cls='B',status='Established eta-function definition; the boundary index theorem is its published fate, not an extra theorem recorded on this page.')
item(296,'P000495','theorem','The eta function has no pole at zero: announcement and proof scope',
     r'''\ru{Трудная теор.}: zero is not a pole, stated without a dimension or operator subclass restriction.''',
     r'''For every self-adjoint classical elliptic pseudodifferential operator of positive order on a closed smooth manifold, the meromorphic eta function is regular at s=0. This is a statement about the integrated spectral function; its local residue density need not vanish pointwise.''',
     r'''APS announced the unrestricted assertion in 1973 but explicitly reported the remaining even-dimensional gap in \citet[Introduction, pp.~71--72; Theorem 4.5]{atiyahpatodisinger1976spectral3}. The general result is \citet[Theorem 0.1, pp.~290--291]{gilkey1981residue}. The geometric Dirac-type case already occurs in \citet[Theorem 4.2]{atiyahpatodisinger1975spectral1}.''',
     ['atiyahpatodisinger1973spectral','atiyahpatodisinger1975spectral1','atiyahpatodisinger1976spectral3','gilkey1981residue'],cls='B',
     reconstruction='The closed-manifold and classical-operator hypotheses are supplied. The later proof gap is not projected back into the notebook as a question explicitly asked there.',
     status='Established in full stated generality by the later completion; it would be historically inaccurate to attribute that full proof to the 1973 announcement.')
item(296,'P000495','claim','The shifted circle eta invariant',
     r'''For \(A=i\,d/dx+t\) on periodic functions on \([0,2\pi]\), eigenvalues are \(n+t\), and \(\eta_A(0)=1-2t\).''',
     r'''For real t, the spectrum is \(\mathbb Z+t\). If \(a=\{t\}\in(0,1)\), then \(\eta_A(s)=\zeta(s,a)-\zeta(s,1-a)\), so \(\eta_A(0)=1-2a\). If t is integral, omitting the zero eigenvalue gives \(\eta_A(0)=0\). Thus the notebook formula is correct only on the branch 0<t<1.''',
     r'''This is the elementary model of spectral asymmetry in the APS programme; the evaluation uses \(\zeta(0,a)=1/2-a\), checked in \citet[\S25.11]{nist2026dlmf}.''',
     ['atiyahpatodisinger1975spectral1','nist2026dlmf'],cls='B',literal='false as written',match='partial',development='annotated',
     reconstruction=r'\ours\ The Hurwitz-zeta derivation and the integral-t correction are supplied explicitly; shifting t by 1 independently checks the required periodicity.',
     status='Established branch formula with integer jumps; the unrestricted affine formula cannot be correct.')
item(296,'P000495','remark','Spectral asymmetry is a regularized difference',
     r'''\(\eta(0)\) is described by \(\sum_{\lambda>0}1-\sum_{\lambda<0}1\).''',
     r'''The displayed difference means evaluation at s=0 after meromorphic continuation of \(\sum\operatorname{sign}(\lambda)|\lambda|^{-s}\), not subtraction of two infinite dimensions. The reduced invariant is often \((\eta_A(0)+\dim\ker A)/2\), considered modulo integers, but that extra normalization is not given in the notebook.''',
     r'''The regularized interpretation is central to \citet[Introduction]{atiyahpatodisinger1975spectral1}; dependence on spectral flow connects thematically to the earlier GP-1971-04 thread without identifying the two questions.''',
     ['atiyahpatodisinger1975spectral1'],cls='B',status='Established regularized invariant, not an ordinary signed count.')
item(296,'P000495','question','Character-weighted spectral L-series',
     r'''The general problem proposes summing multiplicative characters of eigenvalues and remarks that complex numbers have more complicated characters.''',
     'The notebook does not specify the operator class, spectral cut, allowed characters, convergence factor, evaluation point, or invariant to be constructed. Its real sign-character example is identifiable, but a unique complex-spectrum theorem or definite open question is not.',
     'The APS papers supply the eta example, not a result with these unspecified complex-character quantifiers. Searching their announcements, later parts and the spectral-asymmetry literature did not identify an exact completion of this sentence.',
     ['atiyahpatodisinger1973spectral','atiyahpatodisinger1976spectral3'],cls='F',literal='not determinable',match='thematic only',verification='unresolved lead',confidence='low',
     status='Programme recognizable; a definite problem suitable for the problem index is not recoverable.')
correction('P000495','Circle eta formula',r'\(\eta(0)=1-2t\), unrestricted t.',
           r'For \(0<t<1\) this holds; otherwise use \(1-2\{t\}\), with value 0 at integers.',
           'The scan gives no branch restriction. Integer translation preserves the spectrum, whereas the affine expression is not periodic.')
save()

# Record 298 lies before Gabrielov's record 297 on the manuscript page.
talk(298,'1973-03-26','S. I. Gelfand','P000495-P000497',
     'p-adic distributions, integration and the zeta function',
     r'''The talk introduces finitely additive p-adic distributions on residue classes, contrasts the unbounded invariant distribution with a bounded floor-function construction, and gives a moderate-growth integration criterion. It then sketches interpolation of negative odd zeta values. The missing Euler factor, weight branch and possible pole make the final unqualified continuity assertion false. The source places this continuation before Gabrielov on P000497, although the catalogue numbers 297 and 298 suggest the reverse order.''')
item(298,'P000496','definition','Distributions on residue classes',
     r'''For \(A_m=p^m\mathbb Z_p\), the notes require \(\mu(a+A_m)=\sum_{j=0}^{p-1}\mu(a+jp^m+A_{m+1})\).''',
     r'''A K-valued distribution on \(\mathbb Z_p\), for a complete non-Archimedean extension K of \(\mathbb Q_p\), is a finitely additive function on compact open sets. It is determined by its values on residue classes, subject to the displayed refinement identity and independence of the representative a. A bounded distribution is a measure in the Banach-space sense, with \(\sup_{m,a}|\mu(a+p^m\mathbb Z_p)|<\infty\).''',
     r'''The distinction is made explicitly in \citet[\S8.4]{manin1973periods} and \citet[\S1]{manin1976nonarchimedean}; the underlying distribution formalism predates these lectures.''',
     ['manin1973periods','manin1976nonarchimedean'],status='Standard definition. Finite additivity alone does not imply a bounded functional on all continuous functions.')
item(298,'P000496','construction','The normalized invariant distribution is unbounded',
     r'''Translation invariance gives \(\mu(a+A_m)=p^{-m}\); the measure of a small set is large in the p-adic norm.''',
     r'''Among translation-invariant \(\mathbb Q_p\)-valued distributions with total mass 1, refinement forces \(\mu(a+p^m\mathbb Z_p)=p^{-m}\). Its norm on a level-m class is \(p^m\), so it is unbounded and does not define a continuous integration functional on all of \(C(\mathbb Z_p,\mathbb Q_p)\). Without total-mass normalization any constant multiple is possible.''',
     r'''This is the elementary invariant-distribution example recalled in \citet[\S8.4]{manin1973periods}.''',
     ['manin1973periods'],status='Established. The missing total-mass condition is necessary for the phrase only possibility.')
item(298,'P000496','construction','The bounded floor-function distribution',
     r'''For positive integer c prime to p, \(\mu_c(a+A_m)=\lfloor ca/p^m\rfloor-(c-1)/2\), with \(0\leq a<p^m\).''',
     r'''Using the canonical representative \(0\leq a<p^m\), this formula defines a bounded finitely additive \(\mathbb Q_p\)-valued distribution. For odd p its values are p-integral; for p=2 the condition c odd again makes every value integral. The representative convention is essential: the unrestricted floor expression is not periodic in a.''',
     r'''\citet[\S8.4, Example 2]{manin1973periods} gives this construction and attributes it to Mazur. It belongs to the pre-existing measure approach to p-adic zeta functions, not a new problem posed here.''',
     ['manin1973periods'],development='annotated',
     reconstruction=r'''\ours\ Refinement reduces to \(\sum_{j=0}^{p-1}\lfloor u+cj/p\rfloor=\lfloor pu\rfloor+(c-1)(p-1)/2\), with \(u=ca/p^{m+1}\). Permuting the residues cj modulo p proves the identity. An independent exact-integer check over several primes and c values is supplied.''',
     status='Established bounded distribution; the historical label in the notes suppresses the Mazur regularization step.')
item(298,'P000496','construction','The two-valued distribution for c equal to two',
     r'''\(\mu_2\) is \(+1/2\) above the midpoint and \(-1/2\) below it.''',
     r'''For an odd prime p and \(0\leq a<p^m\), \(\mu_2(a+p^m\mathbb Z_p)=-1/2\) if \(2a<p^m\) and \(+1/2\) if \(2a>p^m\). Equality is impossible. This example does not use c=2 at p=2, where c would not be prime to p.''',
     r'''This is the c=2 specialization of \citet[\S8.4]{manin1973periods}.''',
     ['manin1973periods'],status='Established, with the odd-prime restriction restored.')
item(298,'P000496','method','Riemann sums and the bounded case',
     r'''For a representative set \(R_m\), form \(S(R_m)=\sum_{a\in R_m}f(a)\mu(a+A_m)\), and seek a representative-independent limit.''',
     r'''If \(\mu\) is bounded and f is continuous on compact \(\mathbb Z_p\), these sums converge in K, independently of the representatives. Uniform continuity and the ultrametric triangle inequality bound any refinement error by \(\|\mu\|\) times the oscillation of f on residue classes. Locally constant f requires only finite additivity: the sums eventually stabilize.''',
     r'''This is standard non-Archimedean integration, formulated in \citet[\S1]{manin1976nonarchimedean}.''',
     ['manin1976nonarchimedean'],status='Established. The distinction between locally constant and continuous integrands matters for unbounded distributions.')
item(298,'P000496','theorem','Moderate growth suffices for Lipschitz integrands',
     r'''\(p^{-m}\max_a|\mu(a+A_m)|_p\to0\); a Lipschitz condition on f then gives the integral.''',
     r'''Let K be complete and put \(M_m=\max_a|\mu(a+p^m\mathbb Z_p)|\). If \(p^{-m}M_m\to0\) and \(|f(x)-f(y)|\leq C|x-y|_p\), the Riemann sums converge independently of representatives. A consecutive-level error is at most \(Cp^{-m}M_{m+1}\), which tends to zero; the ultrametric inequality gives the Cauchy property.''',
     r'''This is the criterion in \citet[\S8.6]{manin1973periods}, published after the seminar report of Manin's lectures. The class records development by the reported author.''',
     ['manin1973periods'],cls='B',status='Established sufficient condition. It excludes the normalized invariant distribution, whose scaled growth is constantly one.')
item(298,'P000497','theorem','Negative odd zeta values are rational',
     r'''\(\zeta(1-2k)\) is rational for every positive integer k and is expressed through Bernoulli numbers.''',
     r'''With \(t/(e^t-1)=\sum_{j\geq0}B_jt^j/j!\), \(\zeta(1-2k)=-B_{2k}/(2k)\) for k positive. This is a value of the meromorphic continuation, not of the original divergent Dirichlet series at that argument.''',
     r'''Classical before the seminar; see \citet[\S25.11]{nist2026dlmf} for the Hurwitz-zeta specialization and \citet[\S0.1]{manin1976nonarchimedean} for its interpolation role.''',
     ['nist2026dlmf','manin1976nonarchimedean'],status='Established. These values connect the next two arithmetic talks to the Bernoulli discussion on P000500.')
item(298,'P000497','claim','The uncorrected zeta sequence is not a continuous function of weight',
     r'''For arbitrary positive integers \(k_i\to a\) p-adically, the notes assert \(\zeta(1-2k_i)\to\zeta(a)\) and a continuous function on all \(\mathbb Z_p\).''',
     r'''The Kubota--Leopoldt interpolation uses \((1-p^{n-1})\zeta(1-n)\), with n restricted to a fixed residue class modulo p-1 for odd p, and with the appropriate tame-character branch. The zeta branch has a pole at s=1, so a universal continuous function on all weights is not obtained. The raw values in the notebook do not have the stated continuity property even on a nonpolar branch.''',
     r'''The theorem of \citet{kubotaleopoldt1964} predates the talk; \citet[\S0.1 and \S0.5]{manin1976nonarchimedean} explicitly explains the Euler factor and regularization. Original 1964 archival metadata was opened; the exact interpolation formula was read in Manin's exposition.''',
     ['kubotaleopoldt1964','manin1976nonarchimedean'],literal='false as written',verification='indirect',development='annotated',
     reconstruction=r'''\ours\ For p=5 take \(k_i=1+2\cdot5^i\). Then \(k_i\to1\) and \(2k_i\equiv2\pmod4\). Correct interpolation gives \(\zeta(1-2k_i)\to(1-5)\zeta(-1)=1/3\), since \(5^{2k_i-1}\to0\). The constant sequence k=1 instead gives \(-1/12\). The two limits differ. Exact Bernoulli arithmetic checks this discrepancy and the corrected congruences at small levels.''',
     status='The notebook statement is false; the properly normalized branch theorem is established. No unresolved interpolation problem is inferred.')
item(298,'P000496-P000497','claim','The Mellin transform and its regularizing factors',
     r'''The floor measure is first said to be obtained from a zeta function by a Mellin transform; the next page says the zeta function is the Mellin transform of the measure.''',
     r'''For a bounded measure on \(\mathbb Z_p^\times\), its Mellin transform is the function of a continuous character \(\chi\) given by \(\chi\mapsto\int\chi(a)\,d\mu(a)\). For the regularized Bernoulli measure, this gives a regularized p-adic L-function; the Euler factor and the auxiliary-c regularization factor must be retained or explicitly divided out where allowed. It is not literally the unmodified complex zeta function.''',
     r'''The direction of the transform and the regularization are spelled out in \citet[\S0.4--0.5]{manin1976nonarchimedean}.''',
     ['manin1976nonarchimedean'],literal='false as written',status='Established measure construction and Mellin transform, with the normalization caveat made explicit.')
correction('P000496','Invariant distribution uniqueness',r'\(p^{-m}\) is the only possibility.',r'This is the unique translation-invariant distribution of total mass 1.',
           'The scan states uniqueness without a normalization. Multiplying every value by a constant preserves finite additivity and invariance.')
correction('P000496-P000497','Mellin-transform direction', 'The measure is obtained by the Mellin transform from the zeta function.',
           'The Mellin transform sends the regularized measure to a character function; recovering a measure is the inverse problem.',
           'The scan confirms the reversed sentence on P000496; the continuation on P000497 has the forward direction.')
correction('P000497','Zeta continuity assertion',r'Raw \(\zeta(1-2k_i)\) has a limit depending only on \(\lim k_i\), everywhere.',
           r'Insert \(1-p^{2k_i-1}\), fix the tame-character branch, and exclude or account for the pole.',
           'The displayed notebook formula lacks these conditions. The p=5 counterexample and the published interpolation formula distinguish a faithful mathematical error from a transcription fault.')
save()

talk(299,'1973-04-09','S. I. Gelfand','P000498-P000499',
     'Manin’s modular periods and ordinary p-adic L-functions',
     r'''Explicitly an account of Yu. I. Manin's lectures, this record resumes integration and then builds measures from Hecke-eigenform periods. It culminates in a primitive-character interpolation formula. The source omits the Hecke weights, writes a wrong automorphy factor, leaves a residue class ambiguous, and combines an odd real-period component with even characters. The published 1973 paper identifies the construction, but the notebook's final prefactor cannot be preserved without choosing period, Gauss-sum and measure conventions.''')
item(299,'P000498','definition','Vector-valued distributions and clopen sets',
     r'''\(\mu(U)\in W\) for finite-dimensional \(W/\mathbb Q_p\); \(\mu(U_1\cup U_2)=\mu(U_1)+\mu(U_2)\); \(A_n=p^n\mathbb Z_p\) is called a basis.''',
     r'''For a finite-dimensional p-adic vector space W, a distribution is additive on disjoint compact open subsets of \(\mathbb Z_p\). The cosets \(a+p^n\mathbb Z_p\), not just the subgroups at zero, form its clopen basis. For all of \(\mathbb Q_p\), allow integer n and centers in \(\mathbb Q_p\). Overlapping sets require the inclusion--exclusion term.''',
     r'''This repeats the standard framework of record 298; compare \citet[\S8.4]{manin1973periods}.''',
     ['manin1973periods'],literal='false as written',status='Established after adding disjointness and translating the neighbourhood basis.')
item(299,'P000498','method','The missing measure in the Riemann sum',
     r'''\(S(R_m)=\sum f(a)(a+A_m)\); boundedness and local constancy are offered as sufficient conditions.''',
     r'''The scalar-vector product is \(S(R_m)=\sum f(a)\mu(a+A_m)\in W\). If f is locally constant the sums stabilize for every finitely additive distribution, without a boundedness assumption. If the distribution is bounded, every continuous f can be integrated by uniform approximation.''',
     r'''This is the integration formalism of \citet[\S8.5--8.6]{manin1973periods}; the notes give a sufficient but unnecessarily restrictive condition.''',
     ['manin1973periods'],literal='false as written',status='Established; the absent mu is a visible omission in the manuscript itself.')
item(299,'P000498','construction','Repeated floor-function measure',
     r'''The formula \(\mu_c(a+A_n)=\lfloor ca/p^n\rfloor-(c-1)/2\) is repeated and finite additivity assigned as a useful exercise.''',
     r'''For positive integer c prime to p and canonical \(0\le a<p^n\), the construction and boundedness are exactly those of 1972-298.3. The same floor-sum permutation proves compatibility with refinement.''',
     r'''This repeats \citet[\S8.4, Example 2]{manin1973periods}. It is indexed as a new occurrence, not a new theorem or a separate research problem.''',
     ['manin1973periods'],status='Established; linked to the previous occurrence and its exact computation.')
item(299,'P000498','construction','Analytic characters and the prime two',
     r'''\(\chi_t(a)=e^{t\log a}\), with \(a\equiv1\pmod p\) and \(t\in\mathbb Z_p\).''',
     r'''For odd p this formula defines a character on \(1+p\mathbb Z_p\); at p=2 the displayed exponential formula is safely valid on \(1+4\mathbb Z_2\). A character of \(\mathbb Z_p^\times\) also requires its finite torsion component. The analytic family indexed by t in \(\mathbb Z_p\) does not exhaust finite-order wild characters with values in extensions of \(\mathbb Q_p\).''',
     r'''The full character parametrization is in \citet[\S8.1--8.3]{manin1973periods}.''',
     ['manin1973periods'],status='Established local analytic family, with the p=2 domain and finite character components restored.')
item(299,'P000498','definition','Holomorphic cusp forms and the automorphy factor',
     r'''\(\varphi(z)=\sum_{n\ge1}\lambda_ne^{2\pi inz}\), but \(\varphi(gz)=(az+c)^{-w}\varphi(z)\).''',
     r'''A holomorphic level-one cusp form f of integral weight w satisfies \(f((az+b)/(cz+d))=(cz+d)^w f(z)\) for every matrix in \(\mathrm{SL}_2(\mathbb Z)\), is holomorphic on the upper half-plane, and has zero constant Fourier coefficient at the cusp. Nonzero level-one forms have even weight; the first cusp-form weight is 12. The notes' negative exponent would belong to a differently defined slash action, and az+c is not its denominator.''',
     r'''The convention is fixed in \citet[\S1.1]{manin1973periods}; the modular-form theory itself long predates the lecture.''',
     ['manin1973periods'],literal='false as written',status='Established definition; both the matrix entries and the exponent require correction.')
item(299,'P000499','construction','Hecke operators and the eigenvalue normalization',
     r'''\(T_m f=\sum_{ad=m,\,0\le b<d}f((az+b)/d)\), followed by \(T_m f=\lambda_mf\) when \(\lambda_1=1\).''',
     r'''For weight w and the Fourier normalization \(a_1=1\), use
     \[T_m f(z)=m^{w-1}\sum_{\substack{ad=m\\a,d>0}}d^{-w}\sum_{b=0}^{d-1}f((az+b)/d).\]
     A simultaneous normalized eigenform has eigenvalue \(a_m\). In particular \(T_pf=p^{w-1}f(pz)+p^{-1}\sum_bf((z+b)/p)\). The unweighted sum written in the notebook is generally not this modular operator.''',
     r'''Compare the normalization in \citet[\S3, equation (11)]{manin1973periods}; this is standard Hecke theory.''',
     ['manin1973periods'],literal='false as written',status='Established with the weights restored. The normalization determines the quadratic used below.')
item(299,'P000499','definition','Primitive multiplicative characters',
     r'''For conductor \(p^r\), primitivity is described by nontriviality on \(p^{r-1}\mathbb Z/p^r\mathbb Z\).''',
     r'''A Dirichlet character modulo \(p^r\) is a character of the unit group, extended by zero to nonunits. For r at least 2, conductor exactly \(p^r\) means nontriviality on \(1+p^{r-1}\mathbb Z/p^r\mathbb Z\). For r=1 it means a nontrivial character modulo p. The additive subgroup printed in the notes is not contained in the multiplicative unit group.''',
     r'''Primitivity is used precisely to cancel a lower-level sum in \citet[\S10.2]{manin1973periods}.''',
     ['manin1973periods'],literal='false as written',status='Established definition, with the missing 1+ and the conductor-one exception separated.')
item(299,'P000499','construction','Twisting the cusp form changes its level',
     r'''\(f_\chi(z)=\sum a_n\chi(n)e^{2\pi inz}\) is also modular.''',
     r'''For a level-one cusp form of weight w and a primitive Dirichlet character of conductor q, the twist is a cusp form of weight w on \(\Gamma_0(q^2)\) with nebentypus \(\chi^2\) (its minimal level may be described more sharply). It is not generally a form for the original full modular group.''',
     r'''The twist is the input of \citet[\S10]{manin1973periods}; the passage to an appropriate congruence group is a standard earlier construction.''',
     ['manin1973periods'],status='Established; the unnamed level and character must be part of the statement.')
item(299,'P000499','theorem','The Mellin integral and its constant',
     r'''\(L(f,\chi,s)=C\int_0^{i\infty}f_\chi(z)z^{s-1}dz=\sum a_n\chi(n)n^{-s}\); the constant at s=1 is overwritten.''',
     r'''For a holomorphic cusp form, initially in a right half-plane,
     \[\int_0^\infty f_\chi(iy)y^{s-1}dy=(2\pi)^{-s}\Gamma(s)L(f,\chi,s).\]
     The cusp conditions give the usual continuation of the completed L-function. At s=1, \(L(f,\chi,1)=-2\pi i\int_0^{i\infty}f_\chi(z)dz\). If the contour form uses \(z^{s-1}\), the chosen branch contributes an additional \(i^s\).''',
     r'''The s=1 relation is used in \citet[\S10.2]{manin1973periods}; the Mellin identity is classical.''',
     ['manin1973periods'],status='Established. A constant independent of s cannot describe the general Mellin identity.')
item(299,'P000499','theorem','Algebraic normalized periods',
     r'''After dividing \(\operatorname{Re}\int_0^x f(z)dz\) by a period omega, the values at rational x are algebraic integers in a fixed number field, in many cases.''',
     r'''For a normalized level-one Hecke eigenform with its real Fourier embedding, suitable nonzero even and odd periods normalize the corresponding components of \(I(x)=\int_x^{i\infty}f(z)dz\), x rational, into a fixed number field. After a common scaling the values lie in its ring of integers. The choice of parity and period is part of the theorem; no general assertion of transcendence of every possible period is needed.''',
     r'''This is the algebraicity and integrality input of \citet[Theorem 1.2 and Proposition 9.2(c)]{manin1973periods}. The notebook reports the author's lectures before the paper.''',
     ['manin1973periods'],cls='B',status='Established in this level-one setting. A chosen p-adic place of the coefficient field is needed for the later measure.')
item(299,'P000499','claim','Parity of the real period conflicts with the even character',
     r'''The same passage assumes \(\chi(-1)=1\) but uses \(\ell(x)=\omega^{-1}\operatorname{Re}\int_0^x f(z)dz\).''',
     r'''For real Fourier coefficients, let \(J(x)=\int_0^x f(z)dz\) along a path in the upper half-plane between rational cusps. Then \(J(-x)=-\overline{J(x)}\). Thus its real part is odd and its imaginary part is even. The written real component pairs to zero with every even character on a symmetric residue system. An even-character interpolation must use the even period component, with its matching normalization.''',
     r'''The consistent even/odd separation is in \citet[Proposition 9.2(b), equation (35), and Theorem 10.2]{manin1973periods}.''',
     ['manin1973periods'],literal='false as written',development='annotated',
     reconstruction=r'''\ours\ Change variables \(z\mapsto-\bar z\) in the path integral and use \(f(-\bar z)=\overline{f(z)}\); the differential supplies the minus sign. Pairing a and -a independently checks the forced cancellation. The scan visibly has Re and an even character.''',
     status='A genuine parity error in the literal formula. Choosing the correct component repairs the established construction.')
item(299,'P000499','construction','The ordinary unit root',
     r'''\(T^2-\lambda_pT+p^{w-1}=0\), roots \(\pi,\bar\pi\), with \(\lambda_p\not\equiv0\pmod p\).''',
     r'''Fix a p-adic embedding of the eigenvalue field, with valuation ring \(\mathcal O_K\), and assume \(a_p\in\mathcal O_K^\times\). For w at least 2 the polynomial has a unique unit root alpha by Hensel lifting of its simple nonzero residue root; the other root is \(\beta=p^{w-1}/\alpha\) and has valuation w-1 when \(v(p)=1\). The bar does not mean complex conjugation in this p-adic argument.''',
     r'''This is the ordinary specialization of the root condition in \citet[\S9.5]{manin1973periods}.''',
     ['manin1973periods'],status='Established. Ordinarity is a condition at the selected place, not an unqualified complex inequality.')
item(299,'P000499','construction','A corrected ordinary measure from periodic Hecke periods',
     r'''A limit of sums of \(\ell(b/p^m)\), divided by \(\pi^m+\bar\pi^m\), is given; the congruence after b is ambiguously 0 or a.''',
     r'''A precise published replacement uses a periodic integral-valued normalized period P with
     \[\sum_{j=0}^{p-1}P((x+j)/p)=a_pP(x)-p^{w-2}P(px).\]
     For the unit root alpha, define for m at least 1
     \[\mu_\alpha(a+p^m\mathbb Z_p)=\alpha^{-m}P(a/p^m)-p^{w-2}\alpha^{-m-1}P(a/p^{m-1}).\]
     This is bounded and compatible with refinement; define its total mass by summing level-one values. The explicit two-term formula avoids an unverified identification of the notebook's averaging normalization.''',
     r'''The construction is \citet[Lemma 9.4 and equation (39)]{manin1973periods}, with his weight w+2 renamed w here. The lemma is credited there to Nasybullin as improving the original construction.''',
     ['manin1973periods'],cls='B',match='partial',development='annotated',
     reconstruction=r'''The two-term replacement, period choice and weight conversion are explicit editorial reconstruction. \ours\ Summing children produces the coefficient \(\alpha^{-m-1}(a_p-p^{w-1}/\alpha)=\alpha^{-m}\) on \(P(a/p^m)\); periodicity gives the other term. Unit alpha and integral P give boundedness. A separate derivation and exact rational coefficient check confirm the identity.''',
     status='The ordinary measure is established. The ambiguous residue must depend on a, but the exact displayed averaging convention was not matched.')
interp_id=item(299,'P000499','question','Interpolation of primitive-character L-values',
     r'''The circled question asks for \(\int\chi\,d\mu\) as a multiple of \(L(f,\chi,1)\); the final line supplies a power of pi, \(p^r\), omega and a Gauss sum.''',
     r'''Let \(\chi\) be a nontrivial primitive even character of conductor \(q=p^r\), with its values embedded in a finite p-adic extension. Use the preceding measure for the even component
     \(P(x)=(I(x)+I(-x))/(2\Omega_+)\), \(I(x)=\int_x^{i\infty}f(z)dz\), normalized algebraically. Then
     \[\int_{\mathbb Z_p^\times}\chi^{-1}\,d\mu_\alpha=\alpha^{-r}\sum_{a\bmod q}\chi^{-1}(a)P(a/q).\]
     With \(\tau(\chi^{-1})=\sum_a\chi^{-1}(a)e^{2\pi ia/q}\), the sum is the algebraic value represented over the complex numbers by \(i\tau(\chi^{-1})L(f,\chi,1)/(2\pi\Omega_+)\). The complex expression is transported p-adically through its algebraic normalization, not by embedding arbitrary complex periods.''',
     r'''The precise interpolation theorem is \citet[Theorem 10.2]{manin1973periods}. The displayed notebook constant is not certified because its period parity, root exponent and Gauss-sum convention are not consistently specified.''',
     ['manin1973periods'],cls='B',match='partial',problem='GP-1972-403',development='annotated',
     reconstruction=r'''\ours\ Primitivity cancels the lower-level term in the two-term measure. The finite Gauss identity \(\sum_a\chi^{-1}(a)e^{2\pi ina/q}=\tau(\chi^{-1})\chi(n)\), followed by the Mellin integral, gives the stated prefactor. Independent derivations check both cancellation and parity; no new interpolation theorem is claimed.''',
     status='Resolved by the 1973 construction under the precise ordinary and period hypotheses; this is the definite question tracked in the problem index.')
PROBLEMS.append(dict(id='GP-1972-403',title='Ordinary p-adic interpolation of modular L-values',statement=ITEMS[-1]['statement'],occurrences=[interp_id],status=ITEMS[-1]['present_status'],status_date='2026-11',refs=ITEMS[-1]['refs']))
for page,place,reads,should,evidence,typ in [
 ('P000498','Finite additivity','Additivity for U1 union U2 without qualification.','Require disjointness, or subtract the intersection term.','No disjointness sign appears in the scan.','faithful_error'),
 ('P000498','Riemann sum',r'\(f(a)(a+A_m)\)',r'\(f(a)\mu(a+A_m)\)','The scan itself lacks mu; a scalar times a set is not the claimed W-valued sum.','faithful_error'),
 ('P000498','Analytic character at p=2',r'\(a\equiv1\pmod p\), all primes.',r'For the displayed exponential at p=2 use \(a\in1+4\mathbb Z_2\).','The exponential convergence radius differs at two.','faithful_error'),
 ('P000498','Automorphy factor',r'\((az+c)^{-w}\)',r'\((cz+d)^w\) for the stated transformation convention.','The scan clearly has az+c and a negative exponent.','faithful_error'),
 ('P000499','Hecke operator', 'Unweighted sum of f((az+b)/d).',r'Insert \(m^{w-1}d^{-w}\), with positive a,d and ad=m.','The source contains no determinant or weight factors; the eigenvalue and root formulas fix the standard normalization.','faithful_error'),
 ('P000499','Primitive character kernel',r'\(p^{r-1}\mathbb Z/p^r\mathbb Z\)',r'\(1+p^{r-1}\mathbb Z/p^r\mathbb Z\) for r at least 2.','The missing 1+ is decisive: the written set is additive and contains nonunits.','faithful_error'),
 ('P000499','Period component versus parity','Re of the path integral, with chi(-1)=1.','Use the even imaginary period component, or instead change to the odd-character branch.','Both Re and the even parity are visible. Complex conjugation of the path proves the mismatch.','faithful_error'),
 ('P000499','Residue in averaging formula',r'\(b\equiv0\pmod{p^n}\) (possibly a).',r'A measure of \(a+p^n\mathbb Z_p\) must sum \(b\equiv a\pmod{p^n}\); retain 0/a as a palaeographic ambiguity.','The sign is overwritten. A formula independent of a cannot give the intended varying coset distribution.','ambiguity'),
 ('P000499','Final interpolation constant',r'Notebook prefactor with \(\pi^{r-1}\), \(p^r\), omega and \(g(\chi)\).','Do not certify this constant without fixing the measure scale, period component and Gauss-sum convention.','The preceding parity error and ambiguous normalization prevent an exact literal match; the chapter supplies one consistent convention.','ambiguity')]:
    correction(page,place,reads,should,evidence,typ=typ)
save()

talk(300,'1973-04-09','I. M. Gelfand','P000500',
     'Power sums, Bernoulli coefficients and Hurwitz’s lemniscatic analogue',
     r'''Gelfand derives the power-sum coefficients from a triangular system of Taylor identities, then tests it on an exponential to obtain a generating function. A brief proposal about arbitrary fields is not precise enough to identify an additional problem. The page ends with a correctable reference to Hurwitz's 1899 paper on lemniscatic coefficients, linking the arithmetic examples to an elliptic analogue.''')
item(300,'P000500','theorem','Power sums and Bernoulli polynomials',
     r'''\(1^k+\cdots+n^k=P_{k+1}(n)\), called a Bernoulli polynomial.''',
     r'''For each integer k at least zero, the power sum is a rational polynomial of degree k+1:
     \[\sum_{j=1}^n j^k=\frac{B_{k+1}(n+1)-B_{k+1}(1)}{k+1}.\]
     Here \(te^{xt}/(e^t-1)=\sum_{r\ge0}B_r(x)t^r/r!\). The sum polynomial is a difference of Bernoulli-polynomial values, not literally the standard polynomial \(B_{k+1}(n)\).''',
     r'''Classical; the generating conventions are checked in \citet[\S24.2]{nist2026dlmf}.''',
     ['nist2026dlmf'],status='Established. The k=0 endpoint is included by using B(1), avoiding the B1(0)/B1(1) convention trap.')
item(300,'P000500','method','Telescoping Taylor identities',
     r'''For \(F'=f\), sum \(F(j+1)-F(j)=f(j)+f'(j)/2!+\cdots\).''',
     r'''For a polynomial f of degree d, Taylor expansion is finite and exact, giving
     \[F(n+1)-F(1)=\sum_{r=0}^{d}\frac{1}{(r+1)!}\sum_{j=1}^n f^{(r)}(j).\]
     For nonpolynomial analytic f, convergence on each interval must be justified. For merely smooth f, a finite Euler--Maclaurin formula needs its remainder; the infinite expression is not automatically an equality.''',
     r'''The finite identity is elementary; \citet[\S2.10]{nist2026dlmf} gives the rigorous summation formula with remainder.''',
     ['nist2026dlmf'],status='Established in the polynomial setting; regularity alone does not justify an infinite derivative expansion.')
item(300,'P000500','construction','The determinant is finite after polynomial truncation',
     r'''The sums \(S_n,S'_n,\ldots\) are treated as unknowns in a triangular system; an open-ended determinant solves for \(S_n\).''',
     r'''For degree-d f, retain the d+1 unknowns \(\sum_j f^{(r)}(j)\), 0 at most r at most d. The coefficient matrix is upper triangular with diagonal 1. Cramer's rule gives exactly the displayed finite determinant with its first column replaced by endpoint differences. An infinite determinant requires an additional operator or convergence definition absent from the notes.''',
     r'''This is a finite-dimensional derivation of the Bernoulli summation coefficients, consistent with \citet[\S24.2]{nist2026dlmf}.''',
     ['nist2026dlmf'],development='annotated',
     reconstruction=r'''\oursComputed\ Exact rational linear algebra and direct power sums were independently compared for degrees 0 through 12 and several endpoints; all identities agree. This finite verification supports the implementation, while triangularity proves the formula for every degree.''',
     status='Established finite algebra; the source does not define a general infinite determinant.')
item(300,'P000500','definition','The coefficients called B in the notebook include factorials',
     r'''Expanding along the first column gives coefficients \(B_0,B_1,B_2,\ldots\) multiplying successive endpoint derivatives.''',
     r'''If the endpoint differences are left unscaled as on the page, the coefficient of the r-th entry is \(b_r=B_r/r!\), where \(B_r\) is the standard Bernoulli number with \(B_1=-1/2\). Thus \(b_0=1,b_1=-1/2,b_2=1/12,b_4=-1/720\). Using standard B2=1/6 directly in that determinant expansion would be wrong.''',
     r'''The convention follows from \citet[\S24.2]{nist2026dlmf} and the generating identity in the next item.''',
     ['nist2026dlmf'],status='Established after distinguishing normalized coefficients from standard Bernoulli numbers.')
item(300,'P000500','construction','The exponential test and the generating function',
     r'''Set \(f(x)=e^{tx}\), use \(S_n=(e^{t(n+1)}-e^t)/(e^t-1)\), and expand in t.''',
     r'''The finite geometric sum has a removable singularity at t=0. Comparing the endpoint-derivative expansion gives
     \[\sum_{r\ge0}b_rt^r=\frac{t}{e^t-1}.\]
     This is an identity of formal power series over \(\mathbb Q\), or an analytic Taylor series for \(|t|<2\pi\). Its coefficients yield both the Bernoulli recurrence and the power-sum identities.''',
     r'''Classical generating function; see \citet[\S24.2]{nist2026dlmf}.''',
     ['nist2026dlmf'],status='Established. Formal coefficients and analytic convergence are separate valid readings.')
item(300,'P000500','remark','Bernoulli numbers in arbitrary fields',
     r'''Only the sentence \ru{Числа Бернулли в произвольных полях} is recorded.''',
     r'''No construction, range of indices, characteristic restriction, divided-power convention or desired property is supplied. Over characteristic zero the rational coefficients can be transported through the prime field. In positive characteristic the factorials and Bernoulli denominators obstruct an unrestricted reduction of the same generating series.''',
     r'''The classical rational generating series does not identify which extension the speaker intended. The adjacent Hurwitz reference concerns a specific elliptic analogue and does not by itself resolve this arbitrary-field phrase.''',
     ['nist2026dlmf','hurwitz1899lemniscatic'],cls='F',literal='not determinable',match='thematic only',verification='unresolved lead',confidence='low',
     status='Programme not identifiable as a precise problem; no new open question is manufactured.')
item(300,'P000500','remark','Hurwitz’s lemniscatic analogue',
     r'''The page first cites Math. Z., 1898, then corrects itself to Hurwitz, Math. Ann., 1899, pp. 196--226, on lemniscatic coefficients.''',
     r'''The identifiable work is Hurwitz's study of the expansion coefficients of lemniscatic elliptic functions and the corresponding Gaussian-lattice analogues of Bernoulli arithmetic. This is a specific characteristic-zero elliptic theory, not a theorem asserting a universal Bernoulli construction over arbitrary fields.''',
     r'''\citet{hurwitz1899lemniscatic} appeared in Mathematische Annalen 51 (1899), pp.~196--226. The publisher's collected-works entry explicitly records these original details; its preview identifies the Gaussian-lattice setting. The full original proof was not read.''',
     ['hurwitz1899lemniscatic'],verification='publisher metadata checked',status='Identified older reference. The initial journal/year on the page is a faithful bibliographic error corrected later on the same page.')
correction('P000500','Bernoulli coefficient convention',r'\(B_r\) multiplying the raw r-th endpoint derivative.',r'These coefficients are standard \(B_r/r!\).',
           'The determinant expansion and exponential test fix b2=1/12. This is a notation clarification, not evidence of a missing factorial in the transcription.',typ='ambiguity')
correction('P000500','Hurwitz reference','Math. Z., 1898.', 'Mathematische Annalen 51 (1899), 196--226.',
           'The notebook supplies the correct citation lower down; the publisher collected-works metadata confirms it.')
correction('P000480','Pre-indexed Dobrushin record between requested records 287 and 289',
           'The supplied page range includes the 19 February 1973 discussion, but the requested 28-record list omits record 288.',
           'Retain its existing occurrences 1972-288.1 through 1972-288.5 from the supplied previous index; do not create duplicate occurrences or silently assign this page to another speaker.',
           r'The dated manuscript page and the supplied previous index identify the same material. This is an ownership discrepancy in the supplied year partition, not missing new mathematical coverage.',typ='provenance')
correction('P000495-P000497','Order of the three 26 March records',
           'Catalogue order: 296, 297, 298.',
           'Manuscript order: 296 (spectral asymmetry), 298 (p-adic integration), 297 (Gabrielov opening fragment).',
           'The arithmetic continuation occupies the upper part of P000497, before the Gabrielov heading. The chapter follows the manuscript while retaining catalogue record identifiers.',typ='provenance')
save()

if __name__ == '__main__':
    print(f'Root batch: {len(TALKS)} records, {len(ITEMS)} items, {len(PROBLEMS)} problems, {len(CORRECTIONS)} corrections')
