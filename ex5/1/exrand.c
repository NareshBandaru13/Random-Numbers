#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"

int  main(void) //main function begins
{
 
//Uniform random numbers
gaussian("gau1.dat",1000000);
gaussian("gau2.dat",1000000);
v("v.dat",1000000);
//Mean of uniform
//printf("%lf",mean("uni.dat"));
return 0;
}
