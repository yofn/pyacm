#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/318/A

def f(l):
    n, k = l
    odd =      k <=  (n+1)//2
    off = ((k-1)  % ((n+1)//2)) + 1
    return (off<<1)-1 if odd else (off<<1)

l   = list(map(int,input().split()))
print(f(l))

