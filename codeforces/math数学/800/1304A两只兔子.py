#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1304/A

t = int(input())
for _ in range(t):
    x,y,a,b = list(map(int,input().split()))
    if (y-x)%(a+b)!=0:
        print(-1)
    else:
        print((y-x)//(a+b))
         
