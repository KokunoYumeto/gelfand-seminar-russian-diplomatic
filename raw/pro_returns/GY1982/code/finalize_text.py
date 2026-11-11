#!/usr/bin/env python3
"""Fill overview/report templates from the final data and verification outputs.

The templates are retained under research/root for provenance. Rebuilding the
PDF uses the already finalized overview, not this optional editorial script.
"""
from pathlib import Path
import argparse
import json
import re
from chapter_checks import bib_entries
import csv
from collections import Counter


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--directory',type=Path,required=True)
    parser.add_argument('--templates',type=Path,required=True)
    parser.add_argument('--overview-only',action='store_true')
    args=parser.parse_args()
    root=args.directory
    items=json.loads((root/'GY1982_items.json').read_text())
    problems=json.loads((root/'GY1982_problems.json').read_text())
    refs=bib_entries((root/'GY1982_references.bib').read_text())
    corrections=list(csv.DictReader((root/'GY1982_corrections.csv').open()))
    counts=Counter(x['class'] for x in items)
    literal=Counter(x['literal_correctness'] for x in items)
    values={'ITEMS':str(len(items)),'PROBLEMS':str(len(problems)),
            'REFERENCES':str(len(refs)),'CORRECTIONS':str(len(corrections)),
            **{c:str(counts[c]) for c in 'ABCDEF'},
            'MISSING_HYPOTHESES':str(literal['correct with missing hypotheses']),
            'FALSE':str(literal['false as written'])}
    assembly=json.loads((root/'code/assembly_audit.json').read_text())
    aliases={m['draft_key']:m['final_key'] for m in assembly['bibliography_mappings']}
    def fill(text):
        for key,value in values.items():text=text.replace('@@'+key+'@@',value)
        text=re.sub(r'(\\cite[pt]?\*?(?:\[[^\]]*\])*\{)([^}]+)(\})',
                    lambda m:m[1]+','.join(aliases.get(k.strip(),k.strip()) for k in m[2].split(','))+m[3],text)
        unresolved=re.findall(r'@@[A-Z_]+@@',text)
        if unresolved:raise ValueError('Unresolved placeholders: '+', '.join(unresolved))
        return text
    overview=fill((args.templates/'overview_draft.tex').read_text())
    (root/'GY1982_overview.tex').write_text(overview)
    print('Final overview counts:',dict(counts),'total',len(items))
    if args.overview_only:return
    values.update(json.loads((root/'code/report_tables.json').read_text()))
    values['REPORT_REFERENCES']=(args.templates/'report_references.md').read_text().strip()
    values['INDEPENDENT_REVIEW']=(
        'A separate reviewer also derived the same moments from '
        r'\(\mathbb E\chi_\rho([U,V])=1/\dim\rho\), using the symmetric-square, '
        'exterior-square, and adjoint character decompositions, and independently '
        'recounted adjacent plaquettes. The reviewer reopened Theorem 0.1 and '
        'Corollary 7.1 of the primary large-matrix paper and checked the hypotheses '
        'and the exchange of derivatives and limits. The isolated rerun and '
        'character computation both pass. The review records the hashes of the '
        'version reviewed; a subsequent explanatory paragraph added that same '
        'character argument without changing the result. See '
        '`research/spring_integrable/development_review.md` and its computation outputs.')
    build=json.loads((root/'code/build_logs/build_manifest.json').read_text())
    geometry=json.loads((root/'code/pdf_geometry.json').read_text())
    visual=json.loads((root/'code/visual_review.json').read_text())
    audit=json.loads((root/'code/editorial_audit.json').read_text())
    if build.get('unresolved_diagnostics') or build.get('overfull_boxes'):
        raise ValueError('Resolve final TeX diagnostics before finalizing the report.')
    if not geometry['automated_pass'] or audit['result']!='PASS' or visual['result']!='PASS':
        raise ValueError('Final verification is incomplete.')
    values['BUILD_RESULT']=(
        f"**Final result:** the {geometry['pages']}-page PDF builds successfully with "
        'no undefined citations or cross-references, no missing-glyph warnings, '
        'no LaTeX errors, and no overfull boxes. Automated inspection of every PDF '
        'page found no text outside the page, no replacement characters, and no '
        'empty pages. Rendered pages were reviewed for the overview, item layout, '
        'mathematical displays, Cyrillic quotations, development, problem index, '
        'correction entries, and bibliography; the details are recorded in '
        '`code/visual_review.json`. '
        f"The source audit covers all {audit['bibliography_entries']} bibliography entries, "
        f"and all {audit['false_as_written_items']} items marked false as written "
        'have a checked correction-ledger link. Source coverage and final statistics '
        'are recorded in `code/source_coverage.json` and the validation outputs.')
    report=fill((args.templates/'report_draft.md').read_text())
    (root/'GY1982_report.md').write_text(report)
    print('Finalized report with derived tables and completed build/visual results.')


if __name__=='__main__':main()
