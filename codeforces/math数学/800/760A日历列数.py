#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/760/A

m,d = list(map(int,input().split()))
l   = [None] + [31,28] + [31,30]*2 + [31,31] + [30,31]*2
print((l[m]+d+5)//7)
