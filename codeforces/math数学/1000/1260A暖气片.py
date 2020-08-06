#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1260/A
# 完全不用看描述,直接看Example和Note就行..

t = int(input())
for _ in range(t):
    c,s = list(map(int,input().split()))
    cc  = (c-s%c)*(s//c)**2 + (s%c)*(s//c+1)**2
    print(cc)
