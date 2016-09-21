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

import auxLib as ax
import janus.janus as jn


print "# ============================ START ============================ #"

# ============================================================================ #

# --------------------- Variables ------------------------------ #

ppath = os.getcwd() + "/"  # Project Path Location

# -------------------------------------------------------------- #

def main():

    print "Waala"

    # a0 = np.full((2), -1, dtype=np.double)
    # a0[0] = 2.2
    # a0[1] = 4.2
    #
    # a1 = np.full((2, 2), -1, dtype=np.double)
    # a1[0][0] = 5.2
    # a1[1][1] = 6.2
    #
    # cObj, ptrs = jn.getPointers(a0, a1)
    # cObj.gateWay(ptrs[0], 2, 2, ptrs[1])

    alist  = [0.0714285714286, 1, 0.0535714285714, 1, 0.535714285714, -2.07142857143]

    a0 = np.array(alist, dtype=np.double)

    a1 = np.array([-0.616071428572, -0.232142857143], dtype=np.double)

    cObj, ptrs = jn.getPointers(a0, a1)
    cObj.gateWay(ptrs[0], ptrs[1])




# =============================================================================== #

if __name__ == '__main__':
    main()
    print "# ============================  END  ============================ #"
