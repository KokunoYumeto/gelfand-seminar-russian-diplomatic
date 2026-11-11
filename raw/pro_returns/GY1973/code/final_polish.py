#!/usr/bin/env python3
"""Apply the final typography corrections to the audited fragment data."""
from pathlib import Path
import argparse
import csv
import json

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--fragments",type=Path,default=Path(__file__).resolve().parent/"fragments")
    root=p.parse_args().fragments
    replacements={
      "agenda":{
        ("1973-302.14","notes"):r"The bracket contains the doubtful word \ru{неприводимыми}. It asks for finitely many relations among different such objects."},
      "manin_fuchs":{
        ("1973-304.5","statement"):r"On each component of character space, the uniform moderate-growth bound on the distribution makes its Mellin transform analytic on the open unit disc of the character parameter. For integer-power characters \(x\mapsto x^n\), fix \(n\bmod(p-1)\) when \(p\) is odd.",
        ("1973-306.8","reconstruction"):r"The star homomorphism supplies the second unitary relation. A single displayed relation permits a coisometry whose kernel has infinite dimension. Such an operator is not Fredholm.",
        ("1973-308.7","fate"):r"The usual comparison between realization and singular complexes underlies the constructions of classifying spaces in \citet[Chapter~IV, \S3]{weibel2013kbook}."},
      "autumn_representations":{
        ("1973-317.1","statement"):r"For the symplectic frame bundle \(\operatorname{Fr}_{\operatorname{Sp}}(TM)\), form \[\Lambda(TM)=\operatorname{Fr}_{\operatorname{Sp}}(TM)\times_{\operatorname{Sp}(2n,\mathbb R)}\Lambda(n)\longrightarrow M,\qquad \Lambda(n)\cong U(n)/O(n).\] Its fibre consists of all Lagrangian subspaces of \(T_xM\). A section is a Lagrangian distribution, which need not be integrable or globally exist."},
      "spring_integrable":{
        ("1973-329.7","statement"):r"With output-first kernel \(K(y,x)\), define \[C_P=\{(y,\eta;x,\xi):(y,\eta;x,-\xi)\in WF(K)\}.\] Using input-first ordering, the same relation is written \[\{(x,\xi;y,\eta):(x,-\xi;y,\eta)\in WF(K)\}.\] Thus it is the input covector that must change sign when the relation acts on \(WF(u)\) without another sign reversal.",
        ("1973-330.3","notes"):r"The notes assert uniqueness: \ru{можно док., что оно единственно}.",
        ("1973-331.3","fate"):r"\citet[\S4, pp.~370--373]{araki1970factorizable} gives the construction in Fock space and exponential vectors before the seminar. The Hilbert direct sum and its normalization are standard explanatory background. Related constructions occur at 1969-180.7--180.8 and 1970-228.5; these are conceptual continuations, not repeated problem IDs."}}
    total=0
    for owner,changes in replacements.items():
        path=root/owner/"items.json";data=json.loads(path.read_text())
        for item in data:
            for (key,field),value in changes.items():
                if item["id"]==key:
                    item[field]=value;total+=1
        path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n")
    path=root/"manin_fuchs/corrections.csv"
    with path.open(newline="",encoding="utf-8") as f:
        reader=csv.DictReader(f);names=reader.fieldnames;rows=list(reader)
    for row in rows:
        if row["place"]=="speaker attribution" and row["page"]=="P000519-P000520":
            row["should_read"]="Retain these interventions in record 309 and attribute them to A. S. Mishchenko."
    with path.open("w",newline="",encoding="utf-8") as f:
        writer=csv.DictWriter(f,fieldnames=names);writer.writeheader();writer.writerows(rows)
    print("Applied",total,"typographical item revisions and the intervention-spacing revision.")

if __name__=="__main__":main()
