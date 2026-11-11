"""Typeset the prose-authored correction formulas without changing wording."""
from pathlib import Path
import csv,re,pprint,json
p=Path(__file__).resolve().parent
script=p/'make_support.py';s=script.read_text()
marker='# These cells were authored as plain prose' if '# These cells were authored as plain prose' in s else '# The prose-authored cells'
raw=s[s.index('rows=[]\ndef corr'):s.index(marker)]
ns={};exec(raw,ns);rows=ns['rows']
math={
'e_1,...,e_n':r'e_1,\ldots,e_n',
'E_j x=0':r'E_jx=0','h v=chi(h)v':r'hv=\chi(h)v',
'M(psi)':r'M(\psi)','L(psi)':r'L(\psi)','M(chi)':r'M(\chi)',
'e_{i_k}...e_{i_1}':r'e_{i_k}\cdots e_{i_1}',
'[L_psi : M_i/M_{i+1}]':r'[L_\psi:M_i/M_{i+1}]',
'[M_i/M_{i+1} : L_psi]':r'[M_i/M_{i+1}:L_\psi]',
'M_i/M_{i+1}':r'M_i/M_{i+1}',
'P(q)=sum q^i':r'P(q)=\sum_iq^i',
'q^{(length(y)-length(x)-j)/2}':r'q^{(\ell(y)-\ell(x)-j)/2}',
'P_{e,s}=1':r'P_{e,s}=1',
'L(chi)_lambda':r'L(\chi)_\lambda',
'chi=(a_1,...,a_n)':r'\chi=(a_1,\ldots,a_n)',
'0,...,n-1':r'0,\ldots,n-1',
'a_i=lambda_{n+1-i}+i-1':r'a_i=\lambda_{n+1-i}+i-1',
'm(lambda,chi)=P_{n_lambda,n_chi}(1)':r'm(\lambda,\chi)=P_{n_\lambda,n_\chi}(1)',
'm(chi,lambda)=dim L(chi)_lambda':r'm(\chi,\lambda)=\dim L(\chi)_\lambda',
'dim L(lambda)_mu=P_{n_mu,n_lambda}(1)':r'\dim L(\lambda)_\mu=P_{n_\mu,n_\lambda}(1)',
'Sym^3(C^2)':r'\operatorname{Sym}^3(\mathbb C^2)',
'gl(2)':r'\mathfrak{gl}_2','sl(2)':r'\mathfrak{sl}_2','gl2':r'\mathfrak{gl}_2','sl2':r'\mathfrak{sl}_2',
'[R,R]':r'[R,R]',
'x=0':r'x=0','x=+-1':r'x=\pm1',
'p:2^Omega -> (0,1)':r'p:2^\Omega\to(0,1)',
'p:2^Omega -> {0,1}':r'p:2^\Omega\to\{0,1\}',
'p(Omega)=1':r'p(\Omega)=1','p(empty)=0':r'p(\varnothing)=0',
'P(x prime=x double-prime)=1':r'P(x^{\prime}=x^{\prime\prime})=1',
'omega^{-1}':r'\omega^{-1}','omega^2':r'\omega^2','omega-1':r'\omega-1',
'G=union G_n':r'G=\bigcup_nG_n','G_n':r'G_n','G(Gamma,z)':r'G(\Gamma,z)',
'O(t^i)':r'O(t^i)','t^i':r't^i','q^i':r'q^i','M_i':r'M_i','H^i':r'H^i',
'n_+':r'\mathfrak n_+','n_-':r'\mathfrak n_-',
'chi':r'\chi','lambda':r'\lambda','rho':r'\rho','omega':r'\omega','epsilon':r'\varepsilon',
'+--':r'+\!-\!-','1/4':r'\tfrac14','A3':r'A_3',
'R':r'R','V':r'V','C':r'\mathbb C','n':r'n','x':r'x','p':r'p','P':r'P',
}
helpers='''# The prose-authored cells below contain mathematical formulas. Protect
# recognized formulas with math delimiters, then escape only surrounding prose.
MATH_REPLACEMENTS = '''+pprint.pformat(math,sort_dicts=False,width=100)+'''
def correction_tex_escape(value):
    value=str(value)
    protected=[]
    pattern=re.compile(r'(?<![A-Za-z0-9_])(?:'+ '|'.join(re.escape(k) for k in sorted(MATH_REPLACEMENTS,key=len,reverse=True)) +r')(?![A-Za-z0-9_])')
    def keep(match):
        protected.append(r"\\("+MATH_REPLACEMENTS[match.group(0)]+r"\\)")
        return "@@MATH"+str(len(protected)-1)+"@@"
    value=pattern.sub(keep,value)
    mapping={"\\\\":r"\\textbackslash{}","&":r"\\&","%":r"\\%","$":r"\\$","#":r"\\#","_":r"\\_","{":r"\\{","}":r"\\}","~":r"\\textasciitilde{}","^":r"\\textasciicircum{}"}
    value=''.join(mapping.get(ch,ch) for ch in value)
    for n,formula in enumerate(protected):value=value.replace("@@MATH"+str(n)+"@@",formula)
    return value
'''
start=s.index(marker)
end=s.index('for row in rows:',start)
s=s[:start]+helpers+s[end:]
script.write_text(s)
helper_ns={'re':re};exec(helpers,helper_ns)
for row in rows:
 for field in ('place','transcription_reads','should_read','evidence'):row[field]=helper_ns['correction_tex_escape'](row[field])
with (p/'corrections.csv').open('w',newline='') as f:
 writer=csv.DictWriter(f,fieldnames=['page','place','transcription_reads','should_read','evidence','applies_to','type']);writer.writeheader();writer.writerows(rows)
# Fix the one long body formula and asymmetric quotation pair identified in QA.
a=json.loads((p/'items.json').read_text())
for x in a:
 if x['id']=='1981-540.1':
  x['notes']=x['notes'].replace('``unordered sets\\textquotesingle\\','“unordered sets”')
  x['reconstruction']=x['reconstruction'].replace('``Invariant\\textquotesingle\\','“Invariant”')
  old=r'Thus \(S_\chi(uv_\chi,wv_\chi)=\chi(\operatorname{HC}(\tau(u)w))\), using the Harish-Chandra projection extended by evaluation on \(U(\mathfrak h)\).'
  new=r'Thus \[S_\chi(uv_\chi,wv_\chi)=\chi(\operatorname{HC}(\tau(u)w)).\] Here the Harish-Chandra projection is followed by evaluation on \(U(\mathfrak h)\).'
  assert old in x['statement'] or new in x['statement'];x['statement']=x['statement'].replace(old,new)
(p/'items.json').write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
build=p/'make_items.py';text=build.read_text().replace(old,new).replace('``unordered sets\\textquotesingle\\','“unordered sets”').replace('``Invariant\\textquotesingle\\','“Invariant”');build.write_text(text)
print('Typeset formulas in all 35 correction rows; updated the long identity and paired quotes in 1981-540.1.')
