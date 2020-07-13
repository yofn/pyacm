#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/706/A

from math import sqrt

dist    = lambda p1,p2: sqrt(sum([(p1[i]-p2[i])**2 for i in range(len(p1))]))  #n-d point
a,b     = list(map(int,input().split()))
taxil   = [list(map(int,input().split())) for _ in range(int(input()))]
print(min([dist([a,b],t[:2])/t[2] for t in taxil]))

