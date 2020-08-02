#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1183/A

def f(l,k):
    mi = min(l)
    mx = max(l)
    if mx-k>mi+k:
        return -1
    return mi+k

t  = int(input())
for _ in range(t):
    n,k = list(map(int,input().split()))
    l   = list(map(int,input().split()))
    print(f(l,k))

