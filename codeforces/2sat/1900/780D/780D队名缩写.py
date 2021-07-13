#!/usr/bin/env python3

def f(ll):
    d = {}
    for l in ll:
        o1 = l[0][:3]
        o2 = l[0][:2]+l[1][0]
        if o1 not in d: d[o1]=[]
        d[o1].append(o2)
    return d

ll = [input().split() for _ in range(int(input()))]
print(f(ll))
