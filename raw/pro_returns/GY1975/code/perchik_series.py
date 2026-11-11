#!/usr/bin/env python3
"""Exact, independently checked coefficients of the P655--P656 Euler product.

No third-party packages.  Two algorithms over Python integers:
  (1) descending-degree multiplication of individual exterior factors;
  (2) the logarithmic-derivative recurrence, with exact-division checks.
The positive product must be retained through target weight + 2 because
the prefactor has lowest t-degree -2.  No claim of infinite nonvanishing
is made by this finite computation.
"""
from __future__ import annotations
import argparse
import csv
import json
from pathlib import Path
from time import perf_counter


def weights(ell: int):
    return range(-ell - 2, ell + 3, 2)


def positive_product(limit: int):
    """P(t,x) = product_(ell>=1,s in S_ell) (1-t^ell x^s), mod t^(limit+1)."""
    rows = [{} for _ in range(limit + 1)]
    rows[0][0] = 1
    for ell in range(1, limit + 1):
        for s in weights(ell):
            for n in range(limit, ell - 1, -1):
                target = rows[n]
                for k, value in rows[n - ell].items():
                    new = target.get(k + s, 0) - value
                    if new:
                        target[k + s] = new
                    else:
                        target.pop(k + s, None)
    return rows


def logarithmic_product(limit: int):
    """n P_n = sum_(r=1)^n B_r P_(n-r), B_r=-sum_(ell|r)ell sum_s x^(sr/ell)."""
    B = [{} for _ in range(limit + 1)]
    for ell in range(1, limit + 1):
        for r in range(ell, limit + 1, ell):
            factor = r // ell
            for s in weights(ell):
                k = s * factor
                B[r][k] = B[r].get(k, 0) - ell
    rows = [{0: 1}]
    divisions = 0
    for n in range(1, limit + 1):
        accum = {}
        for r in range(1, n + 1):
            for a, b in B[r].items():
                for c, d in rows[n - r].items():
                    accum[a + c] = accum.get(a + c, 0) + b * d
        row = {}
        for k, value in accum.items():
            q, rem = divmod(value, n)
            if rem:
                raise ArithmeticError((n, k, value, rem))
            divisions += 1
            if q:
                row[k] = q
        rows.append(row)
    return rows, divisions


def multiply_laurent(a, b):
    result = {}
    for (n, k), v in a.items():
        for (m, j), w in b.items():
            result[n + m, k + j] = result.get((n + m, k + j), 0) + v * w
    return {key: value for key, value in result.items() if value}


def prefactor_twice():
    result = {(0, 0): 1}
    for n, k in [(-1, -1), (-1, 1), (0, -2), (0, 2)]:
        result = multiply_laurent(result, {(0, 0): 1, (n, k): -1})
    return result


def euler_from_product(rows, max_weight):
    prefactor = prefactor_twice()
    result = {}
    for w in range(-2, max_weight + 1):
        value = sum(c * rows[w - a].get(-b, 0)
                    for (a, b), c in prefactor.items()
                    if 0 <= w - a < len(rows))
        q, rem = divmod(value, 2)
        if rem:
            raise ArithmeticError(('nonintegral Weyl coefficient', w, value))
        result[w] = q
    return result


def run(max_m: int, output: Path):
    output.mkdir(parents=True, exist_ok=True)
    limit = 2 * max_m + 2
    start = perf_counter()
    direct = positive_product(limit)
    t1 = perf_counter()
    alternate, division_count = logarithmic_product(limit)
    t2 = perf_counter()
    assert direct == alternate, 'independent algorithms disagree'
    for n, row in enumerate(direct):
        assert all(row.get(-k, 0) == value for k, value in row.items())
        assert all((n - k) % 2 == 0 for k in row)
        assert all(abs(k) <= 3 * n for k in row)
    coefficients = euler_from_product(direct, 2 * max_m)
    assert all(value == 0 for w, value in coefficients.items() if w % 2)
    known = {-2: 1, 0: 2, 2: 0, 4: 0, 6: 0, 8: -1, 10: 0,
             12: 0, 14: -1, 16: 0, 18: 0, 20: 0, 22: -1, 70: 10}
    for w, expected in known.items():
        if w <= 2 * max_m:
            assert coefficients[w] == expected, (w, coefficients[w], expected)
    with (output / 'perchik_coefficients.csv').open('w', newline='') as stream:
        writer = csv.writer(stream)
        writer.writerow(['m', 'weight_2m', 'relative_euler_characteristic'])
        for w in range(-2, 2 * max_m + 1, 2):
            writer.writerow([w // 2, w, coefficients[w]])
    result = {
        'max_m': max_m, 'max_weight': 2 * max_m,
        'positive_product_cutoff': limit,
        'methods': ['exterior-factor multiplication', 'logarithmic-derivative recurrence'],
        'all_laurent_rows_agree': True,
        'integer_division_checks': division_count,
        'parity_reflection_support_checks': True,
        'known_notebook_coefficients_agree': True,
        'direct_seconds': round(t1 - start, 4),
        'recurrence_seconds': round(t2 - t1, 4),
        'nonzero_positive_m': sum(coefficients[w] != 0 for w in range(2, 2 * max_m + 1, 2)),
        'sum_abs_positive_euler_coefficients': sum(abs(coefficients[w]) for w in range(2, 2 * max_m + 1, 2)),
        'coefficients': {str(w // 2): coefficients[w] for w in range(-2, 2 * max_m + 1, 2)},
        'claim_scope': 'Finite exact calculation only; no infinite nonvanishing conclusion.'
    }
    (output / 'perchik_verification.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--max-m', type=int, default=40)
    parser.add_argument('--output', type=Path, default=Path('perchik_output'))
    args = parser.parse_args()
    if args.max_m < 1:
        parser.error('--max-m must be positive')
    run(args.max_m, args.output)
