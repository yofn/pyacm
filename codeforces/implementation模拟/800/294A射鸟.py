#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/294/A

n   =  int(input())
al  =  [0] + list(map(int,input().split())) + [0]
m   =  int(input())
xyl = [list(map(int,input().split())) for _ in range(m)]
for xy in xyl:
    x,y = xy
    al[x-1] += y-1
    al[x+1] += al[x]-y
    al[x]   = 0
[print(a) for a in al[1:-1]]
