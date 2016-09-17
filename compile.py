#!/home/james/anaconda2/bin/python
import sys
import os
import platform


# ================================ secImports ================================ #

os.system("rm *.so")
os.system("rm *.o")


ppath = os.getcwd()

o = platform.system()
if o == "Linux":
    d = platform.dist()
    if d[0] == "debian":
        os.system("g++ -c -Wall -Werror -fPIC CPPfile.cpp")
        os.system("g++ -shared -o libCPPfile.so CPPfile.o")
        os.system("gcc -c -fPIC -Wall main.c -L"+ppath+ " -lCPPfile")
        os.system("gcc main.o -shared -o main.so -L"+ppath+" -lCPPfile")
        os.system("export LD_LIBRARY_PATH="+ppath+":$LD_LIBRARY_PATH")

    if d[0] == "centos":
        os.system("g++ -c -Wall -Werror -fPIC CPPfile.cpp")
        os.system("g++ -shared -o libCPPfile.so CPPfile.o")
        os.system("gcc -c -fPIC -Wall main.c -L"+ppath+ " -lCPPfile")
        os.system("gcc main.o -shared -o main.so -L"+ppath+" -lCPPfile")
        os.system("export LD_LIBRARY_PATH="+ppath+":$LD_LIBRARY_PATH")

if o == "Darwin":
    os.system("g++ -c -Wall -Werror -fPIC CPPfile.cpp")
    os.system("g++ -shared -o libCPPfile.so CPPfile.o")
    os.system("gcc -c -fPIC -Wall main.c -L"+ppath+ " -lCPPfile")
    os.system("gcc main.o -shared -o main.so -L"+ppath+" -lCPPfile")
    os.system("export LD_LIBRARY_PATH="+ppath+":$LD_LIBRARY_PATH")









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