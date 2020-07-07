#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/368/B
# 必须数据结构?..辅助型数组即可..

n,m =   list(map(int,input().split()))
an  =   list(map(int,input().split()))
mxx =   max(an)
saw =   [False]*(mxx+1)
dis =   [0]*(n+1)
for i in range(n-1,-1,-1):
    x       = an[i]
    dis[i]  = dis[i+1] if saw[x] else dis[i+1]+1
    saw[x]  = True

[print(dis[int(input())-1]) for i in range(m)]
