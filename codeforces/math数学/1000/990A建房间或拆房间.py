#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/990/A

def f(ll):
    n,m,a,b = ll    #3e5
    c1 = (n%m)*b
    c2 = (m-n%m)*a
    return min(c1,c2)

l = list(map(int,input().split()))
print(f(l))
