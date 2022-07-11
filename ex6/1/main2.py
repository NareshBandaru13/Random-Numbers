#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sc


import math
def Q(x):
   if x<0:
     return 1.00
   else:
     return 1 - sc.gammainc(1,x/2)
err1 = []

x = np.linspace(-4,4,60)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
#randvar = np.random.normal(0,1,simlen)
randvar = np.loadtxt('v.dat',dtype='double')
for i in range(0,60):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list
for i in range(len(x)):
   c= 1 - Q(x[i])
   err1.append(c)
   
plt.plot(x.T,err,label = 'theoretical')#plotting the CDF
plt.plot(x.T,err1,'o',label = 'numerical')#plotting the CDF
plt.grid() #creating the grid
plt.legend()
plt.xlabel('$v$')
plt.ylabel('$F_V(v)$')


plt.savefig('v_cdf.pdf')


plt.show() #opening the plot window
