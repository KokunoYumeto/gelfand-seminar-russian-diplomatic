"""Finite exact truncation checks of the formal expression on P000970.

The cube's differential part depends only on input coefficients through
order -4, so truncating products below -12 is sufficient here.
"""
import sympy as s
x,a=s.symbols('x a')
LOW=-12
def clean(p):
    return {k:s.expand(v) for k,v in p.items() if s.expand(v)!=0}
def add(*ps):
    out={}
    for p in ps:
        for k,v in p.items(): out[k]=out.get(k,0)+v
    return clean(out)
def scale(p,c): return clean({k:c*v for k,v in p.items()})
def mul(p,q):
    out={}
    for i,ai in p.items():
        for j,bj in q.items():
            K=i+j-LOW
            if i>=0: K=min(K,i)
            for k in range(K+1):
                n=i+j-k
                out[n]=out.get(n,0)+s.binomial(i,k)*ai*s.diff(bj,x,k)
    return clean(out)
def positive(p): return {k:v for k,v in p.items() if k>=0}
V=x**3+a
L={2:s.Integer(1),0:V}
D={1:s.Integer(1)}
# Recurrence from (D²+V)*B=1, coefficient by coefficient.
B={-2:s.Integer(1)}
for j in range(-3,LOW-1,-1):
    B[j]=s.expand(-2*s.diff(B.get(j+1,0),x)
                  -s.diff(B.get(j+2,0),x,2)-V*B.get(j+2,0))
B=clean(B)
left=mul(L,B)
right=mul(B,L)
assert {k:v for k,v in left.items() if k>=LOW+2}=={0:1}
assert {k:v for k,v in right.items() if k>=LOW+2}=={0:1}
A=add(L,mul({0:x},B))
actual=positive(mul(mul(A,A),A))
L3=mul(mul(L,L),L)
predicted=add(L3,scale(mul({0:x},L),3),scale(D,6))
assert actual==predicted
P1=add(mul(L,L),{0:2*x})
M1=add(L3,scale(mul({0:x},L),3),scale(D,3))
S=add(A,scale(mul(D,mul(B,B)),-1))
assert positive(mul(mul(S,S),S))==M1
residual=add(mul(S,S),scale(P1,-1))
assert max(residual)<=-4
print('SYMPY_VERSION',s.__version__)
print('FORMAL_INVERSE_LEFT_AND_RIGHT_THROUGH_ORDER',LOW+2,'PASS')
print('(L+xL^-1)^3 differential part = L^3+3xL+6D: PASS')
print('CORRECTED_DIXMIER_M = L^3+3xL+3D')
print('LITERAL_TRUNCATED_CUBE_MINUS_CORRECT_M',add(actual,scale(M1,-1)))
print('S=L+xL^-1-DL^-2 gives (S^3)_+=M_correct: PASS')
print('ORDER_OF_S_SQUARED_MINUS_L4',max(residual))
print('ALL FORMAL TRUNCATION CHECKS PASSED')
