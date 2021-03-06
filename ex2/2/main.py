#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt
import scipy

#if using termux
import subprocess
import shlex
#end if

import math
def Q(x):
   return (math.erfc(x/math.sqrt(2)))/2.0
def F(x):
   return 1 - Q(x)
vec_F = scipy.vectorize(F)

x = np.linspace(-4,4,60)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
#randvar = np.random.normal(0,1,simlen)
#randvar = np.loadtxt('uni.dat',dtype='double')
randvar = np.loadtxt('gau.dat',dtype='double')
for i in range(0,60):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list
	
plt.plot(x.T,err,label = 'theoretical')#plotting the CDF
plt.plot(x.T,vec_F(x),'o',label = 'numerical')#plotting the CDF
plt.grid() #creating the grid
plt.legend()
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')



#if using termux
plt.savefig('gau_cdf.pdf')
#plt.savefig('gau_cdf.eps')

#if using termux
#plt.savefig('../figs/gauss_cdf.pdf')
#plt.savefig('../figs/gauss_cdf.eps')
#subprocess.run(shlex.split("termux-open ../figs/gauss_cdf.pdf"))
#else
plt.show() #opening the plot window
