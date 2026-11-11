"""Finite independent checks of editorial reconstructions, GY1981 records530--537.
No numerical result here is offered as a proof beyond the tested range.
Requires Python3 and sympy; writes editorial_checks_output.txt beside this file.
"""
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, combinations_with_replacement, product
from math import comb, gcd
from pathlib import Path
import sympy as sp

out=[]
def report(s):
    out.append(s)
    print(s)

def mobius(n):
    return int(sp.mobius(n))

def divisors(n):
    return [int(x) for x in sp.divisors(n)]

def witt(k,l):
    n=k+l
    return sum(mobius(d)*comb(n//d,k//d) for d in divisors(gcd(k,l)))//n

# Independent necklace enumeration (does not use a Witt/Mobius recurrence).
necklace_cases=0
for n in range(1,11):
    for k in range(n+1):
        reps=set()
        for pos in combinations(range(n),k):
            w=tuple(0 if j in pos else 1 for j in range(n))
            rotations={w[j:]+w[:j] for j in range(n)}
            if len(rotations)==n:
                reps.add(min(rotations))
        assert len(reps)==witt(k,n-k),(n,k,len(reps),witt(k,n-k))
        necklace_cases+=1
report(f'Witt formula versus primitive-necklace enumeration: {necklace_cases} bidegrees, total degree1--10, PASS.')
cat=[1]
for n in range(1,13):
    cat.append(sum(cat[j]*cat[n-1-j] for j in range(n)))
assert all(cat[n]==witt(n,n+1) for n in range(13))
report('Catalan recursion versus Witt specialization, n=0--12: PASS. '+str(cat))

@lru_cache(None)
def gt_count(row):
    if len(row)==1:
        return 1
    return sum(gt_count(tuple(b)) for b in product(*(range(row[i],row[i+1]+1) for i in range(len(row)-1))))

def gt_product(row):
    ans=Fraction(1)
    for i in range(len(row)):
        for j in range(i+1,len(row)):
            ans*=Fraction(row[j]-row[i]+j-i,j-i)
    assert ans.denominator==1
    return ans.numerator
rows=list(combinations_with_replacement(range(-2,5),4))
assert all(gt_count(row)==gt_product(row) for row in rows)
report(f'Gelfand--Tsetlin direct recursive enumeration versus Weyl product: {len(rows)} weakly increasing integer top rows from [-2,4], PASS.')
for row in [(0,0,0,0),(0,0,0,1),(0,1,2,3),(-2,-1,1,4)]:
    report(f'  top row {row}: enumeration={gt_count(row)}, product={gt_product(row)}')

# Interval multiplicities versus ranks, independently reconstructed from explicit matrices.
intervals=[(i,j) for i in range(1,5) for j in range(i,5)]
rank_cases=0
for support in combinations(intervals,3):
    multiplicities={ij:1+(sum(ij)%2) for ij in support}
    slots={i:[(p,q,c) for (p,q),mult in multiplicities.items() for c in range(mult) if p<=i<=q] for i in range(1,5)}
    arrows={}
    for i in range(1,4):
        arrows[i]=sp.zeros(len(slots[i+1]),len(slots[i]))
        for col,label in enumerate(slots[i]):
            if label in slots[i+1]:
                arrows[i][slots[i+1].index(label),col]=1
    ranks={}
    for i in range(1,5):
        ranks[i,i]=len(slots[i])
        current=sp.eye(len(slots[i]))
        for j in range(i+1,5):
            current=arrows[j-1]*current
            ranks[i,j]=current.rank()
    for i,j in intervals:
        recovered=ranks.get((i,j),0)-ranks.get((i-1,j),0)-ranks.get((i,j+1),0)+ranks.get((i-1,j+1),0)
        assert recovered==multiplicities.get((i,j),0)
    rank_cases+=1
report(f'Interval finite-difference inversion versus ranks of explicit block representations: {rank_cases} three-interval supports, PASS.')

# Exact free-Lie calculations in the free associative algebra.
def clean(p):
    return {w:c for w,c in p.items() if c}

def bracket(p,q):
    d=defaultdict(int)
    for w,c in p.items():
        for v,b in q.items():
            d[w+v]+=c*b
            d[v+w]-=c*b
    return clean(d)

def is_lyndon(w):
    return len(w)==1 or all(w<w[i:]+w[:i] for i in range(1,len(w)))

@lru_cache(None)
def standard_bracket(w):
    if len(w)==1:
        return {w:1}
    # Longest proper Lyndon suffix, independently of quotient relations.
    cut=next(i for i in range(1,len(w)) if is_lyndon(w[i:]))
    return bracket(standard_bracket(w[:cut]),standard_bracket(w[cut:]))

@lru_cache(None)
def basis(alpha):
    k,l=alpha
    n=k+l
    return tuple(w for w in product(range(2),repeat=n) if w.count(0)==k and is_lyndon(w))

@lru_cache(None)
def words(alpha):
    k,l=alpha
    return tuple(w for w in product(range(2),repeat=k+l) if w.count(0)==k)

@lru_cache(None)
def basis_matrix(alpha):
    ws=words(alpha)
    bs=basis(alpha)
    return sp.Matrix(len(ws),len(bs),lambda i,j:standard_bracket(bs[j]).get(ws[i],0))

def coordinates(poly,alpha):
    if not poly:
        return sp.zeros(len(basis(alpha)),1)
    v=sp.Matrix([poly.get(w,0) for w in words(alpha)])
    B=basis_matrix(alpha)
    sol=B.gauss_jordan_solve(v)[0]
    assert B*sol==v
    return sol

def polynomial(coords,alpha):
    d=defaultdict(int)
    for c,w in zip(coords,basis(alpha)):
        for word,v in standard_bracket(w).items():
            d[word]+=c*v
    return clean(d)

def lower(poly,i,A):
    """[f_i, poly] in positive degree, by moving Cartan symbols right."""
    d=defaultdict(int)
    cartan=defaultdict(int)
    for w,c in poly.items():
        for p,j in enumerate(w):
            if i==j:
                removed=w[:p]+w[p+1:]
                d[removed]-=c*sum(A[i][q] for q in w[p+1:])
                cartan[removed]-=c
    assert not clean(cartan), 'Uncancelled Cartan term above height one'
    return clean(d)

def row_basis(M):
    return M.rowspace()

def matrix_of_columns(cols,nrows):
    return sp.Matrix.hstack(*cols) if cols else sp.zeros(nrows,0)

def rank_two_compare(a,b,height=8):
    A=((2,-a),(-b,2))
    Q={}
    ideals={}
    dims={}
    ex={(0,):1}; ey={(1,):1}
    relx=ey
    for _ in range(a+1): relx=bracket(ex,relx)
    rely=ex
    for _ in range(b+1): rely=bracket(ey,rely)
    for n in range(1,height+1):
        for k in range(n+1):
            alpha=(k,n-k)
            d=len(basis(alpha))
            if n==1:
                Q[alpha]=sp.eye(d)
            else:
                maps=[]
                for i in range(2):
                    beta=tuple(alpha[j]-(i==j) for j in range(2))
                    if min(beta)<0: continue
                    lowercols=[coordinates(lower(standard_bracket(w),i,A),beta) for w in basis(alpha)]
                    D=matrix_of_columns(lowercols,len(basis(beta)))
                    maps.append(Q[beta]*D)
                stacked=sp.Matrix.vstack(*maps) if maps else sp.zeros(0,d)
                rows=row_basis(stacked)
                Q[alpha]=sp.Matrix.vstack(*rows) if rows else sp.zeros(0,d)
            # Independent Serre ideal generation by brackets with simple generators.
            cols=[]
            if alpha==(a+1,1): cols.append(coordinates(relx,alpha))
            if alpha==(1,b+1): cols.append(coordinates(rely,alpha))
            for i,e in enumerate((ex,ey)):
                beta=tuple(alpha[j]-(i==j) for j in range(2))
                if min(beta)<0 or sum(beta)==0: continue
                for vec in ideals[beta].columnspace():
                    cols.append(coordinates(bracket(e,polynomial(vec,beta)),alpha))
            I=matrix_of_columns(cols,d)
            independent=I.columnspace()
            ideals[alpha]=matrix_of_columns(independent,d)
            serre_dim=d-ideals[alpha].cols
            lower_dim=Q[alpha].rows
            assert serre_dim==lower_dim,(a,b,alpha,serre_dim,lower_dim)
            dims[alpha]=lower_dim
    return dims

for a,b in [(1,1),(2,1),(3,1),(2,2),(3,2)]:
    dims=rank_two_compare(a,b)
    totals=[sum(d for alpha,d in dims.items() if sum(alpha)==n) for n in range(1,9)]
    report(f'Rank-two ({a},{b}), recursive contragredient lowering versus independently generated Serre ideal through height8: PASS; dimensions by height={totals}.')
    if a*b<4:
        assert sum(totals)=={1:3,2:4,3:6}[a*b]

# Formal Euler transform, with independently expanded product and logarithm.
N=14
v={1:2,2:1,3:3,5:2}
P=[0]*(N+1);P[0]=1
for k,vk in v.items():
    factor=[0]*(N+1)
    for m in range(N//k+1):factor[k*m]=comb(vk+m-1,m)
    P=[sum(P[j]*factor[n-j] for j in range(n+1)) for n in range(N+1)]

def mul(p,q):
    return [sum(p[j]*q[n-j] for j in range(n+1)) for n in range(N+1)]
X=[Fraction(x) for x in P];X[0]-=1
power=[Fraction(int(n==0)) for n in range(N+1)]
log=[Fraction(0)]*(N+1)
for m in range(1,N+1):
    power=mul(power,X)
    for n in range(N+1):log[n]+=Fraction((-1)**(m+1),m)*power[n]
assert all(n*log[n]==sum(d*v.get(d,0) for d in divisors(n)) for n in range(1,N+1))
report('Euler-product multiplication versus formal log power series through t^14: PASS; notebook normalization c_k=k dim V_k retained.')

# Two unrelated algebraic consistency checks, not symbolic fitting of data.
p,q=sp.symbols('p q')
assert sp.solve([p+q-1,p+4*q],[p,q])=={p:sp.Rational(4,3),q:sp.Rational(-1,3)}
assert 4*sp.Rational(4,3)+4*sp.Rational(-1,3)-4==0
assert 4*sp.Rational(-1,2)-4==-6
report('Schwarz density: covariance equations give (4/3,-1/3); uniform f rescaling exponent0. Preliminary -1/2 expression has exponent-6, so is not invariant: PASS.')
report('All checks completed. Finite calculations validate only the stated ranges; general claims are justified separately by the cited results and complete proofs in development.tex.')
Path(__file__).with_name('editorial_checks_output.txt').write_text('\n'.join(out)+'\n')
