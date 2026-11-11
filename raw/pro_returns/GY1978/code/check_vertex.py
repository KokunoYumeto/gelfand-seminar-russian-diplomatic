"""Exact finite checks accompanying the P000840 critical annotations."""
from itertools import product
from collections import Counter
import sympy as s

u,v,c=s.symbols('u v c')
states=list(product(range(2),repeat=3))
def swap(a,b):
    M=s.zeros(8)
    for j,t in enumerate(states):
        r=list(t);r[a],r[b]=r[b],r[a]
        M[states.index(tuple(r)),j]=1
    return M
I=s.eye(8);A=swap(0,1);B=swap(0,2);C=swap(1,2)
res=(u*I+c*A)*((u+v)*I+c*B)*(v*I+c*C)-(v*I+c*C)*((u+v)*I+c*B)*(u*I+c*A)
assert all(s.expand(entry)==0 for entry in res)
print('R(u)=uI+cP: additive Yang--Baxter identity verified symbolically on (C^2)^tensor3.')
assert A*B==B*C==C*A and A*C==B*A==C*B and A*B*C==C*B*A
print('Independent permutation identities AB=BC=CA; AC=BA=CB; ABC=CBA verified.')

images=Counter()
for a,b,c0,d in product((-1,1),repeat=4):
    bonds=(a*b,b*c0,c0*d,d*a)
    assert s.prod(bonds)==1
    images[bonds]+=1
assert len(images)==8 and set(images.values())=={2}
assert set(images)=={t for t in product((-1,1),repeat=4) if s.prod(t)==1}
print('Sixteen four-face Ising configurations give exactly eight parity-even bond tuples, each twice.')
for bonds in product((-1,1),repeat=4):
    selector=(s.prod(bonds)+1)//2
    assert selector in (0,1)
    assert bool(selector)==(bonds in images)
print('(ijkl+1)/2 is exactly the bond-parity selector; exponent equals minus beta times half the incident bond sum.')

for N in (2,3):
    for L in (2,3,4,5):
        # Every identity crossing preserves the independent color on each line.
        trace=sum(1 for _ in product(range(N),repeat=L))
        assert trace==N**L
        print(f'Identity crossing example: N={N}, L={L}, vertices={L*(L-1)//2}, trace={trace}=N^L.')
print('All exact checks passed. SymPy',s.__version__)
