#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1358/B

t = int(input())
for _ in range(t):
    n,m = list(map(int,input().split()))
    print((n*m+1)//2)
