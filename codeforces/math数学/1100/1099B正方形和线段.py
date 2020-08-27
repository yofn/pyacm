#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1099/B
# 画n个正方形,需要用尺子画几个边 (平行的不用尺子)
# min(a+b) st. a*b>=n
# https://codeforces.com/blog/entry/64331
# It's easy to see that the answer is not optimal if |a−b|≥2

import math

def f(n):
    s  = int(math.sqrt(n))
    if s*s>=n:
        return s<<1
    if s*(s+1)>=n:
        return (s<<1)+1
    return (s<<1)+2

n = int(input())    #1e9
print(f(n))
