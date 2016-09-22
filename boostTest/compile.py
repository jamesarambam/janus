#!/home/james/anaconda2/bin/python
import sys
import os
import platform


# ================================ secImports ================================ #

ppath = os.getcwd()

os.system("rm *.so")
os.system("rm *.o")
o = platform.system()

compArg_C = []
compArg_Cpp = ["-I/home/james/boost/include/ -L/home/james/boost/lib/"]
compArg_Cpp = []

cArg = ""
cppArg = ""
if len(compArg_C) > 0 :
    cArg = reduce(lambda v1, v2 : v1+" "+v2, compArg_C)
if len(compArg_Cpp) > 0 :
    cppArg = reduce(lambda v1, v2 : v1+" "+v2, compArg_Cpp)


# =============== Execute This First ================= #
# print "export LD_LIBRARY_PATH="+ppath+":$LD_LIBRARY_PATH"
# exit()
# ==================================================== #



if o == "Linux":
    d = platform.dist()
    if d[0] == "debian":
#        os.system("export LD_LIBRARY_PATH="+ppath+":$LD_LIBRARY_PATH")
        os.system("g++ -c -Wall -Werror -fPIC CPPfile.cpp "+cppArg)
        os.system("g++ -shared -o libCPPfile.so CPPfile.o "+cppArg)
        os.system("gcc -c -fPIC -Wall main.c -L"+ppath+ " -lCPPfile "+cArg)
        os.system("gcc main.o -shared -o main.so -L"+ppath+" -lCPPfile "+cArg)

    if d[0] == "centos":
        os.system("export LD_LIBRARY_PATH="+ppath+":$LD_LIBRARY_PATH")
        os.system("g++ -c -Wall -Werror -fPIC CPPfile.cpp "+cppArg)
        os.system("g++ -shared -o libCPPfile.so CPPfile.o "+cppArg)
        os.system("gcc -c -fPIC -Wall main.c -L"+ppath+ " -lCPPfile "+cArg)
        os.system("gcc main.o -shared -o main.so -L"+ppath+" -lCPPfile "+cArg)

if o == "Darwin":
    os.system("export LD_LIBRARY_PATH="+ppath+":$LD_LIBRARY_PATH")
    os.system("g++ -c -Wall -Werror -fPIC CPPfile.cpp " + cppArg)
    os.system("g++ -shared -o libCPPfile.so CPPfile.o " + cppArg)
    os.system("gcc -c -fPIC -Wall main.c -L" + ppath + " -lCPPfile " + cArg)
    os.system("gcc main.o -shared -o main.so -L" + ppath + " -lCPPfile " + cArg)






"""
o = platform.system()
if o == "Linux":
    d = platform.dist()
    if d[0] == "debian":
        os.system("gcc -std=gnu99 -c -fPIC main.c")
        os.system("gcc -std=gnu99 main.o -shared -o main.so")

    if d[0] == "centos":
        os.system("gcc -std=gnu99 -c -fPIC main.c")
        os.system("gcc -std=gnu99 main.o -shared -o main.so")

if o == "Darwin":
    os.system("gcc -std=gnu99 -c -fPIC main.c")
    os.system("gcc -std=gnu99 main.o -shared -o main.so")
"""
