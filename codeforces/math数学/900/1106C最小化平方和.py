#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1106/C
# 尽可能的接近,才能最小化平方和..最小和最大配对?

def f(l):
    l.sort()
    n = len(l)
    return sum([(l[i]+l[n-1-i])**2 for i in range(n//2)])

_   = input()
l   = list(map(int,input().split()))
print(f(l))

