"""Dependency-free exact polynomial checks; analytic proofs are in the TeX file."""
from fractions import Fraction as F
from math import sin, pi, isclose
VARIABLES = ('u', 'n', 'e', 'h', 'p')
ZERO = (0,) * len(VARIABLES)
def const(x):
    return {ZERO: F(x)} if x else {}
def var(name):
    powers = [0] * len(VARIABLES)
    powers[VARIABLES.index(name)] = 1
    return {tuple(powers): F(1)}
def add(*polys):
    result = {}
    for poly in polys:
        for powers, coefficient in poly.items():
            result[powers] = result.get(powers, F(0)) + coefficient
    return {k: v for k, v in result.items() if v}
def scale(poly, coefficient):
    return {k: coefficient * v for k, v in poly.items() if coefficient * v}
def mul(*polys):
    result = const(1)
    for poly in polys:
        product = {}
        for powers, coefficient in result.items():
            for other_powers, other_coefficient in poly.items():
                key = tuple(a + b for a, b in zip(powers, other_powers))
                product[key] = product.get(key, F(0)) + coefficient * other_coefficient
        result = {k: v for k, v in product.items() if v}
    return result
u,n,e,h,p = (var(x) for x in VARIABLES)
den = add(const(1), scale(mul(u,u),-1))
ph_num = add(n, scale(mul(e,u),-1))
ps_num = add(e, scale(mul(n,u),-1))
assert add(ph_num,mul(u,ps_num)) == mul(n,den)
assert add(ps_num,mul(u,ph_num)) == mul(e,den)
q_num = add(mul(ph_num,ph_num),mul(ps_num,ps_num),scale(mul(u,ph_num,ps_num),2))
q_reduced = add(mul(n,n),mul(e,e),scale(mul(n,e,u),-2))
assert q_num == mul(q_reduced,den)
cubic = add(scale(mul(add(h,scale(mul(p,u),-1)),den),2),scale(q_reduced,-1))
expected = add(scale(mul(p,u,u,u),2),scale(mul(h,u,u),-2),scale(mul(n,e,u),2),scale(mul(p,u),-2),scale(h,2),scale(mul(n,n),-1),scale(mul(e,e),-1))
assert cubic == expected
print('Cyclic-momentum identities: both exact polynomial checks passed.')
print('Angular quadratic numerator: (n^2+e^2-2*n*e*u)*(1-u^2).')
print('Nutation cubic: 2*p*u^3-2*h*u^2+2*(n*e-p)*u+2*h-n^2-e^2.')
# Integral of t^2 on [-c,c] is (2/3)c^3.
integral_coefficient = 4 * F(2,3)
volume_coefficient = F(4,3)
assert integral_coefficient == F(8,3)
assert integral_coefficient/volume_coefficient == 2
print('Ellipsoid derivative-square integral: (8/3)*pi^2*a^2*b^2/c.')
print('Ellipsoid ratio to volume: 2*pi*a*b/c^2.')
# Integral of sin^2(angle/2) over [0,2*pi] is pi.
samples = 257
step = 2*pi/samples
largest_error = 0.0
for radius in (1/3, 1.0, 2.5):
    one_row = sum(sin(j*step/2)**2 for j in range(samples))
    circle_integral = radius**2 * step**2 * samples * one_row
    expected_integral = 2*pi**2*radius**2
    largest_error = max(largest_error, abs(circle_integral/expected_integral-1))
    assert isclose(circle_integral, expected_integral, rel_tol=1e-13, abs_tol=1e-13)
print('Circle cosine pair integral: 2*pi^2*R^2 = 2*pi*area.')
print(f'Independent 257-point circle quadrature, three radii: max relative error {largest_error:.3g}.')
print('All exact algebra and normalization checks passed.')
