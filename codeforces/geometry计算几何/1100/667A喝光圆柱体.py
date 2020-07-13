#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/667/A
#1L=1立方分米

from math import pi

def empty(r,h,v,e):
    ve = v/(pi*r*r)
    return ['NO'] if ve<=e else ['YES',h/(ve-e)]

d,h,v,e = list(map(int,input().split()))
[print(r) for r in empty(d/2,h,v,e)]

