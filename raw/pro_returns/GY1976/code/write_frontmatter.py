"""Render counts and the reviewed editorial overview/report templates."""
from pathlib import Path
import argparse
import json

def table(headers,rows):
    return '\n'.join(['| '+' | '.join(headers)+' |','|'+'|'.join('---' for _ in headers)+'|']+
                     ['| '+' | '.join(str(v).replace('|','\\|') for v in row)+' |' for row in rows])

def main():
    ap=argparse.ArgumentParser();ap.add_argument('directory',nargs='?',default='.')
    a=ap.parse_args();d=Path(a.directory)
    c=json.loads((d/'code/output/counts.json').read_text())
    p=json.loads((d/'GY1976_problems.json').read_text())
    labels={'A':'Published soon after','B':'Later development by others','C':'Partly developed',
            'D':'Not developed','E':'Already known','F':'Not identifiable precisely'}
    values={k:str(c['classes'][k]) for k in 'ABCDEF'}
    values.update({'S'+k:str(c['strict_1976_classes'][k]) for k in 'ABCDEF'})
    for token,key in [('TOTAL','items'),('STRICT','strict_1976_items'),('PROBLEMS','problems'),
                      ('REFERENCES','references'),('CORRECTIONS','corrections')]:values[token]=str(c[key])
    values['CLASS_TABLE']=table(['Class','Meaning','Entire package','1976–77 core'],
        [[k,labels[k],c['classes'][k],c['strict_1976_classes'][k]] for k in 'ABCDEF']+
        [['Total','',c['items'],c['strict_1976_items']]])
    values['RECORD_TABLE']=table(['Record','Speaker / catalogue label','Date used','Kind','Items','Class counts'],
        [[r['record'],r['speaker'],r['date'] or 'Undated heading',r['kind'],r['items'],
          ', '.join(f'{k}: {v}' for k,v in r['classes'].items()) or '—'] for r in c['per_record']])
    values['SPEAKER_TABLE']=table(['Attributed speaker','Items'],c['by_speaker'].items())
    values['AREA_TABLE']=table(['Primary area','Items'],c['by_area'].items())
    values['ASSESSMENT_TABLES']='\n\n'.join('**'+title+'**\n\n'+table(['Assessment','Items'],c[key].items())
        for key,title in [('literal_correctness','Literal correctness'),('publication_match','Publication match'),
                          ('verification','Verification depth'),('development','Editorial development')])
    values['PROBLEM_TABLE']=table(['Problem ID','Question','Occurrences'],
        [[q['id'],q['title'],', '.join(q['occurrences'])] for q in p])
    audit=d/'code/output/pdf_audit.json'
    if audit.exists():
        a=json.loads(audit.read_text())
        values['BUILD_RESULT']=(f"**Delivered build:** {a['pages']} PDF pages. The supplied builder, additional validator, "
            'XeLaTeX, BibTeX and both subsequent XeLaTeX passes completed successfully. '
            f"The final log audit reports {a['latex_error_count']} LaTeX errors, "
            f"{a['undefined_citation_or_reference_count']} unresolved citation/reference warnings and "
            f"{a['missing_character_count']} missing-character warnings. "
            'The visual-review record and page contact sheets are retained in `code/output/visual`.')
    else:values['BUILD_RESULT']='Build and visual validation are pending; this sentence must be replaced before packaging.'
    for src,dest in [('overview_template.tex','GY1976_overview.tex'),('report_template.md','GY1976_report.md')]:
        s=(d/'code/templates'/src).read_text()
        for token,value in values.items():s=s.replace('@@'+token+'@@',value)
        if '@@' in s:raise ValueError('Unresolved template token in '+src)
        (d/dest).write_text(s)
    intro=r'''No C or D occurrence qualified for a bounded new research contribution.
The subsections below are critical verifications of statements, calculations
and omissions in the notebook, not newly solved open problems. All results
proved or computed in this task are marked with the supplied authorship
macros; their exact scope and independent checks are stated in the text.
Historical classifications remain those in the occurrence index.
'''
    checks='\n\n'.join((d/'code/research'/f'{pre}_checks.tex').read_text()
                        for pre in ['early','middle','late','root'])
    (d/'GY1976_development.tex').write_text(intro+'\n'+checks+'\n')
    print('Rendered overview, report and critical-verification appendix.')

if __name__=='__main__':main()
