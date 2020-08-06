#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1215/A
# make k1<k2

def f(l):
    a1,a2,k1,k2,n = l
    if k1>k2:
        k1,k2,a1,a2=k2,k1,a2,a1
    o1 = min(n//k1,a1)
    o2 = (n-o1*k1)//k2
    mx = o1+o2
    mi = max(0,n-k1*a1-k2*a2+a1+a2)
    return [mi,mx]

l = [int(input()) for _ in range(5)]
print(*f(l))
