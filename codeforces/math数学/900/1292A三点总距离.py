#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1292/B

def f(l):
    mx  = max(l)
    mn  = min(l)
    return max((mx-mn-2)<<1,0)

t  = int(input())
for _ in range(t):
    l   = list(map(int,input().split()))
    print(f(l))

