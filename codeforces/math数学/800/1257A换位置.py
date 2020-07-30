#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/664/A

t = int(input())
for _ in range(t):
    n,x,a,b = list(map(int,input().split()))
    d   = a-b if a>b else b-a
    print(min(n-1,d+x))
