#!/usr/bin/env python3
#ccpc20qhd-fl(female-l)

def f(nl,ml):
    ml.sort(key=lambda i:i[1],reverse=True)
    m   = len(ml)
    uzl = [False]*m
    e   = 0
    for ai,bi in nl:
        mi = 0
        while e<ai and mi<m:
            if (not uzl[mi]) and (e>=ml[mi][0]):
                e  += ml[mi][1]
                uzl[mi] = True
                mi  = 0  #new score, new chance!
            else:
                mi += 1
        if e<ai:
            return -1
        e+=bi
    return len(nl) + sum(uzl)

t = int(input())
for i in range(t):
    n,m =  list(map(int,input().split()))
    nl  = [list(map(int,input().split())) for _ in range(n)]
    ml  = [list(map(int,input().split())) for _ in range(m)]
    print('Case #%d: %d'%((i+1), f(nl,ml)))

