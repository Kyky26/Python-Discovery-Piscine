#!/usr/bin/python3

import sys

n = len(sys.argv)

if (n == 2):
    print((sys.argv[1]).lower())
else:
    print("none")

# ./downcase_it.py | cat -e
# ./downcase_it.py "LUCIOLE" | cat -e
# ./downcase_it.py 'This exercise is quite easy!' | cat -e