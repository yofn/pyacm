#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/591/A

def f(ll):
    l,p,q=ll
    return l*p/(p+q) 

l   = [int(input()) for _ in range(3)]
print(f(l))

