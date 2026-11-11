# GY1966 records 105–114: completed research slice

Status date: **9 November 2026**. All ten assigned catalogue records are covered. Contents are assigned from the handwritten headings, not the overlapping catalogue ranges.

## Deliverables and counts

- talks.json: 10 records, 105–114.
- items.json: **69 occurrences**.
- problems.json: 8 new entries, provisionally GP-1966-20 through GP-1966-27.
- corrections.csv: 27 entries.
- references.bib: 23 references with opened links and verified notes; individual annotations distinguish full-text/result reading from metadata or abstract checks.
- build_part.py and references_new.bib reproduce the data and validation. Two cumulative bibliography entries are copied verbatim.
- validation.json records the successful field, reference and occurrence checks.

| Class | A | B | C | D | E | F |
|---|---:|---:|---:|---:|---:|---:|
| Items | 7 | 13 | 2 | 0 | 38 | 9 |

| Record | Catalogue speaker | Actual content | Items |
|---|---|---|---:|
| 105 | Louis Nirenberg | P161–162 | 11 |
| 106 | R. A. Minlos | P163–164 | 7 |
| 107 | R. A. Minlos | upper P165 | 5 |
| 108 | V. I. Arnold | lower P165–P166 | 7 |
| 109 | I. M. Gelfand | middle P167 | 4 |
| 110 | Louis Nirenberg | lower P167 | 3 |
| 111 | M. I. Vishik | top P168, headings | 2 |
| 112 | M. I. Vishik | P168–upper P169 | 7 |
| 113 | O. A. Oleinik | lower P169–P170 | 7 |
| 114 | Agranovich heading; geometry list unattributed | P171–172 | 16 |

By catalogue speaker: Nirenberg14; Minlos12; Arnold7; Gelfand4; Vishik9; Oleinik7; Agranovich-associated record16. **The fifteen geometry-list items are not attributed to Agranovich personally.** Interventions by Gelfand are separately identified inside the occurrences.

Suggested area counts: elliptic/PDO/index analysis20 (105,111,112); statistical mechanics12 (106–107); symplectic/Maslov7 (108); representation theory4 (109); heat-kernel PDE3 (110); fluid PDE7 (113); geometry collection with one PDO heading16 (114).

No separate development section is offered for the two C questions. They are precise after explicitly marked reconstruction, but neither yielded a defensible bounded contribution. Short elementary checks remain occurrence annotations rather than claims of new research.

## Attribution and critical readings

P160 ends the preceding record. Minlos and Arnold share P165. P167 starts an additional **“Minlos. Lecture5. Phase transitions”** heading without subsequent mathematical content before Gelfand's heading. It is documented as provenance, without inventing an extra record or theorem. P168 likewise has an unindexed professor's Sturm–Liouville heading, possibly “Lorch”; no mathematical claim follows.

P171 announces Agranovich's third PDO lecture and then immediately gives “Problems of differential geometry”. The list's speaker is unspecified. P173 begins the next Arnold record and is excluded.

The most consequential corrections:

1. P161 genuinely reads **неясна связь** (“the connection is unclear”), not “no connections”, and **младшие члены** (“lower-order terms”), not “leading terms”. Both were rechecked directly on the scan.
2. P162: \(A^0=I\). Analytic continuation of an initially defined diagonal density is not the diagonal of its zero-power delta kernel. The misleading operator statement is handwritten.
3. P165: the Gibbs-entropy definition lacks a minus sign, and the next formula has \(1/\beta\) instead of \(\beta\). Direct substitution of the Gibbs density verifies both corrections.
4. P166: a Lagrangian graph gives a locally exact one-form; a global potential requires exactness. A closed angular form on an annulus is the obstruction.
5. P167: tensor multiplicities do not distinguish D8 and Q8. The reconstruction equations also require unit normalization and a unitary/reality condition. The zero family and the circle-character family \(C_k=z^k\) expose the omissions.
6. P167: for the written heat generator, \(-4t\log p\to d^2\). The page's own Euclidean Gaussian fixes the missing four.
7. P169 ends **отлич.** (“differ”), not **отлип.**.
8. P170: initial/inflow variables are inconsistent in the manuscript. Oleinik's problem uses \(u_0(x,y)\), \(u_1(t,y)\), and monotone compatible data. The crossed-out \(p_y=0\) does not remove the immediately following explicit prose \(p=p(t,x)\).
9. P171: the uncancelled minimal-graph formula visibly has an extra square on the second-derivative term. The Bernstein question is affirmative for domain dimension \(n\le7\), negative for \(n\ge8\); the note's “Done” has no adequate dimension qualification.
10. P172 problem7 has **пересек.** after a cancelled word. It does not legibly say “closed”, so the famous infinitely-many-closed-geodesics conjecture is **not** inserted into the problem index. Problem8 does explicitly say closed.
11. P172: a contact plane field in dimension3 orients the ambient manifold even without coorientation. Martinet answers the corrected orientable question. The literal unqualified statement is false.

## Exact sources, chronology and scope

### Minlos: shared keys and the original variance programme

The shared keys **minlos1967limiting** and **minlos1968lectures** are both present.

[Minlos1967 metadata](https://www.mathnet.ru/eng/faa2817), DOI10.1007/BF01076086: Russian pp60–73, English140–150, received **20 December1966**. The Russian PDF was opened. It constructs a **grand-canonical** dilute limiting Gibbs distribution; its introduction defers mixing and ergodicity. It is not a proof of every canonical notebook hypothesis.

[Minlos1968 metadata](https://www.mathnet.ru/eng/rm5594), DOI10.1070/RM1968v023n01ABEH001235, RMS23(1),137–196. The [English full PDF](https://www.mathnet.ru/php/getFT.phtml?jrnid=rm&option_lang=eng&paperid=5594&what=fullteng) was opened and relevant parts read.

- Introduction137–138: first lectures at Khumsan, September1965; amplified at the Gelfand seminar in autumn1966.
- LectureII149–154: configuration space and limiting distributions. Formula(2.5),151–152, fixes one local event before a uniform supremum over remote events.
- LectureIII§2,158–159: decay and the canonical/grand-canonical conditioning distinction.
- LectureIII§3,160–161: limiting-correlation hypotheses, continuity, bounds, wall-distance convergence rate. The canonical “suitable” specific volume is \(v=v(\Omega,N,\beta)\). The original notebook's quantifiers must still be respected independently.
- LectureIII§4,162–164: pair observable \(\sum f(x-y)\), assumption(3.24) only \(\int|f|<\infty\), mean limit, variance expansion.
- **The p164 remark expressly adds integrability of the mixing majorant and the van-Hove boundary-strip condition.** Thus the expanded lecture repairs the notebook's missing integrable-decay assumption. The first variance term still contains \(f^2\), so \(L^1\) alone does not justify finiteness.
- Problem3 on p164 asks for precise inequalities in the mean and representativeness argument. A stronger exponential large-deviation principle is separately written as(3.29).
- LectureIV164–176: thermodynamic functions and van-Hove limit.

Lenard1975 is an exact match to Gelfand's **full-hierarchy** correlation axioms after reconstruction. The publisher's substantive abstract was read, not the full proof. Existence explicitly permits nonuniqueness; Lenard1973 treats determinacy separately.

### Complex powers, Maslov and PDOs

Seeley1968 is the published Russian translation of a **preprint**, explicitly so identified on p96. It is not silently equated bibliographically with the differently titled1967 proceedings chapter. The numbered kernel assertions and formula(II), p97, closely match the notes and were read. Separate kernel assertions have separate occurrence entries.

Arnold1967 was received **28 September1966**, before the10October talk. The Russian §1, Lemmas1.1–1.2, determinant-square construction and Maslov discussion were read. Publication followed in1967. A labels the exact authorial publication, not priority for each elementary fact. Earlier occurrence **1964-21.3** is linked.

The cumulative keys **kohnnirenberg1965algebra** and **hormander1965pseudo** are reused verbatim. Their publisher metadata was opened; no full-proof reading is claimed. Vishik1 remains F because its headings specify no symbol class or boundedness theorem. Vishik2 has actual formulas and is E.

### Oleinik

Oleinik1966, Doklady168(4),751–754, was received **1March1966** and published before the October report. Its Russian announcement was read, so the recorded existence results are E.

Oleinik1968, RMS23(3),1–66: **Theorem4,28–29**, and **Theorem5,29–32**, were read. The former specifies the monotone initial/inflow problem; the latter gives all-time existence on a sufficiently short streamwise interval with uniform data hypotheses. The isolated \(p_x\le0\) in the notebook is not used to discard those conditions.

Gérard-Varet–Dormy2010: the author-hosted full PDF was opened, and **Theorem1**, author pp4–5, read. It concerns linear Sobolev instability of specified nonmonotone shears and does not contradict Oleinik's monotone class. Initial circulation2009; print2010.

### Geometry problem index

- **GP-1966-21:** Quinto2008 **Problem4.1** exactly matches the sphere-enclosing-ball question after supplying simple connectivity. Theorems5.1–5.2 use real analyticity. Searches yielding geodesic-ray support results were rejected as wrong-transform matches. C is limited to the unverified arbitrary-smooth-metric remainder.
- **GP-1966-22:** Caffarelli–Li2003 **Theorem1.1**,549–550, gives the exact entire convex result and the earlier dimension chronology. Pogorelov's all-dimensional paper was received June1971 and published1972; its metadata was checked separately.
- **GP-1966-23:** Bombieri–De Giorgi–Giusti1969, Introduction, TheoremB and §IV, were read in the1971 Russian translation. Ambient and domain dimensions are kept apart.
- **GP-1966-24:** Sobolev pullback rigidity is proved in the occurrence by testing against1, recovering volume, subtracting the \(L^2\) part and recovering the inverse metric from local Hessian tests. A second check uses the Laplacian principal symbol. Arendt–terElst, preprint2011/publication2017, **Theorem1.1**, was read and is explicitly a **partial** match with order-preserving heat-semigroup data. Abstract Hilbert isometry or isospectrality is insufficient.
- **GP-1966-25:** Yau1976 p659 explicitly states infinite volume for complete noncompact manifolds with Ricci≥0. The publisher's scanned first page was visually inspected; the full proof was not read.
- **GP-1966-26:** Equal-prime-period topology is separated from both Blaschke and Berger conjectures. Cohomology restrictions are known. Li–Song2026 gives a current partial rigidity result with an **entire Grauert tube** assumption; its Introduction and Main Theorem were read. No unrestricted smooth-type classification was verified. The source's rank-one wording is explicitly a reconstruction of a partly cancelled phrase.
- **GP-1966-27:** Martinet1971 metadata and Eliashberg1992 pp165–166 were opened and read at the stated levels. Eliashberg explicitly gives orientable existence and the forced ambient orientation. \(\mathbb{RP}^2\times S^1\) refutes the literal unrestricted assertion.

## Verification and classification lessons

All P161–P172 scans were inspected at formula-critical points. P161, P169 and P172 were reinspected at finalization. Every current-status field is dated; every C item has a precise remainder and worth sentence. There are no D assignments.

Independent elementary checks: positive-eigenspace inverse \(\lambda^{-1}L^*\); Gaussian factor4; Gibbs entropy by substitution; D8/Q8 fusion rules via the unique2D and four1D irreducibles; missing tensor-unit/reality counterexamples; Sobolev metric recovery by energy forms and Laplacian principal symbols; contact orientation under \(\alpha\mapsto f\alpha\).

The classification misses some chronology nuances: an exact later authorial exposition may contain older elementary facts (Arnold); a preprint reported by someone else can be B while already circulating at the talk (Seeley); a title-only record remains F despite an obvious standard theorem one might supply (Vishik1); a positive result may require correcting a missing source hypothesis (contact orientability). C is an audited remainder with an explicit search limitation, not proof of universal absence from the literature.

“Verified” in BibTeX means an opened linked resource. It does not upgrade metadata-only verification to a read proof. The more specific evidence level remains in each bibliography annotation and occurrence assessment.
