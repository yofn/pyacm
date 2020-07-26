#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1353/A
# 最大的放一个,两边各一个0?

t = int(input())
for _ in range(t):
    n,m = list(map(int,input().split()))
    l   = [0,m,m<<1]
    print(l[n-1] if n<=2 else l[2])
