# Carry-out inventory: P000917–P000918

**Scope decision.** These pages are supplied in the envelope for catalog record 488, but their original headings place them in the next academic year. P000917 begins **22 September 1980**, with **D. B. Fuchs** on intersection homology. P000918 first continues the Deligne sentence from P000917, then names **M. I. Graev** and turns to integral geometry. There is no second date on P000918; assignment of Graev's contribution to the same 22 September session is a continuity inference, not a separately written date. Neither page belongs to V. E. Zakharov's 18 February 1980 session, which occupies P000915–P000916.

Both Russian and English supplied transcriptions were read, and both original PNGs were inspected on 10 November 2026. The items below preserve all distinct mathematical content without creating spurious `1979-488.n` occurrences or adding records to the 27-record catalog. The labels B01–B12 are local inventory labels, not permanent problem or occurrence IDs. All modern qualifications are editorial reconstruction, clearly separated from what the notes say.

## Fuchs: intersection homology (P000917; continuation at top of P000918)

### B01. A stratification of a singular complex algebraic space

**Notes.** The space is complex algebraic, of real dimension \(2n\), with a filtration beginning \(X=X_{2n}\supset X_{2n-2}\supset X_{n-3}\supset X_{n-4}\supset\cdots\). The differences \(X_i\setminus X_{i-1}\) are said to be \(i\)-dimensional manifolds, with locally uniform geometry along a stratum.

**Precise reconstruction.** Use a locally conically trivial stratified pseudomanifold of pure real dimension \(2n\), with a compatible filtration by closed sets of dimension at most their subscript and no codimension-one singular stratum. For a complex algebraic variety one can choose an algebraic/Whitney stratification with even-dimensional strata. Local conical triviality is stronger than merely saying each difference is smooth.

**Correction.** The change from subscripts \(2n-2\) to \(n-3,n-4\) is visible in the scan and is a faithful indexing error. A consistent real-dimensional filtration uses \(X_{2n-i}\); odd levels may repeat in the complex-algebraic case. This is a mathematical emendation, not a claim of OCR failure.

**Fate and evidence.** Expository by September 1980. Goresky and MacPherson (1980), §1, supplies the stratified-pseudomanifold framework; the 1977 announcement already introduced the invariant. Full primary sources were read: [1977 announcement](https://www.math.ias.edu/~goresky/pdf/IH0.pdf), [1980 article](https://www.math.ias.edu/~goresky/pdf/IH.pdf). Bibliography keys: `goreskymacpherson1977dualite`, `goreskymacpherson1980intersection`.

### B02. Allowable chains and Poincaré duality

**Notes.** The formula is literally \(\dim(\sigma_j\cap X_{2n-i})=j-2i\), followed by the statement that these chains give another homology/cohomology theory with Poincaré duality.

**Precise reconstruction.** For a perversity \(\bar p\), require the support of a \(j\)-chain \(c\), and separately its boundary, to satisfy


\[
\dim(|c|\cap X_{2n-i})\le j-i+\bar p(i),\qquad
\dim(|\partial c|\cap X_{2n-i})\le j-1-i+\bar p(i).
\]

For lower middle perversity \(\bar m(i)=\lfloor(i-2)/2\rfloor\), a stratum of complex codimension \(c\) gives the upper bound \(j-c-1\). For a compact oriented pseudomanifold, complementary perversities pair over a field. On a complex-algebraic even-stratum space the middle choice is self-dual, giving rational middle-perversity duality.

**Correction.** Equality, the displayed codimension coefficient, and omission of the boundary condition are all mathematically consequential. The scan confirms the equality sign; silently treating it as a transcription of the correct inequality would be inaccurate.

**Fate.** Established before this talk, not a 1980 conjecture. Exact source: Goresky and MacPherson (1977), definition and duality theorem; (1980), §§1.1, 1.3, 3.3. The general integral-coefficient statement needs qualifications and is not inferred from the integer example below.

### B03. Two 2-spheres meeting at a point

**Notes.** The example is \(X=S^2\vee S^2\), drawn as two tangent circles representing the spheres. Ordinary groups in degrees \(0,1,2\) are written \(\mathbb Z,0,\mathbb Z^2\); “MacPherson homology” gives \(\mathbb Z^2,0,\mathbb Z^2\). A one-simplex crossing the meeting point is explicitly forbidden.

**Precise reconstruction.** Stratify the meeting point as a codimension-two singularity and take middle perversity \(\bar m(2)=0\). Allowable zero- and one-chains avoid that point; allowable two-cycles supply one fundamental class from each sphere. Consequently


\[
IH_0^{\bar m}(X;\mathbb Z)=\mathbb Z^2,
\quad IH_1^{\bar m}(X;\mathbb Z)=0,
\quad IH_2^{\bar m}(X;\mathbb Z)=\mathbb Z^2.
\]

This is the intersection homology of the disconnected normalization. The listed ordinary groups are also correct. The picture concerns a singular two-dimensional space, not a smooth connected manifold.

**Fate.** Correct elementary illustration of the already established theory. Directly checked from the allowable-chain definition, using the 1980 paper's chain conditions. No later research problem is introduced.

### B04. Intersection homology is not an ordinary homotopy invariant

**Notes.** The line is explicit: these homology groups are “not homotopy invariant.”

**Precise reconstruction.** Intersection homology is invariant under the appropriate homeomorphisms/stratified equivalences, but not under arbitrary ordinary homotopy equivalences. A homotopy may move chains through a singular stratum without respecting allowability. This statement does not mean that every homotopy-invariance result fails; controlled or stratum-preserving hypotheses matter.

**Fate.** Expository, with exact topological-invariance distinctions in Goresky and MacPherson (1980), introductory discussion and §3.2. The sphere example distinguishes ordinary and intersection homology; it alone is not a demonstration that two homotopy-equivalent spaces have different intersection homology.

### B05. The proposed comparison with \(L^2\) cohomology

**Notes.** “Conjecture: [these groups] coincide with \(L_2\)-cohomology,” with Borel's interest noted. No metric, domain of the differential, compactification or class of singular spaces is specified.

**Precise reconstruction and identification limits.** An \(L^2\) comparison must specify the regular locus's metric, coefficients, domain or extension of \(d\), and whether cohomology is reduced. These choices cannot be reconstructed uniquely from this sentence. One important later precise theorem is the Zucker comparison: for an arithmetic quotient of a Hermitian symmetric domain with its invariant metric and an appropriate finite-dimensional coefficient local system, the \(L^2\) de Rham complex represents the intersection complex on the Baily–Borel compactification. This is a **partial**, explicitly scoped match, not a resolution of every possible reading of the notebook sentence.

**Fate through 10 November 2026.** Looijenga announced the arithmetic result in February 1987 and published it in 1988; Saper and Stern independently announced it in February 1987 and published their full proof in 1990. The exact theorem and hypotheses were read in [Looijenga's primary article](https://www.numdam.org/item/CM_1988__67_1_3_0.pdf), pp. 3–4. [Saper–Stern's publisher record](https://annals.math.princeton.edu/1990/132-1/p01) confirms publication metadata; that full proof was not read. Keys: `looijenga1988l2`, `saperstern1990l2`.

The contemporaneous Cheeger–Goresky–MacPherson comparison programme is separately listed on [Goresky's own publication page](https://www.math.ias.edu/~goresky/MathPubl.html), under 1980, with a later seminar-volume publication. Its [primary PDF](https://www.math.ias.edu/~goresky/pdf/CGM.pdf) was opened, but its text/proof could not be inspected sufficiently in this pass. It is recorded as a lead, not used as a verified general theorem. A chapter for 1980–81 should disambiguate the metric convention before assigning a definite problem identity or an open/closed status.

### B06. Isolated singularities and Deligne's inductive construction

**Notes.** For one isolated singularity, degrees above half the dimension agree with ordinary groups, while degrees below half follow by Poincaré duality. The middle degree is omitted. The last line attributes this to Deligne, and the first line of P000918 adds that the general definition is inductive.

**Precise reconstruction.** For a compact oriented real \(2n\)-dimensional pseudomanifold with isolated conical singularities and field coefficients, let \(U\) be the regular locus. In homological notation,


\[
IH_i^{\bar m}(X)=
\begin{cases}
H_i(U),&i<n,\\
\operatorname{im}(H_n(U)\longrightarrow H_n(X)),&i=n,\\
H_i(X),&i>n.
\end{cases}
\]

The cohomological version is obtained by duality over the coefficient field. Deligne's sheaf construction extends the local system from the regular stratum by successive derived direct images and perversity-dependent truncations. Stating only the strict inequalities leaves an essential middle-degree datum missing.

**Fate and verification.** The original chain theory was already available in 1977/1980. The sheaf treatment appears in Goresky and MacPherson, *Intersection homology II* (1983). The [author's primary history](https://www.math.ias.edu/~goresky/MathPubl.html) records Deligne's 1976 proposal, wide manuscript circulation in 1979–1980, submission in October 1981, loss in the mail, resubmission in June 1982, and publication in February 1983. Thus the publication year is not the first-circulation year. The [primary 1983 PDF](https://www.math.ias.edu/~goresky/pdf/IH2.pdf) was opened, but the original proof was not read; the formula displayed here is explicitly editorial reconstruction. Key: `goreskymacpherson1983intersection`.

## Graev: local integral geometry of curves (P000918)

### B07. Weighted curve integrals and the parameter count

**Notes.** \(D\subset\mathbb R^n\), an \(n+k-1\)-parameter family of curves, equations \(x_i=\varphi_i(x_1,\xi)\), positive weight \(\chi\), and \(F=I_\chi f\). The displayed argument list is \(f(x_1,\varphi_1,\ldots,\varphi_n)\), inconsistent with \(f\) on \(\mathbb R^n\). The parameter vector is first given \(n\) entries and then corrected below to \(n+k-1\).

**Precise reconstruction.** Locally where \(x_1\) parametrizes the curves,


\[
F(\xi)=I_\chi f(\xi)=\int
 f(x_1,\varphi_2(x_1,\xi),\ldots,\varphi_n(x_1,\xi))
 \chi(x_1,\xi)\,dx_1,
\quad f\in C_c^\infty(D),\quad \xi\in\Gamma^{n+k-1}.
\]

The graph needs \(n-1\) coordinate functions, indexed \(2,\ldots,n\). Smoothness, support and a nonvanishing density belong to the setup. Positivity is a convenient real convention; complex analogues require a different integration interpretation.

**Fate and evidence.** Exact framework in Gelfand, Gindikin and Shapiro (1979), §1.1, and Gelfand and Graev (1980), §1, Eqs. (1)–(4). Both full Russian originals were read through MathNet: [1979 primary record](https://www.mathnet.ru/eng/faa1896), [1980 primary record](https://www.mathnet.ru/eng/faa1851). Keys: `gelfandgindikinshapiro1979local`, `gelfandgraev1980admissible`.

### B08. Local inversion and admissible families

**Notes.** Find families for which an inversion formula uses curves through a given point, or curves infinitesimally close to it. Such families are called admissible.

**Precise reconstruction.** The local problem seeks differential forms in parameter space obtained from the transform and a finite number of transverse derivatives, whose periods isolate \(f(x^0)\). Nonzero reconstruction periods must be distinguished from closed-form identities that only characterize the range. The notes begin in the real setting; that qualification changes the result.

**Fate.** The 1979 paper's introduction and §1 explicitly say that its real curve construction gives closed one-forms whose relevant periods vanish; genuine nonzero local inversion is obtained in the complex version (§3). The 1980 paper, §2 following Definition 1, repeats the same warning. Its Theorems 1–4 classify local admissible \(n\)-parameter curve complexes near regular incidence points and construct admissible densities/operators. Consequently “admissible” in the technical real definition is not by itself a theorem of real local inversion. The blanket implication suggested by the seminar shorthand would be false without this qualification. Exact result read, with its restrictions; no broad modern inverse-problem status is inferred.

### B09. The \(k\)-dimensional incidence fiber through a point

**Notes.** For \(x^0\in D\), \(\Gamma_{x^0}\) is defined by the incidence equations and is said to have dimension \(k\).

**Precise reconstruction.** Let


\[
\Gamma_{x^0}=\{\xi:\varphi_i(x_1^0,\xi)=x_i^0, i=2,\ldots,n\}.
\]

If these \(n-1\) equations have independent parameter gradients, the implicit-function theorem gives \(\dim\Gamma_{x^0}=(n+k-1)-(n-1)=k\). The claim need not hold at singular incidence points or for a redundant family.

**Fate.** Elementary, and the exact regularity/rank condition is explicit in Gelfand and Graev (1980), §1. The notebook dimension is correct under this missing hypothesis.

### B10. First-order operators producing closed one-forms

**Notes.** For each point, an operator \(\mathcal H_{x^0}\) sends \(F\) to a one-form on \(\Gamma_{x^0}\), of the form


\[
\mathcal H_{x^0}F
=\sum_{i,j}a_{ij}(x_1^0,\xi)\partial_{\xi_j}F\,d\xi_i
 +F\sum_i b_i(x_1^0,\xi)\,d\xi_i.
\]

Admissibility is phrased as closedness for every \(F=I_\chi f\), and the notes say that for \(k>1\) this is the complete definition.

**Precise reconstruction.** The differential one-form is restricted to the incidence fiber; coefficients may depend smoothly on the incidence pair. Closedness is a nontrivial differential identity when the fiber has dimension greater than one. In the original paper, admissibility also includes a locality/period requirement. The implication from closedness to that requirement is justified under sufficient size/general-position hypotheses, not from the integer inequality \(k>1\) alone for every arbitrary family.

**Fate.** Gelfand–Gindikin–Shapiro (1979), §1.2–1.4, defines the operators and both conditions; its remark on p. 14 explains when closedness implies locality, and Theorem 1 classifies the first-order admissible operators. The full result was read. The note's “complete” definition needs those qualifications.

### B11. The exceptional one-dimensional fiber case

**Notes.** For \(k=1\), every one-form is closed, so require the functional \(f\mapsto\int\mathcal H_{x^0}I_\chi f\) to be supported at \(x^0\).

**Precise reconstruction.** Integrate along an appropriate closed cycle of the one-dimensional incidence fiber (or impose stated endpoint conditions). The resulting functional must vanish whenever \(f\) vanishes near \(x^0\). For a general distribution, point support alone allows derivatives of a delta; additional structure is needed to conclude a multiple of evaluation \(f(x^0)\). The cited framework supplies that stronger conclusion. A nonzero coefficient is separately needed for inversion.

**Fate.** Exact definition in Gelfand and Graev (1980), §2, Definition 1 and following remark. The article again warns that the real curve-case coefficient is zero. Thus the notebook correctly notices why closedness alone is vacuous for \(k=1\), but does not state all conditions needed for a usable inversion formula.

### B12. Trivial operators and the nontrivial quotient

**Notes.** A trivial operator is \(\mathcal H_{x^0}F=d(\mu F)\), and the text says the quotient by trivial operators matters.

**Precise reconstruction.** The expression is exact on the incidence fiber, so its integral over every closed cycle vanishes. Such operators satisfy the formal closedness requirement for every \(F\), without using that \(F\) lies in the transform's range. A meaningful classification therefore factors out these operators and requires a nonzero class; taking \(\mathcal H=0\) cannot establish admissibility in the substantive sense.

**Fate.** Exact in Gelfand–Gindikin–Shapiro (1979), §1.3, Eq. (4), and in Gelfand–Graev (1980), §2, Definition 2. Both primary results read. This is part of the solved local first-order classification, not an additional open problem posed in the fragment.

## Bibliographic and provenance corrections to carry forward

1. The first P000918 reference, *Functional Analysis* **13:2**, is Gelfand–Gindikin–Shapiro, *A local problem of integral geometry in a space of curves* (1979), Russian pp. 11–31 / English pp. 87–102, received 25 December 1978, DOI [10.1007/BF01077241](https://doi.org/10.1007/BF01077241).
2. The second, **14:4**, is **Gelfand–Graev**, *Admissible n-dimensional complexes of curves in Rn* (1980), Russian pp. 36–44 / English pp. 274–281, received 16 June 1980, DOI [10.1007/BF01078303](https://doi.org/10.1007/BF01078303). The scan's shorthand joins the references under the earlier author trio; this is an attribution correction. The article was already submitted before 22 September; exact issue-release day was not verified.
3. The real/complex local-inversion distinction is essential and explicitly supported by both originals. It is not an optional later refinement.
4. These corrections are documented here, rather than silently attaching September material to record 488. The main corrections CSV contains both the page-boundary correction and the specific mathematical and attribution corrections inventoried here.

## Verification ledger

| Source | What was actually checked | Supported use |
|---|---|---|
| Original P000917/P000918 PNGs; supplied Russian and English | Complete text, diagrams, equations and headings | Date/speaker boundary; faithful errors; full inventory |
| Goresky–MacPherson 1977 and 1980 | Full primary text and named definitions/theorems | Allowability, duality, topology; direct check of sphere example |
| Goresky author's publication history; IH II PDF | History read; PDF opened but proof not read | 1976/1979–1980/1983 chronology, not proof verification |
| Cheeger–Goresky–MacPherson PDF | Opened; insufficient accessible proof text | Unresolved contextual lead only |
| Looijenga 1988 | Primary theorem and assumptions on pp. 3–4 read | Exact arithmetic \(L^2\)/IH theorem and 1987 announcement |
| Saper–Stern 1990 | Publisher metadata | Independent publication, with announcement corroborated by Looijenga |
| Gelfand–Gindikin–Shapiro 1979 | Full Russian primary article, especially introduction and §1 | Admissible first-order operators; real/complex distinction; trivial quotient |
| Gelfand–Graev 1980 | Full Russian primary article, §§1–3 and Theorems 1–4 | Regular curve complexes, \(k=1\), local classification, author correction |

No permanent `GP-1979-*` ID is assigned to any carry-out item. They belong to the next academic year's source accounting.
