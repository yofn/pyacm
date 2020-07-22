#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/416/B

m,n =  list(map(int,input().split()))
t   = [[0]*n] + [list(map(int,input().split())) for _ in range(m)]
for i in range(1,m+1):
    t[i][0] += t[i-1][0]
    for j in range(1,n):
        t[i][j] += max(t[i-1][j],t[i][j-1]) 
print(*[t[i][-1] for i in range(1,m+1)])
