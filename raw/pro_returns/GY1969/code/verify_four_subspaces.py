#!/usr/bin/env python3
"""Exact endomorphism dimensions for the notebook's four-subspace example.

All arithmetic is rational. A matrix X preserves a subspace with column
basis B precisely when l^T X b=0 for every column b and every annihilator l.
This supplies an independent check of the geometric argument in the chapter.
"""
from fractions import Fraction as F
import json


def rref(matrix, ncols):
    a = [[F(x) for x in row] for row in matrix]
    pivots = []
    r = 0
    for c in range(ncols):
        p = next((i for i in range(r, len(a)) if a[i][c]), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        z = a[r][c]
        a[r] = [x / z for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c]:
                z = a[i][c]
                a[i] = [x - z * y for x, y in zip(a[i], a[r])]
        pivots.append(c)
        r += 1
        if r == len(a):
            break
    return a, pivots


def nullspace(matrix, ncols):
    a, pivots = rref(matrix, ncols)
    result = []
    for c in range(ncols):
        if c in pivots:
            continue
        v = [F(0)] * ncols
        v[c] = F(1)
        for row, p in enumerate(pivots):
            v[p] = -a[row][c]
        result.append(v)
    return result


def basis(n):
    return [[int(i == j) for i in range(n)] for j in range(n)]


def plus(a, b):
    return [x + y for x, y in zip(a, b)]


def end_dimension(subspaces):
    n = len(subspaces[0][0])
    equations = []
    for columns in subspaces:
        assert len(rref(columns, n)[1]) == len(columns)
        annihilators = nullspace(columns, n)
        for ell in annihilators:
            for b in columns:
                equations.append([ell[i] * b[j] for i in range(n) for j in range(n)])
    rank = len(rref(equations, n * n)[1])
    return n * n - rank, rank


def direct_sum(a, b):
    na = len(a[0][0])
    nb = len(b[0][0])
    return [[v + [0] * nb for v in ea] + [[0] * na + w for w in eb]
            for ea, eb in zip(a, b)]


e1, e2, f1 = basis(3)
s3 = [[e1, e2], [f1, e2], [e1, plus(e2, f1)], [f1, plus(e1, e2)]]
e1, e2, e3, f1, f2 = basis(5)
s5 = [[e1, e2, e3], [f1, f2, e3],
      [e1, plus(e2, f1), plus(e3, f2)],
      [f1, plus(e1, f2), plus(e2, e3)]]
s1 = [[[1]]] * 4
systems = {"S(1,2)": s1, "S(3,2)": s3, "S(5,2)": s5,
           "S(5,2)+S(1,2)": direct_sum(s5, s1),
           "S(3,2)+S(3,2)": direct_sum(s3, s3)}
expected = {"S(1,2)": 1, "S(3,2)": 1, "S(5,2)": 1,
            "S(5,2)+S(1,2)": 7, "S(3,2)+S(3,2)": 4}
output = {}
for name, subspaces in systems.items():
    n = len(subspaces[0][0])
    dims = [len(s) for s in subspaces]
    dimension, rank = end_dimension(subspaces)
    assert dimension == expected[name], (name, dimension)
    grassmann_dimension = sum(d * (n - d) for d in dims)
    output[name] = {"ambient_dimension": n, "subspace_dimensions": dims,
                    "endomorphism_dimension": dimension, "constraint_rank": rank,
                    "orbit_dimension": n * n - dimension,
                    "configuration_space_dimension": grassmann_dimension}
assert output["S(3,2)+S(3,2)"]["orbit_dimension"] == 32
assert output["S(5,2)+S(1,2)"]["orbit_dimension"] == 29
print(json.dumps({"arithmetic": "exact rational", "all_assertions_passed": True,
                  "systems": output}, indent=2))
