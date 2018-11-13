""" iTEBD code to find the ground state of 
the 1D Ising model on an infinite chain.
The results are compared to the exact results.
Frank Pollmann, frankp@pks.mpg.de"""

import numpy as np
from scipy import integrate
from scipy.linalg import expm 
from rand_unitary import *

# First define the parameters of the model / simulation
d=2;chi=100; N=1000;

sz=np.array([[1.,0.],[0.,-1,]])

B=[];s=[]
for i in range(2):
	B.append(np.zeros([2,1,1])); B[-1][0,0,0]=1
	s.append(np.ones([1]))
 #       B.append(np.random.rand(2,10,10))
  #      s.append(np.random.rand(10))
# Generate the two-site time evolution operator
U = np.reshape(rand_unitary(),(2,2,2,2))
mag1=[]
# Perform the imaginary time evolution alternating on A and B bonds
for step in range(0, N):
    mag=[]
    for i_bond in range(2):
        sB = np.tensordot(np.diag(s[np.mod(i_bond-1,2)]),B[i_bond],axes=(1,1))
        C = np.tensordot(sB,sz,axes=(1,0))
        sB=np.conj(sB)
        mag.append(np.squeeze(np.tensordot(sB,C,axes=([0,2,1],[0,1,2]))).item()) 
        mag1.append(np.mean(mag))    
    for i_bond in [0,1]:
        ia = np.mod(i_bond-1,2); ib = np.mod(i_bond,2); ic = np.mod(i_bond+1,2)
        chia = B[ib].shape[1]; chic = B[ic].shape[2]
        # Construct theta matrix and time evolution #
        theta = np.tensordot(B[ib],B[ic],axes=(2,1)) # i a j b
        theta = np.tensordot(U,theta,axes=([2,3],[0,2])) # ip jp a b 
        theta = np.tensordot(np.diag(s[ia]),theta,axes=([1,2])) # a ip jp b 
        theta = np.reshape(np.transpose(theta,(1,0,2,3)),(d*chia,d*chic)) # ip a jp b
        # Schmidt decomposition #
        X, Y, Z = np.linalg.svd(theta,full_matrices=0)		    
        chi2 = np.min([np.sum(Y>10.**(-10)), chi])	
        piv = np.zeros(len(Y), np.bool)
        piv[(np.argsort(Y)[::-1])[:chi2]] = True
        Y = Y[piv]; invsq = np.sqrt(sum(Y**2))
        X = X[:,piv] 
        Z = Z[piv,:]
        # Obtain the new values for B and s #
        s[ib] = Y/invsq 
        X=np.reshape(X,(d,chia,chi2))
        
        X = np.transpose(np.tensordot(np.diag(s[ia]**(-1)),X,axes=(1,1)),(1,0,2))
        B[ib] = np.tensordot(X, np.diag(s[ib]),axes=(2,0))
        B[ic] = np.transpose(np.reshape(Z,(chi2,d,chic)),(1,0,2))

#f = lambda k,g : -2*np.sqrt(1+g**2-2*g*np.cos(k))/np.pi/2.
#E0_exact = integrate.quad(f, 0, np.pi, args=(g,))[0]
#print("E_exact =", E0_exact)
