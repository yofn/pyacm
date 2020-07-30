#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/764/A

def gcd(n,m):
    if n<m:
        n,m = m,n
    while n>0 and m>0:
        t = n
        n = m
        m = t%n
    return n

n,m,z = list(map(int,input().split()))
lca   = n*m//gcd(n,m)

print(z//lca)

