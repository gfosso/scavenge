import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#x = np.array([5, 15, 25, 35, 45, 55])
#y = np.array([5, 15, 25, 35, 45, 55])
y = np.loadtxt('q2gesuent.txt')[2:40]
z=np.arange(0,50,1)[2:40]
#x = np.log(z)
x = np.sqrt(z)
sigmaq=np.loadtxt('q2gesuvarent.txt')[2:40]
plt.plot(x,y,'o',label='<S>')
plt.plot(x,sigmaq,'o',label='$<S^2>-<S>^2$')


model = LinearRegression().fit(x.reshape((-1, 1)), y)
r_sq = model.score(x.reshape((-1, 1)), y)
print('coefficient of determination:', r_sq)
print('slope:',model.coef_)
print('intercept:', model.intercept_)

models = LinearRegression().fit(x.reshape((-1, 1)), sigmaq)
r_sqs = model.score(x.reshape((-1, 1)), sigmaq)
print('coefficient of determination:', r_sqs)
print('slope:',models.coef_)
print('intercept:', models.intercept_)
plt.plot(x,model.intercept_+ x*model.coef_,label='{}+{}*t^0.5'.format(model.intercept_,model.coef_[0]))
plt.plot(x,models.intercept_+ x*models.coef_,label='{}+{}*t^0.5'.format(models.intercept_,models.coef_[0]))
#plt.plot(z,1/3*x,label='1/3*log(t)')
plt.title(r'$ q = 2 \, \, t \in [2,40]$, 10 realizzazioni',size=18)
plt.xlabel(r'$\sqrt{t}$',size=18)
plt.legend()
plt.show()
