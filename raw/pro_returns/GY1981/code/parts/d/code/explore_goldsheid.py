"""Exploratory numerical minimization, not a proof of global optimality."""
import numpy as np
from scipy.optimize import differential_evolution
rng=np.random.default_rng(1981)
for n in range(2,7):
    for sample in range(3):
        q,r=np.linalg.qr(rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)))
        s=q@q.T
        def loss(theta):
            return np.linalg.norm(s-np.diag(np.exp(1j*theta)),ord=2)/2
        opt=differential_evolution(loss,[(0,2*np.pi)]*n,seed=1981+sample,popsize=15,maxiter=300,tol=1e-8)
        print(n,sample,format(opt.fun,'.10f'),flush=True)
