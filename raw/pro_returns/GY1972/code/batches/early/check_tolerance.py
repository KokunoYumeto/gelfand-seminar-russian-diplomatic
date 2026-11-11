"""Exact audit of the P000470 / Vaserstein 1976 section 11(c) assertion.

No numerical approximation or external package is used.  The computation checks
all coordinate orders.  The proof in development.tex, not finite enumeration,
establishes the assertion for every nonzero unital ring and every stabilization.
"""
from itertools import permutations, combinations
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent

def identity(n):
    return [[int(i==j) for j in range(n)] for i in range(n)]

def transvection(n,i,j,a=1):
    M=identity(n); M[i][j]=a; return M

def multiply(A,B,p=None):
    n=len(A)
    C=[[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    return C if p is None else [[x%p for x in row] for row in C]

def support(U,p=None):
    n=len(U)
    return [(i,j) for i in range(n) for j in range(n)
            if ((U[i][j]-int(i==j)) if p is None else (U[i][j]-int(i==j))%p)]

def good_orders(matrices,p=None):
    n=len(matrices[0]); edges=set()
    for U in matrices: edges.update(support(U,p))
    result=[]
    for order in permutations(range(n)):
        position={i:k for k,i in enumerate(order)}
        if all(position[i]<position[j] for i,j in edges):
            result.append([i+1 for i in order])
    return result

def audit(n,p,side):
    V=[transvection(n,0,1),transvection(n,1,2),transvection(n,2,0)]
    W=[transvection(n,0,1,-1),transvection(n,1,2,-1),transvection(n,2,0,-1)]
    for a,b in zip(V,W): assert multiply(a,b,p)==identity(n)
    def relative(i,j):
        return multiply(W[i],V[j],p) if side=="left_cosets" else multiply(V[j],W[i],p)
    pair_orders={f"{i+1},{j+1}":good_orders([relative(i,j)],p)
                 for i,j in combinations(range(3),2)}
    triple_orders=good_orders([relative(0,1),relative(0,2)],p)
    assert all(pair_orders.values()), (n,p,side,"missing edge")
    assert not triple_orders, (n,p,side,"unexpected simplex")
    return dict(dimension=n,coefficient_ring="Z" if p is None else f"F_{p}",
                coset_model=side,pair_orders=pair_orders,
                common_triple_orders=triple_orders,
                every_pair_is_simplex=True,triple_is_simplex=False)

if __name__=="__main__":
    # The integer case explicitly checks the signs, while characteristic two
    # verifies that no argument has inadvertently relied on 1 != -1.
    results=[audit(n,p,side) for n in (3,4,5) for p in (None,2,3,5,7)
             for side in ("left_cosets","right_cosets")]
    matrices={"A":transvection(3,0,1),"B":transvection(3,1,2),"C":transvection(3,2,0)}
    W=[transvection(3,0,1,-1),transvection(3,1,2,-1),transvection(3,2,0,-1)]
    V=list(matrices.values())
    quotients={f"{i+1}^-1 {j+1}":multiply(W[i],V[j]) for i,j in combinations(range(3),2)}
    output=dict(description="Induced permutation-triangular complex, not its flag completion",
                matrices=matrices,left_quotients_over_Z=quotients,
                parameter_cases=len(results),cases=results,
                conclusion="Every pair is a simplex; the triple is not, in every audited case.",
                proof_scope="The accompanying algebraic proof covers every nonzero unital ring and every stabilization.")
    (HERE/"tolerance_output.json").write_text(json.dumps(output,indent=2)+"\n")
    print(json.dumps({k:output[k] for k in ("parameter_cases","conclusion","proof_scope")},indent=2))
