#!/usr/bin/python3

import sys

def greetings(name = ""): #name requires a positional argument so cannot only put name, have to put name="" or name=None
    if (name == ""):
        name = "noble stranger"
    if (type(name) == str):
        print(f"Hello, {name}.")
    else:
        print("Error! It was not a name.")


greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)

