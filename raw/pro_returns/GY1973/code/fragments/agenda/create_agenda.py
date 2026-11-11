"""Generate the independently researched record 302 contribution."""
from pathlib import Path
import json, csv
D=Path(__file__).resolve().parent
items=[]
def add(title,kind,notes,statement,cls,fate,status,refs=(),**kw):
    x=dict(id=f"1973-302.{len(items)+1}",record=302,pages="P000501",
      kind=kind,title=title,notes=notes,statement=statement,reconstruction="",
      fate=fate,present_status="As of 9 November 2026: "+status,
      literal_correctness="correct",publication_match="exact",verification="read the result",
      development="none",problem="",worth="",refs=list(refs),confidence="high")
    x["class"]=cls;x.update(kw);items.append(x)

add("Lichtenbaum's special-value programme in the agenda","conjecture",
 r"Plan item 4 announces \ru{Гипотеза Лихтенбаума} connecting \(\zeta\)-values at integers with higher \(K\)-theories; Manin is the prospective expositor.",
 r"No field, scheme, integer range, leading-term convention, regulator or torsion factor is specified. A programme relating special values and algebraic \(K\)-groups is identifiable, but a unique quantified conjecture is not.",
 "F",r"\citet{lichtenbaum1973values} is a contemporary thematic match: Seattle conference 1972, publication 1973. The notes do not identify a particular conjecture of that paper.",
 "The agenda sentence has no single solved/open truth value and is not a definite problem.",
 ["lichtenbaum1973values"],literal_correctness="not determinable",publication_match="thematic only",
 verification="publisher metadata checked",confidence="medium")

add("Unresolved name in the planned Weil discussion","remark",
 r"Plan item 5 reads \ru{Вей: идеология Герстенцуса}; the surname is already marked doubtful.",
 r"No proposition can be recovered from this uncertain name and the word \textit{ideology}.",
 "F","The scan was compared with both transcriptions. Searches for the supplied Cyrillic form and plausible transliterations did not establish a unique work. No identification with Gersten or Gerstenhaber is asserted.",
 "Unidentified agenda label, not evidence of an undeveloped idea.",
 literal_correctness="not determinable",publication_match="none found",verification="unresolved lead",confidence="low")

add("Finite generation of the two function-field families","claim",
 r"For finite \(k\), the notes assert finite generation of \(\mathrm{SL}_n(k[t])\), \(n\geq3\), and \(\mathrm{SL}_n(k[t,t^{-1}])\), \(n\geq2\).",
 r"For every finite field \(\mathbb F_q\), both families are finitely generated in the displayed ranges.",
 "E",r"The pre-1973 result is credited to Behr 1969 and Harder's reduction theory in \citet[p.~312]{buxkohlwitzel2013rank}.",
 "Established. Finite generation alone does not imply finite presentation.",
 ["buxkohlwitzel2013rank"])

add("Serre's finite-presentation question over a polynomial ring","question",
 r"Are \(\mathrm{SL}_n(k[t])\), \(k\) finite and \(n\geq3\), finitely presented?",
 r"For every prime power \(q\) and integer \(n\geq3\), determine finite presentability of \(\mathrm{SL}_n(\mathbb F_q[t])\).",
 "B",r"No at \(n=3\); yes at \(n\geq4\). The Rank Theorem gives finiteness length \(n-2\) \citep[p.~312]{buxkohlwitzel2013rank}. It credits the complete finite-presentation criterion to Behr 1998. General-rank preprint 2011, final 2013; these are not asserted to be first dates for each special case.",
 "Completely answered, including small finite fields.",
 ["buxkohlwitzel2013rank","serre1974problems"],problem="GP-1973-01")

add("Serre's finite-presentation question over a Laurent ring","question",
 r"The same question is posed for \(\mathrm{SL}_n(k[t,t^{-1}])\), \(k\) finite, \(n\geq2\).",
 r"For every finite field \(\mathbb F_q\) and integer \(n\geq2\), determine finite presentability of \(\mathrm{SL}_n(\mathbb F_q[t,t^{-1}])\).",
 "B",r"The rank sum is \(2(n-1)\), and finiteness length \(2n-3\): no at \(n=2\), yes at \(n\geq3\) \citep[p.~312]{buxkohlwitzel2013rank}. The complete finite-presentation criterion was already established by Behr 1998.",
 r"Completely answered. Replacing \(\mathbb F_q\) by \(\mathbb Z\) changes the problem.",
 ["buxkohlwitzel2013rank","serre1974problems"],problem="GP-1973-02")

add("Coherence of a group","definition",
 r"\ru{Когер. группа}: every subgroup with finitely many generators is finitely presented.",
 r"A group \(G\), not necessarily finitely generated, is coherent when every finitely generated subgroup \(H\leq G\) is finitely presented.",
 "E",r"This is the group-theoretic property in Serre's questions \citep[pp.~734--735]{serre1974problems}. Requiring the ambient group to be finitely presented would improperly exclude the question about \(\mathrm{GL}_n(\mathbb Q)\).",
 "Standard terminology; unrelated to sheaf or ring coherence.",
 ["serre1974problems"],verification="indirect")

add("Free groups are coherent","claim",
 "The notes say that free groups are coherent.",
 "Every subgroup of a free group is free. A finitely generated such subgroup has finite rank and a finite presentation with no relators.",
 "E",r"This is the classical Nielsen--Schreier implication; free coherent groups are recalled in \citet[section~4]{brody2025commensurator}.",
 "Established, even if the ambient free group has infinite rank.",["brody2025commensurator"])

add("Nilpotent groups are coherent","claim",
 r"The faint abbreviation following free is read as \ru{нильпот.}.",
 "Every finitely generated subgroup of a nilpotent group is finitely generated nilpotent, hence polycyclic and finitely presented.",
 "E",r"This is the classical polycyclic implication; see the coherent classes recalled in \citet[section~4]{brody2025commensurator}. The scan supports the transmitted abbreviation.",
 "Established; torsion-freeness and finite generation of the ambient group are unnecessary.",
 ["brody2025commensurator"])

add("Scott's coherence theorem for three-manifold groups","theorem",
 "The notebook explicitly cites Scott, JLMS(2)6(1973),437--440, for coherence of three-manifold fundamental groups.",
 r"For a connected second-countable three-manifold \(M\), with or without boundary, every finitely generated subgroup of \(\pi_1(M)\) is finitely presented: apply Scott's theorem to the corresponding connected covering.",
 "E",r"\citet[section~2]{scott1973finitely} is the exact work, published May 1973, before this meeting. Its original introductory statement was read in the author's collected works.",
 "Established. The covering-space argument supplies the subgroup quantifier.",
 ["scott1973finitely"])

add("The imaginary-quadratic arithmetic example","claim",
 r"\(\mathrm{SL}_2(\Lambda)\) is called coherent, with \(\Lambda\) described as \ru{чисто мнимые элем. квадр. поля}.",
 r"For an imaginary quadratic number field \(K\), \(\mathrm{SL}_2(\mathcal O_K)\) is coherent, where \(\mathcal O_K\) is its ring of integers.",
 "E",r"This is the expected Bianchi-group consequence of \citet{scott1973finitely}: use a torsion-free finite-index subgroup and stability of coherence under finite extensions.",
 "The reconstruction is established. Purely imaginary elements themselves are not a unital coefficient ring.",
 ["scott1973finitely"],reconstruction="Replacing the transmitted description by the ring of integers is a mathematical reconstruction, not a new reading of the ink.",
 literal_correctness="correct with missing hypotheses",publication_match="partial",verification="indirect",confidence="medium")

add("Is SL3(Z) coherent?","question",
 r"The notes explicitly ask whether \(\mathrm{SL}_3(\mathbb Z)\) is coherent.",
 r"Is every finitely generated subgroup \(H\leq\mathrm{SL}_3(\mathbb Z)\) finitely presented?",
 "C",r"The question remains explicit and open in \citet[p.~5]{audibert2025zariski}. Incoherence in ranks \(n\geq4\) does not answer it.",
 "No unconditional resolution was found in the dated search; the universal subgroup quantifier remains.",
 ["audibert2025zariski","serre1974problems"],problem="GP-1973-03",
 worth="Focused work on a specified subgroup family is worthwhile, but this run found no bounded route to full coherence.")

add("Is SL2(Z[1/p]) coherent?","question",
 r"The same line asks about \(\mathrm{SL}_2(\mathbb Z[1/p])\).",
 r"For every prime \(p\), is every finitely generated subgroup of \(\mathrm{SL}_2(\mathbb Z[1/p])\) finitely presented?",
 "C",r"\citet[Theorem~4.2, version~3]{brody2025commensurator} proves a conditional positive result from Greenberg--Shalom. First preprint 2023; checked revision 7 November 2025. The hypothesis is essential to the attribution.",
 "Open unconditionally in the checked literature. Inverting two distinct primes is a different, negatively answered problem.",
 ["brody2025commensurator","serre1974problems"],problem="GP-1973-04",
 reconstruction=r"The conventional assumption that \(p\) is prime is made explicit.",literal_correctness="correct with missing hypotheses",
 worth="A specified subgroup family may admit a bounded study; the required arithmeticity hypothesis and full coherence exceed the contribution justified here.")

add("Coherence of GLn(Q)","question",
 r"The line ends \(\mathrm{GL}_n(\mathbb Q)?\), with no rank restriction.",
 r"For which integers \(n\geq1\) is the abstract discrete group \(\mathrm{GL}_n(\mathbb Q)\) coherent?",
 "B",r"Yes at \(n=1\), no at \(n\geq2\). Baumslag's rational triangular obstruction is recorded with Serre's questions and discussed in \citet[p.~74]{brody2022trees}; block inclusion handles larger ranks.",
 r"Answered. Finitely generated subgroups of \(\mathbb Q^\times\) are finitely generated abelian. The printed resolution is traced to 1974; the exact date of Baumslag's intervening observation is unverified.",
 ["brody2022trees","serre1974problems"],problem="GP-1973-05",verification="indirect",confidence="medium",
 reconstruction=r"The rank 1 exception is explicit. The thesis's displayed Baumslag--Solitar label is not copied: conjugation by \(\operatorname{diag}(p/q,q/p)\) scales a unipotent entry by \((p/q)^2\).")

add("Bracketed relations among irreducibles","question",
 r"A bracket asks about finitely many relations among different \ru{неприводимыми}; that reading is doubtful.",
 "The objects, operation and quantifier over relations are unspecified; a precise question cannot be recovered.",
 "F","Group-presentation and representation-theoretic readings remain possible after scan comparison. Neither warrants a publication match.",
 "Unresolved textual question; excluded from the definite problem index.",
 literal_correctness="not determinable",publication_match="none found",verification="unresolved lead",confidence="low")

add("Which fundamental groups occur?","question",
 r"The second bracket reads \ru{Какие бывают фунд. группы?}",
 "No class of spaces, dimension, compactness condition or equivalence relation is supplied; these choices materially change the question.",
 "F","The preceding three-manifold discussion is possible context, but does not determine the missing hypotheses.",
 "Not identifiable as a definite problem from the surviving wording.",
 literal_correctness="not determinable",publication_match="none found",verification="unresolved lead",confidence="low")

summary=r"""A plan with a substantive Serre interlude. The thirteen agenda headings are: derived categories (Kirillov, Bernstein); several-variable Ahlfors--Nevanlinna theory and Grauert (Henkin, Shabat); Quillen's simplicial \(K\)-theory (Fuchs); Lichtenbaum's special-value programme (Manin); an uncertain Weil/Gersten-name entry; Smale's optimization of several functions; Brown--Douglas--Fillmore \(K\)-theory (Kirillov); Mishchenko's representations; Lusztig on higher signatures; an Atiyah--Bott--Patodi spectral-asymmetry entry (Shubin, names retained as written); Donovan--Freilich on four subspaces (Ponomarev); Manin; and Vershik--Gelfand--Graev's six variations on \(\mathrm{SL}_2\). Bare agenda labels remain in this summary instead of becoming invented theorems. Derived categories connect thematically to 1971-266.3--6 and 1972-281.4. Quillen's subject was already circulating before this meeting \citep{quillen1973higher}.

The interlude separates finite generation from finite presentation for two function-field arithmetic families, then defines coherence and asks arithmetic examples. This material ends on P000501 at the Manin heading. The supplied catalogue range P000501--P000502 overlaps Manin's lecture and is retained only as catalogue metadata."""
talks=[dict(record=302,date="1973-09-03",speaker="I. M. Gelfand",
 pages="P000501-P000502",title="Plan and Serre's finiteness and coherence questions",
 kind="plan",summary=summary)]
problems=[]
for suffix,title,idx,status in [
 ("01","Finite presentation over a finite-field polynomial ring",4,r"Resolved: no at \(n=3\); yes at every \(n\geq4\), for all finite fields."),
 ("02","Finite presentation over a finite-field Laurent ring",5,r"Resolved: no at \(n=2\); yes at every \(n\geq3\), for all finite fields."),
 ("03","Coherence of SL3(Z)",11,r"Open in checked primary literature \citep[p.~5]{audibert2025zariski}."),
 ("04","Coherence of SL2(Z[1/p])",12,r"Open unconditionally; the Greenberg--Shalom hypothesis implies a positive answer \citep[Theorem~4.2, version~3]{brody2025commensurator}."),
 ("05","Ranks for coherence of GLn(Q)",13,r"Coherent only at \(n=1\); rational triangular subgroups obstruct every \(n\geq2\) \citep[p.~74]{brody2022trees}.")]:
    x=items[idx-1]
    problems.append(dict(id="GP-1973-"+suffix,title=title,statement=x["statement"],
      occurrences=[x["id"]],status=status,status_date="2026-11",refs=x["refs"]))
corrections=[
 dict(page="P000501",place="Imaginary-quadratic coefficient ring",
 transcription_reads=r"\(\Lambda\): \ru{чисто мнимые элем. квадр. поля}",
 should_read=r"The standard Bianchi-group interpretation uses \(\Lambda=\mathcal O_K\), the ring of integers of an imaginary quadratic field.",
 evidence="The scan supports the transmitted phrase, but purely imaginary elements are not a unital ring. This is a proposed mathematical reconstruction, not a transcription repair.",
 applies_to="both",type="faithful_error"),
 dict(page="P000501",place="Plan item 5, uncertain surname",
 transcription_reads=r"\ru{Герстенцуса}",should_read="Keep the name unresolved.",
 evidence="Scan and context do not authorize replacing it with Gersten or Gerstenhaber.",
 applies_to="both",type="ambiguity"),
 dict(page="P000501",place="Plan item 10, spectral-asymmetry attribution",
 transcription_reads="Atiyah, Bott, Patodi",
 should_read="Retain the names as written. The spectral-asymmetry announcement is by Atiyah, Patodi and Singer. Atiyah, Bott and Patodi also published their heat-equation/index paper in 1973, so the agenda may conflate two related subjects.",
 evidence=r"The scan supports \ru{Ботт}; bibliographical comparison does not authorize changing the diplomatic text. Compare \citet{atiyahpatodisinger1973spectral} and \citet{atiyahbottpatodi1973heat}.",
 applies_to="both",type="ambiguity"),
 dict(page="P000501-P000502",place="Record 302 catalogue range",
 transcription_reads="Record 302: P000501--P000502",
 should_read="The plan/interlude ends on P000501; its catalogue range overlaps Manin's talk.",
 evidence="The explicit Manin heading establishes the boundary; all record 302 items are located on P000501.",
 applies_to="both",type="provenance")]
for name,data in [("talks",talks),("items",items),("problems",problems)]:
    (D/f"{name}.json").write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n")
with (D/"corrections.csv").open("w",newline="",encoding="utf-8") as f:
    w=csv.DictWriter(f,fieldnames=["page","place","transcription_reads","should_read","evidence","applies_to","type"])
    w.writeheader();w.writerows(corrections)
(D/"area_map.json").write_text(json.dumps({x["id"]:("Number theory" if x["id"].endswith(".1") else "Unidentified" if x["class"]=="F" else "Group theory and topology") for x in items},indent=2)+"\n")
print(f"Record 302: {len(items)} items, {len(problems)} definite questions, {len(corrections)} corrections/ambiguities.")
