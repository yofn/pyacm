#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/190/A
# 最少情况 = 如果孩子够多,每个大人都带孩子,即孩子数=票价; 如果孩子较少则每个大人最多只带一个孩子,即大人数=票价
# 最多情况 = 一个大人带了所有孩子, 其他人都没带 

def f(l):
    n,m = l
    if n==0:
        return ['Impossible'] if m>0 else [0,0]
    return [max(m,n), n+m-1 if m>0 else n+m]

l = list(map(int,input().split()))
print(*f(l))
