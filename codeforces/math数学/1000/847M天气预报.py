#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/847/M

def f(l):
    n  = len(l)
    dl = [l[i+1]-l[i] for i in range(n-1)]
    dl.sort()
    return l[-1] if dl[0]!=dl[-1] else l[-1]+dl[0]

_ = input()
l = list(map(int,input().split()))
print(f(l))
