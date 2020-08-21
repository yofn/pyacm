#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1195/A

def f(l):
    mx = max(l)
    n  = len(l)
    cl = [0]*mx
    for i in l:
        cl[i-1] += 1
    np = sum([c//2 for c in cl])    # number of pairs
    return (np<<1)+(n-(np<<1)+1)//2

n,k = list(map(int,input().split()))
l   = [int(input()) for _ in range(n)]
print(f(l))
