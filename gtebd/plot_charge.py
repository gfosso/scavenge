
for i in range(14,24,4):
    plt.plot((np.arange(len(mag[i]))-len(mag[i])//2+0.5)/(i)**(0.5),mag[i]/tentativi,label=" t=%s "% (i))

plt.plot((np.arange(len(mag[24]))-len(mag[24])//2+0.5)/(24)**(1),mag[24]/tentativi,label=" t=%s "% (24))
plt.ylabel("Q",size=18)
plt.xlabel(r"$\frac{x}{t}$",size=18)
plt.legend()
plt.show()
