"""Reproducible source-page extraction and scope inventory for GY1964."""
from pathlib import Path
import re
import json
import sys

WORK = Path(__file__).resolve().parents[1]
INPUTS = Path(sys.argv[1]) if len(sys.argv)>1 else WORK.parent / "upload"
out = WORK / "source_pages"
out.mkdir(exist_ok=True)
inventory = {}
for language in ("en", "ru"):
    source = (INPUTS / f"GY1964_{language}.tex").read_text()
    matches = list(re.finditer(r"(?m)^\\SourcePage\{GELFAND-P(\d{6})\}\{([^}]*)\}", source))
    inventory[language] = []
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(source)
        body = source[m.start():end]
        page = f"P{m.group(1)}"
        (out / f"{page}_{language}.tex").write_text(body)
        inventory[language].append({"page": page, "label": m.group(2),
                                    "characters": len(body),
                                    "unclear_marks": body.count("\\Unclear{"),
                                    "first_line": body.splitlines()[1] if len(body.splitlines()) > 1 else ""})
    assert len(inventory[language]) == 90
(WORK / "evidence" / "page_inventory.json").write_text(json.dumps(inventory, ensure_ascii=False, indent=2) + "\n")
print("Extracted 90 pages in each of Russian and English; source files unchanged.")
for row in inventory["en"]:
    print(f"{row['page']}: {row['characters']:5} chars, {row['unclear_marks']:2} uncertainty marks; {row['first_line'][:110]}")
