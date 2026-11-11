# Local TeX runtime repair

The installed binaries are TeX Live 2023/Debian:

- /usr/bin/xelatex (XeTeX 0.999995)
- /usr/bin/bibtex (BibTeX 0.99d)
- /usr/bin/xdvipdfmx

The package trees are present at /usr/share/texlive/texmf-dist and /usr/share/texmf, but the normal filename databases and prebuilt XeLaTeX format are missing. The default TEXMF value prefixes these trees with double exclamation marks, which forces database-only lookup and makes installed packages invisible. The environment file changes the search paths to permit filesystem lookup and directs all runtime cache/format writes into this workspace.

## Prepared environment

Source this file in the shell used for both XeLaTeX and BibTeX:

    source code/environment/env.sh

The generated format is:

    .texruntime/texmf-var/web2c/xetex/xelatex.fmt

No package was installed and no global configuration was changed. The local format was generated directly from the installed xelatex.ini and latex.ltx. The system has no language.dat, so the existing hyphen.tex supplies English patterns. The supplied companion style's Babel fallback imports Russian locale data without requiring missing Russian hyphenation patterns.

## Commands for the final build

From the directory containing the generated GY1974_test.tex, its chapter, bibliography, and companion style, after sourcing env.sh:

    /usr/bin/xelatex -interaction=nonstopmode -halt-on-error -file-line-error GY1974_test.tex
    /usr/bin/bibtex GY1974_test
    /usr/bin/xelatex -interaction=nonstopmode -halt-on-error -file-line-error GY1974_test.tex
    /usr/bin/xelatex -interaction=nonstopmode -halt-on-error -file-line-error GY1974_test.tex

If the style is only in code/generation/kit rather than beside the document, additionally set:

    export TEXINPUTS="$(pwd)/code/generation/kit//:"

The trailing colon retains the default package search paths.

## Rebuilding the local format

    bash code/environment/build_format.sh

## Verification

Only the separate smoke document was compiled; no final chapter was touched. It loads the actual companion style, uses Russian text, an AMS theorem/formula, a natbib citation and the plainnat bibliography style. XeLaTeX, BibTeX, and both subsequent XeLaTeX passes returned zero, producing smoke/smoke.pdf. The last pass had no undefined citations or fatal errors.

The smoke document uses the limited system DejaVu family, which lacks italic/slanted faces and therefore issues font-substitution warnings. This is separate from the runtime failure; the chapter's packaged font files should address it. The mathematical fonts and Cyrillic text were successfully processed.
