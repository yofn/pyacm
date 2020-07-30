#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/950/A

l,r,a   = list(map(int,input().split()))
mipa    = min(l,r) + a
print((mipa<<1) if mipa <= max(l,r) else (((l+r+a)//2)<<1))
