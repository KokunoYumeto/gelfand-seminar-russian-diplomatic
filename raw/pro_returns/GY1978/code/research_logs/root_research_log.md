# Root research and audit log

Status cutoff: 10 November 2026 (Europe/Berlin date). This file distinguishes opened records, results read, and inference; it is not a claim of exhaustive database coverage.

## Record 446

Queries included `Kruskal surreal numbers exponential 1978 Gonshor 1986 integration Costin Ehrlich`, `Conway On Numbers and Games 1976 surreal real closed field exponential Gonshor sign sequences`, `surreal numbers omnific integers quotient every surreal fraction`, `Martin Kruskal surreal 1978 Moscow`, `Gonshor exp(x) E_n surreal`, and exact-title/DOI checks. Routine searches used the second engine; an independent first-engine search checked primary coverage and chronology. MathOverflow was used only to find the superseding Costin--Ehrlich article, not as proof authority. No D classification is based on a failed search.

Opened primary/author sources:

- https://www-cs-faculty.stanford.edu/~knuth/sn.html — author metadata: 1974 novel, full title, publisher.
- https://sites.math.rutgers.edu/~zeilberg/EM13/onag1.pdf — opened 18-page image-only second-edition excerpt; onag2.pdf (16 pages) and onag3.pdf (13 pages) also opened. The web reader returned no text and its screenshot interface returned placeholders rather than inspectable pixels. No direct reading of those original proofs is claimed. The previous bibliography key `conway1976numbers` is retained; edition mismatch is explicit.
- https://www.routledge.com/on-numbers-and-games/conway/p/book/9781568811277 — publisher table of contents and second-edition description checked through search retrieval; not evidence of a new 2001 theorem.
- https://www.cambridge.org/core/books/abs/an-introduction-to-the-theory-of-surreal-numbers/introduction/EB380308EEB585CAB634BDF1792944FB — author's introductory excerpt read, including M. D. Kruskal's January 1977 St Louis lecture. Does not prove Moscow attendance independently.
- https://www.cambridge.org/core/books/abs/an-introduction-to-the-theory-of-surreal-numbers/exponentiation/6BADA980CD62CF7915D5DEC358EE246A — Chapter 10 introductory excerpt read: Kruskal's hints, Gonshor's systematic construction, real/infinitesimal/purely infinite split. Print 1986, digital 2010.
- https://arxiv.org/abs/1203.4538 and https://arxiv.org/pdf/1203.4538 — Kuhlmann–Matusinski primary paper; section 2 definitions and Theorems 2.1, 2.3, 2.4, 2.7 read. arXiv metadata gives 20 March 2012 and Order 32(1), 53–68 (2015). The 2018 date in PDF frontmatter is not treated as submission chronology. DOI https://doi.org/10.1007/s11083-013-9315-3 failed redirect; arXiv supplies verified identity and full result.
- https://arxiv.org/abs/1608.03413 and https://arxiv.org/pdf/1608.03413 — Mantova–Matusinski author exposition; relevant section 2 results read. This is a primary author exposition of their own research context, but the quoted basic Conway facts remain historical restatements.
- https://arxiv.org/abs/2208.14331 and https://arxiv.org/html/2208.14331v5 — Costin–Ehrlich final primary paper; sections 2.1–2.3, 8.2–8.4, 9.1 and scope of section 13 read. Precise local series result Proposition 4; exponential Proposition 8(ii); extension Definition 68, integration Theorems 78 and 85. First version 2022-08-30, revision 2024-07-04. Publisher DOI/title/volume 452, article109823, August2024 checked via publisher-indexed retrieval. Direct ScienceDirect open returned403; full author text was accessible.
- https://arxiv.org/abs/1505.02478 — earlier Costin–Ehrlich–Friedman preprint checked as a chronology lead only, not silently used in place of the revised two-author work.
- https://www.cambridge.org/core/journals/journal-of-symbolic-logic/article/abs/number-systems-with-simplicity-hierarchies-a-generalization-of-conways-theory-of-surreal-numbers-ii/6BE3ECB7E41AC2428ACECC04CB453995 — primary publisher abstract checked as an Oz/integer-part lead; not used as full verification of Conway's fraction theorem.

Every local scan P000786–P000790 was viewed in full resolution and compared with both transcriptions. Principal distinctions: multiplication greater-than sign is reconstructible; the factorial Gaussian expression is faithfully copied but false; the omnific-integer reading is a necessary mathematical qualification; the final exponential recursion needs substantive conditions, not merely delimiters. The date and initials discrepancy is kept visible. `1977-445.1–4` in the supplied earlier index are same-source overlaps.

## Record 451 and global provenance

https://old.mccme.ru/gelfand/notes/all-links.html opened in full; rows corresponding to 446–462 checked. The individual record446 page failed to open. The attached source scans, not the unavailable per-record web pages, are the manuscript authority. The heading YEAR1979 is not a separate mathematical talk. Previous-index `1977-451.*` contains Guichardet and Belavin material from the same scans. The catalogue's Fuchs date 5-Mar-78 lies within its1979 sequence; manuscript date5/III-79 must prevail for source attribution. Detailed page mapping and prior-index migrations are assembled in the final coverage output.

## Critical computations

`check_independent.py` independently constructs the spin-one tensor from permutation and contraction operators rather than the researcher's skew-generator matrices, verifies a forbidden cubic-commutator entry, derives Gaussian coefficients from a differential equation and checks an independent integration-by-parts recurrence, and checks contact Jacobi signs. Exact checks and finite numerical experiments are labelled separately. They do not establish any global unproved convergence or integrability statement.

## Independent cross-area source check

Opened https://arxiv.org/pdf/hep-th/0510262 in full and read Mason–Skinner section2 Theorems1–2, footnote1, and section3 p.5. The reviewed text does write first/second Chern-class triviality and later asserts that topologically trivial holomorphic bundles on a quadric are holomorphically trivial. The chapter does not repeat that overbroad shortcut: on P1×P1, O(1,0)⊕O(−1,0) has c1=c2=0 but restricts nontrivially to a ruling. Holomorphic triviality on every incidence quadric is retained as an explicit hypothesis, also present on the supplied Beilinson page. This independent check confirms the distinction flagged during the record audit. The regenerated PDF date (2018) is not substituted for first arXiv circulation31October2005 or journal publication2006.
