#!/usr/bin/env python3
"""Inspect all PDF pages and optionally render representative page PNGs.

Requires PyMuPDF. Text geometry is a supplementary automated check; the
rendered images are reviewed separately for actual layout and readability.
"""
from pathlib import Path
import argparse
import json
import re
import fitz


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pdf',type=Path)
    parser.add_argument('--report',type=Path,default=Path('code/pdf_geometry.json'))
    parser.add_argument('--render-directory',type=Path)
    parser.add_argument('--pages',help='Comma-separated one-based pages, or all')
    args=parser.parse_args()
    doc=fitz.open(args.pdf)
    problems=[]
    result={'pages':len(doc),'page_sizes':{},'out_of_page_text':[],
            'replacement_characters':[],'empty_pages':[],
            'section_starts':[],'page_text_lengths':[],'internal_links':0,
            'external_links':0,'invalid_internal_links':[],'rendered_pages':[]}
    for number,page in enumerate(doc,1):
        size=f'{page.rect.width:.2f} x {page.rect.height:.2f} pt'
        result['page_sizes'][size]=result['page_sizes'].get(size,0)+1
        text=page.get_text()
        result['page_text_lengths'].append(len(text))
        if len(text.strip())<5:
            result['empty_pages'].append(number)
        if '\ufffd' in text:
            result['replacement_characters'].append(number)
        for block in page.get_text('dict')['blocks']:
            for line in block.get('lines',[]):
                for span in line.get('spans',[]):
                    x0,y0,x1,y1=span['bbox']
                    if x0 < -0.5 or y0 < -0.5 or x1 > page.rect.width+0.5 or y1 > page.rect.height+0.5:
                        result['out_of_page_text'].append({'page':number,'bbox':span['bbox'],'text':span['text']})
        for marker in ('Developments','Problem index','Corrections to the transcription','Bibliography'):
            if marker in text:
                result['section_starts'].append({'page':number,'text':marker})
        for link in page.get_links():
            if link.get('kind')==fitz.LINK_GOTO or (link.get('kind')==fitz.LINK_NAMED and 'nameddest' in link):
                result['internal_links']+=1
                if not 0<=link.get('page',-1)<len(doc):
                    result['invalid_internal_links'].append({'page':number,'destination':link.get('nameddest',str(link))})
            elif link.get('kind')==fitz.LINK_URI:
                result['external_links']+=1
    if args.render_directory:
        args.render_directory.mkdir(parents=True,exist_ok=True)
        if args.pages=='all':
            pages=range(1,len(doc)+1)
        elif args.pages:
            pages=[int(s) for s in args.pages.split(',')]
        else:
            pages=sorted(set([1,2,len(doc)]+[r['page'] for r in result['section_starts']]))
        for number in pages:
            if not 1<=number<=len(doc):
                raise ValueError('Page out of range: '+str(number))
            destination=args.render_directory/f'page_{number:03d}.png'
            doc[number-1].get_pixmap(matrix=fitz.Matrix(1.5,1.5)).save(destination)
            result['rendered_pages'].append(number)
    for key in ('out_of_page_text','replacement_characters','empty_pages','invalid_internal_links'):
        if result[key]:
            problems.append(key)
    result['automated_pass']=not problems
    result['visual_review_required']=True
    args.report.parent.mkdir(parents=True,exist_ok=True)
    args.report.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='page_text_lengths'},ensure_ascii=False,indent=2))
    raise SystemExit(bool(problems))


if __name__=='__main__':
    main()
