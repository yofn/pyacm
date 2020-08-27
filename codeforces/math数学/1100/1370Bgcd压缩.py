#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1370/B
# 用偶数?

def f(l):
    n  = len(l)
    ol = [(l[i],i+1) for i in range(n) if l[i]%2>0 ]
    ol.sort(key = lambda t:t[0])
    el = [(l[i],i+1) for i in range(n) if l[i]%2==0]
    en = len(el)
    on = n-en
    rl  = [[el[i][1],el[en-1-i][1]] for i in range(en//2)]
    rl += [[ol[i][1],ol[on-1-i][1]] for i in range(on//2)]
    return rl[:n//2-1]

q = int(input())
for i in range(q):
    _ = input()
    l = list(map(int,input().split()))
    [print(*r) for r in f(l)]
