#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1342/A

t = int(input())
for _ in range(t):
    x,y = list(map(int,input().split()))
    a,b = list(map(int,input().split()))
    if x>y:
        x,y=y,x
    print(min(a*(x+y),x*b+(y-x)*a))
