#!/usr/bin/env bash
rm *.o
rm *.so
g++ -c -Wall -Werror -fPIC CPPfile.cpp
g++ -shared -o libCPPfile.so CPPfile.o
gcc -c -fPIC -Wall main.c -L/Users/james/PycharmProjects/janus -lCPPfile
gcc main.o -shared -o main.so -L/Users/james/PycharmProjects/janus -lCPPfile
export LD_LIBRARY_PATH=/Users/james/PycharmProjects/janus:$LD_LIBRARY_PATH
