"""Independent exact checks: integer Bareiss determinants and Fraction integration.

This file deliberately does not import sympy or bishop_certificates.py.
"""
from fractions import Fraction as F
from math import prod
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def bareiss(rows):
    a = [list(row) for row in rows]
    n = len(a)
    previous, sign = 1, 1
    for k in range(n - 1):
        if a[k][k] == 0:
            swap = next((i for i in range(k + 1, n) if a[i][k]), None)
            if swap is None:
                return 0
            a[k], a[swap] = a[swap], a[k]
            sign *= -1
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = a[i][j] * pivot - a[i][k] * a[k][j]
                assert numerator % previous == 0
                a[i][j] = numerator // previous
        for i in range(k + 1, n):
            a[i][k] = 0
        previous = pivot
    return sign * a[-1][-1]

def normalized_matrix(r, q, y):
    a = [(i * r) % q for i in range(q)]
    return [[prod(y + a[(i + h) % q] for h in range(k))
             for k in range(q)] for i in range(q)]

def multiply(p, q):
    result = [F(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            result[i + j] += a * b
    return result

def integrate(p, a, b):
    return sum(c * (b ** (i + 1) - a ** (i + 1)) / (i + 1) for i, c in enumerate(p))

def verify():
    original = json.loads((ROOT / "evidence/bishop_certificates.json").read_text())
    results = {"method": "integer Bareiss elimination plus Fraction polynomial arithmetic",
               "endpoint_checks": [], "exact_integral_checks": []}
    for r, q in [(1, 2), (2, 3), (3, 4), (3, 10), (9, 16)]:
        d0 = bareiss(normalized_matrix(r, q, 0))
        d1 = bareiss(normalized_matrix(r, q, 1))
        expected = (-1) ** ((q - 1) * (q - 2) // 2) * prod(((j * r) % q) ** j for j in range(1, q))
        assert d0 == expected
        if q in (10, 16):
            first = next(v for v in original["determinants"] if v["r"] == r and v["q"] == q)
            scale = q ** (q * (q - 1) // 2)
            assert F(d0, scale) == F(first["at_zero"])
            assert F(d1, scale) == F(first["at_right_endpoint"])
        results["endpoint_checks"].append({"r": r, "q": q, "scaled_D0": str(d0),
                                           "scaled_D1": str(d1), "sign_change": d0 * d1 < 0})
    for certificate in original["rational_approximants"]:
        r, q = certificate["r"], certificate["q"]
        coefficients = [F(v) for v in certificate["coefficients"]]
        degree = len(coefficients) - 1
        target_power = certificate["target_power"]
        total = F(0)
        for cell in range(q):
            lo, hi = F(cell, q), F(cell + 1, q)
            mid = (lo + hi) / 2
            residual = [F(0)] * (max(degree, target_power) + 1)
            orbit = [F(1)]
            for k, c in enumerate(coefficients):
                for i, v in enumerate(orbit):
                    residual[i] += c * v
                shift = F(k * r, q)
                offset = shift - (mid + shift).__floor__()
                orbit = multiply(orbit, [offset, F(1)])
            residual[target_power] -= 1
            total += integrate(multiply(residual, residual), lo, hi)
        assert total == F(certificate["error_squared"])
        c_bound = sum(abs(c) * F(k * (k - 1), 2) for k, c in enumerate(coefficients))
        assert c_bound == F(certificate["continuity_coefficient"])
        results["exact_integral_checks"].append({"r": r, "q": q, "degree": degree,
                                                "squared_error": str(total), "matches": True})
    selected = next(c for c in original["rational_approximants"] if c["q"] == 2 and c["degree"] == 4)
    assert F(selected["error_squared"]) < F(1, 10000)
    assert F(selected["continuity_coefficient"]) < 13
    results["finite_irrational_transfer_certificate"] = {
        "target": "x^2", "beta": "1/2", "delta_strict_upper_bound": "1/1690000",
        "L2_error_strict_upper_bound": "1/50", "checks": "exact rational inequalities passed"}
    results["conclusion"] = "All independent finite checks agree. No all-parameter statement follows from finite checks."
    return results

if __name__ == "__main__":
    result = verify()
    text = json.dumps(result, indent=2) + "\n"
    (ROOT / "evidence/independent_bishop_check.json").write_text(text)
    print(text, end="")
