#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/706/B
# 一定注意HOLD的目标

def bs(k,li):
    l, r    = 0, len(li)-1
    if li[l] >  k:  return 0
    if li[r] <= k:  return len(li)
    while True:     #HOLD: li[l]<=k<li[r] VERY important!
        if  r-l<2:  return r
        m   = l + ((r-l) >> 1)  #safer; NOTE: () for right order
        if  li[m]>k:
            r = m
        else:
            l = m

n   =   int(input())
xn  =   sorted(list(map(int,input().split())))
q   =   int(input())
[print(bs(int(input()),xn)) for i in range(q)]

