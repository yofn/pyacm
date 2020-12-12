#!/usr/bin/python3

def f(l,m):
    nl = []
    for v in l:
        nl.append((v,    +1))   # true point!
        nl.append((v+m/2,-1))   #ghost point!
        if (v<<1)<=m:
            nl.append((v+m,+1)) # copy point!
    nl.sort()
    cl = 0
    n  = len(l)
    s  = n*(n-1)*(n-2)//6
    for v,t in nl:
        cl += t
        if t==-1:
            s -= cl*(cl-1)//2
    return s

n,m  = list(map(int,input().split()))
l    = list(map(int,input().split()))
print(f(l,m))
