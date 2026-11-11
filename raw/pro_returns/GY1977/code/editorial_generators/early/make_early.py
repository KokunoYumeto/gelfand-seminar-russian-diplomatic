import json
from pathlib import Path

OUT = Path(__file__).parent
talks = []
items = []
areas = {}
problems = []

def talk(record, date, speaker, pages, title, summary, kind='talk'):
    talks.append(dict(record=record, date=date, speaker=speaker, pages=pages,
                      title=title, kind=kind, summary=summary))

def item(record, pages, kind, title, notes, statement, reconstruction='',
         cls='E', fate='', status='', correctness='correct with missing hypotheses',
         match='partial', verification='read the result', development='annotated',
         problem='', worth='', refs=(), confidence='high', area='', speaker=None):
    number = 1 + sum(i['record'] == record for i in items)
    ident = f'1977-{record}.{number}'
    value = dict(id=ident, record=record, pages=pages, kind=kind, title=title,
                 notes=notes, statement=statement, reconstruction=reconstruction,
                 **{'class':cls}, fate=fate, present_status=status or
                 'As of November 2026, this is an established expository item, subject to the hypotheses stated above.',
                 literal_correctness=correctness, publication_match=match,
                 verification=verification, development=development, problem=problem,
                 worth=worth, refs=list(refs), confidence=confidence)
    if speaker:
        value['speaker'] = speaker
    items.append(value)
    areas[ident] = area
    return ident

def checkpoint():
    ordered_items = sorted(items, key=lambda value: (value['record'], int(value['id'].split('.')[1])))
    for name, data in [('talks', talks), ('items', ordered_items), ('problems', problems), ('areas', areas)]:
        (OUT / f'{name}.json').write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n')

talk(419, '1977-09-05', 'V. G. Drinfeld', 'P000705-P000707',
     'Self-dual Yang-Mills fields and twistor bundles',
     r'The report presents the four-dimensional self-duality equation, its conformal invariance, and the twistor fibration \(\mathbf{CP}^{3}\to\mathbf{HP}^{1}\simeq S^{4}\). It states the instanton--holomorphic-bundle correspondence in abbreviated form and sketches how a connection produces a holomorphic structure. A proposed spectral-determinant path integral is much less specified. The opening reference to noncommutative algebraic geometry and BGG is a possible seminar theme, not a developed construction. The record ends before Krichever begins in the lower part of P000707. The catalogue date is retained: the handwritten month on P000705 appears to be IV, so the date is a provenance conflict, not an emendation of a clearly written IX.')
talk(420, '1977-09-05', 'I. M. Krichever', 'P000707-P000708',
     'Algebraic spectral curves and rational solutions of Lax equations',
     r'Krichever describes zero-curvature equations for ordinary differential operators, spectral curves and their degenerations, and rational KdV solutions governed by pole dynamics. The suggestion that rationality should replace an extra commuting operator for every Lax equation has no specified class of equations. These pages continue the finite-gap line represented by earlier items 1975-374.2--1975-374.5 and 1975-379.1. The actual transition to Margulis is at P000709, not at the ends of the overlapping catalogue page ranges.')
talk(421, '1977-09-12', 'G. A. Margulis', 'P000709-P000711',
     'Arithmeticity and superrigidity of higher-rank lattices',
     r'The talk defines lattices, arithmetic subgroups and irreducibility, states higher-real-rank arithmeticity and superrigidity, and sketches the passage from local-field representations to integral structure. It contrasts the theorem with the rank-one situation, then incompletely understood. The modern surviving question in complex hyperbolic dimension at least four is separated from the broad historical formulation. Local rigidity was already discussed in items 1964-8.1--1964-8.2 and 1966-93.1; those are related occurrences, not an earlier occurrence of the precise remaining rank-one problem.')
talk(422, '1977-09-19', 'D. A. Kirzhnits', 'P000712',
     'Announcement of Kirzhnits\u2019s presence',
     r'The overlapping catalogue range contains the bracketed notice that the physicist Kirzhnits is present. It does not identify a second independent mathematical exposition. Drinfeld\textquoteright s coordinate formulas on P000712 are assigned to record 423; Kirzhnits\textquoteright s subsequent physics discussion to record 425, with Gelfand\textquoteright s explicit coin-weighing intervention assigned to record 424. Thus this heading has no duplicated occurrence items.', kind='heading')
talk(423, '1977-09-19', 'V. G. Drinfeld', 'P000712',
     'Coordinate curvature and the Yang-Mills equations',
     r'A short continuation writes curvature, self-duality and the Yang--Mills equation in matrix coordinates. The formulas are the local version of record 419. The implication from self-duality to Yang--Mills is reconstructed using the Bianchi identity, rather than presented as a proof found in the notebook.')
talk(424, '1977-09-19', 'I. M. Gelfand', 'P000713-P000714',
     'Counterfeit coins and entropy',
     r'Gelfand interrupts the thermodynamic discussion with ternary weighing puzzles: 27 coins when the counterfeit is known to be lighter, and 13 when its sign is unknown. The number 13 is consistent with identifying the coin alone, leaving the sign of a never-weighed coin unresolved; requiring its sign as well gives the familiar 12-coin version. The ensuing entropy formulas include a missing minus sign in the binary case. Only the explicit intervention and the immediate combinatorial formulas are assigned here; the physical entropy discussion remains in record 425.')
talk(425, '1977-09-19', 'D. A. Kirzhnits', 'P000713-P000716',
     'Entropy, black-hole thermodynamics and accelerated observers',
     r'The physicist connects microscopic dynamics with entropy, black-hole horizons, the area law, Hawking radiation and the thermal response of accelerated observers. The talk also mentions temperature-dependent symmetry breaking and cosmology. Several statements are heuristic or numerically inaccurate: the solar Schwarzschild radius, the binary entropy sign in the adjoining intervention, and the normalization of the acceleration temperature require separate treatment. A causal loss of access to data is not silently upgraded to a precise quantum-information-loss conjecture. Vishik\textquoteright s closing Monte Carlo aphorism is assigned separately to record 427.')
talk(426, '1977-10-03', 'L. A. Dickey', 'P000717-P000718',
     'Formal variational calculus and Hamiltonian differential operators',
     r'Dickey defines differential polynomials, local functionals, variational derivatives and evolutionary derivations; he then gives an explicit Hamiltonian matrix and asks for a simpler proof of the Jacobi identity. The final comparison is with the third-order KdV Hamiltonian operator. P000718 belongs to this talk throughout, despite the supplied catalogue range ending at P000717; S. I. Gelfand begins on P000719. The principal theorem is linked explicitly in the notebook to Gelfand and Dickey\textquoteright s 1977 paper.')
talk(427, '1977-09-19', 'S. M. Vishik', 'P000716',
     'A Monte Carlo metaphor for a broad seminar',
     r'The only identifiable contribution is the closing aphorism that integrating a large domain calls for the Monte Carlo method, offered as an explanation of the seminar\textquoteright s breadth. No measure, integrand, error estimate or mathematical problem is specified. It is preserved as a remark, not reconstructed as a separate numerical-analysis lecture.')
checkpoint()

# Record 419.
item(419, 'P000705-P000706', 'definition', 'A unitary connection and the self-duality equation',
     r'The notes take a smooth complex bundle \(\xi\) on \(S^{4}\), a connection \(\nabla\), and its curvature \(K\), an \(\operatorname{End}(\xi)\)-valued two-form. They require a Hermitian metric and unitarity and write \(*K=K\).',
     r'On an oriented Riemannian four-manifold, a unitary connection \(A\) on a Hermitian bundle has \(F_A\in\Omega^2(\mathfrak u(E))\). Self-duality means \(*F_A=F_A\); reversing orientation interchanges this equation with anti-self-duality. This is a gauge-invariant condition.',
     r'The distinction between self-dual and anti-self-dual conventions, and the gauge-equivalence qualification, are made explicit here.',
     fate=r'This is the setup of the instanton correspondence reported in \citet[abstract and pp.~117--124]{atiyahward1977instantons}; that paper appeared in June 1977, before the catalogue date of this seminar.',
     correctness='correct', verification='publisher metadata checked', refs=['atiyahward1977instantons'], area='Gauge theory and twistor geometry')
item(419, 'P000705-P000706', 'theorem', 'Conformal invariance of four-dimensional self-duality',
     r'The star on two-forms in dimension four is said not to change when the metric is multiplied by a number. The next page describes a conformal metric as defined up to multiplication by a positive function.',
     r'For \(\widehat g=e^{2\varphi}g\) on an oriented \(d\)-manifold, the Hodge star on \(p\)-forms satisfies \(*_{\widehat g}=e^{(d-2p)\varphi}*_g\). Thus in dimension four the self-duality equation for two-forms depends only on the oriented conformal class.',
     r'The general scaling identity explains why a positive function, not merely a constant, is allowed; it follows directly by comparing the induced inner product on forms with the volume form.',
     fate=r'The conformal formulation is part of the twistor description in \citet[abstract]{atiyahward1977instantons}; the scaling calculation here is elementary reconstruction rather than a new result.',
     correctness='correct', verification='publisher metadata checked', refs=['atiyahward1977instantons'], area='Gauge theory and twistor geometry')
item(419, 'P000706', 'remark', 'Gluons and the proposed physical role of instantons',
     r'The notes say that the quantum analogues are gluons and that they hold quarks together.',
     r'The identifiable content is a motivation from non-Abelian gauge fields and the strong interaction. It supplies no mathematical confinement criterion or theorem relating the displayed self-dual classical fields to a mass gap or a quark potential.',
     r'An identification with the precise confinement question of earlier item 1975-377.10 would add a claim not made on this page.',
     cls='F', fate='No exact mathematical assertion about confinement can be identified here; the neighboring instanton paper is a construction in classical gauge theory, not a proof of this physical slogan.',
     status='As of November 2026, this occurrence remains a physical motivation without a separately recoverable mathematical proposition.',
     correctness='not determinable', match='none found', verification='unresolved lead', development='none', confidence='high', area='Mathematical physics')
item(419, 'P000706', 'method', 'A spectral-determinant path-integral prescription',
     r'To a pair \((\xi,\nabla)\) one is to assign a linear operator, form a regularized determinant from its spectrum, and integrate over solutions; the notes add that this is the denominator.',
     r'No operator, regularization, integration measure, gauge quotient, insertion or normalization is specified. Consequently there is no determined integral, determinant identity or renormalization claim to formalize.',
     r'It is tempting to supply a one-loop gauge-fixed determinant, but the notebook does not choose that construction.',
     cls='F', fate='Searches around the cited 1977 instanton/twistor correspondence identify the geometric report but do not identify this incomplete quantization prescription as a particular published formula.',
     status='As of November 2026, the operator and measure remain unidentified from this source; this is not an open-problem entry.',
     correctness='not determinable', match='none found', verification='unresolved lead', development='none', confidence='low', area='Mathematical physics')
item(419, 'P000706', 'construction', 'The twistor fibration over the four-sphere',
     r'Using \(\mathbf C\subset\mathbf H\), the notes pass from complex lines in \(\mathbf H^2\) to quaternionic lines and obtain \(\mathbf{CP}^3\to\mathbf{HP}^1=S^4\), with two-dimensional fibers.',
     r'Fix right scalar multiplication. The map sends a complex line \(\ell\subset\mathbf H^2\) to its quaternionic span \(\ell\mathbf H\). It is a smooth fiber bundle \(\pi:\mathbf{CP}^{3}\to\mathbf{HP}^{1}\simeq S^4\) with fiber \(\mathbf{CP}^1\simeq S^2\). Projectivization uses \(\mathbf H^2\setminus\{0\}\), so the zero vector must be excluded from the quotient.',
     r'The notes use left quaternionic projectivization; the equivalent right-scalar convention is chosen explicitly here. Deletion of zero is supplied. The fiber dimension is real dimension two, not complex dimension two.',
     fate=r'This is the twistor space underlying \citet[abstract]{atiyahward1977instantons}, already published before the catalogue date.',
     verification='publisher metadata checked', refs=['atiyahward1977instantons'], area='Gauge theory and twistor geometry')
item(419, 'P000706-P000707', 'construction', 'Quaternionic conjugation, invariant lines and the Klein quadric',
     r'An antilinear coordinate map pairs the four complex coordinates, and the notes describe invariant projective lines, the Grassmannian of lines, a quadric, and a real form with real points \(S^4\).',
     r'Let \(J(z_1,z_2,z_3,z_4)=(-\overline z_2,\overline z_1,-\overline z_4,\overline z_3)\). Then \(J^2=-1\), so its projectivization is a fixed-point-free antiholomorphic involution of \(\mathbf{CP}^3\). A complex two-plane invariant under \(J\) is a quaternionic line. Its locus in \(\operatorname{Gr}(2,4)\), identified by the Pl\"ucker embedding with the Klein quadric in \(\mathbf{CP}^5\), is \(\mathbf{HP}^1\simeq S^4\).',
     r'The real points are points of the induced real structure on the Grassmannian, not fixed points in \(\mathbf{CP}^3\). This distinction removes a possible ambiguity in the compressed wording.',
     fate=r'The construction belongs to the geometric background of \citet[pp.~117--124]{atiyahward1977instantons}; only the publisher abstract and bibliographic record were available for that reference in this audit.',
     verification='publisher metadata checked', refs=['atiyahward1977instantons'], area='Gauge theory and twistor geometry')
item(419, 'P000706-P000707', 'theorem', 'The instanton--holomorphic-bundle correspondence',
     r'Under the label Atiyah\textquoteright s theorem, the notes assert a one-to-one correspondence between bundles with self-dual connection on \(S^4\) and algebraic bundles on \(\mathbf{CP}^3\) trivial on every fiber of \(\pi\).',
     r'A safe rank-two version is a correspondence between gauge-equivalence classes of smooth \(SU(2)\) instantons on \(S^4\) and isomorphism classes of holomorphic rank-two bundles on \(\mathbf{CP}^3\), with trivial determinant, holomorphically trivial restriction to each real twistor line, and the compatible quaternionic reality structure required for a positive unitary real form. Choose the orientation so the notebook\textquoteright s sign \(*F=F\) corresponds to this convention.',
     r'The notebook allows arbitrary complex rank and omits equivalence relations and reality conditions. The statement here deliberately specifies the \(SU(2)\) case identified by the publication; bare complex bundles trivial on the real lines do not by themselves encode a unitary connection.',
     fate=r'\citet[abstract]{atiyahward1977instantons} identifies precisely the \(SU(2)\) instanton/algebraic-bundle construction. The paper was received 31 May and published June 1977. Class E uses the supplied 5 September 1977 catalogue date; its pre-talk chronology is conditional because P000705 instead appears to read 5/IV--77. The handwritten date has not been resolved. The full theorem was not accessible in the official copy consulted, so exact matching of every reconstructed reality hypothesis is not claimed.',
     status='As of November 2026, this is the established Ward correspondence. The historical report is recognizable, but its literal all-rank formulation omits indispensable structure.',
     match='partial', verification='publisher metadata checked', refs=['atiyahward1977instantons'], confidence='medium', area='Gauge theory and twistor geometry')
item(419, 'P000707', 'construction', 'A holomorphic structure on the pulled-back bundle',
     r'The direction from a connection to an algebraic bundle is indicated by \(\xi\mapsto f^*\xi\), followed by the notice that details will be given next time. Triviality is specified to mean analytic, or complex, triviality.',
     r'The \((0,1)\)-part of the pulled-back connection defines a Dolbeault operator when its square vanishes. On twistor space, the appropriate half-flatness condition on the original four-dimensional curvature makes this \((0,2)\)-curvature vanish. Along each fiber the pullback is holomorphically trivial.',
     r'The Dolbeault operator, its integrability criterion and the construction of the holomorphic structure are supplied here; they are not a proof recorded on this page. The orientation convention is inherited from the preceding item.',
     fate=r'This is the forward construction of the correspondence identified by \citet[abstract]{atiyahward1977instantons}; the consulted publisher record alone does not supply a full proof. Its class-E chronology is conditional on the supplied 5 September 1977 catalogue date: the paper was received 31 May and published in June, while the unresolved manuscript heading appears to read 5/IV--77.',
     verification='publisher metadata checked', refs=['atiyahward1977instantons'], confidence='medium', area='Gauge theory and twistor geometry')
item(419, 'P000707', 'claim', 'The four-sphere has no complex structure',
     r'The notes observe that \(S^4\) is not a complex manifold, in contrast to its twistor space.',
     r'The smooth four-sphere admits no almost-complex structure, hence no integrable one. Indeed an almost-complex tangent bundle would have \(c_1=0\) because \(H^2(S^4;\mathbf Z)=0\), \(\int c_2=\chi(S^4)=2\), and \(p_1=c_1^2-2c_2\). But \(\int p_1=3\sigma(S^4)=0\), a contradiction.',
     r'The stronger almost-complex obstruction and the characteristic-class argument are explanatory reconstruction; no proof is recorded on the page.',
     fate='This is a classical topological obstruction, not a new consequence of the reported instanton construction. The argument above makes the precise scope of the remark independently checkable.',
     correctness='correct', match='none found', verification='indirect', area='Topology')
checkpoint()

# Record 421.
item(421, 'P000709', 'definition', 'Lattices in semisimple Lie groups',
     r'A discrete subgroup \(\Gamma\subset G\), with \(G\) connected semisimple and for simplicity centerless, is called a lattice when \(\nu(G/\Gamma)<\infty\), where \(\nu\) is induced by Haar measure.',
     r'A lattice in a locally compact unimodular group is a discrete subgroup whose quotient carries finite invariant measure. In a connected semisimple Lie group this definition applies because the group is unimodular. Compactness of the quotient is a stronger condition, called cocompactness or uniformity.',
     fate=r'The definition is the one used in \citet[\S1.1]{tits1977margulis}, a February 1976 exposition revised in April 1976 and printed in 1977.',
     correctness='correct', match='exact', refs=['tits1977margulis'], area='Lie groups and arithmetic lattices')
item(421, 'P000709', 'definition', 'Algebraic groups over a field and integral points',
     r'The notes define an algebraic subgroup of \(GL(n,\mathbf C)\), a \(k\)-group by equations over \(k\), and \(G(k)\). They warn that integral matrices form a group when contained in \(SL(n,\mathbf Z)\).',
     r'For a linear algebraic group \(\mathbf H\) defined over \(\mathbf Q\) and a fixed faithful rational representation, set \(\mathbf H(\mathbf Z)=\mathbf H(\mathbf Q)\cap GL_N(\mathbf Z)\). Here \(GL_N(\mathbf Z)\) means matrices whose inverses also have integer entries, equivalently determinant \(\pm1\). Merely intersecting \(GL_N(\mathbf C)\) with integer-entry matrices is insufficient.',
     r'Distinct symbols \(\mathbf H\) and \(G\) avoid the notebook\textquoteright s reuse of one letter for an algebraic group and a real Lie group.',
     fate=r'\citet[Introduction and \S2]{borelharishchandra1962arithmetic} gives this rational/integral setup; the opened Russian translation is from 1964, of the 1962 original.',
     correctness='correct', match='exact', refs=['borelharishchandra1962arithmetic'], area='Lie groups and arithmetic lattices')
item(421, 'P000709', 'definition', 'Arithmetic subgroups and commensurability',
     r'A subgroup commensurable with \(G(\mathbf Z)\) is arithmetic. For a general real Lie group, the notes use an epimorphism from the real points of a \(\mathbf Q\)-group with compact kernel.',
     r'Two subgroups are commensurable if their intersection has finite index in each. For the semisimple Lie groups in this talk, arithmeticity means commensurability with the image of integral points of a suitable semisimple \(\mathbf Q\)-group under a continuous surjection on real points with compact kernel, allowing the standard finite-center identifications.',
     r'Semisimplicity and the finite-center convention are kept explicit; the following finite-volume conclusion is not true for arbitrary algebraic groups with rational characters.',
     fate=r'Compare \citet[\S2.1]{tits1977margulis} for the restriction-of-scalars and finite-center formulation. Arithmeticity is independent of the integral model up to commensurability.',
     correctness='correct', match='exact', refs=['tits1977margulis'], area='Lie groups and arithmetic lattices')
item(421, 'P000710', 'theorem', 'Finite covolume of arithmetic subgroups',
     r'The notes cite Borel--Harish-Chandra for the statement that an arithmetic subgroup has finite covolume.',
     r'If \(\mathbf H\) is a semisimple algebraic group defined over \(\mathbf Q\), then \(\mathbf H(\mathbf Z)\) is a lattice in \(\mathbf H(\mathbf R)\). More generally, the connected rational-character obstruction must vanish; the semisimple case automatically satisfies that condition. Commensurable subgroups and compact-kernel images preserve the relevant finite-volume property.',
     r'The general algebraic-group qualification prevents reading this as a theorem for \(\mathbf G_m(\mathbf Z)\subset\mathbf G_m(\mathbf R)\), which has infinite covolume.',
     fate=r'\citet[Thms.~7.8 and 9.4]{borelharishchandra1962arithmetic} proves precisely these statements. Both theorem statements and the semisimple proof were read in the Russian translation.',
     match='exact', refs=['borelharishchandra1962arithmetic'], area='Lie groups and arithmetic lattices')
item(421, 'P000710', 'theorem', 'The lattice SL(n,Z) and the modular-area exercise',
     r'\(SL(n,\mathbf Z)\) is given as an example. The audience is asked to check \(n=2\) by calculating a hyperbolic triangle\textquoteright s area.',
     r'\(SL_n(\mathbf Z)\) is a lattice in \(SL_n(\mathbf R)\). For \(PSL_2(\mathbf Z)\) acting on the upper half-plane with curvature \(-1\), the standard fundamental region \(\{|\operatorname{Re}z|\leq\tfrac12,\ |z|\geq1\}\) has area \(\pi/3\). Its finite area, together with the compact stabilizer \(SO(2)\), gives finite Haar covolume.',
     r'The region and normalization are supplied. It is a union of two reflection triangles of area \(\pi/6\), so the triangle drawn in the notes need not itself be a fundamental domain for the orientation-preserving group.',
     fate=r'This is a classical special case of \citet[Thm.~7.8]{borelharishchandra1962arithmetic}. The exercise is solved by \(\int_{-1/2}^{1/2}(1-x^2)^{-1/2}\,dx=\pi/3\); no modern research problem remains.',
     correctness='correct', match='exact', refs=['borelharishchandra1962arithmetic'], area='Lie groups and arithmetic lattices')
item(421, 'P000710', 'definition', 'Irreducibility of a lattice',
     r'A lattice is reducible if, for a nontrivial decomposition \(G=G_1\times G_2\), the product \((G_1\cap\Gamma)\times(G_2\cap\Gamma)\) has finite index in \(\Gamma\).',
     r'For a semisimple group with finite center and no compact factors, irreducibility means that no decomposition into two positive-dimensional normal factors splits the lattice into a product up to finite index. Passing to the adjoint group removes finite central overlaps. Equivalently, projections to proper factor quotients are dense in the usual irreducible-lattice setting.',
     r'The finite-center convention distinguishes a direct product from an almost-direct product.',
     fate=r'The finite-index definition appears in \citet[\S1.1]{tits1977margulis}; the notebook uses its centerless version.',
     correctness='correct', match='exact', refs=['tits1977margulis'], area='Lie groups and arithmetic lattices')
item(421, 'P000710', 'conjecture', 'The overly broad arithmeticity conjecture outside PSL(2,R)',
     r'A historical conjecture attributed to Selberg says that every irreducible lattice is arithmetic except in \(PSL_2(\mathbf R)\). The notes immediately mention counterexamples of Makarov and Vinberg in real hyperbolic groups.',
     r'The literal all-groups assertion is false: rank-one real hyperbolic groups beyond \(PSL_2(\mathbf R)\) admit nonarithmetic lattices. The valid higher-rank theorem requires real rank at least two, irreducibility, finite center and no compact factors.',
     r'The notebook itself retracts the broad formulation through its counterexamples; this is not classified as a conjecture still open in 1977.',
     fate=r'\citet[\S2.2]{tits1977margulis} records the Makarov--Vinberg examples in dimensions three and four and states the correctly restricted Selberg--Piatetski-Shapiro conjecture. The notebook\textquoteright s additional dimension-five attribution was not checked in an original construction.',
     status='As of November 2026, the displayed broad conjecture remains false; it is historical context for higher-rank arithmeticity and the separately indexed rank-one remainder.',
     correctness='false as written', match='partial', refs=['tits1977margulis'], confidence='medium', area='Lie groups and arithmetic lattices')
item(421, 'P000710', 'theorem', 'Margulis arithmeticity in higher real rank',
     r'The answer is that every irreducible lattice is arithmetic when \(\operatorname{rank}G\geq2\). The notes point to an appendix to Raghunathan\textquoteright s book for a proof.',
     r'Let \(G\) be a connected semisimple real Lie group with finite center, without compact factors, and with \(\operatorname{rank}_{\mathbf R}G\geq2\). Then every irreducible lattice in \(G\) is arithmetic.',
     r'Real rank and the structural hypotheses already present or inserted elsewhere on the pages are brought together. The unspecified edition of Raghunathan\textquoteright s book is not treated as an independently verified bibliographic citation.',
     fate=r'\citet[Thm.~1]{tits1977margulis} already reported the full theorem in February 1976. The nonuniform real case had been published by \citet[main arithmeticity result]{margulis1974arithmetic} in 1974; that paper alone is not evidence for the full cocompact case.',
     status=r'As of November 2026, this is Margulis\textquoteright s established arithmeticity theorem. Class E records circulation before this talk, even though some complete expositions appeared later.',
     match='exact', refs=['tits1977margulis','margulis1974arithmetic'], area='Lie groups and arithmetic lattices')
item(421, 'P000710', 'claim', 'Rigidity and the special role of surface lattices',
     r'The notes say that parameters occur only for \(SL_2(\mathbf R)\), while in the other cases there is rigidity, attributed to Selberg and Weil.',
     r'For cocompact lattices in semisimple real Lie groups, the familiar local-rigidity theorem excludes an \(SL_2(\mathbf R)\) factor in the relevant irreducible case. Finite-volume strong rigidity and local rigidity of arbitrary representations are different statements: nonuniform hyperbolic three-manifold groups can deform in \(PSL_2(\mathbf C)\) through representations that cease to be lattices.',
     r'The notebook does not distinguish deformations through lattices from deformations in the full representation variety. Its slogan cannot be used as the latter unrestricted assertion.',
     fate=r'Local rigidity recurs from earlier items 1964-8.1--1964-8.2 and 1966-93.1. \citet[\S2.2]{tits1977margulis} uses the surface-moduli contrast for arithmeticity, but does not validate every possible reading of the slogan.',
     match='thematic only', verification='indirect', refs=['tits1977margulis'], confidence='medium', area='Lie groups and arithmetic lattices')
item(421, 'P000710', 'claim', 'Algebraic coefficients after conjugation',
     r'As a consequence of rigidity, every lattice in \(SL(n,\mathbf R)\) is said to be conjugate to one with algebraic coefficients; no lower bound on \(n\) is written.',
     r'For \(n\geq3\), a lattice in \(SL_n(\mathbf R)\) can be conjugated to a group of matrices over a number field contained in \(\mathbf R\). The claim fails without qualification for \(n=2\): continuously varying surface lattices can have transcendental conjugacy-invariant traces.',
     r'The missing hypothesis \(n\geq3\) is substantive, not a change to the scan. The number-field statement uses finite generation in addition to algebraicity of individual entries.',
     fate=r'The algebraic-definition step is part of the deduction of arithmeticity discussed in \citet[\S5]{tits1977margulis}. Its unqualified formulation in the notebook must be restricted before use.',
     correctness='false as written', match='partial', refs=['tits1977margulis'], area='Lie groups and arithmetic lattices')
item(421, 'P000711', 'theorem', 'The archimedean superrigidity assertion',
     r'The main lemma assumes real rank at least two, an irreducible lattice and no compact factors, all explicitly inserted in the manuscript. If \(T:\Gamma\to GL(n,k)\) has connected simple Zariski closure and non-relatively-compact image, then for \(k=\mathbf R,\mathbf C\) it extends to \(G\).',
     r'In the standard superrigidity formulation, an unbounded Zariski-dense homomorphism of an irreducible higher-real-rank lattice into a connected adjoint simple group over an archimedean local field extends continuously to the ambient real Lie group, with the standard finite-cover and finite-index qualifications when working with nonadjoint groups or finite central twists.',
     r'The target-adjoint or finite-central qualifications are added; the stronger unqualified extension to the precise matrix representation need not follow without them.',
     fate=r'\citet[Thm.~2, \S3]{tits1977margulis} reports superrigidity before the talk. Its statement, rather than a metadata-only attribution, was read.',
     match='exact', refs=['tits1977margulis'], area='Lie groups and arithmetic lattices')
item(421, 'P000711', 'theorem', 'The nonarchimedean compactness assertion',
     r'For \(k=\mathbf Q_p\), the same main lemma says that connected simple Zariski closure and noncompact image are incompatible. The opening definition of local field also includes finite extensions of \(\mathbf Q_p\).',
     r'For a characteristic-zero nonarchimedean local field \(k\), a Zariski-dense homomorphism of the same irreducible higher-real-rank lattice into a connected adjoint simple \(k\)-group has relatively compact image. Noncompactness would force a continuous extension from connected \(G\) to a totally disconnected target, which is impossible.',
     r'The result applies to finite extensions of \(\mathbf Q_p\) as well, and the central/finite-index conventions are the same as in the preceding item.',
     fate=r'This is the nonarchimedean consequence of \citet[Thm.~2 and \S5]{tits1977margulis}; it was already part of the 1976 report.',
     match='exact', refs=['tits1977margulis'], area='Lie groups and arithmetic lattices')
item(421, 'P000711', 'method', 'From local compactness to arithmeticity',
     r'Put \(\Gamma\) in matrices over a number field, list the finitely many primes in denominators of generators, and use relative \(p\)-adic compactness to bound all denominators. The notes conclude arithmeticity.',
     r'After obtaining a number field of definition, one must use its completions \(K_v\), not only \(\mathbf Q_p\), and control all archimedean embeddings. Boundedness at finite places gives preservation of suitable local lattices; restriction of scalars combines the embeddings into a rational algebraic group, whose unwanted archimedean factors are compact. This yields an ambient arithmetic lattice, and finite covolume then gives the required finite index.',
     r'The displayed denominator argument is one step of the proof. Integral containment alone, without the other archimedean factors and finite-index step, is not arithmeticity.',
     fate=r'\citet[\S5]{tits1977margulis} explains the deduction. The source sketch is recognizable but omits exactly the global-field steps listed here.',
     match='partial', refs=['tits1977margulis'], area='Lie groups and arithmetic lattices')
rank_problem_item = item(421, 'P000710', 'question', 'The arithmeticity problem in the remaining rank-one groups',
     r'After real hyperbolic counterexamples and the higher-rank theorem, the notes say that in the other rank-one groups the answer is unknown.',
     r'The historical question is which real-rank-one simple groups admit nonarithmetic lattices. A precise surviving subquestion is: for which integers \(n\geq4\), if any, does \(PU(n,1)\) contain a nonarithmetic lattice?',
     r'The \(PU(n,1)\), \(n\geq4\), formulation is the modern remainder of the broader question, not a verbatim question confined to complex hyperbolic groups in the notebook.',
     cls='C', fate=r'Real hyperbolic groups in every dimension admit nonarithmetic lattices; quaternionic hyperbolic groups of quaternionic dimension at least two and the Cayley hyperbolic group have arithmetic lattices only. \citet[\S2.1]{parker2009lattices} surveys these resolutions. \citet[Introduction]{falbelpasquinelli2023hybrid} explicitly retains the complex-hyperbolic question for \(n\geq4\), while discussing constructions in dimensions two and three.',
     status=r'As of 10 November 2026, the search found no resolution of existence of nonarithmetic lattices in \(PU(n,1)\) for any \(n\geq4\). The introduction of \citet{yu2026mirror}, submitted 30 October 2026, still describes known examples as occurring only in dimensions two and three; its new example is in \(PU(2,1)\). This is a current research statement plus a dated search, not proof that an unlocated solution cannot exist.',
     correctness='correct', match='partial', verification='read the result', problem='GP-1977-01',
     worth='This is a precise and important surviving problem, but no bounded contribution is attempted here: producing a new lattice or an arithmeticity obstruction requires substantially more than the notebook supplies.',
     refs=['parker2009lattices','falbelpasquinelli2023hybrid','yu2026mirror'], confidence='medium', area='Lie groups and arithmetic lattices')
problems.append(dict(id='GP-1977-01', title='Nonarithmetic lattices in complex hyperbolic dimension at least four',
                     statement=r'For which \(n\geq4\), if any, is there a nonarithmetic lattice in \(PU(n,1)\)? This is the modern unresolved part of the notebook\textquoteright s broader rank-one arithmeticity question.',
                     occurrences=[rank_problem_item], status=r'As of 10 November 2026, open in the literature located. The 2023 paper explicitly states the question for \(n\geq4\), and the introduction of \citet{yu2026mirror}, first submitted 30 October 2026, still reports known examples only in dimensions two and three. No higher-dimensional solution was found.',
                     status_date='2026-11', refs=['parker2009lattices','falbelpasquinelli2023hybrid','yu2026mirror']))
checkpoint()

# Record 423; record 422 is a heading, without duplicated items.
item(423, 'P000712', 'definition', 'Curvature in a local gauge',
     r'For matrix functions \(A_\mu\) of four variables the notes write \(F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu+[A_\mu,A_\nu]\).',
     r'In a local trivialization of a smooth vector bundle, write \(D_\mu=\partial_\mu+A_\mu\). Then \([D_\mu,D_\nu]\) acts by multiplication by \(F_{\mu\nu}\), the displayed curvature matrix. For a unitary connection the matrices \(A_\mu\) are skew-Hermitian in a unitary frame.',
     fate=r'This is the coordinate form of the connection in record 419 and the setup identified in \citet[abstract]{atiyahward1977instantons}.',
     correctness='correct', match='partial', verification='publisher metadata checked', refs=['atiyahward1977instantons'], area='Gauge theory and twistor geometry')
item(423, 'P000712', 'definition', 'The coordinate self-duality and Yang-Mills equations',
     r'The notes display \(F_{ij}=\tfrac12\varepsilon_{ijk\ell}F_{k\ell}\) and \([\partial_\mu+A_\mu,F_{\mu\nu}]=0\).',
     r'In oriented orthonormal Euclidean coordinates, self-duality is \(F_{ij}=\frac12\sum_{k,\ell}\varepsilon_{ijk\ell}F_{k\ell}\). The Yang--Mills equation is \(\sum_\mu D_\mu F_{\mu\nu}=0\), where \(D_\mu F=\partial_\mu F+[A_\mu,F]\). On a curved four-manifold these are \(*F=F\) and \(d_A^*F=0\), with the metric divergence understood.',
     r'The repeated-index summation and the local orthonormal-frame/curved-space distinction are supplied. A plain partial-derivative divergence cannot be used in arbitrary coordinates on \(S^4\).',
     fate=r'These are the local equations underlying the earlier instanton report; \citet[abstract]{atiyahward1977instantons} confirms the subject but is not cited as an exact source for this coordinate transcription.',
     match='partial', verification='publisher metadata checked', refs=['atiyahward1977instantons'], area='Gauge theory and twistor geometry')
item(423, 'P000712', 'theorem', 'Self-duality implies the Yang-Mills equation',
     r'The self-duality and Yang--Mills equations are displayed in succession; their implication is not proved on the page.',
     r'For a smooth connection on an oriented Riemannian four-manifold, \(*F_A=\pm F_A\) implies \(d_A^*F_A=0\). Indeed the Bianchi identity gives \(d_AF_A=0\), and \(d_A^*F_A=-*d_A*F_A=\mp*d_AF_A=0\).',
     r'The implication and its one-line proof are explanatory reconstruction of the juxtaposed equations, not an additional attributed proof by Drinfeld.',
     fate=r'This standard curvature identity explains why the self-dual fields in \citet[abstract]{atiyahward1977instantons} solve Yang--Mills; no separate research claim is extracted.',
     correctness='correct', match='partial', verification='indirect', refs=['atiyahward1977instantons'], area='Gauge theory and twistor geometry')
checkpoint()

# Record 420.
item(420, 'P000707', 'construction', 'Zero curvature for differential-operator evolution equations',
     r'The notes write \([\partial_y-L_1,\partial_t-L_2]=0\), where \(L_1,L_2\) are scalar or matrix ordinary differential operators in \(x\) of orders \(n,m\).',
     r'For differential operators with sufficiently differentiable coefficients in \((x,y,t)\), the compatibility of \(\psi_y=L_1\psi\), \(\psi_t=L_2\psi\) is \(L_{1,t}-L_{2,y}+[L_1,L_2]=0\). Equality means that every coefficient of the differential operator vanishes.',
     r'The expanded sign convention and the regularity of coefficients are supplied. Matrix coefficients require attention to noncommutative multiplication but not a change in the compatibility identity.',
     fate=r'The construction predates the talk: \citet[pp.~291--294]{krichever1976zakharov} was received in October 1975 and published in 1976; \citet[\S1]{krichever1977methods} gives the spectral-curve construction. Earlier occurrence: 1975-379.1.',
     correctness='correct', match='exact', refs=['krichever1976zakharov','krichever1977methods'], area='Integrable systems')
item(420, 'P000707', 'claim', 'Quasiperiodic families, rational degenerations and soliton separatrices',
     r'The constructed solutions are described as generally conditionally periodic, with rational specializations; multisoliton KdV solutions form a separatrix-type family for \(u_t=6uu_x+u_{xxx}\).',
     r'Algebro-geometric scalar solutions associated with a smooth compact spectral curve are expressed through a theta function and linear motion on its Jacobian. For suitable real, nonsingular spectral data this gives smooth real quasiperiodic solutions. Singular degenerations can produce soliton or rational solutions, but arbitrary complex spectral data need not yield bounded real quasiperiodic solutions.',
     r'The reality and regularity conditions are essential additions. ``Separatrix'' is retained as a qualitative description of a degeneration, not as a proved global phase-space classification.',
     fate=r'\citet[\S1 and Appendix~2]{krichever1977methods} gives the theta-function and rational-degeneration constructions in a survey based on the earlier seminar program; the printed survey is 1977. The generic real-regular qualification is not stated in the notebook.',
     refs=['krichever1977methods'], area='Integrable systems')
item(420, 'P000707', 'definition', 'Algebraic type and an additional commuting operator',
     r'For an equation with no \(y\), the notes attribute to Manin a condition called algebraic type: there is \(L_3\) commuting with \(L_1\), with \(L_3\notin\mathbf C[L_1,L_2]\).',
     r'A standard finite-gap hypothesis for a scalar ordinary differential operator \(L\) is the existence of a positive-order differential operator \(M\) commuting with \(L\), not generated by \(L\) alone; suitable coprime-order or rank conditions determine the associated spectral data. In a Lax evolution \(L_t=[P,L]\), the time generator \(P\) need not commute with \(L\). Therefore \(\mathbf C[L_1,L_2]\) in the notebook cannot automatically be treated as a commutative spectral ring.',
     r'The standard commuting-ring formulation is a reconstruction, not a silent replacement of the literal condition. The notes do not specify which operators the notation \(\mathbf C[L_1,L_2]\) is intended to generate.',
     fate=r'\citet[Introduction and \S1]{krichever1978commutative} treats commuting rings and clarifies rank restrictions; it also warns of errors in the earlier arbitrary-rank description. Earlier related occurrences are 1975-374.2--1975-374.5, not a new precise Manin problem.',
     correctness='not determinable', match='partial', refs=['krichever1978commutative'], confidence='medium', area='Integrable systems')
item(420, 'P000707', 'construction', 'Spectral curves and genus under degeneration',
     r'The notes attach a curve through relations involving coefficients of fractional powers, say that its genus is generically constant and drops at special parameters, and box genus zero beside the multisoliton degeneration.',
     r'A commuting scalar differential-operator ring determines an affine algebraic spectral curve through polynomial relations among simultaneous eigenvalues. In a degeneration of such curves, the geometric genus of the normalization may fall; a flat family preserves arithmetic genus. Rational or multisoliton limits can have a rational normalization while the singular curve retains positive arithmetic genus.',
     r'The distinction between geometric and arithmetic genus is absent in the notes. No specific fractional-power coefficient relation is recorded, so the individual equation of the curve cannot be recovered.',
     fate=r'The spectral-curve and rational-limit mechanisms are discussed in \citet[\S1 and Appendix~2]{krichever1977methods}. This is a recognizable construction with compressed local details, not a theorem that all notions of genus decrease.',
     refs=['krichever1977methods'], area='Integrable systems')
item(420, 'P000707', 'theorem', 'Polynomial dependence of commuting scalar differential operators',
     r'The notes assert algebraic dependence of \(L_1,L_2\), with a tentative Jacobson attribution and a date in the 1930s.',
     r'For commuting ordinary scalar differential operators of positive order over a differential field of characteristic zero with constant field \(\mathbf C\), the usual Burchnall--Chaundy setting gives a nonzero polynomial \(R\in\mathbf C[X,Y]\) with \(R(L_1,L_2)=0\). This assertion is not true merely because \(L_1,L_2\) occur in a zero-curvature equation: they must commute in the stationary spectral problem.',
     r'The commutativity hypothesis and the distinction from the evolution generator are supplied. The notebook\textquoteright s historical attribution is not used as proof of priority.',
     fate=r'\citet[Introduction]{krichever1978commutative} explicitly traces the commuting-operator relation to Burchnall and Chaundy in the 1920s. Earlier occurrence: 1975-374.2. The exact role of the vaguely dated Jacobson reference was not identified.',
     refs=['krichever1978commutative'], area='Integrable systems')
item(420, 'P000708', 'theorem', 'Rational KdV solutions and many-particle pole dynamics',
     r'Airault, McKean and Moser are credited with replacing rational KdV evolution by an explicitly solvable system for the poles.',
     r'For a rational KdV solution decaying at spatial infinity, away from times with pole collisions the potential has double poles with prescribed leading coefficients, and substitution into KdV gives differential equations and algebraic constraints for their positions. With the notebook\textquoteright s sign convention \(u_t=6uu_x+u_{xxx}\), the principal part is \(-2(x-x_j)^{-2}\). The number of poles, counted in the generic configuration, is triangular in the standard rational KdV family.',
     r'The decay condition, generic-time qualification and sign of the principal part are supplied; the notebook gives no explicit pole equations. The sign follows by canceling the order-five pole in the displayed KdV equation.',
     fate=r'\citet[Appendix~2, pp.~205--207]{krichever1977methods} explicitly relates the rational KdV pole system to Airault--McKean--Moser and describes its constrained configurations. This exact section was read; the original Airault--McKean--Moser publisher copy was inaccessible in this run.',
     match='exact', refs=['krichever1977methods'], area='Integrable systems')
item(420, 'P000708', 'claim', 'Rationality implies a stationary higher KdV relation',
     r'The notes say that, for KdV, requiring rationality can replace the requirement of a third commuting operator.',
     r'Within the standard rational KdV class decaying at infinity, the associated Schr\"odinger operator belongs to the degenerate finite-gap family and admits an additional commuting differential operator; equivalently the potential satisfies a stationary equation in the higher KdV hierarchy. Rationality without the decay, hierarchy and operator-class qualifications is not the statement verified here.',
     r'The precise class is reconstructed from the printed rational KdV result, and is stated separately from the notebook\textquoteright s unqualified sentence.',
     fate=r'\citet[Appendix~2, pp.~205--207]{krichever1977methods} states the connection of rational solutions with stationary higher equations. This resolves the identifiable KdV claim; the universal extension in the next item is distinct.',
     match='exact', refs=['krichever1977methods'], area='Integrable systems')
item(420, 'P000708', 'conjecture', 'The proposed extension from KdV to every Lax equation',
     r'The final suggestion is that replacing the additional commuting operator by rationality is apparently possible for every Lax equation.',
     r'The notes do not specify the class of Lax pairs, coefficient fields, rationality variable, boundary behavior, permitted commuting operators or meaning of equivalence. There is therefore no determined universal assertion to compare with later theorems.',
     r'Restricting the sentence to rational KdV, rational KP, or a particular Calogero--Moser correspondence would create a different and much narrower problem.',
     cls='F', fate=r'The KdV result was located and read in \citet[Appendix~2]{krichever1977methods}. Searches for the broader rationality/commuting-operator formulation did not supply quantifiers missing from this occurrence; a later theorem on one hierarchy would not settle ``every Lax equation''.',
     status='As of November 2026, the intended universal class is unidentified. No new problem identifier is assigned to this underdetermined extrapolation.',
     correctness='not determinable', match='thematic only', verification='unresolved lead', development='none', refs=['krichever1977methods'], confidence='low', area='Integrable systems')
checkpoint()

# Record 424.
item(424, 'P000713', 'problem', 'A known lighter counterfeit among 27 coins',
     r'Gelfand asks for the counterfeit among 27 coins in three weighings when it is known to be lighter.',
     r'Assume exactly one coin is lighter and all others have the same mass. An ideal balance has three outcomes. Comparing equal groups of nine locates the group containing the counterfeit; repeat with groups of three and then single coins. In general \(3^r\) coins can be handled in \(r\) weighings, and the ternary decision-tree bound proves optimality.',
     r'The assumptions on exactly one counterfeit and an ideal balance are stated explicitly; the recursive construction and counting lower bound are supplied.',
     fate=r'This is a classical weighing puzzle, part of the subject of \citet[pp.~231--234]{dyson1946pennies}. Only Dyson\textquoteright s publication metadata was accessible; the elementary argument above independently checks this occurrence.',
     correctness='correct', match='thematic only', verification='publisher metadata checked', refs=['dyson1946pennies'], area='Combinatorics and information theory')
item(424, 'P000713-P000714', 'problem', 'Thirteen coins when only the counterfeit identity is required',
     r'The unknown-sign version is answered by 13 coins in three weighings, then by \((3^N-1)/2\) coins in \(N\) weighings. The proposed first weighing is four against four, leaving five.',
     r'With exactly one counterfeit, no externally supplied genuine coin, equal coin counts on the pans, and only its identity required, \((3^N-1)/2\) coins are achievable and optimal for \(N\geq1\). If both identity and heavier/lighter sign are required, the capacity is \((3^N-3)/2\). For \(N=3\), the respective answers are 13 and 12.',
     r'The Russian says to find the coin and does not require its sign. A balanced ternary code with 12 nonzero columns and a thirteenth zero column verifies the literal 13-coin reading. All-balance outcomes identify coin 13 but leave its sign undetermined. The general construction and bound are explained in the supplementary annotation, and the supplied code enumerates all signed hypotheses for \(N=1,\ldots,6\).',
     fate=r'The classical literature includes \citet[pp.~231--234]{dyson1946pennies}; its full proof was not available in the publisher copy. This chapter\textquoteright s code and elementary reconstruction check the exact convention independently. No correction from 13 to 12 is warranted without changing the required output.',
     correctness='correct with missing hypotheses', match='partial', verification='publisher metadata checked', refs=['dyson1946pennies'], area='Combinatorics and information theory')
item(424, 'P000714', 'method', 'Choosing informative three-outcome weighings',
     r'The algorithm is to divide the coins so that the entropy of the piles is equal, dividing the entropy into three equal parts and avoiding exhaustive search.',
     r'For a deterministic observation \(Y\) with three possible outcomes, information gained about the hidden hypothesis \(X\) is \(I(X;Y)=H(Y)\leq\log3\). Equality requires three equally likely outcomes. Thus one seeks a physically feasible weighing that balances posterior probability mass, not three literally equal entropy values or necessarily equal numbers of coins.',
     r'For 13 equally likely counterfeit identities with equally likely signs, the initial four-versus-four weighing has signed branch counts \(8,8,10\), not three equal counts. Entropy maximization is a guiding criterion; it does not by itself prove a complete weighing algorithm exists.',
     fate=r'\citet[\S6, properties 2, 3 and 5]{shannon1948communication} supplies the entropy bound and conditional-entropy identity. The application to the constrained weighing experiment is reconstruction.',
     correctness='correct with missing hypotheses', match='partial', refs=['shannon1948communication'], area='Combinatorics and information theory')
item(424, 'P000714', 'definition', 'Shannon entropy and the binary sign error',
     r'The binary formula is written \(S=p\ln p+q\ln q\), while the following general formula is \(-\sum_i p_i\ln p_i\). For equiprobable outcomes the notes obtain \(S=\ln N\).',
     r'For a finite probability distribution, \(H(p)=-\sum_i p_i\log p_i\), with \(0\log0=0\). Thus \(H(p,1-p)=-p\log p-(1-p)\log(1-p)\), and \(H\) is maximized at the uniform distribution, where \(H=\log N\). Natural logarithms give nats.',
     r'The minus sign in the binary expression is absent in the scan as well as the transcription. It is a faithful notebook error, not an English translation error.',
     fate=r'\citet[\S6, Thm.~2 and property 2]{shannon1948communication} already gives the characterization and maximum. The formula and sign were checked in the scanned source and against the printed entropy properties.',
     correctness='false as written', match='exact', refs=['shannon1948communication'], area='Combinatorics and information theory')
item(424, 'P000714', 'claim', 'Additivity and conditional information',
     r'The notes appeal to additivity and identify information with a change of entropy, writing \(\Delta I=-\ln(N_f/N_i)\).',
     r'Independent finite random variables satisfy \(H(X,Y)=H(X)+H(Y)\); in general \(H(X,Y)=H(X)+H(Y\mid X)\). The expected information supplied by an observation is \(I(X;Y)=H(X)-H(X\mid Y)\). The displayed count formula equals this entropy reduction on a branch only when the prior and posterior possibilities are uniform over sets of sizes \(N_i,N_f\).',
     r'Independence, conditional probabilities and the uniformity qualification are supplied. Information gain is not an unconditional identity with an arbitrarily signed physical entropy change.',
     fate=r'\citet[\S6, properties 3 and 5--6]{shannon1948communication} gives the identities. Earlier seminar entropy occurrences include 1964-10.1 and 1966-107.4, with different physical emphases.',
     match='exact', refs=['shannon1948communication'], area='Combinatorics and information theory')
checkpoint()

# Record 425.
item(425, 'P000713; P000716', 'claim', 'Temperature can change a broken-symmetry phase',
     r'The opening connects the return of field theory with spontaneous symmetry breaking, macroscopic influences and cosmic history. The closing drawings show an evolving potential well as temperature changes.',
     r'A precise illustrative model is \(V_T(\phi)=\tfrac12 m^2(T)\phi^2+\tfrac\lambda4\phi^4\), \(\lambda>0\). If \(m^2(T)>0\), its unique minimum is \(0\); if \(m^2(T)<0\), the minima are \(\pm\sqrt{-m^2(T)/\lambda}\). Thus a temperature-dependent effective potential can change the symmetry of its minimizing state. No assertion that every theory restores symmetry at high temperature follows.',
     r'The polynomial potential, parameter and explicit minima are an illustrative reconstruction; neither this formula nor a critical temperature is written in the notes.',
     fate=r'The subject predates the talk in \citet{kirzhnitslinde1972macroscopic}. The author-institution publication record and publisher bibliographic search were checked, but the full article was inaccessible, so the drawings are matched thematically, not to a particular theorem.',
     match='thematic only', verification='publisher metadata checked', refs=['kirzhnitslinde1972macroscopic'], confidence='medium', area='Statistical physics and gravitation')
item(425, 'P000713', 'claim', 'Dynamical instability and loss of coarse information',
     r'A region in phase space spreads because of instability, with Sinai billiards and positive entropy as examples; the notes describe this as losing information.',
     r'For a Hamiltonian flow preserving Liouville measure, the fine-grained Gibbs entropy of an absolutely continuous density is invariant under exact evolution. Instability can make a set highly stretched and fine-scaled, so information at finite observational resolution can be lost and a coarse-grained entropy can grow. Positive metric entropy is a property of a specified invariant dynamical system, not a consequence of every instability.',
     r'The distinction between fine-grained conservation and coarse-grained loss is supplied. The page does not specify a billiard geometry or a partition and therefore does not support a new billiard theorem.',
     fate='This is a classical dynamics-to-statistics motivation. Earlier items 1964-10.1 and 1964-10.4 already distinguish metric entropy and information-forgetting language. The claimed loss is valid only after an observational coarse graining is chosen.',
     correctness='correct with missing hypotheses', match='none found', verification='indirect', area='Dynamical systems and entropy')
item(425, 'P000713', 'definition', 'Boltzmann entropy of a macrostate',
     r'A macrostate is fixed by a small number of parameters but allows many microscopic configurations; the notes write \(S=\ln N_{\rm micro}\).',
     r'For a finite set of \(W\) equiprobable microstates compatible with specified macroscopic constraints, \(S=k_B\log W\). For a continuous phase space one needs a reference measure and coarse-graining convention; a raw cardinality is not finite. The notebook uses units \(k_B=1\).',
     r'Equiprobability, the entropy unit and the continuous-state qualification are explicit additions.',
     fate=r'This is the equiprobable case of the information-theoretic entropy discussed in \citet[\S6]{shannon1948communication}; its thermodynamic application long predates the talk. Earlier occurrence: 1964-9.3.',
     match='partial', refs=['shannon1948communication'], area='Statistical physics and gravitation')
item(425, 'P000714', 'claim', 'Ideal-gas expansion and the entropy-information sign',
     r'Kirzhnits writes \(\Delta S=-\Delta I\), draws a gas expanding into a larger volume, and gives \(S=\ln(V/N)\) per molecule. The final sentence says that acquiring information decreases information.',
     r'For an ideal gas at fixed particle number and temperature, the volume-dependent entropy change per particle is \(\Delta S/N=k_B\log(V_f/V_i)\). In particular doubling accessible volume gives \(k_B\log2\). The full entropy also contains temperature, normalization and additive terms. If information is defined as a reduction of uncertainty in the same statistical model, its dimensionless change is opposite to the entropy change.',
     r'The formula in the notes is only the volume contribution. The last sentence should say that acquiring information decreases entropy or uncertainty; the scan faithfully contains the wrong repeated word.',
     fate=r'The information/entropy convention is clarified by \citet[\S6]{shannon1948communication}; the one-molecule gas comparison is developed explicitly in \citet[Fig.~12 and accompanying discussion]{bennett1982thermodynamics}. The gas entropy law itself is pre-1977 exposition.',
     correctness='false as written', match='partial', refs=['shannon1948communication','bennett1982thermodynamics'], area='Statistical physics and gravitation')
item(425, 'P000714', 'remark', 'Maxwell\u2019s demon and the entropy of the whole apparatus',
     r'Maxwell\textquoteright s demon lowers entropy by following the particles.',
     r'An informed controller can reduce a subsystem\textquoteright s entropy by sorting particles or extracting work, but the complete cyclic process must include the controller\textquoteright s memory and its reset. A subsystem entropy decrease alone is not a violation of the second law for an isolated total system.',
     r'The memory, cyclic-operation and total-system qualifications are absent in the notebook. No universal claim that every measurement itself dissipates \(k_BT\log2\) is inserted.',
     fate=r'\citet[discussion of Maxwell\textquoteright s demon, especially Fig.~12]{bennett1982thermodynamics}, received in 1981 and published in 1982, distinguishes reversible measurement from resetting a record. It is a later clarification of a much older thought experiment, not the first appearance of the notebook\textquoteright s remark.',
     match='partial', refs=['bennett1982thermodynamics'], area='Statistical physics and gravitation')
item(425, 'P000714-P000715', 'definition', 'A black-hole horizon as a causal barrier',
     r'The notes ask for forces that keep information in a region, name gravity because it is long-range and of one sign, and describe a black hole as a body that releases no information.',
     r'In an asymptotically flat spacetime with future null infinity \(\mathcal I^+\), the black-hole region is \(M\setminus J^-(\mathcal I^+)\), and its future boundary is the event horizon. Future-directed causal signals from this region cannot reach \(\mathcal I^+\). This is a statement about the causal metric, not a theorem deduced merely from the range and sign of a force.',
     r'The global causal definition is supplied. Gravity\textquoteright s claimed uniqueness and always-attractive character are heuristic motivations, not hypotheses sufficient for the existence of an event horizon.',
     fate=r'The classical causal setting and its difference from quantum emission are explicit in \citet[\S1]{hawking1975particle}. The report\textquoteright s black-hole description is recognizable once restricted to classical signals.',
     match='partial', refs=['hawking1975particle'], area='Statistical physics and gravitation')
item(425, 'P000714-P000715', 'claim', 'The Schwarzschild radius and the incorrect solar value',
     r'Equating Newtonian escape speed to \(c\) gives \(R=2\gamma M/c^2=r_g\). The notes say this survives in exact theory and give seven kilometers for a solar mass.',
     r'For the Schwarzschild solution with mass \(M\), the event-horizon areal radius is \(r_s=2GM/c^2\). The Newtonian escape-speed argument reproduces the expression but does not derive relativistic causal structure. Using the nominal solar mass parameter \(GM_\odot=1.3271244\times10^{20}\,{\rm m^3s^{-2}}\) gives \(r_s\simeq2.95325\,{\rm km}\), rather than seven kilometers.',
     r'The nonrotating, uncharged solution and the meaning of areal radius are specified. Seven is visible in the scan, so this is a faithful numerical notebook error. The quoted ordinary solar radius \(10^6\,{\rm km}\) is only an order-of-magnitude estimate.',
     fate=r'The modern constant is verified in \citet[Table~1]{prsa2016nominal}; the radius is a direct substitution into the notebook\textquoteright s own formula. The classical Schwarzschild setting is also used in \citet[\S2]{hawking1975particle}.',
     correctness='false as written', match='partial', refs=['prsa2016nominal','hawking1975particle'], area='Statistical physics and gravitation')
item(425, 'P000715', 'claim', 'The limited no-hair statement and the missing angular momentum',
     r'Only a few parameters of a black hole can be known: mass, charge and radius.',
     r'A precise established uniqueness theorem assumes a four-dimensional, stationary, asymptotically flat, analytic electrovacuum spacetime, the usual global regularity condition, and a connected nondegenerate horizon. Its domain of outer communications is Kerr--Newman. The family is parameterized by mass, angular momentum and charge; the horizon radius or area is derived, not an independent substitute for angular momentum.',
     r'The field equations, asymptotics, stationarity and regularity are reconstructed. There are other matter theories and other asymptotics with black-hole hair, so the sentence is not a universal information-counting theorem.',
     fate=r'\citet[Thm.~3.3]{chruscielcostaheusler2012stationary} gives the precise theorem read here, including the alternative rotating-horizon assumption. The no-hair program was already established before the seminar, but the notebook omits both angular momentum and the theorem\textquoteright s scope.',
     correctness='false as written', match='partial', refs=['chruscielcostaheusler2012stationary'], area='Statistical physics and gravitation')
item(425, 'P000715', 'theorem', 'Classical increase of event-horizon area',
     r'Hawking is credited with the assertion that the black-hole surface \(S\) increases in every process; merging two holes is presented as geometrically evident from the radius formula.',
     r'In classical general relativity, with the null energy condition and the global predictability/regularity assumptions needed to exclude future endpoints or exposed singularities of horizon generators, the event-horizon area cannot decrease toward the future. For a merger this concerns the final area compared with the sum of initial component areas. The radius formula alone does not prove the merger inequality, because energy can escape as radiation.',
     r'The energy and causal hypotheses, and the distinction between classical area and generalized quantum entropy, are added.',
     fate=r'\citet{hawking1971colliding} published the collision application in May 1971; only its abstract and metadata were read here. \citet[abstract and \S1]{hawking1975particle} explicitly explains that quantum emission can violate the classical area law. The quantum qualification therefore also predates this talk.',
     status=r'As of November 2026, the classical theorem is established under its stated hypotheses; the notebook\textquoteright s phrase every process is not valid for semiclassical evaporation.',
     match='partial', refs=['hawking1971colliding','hawking1975particle'], area='Statistical physics and gravitation')
item(425, 'P000715', 'claim', 'Area entropy, Hawking temperature and the generalized second law',
     r'The area symbol \(S\) motivates a thermodynamic analogy; Bekenstein is said to remove the quotation marks from black-hole temperature by counting inaccessible information. The parenthesis incorrectly calls him Hawking\textquoteright s student.',
     r'In semiclassical Einstein gravity, \(S_{\rm BH}=k_Bc^3A/(4G\hbar)\) and \(T_H=\hbar\kappa/(2\pi c k_B)\) when \(\kappa\) is physical surface acceleration. The generalized second law concerns \(S_{\rm outside}+S_{\rm BH}\). Bekenstein proposed area entropy and the generalized law; Hawking\textquoteright s radiation calculation fixed the temperature and the standard entropy coefficient.',
     r'The exact normalization and attribution are reconstructed from the publications. The causal information metaphor is not itself a microscopic derivation of the entropy in every theory of gravity.',
     fate=r'\citet[abstract]{bekenstein1973entropy} was received in November 1972 and published in April 1973. \citet[abstract]{hawking1976thermodynamics} states the temperature/entropy normalization before the seminar. \citet[recollection of their Princeton student years]{wald2015bekenstein} confirms that Bekenstein\textquoteright s supervisor was John Wheeler.',
     correctness='correct with missing hypotheses', match='partial', refs=['bekenstein1973entropy','hawking1976thermodynamics','wald2015bekenstein'], area='Statistical physics and gravitation')
item(425, 'P000715', 'claim', 'Comparing absorption of hot and cold bodies',
     r'A hot body thrown into a black hole is said to increase its area more than a cold body, in exact agreement with the increase in entropy.',
     r'For a quasistatic perturbation of a stationary hole, the first law is \(\delta(Mc^2)=\kappa c^2\delta A/(8\pi G)+\Omega_H\delta J+\Phi_H\delta Q\). At fixed angular-momentum and charge transfer, larger delivered energy gives larger area increase. Temperature or matter entropy alone does not determine the delivered energy, so the comparison needs specified bodies, trajectories and other conserved quantities.',
     r'The first-law formulation states precisely which comparison is justified; the unconditional hot-versus-cold rule is not a mathematical theorem.',
     fate=r'\citet[Eq.~(3.1)]{hawking1975particle} uses the classical first law in the radiation analysis. Bekenstein\textquoteright s generalized-law proposal \citep[abstract]{bekenstein1973entropy} concerns the combined entropy, not an equality between arbitrary matter entropy and horizon-area change.',
     correctness='correct with missing hypotheses', match='partial', refs=['hawking1975particle','bekenstein1973entropy'], area='Statistical physics and gravitation')
item(425, 'P000715', 'theorem', 'Hawking radiation and the thermal occupation factor',
     r'The notes attribute radiation to Hawking and write the Planck factor \((e^{\hbar\omega/(kT)}-1)^{-1}\); the preceding phrase about pairs is only schematic.',
     r'For a free bosonic field on an asymptotically collapsing geometry settling to a Schwarzschild black hole, the late-time outgoing occupation number has the thermal factor \((e^{\hbar\omega/(k_BT_H)}-1)^{-1}\), multiplied by the mode\textquoteright s transmission or greybody factor. Fermions have a plus sign in the denominator. This is a semiclassical result with a prescribed background and specified incoming vacuum.',
     r'The scattering factor, field statistics and semiclassical assumptions are supplied. A pair-creation cartoon is not the derivation, and the observed spectrum at infinity is not an exact unit-emissivity Planck spectrum in every mode.',
     fate=r'\citet[Eq.~(2.29) and the following fermion discussion]{hawking1975particle} was received in April 1975 and published in 1975. The exact occupation formula and its absorption factor were read in the full paper.',
     match='exact', refs=['hawking1975particle'], area='Statistical physics and gravitation')
item(425, 'P000715', 'remark', 'Causal inaccessibility versus quantum information loss',
     r'Information is said to be lost not through stochasticization but because it is mechanically cut off by the black hole.',
     r'The stated contrast concerns the exterior observer\textquoteright s causal access to the interior. It does not specify whether a complete quantum-gravitational evolution maps pure states to mixed states, what final state is compared, or which algebra of observables is used.',
     r'Promoting this sentence to the precise black-hole unitarity problem would introduce quantifiers and a quantum model not given in the notebook.',
     cls='F', fate=r'\citet[\S1]{hawking1975particle} supplies the nearby semiclassical setting, but the notes do not isolate a complete quantum-evolution conjecture. No exact open problem is inferred merely from the word information.',
     status='As of November 2026, this occurrence is identifiable as a physical motivation, but not as a definite quantum-information-loss assertion whose resolution can be tracked independently.',
     correctness='not determinable', match='thematic only', verification='unresolved lead', development='none', refs=['hawking1975particle'], confidence='medium', area='Statistical physics and gravitation')
item(425, 'P000715', 'construction', 'Uniform acceleration and a Rindler horizon',
     r'A uniformly accelerated observer in vacuum receives light only from part of space, described as half of space; a spacetime diagram accompanies the statement.',
     r'In Minkowski space, the eternal worldline \(ct=(c^2/a)\sinh(a\tau/c)\), \(x=(c^2/a)\cosh(a\tau/c)\) has constant proper acceleration \(a>0\). Its adapted stationary region is the right Rindler wedge \(x>|ct|\), bounded by null horizons. The events from which it can ever receive a signal form the causal past of the worldline; this is not simply a fixed Euclidean half-space at all times.',
     r'The eternal-acceleration assumption and distinction between the wedge and the entire causal past are supplied. This matters because a finite period of acceleration does not by itself produce the same eternal observer horizon.',
     fate=r'\citet[\S~II.B, Eqs.~(2.34)--(2.37)]{crispinohiguchimatsas2008unruh} gives the geometry; the original 1976 detector paper is \citet{unruh1976notes}.',
     match='partial', refs=['crispinohiguchimatsas2008unruh','unruh1976notes'], area='Statistical physics and gravitation')
item(425, 'P000715-P000716', 'theorem', 'The Unruh temperature and observer-dependent particles',
     r'The inertial vacuum is described as a ground state of the electromagnetic Hamiltonian; the accelerated observer is said to find a Planck distribution. The diagram labels \(kT=ha/c\), without a \(2\pi\) factor, and the ground-state equation uses different ket letters on its two sides.',
     r'For the Minkowski vacuum restricted to a Rindler wedge, the boost-time state is thermal in the KMS sense. An observer of constant proper acceleration \(a\) has \(T_U=\hbar a/(2\pi c k_B)\). For free bosonic Rindler modes the mean occupation is \((e^{\hbar\omega/(k_BT_U)}-1)^{-1}\). A detector\textquoteright s detailed balance is thermal, but its entire response need not equal that of an inertial detector in a Minkowski thermal bath.',
     r'The notation is standardized to reduced Planck\textquoteright s constant \(\hbar\); if the handwritten \(h\) means ordinary Planck\textquoteright s constant, the coefficient is instead \(h/(4\pi^2)\). The inertial ground-state equation must use the same vacuum vector on both sides.',
     fate=r'\citet[abstract]{unruh1976notes} appeared in August 1976. \citet[Eq.~(2.125), \S~II.I and Introduction]{crispinohiguchimatsas2008unruh} explicitly verifies the occupation factor, KMS statement and detector qualification; its preprint circulated in October 2007, before 2008 publication.',
     correctness='false as written', match='partial', refs=['unruh1976notes','crispinohiguchimatsas2008unruh'], area='Statistical physics and gravitation')
item(425, 'P000716', 'claim', 'The microwave background as evidence for a hot past',
     r'The notes ask why the universe is hot, quote roughly \(3\,\mathrm K\) from a Planckian cosmic radiation distribution, call it relic radiation, and say the universe is cooling.',
     r'The measured cosmic microwave background is a thermal radiation field. In a homogeneous expanding cosmology with collisionless propagation after thermalization, photon wavelengths scale with the scale factor \(a\), so a Planck spectrum remains Planckian with \(T\propto a^{-1}\). The notebook\textquoteright s \(3\,\mathrm K\) is a rough historical temperature, not an exact modern measurement.',
     r'The cosmological assumptions and redshift argument are supplied. A single-frequency antenna temperature is not itself a full measurement of a Planck spectrum.',
     fate=r'\citet[pp.~419--421]{penziaswilson1965antenna} reports the 1965 excess antenna temperature, with a May 1965 manuscript date, well before this seminar. That paper establishes the observational antecedent; it is not cited as a full-spectrum measurement or a derivation of cosmic initial conditions.',
     match='partial', refs=['penziaswilson1965antenna'], area='Statistical physics and gravitation')
item(425, 'P000716', 'question', 'Does a cosmological horizon explain the radiation temperature?',
     r'The question why the universe is hot is followed by an inaccessible region, the phrase event horizon, the explanation that light has not yet arrived, and an arrow suggesting that this accounts for the temperature.',
     r'Light not yet received from a cosmological region concerns a particle horizon; an event horizon concerns signals that can never be received in the future. Neither causal boundary alone fixes a microwave-background temperature. A horizon-temperature calculation requires a specified spacetime, quantum state and time normalization, none of which are given here.',
     r'The fragment cannot be uniquely identified with de Sitter temperature, a reheating mechanism, or a general explanation of cosmological initial entropy. These are distinct modern questions.',
     cls='F', fate=r'The nearby analogy to thermal horizons is discussed in \citet[Introduction]{crispinohiguchimatsas2008unruh}, but that does not identify this sketch with a particular cosmological theorem. The search found no exact formula whose hypotheses can be recovered from the page.',
     status='As of November 2026, the intended cosmological model and asserted temperature relation remain unidentified. No definite problem identifier is assigned.',
     correctness='not determinable', match='thematic only', verification='unresolved lead', development='none', refs=['crispinohiguchimatsas2008unruh'], confidence='low', area='Statistical physics and gravitation')
checkpoint()

# Record 426.
item(426, 'P000717', 'definition', 'The differential-polynomial algebra and its total derivative',
     r'The generators are \(u_k^{(i)}\), and \(A=K[u_k^{(i)}]\). The notes allow derivations given by infinite sums and define \(D=d/dx\) by \(D u_k^{(i)}=u_k^{(i+1)}\).',
     r'Over a field \(K\) of characteristic zero, let \(A\) be the polynomial algebra in the countably many jet variables, every polynomial involving only finitely many. Then \(D=\sum_{k,i}u_k^{(i+1)}\partial/\partial u_k^{(i)}\) is well defined. Likewise an arbitrary assignment of polynomial images to the generators determines a derivation; its displayed infinite sum acts finitely on each polynomial.',
     r'Characteristic zero is imposed for the subsequent variational identities. Infinite summation here is locally finite on polynomials and does not invoke analytic convergence.',
     fate=r'This formal setup is already explicit in \citet[\S1, pp.~13--14 of the Russian original]{gelfanddikii1977resolvent}, received in December 1976 and printed before the October 1977 talk.',
     correctness='correct with missing hypotheses', match='exact', refs=['gelfanddikii1977resolvent'], area='Integrable systems and variational calculus')
item(426, 'P000717', 'definition', 'Local functionals modulo total derivatives',
     r'The normalization is \(u_n=1\), \(u_{n-1}=0\), and the space of functionals is \(\widetilde A=A/DA\), with the quotient map denoted \(f\mapsto\int f\,dx\).',
     r'After imposing the differential relations \(u_n=1\), \(u_{n-1}=0\), the free dependent variables are \(u_0,\ldots,u_{n-2}\). The local-functional space \(\mathcal F=A/D(A)\) is a vector-space quotient. Integration by parts means \(\int fDg\,dx=-\int (Df)g\,dx\). In general \(D(A)\) is not an ideal, so \(\mathcal F\) is not naturally a quotient algebra.',
     r'The relations include derivatives of the normalized coefficients. The vector-space, rather than algebra, qualification is important for the later Lie bracket.',
     fate=r'\citet[\S1]{gelfanddikii1977resolvent} gives this exact definition and its periodic/rapidly decreasing interpretations; \citet[\S1]{gelfanddikii1978jets} reuses it in the later elementary calculus.',
     correctness='correct', match='exact', refs=['gelfanddikii1977resolvent','gelfanddikii1978jets'], area='Integrable systems and variational calculus')
item(426, 'P000717', 'problem', 'When does an identically zero local integral imply a total derivative?',
     r'The exercise asks whether \(\int_{\mathbf R}f[u(x)]\,dx=0\) for every Schwartz function is equivalent to \(f\in D\mathbf C[u]\).',
     r'Let \(A=\mathbf C[u_k^{(i)}:0\leq k\leq n-2,\ i\geq0]\), with no explicit \(x\), and assume the constant term \(f(0)\) is zero. Then \(\int_{\mathbf R}f[j^\infty u(x)]\,dx=0\) for every Schwartz tuple \(u\) if and only if \(f=Dg\) for some \(g\in A\). All evaluated nonconstant differential monomials are integrable under these hypotheses.',
     r'The tuple interpretation and zero constant term make the analytic integral well defined. Algebraically, vanishing of all Euler derivatives gives \(f\in\mathbf C+D(A)\); the constant must not be dropped. Integration by parts proves one direction, while arbitrary compactly supported variations and the one-dimensional variational homotopy give the converse.',
     fate=r'The periodic and Schwartz realizations and Euler-derivative lemma are discussed in \citet[\S1, pp.~13--14]{gelfanddikii1977resolvent}. Its printed shorthand for the kernel also requires separating constants. This is a classical null-Lagrangian exercise, not an undeveloped problem.',
     correctness='correct with missing hypotheses', match='exact', refs=['gelfanddikii1977resolvent'], area='Integrable systems and variational calculus')
item(426, 'P000717', 'construction', 'The Euler variational derivative',
     r'The map \(\delta/\delta u:\widetilde A\to A^{n-1}\) is given by \((\delta\widetilde f/\delta u)_k=\sum_{\ell\geq0}(-D)^\ell\partial f/\partial u_k^{(\ell)}\).',
     r'For each \(k\), define \(E_k(f)=\sum_{\ell\geq0}(-D)^\ell(\partial f/\partial u_k^{(\ell)})\). The sum is finite on every differential polynomial, and \(E_k(Dg)=0\), so the vector \(E(f)\) is independent of the chosen representative of \(\int f\,dx\). It is the coefficient of an arbitrary variation after integration by parts.',
     r'Finite support and well-definedness on the quotient are explained explicitly; the formula itself is faithfully transcribed.',
     fate=r'\citet[\S1, variational derivative and following theorem]{gelfanddikii1977resolvent} gives the definition and the integration-by-parts characterization. This is the same formal calculus continued in \citet[\S1]{gelfanddikii1978jets}.',
     correctness='correct', match='exact', refs=['gelfanddikii1977resolvent','gelfanddikii1978jets'], area='Integrable systems and variational calculus')
item(426, 'P000718', 'construction', 'The first Gelfand--Dickey Hamiltonian matrix',
     r'The notes define \((\ell f)_r=\sum_s\ell_{rs}f_s\) by a binomial sum involving \(u_{r+s+\gamma+1}\) and powers of \(\pm iD\).',
     r'''With \(0\leq r,s\leq n-2\), \(u_n=1\), \(u_{n-1}=0\), and empty sums interpreted as zero, the operator is
\[\ell_{rs}=\sum_{\gamma=0}^{n-1-r-s}\left[\binom{\gamma+r}{r}u_{r+s+\gamma+1}(-iD)^\gamma-\binom{\gamma+s}{s}(iD)^\gamma\circ u_{r+s+\gamma+1}\right].\]
Here multiplication by a coefficient is an operator, so the right-hand derivative acts on its product with the argument. The matrix is formally skew-adjoint, \(\ell_{rs}^*=-\ell_{sr}\).''',
     r'Composition, empty-sum convention and the use of \(K\supset\mathbf Q(i)\) are supplied. The repeated minus at the manuscript line break denotes a single continued subtraction, not two negatives giving a plus. This is the first, coefficient-linear Gelfand--Dickey bracket; it must not be confused with the later quadratic bracket.',
     fate=r'\citet[\S2, Eq.~(8)]{gelfanddikii1977resolvent} gives the matrix version. \citet[Eq.~(1) and \S5]{lebedevmanin1979volterra} identifies the same coefficient-linear operator, after the derivative convention is changed, with a coadjoint-orbit construction.',
     correctness='correct', match='exact', refs=['gelfanddikii1977resolvent','lebedevmanin1979volterra'], area='Integrable systems and variational calculus')
item(426, 'P000718', 'remark', 'The first nonconstant small-order example',
     r'The cases \(n=2,3\) are called easy, while \(n=4\) is the first substantial example.',
     r'Substitution into the displayed matrix gives \(\ell=-2iD\) for \(n=2\), and \(\ell=\left(\begin{smallmatrix}0&-3iD\\-3iD&0\end{smallmatrix}\right)\) for \(n=3\). Both have constant coefficients. For \(n=4\), \(\ell_{00}=2iD^3-i(2u_2D+u_2^{\prime})\), so coefficient dependence first appears.',
     r'These explicit small-order substitutions are calculated here to explain the notebook\textquoteright s qualitative remark; they are not additional formulas copied from the page.',
     fate=r'The calculation is a direct specialization of \citet[Eq.~(8)]{gelfanddikii1977resolvent} and agrees with the scan. The general Poisson theorem, rather than only these examples, was already proved in that paper.',
     correctness='correct', match='exact', refs=['gelfanddikii1977resolvent'], area='Integrable systems and variational calculus')
item(426, 'P000718', 'construction', 'Evolutionary derivations commute with the total derivative',
     r'To \(f\in A^{n-1}\) the notes assign \(\partial_f=\sum_{k,\ell}f_k^{(\ell)}\partial/\partial u_k^{(\ell)}\), assert \([\partial_f,D]=0\), and hence let it act on \(\widetilde A\).',
     r'Define \(\partial_f(u_k^{(\ell)})=D^\ell f_k\). On each generator, \(\partial_fD=D\partial_f\); therefore the identity holds on all of \(A\). It follows that \(\partial_f(Dg)=D(\partial_fg)\), so \(\partial_f\) descends to \(A/D(A)\). Conversely, every derivation commuting with \(D\) has this form.',
     r'The generator check and converse make the local-finiteness and descent arguments explicit.',
     fate=r'This correspondence is already in \citet[\S1, Eq.~(5)]{gelfanddikii1977resolvent}.',
     correctness='correct', match='exact', refs=['gelfanddikii1977resolvent'], area='Integrable systems and variational calculus')
item(426, 'P000718', 'theorem', 'The Lie algebra of evolutionary characteristics',
     r'The bracket is \([f,g]_r=\partial_fg_r-\partial_gf_r\), with \([\partial_f,\partial_g]=\partial_{[f,g]}\); this makes \(A^{n-1}\) a Lie algebra.',
     r'The map \(f\mapsto\partial_f\) is injective, since \(\partial_fu_k=f_k\), and identifies \(A^{n-1}\) with the Lie algebra of derivations of \(A\) commuting with \(D\). The displayed formula is therefore bilinear, alternating and satisfies Jacobi as the pullback of the commutator of derivations.',
     r'Injectivity is the extra step justifying the inference from the commutator identity to Jacobi.',
     fate=r'\citet[\S2, before Thm.~1]{gelfanddikii1977resolvent} uses exactly this Lie algebra.',
     correctness='correct', match='exact', refs=['gelfanddikii1977resolvent'], area='Integrable systems and variational calculus')
item(426, 'P000718', 'theorem', 'The Poisson bracket on local functionals',
     r'The notes define \(\{\widetilde f,\widetilde g\}=\int\sum_{r,s}(\delta\widetilde f/\delta u_r)\ell_{rs}(\delta\widetilde g/\delta u_s)\,dx\) and state that it makes \(\widetilde A\) a Lie algebra.',
     r'On the differential-polynomial local-functional space over characteristic zero, with the normalization and operator of item 1977-426.5, the displayed bracket is well defined and skew-symmetric and satisfies the Jacobi identity. Since the quotient need not carry a product, the immediate precise assertion is a Lie bracket on local functionals; its Hamiltonian interpretation is formal variational calculus.',
     r'The hypotheses are gathered together and the absence of a natural quotient-algebra product is kept visible.',
     fate=r'\citet[\S2, Thm.~2 and its proof, pp.~16--18]{gelfanddikii1977resolvent} proves Jacobi. This was received 22 December 1976 and published in volume 11, issue 2 of 1977, before the October talk; the notebook itself cites that issue.',
     correctness='correct', match='exact', refs=['gelfanddikii1977resolvent'], area='Integrable systems and variational calculus')
simpler_jacobi_item = item(426, 'P000718', 'problem', 'A conceptual proof of the first Gelfand--Dickey Jacobi identity',
     r'Immediately after the theorem the notes ask: \ru{доказать её попроще} (prove it more simply).',
     r'Give a structural proof of the Jacobi identity for the coefficient-linear operator \(\ell\), explaining its origin instead of checking a large binomial identity term by term.',
     r'``Structural'' spells out a reasonable interpretation of the request for simplicity. It does not claim that the original theorem was unproved, nor does it substitute the distinct second Gelfand--Dickey bracket.',
     cls='B', fate=r'\citet[Introduction, \S5 theorem and \S6]{lebedevmanin1979volterra} explicitly identifies the cumbersome direct Jacobi verification as the problem, realizes this first operator through the coadjoint representation of the formal Volterra group, and gives a new invariant proof. Their paper was received 10 November 1978, circulated as a 1978 ITEF preprint, and appeared in 1979; the introduction acknowledges independent work by Adler.',
     status='As of November 2026, the conceptual-proof request is fulfilled by the Volterra/coadjoint interpretation. The exact operator and the new proof were checked in the full primary article, so this is not inferred from a title alone.',
     correctness='correct', match='exact', problem='GP-1977-02', refs=['lebedevmanin1979volterra','gelfanddorfman1979hamiltonian'], area='Integrable systems and variational calculus')
problems.append(dict(id='GP-1977-02', title='A conceptual proof of the first Gelfand--Dickey Jacobi identity',
                     statement=r'Explain and prove the Jacobi identity for the coefficient-linear Gelfand--Dickey Hamiltonian operator through a structural construction, rather than a direct binomial calculation.',
                     occurrences=[simpler_jacobi_item], status=r'Resolved by the formal Volterra-group/coadjoint construction: \citet[\S\S5--6]{lebedevmanin1979volterra}, received November 1978 and published 1979. The full proof was read; the object is the first Gelfand--Dickey bracket.',
                     status_date='2026-11', refs=['lebedevmanin1979volterra']))
item(426, 'P000718', 'claim', 'Novikov\u2019s third-order Hamiltonian operator for KdV',
     r'Novikov observes that \(A=D^3+uD+Du\) also gives a Lie algebra and can be used to write KdV.',
     r'The scalar operator \(P=D^3+uD+D\circ u=D^3+2uD+u_x\) is Hamiltonian on local functionals. With \(H=\tfrac12\int u^2\,dx\), the evolution \(u_t=P(\delta H/\delta u)\) is \(u_t=u_{xxx}+3uu_x\). Writing \(u=2v\) gives \(v_t=v_{xxx}+6vv_x\). This is the familiar second scalar KdV Poisson structure, distinct from the first-order \(n=2\) matrix above.',
     r'Composition by \(u\), the Hamiltonian and the scaling are supplied. The notebook states no numerical KdV normalization at this point.',
     fate=r'The exact operator is a specialization of the scalar Hamiltonian pair in \citet[\S7, p.~29 of the Russian original]{gelfanddorfman1979hamiltonian}. That section reports that the KdV Lenard scheme was known to the authors from a Moscow lecture by Lax in 1976, providing retrospective evidence of circulation before this talk. This does not establish the earliest priority for the second bracket. The displayed KdV flow is checked here by applying the operator to \(u\).',
     correctness='correct', match='exact', verification='read the result', refs=['gelfanddorfman1979hamiltonian'], speaker='S. P. Novikov', area='Integrable systems and variational calculus')
checkpoint()

# Record 427.
item(427, 'P000716', 'remark', 'Monte Carlo as a metaphor for the seminar\u2019s breadth',
     r'The notes attribute to Senya Vishik the explanation that, to integrate a large domain successfully, one should use the Monte Carlo method.',
     r'The sentence specifies no domain, integrand, probability measure, estimator or accuracy criterion. In its stated context it is a metaphor about broad intellectual sampling, not a recoverable numerical-analysis theorem.',
     r'An unbiased sample-mean estimator and an \(N^{-1/2}\) error bound would be a possible illustration, but attributing either to this occurrence would add mathematical content absent from the source.',
     cls='F', fate='The attribution and metaphor are directly identifiable in the scan. No separate published technical proposal can be matched to the unquantified sentence, and no open numerical-integration problem is manufactured from it.',
     status='As of November 2026, the occurrence remains a contextual remark without a definite mathematical claim to resolve.',
     correctness='not determinable', match='none found', verification='unresolved lead', development='none', confidence='high', area='Seminar method and unidentifiable remarks')
checkpoint()
