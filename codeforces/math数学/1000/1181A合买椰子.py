#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1181/A

def f(l):
    x,y,z=l 
    n = (x+y)//z
    d = 0 if (x%z)+(y%z)<z else z-1-max((x-1)%z,(y-1)%z)
    return [n,d]

l = list(map(int,input().split()))
print(*f(l))
