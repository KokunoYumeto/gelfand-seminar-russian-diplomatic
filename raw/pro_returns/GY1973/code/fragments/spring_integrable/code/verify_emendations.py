"""Independent symbolic checks of critical emendations, not new mathematical claims.
Run from any directory. Requires SymPy. Writes only ../output/.
"""
from pathlib import Path
import json
import sys
vendor=Path(__file__).resolve().parent/"vendor"
if vendor.exists():sys.path.insert(0,str(vendor))
import sympy as s
OUT=Path(__file__).resolve().parents[1]/'output'
OUT.mkdir(exist_ok=True)
x,z,t=s.symbols('x z t',real=True)
u=s.Function('u')(x,z,t)
w=s.Function('w')(x,z,t)
v=s.Function('v')(x,t)
lam,alpha,beta=s.symbols('lambda alpha beta',constant=True)
checks={}

def comp(A,B):
    out={}
    for i,a in A.items():
        for j,b in B.items():
            for k in range(i+1):
                p=i+j-k
                out[p]=out.get(p,0)+a*s.binomial(i,k)*s.diff(b,x,k)
    return {p:s.simplify(c) for p,c in out.items() if s.simplify(c)!=0}
def subtract(A,B):
    return {p:s.simplify(A.get(p,0)-B.get(p,0)) for p in A.keys()|B.keys() if s.simplify(A.get(p,0)-B.get(p,0))!=0}
def action(A,f): return sum(a*s.diff(f,x,i) for i,a in A.items())

L={2:-1,0:u}
A={3:4,1:-6*u,0:-3*s.diff(u,x)}
comm=subtract(comp(A,L),comp(L,A))
expected=s.diff(u,x,3)-6*u*s.diff(u,x)
assert comm=={0:expected}
# A second calculation applies actual derivatives to a generic test function.
phi=s.Function('phi')(x)
assert s.simplify(action(A,action(L,phi))-action(L,action(A,phi))-expected*phi)==0
checks['lax_commutator']={'result':str(comm),'checked_by':['formal composition','direct action on generic test function'],'pass':True}

P={2:1,0:u};Q={3:1,1:s.Rational(3,2)*u+lam,0:s.Rational(3,4)*s.diff(u,x)+w}
pq=subtract(comp(P,Q),comp(Q,P))
expected_pq={1:2*s.diff(w,x),0:s.diff(w,x,2)-s.diff(u,x,3)/4-s.Rational(3,2)*u*s.diff(u,x)-lam*s.diff(u,x)}
assert subtract(pq,expected_pq)=={}
assert s.simplify(action(P,action(Q,phi))-action(Q,action(P,phi))-action(expected_pq,phi))==0
# alpha P_t - beta Q_z = [P,Q].
compat1=s.simplify(-s.Rational(3,2)*beta*s.diff(u,z)-pq[1])
wx=-s.Rational(3,4)*beta*s.diff(u,z)
assert s.simplify(compat1.subs(s.diff(w,x),wx))==0
wz=(alpha*s.diff(u,t)+s.diff(u,x,3)/4+s.Rational(3,2)*u*s.diff(u,x)+lam*s.diff(u,x))/beta
compat0=s.simplify(alpha*s.diff(u,t)-beta*(s.Rational(3,4)*s.diff(u,x,z)+wz)-pq[0])
assert s.simplify(compat0.subs(s.diff(w,x,2),s.diff(wx,x)))==0
compat_elim=s.expand(4*beta*(s.diff(wz,x)-s.diff(wx,z)))
kp=s.diff(4*alpha*s.diff(u,t)+s.diff(u,x,3)+6*u*s.diff(u,x)+4*lam*s.diff(u,x),x)+3*beta**2*s.diff(u,z,2)
assert s.simplify(compat_elim-kp)==0
checks['kp_compatibility']={'commutator':str(pq),'w_x':str(wx),'beta_w_z':str(beta*wz),'eliminated_equation':str(s.expand(kp)),'pass':True}

# Rational exponential parameter avoids hyperbolic simplification assumptions.
k,r=s.symbols('k r',positive=True)
q=8*k**2*r/(1+r)**2
dx=lambda f:s.factor(2*k*r*s.diff(f,r))
dt=lambda f:s.factor(-2*k**3*r*s.diff(f,r))
good=s.factor(4*dt(q)+dx(dx(dx(q)))+6*q*dx(q))
bad=s.factor(4*dt(q)+dx(dx(dx(q)))+q*dx(q))
assert good==0 and s.simplify(bad+5*q*dx(q))==0 and bad!=0
badvalue=bad.subs({k:s.Rational(5,4),r:2})
assert badvalue!=0
checks['one_soliton']={'substitution':'r=exp(2*k*(x-k**2*t-h)), q=8*k**2*r/(1+r)**2','coefficient6_residual':str(good),'coefficient1_residual':str(bad),'explicit_bad_residual_k_5_over_4_r_2':str(badvalue),'pass':True}

a,b,c,mu=s.symbols('a b c mu')
M=s.Matrix([[a,b],[c,-a]])
assert s.expand((mu*s.eye(2)-M).det()-(mu**2+M.det()))==0
checks['traceless_matrix']={'charpoly':str((mu*s.eye(2)-M).det()),'determinant':str(M.det()),'eigenvalue_square':str(-M.det()),'pass':True}

miura_u=s.diff(v,x)+v**2
mkdv=s.diff(v,t)-6*v**2*s.diff(v,x)+s.diff(v,x,3)
kdv=s.diff(miura_u,t)-6*miura_u*s.diff(miura_u,x)+s.diff(miura_u,x,3)
assert s.expand(kdv-s.diff(mkdv,x)-2*v*mkdv)==0
checks['miura_identity']={'identity':'KdV(v_x+v^2)=(D_x+2v)mKdV(v)','pass':True}

evals=[0]+[j*j for j in range(1,9) for _ in range(2)]
gaps=[b-a for a,b in zip(evals,evals[1:])]
assert all(evals[2*j-1]==evals[2*j] for j in range(1,9))
checks['circle_doublets']={'eigenvalues':evals,'adjacent_gaps':gaps,'universal_positive_lower_bound':False,'pass':True}

# Chain-rule coefficient of the leading fast-phase term.
eps,omega,kk,ftheta2=s.symbols('epsilon omega k_phase f_theta2')
leading=s.simplify(eps**2*((omega/eps)**2-(kk/eps)**2)*ftheta2)
assert leading==(omega**2-kk**2)*ftheta2
checks['whitham_fast_phase']={'leading_term':str(leading),'epsilon_survives':False,'pass':True}

report={'date':'2026-11-09','purpose':'Critical emendation checks; no new research theorem or C/D contribution is claimed.','sympy_version':s.__version__,'checks':checks}
(OUT/'emendation_checks.json').write_text(json.dumps(report,indent=2)+'\n')
(OUT/'emendation_checks.txt').write_text('\n'.join([report['purpose']]+[f"{name}: PASS\n{json.dumps(data,indent=2)}" for name,data in checks.items()])+'\n')
print(f'{len(checks)} symbolic/elementary checks passed; output in {OUT}')
