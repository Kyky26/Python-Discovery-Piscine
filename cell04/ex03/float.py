#!/usr/bin/python3

number = float(input("Give me a number: "))

if (int(number) == number): #if float value = integer value 
    print("This number is an integer.")
else:
    print("This number is a decimal.")

#int('3.3') will give valuerror, therefore, we will have to do float('3.3') to convert into float befoe we
#compare it to the typecast int(3.3) will gives 3.
# So 3.3 != 3, so it is a decimal, if the string is '3.0', then float will give 3.0 and int will give 3. So from here we know that the string is an integer.