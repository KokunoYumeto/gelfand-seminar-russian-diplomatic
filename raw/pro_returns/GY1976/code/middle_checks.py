"""Exact, reproducible critical checks; no novel mathematical result claimed."""
import sympy as s
import json
from pathlib import Path
t,z,D,xi=s.symbols('t z D xi')
a,d=s.symbols('a d',nonzero=True)
standard=a/d
first=d/a
Q=t**3*z**2*D**4+2*t*z*D**2+t**2+z**4
n1=lambda q:s.diff(q,t)+q*z
n2=lambda q:s.diff(q,z)+q*t
comm=s.expand(n1(n2(Q))-n2(n1(Q)))
assert comm==0
assert s.diff(t,t)-s.diff(z,z)==0
assert s.diff(t,t)+s.diff(z,z)==2
mu2=2*(s.sinh(2*xi)-s.sin(2*xi))/(s.cosh(2*xi)+s.cos(2*xi)-2)
pole=s.limit(xi*mu2,xi,0)
vpole=s.limit(xi**2*(-4*s.diff(mu2,xi)),xi,0)
assert pole==4 and vpole==16
out={
 'purpose':'Elementary critical annotation; no novelty or class C/D development claimed',
 'berezinian_diagonal':{'standard':str(standard),'first_notebook_formula':str(first),'values_at_a2_d3':[str(standard.subs({a:2,d:3})),str(first.subs({a:2,d:3}))]},
 'flatness_scalar_counterexample':{'B':'Q[t,z]','d':'0','M':'B[D]','P':'z','L':'t','test_polynomial':str(Q),'connection_commutator':str(comm),'correct_derivative_difference':0,'notebook_derivative_sum':2,'bracket':0},
 'notebook_pulse_at_singular_time':{'limit_xi_mu2':str(pole),'limit_xi_squared_v':str(vpole)},
 'lax_independent_audit':'See critical_checks.py and its saved output, supplied by the root author via two independent methods.'
}
p=Path(__file__).with_name('middle_checks_output.json');p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
