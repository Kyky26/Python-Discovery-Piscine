#!/usr/bin/python3

import sys

n = len(sys.argv)

if (n == 2):
    i = 0
    count = 0
    while (i < len(sys.argv[1])):
        if (sys.argv[1][i] == 'z'):
            count += 1
        i += 1
    if (count == 0):
        print("none")
    else:
        for i in range(count):
            print("z", end="")
else:
    print("none")