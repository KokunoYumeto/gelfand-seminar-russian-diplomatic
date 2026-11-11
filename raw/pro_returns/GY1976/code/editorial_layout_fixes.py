"""Apply content-preserving source-format fixes identified by the TeX build."""
from pathlib import Path
import json
import argparse
import re

def main():
    p=argparse.ArgumentParser();p.add_argument('segments',nargs='?',default='work');a=p.parse_args();d=Path(a.segments)
    path=d/'early_items.json';items=json.loads(path.read_text())
    for x in items:
        if x['id']=='1976-398.17':
            old=r'\(\sum_{n\ge1}n\lambda^{-n}/(\lambda-\lambda^{-1})=\lambda^2/[(\lambda-1)^3(\lambda+1)]\)'
            new=r'\[\frac{\sum_{n\ge1}n\lambda^{-n}}{\lambda-\lambda^{-1}}=\frac{\lambda^2}{(\lambda-1)^3(\lambda+1)}.\]'
            x['reconstruction']=x['reconstruction'].replace(old+'.',new).replace(old,new)
        if x['id']=='1976-401.2':
            old=r'\(\sum_{i<j}(-1)^{i+j-1}h([g_i,g_j],g_1,\ldots,\widehat g_i,\ldots,\widehat g_j,\ldots)\)'
            new=r'\[\sum_{i<j}(-1)^{i+j-1}h([g_i,g_j],g_1,\ldots,\widehat g_i,\ldots,\widehat g_j,\ldots).\]'
            x['notes']=x['notes'].replace(old+'; in degree 1',new+' In degree 1')
        if x['id']=='1976-405.4':
            x['notes']=x['notes'].replace('The emphatic sentence is ',r'The emphatic sentence is:\par ')
        if x['id']=='1976-403.6':x['kind']='construction'
    path.write_text(json.dumps(items,ensure_ascii=False,indent=2)+'\n')
    path=d/'early_checks.tex';s=path.read_text().replace('Quadratic normalization along a fixed solution','Quadratic normalization near a solution');path.write_text(s)
    # A control word at a line ending consumes the source newline. Empty braces
    # preserve the following space in the supplied result-marker macros.
    for pre in ['early','middle','late','root']:
        path=d/f'{pre}_checks.tex';s=path.read_text()
        s=re.sub(r'\\(oursComputed|ours)(?![A-Za-z\\{])',r'\\\1{}',s)
        path.write_text(s)
        path=d/f'{pre}_items.json';data=json.loads(path.read_text())
        for x in data:
            for key,value in x.items():
                if isinstance(value,str):x[key]=re.sub(r'\\(oursComputed|ours)(?![A-Za-z\\{])',r'\\\1{}',value)
        path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print('Applied early-record equation layout and permitted-kind fixes.')

if __name__=='__main__':main()
