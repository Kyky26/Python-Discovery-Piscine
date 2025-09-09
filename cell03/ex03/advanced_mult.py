#!/usr/bin/python3

import sys

# total num of arguments
n = len(sys.argv)

i = 0

if (n > 1):
    print("none")
else:
    while (i <= 10):
        j = 0
        print(f"Table de {i}:", end=" ")
        while (j <= 10):
            print(i * j, end = " ")
            j += 1
        i += 1
        print()