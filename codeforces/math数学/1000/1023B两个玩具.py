#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1023/A

def f(ll):
    n,k = ll    #1e14
    f   = k//2 + 1
    e   = min(k-1,n)
    return max(0,e-f+1)

l = list(map(int,input().split()))
print(f(l))
