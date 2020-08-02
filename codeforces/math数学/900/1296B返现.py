#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1296/B
# 每次用10的倍数..10个10个买?
# //9?

def f(n):
    return n + (n-1)//9

t  = int(input())
for _ in range(t):
    n = int(input())
    print(f(n))

