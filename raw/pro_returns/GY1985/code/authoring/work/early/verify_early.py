"""Independent exact checks of annotations in records 642, 643, 647, 648.
These checks do not certify the cited literature or claim new theorems.
"""
import itertools,json
from collections import defaultdict,Counter
import sympy as s
out={}
x,y=s.symbols('x y')
examples=[(x**3+y**4,[1,y,y**2,x,x*y,x*y**2]),(x**2*y+y**4,[1,x,y,y**2,y**3])]
algs=[]
for f,basis in examples:
 G=s.groebner([s.diff(f,x),s.diff(f,y)],x,y,order='lex')
 lead=[tuple(p.LM(order=G.order).exponents) for p in G.polys]
 standard=[x**i*y**j for i in range(8) for j in range(8) if not any(i>=a and j>=b for a,b in lead)]
 assert set(standard)==set(map(s.sympify,basis))
 # A second check: reductions of multiplication close on precisely the proposed basis.
 mons=[s.Poly(v,x,y).monoms()[0] for v in basis]
 for variable in [x,y]:
  for b in basis:
   rem=s.Poly(G.reduce(variable*b)[1],x,y)
   assert all(c==0 or m in mons for m,c in rem.terms())
 algs.append({'f':str(f),'groebner':[str(p.as_expr()) for p in G.polys],'dimension':len(standard),'standard_monomials':[str(a) for a in standard]})
out['jacobian_algebras']=algs
qchecks=[]
for bound in [8,16,24,32]:
 # Independently multiply the two strict-odd-part products.
 right={(0,0):1}
 for odd in range(1,bound+1,2):
  for charge in [1,-1]:
   nxt=defaultdict(int,right)
   for (r,k),v in right.items():
    if k+odd<=bound:nxt[(r+charge,k+odd)]+=v
   right=dict(nxt)
 # Ordinary partitions by unbounded-coin recursion, followed by the theta shift.
 p=[0]*(bound//2+1);p[0]=1
 for j in range(1,len(p)):
  for k in range(j,len(p)):p[k]+=p[k-j]
 left={}
 for r in range(-bound,bound+1):
  for n,c in enumerate(p):
   if r*r+2*n<=bound:left[(r,r*r+2*n)]=c
 assert right==left
 qchecks.append({'max_q_degree':bound,'nonzero_coefficients':len(right),'agreement':True})
out['triple_product_coefficients']=qchecks
nwords=0
for bits in itertools.product([0,1],repeat=8):
 n=sum(bits[i]==1 and bits[j]==0 for i in range(8) for j in range(i+1,8))
 charges=[]
 for g in range(9):
  aa=[g-1-i for i in range(g) if bits[i]==1]
  bb=[j-g for j in range(g,8) if bits[j]==0]
  ss,tt=len(aa),len(bb)
  charges.append(ss-tt)
  assert sum(2*a+1 for a in aa)+sum(2*b+1 for b in bb)==2*n+(ss-tt)**2
 assert all(charges[i+1]-charges[i]==1 for i in range(8))
 nwords+=1
out['binary_word_check']={'words':nwords,'gaps_per_word':9,'area_and_charge_identities':True}
vertices=set()
for free in range(4):
 for fixed in itertools.product([-1,1],repeat=3):
  v=[];it=iter(fixed)
  for i in range(4):v.append(-sum(fixed) if i==free else next(it))
  if abs(v[free])<=1:vertices.add(tuple(v))
expected={v for v in itertools.product([-1,1],repeat=4) if sum(v)==0}
assert vertices==expected and len(vertices)==6
v=sorted(vertices)
dist=lambda a,b:sum((a[i]-b[i])**2 for i in range(4))
dists=Counter(dist(a,b) for a,b in itertools.combinations(v,2))
triangles=[w for w in itertools.combinations(v,3) if all(dist(a,b)==8 for a,b in itertools.combinations(w,2))]
u=[s.Matrix(z) for z in [(1,1,-1,-1),(1,-1,1,-1),(1,-1,-1,1)]]
assert s.Matrix.hstack(*u).T*s.Matrix.hstack(*u)==4*s.eye(3)
assert dists==Counter({8:12,16:3}) and len(triangles)==8
out['four_cube_section']={'vertices':v,'squared_distances':dict(dists),'triangular_faces':len(triangles),'orthogonal_basis_gram':'4 I_3'}
checks=[]
for N in [1,2,3,8,16]:
 partial=1+sum(2**(2*j+1) for j in range(N))
 err=3*partial-1
 assert err==2*4**N
 checks.append({'terms_after_initial_one':N,'valuation_of_three_times_sum_minus_one':2*N+1})
out['two_adic_one_third']=checks
print(json.dumps(out,indent=2))
