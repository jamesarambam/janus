#!/usr/bin/env bash
rm *.o
rm *.so
g++ -c -Wall -Werror -fPIC CPPfile.cpp
g++ -shared -o libCPPfile.so CPPfile.o
gcc -c -fPIC -Wall main.c -L/media/james/Storage/PyCharmProjects/janus/boostTest -lCPPfile
gcc main.o -shared -o main.so -L/media/james/Storage/PyCharmProjects/janus/boostTest -lCPPfile
export LD_LIBRARY_PATH=/media/james/Storage/PyCharmProjects/janus/boostTest:$LD_LIBRARY_PATH
