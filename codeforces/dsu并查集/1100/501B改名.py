#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/501/B

def changes(ul):
    ol  = [u[0] for u in ul]
    nl  = [u[1] for u in ul]
    rl  = []
    for i in range(len(ul)):
        if ol[i] is None:
            continue
        j   = i
        while nl[j] in ol:
            j       = ol.index(nl[j])
            ol[j]   = None
        rl.append('%s %s'%(ol[i],nl[j]))
    return [len(rl)] + rl

ul  = [input().split() for _ in range(int(input()))] #1000;20
[print(r) for r in changes(ul)]

