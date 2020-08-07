#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/515/A
# 错误1: 没考虑负数

def f(l):
    a,b,s = l
    a = a if a>=0 else -a
    b = b if b>=0 else -b
    return s-a-b>=0 and (s-a-b)%2==0

l = list(map(int,input().split()))
print('YES' if f(l) else 'NO')
