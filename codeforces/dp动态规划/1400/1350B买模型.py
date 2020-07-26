#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/1350/B
#https://codeforces.com/blog/entry/77284

t   = int(input())
for _ in range(t):
    n   = int(input())
    sl  = [0] + list(map(int,input().split()))
    fl  = [1]*(n+1)
    for i in range(2,n+1):
        if fl[i]<2 and sl[i]>sl[1]:
            fl[i] = 2
        for j in range(2,(n//i)+1):
            mi  = i*j
            if fl[mi] <= fl[i] and sl[mi] > sl[i]:
                fl[mi] = fl[i]+1
    print(max(fl))
