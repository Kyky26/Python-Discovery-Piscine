#!/usr/bin/python3

def shrink(string):
    print(string[:8])

def enlarge(string):
    size = len(string)
    if (size >= 8):
        shrink(string)
    else:
        string = string.split()
        # print("else:", size)
        for i in range(8 - size):
            string.append('Z')
        print("".join(string))

import sys

n = len(sys.argv)

if (n < 2):
    print("none")
else:
    for i in range(n):
        enlarge(sys.argv[i])

# ./methods_everywhere.py | cat -e
# ./methods_everywhere.py 'lol' 'physically' 'backpack' | cat -e