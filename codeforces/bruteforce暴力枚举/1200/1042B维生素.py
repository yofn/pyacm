#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/1042/B
# 2^1000超标
# 用bitmask来完成覆盖! => 定制,不写通用的了..
# 能暴力就暴力吧!

n   = int(input())
di  = {'a':1,'b':2,'ab':3,'c':4,'ac':5,'bc':6,'abc':7}
cl  = [None]*8
for i in range(n):
    c,s = input().split()
    c   = int(c)
    s   = ''.join(sorted(s.lower()))
    ii  = di[s]
    if (cl[ii] is None) or (c<cl[ii]):
        cl[ii] = c
cl[0] = 0
mcost = sum([c for c in cl if c is not None]) 
fail  = True
for i in range(8):
    for j in range(8):
        for k in range(8):
            if (i|j|k != 7) or (None in [cl[i],cl[j],cl[k]]): 
                continue
            fail = False
            c    = cl[i]+cl[j]+cl[k]
            if c < mcost:
                mcost = c
print(-1 if fail else mcost)

