#!/usr/bin/env python3
import sys

entry_count = int(input())
entries = {}

for count in range(entry_count):
    response = input().split(" ")
    entries[response[0]] = response[1]

lookup_list = []

lookup_entries = str(sys.stdin.read()).splitlines()
count = 0

for lookup in lookup_entries:
    if lookup in entries:
        print("{0}={1}".format(lookup, entries[lookup]))
    else:
        print("Not found")
