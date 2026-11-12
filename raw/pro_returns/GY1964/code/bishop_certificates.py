"""Exact finite computations for the Bishop-operator development.

No finite result is used to claim cyclicity for every irrational parameter.
All integrations and certificates use rational arithmetic, not grid sampling.
Run with python bishop_certificates.py [output-json].
"""
from fractions import Fraction
from pathlib import Path
import json
import math
import sys
import sympy as s

x = s.symbols("x")

def fibre_matrix(r, q, t):
    a = [s.Rational((i * r) % q, q) for i in range(q)]
    return s.Matrix(q, q, lambda i, k: s.prod(t + a[(i + h) % q] for h in range(k)))

def endpoint_formula(r, q):
    a = [s.Rational((i * r) % q, q) for i in range(q)]
    return (-1) ** ((q - 1) * (q - 2) // 2) * s.prod(a[j] ** j for j in range(1, q))

def orbit_polynomials(r, q, degree):
    """Return T_(r/q)^k 1 on each of q intervals [i/q,(i+1)/q)."""
    pieces = []
    for cell in range(q):
        mid = s.Rational(2 * cell + 1, 2 * q)
        row = [s.Poly(1, x)]
        for k in range(degree):
            shift = s.Rational(k * r, q)
            weight = x + shift - s.floor(mid + shift)
            row.append(row[-1] * s.Poly(weight, x))
        pieces.append(row)
    return pieces

def integrate_poly(p, a, b):
    primitive = p.integrate()
    return primitive.eval(b) - primitive.eval(a)

def inner(pieces, left, right, q):
    return sum(integrate_poly(row[left] * row[right], s.Rational(i, q), s.Rational(i + 1, q))
               for i, row in enumerate(pieces))

def least_squares_certificate(r, q, degree, target_power):
    pieces = orbit_polynomials(r, q, degree)
    target = s.Poly(x ** target_power, x)
    gram = s.Matrix(degree + 1, degree + 1,
                    lambda i, j: inner(pieces, i, j, q))
    rhs = s.Matrix([sum(integrate_poly(row[k] * target, s.Rational(i, q), s.Rational(i + 1, q))
                        for i, row in enumerate(pieces)) for k in range(degree + 1)])
    coefficients = gram.inv() * rhs
    error2 = s.Rational(1, 2 * target_power + 1) - (rhs.T * coefficients)[0]
    # Independent direct residual-square integration, not the normal-equation formula.
    direct = s.Integer(0)
    for i, row in enumerate(pieces):
        residual = sum((row[k] * coefficients[k] for k in range(degree + 1)), s.Poly(0, x)) - target
        direct += integrate_poly(residual * residual, s.Rational(i, q), s.Rational(i + 1, q))
    assert s.cancel(error2 - direct) == 0 and error2 >= 0
    coefficient_bound = sum(abs(coefficients[k]) * s.Rational(k * (k - 1), 2)
                            for k in range(degree + 1))
    return {"r": r, "q": q, "degree": degree, "target_power": target_power,
            "coefficients": [str(v) for v in coefficients],
            "error_squared": str(s.factor(error2)),
            "error_decimal": float(s.sqrt(error2)),
            "continuity_coefficient": str(coefficient_bound),
            "continuity_coefficient_decimal": float(coefficient_bound),
            "direct_residual_check": True}

def main():
    result = {"determinants": [], "rational_approximants": [], "checks": {}}
    count = 0
    for q in range(2, 11):
        for r in range(1, q):
            if math.gcd(r, q) != 1:
                continue
            det0 = fibre_matrix(r, q, 0).det(method="domain-ge")
            formula = endpoint_formula(r, q)
            assert det0 == formula and det0 != 0
            # Direct cyclic matrix power is independent of the product construction.
            t = s.Rational(1, 3 * q)
            a = [s.Rational((i * r) % q, q) for i in range(q)]
            B = s.zeros(q)
            for i in range(q):
                B[i, (i + 1) % q] = t + a[i]
            product = s.prod(t + s.Rational(j, q) for j in range(q))
            assert B ** q == product * s.eye(q)
            krylov = s.Matrix.hstack(*[B ** k * s.ones(q, 1) for k in range(q)])
            assert krylov == fibre_matrix(r, q, t)
            count += 1
            if q <= 5:
                polynomial = s.factor(fibre_matrix(r, q, x).det(method="domain-ge"))
                result["determinants"].append({"r": r, "q": q, "polynomial": str(polynomial),
                                               "at_zero": str(det0)})
    result["checks"]["coprime_pairs_q2_to_q10"] = count
    result["checks"]["endpoint_and_matrix_power_checks"] = "all passed"
    # A higher-denominator check is exact but remains a finite check.
    for r, q in [(3, 10), (9, 16)]:
        zero = fibre_matrix(r, q, 0).det(method="domain-ge")
        endpoint = fibre_matrix(r, q, s.Rational(1, q)).det(method="domain-ge")
        result["determinants"].append({"r": r, "q": q, "at_zero": str(zero),
                                       "at_right_endpoint": str(endpoint),
                                       "opposite_endpoint_signs": bool(zero * endpoint < 0)})
    for r, q, degree, target_power in [(1, 2, 2, 2), (1, 2, 4, 2), (1, 2, 8, 2), (1, 3, 6, 2), (2, 3, 6, 2)]:
        result["rational_approximants"].append(least_squares_certificate(r, q, degree, target_power))
    text = json.dumps(result, indent=2) + "\n"
    if len(sys.argv) > 1:
        Path(sys.argv[1]).write_text(text)
    print(text, end="")

if __name__ == "__main__":
    main()
