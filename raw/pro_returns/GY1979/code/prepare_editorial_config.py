#!/usr/bin/env python3
"""Explicit integrated problem and typesetting edits; mathematical scope retained."""
from pathlib import Path
import json
D=Path(__file__).resolve().parent.parent
path=D/'code/editorial_config.json'
cfg=json.loads(path.read_text()) if path.exists() else {}
cfg['source_span_overrides']={'465':'P000848-P000853'}
items=cfg.setdefault('item_overrides',{})
items.setdefault('1979-463.1',{})['fate']=r'The contemporary definition and additive equation are in \citet[Sec.~1, pp.~192--193, eqs.~(1), (3)--(5)]{zakharovschulman1980degenerative}. The paper was received on 1 September 1979 and published in June 1980; receipt is not asserted to be a public circulation date. The later systematic formulation is \citet[Sec.~3, eqs.~(3.8)--(3.9)]{zakharovschulman1988invariants}.'
items.setdefault('1979-463.2',{}).update({
 'fate':r'The exact difference-curve parametrization appears in \citet[Sec.~1, p.~193, eqs.~(12)--(13)]{zakharovschulman1980degenerative}, published in June 1980. That paper credits the general example to S.~V.~Manakov, private communication. The arbitrary-function construction is written explicitly in \citet[Sec.~3, eqs.~(3.10)--(3.12)]{zakharovschulman1988invariants}, followed by the distinction between partial and complete degeneracy. The 1980 formula pages were read and visually checked in the original.',
 'refs':['zakharovschulman1980degenerative','zakharovschulman1988invariants']})
items.setdefault('1979-463.6',{}).update({
 'fate':r'The kinetic form of the resonance obstruction was published soon after the seminar in \citet[Sec.~1, p.~195, final paragraph]{zakharovschulman1980degenerative}, excluding singular delta-type kinetic kernels. The general statement for analytic Hamiltonian invariants with a quadratic leading term is proved in \citet[Theorem~3.1, pp.~291--293]{zakharovschulman1988invariants}; its introduction, pp.~285--286, also identifies a brief 1985 announcement. Class A records the early kinetic result; the full modern reconstruction is supported by the later theorem.',
 'publication_match':'partial'})
items.setdefault('1979-468.11',{})['development']='developed in this chapter'
items.setdefault('1979-465.21',{})['statement']=r'''For a nonnegative self-adjoint Laplace-type operator \(P\) on a closed smooth four-dimensional Riemannian manifold, form \(\zeta_P\) from its positive eigenvalues and let \(B_4\) denote the constant term in the integrated heat expansion. Then
\[
m=\zeta_P(0)=B_4-\dim\ker P.
\]
This value need not be an integer. For the scalar Laplacian on the unit round \(S^4\), the standard coefficient gives \(B_4=29/90\) and \(m=-61/90\), since the kernel consists of constants.'''
items.setdefault('1979-466.4',{})['statement']=r'Over \(\mathbb C\), let \(V\) be a finite-dimensional vector space with nondegenerate alternating form \(\omega\), and let \(A:V\to V\) satisfy \(\omega(Au,v)=\omega(u,Av)\). There is a symplectic basis in which \(A=\operatorname{diag}(J,J^{\mathsf T})\), with \(J\) in Jordan normal form. Each Jordan block therefore occurs with its paired transpose.'
source_items={x['id']:x for x in json.loads((D/'GY1979_items.json').read_text())}
for ident,field,marker in [('1979-463.10','statement',r'\oursComputed\ '),
                         ('1979-465.21','reconstruction',r'\oursComputed\ '),
                         ('1979-466.1','reconstruction',r'\ours\ '),
                         ('1979-466.2','reconstruction',r'\ours\ '),
                         ('1979-466.3','reconstruction',r'\oursComputed\ '),
                         ('1979-470.11','reconstruction',r'\ours\ ')]:
    value=source_items[ident][field]
    if not value.startswith(marker):value=marker+value
    items.setdefault(ident,{})[field]=value
for ident in ('1979-466.2','1979-466.3'):
    items.setdefault(ident,{})['publication_match']='none found'
    items[ident]['verification']='indirect'
items.setdefault('1979-465.24',{})['statement']=r'''On a closed oriented Riemannian four-manifold,
\[
\chi(M)=\frac1{32\pi^2}\int_M
\bigl(|\operatorname{Riem}|^2-4|\operatorname{Ric}|^2+R^2\bigr)\,d\operatorname{vol}.
\]
With curvature two-form matrix \(\Omega\),
\[
p_1(TM)=-\frac1{8\pi^2}\operatorname{tr}(\Omega\wedge\Omega)
\]
in the stated Chern--Weil convention.'''
items.setdefault('1979-467.12',{})['reconstruction']=r'The nonlinear-graviton construction concerns complex geometry with self-dual curvature under additional constraints; it is not a solution for all real Lorentzian Einstein metrics.'
items.setdefault('1979-472.1',{})['reconstruction']=r'The source\textquotesingle s \(W\) is a generating functional. Its relation to an effective action requires a Legendre transform; connected functions and the effective action must be distinguished in the later argument.'
items.setdefault('1979-473.3',{})['statement']=r'''Let \(S\in C^\infty(\mathbb R^n;\mathbb R)\), \(a\in C_c^\infty(\mathbb R^n)\), and let \(x_0\) be the unique critical point of \(S\) in the relevant support, with nonsingular Hessian \(H=S''(x_0)\). As \(\hbar\downarrow0\),
\[
\begin{aligned}
\int_{\mathbb R^n}e^{iS(x)/\hbar}a(x)\,dx
&=e^{iS(x_0)/\hbar}(2\pi\hbar)^{n/2}
  e^{i\pi\operatorname{sgn}(H)/4}\\
&\qquad\times|\det H|^{-1/2}\bigl[a(x_0)+O(\hbar)\bigr].
\end{aligned}
\]
Multiple critical points contribute a sum; a critical manifold requires a different theorem.'''
items.setdefault('1979-473.9',{})['statement']=r'''If \(I(c)\) has the same value \(I\) for every admissible slice parameter \(c\), then
\[
\frac{\int w(c)I(c)\,dc}{\int w(c)\,dc}=I,
\]
provided the denominator is nonzero and the integrals or their regularized meanings exist. Taking \(w=e^{i\Omega}\) gives a gauge-fixing action; normalization is still required for the stated independence.'''
items.pop('1979-477.4',None) # Final primary-source identification supersedes the provisional formatting edit.
items.setdefault('1979-482.10',{})['statement']=r'''For traceless Hermitian generators of \(\mathfrak{su}(N)\) normalized by \(\operatorname{Tr}(T^aT^b)=\delta^{ab}\), completeness gives
\[
\sum_a(T^a)_{ij}(T^a)_{kl}
=\delta_{il}\delta_{jk}-N^{-1}\delta_{ij}\delta_{kl}.
\]
Consequently,
\[
\sum_a\operatorname{Tr}(T^aUT^aV)
=\operatorname{Tr}U\operatorname{Tr}V-N^{-1}\operatorname{Tr}(UV).
\]
Adding the normalized identity generator gives the \(U(N)\) version without the subtraction.'''
items.setdefault('1979-483.4',{})['notes']=r'''\ru{Теорема 1.1}: a unique bar-invariant element has the expansion
\[
C^{\prime}_w=q^{-\ell(w)/2}\sum_{y\le w}P_{y,w}T_y,
\]
with \(P_{w,w}=1\) and the strict degree bound (12).'''
items.setdefault('1979-486.5',{})['notes']=r'After defining speciality, the recorder writes:\par\ru{Неизвестно: стратификация или клет. разбиение}.'
items.setdefault('1979-487.2',{})['notes']=r'The fragment\textquotesingle s central line reads:\par\ru{Элементу} \(G_{n,k}\) \ru{соотв. пара гиперсимплекс + конфигурация}.'
items.setdefault('1979-476.6',{})['statement']=r'''Fix \(x\in\mathbb P^1(\mathbb C)\). For generic quadruples, put
\[
c_x(g_0,g_1,g_2,g_3)
=D\bigl(\operatorname{cr}(g_0x,g_1x,g_2x,g_3x)\bigr).
\]
The five-term identity makes this a homogeneous measurable real three-cocycle for \(GL_2(\mathbb C)\), restricting to \(SL_2(\mathbb C)\). It represents the nonzero degree-three volume class under the comparison between measurable and continuous cohomology. Changing \(x\) gives a cohomologous cocycle.'''
items.setdefault('1979-485.2',{})['fate']=r'\citet[Sec.~3 and the proof of Thm.~6]{olshanskii1980construction} supplies the Gaussian model and its compact dual; compare the decomposition under restriction in \citet[Sec.~1]{olshanskii1978unitary}. The result was formulated in the note presented in June 1979, so the talk is treated as contemporary exposition. The precise public release day of the 1980 issue remains unverified.'
cfg.setdefault('problem_overrides',{})['GP-1975-10']={
 'title':'Continuum confinement and the static potential',
 'statement':r'''For four-dimensional continuum pure \(SU(N)\) Yang--Mills theory at zero temperature, with fixed finite \(N\ge2\) and external fundamental static sources, establish a well-defined subtracted static potential with positive asymptotic string tension:
\[
\lim_{r\to\infty}\frac{V(r)}r=\tau>0.
\]
There are no dynamical fundamental quarks in this formulation. Occurrence 1979-480.3 specializes to \(SU(3)\). Occurrence 1979-482.14 returns to the general confinement goal and proposes normalized large-rank loop equations as a route; that limiting method is not identified with the fixed-rank statement. The stronger constant-width flux-tube hypothesis is excluded from this problem identity.''',
 'status':r'''As of 10 November 2026, the verified results are partial. Wilson's strong-coupling lattice area law \citep[Secs.~IV and VI]{wilson1974confinement} and the controlled large-rank lattice expansion \citep[Theorem~3.1 and Corollaries~3.2--3.3]{chatterjee2015string} do not provide the asserted continuum proof. With light dynamical quarks, string breaking changes the asymptotic static-energy question \citep[Sec.~4]{bulava2019string}. The continuum existence-and-mass-gap problem and confinement are separately stated in \citet[Sec.~5]{jaffewitten2000yangmills}; the former is still listed as unsolved by \citet{clay2026yangmills}. The reused older identifier follows the static-potential goal, while the distinct proposed methods and physical regimes remain explicit.'''
}
cfg.setdefault('bibliography_fields',{}).update({
 'zakharovschulman1980degenerative':{
   'url':'https://zakharov75.itp.ac.ru/static/local/zve75/zakharov/1980/1980-05-1980_PD_ZS.pdf',
   'note':'verified',
   'annote':'Final independent chronology check, 10 November 2026: full original in the ITP conference archive opened and section 1, pp.192--195 read. Equations12--13 on p.193 visually checked: exact difference-curve parametrization, with the general example attributed to S.V.Manakov (private communication). The kinetic obstruction on p.195 excludes singular delta-type kernels; it is not silently identified with the later all-orders Hamiltonian theorem. Received1September1979; publishedJune1980. Receipt is not public circulation. This supersedes the earlier metadata-only access entry in the early batch log.'},
 'kallosh1980selfduality':{'pages':'119--128','number':'1'},
 'senjanovic1976path':{'author':r"Senjanovi{\'{c}}, P."}
 ,'berezin1987superanalysis':{
     'editor':None,
     'annote':'Edited by A. A. Kirillov. The editor is retained here because plainnat warns when a book has both author and editor fields. Publisher metadata and contents opened on 10 November 2026. Grassmann algebra pp.29--73 and graded linear algebra pp.90--130 identified. Full chapter not retrieved; elementary identities and the simple-spectrum lifting argument are checked directly in the companion.'}
})
path.write_text(json.dumps(cfg,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'item_edits':len(items),'problem_edits':len(cfg['problem_overrides']),
                  'bibliographic_edits':len(cfg['bibliography_fields'])},indent=2))
