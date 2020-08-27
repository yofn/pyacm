#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/946/B
# 画个状态转换机出来可能比较有帮助..

def f(l):
    a,b = l
    while True:
        if 0 in [a,b]:
            return [a,b]
        if   a>=(b<<1):
            a = a%(b<<1)
        elif b>=(a<<1):
            b = b%(a<<1)
        else:
            return [a,b]

l = list(map(int,input().split()))
print(*f(l))
