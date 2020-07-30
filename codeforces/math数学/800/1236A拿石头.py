#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1236/A
# 三堆石头,只能(1,2,0)或(0,1,2)的拿,最多能拿多少?
# 优先(0,1,2),然后(1,2,0)

t = int(input())
for _ in range(t):
    a,b,c   = list(map(int,input().split()))
    y       = min(b,c//2)
    x       = min(a,(b-y)//2)
    print((x+y)*3)
