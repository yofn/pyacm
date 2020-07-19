#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1385/A

xyzl = [list(map(int,input().split())) for _ in range(int(input()))]
for xyz in xyzl:
    x,y,z = xyz
    m   = max(xyz)
    abc = [min(xyz)]*3
    i   = xyz.index(m)
    if  m not in xyz[i+1:]:
        print('NO')
        continue
    print('YES')
    j   = i+1 + xyz[i+1:].index(m)
    abc[i+j-1]=m
    print(*abc)
