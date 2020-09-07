#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/732/C
#[b,d,s]=#d + [1,1,1] or [1 0 1] or [1 2 1] or [0,0,1] or [0,1,1] or [1,0,0] or [1,1,0]
# 一样, b(+1/-1), d(+1/-1), s(+1,-1) 这么些可能性..
# 参考天数 = max 或 max-1

def f(l):
    mx = max(l)
    dl = [mx-i for i in l]
    dl.sort()       #0,x,x or 0,0,x or 0,0,0
    if dl[1]>0:     #0,x1,x2 case: ref is mx-1, so x1-1,x2-1
        return dl[1]+dl[2]-2    
    if dl[2]==0:    #0,0,0 case
        return 0
    return dl[2]-1  #0,0,x case: we can +1 to x

l = list(map(int,input().split()))
print(f(l))

