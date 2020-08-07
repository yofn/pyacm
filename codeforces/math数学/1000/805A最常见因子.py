#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/805/A

def f(ll):
    l,r = ll
    return 2 if r>l else l

l = list(map(int,input().split()))
print(f(l))
