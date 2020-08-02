#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/980/A

def f(l):
    nl = sum([c=='-' for c in l])
    np = sum([c=='o' for c in l])
    if np==0:
        return True
    return nl%np==0

l   = list(input())
print('YES' if f(l) else 'NO')

