import matplotlib.pyplot as plt
import numpy as np

y = np.loadtxt('y.dat')

plt.plot(y,'o')
plt.xlabel('points in y')
plt.ylabel('value of y')
plt.show()

