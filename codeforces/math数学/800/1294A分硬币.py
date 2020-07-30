#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1294/A

t = int(input())
for _ in range(t):
    l   = list(map(int,input().split()))
    s   = sum(l)
    m   = max(l[:-1])
    print('YES' if s%3==0 and s//3>=m else 'NO')
