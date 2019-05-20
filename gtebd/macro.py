import numpy as np
import matplotlib.pyplot as plt
from rand_unitary import *
from statistics import stdev
N=1000
q=4
A=np.zeros([q**2,q**2,q**2,q**2,q**2,q**2,q**2,q**2],dtype='complex')
for i in range(N):
    U=rand_unitary(q*2)
    U_d=np.conj(U.T)
    C=np.tensordot(U,U_d,axes=0)
    A+=np.tensordot(C,C,axes=0)

A=A/N
