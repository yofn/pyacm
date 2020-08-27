#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1033/B
# 剪布后的L形面积是否为质数
# a**2-b**2=(a+b)(a-b)

import math

def f(l):
    a,b = l     #1e11
    if a-b>1:
        return False
    s = a+b
    r = int(math.sqrt(s))
    for i in range(3,r+2):
        if s%i==0:
            return False
    return True

q = int(input())
for _ in range(q):
    l = list(map(int,input().split()))
    print('YES' if f(l) else 'NO')
