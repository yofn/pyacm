#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1066/A

def f(ll):
    n,v,l,r = ll    #1e9
    lc = (l-1)//v
    rc = r//v
    tc = n//v
    return lc + tc - rc

q = int(input())    #1e4
for _ in range(q):
    l = list(map(int,input().split()))
    print(f(l))
