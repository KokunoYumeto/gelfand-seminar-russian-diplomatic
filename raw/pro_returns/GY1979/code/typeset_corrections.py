#!/usr/bin/env python3
"""Make correction cells valid readable LaTeX without changing critical readings.

The source batches retain their authored plain-text/LaTeX mix. This final pass
adds math delimiters and escapes literal file-name underscores. Every change is
logged, so an editorial emendation is not confused with a typesetting repair.
"""
from pathlib import Path
import csv,json,re
D=Path(__file__).resolve().parent.parent
p=D/'GY1979_corrections.csv'
rows=list(csv.DictReader(p.open()))

whole_math={
 ('P000841','formula (2)','transcription_reads'),
 ('P000842','formula (3) shifted spin','transcription_reads'),
 ('P000845','complex Hamilton equation','transcription_reads'),
 ('P000845','complex Hamilton equation','should_read'),
 ('P000866','constraint closure formula','transcription_reads'),
 ('P000866','constraint closure formula','should_read'),
 ('P000869','equation (20)','transcription_reads'),
 ('P000869','expectation after equation (18)','transcription_reads'),
 ('P000869','expectation after equation (18)','should_read'),
 ('P000871','scalar example mass term','transcription_reads'),
 ('P000871','scalar example mass term','should_read'),
 ('P000873','equation (23)','transcription_reads'),
 ('P000873','equation (23)','should_read'),
 ('P000879','stress tensor','transcription_reads')}

exact={
 'E7 -> SU(8); E7 possibly called compact':r'\(E_7\to SU(8)\); \(E_7\) possibly called compact.',
 'Exclude all f=a omega+b dot k.':r'Exclude all \(f=a\omega+b\cdot k\).',
 'Exclude all f=aomega+b dot k.':r'Exclude all \(f=a\omega+b\cdot k\).',
 '(C(Rplus,G),mu0) maps to C(Rplus,G)':r'\((C(\mathbb R_+,G),\mu_0)\) maps to \(C(\mathbb R_+,G)\).',
 'The source is Lie-algebra Wiener paths(C0(Rplus,g),mu0), suitably based.':r'The source is Lie-algebra Wiener paths \((C_0(\mathbb R_+,\mathfrak g),\mu_0)\), suitably based.',
 'sigma_i sigma_j=delta_ij+epsilon_ijk sigma_k':r'\(\sigma_i\sigma_j=\delta_{ij}+\epsilon_{ijk}\sigma_k\)',
 'sigma_a barsigma_b-barsigma_b sigma_a':r'\(\sigma_a\bar\sigma_b-\bar\sigma_b\sigma_a\)',
 'Use a conventionally normalized antisymmetrization sigma_a barsigma_b-sigma_b barsigma_a.':r'Use a conventionally normalized antisymmetrization \(\sigma_a\bar\sigma_b-\sigma_b\bar\sigma_a\).',
 'Psi_pm=(1±gamma5)Psi':r'\(\Psi_\pm=(1\pm\gamma_5)\Psi\)',
 't^{(k-4/2}':r'\(t^{(k-4/2}\), with the malformed exponent as transcribed.',
 't^{(k-4)/2}':r'\(t^{(k-4)/2}\)',
 "phi_i(x)phi_i(x')":r"\(\phi_i(x)\phi_i(x')\)",
 "For complex bundle sections use phi_i(x) tensor phi_i(x')* and a fibre trace on the diagonal.":r"For complex bundle sections use \(\phi_i(x)\otimes\phi_i(x')^*\) and a fibre trace on the diagonal.",
 '(du3)^3':r'\((du_3)^3\)',
 '(du3)^2':r'\((du_3)^2\)',
 'Ad(phi) omega+phi^{-1}dphi':r'\(\operatorname{Ad}(\phi)\omega+\phi^{-1}d\phi\)',
 'For a left action use Ad(phi) omega+dphi phi^{-1}; alternatively change action convention consistently.':r'For a left action use \(\operatorname{Ad}(\phi)\omega+d\phi\,\phi^{-1}\); alternatively change the action convention consistently.',
 'F_a^{ik} F_a^{ik}':r'\(F_a^{ik}F_a^{ik}\)',
 'F^a_{ik} F^{aik}, with the chosen spacetime metric':r'\(F^a_{ik}F^{aik}\), with the chosen spacetime metric.',
 'm^2 c = (1/2) Hess(P) c':r'\(m^2c=\tfrac12\operatorname{Hess}(P)c\)',
 'm^2 c = Hess(P) c for the displayed canonical kinetic term':r'\(m^2c=\operatorname{Hess}(P)c\) for the displayed canonical kinetic term.',
 'q/cos(theta_w)':r'\(q/\cos\theta_W\)',
 'g/cos(theta_w)':r'\(g/\cos\theta_W\)',
 'sin(theta_w) times electromagnetic current':r'\(\sin\theta_W\) times the electromagnetic current.',
 'sin^2(theta_w) times electromagnetic current':r'\(\sin^2\theta_W\) times the electromagnetic current.',
 'Integral log x/(1-x) = sum 1/n^2':r'\(\int_0^1\log x/(1-x)\,dx=\sum_{n\ge1}1/n^2\)',
 'Integral log x/(1-x) = -sum_{n>=1} 1/n^2 = -pi^2/6':r'\(\int_0^1\log x/(1-x)\,dx=-\sum_{n\ge1}1/n^2=-\pi^2/6\)',
 'Multiplicatively skew-symmetric: r(g,f)=r(f,g)^(-1)':r'Multiplicatively skew-symmetric: \(r(g,f)=r(f,g)^{-1}\).',
 'F_{alpha beta dotted-gamma dotted-delta} on left, alpha gamma and dotted-beta dotted-delta on right':r'\(F_{\alpha\beta\dot\gamma\dot\delta}\) on the left; \(\alpha,\gamma\) and \(\dot\beta,\dot\delta\) are paired on the right.',
 'Use F_{alpha dotted-beta gamma dotted-delta} for the indicated vector-index pairing.':r'Use \(F_{\alpha\dot\beta\gamma\dot\delta}\) for the indicated vector-index pairing.',
 'The first-order condition is (k dot grad F0)h_k=0 on k dot grad H0=0; nonintegrability requires additional resonance richness.':r'The first-order condition is \((k\cdot\nabla F_0)h_k=0\) on \(k\cdot\nabla H_0=0\); nonintegrability requires additional resonance richness.'
}
parts={
 r's-\frac23':r'\(s-\frac23\)',
 r'S_{\rm cal}':r'\(S_{\rm cal}\)',
 r'S_{\rm ph.ch}':r'\(S_{\rm ph.ch}\)',
 'zeta_P(0)':r'\(\zeta_P(0)\)',
 'Riem^2−4Ric^2+R^2':r'\(|\operatorname{Riem}|^2-4|\operatorname{Ric}|^2+R^2\)',
 'Riem^2':r'\(|\operatorname{Riem}|^2\)',
 'p1=−tr(Omega wedge Omega)/(8pi^2)':r'\(p_1=-\operatorname{tr}(\Omega\wedge\Omega)/(8\pi^2)\)',
 'h_k':r'\(h_k\)',
 'k dot grad F0':r'\(k\cdot\nabla F_0\)',
 'k dot grad H0':r'\(k\cdot\nabla H_0\)',
 "h(e_A,e^A')=i":r"\(h(e_A,e^{A'})=i\)",
 'det(a dU a*)=|det a|^2 det(dU)':r'\(\det(a\,dU\,a^*)=|\det a|^2\det(dU)\)',
 "(L∞ union W_phi)''":r'\((L^\infty\cup W_\phi)^{\prime\prime}\)',
 'log |f^v(g)/g^v(f)|':r'\(\log|f^{v(g)}/g^{v(f)}|\)',
 'f=z^m a, g=z^n b':r'\(f=z^ma\), \(g=z^nb\)',
 'Sp(Ia Ib)=1/2 delta_ab':r'\(\operatorname{Sp}(I_aI_b)=\tfrac12\delta_{ab}\)',
 '1/2 delta_ab':r'\(\tfrac12\delta_{ab}\)',
 'N delta_ab':r'\(N\delta_{ab}\)',
 'p_z+1=0 and p=h-z':r'\(p_z+1=0\) and \(p=h-z\)'
}

math_re=re.compile(r'(\\\(.*?\\\)|\\\[.*?\\\]|\$.*?\$)',re.S)
def process_outside(s,func):
    chunks=math_re.split(s)
    return ''.join(c if i%2 else func(c) for i,c in enumerate(chunks))

def clean_plain(s):
    # Expand compressed editorial shorthand; original cells remain in the log.
    readability={
        'record462':'record 462', 'record469':'record 469',
        'record473':'record 473', 'record479':'record 479', 'record488':'record 488',
        'occurrence1978':'occurrence 1978',
        'Duff1982':'Duff (1982)', 'Sec1.10':'Sec. 1.10',
        'Zakharov--Schulman1988':'Zakharov--Schulman (1988)',
        'eq(3.9)':'eq. (3.9)', 'eq(1.1)':'eq. (1.1)',
        'gives6/5':'gives 6/5', 'gives2, not0':'gives 2, not 0',
        'dimension8, not4':'dimension 8, not 4',
        'Letters29(1979),192;493':'Letters 29 (1979), 192; 493',
        'pages172 and449':'pages 172 and 449',
        'distinguishes1979a':'distinguishes 1979a', 'and1979b':'and 1979b',
        'factors1/2 and1/sqrt2':r'factors \(1/2\) and \(1/\sqrt2\)',
        'andSO4':r'and \(SO(4)\)',
        'are(1±gamma5)/2':r'are \((1\pm\gamma_5)/2\)',
        'factor1/2':r'factor \(1/2\)',
        'spin5/2':'spin 5/2', 'Aragone--Deser1979':'Aragone--Deser (1979)',
        'checked1979':'checked 1979', 'GilkeyCh2':'Gilkey, Ch. 2',
        'GL2C':r'\(GL_2(\mathbb C)\)',
        '|det a|=1':r'\(|\det a|=1\)', 'scalarU1':r'scalar \(U(1)\)',
        'has3;':'has 3;', 'isotropic2-planes':'isotropic 2-planes',
        'Dimension4 versus5':'Dimension 4 versus 5',
        'BGG1978Theorems1--3':'BGG (1978), Theorems 1--3',
        'RussianYu':'Russian Yu.', 'suppliesG.B.':'supplies G. B.',
        'Little1983Def2.2,Prop3.7,Thm3.9':'Little (1983), Definition 2.2, Proposition 3.7 and Theorem 3.9',
        'PrimaryAlbeverioetal2015Sec2.4':'Albeverio et al. (2015), Sec. 2.4',
        'Albeverioetal2015Sec2':'Albeverio et al. (2015), Sec. 2',
        'Wallach1987Secs1,5':'Wallach (1987), Secs. 1 and 5',
        'statedL2':r'stated \(L^2\)', 'typeIII':'type III',
        'definingmu0':r'defining \(\mu_0\)',
        'Yau1977 Theorem1':'Yau (1977), Theorem 1',
        'positive c1':r'positive \(c_1\)',
        'Beilinson1980 section1 Lemma1':'Beilinson (1980), section 1, Lemma 1',
        'Weinberg1967 equations13-14':'Weinberg (1967), equations 13--14',
        'PDG2026 section10.1':'PDG (2026), section 10.1',
        'Kobayashi-Maskawa1973':'Kobayashi--Maskawa (1973)',
        'on22September1980':'on 22 September 1980',
        'Looijenga1988,p3':'Looijenga (1988), p. 3',
        'The1979':'The 1979', 'Sec1.3':'Sec. 1.3', 'onp14':'on p. 14',
        'Gelfand--Gindikin--Shapiro1979,Sec1.1':'Gelfand--Gindikin--Shapiro (1979), Sec. 1.1',
        'Gelfand--Graev1980,Eq4':'Gelfand--Graev (1980), Eq. 4',
        'dates25December1978 and16June1980':'dates 25 December 1978 and 16 June 1980',
        'MathNet':'Math-Net',
        'initialYu':'initial Yu.', 'catalogueG.B.Shabat':'catalogue G. B. Shabat',
        'Yu.Shabat':'Yu. Shabat', 'formula(31)':'formula (31)',
        'f=2omega':r'\(f=2\omega\)',
        'E7(7)/SU(8)':r'\(E_{7(7)}/SU(8)\)',
        'H0=int omega |a|2':r'\(H_0=\int\omega|a|^2\)',
        'B(L2)':r'\(B(L^2)\)',
        'MultiplicationL∞':'Multiplication by the bounded functions',
        'onRplus':r'on \(\mathbb R_+\)',
    }
    for old,new in readability.items():
        s=s.replace(old,new)
    # Literal source/file-name punctuation is escaped only outside mathematics.
    def escape_literals(chunk):
        chunk=re.sub(r'(?<!\\)_',lambda _:r'\_',chunk)
        chunk=re.sub(r'(?<!\\)\^',lambda _:r'\textasciicircum{}',chunk)
        return re.sub(r'(?<!\\)%',lambda _:r'\%',chunk)
    return process_outside(s,escape_literals)

changes=[]
evidence_edits={
 ('P000852','Gilkey date'):'The original scan contains both dates. Numdam metadata confirms volume 38, number 2 (1979), pages 201--240.',
 ('P000852','multiplicity conjecture beside formula(31)'):r'The original scan has an arrow from the underlined Russian word for incorrect to the conjecture attributed to S.~Gelfand.',
 ('P000866','speaker heading'):'The original scan retains the tentative parenthesis; the supplied talk catalogue assigns record 471 to Batalin.',
 ('P000917','Carry-out: allowable-chain equation'):r'The scan clearly has equality and \(j-2i\). The definitions in \citet{goreskymacpherson1977dualite,goreskymacpherson1980intersection} give the corrected perversity bounds. This is a faithful mathematical error in the next-year spillover.',
 ('P000918','Carry-out: real admissibility versus local inversion'):r'\citet[introduction and Sec.~1.3]{gelfandgindikinshapiro1979local} and \citet[Sec.~2, following Definition~1]{gelfandgraev1980admissible} explicitly state that the real coefficient is zero.'
}
for row in rows:
    source_place=row['place']
    for field in ('place','transcription_reads','should_read','evidence'):
        before=row[field];s=exact.get(before,before)
        if field=='evidence':s=evidence_edits.get((row['page'],source_place),s)
        if (row['page'],source_place,field) in whole_math and not s.startswith(r'\('):
            s=r'\('+s+r'\)'
        if row['page']=='P000879' and source_place=='stress tensor' and field=='should_read' and not s.startswith(r'\('):
            first,second=s.split(', or ')
            s=r'\('+first+r'\), or \('+second+r'\).'
        for old,new in parts.items():
            s=process_outside(s,lambda chunk:chunk.replace(old,new))
        s=process_outside(s,clean_plain)
        if s!=before:
            changes.append({'page':row['page'],'place':row['place'],'field':field,
                            'before':before,'after':s})
            row[field]=s
with p.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
(D/'code/corrections_typesetting_output.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'correction_cells_typeset':len(changes)},indent=2))
