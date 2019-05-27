import numpy as np
import csv
import matplotlib.pyplot as plt
tentativi=10
mag=[]
with open('q2mag.txt') as f:
    reader= csv.reader(f)
    for row in reader:
        mag.append(np.array(row,dtype='f'))

for i in range(9,40,10):
    plt.plot((np.arange(len(mag[i]))-len(mag[i])//2+0.5)/(i)**(1.),mag[i]/tentativi,label=" t=%s "% (i))

#plt.plot((np.arange(len(mag[39]))-len(mag[39])//2+0.5)/(39)**(0.5),mag[39]/tentativi,label=" t=%s "% (39))
plt.title('q=2, 10 realizzazioni')
plt.ylabel("Q",size=18)
plt.xlabel(r"$\frac{x}{t}$",size=18)
plt.legend()
plt.show()
