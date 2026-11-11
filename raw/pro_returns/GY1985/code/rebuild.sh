#!/usr/bin/env bash
set -euo pipefail
chapter_dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)
python3 "$chapter_dir/code/build_all.py" "$chapter_dir"
python3 "$chapter_dir/code/validate_chapter.py" "$chapter_dir"
