#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1206/B
# 保持了状态,还谈不上DP?

_   = input()
l   = list(map(int,input().split()))
c   = 0
non = 0
noz = 0
for i in l:
    if   i>0:
        c   += i-1
    elif i<0:
        c   += -i-1
        non += 1  #count negative
    else:
        c   += 1  #zero!
        noz += 1  #count zero
if non%2==1 and noz==0:
    c += 2  #-1 -> 1
print(c)
