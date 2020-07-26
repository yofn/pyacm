#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1360/A
# 较小的x2.再和长边max, 再**2

t = int(input())
for _ in range(t):
    a,b = list(map(int,input().split()))
    if a<b:
        a,b = b,a
    print(max(a,b<<1)**2)
