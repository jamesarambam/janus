#include <iostream>
using namespace std;

extern "C" void gateWay2Cpp(int i0, double *a0, int i1, double *a1,
{

  cout<<"Waala from C++"<<"\n";
  cout<<"\n -------------------- \n";

   double lb = a1[0];
   double ub = a1[1];
   int param_len = i0;
   double root = getRoot2(a0, param_len, lb, ub);
   cout<<"Root : "<<root<<"\n";



}
