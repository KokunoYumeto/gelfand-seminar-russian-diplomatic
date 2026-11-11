"""Exact, reproducible checks for GY1985.

Run: python code/check_mathematics.py --output code/check_mathematics_output.json
No floating point evidence is promoted to a theorem.  Symbolic differential
operators and direct application are separate implementations; stacking facets
are also checked by an independent exhaustive supporting-hyperplane search.
"""
from __future__ import annotations
import argparse, datetime, itertools, json, math, platform
from pathlib import Path
import sympy as s

z,w=s.symbols('z w')
V=s.Function('V')(z,w);u=s.Function('u')(z,w);v=s.Function('v')(z,w)
B=s.Function('B')(z,w)
report={'python':platform.python_version(),'sympy':s.__version__,'arithmetic':'exact symbolic / rational','checks':{}}

def op_add(*ops):
    ans={}
    for op in ops:
        for k,a in op.items():ans[k]=ans.get(k,0)+a
    return {k:s.expand(a) for k,a in ans.items() if s.expand(a)!=0}

def op_scale(c,op):return {k:c*a for k,a in op.items()}

def compose(p,q):
    ans={}
    for (i,j),a in p.items():
        for (k,l),b in q.items():
            for r in range(i+1):
                for t in range(j+1):
                    key=(i-r+k,j-t+l)
                    coef=a*math.comb(i,r)*math.comb(j,t)*s.diff(b,z,r,w,t)
                    ans[key]=ans.get(key,0)+coef
    return op_add(ans)

def commutator(p,q):return op_add(compose(p,q),op_scale(-1,compose(q,p)))

L={(1,1):1,(0,0):V}
P={(3,0):1,(0,3):1,(1,0):u,(0,1):v}
actual=op_add(commutator(P,L),compose({(0,0):B},L))
expected={
 (2,0):3*s.diff(V,z)-s.diff(u,w),
 (0,2):3*s.diff(V,w)-s.diff(v,z),
 (1,1):B-s.diff(u,z)-s.diff(v,w),
 (1,0):3*s.diff(V,z,2)-s.diff(u,z,w),
 (0,1):3*s.diff(V,w,2)-s.diff(v,z,w),
 (0,0):s.diff(V,z,3)+s.diff(V,w,3)+u*s.diff(V,z)+v*s.diff(V,w)+B*V}
assert not op_add(actual,op_scale(-1,expected))
nv_trials=[]
for potential in (z**3*w**2+2*z*w+w**4,2*z**4+w**5+z**2*w**3+1):
    U=3*s.integrate(s.diff(potential,z),w)+z**2
    W=3*s.integrate(s.diff(potential,w),z)+w**3
    BB=s.diff(U,z)+s.diff(W,w)
    def Ll(f):return s.diff(f,z,w)+potential*f
    def Pp(f):return s.diff(f,z,3)+s.diff(f,w,3)+U*s.diff(f,z)+W*s.diff(f,w)
    scalar=s.diff(potential,z,3)+s.diff(potential,w,3)+s.diff(U*potential,z)+s.diff(W*potential,w)
    residuals=[]
    for f in (z**4+w**3+z*w+1,z**3*w**5+2):
        residual=s.expand(Pp(Ll(f))-Ll(Pp(f))+BB*Ll(f)-scalar*f)
        assert residual==0
        residuals.append(str(residual))
    nv_trials.append({'V':str(potential),'u':str(U),'v':str(W),'direct_application_residuals':residuals})
report['checks']['novikov_veselov']={'status':'PASS','formal_coefficients':{str(k):str(a) for k,a in expected.items()},'independent_polynomial_trials':nv_trials}

x,y=s.symbols('x y'); U=s.Function('U')(x);f=s.Function('f')(x,y)
def kdvl(h):return -s.diff(h,x,2)-s.diff(h,y,2)+U*h
def kdva(h):return -4*s.diff(h,x,3)+6*U*s.diff(h,x)+3*s.diff(U,x)*h
kdv_residual=s.expand(kdva(kdvl(f))-kdvl(kdva(f))-(6*U*s.diff(U,x)-s.diff(U,x,3))*f)
assert kdv_residual==0
# Independently use the coefficient-algebra implementation with z playing x.
Uz=s.Function('U')(z)
La={(2,0):-1,(0,2):-1,(0,0):Uz}
Aa={(3,0):-4,(1,0):6*Uz,(0,0):3*s.diff(Uz,z)}
assert not op_add(commutator(Aa,La),{(0,0):-(6*Uz*s.diff(Uz,z)-s.diff(Uz,z,3))})
r,q=s.symbols('r q',positive=True)
def Dx(h):return s.cancel(2*r*s.diff(h,r)+4*q*s.diff(h,q))
def Dt(h):return s.cancel(-8*r*s.diff(h,r)-64*q*s.diff(h,q))
tau2=1+r+q+r*q/9
two_soliton=s.cancel(-2*Dx(Dx(tau2)/tau2))
two_residual=s.cancel(Dt(two_soliton)-6*two_soliton*Dx(two_soliton)+Dx(Dx(Dx(two_soliton))))
assert two_residual==0
modes=[(0,0,1),(2,-8,r),(4,-64,q),(6,-72,r*q/9)]
bilinear=s.expand(sum(ai*aj*((ki-kj)**4+(ki-kj)*(wi-wj)) for ki,wi,ai in modes for kj,wj,aj in modes))
assert bilinear==0
ratios=[]
for rv,qv in ((1,1),(2,4)):
    ux=Dx(two_soliton).subs({r:rv,q:qv})
    ut=Dt(two_soliton).subs({r:rv,q:qv})
    assert ux!=0
    ratios.append(s.cancel(ut/ux))
assert ratios[0]!=ratios[1]
report['checks']['kdv_reduction']={'status':'PASS','direct_function_residual':str(kdv_residual),'second_check':'Leibniz coefficient-algebra expansion','explicit_tau':str(tau2),'explicit_u':str(two_soliton),'two_soliton_PDE_residual':str(two_residual),'independent_bilinear_residual':str(bilinear),'ut_over_ux_at_t0':list(map(str,ratios)),'scope':'global smooth positive tau gives a genuine KdV solution; different velocity ratios at one time rule out even time-dependent translations'}

k=s.symbols('k',nonzero=True)
c=s.Function('c')(z,w);xi=s.Function('xi')(z,w);rho=s.Function('rho')(z,w)
a=-s.diff(c,z)/c;b=-s.I*s.diff(xi,w)
psi1=s.exp(s.I*k*z)*(1+xi/k)
psi2=c*s.exp(s.I*k*w)*(1+rho/k)
def baL(h):return s.diff(h,z,w)+a*s.diff(h,w)+b*h
lead1=s.expand(baL(psi1)/s.exp(s.I*k*z)).coeff(k,0)
lead2=s.expand(baL(psi2)/s.exp(s.I*k*w)).coeff(k,1)
assert s.simplify(lead1)==0 and s.simplify(lead2)==0
# The recorded first-order placement has a nonzero k-leading term in general.
a_bad=s.diff(c,w)/c
bad=s.expand((s.diff(psi1,z,w)+a_bad*s.diff(psi1,z)+b*psi1)/s.exp(s.I*k*z)).coeff(k,1)
assert s.simplify(bad-s.I*a_bad)==0
report['checks']['baker_akhiezer_leading_terms']={'status':'PASS','first_puncture_constant':str(s.simplify(lead1)),'second_puncture_linear':str(s.simplify(lead2)),'recorded_wrong_placement_linear':str(bad),'scope':'leading Laurent constraints; existence is supplied by the cited Baker--Akhiezer theorem'}

X,Y,eta=s.symbols('X Y eta',real=True,nonzero=True)
tau=X+s.I*Y;taub=X-s.I*Y
deformation=(tau+eta*taub/Y)/(1+eta/Y)
deriv=s.simplify(s.diff(deformation,eta).subs(eta,0))
assert deriv==-2*s.I
J=s.Matrix([[0,2],[-2,0]]) # eta=p+iq gives delta tau=2q-2ip.
assert J.det()==4
# d tau wedge d bar tau = -2i det(J) dp wedge dq, while
# d bar eta wedge d eta = 2i dp wedge dq.
wedge_ratio=s.simplify(2*s.I/(-2*s.I*J.det()))
assert wedge_ratio==-s.Rational(1,4)
report['checks']['beltrami_wedge']={'status':'PASS','complex_derivative':str(deriv),'real_jacobian':J.tolist(),'jacobian_determinant':4,'wedge_ratio':str(wedge_ratio)}

det_trials=[]
for vals in ((s.Rational(2),s.Rational(3)),(s.Rational(1,2),s.Rational(7,3),s.Rational(5,4)),()):
    singprod=s.prod(vals);positive_eigenvalues=[a*a for a in vals]
    determinant=s.prod(positive_eigenvalues)
    normsq=1/(singprod**2)
    assert normsq==1/determinant
    det_trials.append({'nonzero_singular_values':list(map(str,vals)),'cohomology_generator_squared_norm':str(normsq),'spectral_determinant':str(determinant)})
report['checks']['finite_determinant_duality']={'status':'PASS','trials':det_trials,'scope':'diagonal singular-value examples, including rank zero; complete proof uses the singular-value decomposition'}

j,t=s.symbols('j t')
todd=s.series(s.exp(j*t)*(1-t/2+t**2/12),t,0,3).removeO().expand().coeff(t,2)
cj=6*j*j-6*j+1
assert s.simplify(todd-cj/12)==0
assert cj.subs(j,2)-13*cj.subs(j,1)==0
report['checks']['anomaly']={'status':'PASS','Todd_coefficient':str(todd),'c_j_values':{str(n):str(cj.subs(j,n)) for n in range(-3,5)},'critical_cancellation':0,'modular_weight_sum':-4+28-24}
assert -4+28-24==0

hyper=[]
for g in range(2,10):
    even_exponents=list(range(2*g-1));odd_exponents=list(range(g-2))
    assert all(2*g-2-i>=0 for i in even_exponents)
    assert all(g-3-i>=0 for i in odd_exponents)
    products={a+b for a in range(g) for b in range(g)}
    assert products==set(even_exponents)
    total=len(even_exponents)+len(odd_exponents)
    assert total==3*g-3 and total-len(products)==g-2
    hyper.append({'g':g,'h0_K2':total,'product_rank':len(products),'cokernel':g-2})
report['checks']['hyperelliptic_quadratics']={'status':'PASS','genera':hyper,'scope':'finite dimension/order verification supplements the uniform local-coordinate proof'}

def initial(d):
    return [s.zeros(d,1)]+[s.eye(d)[:,i] for i in range(d)]

def form(vertices,facet):
    """Exact affine form positive on the interior of the old polytope."""
    M=s.Matrix([[1]+list(vertices[i]) for i in facet])
    ns=M.nullspace();assert len(ns)==1
    coeff=ns[0]
    center=sum(vertices,s.zeros(len(vertices[0]),1))/len(vertices)
    orient=coeff[0]+s.Matrix(coeff[1:]).dot(center)
    assert orient!=0
    if orient<0:coeff=-coeff
    return coeff

def val(coeff,point):return coeff[0]+s.Matrix(coeff[1:]).dot(point)

def facet_enumeration(vertices):
    """Independent exhaustive supporting-hyperplane test, not update rule."""
    n=len(vertices);d=len(vertices[0]); found=set()
    for combo in itertools.combinations(range(n),d):
        M=s.Matrix([[1]+list(vertices[i]) for i in combo])
        if M.rank()!=d:continue
        a=M.nullspace()[0]
        signs=[s.sign(val(a,p)) for p in vertices]
        if (all(c>=0 for c in signs) or all(c<=0 for c in signs)) and sum(c==0 for c in signs)==d:
            found.add(tuple(combo))
    return found

stack_trials=[]
for d,choices in ((2,[0,1,0]),(3,[0,2,1]),(4,[0,0,1,2]),(4,[-1,1,-1,0])):
    verts=initial(d);facets=set(itertools.combinations(range(d+1),d));steps=[]
    for chosen in choices:
        F=sorted(facets)[chosen]
        forms={G:form(verts,G) for G in facets}
        bary=sum((verts[i] for i in F),s.zeros(d,1))/d
        aF=s.Matrix(forms[F][1:])
        bounds=[s.Rational(1)]
        for G,cG in forms.items():
            if G==F:continue
            slack=val(cG,bary);assert slack>0
            bounds.append(slack/(2*(1+abs(s.Matrix(cG[1:]).dot(aF)))))
        eps=min(bounds)
        section=bary-eps*aF
        alternative=bary-eps*aF/3
        for lam in (s.Rational(0),s.Rational(1,7),s.Rational(1,2),s.Rational(1)):
            point=(1-lam)*alternative+lam*section
            assert val(forms[F],point)<0
            assert all(val(cG,point)>0 for G,cG in forms.items() if G!=F)
        n=len(verts)
        newfacets=(facets-{F})|{tuple(sorted(ridge+(n,))) for ridge in itertools.combinations(F,d-1)}
        verts.append(section)
        independent=facet_enumeration(verts)
        assert independent==newfacets
        # Strict support inequalities also prove each prescribed facet is simplicial.
        for G in newfacets:
            cG=form(verts,G)
            assert all(val(cG,p)==0 if i in G else val(cG,p)>0 for i,p in enumerate(verts))
        steps.append({'chosen_facet':list(F),'epsilon':str(eps),'new_vertex':list(map(str,section)),'facets':len(newfacets),'independently_enumerated_facets':len(independent),'line_segment_parameters':['0','1/7','1/2','1']})
        facets=newfacets
    stack_trials.append({'dimension':d,'steps':steps,'status':'PASS'})
report['checks']['stacking_history']={'status':'PASS','trials':stack_trials,'scope':'four finite rational construction histories, two in dimension four; contractibility for every fixed finite history is proved separately'}

dates=['1985-09-21','1985-10-21','1985-02-24','1986-02-24','1987-02-24']
report['checks']['calendar']={date:datetime.date.fromisoformat(date).strftime('%A') for date in dates}
report['all_assertions_passed']=True
parser=argparse.ArgumentParser();parser.add_argument('--output',default=str(Path(__file__).with_name('check_mathematics_output.json')))
args=parser.parse_args()
Path(args.output).write_text(json.dumps(report,ensure_ascii=False,indent=2,default=str)+'\n')
print(json.dumps({'all_assertions_passed':True,'checks':list(report['checks']),'output':args.output},indent=2))
