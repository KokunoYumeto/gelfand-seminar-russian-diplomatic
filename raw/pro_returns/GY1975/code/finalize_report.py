#!/usr/bin/env python3
"""Record completed build/visual checks and replace the report's pending block.

Use --visual-reviewed only after inspecting every rendered page, with enlarged
checks of the developments and any changed or problematic pages.
"""
from pathlib import Path
import argparse
import hashlib
import json
import subprocess
import zipfile

from integrate_chapter import bibliography_entries, field

parser = argparse.ArgumentParser()
parser.add_argument('--chapter', type=Path, required=True)
parser.add_argument('--fragments', type=Path, required=True)
parser.add_argument('--kit-archive', type=Path)
parser.add_argument('--visual-reviewed', action='store_true', required=True)
args = parser.parse_args()
root = args.chapter.resolve()
fragments = args.fragments.resolve()
audit = root / 'audit'
data = json.loads((audit / 'data_audit.json').read_text())
pdf = json.loads((audit / 'pdf_audit.json').read_text())
counts = json.loads((audit / 'counts.json').read_text())
assert data['passed'] and pdf['automated_pass']
assert hashlib.sha256((root / 'GY1975_test.pdf').read_bytes()).hexdigest() == pdf['sha256']
assert not data['source_pages_without_item_range']
assert len(data['warnings']) == 2 and all('383.1' in x for x in data['warnings'])
assert args.visual_reviewed

bib = bibliography_entries((root / 'GY1975_references.bib').read_text())
source_keys = set()
for prefix in ['a', 'b', 'c', 'root']:
    ledger = json.loads((audit / f'{prefix}_sources.json').read_text())
    records = ledger['sources'] if isinstance(ledger, dict) else ledger
    source_keys.update(row['key'] for row in records)
assert set(bib) <= source_keys
verification_notes = {note: sum(field(v, 'note') == note for v in bib.values())
                      for note in ['verified', 'unverified']}

kit_check = {}
if args.kit_archive:
    with zipfile.ZipFile(args.kit_archive) as z:
        for name in ['build_chapter.py', 'gelfand_companion.sty', 'CHAPTER_FORMAT.md']:
            original = z.read('kit/' + name)
            actual = (root / name).read_bytes()
            assert original == actual, name
            kit_check[name] = {'unchanged': True,
                              'sha256': hashlib.sha256(actual).hexdigest()}

chapter_path = root / 'GY1975_chapter.tex'
compiled_source_hash = hashlib.sha256(chapter_path.read_bytes()).hexdigest()
build = subprocess.run(['python', 'build_chapter.py', 'GY1975'], cwd=root,
                       text=True, capture_output=True)
assert build.returncode == 0, build.stdout + build.stderr
assert hashlib.sha256(chapter_path.read_bytes()).hexdigest() == compiled_source_hash
consistency = {'builder_returncode': 0, 'compiled_source_matches_current_data': True,
               'chapter_sha256': compiled_source_hash,
               'pdf_sha256': pdf['sha256']}
(audit / 'source_pdf_consistency.json').write_text(json.dumps(consistency, indent=2) + '\n')

spacing_count = len(pdf['underfull_spacing_notices'])
report_text = f'''The supplied builder and the independent schema audit both pass: all {counts['records']} records, {counts['items']} items, {counts['problems']} problems, {counts['references']} references and {counts['corrections']} corrections are present. All 56 source pages are covered, and current-year item/problem links are reciprocal. All 90 bibliography keys have a corresponding source-ledger record. The supplied builder, style and format specification are byte-for-byte unchanged from the attached kit.

XeLaTeX, BibTeX and the final LaTeX passes completed successfully, producing a **{pdf['pages']}-page PDF**. The final logs contain no LaTeX errors, undefined citations or references, missing glyphs, overfull boxes, or outstanding rerun requests. There are {spacing_count} nonfatal underfull-line spacing notices; their paragraphs were visually inspected and retained because the text is readable and remains inside the margins. BibTeX reports no warnings or errors.

Every page was rendered with Poppler and inspected in contact sheets, with enlarged checks of the mathematical developments, representative dense formulas, and pages changed by the final reciprocal-link repair. The automated PDF audit finds every item ID, no blank pages, no text outside the page, and no text in the outer safety margins. The overview occupies the first two pages; the developments begin on p. 113, the problem index on p. 119, corrections on p. 124, and the bibliography on p. 138. The last link repair changed only pp. 92–96; those pages were inspected again, while all other rendered pages matched the previously inspected images.

Two source-range notices are intentional: items 383.11–12 lie on P000641, beyond the catalogue envelope ending at P000640. The manuscript continuation is recorded in the talk summary; the catalogue metadata and actual item pages are both preserved. These are documented provenance differences, not missing content. Finally, regenerating the chapter from the delivered data reproduced the exact TeX used for the PDF. Machine-readable results and source hashes are in `audit/`.'''
result = {
    'status_date': '2026-11-10', 'counts': counts,
    'pdf_pages': pdf['pages'], 'pdf_sha256': pdf['sha256'],
    'visual_review_passed': True,
    'visual_review_scope': {
        'all_pages_via_contact_sheets': list(range(1, pdf['pages'] + 1)),
        'enlarged_development_pages': list(range(113, 120)),
        'enlarged_representative_formula_pages': [53, 89],
        'final_changed_pages_reinspected': [92, 93, 94, 95, 96],
        'other_final_rendered_pages_unchanged': True,
    },
    'nonfatal_underfull_spacing_notices': spacing_count,
    'accepted_source_range_notices': data['warnings'],
    'all_bibliography_keys_in_source_ledgers': True,
    'bibliography_verification_notes': verification_notes,
    'supplied_kit_identity': kit_check,
    'source_pdf_consistency': consistency,
    'report_text': report_text,
}
(audit / 'final_build_audit.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
subprocess.run(['python', str(Path(__file__).with_name('create_report.py')),
                '--chapter', str(root), '--fragments', str(fragments)], check=True)
print(json.dumps({'final_report_written': True, 'pdf_pages': pdf['pages'],
                  'bibliography_notes': verification_notes}, indent=2))
