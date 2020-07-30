#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1077/A

t = int(input())
for _ in range(t):
    a,b,k   = list(map(int,input().split()))
    p       = (a-b)*(k//2)
    print(p+a*(k%2))
