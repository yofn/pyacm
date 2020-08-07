#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/584/A
# 有n位,又要被t整除

def f(l):
    n,t = l
    m   = 10**n-1
    m  -= m%t
    return m if m>=10**(n-1) else -1

l = list(map(int,input().split()))
print(f(l))
