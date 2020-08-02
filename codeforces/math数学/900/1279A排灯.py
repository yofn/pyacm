#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1279/A
# 类似三角形: 最大的<=另两个之和 (报错)<--推理有错
# +1 

def f(l):
    return (max(l)<<1) <= (sum(l)+1)

t  = int(input())
for _ in range(t):
    l   = list(map(int,input().split()))
    print('YES' if f(l) else 'NO')

