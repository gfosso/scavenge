import numpy as np
import scipy as sp
import scipy.linalg


def  rand_unitary():
    x=[]
    q=[]
    r=[]

    a=np.random.randn(4,4)
    b=np.random.randn(4,4)

    x = a +  complex(0,1)*b

    q, r = scipy.linalg.qr(x)

    r=np.diag(np.diag(r)/np.abs(np.diag(r)))
    return q
