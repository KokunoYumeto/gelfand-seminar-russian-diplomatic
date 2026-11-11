#!/usr/bin/env python3
"""Independent floating-point diagnostics for the proved spectral examples.

The circle uses closed-form geometric sums versus direct eigenvalue sums.
The sphere is summed directly; a geometric tail bound is recorded.
The analytical arguments in the chapter, not these diagnostics, prove limits.
"""
import argparse
import cmath
import json
import math
from pathlib import Path


def pair(z):
    return {'real': z.real, 'imaginary': z.imag}


def circle_coefficient(epsilon, a, m, radius=1.0):
    z = (epsilon + 1j * m * a) / radius
    return epsilon / (2 * math.pi) * (1 + 2 / (cmath.exp(z) - 1))


def circle_direct(epsilon, a, m, radius=1.0):
    cutoff = math.ceil(45 * radius / epsilon)
    terms = [cmath.exp(-(epsilon + 1j * m * a) * k / radius)
             for k in range(1, cutoff + 1)]
    value = epsilon / (2 * math.pi) * (
        1 + 2 * complex(math.fsum(z.real for z in terms),
                        math.fsum(z.imag for z in terms)))
    rho = math.exp(-epsilon / radius)
    bound = epsilon / math.pi * rho ** (cutoff + 1) / (1 - rho)
    return value, cutoff, bound


def sphere_direct(epsilon):
    cutoff = math.ceil(40 / epsilon)
    terms = [(2 * ell + 1) * cmath.exp(
        -(epsilon + 2j * math.pi) * math.sqrt(ell * (ell + 1)))
             for ell in range(cutoff + 1)]
    value = epsilon / (2 * math.pi) * complex(
        math.fsum(z.real for z in terms), math.fsum(z.imag for z in terms))
    rho = math.exp(-epsilon)
    tail = epsilon / (2 * math.pi) * rho ** (cutoff + 1) * (
        (2 * cutoff + 3) / (1 - rho) + 2 * rho / (1 - rho) ** 2)
    return value, cutoff, tail


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path,
                        default=Path(__file__).resolve().parent.parent /
                        'computations/spectral_phase_check.json')
    args = parser.parse_args()
    circle = []
    max_error = 0.0
    for ratio in [2 / 3, math.sqrt(2)]:
        a = 2 * math.pi * ratio
        for epsilon in [0.2, 0.05, 0.01]:
            for m in [1, 2, 3, 7, 15, -3]:
                exact = circle_coefficient(epsilon, a, m)
                direct, cutoff, bound = circle_direct(epsilon, a, m)
                error = abs(exact - direct)
                max_error = max(error, max_error)
                assert error < 1e-10
                assert abs(exact) <= (epsilon + 2) / (2 * math.pi) + 1e-12
                circle.append({'a_over_2piR': ratio, 'epsilon': epsilon,
                               'm': m, 'closed_formula': pair(exact),
                               'direct_sum': pair(direct), 'absolute_difference': error,
                               'cutoff': cutoff, 'exact_arithmetic_tail_bound': bound})
    sphere = []
    for epsilon in [0.2, 0.1, 0.05, 0.02, 0.01, 0.005, 0.002]:
        value, cutoff, bound = sphere_direct(epsilon)
        scaled = epsilon * value
        sphere.append({'epsilon': epsilon, 'coefficient': pair(value),
                       'epsilon_times_coefficient': pair(scaled),
                       'distance_to_minus_one_over_pi': abs(scaled + 1 / math.pi),
                       'cutoff': cutoff, 'exact_arithmetic_tail_bound': bound})
    assert sphere[-1]['distance_to_minus_one_over_pi'] < 0.002
    result = {
        'purpose': 'Diagnostics; not a replacement for the complete proofs.',
        'normalization': 'hat T(m)=(2pi)^-1<T,exp(-im mu)>',
        'circle_closed_form_vs_direct_sum_passed': True,
        'circle_uniform_bound_samples_passed': True,
        'max_circle_difference': max_error,
        'circle': circle,
        'sphere': sphere,
        'caveat': 'Tail bounds are analytical truncation bounds, not interval-arithmetic bounds on floating-point roundoff.'
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k not in ['circle', 'sphere']}, indent=2))
    print('sphere epsilon*coefficient:', sphere[-1]['epsilon_times_coefficient'])


if __name__ == '__main__':
    main()
