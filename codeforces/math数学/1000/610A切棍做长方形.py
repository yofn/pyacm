#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/610/A

def f(n):
    if n%2>0:
        return 0
    n = n//2
    return (n-1)//2

n = int(input())
print(f(n))
