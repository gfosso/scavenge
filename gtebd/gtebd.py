#Attempt to random unitary dynamic with diffusive entanglement growth

import numpy as np
import matplotlib.pyplot as plt
from rand_unitary import *
from mps import *
import csv,getopt
import sys

q=4;chi=200;N=20


#Domain wall initial condition, max charge vs min charge
entanglement=np.zeros([N])
dev_ent=np.zeros([N])
mag=np.zeros([N])
tentativi=100
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
                m+=charge(s[i_bond],B[i_bond],d=q)
            mag[step]+=m/l
            entanglement[step]+=-sum((s[l//2-1]*s[l//2-1])*np.log(s[l//2-1]*s[l//2-1]))
            dev_ent[step]+= (sum((s[l//2-1]*s[l//2-1])*np.log(s[l//2-1]*s[l//2-1])))**2
            for i_bond in range(0,l,2):#only even numbers
         #       U=np.reshape(rand_u1_unitary(q),(q,q,q,q))
                B[i_bond],B[i_bond+1],s[i_bond+1]=evol(B[i_bond],B[i_bond+1],s[i_bond],s[i_bond+1],U=U,chi=chi,d=q)
            B.insert(0,np.zeros([q,1,1]))
            B.append(np.zeros([q,1,1]))
            s.insert(0,np.ones([1]))
            s.append(np.ones([1]))
            B[0][0,0,0]=1 #first and last in max and min charge state
            B[-1][q-1,0,0]=1
            l+=2
    
#np.savetxt('q4gesuent.txt',entanglement/tentativi,delimiter=',')
#np.savetxt('q4gesuvarent.txt',dev_ent/tentativi -(entanglement/tentativi)**2,delimiter=',')
#        csvwriter=csv.writer(f)
#        csvwriter.writerows(dev_ent)
#with open('gesudev.txt','w') as f:
#    csvwriter=csv.writer(f)
#    csvwriter.writerows(entanglement)
plt.plot(mag/tentativi)
#x=np.linspace(0,N)
#plt.plot(x**(0.5))
#plt.plot(x**(1./2.))
#plt.plot(np.arange(N)**(1/2),entanglement/tentativi)
#plt.plot(np.arange(N)**(0.5),entanglement/tentativi)
#plt.plot(np.arange(N)**(0.5),np.sqrt(dev_ent/tentativi-(entanglement/tentativi)**2))
#plt.plot((1/3)*np.log(x))
#plt.yscale("log")
#plt.xscale("log")
plt.show()
