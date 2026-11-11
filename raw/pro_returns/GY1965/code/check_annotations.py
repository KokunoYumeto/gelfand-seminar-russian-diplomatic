#!/usr/bin/env python3
"""Exact independent checks of selected critical annotations.

These finite symbolic checks support, and do not replace, the written proofs.
Run with Python 3 and SymPy 1.14.0 (other recent SymPy versions should work).
"""
import sympy as s

print('Selected notebook annotations: exact symbolic second checks')
print('SymPy version:',s.__version__)
x,y=s.symbols('x y',real=True)
S=s.sin(x)+s.sin(y)-s.sin(x+y)
grad=s.Matrix([s.diff(S,x),s.diff(S,y)])
hessian=s.hessian(S,(x,y))
points=[(0,0),(2*s.pi/3,2*s.pi/3),(4*s.pi/3,4*s.pi/3)]
for point in points:
    g=s.simplify(grad.subs(dict(zip((x,y),point))))
    H=s.simplify(hessian.subs(dict(zip((x,y),point))))
    assert g==s.zeros(2,1)
    print('Torus critical point:',point,'; Hessian =',H,'; determinant =',s.simplify(H.det()))
c=s.symbols('c',real=True)
assert s.factor(2*c*c-c-1)==(c-1)*(2*c+1)
print('Completeness check: cos x=cos y gives x=+/-y modulo 2pi;')
print('minus branch gives (0,0); plus branch gives (cos x-1)(2 cos x+1)=0.')
eps=s.symbols('eps')
cubic=s.expand(s.series(S.subs({x:eps*x,y:eps*y}),eps,0,4).removeO().coeff(eps,3))
assert s.expand(cubic-x*y*(x+y)/2)==0
print('Degenerate-point cubic term:',s.factor(cubic))

# The cubic for the normalized spherical top is recovered by eliminating
# the cyclic velocities in the kinetic energy, independently of the notes.
u,n,e,h,p=s.symbols('u n e h p',real=True)
phidot=(n-e*u)/(1-u*u)
psidot=(e-n*u)/(1-u*u)
cyclic=s.factor(phidot**2+psidot**2+2*u*phidot*psidot)
assert s.cancel(cyclic-(n*n+e*e-2*n*e*u)/(1-u*u))==0
nutation=s.expand(2*(h-p*u)*(1-u*u)-n*n-e*e+2*n*e*u)
expected=2*p*u**3-2*h*u**2+2*(n*e-p)*u+2*h-n*n-e*e
assert s.expand(nutation-expected)==0
print('Spherical-top cyclic kinetic term:',cyclic)
print('Nutation cubic:',nutation)

# Slice derivative and volume use positive semiaxes, with no hidden symmetry.
t,a,b,axis=s.symbols('t a b c',positive=True)
section=s.pi*a*b*(1-t*t/axis**2)
integral=s.integrate(s.diff(section,t)**2,(t,-axis,axis))
volume=4*s.pi*a*b*axis/3
ratio=s.simplify(integral/volume)
assert ratio==2*s.pi*a*b/axis**2
print('Fixed-direction ellipsoid integral / volume:',ratio)
print('The dependence on a*b/c**2 disproves a universal fixed-direction constant.')

# The planar perturbation and its caustic.
q,r=s.symbols('q r',real=True)
F=s.Matrix([q*q-r*r+q,2*q*r-r])
jac=s.factor(F.jacobian((q,r)).det())
assert jac==4*q*q+4*r*r-1
print('Jacobian of z**2+conjugate(z):',jac)
tau=s.symbols('tau',real=True)
w=s.exp(2*s.I*tau)/4+s.exp(-s.I*tau)/2
derivative=s.diff(w,tau)
for j in range(3):
    angle=2*s.pi*j/3
    assert s.simplify(s.expand_complex(derivative.subs(tau,angle)))==0
    second=s.simplify(s.expand_complex(s.diff(w,tau,2).subs(tau,angle)))
    third=s.simplify(s.expand_complex(s.diff(w,tau,3).subs(tau,angle)))
    determinant=s.simplify(s.re(second)*s.im(third)-s.im(second)*s.re(third))
    assert determinant!=0
    print('Ordinary cusp at t=',angle,'; det(w_second,w_third)=',determinant)
print('Completeness of cusp list: w_prime=(i/2) exp(-it)(exp(3it)-1).')
print('PASS: all exact identities and stated negative examples checked.')
