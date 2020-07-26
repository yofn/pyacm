#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1348/A
# 最大的太大了,肯定要挑最小的

t = int(input())
for _ in range(t):
    n = int(input())
    print(2**((n//2)+1)-2)
