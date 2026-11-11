# Root research and verification audit

Research cutoff: 11 November 2026. The chapter's statuses use November 2026.

## Source checks

- Read the complete task and format and catalog metadata from the attached files.
- Opened the MCCME master catalog at https://old.mccme.ru/gelfand/notes/all-links.html. The direct record-561 URL failed in the web reader; record metadata remains grounded in the supplied catalog snapshot, not a claimed successful record-page retrieval.
- Independently viewed original scans P001032, P001033, P001040, and P001115; also read their Russian and English text.
- P001032–33: the quantum commutator question is explicit. The normally ordered invariance assertion must be distinguished from later algebraic deformations.
- P001040: equation (19) really has negative beta, ordered mu,nu sum without an exclusion, and an inserted N^-2 log. Probability Haar measure is an explicit reconstruction needed to fix normalization, not a word visible on the page.
- P001115: the header is 5/IX-83 and the speaker is Deligne. It belongs to the following academic year. This is an input/catalog-range overlap, not a transcription error in the date.

## Reference-by-reference verification

| Key | Opened source | What was checked |
| --- | --- | --- |
| collinsguionnetmaurel2009asymptotics | https://arxiv.org/pdf/math/0608193 and https://arxiv.org/abs/math/0608193 | Full statement of Theorem 0.1 and hypotheses in introduction, normalized probability Haar measure, self-adjoint trace polynomial, coefficient convergence and analytic local limit. Preprint 8 August 2006, revised 25 June 2008, publication metadata Adv. Math. 222(1), 172–215 (2009), DOI 10.1016/j.aim.2009.03.019. Publisher page failed with 403; arXiv PDF and metadata succeeded. |
| collinssniady2006integration | https://arxiv.org/pdf/math-ph/0402073 and https://arxiv.org/abs/math-ph/0402073 | Corollary 2.4 (matrix-entry Haar moments), Theorem 2.1 and Proposition 2.2; original preprint 26 February 2004 and journal reference CMP 264(3), 773–795 (2006), DOI 10.1007/s00220-006-1554-3. |
| eguchikawai1982reduction | https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.48.1063 | Publisher title, authors, abstract reduction claim, received 19 January and published 19 April 1982. Full article was paywalled; do not label it a read full theorem. |
| neuberger2020quenched | https://journals.aps.org/prd/abstract/10.1103/PhysRevD.102.094503 and https://journals.aps.org/prd/pdf/10.1103/PhysRevD.102.094503 | Read sections II–IV, especially eigenvalue instability, distinction between annealed and quenched prescriptions, finite-radius strong-coupling series and unknown weak-coupling boundary conditions. Publication 6 November 2020. |
| bahnsmeinecke2011string | https://arxiv.org/pdf/1103.0974 | Read Proposition 4 (Poisson closure), Corollary 14 (quadratic-generation condition), section 4 (general formal existence via quasi-Lie-bialgebra quantization). Only preprint bibliographic status is asserted. Abstract URL failed; PDF succeeded. |
| bahns2004string | https://arxiv.org/pdf/hep-th/0403108 | Read sections 4–5 on noninvariant anomalies of conventional oscillator normal ordering. This is not a blanket theorem against every modified quantization. Journal metadata J. Math. Phys. 45, 4640–4660 (2004), DOI 10.1063/1.1776644. |
| enriquezhalbout2010quantization | https://arxiv.org/abs/0804.0496 and https://arxiv.org/pdf/0804.0496 | Read Theorem 1.1 on preprint p.1 and the existence consequence on p.2, using Etingof–Kazhdan quantization and Drinfeld associators. The theorem is a bijection of equivalence classes of universal quantization functors; the following paragraph deduces existence. Checked first circulation 3 April 2008. Primary AMS metadata gives JAMS 23(3), 611–653 (2010), DOI 10.1090/S0894-0347-10-00654-5; direct publisher access failed. The application to string charges was read in Bahns–Meinecke, not inferred solely from the general theorem. |

Additional directly opened PDFs used to discriminate approaches, without automatically adding a citation: https://arxiv.org/pdf/math-ph/0202041 (Meusburger–Rehren, proviso on generation and postponed representations), https://arxiv.org/pdf/0909.3279 (Bordemann–Enriquez–Hofer, explicit rank-one/rank-two case, order-h^3 truncation in general). The earlier general-existence gap in the 2009 preprint is not carried forward as a 2026 gap.

## Search record and exclusions

Primary-search queries included the exact Pohlmeyer invariant-quantization titles; “quadratic generation Pohlmeyer”; “Pohlmeyer-Rehren quantization” with a recent-date filter; “unitary matrix integrals small potential analyticity large N free energy Guionnet Maurel Segala Collins”; “Eguchi Kawai model four dimensional free energy strong coupling exact solution”; and recent arXiv-restricted searches combining Eguchi–Kawai with free energy, bootstrap, and four-dimensional solution. Recent results concerned twisted models, fermions, scattering, or two-dimensional reductions. They do not evaluate the literal four-unitary integral of the notes. Failure to locate a global formula is recorded as bounded search evidence, not a universal negative theorem.

The Pohlmeyer route was not selected for development: formal algebraic existence is already established, and Hilbert-space representations or a preferred explicit presentation would extend the notebook's question. Migdal's explicitly displayed free-energy target supplies a precise C item and a bounded calculation without manufacturing a problem.

## Independent computation

The analytic proof uses conditional expectation and Schur orthogonality. `haar_check.py` independently expands matrix indices and enumerates Haar pairings; it agrees symbolically in N>=2. Ordered plaquette-pair counts are computed as 4+36+144+400=584 for d=2,3,4,5. An initially mistyped prose count in the script was corrected to a programmatically computed count before final output. N=1 is checked directly and excluded from formulas with denominator N^2-1. Exact coefficients alone are not used to exchange the large-N and Taylor limits; the cited local theorem provides that step.

## Build environment

The XeTeX and BibTeX binaries and TeX source packages are installed, but the system ls-R database symlinks and prebuilt XeLaTeX format are missing. An unmodified XeLaTeX format is generated in the task workspace from the installed `xelatex.ini` and `latex.ltx`, with an unhashed TEXMF search path. No system files are changed. The final build script records this workaround and all commands, uses the supplied chapter builder and style, and includes build output.

## Independent current arithmetic check

On 11 November 2026, root opened the Numdam publisher/archive entry and the full primary article by Boxer, Calegari, Gee, and Pilloni, *Abelian surfaces over totally real fields are potentially modular*, Publications Mathématiques de l’IHÉS 134 (2021), 153–501, DOI 10.1007/s10240-021-00128-2. URL: https://www.numdam.org/articles/10.1007/s10240-021-00128-2/ ; full text: https://numdam.org/item/10.1007/s10240-021-00128-2.pdf . Theorems 1.1.2–1.1.3, printed p.156, give the genus-two / abelian-surface Hasse–Weil consequence over totally real fields and potential automorphy. The meromorphic continuation conclusion must not be upgraded to universal modularity or holomorphy; see the explicit qualification following Theorem 1.1.5, p.157. The full paper was received 25 December 2018 and first published online 29 November 2021; receipt alone is not evidence of public circulation.

Root also opened Gee’s 2026 ICM primary-author synthesis, https://epubs.siam.org/doi/full/10.1137/25M1806697 , Theorem 1.4, which confirms this status and says the original paper was posted online at the end of 2018. This source is a current synthesis of the 2021 result, not a claim that the genus-two theorem first appeared in 2026. The spring shard supplies the final bibliography and item treatment.

## Development typography check

A five-page isolated development-and-bibliography smoke document was compiled with XeLaTeX/BibTeX. Pages 1 and 3 were rendered and visually inspected: formulas, Russian text, theorem headings, and author–date references are legible and within margins. The full-chapter review and its final diagnostics are recorded separately. The supplied builder and style were byte-compared to the kit and are unchanged.

Root additionally opened https://arxiv.org/abs/2502.20645 and the primary author PDF https://www.math.uchicago.edu/~fcale/papers/Modular.pdf . Theorem B, pp.3–4, assumes a smooth genus-two curve X: y²=f(x) over Q with degree 5, the mod-3 representation of its Jacobian surjective onto GSp4(F3), and good ordinary reduction of X at 2 and 3. It gives actual modularity for that specified class. Theorem A has distinct local/residual conditions and cannot be summarized as modularity of every ordinary abelian surface. ArXiv records initial posting on 28 February 2025 and only preprint status in the opened metadata. Item 1982-595.6 uses the exact Theorem B statement.
