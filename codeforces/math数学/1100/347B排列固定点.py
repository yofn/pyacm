#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/347/B

def f(l):
    n  = len(l)
    c  = sum([i==l[i] for i in range(n)])
    if c==n:
        return c
    d  = sum([l[l[i]]==i for i in range(n) if i!=l[i]])
    return c+2 if d>0 else c+1

q = int(input())
l = list(map(int,input().split()))
print(f(l))
