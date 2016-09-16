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
import os.path

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

def getDim(arrs):

    dim = {}
    iCount = 0
    for item in arrs:
        tmp1 = item.shape
        dim[iCount] = list(tmp1)
        iCount += 1
    return dim


def createCcode(arrs, dim):

    dmap = {1 : 'j', 2 : 'k', 3 : 'l'}
    with open("main.c", 'w') as f:
        f.write("#include <stdio.h>\n\n")
        f.write("void gateWay(")
        for item in range(0, len(arrs)):
            if len(dim[item]) == 1:
                f.write("double *a"+str(item)+",")
            else:
                tstr1 = ""
                for d in range(1, len(dim[item])):
                    f.write("int "+dmap[d]+str(item)+", ")
                    tstr1 += "["+dmap[d]+str(item)+"]"
                f.write("double (*a" + str(item) + ")"+tstr1)
        f.write(")\n")
        f.write("{\n\n\n}")
    print "main.c created !"
    exit()


def getPointers(*ar):

    arrs = list(ar)
    dim = getDim(arrs)
    ptrs = {}
    iCount = 0
    for item in arrs:
        tmp1 = item.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
        ptrs[iCount] = tmp1
        iCount += 1
    if not os.path.exists("main.c"):
        createCcode(arrs, dim)
    else:
        cObj = ctypes.cdll.LoadLibrary("./main.so")
    return cObj, ptrs



# =============================================================================== #

# if __name__ == '__main__':
#     main()
#     print "# ============================  END  ============================ #"
