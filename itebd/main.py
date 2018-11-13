import sys
from mps import *
from rand_unitary import *
import matplotlib.pyplot as plt

def main(argv):
    cristo=mps(bond_dimension=200)
    L=5
    for j in range(10):
        U=rand_unitary()
        cristo.product_state()
        corr=np.zeros(L)
        for i in range(L):
            corr[i] = cristo.expectation_Sz()
            cristo.evol(U)
        plt.plot(corr)
    
    plt.show()


if __name__ == "__main__":
    main(sys.argv[1:])
