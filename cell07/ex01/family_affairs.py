#!/usr/bin/python3

def filter_redheads(data):

    key, value = data
    return value == "red"

def find_the_redheads(data):    
    filtered_dict = dict(filter(filter_redheads,data.items()))
    # print(filtered_dict)
    # filtered_dict = {key:value for key, value in dict.items() if value == "red"}
    return list(filtered_dict.keys())

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}

print(find_the_redheads(dupont_family))