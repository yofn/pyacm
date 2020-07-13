#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/589/B

from math import sqrt,ceil
n   = int(input())
k   = int(ceil(sqrt(n)))
print(4*k if n>k*k-k else 4*k-2)
