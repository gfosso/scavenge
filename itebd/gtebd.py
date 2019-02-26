#Attempt to random unitary dynamic with diffusive entanglement growth

import numpy as np
import matplotlib.pyplot as plt
from rand_unitary import *

q=2;chi=100;N=100

B=[];s=[]

#Domain wall initial condition, max charge vs min charge
B.append(np.zeros(q,1,1))
B[-1][0,0,0]=1
B.append(np.zeros(q,1,1))
B[-1][q,0,0]=1
s.append(np.ones([1]))
s.append(np.ones([1]))

U=np.reshape(rand_u1_unitary(q),(q,q,q,q))
l=2 #initial length
for step in range(N):
	
	for i_bond in range(0,l,2):#only even numbers
		pass
	B.insert(0,np.zeros(q,1,1))
	B.append(np.zeros(q,1,1))
	B[0][0,0,0]=1 #first and last in max and min charge state
	B[-1][q,0,0]=1
