#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/967/A

def f(l1,l2):
    n,a,b = l1
    s = sum(l2)
    l = l2[1:]
    l.sort(reverse=True)
    i = 0
    while b*s>l2[0]*a:
        s -= l[i]
        i += 1
    return i

l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
print(f(l1,l2))
