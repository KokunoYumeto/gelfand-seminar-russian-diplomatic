"""Exact coefficient check of the conic emendation, plus analytic spot checks.

No third-party dependencies. Coefficients are pairs of fractions (Q(i)).
The polynomial certificate is proved by exact coefficient arithmetic; the
analytic checks are numerical illustrations of the separately proved identity.
Run: python check_conic.py
"""
from fractions import Fraction as F
from math import pi
import cmath


def scalar(a=0, b=0):
    return F(a), F(b)


def cadd(a, b):
    return a[0]+b[0], a[1]+b[1]


def cmul(a, b):
    return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]


ZERO = scalar()
ONE = {(0, 0): scalar(1)}
X = {(1, 0): scalar(1)}
Y = {(0, 1): scalar(1)}


def add(*polys):
    out = {}
    for p in polys:
        for mon, coeff in p.items():
            out[mon] = cadd(out.get(mon, ZERO), coeff)
    return {mon: coeff for mon, coeff in out.items() if coeff != ZERO}


def scale(p, coeff):
    return {mon: c for mon, a in p.items() if (c := cmul(a, coeff)) != ZERO}


def sub(p, q):
    return add(p, scale(q, scalar(-1)))


def mul(p, q):
    out = {}
    for (a, b), v in p.items():
        for (c, d), w in q.items():
            mon = a+c, b+d
            out[mon] = cadd(out.get(mon, ZERO), cmul(v, w))
    return {mon: coeff for mon, coeff in out.items() if coeff != ZERO}


def degree(p):
    return max((a+b for a, b in p), default=-1)


def check(name, lhs, rhs):
    residual = sub(lhs, rhs)
    assert not residual, (name, residual)
    print(f'PASS {name}: residual is the zero polynomial in Q(i)[x,y].')


c = sub(add(mul(X, X), mul(Y, Y)), ONE)
f1 = scale(ONE, scalar(F(1, 2)))
f2 = scale(sub(scale(add(X, scale(ONE, scalar(2))), scalar(0, 1)), Y), scalar(F(1, 2)))
a = add(X, mul(c, f1))
b = add(Y, mul(c, f2))
t = add(X, ONE, scale(Y, scalar(0, 1)))
s = sub(add(X, ONE), scale(Y, scalar(0, 1)))
A = sub(sub(mul(s, add(a, ONE)), a), scale(ONE, scalar(2)))
B = scale(mul(s, s), scalar(0, F(1, 2)))

check('input triple unimodular: x*x+y*y-c=1', sub(add(mul(X, X), mul(Y, Y)), c), ONE)
check('t*s=2*(a+1)', mul(t, s), scale(add(a, ONE), scalar(2)))
check('b=t^2/(2i)+i*t*a', b, add(scale(mul(t, t), scalar(0, -F(1, 2))), scale(mul(t, a), scalar(0, 1))))
check('A*a+B*b=1', add(mul(A, a), mul(B, b)), ONE)
print('Degrees:', {'f1': degree(f1), 'f2': degree(f2), 'a': degree(a), 'b': degree(b), 'A': degree(A), 'B': degree(B)})
print('Independent root check: exact Gaussian-rational interpolation on a 6x6 grid,')
print('with the separate degree bound <=5 in each variable; see independent_checks.py.')


def h(w):
    return cmath.exp(1j*pi*(w-1)/2)


def entire_F(w):
    if w == 1:
        return 1j*pi/4-0.5
    if w == -1:
        return 1j*pi/4+0.5
    return (h(w)-w)/(w*w-1)


points = [(0, 1), (0, -1), (1, 1), (1, -1), (2+1j, 0),
          (-0.5j, 2+0.25j), (0.75-0.25j, -2+0.5j), (2, 1+1e-5j)]
worst_bezout = 0.0
worst_row = 0.0
for x, y in points:
    fy, hy = entire_F(y), h(y)
    gy = y+(x*x+y*y-1)*fy
    by = hy+x*x*fy
    AA, BB = -x*fy/hy, 1/hy
    worst_row = max(worst_row, abs(gy-by))
    worst_bezout = max(worst_bezout, abs(AA*x+BB*by-1))
assert worst_row < 1e-10 and worst_bezout < 1e-10
print(f'PASS analytic row identity at {len(points)} selected complex points; max residual {worst_row:.3e}.')
print(f'PASS analytic Bezout identity at {len(points)} selected complex points; max residual {worst_bezout:.3e}.')
print('These analytic spot checks are not a proof of an entire-function identity or a growth bound.')
print('The appendix proves removability, the all-point identities, and a uniform exponential bound.')
