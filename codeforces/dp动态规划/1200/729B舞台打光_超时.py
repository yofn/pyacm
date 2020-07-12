#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/729/B
#四个方向分别做,应该会容易些
#python nested list 不太适合做二维数组用, cf不支持numpy; 所以还是回到一维数组吧

n,m = list(map(int,input().split()))
gd  = [int(i) for row in [input().split() for _ in range(n)] for i in row]
rc  = lambda r,c: r*m+c #r=[0,n),c=[0,m)
cnt = 0

ol  = [gd[rc(0,j)] for j in range(m)]
for i in range(1,n):
    cnt += sum([ol[j]*(1-gd[rc(i,j)]) for j in range(m)])
    ol   =    [max(ol[j],gd[rc(i,j)]) for j in range(m)]

ol  = [gd[rc(n-1,j)] for j in range(m)]
for i in range(n-1,-1,-1):
    cnt += sum([ol[j]*(1-gd[rc(i,j)]) for j in range(m)])
    ol   =    [max(ol[j],gd[rc(i,j)]) for j in range(m)]

ol  = [gd[rc(i,0)] for i in range(n)]
for j in range(1,m):
    cnt += sum([ol[i]*(1-gd[rc(i,j)]) for i in range(n)])
    ol   =    [max(ol[i],gd[rc(i,j)]) for i in range(n)]

ol  = [gd[rc(i,m-1)] for i in range(n)]
for j in range(m-1,-1,-1):
    cnt += sum([ol[i]*(1-gd[rc(i,j)]) for i in range(n)])
    ol   =    [max(ol[i],gd[rc(i,j)]) for i in range(n)]
print(cnt)

