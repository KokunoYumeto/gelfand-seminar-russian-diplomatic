"""Prepare the reviewed chapter archive from its research workspace.

Usage: python prepare_release.py WORK_DIRECTORY INPUT_DIRECTORY RELEASE_DIRECTORY
This copies approved source attachments and reviewed outputs, records visual-QA
provenance, and writes reproduction instructions. It performs no network access.
"""
from pathlib import Path
import hashlib
import importlib.metadata
import json
import shutil
import sys

work, uploads, release = [Path(p).resolve() for p in sys.argv[1:4]]
chapter = work / 'deliverable'
qa = work / 'qa_release'
release.mkdir(parents=True, exist_ok=True)

def copy(source, destination):
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

root_files = [
    'GY1972_talks.json', 'GY1972_items.json', 'GY1972_problems.json',
    'GY1972_overview.tex', 'GY1972_development.tex', 'GY1972_corrections.csv',
    'GY1972_references.bib', 'GY1972_report.md', 'GY1972_chapter.tex',
    'GY1972_test.tex', 'GY1972_test.pdf', 'GY1972_test.bbl',
    'GY1972_test.blg', 'GY1972_test.log', 'GY1972_test.aux', 'GY1972_test.out',
    'build_chapter.py', 'gelfand_companion.sty', 'assembly_metrics.json',
    'validation_summary.json',
]
for name in root_files:
    copy(chapter/name, release/name)
for directory in ['fonts', 'logs']:
    for source in (chapter/directory).rglob('*'):
        if source.is_file() and source.name != 'interrupted_auxiliary.txt':
            copy(source, release/source.relative_to(chapter))

code = release/'code'
for name in ['assemble.py', 'compile_chapter.py', 'audit_deliverable.py',
             'render_qa.py', 'prepare_release.py', 'package_release.py',
             'check_reproduction.py']:
    copy(work/name, code/name)
for source in (work/'batches').rglob('*'):
    if source.is_file() and '__pycache__' not in source.parts:
        copy(source, code/source.relative_to(work))
for source in (work/'kit').iterdir():
    if source.is_file():
        copy(source, code/'kit_original'/source.name)
for name in ['previous_index.md', 'references_cumulative.bib']:
    copy(work/name, release/'inputs'/name)
    # The cross-batch reconciliation script reads these beside its batches.
    copy(work/name, code/name)
for name in ['GY1972_prompt.md', 'GY1972_talks.md', 'GY1972_en.tex',
             'GY1972_ru.tex', 'GY1972_scans.zip', 'GY1972_kit.zip']:
    copy(uploads/name, release/'inputs'/name)

for source in qa.iterdir():
    if source.is_file() and source.suffix in ('.png', '.json'):
        copy(source, release/'qa'/source.name)
render = json.loads((qa/'render_summary.json').read_text())
validation = json.loads((chapter/'validation_summary.json').read_text())
assert validation['status'] == 'passed'
assert validation['pdf_sha256'] == sha(chapter/'GY1972_test.pdf')
assert validation['pdf_pages'] == render['pdf_pages'] == 142

reviewers = {
    'early': {'pages': [1,48], 'detail_pages': [1,2,4,29,45]},
    'buchstaber': {'pages': [49,96], 'detail_pages': [49,52,54,68,79,94]},
    'topology': {'pages': [97,142], 'detail_pages': [104,108,113,114,115,116,119,121,130,136,142]},
}
for batch, scope in reviewers.items():
    file = code/'batches'/batch/'visual_review.md'
    assert file.is_file(), f'Missing visual review: {batch}'
    scope['review_file'] = str(file.relative_to(release))
    scope['review_sha256'] = sha(file)
unchanged = all((work/'qa_final'/'pages'/f'page-{n:03d}.png').read_bytes()
                == (qa/'pages'/f'page-{n:03d}.png').read_bytes()
                for n in range(1,97))
assert unchanged, 'A page previously reviewed changed in the final rebuild.'
visual = {
    'status': 'passed', 'review_date': '2026-11-09',
    'pdf_sha256': validation['pdf_sha256'], 'pdf_pages': 142,
    'all_pages_rendered': True, 'all_contact_sheets_inspected': True,
    'reviewers': reviewers, 'primary_reviewer_detail_pages': [1,113,114,142],
    'first_96_rendered_pages_identical_to_prior_review': unchanged,
    'observations': [
        'No clipping, text collisions, missing glyphs, broken headings or severe whitespace were found.',
        'Russian quotations, mathematical subscripts, fractions and displayed equations are legible in the inspected details.',
        'The overview table, corrective proof, correction entries and bibliography were inspected.',
        'The final engine log has zero overfull boxes and twelve underfull horizontal boxes; the reviewed spacing is acceptable.',
    ],
    'layout_adjustments': {
        'equation_or_citation_layout_items': ['1972-278.7','1972-279.4','1972-282.5',
            '1972-283.5','1972-283.6','1972-283.12','1972-284.6','1972-291.18','1972-294.8'],
        'fonts': 'Four DejaVu Serif faces bundled with their license; original supplied style and builder are unchanged.',
        'other': 'Explicit spacing after editorial proof markers and prose date/locator spacing.',
    },
    'page_render_sha256': {p.name:sha(p) for p in sorted((qa/'pages').glob('page-*.png'))},
    'included_image_sha256': {p.name:sha(p) for p in sorted((release/'qa').glob('*.png'))},
}
(release/'visual_qa.json').write_text(json.dumps(visual,ensure_ascii=False,indent=2)+'\n')
render['manual_visual_review'] = 'passed; see ../visual_qa.json and the three individual reviews'
render['pdf_sha256'] = validation['pdf_sha256']
(release/'qa/render_summary.json').write_text(json.dumps(render,ensure_ascii=False,indent=2)+'\n')

environment = {
    'python': sys.version,
    'PyMuPDF': importlib.metadata.version('PyMuPDF'),
    'Pillow': importlib.metadata.version('Pillow'),
    'tex_engine': json.loads((chapter/'logs/compile_summary.json').read_text())['engine'],
    'fonts': 'DejaVu Serif regular, bold, italic and bold italic; see fonts/LICENSE.txt',
    'runtime_cache_included': False,
}
(release/'build_environment.json').write_text(json.dumps(environment,indent=2)+'\n')
(release/'code/requirements-qa.txt').write_text('PyMuPDF\nPillow\n')

readme = r'''GY1972 — Critical companion to the I. M. Gelfand seminar, 1972–73
======================================================================
Status cutoff: 9 November 2026

START HERE
----------
GY1972_test.pdf is the complete 142-page chapter. GY1972_report.md gives
the coverage, counts, evidentiary limits, development decision, independent
checks and recommendations for the companion website.

28 catalogue records (27 talks and one heading); 272 mathematical items;
A 25, B 14, C 1, D 0, E 219, F 13; 11 problem entries;
73 references; 112 corrections and provenance entries.

The seven required machine-readable/LaTeX files are at the archive root,
along with the generated chapter, standalone driver, compiled PDF and report.
The supplied build_chapter.py and gelfand_companion.sty are unchanged.

SCOPE AND EVIDENCE
------------------
The requested 28 records follow actual manuscript order, including the
5 March order 290, 292, 291 and the 26 March order 296, 298, 297.
P000449 and P000480 already have occurrence owners in the supplied earlier
index. Their ownership is disclosed; duplicate items have not been invented.
Record 286 is a heading, not an additional lecture.

Class records historical fate, not truth. Literal correctness, exactness of
the publication match, confidence and verification level remain separate.
A bibliography note 'verified' records an opened URL/DOI; the annote field
and each item's verification field explain how much was actually checked.
The evidence logs preserve locators and inconclusive searches. A source's
absence from a search result was not treated as evidence of class D.

No C/D item provided a warranted bounded new research target. The sole C
item is explicitly a reconstructed all-degree G/O computation programme;
no particular finite-degree group is asserted to remain unknown. The full
development is instead a corrective proof for the false published flag
assertion in 1972-280.20 (class A). It includes a general-ring counterexample,
an exact support criterion, stabilization and minimal-rank arguments.
Editorial proof/computation markers identify work supplied here, not claims
of historical novelty. Finite calculations do not replace the general proofs.

BUILD THE CHAPTER
-----------------
Requirements: Python 3.10 or later; XeLaTeX and BibTeX; the LaTeX packages
used by the supplied style. Four DejaVu Serif font files and their license
are included. No network connection is required to build or run checks.

From this archive's root:

    python build_chapter.py GY1972
    xelatex -interaction=nonstopmode -halt-on-error GY1972_test.tex
    bibtex GY1972_test
    xelatex -interaction=nonstopmode -halt-on-error GY1972_test.tex
    xelatex -interaction=nonstopmode -halt-on-error GY1972_test.tex

Alternatively, the recorded build driver runs the same required sequence,
starts with clean auxiliary streams, records logs and handles the supplied
runtime's missing system TeX filename database/format without global writes:

    python code/compile_chapter.py .

The local format/cache is regenerated if needed and is not in this archive.
First-pass citation warnings are resolved by BibTeX and later passes. The
final log has no errors, undefined citations/references, missing glyphs or
overfull boxes. Its 12 underfull horizontal boxes were visually reviewed.
Rebuilding can change PDF metadata and hence its byte hash without changing
the chapter. build_environment.json records the production environment.

REASSEMBLE THE REVIEWED DATA
---------------------------
The reviewed checkpoint files are code/batches/{early,buchstaber,topology,root}.
They include source extracts, evidence logs, bibliography verification notes,
authoring scripts, mathematical check scripts and outputs. To regenerate the
seven chapter files and report from those reviewed checkpoints:

    python code/assemble.py .
    python code/compile_chapter.py .

The assembler preserves the fixed schema, orders records, reconciles spacing
and applies the documented equation-layout adjustments. It does not rerun
literature searches or silently revise mathematical claims. Authoring scripts
are retained for traceability; the checked batch data are the release inputs.

The release reproduction check regenerated all 11 source/metrics files in a
temporary directory and found them byte-for-byte identical. Its output is
reproduction_summary.json. To repeat that source-only check:

    python code/check_reproduction.py .

MATHEMATICAL CHECKS AND OUTPUTS
------------------------------
All these computations use the Python standard library only:

    python code/batches/early/check_tolerance.py
        -> code/batches/early/tolerance_output.json
    python code/batches/root/independent_flag_check.py
        -> code/batches/root/independent_flag_check.json
    python code/batches/buchstaber/formal_checks.py
        -> stdout, saved as code/batches/buchstaber/formal_checks.txt
    python code/batches/topology/checks.py
        -> stdout, saved as code/batches/topology/checks_output.txt
    python code/batches/root/check_arithmetic.py
        -> code/batches/root/arithmetic_output.json
    python code/batches/early/independent_audit_checks.py
        -> code/batches/early/independent_audit_checks.json

The flag checks use different implementations and parameter sets. The
independent arithmetic code imports no primary arithmetic code. Separate
proof reviews of the modular measure, G/O scope, Berezin normalizations,
Henkin hypotheses and the other reconstructions are included in evidence.md,
early/root_review.md and buchstaber/p_adic_independent_audit.md.

DATA AND PDF AUDITS
-------------------
The final data/PDF audit uses PyMuPDF; rendering also uses Pillow and Poppler
(pdftoppm). Package names are in code/requirements-qa.txt.

    python code/audit_deliverable.py . inputs/previous_index.md
    python code/batches/early/audit_final_batches.py
    python code/batches/topology/validate_batch.py
    python code/batches/buchstaber/audit_cross_batch.py
    python code/render_qa.py . qa_regenerated

validation_summary.json records the passing release audit. visual_qa.json
records manual inspection scope, the three reviewers' files, final PDF hash
and rendered-page hashes. All 142 pages were rendered; all 12 numbered contact
sheets and the listed full-page details were inspected. The archive includes
those sheets and details. Individual low-resolution page PNGs can be regenerated
with render_qa.py. Re-rendering starts a new manual-review record; it does not
automatically certify visual quality.

The batch marker audit includes three heuristic review candidates, explained
as false positives in early/root_review.md; it has zero errors or warnings.
Original source attachments and extracted previous-index/bibliography inputs
are in inputs/. The original kit is also retained under code/kit_original/.
No downloaded third-party mathematical source PDF is redistributed here.

ARCHIVE INTEGRITY
-----------------
manifest.json lists every payload file with its size and SHA-256 checksum;
it excludes itself to avoid a recursive checksum. To verify an extracted
archive, run:

    python code/package_release.py . --verify

To regenerate a ZIP after an intentional edit and validation:

    python code/package_release.py . --zip ../GY1972.zip

The package command refreshes the manifest, checks ZIP CRC integrity and
compares every archived payload against its manifest. It does not replace
the mathematical, data or visual reviews.
'''
(release/'README.txt').write_text(readme)
print(json.dumps({'release_directory':str(release),'status':'prepared',
                  'pdf_pages':142,'payload_files':sum(p.is_file() for p in release.rglob('*'))},indent=2))
