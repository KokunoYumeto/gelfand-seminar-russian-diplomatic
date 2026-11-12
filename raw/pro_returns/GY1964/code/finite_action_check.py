"""Independent exact check of the finite ergodic-action example in 1964-34.13.

Enumerate GL(3,F_2), compare vector/covector permutation characters, and
check that a point stabilizer fixes no nonzero covector. No source data or
code from the draft's author are used.
"""
from itertools import product
from collections import Counter
from pathlib import Path
import json
import sys

V=list(product(range(2),repeat=3))[1:]

def mv(a,x):
    return tuple(sum(a[i][j]*x[j] for j in range(3))%2 for i in range(3))

def vm(x,a):
    return tuple(sum(x[i]*a[i][j] for i in range(3))%2 for j in range(3))

def main():
    group=[]
    for entries in product(range(2),repeat=9):
        a=tuple(tuple(entries[3*i+j] for j in range(3)) for i in range(3))
        # Over F2, injectivity on all seven nonzero vectors is invertibility.
        if len({mv(a,v) for v in V})==7 and (0,0,0) not in {mv(a,v) for v in V}:
            group.append(a)
    assert len(group)==168
    characters=[]
    for a in group:
        cv=sum(mv(a,v)==v for v in V)
        # A covector is fixed by a^{-1} iff it is fixed by a.
        cd=sum(vm(v,a)==v for v in V)
        assert cv==cd
        characters.append(cv)
    point=(1,0,0)
    stabilizer=[a for a in group if mv(a,point)==point]
    assert len(stabilizer)==24
    common=[v for v in V if all(vm(v,a)==v for a in stabilizer)]
    assert common==[]
    result={'group':'GL(3,F_2)','group_order':len(group),'action_size':7,
            'vector_action_transitive':len({mv(a,point) for a in group})==7,
            'covector_action_transitive':len({vm(point,a) for a in group})==7,
            'characters_equal_for_all_elements':True,
            'fixed_point_character_histogram':dict(sorted(Counter(characters).items())),
            'vector_stabilizer_order':len(stabilizer),
            'nonzero_covectors_fixed_by_vector_stabilizer':common,
            'conclusion':'Both uniform actions are ergodic, their complex Koopman representations are equivalent, but their G-sets are not isomorphic.'}
    text=json.dumps(result,indent=2)+'\n'
    if len(sys.argv)>1: Path(sys.argv[1]).write_text(text)
    print(text,end='')

if __name__=='__main__':main()
