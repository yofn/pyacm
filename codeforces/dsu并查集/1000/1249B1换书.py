#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/1249/B1
#有点并查集的意思,但还不是?

def al(pl,n):
    pl  = [0]+pl
    rl  = [0]*(n+1)
    for i in range(1,n+1):
        if  rl[i] > 0:
            continue
        p       = i
        uset    = [i]
        while pl[p]!=i:
            p   = pl[p]
            uset.append(p)  #add new node
        for j in uset:
            rl[j] = len(uset)
    return rl[1:]

q = int(input())        #200
for _ in range(q):
    n  = int(input())   #200
    pl = list(map(int,input().split()))
    print(*al(pl,n))

