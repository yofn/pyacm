#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/620/A

p1  = list(map(int,input().split()))
p2  = list(map(int,input().split()))
dx  = p1[0]-p2[0] if p1[0]>p2[0] else p2[0]-p1[0]
dy  = p1[1]-p2[1] if p1[1]>p2[1] else p2[1]-p1[1]
print(max(dx,dy))
