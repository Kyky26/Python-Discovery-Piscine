#!/usr/bin/python3

import sys

n = len(sys.argv)

if (n > 2):
    print("parameters:",n-1)
    for i in range(1,n):
        argu = sys.argv[i]
        length = len(sys.argv[i])
        print(f"{argu}: {length}")
else:
    print("none")



# ./count_it.py "Game" "of" "Thrones" | cat -e