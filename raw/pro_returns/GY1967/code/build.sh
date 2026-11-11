#!/usr/bin/env bash
# Rebuild the supplied driver with the amended, audited chapter builder.
set -euo pipefail
chapter_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$chapter_root"
mkdir -p audit

# A normal TeX Live installation needs no overrides. The authoring workspace
# had the binaries and source tree but an incomplete format/search database.
if ! kpsewhich -engine=xetex -format=fmt xelatex.fmt >/dev/null 2>&1; then
  task_texmf_default='{/usr/share/texlive/texmf-dist,/usr/share/texmf}'
  export TEXMF="${GY1967_TEXMF:-$task_texmf_default}"
  export TEXMFVAR="$chapter_root/.build-cache/texmf-var"
  export TEXFORMATS="$TEXMFVAR/web2c/xetex"
  mkdir -p "$TEXFORMATS"
  if [[ ! -s "$TEXFORMATS/xelatex.fmt" ]]; then
    (
      cd "$TEXFORMATS"
      xetex -ini -etex -jobname=xelatex -interaction=nonstopmode \
        -halt-on-error xelatex.ini
    ) > "$chapter_root/audit/tex_format_build.txt" 2>&1
  fi
fi

python3 build_chapter.py GY1967 > audit/build_output.txt 2>&1
xelatex -interaction=nonstopmode -halt-on-error GY1967_test.tex \
  > audit/xelatex_pass1_stdout.txt 2>&1
bibtex GY1967_test > audit/bibtex_stdout.txt 2>&1
xelatex -interaction=nonstopmode -halt-on-error GY1967_test.tex \
  > audit/xelatex_pass2_stdout.txt 2>&1
xelatex -interaction=nonstopmode -halt-on-error GY1967_test.tex \
  > audit/xelatex_pass3_stdout.txt 2>&1
printf '%s\n' 'Built GY1967_chapter.tex and GY1967_test.pdf successfully.'
