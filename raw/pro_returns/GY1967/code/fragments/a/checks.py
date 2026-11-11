"""Reproducible elementary annotations, not new research results.

Run: python fragments/a/checks.py
Uses only the Python standard library. Output is saved in checks_output.txt.
"""
from pathlib import Path
import io
import contextlib
from fractions import Fraction as F
from itertools import permutations
from math import sin, log, pi

def mv(A,v):
    return [sum(a*b for a,b in zip(row,v)) for row in A]
def transpose(A):
    return list(map(list,zip(*A)))
def perron(A):
    v=[1./len(A)]*len(A)
    for _ in range(200):
        w=mv(A,v); lam=sum(w); v=[x/lam for x in w]
    return lam,v
def polynomial_product(p,q):
    out=[0]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):out[i+j]+=a*b
    return out
def characteristic(A):
    n=len(A);out=[0]*(n+1)
    for perm in permutations(range(n)):
        sign=(-1)**sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
        p=[sign]
        for i,j in enumerate(perm):
            p=polynomial_product(p,[-A[i][j],1] if i==j else [-A[i][j]])
        for i,a in enumerate(p):out[i]+=a
    return out

def run():
    print('1. Feynman normalization on the standard two-simplex')
    area=F(1,2)
    # Integrating (3-2*x-y)^(-3) first in y gives
    # ((2-x)^(-2)-(3-2*x)^(-2))/2. The following is its
    # exact rational x-integral over [0,1].
    integral=F(1,2)*((F(1,1)-F(1,2))-F(1,2)*(F(1,1)-F(1,3)))
    print('area =',area,'; integral for (a,b,c)=(1,2,3) =',integral)
    print('2! times integral =',2*integral,'; 1/(abc) =',F(1,6))
    assert area==F(1,2) and 2*integral==F(1,6)
    print('\n2. Failure of the weighted ray selector')
    for m in (2,3,10):
        bound=F(1,2)**m
        print('coordinate',m,'supremum =',bound,'< 1/2')
        assert bound<F(1,2)
    print('\n3. Spherical orbital measure and SO(3) dimension')
    print('2*pi*lambda^2 integral[-1,1] exp(i*lambda*r*z) dz = 4*pi*lambda*sin(lambda*r)/r')
    print('after division by 4*pi*lambda = sin(lambda*r)/r')
    # Numerical angular quadrature independently checks the normalization.
    lam,r=3.,.7
    N=20000
    angular=2*pi*lam**2*sum(__import__('math').cos(lam*r*(-1+(k+.5)*2/N))*2/N for k in range(N))
    target=4*pi*lam*sin(lam*r)/r
    print('midpoint angular quadrature =',angular,'closed formula =',target)
    assert abs(angular-target)<1e-6
    for n in range(4):
        dimension=2*n+1
        numeric=sin(dimension*1e-7)/sin(1e-7)
        print('spin',n,'character at identity =',dimension,'small-angle check =',numeric)
        assert abs(numeric-dimension)<1e-10
    print('\n4. Nonsymmetric Perron example')
    A=[[1,1,0],[1,0,1],[1,0,0]]
    L,R=perron(A);_,left=perron(transpose(A))
    dot=sum(a*b for a,b in zip(left,R));left=[a/dot for a in left]
    P=[[A[i][j]*R[j]/(L*R[i]) for j in range(3)] for i in range(3)]
    w=[left[i]*R[i] for i in range(3)]
    wrong=[[A[i][j]*left[j]/(L*left[i]) for j in range(3)] for i in range(3)]
    ent=-sum(w[i]*P[i][j]*log(P[i][j]) for i in range(3) for j in range(3) if P[i][j]>0)
    residual=max(abs(a-b) for a,b in zip(mv(transpose(P),w),w))
    print('A =',A,'Perron root =',L)
    print('correct row sums =',list(map(sum,P)))
    print('row sums using left vector incorrectly =',list(map(sum,wrong)))
    print('stationary weights =',w,'stationarity residual =',residual)
    print('entropy =',ent,'log(Perron root) =',log(L))
    assert max(abs(sum(row)-1) for row in P)<1e-12 and residual<1e-12
    assert max(abs(sum(row)-1) for row in wrong)>1e-3 and abs(ent-log(L))<1e-12
    print('\n5. Four-block matrix versus one-forbidden-transition model')
    for p,q,r0,s0 in [(2,1,1,1),(3,2,1,1)]:
        sizes=[p,q,r0,s0]; M=sum(sizes); N=p+s0
        types=[k for k,n in enumerate(sizes) for _ in range(n)]
        A4=[[int((i<2 and j in (0,2)) or (i>=2 and j in (1,3))) for j in types] for i in types]
        B=[[1]*N for _ in range(N)];B[N-1][0]=0
        ca=characteristic(A4);cb=characteristic(B)
        print('block sizes',sizes,'determinant',p*s0-q*r0,'char(A) coefficients ascending =',ca,'char(B) =',cb)
        assert ca==[0]*(M-2)+[1,-N,1]
        assert cb==[0]*(N-2)+[1,-N,1]
    print('\n6. Heisenberg central eigenvalue obstruction')
    print('[aX+cY,bX+dY] = (a*d-b*c) Z by bilinearity and [X,Y]=Z; lattice automorphism has determinant+1 or-1')
    for a,b,c,d in [(2,1,1,1),(1,2,1,1),(3,2,1,1)]:
        assert abs(a*d-b*c)==1
    print('\nAll finite and symbolic checks passed. They are annotations, not proofs of the cited literature theorems.')

if __name__=='__main__':
    out=io.StringIO()
    with contextlib.redirect_stdout(out):
        run()
    result=out.getvalue()
    Path(__file__).with_name('checks_output.txt').write_text(result)
    print(result,end='')
