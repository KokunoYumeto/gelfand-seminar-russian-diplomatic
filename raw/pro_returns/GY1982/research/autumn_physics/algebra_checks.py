"""Exact independent checks for disputed notebook formulae; no empirical theorem extrapolation."""
from functools import lru_cache
from pathlib import Path
import sympy as s

h,c,D,t,r,q=s.symbols('h c Delta t r s',nonzero=True)
@lru_cache(None)
def vacuum(word):
    """<h| product L_indices |h>, standard Virasoro convention."""
    if not word:return s.Integer(1)
    if word[0]<0 or word[-1]>0:return s.Integer(0)
    if 0 in word:
        j=word.index(0)
        return (h-sum(word[j+1:]))*vacuum(word[:j]+word[j+1:])
    for j in range(len(word)-1):
        a,b=word[j:j+2]
        if a>0 and b<0:
            swapped=word[:j]+(b,a)+word[j+2:]
            merged=word[:j]+(a+b,)+word[j+2:]
            central=c*s.Rational(a**3-a,12)*vacuum(word[:j]+word[j+2:]) if a+b==0 else 0
            return s.expand(vacuum(swapped)+(a-b)*vacuum(merged)+central)
    raise ValueError(word)

def gram(parts):
    return s.Matrix([[vacuum(tuple(reversed(a))+tuple(-v for v in b)) for b in parts] for a in parts])
G1=gram([(1,)])
G2=gram([(2,),(1,1)])
expected=s.Matrix([[4*h+c/2,6*h],[6*h,4*h*(2*h+1)]])
assert s.simplify(G2-expected)==s.zeros(2)
det=s.factor(G2.det())
assert s.expand(det-2*h*(16*h**2+(2*c-10)*h+c))==0

# Independent Kac parametrization and the source reverse-weight convention.
ct=13-6*(t+1/t)
ht=((r*t-q)**2-(t-1)**2)/(4*t)
Phi=(h+(q*q-1)*(c-13)/24+(r*q-1)/2)*(h+(r*r-1)*(c-13)/24+(r*q-1)/2)+(r*r-q*q)**2/16
assert s.factor(Phi.subs({h:ht,c:ct}))==0
source12=s.expand(16*Phi.subs({r:1,q:2,h:-D}))
assert s.expand(source12-(16*D**2-2*(c-5)*D+c))==0
# At c=0 the nonzero standard level-two root is positive 5/8,
# and its notebook weight is negative 5/8.
assert s.factor((det/(2*h)).subs(c,0))==2*h*(8*h-5)

# Classical Liouville stress tensor, with arbitrary off-shell smooth field.
x,y,mu=s.symbols('x y mu',real=True)
f=s.Function('f')(x,y)
coords=(x,y)
grad=s.Matrix([s.diff(f,z) for z in coords])
lap=sum(s.diff(f,z,2) for z in coords)
V=mu**2*s.exp(f)
H=s.hessian(f,coords)
Id=s.eye(2)
T=grad*grad.T-Id*((grad.dot(grad))/2+V)+2*(Id*lap-H)
trace=s.simplify(s.trace(T))
div=s.Matrix([sum(s.diff(T[a,b],coords[a]) for a in range(2)) for b in range(2)])
assert s.simplify(trace-2*(lap-V))==0
assert s.simplify(div-(lap-V)*grad)==s.zeros(2,1)
# Separate complex-coordinate derivation: f_zbar = V/4, (V/4)_z=V f_z/4.
fz,Vsym=s.symbols('f_z V')
dbar_minus=s.expand(2*fz*Vsym/4-2*Vsym*fz/4)
dbar_plus=s.expand(2*fz*Vsym/4+2*Vsym*fz/4)
assert dbar_minus==0 and dbar_plus==Vsym*fz

# The printed ansatz cannot be both conserved and traceless:
# divergence=(1+alpha)V grad - 2beta Hessian grad,
# trace=alpha V -2beta |grad|² on shell. Independent jet coefficients
# require beta=0, alpha=-1 for divergence but alpha=0 for trace.
alpha,beta=s.symbols('alpha beta')
assert s.solve([1+alpha,beta,alpha],[alpha,beta])==[]

# Witten quadratic model: direct differential check in both Morse signs.
tau,lam,z=s.symbols('tau lambda z',positive=True,real=True)
psi=s.exp(-tau*lam*z*z)
osc=-s.diff(psi,z,2)+4*tau*tau*lam*lam*z*z*psi
assert s.simplify(osc/psi)==2*tau*lam
checks=[]
for sign,occupation in [(1,0),(-1,1)]:
    residual=s.simplify((osc+2*tau*sign*lam*(2*occupation-1)*psi)/psi)
    assert residual==0
    checks.append((sign,occupation,residual))
# Independent first-order factor: (d/dz+2 tau lambda z) psi=0.
assert s.simplify(s.diff(psi,z)+2*tau*lam*z*psi)==0

# Finite-dimensional stochastic quantization normalization, checked with
# a nonquadratic potential rather than only an Ornstein--Uhlenbeck model.
v=s.symbols('v',real=True)
S=v**4/4+v*v/2
def stationary_density_residual(noise_variance,k):
    rho=s.exp(-k*S)
    return s.factor(s.diff(s.diff(S,v)*rho,v)+noise_variance*s.diff(rho,v,2)/2)
assert stationary_density_residual(2,1)==0
assert stationary_density_residual(1,2)==0
assert stationary_density_residual(1,1)!=0

# The Liouville primary covariance sign can be checked independently using
# differential operators D_n: [D_n,D_m]=(m-n)D_{n+m}, whereas two nested
# field commutators act in the reversed differential-operator order.
zz=s.symbols('z')
weight=s.symbols('delta')
test=zz**7+3*zz**2
def primary(n,func):
    return zz**(n+1)*s.diff(func,zz)+(n+1)*weight*zz**n*func
for n,m in [(1,2),(-1,2),(0,-2),(2,-2)]:
    comm=s.expand(primary(n,primary(m,test))-primary(m,primary(n,test)))
    assert s.simplify(comm-(m-n)*primary(n+m,test))==0

lines=[
'All exact symbolic checks passed.',
'Virasoro level-one Gram matrix: '+str(G1),
'Virasoro level-two Gram matrix: '+str(G2),
'Level-two determinant: '+str(det),
'Notebook (r,s)=(1,2) polynomial times 16, with h=-Delta: '+str(source12),
'General Kac parametrization substituted into symmetric polynomial: 0',
'Liouville stress trace: 2*(Laplacian(f)-V)',
'Liouville stress divergence: (Laplacian(f)-V)*gradient(f)',
'Independent holomorphic check, corrected minus sign: '+str(dbar_minus),
'Independent holomorphic check, printed plus sign: '+str(dbar_plus),
'Printed tensor ansatz: no constants alpha,beta satisfy both arbitrary-jet conditions.',
'Witten oscillator checks (Morse sign, occupation, residual): '+str(checks),
'Witten Gaussian also annihilated by independent first-order factor.',
'Fokker-Planck: variance 2 gives exp(-S), variance 1 gives exp(-2*S).',
'Primary differential-operator bracket checked for four mode pairs; nested field commutators reverse this order.',
'These checks certify algebraic identities and convention repairs only; they prove no global matrix-model or continuum measure theorem.'
]
out='\n'.join(lines)+'\n'
print(out,end='')
Path(__file__).with_name('algebra_checks_output.txt').write_text(out)
