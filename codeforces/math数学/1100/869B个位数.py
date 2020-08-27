#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/869/B
# NOTE: 主要是注意溢出问题

def f(l):
    a,b = l     #1e18, so can't directly multiplied!!
    if b==a:
        return 1
    if (b-a)>=5:
        return 0
    p   = 1
    for i in range(a+1,b+1):
        p = (p*(i%10))%10
    return p

l = list(map(int,input().split()))
print(f(l))
