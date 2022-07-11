import numpy as np


u1 = np.loadtxt('bin.dat',dtype='int')
u2 = np.loadtxt('gau.dat',dtype='double')
t1 = open('y.dat','w') 
def fun(a):
   t =[]
   for i in range(len(u1)):
      t.append(str(u1[i]*a + u2[i]))
   for i in t:
      t1.write(f'{i}\n')
      
fun(0.5)
