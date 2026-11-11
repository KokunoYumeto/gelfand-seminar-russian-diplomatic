"""Exact independent checks for the GY1969 critical annotations.

Python 3 standard library only; all arithmetic uses fractions.Fraction.
The all-sites proof is in the chapter. These finite calculations check its
smallest nontrivial instances by two independent constructions.
"""
from fractions import Fraction as Q
from itertools import product
import json


def zeros(n):
    return [[Q(0) for _ in range(n)] for _ in range(n)]


def identity(n):
    return [[Q(i == j) for j in range(n)] for i in range(n)]


def scale(a, q):
    return [[q*x for x in row] for row in a]


def add(a, b):
    return [[x+y for x, y in zip(rowa, rowb)] for rowa, rowb in zip(a, b)]


def multiply(a, b):
    n = len(a)
    out = zeros(n)
    for i in range(n):
        for k in range(n):
            if a[i][k]:
                for j in range(n):
                    if b[k][j]:
                        out[i][j] += a[i][k] * b[k][j]
    return out


def tensor(a, b):
    return [[a[i][j]*b[k][l]
             for j in range(len(a)) for l in range(len(b))]
            for i in range(len(a)) for k in range(len(b))]


def bits(i, n):
    return tuple((i >> (n - 1 - j)) & 1 for j in range(n))


def index(bb):
    out = 0
    for b in bb:
        out = 2 * out + b
    return out


def marginal(matrix, keep, n):
    """Partial trace directly from the computational-basis definition."""
    keep = tuple(keep)
    discard = tuple(j for j in range(n) if j not in keep)
    result = zeros(2 ** len(keep))
    for a, b in product(range(2 ** len(keep)), repeat=2):
        aa, bb = bits(a, len(keep)), bits(b, len(keep))
        for d in product((0, 1), repeat=len(discard)):
            row, col = [0] * n, [0] * n
            for k, x, y in zip(keep, aa, bb):
                row[k], col[k] = x, y
            for k, x in zip(discard, d):
                row[k] = col[k] = x
            result[a][b] += matrix[index(row)][index(col)]
    return result


def embed(matrix, keep, n):
    """Embed an operator by tensoring identities on omitted sites."""
    keep = tuple(keep)
    discard = tuple(j for j in range(n) if j not in keep)
    result = zeros(2 ** n)
    for a, b in product(range(2 ** n), repeat=2):
        aa, bb = bits(a, n), bits(b, n)
        if all(aa[j] == bb[j] for j in discard):
            result[a][b] = matrix[index(tuple(aa[j] for j in keep))][
                                  index(tuple(bb[j] for j in keep))]
    return result


def eigenvector_check(matrix, vector, eigenvalue):
    assert [sum(x*y for x, y in zip(row, vector)) for row in matrix] == [
        eigenvalue*x for x in vector]


bell = [1, 0, 0, 1]  # unnormalized; its squared norm is 2
projector = [[Q(x*y, 2) for y in bell] for x in bell]
assert multiply(projector, projector) == projector
assert sum(projector[i][i] for i in range(4)) == 1
logs = []
for parameter in (Q(1, 2), Q(2, 3)):
    D = add(scale(projector, parameter), scale(identity(4), (1-parameter)/4))
    assert sum(D[i][i] for i in range(4)) == 1
    assert marginal(D, (0,), 2) == marginal(D, (1,), 2) == scale(identity(2), Q(1, 2))
    # Four linearly independent explicit vectors verify the complete spectrum.
    eigenvector_check(D, bell, (1+3*parameter)/4)
    for vector in ([1, 0, 0, -1], [0, 1, 0, 0], [0, 0, 1, 0]):
        eigenvector_check(D, vector, (1-parameter)/4)
    assert (1-parameter)/4 > 0
    global_density = tensor(D, D)
    subsets = [tuple(j for j in range(4) if mask & (1 << j)) for mask in range(16)]
    matrices = []
    for keep in subsets:
        first = embed(marginal(global_density, keep, 4), keep, 4)
        # Independently construct each embedded marginal pair by pair.
        blocks = []
        for pair in ((0, 1), (2, 3)):
            count = sum(j in keep for j in pair)
            blocks.append(D if count == 2 else scale(identity(4), Q(1, 2 if count == 1 else 1)))
        second = tensor(*blocks)
        assert first == second
        matrices.append(first)
    for a, b in product(matrices, repeat=2):
        assert multiply(a, b) == multiply(b, a)
    # A separate obstruction to product diagonalization: negative partial transpose.
    pt = zeros(4)
    for a, b, c, d in product((0, 1), repeat=4):
        pt[2*a+d][2*c+b] = D[2*a+b][2*c+d]
    for vector in ([1, 0, 0, 0], [0, 0, 0, 1], [0, 1, 1, 0]):
        eigenvector_check(pt, vector, (1+parameter)/4)
    eigenvector_check(pt, [0, 1, -1, 0], (1-3*parameter)/4)
    assert (1-3*parameter)/4 < 0
    logs.append({"parameter": str(parameter),
                 "density_eigenvalues": {str((1+3*parameter)/4): 1,
                                         str((1-parameter)/4): 3},
                 "one_site_marginals": "I_2/2",
                 "independently_matched_marginals": 16,
                 "ordered_commutators_exactly_zero": 256,
                 "normalized_bell_coefficient_determinant": "1/2",
                 "partial_transpose_eigenvalues": {str((1+parameter)/4): 3,
                                                    str((1-3*parameter)/4): 1}})
print(json.dumps({"method": "exact rational arithmetic, Python standard library",
                  "result": "all checks passed",
                  "scope": "four sites, all subsets, two parameters; general proof in chapter",
                  "checks": logs}, indent=2))
