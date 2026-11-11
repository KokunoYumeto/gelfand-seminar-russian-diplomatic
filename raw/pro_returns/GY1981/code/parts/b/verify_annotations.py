"""Exact checks of annotations, not a claim to a new theorem.

Python 3 + SymPy. The A3 data reproduce Williamson, Local Hodge theory
of Soergel bimodules, section 8.4, independently from gl4 commutators.
Two methods check the t-adic elementary-divisor multiplicities: a DVR
Schur elimination and rational ranks of truncated multiplication maps.
"""
from functools import lru_cache
from collections import Counter
from itertools import product
import json
from pathlib import Path
import sympy as sp

T=sp.Symbol('t')
ROOTS=((1,0),(2,0),(3,0),(2,1),(3,1),(3,2))
ORDER={r:i for i,r in enumerate(ROOTS)}
TARGET=(2,3,2)

def bracket(x,y):
    i,j=x;k,l=y
    d={}
    if j==k:d[(i,l)]=d.get((i,l),0)+1
    if l==i:d[(k,j)]=d.get((k,j),0)-1
    return [(g,c) for g,c in d.items() if c]

def plus(d,word,c):
    if c:d[word]=sp.expand(d.get(word,0)+c)
    if word in d and d[word]==0:del d[word]

@lru_cache(None)
def normal(word):
    for i in range(len(word)-1):
        if ORDER[word[i]]>ORDER[word[i+1]]:
            a,b=word[i:i+2]
            d=dict(normal(word[:i]+(b,a)+word[i+2:]))
            for g,c in bracket(a,b):
                assert g[0]>g[1]
                for w,k in normal(word[:i]+(g,)+word[i+2:]).items():plus(d,w,c*k)
            return d
    return {word:sp.Integer(1)}

ROOT_WEIGHTS=[tuple(int(b<=j<a) for j in range(3)) for a,b in ROOTS]
def make_basis():
    words=[]
    def go(k,left,word):
        if k==len(ROOTS):
            if left==(0,0,0):words.append(word)
            return
        w=ROOT_WEIGHTS[k]
        cap=min(left[j] for j in range(3) if w[j])
        for e in range(cap+1):go(k+1,tuple(left[j]-e*w[j] for j in range(3)),word+(ROOTS[k],)*e)
    go(0,TARGET,())
    return words
BASIS=make_basis()
assert len(BASIS)==13

def shapovalov(gamma):
    dyn=[a+T*b for a,b in zip((-2,2,-2),gamma)]
    hw=(sum(dyn),dyn[1]+dyn[2],dyn[2],sp.Integer(0))
    @lru_cache(None)
    def act(g,word):
        i,j=g
        if i>j:return normal((g,)+word)
        if i==j:
            z=hw[i]+sum(int(i==a)-int(i==b) for a,b in word)
            return {word:z} if z!=0 else {}
        if not word:return {}
        f,tail=word[0],word[1:]
        out={}
        for w,c in act(g,tail).items():
            for q,d in normal((f,)+w).items():plus(out,q,c*d)
        for h,c in bracket(g,f):
            for w,d in act(h,tail).items():plus(out,w,c*d)
        return out
    def pairing(u,w):
        vec={w:sp.Integer(1)}
        for i,j in u:
            nxt={}
            for q,c in vec.items():
                for z,d in act((j,i),q).items():plus(nxt,z,c*d)
            vec=nxt
        assert not (set(vec)-{()})
        return sp.expand(vec.get((),0))
    a=sp.Matrix([[pairing(u,w) for w in BASIS] for u in BASIS])
    assert a==a.T
    return a

def valuation(f):
    if f==0:return 999
    n,d=sp.fraction(sp.cancel(f))
    def ordpoly(p):return min(e[0] for e,c in sp.Poly(p,T).terms() if c)
    return ordpoly(n)-ordpoly(d)

def dvr_eliminate(a):
    # Exact rational power-series arithmetic modulo t^5. All resulting orders
    # are below 5, and stabilization of independent truncated nullities confirms
    # that there is no hidden higher elementary divisor.
    from fractions import Fraction as F
    N=5
    def coeffs(f):
        p=sp.Poly(f,T)
        return [F(int(p.nth(k).p),int(p.nth(k).q)) for k in range(N)]
    def order(p):return next((k for k,c in enumerate(p) if c),999)
    def mul(p,q):return [sum((p[i]*q[k-i] for i in range(k+1)),F(0)) for k in range(N)]
    def divide(p,q):
        d=order(q)
        assert order(p)>=d
        u=q[d:]+[F(0)]*d
        inv=[1/u[0]]
        for k in range(1,N):inv.append(-sum((u[i]*inv[k-i] for i in range(1,k+1)),F(0))/u[0])
        pp=p[d:]+[F(0)]*d
        return mul(pp,inv)
    a=[[coeffs(a[i,j]) for j in range(a.cols)] for i in range(a.rows)]
    vals=[]
    while a:
        m=len(a)
        v,i,j=min((order(a[i][j]),i,j) for i in range(m) for j in range(m))
        assert v<N
        a[0],a[i]=a[i],a[0]
        for row in a:row[0],row[j]=row[j],row[0]
        pivot=a[0][0]
        vals.append(v)
        bb=[]
        for i in range(1,m):
            ratio=divide(a[i][0],pivot)
            row=[]
            for j in range(1,m):
                pr=mul(ratio,a[0][j])
                row.append([a[i][j][k]-pr[k] for k in range(N)])
            bb.append(row)
        a=bb
    return vals

def integer_rank(mat):
    # Fraction-free rational row elimination, with exact gcd normalization.
    from math import gcd
    from functools import reduce
    a=[[int(mat[i,j]) for j in range(mat.cols)] for i in range(mat.rows)]
    rank=0
    for col in range(mat.cols):
        candidates=[i for i in range(rank,len(a)) if a[i][col]]
        if not candidates:continue
        row=min(candidates,key=lambda i:abs(a[i][col]))
        a[rank],a[row]=a[row],a[rank]
        pv=a[rank][col]
        for i in range(rank+1,len(a)):
            co=a[i][col]
            if not co:continue
            common=gcd(pv,co)
            pp,qq=pv//common,co//common
            for j in range(col,mat.cols):a[i][j]=pp*a[i][j]-qq*a[rank][j]
            g=reduce(gcd,(abs(z) for z in a[i][col:]),0)
            if g>1:
                for j in range(col,mat.cols):a[i][j]//=g
        rank+=1
        if rank==len(a):break
    return rank

def truncation_nullities(a,maxk=4):
    blocks=[a.applyfunc(lambda f:sp.Poly(f,T).nth(k)) for k in range(maxk)]
    n=a.rows
    vals=[]
    for k in range(1,maxk+1):
        block=sp.zeros(n*k)
        for i in range(k):
            for j in range(i+1):block[i*n:(i+1)*n,j*n:(j+1)*n]=blocks[i-j]
        vals.append(k*n-integer_rank(block))
        print('  truncation',k,'nullity',vals[-1],flush=True)
    return vals

out={'method':'exact rational gl4 PBW commutators; DVR elimination checked by truncated block-matrix ranks','basis_size':len(BASIS),'cases':{}}
for name,gamma in [('dominant_rho',(1,1,1)),('regular_nondominant',(1,-2,3)),('reflected_regular_nondominant',(3,-2,1))]:
    print('Computing',name,flush=True)
    positive_coroot_values=[sum(gamma[i:j]) for i in range(3) for j in range(i+1,4)]
    assert 0 not in positive_coroot_values
    a=shapovalov(gamma)
    print("  form built",flush=True)
    vals=dvr_eliminate(a)
    print("  DVR orders",vals,flush=True)
    nulls=truncation_nullities(a)
    expected=[sum(min(k,v) for v in vals) for k in range(1,5)]
    assert nulls==expected
    layers=[vals.count(i) for i in range(4)]
    assert layers==([7,3,2,1] if name=='dominant_rho' else [7,2,4,0])
    out['cases'][name]={'dynkin_direction':gamma,'positive_coroot_values':positive_coroot_values,'elementary_divisor_orders':vals,'layer_dimensions':layers,'truncated_nullities_k_1_to_4':nulls}

# Cauchy signs: two disjoint integer families, and repeated-row edge case.
cauchy=[]
for n in range(1,6):
    xx=[2*i+1 for i in range(n)]; yy=[-3*i-2 for i in range(n)]
    a=sp.Matrix([[sp.Rational(1,x-y) for y in yy] for x in xx])
    rhs=sp.prod((xx[j]-xx[i])*(yy[i]-yy[j]) for i in range(n) for j in range(i+1,n))/sp.prod(sp.Integer(x-y) for x in xx for y in yy)
    assert a.det()==rhs
    cauchy.append({'n':n,'determinant':str(rhs)})
assert sp.Matrix([[sp.Rational(1,x-y) for y in (3,4)] for x in (1,1)]).det()==0
out['cauchy']=cauchy

# Symbolic Rayleigh derivative and inverse transformation.
time=sp.Symbol('s');x=sp.Function('x')(time);u=sp.Function('u')(time);eps=sp.Symbol('epsilon')
ray=eps*sp.diff(u,time,2)+sp.diff(u,time)**3/3-sp.diff(u,time)+u
vdp=eps*sp.diff(x,time,2)+(x*x-1)*sp.diff(x,time)+x
assert sp.expand(sp.diff(ray,time)-vdp.subs(x,sp.diff(u,time)))==0
inverse=-eps*sp.diff(x,time)-x**3/3+x
assert sp.expand(sp.diff(inverse,time)-x+vdp)==0
out['ode_checks']={'rayleigh_derivative':'identically zero residual','inverse_map':'identically zero modulo van der Pol','slow_period':str(2*sp.integrate((sp.Symbol('z')**2-1)/sp.Symbol('z'),(sp.Symbol('z'),1,2)))}

# Binary-cubic coadjoint pairing at f(v_0)=f(v_3)=1.
C=sp.diag(3,1,1,3)
B=sp.BlockMatrix([[sp.zeros(4),C],[-C.T,sp.zeros(4)]]).as_explicit()
assert B.det()==81 and B.rank()==8
out['binary_cubic_check']={'pairing_matrix':str(C),'Kirillov_determinant':int(B.det()),'rank':B.rank()}

# Finite signs: recursive simplest dyadic in each cut versus closed finite formula.
def simplest_between(lo,hi):
    if lo is None and hi is None:return sp.Rational(0)
    if hi is None:return sp.Integer(sp.floor(lo)+1) if lo>=0 else sp.Integer(0)
    if lo is None:return sp.Integer(sp.ceiling(hi)-1) if hi<=0 else sp.Integer(0)
    for k in range(40):
        q=2**k
        p=int(sp.floor(lo*q))+1
        if sp.Rational(p,q)<hi:return sp.Rational(p,q)
    raise AssertionError('No dyadic found')
def signs_cut(word):
    val=sp.Rational(0); lo=None;hi=None
    for s in word:
        if s==1:lo=val
        else:hi=val
        val=simplest_between(lo,hi)
    return val
def signs_formula(word):
    if not word:return sp.Rational(0)
    k=1
    while k<len(word) and word[k]==word[0]:k+=1
    return word[0]*k+sum(sp.Rational(s,2**(j+1)) for j,s in enumerate(word[k:]))
for n in range(9):
    for word in product((-1,1),repeat=n):assert signs_cut(word)==signs_formula(word)
assert signs_formula((1,-1,-1))==sp.Rational(1,4)
out['finite_surreal_check']={'all_sequences_through_length':8,'number_of_sequences':511,'plus_minus_minus':'1/4','methods':'canonical simplest-dyadic cuts versus explicit halving formula'}

path=Path(__file__).with_name('verification_output.json')
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
