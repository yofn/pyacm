#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1136/B
# 三类move: 取(=n), 仍(=n+1), 移(n-1+min(k-1,n-k))

def f(l):
    n,k = l
    return 3*n + min(k-1,n-k)

l = list(map(int,input().split()))
print(f(l))
