#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/1320/A
#直观的DP好像需要O(N**2), 因为n=2e5, 会超时..
#用dsu或tree?
#性质: 只能是一条线,不可能像树一样分叉
#技巧: 全部-i就得到分组
#并非DP,但外表很像

n   = int(input())
bl  = list(map(int,input().split()))
nl  = [(bl[i],bl[i]-i) for i in range(n)]
nl.sort(key = lambda b:b[1])
p   = nl[0]
s   = p[0]
mx  = s
for i in range(1,n):
    if nl[i][1]==p[1]:
        s += nl[i][0]
    else:
        if s>mx:
            mx = s
        s  = nl[i][0]
    p = nl[i]
print(max(s,mx))
