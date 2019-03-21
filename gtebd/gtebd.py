#Attempt to random unitary dynamic with diffusive entanglement growth

import numpy as np
import matplotlib.pyplot as plt
from rand_unitary import *
from mps import *

q=2;chi=100;N=150


#Domain wall initial condition, max charge vs min charge
entanglement=np.zeros([N])
mag=np.zeros([N])
tentativi=10
for i in range(tentativi):
	B=[]
	s=[]
	B.append(np.zeros([q,1,1]))
	B[-1][0,0,0]=1
	B.append(np.zeros([q,1,1]))
	B[-1][q-1,0,0]=1
	s.append(np.ones([1]))
	s.append(np.ones([1]))
	U=np.reshape(rand_u1_unitary(q),(q,q,q,q))
	l=2 #initial length
	for step in range(N):
            m=0
            for i_bond in range(l):
                m+=magnetization(s[i_bond],B[i_bond],d=q)
            mag[step]+=m/l
            entanglement[step]+=-sum((s[l//2-1]*s[l//2-1])*np.log(s[l//2-1]*s[l//2-1]))
            for i_bond in range(0,l,2):#only even numbers
                B[i_bond],B[i_bond+1],s[i_bond+1]=evol(B[i_bond],B[i_bond+1],s[i_bond],s[i_bond+1],U=U,chi=chi,d=q)
            B.insert(0,np.zeros([q,1,1]))
            B.append(np.zeros([q,1,1]))
            s.insert(0,np.ones([1]))
            s.append(np.ones([1]))
            B[0][0,0,0]=1 #first and last in max and min charge state
            B[-1][q-1,0,0]=1
            l+=2

plt.plot(mag/tentativi)
#plt.plot(entanglement/tentativi)
#x=np.linspace(0,N)
#plt.plot(x**(0.5))
#plt.plot(x**(1./3.))
#plt.yscale("log")
#plt.xscale("log")
plt.show()
