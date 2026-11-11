"""Independent symbolic and numerical checks for occurrences 102.1 and 102.5.

No external packages. Sparse Laurent polynomials certify the exact derivative
identity; second-order automatic differentiation supplies an independent check.
Beta-integral values are compared with an endpoint-regularized quadrature.
"""
from fractions import Fraction as Q
from math import sin,cos,exp,pi,sqrt,lgamma,comb
from pathlib import Path
import json


# Monomials are x^a epsilon^b u^c v^d, where u=sin(x^2), v=cos(x^2).
def term(a=0,b=0,c=0,d=0,k=1):
    return {(a,b,c,d):Q(k)} if k else {}


def add(*polys):
    result={}
    for p in polys:
        for m,c in p.items():
            result[m]=result.get(m,Q(0))+c
            if not result[m]: del result[m]
    return result


def scale(p,c):
    return {m:Q(c)*v for m,v in p.items() if c*v}


def multiply(p,q):
    out={}
    for m,a in p.items():
        for n,b in q.items():
            key=tuple(x+y for x,y in zip(m,n))
            out[key]=out.get(key,Q(0))+a*b
    return {m:c for m,c in out.items() if c}


def D(p):
    """Exact derivation: Dx=1, Dε=0, Du=2xv, Dv=-2xu."""
    out={}
    for (a,b,c,d),k in p.items():
        if a: out=add(out,term(a-1,b,c,d,k=k*a))
        if c: out=add(out,term(a+1,b,c-1,d+1,k=2*k*c))
        if d: out=add(out,term(a+1,b,c+1,d-1,k=-2*k*d))
    return out


def reduce_trig(p):
    """Reduce v^(2q+r)=(1-u^2)^q v^r exactly."""
    out={}
    for (a,b,c,d),k in p.items():
        q,r=divmod(d,2)
        for j in range(q+1):
            out=add(out,term(a,b,c+2*j,r,k=k*comb(q,j)*(-1)**j))
    return out


# For A=x^(-1/2)exp(epsilon cos(2x^2)), logarithmic differentiation gives
# A'/A=-1/(2x)-8 epsilon x u v. Then y=A*u.
a=add(term(-1,k=Q(-1,2)),term(1,1,1,1,k=-8))
first=add(multiply(a,term(c=1)),term(1,d=1,k=2))
second=add(D(first),multiply(a,first))
f=add(term(2,k=4),term(2,1,k=16),term(2,1,d=2,k=32),
      term(2,1,c=2,k=-32),term(2,2,2,2,k=-64),term(-2,k=Q(-3,4)))
residual=reduce_trig(add(second,multiply(f,term(c=1))))
assert residual=={}

# At 2x^2=pi/2+2k*pi, u and v have the same sign and u^2=v^2=1/2.
special_derivative={}
for (xpower,epower,upower,vpower),coefficient in D(f).items():
    assert (upower+vpower)%2==0
    key=(xpower,epower)
    special_derivative[key]=special_derivative.get(key,Q(0))+coefficient/Q(2)**((upower+vpower)//2)
special_derivative={k:v for k,v in special_derivative.items() if v}
assert special_derivative=={(1,0):Q(8),(1,1):Q(32),(1,2):Q(-32),(3,1):Q(-128),(-3,0):Q(3,2)}


class Jet:
    """Taylor coefficients through order two; second entry is f', third f''/2."""
    def __init__(self,c0,c1=0.,c2=0.):self.c=(float(c0),float(c1),float(c2))
    @staticmethod
    def lift(a):return a if isinstance(a,Jet) else Jet(a)
    def __add__(self,b):
        b=self.lift(b); return Jet(*(x+y for x,y in zip(self.c,b.c)))
    __radd__=__add__
    def __neg__(self):return Jet(*(-x for x in self.c))
    def __sub__(self,b):return self+-self.lift(b)
    def __mul__(self,b):
        b=self.lift(b); a=self.c; z=b.c
        return Jet(a[0]*z[0],a[0]*z[1]+a[1]*z[0],a[0]*z[2]+a[1]*z[1]+a[2]*z[0])
    __rmul__=__mul__
    def __pow__(self,p):
        a,b,c=self.c
        return Jet(a**p,p*a**(p-1)*b,p*a**(p-1)*c+p*(p-1)/2*a**(p-2)*b*b)
    def sin(self):
        a,b,c=self.c; return Jet(sin(a),cos(a)*b,cos(a)*c-sin(a)*b*b/2)
    def cos(self):
        a,b,c=self.c; return Jet(cos(a),-sin(a)*b,-sin(a)*c-cos(a)*b*b/2)
    def exp(self):
        a,b,c=self.c; z=exp(a); return Jet(z,z*b,z*(c+b*b/2))


def coefficient(x,e):
    return x*x*(4+16*e+32*e*cos(2*x*x)-16*e*e*sin(2*x*x)**2)-3/(4*x*x)


max_relative_residual=0.
for e in [.001,.01,.05]:
    for x in [1.01,1.2,1.8,2.,3.,4.,10.,20.]:
        X=Jet(x,1,0)
        Y=X**(-.5)*(e*(2*X*X).cos()).exp()*(X*X).sin()
        lhs=2*Y.c[2]+coefficient(x,e)*Y.c[0]
        rel=abs(lhs)/max(1,abs(2*Y.c[2]),abs(coefficient(x,e)*Y.c[0]))
        assert rel<1e-11
        max_relative_residual=max(max_relative_residual,rel)

e=Q(1,100)
positive_lower_bound=4+16*e-32*e-16*e*e-Q(3,4)
assert positive_lower_bound>0
negative_derivative_values=[]
for k in range(2,10):
    x=sqrt(pi/4+k*pi)
    derivative=2*x*(4+16*float(e)-16*float(e)**2)-128*float(e)*x**3+3/(2*x**3)
    assert derivative<0
    negative_derivative_values.append(dict(k=k,x=x,fprime=derivative))
gaps=[sqrt((k+1)*pi)-sqrt(k*pi) for k in range(1,20)]
assert all(a>b for a,b in zip(gaps,gaps[1:]))


def adaptive_simpson(fun,a,b,tol=1e-12,max_depth=30):
    fa,fb,fm=fun(a),fun(b),fun((a+b)/2)
    initial=(b-a)*(fa+4*fm+fb)/6
    def rec(a,b,fa,fb,fm,value,tol,depth):
        mid=(a+b)/2
        fl,fr=fun((a+mid)/2),fun((mid+b)/2)
        left=(mid-a)*(fa+4*fl+fm)/6
        right=(b-mid)*(fm+4*fr+fb)/6
        error=left+right-value
        if depth==0 or abs(error)<=15*tol:
            return left+right+error/15
        return rec(a,mid,fa,fm,fl,left,tol/2,depth-1)+rec(mid,b,fm,fb,fr,right,tol/2,depth-1)
    return rec(a,b,fa,fb,fm,initial,tol,max_depth)


endpoint_rows=[]
for delta in [1.,.5,.1,.01,.001,.0001,.000001,.00000001]:
    sine_beta=delta*exp(.5*__import__('math').log(pi)+lgamma(delta/2)-lgamma((delta+1)/2))
    # Remove the singular part analytically before numerical quadrature.
    # δ∫_0^π sin(x)^(δ-1) dx = 2+2δ∫_0^(π/2) sin(x)^(δ-1)(1-cos x) dx.
    fun=lambda theta: 0. if theta==0 else sin(theta)**(delta-1)*2*sin(theta/2)**2
    sine_quad=2+2*delta*adaptive_simpson(fun,0,pi/2)
    assert abs(sine_beta-sine_quad)<2e-11
    # y=x(1-x^2) on [0,1] has endpoint slopes 1 and -2.
    cubic_beta=delta/2*exp(lgamma(delta/2)+lgamma(delta)-lgamma(3*delta/2))
    endpoint_rows.append(dict(lambda_plus_one=delta,sine_beta=sine_beta,
                              sine_regularized_quadrature=sine_quad,cubic_beta=cubic_beta))
assert abs(endpoint_rows[-1]['sine_beta']-2)<2e-7
assert abs(endpoint_rows[-1]['cubic_beta']-1.5)<2e-7

result=dict(status='all independent checks passed',
    symbolic_residual='(y second derivative + f*y)/A = 0 after exact reduction by u^2+v^2=1',
    special_derivative='f_prime=2*x*(4+16*epsilon-16*epsilon^2)-128*epsilon*x^3+3/(2*x^3)',
    positive_lower_bound_for_x_greater_than_one=str(positive_lower_bound),
    automatic_differentiation_samples=24,max_relative_residual=max_relative_residual,
    negative_derivative_samples=negative_derivative_values,
    endpoint_tests=endpoint_rows,
    endpoint_limits=dict(sine=2,cubic=1.5),
    scope='The symbolic identity is exact. Numerical checks independently test differentiation and endpoint asymptotics; the general C1 endpoint statement is justified by the two-sided endpoint proof, not inferred from sampled values.')
output=json.dumps(result,indent=2)+'\n'
Path(__file__).with_name('check_sturm_endpoint_output.json').write_text(output)
print(output,end='')
