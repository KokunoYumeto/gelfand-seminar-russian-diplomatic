# Source this file before invoking the installed XeLaTeX or BibTeX.
# Only runtime state under this workspace is written.
GY_TEX_RUNTIME="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/../.." && pwd)/.texruntime"
export TEXMFVAR="$GY_TEX_RUNTIME/texmf-var"
export TEXMFCONFIG="$GY_TEX_RUNTIME/texmf-config"
export TEXMF="{$TEXMFCONFIG,$TEXMFVAR,/etc/texmf,/usr/share/texmf,/usr/share/texlive/texmf-dist}"
export TEXFORMATS="$TEXMFVAR/web2c/xetex:"
export VARTEXFONTS="$GY_TEX_RUNTIME/fonts"
export TEXMFCACHE="$GY_TEX_RUNTIME/cache"
export XDG_CACHE_HOME="$GY_TEX_RUNTIME/cache"
export FONTCONFIG_FILE=/etc/fonts/fonts.conf
export FONTCONFIG_PATH=/etc/fonts
