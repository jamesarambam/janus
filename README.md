# janus
Janus is a python wrapper for interfacing numpy array to c++ array. c-types does the same job for C but there is no such library for C++. There are many libraries for extending python to C++ but I couldn't find a simple way to interface numpy array to C++ array.

```python
# --------------- main.py ------------ #
import numpy as np
import janus as jn

# create and initialize 1-D numpy array
a0 = np.full((2), -1, dtype=np.double)
a0[0] = 2.2
a0[1] = 4.2

# create and initialize 2-D numpy array
a1 = np.full((2, 2), -1, dtype=np.double)
a1[0][0] = 5.2
a1[1][1] = 6.2

cObj, ptrs = jn.getPointers(a0, a1)
cObj.gateWay(2, ptrs[0], 2, 2, ptrs[1])
```


```cpp
// ------------- CPPfile.cpp -------------- //
#include <iostream>
using namespace std;

extern "C" void gateWay2Cpp(int i0, double *a0, int i1, int j1, double (*a1)[2])
{
  cout<<"\n---- From C++ Change3 : \n";
  cout<<a1[0][0]<<"\n";
  cout<<a1[1][1]<<"\n";
  cout << a1[0][1] << "\n";
  cout<<"j1 : "<< j1 << "\n";
  cout<<"---- END C++ : \n";
  
}
```
For compiling C++ code run "compile.py" first and then you can run the python code. 
