#include <stdio.h>

extern void gateWay2Cpp(double *, int , int , double (*)[2]);

void gateWay(double *a0, int i1, int j1, double a1[2][2])
{
  gateWay2Cpp(a0, i1, j1, a1);

}
