#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/931/A

a   = int(input())
b   = int(input())
d   = a-b if a>b else b-a
n   = d//2
c   = 0 if d%2==0 else n+1
for i in range(1,n+1):
    c += (i<<1)
print(c)
