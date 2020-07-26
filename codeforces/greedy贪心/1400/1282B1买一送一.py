#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/1282/B1
#B2=1600难度

t   = int(input())
for _ in range(t):
    n,p,k   = list(map(int,input().split()))    #2e5,2e9,k=2
    al      = list(map(int,input().split()))    #1e4
    al.sort()
    al      = [0,0] + al + [0]
    for i in range(2,n+3):
        al[i] += al[i-2]
        if al[i]>p:
            break
    print(i-2)

