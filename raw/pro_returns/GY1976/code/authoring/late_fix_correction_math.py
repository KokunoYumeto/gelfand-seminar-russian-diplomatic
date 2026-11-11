from pathlib import Path
import pprint
p=Path('work/late_author.py')
s=p.read_text()
def math(x): return r'\('+x+r'\)'
patches={
('P000686','graph notation'):{
 'transcription_reads':math(r'\varphi(t)=\operatorname{graph}\varphi(t)'),
 'should_read':math(r'\varphi(t)=\operatorname{graph}\Phi(t)')},
('P000686','symmetric-form equivalence'):{
 'transcription_reads':math(r'\sigma=0\text{ on }\Gamma'),
 'should_read':math(r'\sigma=0\text{ on }\operatorname{graph}\Gamma')},
('P000688-P000689','individual trace terms'):{
 'transcription_reads':math(r'\int_X\varphi(x\gamma x^{-1})\,dx')},
('P000688','half-sum of roots'):{
 'transcription_reads':math(r'\rho=\frac12\sum\text{positive roots}'),
 'should_read':math(r'\rho=\frac12\sum_{\alpha>0}m_\alpha\alpha')},
('P000689','final remainder'):{
 'transcription_reads':math(r'O(R^{n-r-1})'),
 'should_read':r'Retain the uncertain symbol; the matched general theorem has \(O(R^{n-1})\).'},
('P000690','Zakharov--Shabat equation'):{
 'transcription_reads':math(r'L_t+P_y=[P,L]'),
 'should_read':math(r'L_t-P_y=[P,L]')},
('P000691','node parameters in real case'):{
 'transcription_reads':r'\(\alpha_i,\beta_i\in k\); \(\alpha_i=\overline{\beta_i}\) for \(k=\mathbb R\)',
 'should_read':r'Use complexified parameters for real descent and require all \(2N\) points distinct.',
 'evidence':r'Real distinct conjugate pairs cannot both lie in \(\mathbb R\); Manin III.5.1 explicitly chooses complex node parameters.'},
('P000692','filtration shift'):{
 'transcription_reads':math(r'M_i=M_{(i-rN)}'),
 'should_read':math(r'M_i=M_{(i+rN)}\quad(M_0=0,\ \mathbf1\in M_1)'),
 'evidence':r'Actual PNG has minus. The preceding vanishing lemma forces a positive shift; Manin III.5.5 uses \(+rN+1\) with generator in \(M_0\).'},
('P000692','generator coefficient equation'):{
 'transcription_reads':math(r'\sum_j(\alpha_i^jE_r-\beta_i^jg_i)m_i'),
 'should_read':math(r'\sum_j(\alpha_i^jE_r-\beta_i^jg_i)m_j'),
 'evidence':r'Actual PNG and Russian have \(m_i\); substitution of the displayed polynomial forces \(m_j\).'},
('P000692','endomorphism ring'):{
 'transcription_reads':math(r'M_r(\mathcal B[\lambda])=\operatorname{End}_{\mathcal B}(N)'),
 'should_read':math(r'M_r(\mathcal B[\lambda])=\operatorname{End}_{\mathcal B[\lambda]}(N)')},
('P000692','flatness equation'):{
 'transcription_reads':math(r'\partial_xd_t-\partial_td_x=[d_x,d_t]'),
 'should_read':math(r'\partial_xd_t-\partial_td_x=-[d_x,d_t]'),
 'evidence':r'Scan has no minus; expansion of \([\partial_x+d_x,\partial_t+d_t]\) fixes the sign.'},
('P000693','left time exponential'):{
 'transcription_reads':r'\[\begin{aligned}g_i(x)&=e^{-xd_x(\alpha_i)+td_t(\alpha_i)}g_i(0,0)\\&\qquad{}\times e^{xd_x(\beta_i)+td_t(\beta_i)}.\end{aligned}\]',
 'should_read':r'\[\begin{aligned}g_i(x,t)&=e^{-xd_x(\alpha_i)-td_t(\alpha_i)}g_i(0,0)\\&\qquad{}\times e^{xd_x(\beta_i)+td_t(\beta_i)}.\end{aligned}\]'},
('P000695','determinantal coorientation'):{
 'transcription_reads':r'\(Z\subset\operatorname{Hom}(\mathbb R^m,\mathbb R^n)\) has canonical coorientation',
 'evidence':r'Arbitrary real determinantal strata need not be coorientable; here the normal space is \(\operatorname{Hom}(\ker A,\operatorname{coker}A)\), with both factors of dimension two.'},
('P000700','hook length'):{
 'evidence':r'The displayed hook formula requires \(h=\text{arm}+\text{leg}+1\); otherwise a removable cell would have length zero.'},
('P000700','branching sentence'):{
 'transcription_reads':r'Every irreducible of \(S_{n-1}\) occurs once.'},
('P000700','regular representation'):{
 'transcription_reads':r'Functions on \(S^n\)',
 'should_read':r'Functions on \(S_n\)',
 'evidence':r'Context is the finite symmetric group and its regular representation of dimension \(n!\).'},
('P000701','rotated coordinates'):{
 'transcription_reads':r'\(X=(x+y)/2;\quad Y=(x-y)/2\)',
 'should_read':r'\(X=(x-y)/2;\quad Y=(x+y)/2\), for the stated graph normalization.'},
('P000701','limit-shape formula'):{
 'should_read':r'Add \(\Omega(X)=|X|\) for \(|X|>1\).',
 'evidence':r'The real square root is defined only on \([-1,1]\); the 1977 paper gives both branches.'},
('P000701','subsequence definition'):{
 'transcription_reads':r'\(i_1<\cdots<i_n\) inside a maximum over \(r\)',
 'should_read':r'\(i_1<\cdots<i_r\)',
 'evidence':r'The scan confirms \(n\); \(r\) is the length being maximized.'},
('P000702','packet dimension in GL(n)'):{
 'transcription_reads':r'\((n^2-1)(g-1)\)',
 'should_read':r'\(n^2(g-1)+1\); the displayed value is for a fixed determinant connection.',
 'evidence':r'Connections on a stable degree-zero bundle form a torsor for \(H^0(X,\operatorname{End}(E)\otimes K_X)\); Riemann--Roch. Rank one gives \(g\), not zero.'},
('P000703','section notation'):{
 'transcription_reads':r'\(f_i\) on \(U_j\)',
 'should_read':r'\(f_i\) on \(U_i\)',
 'evidence':r'The cocycle equation and local restriction \(df_i/f_i\) on \(U_i\) fix the index; the handwritten subscript is ambiguous.'},
('P000704','bottom monodromy diagram'):{
 'should_read':r'\(f(g(u))=\rho(g)(f(u))\)'}
}
marker='def correction(page,place,reads,should,evidence,applies='
pos=s.index(marker)
s=s[:pos]+'CORRECTION_LATEX_OVERRIDES = '+pprint.pformat(patches,sort_dicts=False,width=110)+'\n'+s[pos:]
old="    corrections.append(dict(page=page,place=place,transcription_reads=reads,should_read=should,evidence=evidence,applies_to=applies,type=typ))"
new="""    entry=dict(page=page,place=place,transcription_reads=reads,should_read=should,evidence=evidence,applies_to=applies,type=typ)
    entry.update(CORRECTION_LATEX_OVERRIDES.get((page,place),{}))
    corrections.append(entry)"""
assert old in s
s=s.replace(old,new)
s=s.replace(
'An alternative fundamental-domain formula needs the domain, which the notes do not specify.',
'One can instead integrate over a specified fundamental domain, but the notes do not say so.')
s=s.replace(
r'For constant commuting matrices the compatible solution is \(g_i(x,t)=e^{-xd_x(\alpha_i)-td_t(\alpha_i)}g_i(0,0)e^{xd_x(\beta_i)+td_t(\beta_i)}\).',
r'For constant commuting matrices the compatible solution is \[g_i(x,t)=e^{-xd_x(\alpha_i)-td_t(\alpha_i)}g_i(0,0)e^{xd_x(\beta_i)+td_t(\beta_i)}.\]')
s=s.replace(
r'For a finite simplicial complex \(K\), the vertex weight \(w(v)=\sum_{\sigma\ni v}(-1)^{\dim\sigma}/(\dim\sigma+1)\) satisfies \(\sum_vw(v)=\chi(K)\). For a closed piecewise Euclidean triangulated surface, the angle defect \(\kappa(v)=2\pi-\sum_{\sigma\ni v}\theta_{\sigma,v}\) satisfies \(\sum_v\kappa(v)=2\pi\chi(K)\).',
r'''For a finite simplicial complex \(K\), the vertex weights
 \[w(v)=\sum_{\sigma\ni v}\frac{(-1)^{\dim\sigma}}{\dim\sigma+1}\]
 satisfy \(\sum_vw(v)=\chi(K)\). For a closed piecewise Euclidean triangulated surface, the angle defects
 \[\kappa(v)=2\pi-\sum_{\sigma\ni v}\theta_{\sigma,v}\]
 satisfy \(\sum_v\kappa(v)=2\pi\chi(K)\).''')
p.write_text(s)
print('Installed explicit math-mode overrides for',len(patches),'correction rows, including mixed prose evidence.')
