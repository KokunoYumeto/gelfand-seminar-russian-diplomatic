"""Independent permutation-order audit of the proposed Volodin triangle.

Uses integer matrices and finite-field reduction, independently of the
early-record agent's implementation. No external packages are required.
"""
from itertools import permutations, combinations
from pathlib import Path
import json

def eye(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]

def mul(a,b,p):
    n=len(a)
    return [[sum(a[i][k]*b[k][j] for k in range(n))%p for j in range(n)] for i in range(n)]

def transvection(n,i,j,sign,p):
    a=eye(n); a[i][j]=sign%p
    return a

def orders(mats,p):
    n=len(mats[0]); out=[]
    for order in permutations(range(n)):
        rank={v:i for i,v in enumerate(order)}
        if all(all((a[i][j]-int(i==j))%p==0 or rank[i]<rank[j]
                   for i in range(n) for j in range(n)) for a in mats):
            out.append([x+1 for x in order])
    return out

rows=[]
for p in [2,3,5,7]:
    for n in [3,4,5]:
        edges=[(0,1),(1,2),(2,0)]
        vv=[transvection(n,i,j,1,p) for i,j in edges]
        inv=[transvection(n,i,j,-1,p) for i,j in edges]
        q={(i,j):mul(inv[i],vv[j],p) for i,j in combinations(range(3),2)}
        pair_orders={str(k):orders([v],p) for k,v in q.items()}
        triple=orders([q[(0,1)],q[(0,2)]],p)
        assert all(pair_orders.values()) and not triple
        # Right-quotient model, independently: g_i g_j^{-1}.
        rq={(i,j):mul(vv[i],inv[j],p) for i,j in combinations(range(3),2)}
        assert all(orders([v],p) for v in rq.values())
        assert not orders([rq[(0,1)],rq[(0,2)]],p)
        rows.append(dict(p=p,dimension=n,pair_witnesses={k:v[0] for k,v in pair_orders.items()},
                         common_orders=len(triple),right_model_checked=True))

report={'purpose':'Independent finite check; general nonzero-ring proof is separate.',
        'cases':rows,'result':'Every pair is a simplex; the triple is not, in both quotient conventions.'}
out=Path(__file__).with_suffix('.json')
out.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
