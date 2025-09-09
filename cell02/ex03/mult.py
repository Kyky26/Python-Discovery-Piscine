#!/usr/bin/env python3

first = int(input("Enter the first number:\n"))
second = int(input("Enter the second number:\n"))

number = first * second

print(f"{first} x {second} =", number)

if (number == 0):
    print("This number is both positive and negative.")
elif (number > 0):
    print("This number is positive.")
else:
    print("This number is negative.")