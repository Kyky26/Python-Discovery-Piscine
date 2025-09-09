#!/usr/bin/python3

def array_of_names(dict):
    arr = []
    for key,value in dict.items():
        temp = key.capitalize() + ' ' + value.capitalize()
        arr.append(temp)
    return arr

# def array_of_names(dict):
#     arr = []
#     key = list(dict.keys())
#     value = list(dict.values())
#     for i in range(len(key)):
#         temp = key[i] + ' ' + value[i]
#         arr.append(temp.title()) #.title() is a built-in function to capitalize first letter of each words in a string
#     return arr

persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}

print(array_of_names(persons))


'''
The items() method allows the user to iterate over both keys and values simultaneously. It returns a view of key-value pairs in the dictionary as a tuples.
'''