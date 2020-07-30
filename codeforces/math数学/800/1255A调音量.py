#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1255/A

t = int(input())
l = [0,1,1,2,2]
for _ in range(t):
    a,b = list(map(int,input().split()))
    d   = a-b if a>b else b-a
    print(d//5+l[d%5])
