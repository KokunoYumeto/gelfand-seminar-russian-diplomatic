# GY1986 critical companion

The main reading copy is GY1986_test.pdf. The authoritative chapter inputs are
the seven GY1986 data files specified in CHAPTER_FORMAT.md. GY1986_report.md
explains coverage, research decisions, counts, checks, limitations, and proposed
website presentation.

## Rebuild the reading copy

From this directory, run:

    python3 build_chapter.py GY1986
    xelatex -interaction=nonstopmode -halt-on-error GY1986_test.tex
    bibtex GY1986_test
    xelatex -interaction=nonstopmode -halt-on-error GY1986_test.tex
    xelatex -interaction=nonstopmode -halt-on-error GY1986_test.tex

Alternatively, python3 code/root/build_and_check.py runs these commands and
records their full output and a validation ledger. It also uses pdfinfo and
pdftotext. XeLaTeX needs the packages listed in gelfand_companion.sty and a
Cyrillic-capable text font; the supplied style has font fallbacks.

The chapter builder and style as supplied with the task are retained under
code/kit_original. The final build notes record any compatibility changes.

## Reproduce the mathematical checks

Use Python 3 with SymPy and mpmath. Exact runtime versions are recorded in
code/root/final_validation.json. Run the check programs in code/root; each
has a matching complete .out file. The cube calculation also writes
cube_witnesses.json. The spectral-operator check and its full output are under
code/parts/C. The written proofs, algorithms, and independent checks are
summarized in code/root/proof_review.md and the development section.

These computations establish the stated finite results. They are not
certification of every theorem in the bibliography or claims of historical
novelty.

## Research and source audit

The original six attachments are identified by their SHA-256 hashes in
code/root/input_manifest.json. Source excerpts, the catalogue list, the
previous-year index, and the cumulative bibliography supplied by the user are
included as supporting materials. Re-running preparation against the scans
requires the original attachment packet.

The three research slices and their authoring programs are included under
code/parts. The final standard files are authoritative: edits should be made
there unless deliberately rebuilding the research assembly. The root assembly
and summary generators document how the quantitative ledgers were produced.
Queries, returned source URLs, titles, and fetch failures are preserved in
code/root/research_log.json. Full third-party article texts are not included.

The status cutoff is 12 November 2026. Bibliography verification notes record
opened URLs or DOIs; item-level fields distinguish reading a result from
checking metadata or retaining an unresolved lead.
