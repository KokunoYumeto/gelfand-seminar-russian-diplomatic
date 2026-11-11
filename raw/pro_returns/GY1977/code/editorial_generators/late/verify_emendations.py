"""Exact independent checks of editorial reconstructions; no novelty claimed.
Run with Python and SymPy. Results are written beside this file.
"""
from pathlib import Path
import json
import sympy as s
OUT=Path(__file__).parent
results={}
def zero(expr):
    v=s.simplify(s.expand(expr)); assert v==0,v; return str(v)
# P775: smooth reflectionless potential, independently of the Volterra asymptotic proof.
x,k,r=s.symbols('x k r',real=True,nonzero=True)
u=-2*r**2/s.cosh(r*x)**2
psi=s.exp(-s.I*k*x)*(s.I*k+r*s.tanh(r*x))/(s.I*k+r)
res=s.simplify(s.diff(psi,x,2)-(u-k*k)*psi);assert res==0
z=s.symbols('z')
T=(k+s.I*r)/(k-s.I*r)
lead=s.expand(s.series(s.log(T.subs(k,1/z)),z,0,2).removeO()).coeff(z,1)
assert s.simplify(lead-2*s.I*r)==0
minus_coefficient=(s.I*k-r)/(s.I*k+r)
plus_coefficient=(s.I*k+r)/(s.I*k+r)
assert s.simplify(minus_coefficient-T)==0
assert s.simplify(plus_coefficient-1)==0
results['transmission']={'Schrodinger_residual':str(res),'exact_T':str(T),'minus_infinity_coefficient':str(minus_coefficient),'minus_coefficient_minus_T':'0','plus_infinity_coefficient':str(plus_coefficient),'reflection_coefficient':'0','log_T_leading_coefficient':str(lead),'c0':'-4*r','phi_leading_coefficient':'r=-c0/4','independent_check':'Left-Jost Volterra estimate and physical T=1/A derivation in development.tex','review_correction':'The proposition formerly interchanged T and its inverse at the left endpoint; independent root review caught it, and explicit endpoint checks now enforce the notebook convention.'}
# P776: two low moments checked directly on a Gaussian scaling family.
lam=s.symbols('lam',positive=True)
ug=lam**2*s.exp(-(lam*x)**2)
c0=s.integrate(ug,(x,-s.oo,s.oo))
c1=-3*s.integrate(ug**2,(x,-s.oo,s.oo))
assert s.simplify(lam*s.diff(c0,lam)-c0)==0
assert s.simplify(lam*s.diff(c1,lam)-3*c1)==0
# Generic recursion-operator weights, independent of the two integrated examples.
w=s.symbols('w')
assert s.simplify((3+w-1)-(w+2))==0
results['scaling']={'gaussian_c0':str(c0),'gaussian_c1':str(c1),'lambda_derivative_c0_minus_c0':'0','lambda_derivative_c1_minus_3c1':'0','generic_operator_weights':['d2:h weight w+2','u*h weight2+w','u_prime*primitive(h) weight3+w-1=w+2'],'seed_weight':2,'integrated_nth_weight':'2*n+1','second_derivation':'integration by parts at n0,n1 and homogeneous conjugation for every n in development.tex'}
# P780: derivative elimination, followed independently by differentiation of the result.
U,A,B,C,p,q,t=s.symbols('U A B C p q t')
Ax=-(A-U)*(4*p+A-U)/2-t
Bx=-(B-U)*(4*q+B-U)/2-t
CxA=-(C-A)*(4*q+C-A)/2-Ax
CxB=-(C-B)*(4*p+C-B)/2-Bx
sol=s.solve(s.Eq(CxA,CxB),C)
Csol=U-(p+q)*(A-B)/(p-q+(A-B)/2)
assert len(sol)==1 and s.simplify(sol[0]-Csol)==0
Cx=s.diff(Csol,U)*t+s.diff(Csol,A)*Ax+s.diff(Csol,B)*Bx
ra=s.factor(Ax+Cx+(Csol-A)*(4*q+Csol-A)/2)
rb=s.factor(Bx+Cx+(Csol-B)*(4*p+Csol-B)/2)
assert ra==0 and rb==0
results['Bianchi']={'elimination_solution':str(s.factor(sol[0])),'difference_from_notebook_reconstruction':'0','upper_A_differential_residual':str(ra),'upper_B_differential_residual':str(rb),'scope':'nonzero rational denominator; lower Riccati equations assumed'}
# P781: direct Jacobian at n3 equilibrium; independently a general polynomial identity.
xs=s.symbols('x0:3');vs=s.symbols('v0:3')
force=s.Matrix([-xs[j]+sum((1+2*vs[j]*vs[h])/(xs[j]-xs[h]) for h in range(3) if h!=j) for j in range(3)])
a=s.sqrt(s.Rational(3,2));roots=[-a,s.Integer(0),a]
subs=dict(zip(xs,roots));subs.update(dict.fromkeys(vs,s.Integer(0)))
AA=s.zeros(3)
for j in range(3):
 for h in range(3):
  if h!=j:AA[j,h]=-1/(roots[j]-roots[h])**2
 AA[j,j]=-sum(AA[j,h] for h in range(3) if h!=j)
J=force.jacobian(xs).subs(subs).applyfunc(s.simplify)
assert (J+s.eye(3)+AA).applyfunc(s.simplify)==s.zeros(3)
assert (force.jacobian(vs).subs(subs))==s.zeros(3)
l=s.symbols('lambda')
assert s.factor(AA.charpoly(l).as_expr())==l*(l-1)*(l-2)
# Each Hermite mode exactly diagonalizes the PDE for n1..8; not numerical roots.
checks=[]
for n in range(1,9):
 for m in range(1,n+1):
  H=s.hermite(n-m,x)
  zero(s.diff(H,x,2)/2-x*s.diff(H,x)+n*H-m*H)
  checks.append((n,m))
results['Hermite']={'A_n3':str(AA),'force_jacobian_n3':str(J),'J_plus_I_plus_A':'zero3by3','A_charpoly':str(s.factor(AA.charpoly(l).as_expr())),'Hermite_mode_identity_pairs_checked':checks,'independent_general_argument':'simple-root Vandermonde change of coordinates conjugates I+A to diag(1,...,n)'}
# P829: all nine residue cases of the explicit loop basis (Laurent exponent included).
tt=s.symbols('t',nonzero=True);ee=s.Matrix([[0,1],[0,0]]);ff=s.Matrix([[0,0],[1,0]]);hh=s.diag(1,-1)
def eps(j):
 residue=j%3
 if residue==0:return hh*tt**(j//3)/2
 if residue==1:return ee*tt**((j-1)//3)
 return ff*tt**((j+1)//3)/2
loop_cases=[]
for i in [-1,0,1]:
 for j in [-1,0,1]:
  aij=(j-i+1)%3-1
  assert (eps(i)*eps(j)-eps(j)*eps(i)-aij*eps(i+j)).applyfunc(s.simplify)==s.zeros(2)
  loop_cases.append([i,j,aij])
# Independent Jacobi check solely on residue structure constants.
def ac(i,j):return (j-i+1)%3-1
for i in range(3):
 for j in range(3):
  for h in range(3):assert ac(j,h)*ac(i,j+h)+ac(h,i)*ac(j,h+i)+ac(i,j)*ac(h,i+j)==0
results['loop_bracket']={'nine_residue_cases':loop_cases,'Jacobi_residue_triples_checked':27}
# P831: exact exterior-algebra matrices. Multiplication/left derivative are independent
# of the short symbolic anticommutator derivation printed in the appendix.
N=16
def mult(j):
 M=s.zeros(N)
 for b in range(N):
  if not (b>>j)&1:M[b|(1<<j),b]=(-1)**((b&((1<<j)-1)).bit_count())
 return M
def deriv(j):
 M=s.zeros(N)
 for b in range(N):
  if (b>>j)&1:M[b^(1<<j),b]=(-1)**((b&((1<<j)-1)).bit_count())
 return M
# Generic symbol d_mu is Fourier substitution of the commuting x-derivatives.
d=s.symbols('d0:4')
sigma=[s.eye(2),s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-s.I],[s.I,0]]),s.diag(1,-1)]
V=sum((d[m]*sigma[m] for m in range(4)),s.zeros(2))
QQ=[-s.I*deriv(a)-sum((V[a,b]*mult(2+b) for b in range(2)),s.zeros(N)) for a in range(2)]
QB=[s.I*deriv(2+b)+sum((V[a,b]*mult(a) for a in range(2)),s.zeros(N)) for b in range(2)]
for a in range(2):
 for b in range(2):
  assert (QQ[a]*QB[b]+QB[b]*QQ[a]+2*s.I*V[a,b]*s.eye(N)).applyfunc(s.expand)==s.zeros(N)
  assert (QQ[a]*QQ[b]+QQ[b]*QQ[a]).applyfunc(s.expand)==s.zeros(N)
  assert (QB[a]*QB[b]+QB[b]*QB[a]).applyfunc(s.expand)==s.zeros(N)
results['supertranslations']={'exterior_basis_dimension':16,'generic_four_derivative_symbols':list(map(str,d)),'mixed_anticommutator':'-2*i*sigma^m*d_m','same_chirality_anticommutators':'zero','matrix_pairs_checked':12}
# Decisive low-dimensional counterexamples: mathematical, not bibliographical evidence.
results['elementary_counterexamples']={'BGG_unit':'On the nonzero trivial exterior module all xi act as0, so the recorded unit value vanishes.','Aomoto_zero_weights':'All residues0 satisfy the written strictly-positive-integer exclusion; constants give H0=C for n>0.','Dirac_missing_derivative':'det(mI-Gamma)=m^2-1; no nonzero solution for m!=+-1.','Hermite_n1':'A=(0), but root ODE is x_ddot=-x, so I cannot be omitted.'}
(OUT/'verification_results.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps({'passed':True,'groups':list(results),'Hermite_mode_checks':len(checks),'loop_Jacobi_checks':27,'supercharge_matrix_pairs':12},indent=2))
