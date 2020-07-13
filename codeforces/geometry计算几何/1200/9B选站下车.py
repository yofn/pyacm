#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/9/B
#如果有多个一样的,选择离学校更近的,实际上不用计算距离,永远选最后的

from math import sqrt

n,vb,vs = list(map(int,input().split()))
xl      = list(map(int,input().split()))
xii,yii = list(map(int,input().split()))
time    = lambda rsb,xs,x,y: rsb*xs + sqrt((x-xs)*(x-xs)+y*y)
times   = [time(vs/vb,xl[i],xii,yii) for i in range(n-1,0,-1)] #reverse to prefer later stop
print(n-times.index(min(times)))
