#!/usr/bin/python3

import sys

n = len(sys.argv)

def downcase_it(string):
    return string.lower()

if (n > 1):
    for i in range(1,n):
        print(downcase_it(sys.argv[i]))
else:
    print("none")


# ./downcase_all.py "HELLO WORLD" "I understood Arrays well!"
# ./downcase_all.py "HELLO WORLD" 'I understood Arrays well!'

'''
In order to allow the terminal to be able to print out "I understood Arrays well!" successfully.

1) replace the double quote with single quote " -> '
2) or escape the !, by adding a backslash \ in front of ! to escape "...\!"
3) or like what I have did, cd -> vim .zshrc -> setopt NO_HIST_EXPAND to disable histroy 
expansion whcih is causing this error, but in order to turn it back on if required, same thing: cd -> vim .zshrc -> setopt HIST_EXPAND
'''