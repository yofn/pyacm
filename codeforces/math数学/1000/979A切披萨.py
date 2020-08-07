#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/979/A
# 4->2, 8->4, ..

def f(n):
    if n==1:
        return 0
    return n//2 if n%2==0 else n

n = int(input())
print(f(n+1))
