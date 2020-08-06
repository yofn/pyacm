#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1388/B
# 错误:没考虑0是对应0而不是0000

t = int(input())
for _ in range(t):
    n   = int(input())
    n8  = (n+3)//4
    n9  = n-n8
    print(''.join(['9']*n9+['8']*n8))
