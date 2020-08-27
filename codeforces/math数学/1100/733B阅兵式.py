#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/733/B
# 注意题意: 只能换一列!

def f(l):
    ab = lambda x: x if x>0 else -x
    k  = len(l)
    dl = [c[0]-c[1] for c in l]
    ss = sum(dl)
    mb = ab(ss)
    mi = 0
    for i in range(k):
        b = ab(ss-(dl[i]<<1))
        if b>mb:
            mi = i+1
            mb = b
    return mi

k = int(input())
l = [list(map(int,input().split())) for _ in range(k)] 
print(f(l))
