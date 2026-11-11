#!/usr/bin/env bash
# Rebuild from the seven authoritative GY1969 data files.
set -euo pipefail
gy_task_root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
cd "$gy_task_root"
mkdir -p output

# Some minimal Debian images contain TeX Live files but no ls-R database or
# generated formats. Use the existing files and a workspace-local format.
if ! kpsewhich xelatex.fmt >/dev/null 2>&1; then
    export TEXMF='{.,/usr/share/texmf,/usr/share/texlive/texmf-dist}'
    export TEXFORMATS="$gy_task_root/output/texformats:"
    mkdir -p output/texformats
    if [ ! -f output/texformats/xelatex.fmt ]; then
        (
            cd output/texformats
            xetex -ini -etex -jobname=xelatex -interaction=nonstopmode \
                -halt-on-error xelatex.ini > ../format.log 2>&1
        )
    fi
fi

python build_chapter.py GY1969 > output/builder.log 2>&1
python code/check_dataset.py . > output/dataset_audit.json
xelatex -interaction=nonstopmode -halt-on-error GY1969_test.tex > output/xelatex_pass1.log 2>&1
bibtex GY1969_test > output/bibtex.log 2>&1
xelatex -interaction=nonstopmode -halt-on-error GY1969_test.tex > output/xelatex_pass2.log 2>&1
xelatex -interaction=nonstopmode -halt-on-error GY1969_test.tex > output/xelatex_pass3.log 2>&1
python code/verify_annotations.py > output/verify_annotations.json
python code/verify_four_subspaces.py > output/verify_four_subspaces.json
python code/build_summary.py . > output/build_summary.json
