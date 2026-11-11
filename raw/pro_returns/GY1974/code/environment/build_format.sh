#!/usr/bin/env bash
set -eu
source "$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)/env.sh"
mkdir -p "$TEXMFVAR/web2c/xetex"
cd "$TEXMFVAR/web2c/xetex"
xetex -ini -etex -jobname=xelatex -progname=xelatex \
  -interaction=nonstopmode -halt-on-error xelatex.ini
