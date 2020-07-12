#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/1029/B

n   = int(input())
al  = list(map(int,input().split()))
cnt = 1
mxc = 0
for i in range(n-1):
    if al[i+1]-al[i] <= al[i]:
        cnt += 1
    else:
        if cnt>mxc:
            mxc = cnt
        cnt  = 1
print(max(mxc,cnt))
