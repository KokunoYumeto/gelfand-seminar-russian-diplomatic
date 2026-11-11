#!/usr/bin/env python3
"""Exact finite checks of the Dyson formula copied on GELFAND-P000445.

Three independent algorithms are compared: a residue-restricted lattice sum,
truncated multiplication of the Euler product, and the logarithmic-derivative
recurrence.  This checks coefficients only; it is not a proof of the identity.
Run from any directory: python check_dyson.py --limit 100
"""
import argparse
import itertools
import json
import math


def euler_product(limit):
    # q * product_{m>=1}(1-q^m)^24, truncated after q^limit.
    a = [1] + [0] * (limit - 1)
    for m in range(1, limit):
        b = [0] * limit
        for j in range(min(24, (limit - 1) // m) + 1):
            c = (-1) ** j * math.comb(24, j)
            for k in range(limit - j * m):
                b[k + j * m] += a[k] * c
        a = b
    return [0] + a


def divisor_recurrence(limit):
    # n a_n = -24 sum_{j=1}^n sigma_1(j) a_{n-j}; tau(n)=a_{n-1}.
    sigma = [0] * limit
    for d in range(1, limit):
        for j in range(d, limit, d):
            sigma[j] += d
    a = [1]
    for n in range(1, limit):
        numerator = -24 * sum(sigma[j] * a[n - j] for j in range(1, n + 1))
        assert numerator % n == 0
        a.append(numerator // n)
    return [0] + a


def lattice_sum(limit):
    # If sum v_i^2=10n<=10limit, every |v_i|<=floor(sqrt(10limit)).
    radius = math.isqrt(10 * limit)
    residues = [[a for a in range(-radius, radius + 1) if a % 5 == r]
                for r in (1, 2, 3, 4)]
    totals = [0] * (limit + 1)
    counts = [0] * (limit + 1)
    for first in itertools.product(*residues):
        e = -sum(first)
        if abs(e) > radius or e % 5:
            continue
        v = first + (e,)
        squares = sum(x * x for x in v)
        if squares % 10 or squares > 10 * limit:
            continue
        n = squares // 10
        numerator = math.prod(v[i] - v[j] for i in range(5) for j in range(i + 1, 5))
        assert numerator % 288 == 0
        totals[n] += numerator // 288
        counts[n] += 1
    return totals, counts


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--limit', type=int, default=100)
    args = parser.parse_args()
    assert args.limit >= 1
    product = euler_product(args.limit)
    recurrence = divisor_recurrence(args.limit)
    lattice, counts = lattice_sum(args.limit)
    assert product == recurrence == lattice
    print(json.dumps({
        'scope': f'Exact coefficient checks for 1 <= n <= {args.limit}; not an all-n proof.',
        'algorithms': ['finite Euler-product multiplication', 'divisor-sum recurrence',
                       'residue-restricted four-loop lattice enumeration'],
        'all_equal': True,
        'constant_term_of_unshifted_product': 1,
        'constant_term_of_corrected_q_product': 0,
        'rows': [{'n': n, 'tau': product[n], 'lattice_tuples': counts[n]}
                 for n in range(1, args.limit + 1)]
    }, indent=2))


if __name__ == '__main__':
    main()
