#!/usr/bin/python3

def add_one(parameter):
    parameter = parameter + 1
    return parameter

if __name__ == "__main__":
    var = 9
    print("var:", var)
    new_var = add_one(var)
    print("After add_one func:",new_var)

'''
Observed that when the variable is passed into the add_one function, the add_one function takes that parameter and then add one to it and returns it.
So when we assign it to the new_var, we can see that the initial var is 9 and the new_var after passing into the function gives 10 now.
'''