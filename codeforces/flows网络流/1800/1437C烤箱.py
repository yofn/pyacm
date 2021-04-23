#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1437/C

MAXT = 400
def f(l):
    n   = len(l)
    l.sort()
    dp  = [0]*(MAXT+1)
    for i in range(1,n+1):
        t      = l[i-1]
        dpold  = [i for i in dp]
        dp[i]  = dpold[i-1]+abs(i-t)
        for j in range(i+1,MAXT+1):
            dp[j]=min(dp[j-1],dpold[j-1]+abs(t-j))
        #print(dp[:10])
    return min(dp[n:])

q = int(input())
for _ in range(q):
    n   = int(input())
    l   = list(map(int,input().split()))
    print(f(l))
