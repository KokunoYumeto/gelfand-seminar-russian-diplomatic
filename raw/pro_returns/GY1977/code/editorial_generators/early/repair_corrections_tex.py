#!/usr/bin/env python3
"""Idempotently repair display-cell TeX in the 24 early corrections.

The original prose remains in write_audit.py.  Its generator calls repair_rows
before writing the CSV; this script also repairs an existing CSV in place.
Every replacement accepts only its exact original or already repaired value.
Metadata, row order, row count, and all other display cells remain unchanged.
"""
from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path
import re

DISPLAY_FIELDS = ('place', 'transcription_reads', 'should_read', 'evidence')
METADATA_FIELDS = ('page', 'applies_to', 'type')
REPAIRS = {
    ('Projective quotient notation', 'transcription_reads'): (
        'C^4/C^* and H^2/H^*',
        r'$\mathbb{C}^{4}/\mathbb{C}^{*}$ and $\mathbb{H}^{2}/\mathbb{H}^{*}$'),
    ('Quaternionic real structure', 'should_read'): (
        'On C^4 the lift J has J^2=-1; the induced projective map has square 1.',
        r'On $\mathbb{C}^{4}$ the lift $J$ has $J^{2}=-1$; the induced projective map has square $1$.'),
    ('Instanton/bundle correspondence', 'transcription_reads'): (
        'Self-dual connections correspond to holomorphic bundles on CP^3.',
        r'Self-dual connections correspond to holomorphic bundles on $\mathbb{CP}^{3}$.'),
    ('Manin algebraic-type criterion', 'transcription_reads'): (
        'L_3 not in C[L_1,L_2]',
        r'$L_{3}\notin\mathbb{C}[L_{1},L_{2}]$'),
    ('Manin algebraic-type criterion', 'should_read'): (
        'Retain the expression with an ambiguity note: L_2 is a time-evolution operator in a Lax pair and need not commute with L_1.',
        r'Retain the expression with an ambiguity note: $L_{2}$ is a time-evolution operator in a Lax pair and need not commute with $L_{1}$.'),
    ('Algebraic matrix-entry rigidity', 'transcription_reads'): (
        'Every lattice in SL(n,R) is conjugate to matrices with algebraic entries.',
        r'Every lattice in $\mathrm{SL}(n,\mathbb{R})$ is conjugate to matrices with algebraic entries.'),
    ('Algebraic matrix-entry rigidity', 'should_read'): (
        'Impose the higher-rank hypotheses, in particular n>=3 for this formulation.',
        r'Impose the higher-rank hypotheses, in particular $n\geq3$ for this formulation.'),
    ('Algebraic matrix-entry rigidity', 'evidence'): (
        'P710 scan; Tits1977 superrigidity/arithmeticity statement. The n=2 formulation admits deformations and is false without qualification.',
        r'P710 scan; Tits1977 superrigidity/arithmeticity statement. The $n=2$ formulation admits deformations and is false without qualification.'),
    ('Nonarchimedean places', 'transcription_reads'): (
        'Use Q_p for the p-adic realization of the number-field coefficients.',
        r'Use $\mathbb{Q}_{p}$ for the $p$-adic realization of the number-field coefficients.'),
    ('Nonarchimedean places', 'should_read'): (
        'For a coefficient field K use all nonarchimedean completions K_v, or the equivalent restriction-of-scalars representation over Q_p.',
        r'For a coefficient field $K$ use all nonarchimedean completions $K_{v}$, or the equivalent restriction-of-scalars representation over $\mathbb{Q}_{p}$.'),
    ('Unknown-sign counterfeit puzzle', 'evidence'): (
        'P713 scan confirms 13. Complete independent balanced-ternary construction, upper bound and physical-pan check are in coin_annotation.tex and coin_check_output.json; this is an ambiguity in the success criterion, not a digit error.',
        r'P713 scan confirms 13. Complete independent balanced-ternary construction, upper bound and physical-pan check are in \texttt{coin\_annotation.tex} and \texttt{coin\_check\_output.json}; this is an ambiguity in the success criterion, not a digit error.'),
    ('Binary entropy', 'transcription_reads'): (
        'H=p log p+(1-p) log(1-p)',
        r'$H=p\log p+(1-p)\log(1-p)$'),
    ('Binary entropy', 'should_read'): (
        'H=-p log p-(1-p) log(1-p)',
        r'$H=-p\log p-(1-p)\log(1-p)$'),
    ('Binary entropy', 'evidence'): (
        'P714 scan confirms the missing leading negative sign in the original notebook. Shannon1948 §6 and positivity at p=1/2 verify the emendation.',
        r'P714 scan confirms the missing leading negative sign in the original notebook. Shannon1948 §6 and positivity at $p=1/2$ verify the emendation.'),
    ('Ideal-gas entropy schematic formula', 'transcription_reads'): (
        'S=ln(V/N)',
        r'$S=\ln(V/N)$'),
    ('Ideal-gas entropy schematic formula', 'should_read'): (
        'Treat this as the volume-dependent entropy per particle in units k_B, up to temperature-dependent and additive terms; use Delta S/N=k_B ln(V_f/V_i) at fixed temperature.',
        r'Treat this as the volume-dependent entropy per particle in units $k_{B}$, up to temperature-dependent and additive terms; use $\Delta S/N=k_{B}\ln(V_{f}/V_{i})$ at fixed temperature.'),
    ('Solar-mass Schwarzschild radius', 'evidence'): (
        'P715 scan confirms 7. Evaluation 2(GM_sun)/c^2 with nominal GM_sun from Prsa et al.2016 Table1 gives 2.95325 km; the notebook error is faithfully transcribed.',
        r'P715 scan confirms 7. Evaluation $2(GM_{\odot})/c^{2}$ with nominal $GM_{\odot}$ from Prsa et al.2016 Table1 gives 2.95325 km; the notebook error is faithfully transcribed.'),
    ('Ground-state ket', 'transcription_reads'): (
        'H|Phi>=E_0|phi>',
        r'$H\lvert\Phi\rangle=E_{0}\lvert\phi\rangle$'),
    ('Acceleration temperature', 'transcription_reads'): (
        'kT=ha/c',
        r'$kT=ha/c$'),
    ('Acceleration temperature', 'should_read'): (
        'k_B T= hbar a/(2 pi c), with hbar explicitly distinguished from Planck h.',
        r'$k_{B}T=\hbar a/(2\pi c)$, with $\hbar$ explicitly distinguished from Planck $h$.'),
    ('Acceleration temperature', 'evidence'): (
        'P716 scan and transcribed TikZ formula inspected. Crispino--Higuchi--Matsas2008 thermal formulas verify the coefficient; if h means ordinary Planck constant the denominator is 4 pi^2 c.',
        r'P716 scan and transcribed TikZ formula inspected. Crispino--Higuchi--Matsas2008 thermal formulas verify the coefficient; if $h$ means ordinary Planck constant the denominator is $4\pi^{2}c$.'),
    ('Schwartz local-functional exercise', 'transcription_reads'): (
        'Integral over R of a differential polynomial is used without restricting its constant term.',
        r'Integral over $\mathbb{R}$ of a differential polynomial is used without restricting its constant term.'),
    ('Schwartz local-functional exercise', 'should_read'): (
        'Require f(0)=0 for this integral on all Schwartz tuples; ker(Euler derivative)=C+D(A), and constants must be separated.',
        r'Require $f(0)=0$ for this integral on all Schwartz tuples; $\ker(\text{Euler derivative})=\mathbb{C}+D(A)$, and constants must be separated.'),
    ('Schwartz local-functional exercise', 'evidence'): (
        'P717 scan and Gelfand--Dikii1977 §1 read. A nonzero constant density is not integrable on R; the formal kernel also includes constants.',
        r'P717 scan and Gelfand--Dikii1977 §1 read. A nonzero constant density is not integrable on $\mathbb{R}$; the formal kernel also includes constants.'),
}


def display_errors(text: str) -> list[str]:
    """Check the simple inline TeX grammar used by these display cells."""
    errors = []
    in_math = False
    braces = 0
    i = 0
    while i < len(text):
        ch = text[i]
        if ch == '\\':
            if i + 1 == len(text):
                errors.append('trailing backslash')
                break
            if not text[i + 1].isalpha():
                i += 2
                continue
            command = re.match(r'\\[A-Za-z]+', text[i:]).group()
            i += len(command)
            if command in (r'\url', r'\path', r'\nolinkurl') and i < len(text) and text[i] == '{':
                end = text.find('}', i + 1)
                if end < 0:
                    errors.append('unclosed URL/path argument')
                    break
                i = end + 1
            continue
        if ch == '$':
            in_math = not in_math
        elif ch == '{':
            braces += 1
        elif ch == '}':
            braces -= 1
            if braces < 0:
                errors.append('closing brace without opening brace')
        elif ch in '_^=<>|' and not in_math:
            errors.append(f'raw math character {ch!r} at offset {i}')
        elif ch in '&#%':
            errors.append(f'unescaped TeX special character {ch!r} at offset {i}')
        i += 1
    if in_math:
        errors.append('unclosed inline math delimiter')
    if braces:
        errors.append(f'unbalanced braces: {braces}')
    without_urls = re.sub(r'\\url\{[^}]*\}', '', text)
    if re.search(r'https?://', without_urls):
        errors.append('URL outside \\url{}')
    return errors


def repair_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    repaired = [dict(row) for row in rows]
    found = set()
    for row in repaired:
        for field in DISPLAY_FIELDS:
            key = (row['place'], field)
            if key in REPAIRS:
                old, new = REPAIRS[key]
                if row[field] not in (old, new):
                    raise ValueError(f'Refusing to overwrite unexpected content: {key}')
                row[field] = new
                found.add(key)
            errors = display_errors(row[field])
            if errors:
                raise ValueError(f'{row["page"]} {row["place"]} {field}: {errors}')
    if found != set(REPAIRS):
        raise ValueError(f'Expected correction cells absent: {set(REPAIRS) - found}')
    assert len(repaired) == len(rows)
    assert [[r[k] for k in METADATA_FIELDS] for r in repaired] == [
        [r[k] for k in METADATA_FIELDS] for r in rows]
    return repaired


def main() -> None:
    path = Path(__file__).resolve().parent / 'corrections.csv'
    before = path.read_bytes()
    with path.open(newline='', encoding='utf-8') as stream:
        reader = csv.DictReader(stream)
        fieldnames = reader.fieldnames
        original = list(reader)
    repaired = repair_rows(original)
    changed = [{'row': i, 'page': old['page'], 'place': old['place'],
                'field': key} for i, (old, new) in enumerate(zip(original, repaired), 1)
               for key in DISPLAY_FIELDS if old[key] != new[key]]
    assert repair_rows(repaired) == repaired
    with path.open('w', newline='', encoding='utf-8') as stream:
        writer = csv.DictWriter(stream, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(repaired)
    audit = {
        'rows_before': len(original), 'rows_after': len(repaired),
        'metadata_and_order_preserved': True, 'idempotence_verified': True,
        'display_cells_checked': len(repaired) * len(DISPLAY_FIELDS),
        'validation_errors': [], 'changed_cells': changed,
        'sha256_before': hashlib.sha256(before).hexdigest(),
        'sha256_after': hashlib.sha256(path.read_bytes()).hexdigest(),
    }
    (path.parent / 'corrections_tex_audit.json').write_text(
        json.dumps(audit, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'Validated {len(repaired)} rows / {len(repaired) * len(DISPLAY_FIELDS)} display cells; repaired {len(changed)} cells.')


if __name__ == '__main__':
    main()
