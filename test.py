#!/home/james/anaconda2/bin/python
"""
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Author : James Arambam
Date   : 16 Sep 2016
Description :
Input : 
Output : 

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""

# ================================ priImports ================================ #

import sys
import os
import platform
from pprint import pprint
import numpy as np
import ctypes

# ================================ secImports ================================ #

o = platform.system()
if o == "Linux":
    d = platform.dist()
    if d[0] == "debian":
        sys.path.append("/media/james/Storage/PyCharmProjects")
    if d[0] == "centos":
        sys.path.append("/home/ajsingh/PycharmProjects")
if o == "Darwin":
    sys.path.append("/Users/james/PycharmProjects")

import auxLib.auxLib as ax

print "# ============================ START ============================ #"

# ============================================================================ #

# --------------------- Variables ------------------------------ #

ppath = os.getcwd() + "/"  # Project Path Location

# -------------------------------------------------------------- #


def main():

    a1 = np.full((2), -1, dtype=np.double)
    a1[0] = 2.2
    a1[1] = 4.2

    a2 = np.full((2, 2), -1, dtype=np.double)
    a2[0][0] = 5.2
    a2[1][1] = 6.2

    cInt, ptrs = getPointers(a1, a2)


# =============================================================================== #

if __name__ == '__main__':
    main()
    print "# ============================  END  ============================ #"


"""

import ctypes
import numpy as np
test = ctypes.cdll.LoadLibrary("./main.so")
arr = np.full((2, 2), -1, dtype = np.double)

arr[0][0] = 2.2
arr[1][1] = 4.2

arr_ptr = arr.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
test.gateWay(2, arr_ptr)
print "from python "
print arr

-------------- C -----------

#include <stdio.h>

extern void gateWay2Cpp(int, double (*)[2]);

void gateWay(int dj, double (*arrC)[dj])
{
    printf("---- From C : \n");
    printf("%f\n", arrC[0][0]);
    printf("%f\n", arrC[1][1]);
    printf("df : %d", dj);
    printf("----- END C \n");
    arrC[0][1] = 3.2;
    gateWay2Cpp(dj, arrC);
    //gateWay2Cpp(arrC);
}



"""