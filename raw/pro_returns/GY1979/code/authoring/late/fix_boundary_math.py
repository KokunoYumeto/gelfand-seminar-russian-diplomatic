"""Repair inline mathematical delimiters in the boundary working draft."""
from pathlib import Path
import re
p=Path(__file__).with_name('boundary_inventory.md')
s=p.read_text().replace('\x08ar',r'\bar')
pairs={
 '(2n)':r'2n',
 '(X=X_{2n}supset X_{2n-2}supset X_{n-3}supset X_{n-4}supsetcdots)':r'X=X_{2n}\supset X_{2n-2}\supset X_{n-3}\supset X_{n-4}\supset\cdots',
 r'(X_i\setminus X_{i-1})':r'X_i\setminus X_{i-1}',
 '(i)':'i','(2n-2)':'2n-2','(n-3,n-4)':'n-3,n-4','(X_{2n-i})':'X_{2n-i}',
 r'(dim(sigma_j\cap X_{2n-i})=j-2i)':r'\dim(\sigma_j\cap X_{2n-i})=j-2i',
 r'(\bar p)':r'\bar p','(j)':'j','(c)':'c',
 r'(\bar m(i)=\lfloor(i-2)/2\rfloor)':r'\bar m(i)=\lfloor(i-2)/2\rfloor',
 '(j-c-1)':'j-c-1',r'(X=S^2\vee S^2)':r'X=S^2\vee S^2',
 '(0,1,2)':'0,1,2','(mathbb Z,0,mathbb Z^2)':r'\mathbb Z,0,\mathbb Z^2',
 '(mathbb Z^2,0,mathbb Z^2)':r'\mathbb Z^2,0,\mathbb Z^2',
 r'(\bar m(2)=0)':r'\bar m(2)=0','(L^2)':'L^2','(L_2)':'L_2','(d)':'d','(U)':'U',
 r'(D\subset\mathbb R^n)':r'D\subset\mathbb R^n','((n+k-1))':'n+k-1',
 r'(x_i=\varphi_i(x_1,\xi))':r'x_i=\varphi_i(x_1,\xi)','(chi)':r'\chi',
 r'(F=I_\chi f)':r'F=I_\chi f',
 r'(f(x_1,\varphi_1,\ldots,\varphi_n))':r'f(x_1,\varphi_1,\ldots,\varphi_n)',
 '(f)':'f','(mathbb R^n)':r'\mathbb R^n','(n)':'n','(n+k-1)':'n+k-1',
 '(x_1)':'x_1','(n-1)':'n-1',r'(2,\ldots,n)':r'2,\ldots,n','(f(x^0))':'f(x^0)',
 '(k)':'k',r'(x^0\in D)':r'x^0\in D','(Gamma_{x^0})':r'\Gamma_{x^0}',
 r'(dim\Gamma_{x^0}=(n+k-1)-(n-1)=k)':r'\dim\Gamma_{x^0}=(n+k-1)-(n-1)=k',
 '(mathcal H_{x^0})':r'\mathcal H_{x^0}','(F)':'F','(k>1)':'k>1','(k=1)':'k=1',
 r'(f\mapsto\int\mathcal H_{x^0}I_\chi f)':r'f\mapsto\int\mathcal H_{x^0}I_\chi f',
 '(x^0)':'x^0',r'(mathcal H_{x^0}F=d(\mu F))':r'\mathcal H_{x^0}F=d(\mu F)',
 '(mathcal H=0)':r'\mathcal H=0',
}
# One regex pass prevents substitutions inside newly repaired expressions.
pat=re.compile('|'.join(re.escape(k) for k in sorted(pairs,key=len,reverse=True)))
s=pat.sub(lambda m:r'\('+pairs[m.group()]+r'\)',s)
s=s.replace('The main corrections CSV contains the page-boundary correction that points to this inventory.',
 'The main corrections CSV contains both the page-boundary correction and the specific mathematical and attribution corrections inventoried here.')
assert not any(ord(c)<32 and c not in '\n\t' for c in s)
assert not re.search(r'(?<!\\)\b(?:mathbb|mathcal|supset|cdots|sigma_j|Gamma_)\b',s)
p.write_text(s)
print('Boundary inline math and control characters repaired.')
