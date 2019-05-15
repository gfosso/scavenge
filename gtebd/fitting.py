import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#x = np.array([5, 15, 25, 35, 45, 55])
#y = np.array([5, 15, 25, 35, 45, 55])
y = np.loadtxt('gesuent.txt')[10:50]
z=np.arange(0,50,1)[10:50]
x = np.log(z)
sigmaq=np.loadtxt('gesuvarent.txt')[10:50]
plt.plot(z,y,'o',label='<S>')
plt.plot(z,sigmaq,'o',label='$<S^2>-<S>^2$')


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
plt.plot(z,model.intercept_+ x*model.coef_,label='{}+{}*log(t)'.format(model.intercept_,model.coef_[0]))
plt.plot(z,models.intercept_+ x*models.coef_,label='{}+{}*log(t)'.format(models.intercept_,models.coef_[0]))
#plt.plot(z,1/3*x,label='1/3*log(t)')
plt.legend()
plt.show()
