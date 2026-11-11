# Independent integration review

Reviewed 11 November 2026, read-only, against the supplied prompt and CHAPTER_FORMAT.md. Files reviewed: overview_draft.tex, report_draft.md, and code/assemble.py, chapter_checks.py, rebuild.py, report_tables.py. The supplied builder and the PDF-checking script were also read where relevant. No root file or frozen research file was edited.

## Actionable findings

### 1. Arithmetic theorem scope needed restoration — parent reports fixed

The report initially summarized the 2025 Theorem B immediately after discussing totally real fields, without specifying that the actual modularity theorem in question is for a smooth genus-two curve \(X/\mathbb Q\). It should explicitly name:

- a model \(y^2=f(x)\) with \(\deg f=5\);
- surjectivity of the mod-3 representation of \(\operatorname{Jac}(X)\) onto \(\operatorname{GSp}_4(\mathbb F_3)\);
- good ordinary reduction of the **curve \(X\)** at 2 and 3.

The curve-versus-Jacobian distinction is material. The precise source and opened URLs are already in the spring source audit under boxercalegarigeepilloni2025modularity. Parent confirmed that this report wording has been patched.

### 2. Fedosov summary conflated two constructions — parent reports fixed

The original report sentence “the Fedosov idempotent requires a quadratic partition relation” was too broad. The first **orthogonal block projector** requires \(f_1^2+f_2^2=1\) under the unitary-symbol normalization. The subsequent algebraic idempotent pair is idempotent for arbitrary auxiliary maps; the doubtful cutoff subscript concerns compact support of the difference. Parent confirmed the summary now distinguishes the first projector.

### 3. Speaker statistics would split two catalog identities — normalization requested

report_tables.py groups by the literal speaker field, and assembly originally did not normalize it. The inspected drafts contained:

- “A. B. Zamolodchikov” for 562/567 and “Al. B. Zamolodchikov” for 569.
- “V. L. Ginzburg” for 583/593/596 and a long catalog/identity qualifier as the speaker of 570.

The attached catalog explicitly gives **Al-dr.B. Zamolodchikov** for 562, 567, 569 and 573: Alexander Borisovich, not Alexei Borisovich. Parent asked autumn to normalize all four to “A. B. Zamolodchikov.”

All four Ginzburg catalog entries are **V. L. Ginzburg**. The mathematical identification with V. A. Ginzburg belongs in the summary/provenance correction, while catalog-speaker counting uses the common catalog field. Parent asked autumn to move 570's identification caveat accordingly.

After these updates, verify the speaker table contains a single row for each of those catalog identities. This is the one demonstrated counting defect, rather than a hypothetical formatting concern.

### 4. Final report consistency needs an explicit last gate

rebuild.py regenerates chapter validation statistics but does not regenerate report_tables.py outputs or fill the overview/report templates. chapter_checks.py does not reject unresolved template tokens. Thus a final class change or an unfilled token can coexist with a successful PDF build.

Before packaging, run report_tables.py on the final edited data, refill the report and overview from those exact totals, and reject remaining tokens matching the pattern @@[A-Z_]+@@ in the final overview/report. Compare the class, item, reference and correction totals to validation_statistics.json. This is a delivery guard, not evidence that the intentionally unfinished drafts are incorrect.

## Checks that passed

The source-order list in assemble.py is correct: records 561–592, then 594, 593, 596, 595, 598. EXPECTED in chapter_checks.py is the correct 37-element catalog set. Both April ordering requirements are checked; the assembly itself imposes the complete order. P001115 is correctly excluded from item locations and retained as a provenance boundary.

The current AREA_GROUPS lists form a disjoint 36-record partition, with the year heading handled separately. The report explicitly explains that a single primary area is assigned per record. This gives additive item totals without pretending that the mathematical content has only one subject.

An in-memory examination of all currently saved shard/root bibliography entries found **no changed aliases, alias conflicts, DOI conflicts or empty normalized titles**. The same-key title variants for Tong and Neretin refer to the same works; the Neretin entries share volume, issue, pages and author PDF, and the fuller selected entry supplies the DOI. Current data use only citep/citet, both handled by the assembly and validation patterns. The DOI/title deduplication therefore does not currently lose or redirect a citation.

The longest-entry rule can retain only one per-reference annotation. Preserve the separate shard audits and assembly mapping in the archive as planned; they retain the complementary opened-source routes. This is adequate for the inspected duplicates.

Both item refs and global inline citation keys are checked against the bibliography. The supplied builder additionally checks problem refs. Final XeLaTeX diagnostics catch undefined citations/references and missing characters. The explicit distinction between semantic validation, successful compilation and visual inspection is appropriate.

The four-unitary formulas, low-rank exclusion and local analytic scope in the overview/report agree with the independently reviewed development. The report appropriately keeps meromorphic continuation distinct from actual automorphy, excludes an invented BSD-rank occurrence, distinguishes receipt from first circulation, and retains the notebook's own localization repair.

## Review limits

The review occurred while autumn records 571–573 were still being finalized. The then-current 34-record snapshot is not a coverage finding; assemble.py correctly refuses incomplete coverage. No final PDF build was attempted by this reviewer, and no draft total should be promoted to a final total from this snapshot.

Apart from the scope and speaker issues above, no concrete mathematical or citation-loss error was found in the reviewed integration drafts/scripts.
