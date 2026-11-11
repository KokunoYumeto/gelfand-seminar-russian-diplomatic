"""Exact checks for the P000567--P000568 verification note (Python stdlib).

Run: python code/check_spectral_compatibility.py
Sparse multivariate polynomials over Q implement the identity checks.
Finite rational-parameter checks supplement, and do not replace, the proofs.
"""
from fractions import Fraction as F

NAMES = ('E','p','p1','p2','y','u','a','b','ap','bp','c','t')
N = len(NAMES)

class Poly:
    def __init__(self, value=0):
        self.d = dict(value) if isinstance(value,dict) else ({(0,)*N:F(value)} if value else {})
        self.d = {k:F(v) for k,v in self.d.items() if v}
    def __add__(self, other):
        other = other if isinstance(other,Poly) else Poly(other)
        d = dict(self.d)
        for k,v in other.d.items(): d[k]=d.get(k,F(0))+v
        return Poly(d)
    __radd__=__add__
    def __neg__(self): return Poly({k:-v for k,v in self.d.items()})
    def __sub__(self,other): return self+-other if isinstance(other,Poly) else self+(-F(other))
    def __rsub__(self,other): return -self+other
    def __mul__(self,other):
        other=other if isinstance(other,Poly) else Poly(other)
        d={}
        for k,v in self.d.items():
            for l,w in other.d.items():
                m=tuple(a+b for a,b in zip(k,l));d[m]=d.get(m,F(0))+v*w
        return Poly(d)
    __rmul__=__mul__
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        r=Poly(1)
        for _ in range(n): r=r*self
        return r

def variable(name):
    p=[0]*N;p[NAMES.index(name)]=1
    return Poly({tuple(p):F(1)})

def check(label,p):
    assert not p.d,(label,p.d)
    print(label+': 0 (exact polynomial)')

E,p,p1,p2,y,u,a,b,ap,bp,c,t=map(variable,NAMES)

# Formal real/imaginary components of 4 P^2 times the Riccati residual.
# chi=y/P-i P_x/(2P); multiplying clears all denominators.
res_real=(-2*p*p2+2*p1**2)+(4*y**2-p1**2)+4*p**2*(u-E)
res_imag=4*y*p1-4*y*p1
target=4*p**2*(u-E)+4*y**2-2*p*p2+p1**2
check('Riccati real numerator minus 4P^2(u-Q)',res_real-target)
check('Riccati imaginary numerator',res_imag)

# Independent logarithmic-derivative route ell=psi_x/psi=P_x/(2P)+i y/P.
ell_real_derivative=2*p*p2-2*p1**2
ell_square_real=p1**2-4*y**2
direct=-(ell_real_derivative+ell_square_real)+4*p**2*(u-E)
check('Direct Schrodinger numerator minus 4P^2(u-Q)',direct-target)
check('Direct imaginary numerator',-(-4*y*p1+4*y*p1))

# Independent product-of-solutions/Wronskian route, psi''=(u-E)psi.
prod=a*b
prodx=ap*b+a*bp
prodxx=2*(u-E)*a*b+2*ap*bp
W=a*bp-ap*b
check('Four times product identity plus W^2',4*(E-u)*prod**2+2*prod*prodxx-prodx**2+W**2)

# Gauge invariance after clearing denominators, c independent of x.
scaled=4*(c*p)**2*(u-E)+4*(c*y)**2-2*(c*p)*(c*p2)+(c*p1)**2
check('Gauge compatibility numerator minus c^2 times original',scaled-c**2*target)

# Nonconstant example u=2/x^2, write t=1/x for an exact polynomial identity.
P=E+t**2
Px=-2*t**3
Pxx=6*t**4
R=E**3
check('Nonconstant P=E+x^-2, R=E^3, u=2x^-2',4*R-4*(E-2*t**2)*P**2-2*P*Pxx+Px**2)

# x-independent examples require only R/P^2, hence no transcendental computation.
print('P=exp(E), R=exp(E): Q=E-exp(-E), dQ/dE=1+exp(-E), not identically zero.')
print('P=exp(E), R=E exp(2E): Q=0 exactly.')
print('P=exp(E^m), R=(E-C) exp(2E^m): Q=C, for any constant C and integer m>=1.')

def q_value(e,r,pv,px,pxx):
    return e-r/pv**2+pxx/(2*pv)-px**2/(4*pv**2)

for xv in [F(1,2),F(1),F(3,2),F(3)]:
    for ev in [F(-5),F(0),F(2,3),F(7)]:
        pv=ev+1/xv**2
        if not pv: continue
        computed=q_value(ev,ev**3,pv,-2/xv**3,6/xv**4)
        assert computed==2/xv**2
        print(f'Rational independent substitution x={xv}, E={ev}: Q={computed}')

print('All exact polynomial and rational checks passed.')
