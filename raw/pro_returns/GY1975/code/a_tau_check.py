"""Finite independent checks of the P000613--614 tau formulas.

No finite check is a proof of the general identities. All arithmetic is exact.
The two tau constructions are independent: direct product multiplication and
the logarithmic-derivative recurrence. The Manin sum is enumerated literally
over the stated quadruples, including the half-weight boundary.
"""
from fractions import Fraction
from math import comb
from pathlib import Path
import json

N=50
def sigma(n,k): return sum(d**k for d in range(1,n+1) if n%d==0)

coeff=[1]+[0]*(N-1)
for m in range(1,N):
    new=[0]*N
    for a,c in enumerate(coeff):
        for j in range(min(24,(N-1-a)//m)+1):
            new[a+j*m]+=c*(-1)**j*comb(24,j)
    coeff=new
tau=[0]+coeff
rec=[0,1]
for n in range(2,N+1):
    value=Fraction(-24*sum(sigma(m,1)*rec[n-m] for m in range(1,n)),n-1)
    assert value.denominator==1
    rec.append(value.numerator)

def manin_sum(n,mode):
    out=Fraction(0)
    for D in range(2,n+1):
        for d in range(1,D):
            if mode=='correct': poly=Fraction(691,18)*D**2*d**2*(D**2-d**2)**3
            else: poly=Fraction(D**8*d**2-D**2*d**8)+Fraction(691,6)*(D**6*d**4-D**4*d**6)
            for dp in range(1,n//(D+d)+1):
                rem=n-d*dp
                if rem%D==0 and rem//D>dp:
                    out+=poly
            if n%D==0 and 2*d<=D:
                out+=poly*(Fraction(1,2) if 2*d==D else 1)
    return sigma(n,11)-out

rows=[]
for n in range(1,N+1):
    cv=Fraction(65,756)*sigma(n,11)+Fraction(691,756)*sigma(n,5)-Fraction(691,3)*sum(sigma(m,5)*sigma(n-m,5) for m in range(1,n))
    mv=manin_sum(n,'correct')
    assert tau[n]==rec[n]==cv==mv,(n,tau[n],rec[n],cv,mv)
    rows.append(dict(n=n,tau=tau[n],product_equals_recurrence=True,ramanujan_convolution_agrees=True,manin_corrected_sum_agrees=True))

report=dict(scope=f'1 <= n <= {N}; finite verification only',
    independently_checked_methods=['Direct truncated Euler product','Logarithmic-derivative divisor recurrence'],
    all_checks_passed=True,
    counterexamples=dict(
       notebook_unweighted_partition_sum_at_n2=-1,
       correct_tau2=tau[2],
       notebook_manin_polynomial_with_favourable_halfweight_at_n2=str(manin_sum(2,'notebook')),
       notebook_prime_power_sum_at_p2_a2=tau[2]**2-2*2**11,
       correct_tau4=tau[4]),
    rows=rows)
target=Path(__file__).resolve().parent.parent/'computations/a_tau_check.json'
target.parent.mkdir(parents=True,exist_ok=True)
target.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='rows'},indent=2))
