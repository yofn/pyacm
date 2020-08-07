#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/622/A

import math

def f(n):
    m = int(math.sqrt(n<<1))
    b = ((m+1)//2)*m if m%2==1 else (m//2)*(m+1)
    s = ((m-1)//2)*m if m%2==1 else (m//2)*(m-1)
    if n==b:
        return m
    if n>b:
        return n-b
    if n==s:
        return m-1
    if n>s:
        return n-s

n = int(input())
print(f(n))
