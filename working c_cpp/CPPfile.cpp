#include <iostream>
using namespace std;

extern "C" void gateWay2Cpp(double *a0, int i1, int j1, double (*a1)[2])
{
  cout<<"\n---- From C++ Change3 : \n";
  cout<<a1[0][0]<<"\n";
  cout<<a1[1][1]<<"\n";
  cout << a1[0][1] << "\n";
  cout<<"j1 : "<< j1 << "\n";
  cout<<"---- END C++ : \n";
}
