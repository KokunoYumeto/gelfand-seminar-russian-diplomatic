# GY1973: critical companion to the Gelfand seminar, 1973–74

## Start here

Open GY1973_test.pdf for the complete 148-page chapter. GY1973_report.md explains the editorial decisions, counts, searches, remaining uncertainties, and website recommendations.

The edition contains 32 source records, 301 mathematical occurrences, 17 indexed problems, and 93 corrections or recorded ambiguities. It covers all 53 supplied scan pages. The 30 supplied catalogue entries are retained; two additional records on the scans, 331 and 332, are included under their written date of 25 March 1974, with the catalogue's 1975 discrepancy documented.

The historical counts are A = 25, B = 7, C = 4, D = 0, E = 229, F = 36. The research cutoff is 9 November 2026. No bounded new research contribution to a C or D question was warranted. GY1973_development.tex contains a labelled critical verification appendix, including complete proofs and independently checked computations required to assess the notes.

## Files

| Location | Contents |
| --- | --- |
| GY1973_talks.json, GY1973_items.json, GY1973_problems.json | Authoritative structured edition and problem links |
| GY1973_overview.tex, GY1973_development.tex | Overview and critical verification appendix |
| GY1973_corrections.csv | Source readings, proposed corrections, and evidence |
| GY1973_references.bib | 91 bibliography entries, with verification scope and links |
| GY1973_chapter.tex, GY1973_test.tex, GY1973_test.bbl | Generated chapter, standalone wrapper, and resolved bibliography |
| GY1973_test.pdf | Compiled chapter |
| GY1973_report.md | Editorial report, count tables, coverage and limitations |
| GY1973_statistics.json, GY1973_area_map.json | Reproducible report counts and area labels |
| code | Assembly, validation, mathematical verification, and packaging programs |
| code/fragments | Audited source blocks, historical generators, and computational outputs |
| audit | Search logs, source reviews, input hashes, bibliography inventory, and coverage table |
| logs | Assembly, mathematical verification, data validation, and TeX/BibTeX outputs |
| fonts | Four DejaVu Serif faces and their license |
| MANIFEST.sha256.json | Byte sizes and SHA-256 hashes of every other delivered file |

Of the 91 bibliography entries, 88 are marked verified and three unverified. The latter are explicitly identified in the report and item assessments. A verified link is not a claim that every proof in that source was read. The printed bibliography has 90 entries because the general archive record is not invoked by a typesetting citation.

The supplied builder, style and format specification are byte-identical to the kit. Original source attachments and downloaded publisher papers are not duplicated into this archive. The input hash audit identifies the attachments used; the bibliography and research logs identify the checked publications.

## Build and validate

Use Python 3 and a XeLaTeX installation including the packages required by the supplied style, together with BibTeX. From this directory, run the prescribed sequence:

    python build_chapter.py GY1973
    xelatex GY1973_test
    bibtex GY1973_test
    xelatex GY1973_test
    xelatex GY1973_test

The helper runs the same builder and engines, uses the bundled font faces, and builds in a fresh temporary directory. Compilation errors stop the build; the packaging audit additionally checks the final logs for unresolved diagnostics:

    python code/build_pdf.py
    python code/validate_data.py

On the original runtime, a generated TeX format and filename database were absent despite the packages being installed. The helper contains a documented fallback for that environment. It does not change the supplied builder or style. An additional XeLaTeX pass is used when required to settle labels.

To repeat the independent mathematical checks:

    python code/independent_checks.py
    python code/fragments/autumn_representations/check_conic.py
    python code/fragments/spring_integrable/code/verify_emendations.py

The first two use the Python standard library. The third requires SymPy 1.14.0; its requirement file and original output are in the spring fragment. Symbolic identities and finite exact checks have the scope stated in their accompanying proofs. Numerical checks are not offered as proofs of unbounded assertions.

To reassemble from the delivered audited fragments:

    python code/final_polish.py
    python code/assemble.py
    python code/write_editorial.py
    python code/build_pdf.py
    python code/write_editorial.py --verified

The root JSON, CSV and bibliography files are the authoritative final edition. Older per-fragment generator programs are preserved as research history; some assume the original task directory and source attachments and can regenerate earlier intermediate text. They are not needed for a normal rebuild. To check older problem identifiers against the previous index, pass its path explicitly:

    python code/validate_data.py --previous /path/to/previous_index.md

To regenerate the package and verify all manifest hashes:

    python code/package_deliverable.py --zip /path/to/GY1973.zip

The manifest excludes itself. The packaging program checks the ZIP's CRCs and every payload's SHA-256 digest after writing it.
