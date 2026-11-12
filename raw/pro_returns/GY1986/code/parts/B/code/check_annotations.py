"""Exact/symbolic checks for bounded annotations in records 682--697.

These are editorial calculations, not claimed new research theorems.  The root
agent independently checked the ball probabilities and quantum-KdV development.
"""
from fractions import Fraction
from math import factorial
import mpmath as mp
import sympy as sp

def valuation_factorial(n, p):
    result = 0
    while n:
        n //= p
        result += n
    return result

print('Record 695.8: the displayed k=100 coefficient')
value = Fraction(72**100 * factorial(149), factorial(102) * factorial(50))
v5 = valuation_factorial(149, 5) - valuation_factorial(102, 5) - valuation_factorial(50, 5)
assert v5 == -1 and value.denominator % 5 == 0
print('v_5 =', v5)
print('Reduced denominator =', value.denominator)
print('Integer =', value.denominator == 1)

print('\nRecord 689.5: ball slab at dimension 1000')
mp.mp.dps = 80
d = 1000
normalizer = mp.gamma(mp.mpf(d)/2 + 1) / (
    mp.sqrt(mp.pi) * mp.gamma(mp.mpf(d+1)/2))
for width in ('0.01', '0.005'):
    a = mp.mpf(width)
    beta = mp.betainc(mp.mpf('0.5'), mp.mpf(d+1)/2, 0, a*a, regularized=True)
    quad = 2 * normalizer * mp.quad(
        lambda x: mp.power(1 - x*x, mp.mpf(d-1)/2), [0, a])
    assert abs(beta - quad) < mp.mpf('1e-70')
    print('Half-width/R =', width)
    print('Regularized beta =', mp.nstr(beta, 70))
    print('Density quadrature =', mp.nstr(quad, 70))
    print('Absolute discrepancy =', mp.nstr(abs(beta-quad), 5))

print('\nRecord 693.7: Miura Hamiltonian-operator normalization')
x = sp.symbols('x')
v = sp.Function('v')(x)
f = sp.Function('f')(x)
u = sp.diff(v, x) - v*v
adjoint_D_f = -sp.diff(f, x) - 2*v*f
Pv_adjoint_D_f = sp.diff(adjoint_D_f, x)/2
pushforward = sp.diff(Pv_adjoint_D_f, x) - 2*v*Pv_adjoint_D_f
target = -sp.diff(f, x, 3)/2 - u*sp.diff(f, x) - sp.diff(u*f, x)
residual = sp.simplify(pushforward-target)
assert residual == 0
print('D (1/2 partial) D* - (-1/2 partial^3 - u partial - partial u) =', residual)

print('\nRecord 693.12: Riccati sign')
y = sp.Function('y')(x)
a = sp.Function('a')(x)
alpha = -sp.diff(y, x)/y
riccati = sp.simplify(
    (sp.diff(alpha, x)-alpha*alpha).subs(sp.diff(y,x,2), a*y))
assert sp.simplify(riccati+a) == 0
print('alpha prime - alpha squared, using y double prime = a y:', riccati)
