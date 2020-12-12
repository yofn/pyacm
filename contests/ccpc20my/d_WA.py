#!/usr/bin/env python3

def f(l):
    l.sort()
    return l[0]+l[1]+1

t = int(input())
for i in range(t):
    _   = input()
    l   = list(map(int,input().split()))
    print('Case #%d: %s'%((i+1), f(l)))

