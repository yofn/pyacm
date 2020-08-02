#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/697/A
# 需要考虑的全面些.

def f(l):
    t,s,x = l
    d     = x-t
    return (d==0 or (d>=s and d%s<2))

l   = list(map(int,input().split()))
print('YES' if f(l) else 'NO')

