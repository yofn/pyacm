#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/194/A

def f(l):
    n,k = l
    return max(n*3-k,0)

l   = list(map(int,input().split()))
print(f(l))

