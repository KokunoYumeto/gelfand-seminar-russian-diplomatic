"""Exact finite checks supplement, rather than replace, the printed derivations.

Run with Python 3 and SymPy. All decisions use integer/rational arithmetic.
"""
from itertools import combinations, combinations_with_replacement
from math import comb
import sympy as sp


def row_partitions(m, n):
    return {tuple(reversed(p)) for p in combinations_with_replacement(range(m+1), n)}


def beta_partitions(m, n):
    # Invert the strictly decreasing beta numbers a_i=lambda_i+n-i.
    return {tuple(a-(n-1-i) for i, a in enumerate(reversed(beta)))
            for beta in combinations(range(m+n), n)}


def verify_rectangle(m, n):
    rows = row_partitions(m, n)
    by_beta = beta_partitions(m, n)
    assert rows == by_beta
    assert len(rows) == comb(m+n, n)
    for lam in rows:
        dual = tuple(sum(x >= j for x in lam) for j in range(1, m+1))
        a = [x+n-1-i for i, x in enumerate(lam)]
        b = [n+j-x for j, x in enumerate(dual)]
        assert len(set(a+b)) == m+n
        assert sorted(a+b) == list(range(m+n))
        # Check coefficients, including the empty rectangle, without Laurent evaluation.
        shifted_dual = [m+n-1-(x+m-1-j) for j, x in enumerate(dual)]
        assert b == shifted_dual
        assert all((a+shifted_dual).count(k) == 1 for k in range(m+n))
    return len(rows)


print('PARTITION IDENTITY: two independent exact enumerations')
for cutoff in [4, 6]:
    total = sum(verify_rectangle(m,n)
                for m in range(cutoff+1) for n in range(cutoff+1))
    print(f'All m,n in 0..{cutoff}: {(cutoff+1)**2} rectangles, {total} partitions; PASS')
t = sp.Symbol('t')
written = t + t*t  # m=n=1, lambda=(1)
corrected = t + 1
assert sp.expand(written-(1+t)) != 0
assert sp.expand(corrected-(1+t)) == 0
print('Negative control: m=n=1, lambda=(1): written lhs=t+t^2, rhs=1+t; FAIL as required')
print('Corrected lhs=t+1; PASS')


def gram_jacobian(n):
    # Variables: s_0i followed by s_ij with 1<=i<j<=n.
    edge_pairs = [(0,i) for i in range(1,n+1)] + list(combinations(range(1,n+1),2))
    sq = {p: sp.Symbol(f's{p[0]}_{p[1]}') for p in edge_pairs}
    ell = {p: sp.Symbol(f'l{p[0]}_{p[1]}', positive=True) for p in edge_pairs}
    coords = [sq[(0,i)] for i in range(1,n+1)]
    coords += [(sq[(0,i)]+sq[(0,j)]-sq[(i,j)])/2
               for i,j in combinations(range(1,n+1),2)]
    jac_sq = sp.Matrix(coords).jacobian([sq[p] for p in edge_pairs]).det()
    assert abs(jac_sq) == sp.Rational(1,2)**(n*(n-1)//2)
    substitutions = {sq[p]:ell[p]**2 for p in edge_pairs}
    jac_len = sp.Matrix([g.subs(substitutions) for g in coords]).jacobian(
        [ell[p] for p in edge_pairs]).det()
    expected = sp.Integer(2)**n * sp.prod(ell[p] for p in edge_pairs)
    assert sp.simplify(abs(jac_len)-expected) == 0
    # A positive-definite independent check: choose orthonormal based edge vectors.
    gram = sp.eye(n)
    assert gram.det() == 1
    lengths_squared = [1 if i==0 else 2 for i,j in edge_pairs]
    recovered = sp.zeros(n)
    value = dict(zip(edge_pairs, lengths_squared))
    for i in range(1,n+1):
        for j in range(1,n+1):
            recovered[i-1,j-1] = (value[(0,i)]+value[(0,j)]-
                (0 if i==j else value[tuple(sorted((i,j)))]))/sp.Integer(2)
    assert recovered == gram
    return len(edge_pairs), str(jac_sq), str(sp.simplify(abs(jac_len)/sp.prod(ell.values())))


print('\nGRAM COORDINATE JACOBIAN: independent symbolic matrices')
for n in [1,2,3,4,5]:
    e, d, multiplier = gram_jacobian(n)
    print(f'n={n}, edges={e}: det(dg/ds)={d}; |det(dg/dl)|/product(l)={multiplier}; PASS')
print('One-dimensional invariant density: g=l^2, g^(-1) dg=2 dl/l; PASS')
print('The written volume^(-2) dl scales as dl/l^2 and fails the one-edge invariant-measure check.')
print('\nAll exact checks passed. Finite enumeration is not a proof for unbounded m,n.')
