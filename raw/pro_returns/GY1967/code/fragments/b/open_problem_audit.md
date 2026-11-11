# Independent audit of fragment a: problem statements and surviving open status

Audit date: **9 November 2026**. Auditor: records 141–154 agent. Fragment a was read only; this report does not modify its authoring script or integration files. Files checked: `fragments/a/items.json`, `problems.json`, `research.md`, relevant bibliography entries, and `source_kit/previous_index.md`. The check found **one C occurrence, no D occurrences, and four problem-index entries**.

## Result and action for integration

The mathematical distinctions and classifications in the four problem entries are supported. **One citation locator should be corrected:** the explicit current-status statement in Damjanović (2026) occurs in **§1, Introduction**, in the paragraph on Anosov diffeomorphisms under “Background, and smooth rigidity results,” rather than §2. Update that locator in occurrence **1967-140.6**, problem **GP-1966-01**, and any corresponding research/bibliography annotation. This correction was communicated to the parent before this report was saved. No problem-ID replacement or status reclassification is recommended.

The conventional manifold hypotheses can optionally be made completely explicit as “a closed connected smooth manifold and a C¹ Anosov diffeomorphism.” The existing use of “compact connected manifold” agrees with the standard convention in the cited statement; the optional wording is an exposition clarification, not a newly discovered obstruction.

## 1. General Anosov algebraic classification

**Occurrence:** 1967-140.6. **Problem:** GP-1966-01, reused from 1966-94.4. **Class C is supported.**

The surviving question is whether every Anosov diffeomorphism is topologically conjugate to an affine Anosov map of an infranilmanifold. Spatzier (2016, Conjecture 2.3, printed p.192) states this precise question. Theorem 2.4 on the same page gives the established case when the manifold is already an infranilmanifold. The fragment correctly separates that result from the problem of identifying the ambient manifold, and correctly avoids upgrading topological conjugacy to smooth conjugacy. Local structural stability alone does not supply the global classification.

Damjanović (2026, §1) explicitly says that global topological classification on general manifolds remains open. Thus the November 2026 status has a directly read contemporary source, rather than relying solely on a decade-old conjecture statement. The source's later discussion of higher-rank actions is a distinct rigidity problem and is not being substituted for this one.

**Prior-index check:** `previous_index.md` contains both occurrence 1966-94.4, “Are all Anosov examples algebraic?”, and GP-1966-01, “Algebraic classification of Anosov diffeomorphisms.” Reusing this ID is correct. No new problem ID should be allocated for the 1967 recurrence.

## 2. Commuting interval maps: fixed versus periodic points

**Occurrences:** 1967-133.3–133.4. **Problem:** GP-1967-02. **Class E is supported for both qualified statements.**

Boyce's original paper constructs continuous commuting selfmaps of the closed unit interval without a common fixed point (Boyce, 1969, Introduction and main construction, pp.77–92). The first page records receipt on 9 January 1967 and revision on 1 December 1967. Its references identify Huneke's 1967 announcement and dissertation. This is adequate documentary evidence for circulating counterexamples in 1967, despite the 1969 journal date. The notebook itself reports a counterexample, so it is appropriate not to classify this as an open question at the lecture.

The adjacent positive assertion is different: if f is C¹, g is continuous, both map [0,1] into itself, and f and g commute, there are x and an integer n ≥ 1 such that f(x) = x and gⁿ(x) = x. This exact hypothesis/conclusion is stated across pp.269–270 of Alikhani-Koopaei (1998), where it is attributed to Schwartz (1965). The fragment accurately labels verification of Schwartz as **indirect**; his original proof was not independently read here either. No weakening to arbitrary merely differentiable maps is justified by that evidence.

Alikhani-Koopaei's separate 1998 conjecture about a common periodic point for two arbitrary continuous commuting maps is not the notebook question. The fragment correctly excludes it from the problem inventory. This audit makes no November 2026 status assertion about that separate conjecture.

**Prior-index check:** no matching interval-map problem appears in the supplied previous index. The earlier occurrences involving commuting divergence-free fields concern a different mathematical question. GP-1967-02 is therefore a valid new ID.

## 3. Entropy and hyperbolic automorphisms of the two-torus

**Occurrences:** 1967-138.2, 1967-138.10, 1967-140.17, 1967-140.18. **Problem:** GP-1967-03. **The stated settled status is supported.**

Adler and Weiss (1967, §1, Main Theorem) prove equality of entropy is sufficient for metric conjugacy of ergodic automorphisms of the two-torus; invariance of entropy supplies necessity. The paper defines the metric category as measure-preserving conjugacy. Its §2 includes determinant +1 and −1 automorphisms and Haar measure; §5 expressly treats the determinant −1 case after the determinant +1 construction. Thus the fragment's scope is not improperly enlarged from SL(2,Z) to GL(2,Z).

The source was communicated on 24 April 1967; PubMed identifies the issue as June 1967. The occurrences are consequently expository in October. The original full text was checked through an author upload; its four-block coding and geometric refinement match the cited proof sections. The fragment correctly requires invertibility and preservation of measure modulo null sets, and does not confuse this with an arbitrary measurable intertwining map or an everywhere defined topological conjugacy.

**Prior-index check:** the earlier entropy entries concern the definition of entropy, a finite-entropy bound, or an underspecified forgetting/mixing remark. None is this exact metric-classification problem. GP-1967-03 is a valid new ID. The four repeated occurrences are consistently grouped under it.

## 4. Classifying bundles over Hausdorff bases

**Occurrences:** 1967-132.3, 1967-132.9, 1967-134.8, 1967-135.5, 1967-135.6. **Problem:** GP-1967-01. **The answered programme, rather than an invented open problem, is supported.**

The actual question is made precise by the category in the adjacent lectures. Gelfand and Fuchs (1967, §1, pp.35–37) impose their global fiberwise-linear chart condition and construct universal frame-space targets with an index set depending on the bundle (Proposition 1.1). This is not a single ordinary CW classifying space for all Hausdorff bases. The fragment states this limitation expressly.

The generalization uses the published elementary-object axioms, including the invertibility and equivariant retraction condition. Gelfand and Fuchs (1968, Propositions 1–2 and Theorem 1, pp.516–517) compare local T-triviality with ordinary local triviality, require a sufficiently large index set, and give the universal pullback representation. Theorem 2, p.518, imposes paracompactness of the topological group for the stated characteristic-group calculation. These qualifications are retained in the fragment, including its distinction between the published axioms and the shorter notebook sketch.

**Prior-index check:** 1966-98.2 is a noncompact completion programme, and 1966-97.3 is the augmentation-completion theorem. Their titles do not identify this specific Hausdorff-bundle category or its universal construction. There is no exact earlier problem entry to reuse on the supplied evidence. GP-1967-01 is defensible as a new, answered problem record.

## Source access and audit trail

The retrieval references below are audit identifiers, not replacements for bibliography keys. “Read” means the specified result or passage was inspected, not every proof in each source.

| Existing key | Independently opened source and locator | Access in this audit |
|---|---|---|
| `spatzier2016rigidity` | https://sites.lsa.umich.edu/spatzier/wp-content/uploads/sites/1081/2023/03/brinprize.pdf — Conjecture 2.3, Theorem 2.4, printed p.192 | Full primary-author survey read; `turn167view0`, `turn176view2`, `turn178view2`. |
| `damjanovic2026symmetries` | https://epubs.siam.org/doi/full/10.1137/25M1807964 — §1 Introduction, Anosov paragraph | Publisher full text read; `turn167view1`, `turn176view1`. This is the corrected locator. |
| `boyce1969commuting` | https://zengfk.com.cn/appendix_files/COMMUTING_FUNCTIONS_WITH_NO_COMMON_FIXED_POINT.pdf — pp.77–78, reference list p.92 | Original article in mirror; statement, dates, independent Huneke attribution and 1967 references read; `turn177view3`, `turn179view2`. |
| `schwartz1965periodic` | https://projecteuclid.org/journals/michigan-mathematical-journal/volume-12/issue-3/Common-periodic-points-of-commuting-functions/10.1307/mmj/1028999371.full | Publisher metadata opened earlier in this audit; no independent original-proof reading. Exact assertion verified through the next source. |
| `alikhanikoopaei1998commuting` | https://scispace.com/pdf/on-common-fixedand-periodic-points-of-commuting-functions-1k438agwci.pdf — Introduction, pp.269–270 | Original research article in mirror; exact C¹ statement read, `turn170view0`, `turn173view0`, subsequently reopened. |
| `adlerweiss1967entropy` | https://www.researchgate.net/publication/7187531_ENTROPY_A_COMPLETE_METRIC_INVARIANT_FOR_AUTOMORPHISMS_OF_THE_TORUS — §1 Main Theorem, §§2,4,5 | Author-upload original article text read; `turn176view0`, `turn179view1`. Communication date appears in original text. |
| `adlerweiss1967entropy` | https://pubmed.ncbi.nlm.nih.gov/16591564/ | Bibliographic metadata read; `turn177view2` confirms June 1967, 57(6), 1573–1576, DOI 10.1073/pnas.57.6.1573. The upload page's July label is not used for the issue date. |
| `gelfandfuchs1967topology` | https://www.mathnet.ru/php/getFT.phtml?jrnid=faa&paperid=2842&what=fullt — Introduction and §1 | Original Russian article read, especially category, global-chart condition and Proposition 1.1; `turn177view0`, `turn178view0`. |
| `gelfandfuchs1968classifying` | https://www.mathnet.ru/eng/dan33991 and https://www.mathnet.ru/php/getFT.phtml?jrnid=dan&option_lang=eng&paperid=33991&what=fullt — pp.515–518 | Metadata and original Russian article read; `turn179view0`, `turn180view0`. Initial direct opening failed twice, but following the metadata page's full-text link succeeded. |

A supplementary freshness search for Anosov classification with a one-year recency filter returned a service error (503). It supplies no evidence. The status conclusion rests on the directly opened 2026 primary-author article, corroborated by the exact earlier formulation. This is a targeted literature audit, not a claim to have proved the absence of every possible subsequent announcement.

No change to fragment b's finalized integration artifacts was made during this additional audit.
