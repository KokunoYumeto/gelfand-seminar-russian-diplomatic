"""Reproducible checks for annotated GY1979 exercises, not new priority claims.

Run: python parts/early/verify_annotations.py
The oscillatory integral checks use different contour heights and precisions.
Agreement is numerical evidence, not an interval-arithmetic error certificate.
All error comparisons are made on the exponentially rescaled integral.
"""
from pathlib import Path
from fractions import Fraction
import json
import mpmath as mp

P = Path(__file__).parent

def quartic_contour(dps, height_ratio):
    with mp.workdps(dps):
        b = mp.mpf(1000)
        r = (b/4)**(mp.mpf(1)/3)
        v = mp.mpf(height_ratio)*r
        base = -3*r**4/2
        peak = mp.sqrt(3)*v
        def integrand(t):
            z = t+1j*v
            return mp.exp(-z**4+1j*b*z-base)
        # Symmetry: the negative half-line is the complex conjugate.
        # Extra subdivision resolves the width O(1/r) around the positive peak.
        knots = [mp.mpf(0), peak-mp.mpf(".5"), peak-mp.mpf(".2"),
                 peak, peak+mp.mpf(".2"), peak+mp.mpf(".5"),
                 2*r, 4*r, mp.inf]
        scaled = 2*mp.re(mp.quad(integrand,knots))
        value = scaled*mp.exp(base)
        lead_scaled = mp.sqrt(2*mp.pi/3)/r*mp.cos(
            3*mp.sqrt(3)*r**4/2-mp.pi/6)
        return {
            "dps":dps, "height_over_r":height_ratio,
            "log_scale":mp.nstr(base,dps-8),
            "scaled_integral":mp.nstr(scaled,dps-8),
            "integral":mp.nstr(value,dps-8),
            "leading_saddle_integral":mp.nstr(lead_scaled*mp.exp(base),30),
        }

rows = [quartic_contour(70,"0.5"),quartic_contour(105,"0.49")]
with mp.workdps(100):
    agreement = abs(mp.mpf(rows[0]["scaled_integral"])
                    -mp.mpf(rows[1]["scaled_integral"]))
    a = mp.mpf(1000)
    narrow_quad = 2*mp.quad(lambda x:mp.exp(-a*x**4)*mp.cos(x),
                           [0,mp.mpf(".2"),mp.mpf(".5"),1,mp.inf])
    narrow_series = mp.nsum(lambda k:(-1)**k*mp.gamma((2*k+1)/4)
                            /(2*mp.factorial(2*k)*a**((2*k+1)/4)),[0,mp.inf])
    narrow = {"quadrature":mp.nstr(narrow_quad,60),
              "gamma_series":mp.nstr(narrow_series,60),
              "difference":mp.nstr(abs(narrow_quad-narrow_series),10)}

k1,k2,k3,k4=(1,0),(0,1),(0,0),(1,1)
omega=lambda k:-k[0]**2+k[1]**2
first=Fraction((k1[0]-k3[0])**2-(k1[1]-k3[1])**2,
               (k1[0]-k3[0])**2+(k1[1]-k3[1])**2)
second=Fraction((k2[0]-k4[0])**2-(k2[1]-k4[1])**2,
                (k2[0]+k4[0])**2+(k2[1]+k4[1])**2)
ds={"momenta":[k1,k2,k3,k4],
    "momentum_residual":[k1[j]+k2[j]-k3[j]-k4[j] for j in (0,1)],
    "energy_residual":omega(k1)+omega(k2)-omega(k3)-omega(k4),
    "first_fraction":str(first),"second_fraction":str(second),"w":str(first+second),
    "w_if_only_denominator_signs_changed":str(first+1)}
assert ds["momentum_residual"]==[0,0] and ds["energy_residual"]==0
assert first+second==Fraction(6,5)
# Scalar heat coefficient on the unit round four-sphere; pi cancels exactly.
b4=Fraction(8,3)*Fraction(5*12**2-2*36+2*24,360*16)
assert b4==Fraction(29,90)
out={"scope":"Numerical contour agreement is not a certified absolute or relative error bound. The DS and heat-coefficient checks are exact rational arithmetic.",
     "oscillatory_quartic":rows,
     "difference_of_rescaled_integrals":mp.nstr(agreement,20),
     "narrow_quartic":narrow,"ds_resonant_counterexample":ds,
     "sphere4_scalar_B4":str(b4),"sphere4_scalar_zeta_zero":str(b4-1)}
(P/"annotation_checks.json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))
