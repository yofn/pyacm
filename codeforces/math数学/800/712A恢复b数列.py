#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/712/A

n   = int(input())
al  = list(map(int,input().split())) + [0]
print(*[al[i]+al[i+1] for i in range(n)])
