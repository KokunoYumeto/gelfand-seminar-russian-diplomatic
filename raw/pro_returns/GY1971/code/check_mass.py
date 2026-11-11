#!/usr/bin/env python3
"""Exact editorial audit of the rank-32 even-unimodular mass bound.

The mass formula is historical, not a result proved by this program.
Source: King, arXiv:math/0012231v3, section 2; section 6 checks the bound.
Only the Python standard library is required.
"""
from fractions import Fraction
from math import comb, factorial
import json


def bernoulli_recurrence(limit):
    """Use sum_{j=0}^{n} binom(n+1,j) B_j = 0, n >= 1."""
    out = [Fraction(1)]
    for n in range(1, limit + 1):
        out.append(-sum(Fraction(comb(n + 1, j)) * out[j]
                        for j in range(n)) / (n + 1))
    return out


def bernoulli_stirling(limit):
    """Independently use B_n = sum_k (-1)^k k! S(n,k)/(k+1)."""
    row = [1]
    out = [Fraction(1)]
    for n in range(1, limit + 1):
        nxt = [0] * (n + 1)
        for k in range(1, n + 1):
            nxt[k] = (row[k - 1]
                      + (k * row[k] if k < len(row) else 0))
        row = nxt
        out.append(sum(Fraction((-1)**k * factorial(k) * row[k], k + 1)
                       for k in range(n + 1)))
    return out


def mass(n, bernoulli):
    assert n > 0 and n % 8 == 0
    r = n // 2
    result = abs(bernoulli[r]) / n
    for j in range(1, r):
        result *= abs(bernoulli[2 * j]) / (4 * j)
    return result


def main():
    a = bernoulli_recurrence(30)
    b = bernoulli_stirling(30)
    assert a == b
    masses = {n: mass(n, a) for n in (8, 16, 24, 32)}
    assert all(mass(n, b) == m for n, m in masses.items())
    e8_order = 696729600
    assert masses[8] == Fraction(1, e8_order)
    # Independent normalization check using E8 + E8 and D16+.
    rank16_sum = (Fraction(1, 2 * e8_order**2)
                  + Fraction(1, 2**15 * factorial(16)))
    assert masses[16] == rank16_sum
    bounds = {n: -((-2 * m.numerator) // m.denominator)
              for n, m in masses.items()}
    assert bounds[32] == 80618466
    print(json.dumps({
        'scope': 'Exact evaluation of a published mass formula, not a classification.',
        'formula': 'm_n = |B_(n/2)|/n * product_(j=1)^(n/2-1) |B_(2j)|/(4j)',
        'bernoulli_algorithms_agree_through': 30,
        'rank8_automorphism_check': 'passed',
        'rank16_automorphism_check': 'passed',
        'masses': {str(n): {'exact': str(m), 'approximate': float(m),
                            'ceil_twice_mass': bounds[n]}
                   for n, m in masses.items()},
        'bound_argument': 'Every positive-rank lattice has distinct automorphisms +I and -I; each term in the mass is at most 1/2.'
    }, indent=2))


if __name__ == '__main__':
    main()
