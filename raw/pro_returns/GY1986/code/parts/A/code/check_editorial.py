#!/usr/bin/env python3
"""Exact checks of three editorial formula corrections (not novelty claims).

Requires sympy. Each symbolic calculation has an independent check or explicit
nondegenerate parameter tests. These are verification of manuscript emendations,
not evidence for an unproved general representation-theoretic claim.
"""
import json
from pathlib import Path
import sympy as s

OUT=Path(__file__).resolve().parents[1]
results={}

# 1986-671.5: solve both winding conditions over the real numbers.
a,b,x,y,L1,L2=s.symbols('a b x y L1 L2',real=True)
tau=a+s.I*b
z=x+s.I*y
expr=((L1-s.conjugate(tau)*L2)*z-(L1-tau*L2)*s.conjugate(z))/(2*s.I*b)
real_expr=s.simplify(s.expand(expr))
shift_one=s.simplify(real_expr.subs(x,x+1)-real_expr)
shift_tau=s.simplify(real_expr.subs({x:x+a,y:y+b},simultaneous=True)-real_expr)
assert shift_one==L2 and shift_tau==L1
assert s.simplify(s.im(real_expr))==0
# Independent coordinates z=u+v*tau solve the period problem directly.
u,v=s.symbols('u v',real=True)
assert s.simplify(real_expr.subs({x:u+v*a,y:v*b},simultaneous=True)-(u*L2+v*L1))==0
results['winding']={'real_expression':str(real_expr),'unit_shift':str(shift_one),
 'tau_shift':str(shift_tau),'independent_lattice_coordinates':'u*L2+v*L1',
 'assumption':'b=Im(tau)>0, L1,L2 real','status':'passed'}

# 1986-678.3: exact rank-one antisymmetrizer computation.
a11,a12,a21,a22,b11,b12,b21,b22=s.symbols('a11 a12 a21 a22 b11 b12 b21 b22')
A=s.Matrix([[a11,a12],[a21,a22]])
B=s.Matrix([[b11,b12],[b21,b22]])
flip=s.Matrix([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
P=(s.eye(4)-flip)/2
M=s.kronecker_product(A,B)
c=(a11*b22+a22*b11-a12*b21-a21*b12)/2
assert (P*M*P-c*P).applyfunc(s.expand)==s.zeros(4)
# Independent rank-one trace extracts the scalar without another sandwich.
assert s.expand(s.trace(P*M)-c)==0
identity_sub={a11:1,a12:0,a21:0,a22:1,b11:1,b12:0,b21:0,b22:1}
assert c.subs(identity_sub)==1
results['antisymmetrizer']={'scalar':str(c),'independent_check':'trace(P*(A tensor B))',
 'identity_case':'1; the manuscript coefficient 1/4 instead gives 1/2','status':'passed'}

# 1986-681.5: polynomial reduction in the rank-two finite Hecke algebra.
T,q=s.symbols('T q')
rel=T*T-(q-1)*T-q
Tinv=(T-(q-1))/q
correct=s.rem(q*Tinv**2,rel,T)
wrong=q*T*T
correct_residual=s.factor(s.rem(correct*T-(T-(q-1)),rel,T))
wrong_residual=s.factor(s.rem(wrong*T-(T-(q-1)),rel,T))
assert correct_residual==0 and wrong_residual!=0
# Independent two-dimensional regular representation for several q values.
parameters=[s.Integer(2),s.Integer(-2),s.Rational(3,2)]
checks=[]
for val in parameters:
    mat=s.Matrix([[0,val],[1,val-1]])
    assert mat**2==(val-1)*mat+val*s.eye(2)
    X=val*(mat.inv()**2)
    assert X*mat==mat-(val-1)*s.eye(2)
    assert val*(mat**2)*mat!=mat-(val-1)*s.eye(2)
    checks.append(str(val))
results['hecke_evaluation']={'correct_reduced_X':str(s.factor(correct)),
 'correct_exchange_residual':str(correct_residual),'positive_square_residual':str(wrong_residual),
 'independent_matrix_parameters':checks,'assumption':'q nonzero, (T-q)(T+1)=0',
 'status':'passed'}

target=OUT/'evidence/editorial_checks.json'
target.write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
(OUT/'code/check_editorial.out').write_text(target.read_text())
print(json.dumps(results,ensure_ascii=False,indent=2))
