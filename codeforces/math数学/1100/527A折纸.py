#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/527/A

def f(l):
    a,b = l #a is bigger
    c   = 0
    while b>0:
        c += (a//b)
        t  = b
        b  = a%b
        a  = t
    return c

l = list(map(int,input().split()))
print(f(l))
