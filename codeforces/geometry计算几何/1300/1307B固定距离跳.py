#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/1307/B
#欧式距离..比预想的复杂些..
#三角形.多边形? 多边形条件? 1直接->2三角形->3四边形->..
#错误1=假设所有跳都小于x
#错误2=假设所有a只能用一次
#正确: 情况1; 情况2=求最大..然后一直用最大..

noh = lambda x,m: max(2,(x+m-1)//m) #2 is for m>x=1 case
t   = int(input())
for i in range(t):
    n,x = list(map(int,input().split())) 
    al  = list(map(int,input().split()))    #1e5
    print(1 if x in al else noh(x,max(al)))
