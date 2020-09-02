#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/1076/B
#质数筛? https://oi-wiki.org/math/prime/

import math

def f(n):
    if n%2==0:
        return n//2
    s    = int(math.sqrt(n))
    mf   = n
    for i in range(3,s+1,2):
        if n%i==0:
            mf =i
            break
    return 1+(n-mf)//2

n = int(input())    #1e10
print(f(n))
