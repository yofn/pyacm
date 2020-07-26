#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/1380/C

t   = int(input())
for _ in range(t):
    n,x = list(map(int,input().split()))
    l   = list(map(int,input().split()))
    l.sort(reverse=True)
    c   = 0
    ii  = 0
    for i in range(n):
        if (i-ii+1)*l[i] >= x:
            c += 1
            ii = i+1
    print(c)
