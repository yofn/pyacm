#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/258/A
# 101 => 11

def f(l):
    if '0' not in l:
        return ''.join(l[1:])
    i = l.index('0')
    return ''.join(l[:i]+l[i+1:])

l = list(input())
print(f(l))
