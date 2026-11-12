"""Two numerical evaluations of the exact volume formula for a ball slab."""
import mpmath as m

m.mp.dps=80
d=1000
normalization=m.exp(m.loggamma(m.mpf(d)/2+1)-m.loggamma(m.mpf(d+1)/2))/m.sqrt(m.pi)
print('mpmath',m.__version__,'precision',m.mp.dps,'decimal digits')
for width in ['0.01','0.005']:
    a=m.mpf(width)
    beta=m.betainc(m.mpf(1)/2,m.mpf(d+1)/2,0,a*a,regularized=True)
    quadrature=2*normalization*m.quad(lambda z:(1-z*z)**(m.mpf(d-1)/2),[0,a])
    assert abs(beta-quadrature) < m.mpf('1e-70')
    print('Ball dimension',d,'half-width/R',width,'probability',m.nstr(beta,40))
    print('Independent normalized density quadrature difference',m.nstr(abs(beta-quadrature),5))
print('Both readings of the notebook thickness are far from probability one.')
