import numpy as np


u1 = np.loadtxt('gau1.dat',dtype='double')
u2 = np.loadtxt('gau2.dat',dtype='double')
t1 = open('v.dat','w') 

t =[]
for i in range(len(u1)):
    t.append(str( (u1[i]*u1[i]) + (u2[i]*u2[i]) ))
for i in t:
  t1.write(f'{i}\n')

