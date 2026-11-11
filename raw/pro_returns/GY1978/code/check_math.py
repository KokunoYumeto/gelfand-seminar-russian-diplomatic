"""Independent exact checks for the critical audit; no numerical inference."""
from pathlib import Path
import sympy as s

t,eps,d,x,y=s.symbols('t eps delta x y', real=True)
r=s.symbols('r', positive=True)
z=eps*s.cos(2*t)
flux=s.integrate(s.cos(t)*s.sin(t)*s.diff(z,t),(t,0,2*s.pi))
assert s.simplify(flux+eps*s.pi)==0
print('Boundary integral int xy dz =',flux)
K=s.Matrix([[0,1,-d*y,0],[-1,0,-d*x,0],[d*y,d*x,0,0],[0,0,0,0]])
q=s.symbols('q')
char=s.factor(K.charpoly(q).as_expr())
assert s.simplify(char-q**2*(q**2+1+d**2*(x**2+y**2)))==0
print('Skew matrix characteristic polynomial =',char)
gap=s.pi*(1+eps**2)/s.sqrt(1+eps**2)
assert s.simplify(gap-s.pi*s.sqrt(1+eps**2))==0
print('Optimized area lower bound =',s.simplify(gap))
a,b,c=s.symbols('a b c', real=True)
J=s.Matrix([[0,a,b,c],[-a,0,c,-b],[-b,-c,0,a],[-c,b,-a,0]])
assert s.simplify(J**2+(a*a+b*b+c*c)*s.eye(4))==s.zeros(4)
print('Self-dual matrix square = -(a^2+b^2+c^2) I_4')
u=1/(1+r*r)
L4=s.integrate(2*s.pi**2*r**3*u**4,(r,0,s.oo))
energy=s.integrate(2*s.pi**2*r**3*s.diff(u,r)**2,(r,0,s.oo))
assert L4==s.pi**2/6 and energy==4*s.pi**2/3
print('Bubble integral u^4 =',L4)
print('Bubble Dirichlet energy =',energy)
print('Sharp-constant ratio =',s.simplify(energy**2/L4))
bubble=s.sqrt(8)*u
assert s.simplify(s.diff(bubble,r,2)+3/r*s.diff(bubble,r)+bubble**3)==0
print('Critical bubble solves radial Delta phi + phi^3 = 0')
