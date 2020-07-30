#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1075/A

n  = int(input())
xy = list(map(int,input().split()))
print('White' if sum(xy)<=(n+1) else 'Black')
