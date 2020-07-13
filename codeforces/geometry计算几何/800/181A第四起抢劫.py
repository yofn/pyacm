#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/900/A

n,m = list(map(int,input().split()))
gd  = [list(input()) for _ in range(n)]
il  = []
jl  = []
for i in range(n):
    for j in range(m):
        if gd[i][j]=='*':
            if i in il:
                il.remove(i)
            else:
                il.append(i)
            if j in jl:
                jl.remove(j)
            else:
                jl.append(j)
print(il[0]+1,jl[0]+1)
