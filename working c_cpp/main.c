#include <stdio.h>

extern void gateWay2Cpp(double *, int , int , double (*)[2]);

void gateWay(double *a0, int i1, int j1, double a1[2][2])
{

  printf("---- From C Change3 : \n");
  printf("%f\n", a1[0][0]);
  printf("%f\n", a1[1][1]);
  printf("j1 : %d", j1);
  printf("----- END C \n");
  a1[0][1] = 3.2;

  gateWay2Cpp(a0, i1, j1, a1);

}
