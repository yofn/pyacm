#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/818/A

n,k = list(map(int,input().split()))
r   = n//((k+1)<<1)
print(r,r*k,n-r*(k+1))

