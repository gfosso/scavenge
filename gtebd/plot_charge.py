import numpy as np
import csv
import matplotlib.pyplot as plt
tentativi=30
mag=[]
with open('50T30noconq2mag.txt') as f:
    reader= csv.reader(f)
    for row in reader:
        mag.append(np.array(row,dtype='f'))

#T=np.array([5,15,25,35,45,55])
T=np.array([5,15,25,30,35,40,45])
for i in T:
   # plt.plot((np.arange(len(mag[i]))-len(mag[i])//2+0.5)/(i)**(0.5),mag[i]/tentativi,label=" t=%s "% (i))
    plt.plot((np.arange(-i,len(mag[i])-i,1)-0.5)/i**(1.),mag[i]/tentativi,label=" t=%s "% (i))
#prova con np.arange(-2,len(mag[2])-2,1)+0.5

#plt.plot((np.arange(len(mag[59]))-len(mag[59])//2+0.5)/(59)**(0.5),mag[59]/tentativi,label=" t=%s "% (59))
plt.title(r'q=2, N=30, $\chi_{max}$ = 1000')
plt.ylabel("Q",size=18)
plt.xlabel(r"$\frac{x}{t^{1}}$",size=18)
#plt.ylim(0.7)
#plt.xlim(0.0)


plt.legend()
plt.show()
