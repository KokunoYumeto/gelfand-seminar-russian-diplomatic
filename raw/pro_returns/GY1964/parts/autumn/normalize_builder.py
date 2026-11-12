"""Protect authored LaTeX from Python escape interpretation and normalize titles."""
from pathlib import Path
import io
import tokenize

p = Path(__file__).resolve().parent / 'make_autumn.py'
s = p.read_text().replace(r'\textquotesingle s', '’s')
tokens = []
count = 0
for token in tokenize.generate_tokens(io.StringIO(s).readline):
    if token.type == tokenize.STRING and r'\(' in token.string and not token.string.lower().startswith('r'):
        token = token._replace(string='r' + token.string)
        count += 1
    tokens.append(token)
p.write_text(tokenize.untokenize(tokens))
print('Converted', count, 'LaTeX-bearing string literals to raw strings')
