import numpy as np
import csv
import matplotlib.pyplot as plt
tentativi=20
mag=[]
with open('q2mag.txt') as f:
    reader= csv.reader(f)
    for row in reader:
        mag.append(np.array(row,dtype='f'))

for i in range(1,10,2):
    plt.plot((np.arange(len(mag[i]))-len(mag[i])//2+0.5)/(i)**(0.5),mag[i]/tentativi,label=" t=%s "% (i))
#prova con np.arange(-2,len(mag[2])-2,1)+0.5

plt.plot((np.arange(len(mag[59]))-len(mag[59])//2+0.5)/(59)**(0.5),mag[59]/tentativi,label=" t=%s "% (59))
plt.title('q=2, N=10, chi = 300')
plt.ylabel("Q",size=18)
plt.xlabel(r"$\frac{x}{t}$",size=18)
plt.legend()
plt.show()
