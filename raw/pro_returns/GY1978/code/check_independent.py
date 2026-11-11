"""Independent exact checks for the GY1978 critical annotations.

The spin-one calculation uses permutation and contraction, not skew generators.
The Gaussian checks compare an ODE coefficient recurrence with integration by parts.
Finite numerical tests are explicitly not proofs for every argument or order.
"""
import itertools
import sympy as s
import mpmath as mp

def comm(a,b): return a*b-b*a
N=3
P=s.zeros(N*N); K=s.zeros(N*N)
for i,j in itertools.product(range(N),repeat=2):
    P[N*i+j,N*j+i]=1
    for k in range(N):
        K[N*i+i,N*k+k]=1
assert P*P==s.eye(9) and K*K==3*K and P*K==K and K*P==K
t=s.symbols('t')
# X=K-P for the real skew SO(3) generators; h=X^2+tX.
X=K-P
h=s.eye(9)+(1+t)*K-t*P
assert h==X*X+t*X
A=s.kronecker_product(h,s.eye(3)); B=s.kronecker_product(s.eye(3),h)
C=comm(A+B,comm(A,B))
idx=lambda a,b,c:9*a+3*b+c
row,col=idx(0,0,1),idx(2,1,2)
w=s.factor(C[row,col])
print('SPIN-ONE: independent permutation/contraction representation')
print('X eigenvalues (multiplicity):',X.eigenvals())
print('C[001,212] =',w)
assert w==t*(t-1)*(t+1)
for v in [-3,-2,-1,0,1,2,3]:
    direct=comm(A.subs(t,v)+B.subs(t,v),comm(A.subs(t,v),B.subs(t,v)))[row,col]
    assert direct==w.subs(t,v)
    print('t =',v,'witness =',direct)
print('For arbitrary K23-K12 this entry is zero: first and third site both change.')
print('At notebook t=-2 the witness is -6: regular difference-form R is excluded.')
print('Zeros at t=-1,0,1 alone are not a sufficiency assertion.')

x,y,z=s.symbols('x y z')
def bracket(f,g,sign):
    Xf=s.diff(f,x); Xg=s.diff(g,x)
    Yf=s.diff(f,y)+sign*x*s.diff(f,z)
    Yg=s.diff(g,y)+sign*x*s.diff(g,z)
    return s.expand(f*s.diff(g,z)-g*s.diff(f,z)+Xf*Yg-Xg*Yf)
def jac(f,g,h,sign):
    return s.expand(bracket(f,bracket(g,h,sign),sign)+bracket(g,bracket(h,f,sign),sign)+bracket(h,bracket(f,g,sign),sign))
print('\nCONTACT BRACKET: nested convention [f,[g,h]] + cyclic')
for sig in [1,-1]:
    vals=[bracket(x,y,sig),bracket(y,z,sig),bracket(z,x,sig)]
    print('Y=dy'+('+' if sig==1 else '-')+'x dz:', vals,'Jacobi(x,y,z)=',jac(x,y,z,sig))
assert jac(x,y,z,1)==2 and jac(x,y,z,-1)==0
triples=[(x,y,z),(x*x,y*z,z*z+x),(1+x*y,1+y*z,1+z*x)]
for f,g,g3 in triples:
    determinant=s.det(s.Matrix([[s.diff(q,u) for u in [x,y,z]] for q in [f,g,g3]]))
    assert s.simplify(jac(f,g,g3,1)-2*determinant)==0
    assert jac(f,g,g3,-1)==0
print('Three distinct polynomial triples checked: plus defect=2 det(gradients), minus defect=0.')

print('\nGAUSSIAN TAIL: exact symbolic coefficient checks')
xx=s.symbols('x',positive=True)
coeff=[s.Integer(1)]
for n in range(1,11): coeff.append(-s.Rational(2*n-1,2)*coeff[-1])
for n,c in enumerate(coeff):
    assert c==(-1)**n*s.factorial2(2*n-1)/2**n
print('c_n for n=0..6 in e^(-x^2)/(2x) sum c_n x^(-2n):',coeff[:7])
for n in range(1,9):
    f=s.exp(-xx**2)/(2*xx)*sum(coeff[k]*xx**(-2*k) for k in range(n))
    residual=s.simplify((s.diff(f,xx)+s.exp(-xx**2))/s.exp(-xx**2))
    expected=(-1)**n*s.factorial2(2*n-1)/(2**n*xx**(2*n))
    assert s.simplify(residual-expected)==0
print('Truncated ODE residual equals (-1)^N (2N-1)!!/(2^N x^(2N)), N=1..8.')
# The global remainder proof is mathematical in critical_checks.tex.
mp.mp.dps=80
for v in [mp.mpf(1),mp.mpf(2),mp.mpf(4),mp.mpf('7.5')]:
    exact=mp.sqrt(mp.pi)*mp.erfc(v)/2
    for n in [1,2,3,5,8]:
        approx=mp.exp(-v*v)/(2*v)*sum(mp.mpf(int(s.numer(coeff[k])))/int(s.denom(coeff[k]))/v**(2*k) for k in range(n))
        rem=exact-approx
        bound=mp.exp(-v*v)/(2*v)*mp.mpf(int(s.factorial2(2*n-1)))/(2**n*v**(2*n))
        assert (-1)**n*rem>0 and abs(rem)<bound
    print('x=',mp.nstr(v,5),'N={1,2,3,5,8}: signed next-term bounds verified at 80 digits.')
print('\nAREA COUNTEREXAMPLE: exact boundary flux')
theta=s.symbols('theta',real=True)
epsilon,delta=s.symbols('epsilon delta',real=True)
curve=[s.cos(theta),s.sin(theta),epsilon*s.cos(2*theta),s.Integer(0)]
areas={}
for i,j in itertools.combinations(range(4),2):
    areas[i,j]=s.simplify(s.integrate((curve[i]*s.diff(curve[j],theta)-curve[j]*s.diff(curve[i],theta))/2,(theta,0,2*s.pi)))
assert areas[0,1]==s.pi and all(v==0 for k,v in areas.items() if k!=(0,1))
flux_extra=s.simplify(s.integrate(curve[0]*curve[1]*s.diff(curve[2],theta),(theta,0,2*s.pi)))
assert flux_extra==-s.pi*epsilon
flux=s.pi-delta*flux_extra
assert s.simplify(flux-s.pi*(1+delta*epsilon))==0
bound=s.simplify(flux.subs(delta,epsilon)/s.sqrt(1+epsilon**2))
assert s.simplify(bound-s.pi*s.sqrt(1+epsilon**2))==0
print('Oriented coordinate areas:',areas)
print('Integral of xy dz:',flux_extra)
print('Calibrated lower bound on spanning area:',bound)
omega_matrix=s.Matrix([[0,1,-delta*y,0],[-1,0,-delta*x,0],[delta*y,delta*x,0,0],[0,0,0,0]])
lam=s.symbols('lambda')
assert s.factor(omega_matrix.charpoly(lam).as_expr())==lam**2*(lam**2+delta**2*x**2+delta**2*y**2+1)
print('Skew-form characteristic polynomial: lambda^2(lambda^2+1+delta^2(x^2+y^2)).')
print('For every nonzero real epsilon this exceeds pi; proof of comass and clipping is in the chapter.')
print('\nPERIOD-THREE LIE BRACKET: independent two-by-two loop representation')
H=s.diag(1,-1); E=s.Matrix([[0,1],[0,0]]); F=s.Matrix([[0,0],[1,0]])
def loop_basis(n):
    q,r=divmod(n,3)
    return (H/2,q) if r==0 else ((E,q) if r==1 else (F/2,q+1))
def coefficient(i,j):
    r=(j-i)%3
    return {0:0,1:1,2:-1}[r]
for i,j in itertools.product(range(-12,13),repeat=2):
    Ai,ki=loop_basis(i); Aj,kj=loop_basis(j); Ak,kk=loop_basis(i+j)
    lhs=Ai*Aj-Aj*Ai; rhs=coefficient(i,j)*Ak
    assert lhs==rhs
    if lhs!=s.zeros(2):assert ki+kj==kk
print('All 625 ordered pairs with indices -12..12 obey the notebook residue rule.')
print('Proof for all indices reduces to the nine residue-class pairs and exponent addition.')
print('Evaluation z=1 has a nonzero proper ideal; the loop algebra is not ungraded simple.')
print('All exact assertions passed; numerical checks are finite corroboration only.')
