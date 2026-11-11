#!/usr/bin/env python3
"""Independent exact and numerical checks for the GY1987 development.

Run from the package root:
    python code/verify_development.py > logs/development_checks.json

The proofs in GY1987_development.tex, not finite experiments, establish
the universal statements. Dependencies: Python 3, sympy, numpy.
"""
from fractions import Fraction as F
import json
import platform
import sys

import numpy as np
import sympy as sp


def coeff3(a):
    """Elementary coefficients by independent explicit determinant formulas."""
    tr = a[0][0] + a[1][1] + a[2][2]
    second = sum(
        a[i][i] * a[j][j] - a[i][j] * a[j][i]
        for i, j in [(0, 1), (0, 2), (1, 2)]
    )
    det = (
        a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
        + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
    )
    return tr, second, det


def check_stochastic(a):
    assert all(x >= 0 for row in a for x in row)
    assert all(sum(row) == 1 for row in a)


def real_realization(r, s):
    if r < 0 <= s:
        r, s = s, r
    if r >= 0:
        return [
            [(1 + s) / 2, (1 - s) / 2, F(0)],
            [(1 - s) / 2, (1 + s) / 2, F(0)],
            [1 - r, F(0), r],
        ]
    u, v = -r, -s
    return [
        [F(0), F(1), F(0)],
        [F(0), F(0), F(1)],
        [u * v, u + v - u * v, 1 - u - v],
    ]


def symbolic_checks():
    t, r, s, u, v, a, b = sp.symbols("t r s u v a b", real=True)
    c2 = sp.Matrix([[1+r, 1-r], [1-r, 1+r]]) / 2
    p_real = sp.Matrix([
        [(1+s)/2, (1-s)/2, 0],
        [(1-s)/2, (1+s)/2, 0],
        [1-r, 0, r],
    ])
    p_neg = sp.Matrix([[0,1,0], [0,0,1],
                      [u*v, u+v-u*v, 1-u-v]])
    p0 = (1+2*a)/3
    p1 = (1-a)/3 + b/sp.sqrt(3)
    p2 = (1-a)/3 - b/sp.sqrt(3)
    p_complex = sp.Matrix([[p0,p1,p2], [p2,p0,p1], [p1,p2,p0]])
    cases = [
        ("two_state", c2, (t-1)*(t-r)),
        ("three_real_with_nonnegative_member", p_real, (t-1)*(t-r)*(t-s)),
        ("three_real_both_negative", p_neg, (t-1)*(t+u)*(t+v)),
        ("three_complex_circulant", p_complex, (t-1)*((t-a)**2+b**2)),
    ]
    result = {}
    for name, mat, expected in cases:
        residual = sp.factor((t*sp.eye(mat.rows)-mat).det() - expected)
        assert residual == 0
        assert mat * sp.ones(mat.rows,1) == sp.ones(mat.rows,1)
        result[name] = {"determinant_residual": str(residual),
                        "row_sums": "identically one"}
    residual = sp.expand(3*(1+2*(a*a-b*b))-(1+2*a)**2)
    assert sp.expand(residual - 2*((1-a)**2-3*b*b)) == 0
    result["triangle_inequality_residual"] = str(sp.factor(residual))
    return result


def grid_checks():
    real_count = 0
    rejected_count = 0
    boundary_count = 0
    den = 40
    grid = [F(i, den) for i in range(-den, den+1)]
    for r in grid:
        for s in grid:
            if 1+r+s < 0:
                rejected_count += 1
                continue
            p = real_realization(r,s)
            check_stochastic(p)
            assert coeff3(p) == (1+r+s, r+s+r*s, r*s)
            real_count += 1
            boundary_count += int(1+r+s == 0 or abs(r) == 1 or abs(s) == 1)
    complex_count = 0
    complex_boundary = 0
    den = 48
    for i in range(den+1):
        for j in range(den-i+1):
            p0, p1, p2 = F(i,den), F(j,den), F(den-i-j,den)
            p = [[p0,p1,p2], [p2,p0,p1], [p1,p2,p0]]
            a, b2 = (3*p0-1)/2, 3*(p1-p2)**2/4
            check_stochastic(p)
            assert coeff3(p) == (1+2*a, 2*a+a*a+b2, a*a+b2)
            assert a >= -F(1,2) and a <= 1 and 3*b2 <= (1-a)**2
            complex_count += 1
            complex_boundary += int(min(p0,p1,p2) == 0)
    return {"real_grid_denominator": 40, "feasible_real_pairs": real_count,
            "trace_rejected_real_pairs": rejected_count,
            "real_boundary_cases": boundary_count,
            "circulant_simplex_denominator": 48,
            "circulant_exact_cases": complex_count,
            "circulant_boundary_cases": complex_boundary}


def random_checks(seed):
    rng = np.random.default_rng(seed)
    count = 0
    nonreal_three = 0
    max_modulus_excess = 0.0
    max_triangle_excess = 0.0
    for n in (2, 3, 5, 7):
        for _ in range(500):
            p = rng.integers(0, 30, size=(n,n)).astype(float)
            for row in p:
                if row.sum() == 0:
                    row[0] = 1
            p /= p.sum(axis=1,keepdims=True)
            ev = np.linalg.eigvals(p)
            max_modulus_excess = max(max_modulus_excess, float(np.max(abs(ev))-1))
            assert max(abs(ev)) <= 1+1e-10
            assert min(abs(ev-1)) <= 1e-10
            if n == 3:
                pair = [z for z in ev if abs(z.imag) > 1e-9]
                if pair:
                    nonreal_three += 1
                    for z in pair:
                        excess = abs(z.imag) - (1-z.real)/np.sqrt(3)
                        max_triangle_excess = max(max_triangle_excess,float(excess))
                        assert z.real >= -.5-1e-10 and excess <= 1e-10
                else:
                    assert sum(z.real for z in ev) >= -1e-10
            moments = {}
            for k in range(1,37):
                moments[k] = float(np.trace(np.linalg.matrix_power(p,k)))
                assert moments[k] >= -1e-10
            for k in range(1,7):
                for m in range(1,7):
                    assert moments[k]**m <= n**(m-1)*moments[k*m]+1e-9
            count += 1
    return {"seed":seed, "matrices":count,
            "nonreal_three_state_cases":nonreal_three,
            "maximum_modulus_excess":max_modulus_excess,
            "maximum_triangle_excess":max_triangle_excess}


def obstruction_checks():
    q = F(2,3)
    moments = {k:2+3*(-q)**k for k in range(1,64*32+1)}
    assert all(x >= 0 for x in moments.values())
    tests = 0
    for k in range(1,65):
        for m in range(1,33):
            assert moments[k]**m <= 5**(m-1)*moments[k*m]
            tests += 1
    partitions = []
    for k in range(4):
        traces = (1-q*k, 1-q*(3-k))
        assert min(traces) < 0
        partitions.append({"negative_counts":[k,3-k],
                           "block_traces":[str(x) for x in traces]})
    assert F(1)+2*F(-3,4) == -F(1,2)
    return {"power_sums_checked":64*32, "JLL_pairs_checked":tests,
            "first_four_moments":[str(moments[k]) for k in range(1,5)],
            "all_two_Perron_block_partitions_rejected":partitions,
            "diagnostic_only":"Finite checks do not prove universal JLL validity; see proof."}


def cohomology_linear_checks():
    ab = sp.Matrix([[5,-3],[-2,1]])
    assert ab.det() == -1
    # Adjoint actions of quaternion units i and j, contained in 2I.
    ri = sp.diag(1,-1,-1)
    rj = sp.diag(-1,1,-1)
    constraints = (ri-sp.eye(3)).col_join(rj-sp.eye(3))
    rank = constraints.rank()
    assert rank == 3
    diagonal = sp.eye(3).col_join(sp.eye(3))
    assert diagonal.rank() == 3
    return {"abelianization_relation_determinant":int(ab.det()),
            "adjoint_fixed_space_dimension":3-rank,
            "two_factor_cocycle_space_dimension":6,
            "principal_cocycle_rank":diagonal.rank(),
            "quotient_dimension":6-diagonal.rank(),
            "scope":"Checks the linear algebra; topological hypotheses are proved in the text."}


def tensor_angle_checks():
    """Direct tensor embeddings independently check the cross-Gram formula."""
    random_cases = 0
    construction_cases = 0
    max_gram_error = 0.0
    max_range_excess = 0.0
    max_construction_error = 0.0
    for seed in (737, 198822):
        rng = np.random.default_rng(seed)
        for field in ("real", "complex"):
            for d in range(1, 7):
                eye = np.eye(d)
                for _ in range(25):
                    a, b = rng.normal(size=(d,d)), rng.normal(size=(d,d))
                    if field == "complex":
                        a = a+1j*rng.normal(size=(d,d))
                        b = b+1j*rng.normal(size=(d,d))
                    a, b = a/np.linalg.norm(a), b/np.linalg.norm(b)
                    u = np.column_stack([np.kron(a.ravel(),eye[:,k]) for k in range(d)])
                    v = np.column_stack([np.kron(eye[:,i],b.ravel()) for i in range(d)])
                    direct = u.conj().T@v
                    formula = (a.conj()@b).T
                    err = float(np.max(abs(direct-formula)))
                    max_gram_error = max(max_gram_error,err)
                    assert err < 2e-13
                    cosines = np.linalg.svd(direct,compute_uv=False)
                    excess = float(cosines.sum()-1)
                    max_range_excess = max(max_range_excess,excess)
                    assert excess < 2e-13
                    if d == 1:
                        assert abs(cosines[0]-1) < 2e-13
                    random_cases += 1
        for d in range(2, 7):
            for rank in range(d+1):
                for total in (0.1,0.5,1.0):
                    s = np.zeros(d)
                    if rank:
                        weights = rng.uniform(.1,1,size=rank)
                        s[:rank] = total*weights/weights.sum()
                    if rank == 0:
                        a, b = np.zeros((d,d)), np.zeros((d,d))
                        a[0,0], b[1,1] = 1,1
                    elif rank < d:
                        a, b = np.zeros((d,d)), np.zeros((d,d))
                        for j in range(rank):
                            a[j,j] = np.sqrt(s[j]/total)
                            b[j,j] = np.sqrt(total*s[j])
                        b[rank,0] = np.sqrt(max(0,1-total**2))
                    else:
                        x0 = s/total
                        if total == 1:
                            x = x0
                        else:
                            boundary = np.ones(d)/(d-1)
                            boundary[0] = 0
                            lo,hi = 0.,1.
                            for _ in range(100):
                                alpha = (lo+hi)/2
                                trial = (1-alpha)*x0+alpha*boundary
                                if np.sum(s*s/trial) < 1:
                                    lo = alpha
                                else:
                                    hi = alpha
                            x = (1-lo)*x0+lo*boundary
                        a, b = np.diag(np.sqrt(x)), np.diag(s/np.sqrt(x))
                    error = max(float(np.max(abs(a@b-np.diag(s)))),
                                abs(float(np.linalg.norm(a))-1),
                                abs(float(np.linalg.norm(b))-1))
                    max_construction_error = max(max_construction_error,error)
                    assert error < 2e-10
                    construction_cases += 1
    return {"seeds":[737,198822],"explicit_tensor_embedding_cases":random_cases,
            "range_construction_cases":construction_cases,
            "maximum_cross_Gram_entry_residual":max_gram_error,
            "maximum_trace_norm_excess":max_range_excess,
            "maximum_realization_or_norm_residual":max_construction_error,
            "dimensions_checked":[1,2,3,4,5,6],
            "scope":"Numerical diagnostics independently form the tensor subspaces; the proof establishes all dimensions."}


if __name__ == "__main__":
    output = {"python":platform.python_version(),"sympy":sp.__version__,
              "numpy":np.__version__}
    output["symbolic"]=symbolic_checks()
    output["exact_grid"]=grid_checks()
    output["independent_random_runs"]=[random_checks(1987),random_checks(8811)]
    output["five_dimensional_obstruction"]=obstruction_checks()
    output["cohomology_linear_algebra"]=cohomology_linear_checks()
    output["tensor_angles"]=tensor_angle_checks()
    output["status"]="PASS"
    json.dump(output, sys.stdout, indent=2)
    print()
