#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1196/A

t = int(input())
for _ in range(t):
    l   = list(map(int,input().split()))
    print(sum(l)//2)
