#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1345/A
# 规律? 还是面积和周长的公式?

t = int(input())
for _ in range(t):
    n,m = list(map(int,input().split()))
    print('YES' if (n*m)<=(n+m) else 'NO')
