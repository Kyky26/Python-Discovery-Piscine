#!/usr/bin/python3

import sys

n = len(sys.argv)

if (n < 3):
    print("none")
else:
    for i in range(1,n):
        print(sys.argv[n-i])


# ./aff_rev_params.py "Python" "piscine" "hello" | cat -e
# ./aff_rev_params.py "coucou" | cat -e
# ./aff_rev_params.py | cat -e
