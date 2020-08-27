#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1332/A

def f(l):
    a,c = l
    p = 1
    r = 0
    while a>0 or c>0:
        r += p*((c%3-a%3)%3)
        p *= 3
        c  = c//3
        a  = a//3
    return r

l = list(map(int,input().split()))
print(f(l))
