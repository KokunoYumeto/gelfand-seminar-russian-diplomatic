"""Generate the record 348 critical data; Python standard library only."""
import csv
import json
from pathlib import Path
OUT = Path(__file__).resolve().parents[1]
items = []
def item(pages, kind, title, notes, statement, reconstruction, fate, refs,
         literal="correct", match="exact", verification="read the result",
         confidence="high", development="none"):
    items.append(dict(id=f"1974-348.{len(items)+1}", record=348, pages=pages,
        kind=kind, title=title, notes=notes, statement=statement,
        reconstruction=reconstruction, **{"class":"E"}, fate=fate,
        present_status="As of November 2026: established under the stated hypotheses; this occurrence supplies no unresolved problem.",
        literal_correctness=literal, publication_match=match,
        verification=verification, development=development, problem="", worth="",
        refs=refs, confidence=confidence))

item("P000575", "construction", "The nerve and realization of a category",
 r"Objects give vertices, morphisms edges, composable pairs filled triangles, and composable triples tetrahedra. The graph alone does not retain composition.",
 r"For a small category \(\mathcal C\), set \(N_k\mathcal C=\operatorname{Fun}([k],\mathcal C)\), with faces given by omission/composition and degeneracies by identities. Its geometric realization is \(B\mathcal C\).",
 r"The face and degeneracy maps make the pictured construction precise. A smallness convention is supplied.",
 r"\citet[\S2]{segal1968classifying}, received 14 April 1967 and published 1968. Earlier occurrences: 1971-255.2 and 1973-308.11.",
 ["segal1968classifying"])
item("P000575", "definition", "Partially ordered sets as thin categories",
 r"The notes identify partially ordered sets with categories having at most one morphism between two objects.",
 r"A poset \(P\) defines a category with one arrow \(x\to y\) exactly when \(x\leq y\). Conversely a thin category determines a preorder; it determines a partial order on its objects if it is skeletal. Its nondegenerate nerve consists of strict finite chains.",
 r"Antisymmetry, or equivalently passage to a skeleton, is missing from the stated converse. Two distinct isomorphic objects in a thin category contradict that converse literally.",
 r"\citet[\S2]{segal1968classifying}; \citet[\S1]{quillen1973higher}. Both precede the talk.",
 ["segal1968classifying","quillen1973higher"], literal="correct with missing hypotheses", development="annotated")
item("P000575", "construction", "A group as a one-object category",
 r"A group gives the opposite extreme: one object, group elements as morphisms, and group multiplication as composition.",
 r"For a discrete group \(G\), the one-object category with automorphism group \(G\) has \(N_kG=G^k\). Its realization is a model of \(BG\).",
 r"The discrete case is used here, consistently with the later universal-cover assertion; a topological group requires a topological nerve and different homotopy-group statements.",
 r"\citet[\S3]{segal1968classifying}. Compare 1973-308.12.",
 ["segal1968classifying"], literal="correct with missing hypotheses")
item("P000575", "claim", "A contractible-cover model for a space",
 r"For an open cover \(\{U_\alpha\}\), intersections are unions of cover members; order is inclusion. If the sets are contractible, the notes assert \(|\mathcal C|\simeq X\), followed by \ru{Добавл. пересечения}.",
 r"A sufficient precise version is the nerve theorem for a numerable good open cover of a paracompact space: every nonempty finite intersection is contractible, and \(X\) is homotopy equivalent to the nerve. The category of nonempty finite indexed intersections, ordered by reverse inclusion of index sets, realizes its barycentric subdivision.",
 r"This is a sufficient good-cover reconstruction, not a proof of the more general basis-like formulation in the notes. Numerability, finite-intersection hypotheses, and retention of intersection labels are explicit additions.",
 r"\citet[\S4, Proposition 4.1]{segal1968classifying} supplies the numerable-cover comparison (1968).",
 ["segal1968classifying"], literal="correct with missing hypotheses", match="partial", confidence="medium", development="annotated")
item("P000576", "construction", "The sphere and the octahedral order complex",
 r"Two hemispherical sets have an annular intersection \(w\), so the three-object diagram gives only an interval. Splitting \(w=W_1\cup W_2\) and its overlap into two components produces the drawn octahedral surface.",
 r"Take six contractible open sets in three levels \(\{U,V\}\), \(\{W_1,W_2\}\), \(\{X_1,X_2\}\), each lower-level set included in each higher-level set and no other strict inclusions. Their order complex is \(S^0*S^0*S^0\cong S^2\), the octahedral boundary.",
 r"The written \(x_i\in(W_1\cap W_2)_{\rm comp}\) are interpreted as component labels; actual open components, rather than selected points, are required for this cover argument. The schematic diagram does not specify a unique cover.",
 r"The cover method is in \citet[\S4]{segal1968classifying}; the six-element model is directly reconstructed from the page.",
 ["segal1968classifying"], literal="correct with missing hypotheses", match="partial", development="annotated")
item("P000576", "definition", "The spherical building of a vector space",
 r"For a finite-dimensional vector space over any field, the category of proper subspaces and inclusions is called its building.",
 r"For a field \(K\) and \(n=\dim_KV\geq2\), let \(\mathcal B(V)=\{W:0<W<V\}\), ordered by inclusion. Its order complex is the spherical building of type \(A_{n-1}\). Both zero and \(V\) are excluded.",
 r"The exclusion of zero is supplied by the subsequent definition \(0<W\leq H\) on the same page. Including zero would make the nerve contractible.",
 r"\citet[Example 8.2 and end of \S8]{quillen1978poset} checks the model; \citet{tits1974buildings} expanded the 1968 seminar notes in 1974. Compare 1973-321.5.",
 ["quillen1978poset","tits1974buildings"], literal="correct with missing hypotheses", development="annotated")
item("P000576", "theorem", "The Solomon--Tits homotopy type",
 r"The building is homotopy equivalent to a wedge of spheres of dimension \(n-2\). The number depends on the field and is infinite for an infinite field.",
 r"For \(n\geq2\), \(|\mathcal B(V)|\simeq\bigvee_I S^{n-2}\). For \(K=\mathbb F_q\), \(|I|=q^{\binom n2}\); for an infinite field the index set is infinite. Wedges carry their CW topology, and \(S^0\) is a pointed two-point set.",
 r"The finite-field count makes the notebook's field-dependence explicit: hyperplanes not containing a fixed line number \(q^{n-1}\), so the induction gives \(r_n=q^{n-1}r_{n-1}\), \(r_2=q\). The same induction gives infinitely many summands for an infinite field.",
 r"\citet[Example 8.2 and pp.117--118]{quillen1978poset} gives a later proof of the established theorem. The notebook attributes it to Solomon--Tits, not to new work of Segal.",
 ["quillen1978poset","tits1974buildings"], literal="correct with missing hypotheses", development="annotated")
item("P000576", "claim", "A maximum contracts a poset nerve",
 r"If an ordered set has a maximum, its realization is contractible; a cone is drawn.",
 r"If a nonempty poset \(P\) has a maximum \(m\), each simplex extends to a simplex with vertex \(m\); hence \(|P|\) is a cone. More generally, an initial or terminal object contracts a category's nerve.",
 r"The general categorical version is contextual; the page needs only the maximum case.",
 r"\citet[\S1, Proposition 2, Corollary 2]{quillen1973higher}. Earlier occurrence: 1973-309.5.",
 ["quillen1973higher"])
item("P000576", "construction", "The cover by hyperplane cones",
 r"The maximal elements are hyperplanes; \(|\mathcal C|=\bigcup_H|\mathcal C_H|\), where \(\mathcal C_H=\{W:0<W\leq H\}\); each member is contractible.",
 r"Each \(|\mathcal C_H|\) is a cone on \(H\). Every finite proper-subspace flag has its largest member contained in a hyperplane, so these simplicial subcomplexes cover \(|\mathcal B(V)|\).",
 r"The pieces are subcomplexes, not asserted to be open subsets.",
 r"The contraction is checked by \citet[\S1, Proposition 2]{quillen1973higher}; compare the dual line-cover proof in \citet[end of \S8]{quillen1978poset}.",
 ["quillen1973higher","quillen1978poset"], match="partial")
item("P000576", "claim", "Contracting the fixed-line part of the building",
 r"Fix a line \(L\), and put \(Y=\bigcup_{H\supset L}|\mathcal C_H|\). The notes contract \(Y\) using intersections of the cone cover.",
 r"Let \(P_L=\{0<W<V:W+L<V\}\). Then \(Y=|P_L|\). The order-preserving map \(W\mapsto W+L\) satisfies \(W\leq W+L\geq L\); realization is homotopic both to the identity and to the constant map at \(L\), contracting \(Y\).",
 r"This direct order-homotopy argument supplies the finite-intersection step for arbitrary fields and arbitrary numbers of hyperplanes.",
 r"\citet[\S1, Proposition 2]{quillen1973higher} supplies the homotopy principle. The particular contraction is reconstructed from the notebook.",
 ["quillen1973higher"], match="partial", development="annotated")
item("P000577", "claim", "The nonempty finite-intersection criterion",
 r"If all finite intersections of the covering pieces are contractible and nonempty, their union is contractible. The words excluding an empty intersection are partly overwritten but visible.",
 r"For a numerable open good cover, or a cover of a simplicial complex by subcomplexes, suppose the intersection of every nonempty finite subfamily is nonempty and contractible. The nerve is then a full simplex and the union is contractible.",
 r"The requirement concerns every finite subfamily, not merely those whose intersection happens to be nonempty. The cover topology is supplied. The subcomplex version applies to the building.",
 r"The nerve argument is used in \citet[end of \S8]{quillen1978poset}; the open-cover comparison is in \citet[\S4]{segal1968classifying}.",
 ["quillen1978poset","segal1968classifying"], literal="correct with missing hypotheses", match="partial", development="annotated")
item("P000577", "claim", "Collapsing the common part gives a wedge",
 r"Lemma 1: if \(X=Y\cup Y_1\cup\cdots\cup Y_k\), all pieces are contractible and \(Y_i\cap Y_j\subset Y\) for distinct indices, then \(X\simeq\bigvee_iY_i/(Y_i\cap Y)\).",
 r"Let \(X\) be a CW complex covered by subcomplexes \(Y,Y_i\), with \(Y\) nonempty contractible, \(Y_i\cap Y\ne\varnothing\), and \(Y_i\cap Y_j\subset Y\) for \(i\ne j\). Then \(X\to X/Y\) is a homotopy equivalence and \(X/Y\cong\bigvee_iY_i/(Y_i\cap Y)\). Contractibility of the \(Y_i\) is used in the next step.",
 r"CW/cofibration and nonempty-intersection hypotheses are added. The result extends to arbitrary families of subcomplexes with CW weak topology, as required over an infinite field.",
 r"This elementary quotient fact is used in the 1974 talk. A modern check is \citet[Proposition 0.17]{hatcher2002algebraic}.",
 ["hatcher2002algebraic"], literal="correct with missing hypotheses", match="partial", development="annotated")
item("P000577", "claim", "A cofiber in a contractible space is a suspension",
 r"Lemma 2 states \(Z/Z_0\simeq SZ_0\) when \(Z\) is contractible and \(Z_0\subset Z\); cone and suspension diagrams explain the replacement.",
 r"For a CW pair \((Z,Z_0)\) with \(Z\) contractible and \(Z_0\ne\varnothing\), the quotient is homotopy equivalent to the unreduced suspension \(SZ_0\). Use the mapping cone of the inclusion, which is nullhomotopic.",
 r"The cofibration condition and nonemptiness qualify the unqualified subset notation.",
 r"A later precise reference for this established cofiber fact is \citet[Examples 0.13--0.14]{hatcher2002algebraic}.",
 ["hatcher2002algebraic"], literal="correct with missing hypotheses", development="annotated")
item("P000577", "method", "The hyperplane intersection and dimension induction",
 r"Lemma 3 identifies \(|\mathcal C_H|\cap Y\) with the building of \(H\), yielding reduction by dimension.",
 r"If \(H\) does not contain \(L\), then \(\mathcal C_H\cap P_L=\{W:0<W<H\}\). Indeed \(H+L=V\), while \(W<H\) implies \(\dim(W+L)\leq n-1\). For \(n\geq3\), the preceding decomposition therefore gives \(|\mathcal B(V)|\simeq\bigvee_{H\not\supset L} S|\mathcal B(H)|\).",
 r"The condition \(H\not\supset L\) is restored from the preceding line. For distinct such hyperplanes, \(\dim(H\cap H')=n-2\), so their cone intersection lies in \(Y\), as required. The base case is separate.",
 r"This is the notebook's proof of the theorem checked in \citet[\S8]{quillen1978poset}; that source uses a different, dual cover proof.",
 ["quillen1978poset"], literal="correct with missing hypotheses", match="partial", development="annotated")
item("P000577", "claim", "The dimension-two base case",
 r"The first induction step is \(\dim V=2\), where the building is a collection of points (lines); the phrase about a wedge is overwritten.",
 r"For \(\dim_KV=2\), \(|\mathcal B(V)|=\mathbb P^1(K)\) with the discrete topology. A chosen base line identifies it with a wedge of copies of \(S^0\), one for every remaining line. Over \(\mathbb F_q\) there are \(q+1\) points and \(q\) copies of \(S^0\).",
 r"A wedge of one-point spaces would be a point; the intended spheres are pointed two-point spaces. This also fixes the homology convention below.",
 r"The base case agrees with \citet[Example 8.2]{quillen1978poset} and is directly visible in the row of points.",
 ["quillen1978poset"], literal="not determinable", match="partial", development="annotated")
item("P000577", "claim", "Suspending a wedge of spheres",
 r"The suspension of a wedge of spheres is again a wedge of spheres.",
 r"For a based CW complex \(A=\bigvee_I S^d\), \(d\geq0\), the reduced suspension is \(\Sigma A\cong\bigvee_I S^{d+1}\). The unreduced suspension \(SA\) is homotopy equivalent to \(\Sigma A\), by collapsing the basepoint interval.",
 r"The based CW convention includes the disconnected \(d=0\) case in the induction.",
 r"The standard argument is checked in \citet[Example 0.10]{hatcher2002algebraic}; the notebook uses it in 1974.",
 ["hatcher2002algebraic"], literal="correct with missing hypotheses")
item("P000577", "definition", "The Steinberg module and reduced homology",
 r"The displayed line identifies \(H_{n-2}(|\mathcal C|;\mathbb Z)\) with the Steinberg module of \(V\).",
 r"The integral Steinberg module is \(\operatorname{St}(V)=\widetilde H_{n-2}(|\mathcal B(V)|;\mathbb Z)\), with its natural \(\operatorname{GL}(V)\)-action. For \(n\geq3\), ordinary and reduced homology agree in this degree; for \(n=2\), reduced homology is necessary.",
 r"Over \(\mathbb F_q\) in dimension two, ordinary \(H_0\) has rank \(q+1\), while the reduced group has rank \(q\). The literal formula fails at the base case retained in this talk.",
 r"The building interpretation belongs to the older Solomon--Tits theory; \citet[\S\S8--9]{quillen1978poset} checks its reduced-homology dimension.",
 ["quillen1978poset","tits1974buildings"], literal="false as written", match="partial", development="annotated")
item("P000577", "theorem", "The classifying space of a discrete group is aspherical",
 r"For the category of a group, \(|\mathcal C|=BG\), \(\pi_1(|\mathcal C|)=G\), and the universal covering is contractible.",
 r"For a discrete group \(G\), the nerve realization \(BG\) is a connected CW complex with \(\pi_1(BG)\cong G\) and \(\pi_k(BG)=0\) for \(k>1\).",
 r"Discreteness is essential: for a well-behaved topological group the usual formula is \(\pi_k(BG)\cong\pi_{k-1}(G)\), not asphericity in general.",
 r"\citet[\S3]{segal1968classifying}, published six years before this exposition.",
 ["segal1968classifying"], literal="correct with missing hypotheses")
item("P000577-P000578", "construction", "The contractible chaotic category",
 r"\(\widetilde{\mathcal C}\) has objects the elements of \(G\) and one morphism between every ordered pair. Its realization is called contractible because every element is linked to \(1\).",
 r"The unique morphisms \(g\to1\) form a natural transformation from the identity functor to the constant functor at \(1\). Realization gives a contraction. Simplices are arbitrary finite strings of elements of \(G\).",
 r"Connectedness of a graph alone is insufficient; coherent higher simplices and the natural transformation give the actual argument.",
 r"\citet[\S3 and Proposition 2.1]{segal1968classifying}.",
 ["segal1968classifying"], development="annotated")
item("P000578", "construction", "The universal-cover functor and multiplication convention",
 r"The functor sends each object to the unique object and \(g\to g'\) to \(g^{-1}g'\). Its realization is the universal covering.",
 r"Adopt the convention that a path labelled first \(a\), then \(b\), has composite label \(ab\). Then \((g^{-1}g')(g'^{-1}g'')=g^{-1}g''\), so this is a functor. Left multiplication on strings by discrete \(G\) gives a principal covering \(EG\to BG\), with \(EG\) the contractible realization of the chaotic category.",
 r"An opposite composition convention requires changing the formula consistently. The scan is not emended merely because conventions differ.",
 r"\citet[\S3]{segal1968classifying} gives the construction and the extra local-triviality issue for general topological groups.",
 ["segal1968classifying"], literal="correct with missing hypotheses")
item("P000578", "method", "Transition functions and a bundle's classifying map",
 r"A bundle \(E\to X\), a trivializing cover, intersections, and \(X\to BG\) are drawn. The last sentence about the intersection category stops before completing the construction.",
 r"For a numerable principal \(G\)-bundle over a paracompact base, continuous transition functions define a functor from the topological \v{C}ech category, retaining points in intersections, to the one-object topological category \(G\). Realization and the cover equivalence give the classifying map up to homotopy, using a standard numerable universal-bundle model.",
 r"The completion is editorial. The notes do not specify discrete versus topological \(G\), a principal bundle, or how point-dependent transitions enter the functor. A category of unlabelled open sets alone cannot encode arbitrary transition functions.",
 r"The completion was published in \citet[\S4, Proposition 4.1]{segal1968classifying}; the surviving final sentence is a partial match.",
 ["segal1968classifying"], literal="not determinable", match="partial", development="annotated")

talks=[dict(record=348,date="1974-10-14",speaker="Graeme Segal",pages="P000574-P000580",
 title="Classifying spaces, spherical buildings, and the Solomon--Tits theorem",kind="talk",
 summary=r"The actual Segal text is P000575--P000578, headed 14 October 1974. It constructs nerves, compares covers with spaces, proves the building's wedge-of-spheres homotopy type by a hyperplane induction, and constructs a group classifying space's universal cover. Bundle classification ends mid-construction. The catalogue's wider page envelope includes adjoining talks; P000574, P000579 and P000580 are not assigned to Segal's argument. This exposition continues 1973-308 and 1973-309, with a building connection to 1973-321.5. The base case exposes the missing reduced-homology symbol in the Steinberg-module formula.")]
corrections=[
 ["P000575","posets as categories","category with at most one morphism between two objects","skeletal thin category; otherwise a preorder","Scan P000575 says partially ordered. Distinct uniquely isomorphic objects show the missing antisymmetry; mathematical clarification, not a mistranscribed word.","both","faithful_error"],
 ["P000576","building definition","category of proper subspaces","category of nonzero proper subspaces","The phrase omits nonzero, but the same scan explicitly writes 0 strictly contained in W below. Retain the shorthand and annotate its convention.","both","ambiguity"],
 ["P000576","sphere-cover components",r"\(x_i\) in a connected component of \(W_1\cap W_2\)",r"use contractible open components \(X_i\) in the cover reconstruction","The scan uses membership signs and small x. Interpreting them as open components is editorial, not a secure transcription correction.","both","ambiguity"],
 ["P000577","Lemmas 1 and 2","unqualified subset and quotient formulas","CW subcomplexes or suitable cofibration hypotheses; nonempty intersections","The scan has no point-set hypotheses. Hatcher 2002 Proposition 0.17 and Examples 0.13--0.14 specify the condition used.","both","ambiguity"],
 ["P000577","Steinberg module",r"\(H_{n-2}(|C|;\mathbb Z)\)",r"\(\widetilde H_{n-2}(|C|;\mathbb Z)\)",r"Scan P000577 has no tilde. For dimension two over \(\mathbb F_q\), ordinary \(H_0\) has rank \(q+1\) but the Steinberg module has rank \(q\): a faithful mathematical omission.","both","faithful_error"],
 ["P000575-P000578","record 348 page envelope","P000574-P000580","substantive Segal text: P000575-P000578","The 14/X-74 Segal heading starts on P000575; P000578 ends the bundle paragraph. Adjacent pages contain other talks.","both","provenance"]
]
for number in (7,10,14,15,17):
 items[number-1]["reconstruction"] = r"\ours{} " + items[number-1]["reconstruction"]
for name,data in [("talks",talks),("items",items),("problems",[])]:
 (OUT/f"extra_{name}.json").write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n")
with (OUT/"extra_corrections.csv").open("w",newline="") as f:
 w=csv.writer(f);w.writerow(["page","place","transcription_reads","should_read","evidence","applies_to","type"]);w.writerows(corrections)
print(f"record 348: {len(talks)} talk, {len(items)} items, {len(corrections)} corrections; all class E; no problem entry")
