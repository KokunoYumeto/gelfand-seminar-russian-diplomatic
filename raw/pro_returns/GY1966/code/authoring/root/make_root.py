"""Authoring source for records 92--104 of the GY1966 critical companion.

All mathematical prose is editorially authored from the supplied notebook and
the checked sources in references.bib. Running this file deterministically
recreates the structured root contribution; it makes no network requests.
"""
from pathlib import Path
import json, csv

BASE = Path(__file__).resolve().parent
talks, items, problems, corrections = [], [], [], []

def talk(record, date, speaker, pages, title, summary, kind='talk'):
    talks.append(dict(record=record, date=date, speaker=speaker, pages=pages,
                      title=title, kind=kind, summary=summary))

def item(record, pages, kind, title, notes, statement, cls, fate, status,
         refs=(), reconstruction='', literal='correct with missing hypotheses',
         match='exact', verification='read the result', development='none',
         problem='', worth='', confidence='high', speaker=None):
    n = 1 + sum(x['record'] == record for x in items)
    d = dict(id=f'1966-{record}.{n}', record=record, pages=pages, kind=kind,
             title=title, notes=notes, statement=statement,
             reconstruction=reconstruction, **{'class':cls}, fate=fate,
             present_status='As of 9 November 2026: '+status,
             literal_correctness=literal, publication_match=match,
             verification=verification, development=development, problem=problem,
             worth=worth, refs=list(refs), confidence=confidence)
    if speaker: d['speaker']=speaker
    items.append(d)
    return d['id']

def prob(pid, title, statement, occurrences, status, refs=()):
    problems.append(dict(id=pid,title=title,statement=statement,
                         occurrences=occurrences,status=status,
                         status_date='2026-11',refs=list(refs)))

def corr(page, place, before, after, evidence, applies='both', typ='faithful_error'):
    corrections.append(dict(page=page,place=place,transcription_reads=before,
                           should_read=after,evidence=evidence,applies_to=applies,type=typ))

def save():
    for name, data in [('talks',talks),('items',items),('problems',problems)]:
        (BASE/f'{name}.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    with (BASE/'corrections.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=['page','place','transcription_reads','should_read','evidence','applies_to','type'])
        w.writeheader();w.writerows(corrections)

talk(92,'1966-09-05','I. M. Gelfand','P000140-P000142',
     'Programme; Brieskorn links and exotic spheres',
     r'The actual opening heading and programme occupy P000140: statistical mechanics, pseudodifferential operators, algebraic groups, and deformations. A report attributed to Hirzebruch then describes exotic spheres as links of isolated hypersurface singularities. The catalogue range overlaps subsequent talks; items below follow the handwritten headings. The printed exponent requires an emendation, not merely removal of an uncertainty marker.')
item(92,'P000140','construction','A seven-dimensional hypersurface link',
     r'The notebook intersects \(z_1^3+z_2^{3k-1}+z_3^2+z_4^2+z_5^2=0\) with \(\sum|z_i|^2=\epsilon\), and counts \(10-3=7\) real dimensions.',
     r'For integers \(k\geq1\), the corrected Brieskorn link \(\Sigma(3,6k-1,2,2,2)\subset\mathbb C^5\), cut out on a sufficiently small positive sphere, is a smooth closed real seven-manifold and a homotopy sphere. The written exponent \(3k-1\) does not give homology spheres for every \(k\).',
     'E',r'Brieskorn published the construction in 1966; Hirzebruch explained its sphere criterion in his November 1966 expos\'e, printed in 1968 \citep[\S\S2--3]{brieskorn1966beispiele,hirzebruch1968singularities}.',
     r'established. The notebook is an early report of an existing construction, with a substantive exponent error.',
     ['brieskorn1966beispiele','hirzebruch1968singularities'],
     reconstruction=r'\(6k-1\) is our mathematical emendation. In the exponent graph for \((3,3k-1,2,2,2)\), odd \(k\) leaves an even component of four vertices, which fails the homology-sphere criterion. Even \(k=2\ell\) gives the standard family with parameter \(\ell\).',
     literal='false as written',development='annotated')
item(92,'P000140','theorem','Twenty-eight oriented seven-sphere classes',
     r'As \(k\) varies, all 28 “Milnor spheres” are said to occur.',
     r'The group of oriented smooth homotopy seven-spheres is \(\Theta_7=bP_8\cong\mathbb Z/28\). With the corrected exponent, 28 consecutive parameters represent its 28 oriented diffeomorphism classes, including the standard sphere.',
     'E',r'The signature computation and the enumeration are given in \citet[\S3]{hirzebruch1968singularities}, reporting the 1966 construction.',
     r'established; 28 counts all classes, not 28 exotic classes.',
     ['hirzebruch1968singularities'],reconstruction=r'The orientation convention and inclusion of the standard sphere are supplied explicitly.',literal='correct with missing hypotheses')
item(92,'P000140','theorem','The analogous eleven-dimensional enumeration',
     r'The report adds that the same method produces 992 spheres in dimension 11.',
     r'Adding two quadratic variables gives \(\Sigma(3,6k-1,2,2,2,2,2)\), a homotopy eleven-sphere. Its classes exhaust \(\Theta_{11}=bP_{12}\cong\mathbb Z/992\), with orientations retained.',
     'E',r'\citet[\S3]{hirzebruch1968singularities} gives the corresponding higher-dimensional signature calculation and the order 992.',
     r'established. This numerical claim survives correction of the preceding family.',
     ['hirzebruch1968singularities'],reconstruction=r'The explicit seven-variable polynomial is reconstructed from the phrase “the same method.”',literal='correct')
corr('P000140','Hypersurface exponent',r'\(3k-1\) (provisional)',r'Retain \(3k-1\) diplomatically; annotate the intended \(6k-1\).',r'The circled exponent in the scan begins with 3. The Brieskorn graph criterion rules out odd \(k\) for the written family; the published family has \(6k-1\).')
save()

# Remaining records are appended below; source order is restored in the final save.

talk(93,'1966-09-05','D. A. Kazhdan','P000140-P000143',
     'Bass rigidity and an integral cohomology reduction',
     r'P000141--P000142 report Bass’s work on rigidity of \(\mathrm{SL}_n(\mathbb Z)\), relating deformations to first cohomology and proposing reduction modulo a prime. This resumes the cohomological rigidity and congruence-subgroup discussions indexed at 1964-8.1--2 and 1964-24.1--2. The established conclusion and the incompletely recorded proof reduction must be distinguished.')
item(93,'P000141','theorem','Local rigidity of the standard higher-rank lattice',
     r'For \(n>2\), a continuous family of homomorphisms \(\varphi_t:\mathrm{SL}_n(\mathbb Z)\to\mathrm{SL}_n(\mathbb R)\) starting with inclusion has the form \(g(t)\gamma g(t)^{-1}\).',
     r'For \(n\geq3\), the standard inclusion is locally rigid: all homomorphisms sufficiently close on a finite generating set are conjugate to it. A continuous parameter path starting at inclusion is locally conjugate; a path of conjugators can be chosen on an interval by lifting through the conjugation orbit.',
     'B',r'\citet[\S16, Corollaries 16.4--16.5 and the following remark]{bassmilnorserre1967congruence} give the cohomological rigidity consequences; publication was in 1967 by Bass, Milnor and Serre, whose work Kazhdan is reporting.',
     r'established. This is local deformation rigidity, not the assertion that arbitrary homomorphisms belong to one component.',
     ['bassmilnorserre1967congruence'],reconstruction=r'Closeness on generators and the local-to-path interpretation are made explicit.')
item(93,'P000141','method','The first-cohomology criterion',
     r'The derivative of a deformation is a 1-cocycle with values in the adjoint module; conjugation produces a coboundary. Vanishing \(H^1\) is used to prove rigidity.',
     r'For a finitely generated group \(\Gamma\), Lie group \(G\), and homomorphism \(\rho\), a differentiable path has infinitesimal class in \(H^1(\Gamma,\mathfrak g_{\operatorname{Ad}\rho})\). If that group vanishes, Weil’s local rigidity criterion applies. Nonzero cohomology alone need not integrate to a nontrivial deformation.',
     'E',r'The criterion predates this talk and is explicitly used in \citet[\S16, remark on rigidity]{bassmilnorserre1967congruence}; it recurs from 1964-8.2.',
     r'established; the obstruction to integrating arbitrary cocycles must not be omitted.',
     ['bassmilnorserre1967congruence'],match='partial',reconstruction=r'The warning about nonintegrable cocycles is an editorial clarification.')
item(93,'P000141','method','Passing from an integral adjoint lattice to real coefficients',
     r'The notes choose \(L=\mathfrak{sl}_n(\mathbb Z)\) and identify real first cohomology with its integral counterpart tensored with \(\mathbb R\).',
     r'For a finitely presented \(\Gamma\) and a finite-rank free integral \(\Gamma\)-module \(L\), \(H^1(\Gamma,L)\otimes\mathbb R\cong H^1(\Gamma,L\otimes\mathbb R)\). Thus finiteness of the integral group proves real vanishing.',
     'E',r'The integral conclusion appears in \citet[Corollary 16.5]{bassmilnorserre1967congruence}; the change-of-scalars step is elementary homological algebra.',
     r'correct with finiteness hypotheses. No assertion about all degrees or arbitrary coefficient modules is intended.',
     ['bassmilnorserre1967congruence'],reconstruction=r'Finite presentation makes the cocycle relations a finite matrix calculation and justifies tensoring their kernels with the flat module \(\mathbb R\).',match='partial')
item(93,'P000141-P000142','method','Reduction modulo a prime and the missing restriction term',
     r'The proof attempts to make multiplication by \(p\) surjective on \(H^1(\Gamma,L)\), then reduces to a finite quotient and to \(H^1(\Gamma/\Gamma_p,L/pL)=0\).',
     r'From \(0\to L\xrightarrow{p}L\to L/pL\to0\), vanishing \(H^1(\Gamma,L/pL)\) implies \(p\)-surjectivity. For finitely generated abelian \(H^1(\Gamma,L)\), this excludes a free summand. But inflation--restriction also has \(H^1(\Gamma_p,L/pL)^{\Gamma/\Gamma_p}\); vanishing on the quotient does not alone remove that term.',
     'B',r'The final finiteness theorem matches \citet[Corollary 16.5]{bassmilnorserre1967congruence}, by the authors whose work is being reported; the exact prime-reduction proof in these notes was not matched to a complete published argument.',
     r'the conclusion is established; the recorded proof remains incomplete, rather than an independent open theorem.',
     ['bassmilnorserre1967congruence'],reconstruction=r'Our reconstruction supplies the exact-sequence obstruction and deliberately does not infer the missing vanishing.',match='partial',development='annotated',confidence='medium')
corr('P000142','Cohomology reduction',r'Vanishing on \(\Gamma/\Gamma_p\) finishes the proof.',r'Add control of \(H^1(\Gamma_p,L/pL)^{\Gamma/\Gamma_p}\).',r'The displayed finite quotient does not by itself exhaust the inflation--restriction sequence; this is a missing proof step, not a changed glyph.')
save()

talk(94,'1966-09-05','V. I. Arnold','P000141-P000147',
     'Anosov systems, structural stability, and Smale questions',
     r'The handwritten Arnold heading is on P000142; his discussion ends on P000145. Uniform hyperbolicity, an arithmetic nilmanifold, Morse--Smale systems, Axiom A, and spectral decomposition are interspersed with explicit conjectures. Positive and negative later answers belong to different questions; in particular hyperbolicity of the nonwandering set alone does not force dense periodic points.')
item(94,'P000142','definition','A U-system is uniformly hyperbolic on the whole manifold',
     r'The tangent bundle splits into \(X\oplus Y\), with one part contracted and the other expanded; such an automorphism is a \(U\)-system.',
     r'A \(C^1\) diffeomorphism \(f\) of a closed smooth manifold is Anosov if \(TM=E^s\oplus E^u\) is a continuous invariant splitting and \(\|Df^nv^s\|,\|Df^{-n}v^u\|\leq C\lambda^n\|v^{s,u}\|\) for \(n\geq0\), \(C<\infty\), \(0<\lambda<1\).',
     'E',r'This is the established Anosov notion reviewed in \citet[\S\S1--2]{smale1967dynamical}; the survey followed the 1966 Moscow congress.',
     r'standard. Continuity, invariance and uniform constants are essential.',
     ['smale1967dynamical'],reconstruction=r'The modern constants and bundle regularity explicate the shorthand.')
item(94,'P000142','construction','Hyperbolic toral automorphisms',
     r'A linear torus automorphism with no unit-modulus eigenvalues is the first example.',
     r'If \(A\in\mathrm{GL}(d,\mathbb Z)\) has no eigenvalue of modulus one, \(x+\mathbb Z^d\mapsto Ax+\mathbb Z^d\) is Anosov. Its stable and unstable bundles descend from the generalized eigenspaces.',
     'E',r'The example is included in \citet[\S1]{smale1967dynamical}, and was already discussed in the earlier index at 1964-33.4.',
     r'established and explicit.', ['smale1967dynamical'],literal='correct')
item(94,'P000142-P000143','construction','An arithmetic six-dimensional nilmanifold example',
     r'Two real upper-unitriangular three-by-three groups are combined using the two embeddings of \(\mathbb Z[\sqrt3]\); the quotient is compact. No actual automorphism formula is retained.',
     r'Let \(H\) have coordinates \((a,b,c)\) and law \((a,b,c)(a_2,b_2,c_2)=(a+a_2,b+b_2+ac_2,c+c_2)\). Embed \(H(\mathbb Z[\sqrt3])\) diagonally in \(H(\mathbb R)^2\) by conjugate embeddings. This is a uniform lattice. Multiplication of \(a,c\) by \(u=2+\sqrt3\) and of \(b\) by \(u^2\), with the conjugate action in the second factor, descends to an Anosov automorphism.',
     'E',r'The nilmanifold family is part of the algebraic examples reviewed by \citet[\S1]{smale1967dynamical}; the formula supplied here is a compatible reconstruction, not a claimed verbatim match.',
     r'established construction; the scan determines the lattice more clearly than the missing map.',
     ['smale1967dynamical'],reconstruction=r'\ours\ The chosen map respects the cross-term because \((ua)(uc_2)=u^2ac_2\), preserves the integral lattice since \(u\) is a unit, and has eigenvalues \(u,u,u^2,u^{-1},u^{-1},u^{-2}\). Compactness follows by reduction in the two-dimensional Minkowski lattice successively in \(a,c,b\).',match='partial',development='annotated')
item(94,'P000143','conjecture','Are all Anosov examples algebraic?',
     r'After the nilmanifold construction the notes suggest that all such systems may be of this kind.',
     r'A precise modern version asks whether every Anosov diffeomorphism of a closed connected manifold is topologically conjugate to an affine Anosov automorphism of an infranilmanifold. The weaker manifold question asks only whether the manifold is homeomorphic to an infranilmanifold.',
     'C',r'The strong topological-conjugacy formulation is explicit in \citet[Conjecture 2.3]{spatzier2016rigidity}; \citet[Introduction]{deremainkar2023anosov} retain the weaker manifold question. The latter circulated in 2020, appeared online in 2022, and in print in 2023.',
     r'no general resolution was found in the dated primary-source search. Smooth conjugacy and diffeomorphism to a standard smooth infranilmanifold are stronger, generally invalid replacements.',
     ['smale1967dynamical','spatzier2016rigidity','deremainkar2023anosov','farrellgogolev2012exotic'],reconstruction=r'Topological conjugacy and infranilmanifolds are modern precisifications, not words legible in the notebook.',match='partial',problem='GP-1966-01',worth=r'Further work is worthwhile in a specified algebraic or dimension-restricted class; the unrestricted classification has no plausible bounded proof from these notes.',confidence='medium')
item(94,'P000143-P000144','definition','Structural stability and the choice of equivalence',
     r'Nearby systems should be equivalent, initially described as diffeomorphic and subsequently as related by an \(\epsilon\)-homeomorphism.',
     r'A diffeomorphism is \(C^r\) structurally stable if all sufficiently \(C^r\)-close diffeomorphisms are topologically conjugate. For vector fields use an orbit homeomorphism preserving time orientation, usually allowing reparameterization. A near-identity conjugacy is available in the hyperbolic stability setting.',
     'E',r'\citet[Introduction and \S2]{smale1967dynamical} uses topological equivalence. The same distinction is relevant to 1965-74.1.',
     r'standard; smooth conjugacy would wrongly preserve eigenvalue data under perturbation.',
     ['smale1967dynamical'],reconstruction=r'The precise topology and the flow time-change convention are supplied.',literal='false as written',development='annotated')
item(94,'P000143','theorem','The two-dimensional structural-stability model',
     r'Andronov--Pontryagin theory is cited as the two-dimensional precedent.',
     r'For flows on a closed orientable surface, the classical criterion requires finitely many hyperbolic equilibria and periodic orbits, no saddle connections, and no other nonwandering recurrence. Such fields are structurally stable; the relevant density theorem is a \(C^1\) surface theorem.',
     'E',r'The historical surface theory and Peixoto’s extension are reviewed by \citet[\S2]{smale1967dynamical}.',
     r'established. The notes do not justify transferring the density conclusion to higher dimensions.',
     ['smale1967dynamical'],reconstruction=r'The compact-surface formulation combines the precedent with the standard complete criterion; it is not attributed entirely to the original planar theorem.',match='partial')
item(94,'P000143-P000144','definition','Morse--Smale systems',
     r'Finitely many hyperbolic stationary and periodic trajectories, convergence toward them, and transverse stable/unstable intersections are listed.',
     r'For a smooth flow on a closed manifold, the nonwandering set must be a finite union of hyperbolic equilibria and periodic orbits, and their stable and unstable manifolds must meet transversely. For diffeomorphisms the nonwandering set consists of finitely many hyperbolic periodic points with the same transversality condition.',
     'E',r'The finite-hyperbolic/transverse formulation is the setting of \citet[Theorem 1.2 and \S5]{palissmale1970stability}, circulated in 1968.',
     r'standard; this definition is much narrower than Axiom A.',
     ['palissmale1970stability'],reconstruction=r'The nonwandering-set condition makes the informal convergence clause precise.')
item(94,'P000143','question','Does Morse--Smale imply structural stability?',
     r'The heading says four assertions. Only the first, that Morse--Smale conditions imply stability, is explicitly marked as a question.',
     r'Is every Morse--Smale diffeomorphism or flow on a closed manifold structurally stable in the \(C^1\) topology?',
     'B',r'Yes: \citet[Theorem 1.2; flow version in \S5]{palissmale1970stability}. The paper circulated in 1968, appeared in Russian in 1969, and in the cited proceedings in 1970.',
     r'solved affirmatively.', ['palissmale1970stability'],literal='correct',problem='GP-1966-02')
item(94,'P000143','question','Must a structurally stable system be Morse--Smale?',
     r'The second assertion reverses the implication. The notebook groups assertions 2--4 under \ru{Опровергнуты Смейлом}: refuted by Smale.',
     r'Does structural stability force only finitely many hyperbolic recurrent critical elements?',
     'E',r'The Anosov examples already refute this: see \citet[\S1]{smale1967dynamical}. A hyperbolic toral automorphism is structurally stable and has infinitely many periodic orbits; its suspension gives the flow analogue.',
     r'false in general, with examples available in the theory discussed at the talk.', ['smale1967dynamical'],literal='correct',problem='GP-1966-03')
item(94,'P000143','question','Are Morse--Smale systems dense?',
     r'The third assertion proposes density of Morse--Smale systems; the notebook explicitly includes it among the three assertions refuted by Smale.',
     r'Are Morse--Smale systems dense among all smooth systems on each closed manifold in a specified \(C^r\) topology?',
     'E',r'An open Anosov neighbourhood with infinitely many periodic orbits prevents this general density statement \citep[\S1]{smale1967dynamical}.',
     r'false in general; manifold- and dimension-specific density results do not repair the universal assertion.', ['smale1967dynamical'],literal='correct',problem='GP-1966-04')
item(94,'P000143','question','Are structurally stable systems dense?',
     r'The fourth assertion proposes density of structurally stable systems; the notebook already reports Smale’s refutation.',
     r'Is the set of structurally stable \(C^r\) vector fields dense on every compact smooth manifold?',
     'E',r'\citet[Main theorem]{smale1966nondensity}, received in June 1965 and published in 1966, constructs a compact four-manifold with an open set containing no structurally stable fields.',
     r'false in general. The negative result was already published and reported at this seminar.', ['smale1966nondensity'],literal='correct',problem='GP-1966-05')
item(94,'P000144','definition','A hyperbolic invariant set',
     r'Uniform hyperbolicity is imposed on a closed invariant set, with a point, the whole space, and a Cantor-type set as examples.',
     r'For a diffeomorphism, a compact invariant set \(\Lambda\) is hyperbolic when \(T_\Lambda M\) admits a continuous invariant stable/unstable splitting with uniform exponential estimates. For nonsingular flows add the one-dimensional flow direction. A horseshoe illustrates a proper, totally disconnected hyperbolic set.',
     'E',r'These examples and the invariant-set formulation appear in \citet[\S\S1--2]{smale1967dynamical}.',
     r'standard; the flow-direction summand cannot be omitted from the flow definition.', ['smale1967dynamical'],reconstruction=r'The distinction between maps and flows is supplied.')
item(94,'P000144-P000145','definition','Nonwandering points and Axiom A',
     r'The nonwandering set \(\Omega\) is closed; “Smale systems” satisfy hyperbolicity of \(\Omega\) and density in it of periodic points.',
     r'For a homeomorphism of a compact space, \(x\in\Omega(f)\) if every neighbourhood \(U\) meets \(f^nU\) for some \(n>0\). A \(C^1\) diffeomorphism satisfies Axiom A when \(\Omega(f)\) is hyperbolic and \(\overline{\operatorname{Per}(f)}=\Omega(f)\).',
     'E',r'The two independent clauses are those used by \citet[\S\S2--3]{smale1967dynamical}.',
     r'standard. On a flow, equilibria must also be included among the recurrent critical elements.', ['smale1967dynamical'],reconstruction=r'The modern name Axiom A is used retrospectively.')
item(94,'P000145','remark','Nonwandering does not imply periodic',
     r'The discussion mentions a system with every point nonwandering but no periodic trajectories.',
     r'An irrational rotation \(x\mapsto x+\alpha\) of \(\mathbb R/\mathbb Z\), \(\alpha\notin\mathbb Q\), has \(\Omega=S^1\) and no periodic point. This example is not hyperbolic.',
     'E',r'This elementary distinction is consistent with the separate hypotheses in \citet[\S2]{smale1967dynamical}.',
     r'established counterexample to a claim without hyperbolicity.', ['smale1967dynamical'],reconstruction=r'The irrational rotation is our explicit model for the brief example.',literal='correct',match='partial')
item(94,'P000145','theorem','Generic density of periodic points in the nonwandering set',
     r'A generic periodic-point density theorem is attributed to a difficult-to-read name with a 1964 date.',
     r'For a residual subset of \(\operatorname{Diff}^1(M)\) of a closed smooth manifold, \(\Omega(f)=\overline{\operatorname{Per}(f)}\). The analogous generic flow statement includes equilibria. This is a \(C^1\), not an unrestricted \(C^r\), conclusion.',
     'B',r'\citet[Theorem 6.5 in the Russian version]{pugh1967density}, published in 1967, states the generic flow result; the diffeomorphism formulation above is its standard counterpart. The paper refers to earlier announcements, but the handwritten name/date remains insecure.',
     r'established in \(C^1\). The ambiguous marginal attribution is retained as ambiguous.', ['pugh1967density'],match='partial',confidence='medium')
item(94,'P000145','conjecture','Density of Axiom A systems',
     r'A conjecture asks whether systems satisfying the two Smale conditions are dense.',
     r'Are Axiom A diffeomorphisms \(C^1\)-dense on every closed smooth manifold?',
     'B',r'The general conjecture failed through the robust examples of \citet{abrahamsmale1970nongenericity}; this is a different assertion from Smale’s earlier nondensity of structural stability.',
     r'false in general. Density in restricted classes is a separate question.', ['abrahamsmale1970nongenericity'],literal='correct',problem='GP-1966-06',verification='publisher metadata checked',confidence='medium')
item(94,'P000145','conjecture','Does hyperbolicity of the nonwandering set imply dense periodic points?',
     r'The possibility that condition 1 implies condition 2 is assigned “70\%” confidence.',
     r'If the nonwandering set of a smooth diffeomorphism of a compact manifold is hyperbolic, must periodic points be dense in that set?',
     'B',r'No: \citet[main counterexample]{kurata1979hyperbolic} constructs a hyperbolic nonwandering set without dense periodic points.',
     r'refuted in general. Local maximality and shadowing cannot be silently supplied to the arbitrary nonwandering set.', ['kurata1979hyperbolic'],literal='correct',problem='GP-1966-07')
item(94,'P000145','theorem','Spectral decomposition into basic sets',
     r'The nonwandering set decomposes into finitely many invariant transitive pieces.',
     r'For an Axiom A diffeomorphism on a closed manifold, \(\Omega(f)\) is a disjoint union of finitely many compact invariant topologically transitive basic sets. Periodic density belongs among the hypotheses, even if a preceding speculative implication would have removed it.',
     'B',r'The spectral decomposition theorem is given in \citet[\S3]{smale1967dynamical}, published in 1967. The notebook attests its circulation here in September 1966; an independently checked earlier public-circulation date for this exact statement is not asserted.',
     r'established under Axiom A. The two-clause assumption matters because the preceding conjecture is false.', ['smale1967dynamical'],reconstruction=r'Axiom A is stated explicitly rather than inferred from condition 1.')
for pid,title,stmt,idx,status,refs in [
 ('01','Algebraic classification of Anosov diffeomorphisms',r'Is every Anosov diffeomorphism of a closed manifold topologically conjugate to an affine Anosov map of an infranilmanifold?',4,r'As of November 2026, unresolved in general in the checked literature; see Spatzier’s Conjecture 2.3. The weaker manifold-realization question also remains open. The smooth-category replacement is too strong.',['smale1967dynamical','spatzier2016rigidity','deremainkar2023anosov','farrellgogolev2012exotic']),
 ('02','Structural stability of Morse--Smale systems',r'Are Morse--Smale maps and flows \(C^1\) structurally stable?',8,r'Affirmatively solved; 1968 circulation, 1969 Russian and 1970 English publication.',['palissmale1970stability']),
 ('03','Necessity of Morse--Smale conditions',r'Must structural stability imply the Morse--Smale conditions?',9,r'No; hyperbolic toral automorphisms and their suspension flows provide counterexamples.',['smale1967dynamical']),
 ('04','Density of Morse--Smale systems',r'Are Morse--Smale systems dense on every closed manifold?',10,r'No in general; an open family of Anosov systems supplies an obstruction.',['smale1967dynamical']),
 ('05','Density of structurally stable fields',r'Are structurally stable vector fields dense on every compact manifold?',11,r'No in general, by Smale’s 1966 counterexample, already published at the time of the question.',['smale1966nondensity']),
 ('06','Density of Axiom A',r'Are Axiom A diffeomorphisms \(C^1\)-dense on every closed manifold?',16,r'No in general; Abraham--Smale, 1970.',['abrahamsmale1970nongenericity']),
 ('07','Periodic density from hyperbolic nonwandering set',r'Does hyperbolicity of \(\Omega(f)\) force \(\Omega(f)=\overline{\operatorname{Per}(f)}\)?',17,r'No in general; Kurata, 1979.',['kurata1979hyperbolic'])]:
    prob('GP-1966-'+pid,title,stmt,[f'1966-94.{idx}'],status,refs)
corr('P000143','Equivalence in structural stability',r'Diffeomorphic equivalence',r'Topological conjugacy for maps; topological orbit equivalence for flows.',r'The notebook later explicitly specifies an \(\epsilon\)-homeomorphism on P000144. Smooth equivalence would preserve derivatives at periodic points and is not the intended stable notion.')
corr('P000145','Name and year beside generic density',r'A name interpreted as Goto or Pugh, 1964',r'Keep the name/date uncertain; compare Pugh’s 1967 theorem without rewriting the scan.',r'The scan does not securely resolve the attribution. The later theorem is a mathematical match, not palaeographic proof.',typ='ambiguity')
save()

talk(95,'1966-09-12','G. E. Shilov','P000145-P000148',
     'Regular Hilbert-space functions and a first-order mean operator',
     r'P000146--P000147 introduce a uniform algebra between weak and norm continuity, limiting finite-dimensional spherical means, and a mean-defined differential operator. Linear boundary problems and a fixed-point approach to a semilinear equation follow. Shilov’s 1967 papers closely match this announcement, but the operator is not the usual Hilbert-space trace Laplacian.')
item(95,'P000146','definition','The regular uniform algebra on a Hilbert ball',
     r'For the unit ball \(S\subset H\), \(L(S)\subset\overline R\subset C(S)\), where \(R\) consists of continuous functions of finitely many coordinates and distances \(\|x-a_j\|\).',
     r'Let \(H\) be an infinite-dimensional separable real Hilbert space. In the supremum norm on its closed unit ball, let \(A\) be the uniform closure of the unital algebra generated by the linear coordinates and \(\|x\|^2\). This equals the stated coordinate-and-distance algebra. One has \(C(S_{\rm weak})\subset A\subset C_b(S_{\rm norm})\).',
     'A',r'The regular algebra is defined in \citet[\S1]{shilov1967hilbert1}, received 4 January 1967.',
     r'established. The ambient norm-continuous algebra must be bounded if a uniform Banach-algebra norm is intended.',
     ['shilov1967hilbert1'],reconstruction=r'The identity \(\|x-a\|^2=\|x\|^2-2\langle x,a\rangle+\|a\|^2\) explains the equivalent generators. The subscript \(b\) is an explicit clarification.')
item(95,'P000146','construction','A compactification and its nonevaluation characters',
     r'The maximal-ideal space of \(L(S)\) is the Hilbert ball; that of \(\overline R\) is a compact extension.',
     r'The character space of \(C(S_{\rm weak})\) is the weakly compact ball. For \(A\), an explicit model is \(K=\{(z,s):\|z\|^2\leq s\leq1\}\subset S_{\rm weak}\times[0,1]\), with evaluation points \((x,\|x\|^2)\). Points with \(s>\|z\|^2\) are additional characters.',
     'A',r'\citet[\S1 and the reference to Part II]{shilov1967hilbert1} connects the regular algebra to its maximal ideals. The concrete model here is supplied as a reconstruction.',
     r'the compactification is well defined; it is not the norm ball itself.',
     ['shilov1967hilbert1'],reconstruction=r'\ours\ The set \(K\) is compact because norm squared is weakly lower semicontinuous. The generators extend continuously and separate its points. Evaluation points are dense: use \(x_j=z+\sqrt{s-\|z\|^2}\,e_j\), with orthonormal \(e_j\perp z\). Stone--Weierstrass then identifies \(A\) with \(C(K)\).',match='partial',development='annotated')
item(95,'P000146','theorem','Limiting spherical and ball means coincide',
     r'Finite-dimensional means on spheres and balls have the same infinite-dimensional limit on \(\overline R\).',
     r'For admissible centres \(z\) and radii \(r\), normalized means over increasing finite-dimensional balls or spheres converge for every \(f\in A\), independently of the orthonormal exhaustion. On a generator \(F(\langle e_1,x\rangle,\ldots,\langle e_m,x\rangle,\|x\|^2)\), the limit is \(F(\langle e_1,z\rangle,\ldots,\langle e_m,z\rangle,\|z\|^2+r^2)\).',
     'A',r'The mean construction is in \citet[\S2]{shilov1967hilbert1}.',
     r'established on this algebra; it is not a countably additive uniform measure on an infinite-dimensional sphere.',
     ['shilov1967hilbert1'],reconstruction=r'The displayed formula spells out the finite-coordinate concentration calculation; admissibility means the averaging sets lie in the domain.')
item(95,'P000146','theorem','The mean is multiplicative',
     r'\(M_r\) is a multiplicative functional, usually evaluation only in the compact extension.',
     r'For \(f,g\in A\), \(M_r(fg,z)=M_r(f,z)M_r(g,z)\). For \(r>0\) this is evaluation at \((z,\|z\|^2+r^2)\in K\), not at a Hilbert-space point.',
     'A',r'\citet[\S2]{shilov1967hilbert1} establishes multiplicativity.',
     r'established; finite-dimensional averaging is not multiplicative, and the limiting assertion relies on the restricted regular algebra.',
     ['shilov1967hilbert1'],literal='correct')
item(95,'P000146','definition','The mean-defined first-order derivation',
     r'\(\Delta f(z)=\lim_{r\to0}[M_r(f,z)-f(z)]/r^2\), with the emphatic comment that it is first order and obeys Leibniz’s rule.',
     r'On the domain where this limit exists in the stipulated topology, the mean generator \(L\) is a derivation: \(L(fg)=fLg+gLf\). On smooth regular functions expressed in \((z,s)\), it differentiates in the \(s\)-direction at \(s=\|z\|^2\). In particular \(L\|x\|^2=1\), while it annihilates a smooth finite-coordinate function.',
     'A',r'The operator and its derivation property are in \citet[\S\S2,5]{shilov1967hilbert1}.',
     r'established for its specified function class and closure. It should not be identified with the ordinary sum of second derivatives.',
     ['shilov1967hilbert1'],reconstruction=r'The notation \(L\) avoids confusion with a trace Laplacian. The examples follow directly from the notebook’s normalization.',development='annotated')
item(95,'P000146-P000147','theorem','A regular Dirichlet problem',
     r'For a star-shaped surface \(\sum_{k>m}\xi_k^2=\varphi(\xi_1,\ldots,\xi_m)\) with bounded curvature, the Dirichlet problem has a unique, continuously dependent solution given by an angular mean.',
     r'In Shilov’s regular boundary class, the mean-defined operator has a unique regular harmonic extension of regular continuous boundary data, with continuous dependence in the uniform norm. An unqualified assertion for every weakly closed star-shaped surface is not supported. Even the norm unit sphere is not weakly closed in infinite dimension.',
     'A',r'The linear boundary construction and uniqueness are in \citet[\S\S3,6]{shilov1967hilbert1}.',
     r'established in the published regular-domain framework; the notebook does not retain all the domain hypotheses.',
     ['shilov1967hilbert1'],reconstruction=r'The scope is restricted to the published regular-domain construction instead of guessing a general geometric theorem from “bounded curvature.”',match='partial',confidence='medium')
item(95,'P000147','construction','A Poisson inverse for the regular operator',
     r'The inhomogeneous problem \(\Delta u=g\in\overline R\) also has an explicit formula.',
     r'For the same regular boundary problem, separate a harmonic extension of the boundary data and a zero-boundary solution operator \(P\) satisfying \(LPg=g\) on the allowed regular class. Boundedness of \(P\), with the relevant domain norm, is needed for continuous dependence.',
     'A',r'\citet[\S\S4--5]{shilov1967hilbert1} gives the inhomogeneous construction.',
     r'established within that framework.', ['shilov1967hilbert1'],reconstruction=r'The operator notation \(P\) is introduced for the next fixed-point step.')
item(95,'P000147','method','Semilinear equations by a fixed point',
     r'\(\Delta u=\varphi(x,u(x))\) is said to be solved by a fixed-point method.',
     r'A sufficient abstract version is: on a closed ball of the regular Banach function space, \(T(u)=h+P\varphi(\cdot,u)\) preserves the ball and \(\varphi\) is uniformly Lipschitz in \(u\) with \(\|P\|\operatorname{Lip}_u\varphi<1\). Then \(T\) has a unique fixed point, solving the specified boundary problem.',
     'A',r'The nonlinear programme was published in \citet[Theorems 1--2]{shilov1967hilbert3}, received 16 February 1967.',
     r'established under appropriate existence hypotheses. The bare phrase does not prove global solvability for arbitrary nonlinearities.',
     ['shilov1967hilbert3'],reconstruction=r'The ball-invariance and contraction assumptions are our transparent sufficient version, not a claim that they reproduce the strongest published theorem.',match='partial',development='annotated')
corr('P000146','Ambient uniform algebra',r'\(C(S)\), all strongly continuous functions',r'Use \(C_b(S)\) when referring to a uniform-norm Banach algebra.',r'Norm continuity on a closed infinite-dimensional ball does not imply boundedness; the generated regular algebra is bounded.')
corr('P000146','Dirichlet boundary described as weakly closed',r'\(\Sigma\): closed surface (weak)',r'Preserve the word; annotate that norm-sphere boundaries are not weakly closed.',r'The scan has the parenthetical \ru{слаб}. An orthonormal sequence on the unit sphere converges weakly to 0, so literal weak closedness is incompatible with the basic spherical example.')
save()

talk(96,'1966-09-12','I. M. Gelfand','P000146-P000149',
     'Uniqueness, admissibility, and viscosity for hyperbolic systems',
     r'The middle and lower parts of P000147 ask when nonlinear first-order systems have unique solutions. Scalar convexity, characteristic eigenvector curves, conservation form, viscosity, and travelling waves are juxtaposed. The equations and solution classes in the hydrodynamic remarks are too incomplete for an exact publication match.')
item(96,'P000147','definition','Hyperbolicity requires more than a real spectrum',
     r'\(u_t=A(u)u_x\) is called hyperbolic when all eigenvalues of \(A(u)\) are real.',
     r'For a standard one-dimensional strictly hyperbolic quasilinear system, \(A\) is smooth on an open state set and has \(n\) distinct real eigenvalues there. For non-strict notions, diagonalizability and uniform control of eigenvectors must be specified; a real spectrum alone allows defective matrices.',
     'E',r'The modern strict-hyperbolicity setting of \citet[Theorem 1]{bianchinibressan2005viscosity} makes the assumptions needed for the later uniqueness question explicit.',
     r'the notebook’s definition is incomplete for standard well-posedness theorems.',
     ['bianchinibressan2005viscosity'],reconstruction=r'Strict hyperbolicity is a sufficient precise scope, not an assertion that every physical example has distinct speeds.',match='partial')
item(96,'P000147','claim','Scalar convexity does not select a unique weak solution',
     r'For \(n=1\), uniqueness is said always to hold when \(f\) is convex.',
     r'For \(u_t+F(u)_x=0\) with smooth scalar flux and bounded initial data, entropy admissibility yields the standard unique solution. Convexity alone does not make arbitrary distributional solutions unique. For Burgers flux \(F(u)=u^2/2\) and data 0 left, 1 right, both an expansion shock of speed \(1/2\) and the rarefaction fan are weak solutions.',
     'E',r'Entropy selection was present in \citet{oleinik1957discontinuous}; the general scalar uniqueness framework is \citet{kruzhkov1970first}.',
     r'the literal weak-solution claim is false; the entropy formulation is established.',
     ['oleinik1957discontinuous','kruzhkov1970first'],reconstruction=r'\ours\ The shock satisfies Rankine--Hugoniot since \((1/2-0)/(1-0)=1/2\). The fan is \(u=0,x\leq0\), \(u=x/t,0<x<t\), \(u=1,x\geq t\); it solves the equation in each region and is continuous across its interfaces. Their common initial trace proves nonuniqueness without admissibility.',literal='false as written',match='partial',development='annotated')
item(96,'P000147','remark','Hydrodynamics, magnetohydrodynamics, and an unspecified Godunov class',
     r'Two-component hydrodynamics and apparently magnetohydrodynamics are said to have uniqueness; a narrow class treated by Godunov is mentioned.',
     r'No single uniqueness theorem can be recovered without the exact equations, state restrictions, domain, data, and admissibility criterion. These fragments do not establish uniqueness for every Euler or magnetohydrodynamic system.',
     'F',r'The checked scalar and strictly hyperbolic literature does not identify these particular fragments: \citet{oleinik1957discontinuous,bianchinibressan2005viscosity} are comparisons only.',
     r'unidentified at theorem level; not evidence of an undeveloped problem.',
     ['oleinik1957discontinuous','bianchinibressan2005viscosity'],literal='not determinable',match='thematic only',verification='unresolved lead',confidence='low')
item(96,'P000147','definition','Convexity along an eigenvector field',
     r'Draw eigenvectors in state space; convexity may mean growth of the corresponding eigenvalue along their integral curves.',
     r'If \(A(u)r_i(u)=\lambda_i(u)r_i(u)\) is a smooth simple eigenpair, the genuine-nonlinearity condition is \(D\lambda_i(u)\cdot r_i(u)\ne0\). Linear degeneracy means that derivative vanishes identically. These are properties of characteristic fields in state space, distinct from the space-time characteristics of one solution.',
     'E',r'This is the classical characteristic-field distinction from Lax’s 1957 theory, discussed in the historical setup of \citet{bianchinibressan2005viscosity}.',
     r'established; the notebook gives the correct geometric idea without specifying nonvanishing or normalization.',
     ['bianchinibressan2005viscosity'],match='partial',reconstruction=r'The derivative condition and distinction of the two kinds of curves are supplied.')
item(96,'P000147','method','Conservation form and the meaning of a shock',
     r'Writing \(u_t=\partial_x f(u)\) is said to be better than general quasilinear form.',
     r'For a conservative system \(u_t+F(u)_x=0\), weak solutions and jump conditions are defined distributionally. For a general nonconservative matrix \(A(u)\), \(A(u)u_x\) is not canonically defined at jumps; a regularization or prescribed nonconservative product is additional data.',
     'E',r'The conservative/nonconservative distinction is explicit in \citet[Introduction and Theorem 1]{bianchinibressan2005viscosity}.',
     r'standard; the notebook’s plus-sign convention is converted by \(F=-f\).',
     ['bianchinibressan2005viscosity'],reconstruction=r'The distributional explanation is supplied.',match='partial')
item(96,'P000147','question','Uniqueness selected by identity viscosity',
     r'When does adding \(\epsilon u_{xx}\) give uniqueness?',
     r'A definite interpretation asks whether, for smooth strictly hyperbolic \(A\) and common initial data, solutions of \(u_t+A(u)u_x=\epsilon u_{xx}\) converge as \(\epsilon\downarrow0\) to one limit independent of subsequence. Small total variation, values in a fixed hyperbolicity neighbourhood, and the identity viscosity matrix specify an established scope.',
     'B',r'\citet[Theorem 1]{bianchinibressan2005viscosity} prove this small-BV statement, with uniform BV and Lipschitz dependence; the preprint circulated in November 2001 and publication followed in 2005.',
     r'solved in the stated small-BV setting. The unrestricted wording does not specify a single larger well-posedness problem and is not claimed solved.',
     ['bianchinibressan2005viscosity'],reconstruction=r'The vanishing-viscosity interpretation is distinguished from the easier uniqueness of a fixed strictly parabolic equation.',match='partial',problem='GP-1966-08')
item(96,'P000147','method','Travelling-wave reduction is local information',
     r'The viscosity question is said to reduce to ordinary differential equations.',
     r'For a conservative viscous system, a travelling profile \(U((x-st)/\epsilon)\) satisfies \(U^{\prime}=F(U)-F(u_-)-s(U-u_-)\) after integration, with end states at equilibria. For the notebook sign convention in a nonconservative system, the second-order equation is \(U^{\prime\prime}=-(A(U)+sI)U^{\prime}\).',
     'E',r'Travelling profiles are part of the analysis in \citet{bianchinibressan2005viscosity}; a full Cauchy-problem uniqueness proof needs substantially more.',
     r'the profile reduction is valid; equivalence to global uniqueness of arbitrary solutions is false.',
     ['bianchinibressan2005viscosity'],reconstruction=r'\ours\ Both ODEs are derived here by substitution. They reconstruct a plausible local meaning of the last sentence, not the cancelled word.',match='partial',development='annotated')
prob('GP-1966-08','Uniqueness of the vanishing identity-viscosity limit',r'Under what hypotheses do the solutions of \(u_t+A(u)u_x=\epsilon u_{xx}\) have a unique limit as \(\epsilon\downarrow0\)?',['1966-96.6'],r'As of November 2026: Bianchini--Bressan solve the smooth strictly hyperbolic small-total-variation case. The notes do not determine a universal large-data conjecture.',['bianchinibressan2005viscosity'])
corr('P000147','Scalar uniqueness',r'Always unique if the scalar flux is convex.',r'Unique in the entropy/admissible class; not among all weak solutions.',r'The statement is faithfully present in the scan. The Burgers expansion shock and rarefaction with the same Riemann data distinguish the two readings.')
save()

talk(97,'1966-09-12','I. N. Bernstein','P000147-P000150',
     'The representation-ring completion theorem and the circle',
     r'P000148 explicitly reports part of what Atiyah had explained. The augmentation-ideal completion theorem is illustrated by \(S^1\) and \(\mathbb{CP}^{\infty}\). Two literal slips deserve separate treatment: calling the uncompleted map an embedding for every compact group, and giving the wrong fibre and total space for the tautological bundle.')
item(97,'P000148','construction','The representation ring and associated universal bundles',
     r'\(R_G\) is the commutative ring of finite-dimensional representations and their formal differences; a representation gives a bundle over \(B_G\).',
     r'For compact Lie \(G\), use finite-dimensional complex continuous representations. Direct sum and tensor product define \(R(G)\). The associated-bundle construction sends \([V]\) to \([EG\times_GV]\in K^0(BG)\) and is a ring homomorphism.',
     'E',r'This construction underlies \citet[Introduction]{atiyahsegal1969completion}, whose introduction traces the finite-group and connected-group cases to 1961.',
     r'standard; complex coefficients and virtual bundles are made explicit.', ['atiyahsegal1969completion'],verification='publisher metadata checked')
item(97,'P000148','claim','The uncompleted map need not be an embedding',
     r'The arrow \(R_G\to K(B_G)\) is labelled \ru{Вложение}.',
     r'The map need not be injective for disconnected compact groups. In \(R(C_6)=\mathbb Z[x]/(x^6-1)\), let \(a=(x-1)(x+1)(x^2+x+1)\ne0\). Then \((x^2-x+1)a=0\) and \((x-1)(-x)a=a\), so \(a\in\bigcap_{n\geq1}(x-1)^nR(C_6)\); its completion image vanishes.',
     'E',r'The correct general statement is completion, as in \citet{atiyahsegal1969completion}; the elementary cyclic-group calculation here checks the stronger notebook wording.',
     r'the literal embedding assertion is false in this generality.', ['atiyahsegal1969completion'],
     reconstruction=r'\ours\ The displayed polynomial has degree four and is nonzero modulo the monic degree-six relation. Since \(1+(x-1)x=x^2-x+1\), multiplication by \(-x\) is an inverse to \(x-1\) on the submodule generated by \(a\). Iteration proves membership in every augmentation power. The completion theorem then identifies its image in \(K^0(BC_6)\) with zero.',literal='false as written',match='partial',verification='publisher metadata checked',development='annotated')
item(97,'P000148','theorem','Augmentation completion gives K of the classifying space',
     r'Completing \(R_G\) at virtual representations of dimension zero gives \(K(B_G)\).',
     r'For compact Lie \(G\), \(I_G=\ker(\dim:R(G)\to\mathbb Z)\) and \(\widehat{R(G)}_{I_G}=\varprojlim R(G)/I_G^n\). The associated-bundle map induces \(\widehat{R(G)}_{I_G}\cong K^0(BG)\); also \(K^1(BG)=0\).',
     'E',r'\citet[Introduction]{atiyahsegal1969completion} records the 1961 cases and supplies a unified 1969 proof; the seminar itself documents prior circulation of the general statement.',
     r'established. Class E describes Bernstein’s explicit exposition of Atiyah, rather than a claim of a 1966 Bernstein discovery.', ['atiyahsegal1969completion'],verification='publisher metadata checked',literal='correct')
item(97,'P000148','construction','The circle completion is a formal power-series ring',
     r'\(R_{S^1}=\sum n_ix^i\), only finitely many nonzero coefficients; \(y=x-1\) generates the augmentation ideal and \(\widehat R_{S^1}=\mathbb Z[[y]]\).',
     r'\(R(S^1)=\mathbb Z[x,x^{-1}]\), where \(x\) is the weight-one character. Modulo \(y^n\), \(x=1+y\) is invertible; inverse limits therefore give \(\mathbb Z[[y]]\). The notebook’s geometric series \(1/(1-y)\) is an example of a formal series, not the expansion of \(x^{-1}\).',
     'E',r'This is the standard circle example of the completion theorem \citep{atiyahsegal1969completion}; Atiyah’s course circulated in 1964 and appeared as \citet{atiyah1967ktheory}.',
     r'established elementary calculation.', ['atiyahsegal1969completion','atiyah1967ktheory'],reconstruction=r'The inverse-limit justification and distinction of the two inverses are supplied.',verification='publisher metadata checked',literal='correct')
item(97,'P000148','construction','Projective space and its tautological line bundle',
     r'\(B_{S^1}=\mathbb{CP}^{\infty}\); on \(\mathbb{CP}^n\) the canonical bundle is described as having fibre \(\mathbb{CP}^1\) and total space \(\mathbb{CP}^{n+1}\).',
     r'The tautological complex line bundle \(L\to\mathbb{CP}^n\) has fibre the line \(\ell\cong\mathbb C\) above \([\ell]\). Its unit-circle bundle is \(S^{2n+1}\to\mathbb{CP}^n\), with fibre \(S^1\). Neither the line bundle nor this circle bundle has total space \(\mathbb{CP}^{n+1}\).',
     'E',r'The standard construction is part of Atiyah’s 1964 course, published as \citet{atiyah1967ktheory}.',
     r'the model for \(BS^1\) is correct; the finite-dimensional bundle description is false as written.', ['atiyah1967ktheory'],reconstruction=r'The two actual bundles are distinguished to avoid guessing an unstated projectivization.',literal='false as written',verification='publisher metadata checked',match='partial',development='annotated')
item(97,'P000148','theorem','K of finite and infinite complex projective space',
     r'Every class on \(\mathbb{CP}^n\) is a polynomial in \(x-1\), and \((x-1)^{n+1}=0\); passage to the limit gives the infinite case.',
     r'For \(x=[L]\), \(K^0(\mathbb{CP}^n)=\mathbb Z[x]/((x-1)^{n+1})\), \(K^1(\mathbb{CP}^n)=0\), and the compatible inverse limit is \(K^0(\mathbb{CP}^{\infty})=\mathbb Z[[x-1]]\).',
     'E',r'This is the projective-space calculation in \citet{atiyah1967ktheory}, based on the 1964 lectures.',
     r'established. The exponent depends on the finite stage \(n\).', ['atiyah1967ktheory'],reconstruction=r'The odd K group is supplied to justify the uncomplicated inverse limit.',verification='publisher metadata checked',literal='correct')
corr('P000148','Associated-bundle arrow',r'\ru{Вложение} \(R_G\to K(B_G)\)',r'A homomorphism, inducing an isomorphism after completion.',r'The word is clear in the scan. The explicit nonzero element in \(\bigcap I^n\subset R(C_6)\) shows that injectivity is not valid for all compact groups.')
corr('P000148','Canonical bundle on projective space',r'Fibre \(\mathbb{CP}^1\), total space \(\mathbb{CP}^{n+1}\)',r'Tautological line fibre \(\mathbb C\); unit-circle total space \(S^{2n+1}\).',r'The projective-space symbols are visible in the scan. This is a mathematical slip in the source, not an OCR substitution.')
save()

talk(98,'1966-09-19','I. N. Bernstein','P000148-P000152',
     'Equivariant completion, induction, and a noncompact programme',
     r'P000149--P000150 continue Atiyah’s programme: skeletal limits, equivariant vector bundles, the Borel construction, and reductions to a unitary group and maximal torus. Gelfand asks for a noncompact analogue and suggests a Plancherel replacement for dimension, but does not specify a representation ring or ideal. The family-index explanation is continued at record 104.')
item(98,'P000149','construction','Skeletal inverse limits',
     r'Take \(K((BG)_1)\leftarrow K((BG)_2)\leftarrow\cdots\) and its projective limit.',
     r'For this completion problem, skeletal K-groups determine the completed theory. For a general countable CW filtration \(X=\bigcup X_n\), however, the comparison is governed by \(0\to\varprojlim{}^1K^{-1}(X_n)\to K^0(X)\to\varprojlim K^0(X_n)\to0\). The derived-limit term must be shown to vanish or the pro-system formulation retained.',
     'E',r'The filtration/completion distinction is explicit in \citet{atiyahsegal1969completion}; the simple projective-space tower has vanishing odd groups.',
     r'valid in the appropriate completed interpretation, not an unconditional definition of topological K-theory for every infinite complex.', ['atiyahsegal1969completion'],reconstruction=r'The derived-limit caveat is supplied to prevent an overgeneralization.',verification='publisher metadata checked',match='partial')
item(98,'P000149','question','Gelfand’s noncompact completion programme',
     r'Generalize the K-functor and classifying space to locally compact Lie groups, using infinite-dimensional representations, so that the theorem remains valid.',
     r'This specifies a programme but not a single theorem: it leaves the representation category, Grothendieck construction, completion ideal, and space unspecified. One precise later analogue treats finite proper \(G\)-CW complexes for discrete \(G\); this does not settle all locally compact Lie groups in one canonical interpretation.',
     'F',r'\citet[Theorems 3.2 and 4.3; \S5]{luckoliver2001completion} provide a proper-action analogue and explain difficulties for positive-dimensional noncompact groups.',
     r'partly realized through several inequivalent theories, with no exact notebook conjecture to classify as solved or still open.', ['luckoliver2001completion'],literal='not determinable',match='thematic only',speaker='I. M. Gelfand',confidence='medium')
item(98,'P000149','remark','A Plancherel factor in place of dimension',
     r'Dimension is compared with an uncertain “factor” in the Plancherel formula.',
     r'For a noncompact group, an irreducible unitary representation may be infinite-dimensional; formal degree or Plancherel density can play an analogue of dimension in some formulas. The fragment does not specify a multiplication law, an augmentation homomorphism, or even a class of representations.',
     'F',r'The noncompact K-theory comparison in \citet[\S5]{luckoliver2001completion} does not identify this particular suggestion. No exact theorem match was found.',
     r'unidentifiable beyond the heuristic analogy.', ['luckoliver2001completion'],literal='not determinable',match='none found',verification='unresolved lead',speaker='I. M. Gelfand',confidence='low')
item(98,'P000149','definition','Equivariant K-theory of vector bundles',
     r'A \(G\)-bundle is a vector bundle with compatible linear action on fibres; take sums, tensor products, and formal differences. At a point the answer is \(R_G\).',
     r'For compact Lie \(G\) acting on compact \(X\), \(K_G^0(X)\) is the Grothendieck group of finite-rank complex \(G\)-equivariant vector bundles. Fibre maps are linear and cover the given base action. Pullback from a point makes it an \(R(G)\)-module, and \(K_G^0(*)=R(G)\).',
     'E',r'The construction was already being taught by Atiyah; \citet{atiyahsegal1969completion} uses the theory systematically.',
     r'standard for compact groups. Noncompact groups require additional qualifications.', ['atiyahsegal1969completion'],verification='publisher metadata checked',literal='correct')
item(98,'P000149-P000150','construction','The Borel construction',
     r'\(X_G=E\times_GX\), with \(E\) a free right \(G\)-space over \(B_G\); for a point one recovers \(B_G\).',
     r'Choose a contractible free right \(G\)-space \(EG\). For a left \(G\)-space \(X\), set \(X_G=(EG\times X)/((eg,x)\sim(e,gx))\). An equivariant bundle induces a bundle over \(X_G\), producing \(K_G^*(X)\to K^*(X_G)\).',
     'E',r'This is the comparison map of \citet{atiyahsegal1969completion}.',
     r'standard; contractibility is required of the universal free space.', ['atiyahsegal1969completion'],reconstruction=r'Contractibility and the explicit quotient convention are supplied.',verification='publisher metadata checked')
item(98,'P000150','theorem','The equivariant completion theorem',
     r'\(\widehat K_G(X)\cong K(X_G)\), with completion in the dimension-zero ideal of \(R_G\).',
     r'For compact Lie \(G\) and a finite \(G\)-CW complex \(X\), completion at \(I_G\) gives \(\widehat{K_G^*(X)}_{I_G}\cong K^*(EG\times_GX)\). A pro-system version handles the filtration explicitly; a statement for an arbitrary \(G\)-space without finiteness assumptions is too broad.',
     'B',r'\citet{atiyahsegal1969completion} is the exact general theorem publication. The notebook proves its circulation through Atiyah by September 1966.',
     r'established in the stated finite equivariant-CW setting.', ['atiyahsegal1969completion'],reconstruction=r'The finite \(G\)-CW hypothesis is a safe standard formulation of the announced result.',verification='publisher metadata checked')
item(98,'P000150','claim','Completion by tensoring with the completed coefficient ring',
     r'\(\widehat K_G(X)=K_G(X)\otimes_{R_G}\widehat R_G\) is offered as an exact definition.',
     r'For a Noetherian ring \(R\), ideal \(I\), and finitely generated \(R\)-module \(M\), \(\widehat M_I\cong M\otimes_R\widehat R_I\). Here compact Lie \(G\) and a finite \(G\)-CW complex ensure the relevant finiteness. This tensor formula is not a universal definition for arbitrary modules.',
     'E',r'This algebra is used in \citet{atiyahsegal1969completion}.',
     r'correct with finite-generation assumptions.', ['atiyahsegal1969completion'],reconstruction=r'The commutative-algebra hypotheses are supplied.',verification='publisher metadata checked',match='partial')
item(98,'P000150','construction','Induction to a unitary group',
     r'For \(G\subset U\), \(K_G(X)=K_U(U\times_GX)\), and \(X_G=(U\times_GX)_U\).',
     r'For a closed inclusion of compact Lie groups \(G\subset U(N)\), induction gives an equivalence of equivariant vector-bundle categories over \(X\) and \(U(N)\times_GX\), hence the K-theory isomorphism. The corresponding Borel constructions are naturally equivalent using a common universal free \(U(N)\)-space.',
     'E',r'This induction mechanism belongs to the completion proof in \citet{atiyahsegal1969completion}.',
     r'established; the equality of classifying constructions should be interpreted with the chosen models.', ['atiyahsegal1969completion'],reconstruction=r'Closed inclusion and common universal models make the displayed identities precise.',verification='publisher metadata checked')
item(98,'P000150','method','Maximal-torus splitting by a family index',
     r'For a maximal torus \(T\subset U\), restriction embeds a direct summand, with a dashed reverse map to be explained analytically.',
     r'For \(U=U(N)\), the flag manifold \(U/T\) is complex. The fibrewise Dolbeault index along \(U\times_TX\to X\) defines a retraction of restriction \(K_U(X)\to K_T(X)\): the projection formula and \(\operatorname{ind}_{U}(\bar\partial_{U/T})=1\) give \(p_!p^*=1\). The same mechanism compares the completed/Borel diagram.',
     'E',r'The direct-image strategy is discussed by Atiyah in \citet{atiyah1988commentary}; the theorem is \citet{atiyahsegal1969completion}.',
     r'established. An arbitrary elliptic operator, or the de Rham Euler index, need not give 1.', ['atiyah1988commentary','atiyahsegal1969completion'],reconstruction=r'The Dolbeault operator is our precise realization of the dashed arrow; the notebook postpones its definition to the family-index discussion.',match='partial',verification='publisher metadata checked')
corr('P000150','Lower-right corner of the comparison square',r'\(K_T(X)\)',r'\(K(X_T)\) in the lower Borel row; \(K_T(X)\) identifies with the upper-right equivariant term.',r'The scan really labels the lower-right entry \(K_T(X)\). With that label the right vertical arrow is not the intended completion comparison. The corrected label is a mathematical emendation.')
save()

talk(99,'1966-09-19','R. A. Minlos','P000150-P000156',
     'Canonical ensembles and factorial correlation functions',
     r'The first lecture starts at P000151 and ends near the top of P000155. It defines continuum and lattice models, the thermodynamic limit, canonical Gibbs weights, and correlation densities. The 1968 lectures explicitly identify the autumn 1966 Gelfand seminar as a source, while tracing the earlier course to Khumsan in September 1965. Much of this first lecture is foundational exposition, not a new result. The ordered-pair convention is retained consistently.')
item(99,'P000151','definition','Classical phase space and a Hamiltonian',
     r'A physical system is a state space and a real Hamiltonian; the classical states are \((p_1,\ldots,p_N,x_1,\ldots,x_N)\), with \(p_i\in\mathbb R^\nu\), \(x_i\in\Omega\).',
     r'For bounded measurable \(\Omega\subset\mathbb R^d\), the labelled phase space is \(\mathbb R^{dN}\times\Omega^N\), possibly restricted by \(|x_i-x_j|>\delta\). With \(m>0\), \(H=\sum_i|p_i|^2/(2m)+W_N(x_1,\ldots,x_N)\). Forbidden configurations may equivalently have \(H=+\infty\).',
     'E',r'Expository model setup: \citet[Lecture I]{minlos1968lectures}.',
     r'standard; allowing \(+\infty\) reconciles hard cores with the earlier phrase real-valued.', ['minlos1968lectures'],reconstruction=r'Measurability and labelled-particle convention are explicit.')
item(99,'P000151-P000152','definition','Ordered pair interactions and identical systems',
     r'\(W_N=\sum_{i\ne j}U(|x_i-x_j|)\); systems with fixed potential and mass but different \(N,\Omega\) are identical.',
     r'The notebook sums over ordered distinct pairs. Thus \(\sum_{i\ne j}U=\sum_{i<j}\phi\) with the usual unordered pair potential \(\phi=2U\). A thermodynamic sequence fixes \(U,m,\beta\) while changing \(N\) and the vessel.',
     'E',r'The conventions are compared with \citet[Lecture I]{minlos1968lectures}.',
     r'consistent if the factor two is retained throughout; it is not a transcription error.', ['minlos1968lectures'],reconstruction=r'The conversion \(\phi=2U\) prevents silently importing a different normalization.',literal='correct')
item(99,'P000152-P000154','construction','Integrating out momenta',
     r'The configurational system omits kinetic energy; the full Gibbs density factors into momentum and position distributions.',
     r'For \(\beta,m>0\), Gaussian integration contributes \((2\pi m/\beta)^{dN/2}\). The position marginal is \(Z_{N,\Omega}^{-1}e^{-\beta W_N}\), independently of the momentum variables. A fixed \(N!\) factor cancels from normalized labelled probabilities but matters when defining thermodynamic partition functions.',
     'E',r'The reduction is in \citet[Lecture I]{minlos1968lectures}.',
     r'established exact factorization.', ['minlos1968lectures'],reconstruction=r'The Gaussian factor and normalization qualification are supplied.',literal='correct')
item(99,'P000152','definition','A hard-core lattice gas',
     r'States are distinct sites of a cubic lattice; \(U(x)\) is even, without requiring spherical symmetry.',
     r'On a finite \(\Omega\subset\mathbb Z^d\), configurations are \(N\)-element subsets, or labelled distinct tuples with the corresponding symmetry factor. An even pair interaction \(U(z)=U(-z)\) defines \(W_N=\sum_{i\ne j}U(x_i-x_j)\). Lattice symmetry does not imply rotational invariance.',
     'E',r'This recurs from 1964-3.1; see \citet[Lecture I]{minlos1968lectures}.',
     r'standard.', ['minlos1968lectures'],literal='correct')
item(99,'P000152','remark','Repulsion, decay, and the Lennard--Jones example',
     r'\(U(r)=a r^{-12}-b r^{-6}\), \(a,b>0\), illustrates short-range repulsion and decay; finite-range and hard-core versions are also drawn.',
     r'For rigorous limits one needs quantitative assumptions, for example stability \(W_N\geq-BN\) and integrable tails or \(\int|e^{-\beta\phi(x)}-1|\,dx<\infty\). In physical dimension three the Lennard--Jones form has the appropriate repulsive core and integrable far tail. Mere growth at zero and decay at infinity, without rates or stability, are insufficient.',
     'E',r'The stability issue was treated before this lecture by \citet{fisherruelle1966stability}; later density-expansion hypotheses are explicit in \citet[\S2]{kunatsagkarogiannis2018density}.',
     r'established framework. The aside that physicists use only this potential is not a mathematical theorem.', ['fisherruelle1966stability','kunatsagkarogiannis2018density'],reconstruction=r'The precise stability and regularity assumptions are editorial additions.',match='partial')
item(99,'P000153','definition','Thermodynamic scaling and vessel regularity',
     r'\(\Omega_N\) fills space, \(|\Omega_N|/N\to v\), and the vessel shape is usually immaterial.',
     r'Take \(N\to\infty\), \(|\Omega_N|\to\infty\), \(N/|\Omega_N|\to\rho=1/v\in(0,\infty)\), with a van Hove exhaustion: for each fixed \(a>0\), the volume of the \(a\)-boundary strip is \(o(|\Omega_N|)\). Shape-independent limits require hypotheses on the interaction and on the quantity being limited.',
     'E',r'This continues 1964-3.2; the boundary-strip condition is explicit in \citet[Lecture III, \S4, p.~164]{minlos1968lectures}.',
     r'standard scaling, not a theorem that every correlation limit is unique at every density.', ['minlos1968lectures'],reconstruction=r'The van Hove condition replaces an unrestricted exhaustion.')
item(99,'P000153','definition','The finite canonical Gibbs law',
     r'\(p(a)=Q^{-1}e^{-\beta H(a)}\), \(Q=\int e^{-\beta H}\), is postulated in equilibrium; for a lattice replace density by probabilities.',
     r'Given a reference measure and \(0<Q<\infty\), the canonical law at fixed \(N,\Omega,\beta>0\) has that density. Stationarity alone does not characterize it: many functions of the energy yield invariant laws for Hamiltonian dynamics.',
     'E',r'The canonical ensemble is introduced in \citet[Lecture I]{minlos1968lectures}.',
     r'established equilibrium model; the Gibbs form is an assumption here, not deduced merely from time-independence.', ['minlos1968lectures'],reconstruction=r'Normalization and the logical status of the postulate are supplied.')
item(99,'P000154','definition','Factorial correlation densities',
     r'\(\tau_k=(N!/(N-k)!)p(x_1,\ldots,x_k)\), where \(p\) is a marginal density.',
     r'For a symmetric labelled \(N\)-particle density, \(r_k=(N)_kp_k\), \((N)_k=N(N-1)\cdots(N-k+1)\). It represents ordered distinct particle tuples: \(\mathbb E\sum_{i_1,\ldots,i_k\ {\rm distinct}}h(x_{i_1},\ldots,x_{i_k})=\int h r_k\), whenever the integral is meaningful.',
     'E',r'The factorial convention is explicit in \citet[Lecture III, \S1]{minlos1968lectures}.',
     r'standard. These densities are not normalized probability densities.', ['minlos1968lectures'],reconstruction=r'We use \(r_k\) as a typographically unambiguous synonym for the notebook’s \(\tau_k\).',literal='correct')
item(99,'P000154','theorem','Expectations of summatory observables',
     r'First- and second-order summatory functions have means \(\int f\tau_1\) and \(\iint f\tau_2\).',
     r'For an integrable test function, \(\mathbb E\sum_if(x_i)=\int_\Omega f(x)r_1(x)\,dx\). For an integrable symmetric pair kernel, \(\mathbb E\sum_{i\ne j}h(x_i,x_j)=\int_{\Omega^2}h(x,y)r_2(x,y)\,dx\,dy\); no additional factor \(1/2\) occurs.',
     'E',r'These identities are used in \citet[Lecture III, \S1 and \S4]{minlos1968lectures}.',
     r'exact consequences of the definition.', ['minlos1968lectures'],literal='correct')
item(99,'P000154-P000155','theorem','Local mean particle density',
     r'For the particle count \(n_C\), \(\mathbb E n_C=\int_C\tau_1\); small regions identify \(\tau_1\) as local mean density.',
     r'For measurable \(C\subset\Omega\), \(\mathbb E n_C=\int_Cr_1\). If \(r_1\) is locally integrable, averages over shrinking balls converge to \(r_1(x)\) at its Lebesgue points; if it is continuous, this holds at every interior point.',
     'E',r'The interpretation is given in \citet[Lecture III, \S1]{minlos1968lectures}.',
     r'established, with the usual differentiation qualifications.', ['minlos1968lectures'],reconstruction=r'Lebesgue points specify the sense of the limiting density.')
item(99,'P000155','claim','Probability of exactly one point in a small region',
     r'\(P(n_{\Delta C}=1)=\tau_1(x_0)\Delta C+o(\Delta C)\).',
     r'For shrinking neighbourhoods \(C\) of \(x_0\), continuity of \(r_1\) there and a locally bounded \(r_2\) imply \(P(n_C=1)=r_1(x_0)|C|+o(|C|)\). Indeed \(0\leq\mathbb E n_C-P(n_C=1)\leq\mathbb E[n_C(n_C-1)]=\int_{C^2}r_2=O(|C|^2)\).',
     'E',r'The local interpretation occurs in \citet[Lecture III, \S1]{minlos1968lectures}.',
     r'correct with control of multiple occupancy; hard cores make that control immediate in sufficiently small cells.', ['minlos1968lectures'],reconstruction=r'The explicit factorial-moment estimate is supplied.',development='annotated')
save()

talk(100,'1966-09-26','R. A. Minlos','P000154-P000159',
     'Bulk correlations, clustering, and representative means',
     r'The second lecture begins midway down P000155 and ends on P000157. It deliberately labels several thermodynamic assertions as hypotheses, allows an effective specific volume depending on the correlation order, and uses clustering to argue that pair observables concentrate. The 1968 version restores an integrable decay requirement; nevertheless the displayed variance proof needs more than the stated \(L^1\) condition on the pair kernel. Our bounded development isolates the exact probabilistic implication and its limits.')
item(100,'P000155','claim','Two-cell probabilities and the second correlation density',
     r'\(\tau(x_1,x_2)\Delta x_1\Delta x_2\) is the probability of one particle in each of two small cells.',
     r'For disjoint shrinking cells \(C_1,C_2\) around distinct points, continuous \(r_2\) and locally bounded \(r_3,r_4\) yield \(P(n_{C_1}=n_{C_2}=1)=r_2(x_1,x_2)|C_1||C_2|+o(|C_1||C_2|)\). The exact identity without small-cell qualification is \(\mathbb E(n_{C_1}n_{C_2})=\int_{C_1\times C_2}r_2\).',
     'E',r'Factorial interpretation: \citet[Lecture III, \S1]{minlos1968lectures}.',
     r'correct as a leading-order interpretation, not an exact finite-cell probability.', ['minlos1968lectures'],reconstruction=r'Disjointness and multiple-occupancy bounds are supplied.')
item(100,'P000155-P000156','conjecture','Bulk-correlation hypotheses with an unspecified exceptional set',
     r'Hypotheses 1--5 assert limiting \(\bar\tau_k\), a boundary-distance error, translation invariance, continuity away from exceptional parameters, and boundedness. The effective \(v_N\) may depend on \(k\).',
     r'For a specified stable finite-range continuum pair potential and fixed \((\rho,\beta)\), ask for a canonical bulk limit \(r_{k,N}\to r_k\), independent of a regular vessel exhaustion, and quantitative boundary/mixing estimates strong enough to integrate products of local observables. The dilute regime supplies such results in explicit ranges; the notebook proposes an extension through thermodynamic regimes, without specifying the exceptional set.',
     'F',r'The 1968 account retains hypotheses and asks for precise inequalities \citep[Lecture III, \S3 and Problem 3, p.~164]{minlos1968lectures}. Dilute canonical results appear in \citet[Theorem 2.5 and Corollary 2.6]{pulvirentitsagkarogiannis2015finite} and \citet[Theorems 2.1,2.7]{kunatsagkarogiannis2018density}.',
     r'the programme has rigorous dilute-regime realizations, but no precise all-density residual conjecture is certified by this source. The exceptional set and admissible phase selection are unspecified. F records this failure of exact formulation, not a failure to recognize the subject.',
     ['minlos1968lectures','pulvirentitsagkarogiannis2015finite','kunatsagkarogiannis2018density'],
     reconstruction=r'The conditional moment implication is audited separately under item 1966-100.11. Its completed proof is not presented as an open-problem advance. The broader programme cannot be converted into a precise C question by silently defining its exceptional set.',literal='not determinable',match='partial',confidence='medium')
item(100,'P000155','claim','An order-dependent effective specific volume',
     r'For every \(\tau_k\) there is \(v_N\), depending on the vessel and \(k\), that improves the boundary approximation; \(v_N\to v\).',
     r'In the ideal canonical gas of volume \(V\), \(r_{k,N}=(N)_k/V^k\). The infinite-volume ideal density is \(\rho^k\). For each fixed \(k\leq N\), choosing \(\rho_{N,k}=(N)_k^{1/k}/V\), equivalently \(v_{N,k}=V/(N)_k^{1/k}\), matches that order exactly and \(v_{N,k}\to v\). A single \(\rho_N\) cannot match both orders 1 and 2.',
     'E',r'The canonical adjustment is discussed in \citet[Lecture III, \S3, p.~161]{minlos1968lectures}; the exact ideal-gas calculation is elementary.',
     r'the notebook’s \(k\)-dependent quantifier passes the ideal-gas test. The stronger common-parameter version would fail.', ['minlos1968lectures'],reconstruction=r'\ours\ The explicit \(k\)-dependent formula is calculated here and checked by the supplied code. It verifies only the ideal gas, not interacting boundary rates.',match='partial',development='annotated')
item(100,'P000155-P000156','claim','The exponential wall-rate claim and its missing regime',
     r'For compactly supported potentials the decay function is indicated as \(e^{-\lambda r}\). Continuity may fail at exceptional \((v,\beta)\).',
     r'The displayed \(\gamma\) controls error by distance to the vessel wall, after the order-dependent parameter adjustment. This is distinct from spatial decay between two particle clusters. A precise theorem would specify the potential, thermodynamic regime, boundary conditions, and adjustment before asserting an exponential wall estimate. The notes explicitly allow exceptional parameters and failure of the rate at some volumes per particle.',
     'F',r'\citet[Theorem 2.5, Corollary 2.6]{pulvirentitsagkarogiannis2015finite} gives a related dilute two-point estimate with a finite-volume term; it is not an exact match to this adjusted wall-error assertion.',
     r'no exact theorem with the notebook’s undeclared regime was identified. Its qualified claim is not refuted by imposing a universal quantifier it never states.', ['pulvirentitsagkarogiannis2015finite'],reconstruction=r'The canonical correction in the development concerns unadjusted pair covariance. The ideal gas actually supports the separate k-dependent wall-parameter adjustment, so that calculation does not refute this source claim.',literal='not determinable',match='thematic only',verification='unresolved lead',confidence='medium')
item(100,'P000155-P000156','claim','Translation invariance, continuity, and the density parameter',
     r'Translation invariance gives \(\bar\tau_1=\rho\). The notes say the hypotheses are proved for small \(v\) and \(\beta\), crediting Ruelle.',
     r'A translation-invariant state has a constant one-point density; identifying it with the imposed canonical density additionally uses bulk convergence without loss of mass. The perturbative gas regime is small density/activity, hence large specific volume \(v=1/\rho\), not small \(v\). Within a convergent expansion, correlations depend analytically on the appropriate parameter.',
     'E',r'Ruelle’s gas-phase results appeared in 1963--1964 \citep{ruelle1963correlation,ruelle1964cluster}; canonical density expansions are made precise by \citet[Theorem 2.7]{kunatsagkarogiannis2018density}.',
     r'the qualitative gas-phase conclusion is established; the source’s volume/density wording is inverted.', ['ruelle1963correlation','ruelle1964cluster','kunatsagkarogiannis2018density'],reconstruction=r'The relation \(v=1/\rho\) is already explicit on P000155 and determines the correction.',literal='false as written',match='partial')
item(100,'P000156','question','Can arbitrary initial distributions lead to Gibbs laws?',
     r'Gelfand suggests that any distribution might approach Gibbs as particle number increases; Arnold objects that an ergodic hypothesis is missing.',
     r'Without a rule associating initial laws and dynamics for different \(N\), this is not one convergence theorem. Invariance or ergodicity on an energy surface concerns a microcanonical measure, whereas a canonical law mixes energy levels. Deterministic Hamiltonian evolution preserves energy and cannot send every initial energy distribution to one prescribed canonical distribution.',
     'F',r'The ensemble distinction is treated in \citet[Lecture II]{minlos1968lectures}; no exact publication is identified for this exchange.',
     r'the unrestricted universality suggestion fails; no definite residual conjecture is recoverable.', ['minlos1968lectures'],literal='not determinable',match='thematic only',verification='unresolved lead',speaker='I. M. Gelfand; intervention by V. I. Arnold',confidence='medium')
item(100,'P000156','definition','Representativity is concentration of a normalized sequence',
     r'\(P(|F-\langle F\rangle|>\epsilon)\to0\); the notes immediately call this imprecise because there is no one function \(F\).',
     r'For an extensive observable \(F_N\), the intended property is \((F_N-\mathbb EF_N)/N\to0\) in probability. If \(\mathbb EF_N/N\to m\), this gives \(F_N/N\to m\). Unnormalized fluctuations need not converge to zero.',
     'E',r'The normalization is explicit in \citet[Lecture III, \S4]{minlos1968lectures}.',
     r'established definition; the notebook itself flags the shorthand.', ['minlos1968lectures'],reconstruction=r'The triangular sequence of observables and probability laws is made explicit.',literal='correct with missing hypotheses')
item(100,'P000156','construction','An integrable pair observable',
     r'\(F_N=\sum_{i\ne j}f(x_i-x_j)\), with one fixed \(f\) and \(\int|f|<\infty\).',
     r'Use a real even measurable \(f\in L^1(\mathbb R^d)\) and ordered pairs. A uniform bound \(r_{2,N}\leq C_2\) implies \(\mathbb E|F_N|\leq C_2|\Omega_N|\|f\|_1\). It does not imply a finite second moment. The symmetry condition is inherited from the preceding lecture.',
     'E',r'The same integrability assumption is (3.24) in \citet[Lecture III, \S4]{minlos1968lectures}.',
     r'the expectation is controlled; variance needs additional short-distance integrability.', ['minlos1968lectures'],reconstruction=r'Explicit evenness and the moment distinction are supplied.',development='annotated')
item(100,'P000156','claim','The mean per particle has a correlation-integral limit',
     r'\(\langle F_N\rangle=|\Omega_N|\int\bar\tau_2(\xi)f(\xi)\,d\xi+o(|\Omega_N|)\), hence the mean per particle tends to \(v\) times that integral.',
     r'A sufficient precise hypothesis is \(r_{2,N}\leq C_2\) and almost-everywhere convergence of \(A_N(z)=|\Omega_N|^{-1}\int\mathbf1_{\Omega_N}(x)\mathbf1_{\Omega_N}(x-z)r_{2,N}(x,x-z)\,dx\) to a bulk function \(R(z)\). Then dominated convergence gives \(\mathbb EF_N/|\Omega_N|\to\int fR\), and \(\mathbb EF_N/N\to v\int fR\) if \(|\Omega_N|/N\to v\). Pointwise convergence near a fixed origin alone is insufficient.',
     'A',r'The calculation is published in \citet[Lecture III, \S4, pp.~162--163]{minlos1968lectures}, from the 1965/1966 lectures.',
     r'valid under the stated uniform bulk hypotheses.', ['minlos1968lectures'],reconstruction=r'Uniform integrability and the vessel condition are supplied; the final subscript must remain 2.',match='partial')
item(100,'P000157','conjecture','The multiplicative cluster property',
     r'\(|\bar\tau_{k+s}-\bar\tau_k\bar\tau_s|\leq C_{k,s}\gamma(\min|x_i-y_j|)\) is said to follow, with difficulty, from preceding hypotheses.',
     r'This is a mixing property of the limiting state and requires more than existence, boundedness, translation invariance and continuity of correlations. For example a stationary mixture of Poisson processes of two distinct intensities has bounded factorial densities of each order but a nonzero, distance-independent two-point connected correlation.',
     'E',r'The gas-phase cluster theorem predates the talk \citep{ruelle1964cluster}. The general inference is not supplied by \citet[Lecture III, \S3]{minlos1968lectures}.',
     r'established in suitable pure/uniqueness regimes; false as an automatic consequence of the qualitative properties listed.', ['ruelle1964cluster','minlos1968lectures'],reconstruction=r'\ours\ If the random intensity is \(Z\in\{a,b\}\), \(r_k=\mathbb EZ^k\), and \(r_2-r_1^2=\operatorname{Var}Z>0\). This example refutes the logical implication between qualitative correlation properties; it is not claimed to be a canonical limit for the notebook’s fixed potential.',literal='false as written',match='partial',development='annotated')
item(100,'P000157','claim','The claimed linear variance and its integrability gap',
     r'\(DF_N\sim dN\), so \(D(F_N/N)\sim d/N\) and Chebyshev gives representativity.',
     r'With \(f\in L^1\cap L^2\), bounded second and third factorial densities, and an integrable finite-volume two-pair connected bound allowing an \(O(V^{-1})\) canonical term, one obtains \(\operatorname{Var}F_N=O(V)=O(N)\). These assumptions alone do not give a positive asymptotic coefficient. With only \(L^1\), variance can be infinite; concentration can nevertheless follow by truncation under the same correlation bounds.',
     'A',r'The 1968 proof adds integrable decay and a van Hove condition in its p.~164 remark \citep[Lecture III, \S4]{minlos1968lectures}, but still displays \(f^2\) after assuming only (3.24).',
     r'the notebook’s stated assumptions do not prove the variance asymptotic. The chapter supplies a complete conditional repair and a counterexample, without claiming novelty for the probabilistic method.', ['minlos1968lectures'],reconstruction=r'\ours\ The repair, sharp distinction of moments, and truncation implication are proved in the development. They clarify the bounded implication within GP-1966-09, rather than solve its general thermodynamic part.',literal='false as written',match='partial',development='developed in this chapter',problem='GP-1966-09')
item(100,'P000157','theorem','The exact ordered-pair square expansion',
     r'\(F_N^2=2\sum_{i\ne j}f_{ij}^2+4\sum_{i,j,k\ {\rm distinct}}f_{ij}f_{kj}+\sum_{i,j,k,s\ {\rm distinct}}f_{ij}f_{ks}\).',
     r'For \(f_{ij}=f_{ji}\), this identity partitions two ordered pairs by whether their union has two, three, or four labels. Integration gives coefficients 2, 4, and 1 against \(r_2,r_3,r_4\), respectively. All three sums are over ordered distinct tuples as displayed.',
     'E',r'The same combinatorial calculation occurs in \citet[Lecture III, \S4, p.~163]{minlos1968lectures}.',
     r'exact. The supplied code checks the identity on exhaustive small labelled configurations independently of the proof.', ['minlos1968lectures'],reconstruction=r'\oursComputed\ The evenness requirement is explicit; the exact combinatorial verification is supplied with its output.',literal='correct with missing hypotheses',development='annotated')
prob('GP-1966-09','Representative pair observables: moment hypotheses and concentration',
     r'A precise question extracted from the representativeness argument is which moment and mixing hypotheses justify concentration of \(N^{-1}\sum_{i\ne j}f(x_i-x_j)\), and whether an arbitrary real even \(L^1\) kernel permits the claimed finite linear variance. Minlos’s later Problem 3 asks for quantitative inequalities in this argument. This entry does not index an unspecified all-density existence conjecture.',
     ['1966-100.11'],
     r'As of November 2026: the finite-variance claim under bare \(L^1\) is false even for an ideal gas. The chapter supplies a complete conditional correction with an explicit four-point bound, an \(L^1\) truncation conclusion, and counterexamples. These are checked critical annotations, not a claim that a previously open C/D problem has been solved. Establishing the assumed correlation bound in an interacting model remains model- and regime-dependent.',
     ['minlos1968lectures','pulvirentitsagkarogiannis2015finite','kunatsagkarogiannis2018density'])
corr('P000155','Effective-volume quantifier',r'For each \(\tau_k\), there exists \(v_N\); parenthesis doubtful.',r'Retain dependence on \(k\): \(v_{N,k}\), not one common adjustment for all orders.',r'The scan visibly ends the parenthesis with \ru{и от k}. The ideal-gas factorial densities independently confirm why this quantifier matters.',typ='ambiguity')
corr('P000156','Perturbative parameter',r'Proved only for small \(v\) and \(\beta\).',r'For the cited gas regime, small density/activity, hence large \(v=1/\rho\).',r'The source really has \ru{малых v}. Its own definition \(v=1/\rho\) on the preceding page and the cited gas-phase results show the inversion.')
corr('P000156','Last mean formula',r'\(\bar\tau_k\) with uncertain subscript',r'\(\bar\tau_2\) in the pair-observable formula.',r'The last glyph is overwritten and resembles k; all preceding three integrals on this page have the second correlation function. This is an interpretive emendation, not a confident new glyph reading.',typ='ambiguity')
corr('P000157','Variance conclusion under an L1 hypothesis',r'\(DF_N\sim dN\) from the assumptions displayed.',r'Add second-moment and integrable finite-volume clustering hypotheses for an \(O(N)\) bound; an asymptotic equivalent requires further convergence.',r'The scan’s leading variance term is \(2\iint f^2\tau_2\). An \(L^1\) pair kernel need not make it finite. The 1968 account restores integrable decay, but this separate short-distance defect remains.')
save()
