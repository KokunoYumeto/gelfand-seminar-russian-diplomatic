from pathlib import Path
p=Path(__file__).with_name('make_autumn.py')
s=p.read_text()
s=s.replace("The manuscript's conflicting", "The conflicting manuscript")
s=s.replace("the notebook's unspecified", "the unspecified notebook")
s=s.replace("reconstruction='The meanings of \\(i,i'\\),", "reconstruction=r'The two invariant dimensions,")
p.write_text(s)
