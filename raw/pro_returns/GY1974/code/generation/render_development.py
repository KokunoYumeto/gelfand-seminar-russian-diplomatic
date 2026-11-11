"""Assemble the checked editorial verification appendices, without novelty claims."""
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parent
PARTS=ROOT/"parts"
OUT=ROOT/"GY1974"
intro=r"""\noindent No class C or D item met the selection criterion for a new research development. The following subsections are editorial verification audits: they prove corrections, state local reconstruction limits, and check conventions. The markers \ours{} and \oursComputed{} identify work performed for this companion, without asserting novelty. The final subsection audits adjacent pages already indexed in the preceding year; its 26 rows are not additional current-year occurrences.
"""
files=("early_audit.tex","middle_audit.tex","root_audit.tex","late_audit.tex","early_boundary.tex")
s=intro+"\n"+"\n\n".join((PARTS/f).read_text() for f in files)
s=s.replace(r"early\_code/exact\_checks.py",r"code/exact\_checks.py")
s=s.replace(r"\texttt{check\_dilogarithm.py}",r"\texttt{code/check\_dilogarithm.py}")
s=re.sub(r"\b(At|at|for|and|from|equal|The|November|records|of)(?=\d)",r"\1 ",s)
s=s.replace("AppendixA","Appendix A").replace(r"to\(\pi\)",r"to \(\pi\)")
s=s.replace("correspondingly opposite heat-exponential sign",
            "the opposite sign in the heat exponential")
# Separate result headings from the editorial marker and statement, so that
# a long theorem title and marker do not form an overwide first text line.
s=re.sub(r"(\\begin\{(?:theorem|proposition|lemma|corollary|remark|example)\}(?:\[[^\]]*\])?)(\\oursComputed|\\ours)\b",
         lambda m:m[1]+r"\leavevmode\par\noindent"+m[2]+r"\quad",s)
(OUT/"GY1974_development.tex").write_text(s)
print("Assembled five checked audit components.")
