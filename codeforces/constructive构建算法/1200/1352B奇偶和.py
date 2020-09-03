#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/1352/B
# 1..1..X or 2..2..X

def f(l):
    n,k = l
    if n<k:
        return [['NO']]
    if (n-k)%2==0:
        return [['YES'],[1]*(k-1)+[1+n-k]]
    if n<(k<<1):
        return [['NO']]
    if (n-k-k)%2==0:
        return [['YES'],[2]*(k-1)+[2+n-k-k]]
    return [['NO']]

q = int(input())
for _ in range(q):
    l = list(map(int,input().split()))
    [print(*r) for r in f(l)]
