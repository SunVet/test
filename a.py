#!/usr/bin python3
arr = [0,1,2,1,2,3,4,5,5,7,6,6,6]

x=0
while x < len(arr):
    y = x+1
    while y < len(arr):
        if arr[x] == arr[y]:
            arr.pop(y)
            continue
        y+=1
    x+=1
print(arr)
