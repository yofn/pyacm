#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/1100/C

from math import sin, pi
n,r     = list(map(int,input().split())) #100
print(r*sin(pi/n)/(1-sin(pi/n)))

