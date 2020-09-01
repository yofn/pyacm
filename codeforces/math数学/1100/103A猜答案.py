#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/103/A

n = int(input())
l = list(map(int,input().split()))
s = sum([l[i]*(i+1)-i for i in range(n)])
print(s)
