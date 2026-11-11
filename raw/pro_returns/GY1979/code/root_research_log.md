# Root research and verification log

Status date: 2026-11-10. This records evidence actually consulted, not a claim of exhaustive bibliographic coverage.

## Primary source scans

P000861 and P000862 were opened at full image resolution. The body-spectrum theorem, the two numbered Berezin problems, the quantifiers on odd entries of A and even entries of B, the four-generator remark and the independent-entry proviso agree with the supplied Russian transcription. The chapter's low-rank specializations are explicitly its own constructions.

## Exact publication matches and scope

1. Sergeichuk, V. V. (2000). Canonical matrices for linear matrix problems. *Linear Algebra and its Applications, 317*(1–3), 53–102. https://doi.org/10.1016/S0024-3795(00)00150-6 . Full author PDF opened at https://arxiv.org/pdf/0709.2485 . Theorems 1.1 and 1.3 and section 1.4 read; the algorithm gives a canonical representative for similarity under units of a finite-dimensional matrix algebra. Its reference 32 identifies the 1999 Bielefeld preprint 99-070. The 2007 arXiv date is a later repository deposit. Root proves that the finite even-supermatrix algebra fits this theorem by left regular representation. This is an exact application, not proof of a historical causal response to the 1979 talk.
2. Belitskii, G. R., & Sergeichuk, V. V. (2003). Complexity of matrix problems. *Linear Algebra and its Applications, 361*, 203–222. https://doi.org/10.1016/S0024-3795(02)00391-9 . Full author PDF opened at https://arxiv.org/pdf/0709.2488 . Section 1 and Theorem 1.1 read. The paper defines containment of simultaneous similarity of pairs and the meaning of wildness; it does not say canonical algorithms are impossible.
3. Belitskii (2000), Normal forms in matrix spaces, author institution metadata/abstract opened at https://cris.bgu.ac.il/en/publications/normal-forms-in-matrix-spaces-4/ . DOI 10.1007/BF01291714, journal 38(3), 251–283. Corroborates the algorithmic distinction. Not included as an additional chapter citation because the more directly read Sergeichuk theorem suffices.

## Search strings used

Two independent web search systems were used, with primary-paper and author-page follow-ups. Queries included:

- Berezin Grassmann algebra matrices normal form centralizer odd matrices Jordan
- classification matrices dual numbers simultaneous similarity pairs Sergeichuk Belitskii
- "Grassmann" "centralizer" matrix odd
- "supermatrices" "canonical" "Jordan" Berezin
- "Berezin" "normal forms" supermatrix
- "Grassmann" "commutant" matrix Berezin
- "Canonical matrices for linear matrix problems" Sergeichuk
- "Complexity of matrix problems" Belitskii Sergeichuk arxiv
- "odd" "matrix" "Grassmann" "commuting" Berezin
- "Березин" "жордан" "матриц"
- "матриц" "грассман" "нормальн"
- "Grassmann" "2 × 2" "centralizer"
- "supermatrices" "Jordan normal form"

No exact historical publication of the complete n=2, N=4 commutant stratification was found. Search hits about polynomial identities, Cayley–Hamilton theorems, centralizers of ordinary Jordan matrices, and Grassmann superderivations do not by themselves answer the exact equation in the notes. This is a retrieval limit, not a global-open or novelty assertion.

## Independent computation

`verify_berezin.py` implements exterior multiplication twice using distinct representations. Exact ranks agree for 36 cases. Every kernel vector is substituted back into the original equation, and 1,706 products of basis elements in three representative kernels satisfy the equation. The full machine-readable output is preserved. No numerical rank tolerances or empirical extrapolation are used.

## Energy-representation diagnostic

Hasebe's primary PDF was opened independently at https://arxiv.org/pdf/0805.1329 (version 3, 15 January 2011). Page 1 explicitly identifies the invalid identity in Shimada's Lemma 4.6; equation (2.1) defines the right logarithmic derivative. The chapter constructs and checks an explicit compactly supported SU(2) counterexample to that identity. The construction is a diagnostic of the already documented flaw, not an irreducibility counterexample or a priority claim. `verify_energy_identity.py` checks the example by direct exponential differentiation and by an independently integrated conjugation formula, with exact symbolic agreement at two points.

## Boundary evidence

The supplied previous index already has P000840 content as 1978-460.12 through 1978-460.20. The current source has explicit September 1980 headings at P000917 onward. These are excluded from newly counted 1979 occurrences and retained in the source-coverage and boundary records. The MCCME all-links page was opened at https://old.mccme.ru/gelfand/notes/all-links.html . Direct requests for record-489 through record-491 returned inaccessible responses in this run; no claim to have checked those record pages is made.

## Final integrated bibliography checks

The chapter's104 references were compared with the792-entry supplied cumulative bibliography: no duplicate DOI or candidate cumulative-key violation remained. Three same-key merge differences were reviewed (Wilson1974, Jaffe--Witten and Sergeichuk2000); they concern verification annotations/links, not competing works. The retained versions have the fuller directly read scope. This decision is recorded beside the original alternatives.

Eleven inaccessible publisher leads were independently checked through public Crossref DOI-registration JSON. Ten succeeded on the first pass; the Fradkin--Fradkina request initially returned429 and succeeded on one later retry. Exact returned bibliographic fields and timestamps are saved in bibliography_metadata_output.json. These checks upgraded bibliographic identity only, not an item's proof-verification level. They corrected Kallosh1980 pagination to165(1),119--128. Every final bibliography entry has an opened link/DOI record; the per-item verification and annotations continue to distinguish metadata from read results.

## Final Zakharov chronology check

The independent late-record reviewer located and opened the full1980 primary paper at https://zakharov75.itp.ac.ru/static/local/zve75/zakharov/1980/1980-05-1980_PD_ZS.pdf . Section1, pp.192--195 was read, with equations12--13 on p.193 visually checked. It contains the exact difference-curve parametrization and credits the general example to S.V.Manakov (private communication). Receipt1September1979 predates the seminar; publication wasJune1980. This replaces the earlier metadata-only access limit for that reference.

The kinetic obstruction on p.195 is distinguished from the general analytic-Hamiltonian theorem in the1988 paper, Theorem3.1, pp.291--293. The latter's introduction pp.285--286 identifies a brief1985 announcement. The final463.6 fate and partial-match assessment keep those chronologies separate. No1985 full text is claimed to have been read.
