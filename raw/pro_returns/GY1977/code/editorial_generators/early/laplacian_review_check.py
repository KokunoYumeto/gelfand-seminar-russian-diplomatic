"""Targeted independent audit, without importing the chapter implementation.

Uses combinations rather than recursive partitions, inserts the bracket in
its original first position and counts inversions, and computes exact rank
at the disputed eigenvalue instead of factoring the full characteristic
polynomial. It does not repeat all costly spectral calculations.
"""
from itertools import combinations
from math import comb
from collections import Counter, defaultdict
from pathlib import Path
import json
import sympy as sp
from sympy.polys.matrices import DomainMatrix

OUT=Path(__file__).parent
SOURCE=OUT.parents[1]/'code/output/laplacian_checks.json'
data=json.loads(SOURCE.read_text())

def subsets(weight, degree):
    if degree==0:
        return [()] if weight==0 else []
    return [I for I in combinations(range(1,weight+1),degree) if sum(I)==weight]

def gap_labels(weight):
    labels=defaultdict(list)
    degree=1
    while degree+3*degree*(degree-1)//2<=weight:
        for I in subsets(weight,degree):
            if any(b-a<3 for a,b in zip(I,I[1:])):
                continue
            energy=sum(comb(i,3) for i in I)-sum(a*b for a,b in combinations(I,2))
            alpha=(I[0]>=3)+sum(b-a>3 for a,b in zip(I,I[1:]))
            labels[energy].append({'partition':I,'alpha':alpha,'multiplicity':2**alpha})
        degree+=1
    return dict(labels)

independent=[]
for weight in range(1,26):
    labels=gap_labels(weight)
    independent.append({'weight':weight,
                        'labels':sum(map(len,labels.values())),
                        'distinct_energies':len(labels),
                        'collisions':{e:rows for e,rows in labels.items() if len(rows)>1}})
    if weight in data['weights_checked']:
        recorded=next(row for row in data['spectra'] if row['weight']==weight)
        expected={str(e):sum(row['multiplicity'] for row in rows) for e,rows in labels.items()}
        assert recorded['spectrum']==expected,(weight,'aggregate spectrum')
        assert sum(expected.values())==recorded['dimension']
        recombined=Counter()
        for block in recorded['blocks']:
            assert sum(block['spectrum'].values())==block['dimension']
            assert len(subsets(weight,block['degree']))==block['dimension']
            recombined.update(block['spectrum'])
        assert dict(recombined)==recorded['spectrum']

def differential(domain,codomain):
    positions={I:k for k,I in enumerate(codomain)}
    result=sp.zeros(len(codomain),len(domain))
    for col,I in enumerate(domain):
        for a,b in combinations(range(len(I)),2):
            word=I[:a]+(I[a]+I[b],)+I[a+1:b]+I[b+1:]
            if len(set(word))!=len(word):
                continue
            inversions=sum(word[i]>word[j] for i,j in combinations(range(len(word)),2))
            coefficient=(-1)**(b-1+inversions)*(I[b]-I[a])
            result[positions[tuple(sorted(word))],col]+=coefficient
    return result

weight=25
bases={q:subsets(weight,q) for q in range(8)}
boundary={q:differential(bases[q],bases[q-1]) for q in range(1,8)}
target=[]
for q in range(1,7):
    if q>=2:
        assert boundary[q-1]*boundary[q]==sp.zeros(len(bases[q-2]),len(bases[q]))
    lap=boundary[q].T*boundary[q]+boundary[q+1]*boundary[q+1].T
    nullity=lap.rows-DomainMatrix.from_Matrix(lap-320*sp.eye(lap.rows)).rank()
    old=next(row for row in data['spectra'] if row['weight']==weight)['blocks'][q-1]
    assert nullity==old['spectrum'].get('320',0)
    target.append({'degree':q,'dimension':lap.rows,'nullity_at_320':nullity})

# Two polynomial representatives can also be checked by hand in degree two:
# shift1: -e1 wedge e4 + 3e2 wedge e3;
# shift2: -e2 wedge e5 + 3e3 wedge e4.
harmonic=[]
for shift,weight in [(1,5),(2,7)]:
    basis=subsets(weight,2)
    v=sp.Matrix([-1 if I==(shift,shift+3) else 3 if I==(shift+1,shift+2) else 0 for I in basis])
    down=differential(basis,subsets(weight,1))
    up=differential(subsets(weight,3),basis)
    assert down*v==sp.zeros(down.rows,1)
    assert up.T*v==sp.zeros(up.cols,1)
    harmonic.append({'degree':2,'shift':shift,'weight':weight,'down_and_up_zero':True})

result={'range_independently_enumerated':list(range(1,26)),
        'first_collision':next(row for row in independent if row['collisions']),
        'all_saved_aggregate_spectra_and_block_dimensions_match':True,
        'weight25_exact_nullities':target,
        'weight25_total_320_multiplicity':sum(row['nullity_at_320'] for row in target),
        'degree_two_harmonic_checks':harmonic,
        'method':'Independent combinations; bracket insertion/inversion signs; exact DomainMatrix rank over Q at eigenvalue320.'}
(OUT/'laplacian_review_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
