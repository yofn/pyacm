#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1359/B

_n  =   int(input())
for i in range(_n):
    n,m,x,y = list(map(int,input().split()))
    s2      = max(x+x-y,0)  #how much 1x2 saves? min=0
    tc      = 0
    for j in range(n):
        p   = '*'
        for c in input():
            if   c == '*':  #*
                p   = c
            elif p == '.':  #..
                tc += x-s2
                p   = '*'   #NOTE: to deal with ... case!
            else:           #.
                tc += x
                p   = c
    print(tc)
