#!/usr/bin/env python3
"""Fill report/overview tables from the assembled chapter data, never by hand."""
from pathlib import Path
import argparse
import json


def table(columns, rows):
    result = ['| ' + ' | '.join(columns) + ' |',
              '| ' + ' | '.join('---' for _ in columns) + ' |']
    result += ['| ' + ' | '.join(str(x) for x in row) + ' |' for row in rows]
    return '\n'.join(result)


def main():
    base = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser()
    parser.add_argument('--chapter', type=Path, default=base / 'chapter')
    parser.add_argument('--fragments', type=Path, default=base / 'fragments')
    args = parser.parse_args()
    counts = json.loads((args.chapter / 'audit/counts.json').read_text())
    values = {k.upper(): str(counts[k]) for k in ['items', 'problems', 'references', 'corrections']}
    values.update({k: str(counts['by_class'].get(k, 0)) for k in 'ABCDEF'})
    classes = {'A': 'Published soon after by speaker or Gelfand',
               'B': 'Developed by others into established results',
               'C': 'Partly developed, with a specified remaining question',
               'D': 'Not developed after documented search',
               'E': 'Known before the talk',
               'F': 'Not identifiable from the notes'}
    values['CLASS_TABLE'] = table(['Class', 'Meaning', 'Items', 'Share'],
        [(k, classes[k], counts['by_class'].get(k, 0),
          f"{100*counts['by_class'].get(k,0)/counts['items']:.1f}%") for k in 'ABCDEF'])
    values['SPEAKER_TABLE'] = table(['Catalogue speaker', 'Items'],
        sorted(counts['by_record_speaker'].items(), key=lambda x: (-x[1], x[0])))
    values['ATTRIBUTION_TABLE'] = table(['Attributed speaker or explicit joint attribution', 'Items'],
        sorted(counts['by_attributed_speaker'].items(), key=lambda x: (-x[1], x[0])))
    values['AREA_TABLE'] = table(['Primary area', 'Items'],
        sorted(counts['by_area'].items(), key=lambda x: (-x[1], x[0])))
    headings = [('Literal correctness', 'by_literal_correctness'),
                ('Publication match', 'by_publication_match'),
                ('Verification level', 'by_verification'),
                ('Development', 'by_development')]
    values['ASSESSMENT_TABLES'] = '\n\n'.join('**' + title + '**\n\n' +
        table([title, 'Items'], sorted(counts[key].items(), key=lambda x: (-x[1], x[0])))
        for title, key in headings)
    values['CORRECTION_TABLE'] = table(['Correction category', 'Entries'],
        sorted(counts['corrections_by_type'].items(), key=lambda x: (-x[1], x[0])))
    build_audit_path = args.chapter / 'audit/final_build_audit.json'
    if build_audit_path.exists():
        audit = json.loads(build_audit_path.read_text())
        values['BUILD_RESULT'] = audit['report_text']
    else:
        values['BUILD_RESULT'] = 'Final build and visual inspection are pending in this authoring snapshot.'
    for suffix in ['overview.tex', 'report.md']:
        text = (args.fragments / ('root_' + suffix.replace('.', '_template.'))).read_text()
        for key, value in values.items():
            text = text.replace('@@' + key + '@@', value)
        if '@@' in text:
            raise ValueError('Unfilled template marker in ' + suffix)
        (args.fragments / ('root_' + suffix)).write_text(text)
        (args.chapter / ('GY1975_' + suffix)).write_text(text)
    print('Updated report and overview from', counts['items'], 'items.')


if __name__ == '__main__':
    main()
