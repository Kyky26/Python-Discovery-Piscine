#!/usr/bin/python3

arr = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = []

for i in range(len(arr)):
    if(arr[i] > 5):
        new_array.append(arr[i]+2)
    else:
        continue

print(arr)
print(new_array)