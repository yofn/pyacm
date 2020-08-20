#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1020/A

def f(l):
    dist = lambda a,b:a-b if a>b else b-a
    global a,b
    ta,fa,tb,fb = l
    ht = dist(ta,tb)
    if (fa>=a and fa<=b) or (fb>=a and fb<=b) or ht==0:
        return ht + dist(fa,fb)
    return ht + min(dist(fa,a)+dist(fb,a),dist(fa,b)+dist(fb,b))

n,h,a,b,k   = list(map(int,input().split()))
[print(f(list(map(int,input().split())))) for _ in range(k)]
