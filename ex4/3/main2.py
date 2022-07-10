#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt


import math


x = np.linspace(-4,4,60)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
#randvar = np.random.normal(0,1,simlen)
randvar = np.loadtxt('t.dat',dtype='double')
for i in range(0,60):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

   
plt.plot(x.T,err,'o',label = 'Numerical',)
plt.grid() #creating the grid
plt.legend()
plt.xlabel('$x$')
plt.ylabel('$F_T(t)$')


plt.savefig('t_cdf.pdf')


plt.show() #opening the plot window
