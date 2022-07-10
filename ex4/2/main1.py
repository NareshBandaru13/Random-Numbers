#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import mpmath as mp
import scipy 
import matplotlib.pyplot as plt

maxrange=100
maxlim=6.0
x = np.linspace(-maxlim,maxlim,maxrange)#points on the x axis
simlen = int(1e6) #total number of samples
err = [] #declaring probability list
pdf = [] #declaring pdf list
h = 2*maxlim/(maxrange-1);

#randvar = np.random.normal(0,1,simlen)
#randvar = np.loadtxt('uni.dat',dtype='double')
randvar = np.loadtxt('t.dat',dtype='double')

for i in range(0,maxrange):
	err_ind = np.nonzero(randvar < x[i]) #checking each entry in t.dat < some value in x
	err_n = np.size(err_ind) #noof elements in err_int
	err.append(err_n/simlen) #storing the probability values in a list

	
for i in range(0,maxrange-1):
	test = (err[i+1]-err[i])/(x[i+1]-x[i])
	pdf.append(test) #storing the pdf values in a list



plt.plot(x[0:(maxrange-1)].T,pdf,'o')
plt.grid() #creating the grid
plt.xlabel('$x_i$')
plt.ylabel('$p_T(t_i)$')
plt.legend(["Numerical","Theory"])


plt.savefig('t.pdf')
plt.show() #opening the plot window
