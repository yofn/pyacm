#!/usr/bin/python3
'''
case 7: 相等情况
'''

def f(l,m):
    nl = []
    for v in l:
        nl.append((v,1))            # true point!
        if (v<<1)<=m:
            nl.append((v+m/2,-1))   #ghost point!
    nl.sort(key=lambda t:(t[0],t[1]))
    print(nl)
    cl = 0
    cr = len(l)
    s  = 0
    for v,t in nl:
        cl += t
        cr -= (t==1)
        if t==-1:
            print(cl,cr)
            s += cl*cr
    return s

n,m  = list(map(int,input().split()))
l    = list(map(int,input().split()))
print(f(l,m))
