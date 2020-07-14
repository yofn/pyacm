#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/40/A

from math import sqrt
x,y = list(map(int,input().split())) #1000
r   = sqrt(x*x+y*y)
print('black' if ((int(r)%2>0) ^ (x*y>0)) or r==int(r) else 'white')

