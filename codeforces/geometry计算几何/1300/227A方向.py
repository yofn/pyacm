#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/227/A
#1. 从两点坐标求线段表示,进而判断半平面
#2. 判断一个点在直线的哪边
#3. 用角度..好像更符合左右(右=角度变小,左=角度变大)
#4. 向量叉乘(vector cross product)
#https://codeforces.com/blog/entry/5378?locale=en&f0a28=1

crossp = lambda a,b:a[0]*b[1]-b[0]*a[1]
ray    = lambda a,b:[b[0]-a[0],b[1]-a[1]]
a   = list(map(int,input().split())) #1e9
b   = list(map(int,input().split())) #1e9
c   = list(map(int,input().split())) #1e9
v   = crossp(ray(a,b),ray(a,c))
if   v==0:
    print("TOWARDS")
elif v>0:
    print("LEFT")
else:
    print("RIGHT")
