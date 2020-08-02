#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1238/A
# 太简单?很无聊?

def f(l):
    x,y = l
    return x-y>1

t  = int(input())
for _ in range(t):
    l   = list(map(int,input().split()))
    print('YES' if f(l) else 'NO')

