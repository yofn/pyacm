#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1368/A

for abn in [list(map(int,input().split())) for _ in range(int(input()))]:
    a,b,n = abn
    b,s   = max(a,b),min(a,b)
    i     = 0
    while b<=n: 
        b,s = b+s,b
        i  += 1
    print(i)
