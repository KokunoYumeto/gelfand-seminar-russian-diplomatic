#!/usr/bin/env python3
"""Consolidate the actual visual inspections performed for this chapter.

The page lists record completed image inspections; this script does not
inspect images automatically. It joins those attestations to pixel comparisons
and requires the final PDF hash to match the reviewed render index.
"""
from pathlib import Path
import argparse
import hashlib
import json


def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def read(path):return json.loads(path.read_text())


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--directory',type=Path,required=True)
    parser.add_argument('--work',type=Path,required=True)
    args=parser.parse_args()
    root=args.directory;work=args.work
    final=read(root/'code/render_index.json')
    first=read(root/'code/render_comparison_v3_v4.json')
    second=read(root/'code/render_comparison.json')
    if first['final_sha256']!=second['baseline_sha256']:
        raise ValueError('Disconnected render-comparison chain.')
    if second['final_sha256']!=final['sha256'] or digest(root/'GY1982_test.pdf')!=final['sha256']:
        raise ValueError('Final PDF or rendering changed after review.')
    baseline_hash=first['baseline_sha256'];v4_hash=first['final_sha256']
    root_pages={'v3':[1,2,4,7,20,63],
                'v4':[4,7,9,13,15,17],
                'v5':[4,8,10,11,13,17]}
    assignments={
        'v3':{'root':root_pages['v3'],
              'winter_geometry':[71,85,92,103,108,118,127,147,148,158,169,170,179],
              'spring_integrable':[55,56,60,136,139,140,141,142]},
        'v4':{'root':root_pages['v4'],
              'winter_geometry':[148,149,150,151,152,153,154,169,179],
              'spring_integrable':[142]},
        'v5':{'root':root_pages['v5'],
              'winter_geometry':[150,151,152],
              'spring_integrable':[115]}}
    hashes={'v3':baseline_hash,'v4':v4_hash,'v5':final['sha256']}
    filenames={'v3':'final_visual_review.json','v4':'final_delta_review.json',
               'v5':'final_copy_review.json'}
    sources=[]
    for version,groups in assignments.items():
        for group in ['winter_geometry','spring_integrable']:
            path=work/'agents'/group/filenames[version]
            text=path.read_text()
            if hashes[version] not in text or 'PASS' not in text:
                raise ValueError('Missing or inconsistent reviewer attestation: '+str(path))
            sources.append({'version':version,'reviewer':group,
                            'record':'research/'+group+'/'+path.name,
                            'pages':groups[group],'record_sha256':digest(path)})
    for comparison,version in [(first,'v4'),(second,'v5')]:
        changed={entry['page'] for entry in comparison['changed_pixel_pages']}
        reviewed={n for pages in assignments[version].values() for n in pages}
        if changed!=reviewed:raise ValueError('Changed-page review coverage differs: '+version)
    own={'review_date':'2026-11-11','reviewer':'root',
         'method':'Actual view_image inspection of listed contact sheets and detail pages.',
         'baseline_contact_pages':list(range(1,81)),
         'contact_sheets':[], 'detail_reviews':[],
         'findings':'No clipping or overlap. Initial prose-spacing and quotation defects were corrected; the final affected pages were re-rendered and inspected.',
         'result':'PASS'}
    for n in range(1,5):
        path=work/'final_qa_v3/contacts'/f'contact_{n:02d}.png'
        own['contact_sheets'].append({'pages':[(n-1)*20+1,n*20],'sha256':digest(path)})
    for version,pages in root_pages.items():
        for n in pages:
            path=work/f'final_qa_{version}/details'/f'page_{n:03d}.png'
            own['detail_reviews'].append({'version':version,'pdf_sha256':hashes[version],
                                          'page':n,'image_sha256':digest(path),'layout':'PASS'})
    own_path=work/'root_research/root_visual_review.json'
    own_path.write_text(json.dumps(own,ensure_ascii=False,indent=2)+'\n')
    unique=sorted({n for groups in assignments.values() for pages in groups.values() for n in pages})
    result={'result':'PASS','review_date':'2026-11-11','pdf':'GY1982_test.pdf',
            'pdf_sha256':final['sha256'],'pages':final['pages'],
            'renderer':'Poppler pdftoppm','thumbnail_dpi':60,'detail_dpi':120,
            'overview_pages':[1,2],
            'baseline_contact_review':{'pdf_sha256':baseline_hash,
                'all_pages':list(range(1,180)),
                'root_pages':[1,80],'winter_geometry_pages':[81,179]},
            'detailed_review_assignments':assignments,
            'unique_detailed_pages':unique,'unique_detailed_page_count':len(unique),
            'comparison_chain':[
                {'report':'code/render_comparison_v3_v4.json','unchanged_pages':len(first['unchanged_pixel_pages']),
                 'changed_pages':[x['page'] for x in first['changed_pixel_pages']],'all_changed_pages_reviewed':True},
                {'report':'code/render_comparison.json','unchanged_pages':len(second['unchanged_pixel_pages']),
                 'changed_pages':[x['page'] for x in second['changed_pixel_pages']],'all_changed_pages_reviewed':True}],
            'review_records':sources+[{'record':'research/root/root_visual_review.json','record_sha256':digest(own_path)}],
            'resolved_findings':['Joined prose words/numbers and quotation spacing corrected.',
                'Both Teichmüller bibliography titles now render the umlaut correctly.',
                'Final changed pages have no clipping, overlap or malformed mathematical display.'],
            'remaining_findings':[],
            'scope':'All pages were inspected in contact sheets for gross layout; 41 distinct pages were inspected in detail. This is not a claim of line-by-line visual proofreading of every page. Mathematical and source verification are recorded separately.'}
    (root/'code/visual_review.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'result':'PASS','pages':result['pages'],'distinct_detail_pages':len(unique),
                      'pdf_sha256':final['sha256']},indent=2))


if __name__=='__main__':main()
