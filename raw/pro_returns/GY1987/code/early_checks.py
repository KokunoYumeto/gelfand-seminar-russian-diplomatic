"""Exact checks supporting emendations in the early 1987 records.
These are finite checks of formulas, not substitutes for general theorems.
"""
import itertools, json
from pathlib import Path
import sympy as s

report={}
M=s.Matrix(s.symbols('M1:4'));p=s.Matrix(s.symbols('p1:4'));a=s.symbols('a1:4');A=s.diag(*a)
z=list(M)+list(p)
P1=s.zeros(6);P2=s.zeros(6)
for i,j in itertools.product(range(3),repeat=2):
    P1[i,j]=sum(s.LeviCivita(i,j,k)*M[k] for k in range(3))
    P1[i,j+3]=P1[i+3,j]=sum(s.LeviCivita(i,j,k)*p[k] for k in range(3))
    P2[i,j]=sum(s.LeviCivita(i,j,k)*a[k]*M[k] for k in range(3))
    P2[i,j+3]=P2[i+3,j]=sum(s.LeviCivita(i,j,k)*a[k]*p[k] for k in range(3))
    P2[i+3,j+3]=sum(s.LeviCivita(i,j,k)*M[k] for k in range(3))
H=(M.dot(M)+p.dot(A*p))/2
F=p.dot(p)/2
v1=P1*s.Matrix([s.diff(H,x) for x in z]);v2=P2*s.Matrix([s.diff(F,x) for x in z])
assert all(s.expand(v1[i]+v2[i])==0 for i in range(6))
assert all(s.expand(v1[i]-(A*p).cross(p)[i])==0 for i in range(3))
assert all(s.expand(v1[i+3]-M.cross(p)[i])==0 for i in range(3))
Q=P2.copy()
for i,j in itertools.product(range(3),repeat=2):
    Q[i,j+3]=sum(s.LeviCivita(i,j,k)*a[j]*p[k] for k in range(3))
    Q[j+3,i]=-Q[i,j+3]
    Q[i+3,j+3]=-P2[i+3,j+3]
jac=lambda P,i,j,k:s.expand(sum(P[i,l]*s.diff(P[j,k],z[l])+P[j,l]*s.diff(P[k,i],z[l])+P[k,l]*s.diff(P[i,j],z[l]) for l in range(6)))
assert s.expand(jac(P2,0,3,4)-(a[2]-a[1])*M[1])==0
u=s.symbols('u')
for P in (P1,Q,P1+u*Q):
    for i,j,k in itertools.combinations(range(6),3):
        assert jac(P,i,j,k)==0
vQ=Q*s.Matrix([s.diff(F,x) for x in z])
assert all(s.expand(v1[i]-vQ[i])==0 for i in range(6))
report['neumann']={'literal_jacobi_counterexample':'Jacobi(M1,p1,p2)=(a3-a2) M2, so the printed second table is not Poisson','literal_vector_fields':'printed P2 d(p^2/2) = -P1 dH, checked symbolically','repair':'mixed entry epsilon_ijk a_j p_k and pp entry -epsilon_ijk M_k','repair_jacobi':'all 20 coordinate triples pass, also for the pencil P1+u Q','repair_vector_fields':'Q d(p^2/2)=P1 dH, checked independently against cross products','cross_product':'pdot=M cross p; on p^2=1 and M.p=0, M=p cross pdot'}

q=s.symbols('q');tau=q/(q+1)**2
def W(r):
    assert r!=0
    if r>0:return q*(q**(r-1)-1)/((q+1)*(q**r-1))
    d=-r;return (q**(d+1)-1)/((q+1)*(q**d-1))
for r in range(1,8):
    assert s.cancel(W(r)+W(-r)-1)==0
    assert s.cancel(W(-r-1)-(1-tau/W(-r)))==0
    assert s.limit(W(r),q,1)==s.Rational(r-1,2*r)
    assert s.limit(W(-r),q,1)==s.Rational(r+1,2*r)
for r in range(2,8):assert s.cancel(W(r)*W(1-r)-tau)==0
report['kerov']={'tested_r':'1 through 7 (product 2 through 7)','recurrence_sum_product_limits':'all exact rational identities pass','general_product_derivation':'Cancellation of (q^(r-1)-1)/(q^r-1) against W_(-(r-1)) leaves q/(q+1)^2','literal_counterexample':'q=2, r=2 gives W2 W(-1)=2/9 rather than 1'}

x=s.symbols('x1:5')
def dd(f,i,N=4):
    return s.cancel((f-f.xreplace({x[i]:x[i+1],x[i+1]:x[i]}))/(x[i]-x[i+1])).expand()
def h(n,N=3):
    if n<0:return s.Integer(0)
    if n==0:return s.Integer(1)
    return sum(s.prod(x[i]**e[i] for i in range(N)) for e in itertools.product(range(n+1),repeat=N) if sum(e)==n)
worked=dd(dd(dd(x[0]**7*x[1]**3,1),0),1)
assert s.expand(worked-(h(5)*h(2)-h(6)*h(1)))==0
report['worked_schubert']={'identity':'partial2 partial1 partial2(x1^7 x2^3)=h5 h2-h6 h1 in x1,x2,x3','verification':'operator expansion and independent Jacobi-Trudi determinant agree'}

def inversions(w):return sum(w[i]>w[j] for i in range(len(w)) for j in range(i+1,len(w)))
def schuberts(N):
    top=tuple(range(N,0,-1));polys={top:s.prod(x[i]**(N-i-1) for i in range(N))};queue=[top]
    while queue:
        w=queue.pop()
        for i in range(N-1):
            if w[i]>w[i+1]:
                v=list(w);v[i],v[i+1]=v[i+1],v[i];v=tuple(v);f=dd(polys[w],i,N)
                if v in polys:assert s.expand(polys[v]-f)==0
                else:polys[v]=f;queue.append(v)
    return polys
def integral(f,N):
    coeff=s.Poly(s.expand(f),*x[:N]).as_dict()
    ans=0
    for w in itertools.permutations(range(N)):
        e=tuple(N-1-w[i] for i in range(N))
        ans+=(-1)**inversions(w)*coeff.get(e,0)
    return s.expand(ans)
paircounts={}
for N in (3,4):
    polys=schuberts(N)
    for u,v in itertools.product(polys,repeat=2):
        got=integral(polys[u]*polys[v],N)
        dual=tuple(N+1-a for a in u)
        assert got==int(v==dual),(N,u,v,got,dual)
        for i in range(N-1):
            assert integral(dd(polys[u],i,N)*polys[v],N)==integral(polys[u]*dd(polys[v],i,N),N)
    paircounts[N]=len(polys)**2
# Independent integration check via a reduced longest word for S3.
polys=schuberts(3)
for u,v in itertools.product(polys,repeat=2):
    f=polys[u]*polys[v]
    d=dd(dd(dd(f,0,3),1,3),0,3).subs({xx:0 for xx in x})
    assert d==integral(f,3)
report['poincare']={'pairings_tested':paircounts,'adjoint_identity':'each simple divided difference on every pair in S3 and S4','independent_integration':'S3 alternating-coefficient integration agrees with direct partial1 partial2 partial1 and augmentation','dual_index':'v=w0 u, with Lehmer code complement'}

def detcols(cols):return s.Matrix.hstack(*cols).det()
exchange_samples=[]
for d in (2,3):
    xx=[s.Matrix([2+(i+1)*(j+2)+(i==j) for i in range(d)]) for j in range(d)]
    yy=[s.Matrix([(i+1)**(j+1)+(2 if i==j else 0) for i in range(d)]) for j in range(d)]
    lhs=detcols(xx)*detcols(yy)
    rhs=sum(detcols([yy[i]]+xx[1:])*detcols(yy[:i]+[xx[0]]+yy[i+1:]) for i in range(d))
    assert lhs==rhs
    bad=sum((-1)**(d-i-1)*detcols([yy[0]]+xx[1:])*detcols(yy[:i]+[xx[i]]+yy[i+1:]) for i in range(d))
    exchange_samples.append({'d':d,'lhs':int(lhs),'correct_rhs':int(rhs),'literal_rhs':int(bad)})
assert any(v['lhs']!=v['literal_rhs'] for v in exchange_samples)
# Full symbolic dimension-two identity, independent of numeric checks.
sym=s.symbols('u0:8')
xx=[s.Matrix(sym[0:2]),s.Matrix(sym[2:4])]
yy=[s.Matrix(sym[4:6]),s.Matrix(sym[6:8])]
assert s.expand(detcols(xx)*detcols(yy)-sum(detcols([yy[i],xx[1]])*detcols(yy[:i]+[xx[0]]+yy[i+1:]) for i in range(2)))==0
report['determinant_exchange']={'samples':exchange_samples,'independent_check':'full symbolic d=2 identity; general proof is expansion in the y basis'}

def hcat(U,V):
    return {(k,r,i,t):sum(U.get((k,l,i,j),0)*V.get((l,r,j,t),0) for j,l in itertools.product(range(2),repeat=2)) for k,r,i,t in itertools.product(range(2),repeat=4)}
def vcat(U,V):
    return {(k,l,u,v):sum(U.get((k,l,i,j),0)*V.get((i,j,u,v),0) for i,j in itertools.product(range(2),repeat=2)) for k,l,u,v in itertools.product(range(2),repeat=4)}
AA={(0,0,0,0):1};CC=dict(AA);BB={(0,1,0,0):1};DD={(1,0,0,0):1}
hv=vcat(hcat(AA,CC),hcat(BB,DD))[(0,0,0,0)]
vh=hcat(vcat(AA,BB),vcat(CC,DD))[(0,0,0,0)]
assert (hv,vh)==(1,0)
report['interchange']={'horizontal_then_vertical':hv,'vertical_then_horizontal':vh,'independent_reason':'vertical A,B contraction is identically zero because their common edge indices cannot match'}

mat1=s.eye(2);mat2=s.Matrix([[1,1],[1,2]])
for mat in (mat1,mat2):assert mat.rank()==2 and mat.det()!=0
nz=[[(i,j) for i in range(2) for j in range(2) if mat[i,j]!=0] for mat in (mat1,mat2)]
assert [len(v) for v in nz]==[2,4]
report['bimatroid']={'row_and_column_matroids':'both free rank two','nonzero_singleton_minors':[len(v) for v in nz]}

aa=[1,4,9];vv=s.Matrix([1,2,3]);AA=s.diag(*aa);tt=s.symbols('t')
pert=(tt*s.eye(3)-AA-vv*vv.T).det()
recovered=[s.cancel(-pert.subs(tt,aa[i])/s.prod(aa[i]-aa[j] for j in range(3) if j!=i)) for i in range(3)]
assert recovered==[1,4,9]
assert (tt*s.eye(3)-AA-s.diag(-1,1,1)*vv*(s.diag(-1,1,1)*vv).T).det().expand()==pert.expand()
report['rank_one']={'recovered_squared_coordinates':[int(z) for z in recovered],'sign_nonuniqueness':'flipping only v1 changes the rank-one matrix but preserves the characteristic polynomial'}

# Low-degree normalization of the q-Frobenius expression, checked independently
# against the two one-dimensional H2 characters T1=q and T1=-1.
qq=s.symbols('qq');tt=s.symbols('tt');XX=x[:3]
gen=s.prod((1-z*tt)/(1-qq*z*tt) for z in XX)
Q2=s.cancel(s.series(gen,tt,0,3).removeO().expand().coeff(tt,2)/(qq-1))
s2=h(2,3);s11=sum(XX[i]*XX[j] for i in range(3) for j in range(i+1,3))
assert s.expand(Q2-(qq*s2-s11))==0
report['q_frobenius']={'N2_check':'Q2=q s_(2)-s_(1,1), agreeing with Hecke quadratic roots q,-1','normalization':'Q_r=q^r q_r(X;q^-1)/(q-1)'}

dest=Path(__file__).resolve().parents[1]/'logs'/'early_checks.json'
dest.parent.mkdir(exist_ok=True);dest.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':list(report),'output':str(dest)},indent=2))
