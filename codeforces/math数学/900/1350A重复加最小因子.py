#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1350/A
# 第二次肯定是偶数! 偶数后肯定是+2

def f(l):
    n,k = l
    i   = 2
    while n%i>0:
        i += 1
    return n + i + ((k-1)<<1)

t  = int(input())
for _ in range(t):
    l = list(map(int,input().split()))
    print(f(l))

