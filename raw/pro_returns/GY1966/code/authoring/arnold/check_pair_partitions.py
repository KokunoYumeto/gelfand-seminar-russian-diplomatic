"""Independent exact checks of the Minlos pair-sum calculation.

This validates the index combinatorics by finite enumeration, then checks the
canonical factorial-density identity by polynomial arithmetic and rational tests.
It does not numerically approximate a continuum Gibbs process or prove clustering.
Run from the project root: python parts/arnold/check_pair_partitions.py
"""
from fractions import Fraction as Q
from itertools import permutations, product
from math import prod
from pathlib import Path
import json


def falling(n,k):
    return prod(n-j for j in range(k))


def even_signed_kernel(delta):
    delta=abs(delta)
    return Q(-1 if delta % 2 else 1,1+delta*delta)


def direct_square(points):
    pairs=list(permutations(points,2))
    F=sum((even_signed_kernel(i-j) for i,j in pairs),Q(0))
    by_distinct={2:Q(0),3:Q(0),4:Q(0)}
    counts={2:0,3:0,4:0}
    for i,j in pairs:
        for k,l in pairs:
            distinct=len({i,j,k,l})
            counts[distinct]+=1
            by_distinct[distinct]+=even_signed_kernel(i-j)*even_signed_kernel(k-l)
    assert sum(by_distinct.values())==F*F
    return F,by_distinct,counts


def factorial_terms(points):
    t2=sum((even_signed_kernel(i-j)**2 for i,j in permutations(points,2)),Q(0))
    t3=sum((even_signed_kernel(i-j)*even_signed_kernel(j-k)
            for i,j,k in permutations(points,3)),Q(0))
    t4=sum((even_signed_kernel(i-j)*even_signed_kernel(k-l)
            for i,j,k,l in permutations(points,4)),Q(0))
    return [t2,t3,t4]


count_rows=[]
locations=[0,1,3,4,8,10,11,17]
for n in range(9):
    points=locations[:n]
    F,actual,counts=direct_square(points)
    t2,t3,t4=factorial_terms(points)
    assert actual[2]==2*t2
    assert actual[3]==4*t3
    assert actual[4]==t4
    assert counts=={2:2*falling(n,2),3:4*falling(n,3),4:falling(n,4)}
    assert 2*t2+4*t3+t4==F*F
    count_rows.append(dict(N=n,two_distinct=counts[2],three_distinct=counts[3],four_distinct=counts[4]))

# A non-uniform random simple process on seven sites. Compute its moments in
# two genuinely separate ways: directly over its 128 configurations, and from
# factorial moment measures computed by marginalization.
sites=locations[:7]
probabilities=[Q(j+1,j+3) for j in range(len(sites))]
configurations=[]
for mask in product([False,True],repeat=len(sites)):
    points=tuple(x for x,chosen in zip(sites,mask) if chosen)
    probability=prod(p if chosen else 1-p for p,chosen in zip(probabilities,mask))
    configurations.append((points,probability))
assert sum(p for _,p in configurations)==1
raw_mean=Q(0); raw_second=Q(0)
for points,p in configurations:
    F=sum((even_signed_kernel(i-j) for i,j in permutations(points,2)),Q(0))
    raw_mean+=p*F
    raw_second+=p*F*F


def factorial_density(indices):
    needed=set(indices)
    assert len(needed)==len(indices)
    return sum((p for points,p in configurations if needed.issubset(points)),Q(0))


density_mean=sum((even_signed_kernel(i-j)*factorial_density((i,j))
                  for i,j in permutations(sites,2)),Q(0))
density_t2=sum((even_signed_kernel(i-j)**2*factorial_density((i,j))
               for i,j in permutations(sites,2)),Q(0))
density_t3=sum((even_signed_kernel(i-j)*even_signed_kernel(j-k)*factorial_density((i,j,k))
               for i,j,k in permutations(sites,3)),Q(0))
density_t4=sum((even_signed_kernel(i-j)*even_signed_kernel(k-l)*factorial_density((i,j,k,l))
               for i,j,k,l in permutations(sites,4)),Q(0))
assert density_mean==raw_mean
assert 2*density_t2+4*density_t3+density_t4==raw_second
raw_variance=sum((p*(sum((even_signed_kernel(i-j) for i,j in permutations(points,2)),Q(0))-raw_mean)**2
                  for points,p in configurations),Q(0))
assert raw_variance==2*density_t2+4*density_t3+density_t4-density_mean**2


def poly_multiply(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]+=x*y
    return out


def falling_polynomial(k):
    p=[1]
    for j in range(k):
        p=poly_multiply(p,[-j,1])
    return p


p4=falling_polynomial(4)
p2square=poly_multiply(falling_polynomial(2),falling_polynomial(2))
difference=[a-b for a,b in zip(p4,p2square)]
assert difference==[0,-6,10,-4,0]
absolute_polynomial=poly_multiply(poly_multiply([0,1],[-1,1]),[-6,4])
assert absolute_polynomial==[0,6,-10,4]
canonical_tests=0
for n in range(41):
    for V in [Q(1),Q(3,2),Q(7),Q(19,3),Q(101)]:
        r2=Q(falling(n,2),1)/V**2
        r4=Q(falling(n,4),1)/V**4
        discrepancy=abs(r4-r2*r2)
        expected=Q(n*(n-1)*(4*n-6),1)/V**4
        assert discrepancy==expected
        rho=Q(n,1)/V
        assert discrepancy<=4*rho**3/V
        canonical_tests+=1

result=dict(
    status='all exact independent checks passed',
    pair_partition_coefficients=[2,4,1],
    deterministic_configuration_checks=len(count_rows),
    index_counts=count_rows,
    random_process_configurations=len(configurations),
    random_process_mean=str(raw_mean),
    random_process_second_moment=str(raw_second),
    random_process_variance=str(raw_variance),
    canonical_polynomial_difference='(N)_4 - (N)_2^2 = -4*N^3 + 10*N^2 - 6*N',
    canonical_absolute_identity='|r4-r2^2| = N*(N-1)*(4*N-6)/V^4 <= 4*(N/V)^3/V',
    canonical_rational_parameter_tests=canonical_tests,
    scope='The finite-site experiment checks the factorial-moment combinatorics, including signed even kernels. The continuum tree-integral estimate and L1 truncation argument were independently proved in independent_review.md; no Gibbs-clustering assumption is inferred from these tests.'
)
output=json.dumps(result,indent=2)+'\n'
Path('parts/arnold/check_pair_partitions_output.json').write_text(output)
print(output,end='')
