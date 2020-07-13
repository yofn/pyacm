#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/127/A

from math import sqrt
dist    = lambda p1,p2: sqrt(sum([(p1[i]-p2[i])**2 for i in range(len(p1))]))  #n-d point
n,k     = list(map(int,input().split()))
ps      = [list(map(int,input().split())) for _ in range(n)]
print(0.02*k*sum([dist(ps[i],ps[i+1]) for i in range(n-1)]))

