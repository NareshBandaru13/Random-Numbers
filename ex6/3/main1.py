#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import mpmath as mp
import scipy 
import scipy.special as sc
import matplotlib.pyplot as plt

maxrange=100
maxlim=6.0
x = np.linspace(-maxlim,maxlim,maxrange)#points on the x axis
simlen = int(1e6) #total number of samples
err = [] #declaring probability list
pdf = [] #declaring pdf list
h = 2*maxlim/(maxrange-1);

randvar = np.loadtxt('a.dat',dtype='double')

for i in range(0,maxrange):
	err_ind = np.nonzero(randvar < x[i]) #checking each entry in t.dat < some value in x
	err_n = np.size(err_ind) #noof elements in err_int
	err.append(err_n/simlen) #storing the probability values in a list

	
for i in range(0,maxrange-1):
	test = (err[i+1]-err[i])/(x[i+1]-x[i])
	pdf.append(test) #storing the pdf values in a list

def a_pdf(x):
    if(x<0):
        return 0.00
    else:
        return x*(np.exp(-x*x/2))
	
vec_a_pdf = scipy.vectorize(a_pdf)

plt.plot(x[0:(maxrange-1)].T,pdf,'o')
plt.plot(x,vec_a_pdf(x))#plotting the CDF
plt.grid() #creating the grid
plt.xlabel('$a_i$')
plt.ylabel('$p_A(a_i)$')
plt.legend(["Numerical","Theory"])


plt.savefig('a_pdf.pdf')
plt.show() #opening the plot window
