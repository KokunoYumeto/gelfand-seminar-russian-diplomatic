"""Escape literal prose specials while preserving explicitly delimited TeX math.

Data fields accept LaTeX. This deliberately does not rewrite mathematics or
citations. The authoring fragments occasionally contain plain file names such
as previous_index or plain-text formula descriptions in corrections.
"""
import re


def escape_prose_specials(text):
    replacements = {'_': r'\_', '^': r'\textasciicircum{}',
                    '&': r'\&', '#': r'\#', '%': r'\%'}
    tokens = re.split(r'(\\\([\s\S]*?\\\)|\\\[[\s\S]*?\\\]|'
                      r'(?<!\\)\$\$[\s\S]*?(?<!\\)\$\$|'
                      r'(?<!\\)\$[^$]*(?<!\\)\$|'
                      r'\\(?:url|href)\{[^}]*\}|'
                      r'\\cite\w*\*?(?:\[[^\]]*\])*\{[^}]+\})', text)
    changes = []
    for index in range(0, len(tokens), 2):
        value = tokens[index]
        def replace(m):
            changes.append(m[0])
            return replacements[m[0]]
        tokens[index] = re.sub(r'(?<!\\)[_\^&#%]', replace, value)
    return ''.join(tokens), changes


def normalize_record(record, fields):
    changes = {}
    for field in fields:
        if record.get(field):
            value, marker_spaces = re.subn(r'\\(ours(?:Computed)?)(?=\s)',
                                          lambda m: m[0] + '{}', record[field])
            record[field], changed = escape_prose_specials(value)
            if marker_spaces:
                changed.append('explicit space after editorial marker')
            if changed:
                changes[field] = changed
    return changes
