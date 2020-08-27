#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1189/B

def f(l):
    l.sort(reverse=True)
    if l[0]>=(l[1]+l[2]):
        return ['NO']
    n  = len(l)
    el = l[0:n:2] 
    ol = l[1:n:2]
    ol.reverse()
    return ['YES',' '.join(map(str,el+ol))]

_ = input()
l = list(map(int,input().split()))
[print(r) for r in f(l)]
