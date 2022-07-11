import numpy as np

y = np.loadtxt('y.dat',dtype = float)
b = np.loadtxt('bin.dat',dtype = int)

rows = len(b)
x = 0
z = 0
c = 0
k = 0
for i in range(rows):
	if b[i] == 1:
	   c += 1
	   if y[i] <= 0:
	      x += 1	 
	elif b[i] == -1:
	   k += 1
	   if y[i] >0:
	       z += 1
	       
	       
print('p_(e|0) =',x/c)
print('p_(e|1) =',z/k)
	    
