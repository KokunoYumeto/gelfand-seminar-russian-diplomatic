r"""Format the GY1985 correction rows without changing their critical readings.

Public API: format_rows(rows) -> new list of row dictionaries.

Only the four columns inserted as LaTeX by build_chapter.py are formatted.
Metadata (page, applies_to, type) is deliberately unchanged: the chapter builder
already escapes it. Existing \(...\), \[...\], $...$, and $$...$$ math blocks
are preserved byte-for-byte. Formula typography is explicit and context-bound;
there is no heuristic reinterpretation of an unknown algebraic expression.

Run this module to check all five supplied CSVs and write a before/after mapping,
an exact QA report, and a small LaTeX file containing the changed cells. Source
CSVs and other scripts are never modified.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path
from typing import Iterable, Mapping

LATEX_FIELDS = ("place", "transcription_reads", "should_read", "evidence")
SOURCE_FILES = (
    "early/corrections.csv",
    "strings/corrections.csv",
    "virasoro/corrections.csv",
    "late/corrections.csv",
    "strings/adjacent_corrections.csv",
)

# Each replacement changes formula typography or prose spacing only, preserving every assertion,
# including the mathematically false expressions in the transcription column.
# Explicit bracing is particularly important for L_-1, i_(ell(w)+1), and X_(i+n).
RULES: dict[tuple[str, str, str], list[tuple[str, str]]] = {}


def rule(page: str, place: str, field: str, *pairs: tuple[str, str]) -> None:
    RULES.setdefault((page, place, field), []).extend(pairs)


def math(source: str, latex: str) -> tuple[str, str]:
    return source, r"\(" + latex + r"\)"


# Early records.
rule("P001200", "Marginal Clifford relation", "evidence",
     math("2 delta_ik", r"2\delta_{ik}"))
rule("P001201", "Linear-independence comment", "evidence",
     math("1 and sin(t) on (0,10pi)", r"1\text{ and }\sin(t)\text{ on }(0,10\pi)"))
rule("P001202", "Pochhammer product", "evidence",
     math("(1;q^2)_infinity", r"(1;q^2)_\infty"))
rule("P001204", "Hermitian matrix condition", "evidence",
     math("conjugate(x_2)", r"\overline{x_2}"), math("x_2", r"x_2"))
rule("P001206", "All congruence curves are spheres", "transcription_reads",
     math("H/Gamma_n", r"\mathfrak H/\Gamma_n"))
rule("P001206", "Full modular group quotient", "transcription_reads",
     math("H/SL2(Z)", r"\mathfrak H/SL_2(\mathbb Z)"))

# String geometry records.
rule("P001210", "650, conformal adjoint", "evidence",
     math("L2", r"L^2"), math("exp((j+1)phi)", r"\exp((j+1)\varphi)"),
     math("exp(jphi)", r"\exp(j\varphi)"), math("T^{-j-1}", r"T^{-j-1}"))
rule("P001216", "651, final operator equality", "evidence",
     math("2(|xi|^2I+xi tensor xi)", r"2(|\xi|^2I+\xi\otimes\xi)"),
     math("|xi|^2I", r"|\xi|^2I"))
rule("P001221", "655, Dolbeault exact sequence", "evidence", math("T^j", r"T^j"))
rule("P001224", "656, first cubicle list", "should_read", math("h_t", r"h_t"))
rule("P001224", "656, recursion", "transcription_reads", math("i2", r"i_2"))
rule("P001224", "656, recursion", "should_read",
     math("i1", r"i_1"), math("i_j,i_{j+1}", r"i_j,i_{j+1}"))
rule("P001224", "656, cubicle size", "evidence", math("2^r", r"2^r"))
rule("P001225", "657, central convention", "transcription_reads",
     math("(j-i)", r"(j-i)"), math("(i^3-i)C", r"(i^3-i)C"))
rule("P001225", "657, central convention", "should_read",
     math("e_i=L_{-i}", r"e_i=L_{-i}"), math("C=-c", r"C=-c"))
rule("P001225", "657, Kac polynomial", "evidence",
     math("c=1,r=1,s=2", r"c=1,r=1,s=2"), math("(h-1/4)^2", r"(h-1/4)^2"))
rule("P001228", "657, last differential", "transcription_reads",
     math("dt1...dtn", r"dt_1\cdots dt_n"))
rule("P001228", "657, last differential", "should_read",
     math("dt1...dt_{n+m}", r"dt_1\cdots dt_{n+m}"))
rule("P001228", "657, screening integral", "evidence", math("t_u=t_v", r"t_u=t_v"))

# Virasoro records. Formula fragments in evidence retain their recorded signs.
rule("P001232-P001233", "Target index range", "transcription_reads",
     math("mu=0,...,d", r"\mu=0,\ldots,d"))
rule("P001232-P001233", "Target index range", "should_read",
     math("mu=0,...,d-1", r"\mu=0,\ldots,d-1"))
rule("P001233", "Coordinate Fourier summation", "transcription_reads",
     math("a_m", r"a_m"), math("exp(-in theta)/n", r"\exp(-in\theta)/n"))
rule("P001233", "Coordinate Fourier summation", "should_read", math("a_n", r"a_n"))
rule("P001235", "Two-vertex final bra", "transcription_reads", math("p+k1+k", r"p+k_1+k"))
rule("P001235", "Two-vertex final bra", "should_read", math("p+k1+k2", r"p+k_1+k_2"))
rule("P001236", "Spurion definition (2)", "transcription_reads",
     math("L_i v prime", r"L_i v'"), math("i<0", r"i<0"))
rule("P001236", "Weight equation (5)", "transcription_reads",
     math("L_-1 v prime=v", r"L_{-1}v'=v"),
     math("weight(v prime)=2", r"\operatorname{weight}(v')=2"))
rule("P001236", "Weight equation (5)", "should_read",
     math("Weight(v prime)=0", r"\operatorname{weight}(v')=0"),
     math("weight(v)=1", r"\operatorname{weight}(v)=1"))
rule("P001236", "Weight equation (5)", "evidence",
     math("[L0,L_-1]=L_-1", r"[L_0,L_{-1}]=L_{-1}"))
rule("P001237", "Creation exponential (6)", "transcription_reads",
     math("sum a_-n z^n", r"\sum a_{-n}z^n"), math("1/n", r"1/n"))
rule("P001237", "Creation exponential (6)", "should_read",
     math("sum a_-n z^n/n", r"\sum a_{-n}z^n/n"))
rule("P001237", "Correlation product (8)", "transcription_reads", math("j>1", r"j>1"))
rule("P001237", "Correlation product (8)", "should_read",
     math("1<=i<j<=n", r"1\le i<j\le n"))
rule("P001237", "Vertex residues (10)", "should_read",
     math("X=z^h Y", r"X=z^hY"), math("h=1", r"h=1"),
     math("Res X dz/z=Res Y dz", r"\operatorname{Res}X\,dz/z=\operatorname{Res}Y\,dz"))
rule("P001237", "Cartan condition (11)", "transcription_reads",
     math("A_ij<0", r"A_{ij}<0"))
rule("P001237", "Cartan condition (11)", "should_read",
     math("A_ii=2", r"A_{ii}=2"), math("A_ij<=0", r"A_{ij}\le0"))
rule("P001237", "Gelfand Monster remark", "evidence",
     math("8.08 times 10^53", r"8.08\times10^{53}"))
rule("P001239", "BGG top class", "transcription_reads", math("(xi-xj)", r"(x_i-x_j)"))
rule("P001239", "BGG top class", "should_read", math("(xi-xj)", r"(x_i-x_j)"))
rule("P001239", "BGG top class", "evidence",
     math("n=2", r"n=2"), math("x1-x2=2x1", r"x_1-x_2=2x_1"))
rule("P001240", "Divided-difference denominator", "transcription_reads",
     math("xi+1-xi", r"x_{i+1}-x_i"), math("f-s_i f", r"f-s_i f"))
rule("P001240", "Divided-difference denominator", "should_read",
     math("xi-xi+1", r"x_i-x_{i+1}"))
rule("P001240", "Divided-difference denominator", "evidence",
     math("n=2", r"n=2"), math("x1", r"x_1"), math("P_id=1", r"P_{\mathrm{id}}=1"))
rule("P001240", "Final adjacent transposition and operator", "transcription_reads",
     math("i_(ell(w)+1)", r"i_{\ell(w)+1}"))
rule("P001240", "Final adjacent transposition and operator", "should_read",
     math("i_(ell(w))+1", r"i_{\ell(w)}+1"))
rule("P001240", "Final adjacent transposition and operator", "evidence",
     math("(i_ell, i_ell+1)", r"(i_\ell,i_\ell+1)"))
rule("P001239-P001240", "Longest-element operator indexing", "transcription_reads",
     math("A_(w0 w^-1)", r"A_{w_0w^{-1}}"))
rule("P001239-P001240", "Longest-element operator indexing", "should_read",
     math("partial_(w^-1 w0)", r"\partial_{w^{-1}w_0}"))
rule("P001241", "Sugawara definition (1)", "transcription_reads",
     math("L_i=:sum a_m a_n:", r"L_i=:\!\sum a_m a_n\!:"))
rule("P001241", "Sugawara definition (1)", "should_read",
     math("L_i=(1/2):sum a_m a_n:", r"L_i=\tfrac12:\!\sum a_m a_n\!:"))
rule("P001241", "Classical vector fields", "transcription_reads",
     math("L_n=e^(int) d/dt", r"L_n=e^{int}\,d/dt"), math("(m-n)", r"(m-n)"))
rule("P001241", "Classical vector fields", "should_read",
     math("i e^(int) d/dt", r"i e^{int}\,d/dt"))
rule("P001241", "Norm-only Fock-module assertion", "transcription_reads",
     math("H_pprime", r"H_{p'}"), math("H_p", r"H_p"),
     math("p squared=pprime squared", r"p^2=(p')^2"))
rule("P001242", "Mode relation (12)", "transcription_reads",
     math("X(z)=sum X_i z^i", r"X(z)=\sum X_i z^i"),
     math("[a_n,X_i]=p X_(i+n)", r"[a_n,X_i]=pX_{i+n}"))
rule("P001242", "Mode relation (12)", "should_read",
     math("[a_n,X_i]=p X_(i-n)", r"[a_n,X_i]=pX_{i-n}"))
rule("P001242", "Mode relation (12)", "evidence",
     math("[a_n,X(z)]=p z^n X(z)", r"[a_n,X(z)]=p z^nX(z)"))
rule("P001243", "Cocycle paragraph", "transcription_reads",
     math("epsilon(a,b)epsilon(b,a)=(-1)^(a,b)", r"\epsilon(a,b)\epsilon(b,a)=(-1)^{(a,b)}"))

# Late records: a code filename is text, not an algebraic subscript.
rule("P001245", "Equations (1)--(2), exclusion of Lax pairs", "evidence",
     ("code/check_mathematics.py", r"\texttt{code/\allowbreak{}check\_\allowbreak{}mathematics.py}"))
rule("P001249", "Products of one-forms", "evidence", math("g-2", r"g-2"))
rule("P001250", "Wedge identity after equation (13)", "evidence",
     math("d tau=-2i d eta", r"d\tau=-2i\,d\eta"))
rule("P001253", "Equation (3), one-loop density", "evidence",
     math("q=e^{2pi i tau}", r"q=e^{2\pi i\tau}"))
rule("P001254", "Equation (7), Quillen metric", "evidence",
     math("T=a", r"T=a"), math("a^{-1}e/f", r"a^{-1}e/f"))
rule("P001255", "Determinant of the one-dimensional map", "evidence",
     math("E1 to E2", r"E_1\text{ to }E_2"), math("E1* tensor E2", r"E_1^*\otimes E_2"))

# Adjacent evidence.
rule("P001259", "ADJ-668 derivative vertex", "should_read",
     math("-ip_mu", r"-ip_\mu"), math("exp(ipX)", r"\exp(ipX)"))


# Prose spacing: exact source-cell contexts, never a global letter/digit rule.
# Source dates, identifiers, citation keys, and existing math remain literal.
PROSE_RULE_CELLS: set[tuple[str, str, str]] = set()


def prose_rule(page: str, place: str, field: str, *pairs: tuple[str, str]) -> None:
    rule(page, place, field, *pairs)
    PROSE_RULE_CELLS.add((page, place, field))


prose_rule("P001203-P001204", "Trace Paley-Wiener attribution", "evidence",
           ("received26August1985", "received 26 August 1985"))
prose_rule("P001204", "Bernstein variety equality", "evidence",
           ("Section2.1", "Section 2.1"))
prose_rule("P001204", "Paley-Wiener image conditions", "evidence",
           ("Section1.2", "Section 1.2"))
prose_rule("P001204", "Weil representation of similitude groups", "evidence",
           ("Section2", "Section 2"))
prose_rule("P001204", "Order of record headings", "transcription_reads",
           ("Feigin645", "Feigin 645"), ("Vigneras646", "Vigneras 646"))
prose_rule("P001204", "Order of record headings", "should_read",
           ("Vigneras646", "Vigneras 646"), ("in644", "in 644"),
           ("Feigin645", "Feigin 645"))
prose_rule("P001204", "Order of record headings", "evidence",
           ("still16September", "still 16 September"),
           ("record648", "record 648"), ("of23September", "of 23 September"))
prose_rule("P001206", "Inverse-limit quotient", "evidence",
           ("Arthur1981 Section2", "Arthur 1981 Section 2"))
prose_rule("P001206", "All congruence curves are spheres", "should_read",
           ("level6", "level 6"), ("genus1", "genus 1"),
           ("level7", "level 7"), ("genus3", "genus 3"))
prose_rule("P001206", "All congruence curves are spheres", "evidence",
           ("Example2.23", "Example 2.23"))
prose_rule("P001206", "Full modular group quotient", "evidence",
           ("Proposition2.21", "Proposition 2.21"))
prose_rule("P001207", "Euler product after almost-all qualifier", "evidence",
           ("Arthur1981 Section5", "Arthur 1981 Section 5"))
prose_rule("P001217", "source order", "transcription_reads",
           ("order652 then653", "order 652 then 653"))
prose_rule("P001217", "source order", "should_read",
           ("then652", "then 652"))
for page, record in (
        ("P001207 lower--P001209", "649"),
        ("P001210--P001212", "650"),
        ("P001213--P001216", "651"),
        ("P001219--P001221 upper", "654"),
        ("P001221 lower--P001222", "655"),
        ("P001223--P001224", "656"),
        ("P001225--P001228", "657")):
    prose_rule(page, f"record{record} boundary", "place",
               (f"record{record} boundary", f"record {record} boundary"))
prose_rule("P001248", "Knizhnik heading", "should_read",
           ("record664", "record 664"))
prose_rule("P001258-P001259", "Record ownership in the supplied catalogue page spans",
           "transcription_reads", ("record666", "record 666"))
prose_rule("P001258-P001259", "Record ownership in the supplied catalogue page spans",
           "should_read", ("Record666", "Record 666"),
           ("records667 and668", "records 667 and 668"))
prose_rule("P001258", "Kontsevich date", "evidence",
           ("dated24Feb86", "dated 24 Feb 86"),
           ("check:24Feb85", "check: 24 Feb 85"),
           ("Sunday,24Feb86", "Sunday, 24 Feb 86"),
           ("Monday,24Feb87", "Monday, 24 Feb 87"))
prose_rule("P001259", "Morozov date", "transcription_reads",
           ("Catalogue24February1987", "Catalogue 24 February 1987"))
prose_rule("P001259", "Morozov date", "should_read",
           ("Manuscript24February1986", "Manuscript 24 February 1986"))
prose_rule("P001259", "Morozov date", "evidence",
           ("writes24.2.86", "writes 24.2.86"),
           (r"Beilinson\textquotesingle s17Feb86", r"Beilinson\textquotesingle s 17 Feb 86"))
prose_rule("P001258", "ADJ-667 date", "transcription_reads",
           ("Manuscript24/II/85", "Manuscript 24/II/85"),
           ("catalogue24February1987", "catalogue 24 February 1987"))
prose_rule("P001258", "ADJ-667 date", "evidence",
           ("submittedDecember1986", "submitted December 1986"))
prose_rule("P001259", "ADJ-668 date", "transcription_reads",
           ("Manuscript24.2.86", "Manuscript 24.2.86"),
           ("catalogue24February1987", "catalogue 24 February 1987"))
prose_rule("P001258", "ADJ-667 moduli object", "evidence",
           ("Kontsevich1987section1", "Kontsevich 1987 section 1"))
prose_rule("P001258", "ADJ-667 marginal extension", "should_read",
           ("atp", r"at \(p\)"), ("throughp", r"through \(p\)"))
prose_rule("P001258", "ADJ-667 marginal extension", "evidence",
           ("atp", r"at \(p\)"), ("genus>=2", r"genus \(\ge2\)"))
prose_rule("P001259", "ADJ-668 Gaussian factor", "should_read",
           ("factor1/2", "factor 1/2"))
prose_rule("P001259", "ADJ-668 Gaussian factor", "evidence",
           ("Belavin--Knizhnik1986section6includes", "Belavin--Knizhnik 1986 section 6 includes"))


def _escaped(text: str, index: int) -> bool:
    """Whether the character at index is preceded by an odd backslash run."""
    n = 0
    index -= 1
    while index >= 0 and text[index] == "\\":
        n += 1
        index -= 1
    return bool(n % 2)


def split_math(text: str) -> list[tuple[bool, str]]:
    """Return (is_math, unchanged_segment), including delimiters in math parts."""
    result: list[tuple[bool, str]] = []
    plain_start = i = 0
    while i < len(text):
        if _escaped(text, i):
            i += 1
            continue
        if text.startswith(r"\(", i):
            opening, closing = r"\(", r"\)"
        elif text.startswith(r"\[", i):
            opening, closing = r"\[", r"\]"
        elif text.startswith("$$", i):
            opening = closing = "$$"
        elif text[i] == "$":
            opening = closing = "$"
        else:
            i += 1
            continue
        end = i + len(opening)
        while True:
            end = text.find(closing, end)
            if end < 0:
                raise ValueError(f"Unclosed math delimiter {opening!r} in {text!r}")
            if not _escaped(text, end):
                break
            end += len(closing)
        if i > plain_start:
            result.append((False, text[plain_start:i]))
        end += len(closing)
        result.append((True, text[i:end]))
        i = plain_start = end
    if plain_start < len(text):
        result.append((False, text[plain_start:]))
    return result


def _replace_plain(text: str, old: str, new: str) -> str:
    return "".join(part if is_math else part.replace(old, new)
                   for is_math, part in split_math(text))


# Unknown text is escaped rather than silently interpreted as a formula.
# The checked corpus uses explicit rules for every raw algebraic _ or ^.
_ESCAPES = {"_": r"\_", "^": r"\textasciicircum{}", "&": r"\&",
            "%": r"\%", "#": r"\#"}


def _escape_plain(text: str) -> str:
    return "".join(_ESCAPES.get(c, c) if not _escaped(text, i) else c
                   for i, c in enumerate(text))


def _format_cell(value: str, key: tuple[str, str, str]) -> str:
    for old, new in RULES.get(key, ()):
        value = _replace_plain(value, old, new)
    return "".join(part if is_math else _escape_plain(part)
                   for is_math, part in split_math(value))


def format_rows(rows: Iterable[Mapping[str, str]]) -> list[dict[str, str]]:
    """Copy and format correction rows, preserving metadata, order and count.

    This function is idempotent. It does not mutate any input mapping and does
    not alter existing math, source claims, classification, or record/page data.
    """
    result = []
    for source in rows:
        row = dict(source)
        page, place = source.get("page", ""), source.get("place", "")
        for field in LATEX_FIELDS:
            value = row.get(field)
            if isinstance(value, str):
                row[field] = _format_cell(value, (page, place, field))
        result.append(row)
    return result


def _hazards(text: str) -> list[str]:
    return [c for is_math, part in split_math(text) if not is_math
            for i, c in enumerate(part) if c in _ESCAPES and not _escaped(part, i)]


def _is_subsequence(needles: list[str], haystack: list[str]) -> bool:
    it = iter(haystack)
    return all(any(candidate == needle for candidate in it) for needle in needles)


def audit(work_root: Path, output_dir: Path) -> dict:
    """Audit the corpus, save its exact before/after mapping and a render fixture."""
    output_dir.mkdir(parents=True, exist_ok=True)
    mapping = []
    files = []
    matched_rules = set()
    fallback_algebra = []
    for name in SOURCE_FILES:
        path = work_root / name
        with path.open(encoding="utf-8", newline="") as stream:
            rows = list(csv.DictReader(stream))
        original = json.loads(json.dumps(rows))
        fixed = format_rows(rows)
        assert rows == original, f"Input mutated: {name}"
        assert len(rows) == len(fixed)
        assert format_rows(fixed) == fixed, f"Not idempotent: {name}"
        changed_rows = 0
        for index, (before, after) in enumerate(zip(rows, fixed), 1):
            assert before.keys() == after.keys()
            assert all(before[k] == after[k] for k in before if k not in LATEX_FIELDS)
            changed_rows += before != after
            for field in LATEX_FIELDS:
                old, new = before.get(field, ""), after.get(field, "")
                assert not _hazards(new), (name, index, field, _hazards(new))
                original_math = [p for m, p in split_math(old) if m]
                formatted_math = [p for m, p in split_math(new) if m]
                assert _is_subsequence(original_math, formatted_math), (name, index, field, "math altered")
                citation_pattern = r"\\cite[A-Za-z]*\*?(?:\[[^\]]*\])*\{[^}]*\}"
                assert re.findall(citation_pattern, old) == re.findall(citation_pattern, new), (
                    name, index, field, "citation command or key altered")
                key = (before.get("page", ""), before.get("place", ""), field)
                if key in RULES:
                    matched_rules.add(key)
                if old != new:
                    mapping.append(dict(file=name, row=index, page=before['page'],
                                        place=before['place'], field=field,
                                        before=old, after=new))
                    # A raw algebraic subscript must not have been cosmetically
                    # hidden by a fallback escape. The explicit filename rule is
                    # the sole intended text-underscore use in changed cells.
                    if r"\textasciicircum{}" in new or (r"\_" in new and "mathematics.py" not in new):
                        fallback_algebra.append(dict(file=name, row=index, field=field, after=new))
        files.append(dict(file=name, rows=len(rows), changed_rows=changed_rows))
    assert not fallback_algebra, fallback_algebra
    assert matched_rules == set(RULES), sorted(set(RULES) - matched_rules)

    # Delimiter and text-escaping regression probes. These test material risks:
    # double wrapping, mutation of existing math, escaped dollars, and idempotence.
    probes = [r"Existing \(a_m^2\) and \[A_{ij}\] and $q^2$ and $$r_n$$.",
              r"Already escaped \_ \^{} \& \% \# and dollar \$5.",
              "Text R&D at 50% uses item #3."]
    probe_results = []
    for value in probes:
        once = _format_cell(value, ("", "", ""))
        twice = _format_cell(once, ("", "", ""))
        assert once == twice
        assert not _hazards(once)
        probe_results.append(dict(before=value, after=once))
    assert probe_results[0]["before"] == probe_results[0]["after"]
    assert probe_results[1]["before"] == probe_results[1]["after"]
    assert probe_results[2]["after"] == r"Text R\&D at 50\% uses item \#3."

    report = dict(all_checks_passed=True, files=files, total_rows=sum(x['rows'] for x in files),
                  changed_cells=len(mapping), formula_rule_cells=len(set(RULES) - PROSE_RULE_CELLS),
                  prose_rule_cells=len(PROSE_RULE_CELLS), context_rule_cells=len(RULES),
                  original_math_preserved=True, citation_commands_preserved=True, metadata_unchanged=True,
                  input_not_mutated=True, idempotent=True,
                  raw_latex_hazards_remaining=0, fallback_algebra_escapes=0,
                  delimiter_probes=probe_results,
                  source_csvs_modified=False)
    (output_dir / 'format_corrections_mapping.json').write_text(
        json.dumps(mapping, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    (output_dir / 'format_corrections_qa.json').write_text(
        json.dumps(report, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    lines = [r'\documentclass[10pt]{article}', r'\usepackage[a4paper,margin=20mm]{geometry}',
             r'\usepackage{amsmath,amssymb,fontspec}', r'\setlength{\emergencystretch}{3em}',
             r'\begin{document}', r'\section*{Correction formatter: changed-cell render check}']
    for entry in mapping:
        label = f"{entry['page']}, row {entry['row']}, {entry['field']}"
        lines.extend([r'\par\noindent\textbf{'+_escape_plain(label)+r'}\par', entry['after']+r'\par\medskip'])
    lines.append(r'\end{document}')
    (output_dir / 'format_corrections_test.tex').write_text('\n'.join(lines)+'\n', encoding='utf-8')
    return report


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--work-root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--output-dir', type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args()
    print(json.dumps(audit(args.work_root, args.output_dir), ensure_ascii=False, indent=2))
