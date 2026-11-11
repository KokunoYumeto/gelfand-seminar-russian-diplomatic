"""Exact finite checks for records 115--116, independent of chapter rendering.

These are editorial checks, not numerical evidence for a new general theorem.
Run: python parts/arnold/check_singularities.py
"""
from itertools import product
from functools import lru_cache
from math import comb
from pathlib import Path
from fractions import Fraction as Q
import json


def mu_enumeration(symbol):
    return sum(1 for j in product(*(range(i + 1) for i in symbol))
               if j[0] > 0 and all(a >= b for a, b in zip(j, j[1:])))


def mu_recursion(symbol):
    @lru_cache(None)
    def count(k, previous):
        if k == len(symbol):
            return 1
        return sum(count(k + 1, j) for j in range(min(symbol[k], previous) + 1))
    return count(0, symbol[0]) - 1


def codimension(symbol, source, target, mu):
    return ((target - source + symbol[0]) * mu(symbol)
            - sum((symbol[k] - symbol[k+1]) * mu(symbol[k+1:])
                  for k in range(len(symbol)-1)))


symbols = [tuple(a) for length in range(1, 6)
           for a in product(range(5), repeat=length)
           if a[0] > 0 and all(x >= y for x, y in zip(a, a[1:]))]
for symbol in symbols:
    assert mu_enumeration(symbol) == mu_recursion(symbol)
    for m, n in [(4, 4), (5, 7), (7, 5)]:
        assert codimension(symbol, m, n, mu_enumeration) == codimension(symbol, m, n, mu_recursion)
for m in range(1, 8):
    for n in range(1, 8):
        for i in range(max(0, m-n), m+1):
            if i:
                assert codimension((i,), m, n, mu_recursion) == i * (n-m+i)
table_symbols = [(1,), (1,1), (1,1,1), (2,), (2,1), (3,), (2,2), (2,1,1), (4,)]
table_expected = [1, 2, 3, 4, 7, 9, 10, 10, 16]
table = {str(i): codimension(i, 20, 20, mu_recursion) for i in table_symbols}
assert list(table.values()) == table_expected

def poly(terms):
    return {m:Q(c) for m,c in terms.items() if c}


def add(p,q,scale=Q(1)):
    r=p.copy()
    for m,c in q.items():
        r[m]=r.get(m,Q(0))+scale*c
        if not r[m]:
            del r[m]
    return r


def shift(p,monomial,coefficient=Q(1)):
    return {tuple(a+b for a,b in zip(m,monomial)):coefficient*c for m,c in p.items()}


def multiply(p,q):
    r={}
    for m,c in q.items():
        r=add(r,shift(p,m,c))
    return r


def leading(p):
    return max(p,key=lambda m:(sum(m),m))


def divides(m,n):
    return all(a<=b for a,b in zip(m,n))


def remainder(p,basis):
    p=p.copy(); result={}
    while p:
        m=leading(p)
        for g in basis:
            n=leading(g)
            if divides(n,m):
                p=add(p,shift(g,tuple(a-b for a,b in zip(m,n)),p[m]/g[n]),-1)
                break
        else:
            result[m]=p.pop(m)
    return result


def groebner(generators):
    basis=[]
    for p in generators:
        p=remainder(p,basis)
        if p:
            basis.append(shift(p,(0,0),1/p[leading(p)]))
    pairs=[(i,j) for i in range(len(basis)) for j in range(i)]
    while pairs:
        i,j=pairs.pop()
        f,g=basis[i],basis[j]
        fm,gm=leading(f),leading(g)
        lcm=tuple(max(a,b) for a,b in zip(fm,gm))
        sp=add(shift(f,tuple(a-b for a,b in zip(lcm,fm)),1/f[fm]),
               shift(g,tuple(a-b for a,b in zip(lcm,gm)),1/g[gm]),-1)
        h=remainder(sp,basis)
        if h:
            h=shift(h,(0,0),1/h[leading(h)])
            pairs.extend((len(basis),j) for j in range(len(basis)))
            basis.append(h)
    return basis


def rank(rows):
    if not rows:
        return 0
    a=[[Q(x) for x in r] for r in rows]
    r=0
    for c in range(len(a[0])):
        pivot=next((i for i in range(r,len(a)) if a[i][c]),None)
        if pivot is None:
            continue
        a[r],a[pivot]=a[pivot],a[r]
        v=a[r][c]; a[r]=[x/v for x in a[r]]
        for i in range(r+1,len(a)):
            v=a[i][c]
            if v:
                a[i]=[x-v*y for x,y in zip(a[i],a[r])]
        r+=1
        if r==len(a):
            break
    return r


def groebner_length(generators):
    """Standard-monomial count; pure-power leading terms bound the search."""
    basis = groebner(generators)
    leading_terms = [leading(p) for p in basis]
    xbound = min(a for a, b in leading_terms if b == 0)
    ybound = min(b for a, b in leading_terms if a == 0)
    standard = [(a,b) for a in range(xbound) for b in range(ybound)
                if not any(a >= c and b >= d for c,d in leading_terms)]
    return len(standard)


def linear_relation_length(generators, degree_bound):
    """Independent exact quotient computation degree by degree.

    All input generators here are homogeneous. Thus each homogeneous ideal
    component is exactly spanned by monomial multiples of its generators.
    Summing exact rational codimensions through a degree with zero quotient
    component gives the complete length, since the quotient is standard graded.
    """
    total = 0
    reached_zero = False
    for degree in range(degree_bound + 1):
        monomials = [(a, degree-a) for a in range(degree+1)]
        vectors = []
        for g in generators:
            gd = max(map(sum,g))
            if gd <= degree:
                for a in range(degree-gd+1):
                    p = shift(g,(a,degree-gd-a))
                    vectors.append([p.get((b,c),Q(0)) for b,c in monomials])
        matrix_rank = rank(vectors)
        h = degree + 1 - matrix_rank
        total += h
        if h == 0:
            reached_zero = True
            break
    assert reached_zero
    return total


length_checks = []
for a in range(3, 9):
    literal = [poly({(a,0):1}), poly({(1,a-1):1}), poly({(2,0):1,(0,2):1})]
    repaired = [poly({(a,0):1}), poly({(a-1,1):1}), poly({(2,0):1,(0,2):1})]
    l1, l2 = groebner_length(literal), groebner_length(repaired)
    assert l1 == linear_relation_length(literal, 2*a+2)
    assert l2 == linear_relation_length(repaired, 2*a+2)
    # A separate normal-form derivation: y^2=-x^2, with x^a=0.
    assert l1 == (2*a if a % 2 else 2*a-1)
    assert l2 == 2*a-1
    length_checks.append(dict(a=a, literal=l1, repaired=l2))

def determinant(matrix):
    if len(matrix)==1:
        return matrix[0][0]
    return sum((-1)**i*v*determinant([r[:i]+r[i+1:] for r in matrix[1:]])
               for i,v in enumerate(matrix[0]))


def matrix_product(a,b):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]


determinants = {}
for sign in [-1, 1]:
    # Coefficients of (x2,x1,2*x1+x3,sign*2*x2+x4).
    J = [[0,1,0,0],[1,0,0,0],[2,0,1,0],[0,sign*2,0,1]]
    determinants[str(sign)] = determinant(J)
    assert determinant(J) == -1
    # Independent explicit inverse x1=b, x2=a, x3=c-2b, x4=d-sign*2a.
    inverse = [[0,1,0,0],[1,0,0,0],[0,-2,1,0],[-sign*2,0,0,1]]
    assert matrix_product(J,inverse)==[[int(i==j) for j in range(4)] for i in range(4)]


def derivative(p,variable):
    r={}
    for m,c in p.items():
        if m[variable]:
            n=list(m); n[variable]-=1
            r[tuple(n)]=c*m[variable]
    return r


# Polynomial variables (x,y,epsilon), so epsilon remains symbolic.
F1=poly({(2,0,0):1,(0,2,0):-1,(1,0,1):1})
F2=poly({(1,1,0):2,(0,1,1):-1})
jac=add(multiply(derivative(F1,0),derivative(F2,1)),
        multiply(derivative(F1,1),derivative(F2,0)),-1)
assert jac == poly({(2,0,0):4,(0,2,0):4,(0,0,2):-1})
# Independent Wirtinger formula for z^2 + epsilon conjugate(z).
assert jac == add(poly({(2,0,0):4,(0,2,0):4}),poly({(0,0,2):1}),-1)

for variables in range(1, 5):
    for order in range(5):
        count = sum(sum(exponents) <= order for exponents in product(range(order+1),repeat=variables))
        assert count == comb(variables+order, order)

result = dict(
    status='all exact checks passed',
    independent_mu_comparisons=len(symbols),
    equidimensional_codimensions=table,
    elliptic_algebra_lengths=length_checks,
    transversality_determinants=determinants,
    complex_square_jacobian='4*x^2 + 4*y^2 - epsilon^2',
    independent_checks='Enumeration vs recursive count; Groebner standard monomials vs exact homogeneous relation ranks and a normal-form derivation; determinant vs explicit inverse; real Jacobian vs Wirtinger formula.',
    scope='Finite editorial checks only. The universal statements are cited or proved algebraically in the accompanying annotations.'
)
out = json.dumps(result, indent=2) + '\n'
Path(__file__).with_name('check_singularities_output.json').write_text(out)
print(out,end='')
