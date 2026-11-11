"""Narrow typesetting repairs found by compiling the complete chapter.
Only selected inline/display delimiters and short prose around citations change.
The same repaired text is written to the published JSON and generated chapter.
"""
def format_layout(talks,items):
    targets={
      '1985-651.3':('statement',r'\int_{\mathbb R^N}e^{-x^TAx/2}dx=(2\pi)^{N/2}(\det A)^{-1/2}'),
      '1985-653.2':('notes',r'N=1+\min\{\max(d(p),d(q)),\max(k(p),k(q))\}'),
      '1985-654.7':('notes',r"\lim_{u\to0}u^{-1/2}\varphi(u)=\lim_{u\to0}u^{1/2}\varphi'(u)"),
      '1985-659.3':('notes',r'A(s,t)=B(-\alpha(s),-\alpha(t))'),
      '1985-659.12':('notes',r'\langle0|V(p_2)D(s_2)V(p_3)\cdots D(s_{n-2})V(p_{n-1})|0\rangle')}
    for x in items:
        if x['id'] in targets:
            field,equation=targets[x['id']]
            old=r'\('+equation+r'\)'
            new=r'\['+equation+r'\]'
            assert old in x[field] or new in x[field],x['id']+' layout target changed'
            x[field]=x[field].replace(old,new)
    rewrites={
      '1985-650.8':(
        r"Polyakov's 1981 action is the immediate source \citep[eqs.~(16),(24)--(25)]{polyakov1981quantum}.",
        r"Polyakov gives this action \citep[eqs.~(16), (24)--(25)]{polyakov1981quantum}."),
      '1985-664.3':(
        r"Classical deformation theory is used in \citet[eqs.~(2.13)--(2.19)]{belavinknizhnik1986complex}; the pairing itself predates the talk.",
        r"See \citet[eqs.~(2.13)--(2.19)]{belavinknizhnik1986complex} for its use in deformation theory; the pairing predates the talk.")}
    for x in items:
        if x['id'] in rewrites:
            old,new=rewrites[x['id']]
            assert old in x['fate'] or new in x['fate'],x['id']+' citation-layout target changed'
            x['fate']=x['fate'].replace(old,new)
    for t in talks:
        t['summary']=t['summary'].replace('isotopy of determinant-sign classes','isotopy of classes defined by determinant signs')
    return talks,items
