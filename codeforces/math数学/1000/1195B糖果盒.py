#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1195/B
# n = 动作数目; k = 剩下的糖果; 输出 = 吃了多少糖果 (唯一)

import math

def f(n,k):
    m = int(math.sqrt((n+k+1)<<1))
    return n-m+1

n,k = list(map(int,input().split()))
print(f(n,k))
