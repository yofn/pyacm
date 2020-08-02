#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1016/A

def f(l,m):
    n = len(l)
    for i in range(1,n):
        l[i] += l[i-1]
    bl = [x//m for x in l]
    for i in range(n-1,0,-1):
        bl[i]-= bl[i-1]
    return bl

_,m = list(map(int,input().split()))
l   = list(map(int,input().split()))
print(*f(l,m))

