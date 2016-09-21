#include <iostream>
#include "gslBrent.h"

using namespace std;

extern "C" void gateWay2Cpp(double *a0,  double *a1)
{
			cout<<"Waala from C++"<<"\n";
			cout<<"\n -------------------- \n";

       double lb = a1[0];
       double ub = a1[1];
       int param_len = 6;
       double root = getRoot2(a0, param_len, lb, ub);
       cout<<"Root : "<<root<<"\n";


}
