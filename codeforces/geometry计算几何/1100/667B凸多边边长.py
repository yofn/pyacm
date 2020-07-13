#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/667/B
#凸多边形的边长条件? 广义三角形条件: 最长边<其他边之和..

_   = int(input())
l   = list(map(int,input().split()))
print( (max(l)<<1)+1-sum(l) )
