#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1395/A
# 奇偶性, 回文最多一个奇数

def f(l):
    fixed = 0 in l[:3]  #can odd/even be flipped?
    return sum([i%2 for i in l])<2 if fixed else sum([i%2 for i in l])!=2

q   = int(input())
[print('Yes' if f(list(map(int,input().split()))) else 'No') for _ in range(q)]
