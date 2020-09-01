#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/174/A

def f(l1,al):
    n,b = l1
    c   = (sum(al) + b)/n
    if max(al)>c:
        return [-1]
    return [c-a for a in al]

l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
[print(r) for r in f(l1,l2)]
