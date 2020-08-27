#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1085/B
# min x st. (x div k)⋅(x mod k)=n

def f(l):
    n,k=l
    r = k-1
    while n%r>0:
        r -= 1
    d = n//r
    return d*k+r

l = list(map(int,input().split()))
print(f(l))
