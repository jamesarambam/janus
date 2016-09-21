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

    dmap = {0 : 'i', 1 : 'j', 2 : 'k', 3 : 'l', 4 : 'm'}
    with open("main.c", 'w') as f:
        f.write("#include <stdio.h>\n\n")
        f.write("extern void gateWay2Cpp(")
        tstr = ""
        for item in range(0, len(arrs)):
            if len(dim[item]) == 1:
                tstr += reduce(lambda v1, v2 : v1+""+v2, map(lambda x : "int , ", [i for i in range(len(dim[item]))]))
                tstr += "double *, "
            else:
                tstr += reduce(lambda v1, v2 : v1+""+v2, map(lambda x : "int , ", [i for i in range(len(dim[item]))]))
                tstr += "double (*)"+reduce(lambda  v1, v2 : v1+""+v2, map(lambda x : "["+str(dim[item][x])+"], ", [i for i in range(1, len(dim[item]))]))
        f.write(tstr[0:len(tstr)-2]+");")
        tstr = ""
        f.write("\n\nvoid gateWay(")
        for item in range(0, len(arrs)):
            if len(dim[item]) == 1:
                tstr += reduce(lambda v1, v2 : v1+""+v2, map(lambda x : "int "+dmap[x]+str(item)+", ", [i for i in range(len(dim[item]))]))
                tstr += "double *a"+str(item)+","
            else:
                tstr += reduce(lambda v1, v2 : v1+""+v2, map(lambda x : "int "+dmap[x]+str(item)+", ", [i for i in range(len(dim[item]))]))
                tstr += "double a"+ str(item) +reduce(lambda  v1, v2 : v1+""+v2, map(lambda x : "["+str(dim[item][x])+"]", [i for i in range(len(dim[item]))]))
                tstr += ", "
        tstr = tstr[0:len(tstr)-2]
        f.write(tstr)
        f.write(")")
        f.write("\n")
        f.write("{\n\n")
        f.write("  gateWay2Cpp(")
        tstr = ""
        for item in range(0, len(arrs)):
            if len(dim[item]) == 1:
                tstr += reduce(lambda v1, v2 : v1+""+v2, map(lambda x : dmap[x]+str(item)+", ", [i for i in range(len(dim[item]))]))
                tstr += "a"+str(item)+", "
            else:
                tstr += reduce(lambda v1, v2 : v1+""+v2, map(lambda x : dmap[x]+str(item)+", ", [i for i in range(len(dim[item]))]))
                tstr += "a"+ str(item)
                tstr += ", "

        tstr = tstr[0:len(tstr)-2]
        f.write(tstr)
        f.write(");")
        f.write("\n\n}")
    print "main.c created !"


def createCppCode(arrs, dim):

    dmap = {0 : 'i', 1 : 'j', 2 : 'k', 3 : 'l', 4 : 'm'}
    with open("CPPfile.cpp", 'w') as f:
        f.write("#include <iostream>\n")
        f.write("using namespace std;\n\n")
        f.write('extern "C" void gateWay2Cpp(')
        tstr = ""
        for item in range(0, len(arrs)):
            if len(dim[item]) == 1:
                tstr += reduce(lambda v1, v2 : v1+""+v2, map(lambda x : "int "+dmap[x]+str(item)+", ", [i for i in range(len(dim[item]))]))
                tstr += "double *a"+str(item)+", "
            else:
                tstr += reduce(lambda v1, v2 : v1+""+v2, map(lambda x : "int "+dmap[x]+str(item)+", ", [i for i in range(len(dim[item]))]))
                tstr += "double (*a"+ str(item)+")" +reduce(lambda  v1, v2 : v1+""+v2, map(lambda x : "["+str(dim[item][x])+"]", [i for i in range(1, len(dim[item]))]))
                tstr += ", "
        tstr = tstr[0:len(tstr)-2]
        f.write(tstr)
        f.write(")")
        f.write("\n")
        f.write("{\n\n\n}")
    print "CPPfile.cpp created !"



def getPointers(*ar):

    arrs = list(ar)
    dim = getDim(arrs)
    ptrs = {}
    iCount = 0
    for item in arrs:
        tmp1 = item.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
        ptrs[iCount] = tmp1
        iCount += 1

    if not (os.path.exists("main.c") and os.path.exists("CPPfile.cpp")):
        createCcode(arrs, dim)
        createCppCode(arrs, dim)
        exit()
    else:
        cObj = ctypes.cdll.LoadLibrary("./main.so")


    return cObj, ptrs



# =============================================================================== #

# if __name__ == '__main__':
#     main()
#     print "# ============================  END  ============================ #"
