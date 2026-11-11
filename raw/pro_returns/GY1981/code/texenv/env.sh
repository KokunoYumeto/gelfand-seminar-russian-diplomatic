# Source this file from bash before running the chapter build.
GY_TEX_ROOT="$(CDPATH= cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
export TEXMFHOME="$GY_TEX_ROOT/texmf-home"
export TEXMFVAR="$GY_TEX_ROOT/texmf-var"
export TEXMFCONFIG="$GY_TEX_ROOT/texmf-config"
export TEXMFCACHE="$GY_TEX_ROOT/cache"
export VARTEXFONTS="$GY_TEX_ROOT/fonts-var"
export XDG_CACHE_HOME="$GY_TEX_ROOT/cache"
# Debian's packaged ls-R files point into absent /var/lib/texmf.
# Omitting !! permits normal filesystem searches in the installed trees.
export TEXMF="{$TEXMFHOME,$TEXMFVAR,/usr/share/texlive/texmf-dist,/usr/share/texmf,/etc/texmf}"
export TEXFORMATS="$GY_TEX_ROOT/formats//:"
export TEXFONTMAPS="$GY_TEX_ROOT/texmf-home/fonts/map//:"
export DVIPDFMXINPUTS="$GY_TEX_ROOT/texmf-home/dvipdfmx//:"
export XDVIPDFMXINPUTS="$GY_TEX_ROOT/texmf-home/dvipdfmx//:"
