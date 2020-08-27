#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/858/A

def f(l):
    n,k = l
    e2  = 0
    e5  = 0
    while n%(2**e2)==0:
        e2 += 1
    e2 -= 1
    while n%(5**e5)==0:
        e5 += 1
    e5 -= 1
    return n*(2**(max(0,k-e2)))*(5**(max(0,k-e5)))

l = list(map(int,input().split()))
print(f(l))
