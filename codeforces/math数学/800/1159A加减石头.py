#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1159/A

n   = int(input())
ol  = list(input())
ol.reverse()
c   = 0
pc  = 0
for o in ol:
    if o=='+':
        if pc==0:
            c   += 1
        else:
            pc  -= 1
    if o=='-':
        pc += 1
print(c)
