#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/706/B

def bs(k,li):
    if k <  li[0]:  return 0
    if k >= li[-1]: return len(li)
    l, r    = 0, len(li)-1
    while True:
        if  r-l < 2: return r  #li[r]>k>li[l] is for sure!
        m   = l + ((r-l) >> 1) #safer; NOTE: () for right order
        if   li[m]<k:
            l = m   #make sure li[l]<k
        elif li[m]>k:
            r = m   #make sure li[r]>k
        else: #case of finding k exactly!
            while li[m]==k:
                m += 1  #NOTE TLE?
            return m

n   =   int(input())
xn  =   sorted(list(map(int,input().split())))
q   =   int(input())
[print(bs(int(input()),xn)) for i in range(q)]

