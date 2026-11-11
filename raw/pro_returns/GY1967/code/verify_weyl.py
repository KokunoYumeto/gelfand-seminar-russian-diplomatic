"""Exact finite checks for the accompanying proved Weyl-division-ring special case.

The proof is in GY1967_development.tex. These calculations check conventions,
ordering, inverses and selected examples; they do not prove a universal theorem.
Requires Python 3 and SymPy. Run from the archive root:
    python code/verify_weyl.py
"""
from pathlib import Path
import json
import sympy as s

q=s.symbols('q')
counts={}
def check_zero(value, family):
    reduced=s.cancel(value)
    assert reduced == 0, (family, reduced)
    counts[family]=counts.get(family,0)+1

def mul(left,right,minimum=-12):
    """Truncated generalized-Leibniz product, coefficients left of p powers."""
    out={}
    for i,a in left.items():
        for j,b in right.items():
            for k in range(max(0,i+j-minimum+1)):
                d=i+j-k
                out[d]=out.get(d,0)+s.binomial(i,k)*a*s.diff(b,q,k)
    return {j:s.cancel(a) for j,a in out.items() if s.cancel(a)!=0}

for j in range(-5,6):
    left=mul({j:s.Integer(1)},{0:q})
    right=mul({0:q},{j:s.Integer(1)})
    for power in set(left)|set(right)|{j-1}:
        expected=s.Integer(j) if power==j-1 else s.Integer(0)
        check_zero(left.get(power,0)-right.get(power,0)-expected,
                   'formal_commutator_coefficients')

print('Formal commutator checks passed.', flush=True)

thetas=[q,2*q+3,-1/q,(2*q+1)/(q+1),(q-2)/(3*q+1)]
inverses=[q,(q-3)/2,-1/q,(1-q)/(q-2),(q+2)/(1-3*q)]
shears=[s.Integer(0),q**2,1/q,(q+1)/(q**2+1),q-1/(q-2)]
tests=[s.Integer(1),q,q**2,1/q,(q+2)/(q**2+3)]
records=[]
for theta,psi in zip(thetas,inverses):
    check_zero(theta.subs(q,psi)-q,'mobius_inverse_substitutions')
    check_zero(psi.subs(q,theta)-q,'mobius_inverse_substitutions')
    a=1/s.diff(theta,q)
    b=1/s.diff(psi,q)
    for r in shears:
        inv_shear=-b*r.subs(q,psi)
        # phi_theta,r after its proposed inverse: left-normal coefficients.
        check_zero(b.subs(q,theta)*a-1,'inverse_left_p_coefficient')
        check_zero(b.subs(q,theta)*r+inv_shear.subs(q,theta),
                   'inverse_left_constant_coefficient')
        # Reverse order, independently reduced.
        check_zero(a.subs(q,psi)*b-1,'inverse_right_p_coefficient')
        check_zero(a.subs(q,psi)*inv_shear+r.subs(q,psi),
                   'inverse_right_constant_coefficient')
        def P(f): return a*s.diff(f,q)+r*f
        for f in tests:
            check_zero(P(theta*f)-theta*P(f)-f,
                       'differential_operator_commutator_on_rational_tests')
        # Independently check the conjugation action of the zero-shear section.
        check_zero(b.subs(q,theta)*r.subs(q,theta)
                   -s.diff(theta,q)*r.subs(q,theta),
                   'section_conjugation_coefficient')
        records.append({'theta':str(theta),'shear':str(r),'inverse_coordinate':str(psi),
                        'inverse_shear':str(s.cancel(inv_shear))})

print('Möbius/shear and operator checks passed.', flush=True)

# Different finite parameters for the binomial identity used in associativity.
for i in [-4,-1,0,1,3]:
    for j in [-3,0,2]:
        for u in range(4):
            for v in range(4):
                lhs=sum(s.binomial(j,t)*s.binomial(i,u+v-t)*s.binomial(u+v-t,u)
                        for t in range(v+1))
                rhs=s.binomial(i,u)*s.binomial(i+j-u,v)
                check_zero(lhs-rhs,'generalized_vandermonde_finite_checks')

result={'sympy_version':s.__version__,'status':'all exact checks passed',
        'total_assertions':sum(counts.values()),'counts':counts,
        'parameters':records,
        'limitation':'Finite exact checks only. Universal assertions rest on the complete proofs.'}
out=Path(__file__).resolve().parents[1]/'audit/verify_weyl_output.json'
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='parameters'},indent=2))
