#!/usr/bin/env python3
#https://codeforces.com/contest/1399/problem/F
#不能固定一个,必须两边都能动!
#如何排序?

def f(ll):
    n   = len(ll)
    ll.sort(key=lambda s:(s[1],-s[0]))
    cl  = [1]*n     #max nubmer of taowa, inclding itself
    for i in range(n):
        l = ll[i][0]
        for j in range(i):
            if ll[j][0]>=l:
                cl[i] = max(cl[i],cl[j]+1)
                #cl[i] += 1
    dp  = {}
    print(ll)
    print(cl)
    for i in range(n):  #fix left
        l,r = ll[i]
        if r not in dp:
            dp[r]   = 0
        if l-1 not in dp:
            dp[l-1] = 0
        dp[r] = max(dp[r],dp[l-1]+cl[i])
        print(dp)
    return max(dp.values())

T = int(input())
for i in range(T):
    n  =  int(input())
    ll = [list(map(int,input().split())) for _ in range(n)]
    print(f(ll))
