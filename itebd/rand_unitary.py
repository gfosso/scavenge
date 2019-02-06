import numpy as np
import scipy as sp
from scipy.linalg import block_diag

#random unitary Haar distribuited
def  rand_unitary(n):
	x=(sp.randn(n,n) + 1j*sp.randn(n,n))/np.sqrt(2.0)
	q, r = np.linalg.qr(x)
	d=sp.diagonal(r)
	ph=d/sp.absolute(d)
	q=np.multiply(q,ph,q)
	return q


#random unitary conserving U(1) charge
def rand_u1_unitary(q):
	m=rand_unitary(1)
	for i in range(2*(q-1)-1,-1,-1):
		m=block_diag(m,rand_unitary(q-np.abs(i+1-q)))

	return m
