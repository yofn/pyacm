#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/2048/A
# 错误:没考虑合并之后的再合并
# 注意:i<n的条件必须放在前面!

def f(l,n):
    l.sort(reverse=True)
    i = 0
    while i<n and l[i]>2048:
        i += 1
    r = 2048
    while i<n and r>0:
        r -= l[i]
        i += 1
    return r==0

t = int(input())
for _ in range(t):
    n = int(input())    #100
    l = list(map(int,input().split()))
    print('YES' if f(l,n) else 'NO')
