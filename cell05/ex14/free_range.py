#!/usr/bin/python3

import sys

n = len(sys.argv)

if (n == 3):
    arr = []
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    for i in range(start,end+1):
        arr.append(i)
    print(arr)
else:
    print("none")