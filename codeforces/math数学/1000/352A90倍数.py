#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/352/A

def f(l):
    n  = len(l)
    n0 = sum([i==0 for i in l])
    if n0==0:
        return -1
    n5 = n-n0
    n5 = (n5//9)*9
    if n5==0:
        return 0
    return ''.join(['5']*n5+['0']*n0)

_ = input()
l = list(map(int,input().split()))
print(f(l))
