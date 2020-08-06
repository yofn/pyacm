#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1245/A
# 假设a<b, 看(k*b)%a能否覆盖所有余数..

def f(l):
    a,b = l
    if a>b:
        a,b=b,a
    bl  = [False] + [True]*(a-1)
    for i in range(1,a+1):
        bl[(i*b)%a] = False
    return sum(bl)>0

t = int(input())
for _ in range(t):
    l = list(map(int,input().split()))
    print('Infinite' if f(l) else 'Finite')
