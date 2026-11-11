"""Independent exact arithmetic audit of the two-soliton nonrigidity check.

This uses logarithmic-derivative moments, independently of the rational
vector-field derivative implementation in code/check_mathematics.py.
"""
from fractions import Fraction as Q
from pathlib import Path
import json

modes = [(0, 0), (2, -8), (4, -64), (6, -72)]
ratios = []
trials = []
for a in (Q(1), Q(2)):
    weights = [Q(1), a, a*a, a*a*a/9]
    moments = [sum(weight*k**j for weight, (k, omega) in zip(weights, modes))
               for j in range(4)]
    mixed = [sum(weight*omega*k**j for weight, (k, omega) in zip(weights, modes))
             for j in range(3)]
    M0, M1, M2, M3 = moments
    N0, N1, N2 = mixed
    qxxx = M3/M0 - 3*M2*M1/M0**2 + 2*M1**3/M0**3
    qxxt = N2/M0 - (2*N1*M1 + N0*M2)/M0**2 + 2*N0*M1**2/M0**3
    assert qxxx != 0
    ratios.append(qxxt/qxxx)
    trials.append(dict(r=str(a), s=str(a*a), Ux=str(-2*qxxx),
                       Ut=str(-2*qxxt), ratio=str(qxxt/qxxx)))
assert ratios[0] == -Q(92, 3)
assert ratios[1] == -Q(89524, 4861)
assert ratios[0] != ratios[1]
pair_values = {}
for i, (ki, wi) in enumerate(modes):
    for j, (kj, wj) in enumerate(modes):
        if i < j:
            pair_values[f'{i},{j}'] = (ki-kj)**4 + (ki-kj)*(wi-wj)
assert [pair_values[f'{i},{j}'] for i, j in ((0,1),(0,2),(1,3),(2,3))] == [0]*4
assert Q(pair_values['0,3'], 9) + pair_values['1,2'] == 0
report = dict(all_checks_passed=True, arithmetic='exact fractions',
              method='logarithmic derivative moments; unordered bilinear pairs',
              nonrigidity=trials, bilinear_pair_values=pair_values,
              scope='The uniform identity and Euclidean-motion argument are proved in late_review.md.')
path = Path(__file__).with_name('late_review_output.json')
path.write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
