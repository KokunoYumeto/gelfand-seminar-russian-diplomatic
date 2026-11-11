"""Authoring/checkpoint source for records 272--275 and 280--281.

This file is intermediate reproducibility material; the schema JSON files are
the deliverables. Run after each record is added to save a complete checkpoint.
"""
import csv
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
talks, items, problems, corrections = [], [], [], []

def talk(record, date, speaker, pages, title, summary):
    talks.append(dict(record=record, date=date, speaker=speaker, pages=pages,
                      title=title, kind="talk", summary=summary))

def item(record, pages, kind, title, notes, statement, reconstruction, fate,
         status, refs, cls="E", literal="correct", match="exact",
         verification="read the result", development="none", problem="",
         confidence="high", worth=""):
    n = sum(x["record"] == record for x in items) + 1
    items.append(dict(id=f"1972-{record}.{n}", record=record, pages=pages,
        kind=kind, title=title, notes=notes, statement=statement,
        reconstruction=reconstruction, **{"class":cls}, fate=fate,
        present_status="As of 9 November 2026: " + status,
        literal_correctness=literal, publication_match=match,
        verification=verification, development=development, problem=problem,
        worth=worth, refs=refs, confidence=confidence))

def corr(page, place, reads, should, evidence, applies="both", typ="faithful_error"):
    corrections.append(dict(page=page, place=place, transcription_reads=reads,
        should_read=should, evidence=evidence, applies_to=applies, type=typ))

def save():
    for name, value in [("talks",talks),("items",items),("problems",problems)]:
        (HERE / (name+".json")).write_text(json.dumps(value,ensure_ascii=False,indent=2)+"\n")
    with (HERE/"corrections.csv").open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=["page","place","transcription_reads","should_read","evidence","applies_to","type"])
        w.writeheader(); w.writerows(corrections)
    print(f"checkpoint: {len(talks)} records, {len(items)} items, {len(problems)} problems, {len(corrections)} corrections")

G = ["griffiths1970periods"]
GDATE = r"The exposition predates this talk: \citet[\S2, pp.~232--235]{griffiths1970periods} summarizes the period-domain formalism in an invited lecture delivered on 29 August 1968, received on 18 September 1969, and published in March 1970."

talk(272,"1972-09-25","A. M. Gabrielov","P000450-P000451",
     "Variations of Hodge structure and their classifying domains",
     r"Gabrielov defines an integral variation of polarized Hodge structure, its flat holomorphic bundle and Griffiths transversality, then describes the classifying flag domain and its homogeneous-space presentation. This is an expository continuation of 1969-182.2 and 1971-251.1--5, not an announcement of a new theorem. The actual heading is on P000450; P000449 is the preceding talk's tail. Two statements require mathematical emendation rather than transcription repair: the orthogonality index on P000451, and the unrestricted claim that the associated Riemannian symmetric space has a complex structure.")

item(272,"P000450","definition","Integral local system and its scalar extensions",
 r"Over a nonsingular complex analytic space \(S\), the notes take a locally free finite-rank sheaf \(H_{\mathbb Z}\), form \(H_{\mathbb C}=H_{\mathbb Z}\otimes\mathbb C\), \(H_{\mathbb R}\), and \(H_{\mathcal O}=H_{\mathbb Z}\otimes\mathcal O_S\), and call a local system a bundle with connection.",
 r"An integral local system is a sheaf locally isomorphic to \(\underline{\mathbb Z}^{,r}\). Tensoring over \(\mathbb Z\) with the constant real or complex sheaf gives local systems; \(\mathcal H=H_{\mathbb Z}\otimes_{\mathbb Z}\mathcal O_S\) is a holomorphic vector bundle. Locally constant complex sheaves correspond to holomorphic bundles with integrable holomorphic connection; an integral structure is additional data.",
 r"The word integrable (equivalently flat) is necessary in the connection equivalence. The complex local system and its associated holomorphic bundle must be distinguished, although the notebook sometimes writes \(H_{\mathbb C}\) for both.",
 GDATE, "standard local-system/VHS terminology; no research problem is posed.",G,
 literal="correct with missing hypotheses")

item(272,"P000450","construction","Canonical flat connection and horizontal sections",
 r"The displayed connection is \(\nabla:H_{\mathcal O}\to\Omega_S^1\otimes_{\mathcal O_S}H_{\mathcal O}\), called Gauss--Manin; the kernel is the sheaf of locally constant complex sections.",
 r"For a complex local system \(L\), the associated bundle \(\mathcal H=L\otimes_{\mathbb C}\mathcal O_S\) has the flat connection \(\nabla(v\otimes f)=v\otimes df\), with \(\ker\nabla=L\). For a smooth proper family, the construction applied to a cohomology local system is the Gauss--Manin connection.",
 r"The first construction needs no family. The name Gauss--Manin is geometrically justified only after identifying the local system with the cohomology of such a family; the notes do not supply a family here. This repeats the setting of 1969-182.2 and 1971-251.5.",
 GDATE + r" Its formula (2.1) records the connection's compatibility with the Hodge filtration.",
 "the local-system construction and its geometric Gauss--Manin specialization remain standard.",G)

item(272,"P000450","definition","Hodge filtration and Griffiths transversality",
 r"A decreasing filtration \(F^0\supset F^1\supset\cdots\supset F^n\) by holomorphic subbundles is required to satisfy \(\nabla\mathcal F^p\subset\Omega_S^1\otimes\mathcal F^{p-1}\). A locally constant bilinear form is to give a polarized Hodge structure in each fibre.",
 r"A polarized integral variation of pure Hodge structure of weight \(n\) consists of an integral local system, holomorphic subbundles \(F^p\mathcal H\), a flat bilinear form \(Q\), fibrewise Hodge opposition and positivity, and \(\nabla(F^p\mathcal H)\subset\Omega_S^1\otimes F^{p-1}\mathcal H\). The displayed finite range presupposes effective Hodge types \(0\leq p,q\leq n\); the general definition uses all integer indices, with eventually constant endpoints.",
 r"The bundle \(\mathcal H\), not a locally constant sheaf, carries the holomorphic filtration. Flatness and the effective-weight convention make explicit the notebook's abbreviated notation.",
 GDATE + r" See equation (2.1) for transversality and the preceding definition of the classifying space.",
 "established definition; the notes do not pose a transversality conjecture.",G,
 literal="correct with missing hypotheses")

item(272,"P000450-P000451","construction","Compact dual and the erroneous orthogonality index",
 r"The notes impose fixed flag dimensions and the displayed condition \(\psi(F^p,F^{n-p})=0\). The original P000451 scan has this same index, without \(+1\).",
 r"Fix a real vector space \(H_{\mathbb R}\), Hodge numbers of weight \(n\), and a nondegenerate \((-1)^n\)-symmetric bilinear form \(Q\). The compact dual is the projective variety of flags with the prescribed dimensions and \(Q(F^p,F^{n-p+1})=0\) for every \(p\), taking the appropriate connected flag component if needed.",
 r"The index is emended to \(n-p+1\), also written correctly in Gabrielov's continuation on P000458. This is a mathematical error faithfully transcribed: the stronger printed condition would generally force the intended pairing of complementary Hodge types to vanish.",
 GDATE + r" The bilinear relations and flag-domain construction in \S2 support the corrected formulation, not the literal index.",
 "the standard compact-dual construction is established; the notebook's literal orthogonality formula is false.",G,
 literal="false as written",match="partial",development="annotated")

item(272,"P000451","definition","Opposed filtrations, Hodge decomposition, and Weil operator",
 r"The page imposes \(F^p\oplus\overline{F^{n-p+1}}=H_{\mathbb C}\), defines \(H^{p,n-p}=F^p\cap\overline{F^{n-p}}\), and lets \(C\) act by \(i^{2p-n}\) on this summand.",
 r"For a decreasing exhaustive separated filtration satisfying the displayed opposition, \(H_{\mathbb C}=\bigoplus_{p+q=n}H^{p,q}\), \(\overline{H^{p,q}}=H^{q,p}\), and \(F^p=\bigoplus_{r\geq p}H^{r,n-r}\). The real-linear Weil operator complexifies to \(C|_{H^{p,q}}=i^{p-q}\).",
 r"The direct-sum decomposition and recovery of the filtration are stated explicitly to unpack the notebook's concise definition; the notation and exponent themselves are faithful.",
 GDATE,
 "the standard equivalence between opposed filtrations and pure real Hodge decompositions.",G)

item(272,"P000451","definition","Polarization positivity and the open period domain",
 r"The form \(\psi(x,C\bar x)\) is positive, and imposing this positivity and opposition gives an open subset \(D\) of the compact flag variety \(\overline D\).",
 r"Normalize the real polarization \(Q\) so that \(h(x,y)=Q(x,C\overline y)\) is a positive-definite Hermitian form. For fixed polarized Hodge numbers and fixed \(Q\), the flags satisfying Hodge opposition and this positivity form an open complex submanifold \(D\) of the compact dual. Its connected components may be selected separately.",
 r"The harmless overall sign convention for \(Q\) is fixed explicitly; positivity means for every nonzero complex vector. Integrality of a lattice does not make the period domain discrete.",
 GDATE,
 "standard period-domain construction with the stated polarization convention.",G)

item(272,"P000451","theorem","Homogeneous period domain and compact stabilizer",
 r"The real group preserving \(\psi\) acts transitively on \(D\); the stabilizer \(H\) is compact.",
 r"Let \(G_{\mathbb R}\) be the full real isometry group of the polarization with the relevant flag-component action. A period-domain orbit is \(G_{\mathbb R}/V\), where the stabilizer \(V\) of a polarized Hodge decomposition is compact. The identity component \(G_{\mathbb R}^{0}\) acts transitively on each connected component of the period domain.",
 r"The notebook's stabilizer \(H\) is renamed \(V\) to distinguish it from the Hodge vector space. Connected-component qualifications are necessary if one replaces the full real isometry group by its identity component; the continuation on P000458 does so.",
 GDATE + r" See equation (2.3) and the surrounding homogeneous-space description.",
 "established homogeneous-space description, component by component.",G)

item(272,"P000451","claim","Projection to a Riemannian symmetric space",
 r"For a maximal compact \(K\supset H\), the map \(G/H\to G/K\) is said not to be holomorphic; the following sentence says \(G/K\) has a complex structure.",
 r"A maximal compact subgroup \(K\) containing the compact period stabilizer \(V\) gives a smooth fibration \(K/V\to G_{\mathbb R}/V\to G_{\mathbb R}/K\). The base is a Riemannian symmetric space and is not, in general, Hermitian symmetric. In the Hermitian cases the projection need not be holomorphic; when \(V=K\), it is the identity and is holomorphic for the compatible structure.",
 r"Both universal assertions need qualification. No complex structure on the symmetric space is supplied in the notes. The correct general statement is smooth homogeneity, with additional hypotheses for complex geometry.",
 GDATE + r" Equation (2.3) explicitly describes a differentiable fibration and qualifies holomorphicity; it does not assert that every symmetric quotient is complex.",
 "the literal blanket claim is false; the qualified period-domain fibration is classical.",G,
 literal="false as written",match="partial",development="annotated")

corr("P000449-P000451","record 272 boundary","catalogue range P000449-P000453","Gabrielov's notes begin at the dated heading on P000450 and end on P000451; P000449 belongs to the preceding material.","Original headings and consecutive source pages; catalogue ranges overlap adjacent talks.",typ="provenance")
corr("P000450","local system parenthesis","local system = bundle with connection","local system = bundle with flat (integrable) connection; the integral lattice is additional data",r"P000450 scan omits flatness; the connection is locally \(d\). Griffiths 1970, section 2.")
corr("P000451","first displayed orthogonality",r"\(\psi(F^p,F^{n-p})=0\)",r"\(\psi(F^p,F^{n-p+1})=0\)",r"The scan genuinely has \(n-p\); P000458 and the polarization relations show the required \(+1\).")
corr("P000451",r"last assertion about \(G/K\)",r"\(G/K\) has complex structure; the projection is not holomorphic",r"\(G/K\) is Riemannian symmetric in general; a complex structure and nonholomorphicity require further hypotheses, with \(V=K\) an immediate exception.","Original scan; Griffiths 1970, equation (2.3) and surrounding text.")
save()

TREF=["mumford1972degenerating","serre1977arbres"]
TFATE=r"The local-field tree was already part of the established theory: \citet[Introduction, pp.~130--131, and \S1]{mumford1972degenerating} uses the lattice tree and its \(q+1\) neighbours in a paper received on 16 March 1971 and published in 1972. \citet[Chapter~II]{serre1977arbres} is a later systematic exposition based on his 1968--1969 Coll\`ege de France course; its 1977 publication is not the construction's first circulation."

talk(273,"1972-09-25","Yu. I. Manin","P000452-P000453",
 "Retelling of Manin's first lecture on p-adic numbers: the lattice tree",
 r"The heading explicitly calls this a \ru{пересказ}, a retelling of Manin's first lecture. The two pages construct the regular tree of homothety classes of rank-two lattices over a nonarchimedean local field, with its \(\mathrm{PGL}_2\)-action and invariant distance. The analogy with the Lobachevsky plane is motivational. A crossed-out equal-characteristic alternative is not promoted to an assertion by the speaker, and the vague reference to A. Weil is not assigned to an invented publication.")

item(273,"P000452","definition","Local field, valuation ring, and projective linear action",
 r"The uncancelled text takes \(K\) to be a finite extension of \(\mathbb Q_p\), with integer ring \(A\), maximal ideal \(\mathfrak m\), and fractional linear transformations of \(\mathbb P^1(K)\).",
 r"For a finite extension \(K/\mathbb Q_p\), put \(A=\mathcal O_K\), \(\mathfrak m=(\pi)\), and \(k=A/\mathfrak m\cong\mathbb F_q\). Then \(G=\mathrm{PGL}_2(K)=\mathrm{GL}_2(K)/K^\times\) acts on \(\mathbb P^1(K)\) by \(z\mapsto(az+b)/(cz+d)\), with the usual interpretation at poles and infinity.",
 r"Invertibility of the representing matrix and the projective convention at infinity are made explicit. The construction also works for equal-characteristic local fields, but that extension is editorial: the relevant phrase is cancelled in the original.",
 TFATE,"standard local-field setting and projective action; no open question.",TREF)

item(273,"P000452","definition","Lattices, homothety classes, and the vertex homogeneous space",
 r"A lattice is written \(L=Ae_1\oplus Ae_2\); lattices are equivalent when they differ by a scalar in \(K^\times\). Vertices are these equivalence classes, also written \(G/U\) for \(U=\mathrm{GL}_2(A)/A^\times\).",
 r"A full lattice in \(K^2\) is a finitely generated \(A\)-submodule spanning \(K^2\), necessarily free of rank two. The homothety classes form a transitive \(G\)-set. The stabilizer of \([A^2]\) is the image of \(K^\times\mathrm{GL}_2(A)\) in \(G\), naturally \(\mathrm{GL}_2(A)/A^\times\); hence the vertex set is \(G/U\).",
 r"Fullness and spanning are essential: a rank-two module embedded degenerately would not define the intended vertex. The stabilizer identification unpacks the concise quotient notation.",
 TFATE,r"standard vertex model of the Bruhat--Tits tree of \(\mathrm{PGL}_2(K)\).",TREF)

item(273,"P000452","theorem","Simultaneous elementary divisors for two lattices",
 r"For two lattices the notes assert a basis with \(L_1=Ae_1\oplus Ae_2\) and \(L_2=A\pi^{\nu_1}e_1\oplus A\pi^{\nu_2}e_2\), with integers \(\nu_i\).",
 r"For full lattices \(L_1,L_2\subset K^2\), there is an \(A\)-basis \(e_1,e_2\) of \(L_1\) and integers \(\nu_1\leq\nu_2\) such that \(L_2=\pi^{\nu_1}Ae_1\oplus\pi^{\nu_2}Ae_2\). The unordered exponents are uniquely determined; simultaneous scaling of \(L_2\) shifts both by the same integer.",
 r"This is Smith normal form over the discrete valuation ring after multiplying \(L_2\) by a sufficiently large power of \(\pi\). The ordering and uniqueness, needed for distance, are supplied explicitly.",
 TFATE,"classical elementary-divisor theorem; its use here is expository.",TREF)

item(273,"P000453","construction","Invariant distance between lattice classes",
 r"Representatives are normalized to \(L_2=Ae_1\oplus A\pi^\nu e_2\subset L_1\), \(\nu\geq0\), with \(L_1/L_2\cong A/\mathfrak m^\nu\). The distance is \(\nu\), equivalently \(|\nu_1-\nu_2|\).",
 r"For homothety classes \([L_1],[L_2]\), define \(d([L_1],[L_2])=|\nu_1-\nu_2|\), where \(\nu_i\) are the simultaneous elementary divisors. This is independent of bases and representatives, invariant under \(\mathrm{PGL}_2(K)\), and is a metric. The stated cyclic quotient holds after the indicated normalized inclusion; arbitrary representatives need not admit a quotient \(L_1/L_2\).",
 r"The scan explicitly boxes \(L_2\subset L_1\), so the initial normalized quotient is not erroneous. The later variant with two quotient summands must also be read after scaling to an inclusion; negative exponents cannot be used in \(A/\pi^{\nu_i}A\).",
 TFATE,"the standard graph distance, with the inclusion convention restored for quotient formulas.",TREF,
 literal="correct with missing hypotheses")

item(273,"P000453","construction","Adjacency and the q plus one neighbours",
 r"Two vertices are joined when their distance is one, and exactly \(q+1\) edges meet at each vertex.",
 r"The neighbours of \([L]\) are represented uniquely by sublattices \(L'\) with \(\pi L\subsetneq L'\subsetneq L\). They correspond to one-dimensional subspaces of \(L/\pi L\cong k^2\), so there are \(|\mathbb P^1(k)|=q+1\) neighbours.",
 r"The residue-line correspondence is the modern explanation of the stated valency; the notebook states the result without this proof.",
 TFATE,"a classical local combinatorial description of the tree.",TREF)

item(273,"P000453","theorem","The lattice graph is a tree",
 r"The graph \(\Delta\) is called a connected graph without cycles, with its natural \(G\)-action.",
 r"The graph of homothety classes of full rank-two \(A\)-lattices and distance-one edges is connected and acyclic. Its graph metric is the elementary-divisor metric, and the action of \(\mathrm{PGL}_2(K)\) preserves adjacency. Thus its geometric realization is the Bruhat--Tits tree in rank one.",
 r"The name Bruhat--Tits is modern identification, not an extra theorem attributed to this retelling. No assertion about higher-rank buildings is inferred.",
 TFATE,"established rank-one building; the notebook contains no unresolved tree theorem.",TREF)

item(273,"P000452-P000453","remark","Analogy with the hyperbolic plane and the unspecified Weil reference",
 r"The graph is described as an analogue of the Lobachevsky plane, with a disk drawing and a brief \ru{см. А. Вейль} near the distance discussion.",
 r"The precise content available is the analogy between \(\mathrm{PGL}_2(K)/\mathrm{PGL}_2(A)\) with its lattice-tree metric and an archimedean rank-one symmetric space. The drawing does not identify the tree with a two-dimensional hyperbolic manifold, and no particular theorem or work of Weil is named.",
 r"Only the explicit analogy is retained. The bibliographic allusion is unresolved, but the mathematical tree construction is identified independently and is not classified F solely because that allusion lacks a title.",
 r"\citet[Introduction, pp.~130--131]{mumford1972degenerating} explicitly develops the same local-field/upper-half-plane analogy before this lecture. The notes do not provide enough information to identify the intended Weil citation.",
 "an established analogy, with one unidentified bibliographic allusion and no additional definite problem.",TREF,
 match="partial",confidence="medium")

corr("P000452","Manin heading","first lecture of Manin","retelling of Manin's first lecture",r"The original heading ends (\ru{пересказ}); this qualifies the attribution of the surviving notes.",typ="provenance")
corr("P000453","two-summand quotient variant",r"\(L_1/L_2=A/\pi^{\nu_1}A\oplus A/\pi^{\nu_2}A\) without an inclusion qualification",r"Use representatives with \(L_2\subset L_1\) and nonnegative exponents; the distance remains \(\lvert\nu_1-\nu_2\rvert\) independently.","The initial normalized inclusion is explicit in the scan; the later quotient variant suppresses that convention.")
save()

RREF=["serre1979local","milne2020ant"]
RFATE=r"This is classical local ramification theory, already organized in Serre's 1962 \emph{Corps locaux}; the opened English edition is \citet[Chapter~IV, pp.~61--79]{serre1979local}. The precise formulas and proofs were read in \citet[Lemma~7.57, Theorem~7.58, and Corollary~7.59, pp.~130--131]{milne2020ant}; this modern check is not evidence of a later discovery."

talk(274,"1972-09-25","D. A. Kazhdan","P000454-P000455",
 "Local-field ramification as preparation for Tate's p-divisible groups",
 r"The heading identifies Tate's paper in the Russian translation, \emph{Matematika} 13:2, \S3. The surviving mathematics is a preparatory account of finite Galois extensions of local fields: the ramification filtration, residue and tame characters, additive higher quotients, and solvability. The notebook shifts the usual lower-numbering convention by one. It introduces \(\mathbb C_p\), but does not state Tate's later theorem on its Galois action, so that theorem is not silently supplied as a talk item.")

item(274,"P000454","definition","The field C p and the exact Tate reading target",
 r"The heading cites \ru{ст. Тэйта, Математика, 13:2, \S3} and defines \(\mathbb C_p\) as the completion of an algebraic closure of \(\mathbb Q_p\).",
 r"Fix an algebraic closure \(\overline{\mathbb Q}_p\), extend the \(p\)-adic absolute value uniquely to it, and let \(\mathbb C_p\) be its completion. The target reference is \S3 of Tate's \emph{p-Divisible Groups}; no specific theorem about \(\mathbb C_p\) beyond this construction is stated on the surviving pages.",
 r"The bibliographic identification is exact: the 1969 Russian translation, pp.~3--25, appeared in the specified volume and issue. The English original appeared in the proceedings of the 1966 Driebergen local-fields conference in 1967. The heading's intended destination is kept separate from the finite-extension preliminaries actually recorded.",
 r"\citet[\S3]{tate1967pdivisible} is the identified source, in Manin's 1969 Russian translation. The citation predates Kazhdan's 1972 exposition; no new Tate theorem is inferred from the heading.",
 "the construction and reading reference are identified; the notes do not support an additional Hodge--Tate comparison item.",["tate1967pdivisible"])

item(274,"P000454","definition","Finite local Galois extensions and normalized valuation",
 r"The notes write \(K/\mathbb Q_p\) and \(L/K\) finite, set \(G=\operatorname{Gal}(L/K)\), introduce their integer and residue rings, and choose \(|\pi|=|k|^{-1}\).",
 r"Let \(K/\mathbb Q_p\) be finite and let \(L/K\) be finite Galois. Write \(\mathcal O_K,\mathcal O_L\) for integer rings, \(\mathfrak m_K=(\pi),\mathfrak m_L=(\tau)\), and \(k,\ell\) for residue fields. Normalize \(|\pi|_K=|k|^{-1}\), and use its unique extension to \(L\); every element of \(G\) preserves this valuation and \(\mathcal O_L\).",
 r"The Galois hypothesis is supplied because it is needed for the surjectivity onto \(\operatorname{Gal}(\ell/k)\) asserted later. Simply naming the automorphism group of an arbitrary finite extension is not enough. The valuation on \(L\) here extends the chosen one on \(K\), rather than being independently normalized by \(|\ell|\).",
 RFATE,"standard local-field setup with the Galois hypothesis made explicit.",RREF,
 literal="correct with missing hypotheses")

item(274,"P000454","definition","Ramification filtration and its shifted indexing",
 r"The definition is \(G_i=\{g:\ g(x)-x\in\mathfrak m_L^i\text{ for every }x\in\mathcal O_L\}\), with \(G=G_0\supset G_1\supset\cdots\supset\{1\}\); every \(G_i\) is normal.",
 r"For the finite Galois extension just specified, define \(G_i^{\rm note}\) by that formula for \(i\geq0\). These are normal subgroups of \(G\), eventually trivial. They satisfy \(G_0^{\rm note}=G\) and \(G_i^{\rm note}=G_{i-1}^{\rm lower}\) for \(i\geq1\), where the conventional lower filtration has inertia at index zero.",
 r"The shifted indexing is intentional and consistent across both pages; it is not silently changed. Eventual triviality follows from finiteness of \(G\) and separation of the valuation topology, not from a fixed universal length.",
 RFATE,"classical filtration with an explicitly recorded one-place indexing shift.",RREF)

item(274,"P000454-P000455","theorem","Residue-field quotient and the exercise on surjectivity",
 r"Reduction gives \(\psi:G\to\operatorname{Gal}(\ell/k)\); its kernel is \(G_1\), and proving that the induced injection \(G_0/G_1\to\operatorname{Gal}(\ell/k)\) is an isomorphism is left as an exercise.",
 r"For a finite Galois extension of nonarchimedean local fields, reduction yields the exact sequence \(1\to G_1^{\rm note}\to G\to\operatorname{Gal}(\ell/k)\to1\). The quotient is cyclic, generated by the finite-field Frobenius. A residue element must be lifted to \(\mathcal O_L\); kernel membership means fixing every residue element.",
 r"The notebook writes a lift \(x\in L\) and suppresses the universal quantifier in one line; the lift must be integral. The exercise is a classical expository task with a definite known answer, not a new research problem; it is therefore indexed as an occurrence but not assigned a new problem identifier.",
 RFATE + r" The surjectivity is explicit in Milne's Theorem~7.58(a).",
 "the exercise is solved by the standard maximal unramified subextension argument.",RREF,
 literal="correct with missing hypotheses",development="annotated")

item(274,"P000455","theorem","Tame character on the first inertia quotient",
 r"The map \(g\mapsto\overline{g(\tau)/\tau}\) is said to identify \(G_1/G_2\) with a subgroup of \(\ell^\times\), independently of the uniformizer.",
 r"For \(g\in G_1^{\rm note}\), let \(\chi(g)=\overline{g(\tau)/\tau}\in\ell^\times\). This is a homomorphism, its kernel is \(G_2^{\rm note}\), and it is independent of the uniformizer \(\tau\). Thus tame inertia \(G_1^{\rm note}/G_2^{\rm note}\) is cyclic of order prime to the residue characteristic.",
 r"Independence uses inertia: if \(\tau'=u\tau\) with \(u\in\mathcal O_L^\times\), then \(g(u)/u\) reduces to one. The map is first defined on \(G_1\), and only then induces an injection on its quotient.",
 RFATE + r" See Milne's Corollary~7.59 and its first character computation.",
 "the standard tame-inertia character.",RREF)

item(274,"P000455","theorem","Additive characters on higher ramification quotients",
 r"For \(i\geq2\), the notes use \(\overline{(g(\tau)/\tau-1)/\tau^{i-1}}\in\ell\) and state that its kernel is \(G_{i+1}\), although the displayed domain is already \(G_i/G_{i+1}\).",
 r"For \(i\geq2\), the map \(c_i:G_i^{\rm note}\to(\ell,+)\), \(c_i(g)=\overline{(g(\tau)-\tau)/\tau^i}\), is a homomorphism with kernel \(G_{i+1}^{\rm note}\). Consequently \(G_i^{\rm note}/G_{i+1}^{\rm note}\) embeds in the additive residue group and is an elementary abelian \(p\)-group.",
 r"The character's domain is repaired before taking the quotient; an injective map defined on \(G_i/G_{i+1}\) has trivial kernel, not \(G_{i+1}\). Unlike the tame character, these coordinate-valued higher characters can change with the uniformizer, although the quotient statement is intrinsic.",
 RFATE + r" The same calculation, with the usual one-place shift, is the second part of Milne's Corollary~7.59.",
 "the higher quotient theorem is standard; the literal domain/kernel combination is inconsistent.",RREF,
 literal="false as written",match="partial",development="annotated")

item(274,"P000454-P000455","theorem","Solvability of finite local Galois groups",
 r"Kazhdan announces that the filtration will show \(G\) is solvable; every successive quotient is declared abelian.",
 r"For every finite Galois extension \(L/K\) of nonarchimedean local fields with finite residue field, \(\operatorname{Gal}(L/K)\) is solvable: the residue quotient is cyclic, the tame quotient is cyclic, and the remaining finite filtration has elementary abelian \(p\)-quotients.",
 r"The finite residue field and Galois assumptions are essential to this precise formulation; the statement is not a theorem about arbitrary discretely valued fields or arbitrary global number fields.",
 RFATE + r" Milne's Corollary~7.59 states the solvability conclusion explicitly.",
 "classical and completely proved; no outstanding solvability question is stated.",RREF,
 literal="correct with missing hypotheses")

item(274,"P000455","definition","Unramified, tame, and totally ramified extensions",
 r"The page calls \(G_1=1\) unramified, \(G_2=1\) \ru{слаборазветвл.}, translated weakly ramified, and \(G_0=G_1\) purely ramified.",
 r"In the notebook's shifted numbering, a finite Galois local extension is unramified iff \(G_1^{\rm note}=1\), tamely ramified iff \(G_2^{\rm note}=1\), and totally ramified iff \(G_0^{\rm note}=G_1^{\rm note}\). Modern weak ramification instead means \(G_2^{\rm lower}=1\), equivalently \(G_3^{\rm note}=1\).",
 r"The old descriptive phrase must not be conflated with the now distinct technical term weakly ramified. The translation is literal, so this is primarily a terminology annotation rather than evidence that the original writer miscomputed the groups.",
 RFATE + r" Milne's paragraph after Corollary~7.59 identifies tame and unramified extensions in the standard numbering. The modern distinction from weak ramification is explicit in \citet[\S1, p.~1]{johnston2012weak}, first posted in April 2012; that source is used for terminology only.",
 "the three intended notions are identified, with tame replacing weak in modern terminology.",RREF+["johnston2012weak"],
 literal="correct with missing hypotheses",match="partial",development="annotated")

corr("P000454","finite-extension setup",r"\(L/K\) finite; \(G=\operatorname{Gal}(L/K)\)",r"Assume \(L/K\) finite Galois for the later residue quotient isomorphism.","Original page omits Galois; the surjectivity exercise on P000455 needs it. Milne 2020, Theorem 7.58.")
corr("P000454","residue-field lift and kernel",r"\(x\in L\); \(\bar x^g=\bar x\) without explicit quantifier",r"Choose \(x\in\mathcal O_L\) lifting \(\bar x\); \(g\) is in the kernel iff every \(\bar x\in\ell\) is fixed.","Original scan and the definition of reduction modulo the maximal ideal.")
corr("P000455","domain and kernel of higher character",r"\(\psi_i:G_i/G_{i+1}\to\ell\); \(\ker\psi_i=G_{i+1}\)",r"Define \(\psi_i\) on \(G_i\) with that kernel, or state that its induced map from \(G_i/G_{i+1}\) is injective.","P000455 scan has the same domain/kernel inconsistency; Milne 2020, Corollary 7.59.")
corr("P000455","ramification terminology",r"weakly ramified means \(G_2=1\)",r"tamely ramified in modern terminology; modern weak ramification would mean \(G_3=1\) in the notebook's indexing.",r"The Russian scan has \ru{слаборазветвл.}; the distinction is terminological, not a mistranscription.",typ="ambiguity")
save()

talk(275,"1972-10-02","A. M. Gabrielov","P000456-P000458",
 "Local systems, flat connections, and polarized Hodge flags",
 r"The continuation rebuilds the sheaf and bundle foundations carefully, gives the flat connection in a local constant frame, then returns to polarized flag domains. It repeats the classical line of record 272 with fuller definitions. The original scan reverses the parity of the polarization, a substantive mathematical error. The final two bare headings, Manin's second lecture and Kazhdan again on Tate, contain no additional mathematical assertions and are recorded as headings in this summary only.")

item(275,"P000456","definition","Constant sheaf and its étalé space",
 r"The constant sheaf \(\mathbb Z\) has constant-number sections over a connected domain; it is associated to the presheaf \(U\mapsto\mathbb Z\). Its sheaf space is written \(S\times\mathbb Z\).",
 r"On a complex manifold \(S\), the constant sheaf \(\underline{\mathbb Z}\) is the sheaf of locally constant integer-valued functions, equivalently the sheafification of the constant presheaf. Its \(\acute{e}\)tal\'{e} space is \(S\times\mathbb Z\), with \(\mathbb Z\) discrete. On a connected nonempty open set its sections are \(\mathbb Z\); on a disconnected open set they need not be globally constant.",
 r"The sheafification and connected-open qualification are part of the mathematical distinction being explained in the notes, not a new theorem. The empty set convention for the constant presheaf is immaterial after sheafification.",
 GDATE + r" This elementary local-system background underlies the bundle formulation used there.",
 "standard sheaf theory and the intended foundation for the Hodge discussion.",G,
 match="partial")

item(275,"P000456","construction","Integral local systems from locally constant transition functions",
 r"Locally \(H_{\mathbb Z}|_U\cong U\times\mathbb Z^n\), \(\Gamma(U,H_{\mathbb Z})\cong\mathbb Z^n\), and transition functions take values in \(\mathrm{GL}_n(\mathbb Z)\); connectedness of \(S\) makes the rank constant.",
 r"A rank-\(r\) integral local system is obtained by gluing constant sheaves on a trivializing cover with locally constant \(\mathrm{GL}_r(\mathbb Z)\)-valued transition functions satisfying the cocycle condition. Its rank is locally constant, hence constant on connected \(S\). The section formula \(\Gamma(U,H_{\mathbb Z})\cong\mathbb Z^r\) holds for connected trivializing \(U\).",
 r"The displayed product is the local \(\acute{e}\)tal\'{e}-space model; \(U\) must be connected for the asserted section group. The cocycle condition is implicit in the gluing language and is stated explicitly here.",
 GDATE + r" This revisits 1972-272.1 with a transition-function description.",
 "standard gluing description, not a newly posed classification problem.",G,
 literal="correct with missing hypotheses",match="partial")

item(275,"P000456","construction","Associated real, complex, and holomorphic bundles",
 r"Using the same transition matrices, the notes construct \(H_{\mathbb R}\), \(H_{\mathbb C}\), and the sheaf \(H_{\mathcal O}\) of holomorphic sections, with \(H_{\mathcal O}=H_{\mathbb Z}\otimes_{\mathbb Z}\mathcal O_S\).",
 r"Extend the transition matrices of an integral local system along \(\mathbb Z\subset\mathbb R\subset\mathbb C\). This produces real and complex flat vector bundles; the latter's locally constant transition functions are holomorphic and define a holomorphic bundle whose sheaf of sections is \(\mathcal H=H_{\mathbb Z}\otimes\mathcal O_S\).",
 r"The local system of flat sections, the total vector bundle, and the sheaf of all holomorphic sections are distinguished explicitly; the notebook uses one symbol in more than one of these senses.",
 GDATE,
 "the standard passage from integral monodromy to a flat holomorphic bundle.",G)

item(275,"P000456-P000457","construction","Flat connection in a locally constant frame",
 r"The connection is \(\mathbb C\)-linear, satisfies \(\nabla(\varphi f)=\varphi\nabla f+d\varphi\otimes f\), and in a constant frame \(u_i\) is \(\nabla\sum_i\varphi_i u_i=\sum_i d\varphi_i\otimes u_i\). Its curvature is zero.",
 r"For a holomorphic bundle defined by locally constant transition matrices, the local operator \(d\) in each constant frame glues to a globally defined holomorphic connection. It is complex-linear, satisfies the displayed Leibniz rule, and its extension to bundle-valued forms has \(\nabla^2=0\). Its horizontal sheaf is exactly the initial complex local system.",
 r"The connection is not \(\mathcal O_S\)-linear; complex-linearity and the Leibniz rule are the correct axioms. Zero curvature is both explicitly stated and justified by the local formula, so it is not merely an omitted hypothesis here.",
 GDATE + r" This expands the flat/Gauss--Manin construction in 1972-272.2.",
 "a complete standard local construction with no unresolved step.",G)

item(275,"P000457","definition","Horizontal polarization and transversality of the Hodge filtration",
 r"The holomorphic filtration is again required to satisfy Griffiths' condition, and a locally constant bilinear form \(\psi\) is required to produce a Hodge structure at every point.",
 r"For the flat holomorphic bundle \((\mathcal H,\nabla)\), require decreasing holomorphic subbundles \(F^p\mathcal H\) with \(\nabla F^p\subset\Omega_S^1\otimes F^{p-1}\), and a flat bilinear form \(Q\). Together with fibrewise opposition, weight parity, and positivity, these give a polarized variation of pure Hodge structure.",
 r"The form's local constancy means \(\nabla Q=0\), and the filtration need not be flat. The later fibrewise relations, including the parity correction in the next item, are incorporated only as explicitly identified components of the definition.",
 GDATE + r" The transversality equation is (2.1). This is a repeat of 1972-272.3, not an independent research problem.",
 "standard polarized variation; the notes' repetition is preserved in the occurrence index.",G)

item(275,"P000458","claim","Parity of the polarization is reversed in the notebook",
 r"The form is said to be symmetric for odd \(n\) and skew-symmetric for even \(n\). Both Russian and English transcriptions follow the handwriting.",
 r"For a pure polarized Hodge structure of weight \(n\), the bilinear polarization satisfies \(Q(y,x)=(-1)^n Q(x,y)\): it is symmetric for even \(n\) and alternating for odd \(n\). With the notebook's Weil-operator convention, an overall real sign can be chosen so that \(Q(x,C\bar y)\) is positive Hermitian.",
 r"The parity reversal is a faithful mathematical error, not a translation correction. Changing an overall sign of \(Q\) cannot change symmetric into alternating; it therefore cannot explain the reversed statement.",
 r"\citet[\S1, equations (1.7)--(1.15)]{griffiths1968periods1} gives the correct parity and bilinear relations before the talk; \citet[\S2]{griffiths1970periods} summarizes the same framework.",
 "the literal parity claim is false, and the standard correction is unambiguous.",["griffiths1968periods1","griffiths1970periods"],
 literal="false as written",match="partial",development="annotated")

item(275,"P000457-P000458","construction","Projective flag variety and the corrected isotropic compact dual",
 r"For dimensions \(k_0\geq k_1\geq\cdots\geq k_n\), the flag space is projective algebraic. The following page now writes \(\psi(F^p,F^{n-p+1})=0\) with the correct index.",
 r"In a fixed complex vector space, flags of dimensions \(k_p\) form a projective partial flag variety. Imposing the closed bilinear relations \(Q(F^p,F^{n-p+1})=0\), with dimensions compatible with a polarized weight-\(n\) Hodge structure, gives the compact dual; a connected component is chosen when necessary.",
 r"The dimensions are constrained by the intended Hodge numbers and the nondegenerate form; arbitrary numerical flags need not admit polarized Hodge points. P000458 corrects the earlier index internally, but does not explicitly announce an erratum.",
 GDATE + r" The flag variety and the bilinear subvariety are separated here to make the algebraic and positivity conditions transparent.",
 "standard projective compact dual; the correct formula links back to the emendation of 1972-272.4.",G,
 literal="correct with missing hypotheses")

item(275,"P000458","construction","Opposition, Weil operator, and positivity define the period domain",
 r"The page imposes \(F^p\oplus\overline{F^{n-p+1}}=H_{\mathbb C}\), defines the Weil operator by Hodge type, requires \(\psi(x,C\bar y)\) positive Hermitian, and calls \(D\) open in \(\overline D\).",
 r"After correcting the parity of \(Q\), the opposition identities recover the Hodge decomposition; let \(C|_{H^{p,n-p}}=i^{2p-n}\). The flags for which \(Q(x,C\bar y)\) is positive definite form the period domain, open in the isotropic compact dual, determined by the Hodge numbers and the fixed real polarization form.",
 r"This combines the page's related fibrewise defining relations into one item, while retaining parity and the compact-dual construction as separate claims because each has its own correction or hypothesis.",
 GDATE,
 "classical period-domain construction; this repeats 1972-272.5--6 with no new question.",G)

item(275,"P000458","claim","Announced homogeneity and the identity-component qualification",
 r"For next time, the complex isometry group is to be shown transitive on \(\overline D\), and the identity component of the real group transitive on \(D\).",
 r"The relevant complex isometry group acts transitively on each appropriate isotropic flag orbit. The identity component \(G_{\mathbb R}^0\) acts transitively on a chosen connected component of the polarized period domain. If \(D\) denotes all components at once, transitivity of the identity component need not hold.",
 r"A connected-component choice is supplied. The notes announce an elementary homogeneous-space proof for a subsequent meeting; they do not formulate homogeneity as an open problem.",
 r"\citet[\S2, especially equation (2.3)]{griffiths1970periods} already uses the homogeneous presentation. Its underlying exposition circulated in the 1968 invited lecture and was published in 1970.",
 "established homogeneity with the component convention stated explicitly.",G,
 literal="correct with missing hypotheses",development="annotated")

corr("P000456","local section group",r"\(\Gamma(U,H_{\mathbb Z})=\mathbb Z^n\) for an unspecified trivializing \(U\)",r"Assume \(U\) connected, or use locally constant maps \(U\to\mathbb Z^n\).",r"The scan's local trivialization does not by itself require connected \(U\); the earlier sentence handles connected domains.")
corr("P000458","polarization parity",r"symmetric for odd \(n\) and skew-symmetric for even \(n\)",r"symmetric for even \(n\) and alternating for odd \(n\)","Confirmed directly in P000458 scan; Griffiths 1968 I, equations (1.7)--(1.15).")
corr("P000458","real-group transitivity",r"the identity component acts transitively on \(D\)",r"the identity component acts transitively on each chosen connected component of \(D\)","The scan explicitly says component of unity; disconnected period domains require this qualification.")
corr("P000458","two final headings","Manin's 2nd lecture; D. Kazhdan, more on Tate","Bare continuation headings without surviving mathematical content on this page","Original scan; no assertion or new problem is recoverable from the headings alone.",typ="provenance")
save()

VREF=["vaserstein1973foundations","vaserstein1976foundations"]
VDATE=r"The exact framework appears in \citet{vaserstein1973foundations}, received on 14 November 1972, the day after this talk; the detailed treatment \citet{vaserstein1976foundations} was received on 26 February 1975 and published in 1976."
VOLD=r"\citet[\S1]{volodin1971extraordinary} had already published a flag-based simplicial approach in 1971, from a manuscript received on 27 July 1970. Its general module-flag formulation should not be confused term by term with every coordinate convention of this talk."

talk(280,"1972-11-13","L. N. Vasserstein","P000468-P000470",
 "Simplicial algebraic K theory, stabilization, and Steinberg groups",
 r"Vasserstein builds the quasiunit and matrix functors, the permutation-triangular simplicial space, its homotopy groups and block-sum structure, the cone swindle, and the low-degree identifications with elementary and Steinberg groups. A unital-ring hypothesis is explicitly introduced on P000469 and must be retained; the talk's initial allowance of nonunital rings does not erase that restriction. The short Foundations announcement was received the next day. The final tolerance question is an exact assertion in the later 1976 paper, but is false for the literal simplicial definition: three stable elementary matrices give a minimal-rank obstruction. The correction is developed as a published-claim audit, not relabelled as an undisseminated open idea.")

item(280,"P000468","construction","Formal unitization of an associative ring",
 r"For an associative ring \(A\), not necessarily with identity, \(iA\) formally adjoins an identity, with \(A\) a two-sided ideal and \(iA/A=\mathbb Z\); \(i\) is a functor.",
 r"For any associative ring \(A\), define \(iA=\mathbb Z\oplus A\) additively, with \((m,a)(n,b)=(mn,mb+na+ab)\). Its identity is \((1,0)\), the map \(A\to iA\), \(a\mapsto(0,a)\), identifies an ideal, and \(iA/A\cong\mathbb Z\). Every ring homomorphism induces the identity on \(\mathbb Z\) and the given map on \(A\).",
 r"The multiplication, implicit in formal adjoining, is written explicitly. Even if \(A\) already has an identity, this formal unitization is not being identified with \(A\) itself.",
 VDATE + r" See \citet[\S1, pp.~100--101]{vaserstein1976foundations}. The elementary unitization construction itself is antecedent background, so its occurrence is E.",
 "standard functorial unitization used to organize nonunital K theory.",VREF)

item(280,"P000468","definition","Quasiunits under the circle product",
 r"The law \(a\circ b=a+b+ab\) is associative, and \(GA\subset A\) is its group of invertible elements with identity zero. The map \(a\mapsto1+a\) is described as a homomorphism into ordinary units.",
 r"The operation \(\circ\) makes \(A\) a monoid with identity zero. Its invertible elements are precisely \(GA=\{a\in A:1+a\in(iA)^\times\}\), and \(a\mapsto1+a\) identifies this group with the units of \(iA\) congruent to one modulo \(A\). Ring homomorphisms preserve quasiunits and give a group-valued functor \(G\).",
 r"The map from all of \(A\) lands in the multiplicative monoid \(1+A\), not necessarily its unit group; only its restriction to \(GA\) lands in units. For example, \(-1\) in a nonzero unital ring is not quasiinvertible.",
 VDATE + r" The precise quasiunit convention is \citet[\S2, p.~101]{vaserstein1976foundations}.",
 "the quasiunit construction is standard; the literal unrestricted units statement needs correction.",VREF,
 literal="false as written",match="partial",development="annotated")

item(280,"P000468","construction","Finite matrix stabilization and the stable general linear group",
 r"The notes introduce \(M_kA\), the finite-support matrix ring \(MA\), and its quasiunit group \(GMA\).",
 r"Let \(M_kA\) be the ring of \(k\times k\) matrices and \(MA=\bigcup_k M_kA\) under upper-left embeddings with zero complementary block. For unital \(A\), the map \(a\mapsto I+a\) identifies \(GMA\) with the stable group \(\mathrm{GL}(A)=\varinjlim_k\mathrm{GL}_k(A)\), whose stabilization adjoins identity blocks.",
 r"The zero-block and identity-block stabilization conventions agree only after the change from circle coordinates to ordinary multiplicative coordinates. The finite-support ring \(MA\) is not itself unital when \(A\ne0\).",
 VDATE + r" See \citet[\S3, p.~101]{vaserstein1976foundations}. These standard matrix conventions are also the background of 1971-256.1.",
 "standard stable matrix group, with both coordinate conventions distinguished.",VREF)

item(280,"P000468","construction","Row-and-column-finite cone and suspension rings",
 r"The ring \(\widetilde\Omega A\) consists of infinite matrices with finitely many nonzero entries in every row and column; \(MA\) is its finite-support two-sided ideal, and \(\Omega A=\widetilde\Omega A/MA\).",
 r"With indices in \(\mathbb N\), row-and-column-finite matrices over any associative ring form a ring under ordinary matrix multiplication: each entry is a finite sum and row and column finiteness are preserved. Finite-support matrices form a two-sided ideal. The quotient is the notebook's suspension ring. All three constructions are functorial in \(A\).",
 r"The tilde distinguishes the cone from its quotient throughout this chapter; later sources use different Omega decorations. No boundedness condition on the number of entries per row is imposed by these notes.",
 VDATE + r" The definitions occur at the start of the 1973 announcement and in \citet[\S3]{vaserstein1976foundations}. Earlier occurrences are 1971-253.5 and 1971-256.2.",
 "established cone/suspension machinery; the later vanishing theorem is a separate item.",VREF)

item(280,"P000468","definition","Strict triangular matrices and their quasiinverses",
 r"The subring \(\Theta A\) is called upper triangular but is defined by \(a_{ij}=0\) for \(i\leq j\); the page says \(G\Theta A=\Theta A\) because its matrices are nilpotent.",
 r"Choose either strict upper triangular finite-support matrices, with \(a_{ij}=0\) for \(i\geq j\), or the transposed lower convention. Every such matrix \(a\) is nilpotent, and its circle inverse is the finite sum \(-a+a^2-a^3+\cdots\). Thus the triangular ring is a group under \(\circ\). The union over coordinate permutations is the same with either choice of orientation.",
 r"The word upper and the written inequality disagree in the handwriting. The choice is harmless for the subsequent permutation-triangular construction, but the two conventions are not presented as literally identical definitions.",
 r"\citet[\S3 and \S11]{vaserstein1976foundations} uses triangular matrices in the same simplicial construction; the nilpotent inverse is the elementary geometric-series identity.",
 "standard nilpotent quasiunit subgroup with a recorded orientation inconsistency.",["vaserstein1976foundations"],
 literal="correct with missing hypotheses",match="partial",development="annotated")

item(280,"P000468","claim","Reindexing requires injective maps",
 r"A bijection \(\mathbb N\to\mathbb N\) simultaneously permutes rows and columns and is called an inner automorphism. The next sentence claims that even any map \(\mathbb N\to\mathbb N\) gives an endomorphism.",
 r"Every injection \(e:\mathbb N\hookrightarrow\mathbb N\) gives a ring embedding \(MA\to MA\) by placing \(a_{ij}\) in position \((e(i),e(j))\) and filling other entries with zero; bijections give automorphisms. Arbitrary noninjective reindexings do not preserve matrix multiplication. For unital \(A\), a permutation is implemented by conjugation in the larger row-and-column-finite matrix ring, but need not be inner in the finitary stable group.",
 r"\ours\ A collapsed pair of indices sends two orthogonal diagonal matrix units \(E_{11},E_{22}\) over \(\mathbb Z\) to the same \(E_{kk}\): their original product is zero and the product of their images is not. Thus injectivity is indispensable. The ambient meaning of inner is supplied separately.",
 r"\citet[\S4, pp.~101--102]{vaserstein1976foundations} correctly uses embeddings of \(\mathbb N\); it matches the repaired statement, not the arbitrary-map wording.",
 "the notebook's arbitrary-map assertion is false; the injection construction is elementary and established.",["vaserstein1976foundations"],
 literal="false as written",match="partial",development="annotated")

item(280,"P000468-P000469","construction","Permutation-triangular simplices and the based space S A",
 r"A finite \(X\subset GMA\) is a simplex if a common left translation followed by a coordinate permutation carries it into \(\Theta A\). The distinguished vertex is zero, and the resulting simplicial scheme is \(SA\). Volodin is credited for its use in K theory.",
 r"In multiplicative coordinates for unital \(A\), let \(U_\prec\) be the stable unitriangular subgroup for a total coordinate order obtained by a permutation. A finite vertex set \(X\subset\mathrm{GL}(A)\) is a simplex exactly when \(X\subset gU_\prec\) for some \(g\) and one order \(\prec\). The identity is the base vertex. This defines an abstract simplicial complex and functorial maps under ring homomorphisms.",
 r"A single translation and a single order must work for the whole set. Replacing this by a separate order for each pair changes the complex. The literal coordinate model is kept distinct from more general module-flag versions. The notebook's zero vertex corresponds to \(I\).",
 VOLD + " " + VDATE + r" The left-translation definition is explicit in the 1973 announcement; \citet[\S11, Remark~(b), pp.~110--111]{vaserstein1976foundations} uses the right-translation version and identifies the two via inversion. See also 1971-253.1 and 1971-256.1.",
 "an identified early simplicial K-theory model; its false tolerance assertion is separately audited below.",
 ["volodin1971extraordinary","vaserstein1973foundations","vaserstein1976foundations"])

item(280,"P000469","definition","Positive K groups from homotopy groups under the stated unit hypothesis",
 r"The page explicitly begins \ru{Пусть в кольце A есть единица} before defining \(K_nA=\pi_{n-1}SA\), \(n\geq1\). It notes the usual group structure for \(n\geq2\) and automatic abelianity for \(n\geq3\).",
 r"For an associative unital ring \(A\), define the positive groups in this model by \(K_n(A)=\pi_{n-1}(|SA|,I)\) for \(n\geq1\), with \(K_1\) initially the based set of components until its group law is supplied. This unital Volodin-type model agrees with algebraic K theory after the comparison theorem. The displayed formula alone does not define \(K_0\) or negative groups.",
 r"The unital hypothesis is genuinely on the scan and is not an editorial repair. The notation \(\pi\) is interpreted via realization, equivalently the combinatorial homotopy model used in the later paper. Nonunital groups require the relative/unitization construction and must not be substituted into this formula without further hypotheses.",
 VOLD + " " + VDATE + r" \citet[Corollary~15.1 and Chapter~V]{vaserstein1976foundations} gives the unital identification and comparison. The general comparison is already tracked by GP-1971-21, but this page poses no new comparison question.",
 "an established model for unital positive algebraic K theory; no claim for arbitrary nonunital rings is inferred.",
 ["volodin1971extraordinary","vaserstein1973foundations","vaserstein1976foundations"])

item(280,"P000469","method","Whitehead stabilization homotopy and five block matrices",
 r"Reindexing a sphere map is said not to change its homotopy class. The proof moves a finite matrix block using five circle-coordinate matrices: \(\left(\begin{smallmatrix}a&0\\0&0\end{smallmatrix}\right)\), \(\left(\begin{smallmatrix}a&a\\0&0\end{smallmatrix}\right)\), \(\left(\begin{smallmatrix}0&a\\-I&0\end{smallmatrix}\right)\), \(\left(\begin{smallmatrix}0&0\\-I&a\end{smallmatrix}\right)\), \(\left(\begin{smallmatrix}0&0\\0&a\end{smallmatrix}\right)\).",
 r"For a unital ring and a based simplicial representative of a homotopy class in \(SA\), every injective coordinate reindexing induces the same homotopy class. After reducing to a finite block and a block swap, consecutive maps in the displayed five-step construction are contiguous, giving a homotopy from a matrix block to its shifted copy. All entries \(-I\) belong to the ring because the unit hypothesis is in force.",
 r"Finite-block reduction is made for a finite simplicial representative; it is not an assertion that an arbitrary continuous map has a literal image consisting of finitely many vertices. This is a specific simplicial implementation of the older Whitehead stabilization idea.",
 VDATE + r" The exact five-block method and its contiguity checks occur in \citet[Lemma~13.1 and Theorem~13.1, pp.~112--114]{vaserstein1976foundations}; class A concerns this implementation, not priority for Whitehead's original lemma.",
 "the detailed stabilization construction is published and valid with the stated unit convention.",VREF,
 cls="A")

item(280,"P000469","definition","Elementary simplicial homotopy is contiguity",
 r"Maps \(s_1,s_2\) are elementarily homotopic when \(s_1X\cup s_2X\) is a simplex for every source simplex \(X\). The line naming the domains and codomains reuses \(S'\) inconsistently.",
 r"Two simplicial maps \(s_1,s_2:S\to T\) are contiguous if, for each simplex \(X\) of \(S\), the union \(s_1(X)\cup s_2(X)\) is a simplex of \(T\). Their realizations are homotopic; a finite chain of such contiguities gives the combinatorial homotopies used here.",
 r"The source and target letters are normalized; the substantive simplex condition is unchanged. Pairwise adjacency of images alone is insufficient for contiguity unless the target is flag, and the target in this talk is not flag in general.",
 r"\citet[\S\S7--10, especially \S9, Remark~(b)]{vaserstein1976foundations} formalizes this standard simplicial notion before applying it to the five-block argument.",
 "standard contiguity, with the required whole-simplex condition preserved.",["vaserstein1976foundations"],
 literal="correct with missing hypotheses",development="annotated")

item(280,"P000469-P000470","construction","Interleaved block sum and its homotopy invariance",
 r"The injections \(f(i)=2i\), \(g(i)=2i+1\) give \(a\oplus b=a^f+b^g\). The raw operation is described as noncommutative, nonassociative, and without a neutral element; it induces \(SA\times SA\to SA\).",
 r"Disjoint coordinate embeddings define a block-sum map on finite matrices and on the simplicial spaces. Different choices of embeddings, parenthesization, and order are related on homotopy groups by stabilization homotopies. Consequently the operation on classes has a neutral element and is independent of those choices, even though the chosen coordinate formula is not strictly associative or strictly unital.",
 r"The product is the simplicial product appropriate to the model, and the claim about operations on all \(K_i\), \(i\geq0\), exceeds the displayed definition when \(i=0\); here the conclusion is restricted to \(i\geq1\). A separately defined \(K_0\) also has direct sum, but is not constructed on these pages.",
 VDATE + r" See \citet[\S4 and Corollary~13.1]{vaserstein1976foundations}. The basic block-sum idea is older; the source supplies the precise coordinate and homotopy bookkeeping.",
 "established block-sum operation in positive K theory; the isolated zero index is annotated.",VREF,
 literal="correct with missing hypotheses",development="annotated")

item(280,"P000470","theorem","Interchange gives abelian group structures",
 r"Block sum and the previously introduced homotopy operations are mutually distributive, hence coincide and are commutative. The page describes the resulting sum as an H-space structure.",
 r"Under the unital hypothesis, block sum induces abelian group laws on all \(K_n(A)\), \(n\geq1\), agreeing with ordinary homotopy-group composition where that already exists. The key algebraic principle is the interchange law for two binary operations with the same two-sided identity: the operations then agree and are associative and commutative. A homotopy-unit H-space formulation expresses the same block-sum construction on realization.",
 r"For \(K_1=\pi_0\), inverses and a group operation must be supplied rather than inferred solely from the topology of components; the ensuing elementary quotient provides them. The word distributive is interpreted as the interchange identity, not the ordinary ring distributive law.",
 r"\citet[Lemma~10.2, Corollary~13.1, and Theorem~13.2]{vaserstein1976foundations} proves exactly these assertions. The interchange principle and the already-known K-group structures are expository; no new general H-space theorem is attributed to the talk.",
 "standard abelian positive K groups, with the low-degree group-law issue accounted for.",["vaserstein1976foundations"])

item(280,"P000470","method","Infinite block sum and vanishing of cone K theory",
 r"On \(\widetilde\Omega A\) even an infinite number of matrices can be summed in blocks; the notes conclude that its K functors are trivial.",
 r"For an associative unital ring \(A\), the row-and-column-finite cone ring admits an infinite-sum endomorphism compatible with two complementary coordinate embeddings. On positive K groups its identity satisfies \(x+\rho_*(x)=\rho_*(x)\); hence \(K_n(\widetilde\Omega A)=0\) for \(n\geq1\). Infinite sums mean a specified block-diagonal placement with finite support in each row and column, not arbitrary entrywise infinite sums.",
 r"The unital hypothesis introduced on P000469 is retained. Extending the vanishing to \(K_0\) and negative degrees requires the separately developed theory; none is defined by the homotopy formula in this talk. This is the algebraic Eilenberg swindle in the specified matrix model.",
 VDATE + r" The first theorem of the 1973 announcement states cone vanishing; \citet[Lemmas~18.1--18.2 and Corollary~18.1]{vaserstein1976foundations} gives the infinite-sum proof. Earlier occurrences are 1971-253.5 and 1971-256.3; A records the subsequent implementation, not a new origin for the swindle.",
 "published cone-vanishing theorem with an exact infinite-sum construction; no unresolved cone problem here.",VREF,
 cls="A",literal="correct with missing hypotheses")

item(280,"P000470","theorem","K one as components modulo elementary matrices",
 r"\(K_1A=\pi_0SA\); \(EA\) is the identity component, described as products of elementary or pseudotriangular matrices.",
 r"For unital \(A\), the component of the identity vertex in \(SA\) consists of the stable elementary subgroup \(E(A)\subset\mathrm{GL}(A)\). Thus \(\pi_0SA\cong\mathrm{GL}(A)/E(A)=K_1(A)\). A path consists of finitely many simplex edges, and triangular factors decompose into elementary transvections.",
 r"Component is understood in the realization or in edge-path connectivity, rather than in a topology on the discrete set of matrices. The ordinary multiplicative elementary matrix is \(I+aE_{ij}\), corresponding to \(aE_{ij}\) in circle coordinates.",
 r"The classical quotient predates the talk; \citet[III, Whitehead's Lemma~1.3.3]{weibel2013kbook} records it and its 1950 antecedent. The exact component computation is \citet[Theorems~14.1--14.2]{vaserstein1976foundations}.",
 "standard K-one identification; no new quotient conjecture.",["weibel2013kbook","vaserstein1976foundations"])

item(280,"P000470","theorem","Elementary perfectness and the idempotent-ring extension",
 r"The notes explicitly allow either \(A\ni1\) or \(AA=A\), then assert \(EA=[GMA,GMA]=[EA,EA]\).",
 r"If \(A\) is an associative ring satisfying \(A^2=A\), where \(A^2\) is the additive subgroup generated by products, then the stable elementary group satisfies \(E(A)=[GMA,GMA]=[E(A),E(A)]\). In particular it is perfect, and the stable quasiunit abelianization is the elementary quotient. A unital ring satisfies the idempotence condition automatically.",
 r"The idempotent condition means finite sums of products, not that every element is a single product. It applies here to the commutator assertion; no blanket extension of every subsequent universal-central-extension claim to all nonunital idempotent rings is inferred.",
 VDATE + r" \citet[Theorem~5.1, pp.~103--104]{vaserstein1976foundations}, applied with \(B=A\), proves the nonunital idempotent extension. The unital Whitehead theorem is older; class A concerns the stated extension and its publication in the speaker's treatment.",
 "published under the precise idempotent-ring hypothesis.",VREF,
 cls="A")

item(280,"P000470","claim","Triangular generators and their elementary relations",
 r"\(\Theta A\) is said to have generators \(a^{ij}\), with \(a\) in position \((i,j)\), the addition relation, the adjacent-root commutator relation, and commuting relations for some other pairs.",
 r"For a fixed coordinate order, the unitriangular group is generated by \(t_{ij}(a)=I+aE_{ij}\), \(i\prec j\), with \(t_{ij}(a)t_{ij}(b)=t_{ij}(a+b)\), \([t_{ij}(a),t_{jk}(b)]=t_{ik}(ab)\) for \(i\prec j\prec k\), and \([t_{ij}(a),t_{kl}(b)]=1\) when \(j\ne k\) and \(i\ne l\). In the stable finite-support setting these are the triangular presentation relations.",
 r"The allowed indices and the omitted commuting condition are reconstructed explicitly. The presentation of a fixed triangular group is distinguished from the all-root Steinberg presentation and from a presentation of \(E(A)\), which generally has additional K-two relations.",
 r"\citet[\S6 and the triangular map in the proof of Theorem~15.2]{vaserstein1976foundations} uses these relations to pass from triangular groups to the Steinberg group. The general relations are also stated in \citet[III, \S5.1]{weibel2013kbook}.",
 "standard triangular elementary relations; the notebook's phrase defining relations is correct only with its group and index set specified.",["vaserstein1976foundations","weibel2013kbook"],
 literal="correct with missing hypotheses",match="partial")

item(280,"P000470","definition","Stable Steinberg group with the missing index restrictions restored",
 r"The group \(\operatorname{St}A\) is generated by all the displayed elementary symbols and Steinberg relations; the commuting cases are abbreviated as some commutators being zero.",
 r"For an associative ring \(A\), define \(\operatorname{St}(A)\) on generators \(x_{ij}(a)\), \(i\ne j\), with \(x_{ij}(a)x_{ij}(b)=x_{ij}(a+b)\), \([x_{ij}(a),x_{jk}(b)]=x_{ik}(ab)\) for distinct \(i,j,k\), and \([x_{ij}(a),x_{kl}(b)]=1\) if \(i\ne l\) and \(j\ne k\). It maps onto \(E(A)\) by \(x_{ij}(a)\mapsto I+aE_{ij}\).",
 r"Zero in the notes is the identity of the circle-law convention; the abstract group relations use one. The full index restrictions are essential. Opposite-root pairs are not declared commuting.",
 r"This is the classical Steinberg construction, treated before the talk in \citet{milnor1972introduction} (publisher date 21 January 1972). The precise presentation was read in \citet[III, Definition~5.1]{weibel2013kbook} and \citet[\S6]{vaserstein1976foundations}; the Milnor publisher page alone is used for chronology, not as a claim to have read its theorem text.",
 "established stable Steinberg presentation.",["milnor1972introduction","weibel2013kbook","vaserstein1976foundations"],
 literal="correct with missing hypotheses")

item(280,"P000470","theorem","Steinberg group as paths and the K two kernel",
 r"Loops represent relations among elementary matrices; the exact sequence \(0\to K_2A\to\operatorname{St}A\to EA\to0\) is displayed. Steinberg-group elements are described as homotopy classes of paths starting at zero with endpoints fixed under homotopy.",
 r"For a unital ring, the path-group model of \(\operatorname{St}(A)\) maps a based path class to its endpoint in \(E(A)\), with multiplication using translated concatenation. Its kernel is the loop group \(\pi_1(SA,I)=K_2(A)\); thus \(1\to K_2(A)\to\operatorname{St}(A)\to E(A)\to1\) is exact.",
 r"The group law on paths is not bare concatenation of paths with unrelated endpoints; translation makes the endpoints composable. The zeroes in the group exact sequence are conventional shorthand and are rewritten as ones.",
 r"\citet[Theorem~15.2 and Corollary~15.2]{vaserstein1976foundations} proves the exact path/Steinberg identification and attributes the theorem to Volodin. The underlying simplicial theory had circulated by the July 1970 submission of \citet{volodin1971extraordinary}, published in 1971, so the identification is expository here.",
 "the standard positive-degree low-dimensional identification; no new universal-relation problem is posed on these pages.",["vaserstein1976foundations","volodin1971extraordinary"])

item(280,"P000470","theorem","Universal central extension and the second homology of E A",
 r"The notes write \(K_2A=H_2EA\) and describe \(\operatorname{St}A\) as the universal central extension of \(EA\).",
 r"For an associative unital ring \(A\), the stable Steinberg group \(\operatorname{St}(A)\to E(A)\) is the universal central extension of the perfect elementary group. Therefore \(K_2(A)\cong H_2(E(A);\mathbb Z)\). Stability and the unit convention are part of the assertion; arbitrary small finite matrix ranks require separate results.",
 r"The integral trivial coefficients in group homology are supplied. The active unital hypothesis from P000469 is retained, and the immediately preceding idempotent-ring alternative is not automatically propagated to this stronger claim.",
 r"The classical Kervaire--Steinberg theorem is stated and proved in \citet[III, Theorem~5.5]{weibel2013kbook}; its preceding discussion points to \citet[\S5]{milnor1972introduction}, published before this talk. The latter's publication was checked from the publisher, while the mathematical theorem was read in Weibel.",
 "established stable unital theorem, with scope distinct from finite-rank or unrestricted nonunital variants.",["weibel2013kbook","milnor1972introduction"],
 literal="correct with missing hypotheses")

item(280,"P000470","problem","Pairwise simplices need not form a simplex: the tolerance assertion",
 r"The explicit \ru{Задача} asks whether three vertices with all three edges present form a simplex, and generalizes this to every finite pairwise adjacent set, calling it a tolerance-space property.",
 r"For the complex defined in 1972-280.7, the proposed assertion is: every finite \(X\subset\mathrm{GL}(A)\) whose two-element subsets are simplices is itself a simplex. It is false for every nonzero unital ring. The vertices \(I+E_{12},I+E_{23},I+E_{31}\) are pairwise adjacent but do not lie in any common coset of a permutation-unitriangular subgroup, even after stabilization.",
 r"The question is interpreted with the single common translation and order of P000468, not as a flag completion imposed by definition. The complete counterexample, the acyclic-support criterion, and minimal-rank check are proved in the corrective appendix and marked \ours; finite computations are marked \oursComputed. No novelty or priority claim is made for the counterexample.",
 VDATE + r" Crucially, \citet[\S11, Remark~(c), p.~111]{vaserstein1976foundations} asserts exactly this property after defining the complex and identifying left/right conventions in Remark~(b). Thus A records exact publication of the assertion, not its validity. It is not an orphan D item. The same remark says the assertion is not used in that paper, so this correction alone does not refute the paper's K-theory comparisons.",
 "refuted in the literal model by the fully checked three-vertex example; the published claim is corrected, and no open problem is manufactured from it.",VREF,
 cls="A",literal="false as written",match="exact",development="developed in this chapter",problem="GP-1972-101")

problems.append(dict(id="GP-1972-101",title="Does pairwise adjacency imply a simplex in the permutation-triangular K-theory complex?",
 statement=r"For a nonzero unital ring \(A\), let the vertices be stable invertible matrices, and let a finite set be a simplex when it lies in one left coset of a subgroup of matrices unitriangular for one permutation of the coordinate order. Must every finite pairwise adjacent set be a simplex? The notebook first asks the three-vertex case and then the finite version.",
 occurrences=["1972-280.20"],status=r"As of 9 November 2026, the literal assertion is false. It was explicitly asserted in \citet[\S11, Remark~(c)]{vaserstein1976foundations}, not left undisclosed. The appendix gives a complete proof for the triple \(I+E_{12},I+E_{23},I+E_{31}\) over every nonzero unital ring, checks invariance under stabilization and coset conventions, and includes independent exact computation. This is a correction of a published claim, with no assertion of priority for the counterexample.",
 status_date="2026-11",refs=["vaserstein1976foundations"]))

corr("P000468","map into ordinary units",r"\(A\to1+A\) is a homomorphism into invertible elements",r"The monoid map is defined on \(A\); restrict its domain to \(GA\) to obtain a homomorphism into units.","P000468 scan and the preceding definition of quasiunits; Vaserstein 1976, section 2.")
corr("P000468","triangular convention",r"upper triangular; \(a_{ij}=0\) for \(i\leq j\)",r"Either strict lower triangular with the written inequality, or strict upper triangular with \(i\geq j\).","Both the word and inequality are clearly present in the scan; transposition leaves the permutation-triangular construction unchanged.",typ="ambiguity")
corr("P000468","arbitrary reindexing",r"any map \(\mathbb N\to\mathbb N\) induces an endomorphism","an injective map induces the stated matrix-ring embedding","Original scan says any map; collapsing two diagonal matrix units contradicts multiplicativity. Vaserstein 1976 section 4 correctly requires embeddings.")
corr("P000468","inner permutation automorphism","inner automorphism",r"implemented by a permutation multiplier (or by a unit of the row-and-column-finite ring for unital \(A\)), not necessarily by a finitary stable unit","Infinite permutations need not be finitary. The scan does not specify the ambient ring.",typ="ambiguity")
corr("P000469","elementary homotopy source and target",r"\(s_1,s_2:S'\to S'\) with \(X\subset S\)",r"\(s_1,s_2:S\to S'\), and \(s_1(X)\cup s_2(X)\) a simplex in \(S'\) for every source simplex \(X\)",r"The source prime is a short doubtful stroke in the scan; the following unprimed \(X\subset S\) and primed target fix the intended roles.",typ="ambiguity")
corr("P000470",r"range of block-sum \(K\) indices",r"all \(K_i\), \(i\geq0\)",r"all \(K_i\), \(i\geq1\), for the displayed homotopy definition; \(K_0\) requires its separate definition",r"P000469 explicitly defines only \(K_n=\pi_{n-1}(SA)\) for \(n\geq1\); no \(K_0\) construction is given here.",typ="ambiguity")
corr("P000470","omitted Steinberg commuting restrictions","some commutators are zero",r"\([x_{ij}(a),x_{kl}(b)]=1\) for \(i\ne l\) and \(j\ne k\); adjacent-root relation requires distinct \(i,j,k\)","The scan abbreviates the restrictions; Vaserstein 1976 section 6 and Weibel III.5.1 give the exact relations.",typ="ambiguity")
corr("P000470","tolerance task","if every pair is a simplex, the whole finite set is a simplex",r"False for the defined complex: \(I+E_{12},I+E_{23},I+E_{31}\) are pairwise adjacent but not a simplex.","P000468 fixes a common translation and coordinate order; complete proof and two independent exact audits. The same false assertion appears in Vaserstein 1976 section 11 Remark(c), p.111.")
corr("P000470","end of record280/start of record281","catalogue ranges overlap","Vasserstein ends after the tolerance problem; Kazhdan begins at the underlined derived-category heading lower on the same page.","Original P000470 scan and P000471 continuation.",typ="provenance")
save()

DREF=["hartshorne1966residues","stacks2026foundations"]
DFATE=r"The notes explicitly refer to \citet[Chapter~I, pp.~19--84]{hartshorne1966residues}, published in 1966 from the Harvard seminar of 1963--1964. The publisher record and contents were checked; the exact modern statements and proofs were read separately in \citet[Tags 05R1 and 05RR]{stacks2026foundations}. This is exposition of an established construction, not a 1972 announcement."

talk(281,"1972-11-13","D. A. Kazhdan","P000470-P000471",
 "Derived categories by localization of the homotopy category",
 r"Kazhdan defines the homotopy category of complexes, quasi-isomorphisms, the equivalent pre- and post-composition cancellation criteria, and localization to form the derived category. Hartshorne's \emph{Residues and Duality} is explicitly cited. The talk begins below Vasserstein's tolerance problem on P000470 and ends before Buchstaber's heading on P000471; the intervening material is a short foundational exposition rather than an unresolved localization proposal.")

item(281,"P000470","definition","Homotopy category of complexes in an abelian category",
 r"For an abelian category \(C\), the notes introduce \(K_C\) as the category of complexes and then explicitly specify homotopy classes of complex morphisms as its arrows.",
 r"Let \(C\) be an abelian category, with an appropriate smallness convention. The category \(K(C)\) has cochain complexes as objects and chain maps modulo chain homotopy as morphisms. Composition is induced by composition of chain maps. Homology or cohomology is well defined on these morphism classes.",
 r"The full sentence defines the homotopy category, not the unquotiented category of complexes. Cochain indexing is chosen for clarity; the notebook's upward arrows can equally be reindexed homologically.",
 DFATE + r" See also the opening paragraph of Stacks Tag 05RR.",
 "standard homotopy-category definition; no ambiguity remains after reading the morphism line.",DREF)

item(281,"P000470","definition","Quasi-isomorphisms as the class to be inverted",
 r"The class \(S\subset\operatorname{Hom}K_C\) consists of morphisms inducing isomorphisms on homology.",
 r"A morphism in \(K(C)\) is a quasi-isomorphism if its maps \(H^n\) are isomorphisms for every integer \(n\). This condition is invariant under chain homotopy; equivalently the cone of a representing chain map is acyclic. These morphisms form the saturated multiplicative system used in the derived category.",
 r"The all-degrees quantifier and cone characterization unpack the abbreviated homology condition. Saturation is a standard structural theorem used for the subsequent localization, not an extra claim that the notes explicitly proved.",
 DFATE + r" The exact multiplicative-system statement is Stacks Lemma~13.11.2, Tag 05RR.",
 "standard quasi-isomorphisms and their localization class.",DREF)

item(281,"P000471","theorem","Equivalent left and right cancellation by quasi-isomorphisms",
 r"For \(f,g:K\to K'\), the page asserts equivalence between \(fs_1=gs_1\) for a quasi-isomorphism \(s_1:K_1\to K\) and \(s_2f=s_2g\) for a quasi-isomorphism \(s_2:K'\to K_2\).",
 r"In the homotopy category of complexes of an abelian category, the following are equivalent for parallel arrows \(f,g:X\to Y\): there exists a quasi-isomorphism \(s:Z\to X\) with \(fs=gs\); there exists a quasi-isomorphism \(t:Y\to W\) with \(tf=tg\); and the images of \(f,g\) in \(D(C)\) agree. All displayed equalities before localization are in \(K(C)\), hence mean chain homotopy for representing maps.",
 r"The target arrow's direction is fixed by the scanned diagram. Requiring literal equality of representing chain maps would change the statement; the preceding definition of \(K_C\) is therefore decisive. The equality-in-localization characterization is its standard consequence.",
 DFATE + r" Stacks Lemma~13.5.5, Tag 05R1, proves both cancellation directions by an acyclic mapping cone and the dual argument.",
 "a proved calculus-of-fractions lemma; no extra injective or projective resolution hypothesis is needed.",DREF)

item(281,"P000471","construction","Derived localization and composition of fractions",
 r"The notes write \(L_C=S^{-1}K_C\), say that the arrows of \(S\) become invertible, and invoke the preceding lemma in defining composition; the reading reference is Hartshorne.",
 r"For a small abelian category \(C\), or another setting in which the relevant localization has set-valued Hom classes, define \(D(C)=S^{-1}K(C)\). It is characterized by the universal property that functors from \(K(C)\) inverting all quasi-isomorphisms factor through it. Morphisms may be represented by roofs \(X\xleftarrow{s}Z\xrightarrow{f}Y\), with \(s\in S\); the left/right Ore and cancellation conditions define composition and equality of roofs.",
 r"The single displayed cancellation lemma is part of a full calculus of fractions; it alone does not prove every localization axiom. The set-theoretic qualification avoids asserting that every large abelian category has a locally small unbounded derived category. Neither boundedness nor enough injectives is imposed by these particular notes.",
 DFATE + r" Stacks Definition~13.11.3 gives the localization, and Remark~13.11.4 states the smallness issue explicitly.",
 "the standard derived category in the stated size setting, with the notebook's shorthand expanded.",DREF,
 literal="correct with missing hypotheses")

corr("P000470-P000471","category of complexes terminology",r"\(K_C\) called category of complexes",r"\(K_C\) is the homotopy category: its morphisms are chain-homotopy classes, as the next line explicitly says.","P000470 scan; this is a reading clarification, not a contradictory transcription.",typ="ambiguity")
corr("P000471","end of record281","catalogue range continues through P000472","Kazhdan's derived-category exposition ends before the Buchstaber heading on P000471.","Original P000471 scan and the explicit change of speaker.",typ="provenance")
save()
