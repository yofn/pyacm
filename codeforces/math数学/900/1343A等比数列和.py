#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1343/A

def f(n):
    pk = 4
    while n%(pk-1)!=0:
        pk = pk<<1
    return n//(pk-1)

t  = int(input())
for _ in range(t):
    n   = int(input())
    print(f(n))

