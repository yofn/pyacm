#!/usr/bin/env python3

'''
https://codeforces.com/group/H9K9zY8tcT/contest/297258/problem/J
log it.. 分布
只要runner-up的value=0,且超过一个!, 即[0,2/+,..]即可...下一步就是
print(d[:p+1])
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
    d     = makeD(l)
    n     = len(d)
    p     = n-1     # points to the REAL runner-up group
    rr    = 0       # count of ROUND
    while True:
        r     = d[p]    # runner-up
        if r[0]==0 and r[1]>1:
            return rr
        # decide step: FAST-mode or SLOW-mode(1); FAST=SINGLE; SLOW=SPLIT;  (split,merge,update, in what order?)
        fast  = r[0]>(r[2]-1)       #FAST if r[0] would be >=0
        ss    = r[2] if fast else 1 #ss = STEP
        rr   += ss
        # 1. update other groups
        for i in range(p):
            d[i][0] -= ss
        # 2. update RUNNER-up in FAST-mode; split if in SLOW-mode!
        if fast:
            r[0] -= ss-1
        else:
            ng    = [r[0]-1,r[1]//2,r[2]-1] 
            r[1] -= ng[1]
            r[2] -= 1
        # 3. Merge
        if p>0 and r[0] == d[p-1][0]:
            p       -= 1     # MERGE two groups as new runner-up group
            d[p][1] += r[1]
            d[p][2]  = log2i(d[p][1])+1
        # 4. append new runner-up if in SLOW mode!
        if (not fast) and ng[1]>0:
            if p<n-1:
                d[p+1] = ng
            else:
                d.append(ng)
                n += 1
            p += 1 

_  = input()
l  = list(map(int,input().split()))
print(f(l))
