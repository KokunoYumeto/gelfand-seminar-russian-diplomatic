"""Elementary independent checks for the source emendations, not new theorems.

Run: python independent_checks.py
Writes checks_output.json alongside this file. All exact assertions are symbolic.
The zeta derivative also has an independent high-precision numerical check.
"""
import pathlib,json,itertools
import sympy as s
import mpmath as mp
D=pathlib.Path(__file__).parent
out={}
x=s.symbols('x');u=s.Function('u')(x)
def EL(density):
 return s.simplify(s.diff(density,u)-s.diff(s.diff(density,s.diff(u,x)),x))
written=EL((s.diff(u,x)**2+u**3)/4)
repaired=EL(-s.diff(u,x)**2/8-u**3/4)
assert written==3*u**2/4-s.diff(u,x,2)/2
assert repaired==s.diff(u,x,2)/4-3*u**2/4
out['1982-586.1']={'written_density_EL':str(written),'repaired_density_EL':str(repaired)}
a,d,b,c,l=s.symbols('a d b c lambda',real=True)
M=s.Matrix([[a,b+s.I*c],[b-s.I*c,d]])
discr=s.discriminant((l*s.eye(2)-M).det(),l)
assert s.expand(discr-((a-d)**2+4*(b*b+c*c)))==0
out['1982-586.4']={'squared_eigenvalue_separation':str(s.factor(discr)),'free_normalized_plane_wave_gap':'4 epsilon^2 |vhat(2k)|^2'}
f,g,z=s.symbols('f g z',nonzero=True)
P=s.Matrix([[f*f,f*g*z],[f*g/z,g*g]])
assert s.simplify(P*P-(f*f+g*g)*P)==s.zeros(2)
out['1982-590.3_orthogonal']={'identity':'P^2=(f1^2+f2^2)P','condition':'f1^2+f2^2=1'}
a,t=s.symbols('a tau',commutative=False)
P1=s.Matrix([[1-t*a,t],[a*(1-t*a),a*t]])
P2=s.Matrix([[0,t],[0,1]])
assert (P1*P1-P1).applyfunc(s.expand)==s.zeros(2)
assert P2*P2==P2
assert (P1-P2).subs(a,0)==s.diag(1,-1)
out['1982-590.3_pair']={'identities':'P1^2=P1 and P2^2=P2 without assuming a and tau inverse','bad_cutoff_limit':'a=0 gives P1-P2=diag(1,-1); idempotence is not compact support'}
# Basis order e,f,h; [h,e]=2e, [h,f]=-2f, [e,f]=h.
E=[s.eye(3)[:,j] for j in range(3)]
def bracket(v,w):
 ve,vf,vh=v;we,wf,wh=w
 return s.Matrix([2*(vh*we-ve*wh),2*(vf*wh-vh*wf),ve*wf-vf*we])
q=s.symbols('q')
forms={'zero':s.zeros(3),'minus_identity':-s.eye(3),
 'split':s.diag(-1,0,0),
 'nonskew':s.Matrix([[-1,0,0],[0,0,0],[-1,0,0]]),
 'parameter':s.diag(-1,0,q)}
for name,B in list(forms.items()):forms[name+'_involution']=-s.eye(3)-B
for name,B in forms.items():
 R=2*B+s.eye(3)
 for v,w in itertools.combinations(E,2):
  rb=bracket(B*v,B*w)-B*(bracket(B*v,w)+bracket(v,B*w)+bracket(v,w))
  mc=bracket(R*v,R*w)-R*(bracket(R*v,w)+bracket(v,R*w))+bracket(v,w)
  assert rb.applyfunc(s.simplify)==s.zeros(3,1),(name,rb)
  assert mc.applyfunc(s.simplify)==s.zeros(3,1),(name,mc)
out['1982-589.3']={'normal_forms_checked':list(forms),'claim':'These checks verify the listed solutions and R=2B+I convention. Completeness belongs to the cited classification, not to this computation.'}
mp.mp.dps=60
values=[]
for period in [mp.mpf(1),2*mp.pi,mp.mpf(7)/3]:
 derivative=mp.diff(lambda w:2*(period/(2*mp.pi))**(2*w)*mp.zeta(2*w),-2)
 expected=48*mp.zeta(5)/period**4
 assert abs(derivative-expected)<mp.mpf('1e-50')
 values.append({'T':mp.nstr(period,25),'derivative':mp.nstr(derivative,45),'48_zeta5_over_T4':mp.nstr(expected,45),'absolute_error':mp.nstr(abs(derivative-expected),4)})
out['1982-587.10']={'identity':'zeta_L prime(-2)=48 zeta_R(5)/T^4','numerical_checks':values}
v=s.Function('v')(x);y=s.Function('y')(x)
miura=s.expand(s.diff(s.diff(y,x)+v*y,x)-v*(s.diff(y,x)+v*y))
assert s.simplify(miura-(s.diff(y,x,2)+(s.diff(v,x)-v*v)*y))==0
out['1982-592.11']={'operator_identity':'(D-v)(D+v)=D^2+v_x-v^2'}
(D/'checks_output.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'status':'all checks passed','entries':list(out)},indent=2))
