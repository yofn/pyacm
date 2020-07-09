#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1355/B

def groups(a):
    a.sort()
    nog = 0
    n   = len(a)
    l   = 0
    r   = l+a[l]-1
    while r<n:
        if  r < l+a[r]-1:
            r = l+a[r]-1
            continue
        nog += 1
        l    = r+1
        if l>n-1:
            break
        r    = l+a[l]-1
    return nog

rl  = []
for i in range(int(input())):
    _ = int(input())
    a = list(map(int,input().split()))
    rl.append(groups(a))
[print(r) for r in rl]
