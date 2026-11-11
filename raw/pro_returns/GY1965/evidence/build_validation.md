# Final build and inspection

**Date:** 9 November 2026. **Outcome:** The delivered chapter builds successfully; the final data, citation, PDF and visual audits pass.

## Data and build

The final assembly was run from the archive's own frozen inputs:

```bash
python code/assemble.py --parts code/parts --output .
python code/write_summary.py .
bash code/build.sh
```

The chapter builder reports **37 records, 298 occurrences, 9 questions, 63 references, and 26 correction entries**. The additional validator reports **zero errors and zero review notices**. It checks required fields, enums, source order, sequential occurrence numbering, reciprocal problem links, bibliography and citation coverage, and unwanted control characters. All delivered Python scripts also pass parsing.

The successful final sequence is XeLaTeX, BibTeX, XeLaTeX, XeLaTeX. The final logs contain **no LaTeX warnings, no undefined citations or references, no missing glyphs, no overfull boxes, and no BibTeX warnings or errors**. Full command output and logs are retained in `evidence/build/`.

The log retains 17 underfull-box diagnostics concerning loose line justification. The affected layouts were included in visual inspection and show no clipping, collision, or unreadable content; these diagnostics are not compilation errors and have not been hidden by changing the reporting threshold.

This minimal environment required initialization of a local XeLaTeX format. The bootstrap and its local-directory handling are included in `code/build.sh`; the generated format is not bundled. The complete licensed DejaVu Serif family is included. The supplied style's Russian-language fallback was adapted to the available Babel locale while preserving the Russian text. These build changes do not change mathematical content or the seven-file data schema.

## Final PDF

| Check | Result |
|---|---:|
| Pages | 133 |
| Page size | A4 |
| Overview | 2 pages, ending before record 53 on page 2 |
| Occurrence identifiers found in extracted PDF text | 298 of 298 |
| Distinct resolved occurrence destinations | 298 of 298 |
| Internal links with valid page destinations | 868 of 868 |
| Bibliography destinations | 63 |
| Text spans outside page boundaries | 0 |

The PDF SHA-256 is:

```text
a4a0a80e9ece747691bee981231a4dad1bf86af1e12c18449934aa6c425ff7db
```

The machine-readable results and the PyMuPDF version are in `pdf_audit.json`. These numerical checks do not by themselves establish good layout. The parent editor inspected contact sheets covering all 133 pages, and an independent reviewer inspected selected full-page renders of the overview, catalogue, entire development, problem index, corrections, and bibliography. The page list and findings are recorded in `pdf_review.md`.

Two visual problems were corrected before delivery: long occurrence titles initially crowded or displaced their class badge, and a long talk heading initially appeared at the foot of a page without its summary. The final style gives the title and badge separate columns and keeps talk metadata with the following text. The final visual review confirms those repairs. Corrections use wide stacked entries rather than a narrow five-column table; the formulas, evidence and Russian readings remain legible.

## Mathematical verification

The exact Weyl-field checks passed with seeds **1965** and **20261109**, including the deliberately incorrect negative controls. Separate symbolic implementations verified the top polynomial, fixed-direction ellipsoid counterexample, torus critical points, and three-cusp calculation. Independent written derivations cover the centralizer and stabilizer proofs, innerness criterion, finite-group averaging, early algebra and trace examples, middle analytic and geometric annotations, and the late boundary-cosine and Radon normalizations. Details and accepted wording corrections are in the four proof-review files and the main research report. None of these finite checks is treated as a proof of the unrestricted Weyl-field classification.

## Packaging

The archive contains the seven required chapter data files, the report, generated chapter and standalone driver, compiled PDF and bibliography, build tools, licensed fonts, research and computation code with outputs, source evidence, and review records. It excludes duplicated uploaded scans and transcriptions, transient TeX auxiliary files, Python caches, and the local TeX format. `MANIFEST.sha256` hashes every other packaged file; the ZIP integrity check is performed after packaging.
