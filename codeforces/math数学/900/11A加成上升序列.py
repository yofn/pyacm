#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/11/A

n,d = list(map(int,input().split()))
bl  = list(map(int,input().split()))
c   = 0
for i in range(1,n):
    dd = bl[i-1]-bl[i]
    if dd<0:
        continue
    s       = dd//d + 1
    bl[i]  += s*d
    c      += s
print(c)
