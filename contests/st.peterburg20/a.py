#!/usr/bin/python3

def f(l):
    ss = sum(l)+1
    dp = [True] + [False]*(ss-1)
    for v in l:
        for i in range(ss-1,v-1,-1): #KEY!
            dp[i] = dp[i] or dp[i-v]
    ct = sum(dp)
    return ct*(ss*2-ct+1)//2

_  = int(input())
l  = list(map(int,input().split()))
print(f(l))
