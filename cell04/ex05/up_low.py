#!/usr/bin/python3

string = input()
new_string = ""

#print(len(string))
i = 0;
while(i < len(string)):
    temp = string[i]
    if (temp.isupper() == True):
        new_string = new_string + temp.lower()
    else:
        new_string = new_string + temp.upper()

    i += 1

print(new_string)