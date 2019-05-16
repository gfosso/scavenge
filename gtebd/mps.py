from ham import *


#expectation value of sz
def magnetization(s,B,d):
    sz=np.diag([Sz(conf,0) for conf in range(0,d)])
 #   sz=np.array([[0,1],[1,0]])
    mag=0.
    sB = np.tensordot(np.diag(s),B,axes=(1,1))
    C=np.tensordot(sB,np.conj(sB),axes=([0,2],[0,2]))
    mag = np.real( np.tensordot(C,sz,axes=([0,1],[0,1])))
    return mag

def charge(s,B,d):
    sz=np.diag(np.arange(d))
    mag=0.
    sB = np.tensordot(np.diag(s),B,axes=(1,1))
    C=np.tensordot(sB,np.conj(sB),axes=([0,2],[0,2]))
    mag = np.real( np.tensordot(C,sz,axes=([0,1],[0,1])))
    return mag

#correlator between sz in different positions
def corrszsz(dist,s,B,d):
    sz=np.diag([Sz(conf,0) for conf in range(0,d)])
    corr=0.0
    if dist ==0:
        sz2= np.tensordot(sz,sz,axes=(1,0))
        for i_bond in range(2):
            sB = np.tensordot(np.diag(s[np.mod(i_bond-1,2)]),B[i_bond],axes=(1,1))
            C=np.tensordot(sB,np.conj(sB),axes=([0,2],[0,2]))
            corr += np.real( np.tensordot(C,sz2,axes=([0,1],[0,1])) - np.tensordot(C,sz,axes=([0,1],[0,1]))*np.tensordot(C,sz,axes=([0,1],[0,1])))
        return corr*0.5

    if dist !=0:
        dist=np.abs(dist)
        for i_bond in range(2):
            sB = np.tensordot(np.diag(s[np.mod(i_bond-1,2)]),B[i_bond],axes=(1,1))
            C=np.tensordot(sB,np.conj(sB),axes=(0,0))
            R = np.tensordot(C,sz,axes=([0,2],[0,1]))
            mean1= np.trace(R)
            for i in range(dist-1):
                T=np.tensordot(R,B[np.mod(i_bond+1+i,2)],axes=(0,1))
                T=np.tensordot(T,np.conj(B[np.mod(i_bond+1+i,2)]),axes=(0,1))
                R=np.trace(T,axis1=0,axis2=2)
            C=np.tensordot(B[np.mod(i_bond+dist,2)],np.conj(B[np.mod(i_bond+dist,2)]),axes=(2,2))
            L=np.tensordot(R,C,axes=([0,1],[1,3]))
#            corr += np.real(np.tensordot(L,sz,axes=([0,1],[0,1])) - mean1*mean1) dovrebbe essere quello connesso
            corr +=np.real( np.tensordot(L,sz,axes=([0,1],[0,1])))
        return corr*0.5


#time evolution
def evol(B1,B2,s1,s2,U,chi,d):
        chia = B1.shape[1]; chic = B2.shape[2]
        # Construct theta matrix and time evolution #
        theta = np.tensordot(B1,B2,axes=(2,1)) # i a j b
        theta = np.tensordot(U,theta,axes=([2,3],[0,2])) # ip jp a b 
        theta = np.tensordot(np.diag(s1),theta,axes=([1,2])) # a ip jp b 
        theta = np.reshape(np.transpose(theta,(1,0,2,3)),(d*chia,d*chic)) # ip a jp b
        # Schmidt decomposition #
        X, Y, Z = np.linalg.svd(theta,full_matrices=0)
        chi2 = np.min([np.sum(Y>10.**(-15)), chi])	
        piv = np.zeros(len(Y), np.bool)
        piv[(np.argsort(Y)[::-1])[:chi2]] = True
        Y = Y[piv]; invsq = np.sqrt(sum(Y**2))
        X = X[:,piv] 
        Z = Z[piv,:]
        # Obtain the new values for B and s #
        s2 = Y/invsq 
        X=np.reshape(X,(d,chia,chi2))
        X = np.transpose(np.tensordot(np.diag(s1**(-1)),X,axes=(1,1)),(1,0,2))
        B1 = np.tensordot(X, np.diag(s2),axes=(2,0))
        B2 = np.transpose(np.reshape(Z,(chi2,d,chic)),(1,0,2))

        return B1,B2,s2

