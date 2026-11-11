#!/usr/bin/env python3
"""Exact editorial audits, not new research results. Run with Python/SymPy."""
from pathlib import Path
from fractions import Fraction
import sympy as s
out=[]
def report(label,value):
    out.append(f'{label}: {value}')
def zero(label,expr):
    z=s.simplify(expr)
    assert z==0,(label,z)
    report(label,'PASS (exact zero)')

# Kernel: first derivation from the geometric series; second from rational identities.
l,r=s.symbols('lambda r',nonzero=True)
k=s.factor((r*s.diff(r/(1-r),r)).subs(r,1/l)/(l-1/l))
target=l**2/((l-1)**3*(l+1)); t=l+1/l
zero('Kernel series / rational expression',k-target)
zero('Kernel square trace identity',k**2*(t-2)**3*(t+2)-1)
report('Kernel closed form',str(k))
# Independently check finite sums plus exact tail using Python Fractions, without SymPy.
for lam in (Fraction(3,2),Fraction(2),Fraction(3),Fraction(5)):
    for N in (1,2,7,23):
        q=1/lam
        finite=sum(Fraction(j)*q**j for j in range(1,N+1))
        tail=q**(N+1)*((N+1)-N*q)/(1-q)**2
        exact=lam**2/((lam-1)**3*(lam+1))
        assert (finite+tail)/(lam-1/lam)==exact
    report(f'Independent rational finite-tail checks lambda={lam}','PASS N=1,2,7,23')

# General point transformation formula, independently expanded to degree two.
x,y,p,e=s.symbols('x y p epsilon')
a,b,c,f,g=[s.Function(z)(x) for z in ('a','b','c','f','g')]
F=a*y*y+b*y*p+c*p*p
X=x+f*y;Y=y+g*y*y
def D(v): return s.diff(v,x)+p*s.diff(v,y)+F*s.diff(v,p)
XX=D(X);YY=D(Y)
new=(D(YY)*XX-YY*D(XX))/XX**3
quadr=s.expand(s.series(new.subs({y:e*y,p:e*p}),e,0,3).removeO().coeff(e,2))
expected=(a+s.diff(g,x,2))*y*y+(b+4*s.diff(g,x)-s.diff(f,x,2))*y*p+(c+2*g-2*s.diff(f,x))*p*p
zero('Full chain rule / quadratic coefficient formula',quadr-expected)
report('Quadratic coefficient formula',str(s.collect(quadr,[y,p])))
residual=a+s.diff(c,x,2)/6-s.diff(b,x)/3
subg=s.diff(f,x)-c/2
after=s.expand(expected.subs(g,subg).doit())
after=after.subs(s.diff(f,x,3),(2*s.diff(c,x,2)-s.diff(b,x))/3).subs(s.diff(f,x,2),(2*s.diff(c,x)-b)/3)
zero('Eliminated quadratic terms',after-residual*y*y)

# Independent normalization check with concrete polynomial coefficients and an exact full transform.
F0=(1+x*x)*y*y+(x+2)*y*p+(x**3-x)*p*p
f0=x**4/s.Integer(6)-x**3/s.Integer(18)-2*x*x/s.Integer(3)
g0=s.diff(f0,x)-(x**3-x)/2
def D0(v): return s.diff(v,x)+p*s.diff(v,y)+F0*s.diff(v,p)
X0=x+f0*y;Y0=y+g0*y*y
new0=(D0(D0(Y0))*D0(X0)-D0(Y0)*D0(D0(X0)))/D0(X0)**3
q0=s.expand(s.series(new0.subs({y:e*y,p:e*p}),e,0,3).removeO().coeff(e,2))
expected0=(1+x*x+x-s.Rational(1,3))*y*y
zero('Independent polynomial normalization instance',q0-expected0)

# Tresse H on the normalized reference solution and on the counterexample.
def H_of(F):
    def d(v):return s.diff(v,x)+p*s.diff(v,y)+F*s.diff(v,p)
    return s.expand(d(d(s.diff(F,p,2)))-4*d(s.diff(F,y,p))-s.diff(F,p)*d(s.diff(F,p,2))+6*s.diff(F,y,2)-3*s.diff(F,y)*s.diff(F,p,2)+4*s.diff(F,p)*s.diff(F,y,p))
H=H_of(F)
zero('Tresse H on reference solution equals 12A',H.subs({y:0,p:0})-12*residual)
zero('Counterexample ypp=y^3 gives H=36y',H_of(y**3)-36*y)
report('Counterexample invariant',str(H_of(y**3)))

# Vector-field transformation under an arbitrary coordinate change.
phi=s.Function('phi')(x);v=s.Function('v')(x)
V=s.diff(phi,x)*v
DX=lambda z:s.diff(z,x)/s.diff(phi,x)
I2new=2*V*DX(DX(V))-DX(V)**2
Sch=s.diff(phi,x,3)/s.diff(phi,x)-s.Rational(3,2)*(s.diff(phi,x,2)/s.diff(phi,x))**2
zero('General I2 transformation / Schwarzian identity',I2new-(2*v*s.diff(v,x,2)-s.diff(v,x)**2+2*v*v*Sch))
for phi0 in ((2*x+1)/(x+1),(x-2)/(3*x+4)):
    v0=1+x+x*x+x**4
    VV=s.diff(phi0,x)*v0
    dd=lambda z:s.diff(z,x)/s.diff(phi0,x)
    zero(f'Independent Mobius example {phi0}',2*VV*dd(dd(VV))-dd(VV)**2-(2*v0*s.diff(v0,x,2)-s.diff(v0,x)**2))

# Auxiliary elimination: direct substitution and independent square completion.
A,B,Faux,Gaux,m,h=s.symbols('A B Faux Gaux m g')
P=m*A+h*(A*A-B*B);Q=m*B+2*h*A*B
L=s.Rational(1,2)*(Faux**2+Gaux**2)+Faux*P+Gaux*Q
sol=s.solve([s.diff(L,Faux),s.diff(L,Gaux)],[Faux,Gaux])
eliminated=s.expand(L.subs(sol))
claimed=-m*m*(A*A+B*B)/2-m*h*A*(A*A+B*B)-h*h*(A*A+B*B)**2/2
zero('Auxiliary Euler substitution',eliminated-claimed)
zero('Independent completion of two squares',L-(s.Rational(1,2)*(Faux+P)**2+s.Rational(1,2)*(Gaux+Q)**2-(P*P+Q*Q)/2))
report('Eliminated scalar polynomial',str(s.factor(eliminated)))
for vals in ((1,2,3,4),(-2,1,5,-3),(0,3,-1,2)):
    aa,bb,mm,hh=vals
    assert eliminated.subs({A:aa,B:bb,m:mm,h:hh})==claimed.subs({A:aa,B:bb,m:mm,h:hh})
report('Independent auxiliary numerical substitutions','PASS 3 integer parameter sets')

# An explicit real Majorana matrix check for the notebook signature.
E=s.Matrix([[0,1],[-1,0]]);S=s.Matrix([[0,1],[1,0]]);Z=s.diag(1,-1);I=s.eye(2)
gamma=[s.kronecker_product(E,I),s.kronecker_product(S,S),s.kronecker_product(S,Z),s.kronecker_product(Z,I)]
metric=[-1,1,1,1]
for i in range(4):
    for j in range(4):
        assert gamma[i]*gamma[j]+gamma[j]*gamma[i]==(2*metric[i]*s.eye(4) if i==j else s.zeros(4))
    assert (gamma[0]*gamma[i]).T==gamma[0]*gamma[i]
report('Real Clifford matrices and symmetric C gamma bilinears','PASS 16 Clifford identities and 4 bilinear symmetries')

text='Verification date: 2026-11-10\nPurpose: editorial mathematical audit; no novelty claim.\n'+'\n'.join(out)+'\n'
Path(__file__).with_name('early_checks_output.txt').write_text(text)
print(text)
