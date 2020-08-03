#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/267/A

def f(l):
    b,s = max(l), min(l)
    c   = 0
    while s>0:
        c += b//s
        t  = s
        s  = b%s
        b  = t
    return c

t  = int(input())
for _ in range(t):
    l   = list(map(int,input().split()))
    print(f(l))

