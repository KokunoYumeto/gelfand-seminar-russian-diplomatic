"""Bounded editorial calculations for GY1975 records 375--385.

These verify notebook normalizations and classical examples; they make no
claim to resolve the continuum confinement problem or a new inverse problem.
Run from any directory. Outputs are written beside this script.
"""
from pathlib import Path
import json
import sympy as s
import mpmath as mp

x=s.symbols('x', positive=True)
u=s.Function('u')(x)
v=s.Function('v')(x)
w=s.Function('w')(x)
c1,c2=s.symbols('c1 c2')

def add(a,b,sign=1):
    keys=set(a)|set(b)
    return {i:z for i in keys if (z:=s.simplify(a.get(i,0)+sign*b.get(i,0)))!=0}

def mul(a,b):
    out={}
    for i,ai in a.items():
        for j,bj in b.items():
            for k in range(i+1):
                p=i+j-k
                out[p]=out.get(p,0)+s.binomial(i,k)*ai*s.diff(bj,x,k)
    return {i:z for i,q in out.items() if (z:=s.simplify(q))!=0}

L={2:-s.Integer(1),0:u}
M={3:s.Integer(1),1:v,0:w}
comm=add(mul(L,M),mul(M,L),-1)
expected={2:-2*s.diff(v,x)-3*s.diff(u,x),
          1:-s.diff(v,x,2)-2*s.diff(w,x)-3*s.diff(u,x,2),
          0:-s.diff(w,x,2)-s.diff(u,x,3)-v*s.diff(u,x)}
assert add(comm,expected,-1)=={}
subs={v:-s.Rational(3,2)*u+c1,w:-s.Rational(3,4)*s.diff(u,x)+c2}
reduced={i:s.simplify(q.subs(subs).doit()) for i,q in comm.items()}
assert reduced[2]==0 and reduced[1]==0
stationary=s.diff(u,x,3)-6*u*s.diff(u,x)+4*c1*s.diff(u,x)
assert s.simplify(reduced[0]+stationary/4)==0

P={2:s.Integer(1),0:-2/x**2}
R={3:s.Integer(1),1:-3/x**2,0:3/x**3}
assert add(mul(P,R),mul(R,P),-1)=={}
assert add(mul(R,R),mul(mul(P,P),P),-1)=={}

z=s.symbols('z')
assert s.expand((z+1)*z*(z-1)-(z**3-z))==0

mp.mp.dps=60
abel=[]
for et in ['0.1','0.3','0.7','0.95']:
    eta=mp.mpf(et)
    c=mp.sqrt(1-eta**2)
    def transformed(theta):
        tau=mp.sqrt(eta**2+(1-eta**2)*mp.sin(theta)**2)
        tau=min(mp.mpf(1),tau)
        Mprime=-mp.acos(tau)/mp.pi
        return 2*Mprime*c*mp.cos(theta)/tau
    val=mp.quad(transformed,[0,mp.pi/4,mp.pi/2])
    err=abs(val-mp.log(eta))
    assert err<mp.mpf('1e-45')
    abel.append({'eta':et,'computed_log_psi':mp.nstr(val,35),
                 'exact_log_eta':mp.nstr(mp.log(eta),35),
                 'absolute_error':mp.nstr(err,8)})

data={
    'status_date':'2026-11-10',
    'scope':'Editorial verification of classical formulas; no new research theorem claimed.',
    'school_commutator':{str(i):str(q) for i,q in sorted(comm.items(),reverse=True)},
    'school_reduced_constant_coefficient':str(reduced[0]),
    'school_stationary_equation':str(stationary)+' = 0',
    'cusp_commutator_zero':True,
    'cusp_R_squared_equals_P_cubed':True,
    'elliptic_coordinate_shift_checked':True,
    'abel_constant_profile':abel,
    'abel_normalization':'m = action/pi; log(psi(eta)) = 2 integral_eta^1 (tau*m(tau))prime / sqrt(tau^2-eta^2) dtau. Without /pi in m, coefficient is 2/pi.'
}
output_path = Path(__file__).resolve().parent.parent / 'computations' / 'b_checks_output.json'
output_path.parent.mkdir(parents=True, exist_ok=True)
output_path.write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(data,indent=2))
