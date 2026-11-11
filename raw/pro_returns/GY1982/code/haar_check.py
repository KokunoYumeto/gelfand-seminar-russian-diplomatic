#!/usr/bin/env python3
"""Exact independent index-contraction check for GY1982, item 1982-565.6.

No sampling or floating-point arithmetic is used.  Each trace is expanded in
matrix entries.  The p=1,2 unitary Haar moment formula identifies indices;
each remaining index loop contributes N.  This checks the conditional-
expectation/character proof in GY1982_development.tex by a different route.
Requires Python 3 and SymPy.  Run: python code/haar_check.py.
"""
from collections import defaultdict
from itertools import permutations, product
import json
from pathlib import Path
import sympy as sp

N = sp.Symbol('N', positive=True, integer=True)


class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))

    def find(self, n):
        while self.parents[n] != n:
            self.parents[n] = self.parents[self.parents[n]]
            n = self.parents[n]
        return n

    def join(self, a, b):
        self.parents[self.find(a)] = self.find(b)

    def components(self):
        return len({self.find(i) for i in range(len(self.parents))})


def haar_trace_product(traces):
    """Expectation of traces of words in independent Haar U(N) matrices.

    A token (a,+1) is U_a, and (a,-1) is U_a^*.  We only need p <= 2
    copies of U_a and U_a^* for each label a; valid for all integers N >= 2.
    """
    occurrences = defaultdict(lambda: [[], []])
    offset = 0
    for word in traces:
        for j, (label, sign) in enumerate(word):
            row, col = offset+j, offset+(j+1) % len(word)
            if sign == 1:
                occurrences[label][0].append((row, col))
            else:
                # (U^*)_{row,col} = conjugate(U_{col,row}).
                occurrences[label][1].append((col, row))
        offset += len(word)
    choices = []
    for plus, minus in occurrences.values():
        if len(plus) != len(minus):
            return sp.Integer(0)
        p = len(plus)
        assert p in (1, 2), 'This checker deliberately implements only p=1,2.'
        terms = []
        for sigma in permutations(range(p)):
            for tau in permutations(range(p)):
                pairs = [(plus[k][0], minus[sigma[k]][0]) for k in range(p)]
                pairs += [(plus[k][1], minus[tau[k]][1]) for k in range(p)]
                if p == 1:
                    weight = 1/N
                elif sigma == tau:
                    weight = 1/(N*N-1)
                else:
                    weight = -1/(N*(N*N-1))
                terms.append((pairs, weight))
        choices.append(terms)
    answer = 0
    for terms in product(*choices):
        uf = UnionFind(offset)
        weight = 1
        for pairs, term_weight in terms:
            weight *= term_weight
            for a, b in pairs:
                uf.join(a, b)
        answer += weight * N**uf.components()
    return sp.factor(answer)


def W(a, b):
    return [(a, 1), (b, 1), (a, -1), (b, -1)]


def must_equal(label, actual, expected):
    assert sp.cancel(actual-expected) == 0, (label, actual, expected)
    print(f'{label} = {sp.factor(actual)} [exact symbolic agreement]')


def main():
    print('GY1982 exact Haar calculation; domain: every integer N >= 2')
    moments = {
        'E W12': haar_trace_product([W(1,2)]),
        'E W12^2': haar_trace_product([W(1,2),W(1,2)]),
        'E W12 conjugate(W12)': haar_trace_product([W(1,2),W(2,1)]),
        'E W12 W13': haar_trace_product([W(1,2),W(1,3)]),
        'E W12 W31': haar_trace_product([W(1,2),W(3,1)]),
        'E W12 W34': haar_trace_product([W(1,2),W(3,4)]),
    }
    targets = [1/N,4/(N*N-1),N*N/(N*N-1),2/N**2,2/N**2,1/N**2]
    for (name, actual), expected in zip(moments.items(),targets):
        must_equal(name,actual,expected)

    # Second check: sum all ordered off-diagonal plaquette pairs for d=2,3,4,5.
    # Canonical relabeling and symmetry do not assume any conditional covariance.
    cache = {}
    rows = []
    for d in (2,3,4,5):
        words = [W(a,b) for a in range(d) for b in range(d) if a != b]
        second = 0
        for left,right in product(words,repeat=2):
            names = {}
            canonical = []
            for word in (left,right):
                converted = []
                for a, sign in word:
                    if a not in names:
                        names[a] = len(names)
                    converted.append((names[a],sign))
                canonical.append(tuple(converted))
            key = tuple(canonical)
            if key not in cache:
                cache[key] = haar_trace_product(canonical)
            second += cache[key]
        mean = d*(d-1)/N
        variance = sp.factor(second-mean**2)
        target = d*(d-1)*((N*N+4)/(N*N-1)+(4*d-10)/N**2)
        must_equal(f'Var S, d={d}',variance,target)
        for n in (2,3,4,7,11):
            row = {'d':d,'N':n,
                   'Fprime':str(-sp.Integer(d)-sp.Rational(d*(d-1),n*n)),
                   'Fsecond':str(variance.subs(N,n))}
            rows.append(row)
    pair_count = sum((d*(d-1))**2 for d in (2,3,4,5))
    print(f'All {pair_count} ordered plaquette pairs for d=2,3,4,5: checked symbolically.')
    print('Independent low-rank edge case: N=1, every commutator is 1,')
    print('F_{d,1}(beta)=-d^2 beta; Fsecond=0. The N>=2 formula is NOT used at N=1.')
    print('For d=4, large-N derivatives: Fprime -> -4, Fsecond -> 12.')
    print('These coefficient calculations alone do not interchange limits or')
    print('prove an all-coupling free energy. Local analyticity uses the cited theorem.')
    print('Exact rational spot evaluations:')
    print(json.dumps(rows,indent=2))
    output = Path(__file__).with_name('haar_check_results.json')
    output.write_text(json.dumps({'symbolic_domain':'N>=2','moments':{k:str(v) for k,v in moments.items()},
                                  'spot_checks':rows,'N1':'F=-d^2 beta; Fsecond=0',
                                  'large_N_d4':{'Fprime':-4,'Fsecond':12}},indent=2)+'\n')


if __name__ == '__main__':
    main()
