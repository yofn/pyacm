#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1283/A

t = int(input())
for _ in range(t):
    h,m = list(map(int,input().split()))
    print(1440-h*60-m)
