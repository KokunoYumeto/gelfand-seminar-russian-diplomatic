"""Exact independent checks of two elementary editorial reconstructions.

Python standard library only. Output is JSON; no random or network input.
This checks arithmetic identities, not the general cited classification theorems.
"""
import json
from pathlib import Path

def add(p,q):
    n=max(len(p),len(q));return [(p[i] if i<len(p) else 0)+(q[i] if i<len(q) else 0) for i in range(n)]
def mul(p,q):
    r=[0]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q): r[i+j]+=a*b
    return r
def mod6(p):
    r=[0]*6
    for i,a in enumerate(p):r[i%6]+=a
    return r

x_minus_1=[-1,1]
a=mul(mul(x_minus_1,[1,1]),[1,1,1])
phi6=[1,-1,1]
assert any(mod6(a))
assert mod6(mul(phi6,a))==[0]*6
assert mod6(mul(mul(x_minus_1,[0,-1]),a))==mod6(a)
ys=[1]
for n in range(1,33):
    ys=mul(ys,mul(x_minus_1,[0,-1]))
    assert mod6(mul(ys,a))==mod6(a)

def qa(x,y):return (x[0]+y[0],x[1]+y[1])
def qm(x,y):return (x[0]*y[0]+3*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def hp(x,y):
    a,b,c=x;aa,bb,cc=y
    return qa(a,aa),qa(qa(b,bb),qm(a,cc)),qa(c,cc)
u=(2,1);ui=(2,-1)
assert qm(u,ui)==(1,0)
u2=qm(u,u)
def autom(x):a,b,c=x;return qm(u,a),qm(u2,b),qm(u,c)
examples=[((i,1-i),(i*i,-i),(2-i,i+1)) for i in range(-5,6)]
tests=0
for x in examples:
    for y in examples:
        assert autom(hp(x,y))==hp(autom(x),autom(y))
        tests+=1

result={
 'status':'PASS',
 'cyclic_group':{'group':'C6','nonzero_element_coefficients_low_to_high':a,
   'annihilator':'x^2-x+1','inverse_multiplier_on_element':'-x',
   'augmentation_power_tests':32,'all_remainders_equal':True},
 'heisenberg':{'quadratic_ring':'Z[sqrt(3)]','unit':u,'inverse':ui,
   'central_coordinate':'b','weights':['u','u^2','u'],
   'exact_product_tests':tests,'all_passed':True},
 'limits':'Finite checks corroborate the displayed identities; the chapter supplies their general algebraic proofs.'}
text=json.dumps(result,indent=2)+'\n'
Path(__file__).with_name('check_editorial_algebra_output.json').write_text(text)
print(text,end='')
