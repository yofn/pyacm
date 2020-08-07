#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/143/A
# 9^4, 所以用暴力搜索
# 如果写成矩阵会好点?

def f(ll):
    for g0 in range(1,10):
        g1 = ll[0][0]-g0    #r1
        if g1<1 or g1>9 or g1==g0:
            continue
        g2 = ll[1][0]-g0    #c1
        if g2<1 or g2>9 or g2==g0:
            continue
        g3 = ll[2][0]-g0    #d1
        if g3<1 or g3>9 or g3==g0:
            continue
        if g1==g2 or g2==g3 or g1==g3:
            continue
        if g2+g3 != ll[0][1]:   #r2
            continue
        if g1+g3 != ll[1][1]:   #c2
            continue
        if g1+g2 != ll[2][1]:   #d3
            continue
        return [[g0,g1],[g2,g3]]
    return [[-1]]

ll = [list(map(int,input().split())) for _ in range(3)]
[print(*r) for r in f(ll)]
