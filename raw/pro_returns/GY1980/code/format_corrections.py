#!/usr/bin/env python3
"""Typeset reviewed formula fragments in the correction CSVs, idempotently.

Run from any directory. Only parts/*_corrections.csv, GY1980_corrections.csv,
and checks/correction_typesetting_output.txt are written. This is a formatting
pass: it neither repairs the source mathematics nor changes correction types.
Existing LaTeX math is protected. Explicit replacements, rather than a guess
at a general mathematical grammar, cover the inspected ninety-row apparatus.
"""

from __future__ import annotations

import argparse
import collections
import csv
import io
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIELDS = ["page", "place", "transcription_reads", "should_read", "evidence",
          "applies_to", "type"]
PROTECTED = {"page", "applies_to", "type"}

# Longer expressions precede their constituent symbols. Each replacement is
# applied only to text outside existing or newly inserted math delimiters.
# In a "transcription_reads" cell even a false/malformed equation is preserved.
REPLACEMENTS = [
    ("The coefficients of df(v) lie in O_X", r"The coefficients of \(df(v)\) lie in \(\mathcal O_X\)"),
    ("O_X tensor factor", r"\(\mathcal O_X\) tensor factor"),
    ("The boundary of I^n times I^m has dimension n+m-1", r"The boundary of \(I^n\times I^m\) has dimension \(n+m-1\)"),
    ("The actual scan has n+m.", r"The actual scan has \(n+m\)."),
    ("G_m into A^1 gives O(*0), with the proper submodule O", r"\(\mathbb G_m\) into \(\mathbb A^1\) gives \(\mathcal O(*0)\), with the proper submodule \(\mathcal O\)"),
    ("G_1^3", r"\(G_1^3\)"),
    ("G_n^m", r"\(G_n^m\)"),
    ("x_i=1, i=1,...,n+m", r"\(x_i=1\), \(i=1,\ldots,n+m\)"),
    ("H_fi", r"\(H_{f_i}\)"),
    ("(cos x,cos²x)", r"\((\cos x,\cos^2 x)\)"),
    ("y²=P_n(x)", r"\(y^2=P_n(x)\)"),
    ("sum c_ab x^a y^b = c_ab t^(an+bm)", r"\(\sum c_{ab}x^a y^b=c_{ab}t^{an+bm}\)"),
    ("x=t^n u(t), y=t^m v(t)", r"\(x=t^n u(t)\), \(y=t^m v(t)\)"),
    ("N=-sum ord_boundary(Q)", r"\(N=-\sum\operatorname{ord}_{\mathrm{boundary}}(Q)\)"),
    ("Euler characteristic = (-1)^(n-1) n! Vol(Delta)", r"Euler characteristic \(=(-1)^{n-1}n!\operatorname{Vol}(\Delta)\)"),
    ("Euler characteristic = -n! Vol(Delta)", r"Euler characteristic \(=-n!\operatorname{Vol}(\Delta)\)"),
    ("L=D^2-u; A=D^3-uD-Du; [L,A]=L_t", r"\(L=D^2-u\); \(A=D^3-uD-Du\); \([L,A]=L_t\)"),
    ("L=D^2+u, A=-4D^3-3(uD+Du), L_t=[L,A]", r"\(L=D^2+u\), \(A=-4D^3-3(uD+Du)\), \(L_t=[L,A]\)"),
    ("E_t (J(lambda)U) cross E", r"\(E_t\,(J(\lambda)U)\times E\)"),
    ("E_t=(J(lambda)U) cross E", r"\(E_t=(J(\lambda)U)\times E\)"),
    ("U_t=(JU) cross V", r"\(U_t=(JU)\times V\)"),
    ("Preserve U_t", r"Preserve \(U_t\)"),
    ("V_t is a plausible emendation", r"\(V_t\) is a plausible emendation"),
    ("N_F(R)=c V R^n+O(R^(n-1))", r"\(N_F(R)=cVR^n+O(R^{n-1})\)"),
    ("c=kappa_n n!/(2pi)^n", r"\(c=\kappa_n n!/(2\pi)^n\)"),
    ("e^z-1", r"\(e^z-1\)"),
    ("R/pi+O(1)", r"\(R/\pi+O(1)\)"),
    ("S(Delta)=integral product kappa_i dS", r"\(S(\Delta)=\int\prod_i\kappa_i\,dS\)"),
    ("R maps to -g^{-1} tensor g^{-1} R g tensor g", r"\(R\mapsto-(g^{-1}\otimes g^{-1})R(g\otimes g)\)"),
    ("S_{j_1k_3}^{k_1j_3}", r"\(S_{j_1k_3}^{k_1j_3}\)"),
    ("S_{i_1k_3}^{k_1j_3}", r"\(S_{i_1k_3}^{k_1j_3}\)"),
    ("[tr_3 S_13,tr_3 Sprime_13]=0", r"\([\operatorname{tr}_3 S_{13},\operatorname{tr}_3 S^{\prime}_{13}]=0\)"),
    ("[tr_1 S_13,tr_2 Sprime_23]=0", r"\([\operatorname{tr}_1 S_{13},\operatorname{tr}_2 S^{\prime}_{23}]=0\)"),
    ("R_12", r"\(R_{12}\)"),
    ("L6^2=L4^3+g1 L4+g0", r"\(L_6^2=L_4^3+g_1L_4+g_0\)"),
    ("L6^2=L4^3+g1 L+g0", r"\(L_6^2=L_4^3+g_1L+g_0\)"),
    ("L6=L^3+(3/2)(xL+Lx)=L^3+3xL+3D", r"\(L_6=L^3+\tfrac32(xL+Lx)=L^3+3xL+3D\)"),
    ("L6=L^3+3x^2 L+3Lx^2", r"\(L_6=L^3+3x^2L+3Lx^2\)"),
    ("A=L+x L^{-1}; L6=(A^3)_+", r"\(A=L+xL^{-1}\); \(L_6=(A^3)_+\)"),
    ("(A^3)_+=L^3+3xL+6D", r"\((A^3)_+=L^3+3xL+6D\)"),
    ("L+xL^{-1}-D L^{-2}", r"\(L+xL^{-1}-DL^{-2}\)"),
    ("T_k^ell", r"\(T_k^{\ell}\)"),
    ("gamma0=0 => q(x)=x", r"\(\gamma_0=0\Rightarrow q(x)=x\)"),
    ("gamma0=0 and q(x)=x", r"\(\gamma_0=0\) and \(q(x)=x\)"),
    ("V(Delta,...,Delta)=Vol(Delta)", r"\(V(\Delta,\ldots,\Delta)=\operatorname{Vol}(\Delta)\)"),
    ("number of roots=n! V", r"number of roots \(=n!V\)"),
    ("number of roots=V", r"number of roots \(=V\)"),
    ("formulation2V=S", r"formulation \(2V=S\)"),
    ("coefficient normalization S and diagonal normalization V", r"coefficient normalization \(S\) and diagonal normalization \(V\)"),
    ("S(Delta)", r"\(S(\Delta)\)"),
    ("0<c1<c2<1", r"\(0<c_1<c_2<1\)"),
    ("Phi-prime", r"\(\Phi^{\prime}\)"),
    ("positive on (0,1)", r"positive on \((0,1)\)"),
    ("p1(E)+p1(Q)=0", r"\(p_1(E)+p_1(Q)=0\)"),
    ("p1 of the complementary bundles", r"\(p_1\) of the complementary bundles"),
    ("with nm even", r"with \(nm\) even"),
    ("odd nm", r"odd \(nm\)"),
    ("symplectic M with", r"symplectic \(M\) with"),
    ("f(M) is convex", r"\(f(M)\) is convex"),
    ("For n≥2", r"For \(n\ge2\)"),
    ("degree n", r"degree \(n\)"),
    ("divisor of Q restricted", r"divisor of \(Q\) restricted"),
    ("(-1)-exceptional", r"\((-1)\)-exceptional"),
    ("0≥1", r"\(0\ge1\)"),
    ("u2=0", r"\(u_2=0\)"),
    ("Z2 conjugation", r"\(\mathbb Z_2\) conjugation"),
    ("quadrics in P3", r"quadrics in \(\mathbb P^3\)"),
    ("repeat j1", r"repeat \(j_1\)"),
    ("require i1", r"require \(i_1\)"),
    ("confirms tr3", r"confirms \(\operatorname{tr}_3\)"),
    ("The unscripted L is literal", r"The unscripted \(L\) is literal"),
    ("identify L4", r"identify \(L_4\)"),
    ("square root of L4", r"square root of \(L_4\)"),
    ("the commuting L6", r"the commuting \(L_6\)"),
    ("arbitrary rational q is", r"arbitrary rational \(q\) is"),
    ("zeta(1-i)", r"\(\zeta(1-i)\)"),
    ("zeta(-1)=-1/12", r"\(\zeta(-1)=-1/12\)"),
    ("A and alpha are scalar and v0 has three components", r"\(A\) and \(\alpha\) are scalar and \(v_0\) has three components"),
    ("L=-I+compact operator", r"\(L=-I+\text{compact operator}\)"),
    ("nu=1", r"\(\nu=1\)"),
    ("ell<n", r"\(\ell<n\)"),
    ("k<ell", r"\(k<\ell\)"),
    ("T is constant", r"\(T\) is constant"),
    ("p=p(rho)", r"\(p=p(\rho)\)"),
    ("x=xi+t f(xi)", r"\(x=\xi+t f(\xi)\)"),
    ("1+t fprime(xi)=0", r"\(1+t f^{\prime}(\xi)=0\)"),
    ("in R3", r"in \(\mathbb R^3\)"),
    ("Euclidean R3", r"Euclidean \(\mathbb R^3\)"),
    ("Gamma(Cmin)", r"\(\Gamma(C_{\min})\)"),
    ("Gamma(C)", r"\(\Gamma(C)\)"),
    ("unique Cmin and Cmax", r"unique \(C_{\min}\) and \(C_{\max}\)"),
    ("q-i and the real-codimension 2i", r"\(q-i\) and the real-codimension \(2i\)"),
    ("f in D", r"\(f\in\mathcal D\)"),
    ("O has the nonzero annihilator partial acting on 1, and D itself", r"\(\mathcal O\) has the nonzero annihilator \(\partial\) acting on \(1\), and \(\mathcal D\) itself"),
    ("scan clearly has C", r"scan clearly has \(\mathbb C\)"),
    ("require R.", r"require \(\mathbb R\)."),
    ("torus in C2", r"torus in \(\mathbb C^2\)"),
    ("The scan inspected: the symbol is i", r"The scan inspected: the symbol is \(i\)"),
    ("the symbol is i and", r"the symbol is \(i\) and"),
    ("Only R, C, H and Cayley", r"Only \(\mathbb R\), \(\mathbb C\), \(\mathbb H\) and Cayley"),
    ("precisely R, C, H, O even", r"precisely \(\mathbb R\), \(\mathbb C\), \(\mathbb H\), \(\mathbb O\) even"),
    ("M is a constant sheaf", r"\(M\) is a constant sheaf"),
    ("M defines a constant sheaf", r"\(M\) defines a constant sheaf"),
    ("calligraphic A.", r"calligraphic \(\mathcal A\)."),
    ("A general A-module", r"A general \(A\)-module"),
    ("right End(P)-modules", r"right \(\operatorname{End}(P)\)-modules"),
    ("Differentiating y delta=0 gives delta+y delta-prime=0", r"Differentiating \(y\delta=0\) gives \(\delta+y\delta^{\prime}=0\)"),
    ("B without a prime before A-prime and B in", r"\(B\) without a prime before \(A^{\prime}\) and \(B\) in"),
    ("the module M in", r"the module \(M\) in"),
    ("exponential parameter a.", r"exponential parameter \(a\)."),
    ("the manuscript writes U.", r"the manuscript writes \(U\)."),
]


def escaped(text: str, position: int) -> bool:
    backslashes = 0
    position -= 1
    while position >= 0 and text[position] == "\\":
        backslashes += 1
        position -= 1
    return backslashes % 2 == 1


def segments(text: str):
    """Yield (is_math, content), validating paired TeX math delimiters."""
    start = i = 0
    while i < len(text):
        if escaped(text, i):
            i += 1
            continue
        closing = None
        if text.startswith(r"\(", i):
            opening, closing = r"\(", r"\)"
        elif text.startswith(r"\[", i):
            opening, closing = r"\[", r"\]"
        elif text.startswith("$$", i):
            opening = closing = "$$"
        elif text[i] == "$":
            opening = closing = "$"
        elif text.startswith((r"\)", r"\]"), i):
            raise ValueError(f"Unmatched closing delimiter: {text!r}")
        if closing is None:
            i += 1
            continue
        if start < i:
            yield False, text[start:i]
        end = text.find(closing, i + len(opening))
        while end >= 0 and escaped(text, end):
            end = text.find(closing, end + len(closing))
        if end < 0:
            raise ValueError(f"Unclosed math delimiter: {text!r}")
        end += len(closing)
        yield True, text[i:end]
        start = i = end
    if start < len(text):
        yield False, text[start:]


def format_cell(text: str) -> str:
    for old, new in REPLACEMENTS:
        text = "".join(part if is_math else part.replace(old, new)
                       for is_math, part in segments(text))
    return text


def raw_math_characters(text: str):
    for is_math, part in segments(text):
        if not is_math:
            for i, char in enumerate(part):
                if char in "_^" and not escaped(part, i):
                    yield char


def serialize(rows):
    out = io.StringIO(newline="")
    writer = csv.DictWriter(out, fieldnames=FIELDS, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return out.getvalue()


def row_counter(rows):
    return collections.Counter(tuple(row[field] for field in FIELDS) for row in rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="validate without rewriting CSVs")
    args = parser.parse_args()
    paths = sorted((ROOT / "parts").glob("*_corrections.csv"))
    paths.append(ROOT / "GY1980_corrections.csv")
    log = ["Correction typesetting audit", "Mode: " + ("check" if args.check else "apply")]
    all_before, all_after = {}, {}
    total_changes = 0
    for path in paths:
        with path.open(encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle)
            if reader.fieldnames != FIELDS:
                raise ValueError(f"Header mismatch: {path}")
            before = list(reader)
        after = []
        changes = []
        for number, original in enumerate(before, 1):
            row = dict(original)
            for field in FIELDS:
                if row[field] is None:
                    raise ValueError(f"Missing cell: {path}:{number}:{field}")
                if field != "type":
                    row[field] = format_cell(row[field])
                    if list(raw_math_characters(row[field])):
                        raise ValueError(f"Bare underscore/caret: {path}:{number}:{field}: {row[field]!r}")
                    if format_cell(row[field]) != row[field]:
                        raise ValueError(f"Non-idempotent format: {path}:{number}:{field}")
                if field in PROTECTED and row[field] != original[field]:
                    raise ValueError(f"Metadata modified: {path}:{number}:{field}")
                if row[field] != original[field]:
                    changes.append((number, field, original[field], row[field]))
            after.append(row)
        if len(before) != len(after):
            raise ValueError(f"Row count changed: {path}")
        if collections.Counter(r["type"] for r in before) != collections.Counter(r["type"] for r in after):
            raise ValueError(f"Correction types changed: {path}")
        # A CSV round trip preserves every field, including evidence and types.
        if list(csv.DictReader(io.StringIO(serialize(after)))) != after:
            raise ValueError(f"CSV serialization mismatch: {path}")
        all_before[path] = before
        all_after[path] = after
        total_changes += len(changes)
        log.append(f"\n{path.relative_to(ROOT)}: {len(after)} rows; {len(changes)} changed cells")
        for number, field, old, new in changes:
            log.extend([f"  row {number}, {field}", f"    before: {old}", f"    after:  {new}"])
        log.append("  PASS: headers, row order/count, page/language/type metadata, and CSV round trip")
        log.append("  PASS: balanced math delimiters; no bare _/^ outside math; cellwise idempotence")

    main_path = ROOT / "GY1980_corrections.csv"
    if len(all_after[main_path]) != 90:
        raise ValueError("The main correction table must retain exactly 90 rows")
    batch_before = [row for path in paths[:-1] for row in all_before[path]]
    batch_after = [row for path in paths[:-1] for row in all_after[path]]
    if row_counter(batch_before) != row_counter(all_before[main_path]):
        raise ValueError("Main/batch input rows differ; do not silently reconcile them")
    if row_counter(batch_after) != row_counter(all_after[main_path]):
        raise ValueError("Main/batch output rows differ")

    # Validate everything before writing any CSV. Only changed CSVs are rewritten.
    written = 0
    if not args.check:
        for path in paths:
            if all_before[path] != all_after[path]:
                path.write_text(serialize(all_after[path]), encoding="utf-8", newline="")
                written += 1
    log.extend([
        "\nPASS: main table retains 90 rows; batch rows total 90",
        "PASS: the same formatting produces identical main/batch row multisets",
        f"Changed cells across all copies: {total_changes}; CSV files written: {written}",
        "PASS: only correction CSVs and this audit log are in the script's write scope",
        "",
    ])
    output = "\n".join(log)
    log_path = ROOT / "checks" / "correction_typesetting_output.txt"
    log_path.parent.mkdir(exist_ok=True)
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(output + "\n")
    print(output)
    if args.check and total_changes:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
