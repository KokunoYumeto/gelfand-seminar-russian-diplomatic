"""Exact independent checks of selected mathematical emendations in the chapter."""
from pathlib import Path
import json, math
import sympy as s

x,y,u,v,t,L=s.symbols('x y u v t L', real=True)
checks=[]
identity=s.expand((x*x-y*y)**2+(2*x*y)**2-(x*x+y*y)**2)
assert identity==0
checks.append({'claim':'real pair has no common nonzero isotropic vector',
               'identity':'(x^2-y^2)^2+(2xy)^2=(x^2+y^2)^2'})
det=s.det(s.Matrix([[u,v],[v,-u]]))
assert det == -u*u-v*v
checks.append({'claim':'every nonzero real combination is indefinite',
               'determinant':str(det)})

adic=[]
for k in range(1,25):
    negative=sum(2*3**j for j in range(k+1))
    half=2+sum(3**j for j in range(1,k+1))
    assert negative+1 == 3**(k+1)
    assert 2*half-1 == 3**(k+1)
    adic.append({'maximum_power':k,'minus_one_error':negative+1,'twice_half_error':2*half-1})

riesz=[]
for n in [1,2,3,5,8]:
    for m in [2,4,6]:
        exponent=s.Rational(n,m)
        integral=s.integrate(t**exponent,(t,0,L))/L
        target=L**exponent*s.Rational(m,m+n)
        assert s.simplify(integral-target)==0
        riesz.append({'dimension':n,'operator_order':m,'coefficient':str(s.Rational(m,m+n))})

sphere=[]
for n in [2,3,4,7]:
    for k in range(0,16):
        h=math.comb(n+k,k)-(math.comb(n+k-2,k-2) if k>=2 else 0)
        closed=(2*k+n-1)*math.factorial(k+n-2)//(math.factorial(k)*math.factorial(n-1))
        assert h==closed
        sphere.append({'sphere_dimension':n,'degree':k,'multiplicity':h})

out={'status':'all exact checks passed','symbolic_checks':checks,
     'adic_checks':adic,'riesz_coefficients':riesz,'spherical_multiplicities':sphere,
     'limitation':'These finite checks supplement the exact formulas and source readings; no universal inference is made from sampled values.'}
path=Path(__file__).resolve().parents[1]/'audit/verify_editorial_output.json'
path.parent.mkdir(parents=True,exist_ok=True)
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'symbolic_identities':len(checks),
                  'adic_cases':len(adic),'riesz_cases':len(riesz),'sphere_cases':len(sphere)},indent=2))
