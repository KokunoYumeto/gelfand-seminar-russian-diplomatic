"""Exact polynomial checks supporting the affine unit obstruction.

The impossibility of the operator embedding is proved in the chapter;
this script verifies the coordinate identity and squarefreeness only.
"""
import sympy as s
z,w,Y=s.symbols('z w Y')
F=z*w**2-z**4-1
h=z**5+z
assert s.expand(z*(w**2-z**3)-1-F)==0
assert s.expand((Y**2-h).subs(Y,z*w)-z*F)==0
assert s.gcd(h,s.diff(h,z))==1
# The ideal (F,F_z,F_w) is the whole ring, hence no affine singular point.
G=s.groebner([F,s.diff(F,z),s.diff(F,w)],w,z)
assert list(G)==[1]
print('SYMPY_VERSION',s.__version__)
print('AFFINE_EQUATION',F)
print('UNIT_IDENTITY z*(w**2-z**3)=1 modulo F: PASS')
print('BIRATIONAL_IDENTITY (Y**2-z**5-z)|Y=z*w = z*F: PASS')
print('SQUAREFREE_GCD',s.gcd(h,s.diff(h,z)))
print('SINGULAR_IDEAL_GROEBNER_BASIS',list(G))
print('BRANCH_POINTS five finite simple roots plus infinity; genus=(6-2)/2=2')
print('ALL AFFINE MODEL CHECKS PASSED')
