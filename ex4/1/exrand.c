#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"

int  main(void) //main function begins
{
 
//Uniform random numbers
uniform("uni1.dat", 1000000);
uniform("uni2.dat", 1000000);

//Gaussian random numbers
//gaussian("gau.dat", 1000000);

//double mn,var;
//mn = mean("uni.dat");
//var = variance("uni.dat",mn);

//printf("mean = %lf\nvariance = %lf\n",mn,var);

//Mean of uniform
//printf("%lf",mean("uni.dat"));
return 0;
}
