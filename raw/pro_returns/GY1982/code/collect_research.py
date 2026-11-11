#!/usr/bin/env python3
"""Collect audit records, authoring code, and computation output for delivery.

Full external papers, rendered scans and temporary build products are excluded.
The final root-level data remain authoritative over the archived research drafts.
"""
from pathlib import Path
import argparse
import json
import shutil


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--directory',type=Path,required=True)
    parser.add_argument('--shards',type=Path,required=True)
    parser.add_argument('--root-research',type=Path,required=True)
    parser.add_argument('--previous-index',type=Path,required=True)
    parser.add_argument('--cumulative',type=Path,required=True)
    parser.add_argument('--catalog',type=Path,required=True)
    args=parser.parse_args()
    destination=args.directory/'research'
    copied=[]
    for group in ['autumn_physics','winter_geometry','spring_integrable']:
        source=args.shards/group
        target=destination/group
        target.mkdir(parents=True,exist_ok=True)
        for file in sorted(source.iterdir()):
            if not file.is_file():continue
            is_output_text=file.name.endswith('_output.txt') or file.name=='root_haar_rerun.txt'
            if file.suffix not in {'.py','.json','.csv','.bib','.md'} and not is_output_text:continue
            shutil.copy2(file,target/file.name)
            if group=='autumn_physics' and file.name=='research_notes.md':
                note=(target/file.name).read_text()
                note=note.replace('Speaker V. only in manuscript; catalogue V.L. conflicts with probable mathematical V.A. attribution, recorded as provenance.',
                    'The manuscript gives only V. Ginzburg; the supplied catalogue gives V. L. Ginzburg. These are preserved without inferring a different speaker from related publications. V. A. Ginzburg’s 1983 paper is a mathematical comparison source, not speaker-identification evidence. The earlier preference for V. A. was withdrawn in the final provenance review.')
                note=note.replace('570 retains catalogueV.L.Ginzburg with the V.A. identification caveat in its body;',
                    '570 retains catalogue V. L. Ginzburg without preferring V. A. as the speaker;')
                (target/file.name).write_text(note)
            copied.append((target/file.name).relative_to(args.directory).as_posix())
    target=destination/'root'
    target.mkdir(parents=True,exist_ok=True)
    for name in ['research_notes.md','source_audit.json','write_audit.py','references.bib',
                 'overview_draft.tex','report_draft.md','report_references.md','provenance_review.md',
                 'root_visual_review.json']:
        shutil.copy2(args.root_research/name,target/name)
        copied.append((target/name).relative_to(args.directory).as_posix())
    target=destination/'inputs'
    target.mkdir(parents=True,exist_ok=True)
    for source,name in [(args.previous_index,'previous_index.md'),
                        (args.cumulative,'references_cumulative.bib'),
                        (args.catalog,'GY1982_talks.md')]:
        shutil.copy2(source,target/name)
        copied.append((target/name).relative_to(args.directory).as_posix())
    result={'files_copied':len(copied),'files':copied,
            'excluded':'Full external papers, source scan images, temporary renders and build products.'}
    (args.directory/'code/research_collection.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print('Collected',len(copied),'research, authoring, input-index and verification files.')


if __name__=='__main__':main()
