"""Exact independent checks for the massive-Dirac negative-cut example."""
from pathlib import Path
import json
import sympy as sp
I=sp.I
pauli=[sp.Matrix([[0,1],[1,0]]),sp.Matrix([[0,-I],[I,0]]),sp.diag(1,-1)]
alpha=[sp.kronecker_product(pauli[0],q) for q in pauli]
beta=sp.kronecker_product(pauli[2],sp.eye(2))
gammas=alpha+[beta]
for a in gammas:assert a.H==a
checks=0
for i,a in enumerate(gammas):
 for j,b in enumerate(gammas):
  assert a*b+b*a==(2*sp.eye(4) if i==j else sp.zeros(4));checks+=1
k=sp.symbols('k1 k2 k3',real=True);mu=sp.Symbol('mu',positive=True);lam=sp.Symbol('lambda');s=sp.Symbol('s');t=sp.Symbol('t',positive=True)
p=sum((g*q for g,q in zip(alpha,k)),sp.zeros(4))+mu*beta
squared=sum(q*q for q in k)+mu*mu
assert p.H==p
assert sp.simplify(p*p-squared*sp.eye(4))==sp.zeros(4)
assert sp.trace(p)==0
expected=(lam**2-squared)**2
assert sp.expand(p.charpoly(lam).as_expr()-expected)==0
leading=4*sp.pi**sp.Rational(3,2)
volume=(2*sp.pi)**3
assert sp.simplify(4*volume/(4*sp.pi)**sp.Rational(3,2)-leading)==0
coefficient=sp.expand(sp.series(sp.exp(-mu**2*t),t,0,3).removeO()).coeff(t,2)
a=sp.simplify(leading*coefficient)
residue=sp.simplify(2*a/sp.gamma(-sp.Rational(1,2)))
assert residue==-2*sp.pi*mu**4
regular_constant=sp.Symbol('regular_constant')
cut_plus=sp.simplify(sp.limit((1+sp.exp(-I*sp.pi*s))/2*(residue/(s+1)+regular_constant),s,-1))
cut_minus=sp.simplify(sp.limit((1+sp.exp(I*sp.pi*s))/2*(residue/(s+1)+regular_constant),s,-1))
assert cut_plus==-I*sp.pi**2*mu**4
assert cut_minus==I*sp.pi**2*mu**4
report={
 'clifford_anticommutator_checks':checks,
 'hermitian_matrices':True,
 'operator_square':str(squared)+' times I_4',
 'characteristic_polynomial':str(expected),
 'independent_volume_normalization':str(leading),
 'heat_t_half_coefficient':str(a),
 'absolute_zeta_residue_at_minus_one':str(residue),
 'Z_plus_negative_eigenvalue_argument':'+pi',
 'Z_plus_branch_interval':'(-pi/2, 3pi/2)',
 'Z_plus_value_at_minus_one':str(cut_plus),
 'Z_minus_negative_eigenvalue_argument':'-pi',
 'Z_minus_branch_interval':'(-3pi/2, pi/2)',
 'Z_minus_value_at_minus_one':str(cut_minus),
 'difference_Z_plus_minus_Z_minus':str(sp.simplify(cut_plus-cut_minus)),
 'regular_part_cancels':True,
}
p=Path(__file__).with_name('negative_cut_output.json');p.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
