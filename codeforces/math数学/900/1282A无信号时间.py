#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1282/A

def f(l):
    a,b,c,r = l
    if a>b:
        a,b = b,a
    c1 = c-r
    c2 = c+r
    if b<=c1  or a>=c2:
        return b-a
    return max(c1-a,0) + max(0,b-c2)

t  = int(input())
for _ in range(t):
    l   = list(map(int,input().split()))
    print(f(l))

