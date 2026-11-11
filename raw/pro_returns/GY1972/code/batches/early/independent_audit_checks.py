"""Independent exact checks of root items 298.8 and 300.1--300.4.

No root scripts or outputs are imported.  Fractions alone implement Bernoulli
recurrence, direct summation, polynomial differentiation and triangular solves.
These finite checks supplement, rather than replace, the proofs in the audit.
"""
from fractions import Fraction as Q
from math import comb, factorial
import json
from pathlib import Path


def bernoulli_list(last):
    ans = [Q(1)]
    for m in range(1, last + 1):
        ans.append(-sum(Q(comb(m + 1, j)) * ans[j] for j in range(m)) / (m + 1))
    return ans


def vp(value, prime):
    value = Q(value)
    if not value:
        return "infinity"
    n, d = abs(value.numerator), value.denominator
    v = 0
    while n % prime == 0:
        n //= prime
        v += 1
    while d % prime == 0:
        d //= prime
        v -= 1
    return v


def evaluate(coeff, x):
    return sum(a * Q(x) ** j for j, a in enumerate(coeff))


def derivative(coeff):
    return [j * coeff[j] for j in range(1, len(coeff))]


def primitive(coeff):
    return [Q(0)] + [a / (j + 1) for j, a in enumerate(coeff)]


def bernoulli_polynomial_value(m, x, values):
    return sum(Q(comb(m, j)) * values[j] * Q(x) ** (m - j) for j in range(m + 1))


B = bernoulli_list(502)
assert B[:5] == [Q(1), Q(-1, 2), Q(1, 6), Q(0), Q(-1, 30)]

zeta_checks = []
for i in range(4):
    k = 1 + 2 * 5**i
    n = 2 * k
    raw = -B[n] / n
    corrected = (1 - 5 ** (n - 1)) * raw
    assert n % 4 == 2
    assert vp(raw - Q(1, 3), 5) >= i + 1
    assert vp(raw + Q(1, 12), 5) == 1
    assert vp(corrected - Q(1, 3), 5) >= i + 1
    zeta_checks.append({
        "i": i, "k": k, "n": n,
        "raw_zeta": str(raw),
        "v5_raw_minus_one_third": vp(raw - Q(1, 3), 5),
        "v5_raw_minus_zeta_minus_one": vp(raw + Q(1, 12), 5),
        "v5_corrected_minus_one_third": vp(corrected - Q(1, 3), 5),
    })

power_checks = []
matrix_checks = []
for degree in range(13):
    # Independent inverse row by solving c*A=e_0, with A upper triangular.
    A = [[Q(1, factorial(col - row + 1)) if col >= row else Q(0)
          for col in range(degree + 1)] for row in range(degree + 1)]
    invrow = []
    for col in range(degree + 1):
        target = Q(int(col == 0))
        invrow.append(target - sum(invrow[j] * A[j][col] for j in range(col)))
    assert invrow == [B[r] / factorial(r) for r in range(degree + 1)]
    for endpoint in (0, 1, 2, 5, 11):
        direct = sum(Q(j) ** degree for j in range(1, endpoint + 1))
        formula = (bernoulli_polynomial_value(degree + 1, endpoint + 1, B)
                   - bernoulli_polynomial_value(degree + 1, 1, B)) / (degree + 1)
        assert direct == formula
        power_checks.append({"degree": degree, "endpoint": endpoint, "sum": str(direct)})

        # A polynomial with all degrees represented tests more than monomials.
        f = [Q((-1) ** j * (j + 1), j + 2) for j in range(degree + 1)]
        functions = [f]
        for r in range(degree):
            functions.append(derivative(functions[-1]))
        sums = [sum(evaluate(g, j) for j in range(1, endpoint + 1)) for g in functions]
        differences = []
        for g in functions:
            G = primitive(g)
            differences.append(evaluate(G, endpoint + 1) - evaluate(G, 1))
        assert all(sum(A[r][c] * sums[c] for c in range(degree + 1)) == differences[r]
                   for r in range(degree + 1))
        recovered = sum(invrow[r] * differences[r] for r in range(degree + 1))
        assert recovered == sums[0]
        matrix_checks.append({"degree": degree, "endpoint": endpoint,
                              "recovered_sum": str(recovered)})

output = {
    "status": "all assertions passed",
    "method": "Independent exact Fraction implementation; no root code imported",
    "zeta_limit_argument": "The fixed nonpolar weight branch is continuous; corrected values tend to (1-5)*zeta(-1)=1/3, while 5^(n_i-1) tends to zero. The constant sequence instead has value -1/12.",
    "zeta_difference_of_limits": str(Q(1, 3) + Q(1, 12)),
    "zeta_cases": zeta_checks,
    "power_sum_cases": power_checks,
    "triangular_system_cases": matrix_checks,
    "bernoulli_coefficients_0_to_12": [str(B[r] / factorial(r)) for r in range(13)],
    "k_zero_endpoint": "(B1(n+1)-B1(1))=n, including n=0; replacing B1(1) by B1(0) incorrectly gives n+1.",
}
destination = Path(__file__).with_name("independent_audit_checks.json")
destination.write_text(json.dumps(output, indent=2) + "\n")
print(json.dumps({"status": output["status"], "zeta_cases": len(zeta_checks),
                  "power_cases": len(power_checks), "matrix_cases": len(matrix_checks),
                  "output": str(destination)}))
