#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/72/G
# 该题目cf不支持python~~因此不放入周赛题库..

n = int(input())
if n<2:
    print(1)
else:
    l = [1,1] + [0]*(n-1)
    for i in range(2,n+1):
        l[i] = l[i-1] + l[i-2]
    print(l[-1])

