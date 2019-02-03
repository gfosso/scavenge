import sys
from mps import *
from rand_unitary import *
import matplotlib.pyplot as plt

def main(argv):
    cristo=mps(bond_dimension=100)
    L=7
    N=100
    corr=np.zeros(L)
    dev=np.zeros(L)
    for j in range(N):
        U=rand_unitary(4)
        cristo.product_state()
        for i in range(L):
            x= np.sum(cristo.spectrum()*np.log2(cristo.spectrum()))
            corr[i] -= x 
            dev[i] += x*x
            cristo.evol(U)

    plt.plot(dev/N - (corr/N)**2,'bo')
    plt.plot(corr/N,'r+')
    t=np.arange(0,L,1)
    plt.plot(t**(2/3),label="2/3")
    plt.plot(t**(3/3),label="1")
    plt.xscale('log')
    plt.yscale('log')
    plt.legend()
    plt.show()



if __name__ == "__main__":
    main(sys.argv[1:])
