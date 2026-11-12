"""Exact Haar moments via Gram pseudoinverses, plus independent checks.

The pseudoinverse is essential when degree m exceeds matrix rank N.
The N=2 endpoint formula and the N=3 ordinary HCIZ determinant supply
independent analytic comparisons.  Floating point is used only for a
high-precision illustration of the analytically proved Taylor bound.
"""
from functools import lru_cache
from itertools import permutations,product
from math import factorial
import sympy as s
import mpmath as mp

def inv(p):
    result=[0]*len(p)
    for i,v in enumerate(p):
        result[v]=i
    return tuple(result)

def compose(p,q):
    return tuple(p[q[i]] for i in range(len(p)))

def cycles(p):
    seen=set(); answer=0
    for i in range(len(p)):
        if i not in seen:
            answer+=1; j=i
            while j not in seen:
                seen.add(j); j=p[j]
    return answer

@lru_cache(None)
def haar_gram(N,m):
    perms=list(permutations(range(m)))
    G=s.Matrix([[N**cycles(compose(inv(p),q)) for q in perms] for p in perms])
    W=G.pinv()
    assert G*W*G == G and W*G*W == W
    return perms,G,W

def moment(A,m):
    N=A.rows
    if m == 0:
        return s.Integer(1)
    perms,G,W=haar_gram(N,m)
    tuples=list(product(range(N),repeat=m))
    fixed={t:[k for k,p in enumerate(perms) if all(t[i] == t[p[i]] for i in range(m))] for t in tuples}
    # Cache moments for equality patterns of the row and column tuples.
    monomial={}
    answer=0
    for ii in tuples:
        for jj in tuples:
            coefficient=s.prod(A[ii[k],jj[k]] for k in range(m))
            if coefficient == 0:
                continue
            key=(tuple(fixed[ii]),tuple(fixed[jj]))
            if key not in monomial:
                monomial[key]=sum(W[p,q] for p in key[0] for q in key[1])
            answer+=coefficient*monomial[key]
    return s.expand(answer)

def n2_moment(A,m):
    alpha=A[0,0]+A[1,1]
    beta=A[0,1]+A[1,0]
    # Polynomial version is valid at coalescing endpoints as well.
    return s.expand(sum(alpha**j*beta**(m-j) for j in range(m+1))/s.Integer(m+1))

def rank_one_hciz_moment(p,q,m):
    N=len(p); degree=N*(N-1)//2
    vand=s.prod(p[j]-p[i] for i in range(N) for j in range(i+1,N))*s.prod(q[j]-q[i] for i in range(N) for j in range(i+1,N))
    determinant_coefficient=0
    for perm in permutations(range(N)):
        inversions=sum(perm[i]>perm[j] for i in range(N) for j in range(i+1,N))
        linear=sum(p[i]*q[perm[i]] for i in range(N))
        determinant_coefficient+=(-1)**inversions*s.Rational(linear**(m+degree),factorial(m+degree))
    return s.factor(factorial(m)*s.prod(factorial(k) for k in range(1,N))*determinant_coefficient/vand)

def main():
    print('SymPy',s.__version__,'mpmath',mp.__version__)
    cases=[s.Matrix([[1,2],[3,5]]),s.Matrix([[1,s.I],[2,-1]]),s.Matrix([[1,2],[3,4]])]
    for index,A in enumerate(cases,1):
        limit=4 if index == 1 else 3
        values=[]
        for m in range(limit+1):
            exact=moment(A,m)
            assert s.simplify(exact-n2_moment(A,m)) == 0
            values.append(str(exact))
        print('N=2 case',index,'A=',A,'moments m=0..'+str(limit),values,'PASS')
    for m in range(1,5):
        assert moment(s.Matrix([[3]]),m) == 3**m
    print('N=1 m=1..4 singular-Gram tests: PASS')
    for N,m in [(1,3),(2,3),(2,4),(3,3)]:
        _,G,_=haar_gram(N,m)
        print('Gram N,m,shape,rank:',N,m,G.shape,G.rank())
    p=[-1,0,2]; q=[-2,1,3]
    A=s.Matrix([[x*y for y in q] for x in p])
    for m in range(4):
        exact=moment(A,m); hciz=rank_one_hciz_moment(p,q,m)
        assert exact == hciz
        print('N=3 ordinary HCIZ comparison m=',m,'moment=',exact,'PASS')
    A=s.Matrix([[1,2,0],[-1,3,4],[2,-2,5]])
    N=3; S=sum(A); F=sum(x*x for x in A)
    R=sum(sum(A[i,j] for j in range(N))**2 for i in range(N))
    C=sum(sum(A[i,j] for i in range(N))**2 for j in range(N))
    expected2=s.Rational(S*S+F,N*N-1)-s.Rational(R+C,N*(N*N-1))
    assert moment(A,1) == s.Rational(S,N)
    assert moment(A,2) == expected2
    print('N=3 arbitrary-coefficient first/second-moment comparison:',s.Rational(S,N),expected2,'PASS')
    mp.mp.dps=80
    A=s.Matrix([[1,2],[3,5]])
    alpha=mp.mpf(6); beta=mp.mpf(5); centre=(alpha+beta)/2; radius=abs(alpha-beta)/2
    exact=mp.exp(centre)*mp.sinh(radius)/radius
    for K in [8,12,20]:
        # The centered integral is uniform on [-1/2,1/2].
        approximate=mp.exp(centre)*sum(radius**m/(mp.factorial(m)*(m+1)) for m in range(0,K+1,2))
        bound=mp.exp(centre+radius)*radius**(K+1)/mp.factorial(K+1)
        error=abs(exact-approximate)
        assert error <= bound
        print('N=2 centered Taylor K=',K,'absolute error',mp.nstr(error,25),'analytic bound',mp.nstr(bound,25))
    print('All exact comparisons passed, including m>N. Decimal bounds are illustrative evaluations of exact analytic inequalities.')

if __name__ == '__main__':
    main()
