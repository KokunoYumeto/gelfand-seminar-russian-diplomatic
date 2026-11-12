"""Reconstructed method; requires mpmath."""
import json
import mpmath as mp

mp.mp.dps = 80

def exact_integral(a):
    a = mp.mpf(a)
    z = -mp.j*a
    return mp.im(
        mp.gammainc(mp.mpf(1)/3, 0, z) /
        (3*z**(mp.mpf(1)/3))
    )

def asymptotic(a):
    a = mp.mpf(a)
    return (
        mp.gamma(mp.mpf(1)/3)/(6*a**(mp.mpf(1)/3))
        - mp.cos(a)/(3*a)
        - 2*mp.sin(a)/(9*a*a)
    )

rows = []
for a in (1, 10, 100, 100000):
    value = exact_integral(a)
    row = {"A": a, "integral": mp.nstr(value, 65)}
    if a <= 100:
        points = [mp.mpf(0)]
        k = 1
        while k*mp.pi < a:
            points.append((k*mp.pi/a)**(mp.mpf(1)/3))
            k += 1
        points.append(mp.mpf(1))
        q = mp.quad(lambda x: mp.sin(a*x**3), points)
        row["quadrature_error"] = mp.nstr(abs(value-q), 8)
        assert abs(value-q) < mp.mpf("1e-60")
    if a == 100000:
        error = abs(value-asymptotic(a))
        bound = mp.mpf(20)/(27*mp.mpf(a)**3)
        row.update(
            asymptotic=mp.nstr(asymptotic(a), 65),
            absolute_error=mp.nstr(error, 20),
            bound=mp.nstr(bound, 20)
        )
        assert error <= bound
    rows.append(row)

print(json.dumps(rows, indent=2))
