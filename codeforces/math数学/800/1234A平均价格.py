#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1234/A

t = int(input())
for _ in range(t):
    n   = int(input())
    l   = list(map(int,input().split()))
    print((sum(l)+n-1)//n)
