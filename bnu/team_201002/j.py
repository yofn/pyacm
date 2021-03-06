#!/usr/bin/env python3

'''
https://codeforces.com/group/H9K9zY8tcT/contest/297258/problem/J
log it.. 分布
只要runner-up的value=0,且超过一个!, 即[0,2/+,..]即可...下一步就是
print(d[:p+1])
gap的时候会超时!! 即使只有一个..
还需要考虑一种特殊情况,就是合并成一个的时候!!! (<--这是题解中2的一个特例)
'''

def log2i(n):
    i = 0
    while n>1:
        n  = n>>1
        i += 1
    return i

def makeD(l):
    l = sorted([l[0]-i for i in l[1:]],reverse=True)
    n = len(l)
    p = 0
    d = []
    for i in range(1,n+1):
        if i==n or l[i]!=l[i-1]:
            d.append([l[i-1],i-p])  #(val,#val) 
            p = i
    return [[g[0],g[1],log2i(g[1])+1] for g in d]

def f(l):
    inf   = 9e999
    d     = makeD(l)
    n     = len(d)
    p     = n-1     # points to the REAL runner-up group
    rr    = 0       # count of ROUND
    while True:
        r     = d[p]    # runner-up; r[0]=dist2J, r[1]=GroupSize, r[2]=@nRound
        if r[0]==0 and r[1]>1:
            return rr
        s2j   = r[2]*(r[0]//(r[2]-1)) if r[2]>1 else inf
        s2m   = (d[p-1][0]-r[0])*r[2] if p>0 else inf
        case1 = (s2m<=s2j)                          # safely MERGE 2nd and 3rd places (aka p,p-1)
        case2 = (not case1) and (s2j > 0)           # safely MOVE  2nd without merge happens
        case3 = (not case1) and (not case2)         # baby stepping, which involves SPLITTING
        ss    = s2m if case1 else (s2j if case2 else 1)
        rr   += ss
        # COMMON to all cases!
        for i in range(p):
            d[i][0] -= ss
        if case1:
            p       -= 1     # MERGE two groups as new runner-up group
            d[p][1] += r[1]
            d[p][2]  = log2i(d[p][1])+1
        if case2:
            r[0]    -= ss-(ss//r[2])
        if case3:
            ng    = [r[0]-1,r[1]//2,r[2]-1] 
            r[1] -= ng[1]
            r[2] -= 1
            if p<n-1:
                d[p+1] = ng
            else:
                d.append(ng)
                n += 1
            p += 1 

_  = input()
l  = list(map(int,input().split()))
print(f(l))
