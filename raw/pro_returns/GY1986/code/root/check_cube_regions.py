"""Two independent exact counts for the notebook's cube-cutting problem.

Method 1: split convex cells using an exhaustive rational candidate-vertex set.
Method 2: count intersection flats and their Mobius values (localized Zaslavsky).
Planes on the cube boundary do not cut its interior.
"""
from itertools import combinations,product
from functools import reduce
from math import gcd
from pathlib import Path
import json
import sympy as s

def primitive(values):
    values=[int(v) for v in values]
    g=reduce(gcd,(abs(v) for v in values))
    values=[v//g for v in values]
    if next(v for v in values if v) < 0:
        values=[-v for v in values]
    return tuple(values)

def value(plane,point):
    return sum(plane[i]*point[i] for i in range(3))+plane[3]

def intersection3(planes):
    M=s.Matrix([p[:3] for p in planes])
    if M.det() == 0:
        return None
    v=M.inv()*s.Matrix([-p[3] for p in planes])
    return tuple(v)

def line_data(p,q):
    if s.Matrix(p[:3]).cross(s.Matrix(q[:3])) == s.zeros(3,1):
        return None
    R,piv=s.Matrix([p,q]).rref()
    free=next(i for i in range(3) if i not in piv)
    base=[s.Integer(0)]*3; direction=[s.Integer(0)]*3
    direction[free]=s.Integer(1)
    for row,col in enumerate(piv):
        base[col]=-R[row,3]
        direction[col]=-R[row,free]
    key=tuple(R)
    return key,tuple(base),tuple(direction)

def line_meets_interior(base,direction):
    lower=None; upper=None
    for b,v in zip(base,direction):
        if v == 0:
            if not -1 < b < 1:
                return False
        else:
            endpoints=sorted([(-1-b)/v,(1-b)/v])
            lower=endpoints[0] if lower is None else max(lower,endpoints[0])
            upper=endpoints[1] if upper is None else min(upper,endpoints[1])
    return lower is None or upper is None or lower < upper

def point_on_line(point,base,direction):
    diff=s.Matrix([point[i]-base[i] for i in range(3)])
    return diff.cross(s.Matrix(direction)) == s.zeros(3,1)

def main():
    vertices=list(product([-1,1],repeat=3))
    planes=set()
    for x,y,z in combinations(vertices,3):
        normal=(s.Matrix(y)-s.Matrix(x)).cross(s.Matrix(z)-s.Matrix(x))
        assert normal != s.zeros(3,1)
        planes.add(primitive(list(normal)+[-normal.dot(s.Matrix(x))]))
    planes=sorted(planes)
    cutting=[p for p in planes if min(value(p,v) for v in vertices)<0<max(value(p,v) for v in vertices)]
    boundary=[p for p in planes if p not in cutting]
    print('SymPy',s.__version__)
    print('Distinct planes through vertex triples:',len(planes))
    print('Boundary planes:',len(boundary),'interior-cutting planes:',len(cutting))
    print('Interior planes n_x x+n_y y+n_z z+d=0:',cutting)
    candidates=set(vertices)
    for triple in combinations(planes,3):
        point=intersection3(triple)
        if point is not None and all(-1 <= x <= 1 for x in point):
            candidates.add(point)
    candidates=sorted(candidates)
    cells=[frozenset(range(len(candidates)))]; trajectory=[1]
    for p in cutting:
        signs=[s.sign(value(p,v)) for v in candidates]
        refined=[]
        for cell in cells:
            positive=any(signs[i]>0 for i in cell)
            negative=any(signs[i]<0 for i in cell)
            if positive and negative:
                refined.extend([frozenset(i for i in cell if signs[i]>=0),frozenset(i for i in cell if signs[i]<=0)])
            else:
                refined.append(cell)
        cells=refined; trajectory.append(len(cells))
    witnesses=[]
    sign_patterns=set()
    for cell in cells:
        point=tuple(sum(candidates[i][j] for i in cell)/s.Integer(len(cell)) for j in range(3))
        assert all(-1 < x < 1 for x in point)
        signs=tuple(int(s.sign(value(p,point))) for p in cutting)
        assert 0 not in signs
        sign_patterns.add(signs)
        witnesses.append({'point':[str(x) for x in point],'signs':signs})
    assert len(sign_patterns) == len(cells)
    print('Candidate vertices inside closed cube:',len(candidates))
    print('Convex-cell splitting trajectory:',trajectory)
    print('Method 1 region count:',len(cells))
    # Independent intersection-lattice computation.
    lines={}
    for p,q in combinations(cutting,2):
        data=line_data(p,q)
        if data is None:
            continue
        key,base,direction=data
        if not line_meets_interior(base,direction):
            continue
        multiplicity=sum(value(plane,base)==0 and sum(plane[i]*direction[i] for i in range(3))==0 for plane in cutting)
        lines[key]=(base,direction,multiplicity-1)
    points=set()
    for triple in combinations(cutting,3):
        point=intersection3(triple)
        if point is not None and all(-1<x<1 for x in point):
            points.add(point)
    point_values={}
    for point in points:
        k=sum(value(p,point)==0 for p in cutting)
        line_sum=sum(mu for base,direction,mu in lines.values() if point_on_line(point,base,direction))
        mu=-(1-k+line_sum)
        assert mu < 0
        point_values[point]=mu
    line_sum=sum(data[2] for data in lines.values())
    point_sum=sum(abs(mu) for mu in point_values.values())
    regions=1+len(cutting)+line_sum+point_sum
    print('Interior line flats:',len(lines),'sum |mu|:',line_sum)
    print('Interior point flats:',len(points),'sum |mu|:',point_sum)
    print('Method 2: 1 +',len(cutting),'+',line_sum,'+',point_sum,'=',regions)
    assert regions == len(cells) == 96
    out={'coordinate_cube':'[-1,1]^3','planes':planes,'cutting_planes':cutting,
         'method_1_trajectory':trajectory,'method_2_terms':[1,len(cutting),line_sum,point_sum],
         'regions':regions,'rational_interior_witnesses':witnesses}
    Path(__file__).with_name('cube_witnesses.json').write_text(json.dumps(out,indent=2))
    print('PASS: independent exact counts agree with the manuscript answer 96.')

if __name__ == '__main__':
    main()
