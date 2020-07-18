#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/1292/A
#由于toggle,dsu实现的话还要支持split?
#每次q必须低于O(n)! 每次查询都走一遍是不行的!
#分成两个情况:
# 1. unblock->block的情况: 判断一下block的位置和周围位置状态
# 2. unblock action: 将unblock块和三个邻居分别union, 然后再看(1,1)和(2,n)是否联通.
# 但是问题是要为case 2维护dsu; 所以case1也要用dsu来做才行....
# 1. block action, 应如何维护dsu??
# 还有一个问题是2xn是用两个list,一个大list还是如何表示? 还是两个dsu?
# 还是太复杂了,感觉有更简单的方法,可能被dsu带歪了..
# NOTE: no dsu used!
# https://codeforces.com/blog/entry/73051
# https://www.youtube.com/watch?v=mhrvlor1qH0
# https://codeforces.com/contest/1292/submission/69151636
# 注意对bad的定义, 我们的定义是走不到的地方从左边走$完全$走不到的列! 如果能走到一行,也算good,不算bad!
# https://codeforces.com/contest/1292/submission/69151636 实现更简洁,建议参考! NOTE


def okay(t):
    global gd,bl,bc
    r,c = t[0]-1,t[1]-1
    rr  = 1 if r==0 else 0
    if gd[r][c]:        # cell unblocked -> blocked
        if (not bl[c]) and False in gd[rr][c-1:c+1]:    #will block this!
            bl[c]    = True    #need some drawing to illustrate
            bc      += 1       #note definition of bad column!
        if c<n-1 and (not bl[c+1]) and (not gd[rr][c+1]):
            bl[c+1]  = True
            bc      += 1
    else:   #cell blocked -> unblocked, may affect c and c+1
        if c>0   and bl[c]   and gd[r][c-1]:    #will unlock c
            bl[c]    = False
            bc      -= 1
        if c<n-1 and bl[c+1] and gd[r][c+1]:    #will unlock c+1
            bl[c+1]  = False
            bc      -= 1
    gd[r][c] = not gd[r][c] #DON't forget to flip!
    return bc==0

n,q = list(map(int,input().split()))    #1e5,1e5
tl  = [list(map(int,input().split())) for _ in range(q)]
gd  = [[True]*n, [True]*n]
bl  = [False]*n #bad column list
bc  = 0         #bad column count
[print('Yes' if okay(t) else 'No') for t in tl]

