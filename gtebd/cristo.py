#Attempt to random unitary dynamic with diffusive entanglement growth

import numpy as np
import matplotlib.pyplot as plt
from rand_unitary import *
from mps import *
from statistics import stdev

q=50;chi=100;N=150

q=np.array([2,4,6,10,15,20,25,30])
#Domain wall initial condition, max charge vs min charge
tentativi=100
entanglement=[]
dev_entanglement=np.zeros([len(q)])
mean_entanglement=np.zeros([len(q)])
for j in range(len(q)):
    entanglement.append(np.zeros([tentativi]))
    for i in range(tentativi):
        B=[]
        s=[]
        B.append(np.zeros([q[j],1,1]))
        B[-1][0,0,0]=1
        B.append(np.zeros([q[j],1,1]))
        B[-1][0,0,0]=1
        s.append(np.ones([1]))
        s.append(np.ones([1]))
        U=np.reshape(rand_unitary(q[j]*q[j]),(q[j],q[j],q[j],q[j]))
        B[0],B[1],s[1]=evol(B[0],B[1],s[0],s[1],U=U,chi=chi,d=q[j])
        entanglement[j][i]+=-sum((s[1]*s[1])*np.log(s[1]*s[1]))/np.log(q[j])
    dev_entanglement[j]+=stdev(entanglement[j])
    mean_entanglement[j]+=np.mean(entanglement[j])

plt.plot(q,dev_entanglement)
plt.plot(q,mean_entanglement)
#plt.plot(mag/tentativi)
#plt.plot(entanglement/np.log(q))
#x=np.linspace(0,N)
#plt.plot(x**(0.5))
#plt.plot(x**(1./3.))
#plt.yscale("log")
#plt.xscale("log")
plt.show()
