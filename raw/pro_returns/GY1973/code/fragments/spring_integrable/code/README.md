# Spring fragment reproduction

The generators write only to their parent fragment directory. Run from the task workspace root:

    python work/fragments/spring_integrable/code/make_references.py
    python work/fragments/spring_integrable/code/make_fragment.py
    python work/fragments/spring_integrable/code/check_fragment.py

make_references.py reads the supplied work/references_cumulative.bib, preserving the first entry under each reused key. It records current-run verification and adds the new entries. add_references.py is the idempotent construction helper used to insert the final seven entries; it is not needed to rerun the completed generator.

For symbolic verification, use Python with sympy==1.14.0 (see requirements.txt):

    python work/fragments/spring_integrable/code/verify_emendations.py

The script optionally recognizes a local vendor dependency directory. Archived results were produced with SymPy1.14.0. Checks cover formal operators versus direct action, rational soliton substitution, Miura factorization, a matrix characteristic polynomial, circle doublets, and Whitham scaling. Outputs are the adjacent output/emendation_checks.json and .txt. These verify critical emendations, not newly claimed integrability theorems.

check_fragment.py writes output/data_check.json. The supplied build_chapter.py separately passed; the integrating agent handles final TeX compilation in its configured runtime.
