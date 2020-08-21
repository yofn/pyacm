#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/114/A
# 快速幂 (实际用不到) 实现的过于复杂了..

def f(k,l):
    pl = [k]
    while l>pl[-1]:
        pl.append(pl[-1]**2)
    if pl[-1]%l > 0 or k>l:
        return ['NO']
    t = pl[-1]//l
    i = len(pl)-1
    p = 2**i
    while True:
        if t==1:
            return ['YES',p-1]
        if i<1:
            return ['NO']
        i-= 1
        if t<pl[i]:
            continue
        if t%pl[i] > 0:
            return ['NO']
        t = t//pl[i]
        p = p-2**i

k = int(input())
l = int(input())
[print(r) for r in f(k,l)]

