#!/usr/bin/env bash
# Compile the delivered chapter. Also supports this task's minimal Debian
# image, whose TeX distribution exists but whose ls-R database/format is absent.
set -euo pipefail
chapter_dir=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
cd "$chapter_dir"

if ! kpsewhich xelatex.fmt >/dev/null 2>&1; then
  gy_tex_work="${GY1965_TEX_WORK:-$chapter_dir/build-work}"
  mkdir -p "$gy_tex_work/web2c"
  # No !! prefix: search the installed trees even without Debian's ls-R files.
  export TEXMF="{$gy_tex_work,/usr/share/texmf,/usr/share/texlive/texmf-dist}"
  export TEXFORMATS="$gy_tex_work/web2c"
  export TEXMFVAR="$gy_tex_work"
  export TEXMFCONFIG="$gy_tex_work"
  if [[ ! -f "$gy_tex_work/web2c/xelatex.fmt" ]]; then
    xetex -ini -etex -interaction=nonstopmode -halt-on-error \
      -jobname=xelatex -progname=xelatex \
      -output-directory="$gy_tex_work/web2c" xelatex.ini \
      > "$gy_tex_work/format-build.txt"
  fi
fi

mkdir -p evidence/build
python build_chapter.py GY1965 > evidence/build/builder.txt
python code/validate_chapter.py . > evidence/build/data-audit.txt
xelatex -interaction=nonstopmode -halt-on-error GY1965_test.tex > evidence/build/xelatex-pass1.txt
bibtex GY1965_test > evidence/build/bibtex.txt
xelatex -interaction=nonstopmode -halt-on-error GY1965_test.tex > evidence/build/xelatex-pass2.txt
xelatex -interaction=nonstopmode -halt-on-error GY1965_test.tex > evidence/build/xelatex-pass3.txt
cp GY1965_test.log evidence/build/final-xelatex.log
cp GY1965_test.blg evidence/build/final-bibtex.log
printf '%s\n' 'Chapter data audit and XeLaTeX/BibTeX build completed.'
