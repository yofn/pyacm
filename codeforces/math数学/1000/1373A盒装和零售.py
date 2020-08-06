#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1373/A

t = int(input())
for _ in range(t):
    a,b,c   = list(map(int,input().split()))
    print(-1 if a>=c else 1, b if c<a*b else -1)
