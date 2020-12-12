#!/usr/bin/env python3
#ccpc20wh
#https://codeforces.com/gym/102798/problem/D

import math

def f(c):
    i  = 0
    cc = math.floor(math.sqrt(c))
    while i<=1e6 and i<cc:
        i += 1
        if c%i>0:
            continue
        j  = c//i
        if i>1 and j%i==0:
            return True     #c=i*j(which divides i), i>1
        jj = math.floor(math.sqrt(j))
        if jj>1 and j == jj*jj:
            return True     #c=i*jj*jj, jj>1
    return False
    
n = int(input())
for i in range(n):
    c = int(input())        #1e18
    print('yes' if f(c) else 'no')
