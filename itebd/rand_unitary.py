import numpy as np
import scipy as sp


def  rand_unitary(n):

    x =( sp.randn(n,n) +  1j*sp.randn(n,n))/np.sqrt(2.0)
    q,r = np.linalg.qr(x)
    d=sp.diagonal(r)
    ph=d/sp.absolute(d)
    q=np.multiply(q,ph,q)
    return q
