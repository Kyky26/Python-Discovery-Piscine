#!/usr/bin/env python3

password = "Python is awesome"

pass_code = input().strip()

if (pass_code == password):
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")