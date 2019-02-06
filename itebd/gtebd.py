#Attempt to random unitary dynamic with diffusive entanglement growth

import numpy as np
import matplotlib.pyplot as plt
from rand_unitary import *

q=2;chi=100;N=100

B=[];s=[]

B.append(np.zeros(q,1,1))
B[-1][0,0,0]=1
B.append(np.zeros(q,1,1))
B[-1][q,0,0]=1
s.append(np.ones([1]))
s.append(np.ones([1]))

U=np.reshape(rand_u1_unitary(q),(q,q,q,q))

for step in range(N):

