#!/usr/bin/python3

import math

def ff(m):
    s  = sum([min(math.pi*i/m,2) for i in range(1,m)])
    return (s+1)*(m<<1)

def f(n,m):
    l1 = lambda n,m : m*(n+1)*n if m>1 else 0
    l2 = lambda n,m : 2*m*m*(n-1)*n*(n+1)//3
    return l1(n,m) + l2(n,m) + ff(m)*n*(n+1)*(n*2+1)/6

n,m = map(int,input().split())
print(f(n,m))
