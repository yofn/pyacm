#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/797/A

def f(l):
    n,k = l #1e5,20; ..not big!
    fl  = []
    while True:
        if n==1:
            return [-1]
        if k==1:
            return fl + [n]
        f = 2
        while n%f>0:
            f += 1
        fl.append(f)
        n  = n//f
        k -= 1

l = list(map(int,input().split()))
print(*f(l))
