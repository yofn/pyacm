#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1263/A
# 直觉: min(max(l),sum(l)-max(l)) <--错误!

def f(l):
    c  = max(l)
    ab = sum(l)-c
    return ab if ab<=c else sum(l)//2

q = int(input())
for _ in range(q):
    l = list(map(int,input().split()))
    print(f(l))
