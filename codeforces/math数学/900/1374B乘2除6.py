#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1374/B


def m2d6(n):
    e2  = 0
    e3  = 0
    while n%2==0:
        n   = n//2
        e2 += 1
    while n%3==0:
        n   = n//3
        e3 += 1
    if e2>e3 or n>1:
        return -1
    return (e3<<1)-e2

t   = int(input())
for _ in range(t):
    n = int(input())
    print(m2d6(n))
