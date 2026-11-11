"""Supplement only: never add these records to the core 649--657 files/counts."""
from pathlib import Path
import json,re,csv
OUT=Path(__file__).resolve().parent
adj=[]
def add(record,kind,title,notes,statement,reconstruction,fate,status,refs,
        cls='E',literal='correct with missing hypotheses',match='partial',
        verification='read the result',development='none',confidence='high'):
    n=1+sum(x['record']==record for x in adj)
    adj.append(dict(id=f'ADJ-{record}.{n}',record=record,
        pages='P001258' if record==667 else 'P001259',kind=kind,title=title,
        notes=notes,statement=statement,reconstruction=reconstruction,
        **{'class':cls},fate=fate,present_status='As of November 2026: '+status,
        literal_correctness=literal,publication_match=match,verification=verification,
        development=development,problem='',worth='',refs=list(refs),confidence=confidence))

add(667,'definition','A curve with a point and a formal parameter is not unmarked Teichmueller space',
 r'''Kontsevich's page calls \(M_g\) Teichm\"uller space and writes \(\widetilde M_g=(C,p,x)\), where \(x\) is a coordinate at \(p\).''',
 r'''For \(g\ge2\), let \(\widehat{\mathcal M}_{g,1}\) parameterize smooth connected projective complex curves \(C\) of genus \(g\), a point \(p\), and a formal parameter \(x\in\widehat{\mathfrak m}_p\) with nonzero first derivative. It is the inverse limit of the finite-jet moduli spaces. Forgetting \(x\) gives pointed moduli \(\mathcal M_{g,1}\); forgetting both \(p,x\) gives \(\mathcal M_g\). A topological marking would instead place these constructions over Teichm\"uller space.''',
 r'''The triple records no topological marking. We use a moduli stack or a local smooth cover rather than silently identify it with Teichm\"uller space. A formal parameter need not be a convergent analytic coordinate on a fixed disk.''',
 r'''\citet[\S1]{kontsevich1987virasoro} explicitly constructs these finite-jet moduli and their inverse limit. The paper was submitted 3 December 1986 and published in issue 2 of 1987.''',
 r'''The objects are identifiable standard deformation-theoretic data (E). The notebook's two uses of the word Teichm\"uller require this distinction.''',('kontsevich1987virasoro',),match='exact')
add(667,'definition','Formal local vector fields and the curve-dependent global subalgebra',
 r'''The page defines \(\mathfrak g=\mathbb C((x))\partial_x\), \(\mathfrak k=\mathbb C[[x]]\partial_x\), and \(\gamma\) as Laurent expansions of vector fields on \(C\) with a pole only at \(p\).''',
 r'''Set \(\gamma_{C,p,x}=H^0(C,T_C(*p))\subset\mathbb C((x))\partial_x\) by Laurent expansion. Its elements are algebraic vector fields on \(C\setminus\{p\}\), meromorphic on \(C\) with finite pole order at \(p\). The local subalgebra \(\mathfrak k\) consists of fields regular on the formal disk, while \(\mathfrak k_0=x\mathbb C[[x]]\partial_x\) consists of fields fixing its marked origin.''',
 r'''The space \(\gamma\) depends on the curve and parameter; \(\mathfrak k\) does not. The marginal phrase \ru{всю C!!} cannot mean holomorphic extension through \(p\): for \(g\ge2\), \(H^0(C,T_C)=0\), whereas meromorphic fields with allowed pole order are essential here.''',
 r'''These subalgebras and the global punctured-curve condition are defined in \citet[\S1]{kontsevich1987virasoro}.''',
 r'''The finite-pole global subalgebra is exactly identified (E). The ambiguous marginal instruction is retained as provenance rather than imposed as a false extra condition.''',('kontsevich1987virasoro',),match='exact',development='annotated')
add(667,'theorem','Virasoro uniformization: the infinitesimal action and stabilizer',
 r'''Theorem1 says \(\mathfrak g\) acts on \(\widetilde M_g\), with stabilizer \(\gamma\), so it is locally the homogeneous space \(\mathfrak g/\gamma\).''',
 r'''For the moduli of smooth genus-\(g\ge2\) pointed curves with a formal parameter, the Lie algebra \(\operatorname{Der}\mathbb C((x))\) acts infinitesimally. At \((C,p,x)\), evaluation of that action is surjective and its kernel is \(H^0(C,T_C(*p))\). Thus \(T_{(C,p,x)}\widehat{\mathcal M}_{g,1}\cong\mathbb C((x))\partial_x/\gamma_{C,p,x}\), in the formal inverse-limit sense.''',
 r'''This is an infinitesimal uniformization theorem. It does not assert the existence of an ordinary global Lie group, a single fixed subgroup for all curves, or a global homogeneous-space presentation. The completed formal setting and genus hypothesis are supplied.''',
 r'''Exact match to \citet[\S1, proposition and preceding tangent formula]{kontsevich1987virasoro}. The paper credits independent results of Beilinson and Schechtman. Publication in 1987 follows either the manuscript's 1985 heading or the catalogue's February1987 date; the latter conflict is not resolved by the mathematics.''',
 r'''Published soon after by the speaker (A), with the precise infinitesimal meaning verified in the primary paper.''',('kontsevich1987virasoro',),cls='A',match='exact')
add(667,'method','A meromorphic lift of a one-parameter deformation',
 r'''For a one-parameter family the notebook chooses a connection with poles only at the section \(p\), locally \(\nabla_t=\partial_t+F(x,t)\partial_x\).''',
 r'''Locally on a smooth one-dimensional base, a family of smooth projective curves with section admits a lift of the base tangent vector to a relative meromorphic vector field after allowing a sufficiently high finite pole order along that section. In a formal trivialization it has the written form. Two such lifts differ by a relative vertical meromorphic field; at a fixed fiber their difference belongs to \(\gamma_{C,p,x}\).''',
 r'''Allowing a sufficiently large pole divisor kills the relevant first cohomology by Serre vanishing, giving local existence. This is a noncanonical local lift, not a globally chosen holomorphic connection. Its ambiguity explains the quotient by \(\gamma\). The notebook neither fixes a pole order nor proves uniqueness.''',
 r'''This is the deformation-theoretic interpretation of \citet[\S1]{kontsevich1987virasoro}; the article states the equivalent Kodaira--Spencer and Laurent-field description rather than this exact local connection formula.''',
 r'''The construction is explained within the established infinitesimal uniformization. It is E as deformation-theoretic machinery, with a partial publication match rather than a claim of a separately stated theorem.''',('kontsevich1987virasoro',),development='annotated')
add(667,'claim','The erroneous g/k tangent quotient and the two forgetting maps',
 r'''One line says \(T\widetilde M_g=\mathfrak g/\mathfrak k\), but the following display divides instead by fields extending to \(C\setminus\{p\}\).''',
 r'''The tangent space with full formal parameter is \(\mathfrak g/\gamma\). The tangent space of unpointed moduli is \(\mathfrak g/(\gamma+\mathfrak k)\cong H^1(C,T_C)\), of complex dimension \(3g-3\). The tangent space of pointed moduli is \(\mathfrak g/(\gamma+\mathfrak k_0)\cong H^1(C,T_C(-p))\), of dimension \(3g-2\). The intermediate quotient \(\mathfrak g/\mathfrak k\) is merely the space of formal principal parts; it is not any of these complete tangent spaces.''',
 r'''These formulas follow from the two-open-set formal gluing calculation: changes of the trivialization on the punctured curve contribute \(\gamma\), while those on the disk contribute \(\mathfrak k\) or \(\mathfrak k_0\) depending on whether its center is remembered. They also distinguish \(\operatorname{Der}\mathbb C[[x]]\) from the Lie algebra \(x\mathbb C[[x]]\partial_x\) of formal coordinate changes fixing the point.''',
 r'''\citet[\S1]{kontsevich1987virasoro} gives the full-parameter tangent formula and notes that regular formal fields act transitively along the fibers of forgetting the point and parameter. The two finite-dimensional cohomology quotients are the explicit editorial reconstruction.''',
 r'''The first written quotient is false (E correction); the next display contains the intended curve-dependent stabilizer. No open deformation problem remains.''',('kontsevich1987virasoro',),literal='false as written',match='exact',development='annotated')
add(667,'theorem','The central extension lifts to determinant-of-cohomology lines',
 r'''The final lines say that the Virasoro central extension acts in the determinant bundle \(d_k\) pulled back from \(M_g\) to \(\widetilde M_g\).''',
 r'''For an integer \(k\), let \(\lambda_k(C)=\det H^0(C,K_C^k)\otimes\det H^1(C,K_C^k)^{-1}\). The infinitesimal Laurent-vector-field action lifts to a Virasoro central extension acting by first-order differential operators on the pullback of \(\lambda_k\) to curves with a formal parameter. Relative to the determinant extension for \(k=0\) (equivalently \(k=1\)), its cocycle class is multiplied by \(6k^2-6k+1\). The numerical central charge changes with central-generator and dual-line conventions.''',
 r'''The notebook does not define \(d_k\); identifying it with \(\lambda_k\) is the exact source-based reconstruction. A Lie algebra action on sections with nontrivial central action is not an ordinary action of the center-free algebra on the base. No particular scalar central charge is assigned without declaring the cocycle normalization.''',
 r'''\citet[\S\S2--3]{kontsevich1987virasoro} constructs the determinant extension on the Laurent-space Grassmannian and pulls it back to the curve moduli. Section3 supplies the coefficient and the corresponding cancellation corollary.''',
 r'''Published by the speaker in 1987 (A). The determinant-line action is verified directly; no unrelated later Kontsevich-model claim is attached to the page.''',('kontsevich1987virasoro',),cls='A',match='exact')

add(668,'theorem','The critical bosonic measure and the exponent13',
 r'''Morozov, under ``Consequences of the Belavin--Knizhnik theorem'', summarizes Beilinson's talk and writes a sum over genera with measure \(|d\mu_p|^2/(\det\operatorname{Im}T)^{13}\), multiplied by a vertex factor \(K\{V\}\).''',
 r'''For a smooth compact Riemann surface of fixed genus \(p\ge2\), the gauge-fixed critical bosonic vacuum measure can be expressed locally as \(|\mu_p|^2/(\det\operatorname{Im}\tau)^{13}\), where \(\tau\) is the period matrix in a symplectic marking and \(\mu_p\) is the corresponding holomorphic Mumford form, a section of the determinant-line combination \(\lambda_2\otimes\lambda_1^{-13}\). Insertions require the associated normalized matter/ghost correlation factor and their integration data.''',
 r'''This is a fixed-genus determinant identity with specified zero modes. The infinite genus sum and integration near degenerating curves are not proved convergent. Genus0 and1 have automorphisms and additional special zero-mode conventions, so they are not covered by silently repeating the same formula. The scan confirms the exponent13.''',
 r'''\citet[\S\S2--5, especially (2.19), (3.4), and (5.1)]{belavinknizhnik1986complex} proves the determinant-line/holomorphy statement and discusses degeneration poles. The paper cites its own Landau Institute1985 preprint; the full article was submitted18February1986 and publishedAugust1986.''',
 r'''Exposition of already circulating work (E), explicitly credited in the notebook. The recorded theorem does not justify a finite total string partition function.''',('belavinknizhnik1986complex',),match='exact')
add(668,'method','World sheets, topology, and replacing external circles by punctures',
 r'''Two sketches show a propagating loop and a surface capped at two points. The text says that interactions are accounted for by different topologies, and that it is technically convenient to begin and end at points.''',
 r'''In the perturbative world-sheet description of closed strings, the genus labels the loop order, while punctures and their assigned states describe external insertions. Turning an external cylindrical end into a puncture requires a local coordinate and a state/vertex prescription. This is a formal sewing description of amplitudes, not a topological theorem that arbitrary prescribed boundary-loop data equal a point delta function.''',
 r'''The caption abbreviation is retained without a forced expansion. The diagrams specify the physical construction but not a measure, sewing theorem, or convergence statement. The point insertion model below is one chosen Fourier representation.''',
 r'''The earlier surface-sum and insertion formulas are in \citet[eqs.~(1)--(3),(26)--(31)]{polyakov1981quantum}; the fixed-genus consequences appear in \citet[\S6]{belavinknizhnik1986complex}.''',
 r'''Known formal perturbative interpretation (E); no new precise topological or analytic question is posed.''',('polyakov1981quantum','belavinknizhnik1986complex'),literal='not determinable',match='thematic only')
add(668,'construction','Fourier-transforming target point constraints into exponential vertices',
 r'''The page first calls \(V_\alpha\) delta functions, then writes \(V_\alpha(p)=\int e^{ip_\alpha\cdot X(\xi)}d^2\xi\).''',
 r'''For a fixed smooth map, Fourier transformation of \(\delta^{(d)}(X(\xi)-y)\) in the target point \(y\), with convention \(\int e^{ip\cdot y}\delta(X-y)dy\), gives \(e^{ip\cdot X(\xi)}\). In the quantum free-boson theory this exponential needs normal ordering. An integrated closed-string vertex must also be a coordinate-invariant world-sheet density; in conformal coordinates the usual on-shell scalar vertex has conformal weights \((1,1)\) before integration against \(d^2z\).''',
 r'''The elementary Fourier identity is exact for a smooth map. Its promotion to an integrated physical vertex requires a normalization of the action, a momentum/mass-shell condition, regularization, and the ghost prescription. None is specified by the bare coordinate integral.''',
 r'''\citet[eqs.~(26)--(31)]{polyakov1981quantum} gives the vertex construction; \citet[\S6, (6.21)--(6.26)]{belavinknizhnik1986complex} computes the resulting tachyon factors with momentum conservation and mass-shell conditions.''',
 r'''Established construction (E), with the distinction between a classical Fourier identity and a renormalized quantum vertex retained.''',('polyakov1981quantum','belavinknizhnik1986complex'),match='exact')
add(668,'claim','A target delta derivative is not a world-sheet derivative vertex',
 r'''The sentence about derivatives of delta functions is followed by \(\int\partial X^\mu e^{ip\cdot X}\,d^2\xi\).''',
 r'''Fourier transformation of a target-coordinate derivative \(\partial_{y^\mu}\delta(X-y)\) gives a factor \(-ip_\mu e^{ip\cdot X}\) under the preceding convention. It does not give \(\partial X^\mu\). World-sheet derivatives of the free field produce oscillator or descendant insertions. For a closed-string tensor vertex a typical full density includes both \(\partial X^\mu\) and \(\bar\partial X^\nu\), appropriate polarization and on-shell conditions; the isolated chiral factor has an uncontracted world-sheet index.''',
 r'''The notebook does not say which delta variable is differentiated. If it means the same target point whose Fourier transform was just taken, the indicated implication is false. If it means a different state construction, that is missing data, not a justification for silently adding the antiholomorphic factor.''',
 r'''The distinction is an elementary Fourier calculation, checked against the exponential-insertion setup in \citet[eqs.~(26)--(31)]{polyakov1981quantum}.''',
 r'''E with a faithful mathematical gap; no general new vertex-operator theorem is inferred from the incomplete line.''',('polyakov1981quantum',),literal='false as written',match='partial',development='annotated')
add(668,'method','Gaussian integration with sources, determinant powers, and the zero mode',
 r'''Integrating over \(X\) is said to give \((\det\Delta_0)^{-13}\) times products of exponentials \(p_\alpha p_\beta G_{\mathrm{reg}}(\xi_\alpha,\xi_\beta)\). The preceding action has a positive exponent.''',
 r'''Fix a closed connected surface and a nonnegative scalar Laplacian \(\Delta\). For 26 real mean-zero fields with action \(S=\frac12\langle X,\Delta X\rangle\), a finite-mode Gaussian integral with sources \(\sum_a p_a\delta_{z_a}\) equals a normalization times \((\det{}'\Delta)^{-13}\exp[-\frac12\sum_{a,b}p_a\cdot p_b\,G(z_a,z_b)]\), before diagonal regularization, where \(G=\Delta^{-1}\) on mean-zero functions. Integrating the constant target mode separately gives \((2\pi)^{26}\delta^{(26)}(\sum_a p_a)\). The infinite-dimensional determinant requires zeta regularization.''',
 r'''The sign and factor1/2 are stated for this explicit action and covariance convention; another convention for \(G\) changes their appearance. A positive Euclidean exponential of positive energy is divergent. The prime, momentum-conservation delta, and contractions of target indices are missing from the notebook's shorthand. Derivative vertices require additional differentiated Green-function contractions.''',
 r'''\citet[\S6, (6.21)--(6.24)]{belavinknizhnik1986complex} performs this Gaussian source calculation and explicitly uses momentum conservation. The finite-mode completion-of-the-square identity provides the normalization check.''',
 r'''Established Gaussian calculation (E). The result read is a regularized fixed-surface building block, not a rigorous value for the total genus sum.''',('belavinknizhnik1986complex',),literal='false as written',match='exact',development='annotated')
add(668,'construction','The Green-function diagonal and Wick ordering',
 r'''The final line defines \(G_{\mathrm{reg}}\) as a Green function smoothed when the two points coincide.''',
 r'''The two-dimensional scalar covariance has a logarithmic diagonal singularity. For a mollified mean-zero Gaussian field \(X_\varepsilon\), define a point exponential at finite cutoff by \(:e^{ip\cdot X_\varepsilon(z)}:=\exp(ip\cdot X_\varepsilon(z)+\frac12|p|^2\mathbb E[X_\varepsilon^1(z)^2])\). At pairwise distinct points, its normalized correlation has limit \(\exp[-\sum_{a<b}p_a\cdot p_bG(z_a,z_b)]\). Integrated collisions, local metric factors, and alternative diagonal finite parts require additional prescriptions.''',
 r'''Here the components have identical scalar covariance and are independent. This formula identifies one precise diagonal subtraction. Merely replacing the diagonal by an arbitrary smooth value does not select the physical normalization or prove integrability when insertion points collide.''',
 r'''\citet[\S6, between (6.24) and (6.26)]{belavinknizhnik1986complex} explicitly regularizes the diagonal and then imposes the mass-shell condition; \citet[\S3]{dotsenkofateev1984conformal} supplies the corresponding normal-ordered free-boson contraction framework.''',
 r'''Known renormalized Gaussian building block (E). No unqualified convergence theorem is extracted from the notebook's word ``smoothed''.''',('belavinknizhnik1986complex','dotsenkofateev1984conformal'),match='partial',development='annotated')

own_checks={
 'ADJ-667.2':r'Editorial check of the marginal whole-curve interpretation \ours.',
 'ADJ-667.4':r'Editorial local-lift argument from vanishing of the first cohomology after a sufficiently large pole divisor \ours.',
 'ADJ-667.5':r'Editorial formal-gluing derivation of the two forgetting-map tangent quotients \ours; the full-parameter uniformization theorem is due to Kontsevich.',
 'ADJ-668.3':r'Editorial Fourier identity in the stated sign convention \oursComputed; the quantum vertex construction is prior literature.',
 'ADJ-668.4':r'Editorial target-delta derivative calculation \oursComputed.',
 'ADJ-668.5':r'Editorial finite-mode Gaussian completion of the square and zero-mode check \oursComputed; the string-theory application is the cited published calculation.',
 'ADJ-668.6':r'Editorial Wick-subtraction and off-diagonal contraction calculation \oursComputed; normal ordering itself is established machinery.',
}
for item in adj:
    if item['id'] in own_checks:
        item['reconstruction']+=' '+own_checks[item['id']]
        if item['development']=='none':item['development']='annotated'
    for field in ('notes','statement','reconstruction','fate','present_status'):
        for a,b in {'February1987':'February 1987','Institute1985':'Institute 1985','submitted18February1986':'submitted 18 February 1986','publishedAugust1986':'published August 1986','Genus0 and1':'Genus 0 and 1','factor1/2':'factor 1/2'}.items():
            item[field]=item[field].replace(a,b)
(OUT/'adjacent_items.json').write_text(json.dumps(adj,ensure_ascii=False,indent=2)+'\n')

header=r'''\subsection{Adjacent-page supplement: Kontsevich and Morozov}
\label{supp:1985-adjacent}
These two pages are preserved as supplementary evidence only. Their records
667--668 lie outside the requested core records 641--666; they are excluded
from the year's core talk and occurrence counts and receive ADJ-prefixed
identifiers. The manuscript heading on P001258 reads \(24/\mathrm{II}/85\),
whereas catalogue record 667 gives 24 February 1987. P001259 reads
24 February 1986, whereas record 668 also gives 24 February 1987.
Neither conflict is silently repaired. Kontsevich's matching paper was
submitted 3 December 1986 and published in 1987; Morozov explicitly reports
Belavin--Knizhnik and Beilinson rather than claiming new results. The technical
assessment below is independent of resolving these dates.

'''
parts=[header]
for item in adj:
    parts.append('\\subsubsection{'+item['id']+': '+item['title'].replace('_',r'\_')+'}\n')
    parts.append('\\noindent\\textbf{Source.} '+item['pages']+'; '+('M. L. Kontsevich' if item['record']==667 else 'Morozov')+'.\\par\n')
    for field,label in [('notes','Notebook'),('statement','Precise statement'),('reconstruction','Reconstruction and limits'),('fate','Literature fate'),('present_status','Present status')]:
        parts.append('\\noindent\\textbf{'+label+'.} '+item[field]+'\\par\n\n')
    parts.append('\\noindent\\textbf{Assessment.} Class '+item['class']+'; literal correctness: '+item['literal_correctness']+'; publication match: '+item['publication_match']+'; verification: '+item['verification']+'; development: '+item['development']+'; confidence: '+item['confidence']+'.\\par\n\n')
(OUT/'adjacent.tex').write_text(''.join(parts))

# Add only the new primary reference; the remaining references already occur in
# the core shard. The key is new after checking the cumulative bibliography.
key='kontsevich1987virasoro'
bib=r'''@article{kontsevich1987virasoro,
  author = {Kontsevich, Maxim L.},
  title = {{Virasoro} algebra and {Teichm{\"u}ller} spaces},
  journal = {Functional Analysis and Its Applications},
  year = {1987},
  volume = {21},
  number = {2},
  pages = {156--157},
  doi = {10.1007/BF01078034},
  url = {https://www.mathnet.ru/eng/faa1198},
  note = {verified},
  annote = {Primary Math-Net metadata and full two-page Russian original read. Section1, finite-jet moduli, tangent quotient and proposition; sections2--3 determinant extension and Virasoro action checked. Received3December1986. The author-hosted English PDF was also opened but had no usable OCR. Source dates1985/1987 remain unresolved; no date correction is inferred from the publication.}
}
'''
p=OUT/'references.bib';txt=p.read_text()
if not re.search(r'@\w+\{'+key+r',',txt):p.write_text(txt+'\n% Adjacent-page supplement only\n'+bib)

p=OUT/'sources.json';sources=json.loads(p.read_text())
addsources=[
 dict(key=key,url='https://www.mathnet.ru/eng/faa1198',ref='turn132view1',title='Virasoro algebra and Teichmueller spaces',opened=True,verified=True,scope='Primary metadata, DOI and receipt date.',locators='',checked='2026-11-11'),
 dict(key=key,url='https://www.mathnet.ru/php/getFT.phtml?jrnid=faa&option_lang=eng&paperid=1198&what=fullt',ref='turn133view1',title='Virasoro algebra and Teichmueller spaces',opened=True,verified=True,scope='Full two-page Russian primary paper read. Does not resolve manuscript/catalogue date conflict.',locators='section1 proposition and tangent formula; sections2--3 determinant construction and coefficient',checked='2026-11-11'),
 dict(key=key,url='https://www.ihes.fr/~/maxim/TEXTS/Virasoro_algebra_and_Teichmuller_spaces.pdf',ref='turn132view0',title='Virasoro algebra and Teichmueller spaces (English)',opened=True,verified=True,scope='Author-hosted two-page English PDF opened without readable OCR; actual result read in Russian Math-Net copy.',locators='',checked='2026-11-11'),
 dict(key='belavinknizhnik1986complex',url='https://strings.itp.ac.ru/Papers/belavin1986.pdf',ref='turn141view3',title='Complex geometry and the theory of quantum strings',opened=True,verified=True,scope='Additional primary reading for Morozov supplement: Gaussian source integral, momentum conservation, diagonal regularization and mass-shell condition.',locators='section6, (6.21)--(6.26), pp.225--226',checked='2026-11-11'),
 dict(key='beilinsonschechtman1988determinant',url='https://doi.org/10.1007/BF01221114',ref='turn132view2',title='Determinant bundles and Virasoro algebras',opened=True,verified=False,scope='Attempted DOI opening failed; not cited as a read result. Kontsevich1987already states independent attribution.',locators='',checked='2026-11-11')]
for s in addsources:
    if not any(x['url']==s['url'] and x['ref']==s['ref'] for x in sources):sources.append(s)
p.write_text(json.dumps(sources,ensure_ascii=False,indent=2)+'\n')

# Separate corrections file, so the core57-row count and provenance remain stable.
rows=[
 ['P001258','ADJ-667 date','Manuscript24/II/85; catalogue24February1987','Retain both; unresolved','Scan and catalogue conflict; matching paper submittedDecember1986 does not by itself decide which heading is wrong.','both','provenance'],
 ['P001259','ADJ-668 date','Manuscript24.2.86; catalogue24February1987','Retain both; unresolved','Scan and catalogue conflict; the report identifies circulating Belavin--Knizhnik work under either date.','both','provenance'],
 ['P001258','ADJ-667 moduli object','Triple(C,p,x) is called Teichmueller space','Formal-parameter pointed moduli, or its pullback to a marked Teichmueller cover','No topological marking is included in the triple; Kontsevich1987section1.','both','ambiguity'],
 ['P001258','ADJ-667 tangent quotient',r'\(\mathfrak g/\mathfrak k\)',r'\(\mathfrak g/\gamma\) for the full formal-parameter moduli','The next display gives the correct global stabilizer. Further quotient by k gives unpointed moduli.','both','faithful_error'],
 ['P001258','ADJ-667 marginal extension',r'\ru{всю C!!}','Allow meromorphic pole atp; do not demand holomorphic extension throughp','Gamma was defined by possible pole atp; whole-curve holomorphic vector fields vanish for genus>=2.','both','ambiguity'],
 ['P001259','ADJ-668 Euclidean sign','Positive exponential of positive kinetic energy','With positive kinetic energy use exp(-S), or explicitly declare a different signature/convention','The subsequent Gaussian determinant computation needs a convergent Gaussian before analytic continuation.','both','faithful_error'],
 ['P001259','ADJ-668 derivative vertex','A target delta derivative gives a world-sheet derivative times an exponential',r'Target derivative gives \(-ip_\mu e^{ipX}\) in the stated Fourier convention; world-sheet derivative is another insertion','Elementary Fourier identity; the incomplete chiral factor is not yet a scalar integrated closed-string vertex.','both','faithful_error'],
 ['P001259','ADJ-668 Gaussian factor','Unprimed scalar determinant; all-pairs exponent with unspecified sign/coefficient','Use det-prime and isolate the constant mode; fix covariance/action convention for sign and factor1/2','Belavin--Knizhnik1986section6includes momentum conservation.','both','faithful_error'],
 ['P001259','ADJ-668 Green regularization','Smooth the diagonal','Choose a specified Wick/finite-part prescription and separately check integrated collisions','Off-diagonal Gaussian correlations do not imply convergence of the full insertion/moduli integrals.','both','ambiguity']
]
with (OUT/'adjacent_corrections.csv').open('w',newline='') as f:
    w=csv.writer(f);w.writerow(['page','place','transcription_reads','should_read','evidence','applies_to','type']);w.writerows(rows)
print('Wrote',len(adj),'separate adjacent items, adjacent.tex,9 adjacent corrections; bibliography/source ledger extended.')
