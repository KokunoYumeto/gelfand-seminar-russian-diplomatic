"""Independent coefficient/sign audit for P000807; no peer data are mutated."""
import sympy as s
r,rho,c=s.symbols('r rho c',positive=True)
u=1/(1+r*r)
surface=s.Integer(2)*s.pi**2
I4=s.simplify(surface*s.integrate(u**4*r**3,(r,0,s.oo)))
Igrad=s.simplify(surface*s.integrate(s.diff(u,r)**2*r**3,(r,0,s.oo)))
assert I4==s.pi**2/6 and Igrad==4*s.pi**2/3
assert s.simplify(Igrad**2/I4)==32*s.pi**2/3
print('integral u^4 =',I4)
print('integral grad(u)^2 =',Igrad)
print('squared-gradient/quartic ratio =',s.simplify(Igrad**2/I4))

b=c/(r*r+rho*rho)
lap=s.factor(s.diff(b,r,2)+3*s.diff(b,r)/r)
res=s.factor(lap+b**3)
assert s.simplify(res-c*(c*c-8*rho*rho)/(r*r+rho*rho)**3)==0
assert s.simplify(res.subs(c,s.sqrt(8)*rho))==0
print('Delta[c/(r^2+rho^2)] =',lap)
print('Delta bubble + bubble^3 =',res)
print('c=sqrt(8)rho gives exact residual0.')
print('lim r * radial L2 integrand =',s.limit(r*surface*r**3*b**2,r,s.oo),
      '(positive: logarithmic divergence)')

# Scaling from u(r), rather than another integration, checks the normalized energy.
gradbubble=s.simplify((s.sqrt(8)*rho)**2/rho**2*Igrad)
quarticbubble=s.simplify((s.sqrt(8)*rho)**4/rho**4*I4)
assert gradbubble==quarticbubble==32*s.pi**2/3
print('Normalized bubble gradient and quartic integrals =',gradbubble)
print('Action =',s.simplify(gradbubble/2-quarticbubble/4))
print('All assertions passed. SymPy',s.__version__)
