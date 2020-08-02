#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/598/A

t  = int(input())
for _ in range(t):
    n   = int(input())  #1e9
    s   = 1
    while s<=n:
        s = s<<1
    ss  = (n//2) * (n+1) if n%2==0 else ((n+1)//2)*n
    print(ss-(s<<1)+2)

