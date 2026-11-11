GY1972 — Critical companion to the I. M. Gelfand seminar, 1972–73
======================================================================
Status cutoff: 9 November 2026

START HERE
----------
GY1972_test.pdf is the complete 142-page chapter. GY1972_report.md gives
the coverage, counts, evidentiary limits, development decision, independent
checks and recommendations for the companion website.

28 catalogue records (27 talks and one heading); 272 mathematical items;
A 25, B 14, C 1, D 0, E 219, F 13; 11 problem entries;
73 references; 112 corrections and provenance entries.

The seven required machine-readable/LaTeX files are at the archive root,
along with the generated chapter, standalone driver, compiled PDF and report.
The supplied build_chapter.py and gelfand_companion.sty are unchanged.

SCOPE AND EVIDENCE
------------------
The requested 28 records follow actual manuscript order, including the
5 March order 290, 292, 291 and the 26 March order 296, 298, 297.
P000449 and P000480 already have occurrence owners in the supplied earlier
index. Their ownership is disclosed; duplicate items have not been invented.
Record 286 is a heading, not an additional lecture.

Class records historical fate, not truth. Literal correctness, exactness of
the publication match, confidence and verification level remain separate.
A bibliography note 'verified' records an opened URL/DOI; the annote field
and each item's verification field explain how much was actually checked.
The evidence logs preserve locators and inconclusive searches. A source's
absence from a search result was not treated as evidence of class D.

No C/D item provided a warranted bounded new research target. The sole C
item is explicitly a reconstructed all-degree G/O computation programme;
no particular finite-degree group is asserted to remain unknown. The full
development is instead a corrective proof for the false published flag
assertion in 1972-280.20 (class A). It includes a general-ring counterexample,
an exact support criterion, stabilization and minimal-rank arguments.
Editorial proof/computation markers identify work supplied here, not claims
of historical novelty. Finite calculations do not replace the general proofs.

BUILD THE CHAPTER
-----------------
Requirements: Python 3.10 or later; XeLaTeX and BibTeX; the LaTeX packages
used by the supplied style. Four DejaVu Serif font files and their license
are included. No network connection is required to build or run checks.

From this archive's root:

    python build_chapter.py GY1972
    xelatex -interaction=nonstopmode -halt-on-error GY1972_test.tex
    bibtex GY1972_test
    xelatex -interaction=nonstopmode -halt-on-error GY1972_test.tex
    xelatex -interaction=nonstopmode -halt-on-error GY1972_test.tex

Alternatively, the recorded build driver runs the same required sequence,
starts with clean auxiliary streams, records logs and handles the supplied
runtime's missing system TeX filename database/format without global writes:

    python code/compile_chapter.py .

The local format/cache is regenerated if needed and is not in this archive.
First-pass citation warnings are resolved by BibTeX and later passes. The
final log has no errors, undefined citations/references, missing glyphs or
overfull boxes. Its 12 underfull horizontal boxes were visually reviewed.
Rebuilding can change PDF metadata and hence its byte hash without changing
the chapter. build_environment.json records the production environment.

REASSEMBLE THE REVIEWED DATA
---------------------------
The reviewed checkpoint files are code/batches/{early,buchstaber,topology,root}.
They include source extracts, evidence logs, bibliography verification notes,
authoring scripts, mathematical check scripts and outputs. To regenerate the
seven chapter files and report from those reviewed checkpoints:

    python code/assemble.py .
    python code/compile_chapter.py .

The assembler preserves the fixed schema, orders records, reconciles spacing
and applies the documented equation-layout adjustments. It does not rerun
literature searches or silently revise mathematical claims. Authoring scripts
are retained for traceability; the checked batch data are the release inputs.

The release reproduction check regenerated all 11 source/metrics files in a
temporary directory and found them byte-for-byte identical. Its output is
reproduction_summary.json. To repeat that source-only check:

    python code/check_reproduction.py .

MATHEMATICAL CHECKS AND OUTPUTS
------------------------------
All these computations use the Python standard library only:

    python code/batches/early/check_tolerance.py
        -> code/batches/early/tolerance_output.json
    python code/batches/root/independent_flag_check.py
        -> code/batches/root/independent_flag_check.json
    python code/batches/buchstaber/formal_checks.py
        -> stdout, saved as code/batches/buchstaber/formal_checks.txt
    python code/batches/topology/checks.py
        -> stdout, saved as code/batches/topology/checks_output.txt
    python code/batches/root/check_arithmetic.py
        -> code/batches/root/arithmetic_output.json
    python code/batches/early/independent_audit_checks.py
        -> code/batches/early/independent_audit_checks.json

The flag checks use different implementations and parameter sets. The
independent arithmetic code imports no primary arithmetic code. Separate
proof reviews of the modular measure, G/O scope, Berezin normalizations,
Henkin hypotheses and the other reconstructions are included in evidence.md,
early/root_review.md and buchstaber/p_adic_independent_audit.md.

DATA AND PDF AUDITS
-------------------
The final data/PDF audit uses PyMuPDF; rendering also uses Pillow and Poppler
(pdftoppm). Package names are in code/requirements-qa.txt.

    python code/audit_deliverable.py . inputs/previous_index.md
    python code/batches/early/audit_final_batches.py
    python code/batches/topology/validate_batch.py
    python code/batches/buchstaber/audit_cross_batch.py
    python code/render_qa.py . qa_regenerated

validation_summary.json records the passing release audit. visual_qa.json
records manual inspection scope, the three reviewers' files, final PDF hash
and rendered-page hashes. All 142 pages were rendered; all 12 numbered contact
sheets and the listed full-page details were inspected. The archive includes
those sheets and details. Individual low-resolution page PNGs can be regenerated
with render_qa.py. Re-rendering starts a new manual-review record; it does not
automatically certify visual quality.

The batch marker audit includes three heuristic review candidates, explained
as false positives in early/root_review.md; it has zero errors or warnings.
Original source attachments and extracted previous-index/bibliography inputs
are in inputs/. The original kit is also retained under code/kit_original/.
No downloaded third-party mathematical source PDF is redistributed here.

ARCHIVE INTEGRITY
-----------------
manifest.json lists every payload file with its size and SHA-256 checksum;
it excludes itself to avoid a recursive checksum. To verify an extracted
archive, run:

    python code/package_release.py . --verify

To regenerate a ZIP after an intentional edit and validation:

    python code/package_release.py . --zip ../GY1972.zip

The package command refreshes the manifest, checks ZIP CRC integrity and
compares every archived payload against its manifest. It does not replace
the mathematical, data or visual reviews.
