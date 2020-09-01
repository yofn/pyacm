#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/705/A
# dp?
# 不能选#v=1的环.
# 所有-1, 和为奇数 => 1赢
# 所有-1, 和为偶数 => 2赢


def f(l):
    n     = len(l)
    rl    = [0]*n
    rl[0] = l[0]%2+1
    for i in range(1,n):
        rl[i] = rl[i-1] if l[i]%2>0 else (3-rl[i-1])
    return rl

q = int(input())
l = list(map(int,input().split()))
[print(r) for r in f(l)]
