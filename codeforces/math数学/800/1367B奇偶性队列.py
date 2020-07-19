#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1367/B

n = int(input())
for _ in range(n):
    m  = int(input())
    l  = list(map(int,input().split()))
    wc = [0,0]
    for i in range(m):
        if l[i]%2 != i%2:
            wc[i%2] += 1
    print(-1 if wc[0]!=wc[1] else wc[0])
