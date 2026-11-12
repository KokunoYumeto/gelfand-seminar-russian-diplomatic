"""Audit the naive permutation-only stationary formula for a two-source U(3) integral."""
from itertools import permutations
from math import factorial
import sympy as s
from check_unitary_integral import moment

P=s.Matrix([[0,0],[1,0],[0,1]])
Q=s.Matrix([[0,0],[2,1],[1,3]])
A=P*Q.T
print('Rows of P are the two-component p_i:',P)
print('Rows of Q are the two-component q_j:',Q)
print('A_ij=p_i dot q_j:',A)
data=[]
for perm in permutations(range(3)):
    S=sum(A[i,perm[i]] for i in range(3))
    D=s.prod(A[i,perm[i]]+A[j,perm[j]]-A[i,perm[j]]-A[j,perm[i]] for i in range(3) for j in range(i+1,3))
    print('permutation',perm,'action',S,'quadratic denominator',D)
    assert D != 0
    data.append((S,D))
    # Independently check each factor by differentiating the phase along a
    # real Givens rotation, a valid one-parameter subgroup of U(3).
    theta=s.symbols('theta',real=True)
    permutation_matrix=s.zeros(3)
    for row,column in enumerate(perm):
        permutation_matrix[row,column]=1
    for i in range(3):
        for j in range(i+1,3):
            R=s.eye(3)
            R[i,i]=R[j,j]=s.cos(theta)
            R[i,j]=-s.sin(theta);R[j,i]=s.sin(theta)
            U=R*permutation_matrix
            phase=sum(A[row,column]*U[row,column]**2 for row in range(3) for column in range(3))
            curvature=-s.diff(phase,theta,2).subs(theta,0)/2
            factor=A[i,perm[i]]+A[j,perm[j]]-A[i,perm[j]]-A[j,perm[i]]
            assert s.simplify(curvature-factor)==0
coefficients=[s.factor(2*sum(S**k/(s.Integer(factorial(k))*D) for S,D in data)) for k in range(7)]
print('Coefficients of t^(-3),t^(-2),...,t^3 in naive stationary formula:',coefficients)
print('Exact integral is entire with value 1 at t=0.')
print('Independent Givens-rotation checks of all 18 quadratic factors: PASS')
print('Exact Haar moments m=0..3 from Gram pseudoinverse:',[moment(A,m) for m in range(4)])
if coefficients[:3] != [0,0,0] or coefficients[3] != 1:
    print('FAILS as an exact finite fixed-point formula: pole or wrong zero-coupling value.')
else:
    print('Leading cancellation is sufficient through t^0; compare later moments.')
