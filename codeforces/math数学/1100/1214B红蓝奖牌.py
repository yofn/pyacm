#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1214/A
# 有点水,看多少种组合
# bmax = min(n,b)
# bmin = n-min(n,g)
# return bmax-bmin+1

def f(l):
    b,g,n = l
    return min(n,b)+min(n,g)-n+1

l = [int(input()) for _ in range(3)]
print(f(l))
