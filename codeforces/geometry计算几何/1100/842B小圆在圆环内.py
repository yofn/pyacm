#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/842/B

from math import sqrt
dist    = lambda p: sqrt(sum([d*d for d in p]))
inCrust = lambda l,r,rl,rr: (l-r)>=rl and (l+r)<=rr
rr,d    = list(map(int,input().split())) #500
xyrl    = [list(map(int,input().split())) for _ in range(int(input()))]
print(sum([inCrust(dist(xyr[:2]),xyr[2],rr-d,rr) for xyr in xyrl]))

