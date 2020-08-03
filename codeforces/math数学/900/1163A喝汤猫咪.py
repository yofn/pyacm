#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1163/A
# n,m 最多几组..
# 1. 看还剩多少人..组数<=人数
# 2. 看能截断几次..截断2次=2组

def f(l):
    n,m = l
    if m<2:
        return 1
    return min(m,n-m)

l  = list(map(int,input().split()))
print(f(l))

