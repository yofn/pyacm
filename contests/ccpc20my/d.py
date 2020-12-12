#!/usr/bin/env python3

def f(l):
    l.sort()
    n = len(l)
    s = l[0]
    for i in range(1,n):
        x  = l[i]*i-s   # bonus needed to align l[0]-l[i-1] to l[i]
        if x>l[i]:      # not enough!
            return 1 + s//(i-1)
        s += l[i]
    return 1 + s//(n-1)

t = int(input())
for i in range(t):
    _   = input()
    l   = list(map(int,input().split()))
    print('Case #%d: %s'%((i+1), f(l)))

