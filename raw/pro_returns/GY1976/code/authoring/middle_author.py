"""Authoring source for GY1976 records 406--410. All text is editorial LaTeX.
Run from the workspace root. Does not touch the merged chapter files.
"""
import json, csv, re
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / 'work'
talks, items, problems, corrections, areas = [], [], [], [], {}

def talk(record, date, speaker, pages, title, summary, kind='talk'):
    talks.append(dict(record=record,date=date,speaker=speaker,pages=pages,title=title,kind=kind,summary=summary))

def item(record, pages, kind, title, notes, statement, reconstruction, fate, status,
         cls='E', literal='correct with missing hypotheses', match='exact', verification='read the result',
         development='none', problem='', worth='', refs=(), confidence='high', speaker=None, area=None):
    n = 1 + sum(x['record']==record for x in items)
    x = dict(id=f'1976-{record}.{n}',record=record,pages=pages,kind=kind,title=title,notes=notes,
             statement=statement,reconstruction=reconstruction,**{'class':cls},fate=fate,
             present_status='As of November 2026, '+status,literal_correctness=literal,
             publication_match=match,verification=verification,development=development,
             problem=problem,worth=worth,refs=list(refs),confidence=confidence)
    if speaker: x['speaker']=speaker
    items.append(x)
    areas[x['id']]=area or {406:'Supergeometry',407:'Gauge theory and differential geometry',408:'Lie theory and q-series',410:'Integrable differential equations'}[record]
    return x['id']

def correction(page,place,reads,should,evidence,applies='both',typ='faithful_error'):
    # The chapter builder inserts these cells as LaTeX, not escaped plain text.
    def formula(s):
        return r'\('+s+r'\)' if '\\' in s and r'\(' not in s and r'\[' not in s else s
    reads, should = formula(reads), formula(should)
    corrections.append(dict(page=page,place=place,transcription_reads=reads,should_read=should,evidence=evidence,applies_to=applies,type=typ))

def save():
    for name,value in [('talks',talks),('items',items),('problems',problems)]:
        (WORK/f'middle_{name}.json').write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
    with (WORK/'middle_corrections.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=['page','place','transcription_reads','should_read','evidence','applies_to','type']); w.writeheader(); w.writerows(corrections)
    meta=dict(records=[t['record'] for t in talks],actual_pages={str(t['record']):t['pages'] for t in talks},
              inspected_scan_pages=[f'P{i:06d}' for i in range(670,685)],areas=areas,
              class_counts=dict(Counter(x['class'] for x in items)),area_counts=dict(Counter(areas.values())),
              source_policy='Russian transcription controls; actual scans inspected for all pages P000670--P000684; catalogue spans are broader than the identified notes.',
              status_date='2026-11-10',stage='complete segment' if len(talks)==5 else 'incremental authoring')
    (WORK/'middle_meta.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')

talk(406,'1976-10-18','I. N. Bernstein','P000670-P000674','Superdomains, Berezin integration, and Stokes boundaries',
 r'''The dated continuation begins on P000670, after a separate question about factors. Bernstein explains superfunctions, parity-preserving morphisms, nilpotent Taylor expansion, and why a boundary requires an embedded subsupermanifold in addition to its ordinary body. The circle and half-line examples lead to the Stokes problem, soon printed by Bernstein and Leites. P000673--P000674 explicitly form a retrospective summary of earlier super talks copied from I.~Dorfman's notebook; their definitions and linear algebra are indexed here with that provenance, rather than assigned a new seminar date. The catalogue's P000668--P000675 span also includes adjoining talks.''')

item(406,'P000670','problem','Factors and matrices of continuous order',
 r'''Before Bernstein's heading the page asks: \ru{записать \(\mathrm{II}_1\)-факторы через матрицы непр. порядка}, followed by a doubtful \ru{не сделанная}. No attribution, definition, or proposed equivalence is supplied.''',
 r'''The surviving wording requests some representation of type \(\mathrm{II}_1\) factors by ``matrices of continuous order.'' It does not specify the matrix object, a topology, an approximation property, or whether every factor is intended. No determinate modern theorem or conjecture can therefore be extracted.''',
 r'''``Continuous order'' is retained as an unidentified expression. Interpreting it as finite-dimensional microstate approximation, an embedding into an ultrapower, or continuous geometry would add a substantive condition absent from the page.''',
 r'''Searches for the Russian phrase, continuous-order matrices, factors, and Gelfand did not identify an exact publication. The connection with known matrix approximation problems is only a possible theme and is not used as a solution claim.''',
 'the exact question remains unidentified; this is an evidence limitation, not an assertion that a specified operator-algebra problem is open.',
 cls='F',literal='not determinable',match='none found',verification='unresolved lead',confidence='low',area='Operator algebras')

item(406,'P000670-P000671; P000673-P000674','definition','Supercommutative functions and their parity',
 r'''The notes write \(C^\infty(\mathbb R^p)\otimes\Lambda(\xi_1,\ldots,\xi_q)\), expand in monomials with exponents zero or one, and set parity equal to total odd degree modulo two. The retrospective page gives \(A=A_0\oplus A_1\) and \(ab=(-1)^{p(a)p(b)}ba\).''',
 r'''For an open \(U\subset\mathbb R^p\), set \(\mathcal O(U)=C^\infty(U;\mathbb R)\otimes\Lambda(\mathbb R^q)\). Every element has a unique expansion \(f=\sum_{I\subseteq\{1,\ldots,q\}}f_I(u)\xi^I\), with increasing indices in \(\xi^I\). For homogeneous \(a,b\), \(ab=(-1)^{|a||b|}ba\); the grading is by \(|I|\bmod2\), not by polynomial degree in the even variables.''',
 r'''Homogeneity in the sign rule and the increasing order of exterior generators are explicit here. The final exponent \(\alpha_k\) on P000670 is a faithful index slip for \(\alpha_q\).''',
 r'''Already printed in \citet[\S2, p.~505]{berezinleites1975supermanifolds}; the same definitions appear in \citet[\S\S1--2]{bernsteinleites1977integral}. The 1975 paper was received on 24 March 1975.''',
 'this is the standard local algebra of a smooth supermanifold.',refs=['berezinleites1975supermanifolds','bernsteinleites1977integral'])

item(406,'P000670; P000674','definition','Superdomains as locally ringed spaces',
 r'''A superdomain is an open set \(U\subset\mathbb R^p\) with the sheaf \(V\mapsto C^\infty(V)\otimes\Lambda(\xi_1,\ldots,\xi_q)\). The sketches illustrate an ordinary interval carrying this sheaf and an underlying one-point space.''',
 r'''A smooth superdomain of dimension \(p|q\) is \((U,\mathcal O_U)\), where \(U\subset\mathbb R^p\) is open and \(\mathcal O_U=C^\infty_U\otimes\Lambda(\mathbb R^q)\). A smooth supermanifold is a locally ringed space locally isomorphic to one of these models; its body is obtained by quotienting the nilpotent ideal generated by the odd functions.''',
 r'''The local-ring condition and the body quotient are supplied to make precise the ringed-space shorthand. The notes only use the local split model; they do not assert a canonical global splitting.''',
 r'''This is the construction of \citet[Definition~1, pp.~505--506]{berezinleites1975supermanifolds}, before this talk; compare the compact formulation in \citet[\S\S2, 8]{bernsteinleites1977integral}.''',
 'the local ringed-space formulation is established and carries no unresolved classification claim here.',refs=['berezinleites1975supermanifolds','bernsteinleites1977integral'])

item(406,'P000670; P000674','theorem','Morphisms determined by coordinate pullbacks',
 r'''A map covers a map of the bodies and induces a unital algebra homomorphism in the reverse direction preserving parity. The retrospective page says that it suffices to specify \(v_i^*,\eta_j^*\), and gives \(v=u+\xi_1\xi_2,\eta_1=u\xi_1,\eta_2=\xi_2\).''',
 r'''A morphism \(\Phi:U^{p|q}\to V^{m|n}\) is a body map together with a parity-preserving local unital homomorphism of sheaves \(\Phi^\sharp:\mathcal O_V\to\Phi_*\mathcal O_U\). It is uniquely specified by even sections \(a_1,\ldots,a_m\) and odd sections \(\beta_1,\ldots,\beta_n\), provided the body tuple \((a_{1,0},\ldots,a_{m,0})\) takes values in \(V\). Smooth functions of the \(a_i\) are evaluated by their finite nilpotent Taylor expansion.''',
 r'''The body-image condition and the sheaf/locality requirement are essential additions. The example with \(\eta_1=u\xi_1\) is a morphism but is not an invertible coordinate change where \(u=0\).''',
 r'''Morphisms were defined in \citet[Definition~3 and coordinate changes, p.~506]{berezinleites1975supermanifolds}; the exact coordinate determination is stated in \citet[\S3]{bernsteinleites1977integral}.''',
 'the coordinate theorem is standard; invertibility requires an invertible body differential and invertible odd linear block.',refs=['berezinleites1975supermanifolds','bernsteinleites1977integral'])

item(406,'P000670','construction','Endomorphisms of a point with two odd directions',
 r'''For \(p=0,q=2\) the underlying space is a point. The allowed images of \(\xi_1,\xi_2\) are arbitrary linear combinations of the odd generators; a term proportional to \(\xi_1\xi_2\) is crossed out because parity must be preserved.''',
 r'''Every parity-preserving unital \(\mathbb R\)-algebra endomorphism of \(\Lambda(\xi_1,\xi_2)\) is determined by \(\xi_1\mapsto a\xi_1+b\xi_2\), \(\xi_2\mapsto c\xi_1+d\xi_2\). Any real \(a,b,c,d\) are allowed; the endomorphism is an automorphism exactly when \(ad-bc\ne0\). A quadratic term cannot occur in the image of an odd generator.''',
 r'''The automorphism criterion is an elementary consequence, not a claim explicitly written on the page. It clarifies the distinction between an endomorphism and a coordinate change.''',
 r'''This is the \(0|2\) instance of the pre-existing coordinate-morphism formalism in \citet[Definition~3]{berezinleites1975supermanifolds}; compare \citet[\S3]{bernsteinleites1977integral}.''',
 'this finite exterior-algebra example is completely determined by its odd degree-one part.',literal='correct',refs=['berezinleites1975supermanifolds','bernsteinleites1977integral'])

item(406,'P000671; P000674','question','The nilpotent Taylor formula for a smooth pullback',
 r'''The classroom question is \ru{куда переходит \(\sin v\)?} for \(v=u+\xi_1\xi_2\). The next display supplies \(g_{00}(u+\xi_1\xi_2)=g_{00}(u)+\xi_1\xi_2g'_{00}(u)\).''',
 r'''If \(\varepsilon=\xi_1\xi_2\), then \(\varepsilon^2=0\) and \(g(u+\varepsilon)=g(u)+\varepsilon g'(u)\) for every smooth \(g\). Thus \(\Phi^*(\sin v)=\sin u+\xi_1\xi_2\cos u\). More generally, if even nilpotents \(n_i\) generate a nilpotent ideal, \(g(u+n)=\sum_\alpha (\partial^\alpha g)(u)n^\alpha/\alpha!\), a finite sum.''',
 r'''The sine answer and the multi-variable version spell out the Taylor rule rather than assume analyticity of \(g\). This repeats the earlier seminar item 1975-389.7, not a new unsolved problem.''',
 r'''The construction is implicit in the 1975 coordinate formalism and explicit in \citet[\S3]{bernsteinleites1977integral}; the present notes themselves answer the posed question.''',
 'the question has the displayed exact algebraic answer for smooth functions.',literal='correct',refs=['berezinleites1975supermanifolds','bernsteinleites1977integral'])

item(406,'P000671; P000673-P000674','definition','Even and left odd partial derivatives',
 r'''Even derivatives differentiate coefficients. The odd rules include \(\partial_{\xi_1}(\xi_1\xi_2)=\xi_2\), \(\partial_{\xi_2}(\xi_1\xi_2)=-\xi_1\), and the sign from the number of preceding generators.''',
 r'''On the ordered monomial \(f(u)\xi_1^{\alpha_1}\cdots\xi_q^{\alpha_q}\), \(\partial_{u_i}\) acts on \(f\), whereas the left derivative is \[\partial_{\xi_j}(f\xi^\alpha)=\alpha_j(-1)^{\alpha_1+\cdots+\alpha_{j-1}}f\xi_1^{\alpha_1}\cdots\widehat{\xi_j^{\alpha_j}}\cdots\xi_q^{\alpha_q}.\] It satisfies \(\partial_{\xi_j}(ab)=(\partial_{\xi_j}a)b+(-1)^{|a|}a\partial_{\xi_j}b\) for homogeneous \(a\).''',
 r'''The left-derivative convention is made explicit; switching to right derivatives changes matrix-coordinate conventions and must be done consistently.''',
 r'''These pre-existing Grassmann differentiation rules are written explicitly in \citet[\S4]{bernsteinleites1977integral}; the earlier density formula in \citet[\S3]{berezinleites1975supermanifolds} instead labels a right-derivative convention.''',
 'the formulas are standard once the left/right convention is fixed.',literal='correct',refs=['bernsteinleites1977integral','berezinleites1975supermanifolds'])

item(406,'P000673','theorem','The Berezinian and the reciprocal formula in the recap',
 r'''The first formula gives \(\det(A_{11})^{-1}\det(A_{22}-A_{21}A_{11}^{-1}A_{12})\). Lower down the same page gives \(\operatorname{Ber}J=\det(D)^{-1}\det(A-BD^{-1}C)\) and multiplicativity.''',
 r'''For an invertible even block matrix \(J=\left(\begin{smallmatrix}A&B\\C&D\end{smallmatrix}\right)\) over a supercommutative real or complex algebra, with invertible even diagonal blocks, \[\operatorname{Ber}J=\frac{\det(A-BD^{-1}C)}{\det D}=\frac{\det A}{\det(D-CA^{-1}B)}.\] It is an even unit and \(\operatorname{Ber}(J_1J_2)=\operatorname{Ber}J_1\operatorname{Ber}J_2\).''',
 r'''The first notebook expression is the inverse of the usual Berezinian. This is a faithful mathematical error, not an OCR correction: on a diagonal \(1|1\) matrix \(\operatorname{diag}(a,d)\), it gives \(d/a\), whereas the lower formula gives \(a/d\). The independent check is recorded in the critical annotations.''',
 r'''The density multiplier already appears in \citet[formula~(3)]{berezinleites1975supermanifolds}; \citet[\S1]{bernsteinleites1977integral} states the Berezinian formula and multiplicativity and credits Berezin's 1971 formula. Thus this is exposition with an internal reciprocal inconsistency.''',
 'the corrected Berezinian formula is established; the two literal notebook definitions cannot be used simultaneously.',literal='false as written',development='annotated',refs=['berezinleites1975supermanifolds','bernsteinleites1977integral'])

item(406,'P000673','claim','Supertrace, logarithm, and supertranspose',
 r'''The recap writes \(\operatorname{str}J=\operatorname{tr}A-\operatorname{tr}D\), \(\det J=\exp\operatorname{str}\log J\), ordinary cyclicity of supertrace, and \(\left(\begin{smallmatrix}A&B\\C&D\end{smallmatrix}\right)^{*}=\left(\begin{smallmatrix}A^*&C^*\\-B^*&D^*\end{smallmatrix}\right)\).''',
 r'''For an even matrix \(J\), the supertrace is \(\operatorname{tr}A-\operatorname{tr}D\). Whenever a compatible formal or analytic logarithm exists, \(\operatorname{Ber}J=\exp(\operatorname{str}\log J)\); equivalently \(\operatorname{Ber}(e^X)=e^{\operatorname{str}X}\) for even \(X\). For homogeneous endomorphisms \(X,Y\), \(\operatorname{str}(XY)=(-1)^{|X||Y|}\operatorname{str}(YX)\). With the stated even-matrix convention the supertranspose is \(J^{st}=\left(\begin{smallmatrix}A^t&C^t\\-B^t&D^t\end{smallmatrix}\right)\).''',
 r'''The ungraded cyclic identity holds for the even matrices under discussion; it would be false without that restriction. The logarithm formula uses the lower, usual Berezinian, not the first reciprocal determinant. The star is read as transpose, not complex adjoint; the page gives no conjugation convention.''',
 r'''These are algebraic identities belonging to the same older Berezinian formalism. The opened \citet[\S1]{bernsteinleites1977integral} verifies the determinant normalization, but does not itself print all the supertrace and transpose assertions: the publication match for this combined recital is partial, and the identities have been checked algebraically here.''',
 'the identities hold with the displayed parity and logarithm restrictions.',match='partial',development='annotated',refs=['bernsteinleites1977integral'])

item(406,'P000671; P000674','definition','Berezinian volume elements rather than a top ordinary form',
 r'''The notes say that one integrates densities transforming by the Berezinian, and define \(\rho=fD(x)\), \(D(y)/D(x)=\operatorname{Ber}J\). They contrast these with ordinary differential forms.''',
 r'''For an oriented smooth \(p|q\) supermanifold, the Berezinian line has local generator \(D(u,\xi)\) and transition law \(D(y)=\operatorname{Ber}(\partial y/\partial x)D(x)\), with coefficients pulled back to a common chart. Thus a section satisfies \(f_x=(f_y\circ\Phi)\operatorname{Ber}D\Phi\). For \(q>0\), the usual super differential-form algebra has no maximal form degree, since the differentials of odd coordinates commute in exterior degree. A Berezinian section is therefore not a highest ordinary differential form.''',
 r'''Orientation and coefficient pullback are explicit here. The statement ``forms cannot be integrated'' is read as the lack of this canonical top-form construction, not a prohibition of every integration operation on superforms.''',
 r'''The density law is already \citet[Definition~5 and formula~(3)]{berezinleites1975supermanifolds}; \citet[\S\S5--7]{bernsteinleites1977integral} distinguishes volume, differential, and integral forms.''',
 'the distinction is standard and is essential to the Stokes formulation below.',refs=['berezinleites1975supermanifolds','bernsteinleites1977integral'])

item(406,'P000672; P000674','theorem','Compactly supported Berezin integration',
 r'''The integral is the ordinary integral of the coefficient of \(\xi_1\cdots\xi_q\). The recap attributes coordinate independence to Berezin and explicitly requires compact support.''',
 r'''Fix an orientation of \(U\subset\mathbb R^p\) and the odd convention \(\int\xi_1\cdots\xi_q\,D\xi=1\). For a compactly supported Berezinian section \(\rho=fD(u,\xi)\), define \(\int_{U^{p|q}}\rho=\int_U f_{\{1,\ldots,q\}}(u)\,du\). This is invariant under orientation-compatible super-coordinate changes and extends by partitions of unity to oriented smooth supermanifolds.''',
 r'''The fixed odd ordering removes the apparent discrepancy between different conventions for \(d\xi_1d\xi_2\). Compact support is inside the open body; allowing support to reach a missing boundary invalidates the unqualified change-of-variables statement.''',
 r'''This is \citet[Theorem~1]{berezinleites1975supermanifolds}, published in 1975. \citet[\S5]{bernsteinleites1977integral} restates it and gives Rudakov's boundary counterexample when the support hypothesis is removed.''',
 'the theorem is established; boundary integrals require the extra geometric data in the following items.',literal='correct',refs=['berezinleites1975supermanifolds','bernsteinleites1977integral'])

item(406,'P000671-P000672','definition','Regular ideals and embedded even boundaries',
 r'''A subsupermanifold is described by an ideal of functions; a boundary is cut out by an even superfunction \(f=0\). The notes emphasize that it carries the structure of a subsupermanifold.''',
 r'''An embedded codimension \(r|s\) subsupermanifold is locally given by \(r\) even and \(s\) odd functions whose body Jacobian has the corresponding full even and odd ranks, so that they extend to a super-coordinate system. In particular an even \(f\) with \(df_0\ne0\) on \(f_0^{-1}(0)\) defines a codimension \(1|0\) boundary. An arbitrary ideal defines a ringed subspace, not necessarily a subsupermanifold.''',
 r'''The necessary rank condition is supplied; it cannot be omitted from the ideal description.''',
 r'''The regular-equation result predates the talk: \citet[Theorem~2]{berezinleites1975supermanifolds}. The boundary-specific formulation is \citet[\S\S8, 11]{bernsteinleites1977integral}.''',
 'regularity separates smooth embedded boundaries from singular quotient spaces.',refs=['berezinleites1975supermanifolds','bernsteinleites1977integral'])

item(406,'P000671-P000672','construction','A closed superdomain includes a choice of superboundary',
 r'''The same body \([0,\infty)\) has boundaries \(u=0\) and \(u+c\xi_1\xi_2=0\). The disc similarly has the two boundaries \(u_1^2+u_2^2-1=0\) and \(u_1^2+u_2^2-1-\xi_1\xi_2=0\).''',
 r'''A closed superdomain consists of a closed region \(F\) with smooth body boundary and an embedded \((p-1)|q\) subsupermanifold with body \(\partial F\). Distinct ideals \((u)\) and \((u+c\xi_1\xi_2)\) on the same ambient \(1|2\) superdomain give distinct such boundaries when \(c\ne0\). Berezin integration is defined in boundary-adapted charts; the body alone does not determine it.''',
 r'''This is extra geometric boundary data, not a choice between two unequal ordinary point sets. With a compactly supported \(g\), the naive change \(v=u+c\xi_1\xi_2\) changes a top-coefficient half-line integral by \(c\int_0^\infty g'_0(u)du=-cg_0(0)\) if both coordinate half-lines are held fixed.''',
 r'''The exact closed-domain definition is \citet[\S11]{bernsteinleites1977integral}, submitted 6 October 1976 and printed in 1977. The submission date precedes this talk; a separate public-circulation date has not been established. Class A records publication chronology rather than priority of this seminar.''',
 'the extra boundary embedding and the resulting boundary term are established.',cls='A',refs=['bernsteinleites1977integral'])

item(406,'P000672','claim','Straightening the nilpotently displaced circle',
 r'''To normalize \(u_1^2+u_2^2-1-\xi_1\xi_2=0\), the notebook writes \((u_1-\tfrac12\xi_1\xi_2)^2+u_2^2-1=0\). The scan confirms the missing denominator is not supplied in the handwriting.''',
 r'''Let \(\varepsilon=\xi_1\xi_2\). On the chart \(u_1\ne0\), the substitution \(v_1=u_1-\varepsilon/(2u_1)\), \(v_2=u_2\), with unchanged odd coordinates, gives exactly \(v_1^2+v_2^2-1=u_1^2+u_2^2-1-\varepsilon\). An analogous chart uses \(u_2\ne0\). Such charts cover the body circle.''',
 r'''Direct expansion of the notebook substitution gives \(u_1^2+u_2^2-1-u_1\varepsilon\), so the written normalization is false. The local division by \(u_1\) is an editorial correction with its domain stated, not a claimed global coordinate formula.''',
 r'''The boundary-straightening framework is exactly the one used in \citet[\S11]{bernsteinleites1977integral}, published in 1977 after submission on 6 October 1976. That short paper does not print this particular circle substitution, so the publication match is partial.''',
 r'the local corrected substitution is exact because \(\varepsilon^2=0\); the literal notebook formula fails.',cls='A',literal='false as written',match='partial',development='annotated',refs=['bernsteinleites1977integral'])

item(406,'P000672','claim','A boundary-preserving half-line change of variables',
 r'''For \(v=u+u\xi_1\xi_2\), the notes observe that \(u=0\) becomes \(v=0\), then begin a check using \(g_{11}\) and mark \(Dv/Du\). The displayed expansion does not yet include the transformed full superfunction and Berezinian.''',
 r'''Put \(\varepsilon=\xi_1\xi_2\), \(v=u(1+\varepsilon)\), and \(\eta_i=\xi_i\). For \(G(v,\eta)=g_0(v)+g_1(v)\eta_1+g_2(v)\eta_2+g_{12}(v)\eta_1\eta_2\), one has \(\operatorname{Ber}D\Phi=1+\varepsilon\). The top coefficient of \(\Phi^*(G D(v,\eta))\) is \(g_{12}(u)+(ug_0(u))'\). If the coefficients are smooth at zero and compactly supported toward infinity, its half-line integral is \(\int_0^\infty g_{12}(u)du\).''',
 r'''The omitted lower coefficient and Jacobian are restored. The extra term integrates to \([ug_0(u)]_0^\infty=0\), which directly verifies the intended boundary-preserving invariance; expanding only \(g_{11}\) is not that proof.''',
 r'''This is the local model of \citet[\S11]{bernsteinleites1977integral}, received 6 October 1976 and printed in 1977; the explicit coefficient check here is a critical annotation, not a new theorem.''',
 'the corrected calculation establishes the claimed invariance under its stated support hypotheses.',cls='A',match='partial',development='annotated',refs=['bernsteinleites1977integral'])

stokes_id=item(406,'P000671-P000672','problem','Stokes formula for a nilpotently displaced disc',
 r'''The text asks \ru{Теорема Стокса --- ?}, \ru{Что интегр. по границе?}, and finally \ru{теор. Стокса для круга \(u_1^2+u_2^2+c\xi_1\xi_2-1=0\)}. It names Bernstein and Leites in connection with boundary integration.''',
 r'''Let \(M\) be an oriented smooth supermanifold of dimension \(p|q\), and let \(\mathcal D\) be a closed superdomain with embedded even boundary \(\partial\mathcal D\), oriented by the outward-normal convention. For a compactly supported integral form \(\omega\) of degree \(p-1\), \[\int_{\mathcal D}d\omega=\int_{\partial\mathcal D}\iota^*\omega.\] In particular this applies in \(\mathbb R^{2|2}\) to the disc with boundary ideal \((u_1^2+u_2^2+c\xi_1\xi_2-1)\), since its body differential is nonzero on the unit circle.''',
 r'''Integral forms, their differential, and the boundary restriction map supply the missing objects. They are defined in the later publication; the notebook itself poses the problem and does not record a complete general Stokes theorem.''',
 r'''The exact answer is \citet[\S12, Stokes' formula, with \S\S7, 9, 11]{bernsteinleites1977integral}. The manuscript was submitted on 6 October 1976, before the 18 October seminar, and printed in 1977; no earlier public-circulation date has been verified.''',
 'this boundary problem is solved in the stated integral-form category. It does not furnish a remaining class C or D research problem.',cls='A',problem='GP-1976-10',refs=['bernsteinleites1977integral'])

item(406,'P000672','remark','Berezin and Marinov on classical Grassmann mechanics',
 r'''A bibliographic aside, with a question mark after Marinov's name, refers to a work on classical mechanics in Fermi and Bose variables. No Hamiltonian, bracket, or motion equation is written.''',
 r'''The identifiable subject is classical dynamics on an algebra containing both commuting and anticommuting variables. The notes do not specify a model or a theorem, and no particular equations of spinning-particle mechanics are attributed to the speaker here.''',
 r'''The 1975 announcement and 1976 report/1977 full paper are plausible bibliographic referents. Identification of the topic is stronger than identification of which version the speaker meant.''',
 r'''The author's institutional bibliography lists \citet{berezinmarinov1975classical}, before the talk. INSPIRE records \citet{berezinmarinov1977particle} as report ITEP-43-1976 and publication in 1977. Only bibliographic metadata was checked for this aside; no unrecorded mechanics result is inferred.''',
 'the bibliographic topic is identified, while the exact version referred to and any intended mathematical proposition remain unspecified.',match='thematic only',verification='indirect',literal='not determinable',confidence='medium',refs=['berezinmarinov1975classical','berezinmarinov1977particle'])

problems.append(dict(id='GP-1976-10',title='Stokes formula for closed superdomains with even boundary',
 statement=r'''Construct the appropriate integral forms and boundary restriction for an oriented smooth \(p|q\) supermanifold with a specified embedded even boundary, and establish \(\int_{\mathcal D}d\omega=\int_{\partial\mathcal D}\iota^*\omega\) for compactly supported \((p-1)\)-degree integral forms; the notebook tests the boundary \(u_1^2+u_2^2+c\xi_1\xi_2-1=0\).''',
 occurrences=[stokes_id],status=r'''Solved by \citet[\S12]{bernsteinleites1977integral}, submitted 6 October 1976 and published in 1977. The submission predates the dated seminar; public circulation before that date has not been established. As of November 2026 this exact smooth-boundary statement is settled.''',status_date='2026-11',refs=['bernsteinleites1977integral']))

correction('P000670','last exponent in superfunction expansion',r'\xi_q^{\alpha_k}',r'\xi_q^{\alpha_q}','Scan and Russian transcription agree on k; the indexed expansion requires q.')
correction('P000670','caption for excluded even term in image of odd generator','disallowed, since it preserves parity','disallowed because the morphism must preserve parity','Russian wording explains the parity requirement; the quadratic term itself is even.','en','translation')
correction('P000671','second superfunction ring',r'g(v,\xi_1,\xi_2)',r'g(v,\eta_1,\eta_2)','The target coordinates were named eta; the scan itself reuses xi. This is a harmless faithful notation slip.')
correction('P000672','circle-normalizing substitution',r'(u_1-\tfrac12\xi_1\xi_2)^2+u_2^2-1',r'(u_1-\xi_1\xi_2/(2u_1))^2+u_2^2-1\quad(u_1\ne0)','Direct expansion; scan confirms no u1 denominator. The corrected formula is local, with the u2 chart covering the remaining boundary.')
correction('P000672','half-line invariance calculation',r'Expansion of \(g_{11}\) alone',r'Top coefficient \(g_{12}+(u g_0)^{\prime}\), including \(\operatorname{Ber}D\Phi=1+\xi_1\xi_2\)','Full pullback calculation, not a diplomatic emendation; the notebook check is incomplete.')
correction('P000673','first block determinant definition',r'\det(A_{11})^{-1}\det(A_{22}-A_{21}A_{11}^{-1}A_{12})',r'\det(A_{11})/\det(A_{22}-A_{21}A_{11}^{-1}A_{12})','Scan confirms reciprocal; lower Berezinian and exp(str log) on the same page require the corrected normalization. Diagonal 1|1 check.')
correction('P000673-P000674','record provenance','Continuation of the 18 October talk without qualification','Retrospective summary of earlier Bernstein talks from I. Dorfman\'s notebook','Explicit handwritten heading on P000673; retained within record406 without manufacturing a new session.',typ='provenance')
save()

talk(407,'1976-10-25','V. N. Popov [catalogue; attribution conflict]','P000675-P000677','Connections, free Yang--Mills fields, and Ricci-flat metrics',
 r'''The notes begin on P000675 with Gelfand's request for an elementary explanation of a connection and a reference to Yang and Mills. They develop gauge covariance, the principal-bundle equation \(H\delta_h\Phi=0\), its independence of the auxiliary vertical metric, and the affine-frame realization of the vacuum Einstein equations. The last two results match D.~A.~Popov's 1975 paper and D.~A.~Popov--L.~I.~Daikhin's 1975 note exactly. The supplied catalogue calls the speaker V.~N.~Popov, while the handwritten heading gives only Popov; that conflict is retained explicitly. Mathematical identification of the papers does not prove a correction of the speaker's initials. The identified notes occupy P000675--P000677, narrower than the catalogue's P000673--P000679 packet.''')

item(407,'P000675-P000676','question','What is a connection?',
 r'''Gelfand asks \ru{Что такое связность? (для первокурсников и Полякова)} and lists Nomizu, Sternberg, Bishop--Crittenden, and Landau--Lifshitz. Later the talk represents a connection by a Lie-algebra-valued one-form \(\Omega\) on a principal bundle.''',
 r'''For a smooth right principal \(G\)-bundle \(\pi:P\to M\), a connection is a smooth right-equivariant horizontal subbundle \(H\subset TP\) with \(TP=H\oplus\ker d\pi\). Equivalently it is \(\Omega\in\Omega^1(P;\mathfrak g)\) such that \(\Omega(a^\#)=a\) for each fundamental vertical field and \(R_g^*\Omega=\operatorname{Ad}(g^{-1})\Omega\). Local potentials are \(s^*\Omega\) for local sections \(s\).''',
 r'''The two connection axioms and their equivalent horizontal-space interpretation are supplied. Gelfand's request is pedagogical, not a new research question; no specific edition of the reading-list books is inferred.''',
 r'''The exact principal-connection interpretation is recalled in \citet[\S1, Definition~1]{popovdaikhin1975einstein} and in \citet[\S1]{popov1975yangmills}, both published before the seminar.''',
 'the question is answered by the standard principal-connection definition.',speaker='I. M. Gelfand',refs=['popovdaikhin1975einstein','popov1975yangmills'])

item(407,'P000675','definition','The massless Dirac equation used to introduce gauge coupling',
 r'''The opening equation is the massless Dirac equation for an ordinary four-component spinor. No interaction term is included in that displayed equation.''',
 r'''On four-dimensional Minkowski space with a fixed spin structure, choose matrices \(\gamma^\mu\) satisfying \(\gamma^\mu\gamma^\nu+\gamma^\nu\gamma^\mu=2g^{\mu\nu}I\). A free massless spinor satisfies \(i\gamma^\mu\partial_\mu\Psi=0\), equivalently the equation without the factor \(i\). A gauge coupling in a representation \(R\) replaces \(\partial_\mu\) by \(D_\mu=\partial_\mu+R_*(A_\mu)\).''',
 r'''The Clifford relation and a definite signature convention are needed to interpret the written symbols. The covariant derivative is explanatory reconstruction; the notebook does not yet state a coupled Dirac--Yang--Mills system.''',
 r'''The free Dirac equation was classical long before 1976. The local-symmetry motivation for replacing the derivative is the construction in \citet[``Isotopic gauge transformation,'' pp.~192--193]{yangmills1954conservation}; the publication match is thematic for the notebook's isolated massless equation.''',
 'this is established background, and the displayed free spinor equation does not by itself couple matter to the later gauge field.',match='thematic only',refs=['yangmills1954conservation'])

item(407,'P000675','theorem','Curvature and the source-free Yang--Mills equations',
 r'''The notes give \(\partial_\nu F_a^{\mu\nu}+f^b_{ac}F_b^{\mu\nu}A_\nu^c=0\), the nonlinear curvature formula, and the Killing form \(K_{ab}=f_{ac}^{d}f_{bd}^{c}\) for lowering Lie-algebra indices.''',
 r'''Let \((M,g)\) be pseudo-Riemannian, \(G\) semisimple, and \(A=A_\mu^aT_a dx^\mu\) a local principal connection, with \([T_b,T_c]=f^a_{bc}T_a\). Then \[F=dA+\tfrac12[A,A],\qquad F^a_{\mu\nu}=\partial_\mu A^a_\nu-\partial_\nu A^a_\mu+f^a_{bc}A^b_\mu A^c_\nu.\] The Euler--Lagrange equation of the quadratic curvature action, using a nondegenerate invariant bilinear form, is \(D_\mu F^{\mu\nu}=0\). On Minkowski space the covariant base derivative reduces to \(\partial_\mu\); Lie-algebra dual indices can be identified by the Killing form.''',
 r'''The invariant tensor notation fixes the ambiguous handwritten structure-constant indices. The factor \(1/2\) in the antisymmetrized notebook component expression gives exactly the displayed commutator term. On a curved base one must include the Levi-Civita connection or the equivalent density divergence.''',
 r'''The gauge-field equations originate in \citet[pp.~193--194]{yangmills1954conservation}, received 28 June and published 1 October 1954. The geometric semisimple formulation is \citet[Proposition~3 and equation~(37)]{popov1975yangmills}; it was received in July 1974 and printed in 1975.''',
 'these are the established classical source-free equations; no assertion about quantum existence, a mass gap, or confinement is made here.',refs=['yangmills1954conservation','popov1975yangmills'])

item(407,'P000675','remark','Gelfand\'s reference on quarks',
 r'''Gelfand refers readers to Zel'dovich's UFN article \ru{Кварки для пешеходов}.''',
 r'''This is a reading recommendation about the classification of elementary particles and the quark model. It contains no new mathematical claim in the seminar record.''',
 r'''The abbreviated spoken title is identified with Zel'dovich's 1965 review, ``Classification of elementary particles and quarks `for pedestrians'.'' No result from that review is imported into the notebook.''',
 r'''Publisher and Math-Net metadata identify \citet{zeldovich1965quarks}, published in 1965, as the exact bibliographic referent.''',
 'the reading reference is identified; it should be linked as background rather than indexed as an open problem.',literal='correct',verification='publisher metadata checked',speaker='I. M. Gelfand',refs=['zeldovich1965quarks'])

item(407,'P000675','claim','The distinction between a gauge field and quark matter',
 r'''The notebook says \ru{Ур-ия Янга--Миллса описывают кварки} immediately after the source-free gauge equations and the earlier free Dirac equation.''',
 r'''The displayed unknown \(A\) is a Lie-algebra-valued gauge potential. Quark fields are spinor-valued matter fields carrying a color representation; a classical model with such matter requires a covariant Dirac equation and a current term \(D_\mu F^{\mu\nu}=j^\nu\). Consequently the source-free equation written here describes the gauge sector, not the full coupled quark dynamics.''',
 r'''The phrase may be broad physical motivation, but as a literal identification of the displayed equations with quark fields it is false. Neither confinement nor a statement about individual observed quarks follows.''',
 r'''The original \citet[pp.~192--194]{yangmills1954conservation} distinguishes the gauge potential from the matter wavefunction and its current; the note's free-field terminology is also explicit in \citet[Definitions~1--3]{popovdaikhin1975einstein}. The correction concerns that pre-existing distinction.''',
 'the literal field identification requires correction; no unresolved research assertion is extracted from the motivational sentence.',literal='false as written',match='partial',development='annotated',refs=['yangmills1954conservation','popovdaikhin1975einstein'])

item(407,'P000675','theorem','The abelian reduction and gradient gauge transformations',
 r'''For \(G=U(1)\), the notes obtain Maxwell's equations and write \(A_\mu\mapsto A_\mu+\partial_\mu\alpha\). The antisymmetric matrix separates electric and magnetic components.''',
 r'''For an abelian connection, \(F=dA\) locally, so \(dF=0\) identically and the source-free Yang--Mills equation is \(d{*}F=0\). These are the vacuum Maxwell equations. A local gauge change \(A\mapsto A+d\alpha\) leaves \(F\) unchanged; globally \(A\) need not be a single one-form when the \(U(1)\)-bundle is nontrivial.''',
 r'''The Bianchi equation supplies the homogeneous half of Maxwell's system. Metric raising of both indices is required: the formula with derivatives of \(A_\nu\) directly defines \(F_{\mu\nu}\), not \(F^{\mu\nu}\) in Minkowski coordinates. Electric/magnetic signs depend on the metric and time-coordinate convention.''',
 r'''The comparison with electromagnetism is explicit in \citet[pp.~192--193]{yangmills1954conservation} and \citet[\S1, after Definition~3]{popovdaikhin1975einstein}, both before this talk.''',
 'the abelian reduction is exact, subject to the local-potential and index conventions stated here.',refs=['yangmills1954conservation','popovdaikhin1975einstein'])

item(407,'P000676','theorem','Nonabelian gauge covariance',
 r'''With \(B_\mu=T_aA_\mu^a\), the notes write \(B'_\mu=S^{-1}B^\mu S+S^{-1}\partial_\mu S\), \(F'_{\mu\nu}=S^{-1}F_{\mu\nu}S\), and assert invariance of the equations.''',
 r'''For a smooth \(S:U\to G\), fix \(A'=S^{-1}AS+S^{-1}dS\). Then \(F'=S^{-1}FS\) and \(D'({*}F')=S^{-1}D({*}F)S\). Therefore \(D{*}F=0\) is invariant under changes of local trivialization. In the component formula the same covariant index \(\mu\) must occur on both \(A'_\mu\) and \(A_\mu\).''',
 r'''The isolated raised \(\mu\) in the conjugated potential is a faithful index error. The exterior equation fixes all local-sign conventions and explains precisely what is gauge invariant: the equation is covariant, while the curvature itself is conjugated.''',
 r'''These are \citet[equations~(3)--(5)]{yangmills1954conservation}, with coupling and Hermitian conventions converted to a Lie-algebra-valued connection, and \citet[equations~(5), (20)]{popov1975yangmills}.''',
 'gauge covariance is established; the notebook requires only the indicated index correction.',literal='false as written',development='annotated',refs=['yangmills1954conservation','popov1975yangmills'])

item(407,'P000676','construction','A metric on the total space of a principal bundle',
 r'''Given \(g\) on \(M\), a connection \(\Omega\), and an arbitrary nondegenerate quadratic form \(K\) on \(\mathfrak g\), the notes set \(h=\pi^*g+K(\Omega,\Omega)\), observing that it is generally not invariant.''',
 r'''Let \(g\) be nondegenerate and symmetric on \(TM\), and \(K\) a fixed nondegenerate symmetric form on \(\mathfrak g\). The formula \[h_p(X,Y)=g_{\pi(p)}(d\pi X,d\pi Y)+K(\Omega X,\Omega Y)\] defines a smooth nondegenerate pseudo-Riemannian metric on \(P\): horizontal and vertical directions are orthogonal, with metrics \(g\) and \(K\). It is right \(G\)-invariant exactly when \(K\) is \(\operatorname{Ad}(G)\)-invariant.''',
 r'''Symmetry is made explicit because the source calls \(K\) a quadratic form. Semisimplicity is not needed for this auxiliary metric construction; it is needed only if one insists on taking the Killing form.''',
 r'''The semisimple metric is in \citet[equation~(22)]{popov1975yangmills}; the arbitrary-group extension using an arbitrary nondegenerate form appears explicitly in \citet[\S1, before Lemma~1]{popovdaikhin1975einstein}, printed in 1975.''',
 'the construction is valid without an invariant vertical metric, as the notes correctly emphasize.',literal='correct',refs=['popov1975yangmills','popovdaikhin1975einstein'])

item(407,'P000676','definition','Horizontal curvature and the structural identity',
 r'''Curvature is defined by \(\Phi=H d\Omega=d\Omega+\tfrac12[\Omega,\Omega]\), where \(H\) takes the horizontal component. A horizontal form vanishes when one argument is vertical.''',
 r'''For a principal connection, \(\Phi=d\Omega+\tfrac12[\Omega\wedge\Omega]\) is horizontal and \(\operatorname{Ad}\)-equivariant. Hence it is equivalently a two-form on \(M\) valued in the adjoint bundle. Its covariant exterior derivative vanishes: \(D\Phi=0\), the Bianchi identity.''',
 r'''The bracket includes the wedge product and the Lie bracket. The Bianchi identity is stated here to distinguish curvature geometry from the additional field equation; it is implicit in the later comparison with Maxwell's equations.''',
 r'''These standard connection identities are used in \citet[\S1]{popov1975yangmills} and restated in \citet[\S1]{popovdaikhin1975einstein}, both preceding the seminar.''',
 'the curvature and Bianchi identities are established independently of any field equation.',literal='correct',refs=['popov1975yangmills','popovdaikhin1975einstein'])

item(407,'P000676-P000677','theorem','The projected codifferential is independent of the vertical metric',
 r'''The notes propose \(H\delta_h\Phi=0\) and emphasize that it does not depend on \(K\). A parenthetical sentence makes the broader assertion for equivariant horizontal vector-valued forms.''',
 r'''For the metric \(h\) above and a principal-connection curvature \(\Phi\), \(H\delta_h\Phi\) is horizontal, \(\operatorname{Ad}\)-equivariant, and independent of the chosen nondegenerate \(K\). Thus it defines an intrinsic equation \(\mathcal D\Phi=0\) for any Lie group. For semisimple \(G\), this coincides with the Euler--Lagrange Yang--Mills equation formed using the Killing metric.''',
 r'''The exact verified theorem is for the curvature form. The wider notebook parenthesis about arbitrary equivariant horizontal forms is not needed for the field equation and is not asserted here without specifying its representation and codifferential conventions. No invariant \(K\) is imposed on the curvature theorem: that would improperly weaken the result.''',
 r'''The semisimple equivalence is \citet[Proposition~3]{popov1975yangmills}. The arbitrary-group, arbitrary-\(K\) assertion is exactly \citet[Lemma~1 and Definition~3, p.~791]{popovdaikhin1975einstein}, received 26 June 1975 and published in 1975. It is therefore E, not a post-seminar development.''',
 'the verified curvature equation is established for arbitrary Lie groups; the scope of the broader parenthetical claim is kept separate.',match='partial',refs=['popov1975yangmills','popovdaikhin1975einstein'])

item(407,'P000677','theorem','Projection of the bundle equation to a local gauge',
 r'''For a section \(\zeta\), the notes set \(\theta=\zeta^*\Omega\) and \(\zeta^*\Phi=T_aF^a_{\mu\nu}dx^\mu\wedge dx^\nu\), then write \(\delta_M\zeta^*\Phi+*^{-1}[\theta,*\zeta^*\Phi]=0\).''',
 r'''In a local section, \(A=s^*\Omega\), \(F=s^*\Phi=dA+\tfrac12[A,A]\), and the projected equation is \(D_A{*}F=0\), or \(D_{A,\mu}F^{\mu\nu}=0\). Equivalently it is a covariant codifferential equation \(\delta_A F=0\), with the signature-dependent Hodge sign included in the chosen definition of \(\delta_A\). With a sum over all ordered indices, \(F=\tfrac12T_aF^a_{\mu\nu}dx^\mu\wedge dx^\nu\).''',
 r'''The notebook formula suppresses either a factor \(1/2\) or a restriction \(\mu<\nu\). The invariant exterior formulation avoids declaring its Hodge sign wrong without a convention. Existence of a bi-invariant metric is needed for the usual invariant-action interpretation, not for the arbitrary-group projected equation itself.''',
 r'''The local formula is \citet[equations~(36)--(37)]{popov1975yangmills} and \citet[equations~(2)--(3)]{popovdaikhin1975einstein}; both exact formulations were available in 1975.''',
 'the local and bundle equations agree after fixing normalization and codifferential conventions.',refs=['popov1975yangmills','popovdaikhin1975einstein'])

item(407,'P000677','construction','The affine Cartan connection induced by a metric',
 r'''For the affine frame bundle and \(G=\operatorname{Aff}(\mathbb R^4)\), the notes characterize \(\bar\Omega\) by \(i^*\bar\Omega=(\Omega^g,\chi)\), where \(\chi\) is the displacement or solder form.''',
 r'''For a pseudo-Riemannian \(n\)-manifold, let \(L(M)\) and \(A(M)\) be its linear and affine frame bundles. The Levi-Civita connection \(\Omega^g\) induces the affine connection uniquely characterized by \(i^*\bar\Omega=(\Omega^g,\chi)\) in \(\mathfrak{gl}_n\ltimes\mathbb R^n\). Its curvature restricts to \((R^g,T^g)=(R^g,0)\), because the Levi-Civita connection is torsion free.''',
 r'''The dimension-general formulation and torsion-free condition clarify the four-dimensional example. ``Cartan connection'' follows the affine-frame convention of the source; it is not an arbitrary affine gauge potential with independent translational part.''',
 r'''This construction is written explicitly in \citet[\S2, p.~792, before equation~(5)]{popovdaikhin1975einstein}, published in 1975 after receipt on 26 June.''',
 'the induced affine connection and its curvature decomposition are established.',refs=['popovdaikhin1975einstein'])

item(407,'P000677','theorem','Vacuum Einstein equations as the affine curvature equation',
 r'''On the metric-induced Cartan connections, \(H\delta\Phi=0\) is identified with \(\operatorname{Ric}=0\). The notes underline that these are first order in the connection.''',
 r'''For the affine connection \(\bar\Omega\) induced by a pseudo-Riemannian metric as above, \[H\delta_h\bar\Phi=0\quad\Longleftrightarrow\quad\operatorname{Ric}(g)=0.\] In the splitting \(\mathfrak{aff}_n=\mathfrak{gl}_n\ltimes\mathbb R^n\), the translational component of the projected equation is, up to the fixed Hodge convention, contraction of the Ricci tensor; the linear component is the covariant-divergence equation for curvature.''',
 r'''The equivalence holds on the specified metric-induced, torsion-free affine connections. It is false if one replaces them merely by linear-frame Levi-Civita connections: their Yang--Mills equation alone gives harmonic curvature, not necessarily Ricci flatness. The assertion is about vacuum equations with zero cosmological constant.''',
 r'''This is exactly \citet[Theorem~2 and equation~(5), p.~792]{popovdaikhin1975einstein}, printed in 1975. The source explicitly contrasts its affine result with Yang's linear-frame equation.''',
 'the equivalence is settled with those constraints; it is not an equivalence between all unrestricted Yang--Mills solutions and all Einstein metrics.',refs=['popovdaikhin1975einstein'])

item(407,'P000677','claim','Why the second-order connection equation follows from Ricci flatness',
 r'''A final diagram links \(R_{ij}=0\) with the equation \(R_{ij,k}=R_{ik,j}\); the second-order equations are called consequences of the first-order equations.''',
 r'''For a Levi-Civita connection, the contracted differential Bianchi identity expresses the divergence of Riemann curvature as the antisymmetrized covariant derivative of Ricci, with index signs depending on the curvature convention. Hence \(\operatorname{Ric}=0\) implies \(\nabla_j\operatorname{Ric}_{ik}=\nabla_k\operatorname{Ric}_{ij}\) and \(D^*R=0\). Ricci uses one derivative of the connection coefficients, whereas its covariant derivative uses two. In metric variables their orders are two and three respectively.''',
 r'''The derivative-order assertion is relative to connection coefficients and to the metric-induced constraint. The implication is one-way for the linear-frame equation; a parallel nonzero Ricci tensor also satisfies the displayed derivative identity.''',
 r'''The consequence and the fact that the translational component is fixed are stated immediately after \citet[Theorem~2]{popovdaikhin1975einstein}. This is the same pre-1976 observation, not an additional field equation discovered at the talk.''',
 'the implication follows from the differential Bianchi identity; its converse requires the affine translational equation.',refs=['popovdaikhin1975einstein'])

correction('P000675','claim about quarks','The Yang--Mills equations describe quarks','The displayed source-free equations describe gauge fields; quark matter requires a coupled covariant Dirac equation and a current','Faithful wording in both versions; the displayed unknown is the connection, not a spinor matter field.')
correction('P000675','Maxwell curvature indices',r'F^{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu',r'F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu;\quad F^{\mu\nu}=g^{\mu\alpha}g^{\nu\beta}F_{\alpha\beta}','Scan confirms the mixed index placement; Minkowski raising is not the identity.')
correction('P000676','conjugated potential in gauge transformation',r'B_\mu\mapsto S^{-1}B^\mu S+S^{-1}\partial_\mu S',r'B_\mu\mapsto S^{-1}B_\mu S+S^{-1}\partial_\mu S','The superscript is present in the scan; all terms need the same covariant index.')
correction('P000677','curvature two-form normalization',r'T_aF^a_{\mu\nu}dx^\mu\wedge dx^\nu',r'\tfrac12T_aF^a_{\mu\nu}dx^\mu\wedge dx^\nu\quad\hbox{or sum only over }\mu<\nu','The notes omit a summation convention; if Einstein summation is intended, the factor1/2 is necessary.',typ='ambiguity')
correction('P000675-P000677','speaker initials in catalogue','V. N. Popov','Retain catalogue initials with explicit conflict: the exact papers are by D. A. Popov (with L. I. Daikhin)','Handwritten heading says only Popov; exact 1975 primary papers and author metadata do not justify silently replacing the catalogued speaker.',typ='provenance')
save()

talk(408,'1976-11-22','I. N. Bernstein','P000678-P000680','Euler products, compact-group heat kernels, and affine Lie algebras',
 r'''Bernstein explains Euler and Jacobi identities, Macdonald's root-system generalization, and Kostant's expression through characters and the Casimir. A shifted spectral zeta function is introduced, but its displayed reflection equation lacks the necessary Mellin completion. Olshanetsky intervenes on radial Laplacians and quantum integrability. Bernstein then gives the Cartan-matrix construction and the affine \(A_2\) loop-algebra example. The date 22 November is supplied by the catalogue; the corresponding handwritten start on P000678 is undated and P000680 ends with a New Year greeting. This evidence does not establish additional sessions within the packet. The mathematical notes are P000678--P000680, rather than the catalogue's wider P000677--P000681 span.''')

item(408,'P000678','theorem','Euler\'s pentagonal-number identity',
 r'''The page sets \(\varphi(x)=\prod_{n\ge1}(1-x^n)\) and writes \(\varphi(x)=\sum_{n\in\mathbb Z}(-1)^n x^{(3n^2+n)/2}\).''',
 r'''In \(\mathbb Z[[q]]\), and analytically for \(|q|<1\), \[\prod_{m=1}^\infty(1-q^m)=\sum_{n\in\mathbb Z}(-1)^nq^{n(3n+1)/2}.\] Replacing \(n\) by \(-n\) gives the familiar \(n(3n-1)/2\) convention.''',
 r'''The formal-series or unit-disc domain is added; the plus sign in the notebook exponent is correct, not a transcription error.''',
 r'''This is the classical Euler identity discussed in \citet[\S7, formula~(23)]{demazure1977identites}. That exposition is dated June 1976, although its collected volume was printed in 1977; it therefore documents pre-talk circulation independently of the much older identity.''',
 'the identity is established in both the formal and analytic senses stated.',literal='correct',refs=['demazure1977identites'])

item(408,'P000678','theorem','Jacobi\'s cubic Euler-product identity',
 r'''Jacobi's formula is \(\varphi(x)^3=\sum_{n\ge0}(-1)^n(2n+1)x^{n(n+1)/2}\), described as arising from the theta function.''',
 r'''For \(|q|<1\), or as a formal series, \[\prod_{m\ge1}(1-q^m)^3=\sum_{n\ge0}(-1)^n(2n+1)q^{n(n+1)/2}.\] It is the rank-one specialization of the affine denominator identity, equivalently a specialization or derivative of the Jacobi triple product.''',
 r'''The source's lower limit zero and the coefficient \(2n+1\) are retained. This item identifies the identity itself; it does not assert that the notebook contains the derivation.''',
 r'''\citet[Introduction, equations~(0.6)--(0.7)]{macdonald1972affine} explicitly recovers Jacobi's old identity as the \(A_1\) case. The paper was printed in 1972, well before the seminar.''',
 'the identity and its rank-one root-system interpretation are established.',literal='correct',refs=['macdonald1972affine'])

item(408,'P000678','claim','Partitions and the reciprocal Euler product',
 r'''The notes write \(\varphi(x)^{-1}=\sum p(n)x^n\) and describe \(p(n)\) as partitions into nonnegative summands.''',
 r'''Let \(p(n)\) count unordered partitions of \(n\) into positive integer parts, with \(p(0)=1\). Then \[\prod_{m\ge1}(1-q^m)^{-1}=\sum_{n\ge0}p(n)q^n.\] For each \(m\), the factor \(\sum_{r\ge0}q^{mr}\) records the multiplicity of the positive part \(m\).''',
 r'''Allowing arbitrary zero parts as distinct summands would make the count infinite. The word ``nonnegative'' is harmless only if zero padding is ignored; the precise convention uses positive parts.''',
 r'''The partition function and its use in eta identities are already discussed in \citet[Introduction, pp.~5--6 of the Russian translation]{macdonald1972affine}. The coefficient interpretation follows directly from the geometric-series factors and is old expository material.''',
 'the generating function is established with positive parts or an explicitly equivalent zero-padding convention.',literal='false as written',match='partial',development='annotated',refs=['macdonald1972affine'])

item(408,'P000678','definition','Ramanujan\'s tau function and the eta normalization',
 r'''The definition is \(x\varphi(x)^{24}=\sum\tau(n)x^n\), followed by a remark about a combinatorial definition and a reference to Dedekind's ``theta'' function.''',
 r'''For \(q=e^{2\pi i\tau}\), \(\operatorname{Im}\tau>0\), Dedekind's function is \(\eta(\tau)=q^{1/24}\prod_{m\ge1}(1-q^m)\). The discriminant cusp form is \(\Delta_{\rm mod}(\tau)=\eta(\tau)^{24}=\sum_{n\ge1}\tau(n)q^n\). A direct finite signed combinatorial interpretation of \(\tau(n)\) is the sum of \((-1)^{\sum_j|S_j|}\) over 24 finite subsets \(S_j\subset\mathbb Z_{>0}\) satisfying \(\sum_j\sum_{m\in S_j}m=n-1\).''',
 r'''The notation \(\Delta_{\rm mod}\) avoids collision with the Laplacian later on the page. The signed subset formula is the coefficient expansion of the displayed product, supplied here; it is not claimed to be the specific combinatorial formula intended in the shorthand remark. The Dedekind function is \(\eta\), whereas the earlier Jacobi reference is indeed to theta.''',
 r'''\citet[Introduction, \(A_4\) example and Dyson's tau formula]{macdonald1972affine} discusses precisely the 24th-power application before the talk. \citet[\S1(b)]{demazure1977identites}, a June 1976 exposition, gives the \(SU(5)\) example.''',
 'the defining series is established; no Ramanujan conjecture is being posed by this definition.',literal='correct with missing hypotheses',refs=['macdonald1972affine','demazure1977identites'])

item(408,'P000678','construction','The invariant Casimir and the compact-group Laplacian',
 r'''For compact semisimple \(G\), a Killing-orthonormal basis \(X_i\) is used to write \(\Delta=\sum X_i^2\), asserted to be two-sided invariant and scalar on irreducible representations.''',
 r'''Let \(G\) be a connected compact semisimple Lie group and choose \(X_1,\ldots,X_d\) orthonormal for minus the Killing form. The operator \(\Delta=\sum_i X_i^2\), acting as left-invariant vector fields, is a nonpositive bi-invariant Laplacian. Its negative \(C=-\Delta\) is the positive Casimir and acts on a finite-dimensional irreducible representation of highest weight \(\lambda\) by \(c_\lambda=(\lambda,\lambda+2\rho)\), using the dual Killing normalization.''',
 r'''Minus the Killing form, the Laplace sign, and the normalization on each simple factor are explicit. Without these choices the exponents in the next eta identity and the shift \(d/24\) are not determined.''',
 r'''The Killing-normalized Casimir is the one in \citet[\S3]{demazure1977identites} and in \citet[Theorem~0.1 and its preceding notation]{kostant2003euler}, which restates Kostant's 1976 result. The June 1976 Bourbaki lecture verifies that this formulation circulated before the seminar.''',
 'the operator construction is standard; the notebook needs a consistent sign to use it as an exponent.',refs=['demazure1977identites','kostant2003euler'])

item(408,'P000678-P000679','theorem','Kostant\'s character expansion of an Euler-product power',
 r'''For \(k=\dim G\), the notes write \(\varphi(x)^k=\sum_V c_V\dim(V)x^{\Delta|_V}\), with \(c_V=\chi_V(a)\). The example table gives dimensions 3, 24, and 10 for \(SU(2)\), \(SU(5)\), and the symplectic type \(C_2\).''',
 r'''Let \(G\) be compact, connected, semisimple, and simply connected, \(d=\dim G\), and identify the real weight space \(i\operatorname{Lie}(T)\) with its dual by the Killing form. For \(a_\rho=\exp(2\pi i\,2\rho)\), where \(\rho\) is half the sum of positive roots under that identification, \[\prod_{m\ge1}(1-q^m)^d=\sum_{\lambda\in P_+}\chi_\lambda(a_\rho)\dim(V_\lambda)q^{c_\lambda}.\] Here \(c_\lambda\) is the positive Casimir eigenvalue; \(\chi_\lambda(a_\rho)\in\{-1,0,1\}\). The equality holds for \(0<q<1\); only integral Casimir exponents have nonzero character coefficient.''',
 r'''The notes do not specify \(a\), the sign of \(\Delta\), or the covering group. These are supplied from the exact theorem. \(Sp(4)\) in the table is interpreted as the complex matrix notation for type \(C_2\), whose compact form is often denoted \(Sp(2)\); its dimension is 10.''',
 r'''The exact expansion is restated by its author in \citet[Theorem~0.1, citing his 1976 Theorem~3.1]{kostant2003euler}. Its pre-talk formulation was checked directly in \citet[\S3, formulas~(15)--(16)]{demazure1977identites}, dated June 1976. The original 1976 publisher full text was inaccessible; no claim of having read that original is made.''',
 'the character identity is established; the extra hypotheses and normalization prevent a false literal Laplacian-sign reading.',refs=['kostant2003euler','demazure1977identites','macdonald1972affine'])

item(408,'P000679','construction','The distinguished regular conjugacy class in SU(n)',
 r'''For \(SU(n)\), the notes describe a unique regular conjugacy class whose \(n\)th power is scalar, represented by \(c\operatorname{diag}(\xi,\xi^2,\ldots,\xi^n)\), with \(c\) chosen for determinant one.''',
 r'''Take a primitive \(n\)th root \(\zeta\) and choose \(c\in U(1)\) so that \(c^n\zeta^{n(n+1)/2}=1\). Then \(a=c\operatorname{diag}(\zeta,\ldots,\zeta^n)\in SU(n)\), has distinct eigenvalues, and \(a^n\) is scalar. Conversely, if \(a\in SU(n)\) has distinct eigenvalues and scalar \(n\)th power, its eigenvalues form the full set of roots of one scalar; the determinant condition makes it conjugate to this element. Different permissible choices of \(c\) merely permute that set.''',
 r'''Primitivity of \(\zeta\) and the distinction between one element and one conjugacy class are explicit. The short converse is an elementary reconstruction from the written characterization.''',
 r'''This is the type \(A\) principal-element case of the already circulating Kostant description, recorded in \citet[\S3]{demazure1977identites}; the canonical type-\(\rho\) element is also defined before \citet[Theorem~0.1]{kostant2003euler}.''',
 'the conjugacy-class characterization is exact under the distinct-eigenvalue condition.',literal='correct',refs=['demazure1977identites','kostant2003euler'])

item(408,'P000679','claim','The spectral zeta reflection requires completion',
 r'''The notes define \(\zeta_a(s)\) as the central convolution kernel of \((-\Delta+d/24)^{-s}\) evaluated at \(a\), then assert \(\zeta_a(s)=\zeta_a(d/2-s)\). The scan shows no Gamma or power-of-\(2\pi\) factor.''',
 r'''With the Killing-normalized positive Casimir \(C=-\Delta\), normalized Haar measure, and the distinguished element \(a=a_\rho\), initially for \(\operatorname{Re}s>d/2\), \[Z_a(s)=\sum_\lambda\frac{\chi_\lambda(a)\dim V_\lambda}{(c_\lambda+d/24)^s}.\] Its completion \(\Lambda_a(s)=(2\pi)^{-s}\Gamma(s)Z_a(s)\) satisfies \[\Lambda_a(s)=\int_0^\infty t^{s-1}\eta(it)^d\,dt,\qquad \Lambda_a(s)=\Lambda_a(d/2-s).\] The integral is entire in \(s\), owing to exponential decay at both ends after eta inversion.''',
 r'''Kostant's character identity gives the heat-kernel integrand. The classical transformation \(\eta(i/t)=\sqrt t\,\eta(it)\) and the substitution \(t\mapsto1/t\) prove the completed reflection. The raw symmetry is false: \(Z_a(0)=0\), while \(Z_a(d/2)=(2\pi)^{d/2}\Lambda_a(d/2)/\Gamma(d/2)>0\) for \(d>0\). This is a normalization correction, not a new zeta theorem.''',
 r'''The heat-kernel identification is tied to Kostant's 1976 result, restated in \citet[Theorem~0.1]{kostant2003euler}. The eta inversion used to check the missing completion is the classical formula in \citet[23.18.5--23.18.6]{nist2026dlmf}. The exact raw reflection in the notebook has no valid publication match.''',
 'the completed reflection is established; the literal uncompleted equation needs the displayed correction.',literal='false as written',match='partial',development='annotated',refs=['kostant2003euler','demazure1977identites','nist2026dlmf'])

item(408,'P000679','remark','The unidentified 39th- and 45th-power formulas',
 r'''A short line says that there are also formulas for \(\varphi^{39}\) and \(\varphi^{45}\), followed by the Latin-script name ``Van Esh.'' No sum, lattice, coefficient rule, or normalization is given.''',
 r'''The only definite content is the claimed existence of unspecified identities for two Euler-product powers. Since every such power has an elementary coefficient expansion, the mathematical content depends on the missing special form of the asserted formulas.''',
 r'''The plausible author identification is A.~G. (Bram) van Asch, not a new theorem attributed to a literal ``Van Esh.'' His 1976 paper and the 1973 announcement cited by Demazure are leads; the exact 39/45 assertions were not recovered from an opened full text.''',
 r'''\citet[\S1 and bibliography item~7]{demazure1977identites} identifies van Asch's direct proof and a 1973 announcement. Publisher metadata verifies \citet{vanasch1976modular}, received 28 September 1975 and published June 1976. Searches for the name variants and the exponents did not verify the two particular formulas; the accessible Demazure text does not state them.''',
 'the author and likely literature are partly identified, but the exact notebook item is still not determinate enough to assert a solved or open problem.',cls='F',literal='not determinable',match='thematic only',verification='unresolved lead',confidence='medium',refs=['demazure1977identites','vanasch1976modular'])

item(408,'P000679','method','The affine denominator and homological explanation of Macdonald identities',
 r'''Bernstein credits Kac with a proof using infinite-dimensional Lie algebras and gives the precise Garland--Lepowsky citation, Inventiones 34 (1976), 37--76.''',
 r'''For a symmetrizable Kac--Moody algebra with positive roots \(\Delta_+\), root multiplicities \(\operatorname{mult}\alpha\), Weyl group \(W\), and a weight \(\rho\) satisfying \(\rho(h_i)=1\), the denominator identity is \[\prod_{\alpha\in\Delta_+}(1-e^{-\alpha})^{\operatorname{mult}\alpha}=\sum_{w\in W}(-1)^{\ell(w)}e^{w\rho-\rho}.\] It is an identity in the completion by the positive root cone. In the affine case, the imaginary-root factors account for the Euler-product factor; specialization yields Macdonald's identities.''',
 r'''The formula, the symmetrizability hypothesis, the root multiplicities, and the formal completion are reconstructed from the cited proof tradition, not displayed in the notebook. They explain the role of infinite-dimensional homology rather than merely naming it.''',
 r'''The exact bibliography is \citet{garlandlepowsky1976homology}, received 7 January and published February 1976. Its publisher metadata was checked; the denominator statement and explanation were read in \citet[\S\S4--6, especially (19), (21)]{demazure1977identites}, delivered June 1976. Hence the method was already public before this seminar.''',
 'the affine denominator interpretation is established, including the multiplicities of imaginary roots.',refs=['garlandlepowsky1976homology','demazure1977identites','macdonald1972affine'])

item(408,'P000679','construction','Radial Laplacians become inverse-sine-square Hamiltonians',
 r'''Olshanetsky writes that the radial Laplace operator on a symmetric space becomes \(\tfrac12\sum\partial_{t_k}^2+U\), with \(U=g\sum_{k>\ell}\sin^{-2}(t_k-t_\ell)\).''',
 r'''On a regular radial chamber of a Riemannian symmetric space, let \(J(t)\) be the radial volume density and \(\Delta_{\rm rad}=J^{-1}\operatorname{div}(J\nabla)\). Conjugation gives \[-\tfrac12J^{1/2}\Delta_{\rm rad}J^{-1/2}=-\tfrac12\Delta_{\mathfrak a}+\tfrac14\Delta_{\mathfrak a}\log J+\tfrac18|\nabla\log J|^2.\] In compact type \(A\), \(J=\prod_{i<j}|\sin(t_i-t_j)|^m\); the resulting potential, up to an additive constant and metric scale, is \(m(m-2)\sum_{i<j}\sin^{-2}(t_i-t_j)/4\).''',
 r'''The conjugating factor, chamber, kinetic sign, and geometric coupling are supplied. A general symmetric space has its own restricted root system and root multiplicities; the single pairwise \(A\)-type expression is not its universal formula. In this geometric derivation the coupling is fixed by multiplicities, not arbitrary.''',
 r'''The exact radial-conjugation construction appears in \citet[\S3, Lemma~1 and formula~(3.6)]{olshanetskyperelomov1978radial}, received 16 June 1977 and published in 1978. Class A follows the intervention's author and the subsequent joint paper; older many-particle examples alone would not establish this geometric match.''',
 'the radial construction is established with group multiplicities and a specified radial domain.',cls='A',speaker='M. A. Olshanetsky',refs=['olshanetskyperelomov1978radial'],area='Quantum integrable systems')

item(408,'P000679','claim','A complete commuting family of quantum integrals from radial operators',
 r'''Olshanetsky adds that there is a complete system of observables ``in the quantum sense.'' No domains or specific higher operators are written.''',
 r'''For the Hamiltonians obtained from symmetric-space radial parts with the group values of the coupling constants, the radial invariant differential operators form a commutative algebra. Conjugating this algebra by the same \(J^{1/2}\) gives commuting differential operators including the Hamiltonian and having \(r=\dim\mathfrak a\) algebraically independent principal symbols. This is formal quantum complete integrability on the regular chamber.''',
 r'''The precise assertion concerns commuting differential expressions and independence of symbols. Strong commutation of chosen self-adjoint realizations at collision walls would require domain conditions absent from the notes and is not inferred.''',
 r'''This is the group-coupling assertion of \citet[\S4, Theorem~2 and the preceding commutativity corollary]{olshanetskyperelomov1978radial}, received in 1977 and printed in 1978. The paper gives explicit generators for several root systems in \S5.''',
 'the formal commuting algebra is established under those hypotheses; operator-domain issues are outside this recorded claim.',cls='A',speaker='M. A. Olshanetsky',refs=['olshanetskyperelomov1978radial'],area='Quantum integrable systems')

item(408,'P000679','definition','Generalized Cartan matrices',
 r'''The notebook requires integer entries, \(a_{ii}=2\), symmetric occurrence of zeros, but writes \(a_{ij}<0\) for every \(i\ne j\).''',
 r'''A generalized Cartan matrix is an integer matrix \(A=(a_{ij})\) with \(a_{ii}=2\), \(a_{ij}\le0\) for \(i\ne j\), and \(a_{ij}=0\) if and only if \(a_{ji}=0\). It is symmetrizable if \(DA\) is symmetric for a positive diagonal matrix \(D\).''',
 r'''The strict inequality is a faithful error: it contradicts the adjacent comment about zeros and would exclude disconnected diagrams and most ordinary Dynkin diagrams. Symmetrizability is additional structure, not part of the three basic conditions.''',
 r'''The conditions are classical before the talk: see \citet[Chapter~II, \S1, conditions (M2)--(M5)]{kac1968graded} and \citet[\S5]{demazure1977identites}.''',
 'the corrected nonpositive-off-diagonal definition is standard.',literal='false as written',development='annotated',refs=['kac1968graded','demazure1977identites'])

item(408,'P000680','construction','Chevalley--Serre generators and the missing conventions',
 r'''There are three families \(h_i,e_i,f_i\), called ``\(n\) generators.'' The general brackets use the signs opposite to the later \(\mathfrak{sl}_2\) example, and the \([e,f]\) line repeats the subscript \(i\). Only the \(e\)-Serre relation is explicitly displayed; a maximal-ideal quotient is also mentioned.''',
 r'''Over \(\mathbb C\), the derived Kac--Moody algebra for a generalized Cartan matrix is generated by \(e_i,f_i,h_i\) with \[[h_i,h_j]=0,\quad[h_i,e_j]=a_{ij}e_j,\quad[h_i,f_j]=-a_{ij}f_j,\quad[e_i,f_j]=\delta_{ij}h_i,\] together with \((\operatorname{ad}e_i)^{1-a_{ij}}e_j=(\operatorname{ad}f_i)^{1-a_{ij}}f_j=0\) for \(i\ne j\). The full Kac--Moody algebra uses a realization with Cartan dimension \(2n-\operatorname{rank}A\); for singular \(A\), it is larger than the algebra generated by these \(3n\) elements.''',
 r'''The statement fixes a standard sign convention consistent with the notebook's explicit \(\mathfrak{sl}_2\) brackets, supplies the missing \(f\)-relations and \(i\ne j\), and distinguishes the derived from the full algebra. In a contragredient maximal-ideal construction, the quotient ideal must meet the chosen Cartan subalgebra trivially; an unrestricted ``maximal normal subalgebra'' is not the definition.''',
 r'''The finite/affine defining relations are in \citet[Chapter~II, Proposition~13, equations~(39)]{kac1968graded}; the generalized construction in the form being explained is \citet[\S5]{demazure1977identites}, dated June 1976.''',
 'the corrected presentation is established; the literal mixed signs and indices are not a consistent presentation of the examples that follow.',literal='false as written',development='annotated',refs=['kac1968graded','demazure1977identites'])

item(408,'P000680','theorem','Finite type and the positive-definite criterion',
 r'''The matrix \((2)\) is associated with \(SU(2)\) and \(\left(\begin{smallmatrix}2&-1\\-1&2\end{smallmatrix}\right)\) with \(SU(3)\). For symmetric \(A\), finite dimensionality is asserted equivalent to positive definiteness.''',
 r'''For a symmetric generalized Cartan matrix \(A\), the associated complex Kac--Moody algebra is finite dimensional exactly when \(A\) is positive definite. In that case it is semisimple, with simple factors given by the connected finite Dynkin diagrams. The matrices \((2)\) and \(A_2=\left(\begin{smallmatrix}2&-1\\-1&2\end{smallmatrix}\right)\) give \(\mathfrak{sl}_2(\mathbb C)\) and \(\mathfrak{sl}_3(\mathbb C)\), whose compact real forms integrate to \(SU(2)\) and \(SU(3)\).''',
 r'''The notebook calls the constructed Lie algebra a group. Distinguishing the complex algebra, compact real form, and group avoids tensoring a Lie group with a polynomial ring in the next item. The positive-definite criterion concerns the symmetric matrix here; for symmetrizable matrices it concerns a positive diagonal symmetrization.''',
 r'''The finite diagrams and their contrast with affine diagrams are classified in \citet[Chapter~II, \S\S4--7, Tables~0--3]{kac1968graded}; the finite presentation is also recalled in \citet[\S5]{demazure1977identites}. Both precede the seminar.''',
 'the finite-type criterion and the two examples are established.',refs=['kac1968graded','demazure1977identites'])

item(408,'P000680','theorem','Affine A2 as a central extension of the loop algebra',
 r'''For \(A=\left(\begin{smallmatrix}2&-1&-1\\-1&2&-1\\-1&-1&2\end{smallmatrix}\right)\), the quotient by a one-dimensional center is written \(SU(3)\otimes\mathbb C[x,x^{-1}]\), with \([x^kg,x^\ell g']=x^{k+\ell}[g,g']\).''',
 r'''The derived affine algebra of type \(A_2^{(1)}\) is \(\widehat{\mathfrak{sl}}_3'=(\mathfrak{sl}_3(\mathbb C)\otimes\mathbb C[t,t^{-1}])\oplus\mathbb Cc\), with \[[X\otimes t^m,Y\otimes t^n]=[X,Y]\otimes t^{m+n}+m\delta_{m+n,0}\kappa(X,Y)c,\] for a fixed nonzero invariant form \(\kappa\). Quotienting by \(\mathbb Cc\) gives the loop algebra and exactly the bracket written in the notebook. The full affine algebra additionally has the degree derivation \(d\), with \([d,X\otimes t^m]=mX\otimes t^m\).''',
 r'''The tensor factor is the complex Lie algebra, not \(SU(3)\). The central cocycle and the derived/full distinction are reconstruction explaining why the notebook's center quotient is correct in its intended convention.''',
 r'''\citet[Chapter~II, \S7, loop construction, Lemma~22 and Proposition~13]{kac1968graded} gives the affine realization modulo center. The notebook's conclusion is an exposition of that pre-existing result.''',
 'the central extension, quotient, and derivation distinction are established.',refs=['kac1968graded'])

item(408,'P000680','claim','The scope of the positive-semidefinite loop classification',
 r'''After the affine example, the notes say \ru{все нестрог. опред. получаются так}.''',
 r'''If a symmetric generalized Cartan matrix is indecomposable, positive semidefinite, and singular, it has affine type and corank one; its derived algebra modulo center is the corresponding untwisted loop algebra of finite type \(A,D,E\), including the rank-one affine case. If indecomposability is dropped, positive-semidefinite matrices decompose into finite and affine blocks. In the broader symmetrizable setting, twisted loop algebras also occur.''',
 r'''``Non-strictly definite'' is interpreted as positive semidefinite in the immediately preceding symmetric setting. It cannot mean every matrix that fails positive definiteness: indefinite Kac--Moody algebras generally have neither this corank nor this loop realization.''',
 r'''The distinction between finite, affine, and other growth is the content of \citet[Chapter~II, Theorem~1, \S7 and Tables~0--3]{kac1968graded}. This prior classification supplies the missing scope.''',
 'the restricted affine statement is settled; the unrestricted reading would be false.',literal='correct with missing hypotheses',refs=['kac1968graded'])

correction('P000678','partition terminology','partitions into nonnegative summands','partitions into positive parts, or identify all zero padding','Unlimited zeros otherwise give infinitely many decompositions; handwriting faithfully uses nonnegative.')
correction('P000678','Dedekind function name',r'Dedekind \(\Theta\)-function',r'Dedekind \(\eta\)-function',r'The displayed product \(q^{1/24}\) times the Euler product defines eta; the preceding Jacobi theta reference is separate.')
correction('P000679','raw zeta reflection',r'\zeta(s)=\zeta(\dim\mathfrak g/2-s)',r'\Lambda(s)=\Lambda(\dim\mathfrak g/2-s),\quad\Lambda(s)=(2\pi)^{-s}\Gamma(s)\zeta(s)',r'Actual scan contains no completion; the Mellin transform of \(\eta(it)^d\) gives the corrected relation. The raw values at \(0\) and \(d/2\) differ.')
correction('P000679','Cartan off-diagonal inequality',r'a_{ij}<0\quad(i\ne j)',r'a_{ij}\le0\quad(i\ne j)','The scan has a strict sign; adjacent symmetric-zero remark and standard Cartan examples require allowing zeros.')
correction('P000680','number of generators',r'\(n\) generators \(h_i,e_i,f_i\)',r'\(3n\) generators, in three families indexed by \(i=1,\ldots,n\)','The page lists three families; n is the size of the Cartan matrix.')
correction('P000680','general Chevalley brackets',r'[h_i,e_j]=-a_{ij}e_j,\ [h_i,f_j]=a_{ij}f_j,\ [e_i,f_i]=\delta_{ij}h_i',r'[h_i,e_j]=a_{ij}e_j,\ [h_i,f_j]=-a_{ij}f_j,\ [e_i,f_j]=\delta_{ij}h_i','The scan confirms the signs and repeated i; its later sl2 example fixes the intended convention. An internally consistent opposite convention would also require changing [e,f].')
correction('P000680','Serre relations and quotient','Only positive-generator relation and unrestricted maximal normal subalgebra','Include negative-generator Serre relations for i≠j; in the contragredient construction require the ideal to meet the Cartan subalgebra trivially','These conditions are absent or abbreviated in the notebook, not mistranscribed.',typ='ambiguity')
correction('P000680','loop-algebra notation',r'SU(3)\otimes\mathbb C[x,x^{-1}]',r'\mathfrak{sl}_3(\mathbb C)\otimes\mathbb C[x,x^{-1}]','The source is constructing complex Lie algebras; a compact Lie group is not a vector-space tensor factor.')
correction('P000678-P000680','session date','22 November 1976 throughout the packet','Date supplied by catalogue; the handwritten start is undated and the closing greeting says Happy New Year','Preserve date with provenance rather than infer additional sessions.',typ='provenance')

talk(409,'','-','P000680-P000681','YEAR 1977',
 r'''This catalogue record is the archival year heading between the late-1976 material and the dated Manin notes beginning on P000681. It supplies no independent mathematical statement. The wider catalogue packet P000679--P000681 contains the neighboring talks; no content is invented for the heading.''',kind='heading')
save()

talk(410,'1977-02-14','Yu. I. Manin','P000681-P000684','Spectral curves, rank-two solitons, and filtered bimodules',
 r'''Manin begins with a reference to Calogero's boomeron, then describes a fourth-order Lax system and an explicitly singular, periodically oscillating rank-two pulse. The algebraic part passes from commuting operators to a spectral curve and eigenfunction bundles, contrasts rank-one Jacobian motion with higher-rank bundle moduli, and gives the filtered-bimodule construction and its inverse. Two further connections yield evolution and zero-curvature equations. The material has an unusually close later match in Manin's 1978 survey, including a sign error in the flatness formula that survives into the printed English translation. The last sentence announces Duistermaat for the next meeting; it does not contain that lecture.''')

item(410,'P000681','remark','Calogero and the boomeron reference',
 r'''The opening reads \ru{Калоджеро: бумерон}, beside a sketch of a wave turning back. No equation or parameter identification is attached to this heading.''',
 r'''The identifiable bibliographical referent is the returning-soliton construction named ``boomeron'' by Calogero and Degasperis. The heading alone does not specify which member of their coupled evolution systems is intended, or identify it with the singular pulse subsequently displayed by Manin.''',
 r'''The sketch is read only as a change of propagation direction. The returning boomeron and Manin's periodically singular geyseron are not identified solely from their juxtaposition.''',
 r'''\citet{calogerodegasperis1976boomeron} appeared in the July 1976 issue and was received on 6 May 1976, before this lecture. The publisher's displayed 2008 date is online publication, not the original issue date. Only the publication metadata and title were checked, not an exact match of the subsequent formulas.''',
 'the named reference is identified, while the notebook supplies no separate mathematical assertion about its exact solution.',literal='not determinable',match='thematic only',verification='publisher metadata checked',refs=['calogerodegasperis1976boomeron'])

item(410,'P000681','claim','The fourth-order Lax commutator and two incorrect coefficients',
 r'''The notes set \(L=D^4+vD^2+wD+z\), \(P=D^2+AD+u\), \(D=\partial_x\), and \(L_t=[L,P]\). They print \(v_t=v_{xx}-Av_x-2w_x\), \(w_t=2v_{xxx}+2vv_x-w_{xx}-Aw_x-2z_x\), and the displayed third equation below.''',
 r'''For scalar smooth or meromorphic coefficients on a connected coordinate domain, write \([L,P]=LP-PL\). Absence of the \(D^4\) and \(D^3\) terms forces \(A_x=0\) and \(u=v/2+c_0(t)\). The equivalent system is
 \[\begin{aligned}v_t&=2v_{xx}-Av_x-2w_x,\\ w_t&=2v_{xxx}+vv_x-w_{xx}-Aw_x-2z_x,\\ z_t&=\tfrac12v_{xxxx}+\tfrac12vv_{xx}+\tfrac12wv_x-z_{xx}-Az_x.\end{aligned}\]
 The scalar summand \(c_0(t)\) commutes with \(L\) and has no effect.''',
 r'''The notebook's coefficient of \(v_{xx}\) is 1 instead of 2, and its coefficient of \(vv_x\) is 2 instead of 1. Both are legible in the scan and faithfully transcribed. They cannot both be explained by reversing the commutator or rescaling time. Independent Leibniz-rule expansion and application to a test exponential give the displayed correction; this is a critical annotation, not a new integrable-system result.''',
 r'''The same fourth/second-order system is printed with the correct relative coefficients in \citet[Chapter~III, \S1.5, pp.~79--80; \S6.3, equation~(17), p.~96]{manin1978algebraic}. That source uses \(L_t=[P,L]\) and explicit time/speed scale factors, so a convention change is needed before comparing the right-hand sides. The Russian survey appeared in 1978, the cited English translation in 1979.''',
 'the commutator expansion is settled; the two handwritten coefficients are false under the stated convention.',cls='A',literal='false as written',development='annotated',refs=['manin1978algebraic'])

item(410,'P000681','construction','The recorded rank-two pulse and the missing solution data',
 r'''With \(\xi=x+ct\), the notebook gives
 \[\mu_1=2\frac{\cosh2\xi-\cos2\xi+2\sin\sigma t}{\cosh2\xi+\cos2\xi-2\cos\sigma t},\qquad \mu_2=2\frac{\sinh2\xi-\sin2\xi}{\cosh2\xi+\cos2\xi-2\cos\sigma t},\]
 then \(v=-4\mu_{2x}\), \(\sigma w=4\mu_2\mu_{2x}+6\mu_{2xx}+4\mu_{1x}\). It omits \(z\), calling it inessential, and leaves the relation of \(\sigma\) to \(A\) unspecified.''',
 r'''The displayed expressions define meromorphic functions wherever their common denominator is nonzero. They do not, by themselves, specify a complete solution \((v,w,z)\) of a particular Lax system: \(z\), the parameter relation, and a consistent time/sign normalization must also be given. A complete rank-two one-soliton family with this hyperbolic/trigonometric structure is supplied in Manin's later construction.''',
 r'''No missing \(z\) or parameter relation is invented. In the printed family, writing \(\theta=4a^2\omega t\), the denominator is \(\cosh(2a\xi)+\cos(2a\xi)+2\cos\theta\), the prefactor of \(\mu_2\) is \(-2a\), and the formula is \(w=-6\mu_{2xx}-4\mu_{1x}+4\mu_2\mu_{2x}\). These differences prevent a literal formula-for-formula identification without an explicit change of variables, which the notes do not record.''',
 r'''\citet[Chapter~III, \S1.5, p.~80; \S6.4, equations~(18)--(22) and following display, p.~96]{manin1978algebraic} gives the construction and complete coefficients. The precise structural match supports identification of the family, while the recorded normalization and omitted component justify only a partial publication match.''',
 'the published family is established; the truncated notebook expression is not certified as a complete solution in its literal normalization.',cls='A',literal='not determinable',match='partial',refs=['manin1978algebraic'],confidence='medium')

item(410,'P000681','claim','Periodic singularities of the displayed denominator',
 r'''Beside the pulse sketch the notes say that every \(2\pi/\sigma\) it ``spits,'' with the names geyseron and shooting soliton, and describe explosive instability.''',
 r'''For real \(\xi,t\) and \(\sigma\ne0\), the notebook denominator \(\Delta=\cosh2\xi+\cos2\xi-2\cos\sigma t\) is nonnegative and vanishes exactly when \(\xi=0\) and \(\sigma t\in2\pi\mathbb Z\). At those times \(\mu_2=4/\xi+O(\xi^3)\), hence \(v=-4\partial_x\mu_2=16/\xi^2+O(\xi^2)\). The positive temporal period is \(2\pi/|\sigma|\).''',
 r'''The check follows from \(\cosh2\xi+\cos2\xi=2\sum_{j\ge0}(2\xi)^{4j}/(4j)!\). This verifies an actual pole of the recorded expression and its recurrence, but not nonlinear instability in a specified norm, which would require a perturbation theorem. For \(\sigma=0\), the formula instead has a persistent singular center and the stated period is undefined.''',
 r'''\citet[Chapter~III, \S1.5, p.~80]{manin1978algebraic} describes exactly the same qualitative geyser behavior for the published normalization, whose singular times are phase-shifted. The denominator and Laurent-series check here is independent of the omitted \(z\).''',
 'periodic pole formation in the displayed functions is verified; no stronger stability theorem is implied by the notebook wording.',cls='A',literal='correct with missing hypotheses',match='partial',development='annotated',refs=['manin1978algebraic'])

item(410,'P000681-P000682','method','Commuting operators, spectral curves, and eigenfunction sheaves',
 r'''Manin first constructs \([L_1,P_1]=0\), then solves \(L_1\psi=\lambda\psi\), \(P_1\psi=\mu\psi\) over an affine algebraic curve \(X\). The sketch puts the common-eigenfunction space over \((\lambda,\mu)\), and the next page extends the bundle to a completion.''',
 r'''For commuting scalar ordinary differential operators of positive orders over a differential field of characteristic zero with algebraically closed constant field, the Burchnall--Chaundy relation gives a nonzero polynomial \(Q\) over the constants with \(Q(L_1,P_1)=0\). On a component of the resulting spectral curve where the joint-eigenspace dimension is constant, these eigenspaces form the spectral bundle. Compactification and normalization, with a specified point at infinity and suitable local data, give the algebro-geometric spectral data. At singularities one must allow a torsion-free sheaf rather than automatically a vector bundle.''',
 r'''The scalar, constant-field, generic-rank and completion qualifications are supplied. The sketch is a fibre diagram, not evidence that every singular joint spectrum has an everywhere locally free eigenbundle. The matrix-coefficient case later in the talk is handled through the bimodule axioms, not by an unrestricted extension of the scalar theorem.''',
 r'''\citet[\S2, proposition on p.~293]{krichever1976zakharov} already states the polynomial relation and rank-one inverse construction; it was received 8 October and presented 24 October 1975, then published in 1976. \citet[Theorem~1.1, pp.~176--177]{krichever1978commutative} explicitly attributes the relation to Burchnall and Chaundy. This continues earlier item 1975-391.1.''',
 'the qualified spectral-curve method is established; the singular-fibre caveat remains necessary.',refs=['krichever1976zakharov','krichever1978commutative'])

item(410,'P000682','theorem','Rank-one evolution as translation on the Jacobian',
 r'''For a one-dimensional common-eigenfunction space the page writes \(t\longrightarrow\) a path on the Jacobian. The previous page identifies the rank-one restriction in Krichever's construction.''',
 r'''Let \(C\) be a smooth projective complex curve, \(p_\infty\) a marked point with local coordinate, and choose nonspecial rank-one Baker--Akhiezer divisor data. The commuting flows associated with prescribed principal parts at \(p_\infty\) evolve the degree-zero class of the spectral line bundle by \(a(t)=a(0)+tU\) in \(\operatorname{Jac}(C)\), where \(U\) is determined by the corresponding normalized second-kind differential. Several commuting times give a sum of such translations. The local reconstruction is used away from its exceptional theta divisor.''',
 r'''The notebook says only ``path''; linear translation and the hypotheses are the precise established rank-one statement. Identifying \(\operatorname{Pic}^d(C)\) with the Jacobian requires a reference line bundle. This is not asserted for every path of arbitrary higher-rank bundles.''',
 r'''The rank-one construction is already \citet[\S1, Theorem~1 and Corollaries~1--2]{krichever1976zakharov}; \citet[Chapter~III, \S4, especially the concluding Jacobian linearization]{manin1978algebraic} presents the corresponding bimodule proof. The topic continues the earlier rank-one inverse problem GP-1975-14.''',
 'the rank-one linearization is established under the stated spectral-data hypotheses.',refs=['krichever1976zakharov','manin1978algebraic'])

higher_id=item(410,'P000681-P000682','question','The recurring higher-rank inverse construction',
 r'''The notes contrast \(\dim\{\psi\}=1\) with \(r>1\), refer to Drinfeld's nonexplicit description and difficulties, and replace the Jacobian by a moduli space of bundles. They do not give a higher-rank reconstruction formula here.''',
 r'''The precise recurring inverse problem is to recover commuting scalar ordinary differential operators of generic spectral rank \(r>1\) from appropriate pointed-curve and rank-\(r\) spectral-bundle data. In the nonsingular-curve, general-position setting, one must include a local parameter, a normalized matrix divisor (Tyurin data), and the additional functional parameters; the curve and an unframed bundle alone do not determine the operators.''',
 r'''The inverse-problem formulation is reconstructed from the contrast with the preceding construction and from earlier occurrences 1975-391.3--4. It is narrower than a claim that every holomorphic path in every bundle-moduli space yields a Lax solution. The data and genericity here follow the later effective reconstruction, not an unrecorded theorem attributed to Manin.''',
 r'''\citet[Proposition~2]{drinfeld1977commutative}, received 14 April 1976 and printed in the first 1977 issue, gives the abstract geometric correspondence; the precise public issue date relative to 14 February is not established. \citet[\S2, Lemma~2.2 and Theorem~2.3, pp.~181--182]{krichever1978commutative} gives an effective reconstruction for smooth spectral curves in general position. Its introduction expressly corrects serious errors in the 1977 implementation; it was submitted 15 February 1977, the day after this talk, and printed in 1978. The class B assignment refers to that effective reconstruction by another author, not to discovery of the older abstract correspondence.''',
 'the stated generic inverse problem is solved. Singular spectral curves, special strata, and global real regularity are separate questions, not residual open claims assigned to this notebook.',cls='B',literal='not determinable',match='partial',problem='GP-1975-26',refs=['drinfeld1977commutative','krichever1978commutative'],confidence='medium')
problems.append(dict(id='GP-1975-26',title='Reconstructing higher-rank commuting ordinary differential operators',
 statement=r'''Recover a commuting algebra of scalar ordinary differential operators of generic spectral rank \(r>1\) from correctly normalized pointed-curve, spectral-bundle and local functional data, at least for smooth spectral curves and data in general position. A curve and an unframed bundle alone are not sufficient input.''',
 occurrences=['1975-391.3','1975-391.4',higher_id],
 status=r'''As of November 2026, the generic smooth-curve inverse problem is solved by the abstract Drinfeld correspondence and Krichever's effective reconstruction. \citet[Theorem~2.3]{krichever1978commutative} corrects the earlier 1977 implementation; its received date is 15 February 1977. No claim of a complete classification of all singular or globally regular real cases is attached to this occurrence.''',
 status_date='2026-11',refs=['drinfeld1977commutative','krichever1978commutative']))

item(410,'P000682','claim','Hyperelliptic curves and the two-quadrics shorthand',
 r'''Immediately after the higher-rank moduli remark, the page says \ru{Гиперэлл. кривая} \(\longrightarrow\) \ru{пересеч. 2-х квадрик в} \(\mathbb C^5\). It does not specify a genus, rank, determinant, or which moduli space the arrow denotes.''',
 r'''A precise plausible referent is the classical theorem that for a smooth projective complex curve \(C\) of genus two and a fixed line bundle \(\Lambda\) of odd degree, the moduli space of stable rank-two bundles with determinant \(\Lambda\) is a smooth intersection of two quadrics in \(\mathbb P^5\). The notebook does not supply enough data to identify that theorem uniquely, and it writes affine \(\mathbb C^5\), not projective \(\mathbb P^5\).''',
 r'''Genus two, rank two, fixed odd determinant, stability, and projective ambient space are all candidate reconstruction, not recovered words. A general hyperelliptic curve is not itself a three-dimensional intersection of two quadrics. An affine chart of the classical moduli threefold could explain \(\mathbb C^5\), but no chart is specified.''',
 r'''\citet[\S10, p.~546]{ramanan1980vector} states the hyperelliptic moduli/quadric construction and explicitly attributes the genus-two case to Newstead (1968) and Narasimhan--Ramanan (1969); the publisher metadata for \citet{narasimhanramanan1969moduli} was also checked. This is a strong historical candidate, not an exact identification of the under-specified arrow.''',
 'the candidate classical theorem is settled, but the precise object intended by this notebook shorthand remains uncertain.',cls='F',literal='not determinable',match='thematic only',refs=['ramanan1980vector','narasimhanramanan1969moduli'],confidence='medium',area='Algebraic geometry')

item(410,'P000682','question','The unqualified question about analytic paths',
 r'''The separate two-word question \ru{Аналит. пути?} follows the moduli and two-quadrics remarks.''',
 r'''No definite analytic-path problem is specified: the notes give neither a vector field, an initial condition, a regularity category, a domain of continuation, nor a chosen moduli stratum. The question cannot be assigned a precise existence, integrability, or completeness assertion from this wording alone.''',
 r'''It may concern explicit higher-rank flows on a bundle-moduli space, but that interpretation is not enough to select one theorem. In particular, generic local reconstruction and global nonsingular continuation are different mathematical questions.''',
 r'''The neighboring sources \citet[Chapter~III, \S\S1.4, 3--6]{manin1978algebraic} and \citet[\S\S2--3]{krichever1978commutative} discuss higher-rank construction and bundle deformations, but neither provides an exact identifiable target for the isolated wording. No open-problem status is inferred from failure of identification.''',
 'the intended analytic question is unidentified; this is not evidence for an unresolved theorem.',cls='F',literal='not determinable',match='thematic only',verification='unresolved lead',refs=['manin1978algebraic','krichever1978commutative'],confidence='low')

item(410,'P000682','method','Nodal spectral curves and soliton solutions',
 r'''The notes describe a soliton as a nonstationary solution obtained by using a stationary spectral curve with one double point and distinct tangents.''',
 r'''In the algebro-geometric soliton construction, a rational spectral curve with an ordinary node is obtained by identifying two distinct smooth points of its normalization. A spectral line bundle, or higher-rank bundle with specified gluing matrix, together with marked-point asymptotics and compatible commuting connections, can produce one-soliton-type solutions. More nodes give corresponding gluing parameters and multisoliton families. The node alone does not determine a solution or ensure real nonsingularity.''',
 r'''The normalization, gluing, spectral data and compatibility assumptions are supplied to replace the overbroad descriptive definition. The actual double point in the note has two branches; a cusp would require a different local construction.''',
 r'''\citet[Chapter~III, \S1.4; \S5, especially \S\S5.1--5.5 and 5.12; \S6.1]{manin1978algebraic} gives the precise nodal gluing construction and identifies the number of pairs of glued points with the soliton count. The rank-one degeneration was older; this class A entry concerns the rank-two/matrix construction being explained by the speaker and published in his 1978 survey.''',
 'the stated spectral-data construction is established; the literal node-only criterion needs the additional data and admissibility conditions.',cls='A',match='partial',refs=['manin1978algebraic'])

item(410,'P000682','definition','Differential-operator algebra and compatible evolution conventions',
 r'''The algebraic setting is a characteristic-zero field \(k\), a \(k\)-algebra \(\mathcal B\), and commuting derivations \(\partial,\partial_1,\partial_2\). The analytic example is \(M_\ell(\mathcal B_0)\), with meromorphic coefficients. The notebook lists stationary Lax, nonstationary Lax and Zakharov--Shabat equations.''',
 r'''Let \(\mathcal B\) be a unital associative central \(k\)-algebra with commuting \(k\)-derivations \(d,d_1,d_2\). The Ore algebra \(\mathcal B[D;d]\) consists of finite sums \(\sum b_jD^j\), with multiplication fixed by \(Db=bD+d(b)\). The derivations \(d_i\) extend coefficientwise and satisfy \(d_iD=0\). Stationarity is \([L,P]=0\). With the later connection convention \(\nabla_1\mathbf1=P\mathbf1\), \(\nabla_2\mathbf1=L\mathbf1\), the compatible equations are \(d_1L=[P,L]\) and \(d_1L-d_2P=[P,L]\).''',
 r'''The Ore multiplication rule is made explicit, especially because matrix coefficients need not commute. The notebook's initial \(d_1L=[L,P]\) is another admissible convention after replacing the evolution operator by its negative, but it cannot be mixed unchanged with the later positive connection definitions. The derivative-plus sign in its third equation is corrected in the final item.''',
 r'''The algebraic setup is exactly \citet[Chapter~III, \S2.1, p.~81]{manin1978algebraic}; the connections are treated in Theorems~2.5--2.6. This packages older Lax and zero-curvature equations into the speaker's subsequent bimodule exposition.''',
 'the algebra and the convention-dependent equations are established; a consistent choice of signs is necessary.',cls='A',literal='correct with missing hypotheses',match='exact',development='annotated',refs=['manin1978algebraic'])

item(410,'P000682-P000683','definition','Krichever--Drinfeld filtered bimodules',
 r'''The structures are a left \(\mathcal B\)-module and right \(\mathcal O\)-module \(\mathcal M\), a distinguished \(\mathbf1\), an exhaustive filtration, and a connection \(\nabla\). The actions are faithful and commute; \(\mathcal M_{-1}=0\), \(\mathcal M_0=\mathcal B\mathbf1\), and every graded piece has rank one. The final line gives \(i\ge-1\) for both the filtration inclusion and the induced isomorphism.''',
 r'''Take \(\mathcal O\) to be the coordinate ring of a geometrically integral affine curve over \(k\). Require commuting faithful left \(\mathcal B\) and right \(\mathcal O\) actions, an exhaustive filtration by left submodules \(0=\mathcal M_{-1}\subset\mathcal M_0\subset\cdots\), with \(\mathbf1\) a free generator of \(\mathcal M_0\), and each \(\mathcal M_i/\mathcal M_{i-1}\) free of rank one for \(i\ge0\). Require \(\nabla(bm)=d(b)m+b\nabla m\), \(\nabla(m\varphi)=(\nabla m)\varphi\), \(\nabla\mathcal M_i\subset\mathcal M_{i+1}\), and induced isomorphisms \(\mathcal M_i/\mathcal M_{i-1}\to\mathcal M_{i+1}/\mathcal M_i\) for \(i\ge0\).''',
 r'''The induced maps on graded pieces are \(\mathcal B\)-linear because the extra Leibniz term drops to the lower filtration level. The isomorphism cannot start at \(i=-1\): its source would be zero (or involve an undefined \(\mathcal M_{-2}\)) while its target is \(\mathcal M_0\ne0\). The degree-raising inclusion alone is harmless at \(-1\).''',
 r'''These are the structures and axioms of \citet[Chapter~III, \S2.2, p.~81]{manin1978algebraic}, a close publication match to the notebook. The induced-isomorphism range is interpreted as \(i\ge0\); no nonexistent initial graded isomorphism is retained.''',
 'the corrected axioms give the filtered differential-module model used in the reconstruction theorem.',cls='A',literal='false as written',development='annotated',refs=['manin1978algebraic'])

item(410,'P000683','construction','The regular bimodule attached to commuting operators',
 r'''For commuting \(L,P\), with \(\bar k[L,P]\) having no zero divisors, the notes put \(\mathcal M=\mathcal B[D]\), \(\mathcal O=k[L,P]\), use left and right multiplication, filter by order, and set \(\nabla Q=DQ\).''',
 r'''Given an injective \(k\)-algebra homomorphism \(i:\mathcal O\hookrightarrow\mathcal B[D;d]\), where \(\mathcal O\) is the coordinate ring of a geometrically integral affine curve, take \(\mathcal M=\mathcal B[D;d]\), left multiplication by \(\mathcal B\), right multiplication by \(i(\mathcal O)\), \(\mathbf1=1\), \(\mathcal M_i=\{\sum_{j=0}^i b_jD^j\}\), and \(\nabla Q=DQ\). These satisfy all the preceding axioms.''',
 r'''For the special choice \(\mathcal O=k[L,P]\), one must also ensure that it is an affine curve ring. Absence of zero divisors alone is not enough: taking scalar constant \(L,P\) gives dimension zero. Assuming a geometrically integral curve algebra at the outset avoids claiming an unjustified transcendence-degree assertion for arbitrary matrix operators.''',
 r'''This is exactly \citet[Chapter~III, \S2.2, p.~81]{manin1978algebraic}, which starts from an embedding of an already specified affine curve ring. The printed formulation supplies the missing dimension hypothesis in the notebook shorthand.''',
 'the construction is established with the curve-algebra hypothesis; the domain condition by itself is insufficient.',cls='A',literal='correct with missing hypotheses',development='annotated',refs=['manin1978algebraic'])

item(410,'P000683','theorem','Recovering the commuting algebra from a cyclic filtered module',
 r'''The first theorem recovers an embedding \(\mathcal O\to\mathcal B[D]\) from the bimodule. The diagrams first identify differential operators generated by \(\mathcal B\) and \(\nabla\), then define \(L_\varphi\mathbf1=\mathbf1\varphi\).''',
 r'''For a bimodule satisfying the corrected axioms above, the map \(\mathcal B[D;d]\to\mathcal M\), \(Q\mapsto Q(\nabla)\mathbf1\), is an isomorphism of filtered left modules. For every \(\varphi\in\mathcal O\) there is a unique \(L_\varphi\) with \(L_\varphi\mathbf1=\mathbf1\varphi\); the map \(\varphi\mapsto L_\varphi\) is an injective \(k\)-algebra homomorphism, and the regular-bimodule construction recovers \(\mathcal M\).''',
 r'''The filtration shows inductively that \(\mathbf1,\nabla\mathbf1,\ldots,\nabla^i\mathbf1\) form a left \(\mathcal B\)-basis of \(\mathcal M_i\); this proves existence and uniqueness rather than assuming cyclicity. Right \(\mathcal O\)-linearity of \(\nabla\) makes the right action commute with every differential operator, and faithfulness proves injectivity. The diagrams express these maps; no extra unrecorded geometric correspondence is needed.''',
 r'''The notebook's Theorem~1 becomes \citet[Chapter~III, Theorem~2.4, pp.~82--83]{manin1978algebraic}, including the observation that the cyclic-module part does not use \(\mathcal O\). This is an exact later publication of the speaker's presentation.''',
 'the algebraic reconstruction is established for the stated axioms.',cls='A',literal='correct',refs=['manin1978algebraic'])

item(410,'P000683','theorem','A second connection produces Lax evolution',
 r'''The second theorem introduces \(\nabla_1\) commuting with \(\nabla\) and the right \(\mathcal O\)-action, puts \(\nabla_1\mathbf1=P\mathbf1\), and indicates a Lax equation with an uncertain commutator sign. Its written Leibniz line is \(\nabla_1(bm)=\partial_1b+\nabla_1m\), omitting both multiplicative factors.''',
 r'''Let \(d_1\) commute with \(d\), and let \(\nabla_1\) satisfy \(\nabla_1(bm)=d_1(b)m+b\nabla_1m\), \([\nabla_1,\nabla]=0\), and right \(\mathcal O\)-linearity. Define \(P\) by \(\nabla_1\mathbf1=P\mathbf1\). Then every recovered \(L_\varphi\) satisfies \(d_1L_\varphi=[P,L_\varphi]\).''',
 r'''Applying \(\nabla_1\) to \(L_\varphi\mathbf1=\mathbf1\varphi\) gives \((d_1L_\varphi+L_\varphi P)\mathbf1=PL_\varphi\mathbf1\); cyclic freeness removes \(\mathbf1\). This fixes the sign for the stated convention. The earlier notebook convention \(d_1L=[L,P]\) requires replacing its evolution operator by \(-P\). The missing Leibniz factors are a faithful error, not a translation issue.''',
 r'''This is \citet[Chapter~III, Theorem~2.5, p.~83]{manin1978algebraic}, with the exact sign \([P,L_\varphi]\) verified in the printed formula and proof.''',
 'the theorem is established after restoring the Leibniz rule and fixing the evolution-operator convention.',cls='A',literal='false as written',development='annotated',refs=['manin1978algebraic'])

item(410,'P000684','theorem','Three commuting connections and the shared zero-curvature sign error',
 r'''The third theorem drops all mention of \(\mathcal O\), assumes pairwise commuting \(\nabla,\nabla_1,\nabla_2\), puts \(\nabla_1\mathbf1=P\mathbf1\), \(\nabla_2\mathbf1=L\mathbf1\), and writes \(\partial_2P+\partial_1L=\pm[L,P]\). Both the plus sign and the explicit sign uncertainty are visible in the scan.''',
 r'''Let the filtered left \(\mathcal B\)-module, cyclic element and \(d\)-connection satisfy the preceding axioms with \(\mathcal O\) omitted. Let \(d,d_1,d_2\) commute and let their connections \(\nabla,\nabla_1,\nabla_2\) commute pairwise. Define \(P,L\) by the notebook's two equations. Then
 \[d_1L-d_2P=[P,L].\]
 Equivalently, \([d_1-P,d_2-L]=0\) as differential operators acting on a common auxiliary wavefunction.''',
 r'''On the cyclic vector, flatness gives \(0=(d_1L+LP-d_2P-PL)\mathbf1\). Thus the derivative terms have opposite signs, and the bracket sign is fixed. As a concrete check, take \(\mathcal B=k[t,z]\), \(d=0\), \(\mathcal M=\mathcal B[D]\), \(\nabla=D\), \(\nabla_1=\partial_t+R_z\), \(\nabla_2=\partial_z+R_t\), where \(R\) is right multiplication. These connections commute and give \(P=z,L=t\); the correct difference is zero, whereas the notebook's sum is 2 and either commutator sign is zero.''',
 r'''\citet[Chapter~III, Theorem~2.6, p.~83]{manin1978algebraic} is an exact structural match, but its printed English statement also has a plus sign: with its swapped labels \(\nabla_1\mathbf1=L\mathbf1\), \(\nabla_2\mathbf1=P\mathbf1\), it prints \(d_1P+d_2L=[P,L]\). Its own flatness proof requires \(d_1P-d_2L=[L,P]\). The scan of that printed page was inspected. Thus publication confirms the theorem's provenance but does not validate the literal formula; this is a faithful error shared by the notebook and the cited translation.''',
 'the corrected flatness identity is established; the literal plus-sign formula is false even for scalar commuting multiplication operators.',cls='A',literal='false as written',development='annotated',refs=['manin1978algebraic'])

correction('P000681','fourth-order Lax system',r'v_t=v_{xx}-Av_x-2w_x;\quad w_t=2v_{xxx}+2vv_x-w_{xx}-Aw_x-2z_x',r'v_t=2v_{xx}-Av_x-2w_x;\quad w_t=2v_{xxx}+vv_x-w_{xx}-Aw_x-2z_x','Both coefficients are confirmed by the handwritten scan. Independent Ore-product and test-function calculations agree; Manin ChapterIII§6 equation17 has the corrected relative coefficients.')
correction('P000681','pulse normalization and omitted component',r'\sigma w=4\mu_2\mu_{2x}+6\mu_{2xx}+4\mu_{1x};\quad z=\ldots','Retain the recorded formula; do not certify it as a complete solution without z and a parameter/sign convention','Manin printedp80 gives a closely related but differently signed/scaled family. No unique emendation is justified from this excerpt.',typ='ambiguity')
correction('P000681','positive recurrence period',r'2\pi/\sigma',r'2\pi/|\sigma|\quad(\sigma\ne0)','The page allows any real sigma; positive temporal period requires absolute value and excludes zero.')
correction('P000682','two-quadrics ambient and missing data',r'\text{hyperelliptic curve}\longrightarrow\text{two quadrics in }\mathbb C^5','Retain as ambiguous; a plausible candidate is the genus-two rank-two fixed odd-determinant moduli space in projective P5','Actual scan says C5. The classical moduli theorem has further hypotheses absent from the note; affine-chart interpretation is possible but unrecorded.',typ='ambiguity')
correction('P000683','graded connection isomorphism lower bound',r'i\ge-1',r'i\ge0\text{ for the induced graded isomorphism}',r'At \(i=-1\) the source graded piece is zero or undefined while the target is \(M_0\), a free rank-one module. The mere inclusion \(\nabla M_i\subset M_{i+1}\) may include \(i=-1\).')
correction('P000683','Theorem2 module order',r'(\mathcal O,\mathcal B)\text{-bimodule}',r'(\mathcal B,\mathcal O)\text{-bimodule}','The preceding definitions and subsequent formulas use a left B-action and right O-action; the reversed order is visible in the scan.')
correction('P000683','Theorem2 Leibniz rule',r'\nabla_1(bm)=\partial_1b+\nabla_1m',r'\nabla_1(bm)=(\partial_1b)m+b\nabla_1m','The scan visibly omits both factors; the printed Manin theorem assumes a connection, hence the full Leibniz rule.')
correction('P000683','Theorem2 commutator sign',r'\partial_1L_\varphi=\pm[L_\varphi,P]',r'\partial_1L_\varphi=[P,L_\varphi]\text{ when }\nabla_1\mathbf1=P\mathbf1',r'Direct application of the connection to \(L_\varphi\mathbf1=\mathbf1\varphi\) fixes the sign; Manin Theorem 2.5, printed p. 83, agrees.',typ='ambiguity')
correction('P000682; P000684','zero-curvature derivative and bracket signs',r'\partial_1L+\partial_2P=\pm[L,P]',r'\partial_1L-\partial_2P=[P,L]\text{ for }\nabla_1\mathbf1=P\mathbf1,\ \nabla_2\mathbf1=L\mathbf1','The plus sign is faithful to the scan. Flatness expansion and the scalar counterexample P=z,L=t disprove it. Manin Theorem2.6 printedp83 repeats a plus-sign error under swapped labels.')
save()

# Continuity links are matched at statement level; they do not invent new
# occurrences of a previous open problem when only its surrounding topic recurs.
prior_links={
 '1976-406.2':['1975-389.1'], '1976-406.3':['1975-389.1'],
 '1976-406.4':['1975-389.3'], '1976-406.6':['1975-389.7'],
 '1976-406.11':['1975-389.2'],
 '1976-408.1':['1975-366.1'], '1976-408.2':['1975-366.2'],
 '1976-408.3':['1975-366.1'], '1976-408.4':['1975-366.3','1975-370.3'],
 '1976-408.6':['1975-366.4','1975-370.18'],
 '1976-408.8':['1975-366.5','1975-370.15'],
 '1976-410.5':['1975-391.1'],
 '1976-410.6':['1975-384.3','1975-385.8'],
 '1976-410.7':['1975-391.3','1975-391.4'],
 '1976-410.12':['1975-385.1'],
 '1976-410.14':['1975-383.10'],
}
for x in items:
 if x['id'] in prior_links:
  links=', '.join(prior_links[x['id']])
  x['reconstruction']+=' Earlier-index continuity: '+links+'. These links identify a recurring statement or construction; only the explicitly indexed inverse problem reuses a problem ID.'
save()
meta=json.loads((WORK/'middle_meta.json').read_text())
meta.update(prior_occurrence_links=prior_links,
            required_record_coverage={str(r):'present' for r in range(406,411)},
            item_counts=dict(Counter(str(x['record']) for x in items)),
            heading_records=[409],
            scan_boundaries=['P000670: factors fragment precedes dated Bernstein heading',
              'P000673--674: retrospective Dorfman-notebook recap explicitly labelled',
              'P000675: dated Popov heading; initials attribution conflict retained',
              'P000678: undated Bernstein start; catalogue date retained with provenance',
              'P000680--681: archival YEAR 1977 heading, no mathematical item',
              'P000681: dated 14 February 1977 Manin start',
              'P000684: Manin ends; announcement of Duistermaat is not his lecture'],
            decision_on_development='No class C or D problem identified. Critical formula checks are annotations, not claimed research developments.')
(WORK/'middle_meta.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')

