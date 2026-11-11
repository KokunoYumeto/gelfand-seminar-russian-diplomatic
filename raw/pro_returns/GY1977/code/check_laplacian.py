"""Independent exact CE-complex check of the notebook P000784–785.

No floating point eigenvalue test is used.  The first algorithm forms integer
boundary matrices and factors characteristic polynomials.  A second algorithm
enumerates the stated gap partitions, without using any boundary coefficients.
The equality is a finite check, not a proof of the general spectral theorem.
"""
from pathlib import Path
from collections import Counter
from functools import lru_cache
import json, math
import sympy as s

OUT=Path(__file__).resolve().parent/'output'
OUT.mkdir(exist_ok=True)

@lru_cache(None)
def parts(n,lo=1,gap=1):
    if n==0: return ((),)
    result=[]
    for a in range(lo,n+1):
        for rest in parts(n-a,a+gap,gap): result.append((a,)+rest)
    return tuple(result)

def boundary(col,rows):
    index={x:i for i,x in enumerate(rows)}
    answer=s.zeros(len(rows),len(col))
    for k,I in enumerate(col):
        for i in range(len(I)):
            for j in range(i+1,len(I)):
                merged=I[i]+I[j]
                rem=I[:i]+I[i+1:j]+I[j+1:]
                if merged in rem:continue
                sign=(-1)**(i+j-1+sum(x<merged for x in rem))
                answer[index[tuple(sorted((merged,)+rem))],k]+=sign*(I[j]-I[i])
    return answer

def expected(n):
    spec=Counter();labels={}
    for I in parts(n,1,3):
        E=sum(math.comb(a,3) for a in I)-sum(I[i]*I[j] for i in range(len(I)) for j in range(i+1,len(I)))
        alpha=(int(I[0]>=3) if I else 0)+sum(I[i]-I[i-1]>3 for i in range(1,len(I)))
        spec[E]+=2**alpha
        labels.setdefault(E,[]).append(I)
    return spec,labels

rows=[];first_collision=None
checked_weights=list(range(1,23))+[25]
for n in checked_weights:
    P=parts(n);top=max(map(len,P));bases={q:[I for I in P if len(I)==q] for q in range(top+2)}
    ds={q:boundary(bases[q],bases.get(q-1,[])) for q in range(1,top+2)}
    actual=Counter();blocks=[]
    for q in range(1,top+1):
        if q>1: assert ds[q-1]*ds[q]==s.zeros(len(bases[q-2]),len(bases[q]))
        D=ds[q].T*ds[q]+ds[q+1]*ds[q+1].T
        factors=s.factor_list(D.charpoly().as_expr())[1]
        block=Counter()
        for poly,multiplicity in factors:
            assert s.degree(poly)==1,(n,q,poly)
            root=s.solve(poly)[0]
            assert root.is_Integer and root>=0,(n,q,root)
            block[int(root)]+=multiplicity
        actual+=block
        blocks.append({'degree':q,'dimension':len(bases[q]),'spectrum':dict(sorted(block.items()))})
    target,labels=expected(n)
    assert actual==target,(n,actual,target)
    rows.append({'weight':n,'dimension':len(P),'spectrum':dict(sorted(actual.items())),
                 'gap_partition_count':sum(map(len,labels.values())),
                 'distinct_eigenvalue_count':len(actual),'blocks':blocks})

# A separate polynomial representation verifies the stated two harmonic vectors.
harmonic=[]
for q in range(1,5):
    z=s.symbols('z0:'+str(q))
    vand=s.prod(z[i]-z[j] for i in range(q) for j in range(i+1,q))**3
    for shift in (1,2):
        poly=s.Poly(s.expand(vand*s.prod(x**shift for x in z)),*z)
        weight=q*shift+3*q*(q-1)//2
        B=[I for I in parts(weight) if len(I)==q]
        v=s.Matrix([poly.coeff_monomial(s.prod(z[k]**I[k] for k in range(q))) for I in B])
        d=boundary(B,[I for I in parts(weight) if len(I)==q-1])
        up=boundary([I for I in parts(weight) if len(I)==q+1],B)
        assert d*v==s.zeros(d.rows,1)
        assert up.T*v==s.zeros(up.cols,1)
        harmonic.append({'degree':q,'shift':shift,'weight':weight,'nonzero_coefficients':sum(x!=0 for x in v),'harmonic':True})

for n in range(1,81):
    _,labels=expected(n)
    collisions={E:I for E,I in labels.items() if len(I)>1}
    if collisions:
        first_collision={'weight':n,'collisions':collisions}
        break
result={'weights_checked':checked_weights,'method':'exact integer boundaries and characteristic polynomials',
        'comparison_scope':'Each exterior-degree block is computed exactly; gap-partition comparison is for the aggregate spectrum at fixed weight.',
        'collision_search_weights':list(range(1,first_collision['weight']+1)) if first_collision else list(range(1,81)),
        'first_collision':first_collision,'spectra':rows,'harmonic_checks':harmonic}
(OUT/'laplacian_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print('d^2=0; aggregate exact weight spectra agree with corrected gap-partition formula for weights 1–22 and 25.')
print('First collision:',first_collision)
print('Both Vandermonde-cubed vectors are cycles and cocycles for degrees 1–4.')
