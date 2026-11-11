from pathlib import Path
p=Path('work/late_research_log.md')
s=p.read_text()
s=s.replace('Frame Robinson Thrall1954hook graphs symmetric group Canadian Journal Mathematics pdf','Frame Robinson Thrall 1954 hook graphs symmetric group Canadian Journal Mathematics pdf')
s=s.replace('Schensted1961longest increasing decreasing subsequences pdf','Schensted 1961 longest increasing decreasing subsequences pdf')
s=s.replace('Tyurin periods quadratic differentials1978rm3586_eng.pdf','Tyurin periods quadratic differentials 1978 rm3586_eng.pdf')
s=s.replace('Gelfand Graev admissible line complexes tangent surface curve1977integral geometry','Gelfand Graev admissible line complexes tangent surface curve 1977 integral geometry')
s=s.replace('Aitken1943"determinants" "tableaux" skew standard','Aitken 1943 "determinants" "tableaux" skew standard')
s=s.replace('"Two Remarks on Skew Tableaux" Stanley2011published','"Two Remarks on Skew Tableaux" Stanley 2011 published')
s=s.replace('Spacing in items1–4and9–10above is condensed for presentation; the queries searched the indicated author/year/title terms. ','')
for a,b in {
'full13-page':'full 13-page','Full13-page':'Full 13-page','Full4-page':'Full 4-page','full17-page':'full 17-page',
'Theorems5.1–5.2':'Theorems 5.1–5.2','Proposition5.15':'Proposition 5.15','Theorems8.8–8.9and9.1':'Theorems 8.8–8.9 and 9.1',
'ChapterIII':'Chapter III','Theorem2.6':'Theorem 2.6','ChapterIsections1–3':'Chapter I sections 1–3',
'ChapterIIsection2':'Chapter II section 2','Definitions2.2.1–2.2.8and equation2.2.7':'Definitions 2.2.1–2.2.8 and equation 2.2.7',
'Exercises1–13pp204–205':'Exercises 1–13, pp. 204–205','Exercise10forbids':'Exercise 10 forbids',
'Exercises1and8support':'Exercises 1 and 8 support','Exercises12–13match':'Exercises 12–13 match',
'Theorems1–3and insertion':'Theorems 1–3 and insertion',
'Theorem7.1andsection9':'Theorem 7.1 and section 9','generalizedGaussianfield':'generalized Gaussian field',
'Theorems2.9and5.8':'Theorems 2.9 and 5.8','Equation1.2derives':'Equation 1.2 derives',
'publisherPDF':'publisher PDF','AuthorPDFhas':'Author PDF has','Math-Netmetadata':'Math-Net metadata',
'publishermetadata':'publisher metadata','Cumulativekeygelfand1967planes':'Cumulative key: gelfand1967planes',
'Cumulativekeygelfand1969forms':'Cumulative key: gelfand1969forms',
'and1977results':'and 1977 results','or1977results':'or 1977 results',
'GP-1975-26is':'GP-1975-26 is','GP-1975-14is':'GP-1975-14 is',
'Stage2research':'Stage 2 research','returned403and':'returned 403 and',
'5/IV-77remains':'5/IV-77 remains','toIXwould':'to IX would','adjacent1977–78context':'adjacent 1977–78 context',
'fabricated1976occurrences':'fabricated 1976 occurrences','Theorem2.6, p83':'Theorem 2.6, p. 83',
'Theorems2.4–2.6':'Theorems 2.4–2.6','Lem ma':'Lemma'
}.items():s=s.replace(a,b)
p.write_text(s)
print('Polished query strings and audit prose; no data changes.')
