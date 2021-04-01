#!/usr/bin/env python3
#https://codeforces.com/contest/1399/problem/F
#不能固定一个,必须两边都能动!
#如何排序?

import sys
sys.setrecursionlimit(900000)

dp  = {}
csl = []    #csl[r]=[l1,l2,..]

def flr(l,r):
    global dp
    global csl
    if l in dp and r in dp[l]: return dp[l][r]
    if l not in dp:
        dp[l] = {}
    t   = flr(l,r-1)
    for li in cls[r]:    #[l,li-1] + [li,r]
        t = max(t,flr(l,li-1)+flr(li,r))
    dp[l][r]  = t
    return t

def f(sl):
    global  dp
    global  csl
    dp  = {}
    tl  = list(set([s[0] for s in sl] + [s[1] for s in sl]))
    tl.sort()
    cd  = {}
    for i in range(len(tl)):
        cd[tl[i]] = i
    csl = [[] for i in range(len(tl))]
    for s0,s1 in sl:
        csl[cd[s1]].append(cd[s0])
    return flr(0,len(tl))

T = int(input())
for i in range(T):
    n  =  int(input())
    ll = [list(map(int,input().split())) for _ in range(n)]
    print(f(ll))
