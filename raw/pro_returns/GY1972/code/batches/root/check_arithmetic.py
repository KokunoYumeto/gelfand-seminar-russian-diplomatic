"""Exact checks of the chapter's arithmetic annotations (standard library only).

The proofs are in the item records. Finite checks are not used to infer an
all-prime or all-degree theorem. Run this file to reproduce arithmetic_output.json.
"""
from fractions import Fraction as Q
from math import comb, factorial, gcd
from pathlib import Path
import json


def bernoulli(n):
    b = [Q(1)]
    for m in range(1, n + 1):
        b.append(-sum((Q(comb(m + 1, k)) * b[k] for k in range(m)), Q()) / (m + 1))
    return b


def valuation(x, p):
    x = Q(x)
    if not x:
        return 'infinity'
    a, b = abs(x.numerator), x.denominator
    v = 0
    while a % p == 0:
        a //= p
        v += 1
    while b % p == 0:
        b //= p
        v -= 1
    return v


def floor_measure(a, p, m, c):
    assert 0 <= a < p ** m and gcd(p, c) == 1
    return Q((c * a) // (p ** m)) - Q(c - 1, 2)


def bernoulli_polynomial(n, x, numbers):
    return sum((Q(comb(n, k)) * numbers[k] * x ** (n-k)
                for k in range(n+1)), Q())


def main():
    floor_cases = 0
    for p in (2, 3, 5, 7):
        for c in range(1, 12):
            if gcd(c, p) != 1:
                continue
            for m in range(4):
                for a in range(p ** m):
                    parent = floor_measure(a, p, m, c)
                    children = sum((floor_measure(a + j*p**m, p, m+1, c)
                                    for j in range(p)), Q())
                    assert parent == children, (p, c, m, a)
                    assert valuation(parent, p) == 'infinity' or valuation(parent, p) >= 0
                    floor_cases += 1

    numbers = bernoulli(102)
    inverse_coefficients = [Q(1)]
    for m in range(1, 14):
        inverse_coefficients.append(-sum((inverse_coefficients[j] / factorial(m-j+1)
                                         for j in range(m)), Q()))
    assert all(inverse_coefficients[j] == numbers[j] / factorial(j)
               for j in range(14))
    power_cases = 0
    for d in range(13):
        for n in range(1, 12):
            direct = sum(j**d for j in range(1, n+1))
            via_polynomial = (bernoulli_polynomial(d+1, n+1, numbers)
                              - bernoulli_polynomial(d+1, 1, numbers)) / (d+1)
            endpoints = [Q((n+1)**(d+1)-1, d+1)]
            for r in range(1, d+1):
                endpoints.append(Q(factorial(d), factorial(d-r+1))
                                 * ((n+1)**(d-r+1)-1))
            solved = [Q()] * (d+1)
            for r in range(d, -1, -1):
                solved[r] = endpoints[r] - sum((solved[j]/factorial(j-r+1)
                                               for j in range(r+1, d+1)), Q())
            via_coefficients = sum((inverse_coefficients[r] * endpoints[r]
                                    for r in range(d+1)), Q())
            assert direct == via_polynomial == solved[0] == via_coefficients, (d, n)
            power_cases += 1

    zeta_rows = []
    for i in range(3):
        k = 1 + 2 * 5**i
        n = 2*k
        raw = -numbers[n]/n
        corrected = (1-5**(n-1))*raw
        raw_error = valuation(raw-Q(1, 3), 5)
        corrected_error = valuation(corrected-Q(1, 3), 5)
        assert isinstance(raw_error, int) and raw_error >= i+1
        assert isinstance(corrected_error, int) and corrected_error >= i+1
        assert raw != Q(-1,12)
        zeta_rows.append(dict(i=i, k=k, n=n, raw_zeta=str(raw),
                              raw_error_from_limit_1_over_3_valuation=raw_error,
                              corrected_error_from_limit_1_over_3_valuation=corrected_error))

    # Independent rational specializations of the symbolic root identity.
    # P_m and P_{m-1} are arbitrary: only the Hecke relation is assumed.
    root_cases = 0
    for p in (2,3,5,7):
        for weight in (2,4,12):
            for alpha in (Q(1),Q(2),Q(-3)):
                eigenvalue = alpha + Q(p**(weight-1))/alpha
                c = Q(p**(weight-2))
                for m in (1,2,4):
                    child_coeff = alpha**(-m-1)*eigenvalue-p*c*alpha**(-m-2)
                    assert child_coeff == alpha**(-m)
                    root_cases += 1

    out = dict(
        status='all exact checks passed',
        floor_refinements=floor_cases,
        floor_primes=[2,3,5,7], floor_c_range=[1,11], floor_levels=[0,3],
        power_sum_cases=power_cases, degrees=[0,12], endpoints=[1,11],
        normalized_bernoulli=[str(x) for x in inverse_coefficients[:9]],
        zeta_counterexample=zeta_rows,
        constant_sequence_raw_limit='-1/12', nonconstant_sequence_raw_limit='1/3',
        root_identity_specializations=root_cases,
        limitation='Finite arithmetic checks supplement the general proofs; no convergence theorem is inferred from them.')
    destination = Path(__file__).with_name('arithmetic_output.json')
    destination.write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
