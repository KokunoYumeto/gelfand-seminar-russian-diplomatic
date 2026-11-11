#!/usr/bin/env python3
"""Compare reviewed and final Poppler renders after limited editorial changes.

The two directories are outputs of render_review.py. Intermediate page images
are not distributed; this script and its result document the final QA delta.
Changed pages are rendered at 120 dpi for actual visual inspection.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import argparse
import hashlib
import json
import subprocess
from PIL import Image, ImageChops
import fitz


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--baseline',type=Path,required=True)
    parser.add_argument('--final',type=Path,required=True)
    parser.add_argument('--index',type=Path,required=True)
    parser.add_argument('--report',type=Path,required=True)
    args=parser.parse_args()
    baseline=json.loads((args.baseline/'render_index.json').read_text())
    final=json.loads(args.index.read_text())
    pdf=Path(final['pdf'])
    if hashlib.sha256(pdf.read_bytes()).hexdigest()!=final['sha256']:
        raise ValueError('Final PDF changed after rendering.')
    if baseline['pages']!=final['pages']:
        raise ValueError('Pagination changed; a complete new visual review is required.')
    before=sorted((args.baseline/'thumbnails').glob('page-*.png'))
    after=sorted((args.final/'thumbnails').glob('page-*.png'))
    if len(before)!=final['pages'] or len(after)!=final['pages']:
        raise ValueError('Incomplete page-render set.')
    changed=[]
    unchanged=[]
    for number,(a,b) in enumerate(zip(before,after),1):
        ia=Image.open(a).convert('RGB');ib=Image.open(b).convert('RGB')
        if ia.size!=ib.size:raise ValueError('Page geometry changed.')
        bbox=ImageChops.difference(ia,ib).getbbox()
        if bbox:changed.append({'page':number,'changed_pixel_bbox':list(bbox)})
        else:unchanged.append(number)
    original_pdf=args.baseline/'GY1982_test.pdf'
    original=fitz.open(original_pdf); current=fitz.open(pdf)
    text_changes=[n+1 for n in range(len(current))
                  if original[n].get_text()!=current[n].get_text()]
    existing={entry['page']:entry['file'] for entry in final['detail_pages']}
    details=args.final/'details';details.mkdir(exist_ok=True)
    def render(entry):
        number=entry['page']
        if number in existing:
            return {'page':number,'file':existing[number]}
        path=details/f'page_{number:03d}'
        run=subprocess.run(['pdftoppm','-f',str(number),'-l',str(number),
                            '-r','120','-singlefile','-png',str(pdf),str(path)],
                           stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
        if run.returncode:raise RuntimeError(run.stdout)
        return {'page':number,'file':str(path.with_suffix('.png').resolve())}
    with ThreadPoolExecutor(max_workers=3) as pool:
        changed_details=list(pool.map(render,changed))
    final['additional_detail_pages']=[entry for entry in changed_details
                                       if entry['page'] not in existing]
    args.index.write_text(json.dumps(final,ensure_ascii=False,indent=2)+'\n')
    result={'baseline_sha256':baseline['sha256'],'final_sha256':final['sha256'],
            'pages':final['pages'],'comparison_dpi':60,
            'unchanged_pixel_pages':unchanged,'changed_pixel_pages':changed,
            'changed_text_pages':text_changes,'changed_detail_pages':changed_details,
            'interpretation':'Unchanged page pixels carry forward the recorded v3 visual inspection. Every changed page requires a new detail-page review.'}
    args.report.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'pages':final['pages'],'unchanged_pixels':len(unchanged),
                      'changed_pixel_pages':[x['page'] for x in changed],
                      'changed_text_pages':text_changes},indent=2))


if __name__=='__main__':main()
