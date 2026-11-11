#!/usr/bin/env python3
"""Exact rational checks of the two editorial formula audits; standard library only.
These calculations verify identities; they claim no mathematical novelty.
"""
from fractions import Fraction as F
from pathlib import Path
import json

class Poly:
    names=('q1','q2','p1','p2','c','d','E','a')
    n=len(names)
    def __init__(self,terms=0):
        if isinstance(terms,Poly):self.t=terms.t.copy()
        elif isinstance(terms,dict):self.t={p:F(c) for p,c in terms.items() if c}
        else:self.t={(0,)*self.n:F(terms)} if terms else {}
    @classmethod
    def variable(cls,i):
        p=[0]*cls.n;p[i]=1;return cls({tuple(p):1})
    def __add__(self,b):
        b=Poly(b);d=self.t.copy()
        for p,c in b.t.items():d[p]=d.get(p,F(0))+c
        return Poly(d)
    __radd__=__add__
    def __neg__(self):return Poly({p:-c for p,c in self.t.items()})
    def __sub__(self,b):return self+-Poly(b)
    def __rsub__(self,b):return Poly(b)+-self
    def __mul__(self,b):
        b=Poly(b);d={}
        for p,c in self.t.items():
            for q,e in b.t.items():
                z=tuple(i+j for i,j in zip(p,q));d[z]=d.get(z,F(0))+c*e
        return Poly(d)
    __rmul__=__mul__
    def __truediv__(self,c):return self*F(1,c)
    def __pow__(self,k):
        assert isinstance(k,int) and k>=0
        z=Poly(1)
        for _ in range(k):z=z*self
        return z
    def diff(self,i):
        z={}
        for p,c in self.t.items():
            if p[i]:q=list(p);q[i]-=1;z[tuple(q)]=c*p[i]
        return Poly(z)
    def substitute(self,i,value):
        z=Poly()
        for p,c in self.t.items():
            q=list(p);q[i]=0;z+=Poly({tuple(q):c})*Poly(value)**p[i]
        return z
    def __eq__(self,b):return self.t==Poly(b).t

def pb(f,g):return sum((f.diff(i)*g.diff(i+2)-f.diff(i+2)*g.diff(i) for i in range(2)),Poly())
q1,q2,p1,p2,c,d,E,a=(Poly.variable(i) for i in range(8))
J1a=p1*p2-q2**2/2-F(5,2)*q1**2*q2-a*q1**4+c*q1**2-d*q1
D=q1**5+2*c*q1**3+d*q1**2-4*q1*q2**2+4*c*q1*q2-2*d*q2
J2=p1**2-2*q1*p1*p2+2*(q2-c)*p2**2+D
bracket=pb(J1a,J2)
assert bracket==(8*a-5)*q1**3*(q1*p2-p1)
J1=J1a.substitute(7,F(5,8))
assert pb(J1,J2)==0
flow=[p2,p1,5*q1*q2+F(5,2)*q1**3-2*c*q1+d,q2+F(5,2)*q1**2]
def Dx(f):return sum((f.diff(i)*flow[i] for i in range(4)),Poly())
assert Dx(J1)==0 and Dx(J2)==0
P=E**2+q1*E/2+(q1**2-2*q2+2*c)/16
R=(E-q1)*P**2+P*Dx(Dx(P))/2-Dx(P)**2/4
expected=E**5+c*E**3/4-d*E**2/16+(J1/32+c**2/64)*E-J2/256-c*d/128
assert R==expected
assert Dx(R)==0
assert Dx(Dx(Dx(P)))-4*(q1-E)*Dx(P)-2*p2*P==0

class Jet:
    def __init__(self,v,grad):self.v=F(v);self.g=tuple(map(F,grad))
    def lift(self,o):return o if isinstance(o,Jet) else Jet(o,[0]*len(self.g))
    def __add__(self,o):
        o=self.lift(o);return Jet(self.v+o.v,[a+b for a,b in zip(self.g,o.g)])
    __radd__=__add__
    def __neg__(self):return Jet(-self.v,[-a for a in self.g])
    def __sub__(self,o):return self+-self.lift(o)
    def __rsub__(self,o):return self.lift(o)+-self
    def __mul__(self,o):
        o=self.lift(o);return Jet(self.v*o.v,[a*o.v+self.v*b for a,b in zip(self.g,o.g)])
    __rmul__=__mul__
    def inverse(self):return Jet(1/self.v,[-a/self.v**2 for a in self.g])
    def __truediv__(self,o):return self*self.lift(o).inverse()
    def __rtruediv__(self,o):return self.lift(o)*self.inverse()

checks=[]
for n in range(3,7):
    x=[F(3),F(4)]+[F(0)]*(n-2);r=F(5)
    u=[Jet(x[h]/r,[F(h==l)/r-x[h]*x[l]/r**3 for l in range(n)]) for h in range(n)]
    Du=[[Jet(F(i==h)/r-x[i]*x[h]/r**3,[-F(i==h)*x[l]/r**3-(F(i==l)*x[h]+x[i]*F(h==l))/r**3+3*x[i]*x[h]*x[l]/r**5 for l in range(n)]) for h in range(n)] for i in range(n)]
    norm=1+sum((v*v for v in u),Jet(0,[0]*n))
    for alpha,beta,label in [(F(1,n-2),F(4,n-2),'literal'),(F(4,n-2),F(4,n-2),'reconstructed')]:
        flux=[]
        for j in range(n):
            row=[]
            for k in range(n):
                z=Jet(0,[0]*n)
                for i in range(n):
                    for h in range(n):
                        A=F(i==j)*F(h==k)+(F(j==k)+alpha*u[j]*u[k]/norm)*(F(i==h)+beta*u[i]*u[h]/norm)
                        z+=A*Du[i][h]
                row.append(z)
            flux.append(row)
        residual=[sum(flux[j][k].g[j] for j in range(n)) for k in range(n)]
        expected_residual=[(n-1)*(alpha*F(n-2,2)-2)*v/r**3 for v in x]
        assert residual==expected_residual,(n,label,residual,expected_residual)
        checks.append({'dimension':n,'tensor':label,'point':[str(z) for z in x],'divergence':[str(z) for z in residual]})
result={'arithmetic':'exact rational coefficients; no floating point',
 'poisson_bracket':'{J1(a),J2}=(8a-5)q1^3(q1p2-p1)',
 'corrected_bracket_zero':True,'hamiltonians_conserved':True,
 'spectral_polynomial':'E^5+(c/4)E^3-(d/16)E^2+(J1/32+c^2/64)E-J2/256-cd/128',
 'spectral_identity_zero':True,'third_order_identity_zero':True,
 'giusti_independent_tensor_jet_checks':checks,
 'scope':'Polynomial identities are symbolic in all variables. Tensor jet checks are finite checks supplementing the full dimension-independent analytic proof; they are not a substitute for it.'}
out=Path(__file__).with_name('exact_checks.json');out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
