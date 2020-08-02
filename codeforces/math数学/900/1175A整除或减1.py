#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1175/A

def f(l):
    n,k = l
    c   = 0
    while n>0:
        c += (1+n%k)
        n  = n//k
    return c-1

t  = int(input())
for _ in range(t):
    l   = list(map(int,input().split()))
    print(f(l))

