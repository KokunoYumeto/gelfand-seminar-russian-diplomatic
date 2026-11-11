"""Exhaustive checks of an explanatory balanced-ternary construction.

Equal numbers are placed on each pan.  Exactly one coin differs, of unknown
sign.  The required output is its identity; its sign need not be recovered.
This is not a claim of a new counterfeit-coin algorithm.
"""
from itertools import product
from collections import defaultdict, Counter
import json
from pathlib import Path

cycle = {(-1, 0), (0, 1), (1, -1)}

def columns(n):
    selected = []
    for word in product((-1, 0, 1), repeat=n):
        first_change = next(((a,b) for a,b in zip(word,word[1:]) if a != b), None)
        if first_change in cycle:
            selected.append(word)
    return selected + [(0,)*n]

def check(n):
    cols = columns(n)
    assert len(cols) == (3**n-1)//2
    rows = list(zip(*cols))
    pan_counts = [dict(Counter(row)) for row in rows]
    assert all(row.count(-1) == row.count(1) for row in rows)
    histories = defaultdict(list)
    for coin, column in enumerate(cols,1):
        for sign in (-1,1):
            # Independent physical computation: every genuine contribution
            # cancels because rows balance; add the counterfeit deviation.
            outcomes = []
            for row in rows:
                left = sum(10 + (sign if j == coin-1 else 0)
                           for j,side in enumerate(row) if side == -1)
                right = sum(10 + (sign if j == coin-1 else 0)
                            for j,side in enumerate(row) if side == 1)
                outcomes.append((right > left) - (right < left))
            outcome = tuple(outcomes)
            assert outcome == tuple(sign*x for x in column)
            histories[outcome].append((coin,sign))
    assert all(len({coin for coin,sign in states}) == 1 for states in histories.values())
    collisions = {','.join(map(str,h)):states for h,states in histories.items() if len(states)>1}
    assert list(collisions) == [','.join('0' for _ in range(n))]
    return dict(weighings=n, coins=len(cols), pan_counts=pan_counts,
                signed_states=2*len(cols), histories=len(histories),
                identity_collisions=0, sign_ambiguities=collisions,
                columns=cols if n==3 else None)

if __name__ == '__main__':
    output = dict(assumptions='Exactly one counterfeit; equal coin counts per pan; identity required, sign optional.',
                  checks=[check(n) for n in range(1,7)])
    destination=Path(__file__).with_name('coin_check_output.json')
    destination.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(output,indent=2))
