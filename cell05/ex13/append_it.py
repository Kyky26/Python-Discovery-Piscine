#!/usr/bin/python3

import sys

n = len(sys.argv)

if (n > 1):
    i = 0
    count = 0

    for i in range(1,n):
        if ("ism" not in sys.argv[i]):
            print(sys.argv[i] + "ism")
        else:
            continue
else:
    print("none")