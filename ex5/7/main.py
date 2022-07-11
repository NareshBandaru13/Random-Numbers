import numpy as np
import scipy
import scipy.special as sc
import matplotlib.pyplot as plt

def Q(x):
  return (sc.erfc(x/np.sqrt(2)))/2
vec_Q = scipy.vectorize(Q)
x = np.linspace(0,4,50)
plt.plot(x,vec_Q(x),label = 'Theoritical')

x1 = np.linspace(0,1,10)
u1 = np.loadtxt('bin.dat',dtype='int')
u2 = np.loadtxt('gau.dat',dtype='double') 
def P(a):
   t= []
   for i in range(len(u1)):
      t.append(u1[i]*a + u2[i])
   x,z,c,k = 0,0,0,0
   for i in range(len(u1)):
       if u1[i] == 1:
           c += 1
           if t[i] <= 0:
               x += 1
       elif u1[i] == -1:
           k += 1
           if t[i] >0:
               z += 1
	    
   return 0.5*((x/c)+(z/k))

vec_P = scipy.vectorize(P)
plt.plot(x1,vec_P(x1),'o',label = 'Numerical')
plt.grid()
plt.legend()
plt.show()
 
      


