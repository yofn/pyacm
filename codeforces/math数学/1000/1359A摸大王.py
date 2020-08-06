#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1359/A

t = int(input())
for _ in range(t):
    n,m,k   = list(map(int,input().split()))
    winner  = min(n//k,m)
    second  = (m-winner+k-2)//(k-1)
    print(winner-second)
