#include <stdio.h>

void gateWay(double *a0, int j1, double (*a1)[j1])
{
    printf("---- From C : \n");

    printf("-------arr 0 --------\n");
    printf("%f\n", a0[0]);
    printf("%f\n", a0[1]);

    printf("-------arr 1 --------\n");
    printf("%f\n", a1[0][0]);
    printf("%f\n", a1[1][1]);
    printf("n : %d", j1);
    printf("\n----- END C \n");

}
