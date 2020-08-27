#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/883/M
# 示意图很有误导性

def f(l1,l2):
    g  = lambda d: 2 if d==0 else 1+(d if d>0 else -d)
    d2 = g(l1[0]-l2[0])+g(l1[1]-l2[1])
    return d2<<1

l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
print(f(l1,l2))
