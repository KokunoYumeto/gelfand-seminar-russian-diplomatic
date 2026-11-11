"""Exact checks for P000970 and a bounded genus-two realization.

All coefficients are in QQ[a,x].  Operators are in left normal form
sum c_j(x) D^j, with D x - x D = 1.  No floating point is used.
Run from the chapter directory: python code/check_weyl.py > checks/weyl_output.txt
"""
from math import comb
import json
from pathlib import Path
import sympy as s

x,a,z=s.symbols('x a z')

def clean(p):
    return {k:s.expand(v) for k,v in p.items() if s.expand(v)!=0}

def add(*ps):
    out={}
    for p in ps:
        for k,v in p.items():
            out[k]=out.get(k,0)+v
    return clean(out)

def scale(p,c):
    return clean({k:c*v for k,v in p.items()})

def mul(p,q):
    out={}
    for i,pi in p.items():
        for j,qj in q.items():
            for k in range(i+1):
                n=i+j-k
                out[n]=out.get(n,0)+comb(i,k)*pi*s.diff(qj,x,k)
    return clean(out)

def power(p,n):
    out={0:s.Integer(1)}
    for _ in range(n):
        out=mul(out,p)
    return out

def comm(p,q):
    return add(mul(p,q),scale(mul(q,p),-1))

def action(p,f):
    return s.expand(sum(v*s.diff(f,x,k) for k,v in p.items()))

def printop(name,p):
    print(name, '{'+', '.join(str(k)+': '+str(p[k]) for k in sorted(p,reverse=True))+'}')

D={1:s.Integer(1)}
L={2:s.Integer(1),0:x**3+a}
L4=add(power(L,2),{0:2*x})
L6=add(power(L,3),scale(mul({0:x},L),3),scale(D,3))
badL6=add(power(L,3),scale(mul({0:x**2},L),3),scale(mul(L,{0:x**2}),3))
bad=comm(L4,badL6)
print('SYMPY_VERSION',s.__version__)
print('CONVENTION D*x-x*D = 1:',comm(D,{0:x}))
printop('NOTEBOOK_LITERAL_COMMUTATOR',bad)
assert bad
printop('DIXMIER_CORRECTED_COMMUTATOR',comm(L4,L6))
assert not comm(L4,L6)
ell=add(power(L6,2),scale(power(L4,3),-1))
printop('DIXMIER_M2_MINUS_L4_CUBED',ell)
assert ell=={0:-a}

P=add(power(L,2),{0:6*x})
M=add(mul(L,power(P,2)),mul(add(scale(mul({0:x},L),3),scale(D,-3)),P),
      scale(mul({0:x**2},L),9),{1:-18*x,0:s.Integer(9)})
compactM=add(power(L,5),
             scale(add(mul({0:x},power(L,3)),mul(power(L,3),{0:x})),s.Rational(15,2)),
             scale(add(mul({0:x**2},L),mul(L,{0:x**2})),45))
compact_offset=add(compactM,scale(M,-1))
assert compact_offset=={0:s.Integer(9)}
printop('MIRONOV_DISPLAYED_FORM_MINUS_CENTERED_M',compact_offset)
print('MIRONOV_DISPLAYED_FORM_REQUIRES_SCALAR_SHIFT -9 for stated F')
assert not comm(P,compactM)
Q=z**2+3*x*z+9*x**2
V=x**3+a
W=6*x
Qx=s.diff(Q,x)
F=s.expand((4*(z-W)*Q**2-4*V*Qx**2+s.diff(Q,x,2)**2
              -2*Qx*s.diff(Q,x,3)+2*Q*(2*s.diff(V,x)*Qx
              +4*V*s.diff(Q,x,2)+s.diff(Q,x,4)))/4)
print('GENUS2_Q',Q)
print('GENUS2_F',F)
assert s.diff(F,x)==0
assert F==z**5+27*a*z**2+81
printop('GENUS2_P',P)
printop('GENUS2_M',M)
cm=comm(P,M)
rel=add(power(M,2),scale(power(P,5),-1),scale(power(P,2),-27*a),{0:-81})
printop('GENUS2_COMMUTATOR',cm)
printop('GENUS2_SPECTRAL_RELATION_RESIDUAL',rel)
assert not cm and not rel
disc=s.factor(s.discriminant(F,z))
print('GENUS2_DISCRIMINANT',disc)
print('SQUAREFREE_AT_a_0',s.gcd(F.subs(a,0),s.diff(F,z).subs(a,0)))
assert s.gcd(F.subs(a,0),s.diff(F,z).subs(a,0))==1

# Independent check: compute action directly on polynomials, without multiplying
# coefficient dictionaries.  Commutator order <= 13; relation order <= 20.
# An order <=r differential operator is zero if it kills 1,x,...,x^r.
# This triangular fact makes these exact checks complete at each chosen a.
def repeated(op,f,n):
    for _ in range(n):
        f=action(op,f)
    return f

for av in [-2,0,1,3]:
    ps={k:v.subs(a,av) for k,v in P.items()}
    ms={k:v.subs(a,av) for k,v in M.items()}
    for n in range(21):
        f=x**n
        assert s.expand(action(ps,action(ms,f))-action(ms,action(ps,f)))==0
        assert s.expand(action(ms,action(ms,f))-repeated(ps,f,5)
                        -27*av*repeated(ps,f,2)-81*f)==0
    print('INDEPENDENT_ACTION_CHECK a='+str(av)+' monomials=0..20 PASS')

print('ALL EXACT WEYL CHECKS PASSED')
