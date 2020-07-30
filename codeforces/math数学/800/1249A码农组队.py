#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1249/A

t = int(input())
for _ in range(t):
    n   = int(input())
    al  = list(map(int,input().split()))
    al.sort()
    dl  = [al[i]-al[i-1] for i in range(1,n)]
    print(2 if 1 in dl else 1)
