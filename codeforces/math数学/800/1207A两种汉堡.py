#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1207/A

t = int(input())
for _ in range(t):
    b,p,f   = list(map(int,input().split()))
    h,c     = list(map(int,input().split()))
    b1      = min(b//2,p) if h>c else min(b//2,f)
    b2      = (b//2)-b1
    b2      = min(b2,f)   if h>c else min(b2,p)
    print(b1*h+b2*c if h>c else b1*c+b2*h)
