#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1283/B

def f(l):
    n,k = l
    return min(n, (n//k)*k + (k>>1))

t  = int(input())
for _ in range(t):
    l   = list(map(int,input().split()))
    print(f(l))

