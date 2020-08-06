#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/2048/A
# 错误:没考虑合并之后的再合并

def f(l):
    l.sort()
    i = 0
    while i<len(l):
        if l[i]==2048:
            return True
        if i+1<len(l) and l[i]==l[i+1]:
            l[i+1] += l[i]
        i += 1
    return False

t = int(input())
for _ in range(t):
    n = int(input())    #100
    l = list(map(int,input().split()))
    print('YES' if f(l) else 'NO')
