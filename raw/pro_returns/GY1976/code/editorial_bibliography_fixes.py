"""Correct BibTeX types/series fields using opened primary catalogue metadata.

Numdam supplies Bourbaki volume-series numbers 18/19, distinct from exposition
numbers 483/497. The ICM volume's actual copyright page supplies its publisher.
The PDG document is an online review chapter, represented as a misc entry rather
than an incomplete book-chapter record. Keys and historical years are unchanged.
"""
from pathlib import Path
import argparse
import re
from merge_chapter import bib_entries

def field(entry,name,value):
    m=re.search(r'\b'+re.escape(name)+r'\s*=\s*\{',entry,re.I)
    if m:
        i=m.end();depth=1
        while i<len(entry) and depth:
            if entry[i]=='{' and entry[i-1]!='\\':depth+=1
            elif entry[i]=='}' and entry[i-1]!='\\':depth-=1
            i+=1
        if value is not None:return entry[:m.start()]+name+' = {'+value+'}'+entry[i:]
        while i<len(entry) and entry[i].isspace():i+=1
        if i<len(entry) and entry[i]==',':i+=1
        return entry[:m.start()]+entry[i:]
    if value is None:return entry
    return entry.rstrip()[:-1].rstrip().rstrip(',')+',\n '+name+' = {'+value+'}\n}'

def main():
    ap=argparse.ArgumentParser();ap.add_argument('segments',nargs='?',default='work');a=ap.parse_args();d=Path(a.segments)
    changes={
      'early':{'amslercredegrand2024quark':{
        'howpublished':r'Review of Particle Physics, Section~15; S. Navas et al., Physical Review D 110, 030001 (2024)'}},
      'middle':{'demazure1977identites':{'series':r'S\'eminaire Bourbaki','number':'18','chapter':r'Expos\'e 483'},
                'ramanan1980vector':{'publisher':'Academia Scientiarum Fennica','editor':'Lehto, Olli','address':'Helsinki'}},
      'late':{'duistermaat1974morse':{'number':None,'chapter':r'Expos\'e 25',
                   'booktitle':r'S\'eminaire \'Equations aux d\'eriv\'ees partielles, 1973--1974'},
              'macpherson1978combinatorial':{'series':r'S\'eminaire Bourbaki','number':'19',
                   'chapter':r'Expos\'e 497','publisher':'Springer-Verlag'}}}
    for pre,entries in changes.items():
        p=d/f'{pre}_references.bib';s=p.read_text();parsed=bib_entries(s)
        for key,fields in entries.items():
            old=parsed[key];new=old
            if key=='amslercredegrand2024quark':new=new.replace('@incollection{','@misc{',1)
            for name,value in fields.items():new=field(new,name,value)
            s=s.replace(old,new)
        p.write_text(s)
    print('Corrected five BibTeX records; all keys and verified URLs retained.')

if __name__=='__main__':main()
