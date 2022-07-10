import matplotlib as plt
import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(0,1,100)
x2 = np.linspace(0,0,100)
x3 = np.linspace(1,1,100)

plt.plot(x1,x2)
plt.plot(x1,x3,label = 'y = 1')
plt.plot(x3,x1,label = 'x = 1')
plt.plot(x2,x1)
plt.plot(x1,0.5 - x1,label = '0 < x + y = t < 1')
plt.plot(x1,1.5 - x1,label = '1 < x + y = t < 2')
plt.legend(loc='upper right')
plt.annotate("A(1,1)",(1,1))
plt.annotate("B(1,t-1)",(1,0.5))
plt.annotate("C(t-1,1)",(0.5,1))
plt.annotate("D(1,0)",(1,0))
plt.annotate("E(0,1)",(0,1))
plt.annotate("F(t,0)",(0.5,0))
plt.annotate("E(0,t)",(0,0.5))
plt.show()

