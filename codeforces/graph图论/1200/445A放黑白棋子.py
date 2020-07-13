#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/445/A
#构建? BW.. WB..?

n,m = list(map(int,input().split()))
gd  = [list(input()) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if gd[i][j]=='.':
            gd[i][j]='B' if (i+j)%2==0 else 'W'
[print(''.join(l)) for l in gd]
