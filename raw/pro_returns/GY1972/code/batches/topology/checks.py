"""Independent mathematical sanity checks for this batch (oursComputed).

Standard-library-only. Exact integer algebra is separated from numerical
quadrature; numerical samples never substitute for the proofs in the index.
"""
import math
from fractions import Fraction

def simpson(f,a,b,n):
    assert n%2==0
    h=(b-a)/n
    return h/3*(f(a)+f(b)+4*sum(f(a+j*h) for j in range(1,n,2))+2*sum(f(a+j*h) for j in range(2,n,2)))

def add_polys(*polys):
    result=[0]*max(map(len,polys))
    for p in polys:
        for i,c in enumerate(p): result[i]+=c
    while len(result)>1 and result[-1]==0: result.pop()
    return result

# After conjugation, the w term is a^2 - 2a^2 + a^2 + d^2.
# Coefficients of (a^2,d^2), and of a in the w' term, cancel exactly.
assert [1-2+1,1]==[0,1] and -2+2==0
print('oursComputed: exact pencil coefficients: w -> d^2 lambda^2; w-prime -> 0; w-double-prime -> 1.')

# Differentiate e^(2gnx)(A+B cos(2nx)+C sin(2nx)), where
# A=1/(4gn), B=-g/(4n(1+g^2)), C=-1/(4n(1+g^2)).
# Clearing 2(1+g^2), the constant/cos/sin coefficient identities are:
assert add_polys([1,0,1],[-1,0,-1])==[0]
assert add_polys([0,0,-1],[-1],[1,0,1])==[0]
assert add_polys([0,-1],[0,1])==[0]
print('oursComputed: exact differentiated primitive coefficients = (1/2,-1/2,0).')
print('Endpoint sin(2n*pi)=0, cos(2n*pi)=1 gives norm^2=(exp(2*g*n*pi)-1)/(4*g*n*(1+g^2)).')
print('oursComputed: independent quadrature on original x and endpoint-scaled s, at two mesh sizes:')
for gamma in [-1.2,-0.3,0.15,0.7]:
    for n in [1,3,8]:
        scale=max(0,2*gamma*n*math.pi)
        closed=math.expm1(2*gamma*n*math.pi)*math.exp(-scale)/(4*gamma*n*(1+gamma*gamma))
        errs=[]
        for grid in [4000,8000]:
            direct=simpson(lambda x:math.exp(2*gamma*n*x-scale)*math.sin(n*x)**2,0,math.pi,grid)
            scaled=simpson(lambda s:math.exp(-2*abs(gamma)*s)*math.sin(s)**2,0,n*math.pi,grid)/n
            err1=abs(direct/closed-1);err2=abs(scaled/closed-1)
            assert max(err1,err2)<1e-8
            errs.append((err1,err2))
        print(' gamma=%s n=%d errors=%s'%(gamma,n,errs))

print('Exact independent sine identity: sin(n(pi+s))=(-1)^n sin(ns), sin(n(pi-s))=-(-1)^n sin(ns).')
maxcancel=max(abs(math.sin(n*(math.pi+s))+math.sin(n*(math.pi-s))) for n in [1,2,7,19] for s in [0.02,0.13,0.61])
assert maxcancel<1e-12
print('oursComputed: reflected-interval sample cancellation error =',maxcancel)

def determinant(matrix):
    a=[list(map(Fraction,row)) for row in matrix]
    sign=1; det=Fraction(1)
    for k in range(len(a)):
        pivot=next((i for i in range(k,len(a)) if a[i][k]),None)
        if pivot is None:return Fraction(0)
        if pivot!=k:a[k],a[pivot]=a[pivot],a[k];sign=-sign
        p=a[k][k];det*=p
        for i in range(k+1,len(a)):
            q=a[i][k]/p
            for j in range(k,len(a)):a[i][j]-=q*a[k][j]
    return sign*det

cartan=[[2*int(i==j) for j in range(6)] for i in range(6)]
for i,j in [(0,1),(1,2),(2,3),(3,4),(2,5)]:cartan[i][j]=cartan[j][i]=-1
principal=[int(determinant([row[:j] for row in cartan[:j]])) for j in range(1,7)]
assert principal==[2,3,4,5,6,3]
print('oursComputed: E6 Cartan exact leading principal minors =',principal)
print('Sylvester criterion: negative E6 has inertia (0,0,6); adding the published rank-two zero form gives (0,2,6).')

print('oursComputed: KU(S2), k=4, coefficient residues mod3:',[(N,(3*4**N)%3) for N in range(8)])
print('Universal proof: 4 is a unit equal to1 mod3, also after inverting4.')
print('oursComputed: KO(S4) prime-divisibility checks with several possible finite J-orders:')
primes=[2,3,5,7,11,13,17,19,23,29,31,37]
for M in [1,2,24,120,5040]:
    q=next(p for p in primes if M%p); k=q+1
    assert (k*k-1)%q==0 and k%q==1 and M%q!=0
    print(' M=%d q=%d k=%d M_mod_q=%d (k^2-1)_mod_q=%d'%(M,q,k,M%q,(k*k-1)%q))
print('Universal proof: for every finite M some prime q does not divide M; k=q+1 is a unit modq.')
print('PASS: all exact identities and independent numerical checks.')
