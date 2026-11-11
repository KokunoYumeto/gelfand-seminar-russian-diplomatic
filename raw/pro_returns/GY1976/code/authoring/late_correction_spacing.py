from pathlib import Path
p=Path('work/late_author.py')
s=p.read_text()
replacements={
 'Tyurin1977Introduction assumes Möbius coordinate changes.':'Tyurin (1977), Introduction, assumes Möbius coordinate changes.',
 'Catalogue record418 is the1977--78 heading; P705 explicitly marks34thseminar year and names V.Drinfeld in a new heading.':'Catalogue record 418 is the 1977--78 heading; P000705 explicitly marks the thirty-fourth seminar year and names V. Drinfeld in a new heading.',
 'Frame, Robinson and Thrall publisher record dates Canadian Journal of Mathematics6 to1954.':'The Frame, Robinson and Thrall publisher record dates Canadian Journal of Mathematics, volume 6, to 1954.',
 'Both radical indices4 are visible onPNG. Ivanov--OlshanskiTheorem7.1 uses centered square-root-scale profile fluctuations and a nonwhite generalizedGaussianfield.':'Both radical indices 4 are visible on the PNG. Ivanov--Olshanski, Theorem 7.1, uses centered profile fluctuations and a generalized Gaussian field with nonwhite covariance.',
 'The cited1961Canadian Journal paper is C.Schensted, Longest Increasing and Decreasing Subsequences.':'The cited 1961 Canadian Journal paper is C. Schensted, Longest Increasing and Decreasing Subsequences.',
 'Tyurin1978ChII2Exercise10. Full proof independently checked.':'Tyurin (1978), Chapter II, section 2, Exercise 10. Full proof independently checked.',
 'Tyurin1978ChII2Exercise13 explicitly invoke':'Tyurin (1978), Chapter II, section 2, Exercise 13, explicitly invoke',
 'Gelfand–Graev1968 section2 Definition2 specifies':'Gelfand--Graev (1968), section 2, Definition 2, specifies',
 'GGS1967 Theorem1 states classPhi as an independent hypothesis.':r'GGS (1967), Theorem 1, states class \(\Phi\) as an independent hypothesis.',
 'PNG clearly says1-dimensional; the integrand is a(1,1)-form. GGS1967 Theorem2 explicitly says real dimension2k.':r'The PNG clearly says one-dimensional; the integrand is a \((1,1)\)-form. GGS (1967), Theorem 2, explicitly says real dimension \(2k\).',
 'Rank of the associated alternating form distinguishes ranks4 and2; rank2 gives a special complex.':'The rank of the associated alternating form distinguishes ranks four and two; rank two gives a special complex.'
}
for a,b in replacements.items():s=s.replace(a,b)
p.write_text(s)
print('Corrected the two overfull evidence strings and improved source-locator spacing.')
