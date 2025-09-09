#!/usr/bin/python3

import sys

n = len(sys.argv)

if (n == 2):
    print((sys.argv[1]).upper())
else:
    print("none")

# ./upcase_it.py | cat -e
# ./upcase_it.py "initiation" | cat -e
# ./upcase_it.py 'This exercise is quite easy!' | cat -e