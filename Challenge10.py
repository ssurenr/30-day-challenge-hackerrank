#!/bin/python3

count = 0
countstore = []

n = int(input().strip())
binary = str(bin(n))[2:]

for letter in binary:
    if letter == "1":
        count = count + 1
        countstore.append(count)
    else:
        count = 0

print(max(countstore))
