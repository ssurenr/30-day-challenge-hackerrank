#!/bin/python3

n = int(input().strip())
arr = input().split(' ')

for number in arr[::-1]:
    print(number, end='' + ' ')
