#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/433/B
#这好像也是前缀和,算DP吗?

n   = int(input())

v   = list(map(int,input().split()))
s   = sorted(v)
vv  = [0]
ss  = [0]
[vv.append(vv[i]+v[i]) for i in range(n)]
[ss.append(ss[i]+s[i]) for i in range(n)]

m  = int(input())
[print(vv[r]-vv[l-1] if t==1 else ss[r]-ss[l-1]) for t,l,r in [map(int,input().split()) for i in range(m)]]
