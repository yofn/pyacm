#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1326/B
# x[0] -> a[0] -> x[1] -> a[1] 这样的恢复次序

def f(b):
    m   = 0
    for i in range(len(b)):
        b[i] += m
        if b[i]>m:
            m=b[i]
    return b

n   = int(input())
l   = list(map(int,input().split()))
print(*f(l))

