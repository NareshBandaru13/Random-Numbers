#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import scipy
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end if

import math
def cdf_V(x):
	if x<0: 
		x=0.00
	else:
	   return 1-np.exp(-x/2)
	
vect_cdf = scipy.vectorize(cdf_V)

x = np.linspace(-4,4,60)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
#randvar = np.random.normal(0,1,simlen)
randvar = np.loadtxt('v.dat',dtype='double')

for i in range(0,60):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

plt.plot(x.T,err,label = 'theoretical')#plotting the CDF
plt.plot(x.T,vect_cdf(x),'o',label = 'numerical')#plotting the CDF
plt.grid() #creating the grid
plt.legend()
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')

#if using termux
plt.savefig('V_cdf.pdf')
#plt.savefig('V_cdf.eps')

#if using termux
#plt.savefig('../figs/gauss_cdf.pdf')
#plt.savefig('../figs/gauss_cdf.eps')
#subprocess.run(shlex.split("termux-open ../figs/gauss_cdf.pdf"))
#else
plt.show() #opening the plot window
