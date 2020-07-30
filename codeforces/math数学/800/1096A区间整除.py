#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1096/A

t = int(input())
for _ in range(t):
    l,r = list(map(int,input().split()))
    print(r//2,(r//2)<<1)
