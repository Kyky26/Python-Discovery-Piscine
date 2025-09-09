#!/usr/bin/python3

import math

number = float(input("Give me a number: "))

print(math.ceil(number))


#Another method:
'''
print("orginal:",number)
diff = number - int(number)
if (diff > 0):
    number = int(number) + 1
if (diff <= 0):
    number = int(number)

print(number)
'''

