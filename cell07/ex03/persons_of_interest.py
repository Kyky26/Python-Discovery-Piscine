#!/usr/bin/python3

#shebang line: tells the unix system to run this script using the python3 interpreter

def famous_births(item): #define a function called famous_births to take in 1 argument which is item which is going to be the intital nested dictionary
    holding = dict(
        sorted(item.items(), key=lambda item: item[1]['date_of_birth']))
    # print(holding)

    for key,value in holding.items():
        print(f"{value['name']} is a great scientist born in {value['date_of_birth']}.")


'''
item.items will return a list of key-value pairs (tuples, tuples means unchangeable)
[
  ("ada", {"name": "Ada Lovelace", "date_of_birth": "1815"}),
  ("cecilia", {"name": "Cecila Payne", "date_of_birth": "1900"}),
  ...
]

sorted(..., key=lambda item: item[1]['date_of_birth']))
- This will sort those pairs according to the date_of_birth value inside the nested loop (Ascending order by default)
- item[1]: Inner dictionary (for example: {"name": "Ada Lovelace", "date_of_birth": "1815"}, ...)
- item[1]['date_of_birth'] accesses the birth year

dict(...) at the start will turn the 
'''

women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

famous_births(women_scientists)