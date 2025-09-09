#!/usr/bin/python3

import sys

n = len(sys.argv)

if (n == 3):
    count = 0
    check = sys.argv[1]
    content = sys.argv[2]
    content = content.split(" ")
    for i in range(len(content)):
        if (check == content[i]):
            count += 1
        else:
            continue
    if (count > 0):
        print(count)
    else:
        print("none")
else:
    print("none")


# Another method
'''
if (n == 3):
    count = (sys.argv[2]).count(sys.argv[1])
    if (count > 0):
        print(count)
    else:
        print("none")
else:
    print("none")
'''

# ./scan_it.py "the" "the quick brown fox jumps over the lazy dog" | cat -e
# ./scan_it.py "123" "the quick brown fox jumps over the lazy dog" | cat -e
# ./scan_it.py "the" | cat -e
# ./scan_it.py | cat -e