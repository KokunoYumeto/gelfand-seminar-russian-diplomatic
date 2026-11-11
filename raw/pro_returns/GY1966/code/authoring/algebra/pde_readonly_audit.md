# Independent read-only audit of the PDE slice

Checked 9 November 2026. No files in `parts/pde` were modified.

## Passing checks

- 10 records 105–114, 69 occurrences, 8 problems, 23 distinct bibliography keys.
- All required item fields, consecutive `1966-<record>.<n>` IDs, cited-key membership in each item, bibliography membership, problem occurrences, dated present statuses and C-item worth fields checked independently; no errors.
- The two reused cumulative keys are `kohnnirenberg1965algebra` and `hormander1965pseudo`.
- Actual content boundaries checked from the Russian page chunks: Nirenberg P161–162; Minlos P163–164 and upper P165; Arnold lower P165–166; Gelfand and Nirenberg share P167; Vishik's heading and next lecture share P168; Oleinik starts lower P169 and continues P170; geometry list P171–172; Arnold's next lecture starts P173. Summaries and item locators correctly distinguish these from the overlapping catalogue-wide ranges.
- Quinto's full primary PDF was independently reopened. Problem 4.1 exactly matches geodesic spheres whose enclosed balls contain a fixed ball. Section 5 explicitly retains real analyticity; no ray-transform substitution occurs. This supports the slice's partial-result identification, while the current nonresolution claim remains qualified as a search result.
- Li–Song's full primary PDF was independently reopened. The Main Theorem requires an entire Grauert tube and proves the stated complex-projective metric rigidity. It does not prove unrestricted smooth classification.

## Reported integration risks

1. **LaTeX correction cells:** raw `_` and `^` outside math occur in PDE correction rows 7, 9, 14, 15, 19 and 21. Examples: `p=∂_V log Z`, `C_i`, `p_y`, `β^{-1}`, `a^{ij}`. The chapter builder inserts these fields verbatim. Math delimiters or escaping are needed. Root was notified immediately.
2. **Scope refinement for the Li–Song comparison:** their definition of Zoll additionally requires each prime geodesic to be simple (injective before the common period). The notebook reconstruction only specifies equal prime periods. Its status is already marked partial, but the comparison should say “Zoll in their sense” or mention simple closed geodesics in addition to the entire-Grauert-tube hypothesis.
3. **Problem-index citation rendering:** PDE problem statuses carry `refs` metadata but no `\cite...` text. The supplied builder does not render the refs array. This is not a schema failure, since linked occurrences contain citations, but root may wish to append citations to status text for a self-contained printed problem index.
4. **Chronology wording:** journal receipt does not by itself establish public circulation or publication before a seminar date. The Oleinik bibliography annotation's “received 1 March 1966, hence published before October” should rely on the actual 1966 issue, not the inference from receipt alone. The core mathematical attribution is plausible and the primary announcement was actually opened by the author of the slice.

No serious theorem/source mismatch was found within the requested schema, references and source-boundary audit. Full proofs and the newest literature on the two C questions were not independently re-researched; this audit does not upgrade the original access levels.
