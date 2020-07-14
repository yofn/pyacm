#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/820/B
#用圆来帮助多边形可视化?
#..O(n**2)被排除!

n,a = list(map(int,input().split())) #1e5; 180
sa  = 360/n
v2  = 1
v1  = 2
vd  = max(1,int(a*n/180+0.5))   #round
v3  = min(n,v1+vd)      #may not allowed
print(v1,v2,v3)

