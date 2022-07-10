#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt
import scipy

#if using termux
import subprocess
import shlex
#end if

import math


x = np.linspace(-4,4,60)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
#randvar = np.random.normal(0,1,simlen)
randvar = np.loadtxt('uni.dat',dtype='double')
#randvar = np.loadtxt('gau.dat',dtype='double')
for i in range(0,60):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

def cdfUniform(x):
	if(x<=0):
		x=0
	elif(x>1):
		x=1
	return x
    
t = []
for i in range(len(x)):
	t.append(cdfUniform(x[i]))
    
    
plt.plot(x.T,err,label = 'theoretical')#plotting the CDF
plt.plot(x.T,t,'o',label = 'numerical')#plotting the CDF
plt.grid() #creating the grid
plt.legend()
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')

#if using termux
plt.savefig('uni_cdf.pdf')
#plt.savefig('uni_cdf.eps')

#if using termux
#plt.savefig('../figs/gauss_cdf.pdf')
#plt.savefig('../figs/gauss_cdf.eps')
#subprocess.run(shlex.split("termux-open ../figs/gauss_cdf.pdf"))
#else
plt.show() #opening the plot window
