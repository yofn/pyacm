#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/996/A

total = int(input())
bills = [100,20,10,5,1]
nob   = 0
for b in bills:
    nob     += total//b
    total    = total%b
    if total == 0:
        break
print(nob)
