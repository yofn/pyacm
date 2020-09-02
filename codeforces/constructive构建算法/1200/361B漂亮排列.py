#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/361/B
# k最大n-1,最小0

def f(l):
    n,k = l
    return [-1] if k>=n else [n-k]+list(range(1,n-k))+list(range(n-k+1,n+1)) 

l = list(map(int,input().split()))
print(*f(l))
