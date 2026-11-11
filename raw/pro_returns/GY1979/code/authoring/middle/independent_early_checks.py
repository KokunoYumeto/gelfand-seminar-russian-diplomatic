"""Independent review calculations; never rewrites the early agent's outputs.

The oscillatory integral uses a saddle-centered finite interval, with an analytic
bound on the discarded contour tails. Quadrature itself is not interval certified.
The sphere value is derived separately from its spectral Hurwitz-zeta expansion.
"""
from pathlib import Path
from fractions import Fraction as F
import mpmath as mp
import json
p=Path(__file__).resolve().parent
mp.mp.dps=85
b=mp.mpf(1000); r=mp.root(b/4,3); theta=3*mp.sqrt(3)*r**4/2
base=-3*r**4/2
# z = sqrt(3)*r/2 + y/r + i*r/2, on the positive half of the contour.
def local(y):
    return mp.exp(-3*(1+1j*mp.sqrt(3))*y*y
                  -2*(mp.sqrt(3)+1j)*y**3/r**2-y**4/r**4)
Y=mp.mpf(14)
z=mp.quad(local,[-Y,-4,-1,0,1,4,Y])
scaled=2*mp.re(mp.exp(1j*theta)*z)/r
# On t>=0, |scaled integrand|<=exp(-3*y^2/4). Include both tails and factor2/r.
tail=(4/r)*mp.sqrt(mp.pi)/(2*mp.sqrt(mp.mpf(3)/4))*mp.erfc(mp.sqrt(mp.mpf(3)/4)*Y)
original=json.loads((p.parent/'early'/'annotation_checks.json').read_text())
reported=mp.mpf(original['oscillatory_quartic'][1]['scaled_integral'])
psi=theta-mp.pi/6
lead=mp.sqrt(2*mp.pi/3)/r*mp.cos(psi)
first=mp.sqrt(2*mp.pi/3)/r*(mp.cos(psi)+mp.mpf(7)/(144*r**4)*mp.cos(psi-2*mp.pi/3))
# Finite Taylor approximation, with global Lagrange-remainder integral bound.
a=mp.mpf(1000); N=12
terms=[(-1)**k*mp.gamma(mp.mpf(2*k+1)/4)/(2*mp.factorial(2*k)*a**(mp.mpf(2*k+1)/4)) for k in range(N+1)]
narrow=mp.fsum(terms)
narrow_remainder=mp.gamma(mp.mpf(2*N+3)/4)/(2*mp.factorial(2*N+2)*a**(mp.mpf(2*N+3)/4))
# Original DS expression, independently evaluated with exact integer vectors.
def ds(points):
    a,b,c,d=points
    num=lambda v:v[0]**2-v[1]**2
    norm=lambda v:v[0]**2+v[1]**2
    sub=lambda u,v:tuple(x-y for x,y in zip(u,v))
    add=lambda u,v:tuple(x+y for x,y in zip(u,v))
    left=F(num(sub(a,c)),norm(sub(a,c)))
    right=F(num(sub(b,d)),norm(add(b,d)))
    return {'momentum_residual':list(sub(add(a,b),add(c,d))),
            'energy_residual':-num(a)-num(b)+num(c)+num(d),
            'first_fraction':str(left),'second_fraction':str(right),'sum':str(left+right)}
# For S4, eigenvalues l(l+3), multiplicity (l+1)(l+2)(2l+3)/6, l>=1.
# Set q=5/2. Only k=1,2 contribute extra pole terms at s=0 in the binomial expansion.
q=F(5,2)
B2=q*q-q+F(1,6)
B4=q**4-2*q**3+q*q-F(1,30)
hz_minus1=-B2/2; hz_minus3=-B4/4
zeta0=(hz_minus3-hz_minus1/4+F(81,64)-F(9,32))/3
assert zeta0==F(-61,90)
out={
 'check_date':'2026-11-10',
 'quartic':{'scaled_integral':mp.nstr(scaled,75),'integral':mp.nstr(scaled*mp.exp(base),65),
             'difference_from_early_105dps_rescaled':mp.nstr(abs(scaled-reported),12),
             'rigorous_discarded_tail_bound_in_rescaled_integral':mp.nstr(tail,12),
             'quadrature_is_interval_certified':False,
             'leading_rescaled':mp.nstr(lead,35),'one_correction_rescaled':mp.nstr(first,35),
             'relative_error_leading':mp.nstr(abs((lead-scaled)/scaled),15)},
 'narrow_quartic':{'terms':N+1,'finite_sum':mp.nstr(narrow,65),
                   'analytic_taylor_remainder_bound':mp.nstr(narrow_remainder,12)},
 'ds_original_example':ds([(1,0),(0,1),(0,0),(1,1)]),
 'ds_all_nonzero_example':ds([(2,2),(1,3),(1,2),(2,3)]),
 'sphere4_spectral_derivation':{'hurwitz_zeta_minus1_q5over2':str(hz_minus1),
                 'hurwitz_zeta_minus3_q5over2':str(hz_minus3),
                 'positive_spectrum_zeta_at_zero':str(zeta0),'heat_B4':str(zeta0+1)}
}
(p/'independent_early_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
