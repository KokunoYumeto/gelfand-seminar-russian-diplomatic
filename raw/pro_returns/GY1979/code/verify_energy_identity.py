#!/usr/bin/env python3
"""Two exact checks of the nonabelian logarithmic-derivative diagnostic.

This checks a false identity used in a published proof, not irreducibility.
The local construction extends by a smooth bump to a compactly supported
su(2)-valued function, because the bump is identically one near the point.
"""
import json
import sympy as s

x, y, t = s.symbols('x y t', real=True)
X = s.Matrix([[0, 1], [-1, 0]])
Y = s.diag(s.I, -s.I)
Id = s.eye(2)
zero = s.zeros(2)
assert X.conjugate().T == -X and Y.conjugate().T == -Y
assert s.trace(X) == s.trace(Y) == 0
assert X * X == Y * Y == -Id and X * Y == -Y * X

# Check 1: directly differentiate the closed 2 x 2 matrix exponential.
r = s.sqrt(x*x + y*y)
Phi = x*X + y*Y
exp_phi = s.cos(r)*Id + s.sin(r)/r*Phi
p = {x:s.pi/2, y:0}
direct = s.simplify(exp_phi.diff(y).subs(p) * exp_phi.subs(p).inv())
expected = (2/s.pi)*(X*Y)
assert s.simplify(direct-expected) == zero
assert direct != Y

# Check 2: integrate the conjugated tangent matrix, independently of r.
# Differentiating exp(A+uB) gives dexp_A(B) exp(-A)
# = integral_0^1 exp(tA) B exp(-tA) dt.
A = (s.pi/2)*X
exp_tA = s.cos(t*s.pi/2)*Id + s.sin(t*s.pi/2)*X
exp_minus_tA = s.cos(t*s.pi/2)*Id - s.sin(t*s.pi/2)*X
integral = s.simplify((exp_tA*Y*exp_minus_tA).applyfunc(
    lambda z: s.integrate(z,(t,0,1))))
assert integral == direct

# Check a second point and the local differential series to first order.
p2 = {x:s.pi/4, y:0}
direct2 = s.simplify(exp_phi.diff(y).subs(p2)*exp_phi.subs(p2).inv())
assert direct2 == (2/s.pi)*(Y+X*Y)
series = s.sin(2*x)/(2*x)*Y + s.sin(x)**2/x*(X*Y)
assert series.applyfunc(lambda z:s.limit(z,x,0)) == Y
assert series.applyfunc(lambda z:s.diff(z,x).limit(x,0)) == X*Y

def entries(A):
    return [[str(v) for v in row] for row in A.tolist()]
print(json.dumps({
    'all_checks_passed': True,
    'group': 'SU(2)',
    'point': ['pi/2','0'],
    'X': entries(X), 'Y': entries(Y),
    'dPhi_dy': entries(Y),
    'beta_expPhi_dy_direct': entries(direct),
    'beta_expPhi_dy_integral': entries(integral),
    'second_point': ['pi/4','0'],
    'second_point_value': entries(direct2),
    'first_order_check': 'beta_y = Y + x X Y + O(x^2)',
    'scope': 'Counterexample to dPhi = d(exp Phi) exp(-Phi); no claim about irreducibility.'
}, indent=2))
