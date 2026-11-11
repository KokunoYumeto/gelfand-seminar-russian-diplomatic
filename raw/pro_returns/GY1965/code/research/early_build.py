"""Reproducible editorial data for records 53--68. Not a mathematical test suite."""
from pathlib import Path
import json
import csv
from collections import Counter

OUT = Path(__file__).parent
talks, items, problems, corrections = [], [], [], []
AB = "atiyahbott1964notes"
FAC = "serre1955coherent"
RR = "borelserre1958riemannroch"
KOHN = "kohn1963potential"
TA = "grothendieck1957homological"

def checkpoint():
    for name, data in [("talks", talks), ("items", items), ("problems", problems)]:
        (OUT / f"early_{name}.json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    with (OUT / "early_corrections.csv").open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["page","place","transcription_reads","should_read","evidence","applies_to"])
        w.writeheader()
        w.writerows(corrections)

def T(record, date, speaker, pages, title, summary, kind="talk"):
    talks.append(dict(record=record, date=date, speaker=speaker, pages=pages, title=title,
                      kind=kind, summary=summary, source_order=len(talks)+1))
    checkpoint()

def I(record, pages, kind, title, notes, statement, reconstruction="", cls="E",
      fate="", status="", correctness="correct with missing hypotheses",
      match="exact", verification="read the result", development="annotated",
      problem="", worth="", refs=None, confidence="high", area=""):
    refs = refs or []
    if not fate:
        fate = (r"Already part of the expository framework in \citet{" + refs[0] + "}."
                if refs else "No independent publication identification is claimed.")
    if not status:
        status = ("As of 9 November 2026, the precise statement is a standard established result or definition."
                  if cls == "E" else
                  "As of 9 November 2026, the surviving entry does not determine a unique mathematical assertion.")
    n = 1 + sum(x["record"] == record for x in items)
    items.append(dict(id=f"1965-{record}.{n}", record=record, pages=pages, kind=kind,
                      title=title, notes=notes, statement=statement,
                      reconstruction=reconstruction, **{"class":cls}, fate=fate,
                      present_status=status, literal_correctness=correctness,
                      publication_match=match, verification=verification,
                      development=development, problem=problem, worth=worth,
                      refs=refs, confidence=confidence, area=area))
    checkpoint()
    return items[-1]["id"]

def C(page, place, old, new, evidence, applies="both"):
    corrections.append(dict(page=page, place=place, transcription_reads=old,
                            should_read=new, evidence=evidence, applies_to=applies))
    checkpoint()

T(53,"1965-09-20","J. J. Kohn","P000090-P000091",
  "The d-bar Neumann problem and the Levi problem",
  r"Kohn discusses solving \(\bar\partial u=\alpha\), the Levi form, and the passage from a local supporting holomorphic polynomial to a global nonextendible holomorphic function. The second page introduces the Dolbeault complex, the Neumann quadratic form, a boundary estimate, and the Kohn--Rossi extension paper. These are accounts of work already available before this talk, not announcements inferred solely from later publication dates \citep{kohn1963potential,kohn1963harmonic,kohn1964harmonic,kohnrossi1965extension}. The dated heading begins on P000090; P000088--P000089 belong to the preceding invariant-subspace discussion. A short reading programme at the end names algebraic groups and algebraic geometry.")

I(53,"P000090","question","Compatibility and global solvability of the d-bar equation",
  r"Given the coefficients \(\alpha_j\), the notes ask when \(u_{\bar z_j}=\alpha_j\) is soluble and how \(u\) depends on them; they write the cross-derivative compatibility conditions.",
  r"Let \(\Omega\Subset\mathbb C^n\) have \(C^\infty\) strongly pseudoconvex boundary and let \(\alpha=\sum_j\alpha_j\,d\bar z_j\in C^\infty(\overline\Omega;\Lambda^{0,1})\). If \(\partial\alpha_j/\partial\bar z_k=\partial\alpha_k/\partial\bar z_j\), there is \(u\in C^\infty(\overline\Omega)\) with \(\bar\partial u=\alpha\); the canonical solution is \(u=\bar\partial^*N_1\alpha\). Without a global condition on \(\Omega\), compatibility alone need not give global solvability.",
  r"The global strong pseudoconvexity and smoothness assumptions are supplied from the ensuing argument. The notes begin with only a bounded domain; they do not state a general necessary-and-sufficient theorem for arbitrary domains.",
  refs=[KOHN,"kohn1963harmonic","kohn1964harmonic"], match="partial",
  problem="GP-1965-E01", area="Several complex variables")
I(53,"P000090","definition","The complex tangent space and Levi form",
  r"A defining function \(r\) is negative inside \(M\); the complex tangent vectors satisfy \(\sum r_{z_j}a^j=0\), and the displayed Hermitian form is \(\sum r_{z_i\bar z_j}a^i\bar a^j\).",
  r"For a \(C^2\) real defining function with \(dr\ne0\) on \(\partial\Omega\), the complex tangent space at \(p\) is \(\ker\partial r(p)\). Its Levi form is \(\mathcal L_r(p;a)=\sum_{j,k}r_{z_j\bar z_k}(p)a_j\bar a_k\); strong pseudoconvexity means positivity for every nonzero complex tangent vector. Multiplying \(r\) by a positive smooth factor multiplies this restricted form by that factor.",
  r"The sign convention depends on \(\Omega=\{r<0\}\); positivity on the full ambient complex tangent space is not required.",
  refs=[KOHN], correctness="correct", area="Several complex variables")
I(53,"P000090","construction","A local holomorphic support function",
  r"Positivity of the Levi form is used to construct a holomorphic polynomial \(W\) whose zero set touches the boundary at \(p\) and otherwise lies outside the domain near \(p\).",
  r"At a strongly pseudoconvex point \(p\) of a \(C^2\) boundary, a holomorphic polynomial \(W\) of degree at most two can be chosen with \(W(p)=0\), \(dW(p)\ne0\), and \(W(z)\ne0\) on \((\overline\Omega\cap U)\setminus\{p\}\), after shrinking \(U\). One obtains \(W\) from the holomorphic part of the second-order Taylor expansion of a suitably modified defining function.",
  r"A quadratic change in the defining function can make the real estimate strict in all relevant directions. The conclusion is local; the sketch does not prove global pseudoconvexity.",
  refs=[KOHN], area="Several complex variables")
I(53,"P000090","method","Globalizing the local pole",
  r"With a cut-off \(g=1\) near \(p\), the notes solve \(\bar\partial u=\bar\partial(g/W)\) and form \(h=u-g/W\). The final sentence attributes noncontinuation to \(u\).",
  r"Under the preceding smooth strongly pseudoconvex domain assumptions, choose \(g\) supported in the support-function neighbourhood. The form \(\alpha=\bar\partial(g/W)\), extended by zero, is smooth on \(\overline\Omega\) and \(\bar\partial\)-closed. A smooth solution \(u\) gives a holomorphic \(h=u-g/W\) on \(\Omega\) with a singularity at \(p\), so \(h\) does not extend holomorphically across \(p\).",
  r"It is \(h\), not the globally smooth correction \(u\), whose boundary singularity is forced. Smoothness of \(\alpha\) follows because \(\bar\partial g=0\) near the only local zero of \(W\).",
  refs=[KOHN], correctness="false as written", problem="GP-1965-E01",
  area="Several complex variables")
I(53,"P000091","construction","The Dolbeault complex",
  r"The spaces \(a^{p,q}\) of forms and the arrows \(a^{p,q-1}\to a^{p,q}\to a^{p,q+1}\) are written with differential \(\bar\partial\).",
  r"On a complex manifold, \(C^\infty\) differential forms split by bidegree and \(\bar\partial:A^{p,q}\to A^{p,q+1}\) satisfies \(\bar\partial^2=0\). On a domain with boundary the maximal \(L^2\) realizations form a Hilbert complex; domains must be imposed before defining Hilbert adjoints.",
  r"The notes alternate \(a\) and \(\alpha\) as space letters. The Hilbert completion and operator domains are made explicit here.",
  refs=[KOHN], correctness="correct", area="Several complex variables")
I(53,"P000091","method","The Neumann quadratic form and canonical solution",
  r"The quadratic form is \(Q(\varphi,\psi)=(\bar\partial\varphi,\bar\partial\psi)+(\bar\partial^*\varphi,\bar\partial^*\psi)\); a positive higher-order equation is proposed to solve the first-order compatible system.",
  r"On \(L^2\) forms, put \(\mathcal D(Q)=\mathcal D(\bar\partial)\cap\mathcal D(\bar\partial^*)\). The closed nonnegative form defines the self-adjoint \(\bar\partial\)-Neumann Laplacian \(\Box=\bar\partial\bar\partial^*+\bar\partial^*\bar\partial\). If its inverse \(N_q\) exists on the orthogonal complement of its harmonic kernel, a closed \((p,q)\)-form orthogonal to that kernel is solved by \(\bar\partial^*N_q\alpha\).",
  r"The first-order equation follows using the complex identity and commutation with \(N\), not merely by solving an arbitrary positive second-order equation. The displayed domain in the notebook must also include \(\mathcal D(\bar\partial)\).",
  refs=[KOHN,"kohn1963harmonic"], area="Several complex variables")
I(53,"P000091","claim","The boundary estimate and its limitations",
  r"The estimate \(\int_{\partial M}|\varphi|^2\,dS\le C Q(\varphi,\varphi)\) is displayed, followed by the warning that it does not control the sum of squares of all first derivatives.",
  r"For a bounded smooth strongly pseudoconvex domain in \(\mathbb C^n\), \(q\ge1\), and smooth \((p,q)\)-forms satisfying the \(\bar\partial^*\) boundary condition, the boundary \(L^2\) norm is bounded by \(C Q\). More generally on a strongly pseudoconvex manifold an added \(L^2\) term or projection away from harmonic forms is needed. For \(0<q<n\), this is not a full \(H^1\) coercive estimate; at top antiholomorphic degree the boundary condition is of Dirichlet type.",
  r"The degree and geometric hypotheses are indispensable: at \(q=0\), nonzero holomorphic functions can have \(Q=0\) and a nonzero boundary norm. The notebook's one-dimensional comparison refers to the top-degree situation.",
  refs=[KOHN], area="Several complex variables")
I(53,"P000091","remark","A reference to general overdetermined systems",
  r"The notes refer to work of Spencer on general overdetermined systems but give no operator class or statement.",
  r"No unique theorem about general overdetermined systems can be extracted. The identifiable idea is to exploit a differential complex and its compatibility operator when reducing a first-order system to a second-order variational problem.",
  r"This is a programme-level reference, not a statement that every overdetermined system is solved by the Neumann construction.",
  cls="F", correctness="not determinable", match="thematic only", verification="unresolved lead",
  fate=r"\citet{kohn1963potential} discusses the related complex Neumann work and cites Kohn--Spencer, but this does not identify which general Spencer result the speaker meant.",
  status="As of 9 November 2026, the cited survey and its references establish the context; the notebook reference remains underdetermined.",
  refs=[KOHN], confidence="low", area="Partial differential equations")
I(53,"P000091","remark","The Kohn-Rossi extension reference",
  r"The notes name Kohn and Rossi, Annals of Mathematics 1965, and emphasize holomorphic continuation of forms into the domain.",
  r"A precise special case is: if \(\Omega\Subset\mathbb C^n\), \(n\ge2\), has connected smooth strongly pseudoconvex boundary, every smooth CR function on \(\partial\Omega\) is the boundary value of a holomorphic function smooth on \(\overline\Omega\). Extension for higher-degree forms requires the appropriate tangential compatibility and cohomological conditions.",
  r"The function statement is a safe modern specialization, not a transcription of the unspecified assertion about all forms. No unrestricted forms-extension theorem is attributed to this one-line entry.",
  fate=r"The named article is \citet{kohnrossi1965extension}; its bibliographic identity is confirmed in Kohn's author bibliography. The original theorem text was not obtained in this search.",
  status="As of 9 November 2026, the function-extension theorem is established; the exact higher-form assertion intended here remains unspecified.",
  refs=["kohnrossi1965extension",KOHN], match="partial", verification="indirect",
  confidence="medium", area="Several complex variables")
C("P000090","display following the compatibility equations",
  r"\(\sum u_{z_j}\,d\bar z_j\)",
  r"\(\bar\partial u=\sum u_{\bar z_j}\,d\bar z_j\)",
  "The scan itself omits the bar in this display, although the preceding derivative definition has it. This is a mathematical emendation of a notebook slip, not a demonstrated OCR error.")
C("P000090","last sentence of the cut-off argument",
  "u does not continue holomorphically",
  "h does not continue holomorphically across the chosen boundary point",
  "The scan reads u, while the immediately preceding construction defines h=u-g/W. The singularity is in h; preserve u diplomatically and annotate the mathematical correction.")

T(54,"1965-09-27","R. Finn","P000091-P000092",
  "Total curvature of complete open surfaces",
  r"The brief entry recalls Gauss--Bonnet and Cohn--Vossen, illustrates the difference between closed and complete surfaces, and states the aim of replacing an inequality by an equality. Its final sentence is at the top of P000092, before Gelfand's new heading. Finn's 1965 article is a plausible publication context, but the surviving entry contains no end-defect formula with which to establish an exact theorem match \citep{cohnvossen1935curvature,finn1965conformal}.")
I(54,"P000091","remark","Complete surfaces need not satisfy the closed Gauss-Bonnet equality",
  r"A paraboloid is given as a complete, nonclosed surface with \(C=2\pi\) and \(\chi=1\); a second schematic surface is marked with a strict inequality.",
  r"The graph \(z=x^2+y^2\), with its induced metric, is complete, is homeomorphic to \(\mathbb R^2\), and has total Gaussian curvature \(2\pi\). Completeness alone does not force equality: the Euclidean plane has \(\chi=1\) and total curvature zero.",
  r"The plane is a simple explicit replacement for the unnamed strict-inequality sketch, not an identification of that drawing. For the paraboloid, \(K=4/(1+4r^2)^2\), \(dA=r\sqrt{1+4r^2}\,dr\,d\theta\), whose integral is \(2\pi\).",
  refs=["cohnvossen1935curvature"], match="partial", correctness="correct",
  area="Differential geometry")
I(54,"P000091","theorem","Cohn-Vossen's inequality",
  r"The statement is abbreviated to \(C\le2\pi\chi\) for every complete surface.",
  r"If a connected complete boundaryless Riemannian surface has finite topological type and integrable Gaussian curvature, then \(\int_M K\,dA\le2\pi\chi(M)\). The original formulation permits the corresponding well-defined total-curvature limit; absolute integrability is a convenient sufficient hypothesis here.",
  r"Finite topological type and existence of total curvature are supplied. Without a meaningful integral and Euler characteristic the unqualified expression is not a theorem.",
  fate=r"This is the pre-existing result in \citet[Theorem 6]{cohnvossen1935curvature}.",
  refs=["cohnvossen1935curvature"], area="Differential geometry")
I(54,"P000092","question","Finn's proposed equality with a defect term",
  r"The sole statement about Finn's own aim is to replace the inequality by an equality.",
  r"The entry does not specify the class of metrics, the ends, or a proposed defect invariant. Consequently no unique equality theorem can be reconstructed from it.",
  r"An identity obtained simply by defining a defect as \(2\pi\chi-\int K\,dA\) would be tautological; assigning Finn a particular geometric formula requires information absent here.",
  cls="F", correctness="not determinable", match="partial", verification="publisher metadata checked",
  fate=r"The title and date of \citet{finn1965conformal} fit the discussion, but the accessible publisher record establishes metadata, not the equality intended in this notebook.",
  status="As of 9 November 2026, the search identifies a likely contemporaneous publication context, not an unambiguously formulated unresolved problem.",
  refs=["finn1965conformal"], confidence="low", area="Differential geometry")

T(55,"1965-09-27","I. M. Gelfand","P000092-P000093",
  "Atiyah-Bott: differential operators and elliptic complexes",
  r"Gelfand begins an exposition attributed to Atiyah, introducing symbols, elliptic complexes, and the de Rham and Dolbeault examples. The speaker is Gelfand, not Atiyah. The reference underlying the sequence is the Harvard lecture material dated autumn 1964, preceding these meetings; its Russian translation appeared in 1966, and the journal article followed in 1967 \citep{atiyahbott1964notes,atiyahbott1967lefschetz}. The initial list of applications includes Brouwer, Lefschetz, eigenvectors, and Weyl characters. The symbol and finiteness discussions continue the topics indexed as 1964-28.2, 1964-28.4, and 1964-28.5; the underqualified earlier finiteness assertion 1964-28.3 should not be treated as a stronger theorem.")
I(55,"P000092","remark","Brouwer's theorem among the fixed-point applications",
  r"Brouwer's theorem is listed among the results contained in the proposed fixed-point theory.",
  r"Every continuous map from a closed finite-dimensional real ball to itself has a fixed point. Its relation to Lefschetz theory uses homotopy invariance and a suitable compact-space formulation; the smooth transverse elliptic-complex formula itself is not directly a theorem about arbitrary maps of a ball.",
  r"The ball, continuity, and finite-dimensionality are supplied. The entry gives only the name and does not record the reduction.",
  refs=[AB], match="thematic only", confidence="medium", area="Topology")
I(55,"P000092","remark","Lefschetz's fixed-point theorem in the applications list",
  r"The ordinary Lefschetz formula is named before elliptic complexes are defined.",
  r"For a self-map \(f\) of a finite polyhedron, a nonzero Lefschetz number \(\sum_q(-1)^q\operatorname{tr}(f^*:H^q(X;\mathbb Q)\to H^q(X;\mathbb Q))\) forces a fixed point. For a smooth map of a closed manifold with nondegenerate fixed points, this number is \(\sum_p\operatorname{sgn}\det(I-df_p)\).",
  r"These are precise familiar versions of the name in the notes; their derivation is discussed in record 65.",
  refs=[AB], match="partial", area="Topology")
I(55,"P000092","remark","The eigenvector application",
  r"The notes say that a linear space has an eigenvector.",
  r"Every endomorphism of a nonzero finite-dimensional complex vector space has an eigenvector. If it is invertible, its induced projective transformation has a fixed point, which is exactly an invariant line.",
  r"The endomorphism and the finite-dimensional complex setting must be supplied. The literal wording is not a statement about every real operator or every infinite-dimensional operator.",
  refs=[AB], match="thematic only", confidence="medium", area="Linear algebra")
I(55,"P000092","remark","Weyl's character formula in the applications list",
  r"Weyl's theorem on traces of representations is named without a group, weights, or formula.",
  r"For a compact connected simply connected semisimple group, choose positive roots, let \(W\) be its Weyl group, and let \(\rho\) be half the sum of positive roots. The irreducible representation of dominant integral highest weight \(\lambda\) has character \(\chi_\lambda(t)=\frac{\sum_{w\in W}\epsilon(w)e^{w(\lambda+\rho)}(t)}{\sum_{w\in W}\epsilon(w)e^{w\rho}(t)}\) on regular elements of a maximal torus, where \(\epsilon(w)=\det w\). Extension across the apparent singular set is by continuity.",
  r"This supplies the standard meaning of the named formula. The relevant flag manifold, bundle, and fixed-point derivation are not present in this entry.",
  refs=[AB], match="thematic only", confidence="medium", area="Representation theory")
I(55,"P000092","definition","Differential complexes of vector bundles",
  r"Bundles \(E_1,\ldots,E_n\), spaces of sections, and a sequence of differential maps satisfying \(d^2=0\) are introduced.",
  r"A differential complex on a smooth manifold is a finite sequence of smooth finite-rank vector bundles and differential operators \(d_i:\Gamma(E_i)\to\Gamma(E_{i+1})\) such that \(d_{i+1}d_i=0\). Its \(i\)-th cohomology is \(\ker d_i/\operatorname{im}d_{i-1}\).",
  r"The trivial line-bundle example identifies sections with smooth scalar functions. Compactness is unnecessary for the definition.",
  refs=[AB], correctness="correct", area="Elliptic complexes")
I(55,"P000092","definition","Coordinate-free principal symbols",
  r"The operator acts on \(f^m s\), where \(f(x)=0\), and its value at \(x\) is used to define the symbol in terms of \(df_x\) and \(s(x)\).",
  r"For an order-\(m\) differential operator \(P\), \(P(f^ms)(x)=m!\,\sigma_{\mathrm{alg}}(P)(x,df_x)s(x)\), where \(\sigma_{\mathrm{alg}}(P)(x,\xi)=\sum_{|\alpha|=m}a_\alpha(x)\xi^\alpha\) uses ordinary derivatives. Equivalently the notebook's symbol is \(m!\sigma_{\mathrm{alg}}\). The convention with \(D_j=(1/i)\partial_{x_j}\) introduces the corresponding powers of \(i\).",
  r"The formula is stated for an already local differential operator. It is not silently promoted to a characterization of arbitrary linear maps on sections; the notebook compresses the locality and order discussion.",
  refs=[AB], match="partial", area="Elliptic complexes")
I(55,"P000092","claim","The factor two in the Laplace symbol",
  r"For the Laplacian, the notes obtain \(2(\eta_1^2+\cdots+\eta_n^2)\).",
  r"If \(\Delta=\sum_j\partial_{x_j}^2\) and \(f(x)=0\), then \(\Delta(f^2s)(x)=2|df_x|^2s(x)\). Thus the factor two is correct for the preceding unnormalized symbol definition.",
  r"The evaluation at \(x\), where \(f(x)=0\), is essential. This is neither the globally valid product rule nor the symbol convention of the positive Laplacian \(-\sum\partial_j^2\).",
  refs=[AB], correctness="correct with missing hypotheses", match="partial", area="Elliptic complexes")
I(55,"P000092","definition","Ellipticity of a complex",
  r"The sequence of fibre maps given by the symbols is required to be exact for every \(\eta\ne0\).",
  r"A differential complex is elliptic if for each nonzero real cotangent vector \(\xi\in T_x^*X\), the symbol sequence \(0\to E_{0,x}\to\cdots\to E_{N,x}\to0\) is exact. Each map uses its own operator order; rescaling an individual symbol by a nonzero conventional constant leaves exactness unchanged.",
  r"Nonzero real cotangent vectors are meant, even for complex vector bundles. Finite-dimensional cohomology additionally requires global hypotheses supplied later.",
  refs=[AB], correctness="correct", area="Elliptic complexes")
I(55,"P000093","construction","The Laplace operator as a two-term elliptic complex",
  r"The first example is the trivial line bundle and the Laplace operator between its spaces of sections.",
  r"On a Riemannian manifold, the Laplace operator on functions has invertible scalar principal symbol at each nonzero real covector; hence \(0\to\Gamma(1)\xrightarrow{\Delta}\Gamma(1)\to0\) is an elliptic complex.",
  r"No compactness or boundary condition is required for symbol ellipticity. Fredholm or cohomological finiteness conclusions do not follow for an arbitrary open domain.",
  refs=[AB], correctness="correct", area="Elliptic complexes")
I(55,"P000093","construction","The de Rham symbol is an exact Koszul complex",
  r"The notes identify the symbols of \(d\) with exterior multiplication by \(\eta\) and state that \(e\wedge\eta=0\) implies \(e=a\wedge\eta\).",
  r"The de Rham differential has symbol \(\xi\wedge-\), up to the chosen factor and graded sign. For \(\xi\ne0\), choose \(v\) with \(\xi(v)=1\). Then \(\iota_v(\xi\wedge-)+\xi\wedge\iota_v=\operatorname{id}\), so the exterior-algebra symbol complex is exact in every degree.",
  r"The contraction identity supplies the brief algebraic justification. The notebook's product-rule display misses a sign for odd-degree \(s\): at \(f(x)=0\), \(d(fs)(x)=df_x\wedge s(x)=(-1)^q s(x)\wedge df_x\) for a \(q\)-form. These degree-dependent signs do not affect symbol exactness.",
  refs=[AB], correctness="false as written", area="Elliptic complexes")
I(55,"P000093","construction","The Dolbeault elliptic complex",
  r"A third example is written simply as \(\bar\partial\), and so on.",
  r"For fixed \(p\) on a complex manifold, \((A^{p,\bullet},\bar\partial)\) is elliptic: at a nonzero real covector \(\xi\), the symbol is exterior multiplication by its nonzero \((0,1)\) part. The same contraction argument proves exactness.",
  r"The use of real covectors matters; a nonzero complexified covector may have zero \((0,1)\) part.",
  refs=[AB], correctness="correct", area="Elliptic complexes")
C("P000093","de Rham product-rule display",
  r"\(d(s f)(x_0)=s(x_0)\wedge df_{x_0}\) in positive form degree",
  r"for a \(q\)-form \(s\), \(d(fs)(x_0)=df_{x_0}\wedge s(x_0)=(-1)^q s(x_0)\wedge df_{x_0}\) when \(f(x_0)=0\)",
  "The scan genuinely puts the old form before df with no degree sign. The standard graded product rule supplies the sign. Symbol exactness is unchanged, so this is a convention-sensitive notebook correction, not a change in the ellipticity conclusion.")

T(56,"1965-10-04","I. M. Gelfand","P000093-P000095",
  "Atiyah-Bott: Lefschetz numbers, local terms, and Hodge theory",
  r"The exposition resumes below the dated continuation heading on P000093. Gelfand defines endomorphisms of complexes and their Lefschetz numbers, describes a map with bundle lifts and simple fixed points, states the elliptic fixed-point formula, and starts its spectral proof. The main formulas require a consistent pullback convention, compactness, and the distinction between nonnegative spectrum and strictly positive eigenspaces \citep{atiyahbott1964notes}.")
I(56,"P000093","definition","The symbol formula recalled",
  r"The continuation begins by repeating \(d(f^m s)(x_0)=\sigma(d,\eta)s(x_0)\), with \(\eta=df_{x_0}\).",
  r"For an order-\(m\) differential operator, with \(f(x_0)=0\), the value of \(d(f^m s)\) at \(x_0\) is \(m!\) times the algebraically normalized principal symbol at \(df_{x_0}\), acting on \(s(x_0)\).",
  r"This is a repeat occurrence of the unnormalized symbol convention. The same pointwise-vanishing assumption and factorial convention as record 55 are retained.",
  refs=[AB], correctness="correct with missing hypotheses", area="Elliptic complexes")
I(56,"P000093","remark","Elliptic operators beyond differential operators",
  r"A brief line notes that elliptic operators need not be differential operators.",
  r"Ellipticity also makes sense for classical pseudodifferential operators: an order-\(m\) operator is elliptic when its homogeneous principal symbol is invertible away from the zero section. For example the identity plus a nonzero smoothing integral operator is elliptic of order zero and need not be a differential operator.",
  r"The example specifies one standard extension of the term. The notebook does not yet define the broader class; its oscillatory definition appears in record 61.",
  refs=[AB,"kohnnirenberg1965algebra"], match="partial", area="Pseudodifferential operators")
I(56,"P000093","definition","Complex endomorphisms and induced cohomology maps",
  r"The maps \(T_i\) commute with the differentials and induce \(T_i^*\) on the cohomology.",
  r"If \(d_iT_i=T_{i+1}d_i\), then \(T_i\) preserves \(\ker d_i\) and carries \(\operatorname{im}d_{i-1}\) to itself, so it induces a well-defined linear map \(H^i(T)\) on \(\ker d_i/\operatorname{im}d_{i-1}\).",
  r"The star on \(T_i^*\) denotes the induced cohomology map here, not the metric adjoint.",
  refs=[AB], correctness="correct", area="Elliptic complexes")
I(56,"P000093","theorem","Finiteness of elliptic-complex cohomology",
  r"All cohomology groups of an elliptic complex are said to be finite-dimensional.",
  r"For a finite elliptic complex of smooth finite-rank bundles on a compact smooth manifold without boundary, every smooth cohomology group is finite-dimensional. On a manifold with boundary, ellipticity of the interior symbol alone is insufficient.",
  r"Compactness and absence of boundary are supplied. A noncompact complex can have infinite-dimensional cohomology, for example holomorphic functions in degree zero of a Dolbeault complex.",
  refs=[AB], area="Elliptic complexes")
I(56,"P000093","definition","The Lefschetz number of an elliptic complex",
  r"The alternating trace of the induced cohomology endomorphisms is denoted \(L(T,E)\).",
  r"For a finite cohomologically finite complex, \(L(T,E)=\sum_i(-1)^i\operatorname{tr}H^i(T)\). A consistent grading is part of this definition: shifting every degree by one reverses the sign.",
  r"The notebook labels bundles starting at 1 while also referring to the usual de Rham convention. We use the actual cohomological degree, beginning at zero for forms.",
  refs=[AB], correctness="correct with missing hypotheses", area="Elliptic complexes")
I(56,"P000094","construction","Geometric lifts of a map to the complex",
  r"A map \(f:X\to X\) and maps of the pulled-back bundles define the operators \(T_i\), but the fibre display uses \(f^{-1}x\).",
  r"For a smooth map \(f\) and a bundle morphism \(\phi_i:f^*E_i\to E_i\), define \(T_is(x)=\phi_i(x)s(f(x))\), with \(\phi_i(x):E_{i,f(x)}\to E_{i,x}\). Assume these operators form a chain map. An inverse-map convention is possible when \(f\) is a diffeomorphism, but the kernel and derivative conventions must then change together.",
  r"The source's \(f^{-1}x\) cannot define a fibre for an arbitrary noninvertible map. The displayed pullback and inverse conventions are not silently conflated.",
  refs=[AB], correctness="false as written", match="partial", area="Elliptic complexes")
I(56,"P000094","definition","Simple fixed points and transversality",
  r"The notes call a fixed point simple when \(\det(I-df_p)\ne0\) and describe transverse intersection of the graph and diagonal.",
  r"A fixed point \(p\) of a smooth self-map is nondegenerate if \(I-df_p:T_pX\to T_pX\) is invertible. This is equivalent to transversality of its graph and the diagonal at \((p,p)\), and implies that \(p\) is isolated. On compact \(X\), if every fixed point is nondegenerate, there are finitely many.",
  refs=[AB], correctness="correct", area="Differential topology")
I(56,"P000094","definition","The local Lefschetz contribution",
  r"The local number is an alternating fibre trace divided by the absolute determinant of \(1-df\).",
  r"With the preceding pullback convention and a nondegenerate fixed point, the local contribution is \(\nu_p(T)=\frac{\sum_i(-1)^i\operatorname{tr}\phi_i(p)}{|\det_{\mathbb R}(I-df_p)|}\). The numerator is the supertrace on the graded bundle fibre, not the cohomological trace.",
  r"The real determinant in the denominator is distinguished from the complex determinant used after simplifying a Dolbeault application.",
  refs=[AB], correctness="correct", area="Elliptic complexes")
I(56,"P000094","theorem","The Atiyah-Bott fixed-point formula",
  r"The sum of the local numbers over simple fixed points is asserted to equal \(L(T,E)\).",
  r"Let \(X\) be compact and without boundary, let \(E^\bullet\) be an elliptic complex, and let a smooth map \(f:X\to X\) have only nondegenerate fixed points. If smooth zero-order bundle lifts define a chain map \(T\), then \(L(T,E)=\sum_{p=f(p)}\nu_p(T)\).",
  r"All global and chain-map hypotheses are gathered here. The theorem concerns a geometric operator, not an arbitrary endomorphism of the section complex.",
  fate=r"The theorem was already in the autumn 1964 Harvard notes \citep{atiyahbott1964notes}; the later article \citep{atiyahbott1967lefschetz} does not turn Gelfand's exposition into a new announcement.",
  refs=[AB,"atiyahbott1967lefschetz"], area="Elliptic complexes")
I(56,"P000095","construction","Formal adjoints and the Hodge Laplacian",
  r"After choosing metrics, the adjoint and \(\Box=dd^*+d^*d\) are introduced.",
  r"For a first-order elliptic complex on a closed manifold with Hermitian bundle metrics and a positive density, put \(\Box_i=d_{i-1}d_{i-1}^*+d_i^*d_i\). It is elliptic, formally self-adjoint, and nonnegative: \((\Box_i u,u)=\|d_{i-1}^*u\|^2+\|d_i u\|^2\).",
  r"For a complex whose differentials have unequal positive orders, the unweighted sum need not have the required elliptic principal symbol; one needs an equal-order reduction or suitable powers. The simple formula is used here in its first-order setting.",
  refs=[AB], area="Elliptic complexes")
I(56,"P000095","theorem","Discrete spectrum and harmonic representatives",
  r"The notes describe positive eigenvalues of finite multiplicity, followed by a separate zero-eigenvalue space representing cohomology.",
  r"The self-adjoint elliptic Hodge Laplacian on a closed manifold has nonnegative discrete spectrum, finite-dimensional smooth eigenspaces, and a complete \(L^2\) orthonormal eigenbasis. The harmonic space \(\ker\Box_i=\ker d_i\cap\ker d_{i-1}^*\) maps isomorphically to \(H^i(E^\bullet)\).",
  r"Nonnegative replaces the earlier unrestricted positive. Finite multiplicity means finitely many independent eigenvectors for each eigenvalue, not finitely many eigenvalues overall.",
  refs=[AB], correctness="false as written", area="Elliptic complexes")
I(56,"P000095","claim","Positive-eigenvalue complexes are acyclic",
  r"The differentials preserve the eigenspaces of \(\Box\), and the notes separate the positive-eigenvalue complexes from the harmonic one.",
  r"The identities \(d\Box=\Box d\) and \(d^*\Box=\Box d^*\) give complexes on each eigenspace. If \(\lambda>0\), \(h=d^*/\lambda\) satisfies \(dh+hd=\operatorname{id}\), so that eigenspace complex has zero cohomology.",
  r"The contracting homotopy is the explicit proof later supplied in Bernstein's intervention. No commutation of a separate chain map \(T\) with \(\Box\) is assumed.",
  refs=[AB], correctness="correct", area="Elliptic complexes")
I(56,"P000095","method","Formal trace cancellation",
  r"The notes compare the sum of diagonal matrix entries, the sum of eigenvalues, and integration of a kernel on the diagonal, anticipating cancellation in an alternating trace.",
  r"For a trace-class operator these are valid trace descriptions under their usual convergence hypotheses; a smooth kernel on a closed manifold gives a trace by diagonal integration. A geometric pullback is generally not trace class. The cohomological supertrace must therefore be obtained using a smoothing regularization before applying finite-dimensional cancellation.",
  r"These are formal motivations, not permission to identify divergent ordinary traces. Later records construct the required regularization.",
  refs=[AB], correctness="correct with missing hypotheses", area="Operator theory")
C("P000094","fibre map in the geometric-lift construction",
  r"\(E_{i,f^{-1}x}\to E_{i,x}\) beside a map \(f:X\to X\)",
  r"Choose consistently either \(\phi:f^*E\to E,\ \phi_x:E_{f(x)}\to E_x\), or an inverse-map convention requiring invertibility.",
  "The inverse superscript is visible in the scan. This is a convention mismatch in the notebook, not an established transcription error; there is no single diplomatic substitution valid for every later formula.")
C("P000095","spectral description",
  "positive eigenvalues, with zero eigenspace then used",
  "nonnegative spectrum; strictly positive eigenvalues considered separately from zero",
  "The handwritten positive wording is genuine. The immediately following harmonic discussion and the identity (Box u,u)=||du||^2+||d*u||^2 require nonnegative.")

T(57,"1965-10-11","I. M. Gelfand","P000096",
  "Seminar programme for 1965-66",
  r"The seven agenda entries propose Agranovich on integro-differential operators; Kirillov, Gelfand, or Dynin on Atiyah--Singer and the Cartan--Schwartz and Vishik seminars; Minlos on statistical physics; Graev on adeles; Kirillov and Gelfand on algebraic groups; Gelfand on Bott--Chern and zero distribution of sections; and Kazhdan on Riemann--Roch--Grothendieck. These are assignments and reading topics, not theorem statements. The Bott--Chern reference can be identified as the 1965 Acta Mathematica paper \citep{bottchern1965hermitian}. Kazhdan's talk begins separately in the lower part of the same page.", kind="plan")

T(58,"1965-10-11","D. A. Kazhdan","P000096-P000100",
  "Algebraic varieties, rational equivalence, and the approach to Riemann-Roch",
  r"The announced Riemann--Roch discussion starts with the foundations of classical algebraic geometry: affine sets, regular functions, ringed spaces, gluing, products, and separation. It then introduces cycles and their equivalence via \(\mathbb P^1\), ending with an unfinished proposed map \(K(X)\to A(X)\). The framework belongs to the earlier theory of coherent sheaves and Grothendieck's Riemann--Roch theorem \citep{serre1955coherent,borelserre1958riemannroch}. The last lines do not state a Riemann--Roch formula or a complete axiom system for Chern classes.")
I(58,"P000096","construction","The announced characteristic classes of a vector bundle",
  r"The first line under Kazhdan's heading associates a vector sheaf with a cohomology class, called a Chern class.",
  r"A complex vector bundle \(E\) of rank \(r\) on a paracompact Hausdorff space has characteristic classes \(c_i(E)\in H^{2i}(X;\mathbb Z)\), \(0\le i\le r\), with \(c_0=1\). In the smooth algebraic setting, locally free sheaves have algebraic classes \(c_i(E)\in CH^i(X)\); over \(\mathbb C\), the cycle-class comparison gives their topological counterparts.",
  r"Finite-rank locally free sheaves, rather than arbitrary coherent sheaves on an unspecified singular space, are used for this introductory statement. No particular class or axiom is supplied in the source line.",
  refs=[RR], match="partial", area="Algebraic geometry")
I(58,"P000096","definition","Affine algebraic sets and their coordinate rings",
  r"Over an algebraically closed field, the common zeros of given polynomials form an affine variety; polynomial functions are identified with the quotient by the ideal spanned by the equations.",
  r"For \(I\subset k[x_1,\ldots,x_n]\), the classical algebraic set \(X=V(I)\) has ring of polynomial functions \(k[X]=k[x_1,\ldots,x_n]/I(X)=k[x]/\sqrt I\). One obtains \(k[x]/I\) itself if \(I\) is radical, or if one deliberately uses the possibly nonreduced affine scheme \(\operatorname{Spec}(k[x]/I)\).",
  r"The notebook works with point sets and restrictions of functions, so passing to the radical is required. For example \(x^2=0\) and \(x=0\) define the same classical point set but different quotient rings.",
  refs=[FAC], correctness="false as written", area="Algebraic geometry")
I(58,"P000097-P000098","definition","Regular functions on principal open sets",
  r"Additional nonvanishing conditions are allowed; on the punctured line the functions are \(P(x)/x^m\), and principal opens provide a basis.",
  r"For \(X=\operatorname{Spec}A\) of finite type over an algebraically closed field and \(f\in A\), \(D(f)\) is affine with coordinate ring \(A_f\). In the reduced classical interpretation these are locally rational functions with no poles on \(D(f)\). On \(\mathbb A^1\setminus\{0\}\), the ring is \(k[t,t^{-1}]\).",
  r"For reducible varieties, a single rational-function-field description is inadequate; the localization formulation handles zero divisors correctly. Finitely many nonvanishing conditions combine as a product.",
  refs=[FAC], correctness="correct with missing hypotheses", area="Algebraic geometry")
I(58,"P000097","definition","Prevarieties as locally affine ringed spaces",
  r"A prevariety is locally isomorphic to an affine variety; the notes emphasize that its functions and ringed-space structure accompany its points.",
  r"A classical algebraic prevariety is a space with a sheaf of \(k\)-algebras locally isomorphic to affine algebraic varieties with their regular-function sheaves, subject to the customary finite-type cover condition. The local isomorphisms are isomorphisms of ringed spaces, not just homeomorphisms.",
  r"The finite-type and compatibility conventions distinguish this from an arbitrary locally ringed space or an arbitrary gluing of sets.",
  refs=[FAC], correctness="correct with missing hypotheses", area="Algebraic geometry")
I(58,"P000097-P000098","construction","The structure sheaf and its restriction maps",
  r"The sheaf of rings is specified on a basis of sets defined by a nonvanishing polynomial, with sections identified by their values.",
  r"The presheaf \(D(f)\mapsto A_f\), with localization restriction maps, extends uniquely to the structure sheaf \(\mathcal O_X\) on an affine algebraic variety. Local regular functions that agree on overlaps glue uniquely.",
  r"An arbitrary assignment of rings to open sets would not suffice: the restriction maps and gluing axiom are part of the construction.",
  refs=[FAC], correctness="correct", area="Algebraic geometry")
I(58,"P000098","definition","Morphisms respect functions contravariantly",
  r"The diagram for an isomorphism of ringed spaces includes a map between the bases and an induced map on sheaves of functions in the opposite direction.",
  r"A morphism of locally ringed spaces \(f:X\to Y\) consists of a continuous map and \(f^\#:\mathcal O_Y\to f_*\mathcal O_X\) inducing local homomorphisms of stalks. For affine varieties this is contravariantly equivalent to a homomorphism of their coordinate \(k\)-algebras.",
  r"The notes' emphasis on maps induced by the base is made precise by pullback of regular functions and the local condition. Abstract bundle isomorphisms of the underlying sheaf spaces are not enough.",
  refs=[FAC], area="Algebraic geometry")
I(58,"P000097-P000098","claim","The punctured affine plane is not affine",
  r"The example \(\mathbb C^2\setminus\{0\}\) is called nonaffine but is covered by the two affine opens \(x\ne0\) and \(y\ne0\).",
  r"For any field \(k\), \(U=\mathbb A^2_k\setminus\{0\}\) is covered by \(D(x)\) and \(D(y)\), and \(\Gamma(U,\mathcal O_U)=k[x,y]_x\cap k[x,y]_y=k[x,y]\) inside \(k(x,y)\). If \(U\) were affine, the canonical morphism \(U\to\operatorname{Spec}\Gamma(U,\mathcal O_U)=\mathbb A^2_k\) would be an isomorphism, contrary to its missing origin.",
  r"The intersection computation supplies an algebraic proof and does not depend on analytic Hartogs extension. The classical point-set formulation in the notebook uses \(k=\mathbb C\).",
  refs=[FAC], match="partial", correctness="correct", area="Algebraic geometry")
I(58,"P000098-P000099","construction","Realizing a principal open as a closed affine variety",
  r"The condition \(Q(x)\ne0\) is replaced by the extra equation \(Q(x)y-1=0\).",
  r"If \(X\subset\mathbb A^n\) has coordinate ring \(A\), the maps \(x\mapsto(x,Q(x)^{-1})\) and projection identify \(D(Q)\) with the closed subvariety of \(X\times\mathbb A^1\) defined by \(Qy-1=0\). Algebraically, \(A_Q\cong A[y]/(Qy-1)\).",
  refs=[FAC], correctness="correct", area="Algebraic geometry")
I(58,"P000099","construction","Products and tensor-product coordinate rings",
  r"For affine factors the notebook adds the two extended ideals in the polynomial ring of both variable sets and obtains a tensor product of coordinate rings; general products are glued from affine products.",
  r"If \(X=\operatorname{Spec}A\) and \(Y=\operatorname{Spec}B\) are affine \(k\)-schemes, \(X\times_kY=\operatorname{Spec}(A\otimes_kB)\). For \(A=k[x]/I\), \(B=k[y]/J\), the tensor product is \(k[x,y]/(I\,k[x,y]+J\,k[x,y])\). In the classical reduced finite-type setting over algebraically closed \(k\), these products are again reduced; compatible affine charts glue the general product.",
  r"The operation on ideals is a sum inside the ambient polynomial ring, not an assertion of direct-sum independence.",
  refs=[FAC], correctness="correct", area="Algebraic geometry")
I(58,"P000099","claim","The Zariski topology on a product is not the product topology",
  r"The notes explicitly warn that the product of varieties is not the ordinary topological product.",
  r"For an infinite algebraically closed field, \(\mathbb A^1(k)\) has the cofinite topology. The diagonal in \(\mathbb A^2(k)\) is Zariski closed, but it is dense in the product of the two cofinite topologies. Thus the algebraic product topology is strictly finer in this example.",
  r"This distinguishes the product in varieties from the product in topological spaces and also clarifies the subsequent diagonal criterion.",
  refs=[FAC], correctness="correct", area="Algebraic geometry")
I(58,"P000099","definition","Separation and the closed diagonal",
  r"A prevariety whose diagonal in \(X\times X\) is closed is called an algebraic variety; an aside compares this with Hausdorff separation and then incorrectly with the sheaf axiom.",
  r"A classical prevariety over \(k\) is separated if its diagonal is closed in the algebraic product. In scheme language the diagonal must be a closed immersion. The Hausdorff criterion uses the ordinary topological product; the sheaf condition instead consists of unique gluing of compatible local sections.",
  r"The handwritten sentence that a presheaf is a sheaf when its diagonal is closed has no valid meaning in the displayed framework. It is not a criterion for sheaves.",
  refs=[FAC], correctness="false as written", area="Algebraic geometry")
I(58,"P000099","construction","The affine line with doubled origin",
  r"Two affine lines are glued along the punctured line and the reader is asked to check that the diagonal is not closed.",
  r"Glue two copies of \(\mathbb A^1_k\) by the identity on \(D(t)\). The resulting prevariety has distinct origins \(0_1,0_2\). In the chart \(U_1\times U_2\cong\mathbb A^2\), its diagonal meets the chart in \(\{(t,t):t\ne0\}\), whose closure contains \((0_1,0_2)\); hence the diagonal is not closed.",
  r"The diagram is interpreted as two retained origins, not an infinitesimal double point or a nonreduced scheme.",
  refs=[FAC], match="partial", correctness="correct", area="Algebraic geometry")
I(58,"P000100","definition","Algebraic cycles",
  r"Formal integer combinations \(\sum a_iV_i\) of subvarieties are called cycles, with cycle classes described as more precise than cohomology.",
  r"The group \(Z_r(X)\) is the free abelian group on integral closed \(r\)-dimensional subvarieties of \(X\). One can take the direct sum over \(r\). Over \(\mathbb C\), cycle-class maps connect suitable Chow groups to cohomology or Borel--Moore homology, but rational equivalence is generally finer than homological equivalence.",
  r"Irreducibility, reduced structure, and the dimension grading are supplied. The vague comparison with cohomology is a direction of information, not an assertion that the cycle-class map is injective.",
  refs=[RR], match="partial", area="Algebraic geometry")
I(58,"P000100","definition","Equivalence through a family over the projective line",
  r"Two cycles are declared equivalent when they are fibres at \(a,b\in\mathbb P^1\) of a cycle \(W\subset X\times\mathbb P^1\).",
  r"Rational equivalence on \(Z_r(X)\) is generated by differences of the intersection cycles \(W\cdot(X\times\{a\})-W\cdot(X\times\{b\})\), where \(W\) is an \((r+1)\)-cycle with the relevant intersections proper and \(a\ne b\). The quotient is \(CH_r(X)\). Equivalently one uses divisors of rational functions on integral \((r+1)\)-dimensional subvarieties.",
  r"Intersection multiplicities and generation of an equivalence relation are supplied. Replacing \(\mathbb P^1\) by an arbitrary connected parameter curve would concern algebraic equivalence, a different relation.",
  refs=[RR], area="Algebraic geometry")
I(58,"P000100","construction","Linear equivalence of divisors and the graph of a rational function",
  r"For curves \(U,V\) on a surface, the notes use a function with zeros on \(U\), poles on \(V\), and its graph in \(X\times\mathbb P^1\).",
  r"On a normal integral variety, Weil divisors \(D_0,D_\infty\) are linearly equivalent if \(D_0-D_\infty=\operatorname{div}(f)\) for a nonzero rational function \(f\). The closure of the graph of \(f:X\dashrightarrow\mathbb P^1\) realizes the corresponding rational-equivalence relation with multiplicities.",
  r"One must prescribe orders of zeros and poles, not merely their supports. At indeterminacy points, the graph closure replaces the naive set \((x,f(x))\).",
  refs=[RR], area="Algebraic geometry")
I(58,"P000100","question","The unfinished additive map from K-theory to cycle classes",
  r"Under the heading Chern classes, the notes write a linear map \(K(X)\to A(X)\), begin axiom 1, and cancel its continuation.",
  r"No unique map is defined. The Chern character is additive \(K_0(X)\to CH^*(X)\otimes\mathbb Q\) for smooth \(X\); the total Chern class satisfies a multiplicative Whitney formula and is not an additive map to the integral Chow group. These are distinct candidates.",
  r"Neither rational coefficients nor the decisive axioms survive. It would be an unsupported repair to relabel the entry as a complete definition of the Chern character, or to supply Grothendieck--Riemann--Roch as its statement.",
  cls="F", correctness="not determinable", match="partial", verification="read the result",
  fate=r"\citet{borelserre1958riemannroch} supplies the pre-existing distinction between Chern classes and the Chern character; it does not resolve the cancelled wording.",
  status="As of 9 November 2026, both surrounding theories are established, while the specific transformation intended in these last lines remains unidentified.",
  refs=[RR], confidence="low", area="Algebraic geometry")
C("P000096","coordinate-ring description",
  "quotient by the ideal spanned by the displayed polynomials",
  "for the classical zero set, quotient by the radical of that ideal; alternatively specify a possibly nonreduced scheme",
  "The scan confirms the ideal-of-equations wording. This is a missing mathematical qualification: x^2=0 supplies an immediate counterexample to the unrestricted classical identification.")
C("P000099","aside after the closed-diagonal criterion",
  "a presheaf is called a sheaf if the diagonal is closed",
  "retain as a notebook error; the closed algebraic diagonal characterizes separation of the prevariety, whereas the sheaf axiom is unique gluing",
  "Both transcription and scan genuinely have the presheaf/sheaf words. No transcription repair is justified.")
C("P000100","Chern-class heading and final map",
  r"the map \(K(X)\to A(X)\) is linear",
  "leave the map unidentified; an additive Chern character needs rational coefficients, and total Chern classes obey a multiplicative Whitney formula",
  "The linearity word and cancelled first axiom are visible in the scan. This is an unresolved mathematical identification, not evidence that the scribe meant one uniquely recoverable formula.")

T(59,"1965-10-18","I. M. Gelfand","P000101-P000102",
  "Elliptic complexes and the Hodge decomposition",
  r"Gelfand repeats the symbol and geometric-endomorphism setup, chooses a density and metrics, and introduces the formal adjoint and Laplacian. The eigenspace cohomology assertion reaches the top of P000102. Dynin and Bernstein then intervene before the heading indicating that Gelfand resumes; these three headings are kept as separate catalogue records \citep{atiyahbott1964notes}.")
I(59,"P000101","definition","Repeated symbol and ellipticity setup",
  r"The formula \(d(f^ms)(x_0)=\sigma(d,df_{x_0})s(x_0)\) and the exact symbol sequence are written again.",
  r"For a finite differential complex, the principal symbol of an order-\(m\) operator may be normalized by the displayed \(f^m\) formula, incorporating the factor \(m!\). The complex is elliptic when the fibre symbol sequence is exact at every nonzero real covector.",
  r"The condition \(f(x_0)=0\), explicit in the earlier exposition, is still needed. This is a repeat occurrence of the definitions in record 55, not a new theorem.",
  refs=[AB], area="Elliptic complexes")
I(59,"P000101","construction","Repeated geometric endomorphisms",
  r"A map \(f:X\to X\) and bundle maps give \(T\); the simplest example is differential forms, where \(f\) supplies the fibre map.",
  r"A smooth map \(f\) acts on differential forms by pullback \(f^*\), satisfying \(d f^*=f^*d\). More generally, bundle lifts \(\phi_i:f^*E_i\to E_i\) give a complex endomorphism only if the resulting operators commute with the differentials.",
  r"The bundle diagram is reconstructed with the pullback convention. A generic bundle map covering \(f\) does not automatically produce a chain map in the required direction.",
  refs=[AB], area="Elliptic complexes")
I(59,"P000101","theorem","Repeated finite-dimensionality theorem",
  r"Theorem 1 says that the elliptic complex has finite-dimensional homology.",
  r"A finite elliptic complex on a closed compact smooth manifold has finite-dimensional smooth cohomology in every degree.",
  r"Compactness and absence of boundary are implicit in this continuation, not consequences of the symbol definition. The notebook's homology is the cohomology of its degree-raising complex.",
  refs=[AB], area="Elliptic complexes")
I(59,"P000101","construction","Densities, duality, and formal adjoints",
  r"A nowhere vanishing top form and Hermitian structures define a duality map \(\alpha\), and \(d^*=\alpha^{-1}d'\alpha\) is written.",
  r"A positive smooth density on \(X\) and Hermitian metrics on the bundles define \(L^2\) pairings. The formal adjoint \(d_i^*\) is the unique differential operator satisfying \((d_i u,v)=(u,d_i^*v)\) for compactly supported smooth sections; equivalently it is obtained from the formal transpose by the metric-density identifications.",
  r"A density removes an unnecessary orientability assumption. The notation suppresses different \(\alpha_i\) in adjacent degrees and the anti-linearity required for complex Hermitian duality. On a manifold with boundary a Hilbert-space adjoint additionally involves domains.",
  refs=[AB], match="partial", area="Elliptic complexes")
I(59,"P000101","construction","The repeated Laplacian and finite eigenspaces",
  r"The notes form \(\Box=d^*d+dd^*\), define \(\Gamma_\lambda(E_i)\) by \(\Box s=\lambda s\), and infer finite-dimensional eigenspaces from ellipticity.",
  r"For a first-order elliptic complex on a closed compact manifold, \(\Box_i=d_i^*d_i+d_{i-1}d_{i-1}^*\) is a nonnegative elliptic self-adjoint operator with compact resolvent. Thus each eigenspace is finite-dimensional and consists of smooth sections.",
  r"Ellipticity on a noncompact space alone would not imply this spectral conclusion. The first-order or compatible equal-order setup is retained.",
  refs=[AB], area="Elliptic complexes")
I(59,"P000101","claim","Commutation with the Laplacian",
  r"The identity \(\Box d=d\Box\) is displayed and used to construct the complex on each eigenspace.",
  r"On smooth sections of a differential complex, \(d_{i+1}d_i=0\) gives \(\Box_{i+1}d_i=d_i\Box_i\). Hence \(d_i\) maps the \(\lambda\)-eigenspace in degree \(i\) into that in degree \(i+1\). The analogous adjoint identity also holds.",
  r"The equality is degreewise. It does not imply that an arbitrary chain endomorphism \(T\) commutes with \(\Box\).",
  refs=[AB], correctness="correct", area="Elliptic complexes")
I(59,"P000102","theorem","Cohomology of the eigenspace complexes",
  r"The Hodge assertion is quoted without proof: the eigenspace complex has the original cohomology at \(\lambda=0\) and zero cohomology at \(\lambda\ne0\).",
  r"Under the preceding closed compact elliptic-complex assumptions, \(H^i(\Gamma_\lambda(E^\bullet))=0\) for \(\lambda>0\), and inclusion identifies \(\Gamma_0(E_i)\) with \(H^i(E^\bullet)\).",
  r"The two conclusions have different proofs: an algebraic contracting homotopy for positive \(\lambda\), and the global Hodge decomposition for the harmonic representatives.",
  refs=[AB], correctness="correct", area="Elliptic complexes")

T(60,"1965-10-18","A. S. Dynin","P000102",
  "Intervention on positive-eigenvalue cohomology",
  r"The short intervention insists that nonzero eigenspaces give zero cohomology. The written justification then identifies cohomology with the kernel of a shifted Laplacian and asks about reapplying Hodge theory. That equation is not a valid proof: the shifted operator is not the nonnegative Hodge Laplacian of the original complex. Bernstein's immediately following intervention gives the direct contracting-homotopy argument.")
I(60,"P000102","claim","Acyclicity and the invalid shifted-Laplacian shortcut",
  r"Dynin says the nonzero-\(\lambda\) cohomology is zero, but the boxed formula reads \(H^i(\Gamma_\lambda(E))=\ker(\Box-\lambda)\), followed by a proposed Hodge argument.",
  r"For the Hodge Laplacian, the positive-\(\lambda\) eigenspace complex is acyclic. It is not generally isomorphic in cohomology to \(\ker(\Box-\lambda)\): this kernel is the entire, often nonzero, \(\lambda\)-eigenspace. The correct contraction is \(d^*/\lambda\).",
  r"One cannot replace \(\Box\) by \(\Box-\lambda\) in the harmonic-representative theorem while leaving the differential and inner product unchanged. The source's intended conclusion is correct, while the displayed identification is false.",
  refs=[AB], correctness="false as written", match="partial", area="Elliptic complexes")
C("P000102","Dynin's boxed identification",
  r"\(H^i(\Gamma_\lambda(E))=\ker(\Box-\lambda)\)",
  r"for \(\lambda>0\), \(H^i(\Gamma_\lambda(E))=0\), proved by \(h=d^*/\lambda\); the displayed kernel is the eigenspace, not its cohomology",
  "The boxed equality is genuinely present in the scan. It is a notebook mathematical error or incomplete failed argument, not a mistranscribed valid use of the Hodge theorem.")

T(62,"1965-10-18","I. N. Bernstein","P000102",
  "Intervention giving the contracting homotopy",
  r"Bernstein's named intervention follows Dynin and precedes the words indicating Gelfand's return. It derives the vanishing of positive-eigenvalue cohomology directly from \(\lambda s=dd^*s\). Catalogue record 62 is therefore placed before record 61 in actual source order.")
I(62,"P000102","method","Bernstein's direct proof of acyclicity",
  r"For \(s\in\Gamma_\lambda(E_i)\), \(ds=0\), and \(\lambda\ne0\), the notes write \(s=d(d^*s/\lambda)\); they also state that \(d^*s\) is a smooth eigenfunction.",
  r"If \(\Box s=\lambda s\), \(\lambda>0\), and \(ds=0\), then \(\lambda s=(dd^*+d^*d)s=dd^*s\). Thus \(s=d(d^*s/\lambda)\); since \(d^*\Box=\Box d^*\), the primitive remains in the \(\lambda\)-eigenspace. Elliptic regularity ensures smoothness of the eigensections.",
  r"This is a complete elementary proof inside the already established spectral setup. It does not establish the existence or completeness of that setup by itself.",
  fate=r"The argument is an exposition of the standard Hodge-complex contraction used in \citet{atiyahbott1964notes}; no independent publication novelty is inferred from the intervention.",
  refs=[AB], correctness="correct", area="Elliptic complexes")

T(61,"1965-10-18","I. M. Gelfand","P000102-P000104",
  "Harmonic compression, trace regularization, and pseudodifferential operators",
  r"The heading indicating Gelfand's return comes after both interventions. He compresses the chain map to Laplacian eigenspaces, obtains alternating trace cancellation, introduces the weighted trace series, and begins an oscillatory definition of pseudodifferential operators. That definition continues into the top of P000104, above the next dated heading. The argument follows the 1964 Harvard notes, especially their spectral and pseudodifferential sections \citep{atiyahbott1964notes,kohnnirenberg1965algebra}.")
I(61,"P000102","theorem","The harmonic subcomplex and spectral expansion",
  r"The zero-eigenvalue case is attributed to the Hodge proof, \(\Gamma(E)\) is written as a sum of eigenspaces, and \(\Box s=0\) implies \(ds=0\).",
  r"For a closed compact first-order elliptic complex, \(L^2(E_i)\) is the Hilbert direct sum of its finite-dimensional Laplacian eigenspaces. A harmonic section satisfies both \(d_is=0\) and \(d_{i-1}^*s=0\), and represents a unique cohomology class. A smooth section has a convergent spectral expansion in every Sobolev norm.",
  r"The displayed sum is not an algebraic direct sum: general smooth sections need infinitely many eigencomponents. Smooth spectral convergence uses elliptic estimates.",
  refs=[AB], area="Elliptic complexes")
I(61,"P000102","construction","Compression of a chain map to each eigenspace",
  r"The definition \(T_\lambda=\pi_\lambda T i_\lambda\) uses inclusion and orthogonal projection; the zero block is identified with the induced cohomology map.",
  r"Let \(T\) preserve the smooth complex but not necessarily the metric. Since the spectral projections commute with \(d\), \(T_\lambda=\pi_\lambda T i_\lambda\) is a finite-dimensional chain endomorphism of the \(\lambda\)-complex. On the harmonic complex, \(T_0\) represents \(H^\bullet(T)\).",
  r"Compression does not require \(T\Gamma_\lambda\subset\Gamma_\lambda\). The equality with the cohomological action is after the Hodge identification, not literal preservation of each harmonic section by \(T\).",
  refs=[AB], correctness="correct", area="Elliptic complexes")
I(61,"P000102-P000103","theorem","Hopf trace cancellation on eigenspaces",
  r"The alternating chain trace equals the alternating cohomology trace. The zero block contributes \(L(T,E)\), and every nonzero block contributes zero.",
  r"For a finite-dimensional bounded complex and a chain endomorphism \(S\), \(\sum_i(-1)^i\operatorname{tr}(S|C^i)=\sum_i(-1)^i\operatorname{tr}(H^i(S))\). Applying this to \(T_\lambda\) gives supertrace \(0\) for \(\lambda>0\), and \(L(T,E)\) for \(\lambda=0\).",
  r"Finiteness is essential to this elementary trace identity. It is applied before the infinite sum is formed.",
  refs=[AB], correctness="correct", area="Homological algebra")
I(61,"P000103","construction","The weighted trace series and its half-plane of convergence",
  r"The regularized trace is \(\operatorname{tr}^{z}(E_i)=\sum_\lambda(1+\lambda)^{-z}\operatorname{tr}(T_\lambda|E_i)\), asserted to converge for \(\operatorname{Re}z>\dim X/2\).",
  r"If \(X\) is closed of real dimension \(n\), \(\Box_i\) is a nonnegative elliptic operator of order two, and \(T_i\) is bounded on \(L^2(E_i)\), then \(Z_i(z)=\operatorname{tr}(T_i(1+\Box_i)^{-z})\) is holomorphic for \(\operatorname{Re}z>n/2\). Its spectral series is absolutely convergent there.",
  r"The bound follows from \(|\operatorname{tr}T_\lambda|\le\|T\|\dim\Gamma_\lambda\) and the order-two eigenvalue count. Smooth bundle-weighted pullback by a diffeomorphism is \(L^2\)-bounded; arbitrary smooth maps need a different continuity argument and cannot simply inherit this estimate.",
  refs=[AB], area="Operator theory")
I(61,"P000103","claim","Constancy of the regularized supertrace",
  r"The equality \(L(T,E)=\sum_i(-1)^i\operatorname{tr}^{z}(E_i)\) is written for all \(z\), before continuation is proved.",
  r"In the common convergence half-plane, absolute convergence permits summation over eigenspaces and gives \(\sum_i(-1)^iZ_i(z)=L(T,E)\). Any analytic continuation of this supertrace is the same constant on its connected domain.",
  r"The words for all \(z\) initially mean all \(z\) in the proven half-plane. Entire continuation of the individual geometric traces requires the transversality theorem in record 63; it does not follow from the cancellation identity alone.",
  refs=[AB], area="Elliptic complexes")
I(61,"P000103","remark","An unassigned warning about a pole at zero",
  r"A parenthetical line mentions analytic continuation and a pole at \(z=0\), without specifying which trace function it concerns.",
  r"The entry is insufficient to identify a pole assertion. An infinite ordinary trace at a formal parameter value does not imply a pole of its analytic continuation. Under the later transverse geometric hypotheses, the individual regularized traces are entire and therefore have no pole at zero.",
  r"The warning is retained as ambiguous, rather than silently read as a universal claim about all spectral zeta functions or as a claim about the already constant supertrace.",
  cls="F", correctness="not determinable", match="partial", verification="read the result",
  fate=r"The continuation result in \citet[Section 9]{atiyahbott1964notes} determines the transverse case; it does not identify the referent of this parenthesis.",
  status="As of 9 November 2026, the parenthetical referent remains unidentified; it is not a distinct open trace-regularization problem.",
  refs=[AB], confidence="low", area="Operator theory")
I(61,"P000103","construction","The circle model and the Laplacian sign",
  r"On \(S^1\), \(d=d/dt\) is followed by \(\Box=d^2/dt^2\); a weighted composition operator is also drawn.",
  r"For the standard periodic \(L^2\) metric, \((d/dt)^*=-d/dt\), so the nonnegative Laplacian on the circle complex is \(-d^2/dt^2\), with eigenvalues \(m^2\) for \(e^{imt}\) when the period is \(2\pi\). A geometric action on both functions and one-forms must satisfy the chain-map identity.",
  r"The missing minus sign is a notebook sign error relative to its own definition \(dd^*+d^*d\), not a harmless choice of the signed scalar Laplacian.",
  refs=[AB], correctness="false as written", match="partial", area="Elliptic complexes")
I(61,"P000103-P000104","definition","Oscillatory asymptotics for pseudodifferential operators",
  r"A map \(P:\Gamma_c(E)\to\Gamma(F)\) is called pseudodifferential when \(e^{-i\lambda g}P(e^{i\lambda g}s)\) has an asymptotic expansion with descending orders tending to minus infinity and \(dg\ne0\) on the support of \(s\).",
  r"For a properly supported classical pseudodifferential operator of order \(m\), nonstationary phases give an expansion \(e^{-i\lambda g}P(e^{i\lambda g}s)\sim\sum_{j\ge0}\lambda^{m-j}a_j(g,s)\) as \(\lambda\to+\infty\), with local \(C^\infty\) remainder estimates; the leading term is \(\sigma_m(P)(x,dg_x)s(x)\). Polyhomogeneous classes can allow a more general discrete decreasing degree sequence.",
  r"Continuity, uniform remainder estimates, and localization are needed for a characterization; mere pointwise existence of formal coefficients is insufficient. The notes do not state these analytic quantifiers.",
  fate=r"The oscillatory formulation is in the Harvard exposition \citep{atiyahbott1964notes}; the contemporary operator calculus is \citet{kohnnirenberg1965algebra}.",
  refs=[AB,"kohnnirenberg1965algebra"], match="partial", area="Pseudodifferential operators")
C("P000103","circle example",
  r"\(\Box=d^2/dt^2\)",
  r"\(\Box=-d^2/dt^2\) for \(d=d/dt\) and the standard periodic \(L^2\) metric",
  "The positive sign is visible in the scan. The same notes define Box=dd*+d*d, whereas integration by parts gives (d/dt)*=-d/dt; this is a notebook mathematical correction.")

T(63,"1965-10-26","I. M. Gelfand","P000104-P000105",
  "Regularized traces and the local fixed-point trace",
  r"The next dated continuation begins below the end of the pseudodifferential definition on P000104. Gelfand revisits index, finite-dimensional trace cancellation, and the spectral series; he then states the entire continuation theorem for a transverse geometric map and its equality at zero with the distributional flat trace. The final computation initially calls the delta integral the number of fixed points, omitting its Jacobian weight. The weights are restored explicitly in record 65 \citep{atiyahbott1964notes}.")
I(63,"P000104","definition","The index as the Euler characteristic of a two-term complex",
  r"The two-term elliptic complex is associated with the difference of kernel and cokernel dimensions.",
  r"For an elliptic operator \(P:\Gamma(E)\to\Gamma(F)\) on a closed compact manifold, its Fredholm index is \(\dim\ker P-\dim\operatorname{coker}P\), equal to the Euler characteristic of the two-term complex in degrees zero and one. More generally \(L(\operatorname{id},E)=\sum_i(-1)^i\dim H^i(E)\).",
  r"The Sobolev completions giving a Fredholm operator do not alter its smooth kernel or cokernel. This identity does not yet compute the topological index.",
  refs=[AB], area="Index theory")
I(63,"P000104","construction","The repeated positive-eigenvalue decomposition",
  r"The Laplacian, its eigenspaces, and zero versus nonzero eigenvalues are recalled before introducing the finite-dimensional operators \(T_\lambda\).",
  r"In the closed compact first-order elliptic setting, the smooth eigenspace complexes are acyclic for \(\lambda>0\), and the zero complex is the harmonic realization of cohomology. The spectrum is nonnegative, not strictly positive when cohomology is present.",
  r"This is another occurrence of the Hodge decomposition; the repeated positive wording must retain the separate harmonic case.",
  refs=[AB], area="Elliptic complexes")
I(63,"P000104","construction","Compression does not presume invariance under T",
  r"The notes stress that \(T_\lambda=\pi_\lambda T i_\lambda\) can be used even when \(T\) does not commute with the Laplacian.",
  r"Orthogonal compression of a chain map to the \(\lambda\)-eigenspace complex is itself a chain map because \(d\pi_\lambda=\pi_\lambda d\). The off-diagonal spectral blocks of \(T\) need not vanish. Its compressed supertrace is zero for \(\lambda>0\) and is the cohomological Lefschetz number for \(\lambda=0\).",
  r"The second displayed cancellation on P000104 omits a summation sign: cancellation is over degrees and is not a separate zero trace in each degree.",
  refs=[AB], correctness="false as written", area="Elliptic complexes")
I(63,"P000105","method","The finite-dimensional trace lemma by splitting cycles and boundaries",
  r"The proof decomposes \(A_i=Z_i+C_{Z_i}\) and \(Z_i=B_i+\text{complement}\), then compares the traces.",
  r"For a finite-dimensional complex choose \(C^i=B^i\oplus H^i\oplus L^i\), with \(Z^i=B^i\oplus H^i\). The differential identifies \(L^i\) with \(B^{i+1}\). A chain map preserves the filtration by boundaries and cycles; its diagonal blocks on these two identified spaces have equal traces and cancel in the alternating sum.",
  r"The complements need not be invariant under the chain map. Only its filtration and the induced diagonal blocks are used.",
  refs=[AB], correctness="correct", area="Homological algebra")
I(63,"P000105","claim","Eigenvalue growth and trace regularization",
  r"The series with weights \((1+\lambda)^{-z}\) is repeated, alongside \(\lambda_n\sim n^{K/\dim X}\). A star on \(T_\lambda\) ambiguously suggests the cohomology action.",
  r"For a positive self-adjoint elliptic operator of order \(m>0\) on a closed \(n\)-manifold, its positive eigenvalues counted with multiplicity satisfy \(\lambda_j\sim c j^{m/n}\), with \(c>0\). Thus a bounded multiplier \(T\) gives a trace-class weighted product for \(\operatorname{Re}z>n/m\); for the Hodge Laplacian, \(m=2\).",
  r"The exponent is an order parameter, not a universal constant. The series must use the trace of the chain-space compression \(T_\lambda\), not the trace on zero cohomology, if it is to regularize each individual chain operator. The latter replacement is valid only after taking the alternating sum.",
  refs=[AB], correctness="correct with missing hypotheses", match="partial", area="Spectral theory")
I(63,"P000105","theorem","Entire continuation for transverse geometric operators",
  r"The continuation theorem says that each regularized trace is analytic on the whole plane and that its value at zero equals the flat trace; the identity operator is explicitly excluded from this argument.",
  r"Let a smooth zero-order geometric bundle lift \(T\) cover a self-map of a closed manifold whose graph is transverse to the diagonal. In the Atiyah--Bott elliptic regularization, \(\operatorname{tr}(T(1+\Box)^{-z})\), initially defined in a sufficiently far right half-plane, extends to an entire function of \(z\), with value at zero equal to the distributional flat trace of \(T\).",
  r"This is a theorem special to transverse geometric traces, not a claim that ordinary spectral zeta functions are entire. The identity on a positive-dimensional manifold is not transverse. The general-map convergence half-plane is not justified merely by an \(L^2\) bound from the preceding simplified argument.",
  fate=r"This is the continuation theorem in the spectral proof of \citet[Section 9]{atiyahbott1964notes}. The apparently strong word entire is therefore not itself a notebook error.",
  refs=[AB], area="Pseudodifferential operators")
I(63,"P000105","construction","The distribution kernel and flat trace",
  r"For \(Ts(x)=\varphi(x)s(f(x))\), the notes use the delta kernel and integrate it on the diagonal.",
  r"Relative to a smooth density, the geometric kernel is \(K_T(x,y)=\varphi(x)\delta_{f(x)}(y)\). If the fixed points are nondegenerate, its restriction to the diagonal is defined distributionally and gives \(\operatorname{tr}^{\,b}T=\sum_{p=f(p)}\operatorname{tr}\varphi(p)/|\det_{\mathbb R}(I-df_p)|\).",
  r"Transversality is what legitimizes the delta-function substitution. Arbitrary distributions cannot be restricted to the diagonal merely by writing \(K(x,x)\).",
  refs=[AB], area="Distribution theory")
I(63,"P000105","claim","The delta trace is a weighted fixed-point sum",
  r"The scalar expression \(\int\delta(x,f(x))\,dx\) is called the number of fixed points.",
  r"At isolated nondegenerate fixed points, \(\int\delta(x-f(x))\,dx=\sum_{p=f(p)}|\det(I-df_p)|^{-1}\), with the coordinate-density convention consistently applied. It equals an unweighted count only under special unit-weight conditions.",
  r"The missing absolute Jacobian determinant is essential. It reappears on P000106, so the local source trajectory itself supports this correction.",
  refs=[AB], correctness="false as written", area="Distribution theory")
C("P000104","second displayed spectral cancellation",
  r"\((-1)^i\operatorname{tr}(T_\lambda|E_i)=0\), \(\lambda\ne0\), without a sum",
  r"\(\sum_i(-1)^i\operatorname{tr}(T_\lambda|E_i)=0\)",
  "The scan has no summation sign on this line. Acyclicity cancels alternating traces over all degrees; it does not force each chain-space trace to vanish.")
C("P000105","flat-trace description at the bottom of Gelfand's talk",
  r"\(\int\delta(x,f(x))\,dx\) is the number of fixed points",
  r"\(\sum_{p=f(p)}|\det(I-df_p)|^{-1}\), assuming nondegenerate fixed points",
  "The unweighted description is present in the scan; the multivariable delta change-of-variables formula and the explicit weighted formula on P000106 require the determinant. This is a notebook mathematical omission.")
C("P000105","individual regularized trace series",
  r"\(\sum_\lambda(1+\lambda)^{-z}\operatorname{tr}(T_\lambda^*|E_i)\)",
  r"use the chain-space compression \(T_\lambda\) for the individual trace; the cohomological replacement applies to the alternating sum",
  "The star is visible but its role is unstable. Earlier T* denotes induced cohomology. If read that way here, every positive-eigenvalue contribution would disappear degreewise and would not regularize the original chain operator. Retain the mark diplomatically and explain the type distinction.")

T(64,"1965-10-26","D. A. Kazhdan","P000105-P000106",
  "Finite-type and coherent sheaves",
  r"The five-minute intervention begins at the bottom of P000105 and continues into P000106. Kazhdan defines finite generation and coherence through relation sheaves, warns that one chosen presentation is not enough over a general ring, and states the closure and local-generation properties. Serre's coherent-sheaf paper is explicitly named \citep{serre1955coherent}.")
I(64,"P000105","definition","Sheaves of modules of finite type",
  r"Near each point finitely many sections generate every stalk; they define a map \(\mathcal O_U^n\to M_U\).",
  r"An \(\mathcal O_X\)-module \(M\) is of finite type if every point has a neighbourhood \(U\) on which there is a surjection \(\mathcal O_U^n\twoheadrightarrow M|_U\) for some finite \(n\). Surjectivity is equivalent to generation on every stalk in \(U\).",
  r"Stalks, not geometric fibres after tensoring with residue fields, are the modules meant by the notebook's fibre terminology.",
  refs=[FAC], correctness="correct", area="Sheaf theory")
I(64,"P000105-P000106","definition","Coherence requires finite relations for every finite local tuple",
  r"The kernel of \(\mathcal O_U^n\to M_U\) is the relation sheaf and must be of finite type for every finite set of sections. The notes say that one fixed set is insufficient, using a one-point non-Noetherian-ring example.",
  r"A sheaf \(M\) is coherent if it is of finite type and, for every finite local tuple of sections, the kernel of the corresponding map \(\mathcal O^n\to M\) is of finite type. One finite presentation alone implies coherence when the structure sheaf is coherent, but not over an arbitrary ring.",
  r"Non-Noetherian alone is not enough for the proposed counterexample: some non-Noetherian rings are coherent. An explicit noncoherent ring is \(A=k[x_1,x_2,\ldots]/(x_1x_j:j\ge2)\); \(A\) has its trivial one-generator presentation, but the annihilator of \(x_1\) is the non-finitely-generated ideal \((x_2,x_3,\ldots)\).",
  refs=[FAC], correctness="correct with missing hypotheses", area="Sheaf theory")
I(64,"P000106","theorem","Finite-type submodules of coherent sheaves",
  r"If \(N\subset M\) is of finite type, it is said to be coherent.",
  r"If \(M\) is a coherent \(\mathcal O_X\)-module and \(N\subset M\) is a finite-type submodule sheaf, then \(N\) is coherent: every relation among sections of \(N\) is the same relation when viewed inside \(M\).",
  r"Coherence of the ambient \(M\) is required. Without it, taking \(N=M\) would incorrectly assert that every finite-type sheaf is coherent.",
  refs=[FAC], correctness="correct with missing hypotheses", area="Sheaf theory")
I(64,"P000106","theorem","The two-out-of-three property for coherent sheaves",
  r"For \(0\to M'\to M\to M''\to0\), coherence of two terms is asserted to imply coherence of the third.",
  r"For an exact sequence of sheaves of modules over a sheaf of rings, if two of \(M',M,M''\) are coherent, then so is the third. Kernels, cokernels, and extensions of coherent modules remain coherent.",
  r"This is the coherent-module property, not the corresponding assertion for arbitrary finite-type modules over arbitrary rings.",
  refs=[FAC], correctness="correct", area="Sheaf theory")
I(64,"P000106","claim","Generators at one stalk generate nearby",
  r"Sections generating the module at \(x\) are said to generate it in a neighbourhood of \(x\).",
  r"If \(M\) is a finite-type sheaf near \(x\), and finitely many sections defined near \(x\) generate \(M_x\), they generate \(M\) on a possibly smaller neighbourhood. Indeed the cokernel of the induced finite free map is of finite type and has zero stalk at \(x\), so it vanishes nearby.",
  r"Finite type of \(M\) must be retained. An arbitrary sheaf can have zero stalk at a point without vanishing on any neighbourhood.",
  refs=[FAC], area="Sheaf theory")

T(66,"1965-10-26","S. I. Gelfand","P000106",
  "The algebraic definition of K-theory",
  r"S. Gelfand introduces the Grothendieck group of projective modules, the splitting of its exact-sequence relations, localization over local rings, and the connection with vector bundles. He also asks what changes if all finite-type modules are used over a ring denoted \(E(X)\), whose exact identity is not explained. This heading precedes the new date 1 November and the Smirnov entry; it is therefore earlier in source order than catalogue record 65.")
I(66,"P000106","definition","K0 from finitely generated projective modules",
  r"The free abelian group on projective modules over a commutative ring \(A\) is divided by the exact-sequence relations \([P]-[P_1]-[P_2]\).",
  r"For a unital ring \(A\), \(K_0(A)\) is generated by isomorphism classes of finitely generated projective \(A\)-modules, subject to \([P]=[P_1]+[P_2]\) for exact sequences \(0\to P_1\to P\to P_2\to0\). Commutativity is needed for the usual vector-bundle interpretation, but not for this additive definition.",
  r"Finite generation and isomorphism classes must be supplied. Allowing all projectives with countable sums permits an Eilenberg swindle: \(Q=\bigoplus_{n\ge0}P\cong P\oplus Q\) would force every \([P]\) to be zero.",
  refs=[RR,"swan1962vector"], match="partial", area="K-theory")
I(66,"P000106","claim","The exact sequences of projectives split",
  r"A parenthesis writes \(P=P_1+P_2\) after the defining relation.",
  r"If \(0\to P_1\to P\to P_2\to0\) is exact and \(P_2\) is projective, the quotient map admits a section, hence \(P\cong P_1\oplus P_2\). Thus \(K_0(A)\) is the group completion of the direct-sum monoid of finitely generated projectives.",
  r"The plus sign means an isomorphism to a direct sum; no canonical splitting is asserted.",
  refs=[RR,"swan1962vector"], match="partial", correctness="correct", area="K-theory")
I(66,"P000106","question","Replacing projectives by all finite-type modules",
  r"The notes ask what happens if one takes \(E(X)\) and all modules of finite type; the ring is not defined.",
  r"A standard comparison, once a ring and exact category are specified, is between \(K_0(A)\) and the Grothendieck group of finitely generated modules, denoted \(G_0(A)\) in the Noetherian setting. For a regular Noetherian ring of finite global dimension, finite projective resolutions identify these groups. This does not identify the unnamed \(E(X)\) or assert equality for it.",
  r"The sheaf-versus-global-ring distinction and the exact class of modules matter. For example \(A=k[\varepsilon]/(\varepsilon^2)\) has \(K_0(A)\cong\mathbb Z\) and \(G_0(A)\cong\mathbb Z\), but the natural map sends \([A]\) to \(2[k]\) and is not an isomorphism.",
  cls="F", correctness="not determinable", match="partial", verification="read the result",
  fate=r"\citet{borelserre1958riemannroch} distinguishes locally free and coherent-sheaf Grothendieck groups and explains the role of resolutions. It does not settle which ring the notebook abbreviation denotes.",
  status="As of 9 November 2026, the standard K0/G0 comparison is established, but the particular question involving E(X) cannot be assigned a unique answer from this entry.",
  refs=[RR], confidence="medium", area="K-theory")
I(66,"P000106","theorem","Projective modules are locally free",
  r"Localization at a prime is said to make a projective module free, and a projective module over a local ring is said to be free.",
  r"If \(A\) is a commutative ring and \(P\) is finitely generated projective, then \(P_{\mathfrak p}\) is free over the local ring \(A_{\mathfrak p}\) for every prime \(\mathfrak p\). Its associated sheaf is locally free of finite rank on \(\operatorname{Spec}A\); conversely every finite-rank locally free sheaf on an affine scheme corresponds to a finitely generated projective module.",
  r"The finite generation required by K0 is retained throughout. Local freeness means a neighbourhood statement, stronger than merely knowing each fibre is a vector space.",
  refs=[RR], match="partial", area="K-theory")
I(66,"P000106","theorem","Vector bundles and projective modules of continuous functions",
  r"The topological interpretation refers to locally trivial bundles and the sheaf of continuous functions.",
  r"For a compact Hausdorff space \(X\), global sections give an equivalence between finite-rank complex vector bundles on \(X\) and finitely generated projective modules over \(C(X,\mathbb C)\). The real version uses real bundles and real continuous functions.",
  r"Compactness and the global section ring are supplied for the Serre--Swan formulation. The notes themselves mention a sheaf of rings and do not assert this equivalence for every noncompact space and every finiteness convention.",
  fate=r"This is the established correspondence of \citet{swan1962vector}, whose bibliographic identity was checked against Swan's own bibliography.",
  refs=["swan1962vector"], match="partial", verification="indirect", area="K-theory")
C("P000106","definition of K0",
  "projective modules, with no finiteness qualification",
  "isomorphism classes of finitely generated projective modules",
  "The finiteness word is absent in the scan. The standard K0 definition needs it; otherwise countable direct sums give the displayed Eilenberg-swindle collapse. This is an omitted hypothesis in the notes.")

T(67,"1965-11-01","S. V. Smirnov","P000106",
  "Extreme positive-definite functions on nilpotent groups",
  r"The three-line entry asks for extreme points among positive-definite functions on groups obtained from nilpotent algebras by the Campbell--Hausdorff formula. It does not state the field, topology, normalization, or centrality condition. Smirnov's 1966 paper is a strong contemporaneous lead, received on 3 December 1965, but it treats normalized central positive-definite functions over a discrete field of characteristic zero. That restriction prevents an exact identification of the unrestricted notebook question \citep{smirnov1966positive}. The earlier normalized-central-function topic 1964-13.1 is thematically related; the missing centrality here prevents identifying the two questions.")
I(67,"P000106","construction","The Campbell-Hausdorff nilpotent group",
  r"The groups are obtained from a nilpotent algebra by introducing multiplication with the Campbell--Hausdorff formula.",
  r"For a finite-dimensional nilpotent Lie algebra \(\mathfrak n\) over a field of characteristic zero, the Baker--Campbell--Hausdorff series terminates and defines a polynomial associative group law on the underlying affine space, with identity zero and inverse \(X\mapsto-X\). Over \(\mathbb R\), this is the simply connected nilpotent Lie group in exponential coordinates.",
  r"The algebra must be a Lie algebra and the characteristic condition ensures the rational coefficients are defined. A topology must be chosen separately if continuity of representations is intended.",
  fate=r"This is pre-existing nilpotent-group structure, already underlying \citet{kirillov1962unitary}; \citet{smirnov1966positive} uses the algebraic discrete-field version.",
  refs=["kirillov1962unitary","smirnov1966positive"], match="partial", verification="indirect",
  area="Representation theory")
I(67,"P000106","question","Which convex set of positive-definite functions is intended?",
  r"The notes ask to describe extreme points of positive-definite functions; the parenthesis is the abbreviation \ru{непр. предст.}. The English text expands this as continuous representations.",
  r"A positive-definite function satisfies \(\sum_{j,k}c_j\overline{c_k}\varphi(g_k^{-1}g_j)\ge0\). To ask for nontrivial extreme points one normally fixes \(\varphi(e)=1\). Extremes of all normalized positive-definite functions concern pure states and irreducible cyclic representations; extremes of the normalized central subset instead concern factor characters. The notebook does not determine which set, field, or topology is intended.",
  r"The Russian abbreviation can mean continuous or irreducible and must remain unresolved. Centrality cannot be supplied solely because the later paper needs it. Without normalization, the positive-definite cone has no nonzero extreme points as a convex set, since \(\varphi=\tfrac12(0+2\varphi)\).",
  cls="F", correctness="not determinable", match="partial", verification="read the result",
  fate=r"\citet{smirnov1966positive} classifies normalized central positive-definite functions for nilpotent algebraic groups over discrete characteristic-zero fields. Its extremals are obtained from central characters of algebraic quotients, extended by zero outside the preimage of the quotient centre, with the paper's nontriviality condition on algebraic one-parameter central subgroups. This is a precise partial match, not a solution of the broader unspecified question.",
  status="As of 9 November 2026, the 1966 original theorem has been read and its central-class restriction verified. The notebook question remains underdetermined; it is not classified as an unresolved modern research problem.",
  refs=["smirnov1966positive"], confidence="medium", area="Representation theory")
C("P000106","Smirnov's parenthesis",
  "cont. representations",
  r"retain \ru{непр. предст.}; continuous representations / irreducible representations are both possible expansions",
  "The scan has only the abbreviated Russian phrase. The English expansion selects one meaning without sufficient evidence; the nearby extreme-point question makes irreducibility a live alternative. The later central-character paper does not uniquely disambiguate the notebook.",
  applies="en")

T(65,"1965-11-01","I. M. Gelfand","P000106-P000107",
  "The fixed-point trace and its real and complex applications",
  r"After Smirnov's entry, Gelfand returns to Atiyah. He computes the delta-kernel trace with a Jacobian denominator, repeats the finite-complex trace lemma, and applies the formula to de Rham theory, complex structures, and projective transformations. The real de Rham calculation is identifiable; the complex-case notation and factors are too compressed to recover a unique asserted formula. The local inverse-map and ordinary-map conventions also conflict \citep{atiyahbott1964notes}.")
I(65,"P000106","construction","The weighted delta-kernel fixed-point trace",
  r"The operator first uses \(s(f^{-1}(x))\), but its kernel then uses \(\delta(y-f(x))\); the trace is a sum with denominator \(|1-J_\rho(f)|\).",
  r"With \(Ts(x)=\phi(x)s(f(x))\), nondegenerate fixed points give \(\operatorname{tr}^{\,b}T=\sum_{p=f(p)}\operatorname{tr}\phi(p)/|\det_{\mathbb R}(I-df_p)|\). If instead \(Ts(x)=\phi(x)s(f^{-1}(x))\), replace \(f\) by \(f^{-1}\) consistently and assume it is a diffeomorphism.",
  r"The denominator bars stand for an absolute determinant in dimensions greater than one. Keeping the initial inverse while retaining the later ordinary-map kernel changes the operator and generally its local weight.",
  refs=[AB], correctness="false as written", match="partial", area="Distribution theory")
I(65,"P000106-P000107","theorem","The finite-complex trace lemma repeated",
  r"The notes again define \(H^i=\ker d/\operatorname{im}d\), require that \(T\) commute with \(d\), and equate the two alternating traces.",
  r"For a bounded complex of finite-dimensional vector spaces and a chain endomorphism \(T\), \(\sum_i(-1)^i\operatorname{tr}T_i=\sum_i(-1)^i\operatorname{tr}H^i(T)\). The Euler-characteristic identity is the specialization \(T=\operatorname{id}\).",
  r"The words finite analogue on P000107 supply the intended scope; the formula is not an ordinary-trace identity for the unsmoothed infinite-dimensional section complex.",
  refs=[AB], correctness="correct", area="Homological algebra")
I(65,"P000107","claim","Exterior-power traces give the de Rham numerator",
  r"The local trace calculation is abbreviated as \(\operatorname{tr}\varphi_i=\operatorname{det}-1\), followed by eigenvalue products with alternating signs.",
  r"For any endomorphism \(A\) of a finite-dimensional vector space, \(\sum_{q=0}^n(-1)^q\operatorname{tr}(\Lambda^q A)=\det(I-A)\). With \(A=(df_p)^*\), this is the de Rham fibre supertrace.",
  r"An individual degree trace is not the determinant. The sum over degrees and the determinant argument must be restored; the identity holds without diagonalizability, by polynomial continuity or triangularization.",
  refs=[AB], correctness="false as written", match="partial", area="Linear algebra")
I(65,"P000107","theorem","Recovery of the ordinary Lefschetz formula",
  r"The first application gives the usual Lefschetz number as the sum of fixed-point multiplicities, written as a sum of signs.",
  r"For a smooth self-map of a closed compact real manifold with only nondegenerate fixed points, the de Rham pullback has \(L(f)=\sum_q(-1)^q\operatorname{tr}(f^*|H^q_{\mathrm{dR}}(X))=\sum_{p=f(p)}\operatorname{sgn}\det(I-df_p)\).",
  r"The numerator from exterior powers cancels the absolute determinant in the denominator, leaving the local index. At degenerate isolated fixed points the index is still defined, but is not given by this determinant-sign expression.",
  refs=[AB], correctness="correct with missing hypotheses", area="Differential topology")
I(65,"P000107","claim","The unresolved complex-case specialization",
  r"The complex case mentions holomorphic forms and \(H^{i,0}\), then displays \(|1-J(f)|^2\) in a denominator, \(2\operatorname{Re}(1/(1-J_f))\), and an uncertain conjugate average.",
  r"No single equality is determined by these lines. For comparison, the standard holomorphic Lefschetz formula for a holomorphic bundle \(E\) on a compact complex manifold and a nondegenerate holomorphic map with a bundle lift is \(\sum_q(-1)^q\operatorname{tr}(H^q(T):H^q(X,E)\to H^q(X,E))=\sum_p\operatorname{tr}\phi_p/\det_{\mathbb C}(I-df_p)\).",
  r"The Dolbeault degree, the bundle being resolved, the meaning of the realification, and the factor in the final average are missing or inconsistent. The displayed comparison formula is not attributed verbatim to the notebook.",
  cls="F", correctness="not determinable", match="partial", verification="read the result",
  fate=r"The relevant holomorphic specialization is part of \citet{atiyahbott1964notes}, but this does not uniquely repair the source's bidegrees and factors.",
  status="As of 9 November 2026, the holomorphic fixed-point formula is established; the precise complex-case formula intended on this page is not recoverable with confidence.",
  refs=[AB], confidence="low", area="Complex geometry")
I(65,"P000107","claim","Real and complex traces and determinants",
  r"The last sentence of the complex calculation says that the real trace is the sum of the complex trace and its conjugate; the drawing records \(|a|^2\) for multiplication by \(a\).",
  r"For a complex-linear map \(A\), its underlying real map satisfies \(\operatorname{tr}_{\mathbb R}A=2\operatorname{Re}\operatorname{tr}_{\mathbb C}A\) and \(\det_{\mathbb R}A=|\det_{\mathbb C}A|^2\). Thus \(\operatorname{Re}z=(z+\bar z)/2\), whereas the realified trace is the sum, without the factor one-half.",
  r"These exact linear-algebra identities clarify the different factors, but do not choose which real or complex Lefschetz number was intended in the preceding unfinished calculation.",
  refs=[AB], correctness="correct", match="partial", area="Linear algebra")
I(65,"P000107","remark","Projective transformations and eigenlines",
  r"Fractional-linear transformations of projective space are named as an application.",
  r"If \(A\in GL_{n+1}(\mathbb C)\), fixed points of its projective action on \(\mathbb P^n\) are its invariant lines. For distinct eigenvalues these are \(n+1\) nondegenerate fixed points. The projective transformation acts trivially on \(H^{2q}(\mathbb P^n;\mathbb C)\), so its ordinary Lefschetz number is \(n+1\). Existence of an eigenline holds without the distinct-eigenvalue assumption.",
  r"The generic nondegeneracy condition allows direct use of the local formula; repeated eigenvalues require a limiting or ordinary topological fixed-point argument. The notes do not record a formula for a specified transformation.",
  refs=[AB], match="partial", area="Projective geometry")
C("P000106","operator, kernel, and local-trace formula in record 65",
  r"\(\phi(x)s(f^{-1}(x))\), then \(\phi(x)\delta(y-f(x))\), then denominator \(|1-J_\rho(f)|\)",
  r"make the same choice of \(f\) or \(f^{-1}\) in both operator and kernel, and write \(|\det_{\mathbb R}(I-df_\rho)|\) for the forward convention",
  "All three notations are visible in the scan. The inverse-map mismatch is genuine; the missing determinant notation is shorthand at best. This is an annotated mathematical normalization, not a unique claim about the scribe's intended convention.")
C("P000107","de Rham local numerator",
  r"\(\operatorname{tr}\varphi_i(\rho)=\operatorname{det}-1\)",
  r"\(\sum_i(-1)^i\operatorname{tr}(\Lambda^i(df_\rho)^*)=\det(I-df_\rho)\)",
  "The scan leaves the determinant argument incomplete and the alternating sum is absent in this line. The following eigenvalue-products line and the final signs determine the standard supertrace identity, not an individual-degree equality.")
C("P000107","conjugate-average formula",
  r"\(2\operatorname{Re}(1/(1-J_f))\) followed by an uncertain factor \(1/[?]\) times the conjugate sum",
  "retain the uncertain handwritten denominator; distinguish Re(z)=(z+conjugate(z))/2 from the realified trace z+conjugate(z)",
  "The active numerator 2 is clear, but the later prefactor denominator remains visually uncertain. The scan supports an ambiguity report, not a confident one-character transcription correction.")

T(68,"1965-11-01","D. A. Kazhdan","P000107-P000108",
  "Injectives and right derived functors",
  r"Kazhdan defines injective objects and enough injectives, then constructs right derived functors of a left exact covariant functor through their long exact sequence, vanishing on injectives, and naturality. The final square and existence statement occupy the top of P000108 before Matsaev's new dated heading. This resumes the homological-algebra material already indexed as 1964-49.8; it is not a new open problem \citep{grothendieck1957homological}.")
I(68,"P000107","definition","Injective objects and the extension property",
  r"An object \(Q\) is called injective when \(\operatorname{Hom}(-,Q)\) is exact; a diagram expresses extension of a morphism from a subobject.",
  r"In an abelian category \(\mathcal A\), \(Q\) is injective if every map \(A'\to Q\) extends across every monomorphism \(A'\hookrightarrow A\). Equivalently the contravariant functor \(\operatorname{Hom}_{\mathcal A}(-,Q)\) sends each short exact sequence to an exact sequence \(0\to\operatorname{Hom}(A'',Q)\to\operatorname{Hom}(A,Q)\to\operatorname{Hom}(A',Q)\to0\).",
  r"The variance reverses the order of the sequence. The left exactness of Hom is automatic; surjectivity of the last map is the injectivity condition.",
  refs=[TA], verification="publisher metadata checked", correctness="correct", area="Homological algebra")
I(68,"P000107","definition","Enough injectives",
  r"The category is said to have enough injectives if every object embeds into an injective; sheaves are given as the example.",
  r"An abelian category has enough injectives if for each \(A\) there is a monomorphism \(A\hookrightarrow Q\) with \(Q\) injective. The categories of sheaves of abelian groups, and of modules over a sheaf of unital rings on a space, have enough injectives.",
  r"The sheaf example concerns the abelian module category, not the category of coherent sheaves by itself, which usually does not have enough injective objects within that subcategory.",
  refs=[TA], verification="publisher metadata checked", correctness="correct with missing hypotheses",
  area="Homological algebra")
I(68,"P000107","construction","Right derived functors of a left exact functor",
  r"A covariant left exact functor is introduced and its derived functors are required to start with \(F^0=F\).",
  r"If \(\mathcal A,\mathcal B\) are abelian categories, \(\mathcal A\) has enough injectives, and \(F:\mathcal A\to\mathcal B\) is additive and left exact, choose an injective resolution \(A\to I^\bullet\) and define \(R^iF(A)=H^i(F(I^\bullet))\). Comparison maps make the result functorial and independent up to canonical isomorphism of the resolution.",
  r"Additivity is made explicit. The superscript denotes right derived functors of a covariant left exact functor, despite the notebook heading's generic use of homology.",
  refs=[TA], verification="publisher metadata checked", area="Homological algebra")
I(68,"P000107","theorem","The long exact sequence of derived functors",
  r"For \(0\to A\to B\to C\to0\), the notes display the beginning of the long exact sequence; the last visible arrow after \(F^1(B)\) is labelled \(\delta\).",
  r"Each short exact sequence gives \(0\to F(A)\to F(B)\to F(C)\xrightarrow{\delta^0}R^1F(A)\to R^1F(B)\to R^1F(C)\xrightarrow{\delta^1}R^2F(A)\to\cdots\). Connecting maps go from \(R^iF(C)\) to \(R^{i+1}F(A)\).",
  r"The arrow \(R^1F(B)\to R^1F(C)\) is induced by \(B\to C\), not a connecting map. The missing term beyond the frame is not treated as legible source text.",
  refs=[TA], verification="publisher metadata checked", correctness="false as written",
  area="Homological algebra")
I(68,"P000108","claim","Naturality of the connecting maps",
  r"The two short exact sequences are related by a map, and a square is drawn with \(F^0(A)\) at its upper left but \(F^0(C')\) at its lower left; the vertical arrows point upward.",
  r"For a morphism of short exact sequences from \(0\to A\to B\to C\to0\) to \(0\to A'\to B'\to C'\to0\), naturality says \(R^{i+1}F(A\to A')\,\delta^i=\delta'^i\,R^iF(C\to C')\). The square has \(R^iF(C)\) and \(R^{i+1}F(A)\) in its top row and the primed counterparts below, with downward induced arrows.",
  r"The original square's upper-left letter and the direction of its arrows disagree with the stated morphism of sequences. The modern square is a correction, not a claim that the handwritten A was C.",
  refs=[TA], verification="publisher metadata checked", correctness="false as written",
  area="Homological algebra")
I(68,"P000107-P000108","theorem","Existence and uniqueness through effaceable delta-functors",
  r"The conditions include vanishing \(F^i(Q)=0\) for injectives and a final theorem that the derived functors exist and are unique when there are enough injectives.",
  r"The right derived functors form a cohomological \(\delta\)-functor with \(R^0F=F\), natural connecting maps, and \(R^iF(Q)=0\) for injective \(Q\), \(i>0\). Because every object embeds into an injective, the positive-degree functors are effaceable; hence this \(\delta\)-functor is universal and unique up to the unique isomorphism extending the identity of \(F\).",
  r"Uniqueness concerns the compatible system of functors and connecting maps. A list of groups with unrelated long exact sequences would not supply the required naturality or universal property.",
  refs=[TA], verification="publisher metadata checked", area="Homological algebra")
C("P000107","last visible arrow in the long exact sequence",
  r"\(F^1(B)\xrightarrow{\delta}\cdots\)",
  r"\(R^1F(B)\to R^1F(C)\xrightarrow{\delta^1}R^2F(A)\)",
  "The scan visibly places delta over the arrow immediately after F^1(B), at the edge of the image. Its next term is not visible. The correction gives the standard continuation and locates the genuine connecting arrow, without claiming the missing term was read.")
C("P000108","naturality square",
  r"upper-left \(F^0(A)\); vertical arrows point upward",
  r"upper-left \(F^0(C)\); for the displayed downward morphism of short exact sequences, both induced vertical arrows point downward",
  "The two sloping strokes and crossbar of handwritten A are clear, and the arrowheads are genuinely upward. The correction is mathematical: covariant functoriality and the source of the connecting map determine the proper square.")

# Within shared pages, use the first handwritten occurrence of each topic.
source_permutations = {63:[2,1,3,4,5,6,7,8], 66:[1,2,3,5,4], 65:[1,2,4,3,5,6,7]}
ordered_items = []
for talk in talks:
    group = [item for item in items if item["record"] == talk["record"]]
    permutation = source_permutations.get(talk["record"])
    if permutation:
        assert sorted(permutation) == list(range(1,len(group)+1))
        group = [group[n-1] for n in permutation]
    for n, item in enumerate(group,1):
        item["id"] = f"1965-{talk['record']}.{n}"
    ordered_items.extend(group)
items[:] = ordered_items

# These are elementary checks or proof completions carried out for this
# companion, not claims of mathematical novelty.
proved_here = {
    "The boundary estimate and its limitations",
    "The de Rham symbol is an exact Koszul complex",
    "Elliptic operators beyond differential operators",
    "Finiteness of elliptic-complex cohomology",
    "Affine algebraic sets and their coordinate rings",
    "The punctured affine plane is not affine",
    "The Zariski topology on a product is not the product topology",
    "The affine line with doubled origin",
    "Acyclicity and the invalid shifted-Laplacian shortcut",
    "The weighted trace series and its half-plane of convergence",
    "The finite-dimensional trace lemma by splitting cycles and boundaries",
    "Coherence requires finite relations for every finite local tuple",
    "Generators at one stalk generate nearby",
    "K0 from finitely generated projective modules",
    "The exact sequences of projectives split",
    "Replacing projectives by all finite-type modules",
    "Which convex set of positive-definite functions is intended?",
    "Exterior-power traces give the de Rham numerator",
}
computed_here = {
    "Complete surfaces need not satisfy the closed Gauss-Bonnet equality",
    "The circle model and the Laplacian sign",
    "The delta trace is a weighted fixed-point sum",
}
for item in items:
    if item["title"] in proved_here:
        item["reconstruction"] = r"\ours\ " + item["reconstruction"]
    if item["title"] in computed_here:
        item["reconstruction"] = r"\oursComputed\ " + item["reconstruction"]

problems.append(dict(
  id="GP-1965-E01", title="Solving d-bar globally to construct a holomorphic boundary singularity",
  statement=r"For a bounded \(C^\infty\) strongly pseudoconvex domain \(\Omega\subset\mathbb C^n\), solve \(\bar\partial u=\alpha\) with smooth dependence and regularity up to the boundary for every smooth closed \((0,1)\)-form, and use this to construct, at each boundary point, a holomorphic function that does not extend across that point.",
  occurrences=["1965-53.1","1965-53.4"],
  status=r"As of 9 November 2026, this precise strongly pseudoconvex version was already solved before the seminar \citep{kohn1963potential,kohn1963harmonic,kohn1964harmonic}. No claim of a new unresolved Levi problem is made.",
  status_date="2026-11", refs=[KOHN,"kohn1963harmonic","kohn1964harmonic"]))

checkpoint()
if __name__ == "__main__":
    print(json.dumps({"talks":len(talks),"items":len(items),"classes":dict(Counter(i["class"] for i in items)),
                      "corrections":len(corrections),"problems":len(problems),
                      "source_order":[t["record"] for t in talks]}, ensure_ascii=False))
