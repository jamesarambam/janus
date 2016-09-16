#!/home/james/anaconda2/bin/python
import sys
import os
import platform


# ================================ secImports ================================ #

os.system("rm *.so")
os.system("rm *.o")


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
