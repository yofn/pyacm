#!/usr/bin/env python3

# 2020暑期排位4C

# input phase
l = input()
n,_k,c = [int(s) for s in l.split(' ')]
dl,xl = [0]*n,[0]*n
for i in range(n):
    l = input()
    dl[i],xl[i]=[int(s) for s in l.split(' ')]

# process phase (时间复杂度是多少?)
ccost = [0]*(c+1)
for i in range(n):
    pcost = [(dl[i]-1)//(j*_k+_k) * xl[i] for j in range(c+1)]
    ncost = [None]*(c+1)
    for j in range(c+1):
        for k in range(c+1-j):
            tmp = ccost[j]+pcost[k]
            if ncost[j+k] is None or ncost[j+k]>tmp:
                ncost[j+k] = tmp
    ccost = ncost 
print(ccost[c])

