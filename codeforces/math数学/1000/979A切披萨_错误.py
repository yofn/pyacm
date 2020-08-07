#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/979/A
# 4->2, 8->4, ..

def f(n):
    e   = 0
    while n%2==0:
        n  = n//2
        e += 1
    return 2**(e-1))*n if e>0 else n

n = int(input())
print(f(n+1))
